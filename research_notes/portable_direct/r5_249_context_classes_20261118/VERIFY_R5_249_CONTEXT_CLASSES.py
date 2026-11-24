#!/usr/bin/env python3
"""Exact fifth-chamber contextual-support quotient. Python standard library only."""
import collections, hashlib, json, sys
from pathlib import Path
SHA = "50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
L = 25845652773852463277015040000
U = 58182461585441404127941754880
BASE = (18,24,82,34,17)
CONTEXT = BASE + (144,208)
def maximal(masks):
    ss = set(masks)
    return tuple(sorted(m for m in ss if not any(v != m and (m & v) == m for v in ss)))
def windows(c,tau):
    return maximal(sum(1<<i for i,x in enumerate(c) if a<=x<=a+tau) for a in c)
def sweep(c,tau):
    ep=sorted(set(z for x in c for z in (2*x-tau,2*x+tau)))
    masks=[sum(1<<i for i,x in enumerate(c) if abs(z-2*x)<=tau) for z in ep]
    masks += [sum(1<<i for i,x in enumerate(c) if abs(a+b-4*x)<=2*tau)
              for a,b in zip(ep,ep[1:])]
    return maximal(masks)
def main():
    path=Path(sys.argv[1] if len(sys.argv)>1 else "EXACT_R5_ALL_101_BUDGETS.json")
    raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    table=json.loads(raw)["counts_and_cohorts"]
    d={k:tuple(map(int,table[str(k)]["counts"])) for k in range(214,315)}
    assert len(d)==101 and all(len(v)==256 for v in d.values())
    bp=set()
    for c in d.values():
        for i,x in enumerate(c):
            for y in c[:i]:
                diff=abs(x-y)
                if L<diff<U: bp.add(diff)
    reps=[L]+sorted(bp)
    assert len(reps)==18
    classes=collections.defaultdict(list)
    for x in range(256):
        if x in CONTEXT:continue
        sig=[]
        for c in d.values():
            centers=[c[h] for h in BASE]+[c[x],c[144],c[208]]
            sig.extend(windows(centers,t) for t in reps)
        classes[tuple(sig)].append(x)
    groups=sorted(classes.values(),key=lambda g:g[0])
    assert len(groups)==53 and sum(map(len,groups))==249
    assert [0,48] in groups
    for g in groups:
        x=g[0]
        for c in d.values():
            centers=[c[h] for h in BASE]+[c[x],c[144],c[208]]
            for t in reps:
                assert windows(centers,t)==sweep(centers,t),(x,t)
    out={"status":"PASS_R5_249_CONTEXT_CLASSES_ALL_F",
         "frozen_science":"435e77af0d180eac32bd1f9c4c464bc4010b7551",
         "count_table_sha256":SHA,
         "context":list(CONTEXT),
         "interval":[str(L),str(U)],
         "candidate_count":249,"class_count":53,"redundant_candidates":196,
         "breakpoints":[str(t) for t in sorted(bp)],
         "classes":groups,"independent_family_crosschecks":53*101*18}
    Path(__file__).with_name("R5_249_CONTEXT_CLASSES.json").write_text(
        json.dumps(out,indent=2,sort_keys=True)+"\n")
    print(out["status"],len(groups),len(bp),out["independent_family_crosschecks"])
if __name__=="__main__":main()
