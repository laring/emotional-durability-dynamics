"""
reproduce_table_c2.py

Reproduces Table C2 (Study 1 RCT: intervention effects on dynamical
parameters) directly from ../data/study1_rct_master.csv.

Usage:
    python3 reproduce_table_c2.py
"""

import pandas as pd
import numpy as np

DATA_PATH = "../data/study1_rct_master.csv"


def main():
    df = pd.read_csv(DATA_PATH)

    rows = []
    for cond in ["control", "design", "AI", "joint"]:
        cond_data = df[df.condition == cond]
        week0 = cond_data[cond_data.week == 0]

        E0_mean, E0_sd = week0["E"].mean(), week0["E"].std()
        lam = cond_data.groupby("participant_id")["lambda"].first()
        gam = cond_data.groupby("participant_id")["gamma"].first()
        K = cond_data.groupby("participant_id")["K"].first()

        rows.append({
            "Condition": cond,
            "N": cond_data.participant_id.nunique(),
            "E0_mean": round(E0_mean, 3),
            "E0_sd": round(E0_sd, 3),
            "lambda_mean": round(lam.mean(), 3),
            "lambda_sd": round(lam.std(), 3),
            "gamma_mean": round(gam.mean(), 3),
            "gamma_sd": round(gam.std(), 3),
            "K_mean": round(K.mean(), 3),
            "K_sd": round(K.std(), 3),
        })

    table = pd.DataFrame(rows)
    print("=" * 90)
    print("TABLE C2 — Study 1 (RCT): Intervention Effects on Dynamical Parameters")
    print("=" * 90)
    print(table.to_string(index=False))

    # Effect size: Joint vs Control
    c = df[(df.condition == "control") & (df.week == 0)]["E"]
    j = df[(df.condition == "joint") & (df.week == 0)]["E"]
    pooled_sd = np.sqrt((c.std() ** 2 + j.std() ** 2) / 2)
    d = (j.mean() - c.mean()) / pooled_sd
    pct_E0 = 100 * (j.mean() - c.mean()) / c.mean()

    lam_c = df[df.condition == "control"].groupby("participant_id")["lambda"].first().mean()
    lam_j = df[df.condition == "joint"].groupby("participant_id")["lambda"].first().mean()
    pct_lambda = 100 * (lam_c - lam_j) / lam_c

    print("\n" + "=" * 90)
    print("Effect size: Joint vs. Control")
    print("=" * 90)
    print(f"  E0: Control M={c.mean():.3f}, Joint M={j.mean():.3f}, "
          f"increase = {pct_E0:.1f}%, Cohen's d = {d:.2f}")
    print(f"  lambda: Control M={lam_c:.3f}, Joint M={lam_j:.3f}, "
          f"reduction = {pct_lambda:.1f}%")

    # Replacement rate by condition
    print("\n" + "=" * 90)
    print("Replacement rate (any replacement within 12 weeks), by condition")
    print("=" * 90)
    for cond in ["control", "design", "AI", "joint"]:
        cond_data = df[df.condition == cond]
        ever = cond_data.groupby("participant_id")["replacement_flag"].max()
        print(f"  {cond:8s}: {ever.mean():.1%}  (n={ever.sum()}/{len(ever)})")


if __name__ == "__main__":
    main()
