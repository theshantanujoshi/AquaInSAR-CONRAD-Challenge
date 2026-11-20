# Open Questions and Decision Register

This register separates unresolved choices from established project context. No answer should be inferred from the weekly plan. The named owner is accountable for bringing evidence or a decision to the stated gate; it does not mean the work is complete.

| ID | Question / open decision | Accountable owner(s) | Planned gate | Evidence needed |
|---|---|---|---|---|
| AQ-01 | Which Uttar Pradesh district/area provides the best combination of groundwater-stress evidence, reference records, Sentinel-1 feasibility, geology, and validation access? | SJ decides; MF and SM provide evidence | Dec 6 | Candidate matrix, source inventories, and documented trade-offs. |
| AQ-02 | What are the official competition submission components and the exact January 7, 2027 cutoff time/timezone? | SJ | Nov 29 | Official competition instructions/checklist. |
| AQ-03 | Which groundwater-level, rainfall, geology, and aquifer datasets are actually accessible for the chosen region and study period? | MF | Dec 6 | Dataset manifests, source links/files, coverage, units, access terms, and quality gaps. |
| AQ-04 | Are there Sentinel-1 scenes with adequate coverage and processing quality for a useful deformation analysis in the chosen region? | SM | Dec 13 | Scene manifest, processing feasibility run, and quality assessment. |
| AQ-05 | What CRS, study boundary, temporal conventions, spatial/temporal resolution, canonical units, exchange formats, missing-data codes, and version rules should contract v1 use? | AC coordinates; MF, SM, AP contribute; SJ reviews | Dec 6 | Actual source schemas, pipeline constraints, and dashboard integration needs. |
| AQ-06 | Do available ground measurements support a meaningful satellite-to-ground validation, including spatial/temporal matching and uncertainty? | MF | Dec 20 | Validation protocol and data-coverage assessment; later comparison results. |
| AQ-07 | Is there enough labeled, representative data to support classification or forecasting, and what evaluation design is defensible? | AC, with MF references | Dec 20 | Sample size, outcome definitions, evaluation split, metrics, and uncertainty analysis. |
| AQ-08 | Which user types need which decisions, how should uncertainty be communicated, and is there evidence of demand or willingness to pay? | AP | Jan 3 | Interview notes/findings, outreach gaps, and assumptions explicitly separated from findings. |
| AQ-09 | Which dashboard layers and alert behaviors can be supported by the evidence available by the deadline? | AP integrates; SJ reviews claims | Jan 3 | Integrated outputs, provenance and uncertainty fields, usability/demo review. |
| AQ-10 | What field interviews or external expert/partner access is feasible, and what can those interviews substantiate? | MF for hydrogeology/validation; AP for customer discovery; SJ for connections | Jan 3 | Interview/outreach log, methods, and clear separation of expert/user testimony from measurement validation. |
| AQ-11 | What does `Project_Details.pdf` specify, and does it add constraints or approved facts missing from the user-provided master context? | SJ | Week 1 | Reviewed PDF text and any applicable source references. |

## Current baseline

The pilot district, datasets, CRS, processing stack, model type, customer demand, pricing, operational alert behavior, and validation results are not established in the repository. The [weekly plan](../tasks/plan.md) assigns the first evidence-gathering tasks. Update this register when a decision is supported by reviewed evidence; preserve the evidence link and decision date.
