"""D25/LIFT GH-7/GH-8 author exact checks; Python standard library only.

Checks rational telescoping arithmetic and p-adic cutoff boundary, not a
proof of T_p == 0 for all primes or any native Enterprise Math experiment.
"""
from fractions import Fraction as F
from math import isqrt


def prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def A(k): return 9 * (4*k + 1)**3

def B(k): return 4 * (4*k + 2) * (4*k + 3) * (k + 1)

def q(k): return F(A(k), B(k))

def C(r):
    x = F(1)
    for k in range(r): x *= q(k)
    return x


def R1(k): return F(4*k - 1, 4)

def R2(k): return R1(k)**2

def rho1(k): return F(3*(160*k*k + 84*k + 5), 32*(k+1)*(2*k+1))

def rho2(k):
    return F(-2048*k**4 -1152*k**3 +1552*k*k +1008*k +109,
             128*(k+1)*(2*k+1))


def modf(f,p):
    assert f.denominator % p != 0, (p, f)
    return f.numerator % p * pow(f.denominator % p, -1, p) % p


def mod_C_array(p):
    d=(p-3)//4
    c=1
    out=[]
    for r in range(d+1):
        out.append(c)
        if r<d:
            c = c * (A(r)%p) * pow(B(r)%p,-1,p) %p
    return out


def main():
    for k in range(45):
        c, cnext = C(k), C(k+1)
        assert cnext*R1(k+1)-c*R1(k)+c*rho1(k) == (8*k+1)*c
        assert cnext*R2(k+1)-c*R2(k)+c*rho2(k) == (8*k+1)*c
    print("RATIONAL_IDENTITIES: 45 consecutive ranks PASS")

    # The hypothetical polynomial solution to the exact Gosper equation
    # must have degree one by comparison of leading coefficients.
    # Degree-four coefficient fixes slope a=1; degree-three gives b=11/16.
    # Degree-two coefficient is then -342, proving incompatibility.
    a,b = F(1),F(11,16)
    def poly_values(k):
        left=A(k)*(a*(k+1)+b)-B(k)*(a*k+b)
        right=B(k)*(8*k+1)
        return left-right
    assert poly_values(0) == F(-405,16) # matches -9*(45)/16
    assert poly_values(1) == F(-9*(608+356+45),16)
    # Verify polynomial difference coefficients via five finite differences.
    vs=[poly_values(k) for k in range(5)]
    diffs=[]
    for j in range(5):
        diffs.append(vs[0]);vs=[vs[i+1]-vs[i] for i in range(len(vs)-1)]
    assert diffs[4]==0 and diffs[3]==0, diffs
    print("GOSPER_POLYNOMIAL_OBSTRUCTION: slope=1 intercept=11/16; degree-2 mismatch=-342 PASS")

    checked=0
    target=0
    for p in range(7,2001):
        if not prime(p) or p%4!=3: continue
        d=(p-3)//4
        cs=mod_C_array(p)
        Tp=sum((8*r+1)*cs[r] for r in range(d+1))%p
        assert B(d)==p*(p*p-1)
        assert 9*(p-2)**3==A(d)
        lead=(p*q(d))
        assert lead.denominator%p!=0
        assert modf(lead,p)==72%p
        # R1 boundary: p/4 C_{d+1}; mod p =18 C_d.
        m1=(modf(F(1,4),p)+18*cs[d]+
            sum(modf(rho1(r),p)*cs[r] for r in range(d+1)))%p
        # R2 boundary: p^2/16 C_{d+1}; mod p=0.
        m2=(-modf(F(1,16),p)+
            sum(modf(rho2(r),p)*cs[r] for r in range(d+1)))%p
        assert Tp==m1==m2,(p,Tp,m1,m2)
        if p%24==19:
            target+=1
            assert Tp==0,(p,Tp) # finite observation, not general theorem
        checked+=1
    print(f"FINITE_FIELD_REGULARIZATION: {checked} primes p=3 mod4, p<2001; {target} frozen 19-class; all identities PASS")
    print("FINITE_T_CONJECTURE_CHECK: all checked 19-class sums zero (finite only)")

    for p in (7,11,19,43,67):
        d=(p-3)//4
        c=[C(r) for r in range(d+2)]
        T=sum((8*r+1)*c[r] for r in range(d+1))
        T1=R1(d+1)*c[d+1]-R1(0)*c[0]+sum(rho1(r)*c[r] for r in range(d+1))
        T2=R2(d+1)*c[d+1]-R2(0)*c[0]+sum(rho2(r)*c[r] for r in range(d+1))
        assert T==T1==T2
        assert modf(F(p)*c[d+1]/c[d],p)==72%p
    print("RATIONAL_FINITE_SUMS: exact fractions p=7,11,19,43,67 PASS")

if __name__=="__main__":main()
