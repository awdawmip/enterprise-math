#!/usr/bin/env python3
"""PREFIX-901: exact second panel census and two-panel overlap union.

Compile the existing verified generic PREFIX-900 classifier:
g++ -O3 -std=c++17 PREFIX900_R6_64ROW_FF_COMPLETE.cpp -o /tmp/ff900
Then: python3 PREFIX901_R6_SECOND_PANEL_CHECK.py /tmp/ff900 > PREFIX901_R6_SECOND_PANEL_FULL.json
All operations use arbitrary-precision exact integers.
"""
import json, math, subprocess, sys
from pathlib import Path

N=1<<32
T=33*N
Q=range(262145,524288,2)
PANEL0=[510001+194*j for j in range(64)]
PANEL1=[510003+194*j for j in range(64)]
S={262147,280001,300001,320003,340007,360007,380003,
   400009,420001,440003,460001,480007,500383,510007,520001,524285}
U=S|{400011+2*j for j in range(256)}|{480011+2*j for j in range(256)}
U|={q for q in Q if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0 for h in range(1,32))}
assert len(U)==552
assert len(set(PANEL0)|set(PANEL1))==128
assert all(a not in U for a in PANEL0+PANEL1)

def prior(a,b):
    return (a*b<T or a in U or b in U
            or (a//math.gcd(a,b))*b<N
            or 33*((N+a-1)//a)>b
            or 33*((N+b-1)//b)>a)

def check_legal(a,b,w):
    x,y,i,j=(w[t] for t in ("x","y","i","j"))
    assert 0<=x<N and 0<=y<N and 0<=i<32 and 0<=j<32
    assert x!=y or i!=j
    assert x%a==y%a and (x^(1<<i))%b==(y^(1<<j))%b

def run(exe):
    rows=[]
    for a in PANEL1:
        r=json.loads(subprocess.check_output([exe,str(a)],text=True))
        assert r["q1"]==a and r["q_count"]==131072
        names=("old_four_family","zf_new","anchored_ff_new","general_ff_new","unresolved")
        assert sum(r[k] for k in names)==131072
        for w in r["general_witnesses"]+r["anchored_examples"]:
            check_legal(a,w["q2"],w)
        rows.append(r)
    totals={key:sum(r[key] for r in rows) for key in names}
    assert totals=={"old_four_family":506797,"zf_new":3465112,
                    "anchored_ff_new":4416184,"general_ff_new":515,"unresolved":0}
    panel=PANEL0+PANEL1
    oldpanel=sum(prior(a,b) for a in PANEL1 for b in PANEL1)
    oldcross=sum(prior(a,b) for a in PANEL0 for b in PANEL1)
    oldfull=sum(prior(a,b) for a in panel for b in panel)
    assert (oldpanel,oldcross,oldfull)==(64,27,182)
    priorE=7567620214
    oldRowE=507393+totals["old_four_family"]
    totalnew=2*(len(panel)*len(Q)-oldRowE)-(len(panel)**2-oldfull)
    assert totalnew==31509850
    union=priorE+totalnew
    assert union==7599130064
    return {
        "schema":"PREFIX901_R6_COMPLETE_128_ROW_CERT_V1",
        "science_pin":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "domain":{"p":32,"min":262145,"max":524287,"step":2,"size":131072},
        "panel0":"510001+194*j for j=0..63",
        "panel1":"510003+194*j for j=0..63",
        "panel1_row_pairs":len(PANEL1)*len(Q),
        "second_panel_totals":totals,
        "old_E_in_second_64_square":oldpanel,
        "old_E_in_first_to_second_cross":oldcross,
        "old_E_in_128_square":oldfull,
        "new_symmetric_128_panel_outside_old_E":totalnew,
        "net_new_beyond_PREFIX900":union-7583378612,
        "certified_total":union,
        "not_yet_certified_in_this_union":len(Q)**2-union,
        "full_general_witnesses":sum(len(r["general_witnesses"]) for r in rows),
        "rows":rows,
        "review":"NOT_INDEPENDENTLY_REVIEWED"
    }

if __name__=="__main__":
    if len(sys.argv)!=2:raise SystemExit("pass compiled PREFIX900 executable")
    print(json.dumps(run(sys.argv[1]),indent=2))
