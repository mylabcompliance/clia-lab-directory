---
license: mit
pretty_name: US CLIA Laboratory Directory (CMS, 2026)
language: [en]
tags: [healthcare, clinical-laboratory, clia, cms, public-health, medical-devices, diagnostics]
size_categories: [100K<n<1M]
task_categories: [tabular-classification]
configs:
  - config_name: labs
    data_files: clia_labs_us_2026-07.csv.gz
---

# US CLIA Laboratory Directory (2026)

All **299,345 active CLIA-certified laboratories** in the United States as of July 1, 2026, cleaned from the CMS *Provider of Services File: Clinical Laboratories*: certificate type, facility type, accreditor and certificate dates for every lab, decoded into readable values. A companion file lists **FDA CLIA test categorizations from the last 24 months** (1,148 test systems).

Maintained by [Sound Lab Consultants](https://soundlabconsult.com/guides/), CLIA consultants to labs, clinics and emergency centers nationwide.

## Files

| File | Rows | Description |
|---|---|---|
| `clia_labs_us_2026-07.csv.gz` | 299,345 | One row per active lab |
| `fda_clia_categorizations_recent.json` | 1,148 test systems | FDA CLIA categorizations (waived / moderate / high) with analytes, dates and FDA document numbers. Refreshed twice weekly in [lab-qc-tools](https://github.com/mylabcompliance/lab-qc-tools) |

## Columns (labs)

`clia_number`, `lab_name`, `address`, `city`, `state`, `zip`, `certificate` (Waiver, PPM, Registration, Compliance, Accreditation), `facility_type`, `accreditation` (CAP, COLA, TJC, AABB, A2LA, AOA, ASHI), `certificate_effective`, `certificate_expires`, `clia_exempt_lab`. Phone numbers are intentionally excluded.

## Quick facts

- About 4 in 5 active labs hold a Certificate of Waiver; physician offices are the largest facility type.
- Largest states: Texas (29,163), Florida (25,710), California (22,905), New York (12,310), Ohio (11,985).

## Uses

Market sizing for diagnostics, public-health research on testing access, mapping point-of-care testing, and checking a lab's certificate status. For plain-English guidance on what each certificate requires, see the [Sound Lab Consultants lab guides](https://soundlabconsult.com/guides/) and the [state-by-state CLIA requirements dataset](https://github.com/mylabcompliance/clia-state-requirements).

## Source and license

Source data: CMS Provider of Services File: Clinical Laboratories (public); FDA CLIA database download (public). Cleaning code: [github.com/mylabcompliance/clia-lab-directory](https://github.com/mylabcompliance/clia-lab-directory). This compilation is MIT licensed.

## Citation

Sound Lab Consultants (2026). *US CLIA Laboratory Directory (2026)*. https://github.com/mylabcompliance/clia-lab-directory
