"""Exact Eisenstein good-prime tests in characteristic zero. No packages required."""
from fractions import Fraction
from functools import lru_cache
from itertools import product

Q=7
# z6 = 1+omega maps to 3 modulo pi=1+3*omega.
z6=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
log3={pow(3,j,7):j for j in range(6)}
zero=((0,0),)*6


def scalar(n):
    return ((n,0),)+zero[1:]


def plus(x,y):
    return tuple((a+c,b+d) for (a,b),(c,d) in zip(x,y))


def times(n,x):
    return tuple((n*a,n*b) for a,b in x)


def product_ring(x,y):
    # Coefficients in Z[z6], z6^2=z6-1; then reduce modulo Phi_7(z).
    c=[[0,0] for _ in range(7)]
    for j,(a,b) in enumerate(x):
        for k,(u,v) in enumerate(y):
            pos=(j+k)%7
            c[pos][0]+=a*u-b*v
            c[pos][1]+=a*v+b*u+b*v
    return tuple((a-c[6][0],b-c[6][1]) for a,b in c[:6])


def unit_power(e):
    return (z6[e%6],)+zero[1:]


def eisen_mult(x,y):
    a,b=x; c,d=y
    return a*c-b*d,a*d+b*c-b*d


@lru_cache(None)
def bar_pi_power(t):
    if t==0:
        return (1,0)
    return eisen_mult(bar_pi_power(t-1),(-2,-3))


def additive_numerator(t,r,v):
    # e(v*pi^r / pi^t) has exponent v*7^r*[omega](bar(pi)^(t-r))/7^t.
    return v*7**r*bar_pi_power(t-r)[1] if r<t else 0


def reduce_cyclotomic(coeff0,coeff1):
    order=len(coeff0)
    step=order//7
    result=[]
    for r in range(6*step):
        a=coeff0[r]-coeff0[6*step+r%step]
        b=coeff1[r]-coeff1[6*step+r%step]
        if r%step:
            assert (a,b)==(0,0), "sum has a component outside Q(zeta_6,zeta_7)"
        else:
            result.append((a,b))
    return tuple(result)


@lru_cache(None)
def direct(t,r,v,k=0):
    """Sum original residues, not the prime-power formula. k=0 or 1."""
    if t==0:
        return scalar(1) if k==0 else unit_power(log3[v%7]) if r==0 else zero
    if k==1 and r==0:
        return zero
    mod=7**t
    aa=[0]*mod
    bb=[0]*mod
    for d in (range(1,7) if k else (0,)):
        slope=(additive_numerator(t,r-1,v)-d*7**(t-1)*bar_pi_power(1)[1]
               if k else additive_numerator(t,r,v))
        shift=log3[d] if k else 0
        for h in range(1,7):
            c,e=z6[(t*log3[h]+shift)%6]
            for x in range(h,mod,7):
                a=x*slope%mod
                aa[a]+=c
                bb[a]+=e
    return reduce_cyclotomic(aa,bb)


def gauss(r):
    # G_r with primitive additive character e(x/pi), not an arbitrary sign.
    a=[0]*7;b=[0]*7
    for x in range(1,7):
        c,d=z6[(r*log3[x])%6]
        j=(-3*x)%7
        a[j]+=c;b[j]+=d
    return reduce_cyclotomic(a,b)


def lift(t,r,v,character):
    if character%6:
        if r!=t-1:
            return zero
        return times(7**(t-1),product_ring(unit_power(-character*log3[v%7]),gauss(character)))
    return scalar(7**t*(r>=t)-7**(t-1)*(r>=t-1))


def main():
    counts=[0,0]
    for t,r,v in product((1,3,4,6),range(9),(1,3)):
        assert direct(t,r,v)==lift(t,r,v,t)
        counts[0]+=1
    for t,r,v in product((1,3,4),range(7),(1,3)):
        expected=(times(-1,product_ring(gauss(1),lift(t,r-1,v,t-1))) if r else zero)
        assert direct(t,r,v,1)==expected
        counts[1]+=1
    assert direct(4,3,1)!=zero and direct(4,9,1)==zero
    assert direct(1,0,6)==times(-1,direct(1,0,1))
    assert direct(6,5,1)==scalar(-7**5)
    for r in (1,3,4):
        assert product_ring(gauss(r),gauss(-r))==scalar((-1)**r*7)

    # Arbitrary finite vectors. Delta-base testing certifies rank and inversion.
    M=3
    exponents=[6*m+j for m in range(M+1) for j in (0,1,3,4)]
    for v in (1,3,6):
        for index in exponents:
            def F(r):
                return scalar(1) if index==0 else lift(index,r,v,index)
            rec={}
            for m in range(M+1):
                D=F(6*m+4)
                rec[6*m]=(D if m==0 else times(Fraction(1,6*7**(6*m-1)),
                                               plus(D,times(-1,F(6*(m-1)+1)))))
                for j in (1,3,4):
                    inverse_G=times(Fraction((-1)**j,7),gauss(-j))
                    rec[6*m+j]=times(Fraction(1,7**(6*m+j-1)),
                                     product_ring(product_ring(plus(F(6*m+j-1),times(-1,D)),
                                                               inverse_G),unit_power(j*log3[v])))
                assert F(6*m+1)==D
                assert plus(times(6,F(6*m+5)),F(6*m+7))==times(7,D)
            assert all(rec[t]==scalar(int(t==index)) for t in exponents)

            # Normalized positive-slice transform for k=1 (divide out omega^-1 G1).
            def B(r):
                return zero if index==0 else lift(index,r-1,v,index-1)
            def D1(m):
                return zero if m<0 else B(6*m+2)
            first = unit_power(log3[v]) if index==0 else zero
            rec1={0:product_ring(first,unit_power(-log3[v]))}
            for t in exponents[1:]:
                m,j=divmod(t,6)
                if j==1:
                    rec1[t]=times(Fraction(1,6*7**(t-1)),plus(D1(m),times(-1,D1(m-1))))
                else:
                    inv_gauss=times(Fraction((-1)**((t-1)%6),7),gauss(1-t))
                    rec1[t]=times(Fraction(1,7**(t-1)),
                                  product_ring(product_ring(plus(B(t),times(-1,D1((t-2)//6))),
                                                            inv_gauss),unit_power((t-1)*log3[v])))
            assert all(rec1[t]==scalar(int(t==index)) for t in exponents)
            for m in range(M+1):
                assert B(6*m+5)==D1(m)
                assert plus(times(6,B(6*m+1)),D1(m))==times(7,D1(m-1))

    # Finite-ray table: Gamma(a+b*omega)=(1+i^(-b)+i^a+i^(b-a))/2.
    def gamma(x):
        a,b=x
        powers=((1,0),(0,1),(-1,0),(0,-1))
        terms=[powers[k%4] for k in (0,-b,a,b-a)]
        value=tuple(Fraction(sum(term[j] for term in terms),2) for j in range(2))
        return powers.index(value) # exponent relative to i
    pi=(1,3)
    p3=eisen_mult(pi,eisen_mult(pi,pi))
    p4=eisen_mult(p3,pi)
    assert (gamma(pi),gamma(p3),gamma(p4))==(1,1,0)
    # G(pi^j)=conj(chi_pi(4)^j)*Gamma(pi^j); give phases as zeta_12 exponents.
    assert tuple((3*gamma(x)-2*j*log3[4])%12 for j,x in [(1,pi),(3,p3),(4,p4)])==(7,3,4)
    print(f"Q=7: {counts[0]} k=0 and {counts[1]} k=1 exact character-zero residue sums passed.")
    print(f"{len(exponents)} coordinate vectors recovered at each of 3 fixed unit values for both k=0,1; their redundant row identities checked.")
    print("p^4 shared-prime, p^6 nonunit, sign of the element unit and ray sign witnesses passed.")


if __name__=="__main__":
    main()
