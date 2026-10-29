#!/usr/bin/env python3
"""GH-104 portable exact check: Hasse-square moment and alternating discriminant.

Uses only Python standard library; arithmetic is in F_p. Algebraic proof is
separately documented; finite checks are verification, not proof of universality.
"""
from math import comb


def add(a, b, p):
    z = [0] * max(len(a), len(b))
    for i, c in enumerate(a): z[i] = (z[i] + c) % p
    for i, c in enumerate(b): z[i] = (z[i] + c) % p
    return trim(z)


def trim(v):
    out = v[:]
    while len(out) > 1 and out[-1] == 0: out.pop()
    return out


def mul(a, b, p):
    z = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): z[i + j] = (z[i + j] + x*y) % p
    return trim(z)


def legendre(d, p):
    a, b = [1], [0, 1]
    if d == 0: return a
    for k in range(1, d):
        c = add([0] + [(2*k+1)*t for t in b], [-k*t for t in a], p)
        c = [(t * pow(k+1, -1, p)) % p for t in c]
        a, b = b, c
    return b


def ha_polynomials(p):
    assert p >= 11 and p % 8 == 3 and all(p % j for j in range(2, int(p**0.5)+1))
    m = (p-3)//8
    d = 2*m
    lp = legendre(d, p)
    assert all(lp[j] == 0 for j in range(1, d+1, 2))
    E = [lp[2*j] for j in range(m+1)]
    # z^m E(1-1/z) = sum_j E_j z^(m-j) (z-1)^j.
    G = [0]*(m+1)
    for j, ej in enumerate(E):
        for k in range(j+1):
            G[m-j+k] = (G[m-j+k] + ej*comb(j, k)*(-1)**(j-k)) % p
    assert G[-1] == 1
    assert G[0] == comb(3*m+1, m) % p
    Q = [0]*m + G
    Qsq = mul(Q, Q, p)
    # M'(z) = -Q(z)^2.  M(0)=0, deg M=N=(p-1)/2.
    M = [0] + [(-c*pow(i+1, -1, p))%p for i,c in enumerate(Qsq)]
    assert (len(M)-1)==4*m+1
    assert M[-1] == 2
    assert mul(Q, Q, p) == [(-i*M[i])%p for i in range(1, len(M))]
    return m, E, G, Q, M


def evalp(a, x, p):
    v=0
    for c in reversed(a):v=(v*x+c)%p
    return v


def resultant(a, b, p):
    a=trim([t%p for t in a]); b=trim([t%p for t in b]);
    m=len(a)-1;n=len(b)-1
    assert m>=1 and n>=1
    # Sylvester matrix with m? Standard: n rows of a, m rows of b.
    mat=[]
    for i in range(n):
        row=[0]*(m+n)
        row[i:i+m+1]=list(reversed(a))
        mat.append(row)
    for i in range(m):
        row=[0]*(m+n)
        row[i:i+n+1]=list(reversed(b))
        mat.append(row)
    det=1
    for j in range(m+n):
        pivot=next((r for r in range(j,m+n) if mat[r][j]%p),None)
        if pivot is None:return 0
        if pivot!=j:
            mat[j],mat[pivot]=mat[pivot],mat[j];det=-det
        elem=mat[j][j]%p; det=det*elem%p
        inv=pow(elem,-1,p)
        for r in range(j+1,m+n):
            if mat[r][j]%p:
                f=mat[r][j]*inv%p
                for col in range(j,m+n):
                    mat[r][col]=(mat[r][col]-f*mat[j][col])%p
    return det%p


def check_prime(p, t_values):
    m,E,G,Q,M=ha_polynomials(p)
    N=len(M)-1
    for t in t_values:
        F=M[:];F[0]=(F[0]-t)%p
        deriv=[(i*M[i])%p for i in range(1,len(M))]
        res_full=resultant(F,deriv,p)
        res_Q=resultant(F,Q,p)
        disc=(-1 if (N*(N-1)//2)%2 else 1)*res_full*pow(M[-1],-1,p)%p
        pred=(-pow(2,-1,p)*res_Q**2)%p
        assert disc==pred,(p,t,disc,pred)
    return {"p":p,"m":m,"degree":N,"trials":len(t_values),"E":E if p==11 else None,"G":G if p==11 else None,"M":M if p==11 else None}


def main():
    # Every parameter and resultant operation is exact in F_p.
    ps=[11,19,43,59,67,83,107,131,139,163]
    total=0
    for p in ps:
        v=check_prime(p,range(min(p,7)))
        total+=v['trials']
        print('PASS',v)
    assert (M11:=ha_polynomials(11)[-1])==[0,0,0,2,9,2]
    assert evalp(M11,7,11)==7
    assert pow((-2)%11,(11-1)//2,11)==1
    print('ALL PASS; primes:',len(ps),'resultant specializations:',total,
          '; p=11 critical values: M(0)=0, M(7)=7; discriminant=5*t^2*(t-7)^2')


if __name__=='__main__':main()
