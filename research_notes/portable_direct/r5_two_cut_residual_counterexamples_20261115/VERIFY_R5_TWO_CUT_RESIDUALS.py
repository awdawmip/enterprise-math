#!/usr/bin/env python3
"""Exact radius-two indexed K-center two-cut residuals; Python >=3.9, no deps."""
import itertools, json

def pts(g,a,b,m):
    d=list(g)
    assert a!=b and d[a]==d[b]==3
    if m&1: d[a]-=1
    if m&2: d[b]-=1
    x=[0]
    for gap in d:
        assert gap>=1
        x.append(x[-1]+gap)
    return x

def opt(x,k):
    best=None; F=set()
    for S in itertools.combinations(range(len(x)),k):
        ds=[min(abs(x[t]-x[s]) for s in S) for t in range(len(x))]
        if max(ds)>2: continue
        c=sum(ds)
        if best is None or c<best: best,F=c,{S}
        elif c==best: F.add(S)
    return best,F

def directed(A,B):
    assert A and B
    return max(min(len(set(S)-set(T)) for T in B) for S in A)

def run_case(g,a,b,k):
    x=[pts(g,a,b,m) for m in range(4)]
    O=[opt(z,k) for z in x]
    J=[v for v,_ in O]
    assert J[0] is not None and len(set(J))==1
    F=[v for _,v in O]
    assert F[0]<=F[1] and F[0]<=F[2] and F[1]<=F[3] and F[2]<=F[3]
    P=(F[1]&F[2])-F[0]; Q=F[3]-(F[1]|F[2])
    assert len(F[3])==len(F[1])+len(F[2])-len(F[0])-len(P)+len(Q)
    h=[directed(F[i],F[0]) for i in (1,2,3)]
    hq=directed(Q,F[0]) if Q else 0
    assert h[2]==max(h[0],h[1],hq)
    return dict(gaps=g,cuts=[a,b],K=k,coordinates=x,costs=J,
        optimizers=[[list(s) for s in sorted(v)] for v in F],
        P=[list(s) for s in sorted(P)],Q=[list(s) for s in sorted(Q)],
        maxmin_A_B_AB=h,extra_joint_maxmin=hq)

def small_minimality():
    stats={}
    for n in (3,4):
        count=equalJ=bad_union=bad_intersection=0
        for a,b in itertools.combinations(range(n-1),2):
            other=[q for q in range(n-1) if q not in (a,b)]
            for values in itertools.product((1,2,3),repeat=len(other)):
                g=[3]*(n-1)
                for t,v in zip(other,values): g[t]=v
                for k in range(1,n+1):
                    count+=1
                    O=[opt(pts(g,a,b,m),k) for m in range(4)]
                    if any(v is None for v,_ in O) or len({v for v,_ in O})!=1:
                        continue
                    equalJ+=1
                    F=[v for _,v in O]
                    bad_union+=(F[3]!=(F[1]|F[2]))
                    bad_intersection+=(F[0]!=(F[1]&F[2]))
        assert bad_union==0
        stats[str(n)]=dict(cases=count,equal_finite_optima=equalJ,
                           union_failures=bad_union,intersection_failures=bad_intersection)
    return stats

def main():
    four=run_case([3,3,2],0,1,3)
    five=run_case([3,2,3,2],0,2,3)
    six=run_case([3,2,3,3,2],0,2,4)
    assert four['P']==[[0,2,3]] and four['Q']==[]
    assert five['P']==[] and five['Q']==[[0,3,4]]
    assert six['maxmin_A_B_AB']==[1,1,2]
    assert [1,2,4,5] in six['Q']
    data={'status':'PASS_EXACT_TWO_CUT_RESIDUALS_AND_MINIMAL_UNION_COUNTEREXAMPLE',
          'scope':'derived integer 1D indexed-center radius-two, cuts 3-to-2',
          'n4':four,'n5':five,'n6':six,
          'n_le_4_minimality':small_minimality(),
          'review':'AUTHOR_PROVED_EXACT_FINITE_CHECKED_NOT_REVIEWED'}
    print(json.dumps(data,indent=2,sort_keys=True))

if __name__=='__main__':main()
