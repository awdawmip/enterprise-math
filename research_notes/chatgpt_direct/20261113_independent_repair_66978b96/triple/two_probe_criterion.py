"""Exact local depth-two classifiers and a 49-cell feasible color class."""
import argparse,json
from itertools import product, combinations
from collections import Counter
from pathlib import Path
V=range(5)
Q=list(product(range(2),repeat=3))
def criterion(S):
    return len(S)<4 or len(S)==4 and any(sum(x[i]==0 for x in S)==2 for i in range(3))
def depth(S):
    if len(S)<2:return 0
    return 1+min(max(depth([x for x in S if x[i]==b]) for b in (0,1)) for i in range(3) if 0<sum(x[i] for x in S)<len(S))
def run():
    masks=Counter()
    for m in range(256):
        S=[x for j,x in enumerate(Q)if m>>j&1]
        star=any(all(tuple((z^(j==k)) for j,z in enumerate(t)) in S for k in range(3)) for t in S)
        actual=depth(S);assert (actual<=2)==criterion(S)==(len(S)<=4 and not star)
        masks[len(S),actual]+=1
    A={(i,0)for i in range(1,5)}|{(0,j)for j in range(1,5)}
    valid=lambda x,y,z: (((y,z)in A)!=(x==4))
    worlds={t for t in product(V,repeat=3)if valid(*t)}
    assert len(A)==8 and len(worlds)==49
    hist=Counter();depth_hist=Counter()
    for cube in product(combinations(V,2),repeat=3):
        S=[s for s in Q if tuple(cube[j][s[j]]for j in range(3))in worlds]
        assert criterion(S)
        hist[len(S)]+=1;depth_hist[depth(S)]+=1
    return dict(status='PASS',alphabet=5,npairs=10,checked_local_binary_functions=256,binary_mask_degree_depth=[[n,d,v]for (n,d),v in sorted(masks.items())],witness_size=len(worlds),slices='x=0,1,2,3: exactly one of y,z is 0; x=4: both or neither are 0',stars=sorted(A),cubes=sum(hist.values()),occupancy=dict(sorted(hist.items())),minimal_depth=dict(sorted(depth_hist.items())),interpretation='single valid class; does not construct a coloring by three such classes')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,default=Path(__file__).with_name('two_probe_criterion_results.json'));a=p.parse_args();d=run();a.out.write_text(json.dumps(d,sort_keys=True,indent=1)+'\n');print('PASS',d['witness_size'],d['cubes'],d['occupancy'],d['minimal_depth'])
