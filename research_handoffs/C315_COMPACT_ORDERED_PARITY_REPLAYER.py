#!/usr/bin/env python3
"""C315: exact ordered-node pole-parity audit. Requires frozen C314/C301 input folder.
No C298/C300/C305 routines, only C275 source parameters and C288 frozen paths.
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from math import gcd, lcm
from pathlib import Path
import json, os, sys

ROOT=Path(__file__).resolve().parent
UP=ROOT/"EM_C301_EXACT_PORTABLE"
if not UP.is_dir():
    raise FileNotFoundError("Place frozen C314 EM_C301_EXACT_PORTABLE directory beside script")
os.chdir(UP)  # frozen C288 uses a relative source JSON path
sys.path.insert(0,str(UP))
import C275_STANDALONE_EXACT_REPLAY as src
import C288_ISOLATING_BOXES_EXACT as path_source

def primitive_linear(a,b):
    if b==0:
        return None
    D=lcm(a.denominator,b.denominator)
    x,y=int(a*D),int(b*D)
    G=gcd(x,y)
    return (x//G,y//G) if y>0 else (-x//G,-y//G)

def audit():
    paths,_=path_source.build_paths()
    records=json.loads((UP/"C293_125_REFINED_BRACKETS.json").read_text())["records"]
    assert len(paths)==len(records)==125
    W,B=src.floor_fixed_masses()
    assert len(B)==75 and all(0<W[j]<B[j] for j in src.J)
    assert all(B[j].denominator>1 for j in src.J)
    totals=Counter()
    rows=[]
    for i,p in enumerate(paths):
        assert records[i][0]==i
        lo=F(int(records[i][1]),2**24)
        hi=lo+F(1,2**24)
        mid=(lo+hi)/2
        assert all(p["w"][k]+p["d"][k]*mid < p["w"][k+1]+p["d"][k+1]*mid for k in range(3))
        factors=defaultdict(list)
        for j in src.J:
            for k in range(4):
                q=primitive_linear(p["w"][k]-src.U[j],p["d"][k])
                if q is None:
                    assert p["w"][k]!=src.U[j]
                    totals["fixed_moving_constant"]+=1
                else:
                    factors[q].append(("fixed",j,k))
        for k in range(4):
            for m in range(k+1,4):
                q=primitive_linear(p["w"][k]-p["w"][m],p["d"][k]-p["d"][m])
                assert q is not None
                factors[q].append(("moving",k,m))
        assert all(len(v)==1 for v in factors.values())
        c=Counter()
        for (a,b),values in factors.items():
            t=F(-a,b)
            assert all(src.Z!=p["w"][l]+p["d"][l]*t for l in range(4))
            kind,j,k=values[0]
            if kind=="fixed":
                assert (2-src.U[j]**2)*(3-src.U[j]**2)!=0
                sigma=(-1)**(abs(j-src.I[k])-1)
                assert W[j]+sigma*B[j]!=0
                c["fixed_survive"]+=1
                c["fixed_plus" if sigma>0 else "fixed_minus"]+=1
            else:
                assert p["w"][j]+p["d"][j]*t==p["w"][k]+p["d"][k]*t
                x=p["w"][j]+p["d"][j]*t
                assert (2-x*x)*(3-x*x)!=0
                c["moving_cancel" if (src.I[k]-src.I[j]-1)%2 else "moving_survive"]+=1
            totals["distinct_linear_collisions"]+=1
        assert c["moving_cancel"]==2 and c["moving_survive"]==4
        assert c["fixed_survive"]==300-75*sum(d==0 for d in p["d"])
        dynamic=0
        for k in range(4):
            if p["d"][k]==0: continue
            dynamic+=1
            for m in range(4):
                if m==k:continue
                assert (p["w"][m],p["d"][m]) not in (
                    (p["w"][k],p["d"][k]),(-p["w"][k],-p["d"][k]))
                if p["d"][m]==0: assert p["w"][m]!=src.Z
        c["dynamic_nodes"]=dynamic
        c["reduced_denominator_degree"]=c["fixed_survive"]+c["moving_survive"]+12*dynamic
        assert c["reduced_denominator_degree"]==(265 if i==28 else 352)
        totals.update(c)
        rows.append({"path":i,**dict(c)})
    assert totals["fixed_survive"]==37425
    assert totals["moving_survive"]==500
    assert totals["moving_cancel"]==250
    assert totals["distinct_linear_collisions"]==38175
    assert totals["dynamic_nodes"]==499
    assert totals["reduced_denominator_degree"]==43913
    result={"schema":"C315_FROZEN_PARITY_AUDIT_V1",
            "input":"C275/C284/C288/C293 frozen exact rational source",
            "claim_scope":"conditional on frozen 79-branch scalar C275 model, not original C195 text nor native BRC",
            "fixed_B_nonintegral":75,
            "totals":dict(totals),"rows":rows}
    (ROOT/"C315_RECOMPUTED_125_CERT.json").write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    print("C315_EXACT_PARITY_FULL_DENOMINATOR_PASS",len(rows),dict(totals))

if __name__=="__main__":
    audit()
