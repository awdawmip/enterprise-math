"""Exact finite-ring check of the corrected Clausen parameter-jet reflected tail.
Pure Python stdlib. Author-side check, not independent review or native CM.
"""
def primes_1mod6(limit):
    for p in range(7, limit + 1, 6):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            yield p

def mul(a,b,mod):
    z=[0]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<4:z[i+j]=(z[i+j]+x*y)%mod
    return z

def corrected_jets(p):
    """u[n][k] = [t^k] (-m-t)_n(-2m-2t)_n / ((1-p/2-3t)_n n!), mod p^2."""
    m=(p-1)//6; q=p*p
    halfp=p*pow(2,-1,q)%q
    u=[[1,0,0,0]]
    for n in range(p-1):
        a=n-m; b=n-2*m
        num=[a*b,-2*a-b,2,0]
        d0=(n+1-halfp)*(n+1)%q
        d1=-3*(n+1)
        iv=pow(d0,-1,q)
        beta=-d1*iv%q
        inv=[iv*pow(beta,k,q)%q for k in range(4)]
        u.append(mul(mul(u[-1],num,q),inv,q))
    return u

def original_source(p):
    """r[n] = (1/6)_n(1/3)_n / (2^n n!^2), modulo p^4."""
    q=p**4
    r=[1]
    for n in range(p-1):
        r.append(r[-1]*(6*n+1)*(3*n+1)*pow(36*(n+1)**2,-1,q)%q)
    return r

def check(p):
    m=(p-1)//6; q=p*p
    r=original_source(p)
    raw=sum((6*(a+b)+1)*r[a]*r[b] for a in range(p)
            for b in range(p) if a+b>=p)%(p**4)
    assert raw%q==0
    observed=raw//q
    u=corrected_jets(p)
    inv2=pow(2,-1,q); inv6=pow(6,-1,q); inv18=pow(18,-1,q)
    low=middle=0
    for j in range(1,2*m+1):
        part=0
        for ell in range(1,j+1):
            n=p-ell; alpha=6*(j-ell)+1
            a,b=u[j][0],u[j][1]
            c,d=u[n][2],u[n][3]
            base=alpha*a*c
            nextdigit=p*(6*a*c-alpha*inv6*(b*c+a*d))
            part+=pow(inv2,j+n,q)*(base+nextdigit)
        part=part*inv18%q
        if j<=m:low=(low+part)%q
        else:middle=(middle+part)%q
    predicted=(low+middle)%q
    assert observed==predicted,(p,observed,predicted,low,middle)
    assert middle%p==0,(p,middle)
    return p,observed,low,middle

if __name__=="__main__":
    results=[check(p) for p in primes_1mod6(211)]
    for row in results:
        if row[0] in (7,13,19,31,37,43,73,103,127,157,199,211):
            print("p, Q/p^2 mod p^2, low, middle =",*row)
    print("PASS:",len(results),"primes (p=1 mod 6; 7<=p<=211)")
