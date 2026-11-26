# Data Sources and Processing Options

**Status:** Operational and technical review as of 2026-11-26. Quotas, coverage, access paths, and product maturity can change. No satellite scene, NISAR product, or station-level groundwater series was acquired for this dossier.

## Selection principles

A source is not usable merely because it exists. For each candidate dataset, record:

- spatial coverage and resolution;
- temporal coverage, cadence, and gaps;
- access path and license/terms;
- provenance and version;
- units, datum, and quality flags;
- whether it is raw, intermediate, or analysis-ready;
- whether it can be redistributed or sent to a third-party processing service;
- the actual station, scene, or product identifiers used.

## Satellite radar

### Sentinel-1 (C-band)

**Use:** historical and current deformation time series; the most practical archive for a multi-year study in Uttar Pradesh.

**Verified facts:**

- Sentinel-1 is a C-band radar mission (about 5.6 cm wavelength).
- Sentinel-1C and Sentinel-1D reached their final orbital configuration on **June 24, 2026**, restoring the nominal **six-day interferometric repeat cycle**. Sentinel-1A operations were terminated on **June 29, 2026**.
- Interferometric processing requires **Single Look Complex (SLC)** data, not just GRD amplitude products.
- The archive includes periods with different constellation configurations. Do not assume a fixed repeat interval across the whole record; use the actual acquisition dates.

**Access:** [ASF Vertex](https://search.asf.alaska.edu/) and [Copernicus Data Space](https://dataspace.copernicus.eu/).

**Checks for a candidate:**

- relative orbit/track and pass direction (ascending/descending);
- polarization (VV, VH, or both);
- incidence angle and heading;
- frame/burst coverage over the polygon;
- acquisition dates and SLC availability;
- orbit files and precise orbit availability;
- whether the candidate has both ascending and descending coverage;
- whether the archive has gaps or mode changes.

**Main risk:** C-band coherence over cropland. Crop growth, irrigation, harvest, and surface moisture change the scattering between acquisitions. Archive presence does not prove coherence. Measure coherent-pixel coverage by season on real pairs before promising a multi-year agricultural series.

### NISAR (L-band and S-band)

**Use:** complementary L-band observations where vegetation limits C-band coherence; a future demonstration source; not a multi-year validated trend source as of this snapshot.

**Verified facts:**

- NISAR launched **July 30, 2025**.
- L-band wavelength: **24 cm**; global land coverage.
- S-band wavelength: **9.4 cm**; observations over India and selected calibration/validation sites.
- Exact repeat cycle: **12 days**; average sampling about every **6 days** with ascending and descending passes.
- Swath width: **240 km**.
- Spatial resolution: **3–10 m**, depending on mode.
- L-band products are available through **ASF**; S-band products (and L-band products from the same acquisitions) through ISRO's **Bhoonidhi** portal.
- Data policy: free and open access.
- Level-2 **GUNW** products provide geocoded unwrapped interferograms at **80 m** pixel spacing, with coherence, connected components, and ionospheric phase screen layers.

**Maturity and availability:**

| Release | Coverage/period | Status |
|---|---|---|
| BETA | Selected acquisitions from October 17, 2025 to January 20, 2026 | Pre-calibration; not fully calibrated. |
| PROVISIONAL | All L-band acquisitions from June 17, 2026 through part of October 23, 2026 | Calibrated, partially validated. |
| VALIDATED | All L-band acquisitions starting **October 21, 2026** | Fully calibrated and validated, released November 6, 2026. |
| Reprocessing | Pre-October 21, 2026 backlog | Planned for 2027; validated products will supersede earlier versions. |

**Main risks:**

- The validated record is only about five weeks long as of 2026-11-26. It cannot support a multi-year trend.
- Mixing BETA, PROVISIONAL, and VALIDATED products can introduce differences caused by processing changes, not landscape change.
- L-band is more affected by ionospheric phase than C-band; use the ionospheric layers and correction guidance.
- S-band access and coverage differ from L-band; verify the exact product and portal.
- Product maturity and reprocessing can change the archive; record the CRID/version.

### OPERA DISP-S1 (ruled out for Uttar Pradesh)

**Verified facts:**

- OPERA DISP-S1 is a Level-3 Sentinel-1 surface-displacement product at **30 m** posting.
- Its documented spatial coverage is **North America**: the United States, U.S. territories within 200 km of the U.S. border, Canada, and mainland countries from the southern U.S. border to Panama.
- Temporal extent: 2016-07-01 to present.

**Implication:** OPERA DISP-S1 is not a source for Uttar Pradesh. It should not appear in a UP data manifest. A NISAR-based DISP-NI product exists in the OPERA suite, but its coverage and maturity for India must be checked separately; do not assume it replaces the Sentinel-1 work.

## Groundwater, rainfall, and storage context

### CGWB and India-WRIS

- CGWB yearbooks provide district-level water-level tables and well-level annexures.
- The 2022–23 UP yearbook describes 1,007 manual monitoring wells measured four times a year, with a few participatory records in other months.
- India-WRIS is a national water-resources portal that can be used for data discovery; confirm station-level series, export format, provenance, and terms. The portal did not respond on 2026-11-26, so this is a potential source, not a verified one.
- Record station coordinates, well type, screen depth, aquifer, datum, measurement method, quality flag, and missingness.
- Do not treat a block category as a station measurement or a deformation observation.

### IMD rainfall

- IMD district rainfall statistics provide seasonal and annual context. They were not re-fetched and their terms were not reviewed on 2026-11-26.
- District aggregates may not match the candidate block or well locations.
- If using gridded rainfall, record the product, resolution, version, and aggregation method.
- Rainfall is a confounder and a regressor, not a substitute for groundwater data.

### GRACE / GRACE-FO

- GRACE provides coarse terrestrial-water-storage and groundwater-storage context.
- Its footprint is much larger than a block or well; it cannot validate a local InSAR pixel.
- Use it as regional context alongside local groundwater and rainfall records, not as a local reference label.

## Processing options

### ASF HyP3

**What it is:** on-demand Sentinel-1 InSAR and RTC processing through ASF.

**Verified credit facts (HyP3 Basic):**

- **8,000 free credits per user per month.**
- InSAR at **80 m** pixel spacing: **10 credits** per product, up to **800 products/month**.
- InSAR at **40 m** pixel spacing: **15 credits** per product, up to **533 products/month**.
- HyP3+ purchased-credit cost: **$0.50** per 80 m InSAR product; **$0.75** per 40 m product.
- Output download URLs are time-limited; the API example shows an expiration timestamp. Download promptly and check the current retention policy.

**What it produces:** individual interferometric products (pairs), not a finished time series. A stack still needs a time-series step such as MintPy.

**Illustrative credit arithmetic:**

- A three-year stack at a 12-day cadence has up to about 90 acquisitions; a sequential pair network is about 89 pairs.
- A redundant network with two connections per scene is about 180 pairs.
- Both fit within one month's free 800-job allocation at 80 m.
- Credit budget is therefore unlikely to be the first constraint. Coherence, download volume, storage, and quality review are more likely constraints.

### MintPy

- Open-source InSAR time-series analysis.
- Documented inputs include HyP3, ISCE, ARIA, GMTSAR, SNAP, GAMMA, and other processor formats.
- It analyzes a processed interferogram stack; it does not select acquisitions, fix coherence, or remove the need to understand upstream processing.
- Record the MintPy version, configuration, reference point, network, and corrections.

### ISCE2

- Open-source InSAR processing framework with Sentinel-1 support.
- Full control over processing, but installation, compute, and expertise requirements are higher.
- Use it only if HyP3/MintPy cannot meet a documented need.

### ESA SNAP

- Desktop toolbox for Sentinel data and preprocessing.
- Useful for inspection, subsetting, and some interferometric steps.
- Not a complete, documented time-series workflow by itself.

### StaMPS

- PS/DS time-series package used in research workflows.
- Requires careful parameter selection and quality control.
- Not a turnkey replacement for a reproducible pipeline.

### LiCSBAS / LiCSBAS2 / COMET LiCSBAS

- LiCSBAS analyzes LiCSAR unwrapped interferograms and coherence products.
- The original LiCSBAS repository is unmaintained; its `step01` download broke after the June 2024 COMET-LiCS portal change.
- Use **LiCSBAS2** or the **COMET-maintained LiCSBAS** fork.
- Check whether COMET-LiCSAR frames cover the candidate; do not assume global coverage or current products.

## Recommended feasibility sequence

1. **Define candidate polygons.** Use the SJ rubric and MF's block/station evidence; do not start with a scene.
2. **Query the Sentinel-1 archive.** Count same-track, same-pass SLCs over each polygon; record dates, polarization, and incidence angle.
3. **Process a small pair set with HyP3.** Choose pairs across seasons (pre-monsoon, monsoon, post-monsoon) and inspect coherence.
4. **Measure coherent-pixel coverage.** Report the percentage of the polygon with usable pixels by season and the gaps.
5. **Decide:** if coherence is adequate, build a stack and run MintPy; if not, document a no-go or test an urban/peri-urban benchmark.
6. **Assemble ground reference.** Extract station-level CGWB records and rainfall; define spatial and temporal matching rules.
7. **Compare, don't claim causation.** Report coverage, sample size, missingness, uncertainty, and alternative explanations.
8. **Consider NISAR later.** Use validated L-band data as a complement or demonstration once enough repeats exist; do not mix maturities without care.

## Access and licensing notes

- Sentinel-1: Copernicus open data; check the current terms and attribution.
- NISAR: free and open; L-band via ASF, S-band via ISRO Bhoonidhi; check the product maturity and citation.
- CGWB/India-WRIS: verify station-level access, redistribution, and terms. Do not assume that a public PDF implies a bulk-download license.
- IMD: verify terms for derived products and redistribution.
- GRACE: check the current provider terms and citation.
- Do not send restricted or personal data to a third-party processing service without checking the terms.

## Sources

- ESA, [Sentinel-1C/1D final orbital configuration achieved](https://sentinels.copernicus.eu/-/sentinel-1c/1d-final-orbital-configuration-achieved), 24 June 2026.
- NASA, [NISAR Mission Overview](https://science.nasa.gov/mission/nisar/mission-overview/), accessed 2026-11-26.
- ASF, [NISAR data availability](https://nisar-docs.asf.alaska.edu/availability-overview/), accessed 2026-11-26.
- ASF, [NISAR data products](https://nisar-docs.asf.alaska.edu/products-overview/), accessed 2026-11-26.
- ASF, [HyP3 credits](https://hyp3-docs.asf.alaska.edu/using/credits/), accessed 2026-11-26.
- ASF, [Downloading HyP3 products](https://hyp3-docs.asf.alaska.edu/using/downloading/), accessed 2026-11-26.
- NASA Earthdata, [OPERA DISP-S1 v1](https://www.earthdata.nasa.gov/data/catalog/asf-opera-l3-disp-s1-v1-1), accessed 2026-11-26.
- MintPy, [documentation](https://mintpy.readthedocs.io/en/latest/), accessed 2026-11-26.
- ISCE2, [repository](https://github.com/isce-framework/isce2), accessed 2026-11-26.
- ESA, [SNAP toolbox](https://step.esa.int/main/toolboxes/snap/), accessed 2026-11-26.
- StaMPS, [repository](https://github.com/dbekaert/StaMPS), accessed 2026-11-26.
- LiCSBAS, [original repository](https://github.com/yumorishita/LiCSBAS), [LiCSBAS2](https://github.com/yumorishita/LiCSBAS2), and [COMET LiCSBAS](https://github.com/comet-licsar/LiCSBAS), accessed 2026-11-26.
- CGWB, [Ground Water Level Monitoring](https://cgwb.gov.in/en/ground-water-level-monitoring), accessed 2026-11-26.
- India-WRIS, <https://indiawris.gov.in/>, access attempted 2026-11-26; unreachable at check time.
- IMD, [district rainfall statistics](https://mausam.imd.gov.in/imd_latest/contents/rainfall_statistics_3.php), cited for context; not re-fetched on 2026-11-26.
- NASA/JPL, [GRACE data access](https://grace.jpl.nasa.gov/data/get-data/), accessed 2026-11-26.

See [`source-register.md`](source-register.md) for the consolidated register.
