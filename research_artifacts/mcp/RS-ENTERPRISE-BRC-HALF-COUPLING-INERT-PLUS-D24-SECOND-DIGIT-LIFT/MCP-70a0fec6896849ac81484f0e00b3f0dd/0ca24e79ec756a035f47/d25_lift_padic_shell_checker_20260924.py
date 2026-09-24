def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def legendre(a,p):
    x=pow(a%p,(p-1)//2,p)
    return -1 if x==p-1 else x

def terms_mod_p3(p):
    mod=p**3
    C=1
    out=[1]
    for k in range(0,p-1):
        num=(2*k+1)*(3*k+1)*(3*k+2)
        den=36*(k+1)**3
        C=C*(num%mod)*pow(den%mod,-1,mod)%mod
        out.append(((6*(k+1)+1)*C)%mod)
    return out

def verify_prime(p):
    assert p%24 in (13,19)
    m=(p-1)//6
    mod=p**3
    t=terms_mod_p3(p)
    for k,tk in enumerate(t):
        base=(2*k)//p+(3*k)//p
        if base>=3:
            assert tk==0, (p,k,base,tk)
        elif base==2:
            assert tk%(p*p)==0, (p,k,base,tk)
        elif base==1:
            assert tk%p==0, (p,k,base,tk)
    assert all(t[k]==0 for k in range(4*m+1,6*m+1))
    f=[(t[3*m+r]//(p*p))%p for r in range(1,m+1)]
    chi=legendre(6,p)
    f1=(4*pow(9,-1,p)*chi)%p
    assert f[0]==f1, (p,f[0],f1)
    for r in range(1,m):
        num=r*(6*r-1)*(6*r+1)*(3*r+2)
        den=9*(2*r+1)**3*(3*r-1)
        expected=f[r-1]*(num%p)*pow(den%p,-1,p)%p
        assert f[r]==expected, (p,r,f[r],expected)
    q=f1
    K=q
    for r in range(1,m):
        num=r*(6*r-1)*(6*r+1)*(3*r+2)
        den=9*(2*r+1)**3*(3*r-1)
        q=q*(num%p)*pow(den%p,-1,p)%p
        K=(K+q)%p
    direct=sum(f)%p
    assert K==direct, (p,K,direct)
    S0=sum(t[0:2*m+1])%mod
    S1=sum(t[2*m+1:3*m+1])%mod
    S2=sum(t[3*m+1:4*m+1])%mod
    S3=sum(t[4*m+1:6*m+1])%mod
    W=sum(t)%mod
    assert S3==0
    assert S2==(p*p*direct)%mod
    assert W==(S0+S1+p*p*direct)%mod
    return True

P=[p for p in range(13,5000) if isprime(p) and p%24 in (13,19)]
assert len(P)==166
for p in P:
    verify_prime(p)
print("PASS", len(P), sum(p%24==13 for p in P), sum(p%24==19 for p in P))
