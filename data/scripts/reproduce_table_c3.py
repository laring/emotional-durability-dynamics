"""
reproduce_table_c3.py

Reproduces Table C3 (Study 2 field experiment: heterogeneity in K and
gamma_c across demographic subgroups) directly from
../data/study2_field_master.csv.

Usage:
    python3 reproduce_table_c3.py
"""

import pandas as pd

DATA_PATH = "../data/study2_field_master.csv"

SUBGROUP_ORDER = [
    "18-30_HighFreq", "18-30_LowFreq",
    "31-50_HighFreq", "31-50_LowFreq",
    "51+_HighFreq", "51+_LowFreq",
]


def main():
    df = pd.read_csv(DATA_PATH)

    rows = []
    for sg in SUBGROUP_ORDER:
        # Use the treatment (non-control) row for each subgroup
        treatment = df[(df.subgroup == sg) & (df.condition != "control")].iloc[0]
        rows.append({
            "Subgroup": sg,
            "N": int(treatment["total_N"]),
            "K_mean": treatment["K_mean"],
            "K_sd": treatment["K_sd"],
            "gamma_c_mean": treatment["gamma_c_mean"],
            "gamma_c_sd": treatment["gamma_c_sd"],
            "OR": treatment["transition_OR"],
            "OR_CI": f"({treatment['OR_lower']}-{treatment['OR_upper']})",
        })

    table = pd.DataFrame(rows)
    print("=" * 100)
    print("TABLE C3 — Study 2 (Field, N=45,000): Heterogeneity in K and Critical")
    print("Regeneration Rate (gamma_c) Across Demographic Subgroups")
    print("=" * 100)
    print(table.to_string(index=False))

    print(f"\nTotal N across all subgroups: {table.N.sum():,}")
    print("(Should equal 45,000 to match the manuscript's stated Study 2 sample size)")


if __name__ == "__main__":
    main()
