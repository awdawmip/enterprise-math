#!/usr/bin/env python3
"""Independent native signed-prefix string-set crosscheck of 16 FCK quintets."""
import json
from pathlib import Path
from itertools import combinations
from frozen_model import REQ,W,observe,candidates,primpref
BASE=Path(__file__).resolve().parent
INDEX=[0,1,15,39,40,63,79,119,120,143,159,179,180,199,219,239]
def run():
    cert=json.loads(__import__('gzip').decompress(__import__('base64').b64decode((BASE/'EC49FCK_240_COMPACT.json.gz.b64').read_text())).decode())
    ref={r['i']:r for r in cert}
    chosen={f'{h}:{observe(w)}':w for h,words in W.items() for w in words}
    early=[f'{h}:{s}' for h in (4,5,6) for s in REQ[h]]
    combos=[(*e,f'7:{s}',f'8:{t}') for e in combinations(early,3) for s in REQ[7] for t in REQ[8]]
    cache={};ok=[]
    for i in INDEX:
        slots=combos[i]
        fixed=set().union(*(set(primpref(w)) for k,w in chosen.items() if k not in slots))
        cap=158-len(fixed);entries=[]
        for k in slots:
            if k not in cache:
                h,s=map(int,k.split(':'));cache[k]=candidates(h)[s]
            residuals={frozenset(set(primpref(w))-fixed) for w in cache[k]}
            allowed=[r for r in residuals if len(r)<cap]
            entries.append((k,allowed))
        entries.sort(key=lambda e:(len(e[1]),sum(len(s) for s in e[1])))
        states={frozenset()}
        for k,allowed in entries:
            states={u|s for u in states for s in allowed if len(u|s)<cap}
            if not states:break
        minimum=min([158]+[len(fixed)+len(s) for s in states])
        assert minimum==ref[i]['min']==158 and len(fixed)==ref[i]['fixed'] and tuple(ref[i]['slots'])==slots,(i,minimum)
        ok.append(i)
    print('INDEPENDENT_CROSSCHECK_OK',ok)
if __name__=='__main__':run()
