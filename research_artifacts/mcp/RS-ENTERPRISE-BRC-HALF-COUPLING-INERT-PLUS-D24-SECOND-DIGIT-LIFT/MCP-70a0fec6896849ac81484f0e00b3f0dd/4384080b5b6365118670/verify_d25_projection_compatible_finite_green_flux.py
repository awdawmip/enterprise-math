from math import isqrt

def primes_upto(n):
    s=[True]*(n+1); s[0:2]=[False,False]
    for q in range(2,isqrt(n)+1):
        if s[q]:
            for k in range(q*q,n+1,q): s[k]=False
    return [q for q,ok in enumerate(s) if ok]

def check(p):
    assert p%24 in (13,19)
    m=(p-1)//6
    inv=lambda x: pow(x%p,-1,p)
    a=[0]*(m+1); a[0]=1
    for j in range(m):
        a[j+1]=a[j]*(m-j)*(2*m-j)*inv(2*(j+1)*(j+1))%p
    y=[0]*(m+1); y[1]=inv(10)
    for r in range(1,m):
        y[r+1]=y[r]*2*r*r*inv((r+m+1)*(r+2*m+1))%p

    # L_m G_m sources.
    q={0:(-(m+1)*(2*m+1)*y[1])%p, -m:(2*m*m*y[m])%p}
    for r in range(1,m):
        q[-r]=(2*r*r*y[r]-(m+r+1)*(2*m+r+1)*y[r+1])%p
    assert q[0]==(-inv(18))%p
    assert all(q[-r]==0 for r in range(1,m))

    # Euler Wronskian J=A theta G_m-(theta A)G_m.
    J={}
    for j in range(m+1):
        for r in range(1,m+1):
            h=j-r
            J[h]=(J.get(h,0)-(j+r)*a[j]*y[r])%p

    def rhs(h):
        v=0
        if 0<=h<=m: v+=a[h]*q[0]
        jj=h+m
        if 0<=jj<=m: v+=a[jj]*q[-m]
        return v%p

    for h in range(-m,m+1):
        lhs=(2*h*J.get(h,0)+(3*m-h+1)*J.get(h-1,0))%p
        assert lhs==rhs(h)

    # Adjacent-diagonal h=-1 consequence.
    adj=sum((2*j+1)*a[j]*y[j+1] for j in range(m))%p
    assert adj==(inv(9)-4*m*m*a[m]*y[m])%p

    # Projection-compatible finite G_m gives the same C_m.
    c_proj=0
    for h in range(m):
        H=sum(a[h+r]*y[r] for r in range(1,m-h+1))%p
        c_proj=(c_proj+(6*h+1)*H)%p
    c_double=sum((6*(j-r)+1)*a[j]*y[r] for j in range(1,m+1) for r in range(1,j+1))%p
    assert c_proj==c_double

def main():
    targets=[p for p in primes_upto(4999) if p%24 in (13,19)]
    failures=[]
    for p in targets:
        try: check(p)
        except Exception as exc: failures.append((p,repr(exc)))
    print('target_primes',len(targets))
    print('class13',sum(p%24==13 for p in targets))
    print('class19',sum(p%24==19 for p in targets))
    print('failures',len(failures))
    if failures:
        print(failures[:20]); raise SystemExit(1)

if __name__=='__main__': main()
