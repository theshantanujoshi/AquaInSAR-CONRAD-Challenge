# Independent Research Notes: AquaInSAR

**Purpose:** background research gathered outside the dated deliverables in `tasks/plan.md`. This is a reference note, not a pilot selection, approved methodology, or evidence that AquaInSAR has produced or validated results.

**Research snapshot:** 2026-11-24. Recheck live access, product status, competition rules, and data releases before relying on operational details.

## How to use these notes

- Treat cited studies as published evidence about their own locations, periods, methods, and uncertainties. Their results do not establish a groundwater–subsidence relationship for a future AquaInSAR pilot.
- Separate **ground displacement** (an InSAR observation) from **groundwater level/storage** and from **cause**. InSAR does not measure aquifer water levels.
- A source's existence is not proof that the data are available at the required spatial/temporal scale, licensed for the intended use, or usable in a prototype.
- The candidate leads below are research leads only. MF's planned inventory and the team's rubric remain the decision process.

## Findings at a glance

1. **There is published InSAR work in Uttar Pradesh, but the clearest examples found are urban.** Lucknow and Varanasi have published Sentinel-1 studies. This is evidence of local deformation observations, not proof that the signal is groundwater-caused everywhere or that it transfers to agricultural pixels.
2. **Uttar Pradesh has extensive official groundwater monitoring and assessment material.** CGWB publishes quarterly well observations and state resource assessments. Dataset resolution, well metadata, and access terms still need checking for any chosen study area.
3. **Sentinel-1 is practical for a historical deformation study, but crop cover is a material feasibility risk.** Its C-band interferometric signal can decorrelate as vegetation and surface conditions change; a real stack and coherence assessment are required.
4. **A low-friction processing route exists.** ASF HyP3 offers Sentinel-1 on-demand products with a monthly free credit allocation; MintPy supports time-series analysis of HyP3 and several other processor outputs. Availability and quotas can change.
5. **NISAR is a promising complement, not a historical substitute yet.** Validated L-band products in the public catalog begin on 2026-10-21, so the validated time span is too short as of this snapshot for a multi-year trend.
6. **The official competition materials list a Water Challenge as well as Aerospace & Aviation.** The product may have a plausible category fit in either; confirm the registered choice and any change process with Conrad.

## Scientific context and Uttar Pradesh evidence

### What InSAR can and cannot establish

Differential InSAR estimates changes in satellite-to-ground range between acquisitions. A time series can estimate line-of-sight displacement for coherent pixels. A line-of-sight rate is not automatically vertical subsidence: horizontal motion can contribute, and viewing geometry, reference choice, atmosphere, orbit errors, decorrelation, unwrapping errors, and processing choices affect the estimate. See the [ASF Sentinel-1 InSAR Product Guide](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/) for product interpretation and error sources.

Even where downward motion and groundwater decline coincide, correlation does not by itself establish cause. Compaction of compressible aquifer materials is a plausible mechanism, but geology, construction, tectonics, seasonal soil movement, and other processes must be considered. InSAR measures surface motion; independent groundwater observations and hydrogeological interpretation are needed to test a groundwater explanation.

### Published Uttar Pradesh examples located in this scan

| Study area | Evidence reported by the cited study | Limits for AquaInSAR |
|---|---|---|
| Lucknow | A 2022 PSInSAR study used 58 ascending and 60 descending Sentinel-1 acquisitions from 2014–2020. A separate 2022 study reports two subsidence zones and estimates roughly 10–40 mm/year over about 27.6 km² (9.3% of its study area). | Urban/peri-urban findings; study-specific estimates and methods. Do not generalize the rates to a rural district or interpret them as an independently validated groundwater forecast. |
| Lucknow | A 2025 study combines Sentinel-1, GNSS, and in-situ observations from 2014–2024 and reports a maximum subsidence rate exceeding about 36 mm/year near Charbagh, Indira Nagar, and nearby areas. | The published abstract attributes the pattern principally to groundwater over-extraction; AquaInSAR should treat that as the authors' interpretation and inspect the full method, reference network, and uncertainty before reusing the claim. |
| Varanasi | A 2024 study combines Sentinel-1 (2017–2023), GRACE (2003–2023), groundwater levels (1998–2023), and precipitation (2002–2023); it reports about 2–8 mm/year subsidence along parts of the Ganga riverfront and a regional GRACE-derived groundwater-storage decline estimate. | The riverfront result is a local urban signal. GRACE is coarse relative to city/block/well scales; do not present it as a local well measurement. |

The studies establish that relevant analysis has been attempted in the state. They do **not** settle the team's pilot choice. A key gap is the scarcity of comparably clear, peer-reviewed, agricultural-pixel evidence found in this quick scan.

### Agricultural coherence and signal risk

Interferometric phase requires sufficiently similar radar scattering between acquisitions. Crops change with growth, irrigation, harvest, and monsoon conditions; this can reduce coherence and leave gaps precisely in the agricultural areas of interest. The actual risk depends on crop calendar, acquisition interval, surface moisture, orbit, and local scattering. Screen real Sentinel-1 SLCs for each candidate and report coherent-pixel coverage by season before promising a regional time series. Urban persistent scatterers may help characterize nearby deformation, but they are not a substitute for agricultural coverage or groundwater validation.

## Data sources and their role

| Source | Potential use | Important caveat / next check |
|---|---|---|
| [CGWB groundwater monitoring](https://cgwb.gov.in/en/ground-water-level-monitoring) | Observation-well water levels; CGWB says measurements are made four times yearly and provides compiled historical data since 1994. | Inspect the specific station coordinates, well type/screen/datum, missing records, aquifer, and temporal continuity. National network size does not imply dense coverage in a selected block. |
| [CGWB Ground Water Year Book, Uttar Pradesh 2023–24](https://cgwb.gov.in/cgwbpnm/publication-detail/1730) | State/yearbook context and water-level observations. The 2022–23 yearbook describes a 1,007-well network; a later CGWB bulletin reports 1,464 operational wells as of May 2024. | Network counts are date-dependent; use the matching yearbook/bulletin and station-level data rather than a headline count. |
| [CGWB Dynamic Ground Water Resources of Uttar Pradesh, 2024](https://cgwb.gov.in/cgwbpnm/publication-detail/1534) | Official assessment-unit categories and state resource estimates. The 2024 assessment summary reports 836 units: 566 safe, 165 semi-critical, 46 critical, and 59 over-exploited; overall extraction stage about 70.45%. | Assessment categories are not well-level observations or a direct subsidence mechanism. Check the assessment year and exact unit boundary; the report is a screening source, not local validation. |
| [India-WRIS](https://indiawris.gov.in/) | Potential source discovery for water resources and monitoring data. | Confirm actual station series, downloadable format, access conditions, and provenance for the candidate. Do not assume every portal layer is an open, analysis-ready dataset. |
| [IMD rainfall statistics](https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php) | District rainfall statistics and seasonal context. | District aggregates may not match the pilot boundary or well locations; document temporal aggregation and spatial mismatch. |
| [ASF Vertex / Sentinel-1 archive](https://search.asf.alaska.edu/) and [Copernicus Data Space](https://dataspace.copernicus.eu/) | Search and access Sentinel-1 scenes; SLC is required for interferometric processing. | Query the actual candidate polygons, product type, relative orbit, dates, polarization, and acquisition count. Archive presence does not prove coherence or processing success. |
| [GRACE / GRACE-FO](https://grace.jpl.nasa.gov/data/get-data/) | Broad regional terrestrial-water-storage context and long temporal trends. | Coarse spatial footprint; storage is not synonymous with groundwater, and it cannot resolve an individual well or small district reliably. Use as context alongside local data, not a local reference label. |
| [NISAR data availability](https://nisar-docs.asf.alaska.edu/availability-overview/) | New L-band radar observations and Level-2 products, potentially useful where vegetation limits C-band coherence. | Validated L-band collections start 2026-10-21 as of this snapshot. The record is too short for a multi-year trend, and cross-sensor records require careful treatment. |

The current official 2024 state summary differs from older UP assessment summaries. Never mix category counts from different assessment years in one comparison without labeling the year and method.

## Processing options and practical implications

### ASF HyP3 plus MintPy

ASF's [HyP3 Basic](https://hyp3-docs.asf.alaska.edu/about/hyp3_basic/) provides on-demand Sentinel-1 products. Current documentation states 8,000 free credits per user per month; output links for most on-demand products expire after 14 days. The exact credit cost depends on product and resolution, so check the current [credit guidance](https://hyp3-docs.asf.alaska.edu/using/credits/) before submitting a stack and download outputs promptly.

[MintPy](https://mintpy.readthedocs.io/en/latest/) is an open-source InSAR time-series analysis package. Its documented inputs include HyP3, ISCE, ARIA, GMTSAR, SNAP, GAMMA, and other processor formats. It analyzes a processed interferogram stack; it does not remove the need to select suitable acquisitions, assess coherence, or understand the upstream processing.

### Other routes

- [ESA SNAP](https://step.esa.int/main/toolboxes/snap/) is a desktop toolbox for Sentinel data and can support preprocessing. It is not by itself a substitute for a documented time-series workflow and quality review.
- [ISCE2](https://github.com/isce-framework/isce2) is an open-source InSAR processing framework with Sentinel-1 support. Installation and computing burden need to be tested on the team's actual environment.
- [ASF's InSAR guides and tutorials](https://hyp3-docs.asf.alaska.edu/) provide documented on-demand product workflows and examples that connect HyP3 products to MintPy.

**Practical recommendation for the feasibility phase:** first use ASF Vertex/HyP3 to screen a small set of representative same-track pairs or bursts; inspect coherence and masks across crop seasons; only then commit to a longer stack and MintPy. This is a workflow suggestion, not a completed test or final tool decision.

## Pilot-region implications (leads, not rankings)

- **Lucknow/peri-urban fringe:** strongest published UP precedent found in this scan and potentially a practical first processing target. It is urban-centered, so it may not satisfy the agricultural-region research question without a carefully bounded agricultural fringe and compatible ground records.
- **Varanasi/Ganga riverfront:** published local subsidence analysis and long water-level context exist, but reported motion is modest and riverfront/urban-centered. A regional GRACE signal is not a local validation series.
- **Western UP candidates:** official assessments and groundwater-monitoring records may support stress screening, but this research pass did not establish a district-specific, independently validated agricultural subsidence signal. MF/SM should test these with the rubric and actual archives.

No candidate is selected or scored here. Use the official rubric, compare at least three defined areas, and retain a no-go/conditional outcome if ground-reference coverage, SLC coverage, coherence, or mechanism evidence is inadequate.

## Competition and product strategy questions

The 2026–27 [Student Guide](https://conrad.spacecenter.org/wp-content/uploads/2026/08/2026-2027-Conrad-Challenge-Student-Guide-Official.pdf) says the Innovation Stage materials and payment are due **January 7, 2027 at 11:59 PM Central Time**. The [Innovation Stage page](https://conrad.spacecenter.org/the-challenge/innovation-stage/) and calendar also list Jan 7, while the general [Challenge overview](https://conrad.spacecenter.org/the-challenge/) shows Jan 8 in its timeline. Use the guide and the team's registered portal as the working authority, and confirm if they differ. In January, 11:59 PM CST on Jan 7 converts to 11:29 AM IST on Jan 8.

The guide calls for a combined maximum **3,000-word Innovation Brief** answering ten questions, a **3–5 minute video** demonstrating an innovation model, and a **website**. It also requires a reference attachment and allows up to two optional attachments. The guide's judging weights are **Innovation 30%; Storytelling and Professionalism 20%; Practicality 20%; Marketing Strategy 20%; Finances 10%**. Innovation includes originality and IP defensibility; practicality looks for evidence and proof of concept. Confirm formatting, upload rules, and payment status in the team's portal before submission.

The team's current category is recorded as Aerospace & Aviation. The official [Water Challenge](https://conrad.spacecenter.org/water-challenge/) focuses on safe, sustainable water sources and solutions improving water equity, efficiency, or purity. Aerospace & Aviation's stated focus is advancing aerospace/aviation exploration and technology ([category page](https://conrad.spacecenter.org/aerospace-and-aviation/)). AquaInSAR has a plausible case in either category: its method uses satellite radar, while its user problem concerns groundwater. The guide says category is selected during Activation/Lean Canvas; the [rules](https://conrad.spacecenter.org/the-challenge/rules-and-regulations/) give Space Center Houston final authority over category assignment but do not specify whether a submitted choice can be changed. Ask Conrad directly before assuming a change is possible.

For judges or users, a map alone is unlikely to establish value. A credible demonstration should show the source and date of each layer, the uncertainty/quality mask, the ground-reference comparison, what decision the information could change, and what the method cannot say. A short, reproducible, carefully scoped pilot is more defensible than a broad prediction claim unsupported by labels.

For judges or users, a map alone is unlikely to establish value. A credible demonstration should show the source and date of each layer, the uncertainty/quality mask, the ground-reference comparison, what decision the information could change, and what the method cannot say. A short, reproducible, carefully scoped pilot is more defensible than a broad prediction claim unsupported by labels.

## Sources and further reading

### Official and operational sources

- CGWB, [Ground Water Level Monitoring](https://cgwb.gov.in/en/ground-water-level-monitoring).
- CGWB, [Dynamic Ground Water Resources of Uttar Pradesh, 2024](https://cgwb.gov.in/cgwbpnm/publication-detail/1534).
- CGWB, [Ground Water Year Book of Uttar Pradesh 2023–24](https://cgwb.gov.in/cgwbpnm/publication-detail/1730).
- European Space Agency, [Sentinel-1 facts and figures](https://www.esa.int/et/articles/about-us/directorates/earth-observation-programmes/copernicus/sentinel-1/facts-and-figures) and [end of Sentinel-1A operations](https://www.esa.int/ga/articles/about-us/directorates/earth-observation-programmes/copernicus/sentinel-1/time-to-say-goodbye-to-sentinel-1a).
- Alaska Satellite Facility, [HyP3 Basic](https://hyp3-docs.asf.alaska.edu/about/hyp3_basic/), [credit guidance](https://hyp3-docs.asf.alaska.edu/using/credits/), and [Sentinel-1 InSAR Product Guide](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/).
- ASF, [NISAR data availability](https://nisar-docs.asf.alaska.edu/availability-overview/) and [NISAR product overview](https://nisar-docs.asf.alaska.edu/products-overview/).
- MintPy, [documentation and supported input formats](https://mintpy.readthedocs.io/en/latest/).
- ESA, [SNAP toolbox](https://step.esa.int/main/toolboxes/snap/); ISCE, [ISCE2 repository](https://github.com/isce-framework/isce2).
- IMD, [district rainfall statistics](https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php); NASA/JPL, [GRACE data access](https://grace.jpl.nasa.gov/data/get-data/).

### Peer-reviewed Uttar Pradesh studies

- Awasthi, S. et al. (2022). “Analyzing urbanization induced groundwater stress and land deformation using time-series Sentinel-1 datasets applying PSInSAR approach.” *Science of the Total Environment*, 844, 157103. [DOI: 10.1016/j.scitotenv.2022.157103](https://doi.org/10.1016/j.scitotenv.2022.157103).
- (2022). “Multi-temporal analysis of groundwater depletion-induced land subsidence in Central Ganga Alluvial plain, Northern India.” [DOI: 10.1080/10106049.2022.2060322](https://doi.org/10.1080/10106049.2022.2060322).
- (2024). “Declining groundwater and its impacts along Ganga riverfronts using combined Sentinel-1, GRACE, water levels, and rainfall data.” *Science of the Total Environment*. [DOI: 10.1016/j.scitotenv.2024.170932](https://doi.org/10.1016/j.scitotenv.2024.170932).
- More, S. et al. (2025). “Groundwater over-extraction and associated land subsidence in Lucknow, Ganga Basin, India: Insights from space geodetic observations.” *Near Surface Geophysics*, 23(4), 420–433. [DOI: 10.1002/nsg.70020](https://doi.org/10.1002/nsg.70020).

### Official competition sources to verify before submission

- Conrad Challenge, [2026–27 Student Guide](https://conrad.spacecenter.org/wp-content/uploads/2026/08/2026-2027-Conrad-Challenge-Student-Guide-Official.pdf), [Innovation Stage](https://conrad.spacecenter.org/the-challenge/innovation-stage/), [Challenge overview](https://conrad.spacecenter.org/the-challenge/), [Water Challenge](https://conrad.spacecenter.org/water-challenge/), [Aerospace and Aviation](https://conrad.spacecenter.org/aerospace-and-aviation/), and [Rules and Regulations](https://conrad.spacecenter.org/the-challenge/rules-and-regulations/). Page paths and requirements may change; check the team's portal and current handbook.

## Follow-up checks for the team

1. Confirm the portal's cutoff and registered category; ask the organizer whether category changes are possible.
2. Have MF define at least three candidate boundaries and inspect station-level CGWB records, aquifer metadata, rainfall coverage, and access terms.
3. Have SM query same-track SLC acquisitions for those boundaries, then measure coherent-pixel coverage by season on real pairs.
4. Have AC decide whether local wells, district aggregates, or another reference can support a valid spatial/temporal comparison; document the scale mismatch.
5. Treat NISAR as a future/complementary source until enough validated repeat observations exist for the intended trend analysis.
6. Update this note when findings are confirmed with candidate-specific evidence; keep the assessment date and source versions visible.
