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
def main():
    k=[K(i) for i in range(1,13)]; P=k[::2];M=k[1::2]
    assert [nu(x) for x in P]==[0,2,4,6,8,10]
    assert [nu(x) for x in M]==[1,3,5,7,9,11]
    pl=[x[nu(x)] for x in P];ml=[x[nu(x)] for x in M]
    assert pl==[2,-8,6,106,83,9] and ml==[-1,-11,53,119,36,1]
    assert all(x%5 for x in pl+ml)
    counts=dict(frozen_lead_checks=24,polynomial_factorization_identities=0,
      six_axis_full_jet_collapse_checks=0,background_reference_recovery_permutations=0,
      background_reference_recovery_axis_checks=0,lower_bound_witnesses=0)
    U=[];V=[]
    for j in range(6):
        u=P[j][2*j:];v=M[j][2*j+1:];U.append(u);V.append(v)
        assert sh(u,2*j)==P[j] and sh(v,2*j+1)==M[j]
        for a in (1,2,5):
            ap=sh(v,a);am=sh(u,a-1)
            assert nu(ap)==a and nu(am)==a-1 and ap[a]%5 and am[a-1]%5
            assert mul(ap,P[j])==mul(am,M[j])
            counts['polynomial_factorization_identities']+=1
    perms=list(itertools.permutations(range(6)))
    for a in (1,2,5):
        for perm in perms:
            for x,j in enumerate(perm):
                ap=sh(V[j],a);am=sh(U[j],a-1)
                H=[-z for z in mul(ap,P[j])]
                assert add(mul(ap,P[j]),H)==[0] and add(mul(am,M[j]),H)==[0]
                counts['six_axis_full_jet_collapse_checks']+=1
    for a in (1,2,5):
        for h in (0,1,3,4,9,24):
            k0=2*(h+1);k1=k0+pow_gt(h,5)
            labels={}
            for x in range(6):
                for j in range(6):
                    ap=sh([1+x%3,2+j,1],a)
                    am=sh([2+j,1,3],max(a-1,0))
                    B=[[x+j+l+1,2*l-x,1+j] for l in range(h+1)]
                    H0=H_at(B,k0);H1=H_at(B,k1)
                    y0=add(mul(ap,P[j]),H0);y1=add(mul(am,M[j]),H1)
                    restored=add(y0,[-v for v in H0])
                    order=nu(restored,5)
                    assert restored==mul(ap,P[j]) and order==a+2*j
                    assert all(z%5==0 for z in jet(add(H1,[-v for v in H0]),a+8))
                    labels[x,j]=order if order<=a+8 else None
                    counts['background_reference_recovery_axis_checks']+=1
            for perm in perms:
                obs=[labels[x,j] for x,j in enumerate(perm)]
                assert sorted(obs,key=lambda z:99 if z is None else z)==[a,a+2,a+4,a+6,a+8,None]
                assert [((z-a)//2 if z is not None else 5) for z in obs]==list(perm)
                counts['background_reference_recovery_permutations']+=1
    for a in (1,2,5):
        for j in (4,5):
            d=a+7
            assert jet(mul(sh([1],a),P[j]),d)==[0]*(d+1)
            assert jet(mul(sh([1],a-1),M[j]),d)==[0]*(d+1)
            counts['lower_bound_witnesses']+=1
    return {'schema':'EM_R633_GAIN_DROP_FULL_JET_COLLAPSE_V1','date':'2026-11-08',
      'frozen_science_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'frozen_K_generator_blob':'7fa7a762f758b30c6090468ac43487daa34abad8',
      'parent_commit':'a9dbf2905918c97935cefbaa184d03e0b146c0b9',
      'model':'integer polynomial axis-specific sign-dependent gains; arbitrary integer Newton background includes constant',
      'prime':5,'P_leading':pl,'M_leading':ml,
      'obstruction':'Y_plus == Y_minus == 0 exactly as integer polynomials for all 720 permutations and all a>=1; analytical identity valid to infinite precision',
      'repair':'one exact same-background reference R_x=H_x(k0); first-signed response modulo 5 has valuation a+2j-2 and d=a+8 suffices',
      'counts':counts,'total_exact_checks':sum(counts.values()),
      'marker':'R633_FULL_JET_GAIN_DROP_COLLAPSE_AND_REFERENCE_REPAIR_PASS',
      'claim_status':'AUTHOR_SIDE_EXACT_PROOF_UNREVIEWED_NOT_ADMITTED'}
if __name__=='__main__':
    d=main()
    Path(__file__).with_name('R633_EVIDENCE.json').write_text(json.dumps(d,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'marker':d['marker'],'counts':d['counts'],'total_exact_checks':d['total_exact_checks']},sort_keys=True))
