#!/usr/bin/env python3
"""D25 V original finite-Clausen cutoff: exact p=13/19 (mod24) test to 1000."""
def primes(n):
    a=[True]*(n+1); a[:2]=[False,False]
    for d in range(2,int(n**.5)+1):
        if a[d]:
            for k in range(d*d,n+1,d): a[k]=False
    return [p for p in range(n+1) if a[p]]

def exact_case(p):
    mod=p**3
    # d_n=(1/8)_n(3/8)_n/[9^n(n!)^2], denominator 576(n+1)^2
    d=[1]
    for n in range(p-1):
        d.append(d[-1]*(8*n+1)*(8*n+3)*pow(576*(n+1)**2,-1,mod)%mod)
    M=sum(d)%mod
    N=sum(n*x for n,x in enumerate(d))%mod
    H=(M+16*N)%mod
    Q=sum((1+8*(i+j))*d[i]*d[j]
          for i in range(p) for j in range(p-i,p))%mod
    V_square=(M*H-Q)%mod
    # Independent original C_n=(4n)!/[(n!)^4 2304^n] recurrence.
    c=1; V_original=0
    for n in range(p):
        V_original=(V_original+(8*n+1)*c)%mod
        if n+1<p:
            c=c*(4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)*pow(2304*(n+1)**4,-1,mod)%mod
    assert V_square==V_original==p%mod, (p,V_square,V_original)
    assert Q%p==0, (p,Q)
    if p%24==19:
        assert Q%p**2==0, (p,Q)
    elif p%24==13:
        assert M%p**2==0 and Q%p**2==p**2-p, (p,M,Q)
        root=(5*p-1)//8
        assert (p-1)//2<root and (p+1)//2<=root
    return {"p":p,"M_mod_p2":M%p**2,"H_mod_p":H%p,
            "Q_mod_p2":Q%p**2,"V_mod_p3":V_original}

def main():
    rows=[exact_case(p) for p in primes(1000) if p%24 in (13,19)]
    a=[r for r in rows if r["p"]%24==13]
    b=[r for r in rows if r["p"]%24==19]
    assert len(a)==22 and len(b)==23
    print("PASS",len(rows),"p=13(mod24)",len(a),"p=19(mod24)",len(b))
    for p in (13,19,37,43,61,67,373):
        print(next(row for row in rows if row["p"]==p))

if __name__=="__main__":
    main()
