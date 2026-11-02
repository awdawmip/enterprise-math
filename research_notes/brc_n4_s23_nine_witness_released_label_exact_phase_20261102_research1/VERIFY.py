"""Exact complete certificate for nine lawful BRC N4/S23 witnesses.
Verification: python3 VERIFY.py (stdlib only). Frozen science pin 43ec6098...
"""
from fractions import Fraction as F
from itertools import product, combinations
import json
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
AA=(0,0,0,1,1,1);BB=(2,2,3,2,2,4);CC=(5,6,7,8,9,10);G=(0,0,1,2,2,3)
def p(z):
    z=list(map(F,z));rows=[]
    for a,b,c in zip(AA,BB,CC):
        x,y,t=z[a],z[b],z[c];v=(1-x)*(1-y)
        rows.append((x,(1-x)*y,v*t,v*(1-t)))
    return tuple(tuple(sum(F(M[i][s],20)*rows[s][j] for s in range(6))
                       for j in range(4)) for i in range(6))
def q(k):
    return tuple(tuple(sum(F(M[i][s],20)*k[G[s]][j] for s in range(6))
                       for j in range(4)) for i in range(6))
def tv(a,b):return sum(abs(x-y) for x,y in zip(a,b))/2
def loss(a,b):return max(tv(x,y) for x,y in zip(a,b))
def parse(s):
    t=tuple(tuple(map(F,row.split())) for row in s.split(';'))
    assert len(t)==4 and all(len(row)==4 and sum(row)==1 and min(row)>=0 for row in t)
    return t
def O(s,t):return (s,t,0,0,0,0,1,1,1,0,1)
def N(s,t):return (s,t,0,0,0,1,0,0,0,0,0)
raw={'W':(1,0,0,0,1,0,0,0,0,0,0),
     'J':(1,F(1,3),0,0,0,0,0,0,0,1,0),
     'A':O(F(1,7),1),'B':O(1,F(1,7)),
     'C':N(F(1,7),1),'X':O(1,F(1,15)),
     'Y':(1,0,0,0,0,0,0,0,1,1,1),
     'Z':(0,1,0,1,0,1,1,0,0,0,0)}
OFF=('00000000000','00000001000','00000000001','00101000000',
     '00110000000','00101001000','00100000001','00100000000')
BASE=('34 24 34 24','34 23 34 34','34 34 34 23','24 24 12 12',
      '12 12 24 34','12 13 23 24','23 34 12 13','24 34 12 14')
def pair(s):return tuple(tuple(F(row.count(str(t)),2) for t in range(1,5)) for row in s.split())
fixed=[q(pair(s)) for s in BASE]
points={name:p(z) for name,z in raw.items()}
assert all(len(z)==11 and all(F(0)<=F(v)<=F(1) for v in z) for z in raw.values())
assert all(all(sum(row)==1 and min(row)>=0 for row in pp) for pp in points.values())
KERNELS = {
    1: (
        "9/14 0 0 5/14;1/2 0 1/2 0;1/2 0 0 1/2;1/2 1/2 0 0",
        "1/2 1/2 0 0;1/2 0 1/2 0;0 0 1/2 1/2;0 0 1/2 1/2",
        "0 0 1/2 1/2;0 1/2 0 1/2;1/2 0 0 1/2;1/2 0 0 1/2",
    ),
    2: (
        "9/14 0 0 5/14;1/2 0 1/7 5/14;1/2 0 0 1/2;1/2 1/2 0 0",
        "1/2 1/2 0 0;1/2 0 1/2 0;0 0 1/2 1/2;0 0 1/2 1/2",
        "0 0 1/2 1/2;0 1/2 1/2 0;1/2 0 0 1/2;1/2 0 0 1/2",
    ),
    3: (
        "9/14 0 0 5/14;1/2 0 1/2 0;1/2 0 0 1/2;1/2 1/2 0 0",
        "1/2 1/2 0 0;1/2 0 1/2 0;0 0 1/2 1/2;0 0 1/2 1/2",
        "0 0 1/2 1/2;0 1/2 0 1/2;1/2 0 0 1/2;1/2 0 1/2 0",
    ),
    4: (
        "4/35 1/2 0 27/70;1/7 0 5/14 1/2;1/2 1/2 0 0;1/2 1/2 0 0",
        "1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 0 1/2;1/2 1/2 0 0",
        "1/2 0 1/2 0;1/2 1/2 0 0;0 0 1/2 1/2;0 0 1/2 1/2",
    ),
    5: (
        "10/21 0 11/21 0;2/3 0 0 1/3;10/21 0 8/105 47/105;6/7 0 0 1/7",
        "1 0 0 0;10/21 0 11/21 0;0 0 10/21 11/21;0 10/21 10/21 1/21",
        "0 10/21 10/21 1/21;1/7 11/21 1/3 0;11/21 10/21 0 0;11/21 0 0 10/21",
    ),
    6: (
        "4/35 1/2 0 27/70;0 0 1/2 1/2;1/2 1/2 0 0;1/2 1/2 0 0",
        "1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 0 1/2;1/2 1/2 0 0",
        "1/2 0 1/2 0;1/2 1/2 0 0;0 0 1/2 1/2;0 0 1/2 1/2",
    ),
    7: (
        "1/2 0 1/2 0;1/2 1/2 0 0;1/2 0 1/10 2/5;1/2 0 0 1/2",
        "1 0 0 0;1 0 0 0;0 0 1/2 1/2;0 1/2 1/2 0",
        "0 1/2 4/35 27/70;1/7 0 5/14 1/2;1/2 1/2 0 0;1/2 0 1/2 0",
    ),
    8: (
        "1/2 0 1/2 0;1/2 1/2 0 0;1/2 1/3 1/10 1/15;1/2 0 1/3 1/6",
        "1/2 0 1/2 0;1 0 0 0;0 0 1/2 1/2;0 1/2 1/2 0",
        "1/7 1/2 5/14 0;1/7 0 5/14 1/2;1/2 1/2 0 0;1/2 0 0 1/2",
    ),
}

upper={}
for h,strings in KERNELS.items():
    bank=[q(parse(s)) for s in strings]
    pts={**points, 'T'+str(h):p(OFF[h-1])}
    bound=F(11,21) if h==5 else F(1,2)
    risks={name:min(loss(pt,b) for b in bank) for name,pt in pts.items()}
    assert max(risks.values())==bound,(h,risks)
    assert all(v<=bound for v in risks.values())
    # Every retained fixed pair kernel is unusable below 1/2 on all nine witnesses.
    assert all(min(loss(pt,fixed[j]) for j in range(8) if j!=h-1)>F(1,2)
               for pt in pts.values()),h
    upper[str(h)]={'radius':str(bound),'risks':{k:str(v) for k,v in risks.items()}}
# At h=5 the remaining seven FROZEN pair decoders cannot serve any witness for radius < 11/21.
pts5={**points,'T5':p(OFF[4])}
fixed5={name:min(loss(pt,fixed[j]) for j in range(8) if j!=4)
        for name,pt in pts5.items()}
assert all(v>F(11,21) for v in fixed5.values()),fixed5
names=tuple(pts5)
# If three targets use one common stochastic decoder on prepared row i,
# their pairwise disjoint maximizer events imply 3*r >= sum_atom(max_target P_i(atom)) - 1.
# Each maximizer is a real disjoint partition of {1,2,3,4} by deterministic tie break.
forbidden=[]
for ids in combinations(range(9),3):
    vals=[(sum(max(pts5[names[j]][i][t] for j in ids) for t in range(4))-1)/3
          for i in range(6)]
    score=max(vals)
    if score>=F(11,21):
        row=vals.index(score)
        forbidden.append((ids,score,row))
assert len(forbidden)==70,len(forbidden)
critical=[(tuple(names[j] for j in ids),i,score)
          for ids,score,i in forbidden if score==F(11,21)]
assert critical==[(('A','Z','T5'),0,F(11,21))],critical
# Any cover by three arbitrary real decoders induces one of 3**9 colorings.
# Exhaust all assignments; a forbidden monochromatic triple contradicts radius < 11/21.
checked=0;hit={}
for colors in product(range(3),repeat=9):
    match=next((ids for ids,score,i in forbidden
                if colors[ids[0]]==colors[ids[1]]==colors[ids[2]]),None)
    assert match is not None,colors
    hit[match]=hit.get(match,0)+1
    checked+=1
assert checked==3**9 and sum(hit.values())==checked
# Independent crosscheck: all 3281 unlabeled/canonical partitions are covered too.
canonical=set()
for colors in product(range(3),repeat=9):
    rename={};seq=[]
    for c in colors:
        if c not in rename:rename[c]=len(rename)
        seq.append(rename[c])
    canonical.add(tuple(seq))
assert len(canonical)==3281,len(canonical)
print(json.dumps({'pass':'PASS_BRC_N4_S23_NINE_WITNESS_RELEASED_LABEL_PHASE_EXACT_20261102',
 'source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
 'radius_by_released_original_label':{k:v['radius'] for k,v in upper.items()},
 'upper_each_witness_risks':upper,
 'h5_original_fixed_seven_min_risks':{k:str(v) for k,v in fixed5.items()},
 'h5_forbidden_exact_disjoint_event_triples':len(forbidden),
 'h5_tight_triple':{'names':list(critical[0][0]),'prepared_row':critical[0][1]+1,
                    'bound':str(critical[0][2])},
 'all_labeled_three_decoder_assignments_checked':checked,
 'unlabeled_partitions_crosschecked':len(canonical),
 'arithmetic':'Python standard library Fraction, exhaustive exact integer loops',
 'claim_status':'AUTHOR_ANALYTIC_AND_FINITE_EXACT_CERTIFICATE_UNREVIEWED_NOT_ADMITTED'},indent=2))
