#!/usr/bin/env python3
"""Audit original signed-word endpoints, depthwise disjointness, and complete row coverage."""
import argparse,functools,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'EC49FFA_H8_FIVEKEY_DEPTHWISE_20261109'))
import h8_key_depth_sieve as core

@functools.lru_cache(None)
def original_checked(h,k,sig):
    legal=[]
    for label,w in core.words(h,k):
        if label!=sig:continue
        assert len(w)==h
        assert (w.count('a'),w.count('c')+w.count('d'),w.count('f'),w.count('g'))==core.counts(h,k)
        assert w.count('e')==k[2]
        q=0;position=[0]*6
        for ch in w:
            q=core.NEXT[q][core.LETTERS.index(ch)]
            for a in core.STEPS[ch]:position[abs(a)-1]+=1 if a>0 else -1
        assert core.OBS[q]==sig and tuple(position)==(2,0,0,0,0,0)
        legal.append(w)
    return core.prefixes(h,k,sig) if legal else {}

def verify(late,files):
    late=tuple(int(c) for c in late)
    assert late in ((5,7,8,9),(6,7,8,9))
    inv,_,_=core.build_inventories(7,late);groups=core.all_groups(7,late)
    indices=[];bounds=[]
    for f in files:
        for line in Path(f).read_text().splitlines():
            row=json.loads(line);idx=row['index'];K=tuple(tuple(x) for x in row['keys'])
            assert K==tuple(tuple(x) for x in inv[idx])
            D=row['D'];assert len(D)==24;bound=0
            for d,selected in enumerate(D,1):
                assert len(selected)==len(set(selected))
                seen=set()
                for groupidx in selected:
                    h,sig=groups[groupidx];possible=set();lens=[]
                    for k in K:
                        ps=original_checked(h,k,sig)
                        if ps:lens.append(max(ps));possible.update(ps.get(d,()))
                    assert lens and min(lens)>=d and possible
                    assert seen.isdisjoint(possible)
                    seen.update(possible)
                bound+=len(selected)
            assert bound==row['lower_bound']
            indices.append(idx);bounds.append(bound)
    assert sorted(indices)==list(range(len(inv)))
    result={'late':''.join(map(str,late)),'status':'EXACT_INTEGER_PASS','verified':len(indices),'min_bound':min(bounds),'max_bound':max(bounds),'le93':sum(x<=93 for x in bounds)}
    print(json.dumps(result,sort_keys=True))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('late',choices=('5789','6789'))
    p.add_argument('files',nargs='+')
    args=p.parse_args()
    verify(args.late,args.files)
