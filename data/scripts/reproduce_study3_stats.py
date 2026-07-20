"""
reproduce_study3_stats.py

Reproduces the Study 3 (52-week longitudinal) retention and
circular-behaviour statistics reported in Results Sec. 4.5-4.6, directly
from ../data/study3_52week_summary_master.csv, and verifies internal
consistency against ../data/study3_52week_longitudinal_master.csv.

Usage:
    python3 reproduce_study3_stats.py
"""

import pandas as pd

SUMMARY_PATH = "../data/study3_52week_summary_master.csv"
LONGITUDINAL_PATH = "../data/study3_52week_longitudinal_master.csv"


def main():
    s = pd.read_csv(SUMMARY_PATH)
    l = pd.read_csv(LONGITUDINAL_PATH)

    print("=" * 90)
    print("STUDY 3 (52-WEEK LONGITUDINAL, N=%d)" % len(s))
    print("=" * 90)

    print("\n--- Retention (not replaced by week 52) ---")
    overall_retention = 1 - s.replaced_by_week52.mean()
    print(f"  Overall:    {overall_retention:.1%}")
    for grp in ["High_E_LT", "Control_LT"]:
        g = s[s.group == grp]
        ret = 1 - g.replaced_by_week52.mean()
        print(f"  {grp:12s}: {ret:.1%}  (N={len(g)})")

    print("\n--- Circular behaviour prevalence ---")
    print(f"  Overall (pooled), week 24: {s.circular_behavior_week24.mean():.1%}")
    print(f"  Overall (pooled), week 52: {s.circular_behavior_week52.mean():.1%}")
    for grp in ["High_E_LT", "Control_LT"]:
        g = s[s.group == grp]
        print(f"  {grp:12s}, week 24: {g.circular_behavior_week24.mean():.1%}")
        print(f"  {grp:12s}, week 52: {g.circular_behavior_week52.mean():.1%}")

    print("\n--- Internal consistency check: summary vs. longitudinal file ---")
    w0 = l[l.week == 0][["participant_id", "E_score"]].rename(columns={"E_score": "E_w0"})
    merged0 = s.merge(w0, on="participant_id")
    max_diff_0 = (merged0.E0 - merged0.E_w0).abs().max()
    print(f"  Max |E0 (summary) - E_score week0 (longitudinal)| = {max_diff_0}")

    w52 = l[l.week == 52][["participant_id", "E_score"]].rename(columns={"E_score": "E_w52"})
    merged52 = s.merge(w52, on="participant_id")
    max_diff_52 = (merged52.E_week52 - merged52.E_w52).abs().max()
    print(f"  Max |E_week52 (summary) - E_score week52 (longitudinal)| = {max_diff_52}")
    print("  (Both should be 0.0 -- confirms summary file is a faithful")
    print("   aggregation of the weekly trajectory file)")

    print("\n--- IMPORTANT INTERPRETIVE NOTE ---")
    print("""
    Manuscript Results §4.5-4.6 report circular-behaviour prevalence of
    58% (week 24) and 61% (week 52). These figures correspond to the
    High_E_LT (treatment) condition specifically, NOT the pooled sample.
    See docs/DATA_LINEAGE.md §2.3 for the full reconciliation.
    """)


if __name__ == "__main__":
    main()
