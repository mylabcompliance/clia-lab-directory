"""Clean the CMS Provider of Services (POS) File - Clinical Laboratories into an
analysis-ready directory of active CLIA labs. Usage: python build.py <cms_csv> <out_dir>"""
import sys, os, pandas as pd
CERT = {"1":"Compliance","2":"Waiver","3":"Accreditation","4":"PPM","9":"Registration"}
FAC = {"01":"Ambulance","02":"Ambulatory Surgery Center","03":"Ancillary Test Site","04":"Assisted Living Facility","05":"Blood Bank",
"06":"Community Clinic","07":"Comprehensive Outpatient Rehab","08":"ESRD Dialysis","09":"FQHC","10":"Health Fair","11":"HMO",
"12":"Home Health Agency","13":"Hospice","14":"Hospital","15":"Independent","16":"Industrial","17":"Insurance","18":"ICF/IID",
"19":"Mobile Lab","20":"Pharmacy","21":"Physician Office","22":"Other Practitioner","23":"Prison","24":"Public Health Laboratory",
"25":"Rural Health Clinic","26":"School/Student Health","27":"Skilled Nursing Facility","28":"Tissue Bank","29":"Other"}
ACC = {"CAP_ACRDTD_CD":"CAP","COLA_ACRDTD_CD":"COLA","JCAHO_ACRDTD_CD":"TJC","AABB_ACRDTD_CD":"AABB","A2LA_ACRDTD_CD":"A2LA","AOA_ACRDTD_CD":"AOA","ASHI_ACRDTD_CD":"ASHI"}
COLS = ["PRVDR_NUM","FAC_NAME","ST_ADR","CITY_NAME","STATE_CD","ZIP_CD","PHNE_NUM","PGM_TRMNTN_CD","TRMNTN_EXPRTN_DT",
        "CRTFCT_TYPE_CD","GNRL_FAC_TYPE_CD","CRTFCT_EFCTV_DT","CURRENT_CLIA_LAB_CLSFCTN_CD"] + list(ACC)
def load(path):
    df = pd.read_csv(path, dtype=str, usecols=COLS).fillna("")
    df = df[df.PGM_TRMNTN_CD == "00"].copy()                      # active labs only
    out = pd.DataFrame({
        "clia_number": df.PRVDR_NUM, "lab_name": df.FAC_NAME.str.strip(), "address": df.ST_ADR.str.strip(),
        "city": df.CITY_NAME.str.title(), "state": df.STATE_CD, "zip": df.ZIP_CD.str[:5],
        "phone": df.PHNE_NUM,
        "certificate": df.CRTFCT_TYPE_CD.map(CERT).fillna(""),
        "facility_type": df.GNRL_FAC_TYPE_CD.map(FAC).fillna(""),
        "accreditation": df[list(ACC)].apply(lambda r: ";".join(v for k,v in ACC.items() if r[k].strip()), axis=1),
        "certificate_effective": pd.to_datetime(df.CRTFCT_EFCTV_DT, format="%Y%m%d", errors="coerce").dt.date,
        "certificate_expires": pd.to_datetime(df.TRMNTN_EXPRTN_DT, format="%Y%m%d", errors="coerce").dt.date,
        "clia_exempt_lab": df.CURRENT_CLIA_LAB_CLSFCTN_CD.eq("05"),
    })
    return out
if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    labs = load(src)
    os.makedirs(dst+"/by-state", exist_ok=True)
    public = labs.drop(columns=["phone"])
    for st, g in public.groupby("state"):
        g.sort_values(["city","lab_name"]).to_csv(f"{dst}/by-state/{st}.csv.gz", index=False, compression="gzip")
    summ = pd.crosstab(labs.state, labs.certificate); summ["total"] = summ.sum(axis=1)
    summ.sort_values("total", ascending=False).to_csv(f"{dst}/summary-by-state.csv")
    pd.crosstab(labs.facility_type, labs.certificate).assign(total=lambda x: x.sum(axis=1)).sort_values("total", ascending=False).to_csv(f"{dst}/summary-by-facility-type.csv")
    print(len(labs), "active labs")
