"""Validate synthetic enterprise GRC CSV data, not actual organization compliance."""
from __future__ import annotations
import csv
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def records(path):
    with (ROOT/path).open(encoding='utf-8-sig',newline='') as stream:
        return list(csv.DictReader(stream))
def check():
    risks=records("02-risk-register/Enterprise-Risk-Register.csv")
    nist=records("03-nist-csf-gap-assessment/NIST-CSF-Gap-Scorecard.csv")
    vendors=records("05-vendor-risk-management/Vendor-Risk-Register.csv")
    assert risks and nist and vendors
    ids=[r["Risk ID"] for r in risks]
    assert len(ids)==len(set(ids)),"Duplicate risk ID"
    for r in risks:
        likelihood=int(r["Likelihood"]);impact=int(r["Impact"])
        inherent=int(r["Inherent Risk"]);residual=int(r["Residual Risk"])
        assert 1<=likelihood<=5 and 1<=impact<=5
        assert inherent==likelihood*impact,(r["Risk ID"],"inherent risk mismatch")
        assert 0<=residual<=inherent,(r["Risk ID"],"residual exceeds inherent")
        if r["Due Date"]!="N/A": date.fromisoformat(r["Due Date"])
    cats=[r["Subcategory"] for r in nist]
    assert len(cats)==len(set(cats)),"Duplicate CSF subcategory"
    for r in nist:
        current=int(r["Current Maturity"]); target=int(r["Target Maturity"])
        assert 1<=current<=4 and 1<=target<=4
        assert int(r["Gap"])==target-current,(r["Subcategory"],"incorrect gap")
    for v in vendors:
        score,total=v["Risk Score"].split("/")
        assert int(total)==100 and 0<=int(score)<=100,v["Vendor"]
        date.fromisoformat(v["Assessment Date"]);date.fromisoformat(v["Next Review"])
    return len(risks),len(nist),len(vendors)
if __name__=="__main__":
    counts=check()
    print("PASS: synthetic risk, CSF 1.1 scorecard, and vendor records:",counts)
