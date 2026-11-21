# Pilot-Region Scoring Rubric and Review Checkpoints

**Task:** AQS-W01-SJ<br>
**Owner:** SJ — Project Lead / Technical Advisor<br>
**Version:** Draft v0.1<br>
**Date:** 2026-11-21<br>
**Review gate:** 2026-11-29<br>
**Status:** In Review

## Purpose

This rubric makes the pilot-region decision in Week 2 auditable. It defines the evidence required, how each dimension is scored, what counts as “unknown,” and which minimum conditions must be met before a region can be selected. It does **not** select a region and it does **not** convert source availability into evidence of groundwater stress.

The rubric must support a no-go or conditional decision. A region is not selected because it is convenient, because data exist somewhere, or because a single map looks convincing.

## Design rules

1. **Evidence over convenience.** Every score cites a source, date, and coverage.
2. **Unknown is not zero.** Use `U` when evidence is absent or inaccessible. A `U` is a gap to close, not a low score.
3. **Separate stress types.** Depletion (extraction exceeds recharge), scarcity (limited storage or recharge), drought vulnerability, and contamination are different claims. A “safe” extraction category does not mean water security.
4. **Separate source availability from stress evidence.** A downloadable dataset is not evidence that the aquifer is stressed.
5. **InSAR feasibility is necessary but not sufficient.** Good satellite coverage cannot compensate for missing ground records or an implausible deformation mechanism.
6. **Record rejected alternatives.** The decision log must show why other candidates lost.
7. **No region without a validation path.** If no partner, well record, or expert review path exists, the candidate cannot be selected for a validation claim.

## Dimensions and weights

| # | Dimension | Weight | What must be evidenced |
|---|---|---|---|
| 1 | Documented groundwater stress | 25% | Authoritative, spatially resolved evidence of depletion, scarcity, or drought stress; trend and mechanism; date and coverage |
| 2 | Reference-data coverage and quality | 20% | Monitoring-well density, record length, missingness, datum, aquifer screened, rainfall series, access terms |
| 3 | Sentinel-1 / InSAR feasibility | 20% | Usable SLC tracks, acquisition count and revisit, coherence potential, terrain/geometry, atmosphere, processing capacity |
| 4 | Hydrogeology and deformation plausibility | 15% | Aquifer type, compressible layers, confinement, groundwater mechanism, tectonic/other signals, existing subsidence evidence |
| 5 | Validation and partner access | 10% | University/agency partner, field or data access, expert review, data-sharing terms, realistic timeline |
| 6 | User and decision relevance | 10% | Stakeholder presence, decision the prototype could inform, delivery channel, demand hypotheses (not assumed demand) |

Weights sum to 100%. They are a starting proposal for the 2026-11-29 review and may be changed only with a recorded rationale.

## Scoring anchors

Score each dimension **0, 1, 2, 3, or U**. Use the anchors below; do not interpolate.

### 1. Documented groundwater stress (25%)

| Score | Anchor |
|---|---|
| 0 | No documented stress, or authoritative evidence contradicts the stress claim. |
| 1 | Anecdotal or single-source evidence (news, one report) without quantitative spatial/temporal coverage. |
| 2 | At least two independent authoritative sources; quantitative but partial coverage; trend or mechanism not fully resolved. |
| 3 | Multiple authoritative sources with recent, spatially resolved quantitative evidence; trend and mechanism consistent; local exceptions documented. |
| U | No accessible evidence, or sources cannot be verified. |

Acceptable evidence includes CGWB dynamic groundwater resource assessments, CGWB/UP Ground Water Department year books and decadal trend tables, official drought declarations, peer-reviewed studies, and verified state/agency records. A district aggregate alone is normally a 2, not a 3, because official categories are block-wise.

### 2. Reference-data coverage and quality (20%)

| Score | Anchor |
|---|---|
| 0 | No accessible monitoring wells or reference records for the candidate. |
| 1 | Fewer than 3 wells, or record length under 5 years, or high missingness, or undocumented datum/aquifer. |
| 2 | 3–9 wells with at least 10 years of record and moderate missingness; at least one rainfall series; datum mostly documented. |
| 3 | At least 10 wells with at least 10 years of record and low missingness; documented datum, screen depth, and aquifer; compatible rainfall series; clear access terms. |
| U | Access, coverage, or quality cannot be determined from available documentation. |

Well counts from a single CGWB monitoring event are not the total network. Verify the network, coordinates, screen depth, and missing-data reasons in Week 2.

### 3. Sentinel-1 / InSAR feasibility (20%)

| Score | Anchor |
|---|---|
| 0 | No usable SLC track, or access is blocked, or the area has severe geometric/coherence limitations. |
| 1 | Fewer than 12 acquisitions on one track, or severe seasonal decorrelation, or unresolved terrain/geometry problems. |
| 2 | At least 24 acquisitions on one track over at least 24 months; moderate coherence expected; manageable geometry; a processing path exists. |
| 3 | At least 36 acquisitions on two or more tracks; strong coherence potential; ascending and descending coverage; validated processing capacity and a test stack. |
| U | Archive availability or access has not been queried. |

The Week 1 screen is an **archive availability** result. A score of 2 or 3 still requires a coherence test on real scenes before the pilot decision.

### 4. Hydrogeology and deformation plausibility (15%)

| Score | Anchor |
|---|---|
| 0 | Deformation mechanism is implausible, or tectonics/other signals clearly dominate. |
| 1 | Hard-rock or low-compressibility aquifer; mechanism uncertain; no local subsidence evidence. |
| 2 | Alluvial aquifer with plausible compaction; some aquifer geometry or confinement information; mechanism plausible but untested. |
| 3 | Documented compressible aquifer system with confined layers; existing subsidence or compaction evidence; clear, testable mechanism. |
| U | Aquifer geometry or mechanism cannot be characterized from available sources. |

### 5. Validation and partner access (10%)

| Score | Anchor |
|---|---|
| 0 | No identified validation path and no realistic way to obtain one before the deadline. |
| 1 | A potential partner or dataset is named but not contacted; access uncertain. |
| 2 | A partner or data owner has been identified and initial access is plausible; validation scope still to be agreed. |
| 3 | Confirmed access to independent ground records or expert review, with a named contact and a realistic schedule. |
| U | Access has not been investigated. |

### 6. User and decision relevance (10%)

| Score | Anchor |
|---|---|
| 0 | No plausible user or decision; the output would not change any stated decision. |
| 1 | A user group is hypothesized but no decision, channel, or demand evidence is identified. |
| 2 | At least one concrete user decision and delivery channel are hypothesized; interviews are planned. |
| 3 | Multiple stakeholder types and a specific decision are documented; demand and trust are being tested; the product can represent uncertainty honestly. |
| U | User relevance has not been examined. |

## Minimum gates

A candidate can be **selected** only if all of the following hold:

- Dimension 1 score is at least **2**.
- Dimension 2 score is at least **2**.
- Dimension 3 score is at least **2**.
- Dimension 4 score is at least **1**.
- Dimensions 1–5 contain no `U`.
- At least one validation/partner contact or data-access route is identified.
- No red flag below applies.

A candidate may be **conditionally selected** if the missing condition has a named owner, a specific evidence item, and a due date before the relevant gate. A candidate is **not selected** if the gates fail; the decision log must say whether the failure is evidence, access, feasibility, or mechanism.

## Red flags and disqualifiers

- No accessible ground records and no realistic route to obtain them.
- No consistent Sentinel-1 track for the study period.
- Coherence or terrain problems that cannot be characterized before the deadline.
- Active conflict, safety risk, or access restriction that prevents validation.
- A candidate that is essentially entirely urban, so the groundwater-agriculture question cannot be tested.
- A data license or terms that prohibit the intended analysis or redistribution.
- A deformation signal that is clearly dominated by tectonics, construction, or another non-groundwater process.
- A claim that would require individual well-failure prediction without labels or validation.

## Decision procedure

1. MF and SM present evidence against each dimension, with links and coverage.
2. SJ records a score and a one-line justification for every dimension.
3. If any score is `U`, record the missing evidence and the owner; do not compute a final ranking as if it were zero.
4. Compute the weighted score only for candidates that pass the minimum gates:

   `weighted_score = 100 × Σ (weight_i × score_i / 3)`

   The result is on a 0–100 scale. Report it with the raw scores; the number does not replace the gate decision.
5. Record the decision: **Select**, **Conditional select**, **No-go**, or **Defer**.
6. Record rejected alternatives, the reason, and what evidence could change the decision.
7. For a conditional selection, record the condition, owner, evidence required, and due date.

### Tie-break order

If two candidates pass the gates and are within 5 weighted points:

1. Prefer the candidate with the stronger validation/partner access.
2. Then prefer the candidate with the stronger reference-data coverage and quality.
3. Then prefer the candidate with the more plausible deformation mechanism.
4. Do not tie-break on archive volume or convenience alone.

## Review checkpoints

| Date | Checkpoint | Required inputs | Accountable |
|---|---|---|---|
| 2026-11-23 | Rubric v0.1 shared with MF, SM, AC, AP | This document | SJ |
| 2026-11-24 | Candidate list confirmed; rubric applied to candidate descriptions | MF candidate draft | MF / SJ |
| 2026-11-25 | Archive query starts for the candidate boxes | Candidate boundaries/bboxes | SM |
| 2026-11-27 | Preliminary field lists to AC and AP | MF source inventory; SM screen draft | MF / SM |
| 2026-11-29 | Week 1 gate: rubric, candidate inventory, archive screen, contract/protocol, discovery guide reviewable | All Week 1 drafts | SJ |
| 2026-12-06 | Pilot decision recorded | Scored matrix, source evidence, partner notes | SJ |

Checkpoint notes must record who attended, what was decided, what remains unknown, and the next action with an owner and date.

## Decision-record template

```text
Decision ID: AQ-01-YYYY-MM-DD
Candidates considered: C1, C2, C3
Evidence versions: <links and dates>
Scores:
  C1: D1=x, D2=x, D3=x, D4=x, D5=x, D6=x, weighted=xx/100
  C2: ...
  C3: ...
Gate failures / unknowns: ...
Decision: Select / Conditional select / No-go / Defer
Selected candidate and boundary: ...
Conditions (if any): ...
Rejected alternatives and reasons: ...
What would change the decision: ...
Reviewer: SJ
Date: ...
```

## Sources used to design this rubric

- CGWB, *National Compilation on Dynamic Ground Water Resources of India, 2024*: <https://www.jalshakti-dowr.gov.in/static/uploads/2024/12/ef14a888b8fda9609ebb2d776720b52a.pdf>
- CGWB, *Dynamic Ground Water Resources & Ground Water Quality of Uttar Pradesh, 2024* (state summary): <https://cgwb.gov.in/cgwbpnm/download/1411>
- CGWB, *Ground Water Year Book, Uttar Pradesh, 2023-24*: <https://cgwb.gov.in/cgwbpnm/download/1730>
- CGWB ground water level monitoring: <https://cgwb.gov.in/en/ground-water-level-monitoring>
- IMD district rainfall statistics: <https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php>
- ASF Sentinel-1 search: <https://search.asf.alaska.edu/>
- Copernicus Data Space Ecosystem: <https://dataspace.copernicus.eu/>

These sources are starting points. A source link is not a score; the evidence must be read, dated, and recorded.
