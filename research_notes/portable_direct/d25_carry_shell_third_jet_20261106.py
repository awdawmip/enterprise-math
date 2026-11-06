#!/usr/bin/env python3
"""Independent exact finite-field check of triple signed-carry shells and
Clausen denominator-jet correction. No native D25 experiment is simulated.
"""
from math import isqrt


def primes_to(limit):
    ans=[]
    for n in range(5,limit+1):
        if all(n%d for d in range(2,isqrt(n)+1)): ans.append(n)
    return ans


def mul(a,b,p):
    out=[0]*4
    for i in range(4):
        for j in range(4-i):
            out[i+j]=(out[i+j]+a[i]*b[j])%p
    return out


def inv_linear(k,s,p):
    v=pow(k,-1,p)
    # 1/(k-s*t)=sum_{r=0}^3 (s^r/k^(r+1)) t^r
    return [v*pow(s*v,r,p)%p for r in range(4)]


def check(p):
    assert p>=5 and all(p%d for d in range(2,isqrt(p)+1))
    eps=1 if p%6==1 else -1
    m=(p-eps)//6
    de=(1-eps)//2
    a,b,c=2*m-de,3*m-de,4*m-de
    assert 0<=a<b<c<p
    inv2=pow(2,-1,p)
    cj=[1,0,0,0];mj=[1,0,0,0]
    h2=h3=0
    factorial=[1]*p
    for j in range(1,p):factorial[j]=factorial[j-1]*j%p
    inverse_factorial=[1]*p
    inverse_factorial[-1]=pow(factorial[-1],-1,p)
    for j in range(p-1,0,-1):inverse_factorial[j-1]=inverse_factorial[j]*j%p
    counts=[0,0,0,0]
    leading_sums=[0,0,0,0]
    third_defect_weighted=0
    weighted_zero=[]
    for j in range(p):
        ell=int(j>a)+int(j>b)+int(j>c)
        counts[ell]+=1
        assert all(x==0 for x in mj[:ell]),(p,j,ell,mj)
        predicted=pow(-inv2,j,p)
        for s in (a,b,c):
            if j<=s:
                beta=factorial[s]*inverse_factorial[j]*inverse_factorial[s-j]%p
            else:
                beta=(-1)**(j-s-1)*factorial[s]*factorial[j-s-1]*inverse_factorial[j]%p
            predicted=predicted*beta%p
        assert mj[ell]==predicted and predicted!=0,(p,j,ell,mj,predicted)
        w=(6*j+1)%p
        leading_sums[ell]=(leading_sums[ell]+w*mj[ell])%p
        if w==0:weighted_zero.append((j,ell,mj[ell]))
        # Ratio M/C = 1 + 2H2 t^2 + 6H3 t^3 + O(t^4).
        assert mj[0]==cj[0] and mj[1]==cj[1],(p,j,mj,cj)
        assert (mj[2]-cj[2]-2*h2*cj[0])%p==0,(p,j,2,mj,cj,h2)
        correction=(2*h2*cj[1]+6*h3*cj[0])%p
        assert (mj[3]-cj[3]-correction)%p==0,(p,j,3,mj,cj,h2,h3)
        third_defect_weighted=(third_defect_weighted+w*correction)%p
        if j==p-1:break
        j1=j+1
        v=[1,0,0,0]
        for s in (a,b,c):
            v=mul(v,[(s-j)%p,1,0,0],p)
        v=mul(v,[(-inv2)%p,0,0,0],p)
        v=mul(v,[pow(j1,-2,p),0,0,0],p)
        mj=mul(mul(mj,v,p),inv_linear(j1,3,p),p)
        v_c=mul(v,[pow(j1,1,p),0,0,0],p)
        # C has j1*(j1-t)*(j1-2t); M has j1^2*(j1-3t).
        cj=mul(mul(mul(cj,v_c,p),inv_linear(j1,1,p),p),inv_linear(j1,2,p),p)
        h2=(h2+pow(j1,-2,p))%p
        h3=(h3+pow(j1,-3,p))%p
    assert len(weighted_zero)==1
    j0,k0,nonzero=weighted_zero[0]
    assert j0==(m if eps==1 else 5*m-1)
    assert k0==(0 if eps==1 else 3)
    assert nonzero!=0
    return dict(p=p,shell_counts=counts,shell_weighted_lead=leading_sums,weight_kernel=(j0,k0),third_weighted_defect=third_defect_weighted)


if __name__=='__main__':
    ps=primes_to(3000)
    rows=[check(p) for p in ps]
    print(f'TRIPLE CARRY SHELL + CLAUSEN THIRD JET: {len(rows)}/{len(ps)} PASS')
    for row in rows:
        if row['p'] in (5,7,11,13,17,19,31,73,127,211,373,1009,2999):print(row)
