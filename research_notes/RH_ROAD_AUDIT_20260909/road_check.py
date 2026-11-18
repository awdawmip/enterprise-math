"""Finite checks for the composite-road audit. Run with Python 3.11 or later."""
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from itertools import accumulate
import json


def dec(q):
    q = F(q)
    return D(q.numerator) / D(q.denominator)


def near(a, b):
    if abs(a - b) > D('1e-49') * max(1, abs(a), abs(b)):
        raise ArithmeticError(f"analytic expressions disagree: {a}, {b}")


def displayed(x):
    return format(x, '.22f')


def segment_energy(intercept, slope, lower, upper):
    """Integral of (intercept-slope*x)^2/x^2 from lower to upper."""
    h, c, l, u = map(dec, (intercept, slope, lower, upper))
    return h*h*(1/l-1/u) - 2*h*c*(u/l).ln() + c*c*(u-l)


def check_green():
    # The signed measure has both off-grid atoms and atoms outside the window.
    atoms = [(F(1, 2), F(3, 2)), (F(2), F(-1)), (F(7, 2), F(4, 3)),
             (F(5), F(-5, 7)), (F(9), F(2)), (F(13), F(-11))]
    slope = F(3, 8)
    results = []
    for low, high in [(F(1), F(9)), (F(2), F(13)), (F(5, 2), F(11, 2))]:
        active = [(max(low, p), v) for p, v in atoms if p < high]
        cuts = sorted({low, high, *(p for p, _ in active)})
        cumulative = sum((sum(v for p, v in active if p <= a)**2 *
                          (1/a - 1/b) for a, b in zip(cuts, cuts[1:])), F(0))
        kernel = sum((v*w*(1/max(p, q)-1/high)
                      for p, v in active for q, w in active), F(0))
        assert cumulative == kernel
        piecewise = sum((segment_energy(sum(v for p, v in active if p <= a),
                                        slope, a, b)
                         for a, b in zip(cuts, cuts[1:])), D(0))
        paired = (dec(kernel) + dec(slope**2*(high-low))
                  - 2*dec(slope)*sum((dec(v)*dec(high/p).ln()
                                      for p, v in active), D(0)))
        near(piecewise, paired)
        results.append({'interval': [str(low), str(high)],
                        'atomic_energy_exact': str(kernel),
                        'with_uniform_drift': displayed(paired)})
    return results


def check_cells():
    cases = 0
    for n in (1, 2, 3, 9, 41, 128):
        t = D(n)
        weight = D(1)/(t*(t+1))
        logratio = (1+1/t).ln()
        center = logratio/weight
        variance_mass = 1-logratio**2/weight
        assert t < center < t+1 and variance_mass > 0
        for intercept in (F(-3), F(0), F(7, 3), F(n+2)):
            for slope in (F(-1, 2), F(0), F(5, 7)):
                exact = segment_energy(intercept, slope, n, n+1)
                completed = (weight*(dec(intercept)-dec(slope)*center)**2
                             + dec(slope)**2*variance_mass)
                near(exact, completed)
                cases += 1
    return cases


def prime_divisors(n):
    p = 2
    while p*p <= n:
        if n % p == 0:
            yield p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        yield n


def road_increment(n, a):
    answer = F(1)
    for p in prime_divisors(n):
        answer *= 1-F(1, p**a)
    return answer


def check_arithmetic_green():
    rows = []
    for exponent, horizon in ((1, 4), (1, 12), (2, 17), (3, 24)):
        atoms = {n: road_increment(n, exponent) for n in range(2, horizon+1)}
        atomic = sum((v*w*(F(1, max(n,m))-F(1, horizon))
                      for n,v in atoms.items() for m,w in atoms.items()), F(0))
        cross = sum((dec(v)*dec(F(horizon,n)).ln() for n,v in atoms.items()), D(0))
        best_c = cross/horizon
        minimum = dec(atomic)-cross*cross/horizon
        for c in (D('0.375'), best_c, best_c+D('0.125')):
            by_cell = c*c
            mass = F(0)
            for n in range(1, horizon):
                mass += atoms.get(n, 0)
                by_cell += segment_energy(mass, c, n, n+1)
            near(by_cell, dec(atomic)-2*c*cross+horizon*c*c)
            near(by_cell, minimum+horizon*(c-best_c)**2)
        rows.append({'exponent':exponent,'horizon':horizon,
                     'atomic_quadratic_form_exact':str(atomic),
                     'minimizing_background':displayed(best_c),
                     'minimum_energy':displayed(minimum)})
    return rows


def check_discrete_identity():
    # Integer a makes the road increments rational. The cell identity holds for
    # any c, so varying rational drifts here avoids a zeta-value approximation.
    results = []
    for a, c in ((1, F(1, 2)), (2, F(3, 4)), (3, F(4, 5))):
        horizon = 48
        intercept = F(0)
        discrete = F(0)
        integral = dec(c*c)   # On 0 < x < 1 the discrepancy is -cx.
        weighted_loss = D(0)
        for n in range(1, horizon+1):
            if n > 1:
                intercept += road_increment(n, a)
            mid = intercept - c*F(2*n+1, 2)
            discrete += mid*mid/n**2
            weighted = segment_energy(intercept, c, n, n+1)
            integral += weighted
            # Integrate E^2 w independently, via its polynomial and log moments.
            t = D(n)
            i0 = 1/t**2-(1/t-1/(t+1))
            i1 = (t+D('0.5'))/t**2-(1+1/t).ln()
            i2 = (t*t+t+D(1)/3)/t**2-1
            loss = dec(intercept)**2*i0-2*dec(intercept*c)*i1+dec(c)**2*i2
            assert loss >= 0
            weighted_loss += loss
        harmonic2 = sum((F(1,n*n) for n in range(1,horizon+1)), F(0))
        right = dec(c*c*(1+harmonic2/12))-weighted_loss
        near(integral-dec(discrete), right)
        results.append({'a': a, 'c': str(c), 'last_complete_cell': horizon,
                        'Q_truncated_minus_D_truncated': displayed(right)})
    return results


def check_psi():
    psi = D(0)
    correction = D(0)
    early = []
    for n in range(1, 9):
        primes = list(prime_divisors(n))
        if len(primes) == 1:
            psi += D(primes[0]).ln()
        t = D(n)
        mean_square = ((t-psi)**2+(t-psi)+D(1)/3)/t**2
        exact_weight = (1 - 2*psi*(1+1/t).ln() + psi**2/(t*(t+1)))
        cell = mean_square-exact_weight
        assert cell > 0
        if n == 1:
            first_cell = cell
        correction += cell
        early.append({'N': n, 'psi': displayed(psi), 'positive_loss': displayed(cell)})
    first = F(1, 3)+1  # Integral from 1 to 2 of x^2-1.
    near(first_cell, dec(first))
    coarse_upper = 1+F(2,12)-first   # zeta(2)<1+integral_1^infty x^-2 dx.
    assert coarse_upper == F(-1,6)
    return {'first_cell_loss_exact': str(first), 'cells': early,
            'first_eight_total_loss': displayed(correction),
            'C_strict_upper_rational_from_first_cell': str(coarse_upper)}


def check_phase():
    base = (1,-1,0)
    rows = []
    for shift in range(3):
        v = base[shift:]+base[:shift]
        autocorr = [sum(F(v[j]*v[(j+h)%3],3) for j in range(3)) for h in range(3)]
        assert autocorr == [F(2,3), F(-1,3), F(-1,3)]
        prefix = list(accumulate(v))
        anchored = sum((F(y*y,m*(m+1)) for m,y in enumerate(prefix,1)), F(0))
        inverse_square = sum((F(y*y,h*h) for h,y in enumerate(prefix,1)), F(0))
        rows.append({'cycle':v,'autocorrelation':list(map(str,autocorr)),
                     'anchored_Green_energy_through_x4':str(anchored),
                     'anchored_inverse_square_energy_first_three':str(inverse_square)})
    assert len({z['anchored_Green_energy_through_x4'] for z in rows}) == 3
    # The one-period numerator identity proves the same gap at every H by periodicity.
    f = list(accumulate(base))
    g = list(accumulate(base[1:]+base[:1]))
    excess = [b*b-a*a for a,b in zip(f,g)]
    assert excess == [0,1,0]
    limit = 120
    lhs = sum(F(excess[(h-1)%3],h*h) for h in range(1,limit+1))
    rhs = sum(F(1,h*h) for h in range(2,limit+1,3))
    assert lhs == rhs and rhs > 0
    return {'cycles':rows,'squared_prefix_excess_by_H_residues_1_2_0':excess,
            'exact_inverse_square_gap_through_H120':str(rhs)}


def mobius(n):
    primes = tuple(prime_divisors(n))
    return 0 if any(n % (p*p) == 0 for p in primes) else (-1)**len(primes)


def residue(n, m):
    return F(m % n, n)


def check_prefix():
    limit = 48
    checks = 0
    for n in range(2, limit+1):
        divisors = [d for d in range(1,n+1) if n % d == 0]
        def port(f):
            return sum(mobius(n//d)*(f(d)-f(d-1)) for d in divisors)
        assert port(lambda m:m) == 0
        for k in range(2,limit+3):
            assert port(lambda m: residue(k,m)) == -int(n==k)
            checks += 1
    for M in range(1,limit+1):
        slope = sum(F(mobius(n),n) for n in range(1,M+1))
        for m in range(1,M+1):
            assert slope*m-sum(mobius(n)*residue(n,m) for n in range(2,M+1)) == 1
            assert residue(M+1,m) == F(m,M+1)
    weights = (2,0,-1,0,-1,1)
    dual = sum(v*v*m*(m+1) for m,v in enumerate(weights,1))
    for k in range(2,2*limit+1):
        assert sum(v*residue(k,m) for m,v in enumerate(weights,1)) == -int(k==6)
    assert sum(weights)==1 and dual==92
    return {'largest_prefix':limit,'individual_Ln_column_tests':checks,
            'L6_vector':weights,'L6_dual_squared_norm':dual,
            'squared_barrier_when_column_6_omitted':str(F(1,dual))}


def main():
    with localcontext() as context:
        context.prec = 72
        result = {'arithmetic':'Fractions for combinatorial identities; 72-place Decimal '
                  'with relative threshold 1e-49 for logarithmic finite-interval checks.',
                  'green_intervals':check_green(), 'arithmetic_Green_from_zero':check_arithmetic_green(),
                  'weighted_square_completions':check_cells(),
                  'finite_Q_minus_D':check_discrete_identity(), 'small_parameter_coefficient':check_psi(),
                  'period_three_translates':check_phase(), 'prefix_rigidity':check_prefix()}
        print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
