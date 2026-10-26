#!/usr/bin/env python3
"""Exact finite-ring author checks for D25 corrected-Clausen two-stratum reduction.
External auxiliary arithmetic only; not native CM or project admission.
"""


def primes_1mod6(limit):
    for p in range(7,limit+1,6):
        if all(p%d for d in range(2,__import__('math').isqrt(p)+1)):
            yield p


def original_reflection(p):
    q=p**4
    r=[1]
    for n in range(1,p):
        r.append(r[-1]*(6*n-5)*(3*n-2)*pow(36*n*n,-1,q)%q)
    # Original double sum retains both ordered orientations.
    Q=0
    for a in range(p-1,-1,-1):
        b=p-a
        if b<p:
            # Store direct sum to avoid subtle suffix offset assumptions.
            Q+=sum((6*(a+t)+1)*r[a]*r[t] for t in range(b,p))
    Q%=q
    assert Q%(p*p)==0
    return Q//(p*p)


def harmonic(p):
    h=[0]*p
    for j in range(1,p):
        h[j]=(h[j-1]+pow(j,-1,p))%p
    return h


def reduce_reflection(p, with_diagnostics=False):
    m=(p-1)//6
    u=2*m
    q=p*p
    ph=p*pow(2,-1,q)%q
    fac=[1]*p
    shifted=[1]*p
    for n in range(1,p):
        fac[n]=fac[n-1]*n%q
        shifted[n]=shifted[n-1]*(n-ph)%q
    # Exactly two full modular inversions, followed by O(p) backward updates.
    invfac=[0]*p
    invshift=[0]*p
    invfac[-1]=pow(fac[-1],-1,q)
    invshift[-1]=pow(shifted[-1],-1,q)
    for n in range(p-1,0,-1):
        invfac[n-1]=invfac[n]*n%q
        invshift[n-1]=invshift[n]*(n-ph)%q
    H=[0]*p
    for j in range(1,p):
        H[j]=(H[j-1]+fac[j-1]*invfac[j])%p
    pow2=[1]*(u+1)
    inv2pow=[1]*(u+1)
    inverse_two=pow(2,-1,q)
    for j in range(1,u+1):
        pow2[j]=pow2[j-1]*2%q
        inv2pow[j]=inv2pow[j-1]*inverse_two%q

    # Low no-zero stratum, exact u_{0,j} mod p^2.
    low=[0]*(u+1)
    low[0]=1
    for j in range(1,m+1):
        low[j]=low[j-1]*(j-1-m)*(j-1-2*m)*fac[j-1]*invfac[j]*shifted[j-1]*invshift[j]%q

    # High double-zero stratum, exact u_{2,p-ell} mod p^2,
    # obtained by stripping the two literal Taylor zeros (i=m,2m).
    high=[0]*(u+1)
    for ell in range(1,u+1):
        rank=p-ell
        high[ell]=(2*(-1)**m*fac[m]*fac[2*m]*fac[rank-1-m]
                   *fac[rank-1-2*m]*invfac[rank]*invshift[rank])%q

    # Middle single-zero low stratum, sufficient mod p.
    mid=[0]*(u+1)
    for j in range(m+1,u+1):
        mid[j]=((-1)**(m+j+1)*fac[m]*fac[j-m-1]*fac[2*m]
                *invfac[2*m-j]*invfac[j]**2)%p

    # Logarithmic derivatives, only mod p needed in the p^4 tail.
    low_log=[0]*(u+1)
    for j in range(1,m+1):
        low_log[j]=(H[m]-H[m-j]+2*(H[2*m]-H[2*m-j])+3*H[j])%p
    high_log=[0]*(u+1)
    for ell in range(1,u+1):
        high_log[ell]=(H[m]+2*H[2*m]-H[ell+m]-2*H[ell+2*m]
                       +3*H[ell-1])%p

    f0=[0]*(u+1)
    f1mid=[0]*(u+1)
    g=[0]*(u+1)
    for j in range(1,u+1):
        f0[j]=low[j]*inv2pow[j]%q
        f1mid[j]=mid[j]*inv2pow[j]%p
        g[j]=high[j]*pow2[j]%q

    # Four prefix observers: P,Q in Z/p^2; R,S in F_p.
    P=Q=R=S=0
    T02=U02=Tcorr_low=Tcorr_middle=0
    for j in range(1,u+1):
        P=(P+g[j])%q
        Q=(Q+j*g[j])%q
        R=(R+g[j]*high_log[j])%p
        S=(S+j*g[j]*high_log[j])%p
        wp=((6*j+1)*P-6*Q)%q
        if j<=m:
            U02=(U02+f0[j]*P)%q
            T02=(T02+f0[j]*wp)%q
            Tcorr_low=(Tcorr_low+f0[j]*low_log[j]*wp
                         +f0[j]*((6*j+1)*R-6*S))%p
        else:
            Tcorr_middle=(Tcorr_middle+f1mid[j]*wp)%p

    Tcorr=(Tcorr_low+Tcorr_middle)%p
    scale=pow(2,-p,q)*pow(18,-1,q)%q
    answer=scale*(T02+p*(6*U02-Tcorr*pow(6,-1,p)))%q
    if with_diagnostics:
        without_middle=scale*(T02+p*(6*U02-Tcorr_low*pow(6,-1,p)))%q
        return answer, dict(m=m,T02=T02,U02=U02,T12plusT03=Tcorr,
                            Tcorr_low=Tcorr_low, Tcorr_middle=Tcorr_middle,
                            without_middle=without_middle,
                            low_log=low_log, high_log=high_log,
                            low=low,high=high,mid=mid)
    return answer


def independently_check_jets(p):
    m=(p-1)//6
    q=p*p
    u=2*m
    t0=p*pow(2,-1,q)%q
    arr=[[1,0,0,0]]
    def mul(a,b):
        out=[0]*4
        for i in range(4):
            for j in range(4-i):
                out[i+j]=(out[i+j]+a[i]*b[j])%q
        return out
    for n in range(1,p):
        a=n-1-m;b=n-1-2*m
        inv=pow(n*(n-t0)%q,-1,q)
        ratio=3*n*inv%q
        invden=[inv*pow(ratio,k,q)%q for k in range(4)]
        arr.append(mul(mul(arr[-1],[a*b,-2*a-b,2,0]),invden))
    value, diagnostic=reduce_reflection(p,True)
    for j in range(1,m+1):
        assert arr[j][0]==diagnostic['low'][j],('low',p,j)
        assert arr[j][1]%p==arr[j][0]*diagnostic['low_log'][j]%p,('lowlog',p,j)
    for j in range(m+1,2*m+1):
        assert arr[j][0]==0
        assert arr[j][1]%p==diagnostic['mid'][j],('mid',p,j)
    for ell in range(1,2*m+1):
        j=p-ell
        assert arr[j][0]==arr[j][1]==0
        assert arr[j][2]==diagnostic['high'][ell],('high',p,ell)
        assert arr[j][3]%p==arr[j][2]*diagnostic['high_log'][ell]%p,('highlog',p,ell)
    return value


def main():
    counts=0
    for p in primes_1mod6(997):
        result=reduce_reflection(p)
        original=original_reflection(p)
        assert result==original,(p,result,original)
        counts+=1
    for p in primes_1mod6(211):
        independently_check_jets(p)
    for p in (7,13,19,31,37,43):
        value, diag=reduce_reflection(p,True)
        print('p',p,'Q/p^2',value,'mod',p*p,
              'middle-jet contribution',diag['Tcorr_middle'],
              'omitting middle gives',diag['without_middle'])
    print('PASS:',counts,'primes up to 997; 22 independent rank/jet comparisons up to 211')


if __name__=='__main__':main()
