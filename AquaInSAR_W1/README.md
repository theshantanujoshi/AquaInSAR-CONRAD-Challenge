# AquaInSAR_W1 — AC deliverable package

**Owner:** AC (Aishwary) · **Week:** W1 · **Prepared:** 2026-11-24 · **Review gate:** 2026-11-29
**Task:** AQS-W01-AC — data contract and exploratory satellite-to-ground comparison protocol.

## What this package is

A provisional, reviewable research-engineering foundation:

- a **versioned data contract** (`v0.9.0`, draft) in human-readable and machine-readable form;
- an **exploratory comparison protocol** (`v1.0`, draft) that specifies *how* comparisons may be done, without reporting any result;
- a small **stdlib-only validator** that checks contract consistency and CSV schema/quality;
- offline deterministic **tests**, a **QA report**, a **project-context map**, and an **activity log**.

This package is **not** a processing pipeline, a validated model, a dashboard, or a forecast. No real data, Sentinel-1 scene, deformation product, groundwater series or validation label exists in the repository. Synthetic records in tests are software fixtures labelled `SYNTHETIC_TEST` and are never presented as observations.

## Why the contract is v0.9.0

AQ-01 (pilot), AQ-03 (reference data), AQ-04 (Sentinel-1 feasibility) and AQ-05 (CRS, grid, units, exchange formats, vocabularies) are unresolved. Declaring v1.0 would assert a coherence the evidence does not support. Promotion to `1.0.0` is a recorded decision at the 2026-12-06 gate. See contract §0.

## Directory

```text
AquaInSAR_W1/
├── README.md                          this file
├── contracts/
│   ├── AquaInSAR_Data_Contract_v0.9.0.md          human-readable contract
│   └── AquaInSAR_Data_Contract_v0.9.0.json        canonical machine-readable contract
├── protocols/
│   └── AquaInSAR_Exploratory_Comparison_Protocol_v1.0.md
├── src/aquainsar_w1/
│   ├── __init__.py
│   └── contract_tools.py              contract + CSV validation, stdlib only
├── tests/
│   ├── test_contract_tools.py         schema/quality validation tests
│   └── test_docs_consistency.py       human/machine doc agreement tests
├── reports/
│   ├── W1_QA_Report.md                executed checks and results
│   └── W1_Project_Context_Map.md      classified findings and gap register
└── logs/
    └── AishwaryLogW1.txt              plain-text chronological engineering log
```

## Run the checks

From the repository root (`AquaInSAR-CONRAD-Challenge`), Python 3.10+:

```powershell
$env:PYTHONPATH = "AquaInSAR_W1\src"
python -m aquainsar_w1.contract_tools check-contract --contract AquaInSAR_W1\contracts\AquaInSAR_Data_Contract_v0.9.0.json
python -m unittest discover -s AquaInSAR_W1\tests -v
python -m pytest -q AquaInSAR_W1\tests
```

Validate a real CSV once one exists (the fixture below is not scientific data):

```powershell
python -m aquainsar_w1.contract_tools validate-csv `
  --contract AquaInSAR_W1\contracts\AquaInSAR_Data_Contract_v0.9.0.json `
  --dataset AQS-GW-CGWB-WELL --csv path\to\table.csv
```

The validator exits `0` for PASS / PASS_WITH_WARNINGS, `1` for FAIL, `2` for contract errors. It prints a JSON report with rule IDs, severities, data-row numbers and field names. It never edits, filters, imputes or repairs input data.

## Validation behaviour at a glance

`VR-001` required columns · `VR-002` unexpected columns / empty file (warning) · `VR-003` empty non-nullable field · `VR-004` type/non-finite/range · `VR-005` coordinate range · `VR-006` categorical values · `VR-007` string pattern · `VR-008` unique constraints · `VR-009` value/unit pairing · `VR-010` provenance completeness · `VR-011` contract internal consistency.

Passing validation means "structurally consistent with the provisional contract", not "scientifically valid" and not "comparable to another dataset".

## Status against W1 acceptance criteria

| Criterion | Status |
|---|---|
| Project context inspected | Done — `reports/W1_Project_Context_Map.md` |
| Confirmed requirements distinguished from assumptions | Done — classified map and contract PENDING fields |
| Versioned data contract exists | Done — v0.9.0 draft (not v1.0, see above) |
| Machine-readable contract valid | Checked — see `reports/W1_QA_Report.md` |
| Human and machine representations agree | Checked — automated consistency tests |
| Exploratory comparison protocol documented | Done — v1.0 draft |
| Methodological limitations addressed | Done — protocol §§4.5–4.7 |
| Supporting implementation where justified | Done — stdlib validator, no science performed |
| Tests executed and recorded | See `reports/W1_QA_Report.md` |
| QA report exists | Done |
| Activity log accurate | Done — `logs/AishwaryLogW1.txt` |
| README explains package | Done |
| Files organised for review | Done |

Reviewers should treat all deliverables as **draft pending AC/SJ review**, not as accepted task completion.

## Handover to W2

W2 (`AQS-W02-AC`) requires contract v1.0 after AQ-05 and a runnable ingest/quality-check workflow. Needed inputs: pilot boundary (AQ-01/SJ), real source schemas and manifests (AQ-03/MF), Sentinel-1 acquisition metadata (AQ-04/SM), and dashboard consumption needs (AP). No W2 work is performed here.
