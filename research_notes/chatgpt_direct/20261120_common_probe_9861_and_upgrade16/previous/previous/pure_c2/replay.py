"""Keep the C4 witness supports and test all equal-fee eleven-point exchanges."""
import argparse
from itertools import combinations,product
import json,os,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
def check(last,c4):
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(last/'group'),str(older/'bounds'),str(last/'original')]
    from cyclic11 import observations,class_cost
    from generate import maps
    from frontier9.native.replay_joint import run
    bad,pair=observations()
    def neg(i):return 25*(-(i//25)%5)+5*(-(i//5%5)%5)+(-i%5)
    def img(r,g):return frozenset(g[i] for i in r)
    g=bytes(neg(i) for i in range(125))
    identity=bytes(range(125))
    S=frozenset(map(frozenset,json.loads(c4.read_text())))
    saved=frozenset(map(frozenset,json.loads((HERE/'groups.json').read_text())))
    assert len(S)==12 and sorted(p for r in S for p in r)==list(range(125))
    linear,tr,_=maps()
    aff=[bytes(t[i] for i in l) for l in linear for t in tr]
    def stab(T):return [a for a in aff if all(img(r,a) in T for r in T)]
    assert all(img(r,g) in S for r in S) and len(stab(S))==4
    base=S;choices=[]
    for r in sorted(S,key=sorted):
        other=img(r,g)
        if len(r)!=11 or sorted(r)>=sorted(other):continue
        signs=[(p,g[p]) for p in sorted(r)]
        options=[]
        for z in product(*signs[1:]):
            v=frozenset([signs[0][0],*z])
            if not any((bad[i][j]>>k)&1 for i,j,k in combinations(v,3)):
                options.append((v,img(v,g)))
        assert len(options)==2 and all(class_cost(list(v),pair)==944 for v,_ in options)
        base=base-{r,other};choices.append(options)
    cases=[];pure=[]
    for opts in product(*choices):
        T=base|frozenset(r for orbit in opts for r in orbit)
        stabilizer=stab(T)
        cost=sum(class_cost(list(r),pair) for r in T)
        assert cost==10148
        cases.append(len(stabilizer))
        if len(stabilizer)==2:
            assert set(stabilizer)=={identity,g}
            pure.append(T)
    assert len(choices)==2 and sorted(cases)==[2,2,4,4] and saved in pure
    p,q=pure
    equivalent=next(a for a in aff if all(img(r,a) in q for r in p))
    assert len(aff)==12000
    code=[None]*125
    groups=sorted(map(sorted,saved))
    for k,row in enumerate(groups):
        for i in row:
            assert code[i] is None
            code[i]=k
    assert None not in code
    receipt=json.loads(json.dumps(run(code,1)))
    assert receipt['joint']['total_queries']==10148
    return {'stabilizers_of_four_phase_choices':cases,'pure_tables_in_phase_family':len(pure),
            'affine_maps_carrying_one_pure_phase_to_the_other':len(stab(p)),
            'affine_orbit_size':len(aff)//2,'prices':[class_cost(r,pair) for r in groups],
            'sizes':list(map(len,groups)),'receipt':receipt}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--round3',required=True,type=Path);ap.add_argument('--c4',required=True,type=Path,help='fifth round c4/groups.json')
    a=ap.parse_args();print(json.dumps(check(a.round3.resolve(),a.c4.resolve()),indent=2,sort_keys=True))
