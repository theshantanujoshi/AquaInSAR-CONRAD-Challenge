# AquaInSAR Weekly Task Breakdown

Actionable subtasks for every owner-specific deliverable in [the weekly plan](plan.md). Keep parent task IDs and weekly due dates intact. Subtasks inherit the parent deliverable's due date and start **Not Started**; do not mark progress until evidence exists and is reviewed. The separate CSV is formatted for import as a subtask checklist database.

## Week 1 — parent deadline 2026-11-29

### AQS-W01-SJ — Pilot-region scoring rubric and checkpoints (SJ)

- [ ] **AQS-W01-SJ-01:** List the evidence dimensions for candidate selection: groundwater-stress records, reference-data coverage, Sentinel-1 feasibility, local geology, and validation access.
- [ ] **AQS-W01-SJ-02:** Define how each dimension will be scored and what evidence is required; leave unsupported dimensions marked unknown.
- [ ] **AQS-W01-SJ-03:** Set the weekly review checkpoints and record who must provide inputs before each checkpoint.
- [ ] **AQS-W01-SJ-04:** Publish the dated rubric and source requirements for MF and SM to use.

### AQS-W01-MF — Candidate-region groundwater/reference-data inventory (MF)

- [ ] **AQS-W01-MF-01:** Choose at least three plausible Uttar Pradesh candidate areas for comparison and record their boundaries or location references.
- [ ] **AQS-W01-MF-02:** Locate authoritative groundwater-level, rainfall, aquifer/geology, and monitoring-well sources for each candidate.
- [ ] **AQS-W01-MF-03:** Record source links, spatial and temporal coverage, units, update dates, and access conditions for each dataset.
- [ ] **AQS-W01-MF-04:** Fill the candidate matrix with known gaps and questions; distinguish source availability from evidence of local groundwater stress.

### AQS-W01-SM — Sentinel-1 feasibility screen (SM)

- [ ] **AQS-W01-SM-01:** Query Sentinel-1 archive availability for each area supplied by MF and record the query method and date.
- [ ] **AQS-W01-SM-02:** List available scenes and acquisition dates, orbit direction, relative orbit, polarization, and look geometry where available.
- [ ] **AQS-W01-SM-03:** Assess likely time-series coverage and flag coherence, terrain, geometry, atmospheric, or access constraints.
- [ ] **AQS-W01-SM-04:** Compare feasibility across candidates and send MF and SJ a short evidence-linked screen.

### AQS-W01-AC — Data contract and exploratory comparison protocol (AC)

- [ ] **AQS-W01-AC-01:** Collect the planned fields and formats from MF's reference-data inventory and SM's Sentinel-1 screen.
- [ ] **AQS-W01-AC-02:** Define required fields, CRS, spatial and temporal resolution, timestamps, units, missing-value rules, provenance, quality flags, versioning, and uncertainty.
- [ ] **AQS-W01-AC-03:** Write the proposed spatial/temporal matching and exploratory comparison steps, including how coverage and missingness will be reported.
- [ ] **AQS-W01-AC-04:** Document the boundary between observed deformation, groundwater measurements, and any later interpretation; publish the versioned draft.

### AQS-W01-AP — User discovery guide and dashboard sketch (AP)

- [ ] **AQS-W01-AP-01:** Summarize the agreed project scope, candidate-region context, target user types, and decisions the prototype may support.
- [ ] **AQS-W01-AP-02:** Draft neutral interview questions about current groundwater information, decision timing, trust, and preferred delivery formats.
- [ ] **AQS-W01-AP-03:** Sketch the main dashboard flow, including a regional map, source/date information, data quality, uncertainty, and no-data states.
- [ ] **AQS-W01-AP-04:** Review the sketch for unsupported well-failure or operational-warning claims and share the dated guide and wireframe with SJ.

## Week 2 — parent deadline 2026-12-06

### AQS-W02-SJ — Evidence-based pilot decision and official checklist (SJ)

- [ ] **AQS-W02-SJ-01:** Compare candidate evidence against the W01 rubric with MF and SM; identify missing evidence separately from low scores.
- [ ] **AQS-W02-SJ-02:** Select the pilot region or record a no-go/conditional decision if the evidence is inadequate; document rejected alternatives and uncertainty.
- [ ] **AQS-W02-SJ-03:** Write the research question and scope for the selected region, including what the project will not claim.
- [ ] **AQS-W02-SJ-04:** Locate the official Conrad Challenge checklist and cutoff time/timezone; map required items to owners and save the source.

### AQS-W02-MF — Reference-data package for selected region (MF)

- [ ] **AQS-W02-MF-01:** Collect the available groundwater-level and rainfall records for the selected boundary and study period.
- [ ] **AQS-W02-MF-02:** Gather local geology/aquifer descriptions and the locations or coverage of monitoring wells.
- [ ] **AQS-W02-MF-03:** Create a source manifest recording URLs/files, dates, units, coordinates/CRS, temporal coverage, permissions, and provenance.
- [ ] **AQS-W02-MF-04:** Check for missing periods, inconsistent units, spatial gaps, and access restrictions; package raw inputs unchanged with a data-quality note.

### AQS-W02-SM — Sentinel-1 scenes and repeatable processing setup (SM)

- [ ] **AQS-W02-SM-01:** Select representative Sentinel-1 scenes that cover the chosen region and record scene IDs, dates, orbit and look geometry.
- [ ] **AQS-W02-SM-02:** Acquire the selected scenes or document the exact access failure and recovery options.
- [ ] **AQS-W02-SM-03:** Record the processing software, version, environment, input organization, and initial configuration needed to repeat the setup.
- [ ] **AQS-W02-SM-04:** Run a small setup check and write down scene, storage, or compute blockers in the scene manifest.

### AQS-W02-AC — Final data contract and ingest quality checks (AC)

- [ ] **AQS-W02-AC-01:** Update the W01 contract using MF's reference-data and SM's scene manifests; freeze required fields and accepted formats.
- [ ] **AQS-W02-AC-02:** Implement an ingest step that loads the available manifests/reference records and preserves source identifiers and provenance.
- [ ] **AQS-W02-AC-03:** Add checks for schema, units, timestamps, CRS/spatial bounds, missing values, and duplicate or invalid records.
- [ ] **AQS-W02-AC-04:** Run the workflow on a representative sample, save its quality report, and document every detected issue without silently imputing data.

### AQS-W02-AP — Initial user interviews and refined user flow (AP)

- [ ] **AQS-W02-AP-01:** Recruit interviewees across relevant user types and conduct at least three interviews where access permits.
- [ ] **AQS-W02-AP-02:** Record interview notes with consent and privacy handled; separate direct statements from the team's interpretation.
- [ ] **AQS-W02-AP-03:** Summarize current information sources, decisions, trust concerns, and preferred timing/channel; log outreach gaps if the target is unmet.
- [ ] **AQS-W02-AP-04:** Revise the wireframe/user flow to reflect evidence and share the changes and interview log with SJ.

## Week 3 — parent deadline 2026-12-13

### AQS-W03-SJ — Feasibility gate and blocker actions (SJ)

- [ ] **AQS-W03-SJ-01:** Review MF's reference-data package, SM's scene/setup manifest, AC's ingest checks, and AP's discovery findings.
- [ ] **AQS-W03-SJ-02:** Decide what can be credibly demonstrated by Jan 7 and record technical/scientific limits for each candidate feature.
- [ ] **AQS-W03-SJ-03:** Create a blocker list with impact, owner, next action, and date; resolve cross-vertical dependencies where possible.
- [ ] **AQS-W03-SJ-04:** Publish gate notes with go/no-go or scope-reduction decisions and recovery actions.

### AQS-W03-MF — Clean reference records and hydrogeology note (MF)

- [ ] **AQS-W03-MF-01:** Keep the received source files unchanged and create versioned working copies for cleaning.
- [ ] **AQS-W03-MF-02:** Normalize units, coordinate references, timestamps, and station identifiers while recording each transformation.
- [ ] **AQS-W03-MF-03:** Align records to the selected boundary and summarize coverage, gaps, missingness, and seasonal context.
- [ ] **AQS-W03-MF-04:** Write the pilot hydrogeology note and a quality log; create a reference time series only where the records support it.

### AQS-W03-SM — First deformation result or documented feasibility report (SM)

- [ ] **AQS-W03-SM-01:** Choose a representative scene pair/subset from the W02 manifest and record why it is suitable for the first run.
- [ ] **AQS-W03-SM-02:** Run the preliminary interferometric workflow with saved configuration and input scene identifiers.
- [ ] **AQS-W03-SM-03:** Export a georeferenced preliminary deformation map or time series with coherence/quality information where feasible.
- [ ] **AQS-W03-SM-04:** Document processing steps, units, quality limitations, noise/confounders, and either the result or evidence-based no-go.

### AQS-W03-AC — Exploratory joined-data workflow (AC)

- [ ] **AQS-W03-AC-01:** Load the versioned MF reference series and SM deformation outputs through the shared data contract.
- [ ] **AQS-W03-AC-02:** Implement explicit spatial and temporal matching rules and preserve the source IDs used for each match.
- [ ] **AQS-W03-AC-03:** Report join coverage, unmatched records, missingness, and the resulting analysis sample before interpreting it.
- [ ] **AQS-W03-AC-04:** Create exploratory plots and a reproducible notebook/script; label associations as exploratory and make no unsupported risk prediction.

### AQS-W03-AP — Dashboard shell with provenance and uncertainty panel (AP)

- [ ] **AQS-W03-AP-01:** Set up the dashboard page structure and navigation from the approved W01 wireframe.
- [ ] **AQS-W03-AP-02:** Add the selected study-area context and a map placeholder or actual layer only when supported by the available data.
- [ ] **AQS-W03-AP-03:** Show source, observation date, units, data status, quality, uncertainty, and unavailable/illustrative states.
- [ ] **AQS-W03-AP-04:** Check the main user flow on the intended browser/device and share a runnable prototype or dated capture with a short review checklist.

## Week 4 — parent deadline 2026-12-20

### AQS-W04-SJ — Claim/evidence review and approved prototype scope (SJ)

- [ ] **AQS-W04-SJ-01:** Collect the current outputs from all four verticals and list every scientific/product claim planned for the demo.
- [ ] **AQS-W04-SJ-02:** Link each claim to its evidence, quality limits, and known confounders; mark unsupported claims for removal or qualification.
- [ ] **AQS-W04-SJ-03:** Review the W03 feasibility findings and approve a reduced scope if data or method quality is insufficient.
- [ ] **AQS-W04-SJ-04:** Record scope decisions and update the risk/decision log for the remaining weeks.

### AQS-W04-MF — Satellite-to-ground validation protocol (MF)

- [ ] **AQS-W04-MF-01:** Define which groundwater observations and deformation measurements can be compared and their compatible units/coverage.
- [ ] **AQS-W04-MF-02:** Specify spatial matching, temporal windows, reference baseline, inclusion/exclusion rules, and any aggregation.
- [ ] **AQS-W04-MF-03:** List confounders and cases where subsidence may not indicate groundwater stress, including alternative geological or human causes.
- [ ] **AQS-W04-MF-04:** Assess whether current data support meaningful validation; publish the protocol and coverage/gap report before interpreting results.

### AQS-W04-SM — Expanded processing and quality-controlled products (SM)

- [ ] **AQS-W04-SM-01:** Extend processing across the approved study area/time window using a recorded, repeatable configuration.
- [ ] **AQS-W04-SM-02:** Generate georeferenced deformation maps/time series where data quality permits and include units and dates.
- [ ] **AQS-W04-SM-03:** Create quality/coherence masks and QA figures; flag areas or epochs that should not be interpreted.
- [ ] **AQS-W04-SM-04:** Document atmospheric/noise limits, processing settings, and reproducibility notes in the output bundle.

### AQS-W04-AC — Simple baseline and model/no-model decision (AC)

- [ ] **AQS-W04-AC-01:** Use the W03 joined dataset and MF's validation protocol to define the simplest useful baseline comparison or indicator.
- [ ] **AQS-W04-AC-02:** Document feature definitions, input coverage, assumptions, and the exact evidence used to compute the baseline.
- [ ] **AQS-W04-AC-03:** Evaluate basic stability/sensitivity and uncertainty only to the extent the available observations support it.
- [ ] **AQS-W04-AC-04:** Decide and document whether any risk classification/model is justified; keep it exploratory or choose no-model when labels/sample size are inadequate.

### AQS-W04-AP — First research layer integrated in dashboard (AP)

- [ ] **AQS-W04-AP-01:** Select only quality-checked research layers approved by the owners and confirm their data-contract fields.
- [ ] **AQS-W04-AP-02:** Connect the layer(s) to the dashboard and show source, acquisition/observation date, units, quality, and uncertainty.
- [ ] **AQS-W04-AP-03:** Implement clear no-data, masked-area, and unavailable-data states; do not display illustrative content as measured results.
- [ ] **AQS-W04-AP-04:** Review the integrated view with SM, AC, and SJ; record source mapping and fix any misleading labels.

## Week 5 — parent deadline 2026-12-27

### AQS-W05-SJ — Evidence/integration review and closure actions (SJ)

- [ ] **AQS-W05-SJ-01:** Review each vertical's W04 output and the current end-to-end demo against the approved scope.
- [ ] **AQS-W05-SJ-02:** Build/update the claim-evidence matrix so every demo statement has evidence or is explicitly labeled as a hypothesis.
- [ ] **AQS-W05-SJ-03:** Identify remaining integration and research blockers and assign each an owner and due date.
- [ ] **AQS-W05-SJ-04:** Publish a closure-action log and confirm the team is preparing only claims the available evidence can support.

### AQS-W05-MF — Satellite-to-ground comparison report (MF)

- [ ] **AQS-W05-MF-01:** Apply the W04 protocol to the available groundwater, rainfall, and deformation observations.
- [ ] **AQS-W05-MF-02:** Report the number and coverage of matched observations, comparison units/windows, and any data exclusions.
- [ ] **AQS-W05-MF-03:** Present actual comparison results with uncertainty, confounders, counterexamples, and source-linked figures.
- [ ] **AQS-W05-MF-04:** If the reference data are insufficient, state what cannot be concluded and list the missing data needed for validation.

### AQS-W05-SM — Reproducible processing run and QA outputs (SM)

- [ ] **AQS-W05-SM-01:** Re-run the selected processing workflow from the documented inputs and configuration.
- [ ] **AQS-W05-SM-02:** Have another team member follow the run guide or review it for missing steps and dependencies.
- [ ] **AQS-W05-SM-03:** Produce final candidate maps/time series with metadata, quality indicators, and unreliable/masked areas identified.
- [ ] **AQS-W05-SM-04:** Save the run record, output manifest, QA figures, and known-failure notes in a versioned bundle.

### AQS-W05-AC — Risk-indicator/model evaluation and uncertainty report (AC)

- [ ] **AQS-W05-AC-01:** Define the evaluation design and available sample size/labels before calculating performance measures.
- [ ] **AQS-W05-AC-02:** Evaluate the baseline/indicator against the MF comparison data using only metrics supported by the labels and sample.
- [ ] **AQS-W05-AC-03:** Quantify uncertainty and false positives/negatives or warning lead time only if the data permit a valid estimate.
- [ ] **AQS-W05-AC-04:** Publish reproducible results and explain why forecasting is unsupported if the evidence does not justify it.

### AQS-W05-AP — User discovery report and alert-flow prototype (AP)

- [ ] **AQS-W05-AP-01:** Continue recruitment and reach at least five interviews across two or more stakeholder types where feasible.
- [ ] **AQS-W05-AP-02:** Summarize needs, pain points, trust requirements, and preferred channels; separate quotes from interpretation and record gaps.
- [ ] **AQS-W05-AP-03:** Build a location-specific SMS/WhatsApp alert-flow demo tied to a real or clearly labeled sample evidence record.
- [ ] **AQS-W05-AP-04:** Show uncertainty/source context in the alert, review it with users or experts where possible, and document feedback and venture implications.

## Week 6 — parent deadline 2027-01-03

### AQS-W06-SJ — End-to-end review and approved claims/narrative (SJ)

- [ ] **AQS-W06-SJ-01:** Walk through the complete demo using the current MF, SM, AC, and AP evidence packages.
- [ ] **AQS-W06-SJ-02:** Review every technical and product claim against the claim-evidence matrix; remove unsupported claims and preserve caveats.
- [ ] **AQS-W06-SJ-03:** Map official competition requirements to specific submission sections, owners, and evidence.
- [ ] **AQS-W06-SJ-04:** Approve the final demo outline and record remaining actions and decisions.

### AQS-W06-MF — Final hydrogeology and validation report (MF)

- [ ] **AQS-W06-MF-01:** Consolidate the selected region's aquifer/geology profile and the groundwater/rainfall source inventory.
- [ ] **AQS-W06-MF-02:** Finalize the comparison methodology, data coverage, results, confounders, and counterexamples.
- [ ] **AQS-W06-MF-03:** Separate direct measurements from interpretation and clearly state evidence gaps and validation limits.
- [ ] **AQS-W06-MF-04:** Review all cited sources and publish the final report with a complete data/source manifest.

### AQS-W06-SM — Reproducible pipeline and deformation products packaged (SM)

- [ ] **AQS-W06-SM-01:** Package the selected workflow, dependencies/software versions, input scene IDs, and processing configuration.
- [ ] **AQS-W06-SM-02:** Include the final maps/time series, CRS, units, dates, quality masks, and metadata in the package.
- [ ] **AQS-W06-SM-03:** Write run instructions and limitations covering coherence, atmosphere, noise, and interpretation.
- [ ] **AQS-W06-SM-04:** Check that the bundle contains the inputs/references and instructions needed to reproduce the demonstrated outputs; version and archive it.

### AQS-W06-AC — Frozen justified indicator and evaluation package (AC)

- [ ] **AQS-W06-AC-01:** Freeze the versioned analytical inputs, join rules, code/notebook, and indicator or baseline definition.
- [ ] **AQS-W06-AC-02:** Reproduce the final output layer and link it to its source data and version.
- [ ] **AQS-W06-AC-03:** Finalize evaluation, uncertainty, sample coverage, and supported error measures.
- [ ] **AQS-W06-AC-04:** State explicitly whether a predictive model was justified; document the limitations and freeze the report/output package.

### AQS-W06-AP — Integrated dashboard demo and venture assumptions (AP)

- [ ] **AQS-W06-AP-01:** Integrate the final approved MF, SM, and AC layers using the shared data fields and source references.
- [ ] **AQS-W06-AP-02:** Complete map interactions, layer legends, dates, units, uncertainty, data-quality, and unavailable-data states.
- [ ] **AQS-W06-AP-03:** Prepare a reliable walkthrough/demo path and capture backups in case the live build fails.
- [ ] **AQS-W06-AP-04:** Summarize customer-discovery evidence, pricing/deployment assumptions, and open validation needs as hypotheses rather than proven demand.

## Week 7 — parent deadline 2027-01-07

### AQS-W07-SJ — Final submission check and demo rehearsal (SJ)

- [ ] **AQS-W07-SJ-01:** Compare every required submission component against the verified official competition checklist.
- [ ] **AQS-W07-SJ-02:** Confirm the pitch and demo claims match the reviewed evidence and include scientific limitations.
- [ ] **AQS-W07-SJ-03:** Run a team rehearsal, assign speaking/demo transitions, and record final fixes.
- [ ] **AQS-W07-SJ-04:** Submit by the verified cutoff and save the receipt/confirmation with the final checklist.

### AQS-W07-MF — Scientific accuracy review and Q&A notes (MF)

- [ ] **AQS-W07-MF-01:** Review every groundwater, rainfall, aquifer, and validation statement in the final slides/demo for source accuracy.
- [ ] **AQS-W07-MF-02:** Check that units, periods, locations, uncertainty, confounders, and non-causal interpretations are stated correctly.
- [ ] **AQS-W07-MF-03:** Correct or flag unsupported statements and provide exact suggested wording to SJ.
- [ ] **AQS-W07-MF-04:** Prepare concise answers on hydrogeology, validation quality, and what evidence would change the conclusion.

### AQS-W07-SM — Archived workflow and final technical summary (SM)

- [ ] **AQS-W07-SM-01:** Freeze the demonstrated workflow version and record its commit/tag or archive identifier.
- [ ] **AQS-W07-SM-02:** Archive the scene manifest, processing settings, maps/time series, QA outputs, and run guide.
- [ ] **AQS-W07-SM-03:** Verify every presented deformation result is traceable to its input scenes and configuration.
- [ ] **AQS-W07-SM-04:** Write a final technical summary of method, output quality, limitations, and any no-go findings.

### AQS-W07-AC — Frozen analytics and model/indicator defense (AC)

- [ ] **AQS-W07-AC-01:** Freeze the analytical code, inputs, configuration, output layer, and version identifiers used in the submission.
- [ ] **AQS-W07-AC-02:** Trace each reported metric to its source data and reproducible calculation.
- [ ] **AQS-W07-AC-03:** Prepare a concise explanation of the baseline/indicator, uncertainty, data limits, and model/no-model decision.
- [ ] **AQS-W07-AC-04:** Remove unsupported accuracy, forecasting, false-positive/negative, or lead-time claims from final materials.

### AQS-W07-AP — Frozen dashboard demo and final product summary (AP)

- [ ] **AQS-W07-AP-01:** Freeze the dashboard build and verify the walkthrough starts cleanly and displays the intended evidence.
- [ ] **AQS-W07-AP-02:** Save backup captures/video and document the link/build version and any access requirements.
- [ ] **AQS-W07-AP-03:** Confirm each displayed layer/alert has source and uncertainty context and no unsupported operational claim.
- [ ] **AQS-W07-AP-04:** Deliver the final product, user-discovery, and venture summary with assumptions clearly distinguished from findings.


