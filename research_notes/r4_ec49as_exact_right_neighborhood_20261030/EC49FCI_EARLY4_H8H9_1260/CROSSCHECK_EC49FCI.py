"""Independent signed tuple-prefix verification of nine selected cases."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FCF_EARLY1_LATE3_150'))
from frozen_model import W,REQ,observe,primpref,candidates
from itertools import combinations
import json
B=158

def main():
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{sig}' for h in (4,5,6) for sig in REQ[h]]
    sel={8:[0,199,401,699,839],9:[0,199,200,419]}
    checked=[];cache={}
    for h,indices in sel.items():
        late=[f'{h}:{sig}' for sig in REQ[h]]
        groups=[(*e,l) for e in combinations(early,4) for l in late]
        for idx in indices:
            slots=groups[idx]
            fixed=set().union(*(set(primpref(w)) for slot,w in chosen.items() if slot not in slots))
            cutoff=B-len(fixed)
            states={frozenset()};counts=[]
            for slot in slots:
                if slot not in cache:
                    horizon=int(slot.split(':')[0]);signature=int(slot.split(':')[1])
                    cache[slot]=candidates(horizon)[signature]
                residual={frozenset(set(primpref(w))-fixed) for w in cache[slot]}
                allowed=[r for r in residual if len(r)<cutoff]
                states={u|r for u in states for r in allowed if len(u|r)<cutoff}
                counts.append(len(states))
                if not states:break
            minimum=min([B]+[len(fixed)+len(u) for u in states])
            checked.append(dict(h=h,index=idx,slots=slots,minimum=minimum,
                                stage_counts=counts,fixed_edges=len(fixed)))
            print('CROSSCHECK',h,idx,minimum,flush=True)
    dest=Path(__file__).with_name('EC49FCI_CROSSCHECK_SAMPLES.json')
    dest.write_text(json.dumps({'independent_direct_tuple_prefix':True,'rows':checked},indent=2)+'\n')
if __name__=='__main__': main()
