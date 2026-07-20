# Data Codebook
## Emotional Durability as a Control Variable for Sustainable Human–AI Systems

This codebook documents all variables in the deposited data package. Data are
organised by study. See `DATA_LINEAGE.md` for the processing pipeline that
produced each derived variable, and `../scripts/` for code that reproduces
every table and figure in the manuscript directly from these files.

---

## Study 1 — `study1_rct_master.csv`

**Design:** Pre-registered RCT, N = 1,200 (300 per condition), 12-week duration,
weekly measurement (weeks 0–12).

| Variable | Type | Description |
|---|---|---|
| `participant_id` | integer (1–1200) | Unique participant identifier |
| `condition` | categorical | `control` / `design` / `AI` / `joint` |
| `week` | integer (0–12) | Study week of measurement |
| `E` | continuous (0–1) | Emotional durability, measured via the 7-item Product Attachment Scale (PAS), 7-point Likert, rescaled to [0,1] |
| `lambda` | continuous (>0) | Individual natural decay rate (fixed per participant across weeks); estimated via exponential fit to each participant's E(t) trajectory |
| `gamma` | continuous (≥0) | Individual AI-mediated regeneration rate (fixed per participant); estimated via Hill-function fit to E(t) dynamics (Eq. 1 in manuscript) |
| `K` | continuous (0–1) | Individual cognitive resistance threshold; estimated jointly with λ, γ |
| `replacement_flag` | binary | 1 if participant reported replacing the product in that week |
| `SUS_score` | continuous (0–5 scale as coded here) | System Usability Scale score (functional utility, U); used for TOST equivalence testing across conditions |

**Derived statistics (see Table C2 / `tab:s2` in manuscript):**
- E₀ = mean of `E` at `week == 0`, grouped by `condition`
- λ, γ, K group means = mean of the per-participant fixed values, grouped by `condition`
- Replacement rate = proportion of participants with `replacement_flag == 1` in any week, grouped by `condition`

---

## Study 2 — `study2_field_master.csv`

**Design:** Field experiment with a commercial AI companion platform, N = 45,000,
aggregated to 6 demographic subgroups (3 age brackets × 2 engagement-frequency
levels) × 2 conditions (control / high-γ), under differential privacy (ε = 0.1).
Individual-level logs are not releasable per the platform data-sharing agreement;
this file contains the subgroup-level aggregates used to produce Table C3.

| Variable | Type | Description |
|---|---|---|
| `study` | string | Study identifier (`Study2_Field_DP`) |
| `subgroup` | categorical | One of: `18-30_HighFreq`, `18-30_LowFreq`, `31-50_HighFreq`, `31-50_LowFreq`, `51+_HighFreq`, `51+_LowFreq` |
| `condition` | categorical | `control` / high-γ (treatment) |
| `total_N` | integer | Number of users in this subgroup × condition cell |
| `E_baseline` | continuous | Mean baseline E for the cell |
| `E_baseline_sd` | continuous | SD of baseline E |
| `E_week12` | continuous | Mean E at week 12 |
| `E_week12_sd` | continuous | SD of E at week 12 |
| `repair_count` | integer | Number of repair/maintenance events recorded (objective log data) |
| `replacement_count` | integer | Number of replacement events recorded |
| `circular_behavior_count` | integer | Number of users meeting the circular-behaviour operational definition (see below) |
| `K_mean`, `K_sd` | continuous | Estimated cognitive threshold for the subgroup |
| `gamma_c_mean`, `gamma_c_sd` | continuous | Estimated critical regeneration rate for the subgroup |
| `transition_OR` | continuous | Odds ratio for transition to the D2 (circular-behaviour) attractor |
| `OR_lower`, `OR_upper` | continuous | 95% CI bounds for `transition_OR` |

**Derived statistics (see Table C3 / `tab:s3` in manuscript):** taken directly
from the treatment-condition (`condition != control`) row for each subgroup.

---

## Study 3 — `study3_52week_summary_master.csv` and `study3_52week_longitudinal_master.csv`

**Design:** 52-week longitudinal follow-up, N = 2,500 (1,481 in the High-E /
treatment condition, 1,019 in the control condition). Summary file: one row per
participant. Longitudinal file: one row per participant per week (weeks 0–52,
132,500 rows total).

### `study3_52week_summary_master.csv`

| Variable | Type | Description |
|---|---|---|
| `participant_id` | string | Unique participant identifier |
| `group` | categorical | `High_E_LT` (treatment) / `Control_LT` (control) |
| `E0` | continuous (0–1) | Baseline emotional durability (week 0) |
| `E_week24` | continuous | E at week 24 |
| `E_week52` | continuous | E at week 52 |
| `lambda_est` | continuous | Estimated individual decay rate |
| `K_est` | continuous | Estimated individual cognitive threshold |
| `circular_behavior_week24` | binary | 1 if participant met the circular-behaviour definition at week 24 |
| `circular_behavior_week52` | binary | 1 if participant met the circular-behaviour definition at week 52 |
| `replaced_by_week52` | binary | 1 if participant replaced the product/service before week 52 |

### `study3_52week_longitudinal_master.csv`

Same participant and group identifiers, with one row per `(participant_id, week)`
for `week` = 0…52, tracking `E_score` and `gamma_estimated` over time. Used to
verify that summary-file values (`E0`, `E_week24`, `E_week52`) are internally
consistent with the underlying weekly trajectories (confirmed: 0 discrepancy).

**Circular behaviour operational definition** (per manuscript Methods): active
investment of more than 30 minutes of time OR more than $50 to restore
functionality upon simulated or real degradation, distinct from passive
hoarding. Inter-rater reliability for coding: κ = 0.89.

**Derived statistics (see manuscript Results §4.5–4.6):**
- Retention rate = 1 − mean(`replaced_by_week52`), overall and by `group`
- Circular-behaviour prevalence = mean(`circular_behavior_week24`) and
  mean(`circular_behavior_week52`), overall and by `group`

**Important interpretive note:** manuscript figures of 58% (week 24) and 61%
(week 52) circular-behaviour prevalence refer specifically to the `High_E_LT`
condition, not the pooled sample. The pooled (both-conditions) rate is
43.3% (week 24) / 43.1% (week 52). See `DATA_LINEAGE.md` for full reconciliation.

---

## `summary_statistics.csv`

Study-level and condition-level aggregate statistics (participant counts,
replacement counts, replacement rates) used as an independent cross-check
against `study1_rct_master.csv` and `study2_field_master.csv`. All values in
this file were confirmed to match values computed directly from the
participant-level files (0% discrepancy).
