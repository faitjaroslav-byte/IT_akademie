"""Contract checks for the published teaching extracts, without raw student data."""

import csv
from decimal import Decimal
from pathlib import Path
import unittest


DATA = Path(__file__).resolve().parents[1] / "docs/looker-studio/data"


def rows(filename):
    with (DATA / filename).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


class PisaTrendDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scores = rows("pisa-vysledky.csv")
        cls.shares = rows("pisa-rozlozeni.csv")
        cls.schools = rows("pisa-cesko-druhy-skol.csv")

    def test_grain_and_coverage(self):
        self.assertEqual((len(self.scores), len(self.shares), len(self.schools)), (141, 141, 60))
        for table, fields in (
            (self.scores, ("zeme", "cyklus", "oblast", "populace")),
            (self.shares, ("zeme", "cyklus", "oblast", "populace")),
            (self.schools, ("zeme", "cyklus", "oblast", "druh_skoly")),
        ):
            keys = [tuple(row[field] for field in fields) for row in table]
            self.assertEqual(len(keys), len(set(keys)))
            self.assertEqual({row["cyklus"] for row in table}, {"2015", "2018", "2022", "2025"})
            self.assertTrue(all(row["zdroj_url"].startswith("https://") for row in table))
            self.assertTrue(all(row["datum_cyklu"] == f'{row["cyklus"]}-01-01' for row in table))
        china = [row for row in self.scores if row["typ"] == "Region"]
        self.assertEqual({row["cyklus"] for row in china}, {"2018", "2025"})
        self.assertEqual(len(china), 6)
        self.assertEqual(sum(row["typ"] == "Reference" for row in self.scores), 3)
        self.assertEqual(sum(row["typ"] == "Reference_stala" for row in self.scores), 12)

    def test_shares_match_scores_and_sum_to_one(self):
        score_index = {(row["zeme"], row["cyklus"], row["oblast"]): row
                       for row in self.scores}
        for row in self.shares:
            key = row["zeme"], row["cyklus"], row["oblast"]
            self.assertEqual(row["skore"], score_index[key]["skore"])
            self.assertEqual(sum(Decimal(row[field]) for field in
                                 ("podil_pod_2", "podil_2_4", "podil_5_6")), Decimal("1"))

    def test_published_control_values(self):
        score_index = {(row["zeme"], row["cyklus"], row["oblast"]): row
                       for row in self.scores}
        czech_math = [score_index["Česko", str(year), "Matematika"]["skore"]
                      for year in (2015, 2018, 2022, 2025)]
        self.assertEqual(czech_math, ["492", "499", "487", "477"])
        czech_science = score_index["Česko", "2025", "Přírodní vědy"]
        self.assertEqual((czech_science["skore"], czech_science["oecd_skore"],
                          czech_science["zmena_2022_2025"]), ("490", "482", "-7"))
        self.assertEqual(score_index["Průměr OECD", "2025", "Přírodní vědy"]["skore"], "482")
        self.assertEqual(score_index["Průměr OECD (stálých 35)", "2025", "Přírodní vědy"]["skore"], "484")
        self.assertTrue(all(row["oecd_skore"] == row["zmena_2022_2025"] == ""
                            for row in self.scores if row["cyklus"] != "2025"))
        czech_shares = next(row for row in self.shares if row["zeme"] == "Česko"
                            and row["cyklus"] == "2025" and row["oblast"] == "Přírodní vědy")
        self.assertEqual(tuple(czech_shares[field] for field in
                               ("podil_pod_2", "podil_2_4", "podil_5_6")),
                         ("0.213", "0.717", "0.070"))
        school = next(row for row in self.schools if row["cyklus"] == "2025"
                      and row["oblast"] == "Přírodní vědy"
                      and row["druh_skoly"] == "Víceleté gymnázium")
        self.assertEqual(school["skore"], "595")

    def test_czech_school_2022_mathematics_matches_published_chart(self):
        expected = {
            "Základní škola": "457", "Víceleté gymnázium": "591",
            "Čtyřleté gymnázium": "568", "SOŠ s maturitou": "502",
            "SOU bez maturity": "408",
        }
        actual = {row["druh_skoly"]: row["skore"] for row in self.schools
                  if row["cyklus"] == "2022" and row["oblast"] == "Matematika"}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
