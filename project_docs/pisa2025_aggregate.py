"""Aggregate PISA 2025 student data without exporting individual records."""

import argparse
import csv
from pathlib import Path

import numpy as np
import pyreadstat


COUNTRIES = {
    "CZE": "\u010cesko",
    "SVK": "Slovensko",
    "DEU": "N\u011bmecko",
    "AUT": "Rakousko",
    "POL": "Polsko",
    "EST": "Estonsko",
    "FIN": "Finsko",
    "SGP": "Singapur",
    "KOR": "Ji\u017en\u00ed Korea",
    "USA": "USA",
    "QCI": "B-S-J-Z (\u010c\u00edna)",
}
DOMAINS = {"SCIE": "P\u0159\u00edrodn\u00ed v\u011bdy", "READ": "\u010cten\u00ed", "MATH": "Matematika"}
SCHOOL_GROUPS = {
    "Z\u00e1kladn\u00ed \u0161kola": ["203001"],
    "V\u00edcelet\u00e9 gymn\u00e1zium / konzervato\u0159": ["203002", "203003", "203004", "203005"],
    "\u010cty\u0159let\u00e9 gymn\u00e1zium": ["203006"],
    "SO\u0160 s maturitou": ["203007"],
    "SOU bez maturity": ["203009"],
}
REPLICATES = 80
PLAUSIBLE_VALUES = 10


def accumulator():
    return {
        "n": 0,
        "numer": np.zeros((PLAUSIBLE_VALUES, REPLICATES + 1)),
        "denom": np.zeros((PLAUSIBLE_VALUES, REPLICATES + 1)),
    }


def add_chunk(target, weights, values):
    weight_valid = np.all(np.isfinite(weights), axis=1) & (weights[:, 0] > 0)
    valid = np.isfinite(values) & weight_valid[:, None]
    target["n"] += int(np.all(valid, axis=1).sum())
    usable_weights = np.where(weight_valid[:, None], weights, 0.0)
    target["numer"] += np.where(valid, values, 0.0).T @ usable_weights
    target["denom"] += valid.astype(float).T @ usable_weights


def result(target):
    if target["n"] == 0 or np.any(target["denom"] == 0):
        return None
    estimates = target["numer"] / target["denom"]
    main = estimates[:, 0]
    score = float(main.mean())
    # Fay BRR with rho=0.5; average sampling variance across all PVs.
    sampling = float((4 / REPLICATES) * np.square(estimates[:, 1:] - main[:, None]).sum(axis=1).mean())
    imputation = float((1 + 1 / PLAUSIBLE_VALUES) * main.var(ddof=1))
    return score, (sampling + imputation) ** 0.5, float(target["denom"][:, 0].mean())


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sav", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--chunk-size", type=int, default=50000)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    columns = ["CNT", "PROGN", "W_FSTUWT"]
    columns += [f"W_FSTURWT{i}" for i in range(1, REPLICATES + 1)]
    columns += [f"PV{i}{domain}" for domain in DOMAINS for i in range(1, PLAUSIBLE_VALUES + 1)]
    groups = {}
    program_labels = {}
    processed = 0

    chunks = pyreadstat.read_file_in_chunks(
        pyreadstat.read_sav,
        args.sav,
        chunksize=args.chunk_size,
        usecols=columns,
        output_format="dict",
    )
    for data, metadata in chunks:
        program_labels.update({str(k): v for k, v in metadata.variable_value_labels.get("PROGN", {}).items()})
        country = np.asarray(data["CNT"])
        program = np.asarray(data["PROGN"])
        weights = np.column_stack([np.asarray(data["W_FSTUWT"], dtype=float)] + [np.asarray(data[f"W_FSTURWT{i}"], dtype=float) for i in range(1, REPLICATES + 1)])
        values = {
            domain: np.column_stack([np.asarray(data[f"PV{i}{domain}"], dtype=float) for i in range(1, PLAUSIBLE_VALUES + 1)])
            for domain in DOMAINS
        }
        for code in np.unique(country):
            if code not in COUNTRIES:
                continue
            country_mask = country == code
            selections = [("country", code, country_mask)]
            if code == "CZE":
                selections += [("program", str(p), country_mask & (program == p)) for p in np.unique(program[country_mask]) if p is not None]
            for kind, key, mask in selections:
                if not mask.any():
                    continue
                for domain in DOMAINS:
                    target = groups.setdefault((kind, key, domain), accumulator())
                    add_chunk(target, weights[mask], values[domain][mask])
        processed += len(country)
        print(f"Processed {processed:,} records", flush=True)

    country_rows = []
    program_rows = []
    for (kind, code, domain), target in sorted(groups.items()):
        estimate = result(target)
        if estimate is None:
            continue
        score, se, weighted_n = estimate
        row = {
            "cyklus": 2025,
            "oblast": DOMAINS[domain],
            "skore": f"{score:.3f}",
            "se_skore": f"{se:.3f}",
            "n_zaku": target["n"],
            "vazena_populace": f"{weighted_n:.1f}",
        }
        if kind == "country":
            country_rows.append({"kod": code, "zeme": COUNTRIES[code], "typ": "Region" if code == "QCI" else "Zeme", **row})
        elif target["n"] >= 30:
            program_rows.append({"kod_programu": code, "popis_programu": program_labels.get(code, ""), **row})

    school_rows = []
    for school_type, codes in SCHOOL_GROUPS.items():
        for domain in DOMAINS:
            combined = accumulator()
            for code in codes:
                source = groups.get(("program", code, domain))
                if source is not None:
                    combined["n"] += source["n"]
                    combined["numer"] += source["numer"]
                    combined["denom"] += source["denom"]
            estimate = result(combined)
            if estimate is None:
                continue
            score, se, weighted_n = estimate
            school_rows.append({
                "zeme": COUNTRIES["CZE"], "cyklus": 2025, "oblast": DOMAINS[domain],
                "druh_skoly": school_type, "kody_programu": "+".join(codes),
                "skore": f"{score:.3f}", "se_skore": f"{se:.3f}",
                "n_zaku": combined["n"], "vazena_populace": f"{weighted_n:.1f}",
            })

    write_csv(args.output_dir / "pisa2025-mikrodata-zeme.csv", country_rows, ["kod", "zeme", "typ", "cyklus", "oblast", "skore", "se_skore", "n_zaku", "vazena_populace"])
    write_csv(args.output_dir / "pisa2025-mikrodata-cr-programy.csv", program_rows, ["kod_programu", "popis_programu", "cyklus", "oblast", "skore", "se_skore", "n_zaku", "vazena_populace"])
    write_csv(args.output_dir / "pisa2025-mikrodata-cr-druhy-skol.csv", school_rows, ["zeme", "cyklus", "oblast", "druh_skoly", "kody_programu", "skore", "se_skore", "n_zaku", "vazena_populace"])
    print(f"Wrote {len(country_rows)} country/domain, {len(program_rows)} Czech program/domain, and {len(school_rows)} school-type/domain rows")


if __name__ == "__main__":
    main()
