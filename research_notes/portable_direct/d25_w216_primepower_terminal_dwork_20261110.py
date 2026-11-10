"""Exact author-side D25 prime-power terminal theorem and finite Dwork probe.
No floats; factorial/binomial integers and p-unit inverses only.
PROVED theorem checker + UNPROVED experimental witness are distinct claims.
"""
from math import comb

def vp(n,p):
    if n==0: return 10**12
    t=0
    while n%p==0:
        n//=p
        t+=1
    return t

def test_terminal(p,r):
    n=p**r
    M=p**(3*r+1)
    inv216=pow(216,-1,M)
    z=1
    W=S=0
    for k in range(n):
        B=comb(2*k,k)**2*comb(3*k,k)
        W=(W+(6*k+1)*B*z)%M
        if k<n-1:
            t=vp(k+1,p)
            assert vp(B,p)>=3*t
            u=(k+1)//p**t
            term=-(k-1)*(6*k+5)*(B//p**(2*t))*pow(3*u*u,-1,M)
            S=(S+term*z)%M
        z=z*inv216%M
    N=n-1
    B=comb(2*N,N)**2*comb(3*N,N)
    assert vp(B,p)==3*r
    assert ((B//p**(3*r))*pow(216,-N,p))%p==p-1
    boundary=(7-6*n)*B*pow(216,-N,M)%M
    assert (W-S-boundary)%M==0
    assert (W-S+7*p**(3*r))%M==0
    return (p,r,(W-S)%M)

def W(p,n,mod):
    z=1
    ans=0
    inv=pow(216,-1,mod)
    for k in range(n):
        ans=(ans+(6*k+1)*comb(2*k,k)**2*comb(3*k,k)*z)%mod
        z=z*inv%mod
    return ans

def test_dwork(p,r):
    mod=p**(3*r+1)
    chi=1 if p%3==1 else -1
    base=W(p,p,p**4)
    assert (base-chi*p)%p**3==0
    c=((base-chi*p)%p**4)//p**3
    older=W(p,p**(r-1),mod)
    newer=W(p,p**r,mod)
    defect=(newer-chi*p*older)%mod
    assert defect==c*p**(3*r), (p,r,defect,c)
    return (p,r,c)

if __name__=="__main__":
    exact_pairs=[(5,1),(5,2),(5,3),(7,1),(7,2),(7,3),
                 (11,1),(11,2),(11,3),(13,1),(13,2),(13,3),
                 (19,1),(19,2),(31,1),(31,2)]
    for x in exact_pairs: print("THEOREM_PASS",test_terminal(*x))
    experimental=[(p,2) for p in (5,7,11,13,17,19,23,29,31,37)]
    experimental += [(p,3) for p in (5,7,11,13)]
    experimental += [(p,4) for p in (5,7)]
    for x in experimental: print("FINITE_ONLY",test_dwork(*x))
