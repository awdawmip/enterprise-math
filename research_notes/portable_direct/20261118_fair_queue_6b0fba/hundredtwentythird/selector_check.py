"""CM selector: class accounting and rigorous finite window, python-flint 0.9.0."""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from math import comb, gcd, isqrt
import json

import flint
from flint import acb, arb, ctx, fmpz_poly


WORDS = ('1', 'T', 'S', 'I', 'IT', 'IS')


def forms(d):
    for a in range(1, isqrt(d // 3) + 1):
        for b in range(-a, a + 1):
            c, r = divmod(b*b + d, 4*a)
            if not r and a <= c and gcd(gcd(a, b), c) == 1:
                if b >= 0 or (abs(b) < a and a < c):
                    yield a, b, c


def bits(form, word):
    a, b, c = (z % 2 for z in form)
    for char in reversed(word):
        if char == 'S':
            a, c = c, a
        elif char == 'T':
            c = (a+b+c) % 2
        elif char == 'I':
            a = (a+b+c) % 2
    return a, c


def even_stride(m):
    if m % 4 in (1, 2):
        return 2
    if m % 4 == 0 or m % 8 == 3:
        return 4
    return 8


def stride(d, a, c):
    if d % 8 == 3:  # D=5 mod 8: just one orbit.
        return 1
    if d % 8 == 7:
        return 1 if (a, c) == (0, 1) else 2
    return even_stride(d//4) if (a, c) == (1, 0) else 1


def values(shape):
    a, b, _ = shape
    d = 4*a*shape[2]-b*b
    tau = acb(-arb(b)/(2*a), arb(d).sqrt()/(2*a))
    q = (arb.pi()*acb(0,1)*tau).exp()
    x = tau.modular_lambda()
    W = acb(0).modular_theta(tau)[2]**4
    u = q*q
    ru = abs(u).upper()
    h = 80
    tail = (24*(h+1)*ru**(h+1)/(1-ru)**3).upper()
    lambert = 1-24*sum(k*u**k/(1-u**k) for k in range(1,h+1))
    error = arb(0,tail)
    v = (lambert+acb(error,error)-3/(arb.pi()*tau.imag))/W
    # Each transformed value is also checked through the original CP19 ratio.
    direct = [(1-3*x-v)/(1-x), 1+2*x-v, 3+(v-2)/x]
    ys = []
    for idx, word in enumerate(WORDS):
        z, e = x, v
        for char in reversed(word):
            if char == 'S':
                z, e = 1-z, -e
            elif char == 'T':
                z, e = z/(z-1), e/(1-z)
            elif char == 'I':
                z, e = 1/z, e/z
        beta = direct[idx%3] if idx < 3 else 4-direct[idx%3]
        assert beta.overlaps((1-3*z-e)/(1-z))
        if d in (3,4) and any(z.overlaps(old) for old in ys):
            continue
        ys.append(z)
        yield word, beta


def ball_key(beta):
    # A ball is placed in the cell of its midpoint; the entire ball lies
    # strictly within one extra cell on either side.
    out = []
    for coord in (beta.real, beta.imag):
        scaled = coord*2**150
        k = int(scaled.mid().floor().unique_fmpz())
        assert scaled > k-1 and scaled < k+2
        out.append(k)
    return tuple(out)


def census():
    grid = {}
    cutoff = arb.pi()*arb(41).sqrt()/2
    large_min = (1+3/cutoff)*cutoff.exp()/16-3
    kept, by_a = Counter(), Counter()
    comparisons = close_cells = 0
    signatures = []
    largest = (0, None)
    for d in range(3, 41*64):
        if d % 4 not in (0,3):
            continue
        possible = 1 if d%8 == 3 else (2 if d%8 == 7 else even_stride(d//4))
        if d >= 41*possible*possible:
            continue
        shapes = list(forms(d))
        hc = len(shapes)
        local = Counter()
        for shape in shapes:
            for word,beta in values(shape):
                a,c = bits(shape, word)
                step = stride(d,a,c)
                if d >= 41*step*step:
                    continue
                assert abs(beta-2) < large_min
                # Ensure the reported integer bound follows from ball bounds.
                m = int(abs(beta-2).upper().ceil().unique_fmpz())
                label = (d,*shape,word)
                if m>largest[0]:
                    largest = m,label
                key = ball_key(beta)
                for i in range(-2,3):
                    for j in range(-2,3):
                        for _, other in grid.get((key[0]+i,key[1]+j),()):
                            assert not beta.overlaps(other)
                            close_cells += 1
                grid.setdefault(key,[]).append((label,beta))
                signatures.append((label,*key))
                kept[d] += 1
                local[a,c] += 1
                by_a[step] += 1
        if d not in (3,4) and hc:
            assert all(v == (6 if d%8 == 3 else 2)*hc for v in local.values())
        if local:
            comparisons += sum(local.values())
    return dict(discriminants=len(kept), by_stride=dict(sorted(by_a.items())),
                distinct_marks=comparisons, distinct_pairs=comparisons*(comparisons-1)//2,
                largest_abs_b_minus_2_ceiling=largest[0], largest_example=largest[1],
                interval_cells_power_of_two=-150, neighboring_ball_tests=close_cells,
                tag_cell_sha256=sha256(json.dumps(signatures,separators=(',',':')).encode()).hexdigest(),
                samples={str(-d):kept[d] for d in (3,4,7,15,28,60,124,188,2012,2620) if d in kept})


def peak_census(limit=12000):
    # Independent enumeration of all reduced forms with leading coefficient
    # <=8. Compute actual S/IS centers by their rays, modulo 2 full turns.
    sites = hits = 0
    for d in range(3,limit+1):
        if d%4 not in (0,3):
            continue
        keys = [(1,1)] if d%8==3 else ([(0,0),(1,0),(0,1)] if d%8==7
                                         else [(0,1),(1,1),(1,0)])
        entries = {k:[] for k in keys}
        for a in range(1,9):
            for b in range(-a,a+1):
                c,rem=divmod(b*b+d,4*a)
                if rem or c<a or gcd(gcd(a,b),c)!=1 or (b<0 and (abs(b)==a or c==a)):
                    continue
                for w in ('S','IS'):
                    k=bits((a,b,c),w)
                    entries[k].append((a,b,w))
        for k,items in entries.items():
            step=stride(d,*k)
            if d < 41*step*step:
                continue
            assert min(v[0] for v in items)==step
            rays=set()
            for a,b,w in items:
                assert a%step==0
                if a==step:
                    ray=(Fraction(b,2*a)+(w=='S'))%2
                    assert ray not in rays
                    rays.add(ray)
                    hits+=1
            sites+=1
    return dict(discriminant_bound=limit, checked_large_orbits=sites, peak_marks=hits)


def classical_phi(p):
    """Coefficients of Phi_p from the distinct leading poles of j(q^p)^i j(q)^j, i>=j."""
    bound = p*(p+1)
    order = bound+1
    sigma = [0]*order
    for k in range(1, order):
        for n in range(k, order, k):
            sigma[n] += k**3
    jshift = fmpz_poly([1]+[240*a for a in sigma[1:]]).pow_trunc(3, order)
    for k in range(1, order):
        factor = [0]*order
        for i in range((order-1)//k+1):
            factor[k*i] = comb(23+i, 23)
        jshift = (jshift*fmpz_poly(factor)).truncate(order)
    low = [jshift.pow_trunc(i, order) for i in range(p+2)]
    high = [s.inflate(p).truncate(order) for s in low]

    def term(i, j):
        weight = p*i+j
        return (high[i]*low[j]).truncate(weight+1).left_shift(bound-weight)

    jet = term(p+1, 0)+term(0, p+1)
    phi = {(p+1, 0):1, (0, p+1):1}
    for i in range(p, -1, -1):
        for j in range(i, -1, -1):
            coefficient = -int(jet[bound-(p*i+j)])
            if coefficient:
                phi[i, j] = coefficient
                jet += term(i, j)*coefficient
                if i != j:
                    phi[j, i] = coefficient
                    jet += term(j, i)*coefficient
    assert jet == 0
    return phi


def minus_seven():
    # Reuse the wave-99 exact triangular q-jet construction, now at 7.
    j = -3375
    phi = classical_phi(7)
    assert list(fmpz_poly.hilbert_class_poly(-7)) == [-j, 1]

    def deriv(a, b):
        return sum(c*comb(i,a)*comb(k,b)*j**(i+k-a-b)
                   for (i,k),c in phi.items() if i >= a and k >= b)

    assert deriv(0,0) == 0 and deriv(0,1)
    R = Fraction(deriv(2,0)-deriv(1,1)+deriv(0,2), deriv(0,1))
    psi = 6*j*R + Fraction(7*j-6912,j-1728)
    assert R == Fraction(181,637875) and psi == Fraction(5,21)
    x = fmpz_poly([0,1])
    A4 = 1-x+x**2
    U = -42*A4*(1+x)-5*(1-2*x)*(2-x)*(x+1)
    V = 42*(1-x)*A4
    cases = [([16,-1,1],[198,-273,112]),([16,-31,16],[324,0,7]),
             ([1,-1,16],[198,273,112])]
    product = fmpz_poly([1])
    for coeffs,(c,b,a) in cases:
        f = fmpz_poly(coeffs)
        product *= f
        assert V.resultant(f) != 0 and (a*U**2 + b*U*V + c*V**2) % f == 0
        assert b*b - 4*a*c < 0
    assert product == 256*A4**3 - j*x**2*(1-x)**2
    return dict(j=j, implicit_second_jet=str(R), E2star_E4_over_E6=str(psi),
                lambda_and_centered_b_polynomials_ascending=cases)


def main():
    ctx.prec=384
    ten=arb(10)
    ratios=arb.pi()**2*ten.exp()/(128*ten)
    assert ratios > 100
    assert arb.pi()*arb(41).sqrt()/2 > 10
    assert ten.exp()/16-3 > 32+arb(4)/9*(ten/2).exp()
    assert 2*(arb.pi()/16).sin()*ten.exp()/16 > 6
    print(json.dumps(dict(python_flint=flint.__version__, arb_bits=ctx.prec,
                          small=census(), large_finite_crosscheck=peak_census(), minus_seven=minus_seven()),
                     indent=2,sort_keys=True))


if __name__=='__main__':
    main()
