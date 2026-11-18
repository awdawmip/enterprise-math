"""Standalone exact Python certificate: R5 weighted two-cut suffix observer."""
from itertools import combinations, product
import json

GAPS=(3,2,2,3)
OLD=[frozenset(map(int,s)) for s in ('0125','0135','0235','0245','0246')]
DL,DR=OLD[1],OLD[4]
A={1:[frozenset(map(int,s)) for s in ('1235','1245','1246','1345','1346')],
   3:[frozenset(map(int,s)) for s in ('1235','1236','1245','1246','1345','1346')]}

def core(m,t):
    gaps=list(GAPS)+[x for _ in range(m) for x in (2,1)]
    if t&1:gaps[0]-=1
    if t&2:gaps[3]-=1
    X=[0]
    for gap in gaps:X.append(X[-1]+gap)
    return X

def suffix(h):
    return frozenset(7+2*i+b for i,b in enumerate(h))

def dist(S,T):return len(S-T)

def allopt(m,t,kind='halfcube',Y=None):
    X=core(m,t); N=len(X); K=m+3; best=10**9; opt=[]
    for raw in combinations(range(N),K):
        S=frozenset(raw)
        d=[min(abs(x-X[j]) for j in S) for x in X]
        if max(d)>2:continue
        h=tuple(int(8+2*i in S) for i in range(m-1))
        if kind=='mixed':p=int(0 in S or (int(2 in S)!=h[0]))
        else:p=int(0 in S or (h[0]!=1 if Y is None else h not in Y))
        v=2*sum(d)+p
        if v<best:best,opt=v,[S]
        elif v==best:opt.append(S)
    return best,set(opt)

def minimal_cover(new,old,r,upper):
    old=list(old);new=list(new)
    cover=[sum(1<<i for i,S in enumerate(new) if dist(S,T)<=r) for T in old]
    goal=(1<<len(new))-1
    for k in range(1,upper+1):
        for ids in combinations(range(len(old)),k):
            u=0
            for j in ids:u|=cover[j]
            if u==goal:return k
    raise AssertionError('witness was not a cover')

def run():
    G=[]
    for t in range(4):
        # Seven-event unweighted core certificate, exact 35 candidates.
        X=core(1,t); scores=[]
        for s in combinations(range(7),4):
            ds=[min(abs(x-X[j]) for j in s) for x in X]
            if max(ds)<=2:scores.append((sum(ds),frozenset(s)))
        best=min(v for v,_ in scores)
        assert best==5
        G.append({s for v,s in scores if v==best})
    assert [len(x) for x in G]==[5,12,9,17]
    assert all(0 in s for s in G[0]|G[2])
    assert G[0]==set(OLD)
    assert all({s for s in G[t] if 0 not in s}==set(A[t]) for t in (1,3))
    rows=[]
    for m in range(2,7):
        ell=m-1; H=list(product((0,1),repeat=ell));Y=[h for h in H if h[0]==1]
        row={'m':m,'weighted_counts':[],'mixed_counts':[]}
        for kind in ('halfcube','mixed'):
            for t in range(4):
                val,F=allopt(m,t,kind)
                if t in (0,2):
                    predicted={c|suffix(h) for c in G[t] for h in H}
                    assert val==2*(m+4)+1
                else:
                    predicted={c|suffix(h) for c in A[t] for h in H if (h[0]==1 if kind=='halfcube' else h[0]==int(2 in c))}
                    assert val==2*(m+4)
                assert F==predicted
                row[('mixed' if kind=='mixed' else 'weighted')+'_counts'].append(len(F))
        old=allopt(m,0)[1]
        for t in (1,3):
            new=allopt(m,t)[1]
            lib=([DL|suffix(h) for h in Y]+[DR|suffix(h) for h in Y]) if ell==1 else [(DL if h[1]==0 else DR)|suffix(h) for h in Y]
            assert len(lib)==max(2,2**(ell-1))
            assert all(min(dist(S,T) for T in lib)<=2 for S in new)
            assert max(min(dist(S,T) for T in old) for S in new)==2
            assert all({T for T in old if dist(frozenset((1,3,4,6))|suffix(h),T)<=2}=={DL|suffix(h),DR|suffix(h)} for h in Y)
            if m<=3:assert minimal_cover(new,old,2,len(lib))==len(lib)
        if m<=3:
            row['mixed_exact_r2_libraries']=[minimal_cover(allopt(m,t,'mixed')[1],old,2,5) for t in (1,3)]
        rows.append(row)
    m=4;Y={(0,0,0),(0,1,1)}
    old=allopt(m,0,'halfcube',Y)[1]
    witness=[DL|suffix((0,0,0)),DL|suffix((0,1,1)),DR|suffix((0,0,1))]
    for t in (1,3):
        v,new=allopt(m,t,'halfcube',Y)
        assert v==16 and all(min(dist(S,T) for T in witness)<=2 for S in new)
        assert minimal_cover(new,old,2,3)==3
    evidence={'status':'PASS_R5_WEIGHTED_NONPRODUCT_AMBIENT','frozen_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
              'integer_arithmetic':'twice weighted integer objective',
              'finite_coverage':'all feasible event-center subsets, all four masks, m=2..6; exact library m2..3; ambient m4',
              'rows':rows,'ambient_Y':['000','011'],'ambient_exact_kappa_a_ab':3}
    print(json.dumps(evidence,indent=2))

if __name__=='__main__':run()
