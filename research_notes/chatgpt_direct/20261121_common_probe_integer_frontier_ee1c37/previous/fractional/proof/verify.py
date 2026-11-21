"""Exact standard-library verification of full-star fractional cover witnesses.

This reproduces the finite original-menu observation algebra used in the pinned
common-probe proofs. A class is legal iff it contains none of the resulting
forbidden triples; its read cost counts every history/menu/transform ambiguity.
That reduction and the integer lower bound are inherited scientific inputs, not
newly proved by this checker. All certificate arithmetic here is integral.
"""
from pathlib import Path
from itertools import product, combinations
from collections import defaultdict, Counter
from math import lcm
import argparse,json

POINTS=list(product(range(5),repeat=3))
FULL=(1<<125)-1
EXPECTED={(9,557):2,(10,744):5,(11,936):2,(11,944):1}

def points(mask):
    while mask:
        b=mask&-mask
        yield b.bit_length()-1
        mask-=b

def observation_tables():
    bad=[[0]*125 for _ in POINTS];pair=[[0]*125 for _ in POINTS]
    triples=set()
    for k,(d,start) in enumerate(product((1,3),POINTS)):
        observed=defaultdict(list)
        for i,p in enumerate(POINTS):
            a=tuple(j for j in range(3)if(p[j]-start[j])%5 in(0,d))
            y=tuple(p[j]for j in a)
            observed[a].append((i,y))
        for group in observed.values():
            for (i,x),(j,y)in combinations(group,2):
                if x!=y:pair[i][j]|=1<<k;pair[j][i]|=1<<k
            for (i,x),(j,y),(h,z)in combinations(group,3):
                if len({x,y,z})!=3:continue
                triples.add((i,j,h))
                bad[i][j]|=1<<h;bad[j][i]|=1<<h
                bad[i][h]|=1<<j;bad[h][i]|=1<<j
                bad[j][h]|=1<<i;bad[h][j]|=1<<i
    assert len(triples)==47000
    return bad,pair

def native_class(mask,bad,pair):
    assert 0<mask<=FULL
    ps=list(points(mask))
    for i,j in combinations(ps,2):assert not(bad[i][j]&mask)
    cost=0
    for i in ps:
        union=0
        for j in ps:union|=pair[i][j]
        cost+=union.bit_count()
    return len(ps),cost

def verify_one(path,bad,pair,known):
    doc=json.loads(path.read_text());cores=list(map(int,doc['core_masks']));free=int(doc['free_mask'])
    assert len(cores)==2 and not(cores[0]&cores[1]) and (cores[0]|cores[1]|free)==FULL
    assert not(free&(cores[0]|cores[1]))
    for m in cores:
        if m not in known:known[m]=native_class(m,bad,pair)
        assert known[m]==(12,1104)
    rows=doc['weights'];masks=[int(r['mask'])for r in rows]
    assert len(masks)==len(set(masks))
    q=1
    for r in rows:
        assert type(r['numerator'])is int and type(r['denominator'])is int
        assert r['numerator']>0 and r['denominator']>0
        q=lcm(q,r['denominator'])
    ints=[r['numerator']*(q//r['denominator'])for r in rows]
    coverage=[0]*125;counts=Counter();cost=0
    for m,r,w in zip(masks,rows,ints):
        assert m&free==m
        if m not in known:known[m]=native_class(m,bad,pair)
        typ=known[m];assert typ==(r['size'],r['cost']) and typ in EXPECTED
        counts[typ]+=w;cost+=typ[1]*w
        for p in points(m):coverage[p]+=w
    assert coverage==[q if free>>p&1 else 0 for p in range(125)]
    assert counts==Counter({t:n*q for t,n in EXPECTED.items()})
    assert sum(ints)==10*q and cost+2208*q==9858*q
    least=None;checks=0
    for anchor,weight in zip(masks,ints):
        compatible=[0]*125
        for m,w in zip(masks,ints):
            if m&anchor:continue
            for p in points(m):compatible[p]+=w
        for p in points(free^anchor):
            slack=compatible[p]-weight;checks+=1
            assert slack>=0,(doc['frame'],anchor,p,slack)
            if least is None or slack<least[0]:least=(slack,anchor,p)
    # Outside the free set, the two disjoint unit-weight cores satisfy every
    # positive-anchor inequality. All unlisted legal classes have weight zero.
    # Thus the checked finite support proves the entire implicit star family.
    return {'frame':doc['frame'],'positive_noncore_classes':len(rows),'positive_classes_total':len(rows)+2,'full_label_weight':12,'full_cost':9858,'core_weights':[1,1],'star_checks_inside_free':checks,'all_stars_satisfied':True,'minimum_internal_slack_numerator':least[0],'minimum_internal_slack_denominator':q,'minimum_internal_slack_float_for_display':least[0]/q,'worst_anchor_mask':str(least[1]),'worst_point':least[2]}

def main():
    p=argparse.ArgumentParser();p.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent);p.add_argument('--output',type=Path);a=p.parse_args()
    bad,pair=observation_tables();known={};result=[]
    for frame in range(1,6):
        result.append(verify_one(a.directory/f'cover_{frame}.json',bad,pair,known))
        print(json.dumps(result[-1]),flush=True)
    out={'schema':'FULL_STAR_CERTIFICATE_VERIFICATION_V1','forbidden_triples':47000,'native_classes_checked':len(known),'frames':result,'scope':'exact fractional witnesses, not integer partitions or an improved integer upper bound'}
    if a.output:a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'native_classes_checked':len(known),'frame_count':len(result),'all_verified':True}),flush=True)

if __name__=='__main__':main()
