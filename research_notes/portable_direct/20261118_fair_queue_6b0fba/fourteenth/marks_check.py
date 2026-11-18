"""Exact integer/rational check of the robust-mark counting bounds. Python standard library."""
import json
from fractions import Fraction as Q
from functools import cache
from itertools import combinations
from math import comb, factorial, isqrt


def trig_minorant(t):
    """Coefficients of P(x) <= 1-cos(tx) on 0 <= t*x <= 6."""
    return {2*j: (-1)**(j+1)*t**(2*j)/factorial(2*j) for j in range(1,9)}


def integral_coefficients(t):
    """Power coefficients in z=3e/H of the limiting expression with P replacing w."""
    terms = [Q(0)]*18
    for n, a in trig_minorant(t).items():
        terms[0] += 2*a/(n+1)
        for k in range(n+2):  # lower endpoint ((1+z/3)/3)^(n+1)
            terms[k] -= 2*a*comb(n+1,k)/((n+1)*3**(n+1+k))
        for k in range(n+1):  # 2*P(c*y)+P(1+c*y), integrated against (1-y)
            terms[k+1] += 2*a*(comb(n,k)+2*(k==n))/((k+1)*(k+2)*3**(k+1))
    return terms


def ceil_sqrt(x):
    n = isqrt(x.numerator//x.denominator)
    return n + (n*n < x)


def polynomial_certificate():
    t = Q(43,10)
    terms = integral_coefficients(t)
    fixed = terms[0]
    terms[0] -= Q(111,50)
    terms[1] -= Q(1,6)
    bernstein = [sum(terms[j]*comb(i,j)/comb(17,j) for j in range(i+1))
                 for i in range(18)]
    assert min(bernstein) > Q(1,6000)
    dense = sum(integral_coefficients(Q(18,5)))
    assert dense/3 > Q(9186,10000)**2
    return {"t_fixed":str(t), "fixed_e_squared_coefficient_lower":str(fixed),
            "uniform_bound_bernstein_times_million_floors":[int(x*10**6) for x in bernstein],
            "min_bernstein":str(min(bernstein)), "t_dense":"18/5",
            "dense_squared_coefficient_m2_over_H2_lower":str(dense/3)}


def finite_lower(H,e):
    A, E = H+e, e+1
    L = A//3
    def fourier(t):
        terms = trig_minorant(t)
        # One integer scale for all powers, avoiding rounding and repeated Fraction reductions.
        num, den = t.numerator, t.denominator*H
        common = factorial(16)*den**16
        weights = {n: (-1)**(n//2+1)*num**n*den**(16-n)*(factorial(16)//factorial(n))
                   for n in terms}
        def integer_weight(r):
            return sum(coeff*r**n for n,coeff in weights.items())
        value = E*sum(integer_weight(r) for r in range(L+1,H+1))
        value += sum((E-r)*(2*integer_weight(r)+integer_weight(H+r)) for r in range(1,E))
        return ceil_sqrt(Q(2*value,common))
    old = max(2*E, ceil_sqrt(4*E*(H-A//2)))
    crossed = max(old,ceil_sqrt(4*(E*(H-A//2)+e*E//2)))
    ft = [fourier(t) for t in [Q(43,10),Q(18,5)]]
    return {"frozen":old, "strip_cross":crossed, "fourier_43_10":ft[0],
            "fourier_18_5":ft[1], "combined":max(crossed,*ft)}


def primes(A):
    return [p for p in range(2,A+1) if all(p%q for q in range(2,isqrt(p)+1))]


def prepare_cuts(H,A):
    masks = []
    for r in range(H,0,-1):
        for p in (p for p in primes(A+1) if p==2 or p*r<=A):
            rows = []
            for i in range(min(r,A+1)):
                fine = tuple(sum(1<<x for x in range(j,A+1,r*p))
                             for j in range(i,min(i+r*p,A+1),r))
                if len(fine)>1:
                    rows.append((sum(fine),fine))
            masks.append(rows)
    return masks


def cut_test(bits,e,cuts):
    for rows in cuts:
        lost = 0
        for coarse,fine in rows:
            lost += (bits&coarse).bit_count()-max((bits&f).bit_count() for f in fine)
            if lost>e:
                break
        if lost<=e:
            return False
    return True


def supports(H,e):
    A = H+e
    return set(range(e+1))|set(range(H,A+1)), list(range(e+1,H))


def positions(bits,A):
    return [i for i in range(A+1) if bits>>i&1]


def exact_optimum(H,e):
    A = H+e
    fixed, interior = supports(H,e)
    fixed_bits = sum(1<<x for x in fixed)
    cuts = prepare_cuts(H,A)
    trace = []
    for k in range(len(interior)+1):
        feasible = 0
        witness = None
        for extra in combinations(interior,k):
            bits = fixed_bits|sum(1<<x for x in extra)
            if cut_test(bits,e,cuts):
                feasible += 1
                if witness is None:
                    witness = positions(bits,A)
        trace.append([len(fixed)+k,comb(len(interior),k),feasible])
        if feasible:
            lower = finite_lower(H,e)
            assert lower["combined"]<=len(witness)
            assert literal_robust(witness,H,A,e)
            return {"H":H,"e":e,"optimum":len(witness),"witness":witness,
                    "rows_k_examined_feasible":trace,"bounds":lower}
    raise AssertionError("the full interval is feasible")


def pattern(s,r):
    # Same coordinate order, hence same bit positions for every candidate period.
    return tuple((b-a)%r==0 for a,b in combinations(s,2))


def literal_robust(s,H,A,e):
    for count in range(min(e,len(s))+1):
        for lost in combinations(s,count):
            live = [x for x in s if x not in lost]
            seen = set()
            for r in range(1,A+2):
                sig = pattern(live,r)
                if sig in seen:
                    return False
                if r<=H:  # above-H hypotheses need only differ from targets
                    seen.add(sig)
    return True


def exhaustive_crosscheck(H,e):
    A = H+e
    cuts = prepare_cuts(H,A)
    @cache
    def safe(bits,left):
        if left and bits:
            return all(safe(bits^(1<<x),left-1) for x in positions(bits,A))
        s = positions(bits,A)
        targets = set()
        for r in range(1,A+2):
            sig = pattern(s,r)
            if sig in targets:
                return False
            if r<=H:
                targets.add(sig)
        return True
    fixed,_ = supports(H,e)
    fixed_bits = sum(1<<x for x in fixed)
    robust = 0
    for bits in range(1<<(A+1)):
        ok = safe(bits,e)
        assert ok==cut_test(bits,e,cuts)
        if ok:
            assert bits&fixed_bits==fixed_bits
            robust += 1
    return {"H":H,"e":e,"all_supports":1<<(A+1),"robust":robust}


def main():
    values = [(h,e) for e in [1,2] for h in range(3*e,19)]
    values += [(3*e,e) for e in [3,4,5,6]]
    # The two legacy failure witnesses also exercise an odd prime and an above-horizon order.
    old1 = sorted(set(range(12))-{4,5,6,7})
    assert pattern(old1,4)==pattern(old1,8)
    old2 = [0,3,6]
    assert pattern(old2,1)==pattern(old2,3) and pattern(old2,1)!=pattern(old2,2)
    answer = {"polynomial":polynomial_certificate(),
              "all_support_crosscheck":[exhaustive_crosscheck(h,e) for h,e in [(6,1),(8,1),(6,2),(8,2),(9,3)]],
              "exact_optima":[exact_optimum(h,e) for h,e in values],
              "large_examples":[{"H":h,"e":e,**finite_lower(h,e)} for h,e in
                                [(100,1),(100,2),(4096,1),(4096,2),(900,300),(3000,1000)]],
              "legacy_aliases_verified":[[4,8],[1,3]]}
    print(json.dumps(answer,indent=2))


if __name__=="__main__":
    main()
