#!/usr/bin/env python3
"""Independent all-4-tuples bitset oracle for h=2..5; exact 3,389,185 tuples.
Source model: original BRC six-axis expansion + 9-state observer.
"""
import json,sys,itertools
from pathlib import Path
from BRC_ORIGINAL_MODEL_EC49FFJ import candidates,native,observed
from VERIFY_EC49FFJ_TRIE import admissible_keys
SIG=(1,2,4,8)

def brute(h,key):
    groups={s:[] for s in SIG}
    for w,s in candidates(h,key):
        if s in groups:
            assert observed(w)==s
            n=native(w);groups[s].append((w,tuple(n[:d] for d in range(1,len(n)+1))))
    allp={p for values in groups.values() for _,pseq in values for p in pseq}
    idx={p:i for i,p in enumerate(allp)}
    masks=[[sum(1<<idx[p] for p in ps) for _,ps in groups[s]] for s in SIG]
    best=10**9;total=0
    for x in masks[0]:
        for y in masks[1]:
            ab=x|y
            for z in masks[2]:
                abc=ab|z
                for t in masks[3]:
                    n=(abc|t).bit_count();total+=1
                    if n<best:best=n
    return best,total

def verify(report_path):
    rep=json.loads(Path(report_path).read_text())
    expected={(r['h'],tuple(r['key'])):r for r in rep['rows']}
    total=0;configs=0
    for h in range(2,6):
        for key in admissible_keys(h):
            opt,n=brute(h,key)
            assert opt==expected[(h,key)]['prefix_optimum'],(h,key,opt)
            configs+=1;total+=n
    assert configs==24 and total==3389185,(configs,total)
    return {'status':'EXACT_BRUTE_MATCH','configurations':configs,'combinations':total}

if __name__=='__main__':
    print(json.dumps(verify(sys.argv[1] if len(sys.argv)>1 else 'EXACT_REPORT_EC49FFJ.json'),indent=2))
