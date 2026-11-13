#!/usr/bin/env python3
"""PREFIX-598-R2: exact native X6 BRC positive tail image-cone certificate.
All 48 native phases, 96 bit ports, 576 typed edges retained.
Python stdlib-only, integer and exact rational arithmetic.
"""
from fractions import Fraction as F
from random import Random
from pathlib import Path
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STARS[a]
        for t in (-1,1) for p in near(a,t*k))
IX={v:i for i,v in enumerate(P)}
def nxt(i):
    a,p,c=P[i]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(IX[v] for v in
                 [(a,c,k) for k in near(a,c) if k!=p]
                +[(b,c,k) for k in near(b,c)])
N=tuple(nxt(i) for i in range(48))
G=IX[(0,1,-3)]
R=tuple(IX[(a,c,p)] for a,p,c in P)
AXIS=[abs(c)-1 for a,p,c in P]
S=[[int(j in N[i]) for j in range(48)] for i in range(48)]
GROUP={s:tuple(i for i,(_,_,c) in enumerate(P) if c==s)
       for s in range(-6,7) if s}
assert len(P)==48 and G==4 and len(GROUP)==12
assert all(len(k)==4 for k in GROUP.values())
assert all(R[R[i]]==i for i in range(48))
assert all(S[i][R[j]]==int(i!=j and P[i][2]==P[j][2])
           for i in range(48) for j in range(48))
DROW=[1 if i==G else 2 for i in range(48)]

def q_step(u,x,z):
    out=[]
    for i in range(48):
        d=F(1) if i==G else F(2)
        out.append(x[AXIS[i]]*d*sum(
            F(u[j])*(F(z+3,2) if j==G else F(1))
            for j in N[i]))
    return out

def local_inverse(v,x,z):
    b=[F(v[i],DROW[i]*x[AXIS[i]]) for i in range(48)]
    lam=[F(0)]*48
    for ids in GROUP.values():
        total=sum(b[i] for i in ids)
        for i in ids:
            lam[i]=total/3-b[i]
    return [lam[R[j]]/(F(z+3,2) if j==G else F(1))
            for j in range(48)]

def facets(v):
    w=[F(v[i],DROW[i]) for i in range(48)]
    return [sum(w[j] for j in GROUP[P[i][2]])-3*w[i]
            for i in range(48)]

rng=Random(5981108)
parameters=[([1]*6,0),([1]*6,1),([2,3,5,7,11,13],5),
            ([4,1,5,2,7,3],2)]
inverse_checks=0
facet_checks=0
for x,z in parameters:
    for _ in range(90):
        predecessor=[rng.randrange(8) for i in range(48)]
        current=q_step(predecessor,x,z)
        assert local_inverse(current,x,z)==predecessor
        assert min(facets(current))>=0
        inverse_checks+=1
    for _ in range(90):
        current=[rng.randrange(11) for i in range(48)]
        predecessor=local_inverse(current,x,z)
        assert q_step(predecessor,x,z)==current
        assert (min(predecessor)>=0)==(min(facets(current))>=0)
        inverse_checks+=1
        facet_checks+=1

bad=[0]*48
bad[2]=2
assert min(facets(bad))<0
assert local_inverse(bad,[1]*6,1)[R[2]]<0

facet_witnesses=0
for ids in GROUP.values():
    for special in ids:
        w=[F(0)]*48
        for i in ids:
            w[i]=F(4 if i==special else 1)
        v=[DROW[i]*w[i] for i in range(48)]
        f=facets(v)
        assert f[special]<0
        assert all(f[i]>0 for i in ids if i!=special)
        facet_witnesses+=1
assert inverse_checks==720 and facet_checks==360 and facet_witnesses==48

result={
    "schema":"PREFIX598_R2_NATIVE_48_IMAGE_CONE_V1",
    "scientific_input":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "native_phase_count":48,"native_port_count":96,"native_labelled_actions":576,
    "signed_current_axis_groups":12,"group_size":4,
    "exact_sr_matrix_entries":2304,
    "fixed_image_cone":"Drow * direct_sum_12(J4-I4) * R_ge0^48",
    "domain":"all positive six-axis weights, all z>=0",
    "local_inverse":"Dcol^-1 * R * W0^-1 * Drow^-1 * Dx^-1",
    "facets":48,"extreme_rays":48,
    "irredundancy_witnesses":facet_witnesses,
    "rational_forward_and_inverse_runs":inverse_checks,
    "arbitrary_candidate_facet_vs_inverse_checks":facet_checks,
    "unreachable_integral_port_positive_example":"z=1, v[2]=2, others 0",
    "result":"ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED"
}
out=Path(__file__).with_name(
    "PREFIX598_R2_parameter_independent_image_cone_results.json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",
               encoding="utf-8")
print(result["result"],"inverse",inverse_checks,"facets",facet_witnesses)
