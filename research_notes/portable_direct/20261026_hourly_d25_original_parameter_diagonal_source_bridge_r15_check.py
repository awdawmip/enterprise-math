#!/usr/bin/env python3
"""Author-only exact checks for the fixed-parameter original-series Green--Ward bridge.

The f and original r coefficient recurrences are evaluated independently.
All p-adic arithmetic uses Python integers, no floating point or native CM runtime.
"""
from fractions import Fraction


def primes():
    return [p for p in range(7, 212) if p % 6 == 1 and
            all(p % d for d in range(2, int(p**0.5) + 1))] + [733]


def f_terms(p, modulus=None):
    # At theta=-p/6: f_r=(1/6)_r(1/3)_r/(r!)^2.
    out = [Fraction(1) if modulus is None else 1]
    for k in range(p-1):
        a, b = (6*k+1)*(3*k+1), 18*(k+1)**2
        nxt = out[-1]*Fraction(a,b) if modulus is None else \
            out[-1]*a*pow(b,-1,modulus)%modulus
        out.append(nxt)
    return out


def r_terms(p, modulus=None):
    # Independent original hypergeometric recurrence, r_r=2^{-r} f_r.
    out = [Fraction(1) if modulus is None else 1]
    for k in range(p-1):
        a, b = (6*k+1)*(3*k+1), 36*(k+1)**2
        nxt = out[-1]*Fraction(a,b) if modulus is None else \
            out[-1]*a*pow(b,-1,modulus)%modulus
        out.append(nxt)
    return out


def genuine_edge(n,m,p,f,beta,theta):
    # Exact four-origin cutoff, normalized by p^2; beta_high=f_high/p^2.
    if n >= 0:
        return (2*(m+theta)**2*beta[p-n-1]
              -(6*m*m-8*m*theta+2*theta*theta)*f[2*m-n]*beta[4*m])
    return ((20*m*m-14*m*theta+2*theta*theta)*f[-n]*beta[p-1]
          +(2*m*theta-2*theta*theta)*f[2*m]*beta[p-(2*m+n+1)])


def run_mod(p, digits=3):
    m, N = (p-1)//6, (p-1)//3-1
    L, q, large = -N, p**digits, p**(digits+2)
    fbig, rbig = f_terms(p,large), r_terms(p,large)
    f = [x%q for x in fbig]
    beta = [0]*p
    for k in range(2*m+1,p):
        assert fbig[k]%(p*p) == 0 and fbig[k]%(p**3) != 0
        beta[k] = fbig[k]//(p*p)%q
    assert fbig[2*m]%p == 0 and fbig[2*m]%(p*p) != 0
    inv2 = pow(2,-1,q)
    theta = -p*pow(6,-1,q)%q
    M0, M1 = [0]*(2*N+2), [0]*(2*N+2)
    ix = lambda n:n-L
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n = ell-j
            v = f[j]*beta[p-ell]%q
            M0[ix(n)] = (M0[ix(n)]+v)%q
            M1[ix(n)] = (M1[ix(n)]+j*v)%q
    Z = [(2*M1[ix(n)]-(p-n)*M0[ix(n)])%q for n in range(L,N+2)]
    assert Z[ix(N+1)] == 0
    edge={}
    for n in range(L,N+1):
        edge[n] = genuine_edge(n,m,p,f,beta,theta)%q
        lhs=((p-n)*Z[ix(n)]-(p-n-inv2)*Z[ix(n+1)])%q
        assert lhs == edge[n], ('genuine-face-ward',p,n,lhs,edge[n])
    lam={0:0}
    weight=lambda n:pow(2,n,q)
    for n in range(0,L,-1):
        lam[n-1]=((p-n)*lam[n]-weight(n))*2*pow(2*(p-n)+1,-1,q)%q
    delta=(weight(L)-(p-L)*lam[L])%q
    weighted_z=sum(weight(n)*Z[ix(n)] for n in range(L,1))%q
    via_sources=(sum(lam[n]*edge[n] for n in range(L,0))+delta*Z[ix(L)])%q
    assert weighted_z == via_sources, ('adjoint',p)
    U=sum(weight(n)*M0[ix(n)] for n in range(L,1))%q
    K=sum(weight(n)*M1[ix(n)] for n in range(L,1))%q
    low_direct=(sum(weight(n)*(6*p+1-6*n)*M0[ix(n)]
                    for n in range(L,1))*pow(2,1-p,q))%q
    low_source=(pow(2,1-p,q)*(U+12*K-6*via_sources))%q
    assert low_direct == low_source, ('original-source',p)
    # Genuine f-based high--high, independently of the low--high source.
    high=(p*p*sum((6*(a+b)+1)*pow(2,-a-b,q)*beta[a]*beta[b]
               for a in range(2*m+1,p)
               for b in range(max(2*m+1,p-a),p)))%q
    # Original ordered Q from a second coefficient recurrence, no Ward or jets.
    Q=sum((6*(a+b)+1)*rbig[a]*rbig[b]
           for a in range(1,p) for b in range(max(1,p-a),p))%large
    assert Q%(p*p) == 0
    original=Q//(p*p)%q
    assert (low_source+high)%q == original, ('ordered-original-Q',p)
    edge_scalar=(-6*pow(2,1-p,q)*delta*Z[ix(L)])%q
    return dict(p=p, original=original, low=low_source, high=high,
                adjoint_delta_mod_p=delta%p,
                normalized_left_rank_over_p=(Z[ix(L)]//p)%p,
                original_face_port=edge_scalar)


def run_rational(p):
    m, N = (p-1)//6, (p-1)//3-1
    L=-N
    f,r = f_terms(p),r_terms(p)
    beta=[x/(p*p) for x in f]
    theta=Fraction(-p,6)
    assert all(f[k]==2**k*r[k] for k in range(p))
    M0={n:Fraction(0) for n in range(L,N+2)}
    M1=M0.copy()
    for j in range(1,2*m+1):
        for ell in range(1,2*m+1):
            n=ell-j
            v=f[j]*beta[p-ell]
            M0[n]+=v;M1[n]+=j*v
    Z={n:2*M1[n]-(p-n)*M0[n] for n in M0}
    edges={n:genuine_edge(n,m,p,f,beta,theta) for n in range(L,N+1)}
    for n in range(L,N+1):
        assert (p-n)*Z[n]-(Fraction(p-n)-Fraction(1,2))*Z[n+1] == edges[n]
    lam={0:Fraction(0)}
    for n in range(0,L,-1):
        lam[n-1]=((p-n)*lam[n]-Fraction(2)**n)/(
            Fraction(p-n)+Fraction(1,2))
    delta=Fraction(2)**L-(p-L)*lam[L]
    source=(sum(Fraction(2)**n*(M0[n]+12*M1[n]) for n in range(L,1))
            -6*sum(lam[n]*edges[n] for n in range(L,0))-6*delta*Z[L])
    low=Fraction(2)**(1-p)*source
    direct_low=sum((6*(j+p-ell)+1)*r[j]*r[p-ell]*2
                   for j in range(1,2*m+1) for ell in range(1,j+1))/(p*p)
    assert low==direct_low
    high=sum((6*(a+b)+1)*r[a]*r[b]
             for a in range(2*m+1,p)
             for b in range(max(2*m+1,p-a),p))/(p*p)
    Q=sum((6*(a+b)+1)*r[a]*r[b]
          for a in range(1,p) for b in range(max(1,p-a),p))/(p*p)
    assert low+high==Q
    return 2*N+1


def main():
    rational=sum(run_rational(p) for p in (7,13))
    results=[run_mod(p) for p in primes()]
    assert len(results)==23
    special={x['p']:x for x in results}
    assert special[13]['original']==104 and special[13]['high']==169
    assert special[733]['original']==99531942
    assert special[733]['low']==28072505
    assert special[733]['high']==71459437
    assert special[733]['adjoint_delta_mod_p']==0
    assert special[733]['normalized_left_rank_over_p']==388
    assert special[733]['original_face_port']==124113759
    print('PASS exact rational original-series sources:',rational,'ranks for p=7,13')
    print('PASS modular:',sum(2*((p-1)//3-1)+1 for p in primes()),
          'genuine-edge rankwise checks + 23 adjoint + 23 independent Q checks')
    for p in (7,13,733):print(special[p])

if __name__=='__main__':main()
