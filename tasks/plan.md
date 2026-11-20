# AquaInSAR Weekly Deliverables Plan

## Schedule and scope

**Competition deadline:** January 7, 2027 (assumed from the next upcoming January 7; confirm the cutoff time and timezone against the competition instructions). **Working timezone:** Asia/Kolkata. The plan runs Monday, November 23, 2026 through Thursday, January 7, 2027.

This is a short prototype and submission schedule, not a claim that AquaInSAR can be scientifically validated across all regions or predict individual well failure by the deadline. Risk outputs remain exploratory unless ground-reference data support stronger claims. No progress is presumed: all tasks start **Not Started**. Evidence must be linked or stored with the task and reviewed before marking it complete.

The competition's exact submission checklist is not included in the project files. SJ verifies the official requirements in Week 1 and adds any required deliverables to the final sprint without removing scientific review.

## Task register

Each row is one independently accountable task. The week header supplies its deadline; every task begins Not Started. Evidence is the artifact named in the last column, to be linked in the tracker and reviewed by SJ or the named reviewer.

### Week 1 — Research foundation and feasibility (Nov 23–29)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W01-SJ | SJ — Project Lead / Technical Advisor | Define a scoring rubric for pilot-region selection and weekly review checkpoints. | None | Criteria cover documented groundwater stress, ground records, Sentinel-1 feasibility, geology, and validation access; no region is chosen without evidence. | Not Started | Dated rubric, checkpoint notes, and source links. |
| AQS-W01-MF | MF — Groundwater Research Scientist | Compare at least three plausible Uttar Pradesh candidate areas and inventory groundwater, rainfall, aquifer/geology, and monitoring-well records. | SJ shares the rubric by Nov 24. | Each area has authoritative source links, spatial/temporal coverage, relevant units, and known gaps; candidates are not represented as validated. | Not Started | Candidate matrix and source/data inventory. |
| AQS-W01-SM | SM — Geospatial Research Engineer | Screen Sentinel-1 archive availability and InSAR feasibility for MF's candidate areas. | MF shares candidate list by Nov 25. | For each area, record available acquisition dates, access path, likely temporal coverage, and material coherence/geometry limitations. | Not Started | Reproducible queries or source links and feasibility note. |
| AQS-W01-AC | AC — Machine Learning / Research Engineer | Draft the shared data contract and an exploratory satellite-to-ground comparison protocol. | Preliminary MF and SM field lists by Nov 27. | Contract defines CRS, space/time resolution, timestamps, units, missing values, provenance, quality flags, versioning, and uncertainty; protocol distinguishes observation from inference. | Not Started | Versioned contract and analysis protocol. |
| AQS-W01-AP | AP — Product & Venture Development Engineer | Prepare a user discovery guide and low-fidelity dashboard sketch. | SJ shares the project scope and candidate-region rubric. | Guide tests user decisions and trust needs; sketch shows evidence and uncertainty and avoids individual well-failure claims. | Not Started | Interview guide and dated wireframe. |

### Week 2 — Select the pilot and establish data access (Nov 30–Dec 6)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W02-SJ | SJ — Project Lead / Technical Advisor | Make and document the evidence-based pilot-region decision; lock the initial research question and submission requirements. | W01 candidate matrix from MF and feasibility note from SM. | Decision applies W01 rubric, records rejected alternatives and remaining uncertainty, and cites the official competition checklist and cutoff time. | Not Started | Signed decision log, hypothesis/scope statement, official checklist link. |
| AQS-W02-MF | MF — Groundwater Research Scientist | Assemble a first reference-data package for the selected region. | W02 region decision; W01 source inventory. | Include available groundwater and rainfall records plus geology/aquifer context; record provenance, units, coverage, missingness, and access gaps. | Not Started | Versioned dataset manifest, source files/links, and data-quality note. |
| AQS-W02-SM | SM — Geospatial Research Engineer | Acquire representative Sentinel-1 scenes for the selected region and establish a repeatable processing setup. | W02 region decision and W01 archive screen. | Record scene IDs, dates, orbit/look geometry, download/access method, software/environment, and any acquisition or processing blocker. | Not Started | Scene manifest and reproducible setup notes or documented access failure. |
| AQS-W02-AC | AC — Machine Learning / Research Engineer | Finalize the data contract and create a reproducible ingest/quality-check workflow for the available reference and satellite metadata. | W01 draft contract; W02 MF/SM manifests. | Workflow checks schema, units, timestamps, spatial bounds, missing values, and provenance; invalid or absent data are surfaced, not silently filled. | Not Started | Versioned schema and runnable ingest/check notebook or script with a sample report. |
| AQS-W02-AP | AP — Product & Venture Development Engineer | Conduct initial customer discovery and refine the dashboard's core user flow. | W01 guide; W02 pilot-area context. | Target at least three interviews across relevant user types; if access prevents this, submit outreach log and revised plan. Findings distinguish quotes from interpretation. | Not Started | Interview notes with consent/privacy handled, outreach log, updated wireframe. |

### Week 3 — First observations and baseline (Dec 7–13)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W03-SJ | SJ — Project Lead / Technical Advisor | Hold a feasibility gate and resolve cross-vertical blockers for the selected pilot. | W02 data and scene manifests; W02 discovery findings. | Record what can and cannot be demonstrated by Jan 7, decisions, owners, and dated recovery actions for blockers. | Not Started | Review minutes and updated decision/blocker log. |
| AQS-W03-MF | MF — Groundwater Research Scientist | Clean and align available groundwater/rainfall reference records; describe the pilot hydrogeology. | W02 reference-data package and selected boundary. | Preserve raw sources; document cleaning, units, timestamps, spatial coverage, gaps, and seasonal context; create an interpretable reference time series where data permit. | Not Started | Cleaned versioned data, hydrogeology note, and quality log. |
| AQS-W03-SM | SM — Geospatial Research Engineer | Process a representative interferometric pair or subset for the pilot and produce the first deformation observation or a documented feasibility result. | W02 Sentinel-1 scenes and processing setup. | Output is georeferenced and accompanied by scene IDs, method, quality/coherence information, limitations, and a clear distinction between measured displacement and groundwater interpretation. | Not Started | Reproducible run, preliminary map/time series, and processing log (or evidence-based no-go report). |
| AQS-W03-AC | AC — Machine Learning / Research Engineer | Build an exploratory comparison workflow joining available deformation and ground/environmental records. | W02 data contract; W03 MF and SM outputs. | Spatial/temporal joins are explicit and auditable; report coverage and missingness; no risk prediction is claimed from an unvalidated association. | Not Started | Reproducible notebook/script, join-quality report, and exploratory plots. |
| AQS-W03-AP | AP — Product & Venture Development Engineer | Build the dashboard shell with the selected study area, data provenance, and uncertainty/status panel. | W02 pilot decision; W01 wireframe; current data contract. | Interface labels unavailable or illustrative layers honestly and does not show invented measurements; core navigation works on the target device/browser. | Not Started | Runnable prototype link or capture and short review checklist. |

### Week 4 — Expand processing and evaluate methods (Dec 14–20)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W04-SJ | SJ — Project Lead / Technical Advisor | Review the hypothesis, method, and evidence; approve a defensible scope for the prototype. | W03 outputs from all verticals. | Document the evidence supporting each planned claim, unresolved confounders, and any claims to remove or qualify. | Not Started | Claim-evidence review and updated risk/decision log. |
| AQS-W04-MF | MF — Groundwater Research Scientist | Specify the satellite-to-ground comparison and validation limits for the available reference data. | W03 cleaned reference series and SM preliminary products. | Define comparison units, spatial/temporal matching, baseline, and known confounders; state whether available data can support a meaningful validation. | Not Started | Validation protocol and interim hydrogeology/coverage report. |
| AQS-W04-SM | SM — Geospatial Research Engineer | Expand processing over the selected area/time window and quantify product quality. | W03 processing run and SJ-approved scope. | Produce a georeferenced deformation map/time series where data allow; document coherence/quality masks, atmosphere/noise limitations, and reproducibility. | Not Started | Processing outputs, QA figures, and run configuration. |
| AQS-W04-AC | AC — Machine Learning / Research Engineer | Implement and evaluate a simple, defensible baseline stress indicator or comparison; decide whether modelling is justified. | W03 joined dataset; W04 MF validation protocol. | Baseline, assumptions, data coverage, and uncertainty are explicit; use no complex ML or forecasting without adequate labels and sample size. | Not Started | Versioned analysis, baseline results, and model/no-model rationale. |
| AQS-W04-AP | AP — Product & Venture Development Engineer | Connect the dashboard to the first quality-checked research layer(s). | W03 dashboard shell; W03–W04 SM/AC outputs and contract. | Show data date, units, source, quality/uncertainty, and missing-data state; do not imply operational alerts or validated risk. | Not Started | Integrated prototype link/capture and data-source mapping. |

### Week 5 — Validation and user evidence (Dec 21–27)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W05-SJ | SJ — Project Lead / Technical Advisor | Conduct a midpoint evidence and integration review; assign closure actions. | W04 method review and outputs. | Every claim in the draft demo has an evidence source or is labeled as a hypothesis; blockers have owners and due dates. | Not Started | Review checklist, claim-evidence matrix, action log. |
| AQS-W05-MF | MF — Groundwater Research Scientist | Produce the satellite-to-ground comparison report for available data. | W04 protocol; W04 SM and AC outputs. | Report actual comparisons, coverage, uncertainty, confounders, and counterexamples; if data are insufficient, state that clearly and identify what is missing. | Not Started | Interim validation report with source data references and figures. |
| AQS-W05-SM | SM — Geospatial Research Engineer | Re-run the selected processing workflow and prepare quality-controlled final candidate maps/time series. | W04 pipeline and SJ scope review. | Another team member can follow run instructions; outputs include metadata and quality indicators; failed or unreliable areas are masked/documented. | Not Started | Reproducible run record, output bundle, and QA checklist. |
| AQS-W05-AC | AC — Machine Learning / Research Engineer | Evaluate any proposed risk classification and quantify uncertainty and error modes. | W04 baseline and W05 MF comparison report. | Report evaluation design, sample size, uncertainty, and false positives/negatives only where labels support them; otherwise retain an exploratory indicator and explain why forecasting is unsupported. | Not Started | Model/indicator evaluation report and reproducible results. |
| AQS-W05-AP | AP — Product & Venture Development Engineer | Complete initial user discovery and prototype a location-specific alert flow. | W02 interviews; W04 integrated layers. | Target at least five total interviews across two or more stakeholder types; log recruitment gaps if unmet. Alert is labeled prototype and links its message to evidence/uncertainty. | Not Started | Findings report, interview/outreach log, and alert-flow demo. |

### Week 6 — Integrate and prepare the demonstration (Dec 28–Jan 3)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W06-SJ | SJ — Project Lead / Technical Advisor | Run an end-to-end review and approve the final scientific claims and competition narrative. | W05 evidence package from each vertical. | Demo flow is coherent; every technical claim has evidence and caveats; unsupported claims are removed; submission checklist is mapped to owners. | Not Started | Approved claim-evidence matrix, demo outline, and checklist. |
| AQS-W06-MF | MF — Groundwater Research Scientist | Finalize the hydrogeology and validation report for inclusion in the demo/submission. | W05 comparison report and any new verified reference data. | Clearly separate measured results, interpretation, confounders, and evidence gaps; link all datasets and sources. | Not Started | Reviewed report and data/source manifest. |
| AQS-W06-SM | SM — Geospatial Research Engineer | Package the reproducible processing workflow and selected deformation products. | W05 stable run and QA outputs. | Include inputs, processing configuration, outputs, CRS/units, quality masks, limitations, and instructions sufficient to reproduce the demonstrated result. | Not Started | Versioned pipeline package, maps/time series, and run guide. |
| AQS-W06-AC | AC — Machine Learning / Research Engineer | Freeze the justified baseline/risk indicator and its uncertainty/evaluation materials. | W05 evaluation and MF validation report. | Final output is reproducible, uses only supported claims, includes uncertainty and evaluation limits, and explicitly states if predictive modelling was not justified. | Not Started | Versioned analysis package, evaluation/uncertainty report, and output layer. |
| AQS-W06-AP | AP — Product & Venture Development Engineer | Integrate the selected research outputs in a stable dashboard demo and summarize venture assumptions. | W05 user findings; W06 MF/SM/AC packages. | Dashboard attributes every displayed layer, exposes uncertainty/limitations, and has a reliable demo path; pricing and deployment are labeled as hypotheses. | Not Started | Demo build/link, walkthrough, business-model assumptions sheet. |

### Week 7 — Submission and final rehearsal (Jan 4–7; deadline Jan 7)

| Task ID | Owner / vertical | Objective and deliverable | Dependencies | Acceptance criteria | Status | Evidence |
|---|---|---|---|---|---|---|
| AQS-W07-SJ | SJ — Project Lead / Technical Advisor | Coordinate final submission, verify completeness, and lead the final pitch/demo rehearsal. | W06 approved narrative and official competition checklist. | Required materials are checked against the official rules; claims match evidence; team can explain limitations; final submission receipt is saved if submitted. | Not Started | Final checklist, rehearsal notes, and submission receipt/confirmation. |
| AQS-W07-MF | MF — Groundwater Research Scientist | Complete final scientific accuracy review and prepare answers on hydrogeology and validation. | W06 final report and submission draft. | All groundwater, rainfall, and validation statements match cited evidence; uncertainty and non-causal interpretations are explicit. | Not Started | Final reviewed text/slide comments and Q&A notes. |
| AQS-W07-SM | SM — Geospatial Research Engineer | Freeze and archive the demonstrated Sentinel-1 workflow and map/time-series outputs. | W06 reproducible pipeline and final demo build. | Saved outputs are traceable to input scenes and settings; no last-minute unreviewed processing result is presented as validated. | Not Started | Tagged/archive bundle, manifest, and final technical summary. |
| AQS-W07-AC | AC — Machine Learning / Research Engineer | Freeze analytical outputs and prepare a concise defense of the indicator/model and its limits. | W06 evaluated analysis and final submission draft. | Reported metrics are reproducible and correctly scoped; unsupported forecast or accuracy claims are absent; uncertainty can be explained. | Not Started | Frozen analysis version, metric source, and Q&A notes. |
| AQS-W07-AP | AP — Product & Venture Development Engineer | Freeze the dashboard/alert demo and deliver the product, user evidence, and business summary. | W06 stable dashboard and interview findings. | Demo works from a clean start; displayed content is sourced and qualified; user findings and business assumptions are clearly distinguished. | Not Started | Final demo link/build, backup captures/video, discovery and venture summary. |

## Weekly integration gates

- **Nov 29:** Candidate-region evidence and data contract draft are reviewable.
- **Dec 6:** Pilot region and hypothesis are selected from evidence; actual data access is known.
- **Dec 13:** First satellite processing result or documented feasibility failure; reference data are aligned.
- **Dec 20:** Baseline and product integration reviewed; scope is reduced if evidence is weak.
- **Dec 27:** Ground comparison, error/uncertainty analysis, and user discovery findings are available.
- **Jan 3:** End-to-end demonstration and claims receive SJ's review.
- **Jan 7:** Competition-required materials are submitted by the verified cutoff; submission proof is retained.

## Open assumptions and risks

- SJ must verify the official competition deliverables and exact cutoff time/timezone in Week 1.
- Data access, useful Sentinel-1 coherence, and availability of temporally and spatially compatible groundwater observations are not yet verified.
- If ground data or labeled outcomes are insufficient, the team should present an exploratory regional indicator and evidence gap, not a validated prediction or individual well-failure warning.
- The schedule is compressed; the Dec 13 and Dec 20 gates are intended to expose feasibility problems early and keep the final demonstration honest.
