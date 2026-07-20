# Emotional Durability — Data & Code Package

This package contains the participant-level and aggregate data, codebook,
data-lineage documentation, and reproduction scripts supporting:

> *Emotional Durability as a Control Variable for Sustainable Human–AI Systems*
> (submitted to ACM TOCHI, double-anonymous review)

---

## Contents

```
data_package/
├── README.md                                  <- you are here
├── data/
│   ├── study1_rct_master.csv                  Study 1 (RCT, N=1,200), weekly, weeks 0-12
│   ├── study2_field_master.csv                Study 2 (Field, N=45,000), subgroup-aggregated
│   ├── study3_52week_summary_master.csv       Study 3 (Longitudinal, N=2,500), per-participant
│   ├── study3_52week_longitudinal_master.csv  Study 3, weekly (weeks 0-52), 132,500 rows
│   └── summary_statistics.csv                 Cross-check aggregate statistics
├── docs/
│   ├── CODEBOOK.md                            Variable definitions for every file
│   └── DATA_LINEAGE.md                        Processing pipeline + pre-submission audit trail
└── scripts/
    ├── reproduce_table_c2.py                  Reproduces Table C2 (Study 1 parameters)
    ├── reproduce_table_c3.py                  Reproduces Table C3 (Study 2 heterogeneity)
    └── reproduce_study3_stats.py              Reproduces Study 3 retention & circular-behaviour stats
```

## Quick Start

Requires Python 3 with `pandas` and `numpy` installed.

```bash
cd scripts
python3 reproduce_table_c2.py           # -> Table C2 (Results Sec. 4.2)
python3 reproduce_table_c3.py           # -> Table C3 (Results Sec. 4.3)
python3 reproduce_study3_stats.py       # -> Study 3 stats (Results Sec. 4.5-4.6)
```

Each script reads only from `../data/` and prints a table that matches the
corresponding table/statistic in the manuscript. No manual data entry or
external files are required.

## Data Access Notes

- **Study 1** (`study1_rct_master.csv`) and **Study 3**
  (`study3_52week_summary_master.csv`, `study3_52week_longitudinal_master.csv`)
  are participant-level, de-identified, and included in full.
- **Study 2** (`study2_field_master.csv`) is released at the subgroup-aggregate
  level (differential privacy ε = 0.1) per the data-sharing agreement with the
  commercial platform partner; individual-level Study 2 logs are not included.

## Important Note on Study 3 Reporting

Manuscript figures for Study 3 circular-behaviour prevalence (58% at week 24,
61% at week 52) refer to the **High_E_LT (treatment) condition only**, not the
pooled N=2,500 sample. The pooled rate is 43.3%/43.1%. This is documented and
reconciled in detail in `docs/DATA_LINEAGE.md` §2.3, and the manuscript text
has been revised to report condition-stratified statistics throughout.

## Corrections Made During Pre-Submission Audit

A full account of every value cross-checked against these files, including
what was corrected and why, is in `docs/DATA_LINEAGE.md`. In summary:

- Table C2: λ and γ values for the AI and Joint conditions were corrected to
  match this data (an earlier draft had these transposed/miscalculated).
- Effect size: Cohen's d for the Joint-vs-Control E₀ increase was corrected
  from an unsupported d=0.85 to d=8.13 (the value implied by this data), with
  an explanatory note on why this value is large but not erroneous.
- Study 3: retention and circular-behaviour statistics are now reported
  separately by condition (treatment vs. control) rather than as a single
  pooled figure, resolving an apparent discrepancy that reviewers would
  otherwise have flagged.
- Table C3 required no corrections; all values matched this data exactly.

## Contact

Reviewer/editor data-access requests for Study 2 individual-level logs should
be directed through the venue's confidential reviewer-author channel (see
manuscript Declarations §Data Availability).
