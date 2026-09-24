def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d=3
    while d*d<=n:
        if n%d==0: return False
        d+=2
    return True

def terms_mod_p3(p):
    mod=p**3
    C=1
    out=[1]
    for k in range(p-1):
        num=(2*k+1)*(3*k+1)*(3*k+2)
        den=36*(k+1)**3
        C=C*(num%mod)*pow(den%mod,-1,mod)%mod
        out.append(((6*(k+1)+1)*C)%mod)
    return out

def verify_prime(p):
    m=(p-1)//6
    pp=p*p
    t=terms_mod_p3(p)
    b=[(t[2*m+r]//p)%pp for r in range(1,m+1)]
    q=1
    H=0
    predicted_sum=0
    for s in range(m):
        if s:
            r=s
            num0=(6*r+5)*(6*r+1)*(3*r)*(3*r+1)
            den0=4*(6*r-1)*(3*r+2)**3
            R0=(num0%pp)*pow(den0%pp,-1,pp)%pp
            D=0
            for c,d in [(2,6*r+5),(2,6*r+1),(1,3*r),(1,3*r+1),(-2,6*r-1),(-3,3*r+2)]:
                D=(D+c*pow(d%p,-1,p))%p
            pred=b[s-1]*R0*(1+p*D)%pp
            assert pred==b[s], (p,r,b[s],pred)
            q=q*R0%pp
            H=(H+D)%p
        predicted_sum=(predicted_sum+b[0]*q*(1+p*H))%pp
    assert predicted_sum==sum(b)%pp, (p,predicted_sum,sum(b)%pp)
    n=2*m+1
    fact=[1]*p
    for j in range(1,p):
        fact[j]=fact[j-1]*j%p
    beta=(-10*fact[2*n]*pow(fact[n],-5,p)*pow(pow(216,n,p),-1,p))%p
    assert b[0]%p==beta, (p,b[0]%p,beta)

P=[p for p in range(13,5000) if isprime(p) and p%24 in (13,19)]
assert len(P)==166
for p in P:
    verify_prime(p)
print("PASS",len(P),sum(p%24==13 for p in P),sum(p%24==19 for p in P))
