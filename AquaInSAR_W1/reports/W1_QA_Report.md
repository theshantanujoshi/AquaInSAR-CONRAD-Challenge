# W1 QA Report — AC deliverable package

**Date of execution:** 2026-11-24 (session 23:30–23:38 IST)
**Package:** `AquaInSAR_W1` · **Contract:** `AQS-DC` v0.9.0 · **Protocol:** `AQS-ECP` v1.0.0
**Executor:** AI-assisted work directed for AC; independent reviewer (SJ) review not yet recorded.

All commands were run from the repository root `C:\Users\Hp\Documents\AquaInSAR-CONRAD-Challenge` with Python 3.13.5. `PYTHONPATH` was set to `AquaInSAR_W1\src` (plus `AquaInSAR_W1\tests` for the CLI fixture commands). No network access and no real AquaInSAR data were used.

## 1. Executed checks and actual results

| # | Test performed | Command | Expected outcome | Actual outcome | Status | Remaining issue |
|---|---|---|---|---|---|---|
| 1 | JSON syntax | `python -m json.tool ...v0.9.0.json` | Valid JSON, exit 0 | `JSON_TOOL_EXIT=0` | **PASS** | None |
| 2 | Contract internal consistency | `python -m aquainsar_w1.contract_tools check-contract --contract ...` | `status: PASS`, no issues | `{"contract_id":"AQS-DC","contract_version":"0.9.0","status":"PASS","issues":[]}`, `EXITCODE=0` | **PASS** | Checks are internal, not an external JSON Schema |
| 3 | Contract structure tests | `python -m unittest discover -s AquaInSAR_W1\tests -v` | All tests pass | `Ran 24 tests ... OK`, `EXITCODE=0` | **PASS** | See §2 for earlier failures and fixes |
| 4 | Independent runner | `python -m pytest -q AquaInSAR_W1\tests` | All tests pass | `24 passed, 75 subtests passed in 0.11s`, `EXITCODE=0` | **PASS** | pytest is optional; stdlib unittest is canonical |
| 5 | Human/machine contract agreement | `test_docs_consistency.py` (IDs, field names, rule IDs, version, status) | Every JSON definition appears in the Markdown | All 9 doc tests pass | **PASS** | Agreement is checked for names/IDs/rules, not full prose equivalence |
| 6 | Protocol QA | `test_docs_consistency.py` section/no-results checks | Sections 4.1–4.7 present; explicit "not a results report" | Pass | **PASS** | Methodological review by SJ still pending |
| 7 | Python syntax compile | `python -m py_compile ...` | Exit 0 | `PY_COMPILE_EXIT=0` | **PASS** | Generated `__pycache__` directories were removed after testing; they regenerate on execution |
| 8 | CLI valid CSV | `validate-csv --dataset AQS-GW-CGWB-WELL --csv <SYNTHETIC_TEST fixture>` | `PASS`, 0 issues, exit 0 | `rows_read: 1`, `status: PASS`, `issue_count: 0`, `EXITCODE=0` | **PASS** | Fixture is a software test record, not an observation |
| 9 | CLI invalid CSV | same command with bad date, longitude 200, empty unit, bad category, duplicate id | `FAIL`, issues with correct rule IDs, exit 1 | `status: FAIL`, 6 errors: VR-004, VR-005, VR-003, VR-006, VR-009, VR-008; `EXITCODE=1` | **PASS** | Detection behaviour verified; no input modification checked separately below |
| 10 | Read-only validation | Code inspection + tests using temp files | No write to input CSV | All validators open inputs in read mode; tests create files only in `TemporaryDirectory` / temp path | **PASS** | Not a formal file-hash regression test |
| 11 | Package structure | File listing | Suggested structure present with no empty placeholder files | README, 2 contracts, 1 protocol, 2 modules, 2 test modules, 2 reports, 1 log present | **PASS** | `src/aquainsar.egg-info` remains outside this package |
| 12 | Activity log format | Plain-text read | UTF-8 text, 17 required sections, chronological entries | Present; entries dated only 2026-11-24 with evidence labels | **PASS** | AC review/adoption of AI-assisted entries pending |

## 2. Defects found during execution and corrections applied

| Cycle | Failure observed | Root cause | Correction | Re-test |
|---|---|---|---|---|
| 1 | `check-contract` returned `FAIL` with two `VR-010` errors (`dataset_id` absent from schemas `AQS-GW-CGWB-WELL`, `AQS-RAIN-IMD-DISTRICT`) | The contract's own provenance rule was violated by two of its schemas | Added `dataset_id` field to both schemas in JSON and Markdown; added it to test fixtures | `check-contract` → `PASS`, 0 issues |
| 1 | 7 of 24 tests failed (`17 passed`, pytest `7 failed, 17 passed, 73 subtests passed`) | Four failures from the missing schema field; two from assertions matching line-wrapped prose exactly; one (empty-file case) from the same missing field | Fixed schemas; made two prose assertions robust to line wrapping | Cycle 2 |
| 2 | 4 of 24 tests still failed; diagnostic report showed `VR-001` errors for optional fields `datum`, `screen_depth_m`, `aquifer`, `missing_reason` | Validator incorrectly required **all** schema columns instead of only `required: true` columns | Changed `validate_dataset_csv` to apply `VR-001` only to required fields | Cycle 3: 24/24 pass under both unittest and pytest |

No test expectation was weakened to hide a validation defect. The only assertion changes were for exact prose matching; all validation-behaviour assertions remain unchanged.

## 3. Contract QA detail

- **Syntax:** valid JSON; parsed by `json.load`, `json.tool` exit 0.
- **Schema consistency:** 5 dataset IDs unique; 3 active schemas with unique field names; all field types in the supported vocabulary; patterns compile; ranges ordered; unique constraints and unit pairs resolve to existing fields; 11 validation rules have unique IDs and valid severities.
- **Field definitions:** every field has name, type, required, nullable, description and provenance; units are explicit or absent by design; allowed values and patterns are declared only where justified.
- **Version information:** `AQS-DC` / `0.9.0` / `DRAFT_FOR_W1_REVIEW` present identically in both representations; revision history has one dated entry.
- **Human/machine agreement:** automated checks confirm all dataset IDs, all active field names, all rule IDs/severities and the version/status string appear in the Markdown companion.
- **Units:** canonical units are marked `PENDING`/`PROPOSED`; no conversion logic exists.
- **Known intentional limitation:** all datasets are prospective (`NO_LOCAL_DATA`); CRS, grid, boundary and canonical units remain pending AQ-01/AQ-03/AQ-04/AQ-05.

## 4. Protocol QA detail

- **Objective:** research question, observation/reference definitions and can/cannot-support table present (§4.1).
- **Coherence:** preparation → spatial candidates → temporal candidates → descriptive statistics → uncertainty → reproducibility (§§4.2–4.7).
- **Spatial assumptions:** no method selected; preconditions stated; interpolation disallowed while CRS/well density unverified.
- **Temporal assumptions:** acquisition vs observation distinction; date-only precision; asynchronous-observation limitations.
- **Statistical suitability:** each of eight methods has purpose, inputs, assumptions, output, interpretation and limitations; correlations are conditional on fixed matching; all comparisons must be reported including null results.
- **Uncertainty:** ten factors classified by evidence status; scope/coverage requirements stated.
- **Reproducibility:** inputs, dependencies, configuration, processing sequence, output naming, provenance and execution-record template defined.
- **Result integrity:** explicitly "not a results report"; no computed association, validation or forecast.

## 5. Implementation QA detail

- Imports verified under Python 3.13.5 with no third-party runtime dependency.
- Validation functions tested for: valid rows, missing required column, invalid date, non-finite number, duplicate primary and alternate keys, out-of-range coordinate, empty non-nullable field, invalid categorical value, missing unit, unexpected column (warning), empty file (warning), unknown dataset id, JSON serialisability, contract consistency.
- Error handling: `ContractError` for missing/invalid JSON, unknown dataset or missing active schema; CLI exit codes 0/1/2.
- Reproducibility: deterministic functions, no randomness, temp-file fixtures, no downloads.

## 6. Overall QA status

**All executed checks pass.** This is a PASS of structural, documentation and software checks only. It is **not** a scientific validation and **not** approval of the deliverables: AC/SJ review is still required, and the contract itself remains v0.9.0 pending AQ-01/AQ-03/AQ-04/AQ-05.

## 7. Remaining issues

1. No real data validation possible in W1 (G-01…G-05, G-10).
2. No external JSON Schema validator used; consistency is checked by the project's own tool.
3. Methodological peer/supervisor review not recorded; protocol remains draft.
4. `Project_Details.pdf` and official competition checklist unavailable (G-06, G-07).
5. Stale root `src/aquainsar.egg-info` claims code/tests that are not in the checkout; not part of this package and not treated as capability.
6. Activity log was prepared by AI-assisted session work; AC adoption must be recorded by AC, not assumed.
