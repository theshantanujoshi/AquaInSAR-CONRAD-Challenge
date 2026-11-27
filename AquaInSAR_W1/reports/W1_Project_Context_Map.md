# W1 Project Context Map and Gap Register

**Package:** AquaInSAR_W1 — AC (Aishwary), Week 1
**Prepared:** 2026-11-24
**Status:** Working paper for the 2026-11-29 W1 review gate. Not an approved project decision.

## 1. Purpose

This map records what could be established from the repository before any W1 design work began. It separates evidence classes so that no assumption is silently promoted to a requirement. It accompanies the W1 data contract and exploratory comparison protocol; it is not a research result.

## 2. Evidence classification

| Class | Meaning |
|---|---|
| **CONFIRMED** | Directly stated in project material supplied by the team/organisers. |
| **OBSERVED** | Found in repository files (including build artifacts) without being a team decision. |
| **ASSUMED** | Temporary working assumption needed to make progress; must be confirmed. |
| **PROPOSED** | Recommendation made in this W1 package; not approved. |
| **UNKNOWN** | Not available in the environment; recorded as a gap, not as a negative finding. |

## 3. Context map

| # | Finding | Class | Basis / file | Consequence for W1 design |
|---|---|---|---|---|
| 1 | AquaInSAR is a Conrad Challenge concept by team *The Oopsies*, Aerospace & Aviation category. | CONFIRMED | `README.md`, `docs/project-charter.md` | Package is pre-competition research infrastructure, not a product. |
| 2 | Research question: whether Sentinel-1 deformation is useful evidence of groundwater stress in an agricultural area of Uttar Pradesh when checked against reference data. | CONFIRMED | `docs/project-charter.md`, `docs/research-and-validation.md` | Contract must carry deformation and reference observations as separate datasets with separate quality fields. |
| 3 | A negative or inconclusive result is an acceptable outcome. | CONFIRMED | `docs/project-charter.md` §Research question; `docs/research-and-validation.md` | Protocol must not be designed to force a positive association. |
| 4 | Deformation observation, groundwater measurement, association, validation and prediction are distinct claim levels. | CONFIRMED | `docs/research-and-validation.md`; ADR-0001 `docs/decisions/0001-evidence-first-claims.md` | Protocol forbids prediction/validation language in W1 and W3 exploratory outputs. |
| 5 | No pilot district/block has been selected. | CONFIRMED | `README.md`, `docs/open-questions.md` AQ-01, MF inventory | Geography, CRS and grid cannot be fixed in W1; marked PENDING in the contract. |
| 6 | No real dataset, scene manifest, deformation product, model or dashboard is present in the repository. | OBSERVED | Full recursive file listing; `git ls-files` | Schemas are prospective specifications; no validation against real data is possible in W1. |
| 7 | Four screening candidates exist (C1 western UP, C2 NCR fringe, C3 central UP, C4 Bundelkhand) with 22 inventoried sources, none scored or selected. | OBSERVED | `deliverables/week-01/AQS-W01-MF-candidate-matrix-source-inventory.md` | Dataset inventory entries are `ANTICIPATED_SOURCE_IDENTIFIED`; source links are not local data. |
| 8 | CGWB year book reports four seasonal well readings per year and 1,194 UP monitoring wells as on 2023-03-31; extraction stage is block-wise and is not a water-level trend. | OBSERVED | MF inventory [S1], [S3]; status notes | Temporal matching must handle ~4 observations/year; stage categories are screening context only. |
| 9 | Sentinel-1 C-band is the planned radar source; SLC is required for interferometry; crop decorrelation is a documented feasibility risk. | OBSERVED | `docs/independent-research.md` §§Scientific context, Agricultural coherence; MF inventory [S10] | Acquisition geometry, coherence and convention (LOS vs vertical) are mandatory metadata, not optional. |
| 10 | A six-dimension pilot rubric, weighted scoring, minimum gates and no-go rules were drafted by SJ; it is In Review, not accepted. | OBSERVED | `deliverables/week-01/AQS-W01-SJ-pilot-region-rubric.md` | W1 must not encode rubric outcomes as decisions. |
| 11 | W1 task set is five deliverables; all start Not Started except SJ and MF drafts In Review. | OBSERVED | `tasks/plan.md`, `tasks/todo.md` | AC's W1 output is a draft for review, not a completed/approved task. |
| 12 | A compiled `comparison` module and test bytecode exist, with a beginner-friendly CSV screening design (required columns, date/duplicate/missing/coordinate checks, four-level compatibility, plots). | OBSERVED | `src/aquainsar/__pycache__/comparison.cpython-311.pyc` (inspected as code objects, read-only); `src/aquainsar.egg-info/PKG-INFO` | At the 2026-11-24 snapshot, field names could be aligned for continuity; the source `.py` was absent, so it was not executable evidence. PR #4 later removed these tracked artifacts; see §6. |
| 13 | `PKG-INFO` describes additional W1 artifacts (comparison.py, notebook, synthetic data, reports, pyproject.toml) as implemented. | OBSERVED | `src/aquainsar.egg-info/PKG-INFO`, `SOURCES.txt` | Contradicts the checkout: those files are absent from `git ls-files` and disk. Treated as stale metadata, not capability. PR #4 later removed these tracked artifacts; see §6. |
| 14 | The referenced `Project_Details.pdf` is absent. | OBSERVED | `docs/project-charter.md` §78; `docs/open-questions.md` AQ-11; recursive listing | Competition/project facts in that PDF are unavailable; no constraints are inferred from it. |
| 15 | Exact competition cutoff/checklist and registered category remain to be verified by SJ. | CONFIRMED | `docs/open-questions.md` AQ-02; `docs/independent-research.md` §Competition | No competition-specific schema or deadline is hard-coded in the W1 package. |
| 16 | Canonical CRS, study boundary, grid/resolution, canonical units, study period, exchange formats and missing-reason vocabulary are undecided (AQ-05). | CONFIRMED | `docs/data-contract.md`, `docs/open-questions.md` | Contract v0.9.0 declares these PENDING and requires per-dataset explicit declarations. |
| 17 | Coordinates are stored as longitude/latitude decimal degrees in the MF inventory tables. | OBSERVED | MF inventory [S3] "coordinates in decimal degrees"; CRS not stated | Longitude/x then latitude/y order is PROPOSED; CRS value stays PENDING. |
| 18 | ISO 8601 UTC is the proposed canonical timestamp convention. | PROPOSED | `docs/data-contract.md` row "Timestamp convention" | Adopted as a provisional convention in v0.9.0; AC confirms in contract v1. |
| 19 | ASF HyP3 + MintPy is suggested as a low-friction processing route; NISAR is a future complement. | OBSERVED | `docs/independent-research.md` §§Processing options, Findings | Processing-tool choice is recorded as context, not fixed by W1. |
| 20 | Synthetic data may be used only for software testing and must never be reported as observations. | PROPOSED | W1 assignment §5; ADR-0001 | Unit-test fixtures are labelled `SYNTHETIC_TEST`; no synthetic science output is produced. |

## 4. Internal context summary

- **Investigation:** Satellite-measured surface deformation as one line of evidence about regional groundwater stress, always checked against independent groundwater/rainfall/geology context.
- **Expected research outputs (W3–W6):** joined and quality-checked datasets, exploratory comparisons, a justified baseline indicator or a documented model/no-model decision, uncertainty/evaluation material, and only then supported dashboard layers. W1 produces specifications and tools, not those outputs.
- **Geography:** not selected. Four candidates screened, none scored.
- **Reference data:** source links inventoried (CGWB, IMD, India-WRIS, UP GWD, GSI, NAQUIM, GRACE, etc.); no station-level files downloaded or verified in this repository.
- **Sentinel-1 information:** archive access routes and general mission/coherence notes only; no scene manifest, no acquisition count, no interferogram.
- **Formats present in repository:** Markdown, one CSV task register, compiled Python bytecode and package metadata. No scientific data format is in use locally.
- **Relevant spatial variables:** longitude, latitude, CRS, pixel/station identifiers, boundary geometry (deferred), grid/resolution (deferred).
- **Relevant temporal variables:** SAR acquisition date, well observation date, rainfall accumulation interval, seasonal grouping, reference date for displacement.
- **Expected relationships:** deformation may covary with groundwater level/rainfall under plausible hydrogeology; correlation is not causation and no well-failure forecast is supported without labels and validation.
- **Technical decisions already made (team-owned):** ADR-0001 claim separation; evidence-level ladder; rubric as draft decision procedure; task/ownership model.
- **Unresolved:** items 5, 6, 14–19 above plus all AQ-01…AQ-11 gates.

## 5. Gap register

| ID | Gap | Owner / gate | W1 handling |
|---|---|---|---|
| G-01 | Pilot region and versioned boundary geometry | SJ, AQ-01, 2026-12-06 | Geography fields PENDING; no bbox hard-coded. |
| G-02 | Project CRS, grid, resolution, common units | AC coordinates, AQ-05, 2026-12-06 | Per-dataset CRS mandatory; canonical values `null`/PENDING. |
| G-03 | Real groundwater/rainfall/well metadata (datum, screen, aquifer, missingness) | MF, AQ-03, 2026-12-06 | Schemas include fields but no values are asserted. |
| G-04 | Sentinel-1 scene manifest, track, coherence, geometry | SM, AQ-04, 2026-12-13 | InSAR schema records these as required metadata; no scenes claimed. |
| G-05 | Validation labels / event definitions | MF+AC, AQ-06/AQ-07, 2026-12-20 | Protocol explicitly defers validation and forecasting. |
| G-06 | Official competition checklist and cutoff | SJ, AQ-02, 2026-11-29 | Not encoded in W1 artifacts. |
| G-07 | `Project_Details.pdf` content | SJ, AQ-11, Week 1 | Absent; no facts inferred. |
| G-08 | Missing-value reason vocabulary and exchange formats | AC, AQ-05 | Provisional enum and CSV format proposed for review. |
| G-09 | Missing source `.py` for bytecode-only artifacts | Owner unknown | Bytecode inspected read-only for field-name continuity only; not executable evidence. PR #4 removed the tracked artifacts; gap retained as historical context only. |
| G-10 | User decisions, demand, alert behavior | AP, AQ-08/AQ-09 | Out of W1 scope. |

## 6. Risk notes for reviewers

1. Treating source availability (links) as data availability would be a category error; the contract marks every dataset `NO_LOCAL_DATA`.
2. Treating the stale `PKG-INFO` "implemented and tested" claim as current capability would be wrong; the corresponding files did not exist and PR #4 removed the tracked artifacts.
3. Any correlation computed on synthetic test fixtures would be meaningless; tests exercise validation logic only.
4. Fixing a CRS, grid or unit convention before AQ-05 would create false precision; v0.9.0 intentionally leaves those fields PENDING.
5. **Post-cleanup note (2026-11-27):** PR #4 removed the tracked `src/aquainsar.egg-info/` and `__pycache__/` artifacts from the repository and added `.gitignore` rules. Findings 12–13 above describe the 2026-11-24 snapshot; they are not a claim about the current tree. No AquaInSAR result depends on those artifacts.
