#!/usr/bin/env python3
"""GH-127 exact, independent F_(p^2) character-sum check.
All sums are directly enumerated; predicted values use independent Hasse coefficient extraction.
"""
from math import comb


def pair_add(a,b,p): return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def pair_neg(a,p): return (-a[0]%p,-a[1]%p)
def pair_mul(a,b,p): return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def pair_pow(a,n,p):
    v=(1,0)
    while n:
        if n&1:v=pair_mul(v,a,p)
        a=pair_mul(a,a,p);n//=2
    return v

def pair_inv(a,p):
    norm=(a[0]*a[0]-2*a[1]*a[1])%p
    if norm==0: raise ZeroDivisionError(a)
    z=pow(norm,-1,p)
    return (a[0]*z%p,(-a[1]*z)%p)

def hasse_derivatives(p,B):
    N=(p-1)//2
    d=N//2
    powers=[(1,0)]
    for _ in range(d):powers.append(pair_mul(powers[-1],B,p))
    deriv=[]
    for i in range(N+1):
        val=(0,0)
        for u in range(i,d+1):
            c=comb(N,u)*comb(N-u,u)*comb(u,i)%p
            term=powers[u-i]
            val=pair_add(val, (c*term[0]%p,c*term[1]%p),p)
        deriv.append(val)
    return deriv

def run(p,B):
    assert p%8==3 and p>=11
    q=p*p;N=(p-1)//2;d=N//2;e=(q-1)//2
    assert pow(2,(p-1)//2,p)==p-1, 'F_p[sqrt(2)] must be quadratic field'
    S=[(0,0) for _ in range(e)]
    zero_f=0
    root_power_sum=(0,0)
    boundary_sum=(0,0)
    for a in range(p):
        for b in range(p):
            x=(a,b)
            xx=pair_mul(x,x,p)
            f=pair_add(pair_add(pair_mul(xx,x,p),xx,p),pair_mul(B,x,p),p)
            if f==(0,0):
                zero_f+=1
                root_power_sum=pair_add(root_power_sum,pair_pow(x,e,p),p)
                continue
            boundary_sum=pair_add(boundary_sum,pair_pow(x,e,p),p)
            chi=pair_pow(f,e,p)
            assert chi in ((1,0),(p-1,0))
            t=pair_mul(x,pair_inv(f,p),p)
            v=chi
            for r in range(e):
                S[r]=pair_add(S[r],v,p)
                v=pair_mul(v,t,p)
    assert boundary_sum==pair_neg(root_power_sum,p), (p,B,boundary_sum,root_power_sum)
    deriv=hasse_derivatives(p,B)
    denom=[pow(comb(N,i)%p,-1,p) for i in range(N+1)]
    checked=nonzero=0
    for j in range(N+1):
        for i in range(N+1):
            r=i+j*p
            if r>=e:continue
            pred=pair_mul(deriv[i],pair_pow(deriv[j],p,p),p)
            pred=tuple((-v*denom[i]*denom[j])%p for v in pred)
            assert S[r]==pred,(p,B,r,S[r],pred)
            checked+=1
            if i>d or j>d:
                assert S[r]==(0,0)
                nonzero+=1
    blind=N+1
    print(f'p={p} B={B} q={q} singular_x={zero_f} visible_checked={checked} zero_band={nonzero} blind_r={blind} blind_value={S[blind]} S_1={S[1]} S_p={S[p]} S_pplus1={S[p+1]} corner_S_e={boundary_sum}')
    assert S[p]==pair_pow(S[1],p,p)
    return S

if __name__=='__main__':
    for p, B in [(11,(3,1)),(19,(4,2)),(43,(5,1)),(59,(7,3))]:
        run(p,B)
    V=run(11,(4,0))
    assert V[0]==V[1]==V[11]==(0,0)
    assert V[12]==(2,0)
    print('PASS_GH127_LUCAS_HASSE_TWO_DIGIT_AND_BLIND_SPOT')
