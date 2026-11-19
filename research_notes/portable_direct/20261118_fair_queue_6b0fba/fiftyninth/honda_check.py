"""Exact reduction and local certificates for the Frobenius–Rosati obstruction."""
import itertools
import json
import sympy as sp
from sympy.polys.agca.extensions import MonogenicFiniteExtension

t = sp.symbols("t")
f = sp.Poly(t**8 + 5*t**6 + 245*t**2 + 2401, t, domain=sp.QQ)
assert f.is_irreducible
L = MonogenicFiniteExtension(f)
pi = L.generator
zero, one = L.zero, L.one
M0, M1 = (zero, zero), (one, zero)
sigma = zero, one
pif = pi, zero


def value(coefficients, x):
    out = zero
    for c in coefficients:
        out = out*x + L.convert(c)
    return out


def substitute(x, root):
    return value(sp.Poly(x.as_expr(),t).all_coeffs(),root)


def tau(x):
    return substitute(x,-pi)


def rho(x):
    return substitute(x,7*pi.inverse())


def add(x,y):
    return tuple(a+b for a,b in zip(x,y))


def scale(c,x):
    return tuple(c*a for a in x)


def mul(x,y):
    a,b=x
    c,d=y
    return a*c-b*tau(d), a*d+b*tau(c)


def dagger(x):
    a,b=x
    return rho(a), -tau(rho(b))


def reduced_trace(x):
    return x[0]+tau(x[0])


def central_real(x,d):
    p,q = [sp.Poly(z.as_expr(),t) for z in (x,d)]
    j = next(i for i in range(1,8) if q.nth(i))
    b = p.nth(j)/q.nth(j)
    a = p.nth(0)-b*q.nth(0)
    assert x == L.convert(a) + L.convert(b)*d
    return a,b


def orthogonal_projector(x):
    numerator=mul(x,dagger(x))
    k=reduced_trace(numerator)
    result=scale(k.inverse(),numerator)
    assert mul(result,result)==result and dagger(result)==result
    assert mul(result,x)==x and mul(x,result)==result
    return result,k


def local_roots(modulus):
    return [d for d in range(modulus) if (d*d-23*d+28) % modulus == 0]


def primitive_conic_count(d,m,modulus):
    return sum((x*x-m*y*y-d*z*z) % modulus == 0 and (x|y|z)%2
               for x,y,z in itertools.product(range(modulus),repeat=3))


def odd_unit_residue(a,p):
    return 1 if pow(a%p,(p-1)//2,p)==1 else -1


def main():
    y = pi**2 + 49*pi.inverse()**2
    d = y+14
    delta,eta = pi+7*pi.inverse(), pi-7*pi.inverse()
    assert y**2+5*y-98==zero and d**2-23*d+28==zero
    assert delta**2==d and eta**2==d-28 and (delta+eta)==2*pi
    assert rho(delta)==delta and rho(eta)==-eta and tau(delta)==-delta and tau(eta)==-eta
    assert rho(tau(pi))==tau(rho(pi)) and tau(tau(pi))==rho(rho(pi))==pi
    assert mul(sigma,sigma)==scale(-1,M1) and dagger(sigma)==scale(-1,sigma)
    # Check the anti-automorphism on all pairs of the rational algebra basis.
    basis=[(pi**i,zero) for i in range(8)]+[(zero,pi**i) for i in range(8)]
    anti_pairs=0
    for x in basis:
        assert dagger(dagger(x))==x
        for z in basis:
            assert dagger(mul(x,z))==mul(dagger(z),dagger(x))
            anti_pairs+=1
    T=zero,delta
    assert dagger(T)==T and mul(T,T)==(d,zero) and mul(T,pif)==scale(-1,mul(pif,T))
    # Independently form both orthogonal projections from fifth-round line carriers.
    a=value([4,-12,35,-70,-49],pi)
    b=value([1,-11,35,-35,196],pi)
    q=b*tau(a).inverse()
    assert q*tau(q)==-one
    plus=scale(L.convert(sp.Rational(1,2)),(one,q))
    minus=add(M1,scale(-1,plus))
    assert mul(plus,minus)==mul(minus,plus)==M0
    assert mul(pif,plus)==mul(minus,pif) and dagger(plus)!=plus
    left,k=orthogonal_projector(plus)
    right,k2=orthogonal_projector(minus)
    assert k2==k and right!=add(M1,scale(-1,left)) and mul(pif,left)==mul(right,pif)
    overlap=reduced_trace(mul(left,right))
    w=q*rho(q)
    assert 4*k==2+w+w.inverse() and overlap==one-k.inverse()
    assert overlap==(w-one)**2*((w+one)**2).inverse()
    a0,a1=central_real(overlap,d)
    z=sp.symbols('z')
    real_values=[a0+a1*(23+s*sp.sqrt(417))/2 for s in (-1,1)]
    intervals=[(int(sp.floor(z0*10**6)),int(sp.ceiling(z0*10**6))) for z0 in real_values]
    assert all(0<lo<hi<10**6 for lo,hi in intervals)
    cubic_steps=[]
    for i in range(3):
        old_overlap=overlap
        q=q*(w+3)*(3*w+1).inverse()
        assert q*tau(q)==-one
        ep=scale(L.convert(sp.Rational(1,2)),(one,q))
        em=add(M1,scale(-1,ep))
        p1,_=orthogonal_projector(ep)
        p2,_=orthogonal_projector(em)
        overlap=reduced_trace(mul(p1,p2))
        assert overlap==old_overlap**3*((4-3*old_overlap)**2).inverse() and overlap!=zero
        w=q*rho(q)
        r,s=central_real(overlap,d)
        coeff_height=max(max(abs(int(x.p)).bit_length(),int(x.q).bit_length()) for x in (r,s))
        cubic_steps.append(dict(step=i+1,coordinate_bits=coeff_height,
                                arch_decimal=[str(sp.N(r+s*(23+sign*sp.sqrt(417))/2,8)) for sign in (-1,1)]))
    polynomial=sp.Poly(sp.resultant(t*t-23*t+28, z-a0-a1*t,t),z).clear_denoms()[1].primitive()[1]
    if polynomial.LC()<0: polynomial=-polynomial
    roots=local_roots(256)
    assert roots==[52,227]
    even,odd=roots
    assert (odd%8,(odd-28)%8)==(3,7)
    n_odd=primitive_conic_count(odd,odd-28,4)
    n_even=primitive_conic_count(even//4,(even-28)//4,8)
    assert n_odd==n_even==0
    assert local_roots(49)==[9,14] and local_roots(3)==[1]
    seven=14
    symbol7=odd_unit_residue(-(seven//7)*((seven-28)//7),7)
    assert symbol7==1 and local_roots(7)==[0,2]
    print(json.dumps(dict(
        irreducible_degree=f.degree(),rosati_order_reversal_basis_pairs=anti_pairs,
        odd_dyadic=dict(d_mod_256=odd,primitive_zeros_mod_4=n_odd),
        even_dyadic=dict(d_mod_256=even,normalized_d_mod_8=(even//4)%8,
                         normalized_m_mod_8=((even-28)//4)%8,primitive_zeros_mod_8=n_even),
        root_mod_3=local_roots(3),roots_mod_49=local_roots(49),
        seven_hilbert_symbol_at_d_nonunit=symbol7,negative_places=["2 (d odd)","2 (d even)"],
        projected_line_overlap=dict(form="a+b*d",a=str(a0),b=str(a1),
            primitive_polynomial=[int(c) for c in polynomial.all_coeffs()],
            embedding_order="archimedean boxes listed in ascending d",
            interval_endpoints_in_millionths=intervals),
        cubic_steps=cubic_steps,real_quadratic_coefficient_certificate="(delta*sigma)^dagger=delta*sigma, (delta*sigma)^2=d",
    ),indent=2,ensure_ascii=False))


if __name__=="__main__":
    main()
