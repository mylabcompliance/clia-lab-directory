# CLIA Lab Directory (cleaned CMS data)

Every active CLIA-certified laboratory in the US (299,345 labs as of July 1, 2026), cleaned from the CMS **Provider of Services File: Clinical Laboratories** into readable per-state CSV files.

The raw CMS file has 680,000+ rows (including closed labs) and coded fields. This repo keeps active labs only and decodes certificate types, facility types and accreditors.

Maintained by [Sound Lab Consultants](https://soundlabconsult.com). For what each state adds on top of CLIA, see the companion dataset [clia-state-requirements](https://github.com/mylabcompliance/clia-state-requirements).

## Files

- `data/by-state/XX.csv.gz`: active labs per state (open directly in Excel, pandas or R)
- `data/summary-by-state.csv`: lab counts by state and certificate type
- `data/summary-by-facility-type.csv`: lab counts by facility type and certificate type
- `scripts/build.py`: rebuilds everything from a new CMS quarterly file

## Largest states

| State | Active labs | Waiver | PPM | Compliance / Accreditation / Registration |
|---|---|---|---|---|
| TX | 29,163 | 24,005 | 1,648 | 3,510 |
| FL | 25,710 | 22,348 | 708 | 2,654 |
| CA | 22,905 | 18,275 | 1,909 | 2,721 |
| NY | 12,310 | 10,034 | 802 | 1,474 |
| OH | 11,985 | 10,011 | 1,069 | 905 |
| GA | 11,326 | 9,433 | 832 | 1,061 |
| NC | 11,096 | 8,672 | 1,154 | 1,270 |
| IL | 10,331 | 8,554 | 855 | 922 |
| PA | 9,765 | 7,773 | 1,143 | 849 |
| MI | 8,787 | 7,237 | 825 | 725 |

Nationally, about 4 in 5 active labs hold a Certificate of Waiver; physician offices are the largest single facility type.

## Columns

`clia_number`, `lab_name`, `address`, `city`, `state`, `zip`, `certificate` (Waiver, PPM, Registration, Compliance, Accreditation), `facility_type`, `accreditation` (CAP, COLA, TJC, AABB, A2LA, AOA, ASHI), `certificate_effective`, `certificate_expires`, `clia_exempt_lab`.

Phone numbers are left out of this repo on purpose.

## Rebuild with the newest quarter

```bash
pip install pandas
python scripts/build.py Clia_Data.Q3_2026.csv data
```

Download the newest CSV from [data.cms.gov: Provider of Services File - Clinical Laboratories](https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-clinical-laboratories). Code values come from the CMS POS CLIA record layout.

## License

Source data is a US government work (public domain). The scripts are MIT licensed. Please credit "CMS POS File, cleaned by Sound Lab Consultants" if you republish the cleaned files.

## Not an official source

To confirm a lab's current certificate, use CMS's [QCOR CLIA lookup](https://qcor.cms.gov/). Sound Lab Consultants is an independent consulting firm, not affiliated with CMS. Opening a new lab or preparing for a survey? [soundlabconsult.com](https://soundlabconsult.com) · (602) 874-1311.
