"""D25 universal endpoint sequences; exact rational and modular certificates.

Standalone Python 3 stdlib only. Author-side finite-field check, no native claim.
"""
from fractions import Fraction
from math import comb, factorial


def gbinom(x, n):
    out = Fraction(1)
    for j in range(n):
        out *= (x - j) / (j + 1)
    return out


def E(t, side):
    assert t >= 0 and side in (-1, 1)
    return sum(
        (6*j+1) * Fraction(comb(2*j, j), 8**j) * comb(t, j)
        * gbinom(Fraction(t, 1) + Fraction(side, 3), j)
        for j in range(t+1)
    )


def rmod(x, p):
    assert x.denominator % p
    return (x.numerator % p) * pow(x.denominator, -1, p) % p


def P_at(p, z):
    m = (p-1)//6
    a,b,c = 2*m,3*m,4*m
    acc=0
    for j in range(b+1):
        term=(6*j+1)*pow(-2,-j,p)*comb(b,j)
        # all j < p: generalized binoms via p-unit denominators
        acc=(acc+term*rmod(gbinom(Fraction(a+z),j),p)*rmod(gbinom(Fraction(c+z),j),p))%p
    return acc


def mr_prime(n):
    """Deterministic Miller-Rabin for 0 <= n < 2**64."""
    if n < 2:
        return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%q==0:
            return n==q
    d=n-1;s=0
    while not d%2:
        s+=1;d//=2
    for base in (2,325,9375,28178,450775,9780504,1795265022):
        a=base%n
        if a==0: continue
        x=pow(a,d,n)
        if x in (1,n-1): continue
        for _ in range(s-1):
            x=pow(x,2,n)
            if x==n-1: break
        else: return False
    return True


def verify_field(p):
    assert mr_prime(p) and p%6==1
    m=(p-1)//6;a,c=2*m,4*m
    values=[P_at(p,z) for z in range(p)]
    for t in range(p):
        assert values[(t-a)%p]==rmod(E(t,-1),p),(p,t,-1)
        assert values[(t-c)%p]==rmod(E(t,+1),p),(p,t,+1)
    chi=pow(2,(p-1)//2,p)
    assert chi in (1,p-1)
    sum0=sum(values)%p
    sum1=sum(z*values[z] for z in range(p))%p
    assert sum0==(-2*chi)%p
    assert sum1==(chi*pow(2,-1,p))%p
    assert sum(t*rmod(E(t,+1),p) for t in range(p))%p==rmod(Fraction(11,6),p)*chi%p
    assert sum(t*rmod(E(t,-1),p) for t in range(p))%p==rmod(Fraction(7,6),p)*chi%p
    tangent=-sum(rmod(E(t,+1),p)*pow((t-c)%p,-1,p)
                 for t in range(p) if t!=c)%p
    derivative=0
    b=3*m
    for j in range(b+1):
        c0,c1=1,0
        for h in range(j):
            for d in (a-h,c-h):
                c0,c1=(c0*d)%p,(c1*d+c0)%p
        weight=(6*j+1)*pow(-2,-j,p)*comb(b,j)
        weight=weight*pow(factorial(j),-2,p)
        derivative=(derivative+weight*c1)%p
    assert tangent == derivative%p
    return (p,chi,sum0,sum1,tangent)


def verify_sparse(t, side, p):
    assert p<2**64 and mr_prime(p) and p%6==1 and 0<=t<p
    m=(p-1)//6;a,b,c=2*m,3*m,4*m
    z=t-(a if side==-1 else c)
    U=E(t,side)
    assert U.denominator%p!=0
    assert rmod(U,p)==0
    s=0
    for j in range(min(t,b)+1):
        s+=(6*j+1)*pow(-2,-j,p)*comb(b,j)*rmod(gbinom(Fraction(a+z),j),p)*rmod(gbinom(Fraction(c+z),j),p)
    assert s%p==0
    return {'p':p,'t':t,'side':side,'z_mod_p':z%p,'numerator':str(U.numerator),'denominator':str(U.denominator),'summands_required':min(t,b)+1}


def main():
    for p in [7,13,19,31,37,43,61]:
        row=verify_field(p)
        print('FULL_FIELD_TABLE_AND_MOMENTS_PASS',row)
    cases=[(7,+1,31),(8,+1,31),(8,-1,357681673),(8,+1,516774751693)]
    for case in cases:
        print('SPARSE_PRIME_ROOT_PASS',verify_sparse(*case))
    p=31;m=5;a,b,c=10,15,20
    assert P_at(31,18)==P_at(31,19)==0
    u1=lambda z:(-7*pow(2,-1,p)*b*(a+z)*(c+z))%p
    assert (u1(18),u1(19))==(2,3)
    print('BRC_J1_PORT_COLLISION_PASS', {'p':31,'z1':18,'z2':19,'scalar':0,'labelled_weighted_j1':[2,3]})
    print('ALL_CHECKS_PASS')

if __name__=='__main__':
    main()
