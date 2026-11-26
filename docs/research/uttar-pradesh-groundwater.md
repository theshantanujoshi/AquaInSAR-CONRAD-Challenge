# Uttar Pradesh Groundwater: Official Assessment and Monitoring Evidence

**Status:** Verified from Central Ground Water Board (CGWB) publications accessed 2026-11-26. State-level context only. No pilot area, block, aquifer, or dataset is selected here.

## Why this document exists

AquaInSAR needs a defensible groundwater context before it can choose a pilot or interpret deformation. This document records what the official 2024 state assessment and the 2022–23 monitoring yearbook actually say, and what they do not say.

The core distinction:

- An **assessment unit category** is a water-balance classification at block scale.
- A **monitoring well** is a point measurement of hydraulic head at a specific location, screen depth, and time.
- **InSAR** measures surface displacement along the satellite line of sight.
- None of these is interchangeable with another, and none alone establishes causation.

## 2024 state resource assessment

CGWB's two-page summary, *Dynamic Ground Water Resources & Ground Water Quality of Uttar Pradesh, 2024* (December 2024), reports:

| Indicator | Reported value |
|---|---|
| Assessment unit type | Block |
| Number of assessment units | **836** |
| Average assessment-unit area | 274.59 km² |
| Total annual groundwater recharge | **72.84 bcm** |
| Annual extractable groundwater resource | **66.38 bcm** in the table; **66.37 bcm** in the narrative |
| Annual groundwater extraction | **46.76 bcm** |
| Stage of groundwater extraction | **70.45%** |
| State rainfall | 887.24 mm (as reported) |

### Assessment categories

CGWB defines the categories by stage of extraction:

| Category | Stage of extraction | Number of blocks | Share |
|---|---|---|---|
| Safe | ≤ 70% | **566** | **67.7%** |
| Semi-critical | > 70% and ≤ 90% | **165** | **19.74%** |
| Critical | > 90% and ≤ 100% | **46** | **5.5%** |
| Over-exploited | > 100% | **59** | **7.06%** |

The summary also notes that the 2024 assessment was carried out through the IN-GRES web application developed by CGWB with IIT Hyderabad. The same summary reports earlier assessment years, which is a reminder not to mix category counts across years.

### Hydrogeological setting

The summary identifies five distinct hydrogeological units:

1. Bhabar — mainly a recharge zone with deeper water levels.
2. Terai — fine-grained sediments with occasional pebbles and boulders, between Bhabar and the Central Ganga Plain.
3. Central Ganga Plain — described as the most promising groundwater repository, with a multi-layered aquifer system.
4. Marginal alluvial plain.
5. Southern hard-rock terrain of Bundelkhand, including granite/granitic gneiss and Vindhyan sedimentary formations in Mirzapur and Sonbhadra.

This matters because a subsidence mechanism is geology-dependent. Compressible alluvial aquifers can compact when effective stress changes; hard-rock terrain behaves differently. A state-level category or a single InSAR rate cannot substitute for site geology.

### What the 2024 summary does not establish

- It does not identify which 59 blocks are over-exploited. The two-page summary gives counts and state totals, not a block list.
- It does not provide station-level water levels, well metadata, or time series.
- It does not measure subsidence or aquifer compaction.
- It does not show that an over-exploited block is currently subsiding.
- It does not establish that groundwater extraction is the dominant cause of any local deformation.
- It does not resolve the 66.38 vs 66.37 bcm discrepancy between its table and narrative. Cite the figure with the discrepancy visible or use the table value and note the narrative value.

The full 2024 assessment report or IN-GRES output is needed to screen block names, boundaries, and category changes over time.

## Monitoring network: 2022–23 yearbook

The *Ground Water Year Book, Uttar Pradesh (2022–23)* describes the manual monitoring network and publishes the year's observations.

### Network and frequency

- **1,007 groundwater monitoring wells** across the state.
- Mostly **open wells**, which are slowly being replaced by special bore wells for monitoring (piezometers).
- Water levels measured **four times a year**: May, August, November, and January.
- A few wells are monitored through a participatory program for the remaining eight months.
- Chemical samples are collected once a year in May and analyzed at the regional laboratory.
- Water-level statistics are computed for wells entered in the GEMS software.

### What the yearbook publishes

- Depth-to-water-level tables by district for May 2022, August 2022, November 2022, and January 2023.
- Seasonal fluctuation (May–November 2022).
- Annual fluctuation for four measurement pairs.
- Decadal mean fluctuation.
- Decadal water-level trend for pre-monsoon and post-monsoon (2013–2022).
- Deeper-aquifer water levels for May and November 2022.
- Annexure 1: well-level depth-to-water data for the four measurement rounds.
- Annexure 2: 2013–2022 water-level trends for monitoring wells.

A separate 2023–24 yearbook is also published. Use the year that matches the analysis period and do not mix network counts or categories across years.

### What the monitoring data do not establish

- **A count is not coverage.** One thousand wells across a large state does not mean dense coverage in a candidate block. Station density and spatial representativeness must be measured for the actual polygon.
- **A well is not a pixel.** A well measures hydraulic head at a point and screen interval; an InSAR pixel averages surface motion over its resolution cell. The spatial mismatch must be documented.
- **Four measurements a year are not a continuous series.** Seasonal extremes may be missed, and measurement dates rarely coincide with satellite acquisitions. Interpolation, if used, needs an explicit method and uncertainty.
- **Well type and depth matter.** Open wells, shallow piezometers, and deeper piezometers can respond differently. Compare like with like, and record the screen interval and aquifer.
- **Datum and elevation matter.** Do not compare water-level depths without checking the reference datum and sign convention.
- **A declining head is not automatically compaction.** Storage loss, pumping, recharge, and aquifer properties all matter. Subsidence requires compressible material and effective-stress change.
- **The 2022–23 network count is date-specific.** Do not treat 1,007 as the current operational count without checking a later CGWB source.

## How this evidence can support candidate screening

Use the official material as a screening layer, not a decision:

1. **Block category and trend.** Identify blocks that are over-exploited or critical in the current assessment and worsening across assessment years.
2. **Station-level records.** For the candidate polygon, list stations with coordinates, well type, screen depth, aquifer, measurement dates, datum, and gaps.
3. **Hydrogeology.** Check whether the block is in the Central Ganga Plain alluvium, marginal alluvium, Bhabar/Terai, or hard-rock terrain. Record the aquifer geometry and compressible-layer evidence if available.
4. **Rainfall and recharge context.** Get district or finer rainfall data and document the mismatch between the rainfall polygon and the candidate boundary.
5. **Satellite feasibility.** Check same-track Sentinel-1 SLC coverage and coherence by season before assuming a deformation series is possible.
6. **Validation access.** Check whether GNSS, levelling, or independent displacement observations exist. Groundwater head is not a displacement validation.
7. **Decision record.** Apply the SJ rubric, record rejected alternatives, and keep a no-go/conditional outcome if the evidence is inadequate.

## Data access notes

| Source | Use | Check before relying |
|---|---|---|
| [CGWB 2024 state summary](https://cgwb.gov.in/cgwbpnm/publication-detail/1534) | State and block-category context | Block names and boundaries are not in the two-page summary; get the full assessment or IN-GRES output. |
| [CGWB UP Year Book 2022–23](https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17032384351875462524file.pdf) | Manual water levels and trends | Station-level annexures still need extraction and quality review. |
| [CGWB UP Year Book 2023–24](https://cgwb.gov.in/cgwbpnm/download/1730) | More recent yearbook | Use the matching assessment/yearbook year; do not mix counts. |
| [CGWB Ground Water Level Monitoring](https://cgwb.gov.in/en/ground-water-level-monitoring) | Network description and publication links | Verify current access paths and any telemetry/station-level download. |
| [India-WRIS](https://indiawris.gov.in/) | National water-resources portal; possible station data discovery | **Unreachable on 2026-11-26** (connection timeout). Verify availability, station series, export format, provenance, and terms before relying on it. |
| [IMD rainfall statistics](https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php) | District rainfall context | District aggregates may not match the block or well locations. |

## Open evidence gaps

- No block-level candidate matrix exists yet.
- No station-level CGWB extract has been assembled for a candidate polygon.
- No rainfall series has been matched to a candidate.
- No groundwater hydrograph has been compared with InSAR displacement.
- No aquifer-compaction or compressible-layer assessment exists for a candidate.
- No validation dataset (GNSS, levelling, or independent displacement) has been identified.

These gaps are expected at this stage. They are the reason the pilot and method remain **Open**, not validated.

## Sources

- CGWB, [Dynamic Ground Water Resources & Ground Water Quality of Uttar Pradesh, 2024](https://cgwb.gov.in/cgwbpnm/publication-detail/1534), summary PDF accessed via `https://cgwb.gov.in/cgwbpnm/download/1411` on 2026-11-26.
- CGWB, [Ground Water Year Book, Uttar Pradesh (2022–23)](https://cgwb.gov.in/cgwbpnm/public/uploads/documents/17032384351875462524file.pdf), accessed 2026-11-26.
- CGWB, [Ground Water Year Book, Uttar Pradesh (2023–24)](https://cgwb.gov.in/cgwbpnm/download/1730), publication link accessed 2026-11-26.
- CGWB, [Ground Water Level Monitoring](https://cgwb.gov.in/en/ground-water-level-monitoring), accessed 2026-11-26.
- India-WRIS, <https://indiawris.gov.in/>, access attempted 2026-11-26; the portal did not respond, so no content or terms were verified.
- IMD, [District rainfall statistics](https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php), cited for context; not re-fetched and terms not reviewed on 2026-11-26.

See [`source-register.md`](source-register.md) for the consolidated register and access notes.
