# Feasibility and Claim Ledger

**Status:** Planning and evidence audit as of 2026-11-26. This document records what is supported, what is not, and what must be tested. It is not a pilot selection, a validated method, or a competition result.

## Purpose

AquaInSAR's competition case depends on the Practicality criterion, which the 2026–27 Student Guide weights at **20%** and expands to include feasibility, realism, proof of concept, evidence base, and next steps. The repository currently contains no acquired dataset, processing run, dashboard, or validation. The honest position is therefore:

- the **problem context** is supported by official and published sources;
- the **general method** has published precedents in Uttar Pradesh;
- the **specific agricultural application** is unproven;
- the **product** is a plan, not a demonstrated capability.

This ledger keeps those statements separate so that a deadline does not turn an intention into a claim.

## Claim ledger

Levels follow [`docs/research-and-validation.md`](../research-and-validation.md): Planned, Observed, Associated, Validated, Predicted.

| # | Claim | Current level | Evidence | What would raise it | What would refute or limit it |
|---|---|---|---|---|---|
| C1 | Parts of Uttar Pradesh are groundwater-stressed at block scale. | **Verified official context** (not an AquaInSAR result) | CGWB 2024 summary: 59 of 836 blocks over-exploited, 46 critical, 165 semi-critical; stage of extraction 70.45%. | Block-level extraction time series and a documented candidate boundary. | A candidate block that is safe or improving; state totals that hide local variation. |
| C2 | CGWB monitors groundwater at 1,007 wells in UP four times a year (2022–23). | **Verified official context** | CGWB UP Year Book 2022–23. | Station-level extract for the candidate with coordinates, well type, screen depth, aquifer, datum, and gaps. | Sparse or absent stations in the candidate polygon; inconsistent datum; stale records. |
| C3 | InSAR has detected subsidence in Lucknow at rates up to about 36 mm/year. | **Published** | More et al. (2025); Awasthi et al. (2022); Raju et al. (2022). | Independent reproduction in the candidate area, with uncertainty and reference network. | Urban setting does not transfer; processing choices explain the rate; no coherent pixels in cropland. |
| C4 | Groundwater decline and deformation co-occur in published UP study areas. | **Published association** | Lucknow correlation reported by Awasthi et al. (2022); Varanasi coupling reported by Raju et al. (2024). | A pre-registered comparison in the candidate area controlling for season, rainfall, and geology. | Confounding by loading, irrigation, construction, or atmosphere; weak or absent correlation. |
| C5 | Sentinel-1 provides a usable historical archive over the candidate. | **Planned / unverified** | Mission and orbit facts verified; no scene query or coherence test performed. | Same-track SLC manifest and measured coherent-pixel coverage by season. | C-band decorrelation over crops; gaps; unsuitable track geometry. |
| C6 | NISAR can support a multi-year subsidence trend today. | **Not supported** | Validated L-band record starts 2026-10-21; reprocessing planned for 2027. | Several years of validated products, or a validated reprocessed archive. | The current record is weeks long; maturity mixing biases trends. |
| C7 | AquaInSAR can estimate vertical subsidence from InSAR. | **Planned** | Method described in project docs; no processing performed. | Processed displacement, geometry documentation, ascending/descending decomposition or an explicit LOS-only limitation. | Single-geometry LOS cannot separate vertical and horizontal motion. |
| C8 | AquaInSAR can associate deformation with groundwater conditions. | **Planned** | Workflow proposed; no matched dataset. | Documented spatial/temporal matching, sample size, missingness, uncertainty, and alternative-explanation checks. | Four measurements/year, date mismatch, well-versus-pixel scale mismatch. |
| C9 | AquaInSAR can classify risk or forecast outcomes. | **Planned / not justified** | No labels, no evaluation split, no baseline. | Representative labels, held-out evaluation, false-positive/false-negative reporting, calibration. | Small or biased sample; no independent outcome; prediction would be unsupported. |
| C10 | AquaInSAR has a working product or dashboard. | **Not supported** | No dashboard, pilot dataset, or user test in the repository. | A reproducible demo with provenance, quality masks, and a documented user decision. | A mockup alone is a design artifact, not a working product. |
| C11 | The competition entry is complete and paid. | **Open** | Deadline and fee verified; payment and portal status unknown. | Portal confirmation and receipt. | Missing payment or component by the cutoff. |

## Decision gates

| Gate | Question | Owner | Evidence required | Current status |
|---|---|---|---|---|
| G1 | Which category is registered, and can it change? | SJ | Portal record and Conrad answer. | **Open.** Repository says Aerospace & Aviation; Water Challenge is a plausible fit. |
| G2 | Which candidate area? | SJ, with MF and SM | At least three candidates scored on groundwater stress, station coverage, geology, SLC coverage, coherence, validation access. | **Open.** No candidate matrix for the research branch. |
| G3 | Are station records usable? | MF | Station extract with coordinates, well type, screen depth, aquifer, datum, dates, gaps, and terms. | **Open.** |
| G4 | Is C-band coherence adequate? | SM | Same-track SLC manifest and coherent-pixel fraction by season on real pairs. | **Open.** The central technical risk. |
| G5 | Is there independent displacement validation? | MF | GNSS, levelling, or other independent displacement reference; otherwise state the gap. | **Open.** Groundwater head is not displacement validation. |
| G6 | What can be shown by the deadline? | SJ | Frozen scope, reproducible demo, honest limitations, and a no-go/conditional path. | **Open.** About six weeks remain. |

## Feasibility risks

| Risk | Why it matters | Likelihood | Test | Stop or pivot condition |
|---|---|---|---|---|
| **Cropland coherence** | C-band scattering changes with crops, irrigation, harvest, and soil moisture. A multi-year agricultural series may have too few coherent pixels. | High | HyP3 pairs across pre-monsoon, monsoon, and post-monsoon; measure coherent-pixel fraction inside the polygon. | If usable coverage is negligible in most seasons, pivot to an urban/peri-urban benchmark or document a no-go for the agricultural claim. |
| **Spatial mismatch** | A well is a point at a screen interval; an InSAR pixel averages a resolution cell. | High | Buffer stations, report distance and pixel count, test sensitivity to radius. | If the candidate has too few stations inside a defensible buffer, do not claim well-level association. |
| **Temporal mismatch** | CGWB measures four times a year; satellite dates differ; seasonal extremes may be missed. | High | Match with an explicit window and lag; report sensitivity; avoid interpolating without uncertainty. | If matching leaves too few pairs, report a feasibility gap rather than a correlation. |
| **Vertical/horizontal ambiguity** | LOS displacement mixes vertical and horizontal motion. | Medium–high | Use ascending and descending tracks where available; otherwise label results LOS-only. | Do not call LOS a subsidence rate without stating the geometry assumption. |
| **Atmospheric and orbit artefacts** | Troposphere, ionosphere (L-band), orbit, DEM, and unwrapping errors can create trends. | Medium–high | Apply corrections, inspect residual ramps, compare overlapping pairs, report uncertainty. | If corrections are unavailable or unstable, treat the trend as provisional. |
| **Geology** | Compaction requires compressible material and effective-stress change; hard-rock terrain behaves differently. | Medium | Map the candidate to CGWB hydrogeological units; seek compressible-layer evidence. | Do not assert groundwater-induced compaction in terrain without a credible mechanism. |
| **Reference network** | The chosen stable reference changes absolute rates. | Medium | Document reference area, test sensitivity to alternative references. | A rate that flips sign with a reasonable reference change is not robust. |
| **Data maturity (NISAR)** | Validated L-band record is weeks long; pre-October 2026 reprocessing is planned for 2027. | Certain | Use Sentinel-1 for the historical trend; treat NISAR as complement/demo. | Do not present NISAR as a multi-year validated source. |
| **Access and licensing** | Station-level CGWB/India-WRIS access, redistribution, and third-party processing terms are unverified. | Medium | Confirm terms and export formats before uploading data to a service. | Do not send restricted data to HyP3 or publish it without permission. |
| **Scope versus deadline** | A full pipeline, dashboard, and validation may not fit the remaining time. | High | Freeze a minimum demonstrable scope; cut breadth, not evidence. | Prefer a small, reproducible, honest demo over a broad unsupported claim. |
| **Category narrative** | A space-method story may look misplaced in either category if the user decision is unclear. | Medium | Confirm category; write the user problem and decision first, method second. | Do not change category unilaterally or invent an aviation use. |

## Minimum honest demonstration

If the team wants a Practicality artifact rather than a concept-only entry, the smallest defensible sequence is:

1. **Pick one candidate polygon** with block-level stress context and at least a few CGWB stations. Record why the alternatives were rejected.
2. **Build the SLC manifest** for one track and pass. Record dates, polarization, incidence angle, and gaps.
3. **Process a small seasonal pair set** with HyP3 at 80 m. This is inexpensive: 10 credits per product against 8,000 free monthly credits.
4. **Measure coherence** inside the polygon. Report the coherent-pixel fraction and show an example map with a quality mask.
5. **Extract station records** and state the spatial/temporal matching rule. Plot the available series; do not force a correlation.
6. **Report a bounded result**: for example, "usable coherent pixels in these seasons; displacement estimates with this uncertainty; station coverage is insufficient for validation." A negative result is a valid feasibility finding.
7. **State the decision** the information could change and what the method cannot say.

This sequence produces **Observed** measurements and, at most, an **Associated** comparison. It does not produce a validated prediction. That is acceptable if labeled honestly.

## What can be claimed at submission

Safe now, with citations and scope:

- groundwater stress is officially assessed at block scale in UP;
- CGWB maintains a monitoring network with four annual measurements;
- published studies report subsidence in urban/riverfront UP;
- Sentinel-1 and NISAR have documented capabilities and limits;
- AquaInSAR has a defined hypothesis, workflow, and evidence standard.

Not safe without new artifacts:

- "AquaInSAR detects subsidence in [district]."
- "AquaInSAR validates groundwater depletion."
- "AquaInSAR predicts which wells will fail."
- "NISAR provides a multi-year trend."
- "The dashboard is operational" or "users need this" without evidence.

## Competition framing implications

- **Theme/Innovation (30%):** the novelty is not "using InSAR" alone. It must be the integration, the decision support, and the evidence discipline. Published Lucknow studies mean the method is not novel by itself.
- **Practicality (20%):** a small real processing run and a documented coherence result are stronger than a large mockup. A documented no-go is more credible than an unsupported capability claim.
- **Storytelling (20%):** the groundwater problem and the user decision should lead; the radar method should support them.
- **Marketing (20%) and Finances (10%):** the repository has no customer interviews or cost model yet. Do not present assumptions as findings.

## Open items

- Category and portal cutoff confirmation (G1).
- Candidate selection and station/aquifer evidence (G2, G3).
- Sentinel-1 track/coherence test (G4).
- Independent displacement reference or an explicit validation gap (G5).
- Frozen submission scope and owner sign-off (G6).
- Any user/customer evidence; none is recorded in the repository.

## Sources

This ledger synthesizes documents in this dossier. See [`source-register.md`](source-register.md) for the underlying sources, access dates, and limitations. Project evidence definitions are in [`docs/research-and-validation.md`](../research-and-validation.md); open decisions are in [`docs/open-questions.md`](../open-questions.md).
