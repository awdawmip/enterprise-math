#!/usr/bin/env python3
"""PREFIX-922: generate D, run PREFIX-921 C++ row binary, independently check every named witness."""
from collections import Counter
from hashlib import sha256
import json, subprocess, sys

N=1<<32; FIRST=262145; LAST=524287

def selection():
    chosen=[]
    for b in range(FIRST,LAST+1,2):
        r=1;early=False;late=False
        for d in range(1,53):
            r=(r*2)%b
            if d<=31 and r in (1,b-1):
                early=True;break
            if 32<=d<=52 and r in (1,b-1):late=True
        if late and not early:chosen.append(b)
    assert len(chosen)==91
    return chosen

def audit_one(executable,b):
    p=subprocess.Popen([executable,str(b)],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    expected=FIRST;counts=Counter();digest=sha256();summary=None
    for raw in p.stdout:
        digest.update(raw)
        s=raw.decode("ascii").strip()
        if s.startswith("W "):
            a,bb,t,x,y,i,j=map(int,s[2:].split(","))
            assert a==expected and bb==b and 0<=x<y<N and 1<=t<=3
            assert ((i,j)==(-1,-1)) if t==1 else (0<=i<32 and j==-1) if t==2 else (0<=i<32 and 0<=j<32)
            u=x if i<0 else x^(1<<i)
            v=y if j<0 else y^(1<<j)
            assert (y-x)%a==0 and (v-u)%b==0
            counts[t]+=1; expected+=2
        elif s.startswith("NO_DISTINCT_START_COLLISION "):
            raise AssertionError("Uncertified gap-free row: "+s)
        elif s.startswith("TOTAL "):summary=s
        else:raise AssertionError("Invalid generator line: "+s)
    error=p.stderr.read().decode("utf-8","replace")
    assert p.wait()==0,error
    assert expected==LAST+2 and sum(counts.values())==131072
    assert "no_distinct_start=0" in summary
    return {"b":b,"zero_zero":counts[1],"zero_flip":counts[2],
            "two_flip":counts[3],"sha256":digest.hexdigest()}

if __name__=="__main__":
    exe=sys.argv[1] if len(sys.argv)>1 else "./prefix921w"
    rows=[audit_one(exe,b) for b in selection()]
    sums=[sum(row[k] for row in rows) for k in ("zero_zero","zero_flip","two_flip")]
    assert sums==[437682,5381582,6108288]
    out={"schema":"PREFIX922_R6_W0_EXACT_V1","rows":rows,"selected_b_count":91,
    "full_row_total":91*131072,"invalid_witnesses":0,"first_type_totals":sums}
    print(json.dumps(out,indent=2))
