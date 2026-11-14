#!/usr/bin/env python3
"""EC49FOO exact finite observer check over all 73 common-domain one-key swaps.
Run in a folder with C++-generated EC49FOO_NEIGHBOR_PROFILES.csv and original frozen
master_and_radius3_cases.txt. Outputs EC49FOO_73_NEIGHBORS.csv and an exact summary.
No floating point. Core per-root costs come from the native prefix-trie generator.
"""
import csv, json, itertools, collections, hashlib
from pathlib import Path
P="EC49FOO_NEIGHBOR_PROFILES.csv"
SRC="master_and_radius3_cases.txt"
SHA="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
assert hashlib.sha256(Path(SRC).read_bytes()).hexdigest()==SHA
E={5:(5,7),7:(6,7),13:(6,7),15:(3,5,7),
   17:(3,6,7),19:(3,5,7),21:(3,6,7)}
L=tuple(E);R=(3,5,6,7);base=(-1,-1)
D={};meta={}
with open(P,newline="") as fh:
    for row in csv.DictReader(fh):
        e=(int(row["swap_out"]),int(row["swap_in"]))
        r=int(row["root"]);must=int(row["must"]);opt=int(row["opt"])
        m=int(row["subset"]);v=int(row["cost"])
        if (e,r) in meta:assert meta[e,r]==(must,opt)
        else:meta[e,r]=(must,opt)
        assert m not in D.setdefault((e,r),{})
        D[e,r][m]=v
assert len(D)==74*4
for e,r in D:
    assert meta[e,r]==meta[base,r]
    assert D[e,r].keys()==D[base,r].keys()
legal=[]
for cc in itertools.product(*(E[l] for l in L)):
    rho=dict(zip(L,cc))
    masks={r:sum(1<<l for l in L if rho[l]==r) for r in R}
    legal.append((rho,masks))
assert len(legal)==648
def cost(e,m):return sum(D[e,r][m[r]] for r in R)
with open(SRC) as fh:
    nk,nw,nc=map(int,next(fh).split())
    assert (nk,nw,nc)==(94,178850,38169)
    for k in range(nk):
        n=int(next(fh))
        for j in range(n):next(fh)
    cases=[tuple(map(int,next(fh).split())) for j in range(nc)]
assert cases[32315]==(0,4,5,11,37,39,81)
ids={frozenset(ks):i for i,ks in enumerate(cases)}
edge_rows=[]
for e in sorted({e for e,r in D if e!=base}):
    diff={r:sum(D[e,r][m]!=D[base,r][m] for m in D[e,r]) for r in R}
    delta=[cost(e,m)-cost(base,m) for rho,m in legal]
    changed=sum(bool(v) for v in delta)
    canc=sum(v==0 and any(D[e,r][m[r]]!=D[base,r][m[r]] for r in R)
             for (rho,m),v in zip(legal,delta))
    selected=set(cases[32315]);selected.remove(e[0]);selected.add(e[1])
    case=ids[frozenset(selected)]
    edge_rows.append((e[0],e[1],case,*[diff[r] for r in R],
                      changed,min(delta),max(delta),int(changed==0),
                      int(not any(diff.values())),int(canc>0)))
assert len(edge_rows)==73
with open("EC49FOO_73_NEIGHBORS.csv","w",newline="") as fh:
    w=csv.writer(fh)
    w.writerow(("out","in","original_case_id","changed_03","changed_05",
                "changed_06","changed_07","terminal_changed_648",
                "delta_min","delta_max","terminal_equal","profile_equal",
                "has_local_cancellation"))
    w.writerows(edge_rows)
original=set()
with open("FIRST_NEUTRAL_EDGES_EC49FNS.txt") as fh:
    for line in fh:
        original.update(map(int,line.split()))
assert len(original)==51
previous=[x for x in edge_rows if x[2] in original]
new=[x for x in edge_rows if x[2] not in original]
assert len(previous)==44 and len(new)==29
assert sum(x[10] for x in edge_rows)==37
assert sum(x[11] for x in edge_rows)==37
assert all(x[10]==x[11] for x in edge_rows)
assert (sum(x[10] for x in new),sum(not x[10] for x in new))==(11,18)
compensated=[x for x in edge_rows if x[12]]
assert len(compensated)==1 and compensated[0][:3]==(37,62,33269)
assert sum(x[7] for x in edge_rows)==14139
result={
    "schema":"EC49FOO_NATIVE_ONE_KEY_FINITE_V1",
    "source_sha256":SHA,"frozen_pin":"fc0f038e7bfd12c886b4d37f900bfb770c0f61ab",
    "baseline":32315,"candidate_swaps":609,"same_domain_swaps":73,
    "reachable_root_entries_per_config":168,"named_assignments_per_config":648,
    "new_outside_prior_51":29,"new_equal":11,"new_different":18,
    "all_equal_terminal_and_profiles":37,"all_different_terminal_and_profiles":36,
    "all_assignment_nonzero_cancellation":0,
    "total_changed_assignment_observations":14139,
    "one_local_compensation_example":{"out":37,"in":62,"case":33269,
       "changed_root_entries":12,"changed_terminal_assignments":357,
       "zero_total_nonzero_root_assignments":54},
    "review":"NOT_REVIEWED"
}
with open("EC49FOO_RESULT.json","w") as fh:
    json.dump(result,fh,indent=2);fh.write("\n")
print("EC49FOO_73_PASS: new=29 equal=37 diff=36 local_cancellation_swap=37->62")
