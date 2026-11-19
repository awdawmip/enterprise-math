#!/usr/bin/env python3
"""Independent f0 verification of all six exceptional R5 12-label pairs plus
60 seeded ordinary controls from full 30,135-row census. Exact integer
left-endpoint masks; no C++ adjacency or C++ Bellman code reused.
"""
import json,hashlib,csv,random,functools
from pathlib import Path
base=Path(__file__).parent
raw=(base/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
assert hashlib.sha256(raw).hexdigest()=="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
data=json.loads(raw)
tau=int(json.loads((base/"stages_18.json").read_text())["U"])-1
cs={k:tuple(map(int,data["counts_and_cohorts"][str(k)]["counts"])) for k in range(214,315)}
S=(0,16,32,48,1,64,17,80,18,24)
def actions(pair):
    h=S+pair
    cheapest={}
    for k,vec in cs.items():
        z=[vec[i] for i in h]
        endpoints={2*v-tau for v in z}
        candidates={sum(1<<j for j,c in enumerate(z) if abs(2*c-e)<=tau) for e in endpoints}
        maximal=tuple(sorted(m for m in candidates if not any(m!=n and m&n==m for n in candidates)))
        if maximal!=(4095,):cheapest.setdefault(maximal,k)
    return tuple((k,ms) for ms,k in cheapest.items())
def solve(acts):
    @functools.lru_cache(None)
    def v(L):
        if L.bit_count()<=1:return 0
        offers=[]
        for k,ms in acts:
            children={L&m for m in ms}
            if L in children:continue
            offers.append(k+max(v(c) for c in children))
        assert offers
        return min(offers)
    return v(4095)
with (base/"pair12_f0_all30135.csv").open() as f:
    rows={(int(r["u"]),int(r["v"])):int(r["f0"]) for r in csv.DictReader(f)}
assert len(rows)==30135
rare=[p for p,n in rows.items() if n>733]
assert rare==[(2,82),(8,88),(34,82),(40,88),(50,82),(56,88)]
rng=random.Random(20261119)
controls=rng.sample([p for p,n in rows.items() if n==733],60)
for p in rare+controls:
    observed=solve(actions(p))
    assert observed==rows[p],(p,observed,rows[p])
print("PASS_R5_12_INDEPENDENT",len(rare)+len(controls),"all six exceptional pairs verified")
