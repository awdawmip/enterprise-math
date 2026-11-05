#!/usr/bin/env python3
"""Exact finite CM-cusp triangular transport for D25, author-side diagnostic.
No floating point or native H0/B0 crystalline calculation.
Targeted science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
"""
from math import comb
import json

def poly_multiply(a,b,N,m):
    c=[0]*(N+1)
    for i,x in enumerate(a[:N+1]):
        if x:
            for j,y in enumerate(b[:N+1-i]):
                c[i+j]=(c[i+j]+x*y)%m
    return c

def poly_plus(a,b,N,m):
    return [((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%m
            for i in range(N+1)]

def poly_scale(a,x,N,m):
    return [v*x %m for v in a[:N+1]]+[0]*max(0,N+1-len(a))

def poly_power(a,k,N,m):
    c=constant(1,N)
    for _ in range(k):
        c=poly_multiply(c,a,N,m)
    return c

def poly_inverse(a,N,m):
    c=[0]*(N+1)
    c[0]=pow(a[0],-1,m)
    for n in range(1,N+1):
        c[n]=-c[0]*sum(a[i]*c[n-i] for i in range(1,n+1)) % m
    return c

def square_root_unit(a,N,m):
    assert a[0]%m==1
    c=constant(1,N)
    inv2=pow(2,-1,m)
    for n in range(1,N+1):
        c[n]=(a[n]-sum(c[i]*c[n-i] for i in range(1,n)))*inv2 % m
    return c

def constant(x,N):
    return [x]+[0]*N

def sqrt_one_minus(poly,N,m):
    return square_root_unit(poly_plus(constant(1,N),
                                       poly_scale(poly,-1,N,m),N,m),N,m)

def calculate(p):
    m=p**3
    N=2*(p-1)
    qz_arg=constant(1,N)
    qz_arg[2]=-pow(3,-1,m)%m
    qz=square_root_unit(qz_arg,N,m)
    G=poly_scale(poly_multiply(
        poly_power(poly_plus(constant(5,N),poly_scale(qz,4,N,m),N,m),3,N,m),
        poly_power(poly_plus(constant(1,N),qz,N,m),2,N,m),N,m),432,N,m)
    normalized_Ginv=poly_scale(poly_inverse(G,N,m),G[0],N,m)
    U0=32*pow(729,-1,m)%m
    U=constant(U0,N)
    for it in range(N+6):
        t=[0,0,0]+U[:N-2]
        qt=sqrt_one_minus(t,N,m)
        H=poly_scale(poly_multiply(
            poly_power(poly_plus(constant(5,N),poly_scale(qt,3,N,m),N,m),3,N,m),
            poly_plus(constant(1,N),qt,N,m),N,m),64,N,m)
        ratio=poly_multiply(poly_scale(H,pow(65536,-1,m),N,m),
                            normalized_Ginv,N,m)
        nxt=poly_scale(square_root_unit(ratio,N,m),U0,N,m)
        if nxt==U:
            break
        U=nxt
    else:
        raise RuntimeError("series coefficient solution did not stabilize")
    t=[0,0,0]+U[:N-2]
    qt=sqrt_one_minus(t,N,m)
    # N(s) = 3 U(s) sqrt(1-t(s)) /
    #        (sqrt(1-s^2/3) (3U(s)+s U'(s))).
    derivative_factor=[(i+3)*U[i]%m for i in range(N+1)]
    gauge=poly_multiply(
        poly_scale(poly_multiply(U,qt,N,m),3,N,m),
        poly_inverse(poly_multiply(qz,derivative_factor,N,m),N,m),
        N,m)
    K=2*(p-1)//3
    T=[[0]*(K+1) for _ in range(p)]
    source=gauge[:]
    for k in range(K+1):
        for n in range(p):
            T[n][k]=pow(9,k,m)*pow(3*pow(2,-1,m),n,m)*source[2*n]%m
        source=poly_multiply(source,t,N,m)
    original_216=[
        comb(2*n,n)**2*comb(3*n,n)*pow(216,-n,m)%m
        for n in range(p)]
    original_2304=[
        comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,m)%m
        for k in range(p)]
    for n in range(p):
        reconstructed=sum(T[n][k]*original_2304[k]
                          for k in range(K+1))%m
        assert reconstructed==original_216[n],(p,n,reconstructed,original_216[n])
    W=sum((6*n+1)*v for n,v in enumerate(original_216))%m
    V=sum((8*k+1)*v for k,v in enumerate(original_2304))%m
    h=(p-1)//2
    Vh=sum((8*k+1)*original_2304[k] for k in range(h+1))%m
    J=(3*p-1)//4
    # A p-integral certificate with matched half endpoint:
    short=sum(original_2304[k] *
              (sum((6*n+1)*T[n][k] for n in range(p))-
               ((8*k+1) if k<=h else 0))
              for k in range(K+1))%m
    assert short==(W-Vh)%m
    overhang=sum((8*k+1)*original_2304[k] for k in range(K+1,J+1))%m
    before_overhang=sum((8*k+1)*original_2304[k]
                        for k in range(h+1,K+1))%m
    return dict(p=p, modulus=m, half=h, target_K=K, v_shell_max=J,
                triangular_identity="PASS", W=W,V=V,Vh=Vh,
                W_minus_V=(W-V)%m, short_certificate=short,
                before_overhang=before_overhang, overhang=overhang,
                upper_shell_sum=(before_overhang+overhang)%m,
                origin_U0=U0, origin_gauge0=gauge[0],
                pure_series_iterations=it)

def main():
    primes=[5,7,11,13,17,19,23,31,37]
    rows=[calculate(p) for p in primes]
    assert all(row["upper_shell_sum"]==0 and row["V"]==row["Vh"] for row in rows)
    assert all(row["short_certificate"]==row["W_minus_V"] for row in rows)
    print(json.dumps({"schema":"D25_CUSP_INTEGRAL_FINITE_TRANSPORT_CHECK_V1",
                      "checks":rows, "formal_proof_scope":
                      "Depends on earlier high-branch analytic transformation; exact "
                      "integer formal-series algebra for the finite triangular map; "
                      "numeric verification for listed primes only; native H0/B0 not run"},
                     indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
