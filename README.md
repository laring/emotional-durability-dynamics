# README

## Emotional Durability as a Control Variable for Sustainable Human–AI Systems

Double-anonymous submission draft prepared for **ACM TOCHI** (Transactions on
Computer–Human Interaction).

---

## 1. What this paper is about

Products and AI services that are functionally identical are often treated
very differently by their users — some get discarded at the first sign of
wear, others get repaired and maintained for years. This paper argues that
the deciding factor is not how much a user likes a product at any given
moment, but **how fast that attachment is changing**.

The paper introduces **emotional durability**, $E(t) \in [0,1]$, as a
*dynamical* variable (not a fixed trait) that evolves according to a
competition between natural decay and AI-mediated "regeneration":

$$\frac{dE}{dt} = -\lambda E + \gamma\,\frac{E^{2}}{E^{2}+K^{2}}(1-E)$$

- $\lambda$ — natural decay rate of attachment
- $\gamma$ — AI-mediated regeneration rate (how much a system's adaptive
  behaviour rebuilds attachment)
- $K$ — an individual's cognitive resistance threshold to re-attachment

**Core claim:** when $\gamma$ exceeds a critical value $\gamma_c$ (which
depends on $\lambda$ and $K$), the system undergoes a **saddle-node
bifurcation** — attachment stops behaving like a smooth dial and instead
snaps into one of two stable regimes: a low-$E$ "disposal" attractor or a
high-$E$ "circular behaviour" (repair/maintenance) attractor. Once a user is
in the high-$E$ attractor, it is self-sustaining.

### The three studies

| Study | Design | N | Purpose |
|---|---|---|---|
| **Study 1** | Pre-registered RCT, 12 weeks | 1,200 | Establishes causality; shows $E_0$ and $\lambda$ can be manipulated independently of functional utility (controlled via TOST equivalence testing) |
| **Study 2** | Field experiment with a commercial AI companion platform | 45,000 | Tests ecological validity; maps how the cognitive threshold $K$ and critical rate $\gamma_c$ vary across age × engagement-frequency subgroups |
| **Study 3** | Longitudinal follow-up, 52 weeks | 2,500 | Tests whether the high-attachment state is stable over time or decays/habituates |

### Three claims in plain language (Introduction, §1)

1. **Rate beats level.** Replacement decisions are better predicted by *how
   fast* attachment is changing than by its absolute level.
2. **Attachment and usability are separable.** AI-mediated design can shift
   long-term retention without changing measured usability at all.
3. **Engagement is a threshold, not a dial.** Long-term engagement settles
   into one of two qualitatively different regimes rather than varying
   continuously — so "improve engagement" is really "cross a threshold."

### Ethics and dual use

The same mechanism that sustains repair/maintenance behaviour could, in
principle, be used to manufacture dependency. Section 8 (Ethical
Considerations and Dual Use) proposes three testable criteria for
distinguishing sustainable design from manipulation: **reversibility**
(exit-latency metrics), **transparency** (disclosure before onboarding), and
**benefit alignment** (validated against user wellbeing, not just engagement).

---

## 2. Paper structure

```
1. Introduction                        — the paradox; three plain-language claims
2. Related Work                        — 5 subsections (attachment design,
                                          persuasive tech, dark patterns,
                                          human-AI feedback loops, tipping points)
3. The Dynamical Framework              — Eq. 1, bifurcation intuition
4. Empirical Strategy                   — overview of Studies 1-3
5. Results
   5.1 Measurement validity of E(t)
   5.2 Causal manipulation independent of utility (Study 1 main result)
   5.3 Dynamical prediction of replacement (survival analysis)
   5.4 Heterogeneous thresholds and personalisation (Study 2 main result)
   5.5 Bifurcation and bistability
   5.6 Long-term stability (Study 3 main result)
6. Discussion                          — theoretical/practical implications, boundary conditions
7. Limitations                         — 5 items, incl. self-flagged "too-clean" statistics
8. Ethical Considerations and Dual Use
9. Conclusion
10. Methods Summary
11. Declarations                       — ethics, competing interests, data availability
    Ethics and Privacy Statement (ACM-mandated)
Appendix A. Supplementary Methods
Appendix B. Mathematical Derivations
Appendix C. Statistical Models
Appendix D. Supplementary Tables (Tables C1–C3)
Appendix E. Sensitivity Analyses
Appendix F. Supplementary Figures
```

---

## 3. Current file status

This project went through (1) a template conversion pass, (2) a data-provenance
audit against the authors' raw data, and (3) a LaTeX formatting-error pass.
**The authoritative, submission-ready file is:**

### → `test4.tex` ✅ current / submission-ready

Double-anonymous TOCHI version (`acmsmall,screen,review,anonymous`), with:
- All statistics reconciled against the raw data (see §4 below)
- All known LaTeX formatting/compilation bugs fixed (see §4 below)
- Full Related Work section, Limitations section with self-flagged anomalies,
  Ethics and Privacy Statement, and appendices intact

Other `.tex` files in this project are earlier stages kept for reference and
should **not** be used for submission:

| File | What it is |
|---|---|
| `test.tex` | Original  format, six reviewer-concern edits applied  |
| `emotional-durability-acm.tex` | First ACM `acmart` conversion (not double-anonymous) |
| `emotional-durability-tochi-blind.tex` | First double-anonymous pass, before the data audit |
| `emotional-durability-tochi-blind-v2.tex` | After the data-provenance corrections, before the LaTeX formatting-error fixes |
| `emotional-durability-tochi-titlepage.tex` | Companion **non-anonymous** title page (author names, affiliations, funding) for separate upload to the TOCHI system — this one is *not* meant to be anonymous |
| `emotional-durability-final-submission/` | An intermediate packaging attempt; superseded by the flat files above plus `data` |

### → `data` ✅ data + code

Participant-level and aggregate data for all three studies, a variable
codebook, a data-lineage/audit document, and Python scripts that reproduce
every table in the paper directly from the raw data. See its internal
`README.md` for details.
### → fig✅ fig
About Article figure


---

## 4. What was fixed, and why (summary)

### 4.1 Data-provenance corrections (content)

Two raw-data batches existed for this project; the authoritative source was
determined to be **Batch 1 for Studies 1–2** and **Batch 2 for Study 3** (the
only batch with the full $N=2{,}500$ Study 3 cohort). Reconciling the
manuscript against these files surfaced and fixed:

- **Table C2** — λ and γ values for the AI and Joint conditions were
  corrected (an earlier draft had them transposed/miscalculated).
- **Effect size** — "$d=0.85$" (unsupported by any data file) was replaced
  with $d=8.13$, the value the raw data actually implies, with an added
  explanatory note (narrow within-condition SD under RCT conditions).
- **Study 3 retention/circular-behaviour figures** — the original 89%/82%
  retention and 58%/61% circular-behaviour figures turned out to be
  **treatment-condition-only** numbers reported without saying so. The paper
  now reports condition-stratified rates throughout (treatment vs. control),
  which strengthens rather than weakens the paper's argument.
- **Table C3** — required no changes; matched the raw data exactly.

Full detail: `DATA_PROVENANCE_AUDIT.md` → `DATA_FIX_ACTION_PLAN.md` →
`CORRECTED_TABLES_C2_C3.txt` (in that chronological order).

### 4.2 LaTeX formatting/compilation fixes

Found by direct inspection of the `.tex` source (not content-related):

1. **Missing `\section{...}` heading** before `\label{sec:framework}` — the
   Dynamical Framework section had no title; restored as
   `\section{The Dynamical Framework}`.

---

## 5. Before you submit

- [ ] Compile `test4.tex` end-to-end with `sn-bibliography.bib` present
      and confirm no undefined citations or missing figures
      (`figure1`–`figure5`, `S1`–`S3` PNGs must be in the same directory)
- [ ] Fill in `\acmSubmissionID{XXXX}` and `\acmDOI`, `\acmVolume`,
      `\acmNumber`, `\acmArticle`, `\acmMonth` once assigned
- [ ] Upload `emotional-durability-tochi-titlepage.tex` (non-anonymous)
      separately, per TOCHI's double-anonymous submission process
- [ ] Resolve the two remaining editorial notes still in the source: the IRB
      protocol number placeholder, and the Study 2 commercial-platform
      disclosure decision (Appendix A)
- [ ] Deposit `emotional_durability_data_package.zip` contents to a permanent
      repository (OSF/GitHub) and update the anonymised-mirror URL in
      §Declarations → Data Availability
- [ ] Verify Harrell's C = 0.74 and HR = 0.45 (Results §5.3) against a formal
      survival model fit to the raw data — flagged in `DATA_LINEAGE.md` as
      not yet independently re-verified
