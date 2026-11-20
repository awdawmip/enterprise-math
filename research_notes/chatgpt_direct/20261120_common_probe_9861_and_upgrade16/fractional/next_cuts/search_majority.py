"""Search complete three-point majority cliques and explore larger odd cores."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,time,random
import numpy as np
HERE=Path(__file__).resolve().parent
PROOF=HERE.parent/'proof'

def points(mask):
    while mask:
        b=mask&-mask;yield b.bit_length()-1;mask-=b

def exact_cut(rows,vertices):
    t=sum(1<<i for i in vertices);k=len(vertices)//2+1
    selected=[r for r in rows if (int(r['mask'])&t).bit_count()>=k]
    lhs=sum((Fraction(r['numerator'],r['denominator'])for r in selected),Fraction())
    return {'kind':'odd_point_majority','vertices':list(vertices),'threshold':k,'class_count':len(selected),'lhs_numerator':lhs.numerator,'lhs_denominator':lhs.denominator,'violated':lhs>1}

def search_frame(frame):
    d=json.loads((PROOF/f'cover_{frame}.json').read_text());rows=d['weights'];masks=[int(r['mask'])for r in rows]
    weights=np.array([r['numerator']/r['denominator']for r in rows]);free=list(points(int(d['free_mask'])));lists=[list(points(m))for m in masks]
    pairs=np.zeros((125,125));triples=np.zeros((125,125,125))
    for ps,w in zip(lists,weights):
        for i,j in combinations(ps,2):pairs[i,j]+=w
        for i,j,k in combinations(ps,3):triples[i,j,k]+=w
    best=(-1,None)
    for i,j,k in combinations(free,3):
        v=pairs[i,j]+pairs[i,k]+pairs[j,k]-2*triples[i,j,k]
        if v>best[0]:best=(v,(i,j,k))
    out={'frame':frame,'all_triples_checked':len(free)*(len(free)-1)*(len(free)-2)//6,'best_three_float':best[0],'best_three_exact':exact_cut(rows,best[1])}
    print(json.dumps(out),flush=True)
    rng=random.Random(20261120+frame)
    incidence=np.zeros((len(rows),125),dtype=np.int8)
    for j,ps in enumerate(lists):incidence[j,ps]=1
    for length in [5,7,9]:
        k=length//2+1;best=(-1,None);start=time.monotonic();trials=0
        # This is constructive exploration only, not a universal clique check.
        while time.monotonic()-start<15:
            chosen=set(rng.sample(free,length));hits=incidence[:,list(chosen)].sum(axis=1)
            while True:
                value=float(weights@(hits>=k));improve=None
                for old in chosen:
                    minus=hits-incidence[:,old]
                    score=weights@(minus>=k)
                    marginal=weights*(minus==k-1)
                    scores=score+marginal@incidence
                    for new in free:
                        if new in chosen:continue
                        if improve is None or scores[new]>improve[0]:improve=(float(scores[new]),old,new)
                if improve[0]<=value+1e-10:break
                _,old,new=improve;chosen.remove(old);chosen.add(new);hits+=incidence[:,new]-incidence[:,old]
            trials+=1
            if value>best[0]:best=(value,tuple(sorted(chosen)))
            if value>1.00000001:break
        out[f'best_{length}']={'discovery_trials':trials,'float':best[0],'exact':exact_cut(rows,best[1])}
        print(json.dumps({'frame':frame,'length':length,**out[f'best_{length}']}),flush=True)
    return out

if __name__=='__main__':
    result=[]
    for f in range(1,6):
        result.append(search_frame(f));(HERE/'majority_results.json').write_text(json.dumps(result,indent=2)+'\n')
