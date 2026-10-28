#!/usr/bin/env python3
"""EC49S exact rational verifier for the P/Q-U-Z two-purchase model."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

W=range(3); Z=range(3); U=(0,1); sigma=(1,0,-1)
P={(w,z):F(1,6) if w==z else F(1,12) for w in W for z in Z}
Q={(w,z):F(1,9) for w in W for z in Z}
D={(w,z):P[w,z]-Q[w,z] for w in W for z in Z}
cost={'A':1,'B':2}
codes=tuple((a,d) for a in ('A','B') for d in (0,1))
actions=(None,)+codes
pos=lambda x:max(F(0),x)

def t(w,u,eta):
    return F(1,2)+(eta if u else -eta)*sigma[w]

def group(G,a,eta):
    if not G:return F(0)
    v=-F(len(G)*cost[a],72)
    for u in U:
        signed=[sum((D[w,z]*t(w,u,eta) for w in G),F(0)) for z in Z]
        gain=sum((pos(x) for x in signed),F(0))
        second=sum((t(w,u,eta) for w in G),F(0))/72
        v+=pos(gain-second)
    return v

def checks(eta):
    assert F(0)<=eta<F(1,2)
    for src in (P,Q):
        joint={(w,u,z):src[w,z]*t(w,u,eta) for w in W for u in U for z in Z}
        assert len(joint)==18 and all(x>0 for x in joint.values())
        assert sum(joint.values(),F(0))==1
        for w in W:
            assert sum(src[w,z] for z in Z)==F(1,3)
            for z in Z:
                assert sum(joint[w,u,z] for u in U)==src[w,z]
    for w in W:
        assert group((w,),'A',eta)==F(1,36)
        assert group((w,),'B',eta)==F(1,72)
    for G in ((0,1),(1,2)):
        a=pos(2*eta-F(1,2))/36
        assert group(G,'A',eta)==a
        assert group(G,'B',eta)==a-F(1,36)
    a=pos(6*eta-1)/36
    assert group((0,2),'A',eta)==a
    assert group((0,2),'B',eta)==a-F(1,36)
    a=-F(1,24)+2*pos(eta/12-F(1,48))
    assert group((0,1,2),'A',eta)==a and a<0
    assert group((0,1,2),'B',eta)==a-F(1,24)
    scores=[]
    for m in product(actions,repeat=3):
        score=sum((group(tuple(w for w in W if m[w]==code),code[0],eta)
                   for code in codes),F(0))
        scores.append(score)
    maximum=max(scores)
    assert len(scores)==125
    assert maximum==max(F(5,72),eta/6)
    assert F(1,12)-maximum>0
    # Explicit 2-A witness: W0,2 share code A0; W1 uses A1.
    def accepted(w,u,z):
        return (z==(0 if u else 2)) if w in (0,2) else (z==1)
    alpha=sum((P[w,z]*t(w,u,eta) for w in W for u in U for z in Z
               if accepted(w,u,z)),F(0))
    beta=sum((Q[w,z]*t(w,u,eta) for w in W for u in U for z in Z
              if accepted(w,u,z)),F(0))
    assert alpha==F(5,12)+eta/6 and beta==F(1,3)
    assert alpha-beta-F(4,48)==eta/6
    return maximum,sum(x==maximum for x in scores)

parameters=sorted(set([F(k,80) for k in range(40)]+
                      [F(0),F(1,200),F(1,6),F(1,4),F(1,3),F(5,12),F(49,100)]))
rows=[]
for eta in parameters:
    val,count=checks(eta)
    rows.append({'eta':str(eta),'compressed_max':str(val),
                 'gap':str(F(1,12)-val),'optimizing_maps':count})
assert len(parameters)==45
assert checks(F(1,200))[0]==F(5,72)
report={'status':'PASS','arithmetic':'stdlib fractions.Fraction',
        'eta_rational_points':len(parameters),
        'deterministic_initial_maps_per_eta':125,
        'total_exact_initial_map_evaluations':125*len(parameters),
        'full_max_all_real_eta':'1/12',
        'compressed_max_all_real_eta':'max(5/72, eta/6)',
        'phase_transition':'5/12',
        'exact_gap_at_eta_1_over_200':'1/72',
        'universal_proof_location':'PROOF.md (algebra + multi-affine extremal argument)',
        'rows':rows}
Path(__file__).with_name('EXACT_REPORT.json').write_text(
    json.dumps(report,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
