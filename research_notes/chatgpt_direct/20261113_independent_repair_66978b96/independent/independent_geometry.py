"""Pure-Python verifier for every nonempty joint writer family at n=2, q=5."""
from itertools import combinations, product
from collections import Counter
from pathlib import Path
import argparse,json
V=range(5)
WORLD=list(product(V,repeat=2))
ACTIONS=list(product((1,2),repeat=2))
T=((0,0,0,0,1),(1,2,1,2,0),(2,1,2,1,0),(1,2,1,2,0),(2,1,2,1,0))
I=((0,0,1,1,2),(1,2,0,2,3),(1,3,0,3,2),(2,1,2,0,3),(3,1,3,0,2))
def all_families():
    return [fs for n in range(1,5) for fs in combinations(ACTIONS,n)]
def code(fs):
    missing=[ac for ac in ACTIONS if ac not in fs]
    if not missing:return I
    k=missing[0]
    # T excludes transformed distances (2,2); multiply old x by 2 to flip distance classes.
    return tuple(tuple(T[x*(2 if k[0]==1 else 1)%5][y*(2 if k[1]==1 else 1)%5] for y in V) for x in V)
BOX_STARTS=((0,0),(0,1),(3,2),(1,0),(1,1),(4,2),(2,4),(2,3))
def zero_code(fs):
    sets=[{a[j] for a in fs} for j in range(2)];fixed=[len(v)==1 for v in sets]
    def enc(h):
        if not any(fixed):return 5*h[0]+h[1]
        if all(fixed):
            x,y=[z*next(iter(v))%5 for z,v in zip(h,sets)]
            return next(i for i,(u,v) in enumerate(BOX_STARTS) if (x-u)%5 in (0,2) and (y-v)%5 in (0,2))
        g=fixed.index(True);z=h[g]*next(iter(sets[g]))%5
        return 3*h[1-g]+(0,1,0,1,2)[z]
    return tuple(tuple(enc((x,y))for y in V) for x in V)
def outputs(h,a,e):
    f=[];s=[]
    for z,t,u in zip(h,a,e):
        v=z*t%5
        if v in (u,(u+1)%5):f.append(11);s.append(11 if v==u else u+1)
        else:f.append(u+6);s.append(12)
    return tuple(f),tuple(s)
def evaluate(C,fs):
    hist=Counter();max_inside=max_second=0;instances=0
    for a in fs:
        for e in WORLD:
            cells={}
            for h in WORLD:
                b,s=outputs(h,a,e);msg=C[h[0]][h[1]]
                cells.setdefault((msg,b),[]).append((h,s))
            for (msg,b),histories in cells.items():
                seconds={s for h,s in histories};max_second=max(max_second,len(seconds))
                if b==(11,11):max_inside=max(max_inside,len(histories))
                if len(seconds)>2:return {'invalid_class':dict(writer=a,menu=e,message=msg,first=b,worlds=[h for h,s in histories],seconds=sorted(seconds))}
                if len(seconds)==2:
                    s,t=sorted(seconds);g=next(i for i in range(2)if s[i]!=t[i]);assert b[g]==11
                    choices={}
                    for h,k in histories:
                        ans=int(a[g]*h[g]%5==e[g]); assert choices.setdefault(ans,k)==k
                    assert len(choices)==2
                hist[len(seconds)-1]+=len(histories);instances+=len(histories)
    return dict(instances=instances,max_both_inside=max_inside,max_possible_second=max_second,read_hist={str(k):v for k,v in sorted(hist.items())})
def run():
    families=[]
    for fs in all_families():
        C=code(fs);r=evaluate(C,fs);assert 'invalid_class' not in r
        colors=len({v for row in C for v in row});assert colors==(4 if len(fs)==4 else 3)
        Z=zero_code(fs);z=evaluate(Z,fs);assert z['max_possible_second']==1
        n0=len({m for row in Z for m in row})
        assert n0==(8 if len(fs)==1 else 15 if any(len({a[i]for a in fs})==1 for i in range(2)) else 25)
        families.append(dict(actions=fs,colors=colors,minimum_messages_by_budget=[n0,colors,1],zero_read_check=z,**r))
    assert sum(s['instances']for s in families)==20000
    old=tuple(tuple(((x+2*y)%5)//2 for y in V)for x in V)
    pair_witness=evaluate(old,[(1,2)]);assert 'invalid_class' in pair_witness
    base_witness=evaluate(T,[(2,2)]);assert 'invalid_class' in base_witness
    pairs=list(combinations(V,2));rects=list(product(pairs,repeat=2))
    coverage={tuple(sorted(h for h in WORLD if all(a[j]*h[j]%5 in (e[j],(e[j]+1)%5) for j in range(2)))) for a in ACTIONS for e in WORLD}
    assert coverage=={tuple(product(xx,yy)) for xx,yy in rects}
    color_sizes=sorted(Counter(c for row in I for c in row).values())
    assert len(coverage)==100 and color_sizes==[6,6,6,7]
    return dict(status='PASS',all_histories=25,pullback_rectangles=len(coverage),four_color_class_sizes=color_sizes,
                four_code=I,near_full_code_excluding_22=T,prior_code_counterexample=pair_witness['invalid_class'],near_full_code_counterexample=base_witness['invalid_class'],families=families)
if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,default=Path(__file__).with_name('independent_geometry_results.json'));p=a.parse_args()
    d=run();p.out.write_text(json.dumps(d,sort_keys=True,ensure_ascii=False,indent=1)+'\n');print('PASS',len(d['families']),d['families'][-1],d['prior_code_counterexample'])
