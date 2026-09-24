def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def terms_mod_p3(p):
    M=p**3
    C=1
    out=[1]
    for k in range(p-1):
        num=(2*k+1)*(3*k+1)*(3*k+2)
        den=36*(k+1)**3
        C=C*(num%M)*pow(den%M,-1,M)%M
        out.append(((6*(k+1)+1)*C)%M)
    return out

def verify_prime(p):
    m=(p-1)//6
    n=2*m
    M=p**3
    t=terms_mod_p3(p)
    inv2=pow(2,-1,M)
    inv3=pow(3,-1,M)
    delta=p*inv3%M
    d=1
    A=0
    B=0
    predicted=1
    special=None
    for k in range(1,n+1):
        num=(2*k-1)*(k-1-n)*(3*k-1)
        den=12*k**3
        d=d*(num%M)*pow(den%M,-1,M)%M
        ell=n-k+1
        ie=pow(ell,-1,M)
        A=(A+ie)%M
        B=(B+ie*ie)%M
        u=(6*k+1)*d%M
        factor=(1-delta*A+(delta*delta%M)*(A*A-B)%M*inv2)%M
        expanded=u*factor%M
        assert expanded==t[k], (p,k,expanded,t[k])
        predicted=(predicted+expanded)%M
        if k==m:
            assert u%p==0
            v=(u//p)%(p*p)
            special=(v,A)
            sp=(p*v-(p*p%M)*v*(A%M)*inv3)%M
            assert sp==expanded, (p,k,sp,expanded)
    assert predicted==sum(t[:n+1])%M
    assert special is not None

P=[p for p in range(13,5000) if isprime(p) and p%24 in (13,19)]
assert len(P)==166
for p in P:
    verify_prime(p)
print("PASS",len(P),sum(p%24==13 for p in P),sum(p%24==19 for p in P))
