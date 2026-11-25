# EC49FZM — Exact saturated-fiber multicover certificate and partial fourth-level classification

2026-11-25. Independent portable continuation of EC49FZL, frozen BRC16943, h=14, m=25. Parent report 0c15190b5dfcc7904e48af07be8d446f9b60237b:research_notes/portable_direct/EC49FZL_COMPLETE_THIRD_LEVEL_CLASSIFICATION.md; parent solver and generator 0b8230271b3c981112b138728d8623e4e259d3ad:research_artifacts/portable_direct/EC49FZL/{fullrow.cpp,fourth.py}. Historical author provenance EM-DIRECT-23537B; current private writer binding unconfirmed. Topic request r4-20261125-0930-ec49as-read-v1 SUCCEEDED on Source 7bbb1758d9f1d3d77bc441cd96523e3967fe1bd4, NO_CANONICAL_PUBLICATION_DIRECTORY. No live task owner inferred from directory absence; no CLAIM, Result, Review, or Activity mutation.

## Exact feature-conditioned fiber count

Let active support V have normalized fiber B_V subset K subset A_V, |K|<=h, obtained from a genuine query history W(r,j)=1_{r in V}1_{j not in K}. The declared observers are all future queries and labeled state recovery. Use FZI anchored complete certificate with a common positive row-column anchor; FZJ fibers and quotient. At target x=(U,H), select row feature set T, live column feature set P subset [m] minus H, and missing column feature set Z subset H. A competing V remains row-compatible iff T intersects (U xor V) trivially. Its exact number of compatible holes is zero if B_V intersects P, Z is not contained in A_V, or |C_V|>h where C_V=B_V union Z. Otherwise it is

sum_{i=0}^{min(h-|C_V|,f_V)} binom(f_V,i), where f_V=|A_V minus (C_V union P)|.

Proof: every matching hole set contains C_V, excludes P, and chooses any permitted subset of the f_V remaining optional columns. Sum over row-compatible V. This extends feature conditioning without expanding individual hole sets; feature constraints are not automatically actual query histories, but the anchored FZI resource lemma realizes selected features by actual probes. A singleton total is exactly an identifying feature certificate.

## Saturation-specific exact criterion

All genuine histories in this model have a shared potential-hole universe A0, the complement of the columns with an observed positive answer. Before saturation normalization each active support's fiber is [B_V,A0] truncated at h. Negatives on rows in V force missing columns; positives force their row to belong to every active V and their column live. Normalizing A_V=B_V at |B_V|=h does not change the fiber.

For target |H|=h write O=H minus B_U. Each o in O must be selected as a missing feature: the competitor (U,H minus {o}) is valid. If O subset Z, the U fiber has only H because B_U union Z=H. For every V!=U the following is necessary and sufficient for the chosen feature set to exclude that support:

[T intersects (U xor V)] OR [P intersects (B_V minus H)] OR [|B_V union Z|>h].

Indeed H and Z are subsets of A0. In the absence of these three conditions, K=B_V union Z is an actual competitor, has |K|<=h, avoids P, and matches all chosen row and column features. If any condition holds, all competitors in V are excluded. This also handles normalized saturated V, because |B_V|=h and Z not contained in B_V implies the last inequality. No individual hole expansion is needed.

For fixed T and Z=O union J, J subset B_U, retain V!=U failing the row condition and the capacity condition. Let tau(T,Z) be the minimum hitting-set size of the family {B_V minus H} for these V, with tau=infinity when a required set is empty. Empty family has tau=0. The exact anchored certificate cost is

C_sat(U,H)= min_{T,J subset B_U} [ |O|+|J|+|T minus U|+max(|T intersect U|,tau(T,O union J)) ],

where T ranges over row subsets (notation min_{T,J subset B_U} means only J is restricted to B_U). Proof: the preceding criterion is necessary and sufficient; for fixed T,Z minimum live-feature cost is exactly tau and the FZI cost is nondecreasing in the live-feature count. FZI anchored conversion proves equality to minimum target-specific query certificate cost, not the shared adaptive optimum.

## Exact multiplicity quotient within the certificate

After fixing T, list remaining competing supports V. Group live columns j outside H by their incidence signature (1_{j in B_V})_V. A live group only needs a Boolean selected flag because choosing one suffices for every competitor it hits; extra identical live features cannot decrease the monotone cost. Group j in B_U by signatures (1_{j not in B_V})_V. For a hole group g of multiplicity n_g retain an integer z_g in [0,n_g], not merely a flag. O is already mandatory. For each remaining V the capacity exclusion becomes

|B_V union O| + sum_g z_g 1_{g signature at V=1} > h.

Every grouped assignment lifts to actual labeled selections independently within its disjoint groups, and each original selection maps to an assignment preserving competitor exclusion and (after redundant live selections are removed) nonincreasing resource cost. Therefore this is an exact optimum-preserving quotient for the stated certificate; the live-group Boolean and hole-group multiplicity must be kept distinct. Future adaptive decisions still use FZJ's full fiber quotient; this certificate quotient is not a general dynamic replacement.

## Executed checks on unchanged fourth-level input

Parent fullrow.cpp SHA256 3d1ae2d75991d5b6cd9a131f38068f27d04a1e2fc2abccf6e6673893e00f9d0b, Git blob b14377bbc9b3797a651d6857b7474d33b9c5295d; parent fourth.py Git blob bd275641404bad6fe1d003cc441f8ce1c8abfbd7. Local parent reproduction ZIP contains gen.py, cases.json and parent CSVs. Running fourth.py regenerated byte-identical fourth.json (SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923, Git blob a4cf533ce8c0abffebe1225a1f2ca87ff504c910); this generated JSON is not claimed to be a pre-existing remote file. Census: 4695 ordered, 2393 distinct, 118..3794 states.

Executed saturated_cert.py (code below): 2393 roots, 4786 sampled saturated target states, 28716 feature-set tests (17112 singleton), 2393 unsaturated feature-count tests, 35591465 explicit state comparisons. All assertions passed, including exact grouped criterion versus explicit labeled state filtering. Seed 16943. This validates finite feature decisions, not optimization runtime.

## Fourth-level partial search

Reuse parent solver without changes, compile g++ -O3 -std=c++17 fullrow.cpp -o solver (assertions enabled). Generate exact root inputs with fourth_input.py below, zero-based sorted fourth.json index, k=15, per-root call cap 20000. Only completed CSV rows are classified. Three ranges requested 0..499, 500..2392, 1344..1843; second execution stopped at last completed index 1343, third stopped at 1549. No interrupted row is treated as a result. Completed rows 0..1549: 1497 YES, 53 cap-UNKNOWN, 0 NO. 4662618 recorded recursive calls, 1116479 labeled state replays on YES roots. 843 roots (1550..2392) have no completed row. Ordered mapping: 3050 YES, 110 cap-UNKNOWN, 1535 without completed row. These are exact branch feasibility tests only, not a full 25-column strategy. M14 remains 25..27; finite exceptions exact 35/82.

Exact compact status record: for 0<=id<1550 status=YES except the following UNKNOWN IDs; 1550<=id<2393 not completed. No NO.
976,1155,1156,1206,1208,1235,1240,1265,1287,1316,1320,1322,1325,1326,1327,1334,1346,1356,1385,1408,1409,1412,1417,1419,1436,1445,1451,1462,1470,1472,1475,1484,1486,1487,1492,1496,1497,1499,1500,1505,1511,1512,1513,1515,1516,1521,1523,1525,1529,1530,1531,1533,1545.

Local raw fourth_partial.csv SHA256 494f70227d537e0d57b36477ecaea66ad46dcc7f8c6151deeedc3db440ce8e27 (1550 rows); local reproduction bundle includes raw per-root calls. The compact classification above is the complete set of observed statuses. Source report includes executable reproduction code; raw local CSV may be separately preserved as attachment. No speedup from the new certificate is claimed; the executed adaptive search used the previous solver.

## Reproduction scripts

fourth_input.py:
```python
import json,sys
from gen import physical
cases=json.load(open('fourth.json')); lo,hi,cap=map(int,sys.argv[1:]); print(hi-lo)
for i in range(lo,hi):
 n,key,paths,status=cases[i];r,mask,other=key; st=physical([mask,*other],14,r,0);assert len(st)==n
 print(i,n,25,15,cap)
 for u,h in st:print(u,h)
```

saturated_cert.py (executed exact source):
```python
"""Exact conditional feature-count and saturated certificate checks on frozen FZL roots."""
from gen import physical
from fourth import fibers
from math import comb
import json,random,collections
M=25; HMAX=14; A0=(1<<M)-2

def count_features(f,T,u,P,Z):
    assert not (P&Z)
    total=0
    for v,b,a in f:
        if (u^v)&T or b&P or Z&~a:continue
        c=b|Z
        if c.bit_count()>HMAX:continue
        p=(a&~(c|P)).bit_count()
        total+=sum(comb(p,j) for j in range(min(p,HMAX-c.bit_count())+1))
    return total

def sat_unique(f,u,h,T,P,Z):
    b=next(b for v,b,a in f if v==u)
    assert h.bit_count()==HMAX and not(P&h) and not(Z&~h)
    if (h&~b)&~Z:return False
    return all((u^v)&T or P&c or (c|Z).bit_count()>HMAX for v,c,a in f if v!=u)

def sat_group_unique(f,u,h,T,P,Z):
    b=next(b for v,b,a in f if v==u); o=h&~b
    if o&~Z:return False
    vset=[(v,c) for v,c,a in f if v!=u and not ((v^u)&T)]
    live_groups=collections.Counter(tuple(bool(c>>j&1) for v,c in vset) for j in range(M) if P>>j&1)
    hole_groups=collections.Counter(tuple(not(c>>j&1) for v,c in vset) for j in range(M) if (Z&b)>>j&1)
    for i,(v,c) in enumerate(vset):
        if any(sig[i] for sig in live_groups):continue
        if (c|o).bit_count()+sum(n for sig,n in hole_groups.items() if sig[i])<=HMAX:return False
    return True

def main():
    rng=random.Random(16943); cases=json.load(open('fourth.json')); checks=0; unique=0; statechecks=0; sat_n=0; unsat_checks=0
    for n,key,paths,status in cases:
        r,mask,other=key; f=list(fibers(key)); st=physical([mask,*other],HMAX,r,0);assert len(st)==n
        sat=[(u,h) for u,h in st if h.bit_count()==HMAX]; assert sat
        for u,h in rng.sample(sat,min(2,len(sat))):
            sat_n+=1
            b=next(b for v,b,a in f if v==u);o=h&~b
            for mode in range(6):
                T=rng.getrandbits(10);P=rng.getrandbits(M)&~h;Z=rng.getrandbits(M)&h
                if mode<5:Z|=o
                if mode==0:T=0;P=0;Z=o
                if mode==1:T=1023;P=0;Z=o
                if mode==2:T=0;P=((1<<M)-1)&~h;Z=h
                actual=sum(not ((v^u)&T or K&P or Z&~K) for v,K in st)
                direct=count_features(f,T,u,P,Z); assert actual==direct
                assert sat_unique(f,u,h,T,P,Z)==(actual==1)
                assert sat_group_unique(f,u,h,T,P,Z)==(actual==1)
                checks+=1;unique+=actual==1;statechecks+=len(st)
        unsat=[(u,h) for u,h in st if h.bit_count()<HMAX]
        if unsat:
            u,h=rng.choice(unsat);T=rng.getrandbits(10);P=rng.getrandbits(M)&~h;Z=rng.getrandbits(M)&h
            assert count_features(f,T,u,P,Z)==sum(not ((v^u)&T or K&P or Z&~K) for v,K in st);unsat_checks+=1;statechecks+=len(st)
    print('roots',len(cases),'sampled saturated targets',sat_n,'saturated feature tests',checks,'singleton',unique,'unsaturated tests',unsat_checks,'explicit state comparisons',statechecks)
if __name__=='__main__':main()
```

Next: continue the 843 untouched fourth-level IDs and 53 capped roots without redoing 1497 YES roots; implement the exact saturated grouped multicover optimizer and measure actual node-level benefit before claiming acceleration. P000 unchanged. Evidence grade AUTHOR_PROVED / EXACT_FINITE_FEATURE_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED.
