# AquaInSAR Research Dossier

**Status:** Supplementary research. This is not an official team deliverable, a pilot selection, an approved method, or evidence that AquaInSAR has produced or validated results.

**Research snapshot:** 2026-11-26. Recheck competition rules, product status, data access, and station-level records before relying on operational details.

## Purpose

This dossier compiles cited background for team decisions that are still open in [`docs/open-questions.md`](../open-questions.md): competition requirements, Uttar Pradesh groundwater context, published subsidence evidence, data access, processing options, and feasibility risks.

It expands the earlier [`docs/independent-research.md`](../independent-research.md) note. Where the two differ, use this dossier's source register and access date, then reconcile the difference explicitly.

## How to read the evidence labels

| Label | Meaning |
|---|---|
| **Verified official** | A primary official source was retrieved and checked on the access date. The claim is limited to what that source says. |
| **Published** | A peer-reviewed study reports the finding for its own location, period, and method. AquaInSAR has not reproduced it. |
| **Operational** | Product, quota, coverage, or tool documentation. These details can change without notice. |
| **Planned / associated** | An AquaInSAR intention or an interpretation that is not yet supported by AquaInSAR data. |
| **Open** | A decision or test still required. Absence of evidence is not evidence of absence. |

The repository's evidence levels remain authoritative for project claims: Planned, Observed, Associated, Validated, and Predicted. See [`docs/research-and-validation.md`](../research-and-validation.md).

## Documents

| Document | Question it addresses |
|---|---|
| [`conrad-2026-27.md`](conrad-2026-27.md) | What does the 2026–27 Innovation Stage require, when is it due, how is it judged, and which category fits? |
| [`uttar-pradesh-groundwater.md`](uttar-pradesh-groundwater.md) | What do the official CGWB state assessment and monitoring yearbook establish? |
| [`published-subsidence-evidence.md`](published-subsidence-evidence.md) | What have peer-reviewed studies reported in Uttar Pradesh, and what do those results not establish? |
| [`data-sources-and-tools.md`](data-sources-and-tools.md) | Which satellite, groundwater, rainfall, and processing options are practical, and what are their limits? |
| [`feasibility-and-claim-ledger.md`](feasibility-and-claim-ledger.md) | Which claims are supported, which are open, and what must be tested before committing? |
| [`source-register.md`](source-register.md) | What exactly was accessed, where, and with what limitations? |

## Findings at a glance

1. **The Innovation Stage deadline is January 7, 2027 at 11:59 PM Central Time** in the Student Guide, the Innovation Stage page, and the calendar. The general Challenge overview says January 8. The guide and the registered portal should govern; confirm the discrepancy with Conrad. The entry fee is **$499 USD per team**.
2. **The official Challenge includes a Water Challenge.** The repository currently describes AquaInSAR as Aerospace & Aviation. Both categories are plausible for a satellite-based groundwater-stress concept, but the choice is a team decision and should be confirmed with Conrad. This dossier does not change it.
3. **Uttar Pradesh has a block-level official groundwater assessment.** The 2024 CGWB summary reports 836 assessment units: 59 over-exploited (7.06%), 46 critical (5.5%), 165 semi-critical (19.74%), and 566 safe (67.7%). State totals are screening context, not a pilot selection or a subsidence measurement.
4. **The 2022–23 CGWB yearbook describes 1,007 monitoring wells measured four times a year.** Station-level coverage, well type, screen depth, aquifer, datum, and missingness still need to be checked for any candidate area.
5. **Published Uttar Pradesh subsidence evidence is strongest in urban Lucknow.** A 2025 study reports more than about 36 mm/year near Charbagh and Indira Nagar. Varanasi studies report about 2–8 mm/year along the Ganga riverfront. These are published, location-specific findings, not agricultural validation or proof of causation for a future AquaInSAR pilot.
6. **Sentinel-1 is the practical historical data source, but crop coherence is unverified.** The 1C/1D constellation restored a six-day repeat on June 24, 2026. C-band coherence over cropland must be measured on real pairs before promising a multi-year agricultural time series.
7. **NISAR validated L-band data start on October 21, 2026.** As of this snapshot, the validated record is about five weeks long. It is not a multi-year trend source yet. Reprocessing of pre-October 21 data is planned for 2027.
8. **ASF HyP3 makes a small feasibility test affordable.** HyP3 Basic includes 8,000 free credits per month; an InSAR product costs 10 credits at 80 m or 15 credits at 40 m, or 800/533 products per month. Credit budget is unlikely to be the first constraint; coherence, download, storage, and quality review are.
9. **OPERA DISP-S1 does not cover India.** Its documented coverage is North America. It is not a shortcut for Uttar Pradesh.
10. **AquaInSAR has no processing, pilot dataset, dashboard, or validation in the repository.** All technical claims remain planned or associated until artifacts and evidence exist.

## What this dossier does not do

- It does not select a pilot district, block, aquifer, category, method, or tool.
- It does not reproduce a published result, acquire Sentinel-1/NISAR data, or validate a groundwater–subsidence relationship.
- It does not replace the MF/SM/AC deliverables or SJ's decision gates.
- It does not establish that every cited dataset is licensed, analysis-ready, or available at the required station and date.

## Minimum evidence actions before committing

1. Confirm the registered category and the portal's exact cutoff with Conrad.
2. Use the SJ rubric to compare at least three candidate areas with block-level groundwater evidence.
3. Query same-track Sentinel-1 SLCs and measure coherent-pixel coverage by season.
4. Inspect station-level CGWB records for coordinates, well type, screen depth, aquifer, datum, frequency, and gaps.
5. Run a small HyP3 + MintPy feasibility stack before committing to a long archive.
6. Treat NISAR as a complement or demonstration source until enough validated repeats exist.
7. Keep the claim language at Observed/Associated, not Validated/Predicted, unless independent evaluation supports it.

## Maintenance

- Add new sources to [`source-register.md`](source-register.md) with an access date.
- Update a document only when the underlying source or evidence changes.
- Record disagreements between official pages instead of silently resolving them.
- Do not promote a literature finding to an AquaInSAR result.
