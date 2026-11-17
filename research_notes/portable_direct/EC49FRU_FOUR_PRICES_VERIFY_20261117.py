#!/usr/bin/env python3
"""EC49FRU original-native four-price exact verifier.

Reproduce inside the extracted EC49FRS/FRT self-contained evidence bundle:
  cp EC49FRU_FOUR_PRICES_VERIFY_20261117.py <bundle>/code/
  python <bundle>/code/EC49FRU_FOUR_PRICES_VERIFY_20261117.py

Requires Python stdlib, the archive's original 94-family source, profile CSV,
EC49FQI_NATIVE_DATA.py, EC49FRQ_INDEPENDENT_ALL228.py, and
evidence/EC49FRS_FOUR_EQUAL_SURCHARGE_EXPANSION_20261117.json.
No floating-point costs, no external network, no relabeling of physical queries.
"""
from pathlib import Path
from functools import lru_cache
from collections import Counter
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"code"))
from EC49FRQ_INDEPENDENT_ALL228 import PARTS, ALL, OBS, subset_keys, representatives
from EC49FQI_NATIVE_DATA import V, keys, PIN
assert PIN=="fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
assert len(PARTS)==len(OBS)==len(V)==228
assert len(representatives)==141
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(ROOT/"source/frozen_original_master.txt")=="cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e"
assert sha(ROOT/"source/EC49FPG_PROFILE.csv")=="a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f"

def native(q):
    return q if q<144 else 144+keys.index(subset_keys[q-144])
assert all(OBS[q]==V[native(q)] for q in range(228))
CHARGED=(32,34,140,142)

def solve(price):
    assert len(price)==4 and all(isinstance(x,int) and x>=0 for x in price)
    surcharges=dict(zip(CHARGED,price))
    @lru_cache(None)
    def opt(mask):
        if mask.bit_count()==1: return 0,()
        best=10**80
        choices=[]
        for q,part in enumerate(PARTS):
            children=[mask&piece for piece in part if mask&piece]
            if len(children)<2: continue
            value=(141+surcharges.get(native(q),0))*mask.bit_count()
            value+=sum(opt(m)[0] for m in children)
            if value<best:
                best=value
                choices=[q]
            elif value==best:
                choices.append(q)
        return best,tuple(choices)
    best,choices=opt(ALL)
    return opt,dict(z=list(price),value=best,
                    first=sorted(native(q) for q in choices),
                    masks=opt.cache_info().currsize)

def tree(opt,first_native):
    def rec(mask,force=None):
        if mask.bit_count()==1: return {"leaf":mask.bit_length()-1}
        valid=opt(mask)[1]
        q=next((j for j in valid if native(j)==force),None) if force is not None else valid[0]
        assert q is not None,(force,[native(j) for j in valid])
        children={}
        for p in PARTS[q]:
            sub=p&mask
            if not sub: continue
            i=(sub&-sub).bit_length()-1
            children[str(OBS[q][i])]=rec(sub)
        assert len(children)>=2
        return {"q":native(q),"children":children}
    return rec(ALL,first_native)

def replay(t):
    uses=Counter()
    for i in range(141):
        node=t
        seen=set()
        while "q" in node:
            q=node["q"]
            assert q not in seen
            seen.add(q);uses[q]+=1
            node=node["children"][str(V[q][i])]
        assert node=={"leaf":i}
    return sum(uses.values()),tuple(uses[q] for q in CHARGED),dict(sorted(uses.items()))

def main():
    output={"schema":"EC49FRU_NATIVE_FOUR_PRICES_CERTIFICATE_V1","pin":PIN,
            "original_actions":228,"named_states":141,"anchors":[],"witnesses":{}}
    for z,expected in [((0,0,0,0),41736),((2,2,0,0),42018),((3,3,1,1),42159)]:
        _,result=solve(z)
        assert result["value"]==expected and result["masks"]==13063
        output["anchors"].append(result)
        print("ANCHOR",result,flush=True)
    for name,z,root,expected_base,expected_incidence in [
      ("A",(0,10,10,10),32,296,(141,0,0,0)),
      ("Aprime",(10,0,10,10),34,296,(0,141,0,0)),
      ("B",(10,10,0,10),140,298,(0,0,141,0)),
      ("Bprime",(10,10,10,0),142,298,(0,0,0,141))]:
        opt,result=solve(z)
        t=tree(opt,root)
        base,incidence,counts=replay(t)
        assert (base,incidence)==(expected_base,expected_incidence)
        assert result["value"]==141*base+sum(i*j for i,j in zip(z,incidence))
        output["witnesses"][name]={"root":root,"base_uses":base,
                                    "incidences":incidence,"tree":t,
                                    "physical_query_uses":counts}
        print("WITNESS",name,base,incidence,flush=True)
    prior=json.loads((ROOT/"evidence/EC49FRS_FOUR_EQUAL_SURCHARGE_EXPANSION_20261117.json").read_text())
    t=prior["new_avoiding_trees"]["46"]["tree"]
    base,incidence,counts=replay(t)
    assert (base,incidence)==(299,(0,0,0,0))
    output["witnesses"]["T"]={"root":46,"base_uses":299,
                               "incidences":incidence,"tree":t,
                               "physical_query_uses":counts}
    output["sources_sha256"]={"frozen_master":sha(ROOT/"source/frozen_original_master.txt"),
                              "profile_csv":sha(ROOT/"source/EC49FPG_PROFILE.csv")}
    dest=ROOT/"evidence/EC49FRU_FOUR_INDEPENDENT_PRICES_CERTIFICATE.json"
    dest.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n")
    print("PASS",str(dest),sha(dest))
if __name__=="__main__":
    main()
