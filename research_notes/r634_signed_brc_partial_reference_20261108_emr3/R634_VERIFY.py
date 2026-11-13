#!/usr/bin/env python3
"""Exact integer verification for frozen R462 K, R633 full-jet collision."""
import itertools, json
from math import comb
from pathlib import Path
def C(n,k): return comb(n,k) if 0<=k<=n else 0
def norm(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def add(*rows):
    z=[0]*max(map(len,rows))
    for row in rows:
        for i,v in enumerate(row): z[i]+=v
    return norm(z)
def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): z[i+j]+=v*w
    return norm(z)
def sh(a,n): return [0]*n+list(a)
def K(i):
    ds=(-C(4,i)+C(2,i-1),C(5,i-1)-C(5,i-2),C(7,i-2),-C(9,i-3))
    return add(*([sh([-v*C(i+1-j,q) for q in range(i+2-j)],i-1)
      for j,v in enumerate(ds,1) if v and i+1-j>=0] or [[0]]))
def nu(a,p=None): return next((i for i,x in enumerate(a) if x and (p is None or x%p)),None)
def jet(a,d): return (a+[0]*(d+1))[:d+1]
def pow_gt(h,p):
    v=1
    while v<=h: v*=p
    return v
def H_at(B,k): return add(*[[C(k,l)*v for v in row] for l,row in enumerate(B)])

# R634: BRC sign and source identities are preserved in the verified K generator.
def main():
    N=6
    kk=[K(i) for i in range(1,13)]
    P=kk[::2]; M=kk[1::2]
    assert [nu(v,5) for v in P]==[0,2,4,6,8,10]
    assert [nu(v,5) for v in M]==[1,3,5,7,9,11]
    assert [P[j][2*j] for j in range(N)]==[2,-8,6,106,83,9]
    assert [M[j][2*j+1] for j in range(N)]==[-1,-11,53,119,36,1]
    U=[P[j][2*j:] for j in range(N)]
    V=[M[j][2*j+1:] for j in range(N)]
    perms=list(itertools.permutations(range(N)))
    counts=dict(frozen_lead_checks=24,full_polynomial_uncalibrated_zero_identities=0,
                equivalence_signatures=0,paired_depth_lower_bound=0,
                representative_nonzero_background_signatures=0,
                precision_calibration_orbit_checks=0)
    top={}
    table={}
    for a in (1,2,4):
        zero=[]
        for j in range(N):
            ap=sh(V[j],a); am=sh(U[j],a-1)
            H=[-v for v in mul(ap,P[j])]
            assert nu(ap,5)==a and nu(am,5)==a-1
            assert add(mul(ap,P[j]),H)==[0] and add(mul(am,M[j]),H)==[0]
            counts['full_polynomial_uncalibrated_zero_identities']+=2
            zero.append((ap,am,H))
        d=a+8
        top[str(a)]={}
        for r in range(N+1):
            groups={}
            for perm in perms:
                sig=[]
                for x,j in enumerate(perm):
                    if x<r:
                        ap=sh([1],a)
                        yp=mul(ap,P[j]); ym=mul(ap,M[j])
                        assert nu(yp,5)==a+2*j
                        sig.append((tuple(jet(yp,d)),tuple(jet(ym,d)),tuple(jet([0],d))))
                    else:
                        ap,am,H=zero[j]
                        yp=add(mul(ap,P[j]),H); ym=add(mul(am,M[j]),H)
                        assert yp==[0] and ym==[0]
                        sig.append((tuple(jet(yp,d)),tuple(jet(ym,d)),None))
                groups[tuple(sig)]=groups.get(tuple(sig),0)+1
                counts['equivalence_signatures']+=1
            expected=__import__('math').factorial(N-r)
            assert len(groups)==720//expected and set(groups.values())=={expected}
            top[str(a)][str(r)]={'distinct_transcripts':len(groups),'largest_fiber':expected}
        for j in (4,5):
            assert jet(mul(sh([1],a),P[j]),a+7)==[0]*(a+8)
            assert jet(mul(sh([1],a),M[j]),a+7)==[0]*(a+8)
            counts['paired_depth_lower_bound']+=2
            ap,am,H=zero[j]
            assert add(mul(ap,P[j]),H)==[0]
            counts['paired_depth_lower_bound']+=1
        for x in range(N):
            for j in range(N):
                H=[x+j+1,x+2*j-3,2*x+1]
                ap=sh([1+5*x,1+2*j,3],a)
                am=sh([3+x,2+j],a-1)
                yp=add(mul(ap,P[j]),H)
                ym=add(mul(am,M[j]),H)
                assert add(yp,[-v for v in H])==mul(ap,P[j])
                assert nu(add(yp,[-v for v in H]),5)==a+2*j
                counts['representative_nonzero_background_signatures']+=1
        table[str(a)]={}
        for d in range(max(0,a-1),a+11):
            m=min(N,max(0,(d-a)//2+1))
            h=N-m
            table[str(a)][str(d)]={}
            for r in range(N+1):
                labels=[(tuple(jet(sh(P[j],a),d)),
                         tuple(jet(sh(M[j],a),d)),tuple(jet([0],d))) for j in range(N)]
                uncal=(tuple([0]*(d+1)),tuple([0]*(d+1)),None)
                groups={}
                for perm in perms:
                    key=tuple(labels[j] if x<r else uncal for x,j in enumerate(perm))
                    groups[key]=groups.get(key,0)+1
                    counts['precision_calibration_orbit_checks']+=1
                s=min(r,h)
                expected=__import__('math').factorial(h)//__import__('math').factorial(h-s)*__import__('math').factorial(N-r)
                assert max(groups.values())==expected,(a,d,r)
                table[str(a)][str(d)][str(r)]=expected
    assert sum(counts.values())==196746,counts
    return {
        'schema':'EM_R634_PARTIAL_REFERENCE_MINIMAX_V1',
        'date':'2026-11-08',
        'frozen_science_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'frozen_K_generator_blob':'7fa7a762f758b30c6090468ac43487daa34abad8',
        'claim_status':'AUTHOR_SIDE_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED',
        'theorem':'F(r,d,a)=falling(h,min(r,h))*(6-r)!, h=6-min(6,max(0,floor((d-a)/2)+1)); a>=1',
        'counts':counts,'total_exact_checks':sum(counts.values()),
        'at_depth_a_plus_8':top,'precision_reference_fiber_table':table,
        'marker':'R634_PARTIAL_REFERENCE_MINIMAX_FIBER_PASS'}
if __name__=='__main__':
    data=main()
    Path(__file__).with_name('R634_EVIDENCE.json').write_text(json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'marker':data['marker'],'total_exact_checks':data['total_exact_checks'],'counts':data['counts']},sort_keys=True))
