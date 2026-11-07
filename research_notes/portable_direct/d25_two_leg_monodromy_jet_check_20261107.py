"""Exact D25 monodromy-order and p-adic first-jet certificates.
No native benchmark or all-prime theorem assertion. Standard library only.
"""
from math import comb
from fractions import Fraction

def independent_binomial_path(p, precision=3):
    mod = p**precision
    ia, ib = pow(216, -1, mod), pow(2304, -1, mod)
    xa = xb = 1
    A = B = DB = W = V = 0
    for k in range(p):
        c = comb(2*k, k)**2
        a = c*comb(3*k, k)*xa % mod
        b = c*comb(4*k, 2*k)*xb % mod
        A, B = (A+a)%mod, (B+b)%mod
        DB = (DB+k*b)%mod
        W, V = (W+(6*k+1)*a)%mod, (V+(8*k+1)*b)%mod
        xa, xb = xa*ia%mod, xb*ib%mod
    return A, B, DB, W, V

def independent_ratio_path(p, precision=3):
    mod = p**precision
    ia, ib = pow(216,-1,mod), pow(2304,-1,mod)
    a = b = 1
    A = B = DB = W = V = 0
    for k in range(p):
        A, B = (A+a)%mod, (B+b)%mod
        DB = (DB+k*b)%mod
        W, V = (W+(6*k+1)*a)%mod, (V+(8*k+1)*b)%mod
        if k+1 < p:
            j = k+1
            a = a*(2*j)*(2*j-1)*(3*j)*(3*j-1)*(3*j-2)*ia*pow(j,-5,mod)%mod
            b = b*(4*j)*(4*j-1)*(4*j-2)*(4*j-3)*ib*pow(j,-4,mod)%mod
    return A, B, DB, W, V

def projective_orders(a,b,c):
    # Exponent differences (0, 1, infinity) of 2F1(a,b;c;z).
    def order(delta):
        return "infinite" if delta == 0 else delta.denominator
    return tuple(map(order, (1-c, c-a-b, b-a)))

def main():
    F=Fraction
    orders_A=projective_orders(F(1,6), F(1,3), F(1))
    orders_B=projective_orders(F(1,8), F(3,8), F(1))
    assert orders_A == ("infinite",2,6)
    assert orders_B == ("infinite",2,4)
    assert 4 % 2 != 0 and 4 % 6 != 0
    assert 6 % 2 != 0 and 6 % 4 != 0
    expect={19:(2888,2527,3116,7,15),373:(9878159,28243187,35390986,195,274)}
    for p,(Ap,Bp,DBp,c0,c1) in expect.items():
        assert pow(2,(p-1)//2,p)==p-1  # s^2=2 is irreducible over F_p
        a,b,db,w,v=independent_ratio_path(p)
        assert (a,b,db,w,v)==independent_binomial_path(p)
        assert (a,b,db)==(Ap,Bp,DBp)
        assert a%p**2==b%p**2==db%p==0
        a2,b2,db1 = (a//p**2)%p, (b//p**2)%p, ((db%p**2)//p)%p
        assert db1!=0
        imul=pow(db1,-1,p)
        assert (a2*imul%p,(-3*pow(4,-1,p)*b2*imul)%p)==(c0,c1)
        assert c1 != 0
        print(f"p={p} A2={a2} B2={b2} DB1={db1}; mu={c0}+{c1}*sqrt(2)")
    for p in (11,19,373):
        a,b,db,w,v=independent_ratio_path(p,4)
        assert (a,b,db,w,v)==independent_binomial_path(p,4)
        eps=1 if p%3==1 else -1
        assert (2*v-w-p*eps)%p**4==0   # finite verification ONLY
    p=11
    *_,w,v=independent_ratio_path(p,5)
    assert (2*v-w+p)%p**5 == 6*p**4
    print("PASS: monodromy orders, dual integer jets, finite p4 checks, p11 exact p5 witness")
if __name__=="__main__":
    main()
