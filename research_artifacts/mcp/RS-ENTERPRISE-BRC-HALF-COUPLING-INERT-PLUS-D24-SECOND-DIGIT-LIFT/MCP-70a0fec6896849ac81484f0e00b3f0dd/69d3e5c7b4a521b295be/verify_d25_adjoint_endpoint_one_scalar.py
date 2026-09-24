from math import comb, isqrt

def primes_upto(n):
    sieve=[True]*(n+1)
    sieve[0:2]=[False,False]
    for q in range(2,isqrt(n)+1):
        if sieve[q]:
            for k in range(q*q,n+1,q):
                sieve[k]=False
    return [q for q,ok in enumerate(sieve) if ok]

def check(p):
    assert p % 24 in (13,19)
    m=(p-1)//6
    inv=lambda x: pow(x % p,-1,p)

    a=[0]*(m+1); a[0]=1
    for j in range(m):
        a[j+1]=a[j]*(m-j)*(2*m-j)*inv(2*(j+1)*(j+1)) % p

    y=[0]*(m+1); y[1]=inv(10)
    for r in range(1,m):
        y[r+1]=y[r]*2*r*r*inv((r+m+1)*(r+2*m+1)) % p

    f=[0]*(m+2)
    for r in range(1,m+1):
        f[r]=sum((6*(j-r)+1)*a[j] for j in range(r,m+1)) % p
    assert f[m] == a[m] % p and f[m+1] == 0
    for r in range(1,m):
        assert (f[r]-2*f[r+1]+f[r+2]) % p == (a[r]+5*a[r+1]) % p

    u=[0]*(m+1)
    for r in range(1,m+1):
        u[r]=(f[r]+(r+m)*(r+2*m)*u[r-1])*inv(2*r*r) % p

    c_direct=sum((6*(j-r)+1)*a[j]*y[r]
                 for j in range(1,m+1) for r in range(1,j+1)) % p
    assert c_direct == 2*m*m*y[m]*u[m] % p

    endpoint=inv(18*a[m]*(comb(3*m,m) % p))
    assert 2*m*m*y[m] % p == endpoint
    assert c_direct == u[m]*endpoint % p

    t=[0]*(m+1); t[0]=1
    for h in range(m):
        t[h+1]=t[h]*(2*h+1)*(3*h+1)*(3*h+2)*inv(36*(h+1)**3) % p
    prefix=0; c_prefix=0
    for s in range(1,m+1):
        h=s-1
        prefix=(prefix+(6*h+1)*t[h]) % p
        c_prefix=(c_prefix+a[s]*prefix*inv(12*s*s*t[s])) % p
    assert c_direct == c_prefix

def main():
    targets=[p for p in primes_upto(4999) if p % 24 in (13,19)]
    failures=[]
    for p in targets:
        try:
            check(p)
        except Exception as exc:
            failures.append((p,repr(exc)))
    print("target_primes",len(targets))
    print("class13",sum(p % 24 == 13 for p in targets))
    print("class19",sum(p % 24 == 19 for p in targets))
    print("failures",len(failures))
    if failures:
        print(failures[:20])
        raise SystemExit(1)

if __name__=="__main__":
    main()
