#!/usr/bin/env python3
"""R5 finite frozen-input checks for exact-price failure-density theorem.
Run with EXACT_R5_ALL_101_BUDGETS.json and stages_18.json in same directory.
Python standard library only. Symbolic asymptotics proved separately.
"""
from pathlib import Path
import hashlib, json, itertools, math, collections

P = Path(__file__).resolve().parent
SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
raw = (P / "EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == SHA
source = json.loads(raw)
prices = tuple(range(214,315))
S = (set(range(214,219)),
     {214,*range(216,222)},
     {215,*range(216,222)},
     set(range(223,291)),
     set(range(296,313)))
assert [len(x) for x in S] == [5,7,7,68,17]
centers = [[int(v) for v in source["counts_and_cohorts"][str(k)]["counts"]]
           for k in prices]
tau = int(json.loads((P/"stages_18.json").read_text())["U"])-1
masks = set()
for a in range(256):
    for b in range(a+1,256):
        mask = 0
        for i,c in enumerate(centers):
            if abs(c[a]-c[b])>tau:
                mask |= 1<<i
        masks.add(mask)
minimum=[]
for mask in sorted(masks,key=lambda x:(x.bit_count(),x)):
    if not any(mask & other == other for other in minimum):
        minimum.append(mask)
mask_of = lambda seq: sum(1<<(k-214) for k in seq)
assert len(masks)==53
assert set(minimum)=={mask_of(s) for s in S}
assert all(any(mask & s == s for s in minimum) for mask in masks)

A=S[0]
outside=tuple(sorted(set(prices)-A))
assert outside==tuple(range(219,315))
assert sum(prices)==26664 and sum(outside)==25584
assert math.prod(prices)==math.prod(A)*math.prod(outside)

moments={}
for m in (1,2,3,5,17):
    coeff=collections.Counter()
    for s in range(m):
        for chosen in itertools.combinations_with_replacement(sorted(A),s):
            coeff[(s,sum(chosen))]+=1
    J0=sum(coeff.values())
    J1=sum(cost*n for (s,cost),n in coeff.items())
    assert J0==math.comb(m+4,5)
    assert J1==180*(m-1)*J0
    K=math.prod(range(96,101))*math.prod(A)*J0
    moments[str(m)]={"J0":str(J0),"J1":str(J1),"K_m":str(K)}

# Independent exact m=1 five-bit decodability DP.
# A state records which of the five required witnesses has been hit.
N=1500
memb={k:sum(1<<i for i,s in enumerate(S) if k in s) for k in prices}
dp=[[0]*(N+1) for _ in range(32)]
dp[0][0]=1
for price in prices:
    bit=memb[price]
    nxt=[arr.copy() for arr in dp]
    for n in range(price,N+1):
        for mask in range(32):
            count=nxt[mask][n-price]
            if count:
                nxt[mask|bit][n]+=count
    dp=nxt

total=[0]*(N+1); total[0]=1
for price in prices:
    for n in range(price,N+1):
        total[n]+=total[n-price]

bad_A=[0]*(N+1);bad_A[0]=1
for price in outside:
    for n in range(price,N+1):
        bad_A[n]+=bad_A[n-price]

# Independent inclusion-exclusion over all five zero-hit events at m=1.
IE={}
for sub in range(1,32):
    banned=set().union(*(S[i] for i in range(5) if sub & (1<<i)))
    arr=[0]*(N+1);arr[0]=1
    for price in prices:
        if price not in banned:
            for n in range(price,N+1):
                arr[n]+=arr[n-price]
    IE[sub]=arr

samples={}
for n in (735,840,1000,1200,1500):
    good=dp[31][n]
    bad=total[n]-good
    bad2=sum((1 if sub.bit_count()%2 else -1)*IE[sub][n]
             for sub in range(1,32))
    assert bad==bad2 and bad>=bad_A[n]
    samples[str(n)]={"total":str(total[n]),"good":str(good),
                     "bad":str(bad),"bad_A":str(bad_A[n]),
                     "other_bad":str(bad-bad_A[n])}

result={"schema":"R5_DEFECT_EXPONENT_VERIFIED_V1","input_sha256":SHA,
        "distinct_separation_masks":len(masks),
        "minimal_witness_sets":[sorted(x) for x in S],
        "pole_moment_checks":moments,
        "independent_m1_checks":samples,
        "symbolic_proof":"RESEARCH_R5_DEFECT_EXPONENT.md",
        "review":"NOT_REVIEWED"}
(P/"RESULT_R5_DEFECT_EXPONENT_VERIFIER.json").write_text(
    json.dumps(result,indent=2)+"\n")
print("PASS 32640 pair checks, 53 masks, five minimal witness sets")
print("PASS derivative moments m=1,2,3,5,17")
print("PASS m=1 exact integer DP agrees with inclusion-exclusion at 5 prices")
