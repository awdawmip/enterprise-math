#!/usr/bin/env python3
"""R635 exact signed BRC six-axis common-background fiber verification."""
import itertools, json, math
from math import comb
from pathlib import Path
def C(n,k): return comb(n,k) if 0<=k<=n else 0
def norm(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(*rows):
    z=[0]*max((len(a) for a in rows),default=1)
    for a in rows:
        for i,v in enumerate(a):z[i]+=v
    return norm(z)
def neg(a):return [-x for x in a]
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return norm(z)
def prod(rows):
    z=[1]
    for r in rows:z=mul(z,r)
    return z
def sh(a,n):return [0]*n+list(a)
def jet(a,d):return (a+[0]*(d+1))[:d+1]
def K(i):
    ds=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    return add(*([sh([-v*C(i+1-j,q) for q in range(i+2-j)],i-1)
        for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))
def nu(a):return next((i for i,v in enumerate(a) if v%5),None)
def clipped_nu(a,d):
    r=nu(jet(a,d))
    return r if r is not None else d+1

def main():
    K12=[K(i) for i in range(1,13)]
    P=K12[::2];M=K12[1::2]
    assert [nu(x) for x in P]==[0,2,4,6,8,10]
    assert [nu(x) for x in M]==[1,3,5,7,9,11]
    U=[P[j][2*j:] for j in range(6)]
    V=[M[j][2*j+1:] for j in range(6)]
    assert [u[0] for u in U]==[2,-8,6,106,83,9]
    assert [v[0] for v in V]==[-1,-11,53,119,36,1]
    W=prod([z for j in range(6) for z in (U[j],V[j])])
    divU=[prod([z for i in range(6) for typ,z in ((0,U[i]),(1,V[i]))
          if (i,typ)!=(j,0)]) for j in range(6)]
    divV=[prod([z for i in range(6) for typ,z in ((0,U[i]),(1,V[i]))
          if (i,typ)!=(j,1)]) for j in range(6)]
    for j in range(6):
        assert mul(divU[j],U[j])==W and mul(divV[j],V[j])==W
    perms=list(itertools.permutations(range(6)))
    counts={'frozen_input_leads':24,'factorization':12,
      'original_dual_probe_identities':0,'swap_full_polynomial_identities':0,
      'fiber_invariant_checks':0,'fiber_group_checks':0}
    table={}
    for a in (1,2,4):
        v=[a+2*j for j in range(6)]
        B=[sh(W,e) for e in v]
        for j in range(6):
            Ap=sh(divU[j],a);Am=sh(divV[j],a-1)
            assert nu(Ap)==a and nu(Am)==a-1
            assert mul(Ap,P[j])==B[j] and mul(Am,M[j])==B[j]
            counts['original_dual_probe_identities']+=2
        Hprime=add(B[4],B[5])
        for j in range(6):
            k=5 if j==4 else 4 if j==5 else j
            Q=add([1],neg(sh([1],v[4]-v[j])),neg(sh([1],v[5]-v[j]))) if j<4 else [-1]
            Ap=sh(mul(divU[k],Q),a);Am=sh(mul(divV[k],Q),a-1)
            assert nu(Ap)==a and nu(Am)==a-1
            assert add(mul(Ap,P[k]),Hprime)==B[j]
            assert add(mul(Am,M[k]),Hprime)==B[j]
            counts['swap_full_polynomial_identities']+=2
        table[str(a)]={}
        for d in range(max(0,a-1),a+13):
            m=min(6,max(0,(d-a)//2+1));h=6-m
            D=[max(clipped_nu(add(B[i],neg(B[j])),d)
              for j in range(6) if j!=i) for i in range(6)]
            expectedD=([min(v[j],d+1) for j in range(m)]+[d+1]*h
                       if h>=2 else
                       ([v[j] for j in range(4)]+[v[4],v[4]]
                        if m>=5 else
                        [v[j] for j in range(m-1)]+[v[m-1],v[m-1]]))
            assert D==expectedD,(a,d,m,D)
            groups0={};groups1={}
            for pi in perms:
                k0=tuple(D[j] for j in pi)
                k1=tuple(clipped_nu(B[j],d) for j in pi)
                groups0[k0]=groups0.get(k0,0)+1
                groups1[k1]=groups1.get(k1,0)+1
                counts['fiber_invariant_checks']+=2
            F0=max(2,math.factorial(h));F1=math.factorial(h)
            assert set(groups0.values())=={F0} and max(groups0.values())==F0
            assert set(groups1.values())=={F1} and max(groups1.values())==F1
            counts['fiber_group_checks']+=2
            table[str(a)][str(d)]={'m':m,'F0':F0,'F1':F1}
    assert sum(counts.values())==60672,counts
    return {'schema':'EM_R635_SHARED_BACKGROUND_REFERENCE_FIBER_V1',
        'date':'2026-11-08',
        'frozen_science_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'frozen_K_generator_blob':'7fa7a762f758b30c6090468ac43487daa34abad8',
        'parent_R634_commit':'1fab59f1bb9b0d89d79baa51989aaf30cd33f35b',
        'status':'AUTHOR_SIDE_PROVED_DERIVATION_UNREVIEWED_NOT_ADMITTED',
        'formula_no_reference':'max(2,(6-m)!)',
        'formula_one_reference':'(6-m)!',
        'm':'min(6,max(0,floor((d-a)/2)+1))',
        'counts':counts,'total_exact_checks':sum(counts.values()),
        'fiber_table':table,'marker':'R635_SHARED_BACKGROUND_SINGLE_REFERENCE_PASS'}
if __name__=='__main__':
    data=main()
    Path(__file__).with_name('R635_EVIDENCE.json').write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'marker':data['marker'],'total_exact_checks':data['total_exact_checks'],'counts':data['counts']},sort_keys=True))
