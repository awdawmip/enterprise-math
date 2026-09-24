from math import isqrt

def primes_upto(n):
    s=[True]*(n+1); s[0:2]=[False,False]
    for q in range(2,isqrt(n)+1):
        if s[q]:
            for k in range(q*q,n+1,q): s[k]=False
    return [q for q,ok in enumerate(s) if ok]

def deriv(d,p):
    out={}
    for n,c in d.items():
        if n: out[n-1]=(out.get(n-1,0)+n*c)%p
    return out

def add(out,d,shift,scale,p):
    for n,c in d.items(): out[n+shift]=(out.get(n+shift,0)+scale*c)%p

def check(p):
    assert p%24 in (13,19)
    m=(p-1)//6; inv=lambda x:pow(x%p,-1,p)
    a=[0]*(m+1); a[0]=1
    for j in range(m):
        a[j+1]=a[j]*(m-j)*(2*m-j)*inv(2*(j+1)*(j+1))%p
    y=[0]*(m+1); y[1]=inv(10)
    for r in range(1,m):
        y[r+1]=y[r]*2*r*r*inv((r+m+1)*(r+2*m+1))%p
    A={j:a[j] for j in range(m+1)}; G={-r:y[r] for r in range(1,m+1)}
    H={}
    for i,ci in A.items():
        for j,cj in G.items(): H[i+j]=(H.get(i+j,0)+ci*cj)%p

    # Universal symmetric-square Laurent identity.
    H1=deriv(H,p); H2=deriv(H1,p); H3=deriv(H2,p)
    lhs={}
    add(lhs,H3,3,18,p); add(lhs,H3,2,-36,p)
    add(lhs,H2,2,81,p); add(lhs,H2,1,-108,p)
    add(lhs,H1,1,58,p); add(lhs,H1,0,-36,p); add(lhs,H,0,2,p)
    q={0:(-inv(18))%p,-m:(2*m*m*y[m])%p}; q1=deriv(q,p); A1=deriv(A,p)
    rhs={}
    for i,ci in q.items():
        for j,cj in A1.items(): rhs[i+j]=(rhs.get(i+j,0)-54*ci*cj)%p
    for i,ci in A.items():
        for j,cj in q1.items(): rhs[i+j]=(rhs.get(i+j,0)-18*ci*cj)%p
    for k in set(lhs)|set(rhs): assert lhs.get(k,0)%p==rhs.get(k,0)%p

    Hp=[H.get(h,0)%p for h in range(m)]+[0]
    # Original 3F2 coefficients t_h and first-order transport.
    t=[0]*(m+1); t[0]=1
    for h in range(m):
        t[h+1]=t[h]*(2*h+1)*(3*h+1)*(3*h+2)*inv(36*(h+1)**3)%p
        lhsr=((2*h+1)*(3*h+1)*(3*h+2)*Hp[h]-36*(h+1)**3*Hp[h+1])%p
        assert lhsr==3*(h+1)*a[h+1]%p
    # Closed tail formula.
    for h in range(m):
        tail=sum(a[s]*inv(12*s*s*t[s]) for s in range(h+1,m+1))%p
        assert Hp[h]==t[h]*tail%p
    # Prefix transform for C_m.
    prefix=0; cp=0
    for s in range(1,m+1):
        h=s-1; prefix=(prefix+(6*h+1)*t[h])%p
        cp=(cp+a[s]*inv(12*s*s*t[s])*prefix)%p
    cd=sum((6*(j-r)+1)*a[j]*y[r] for j in range(1,m+1) for r in range(1,j+1))%p
    assert cp==cd

def main():
    targets=[p for p in primes_upto(4999) if p%24 in (13,19)]
    failures=[]
    for p in targets:
        try: check(p)
        except Exception as exc: failures.append((p,repr(exc)))
    print('target_primes',len(targets)); print('failures',len(failures))
    if failures: print(failures[:20]); raise SystemExit(1)

if __name__=='__main__': main()
