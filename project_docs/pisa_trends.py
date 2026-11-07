"""Build the course's three PISA CSVs from OECD and Czech School Inspectorate data."""

import argparse
import csv
from decimal import Decimal, ROUND_HALF_UP
import io
import math
from pathlib import Path
import re

import openpyxl
import pyreadstat


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "docs/looker-studio/data"
YEARS = (2015, 2018, 2022, 2025)
DOMAINS = {
    "Přírodní vědy": ("SCIE", "Table I.B1.2a.36", "Table I.B1.2a.33"),
    "Čtení": ("READ", "Table I.B1.2a.37", "Table I.B1.2a.34"),
    "Matematika": ("MATH", "Table I.B1.2a.38", "Table I.B1.2a.35"),
}
ENTITIES = (
    ("Austria", "Rakousko", "AUT", "Zeme"),
    ("Czechia", "Česko", "CZE", "Zeme"),
    ("Estonia", "Estonsko", "EST", "Zeme"),
    ("Finland", "Finsko", "FIN", "Zeme"),
    ("Germany", "Německo", "DEU", "Zeme"),
    ("Korea", "Jižní Korea", "KOR", "Zeme"),
    ("Poland", "Polsko", "POL", "Zeme"),
    ("Singapore", "Singapur", "SGP", "Zeme"),
    ("Slovak Republic", "Slovensko", "SVK", "Zeme"),
    ("United States*", "USA", "USA", "Zeme"),
    ("B-S-J-Z (China)", "B-S-J-Z (Čína)", "", "Region"),
    ("OECD average", "Průměr OECD", "", "Reference"),
    ("OECD average-35", "Průměr OECD (stálých 35)", "", "Reference_stala"),
)
SCHOOL_TYPES = (
    "Základní škola",
    "Víceleté gymnázium",
    "Čtyřleté gymnázium",
    "SOŠ s maturitou",
    "SOU bez maturity",
)
SCHOOL_PUBLISHED = {
    2015: {
        "Přírodní vědy": (468, 602, 578, 503, 413),
        "Čtení": (462, 589, 582, 506, 397),
        "Matematika": (469, 594, 574, 505, 418),
    },
    2018: {
        "Přírodní vědy": (468, 600, 575, 510, 423),
        "Čtení": (458, 594, 579, 508, 409),
        "Matematika": (470, 596, 582, 513, 428),
    },
    2025: {
        "Přírodní vědy": (459, 595, 582, 510, 413),
        "Čtení": (436, 567, 564, 492, 392),
        "Matematika": (448, 586, 570, 492, 404),
    },
}
SCHOOL_2025_FIGURES = {"Přírodní vědy": "2.1.14", "Čtení": "2.3.3", "Matematika": "2.4.4"}
OECD_2025_CHANGES = {"Přírodní vědy": -3, "Čtení": -14, "Matematika": -9}
OECD_URL = "https://stat.link/mrq53f"
CSI_2015_URL = "https://csi.gov.cz/Csicr/media/Prilohy/PDF_el._publikace/Mezin%C3%A1rodn%C3%AD%20%C5%A1et%C5%99en%C3%AD/NZ_PISA_2015.pdf"
CSI_2018_URL = "https://www.gymzl.cz/wcd/articles/2019_2020/2020_02_pisa/gv58_sk_zpr.pdf"
CSI_2022_URL = "https://csicr.cz/cz/Mezinarodni-setreni/PISA/Datove-soubory-a-dotazniky/PISA-2022"
CSI_2025_URL = "https://csi.gov.cz/CSICR/media/Prilohy/2024_p%C5%99%C3%ADlohy/Dokumenty/PISA-2025_final.pdf"
POPULATION = "Vsichni patnactileti v cilove populaci PISA"
SCHOOL_POPULATION = "Patnactileti zaci daneho druhu skoly"


def rounded(value, digits=0):
    quantum = Decimal("1").scaleb(-digits)
    return Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_UP)


def numeric(value):
    return isinstance(value, (float, int)) and math.isfinite(value)


def indexed_sheet(workbook, title):
    sheet = workbook[title]
    rows = list(sheet.values)
    years = {}
    distribution = "Proficiency level in" in str(rows[6][1])
    header = rows[6] if distribution else rows[7]
    for column, heading in enumerate(header):
        if isinstance(heading, str):
            if heading.startswith("Change") or "\n" in heading:
                break
            match = re.search(r"PISA (\d{4})", heading)
            if match and int(match.group(1)) in YEARS:
                years[int(match.group(1))] = column
    if set(years) != set(YEARS):
        raise ValueError(f"Missing cycle in {title}: {years}")
    entities = {row[0]: row for row in rows[9:] if row[0] in {e[0] for e in ENTITIES}}
    if len(entities) != len(ENTITIES):
        raise ValueError(f"Missing entity in {title}: {set(e[0] for e in ENTITIES) - set(entities)}")
    return years, entities


def country_rows(workbook):
    scores = []
    distributions = []
    change_columns = {"Přírodní vědy": 25, "Čtení": 33, "Matematika": 29}
    for area, (_, score_sheet, distribution_sheet) in DOMAINS.items():
        score_years, score_entities = indexed_sheet(workbook, score_sheet)
        share_years, share_entities = indexed_sheet(workbook, distribution_sheet)
        oecd_2025_score = int(rounded(score_entities["OECD average"][score_years[2025]]))
        for year in YEARS:
            for source_name, name, iso3, kind in ENTITIES:
                if source_name == "OECD average" and year != 2025:
                    continue
                score_row = score_entities[source_name]
                share_row = share_entities[source_name]
                score = score_row[score_years[year]]
                low = share_row[share_years[year]]
                high = share_row[share_years[year] + 2]
                if not numeric(score):
                    if numeric(low) or numeric(high):
                        raise ValueError(f"Shares without score: {source_name} {year} {area}")
                    continue
                if not numeric(low) or not numeric(high):
                    raise ValueError(f"Missing shares: {source_name} {year} {area}")
                common = dict(zeme=name, iso3=iso3, typ=kind, cyklus=year,
                              datum_cyklu=f"{year}-01-01", oblast=area, populace=POPULATION)
                score_int = int(rounded(score))
                change = score_row[change_columns[area]]
                if year != 2025 or kind == "Reference_stala" or kind == "Region":
                    change = ""
                elif kind == "Reference":
                    change = OECD_2025_CHANGES[area]
                elif numeric(change):
                    change = int(rounded(change))
                else:
                    raise ValueError(f"Missing published change: {source_name} {area}")
                scores.append({**common, "skore": score_int,
                               "oecd_skore": oecd_2025_score if year == 2025 and kind != "Reference_stala" else "",
                               "zmena_2022_2025": change,
                               "se_skore": rounded(score_row[score_years[year] + 1], 2),
                               "zdroj_url": OECD_URL})
                low_tenths = int(rounded(low, 1) * 10)
                high_tenths = int(rounded(high, 1) * 10)
                middle_tenths = 1000 - low_tenths - high_tenths
                if min(low_tenths, middle_tenths, high_tenths) < 0:
                    raise ValueError(f"Invalid shares: {source_name} {year} {area}")
                distributions.append({**common, "skore": score_int,
                                      "podil_pod_2": f"{low_tenths / 1000:.3f}",
                                      "podil_2_4": f"{middle_tenths / 1000:.3f}",
                                      "podil_5_6": f"{high_tenths / 1000:.3f}",
                                      "zdroj_url": OECD_URL})
    return scores, distributions


def school_2022_scores(sav_path):
    columns = ["Druh_skoly", "W_FSTUWT"]
    columns += [f"PV{i}{code}" for code, _, _ in DOMAINS.values() for i in range(1, 11)]
    data, meta = pyreadstat.read_sav(str(sav_path), usecols=columns, output_format="dict")
    expected = {1: "Základní škola", 2: "Gymnázium víceleté",
                3: "Gymnázium čtyřleté", 4: "SŠ s maturitou", 5: "SŠ bez maturity"}
    if any(meta.variable_value_labels["Druh_skoly"].get(float(k)) != v for k, v in expected.items()):
        raise ValueError("The 2022 school type labels differ from the documented grouping")
    results = {}
    for area, (code, _, _) in DOMAINS.items():
        scores = []
        for school_code in expected:
            means = []
            for i in range(1, 11):
                values = data[f"PV{i}{code}"]
                numer = denom = 0.0
                for group, weight, value in zip(data["Druh_skoly"], data["W_FSTUWT"], values):
                    if group == school_code and numeric(weight) and weight > 0 and numeric(value):
                        numer += weight * value
                        denom += weight
                if not denom:
                    raise ValueError(f"No students for {school_code} {area}")
                means.append(numer / denom)
            scores.append(int(rounded(sum(means) / len(means))))
        results[area] = tuple(scores)
    if results["Matematika"] != (457, 591, 568, 502, 408):
        raise ValueError("2022 computation does not match published ČŠI mathematics scores")
    return results


def school_rows(sav_path):
    values = {**SCHOOL_PUBLISHED, 2022: school_2022_scores(sav_path)}
    rows = []
    for year in YEARS:
        for area in DOMAINS:
            for index, school in enumerate(SCHOOL_TYPES):
                score = values[year][area][index]
                method = (f"Tabulka ČŠI 7.{dict(zip(DOMAINS, (3, 5, 4)))[area]}"
                          if year == 2015 else "Školní zpráva ČŠI, tabulka 1"
                          if year == 2018 else "Vážený výpočet z národního SAV ČŠI"
                          if year == 2022 else f"Graf ČŠI {SCHOOL_2025_FIGURES[area]}")
                source_url = {2015: CSI_2015_URL, 2018: CSI_2018_URL,
                              2022: CSI_2022_URL, 2025: CSI_2025_URL}[year]
                rows.append(dict(zeme="Česko", iso3="CZE", cyklus=year,
                                 datum_cyklu=f"{year}-01-01", oblast=area,
                                 populace=SCHOOL_POPULATION, druh_skoly=school,
                                 skore=score, zdroj_metoda=method, zdroj_url=source_url))
    return rows


def encoded_csv(rows, fields):
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oecd-xlsx", type=Path, required=True)
    parser.add_argument("--csi-2022-sav", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=DATA_DIR)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    workbook = openpyxl.load_workbook(args.oecd_xlsx, read_only=True, data_only=True)
    scores, distributions = country_rows(workbook)
    schools = school_rows(args.csi_2022_sav)
    files = {
        "pisa-vysledky.csv": encoded_csv(scores, ["zeme", "iso3", "typ", "cyklus",
                                                     "datum_cyklu", "oblast",
                                                     "populace", "skore", "oecd_skore", "zmena_2022_2025",
                                                     "se_skore", "zdroj_url"]),
        "pisa-rozlozeni.csv": encoded_csv(distributions, ["zeme", "iso3", "typ", "cyklus",
                                                           "datum_cyklu", "oblast", "populace", "skore", "podil_pod_2",
                                                           "podil_2_4", "podil_5_6", "zdroj_url"]),
        "pisa-cesko-druhy-skol.csv": encoded_csv(schools, ["zeme", "iso3", "cyklus",
                                                                "datum_cyklu", "oblast", "populace", "druh_skoly",
                                                                "skore", "zdroj_metoda", "zdroj_url"]),
    }
    for filename, contents in files.items():
        path = args.output_dir / filename
        if args.check:
            if path.read_text(encoding="utf-8") != contents:
                raise ValueError(f"Outdated or modified: {path}")
        else:
            path.write_text(contents, encoding="utf-8")
        print(f"{filename}: {contents.count(chr(10)) - 1} rows")


if __name__ == "__main__":
    main()
