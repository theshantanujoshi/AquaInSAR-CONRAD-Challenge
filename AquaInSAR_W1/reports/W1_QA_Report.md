# W1 QA Report — AC deliverable package

**Initial execution:** 2026-11-24 (23:30–23:38 IST)
**Review-fix execution:** 2026-11-27
**Package:** `AquaInSAR_W1` · **Contract:** `AQS-DC` v0.9.0 (draft revision 1) · **Protocol:** `AQS-ECP` v0.9.0 (draft)
**Executor of record:** AI-assisted work directed for AC; independent reviewer (SJ) review not yet recorded.

All commands were run from `<repo-root>` with Python 3.13.5. `PYTHONPATH` was set to `AquaInSAR_W1\src` (plus `AquaInSAR_W1\tests` for CLI fixture commands). No network access and no real AquaInSAR data were used. CI runs the same checks on Python 3.12 via `.github/workflows/validate.yml`.

## 1. Executed checks and actual results (final, 2026-11-27)

| # | Test performed | Command | Expected outcome | Actual outcome | Status | Remaining issue |
|---|---|---|---|---|---|---|
| 1 | JSON syntax | `python -m json.tool <repo-root>/AquaInSAR_W1/contracts/AquaInSAR_Data_Contract_v0.9.0.json` | Valid JSON, exit 0 | `JSON_TOOL_EXIT=0` | **PASS** | None |
| 2 | Contract internal consistency | `python -m aquainsar_w1.contract_tools check-contract --contract ...` | `status: PASS`, no issues | `{"contract_id":"AQS-DC","contract_version":"0.9.0","status":"PASS","issues":[]}`, `EXITCODE=0` | **PASS** | Checks are internal, not an external JSON Schema |
| 3 | Full unittest suite | `python -m unittest discover -s AquaInSAR_W1/tests -v` | All tests pass | `Ran 47 tests ... OK`, `EXITCODE=0` | **PASS** | Includes negative contract tests and all PR-review fix tests |
| 4 | Independent runner | `python -m pytest -q AquaInSAR_W1/tests` | All tests pass | `47 passed, 90 subtests passed in 0.19s`, `EXITCODE=0` | **PASS** | pytest is optional; stdlib unittest is canonical |
| 5 | Human/machine contract agreement | `test_docs_consistency.py` (IDs, field names incl. new geometry/interval/reason-map fields, rule IDs, version, status) | Every JSON definition appears in Markdown | All doc-consistency tests pass | **PASS** | Agreement is checked for names/IDs/rules, not full prose equivalence |
| 6 | Protocol QA | `test_docs_consistency.py` sections, no-results, draft version, numbering note | Sections 4.1–4.7 present; explicit no-results; v0.9.0 draft; assignment numbering explained | Pass | **PASS** | Methodological review by SJ still pending |
| 7 | Contract checker negative tests | `ContractStructureNegativeTests` | Detect duplicate dataset ids, invalid pattern, missing description, missing provenance, invalid conditional flags | All 5 negative tests pass | **PASS** | Checker is now exercised beyond the happy path |
| 8 | Python syntax compile | `python -m py_compile ...` | Exit 0 | `PY_COMPILE_EXIT=0` (initial run); CI uses `compileall` | **PASS** | Generated `__pycache__` directories are removed after testing; they regenerate on execution |
| 9 | CLI valid CSV | `validate-csv --dataset AQS-GW-CGWB-WELL --csv <SYNTHETIC_TEST fixture>` | `PASS`, 0 issues, exit 0 | `rows_read: 1`, `status: PASS`, `issue_count: 0`, `EXITCODE=0` | **PASS** | Fixture is a software test record, not an observation |
| 10 | CLI invalid CSV | Same command with bad date, longitude 200, empty unit, bad category, duplicate id | `FAIL`, correct rule IDs, exit 1 | `status: FAIL`, 6 errors: VR-004, VR-005, VR-003, VR-006, VR-009, VR-008; `EXITCODE=1` | **PASS** | Detection behaviour verified |
| 11 | Value/quality semantics | Tests for MASKED/NOT_MEASURED with and without values | No-value flags reject values; empty values with reasons pass | `VR-012` detected for value+no-value flag; empty+reason rows PASS; VALID+empty still `VR-003` | **PASS** | None |
| 12 | Acquisition geometry | Tests for required platform/orbit/direction and track-aware unique key | Missing geometry fails; different tracks do not collide; same track collides | `VR-001`, `VR-008` behave as specified | **PASS** | None |
| 13 | Row dataset id / reason map / rainfall interval | Tests for VR-014/VR-016/VR-015 | Mismatched id fails; version suffix passes; multiple empty optionals need map; reversed period fails | All cases pass | **PASS** | None |
| 14 | Package structure | File listing | Suggested structure present with no empty placeholder files | README, 2 contracts, 1 protocol, 2 modules, 2 test modules, 2 reports, 1 log present | **PASS** | PR #4 removed tracked `egg-info`/`__pycache__` artifacts; tree is clean |
| 15 | CI configuration | Read `.github/workflows/validate.yml` (present via PR #5) | PRs run check-contract + unittest without third-party deps | Workflow uses `actions/checkout@v4`, `actions/setup-python@v5` (Python 3.12), `json.tool`, `check-contract`, `unittest discover`, `compileall` | **PASS** | Required status check must be enabled in repository settings by the team |
| 16 | Activity log format | Plain-text read | UTF-8 text, 17 required sections, chronological entries | Present; entries dated 2026-11-24 and 2026-11-27 with evidence labels | **PASS** | AC review/adoption of AI-assisted entries pending |

## 2. Defect history

### Initial build cycles (2026-11-24)

| Cycle | Failure observed | Root cause | Correction | Re-test |
|---|---|---|---|---|
| 1 | `check-contract` returned `FAIL` with two `VR-010` errors (`dataset_id` absent from groundwater and rainfall schemas) | Contract violated its own provenance rule | Added `dataset_id` field to both schemas (JSON + Markdown) and fixtures | `check-contract` → PASS |
| 1 | 7 of 24 tests failed | Missing schema field; two over-literal prose assertions | Fixed schemas; made prose assertions robust to line wrapping | Cycle 2 |
| 2 | 4 of 24 tests failed; `VR-001` on optional fields | Validator required all columns, not only required ones | VR-001 applies only to `required: true` fields | Cycle 3: 24/24 pass |

### PR-review correction cycles (2026-11-27)

| Cycle | Failure observed | Root cause | Correction | Re-test |
|---|---|---|---|---|
| 4 | Versioned dataset id `AQS-GW-CGWB-WELL-v1.0.0` rejected by regex | Pattern did not allow `-v<semver>` suffix | Pattern updated in JSON + Markdown for all three schemas | 47/47 pass |
| 4 | No-value quality flag with empty value still produced `VR-003` (test fixture) | Test omitted the quality-flag assignment | Fixture corrected to set `quality_flag=NOT_MEASURED` | 47/47 pass |
| 4 | `VR-016` never fired for multiple empty optional fields | Comprehension reused a stale loop variable instead of `definition["name"]` | Fixed comprehension; also restricted counting to columns actually present in the CSV header | 47/47 pass |

No test expectation was weakened to hide a validation defect. All validation-behaviour assertions remain unchanged or were strengthened.

## 3. Contract QA detail (final)

- **Syntax:** valid JSON; `json.load` and `json.tool` exit 0.
- **Schema consistency:** 5 dataset ids unique; 3 active schemas with unique field names; supported types only; patterns compile; ranges ordered; unique constraints and unit pairs resolve; **16** validation rules with unique ids and valid severities.
- **Value/quality semantics:** value-required flags (`VALID`, `LOW_COHERENCE`, `ATMOSPHERIC`, `QUESTIONABLE`) require a measurement; no-value flags (`MASKED`, `INVALID`, `UNKNOWN`, `NOT_MEASURED`) require an empty value and a recorded reason. Conditional nullability is declared per measurement field and checked by VR-012/VR-013.
- **InSAR geometry:** `platform`, `relative_orbit`, `pass_direction` are required; optional `polarization`/`incidence_angle` added; unique key includes relative orbit and pass direction so tracks are not pooled.
- **Rainfall interval:** `period_start`/`period_end` are required ISO dates; `observation_date` is source-report date only; VR-015 rejects reversed intervals; unique key uses the explicit interval.
- **Provenance:** row `dataset_id` must equal the selected dataset or use `<id>-v<semver>` (VR-014); `missing_reason_map` covers per-field reasons (VR-016).
- **Field definitions:** every field has name, type, required, nullable, description and provenance; units explicit or absent by design.
- **Version information:** `AQS-DC` / `0.9.0` / `DRAFT_FOR_W1_REVIEW` in both files; revision history has initial and 2026-11-27 review-correction entries.
- **Human/machine agreement:** automated checks confirm all dataset ids, active field names, rule ids/severities and version/status in the Markdown companion.
- **Known limitation:** canonical CRS, grid, boundary, units and exchange formats remain pending AQ-01/AQ-03/AQ-04/AQ-05.

## 4. Protocol QA detail (final)

- **Objective and claim boundary:** §4.1; explicitly "not a results report".
- **Version:** lowered from 1.0.0 to `0.9.0` (draft, unreleased); filename renamed accordingly.
- **Numbering:** note added that §§4.1–4.8 retain the W1 assignment numbering, not a chapter index.
- **Spatial/temporal methods:** preconditions stated; no method selected; rainfall matching uses `[period_start, period_end]`, not `observation_date` alone.
- **Statistics:** eight exploratory methods, each with purpose, inputs, assumptions, output, interpretation and limitations; correlations require fixed matching; all comparisons including nulls must be reported.
- **Uncertainty/reproducibility:** ten factors classified by evidence status; inputs, config, sequence, naming, provenance and execution-record template defined.

## 5. Implementation QA detail (final)

- Imports verified under Python 3.13.5 and CI Python 3.12; no third-party runtime dependency.
- 47 tests cover: valid/malformed CSV rows; contract structure negatives; value/quality semantics; geometry; rainfall interval; dataset id; reason maps; duplicate keys; documentation agreement.
- Error handling: `ContractError` for missing/invalid JSON, unknown dataset or missing active schema; CLI exit codes 0/1/2.
- Reproducibility: deterministic functions, no randomness, temp-file fixtures labelled `SYNTHETIC_TEST`, no downloads.

## 6. Overall QA status

**All executed checks pass.** This is a PASS of structural, documentation and software checks only. It is **not** scientific validation and **not** approval of the deliverables: AC/SJ review is still required, and both contract and protocol remain v0.9.0 drafts.

## 7. Remaining issues

1. No real data validation possible in W1 (G-01…G-05, G-10).
2. No external JSON Schema validator used; consistency is checked by the project's own tool.
3. Methodological peer/supervisor review not recorded; both documents remain drafts.
4. `Project_Details.pdf` and official competition checklist unavailable (G-06, G-07).
5. Activity log was prepared by AI-assisted session work; AC adoption must be recorded by AC, not assumed.
6. CI required status check must be enabled in repository settings (workflow file itself is present).
