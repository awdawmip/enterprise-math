#!/usr/bin/env python3
"""
Exact regression for:
D25 LIFT — lawful fixed-p terminal-band cutoff and universal curvature-defect no-go.
Finite regression only; not an all-prime proof.
"""
from math import isqrt

def primes_below(n):
    out=[]
    for x in range(2,n):
        ok=True
        for d in range(2,isqrt(x)+1):
            if x%d==0:
                ok=False
                break
        if ok:
            out.append(x)
    return out

def inv(a,m): return pow(a % m,-1,m)

def B_sequence_mod(p):
    M=p**3
    B=[1]
    cur=1
    for k in range(p-1):
        cur=(cur*((6*k+1)*(3*k+1)%M)*inv(36*(k+1)*(k+1),M))%M
        B.append(cur)
    return B

def y_formula(p,r):
    y=inv(10,p)
    for s in range(1,r):
        y=y*(36*s*s)%p
        y=y*inv((6*s+5)*(3*s+2),p)%p
    return y

def lam(p,s):
    return (s*s*(6*s+1))%p*inv((s+1)*(2*s+1)*(3*s+2),p)%p

def mu(p,s):
    num=(2*s+1)*(3*s+1)*(3*s+2)*(6*s+7)**2
    den=36*(s+1)*(6*s+1)*(s+2)*(2*s+3)*(3*s+5)
    return (num%p)*inv(den,p)%p

def kappa(p,s):
    return (36*s*s)%p*inv((6*s+5)*(3*s+2),p)%p

def D_formula(p,s):
    return (kappa(p,s)*((kappa(p,s+1)-lam(p,s+1))%p)-mu(p,s)*((kappa(p,s)-lam(p,s))%p))%p

def Q_value(p,gs,hs):
    M2=p*p
    assert gs%p==0
    G=(gs//p)%M2
    d=(G*(hs%M2)-1)%M2
    assert d%p==0
    return (d//p)%p

def check(p):
    m=(p-1)//6
    M3=p**3
    M2=p*p
    B=B_sequence_mod(p)
    g=sum(B)%M3
    h=sum(((12*k+1)%M3)*B[k] for k in range(p))%M3
    assert g%p==0
    hbar=h%p
    assert hbar!=0
    top_g=sum(B[p-r] for r in range(1,m+1))%M3
    top_h=sum(((12*(p-r)+1)%M3)*B[p-r] for r in range(1,m+1))%M3
    gs=(g-top_g)%M3
    hs=(h-top_h)%M3
    assert gs%p==0
    qs=[Q_value(p,gs,hs)]
    ys={}
    for s in range(1,m+1):
        k=p-s
        bk=B[k]
        assert bk%(p*p)==0
        y=(bk//(p*p))%p
        assert y==y_formula(p,s)
        assert y!=0
        ys[s]=y
        gs=(gs+bk)%M3
        hs=(hs+((12*k+1)%M3)*bk)%M3
        q=Q_value(p,gs,hs)
        assert (q-qs[-1])%p == hbar*y%p
        qs.append(q)
    G=(g//p)%M2
    direct=(G*(h%M2)-1)%M2
    assert direct%p==0
    Delta=(direct//p)%p
    assert qs[-1]==Delta
    if m>=3:
        U={s:(qs[s]-qs[s-1])%p for s in range(1,m+1)}
        V={s:(U[s+1]-lam(p,s)*U[s])%p for s in range(1,m)}
        delta={s:(V[s+1]-mu(p,s)*V[s])%p for s in range(1,m-1)}
        for s,dv in delta.items():
            assert dv == hbar*ys[s]%p*D_formula(p,s)%p
        st=m-2
        terminal=delta[st]
        expected=(-8069*inv(9604,p))%p*hbar%p*ys[m]%p
        assert terminal==expected
        assert terminal!=0
        if m>=4:
            pen=m-3
            gamma_pen=1209*inv(28,p)%p
            pair=(gamma_pen*delta[pen]+terminal)%p
            expected_pair=(-11913844*inv(26374985,p))%p*hbar%p*ys[m]%p
            assert pair==expected_pair
            assert pair!=0

def main():
    targets=[p for p in primes_below(5000) if p%24 in (13,19)]
    counts={13:0,19:0}
    failures=[]
    for p in targets:
        counts[p%24]+=1
        try: check(p)
        except Exception as e: failures.append((p,repr(e)))
    print('targets',len(targets))
    print('class13',counts[13])
    print('class19',counts[19])
    print('failures',failures)
    assert len(targets)==166
    assert counts[13]==83 and counts[19]==83
    assert not failures

if __name__=='__main__': main()
