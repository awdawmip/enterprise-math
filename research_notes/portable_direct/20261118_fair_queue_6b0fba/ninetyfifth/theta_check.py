"""Finite checks for P46 fixed symmetric theta characteristics. Standard library."""
from collections import Counter
from itertools import product, combinations_with_replacement
import json


def bitdot(x, y):
    return (x & y).bit_count() % 2


def four_action(rows, v):
    return sum(bitdot(row, v) << j for j, row in enumerate(rows))


def symplectic_model():
    summary = Counter()
    signatures = Counter()
    masks = list(combinations_with_replacement(range(4), 2))
    for bits in range(1 << len(masks)):
        rows = [0] * 4
        for n, (i, j) in enumerate(masks):
            if (bits >> n) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
        image = [four_action(rows, y) for y in range(16)]
        if len(set(image)) != 16:
            continue
        diag = sum(((rows[i] >> i) & 1) << i for i in range(4))
        alpha = image.index(diag)
        fixed = []
        # For q(x,y)=x.y+a.x+b.y, pull back along (x,y)->(x+B*y,y).
        # Its difference depends on y only, so checking all y at x=0 suffices.
        for a, b in product(range(16), repeat=2):
            if all((bitdot(image[y], y) ^ bitdot(a, image[y]) ^ bitdot(b,y)) == bitdot(b,y)
                   for y in range(16)):
                assert a == alpha
                fixed.append((a,b))
        even = sum(bitdot(a,b) == 0 for a,b in fixed)
        odd = len(fixed) - even
        assert len(fixed) == 16 and (even, odd) == ((16,0) if not diag else (8,8))
        summary["alternating" if not diag else "nonalternating"] += 1
        signatures[even,odd] += 1
    # Independent signed Gauss sums of all 256 quadratic refinements.
    arfs = Counter()
    for a,b in product(range(16), repeat=2):
        sign_sum = sum((-1)**(bitdot(x,y)^bitdot(a,x)^bitdot(b,y))
                       for x,y in product(range(16), repeat=2))
        assert sign_sum == (-1)**bitdot(a,b)*16
        arfs[sign_sum] += 1
    return {"all_binary_symmetric_4_by_4": 1024, "invertible_by_type": dict(summary),
            "fixed_parities_by_type": {f"{e}_even_{o}_odd": n for (e,o),n in signatures.items()},
            "direct_quadratic_Gauss_sums": dict(arfs)}


def mul(x, y):
    a,b = x
    c,d = y
    return ((a*c-b*d)%7,(a*d+b*c)%7)


def trace_census():
    det = (1,0)
    for sign in (1,1,1,-1):
        det = mul(det, (1,-sign))
    assert det == (0,3)  # -4 i in F_49 under the pullback convention.
    solutions = []
    for even, odd in [(16,0),(8,8)]:
        for plus in range(even+1):
            for pos_i in range(odd+1):
                minus, neg_i = even-plus,odd-pos_i
                trace = ((plus-minus)%7, (neg_i-pos_i)%7)
                if trace == det:
                    solutions.append((plus,minus,pos_i,neg_i))
    assert solutions == [(4,4,6,2)]
    counts = Counter()
    weights = [1,1,1,3]
    for i,j in combinations_with_replacement(range(4),2):
        counts[(weights[i]+weights[j])%4] += 1
    assert dict(counts) == {2:7,0:3}
    return {"field": "F_7[i]/(i^2+1)", "det_one_minus_cotangent_as_real_imag": det,
            "integer_lifts_in_eta_order_1_minus1_i_minusi": solutions,
            "linear_monomials_by_i_exponent": dict(Counter(weights)),
            "quadratic_monomials_by_i_exponent": dict(counts), "fixed_point_degree": 16,
            "nonfixed_orbits_even_odd": [(136-8)//2,(120-8)//2]}


def curve_and_division():
    f = lambda x:(x**3+x*x+1)%7
    values = [f(i) for i in range(7)]
    assert 0 not in values
    # The root of the remainder of f modulo x²−5 is not a root of x²−5.
    test = (-6*pow(5,-1,7))%7
    assert (test**2-5)%7 and all(x*x%7 != 6 for x in range(7))
    # Frobenius on the division polynomial quotient F_343.
    def triple_mul(x,y):
        terms=[0]*5
        for i,xi in enumerate(x):
            for j,yj in enumerate(y):
                terms[i+j] += xi*yj
        for t in (4,3):
            terms[t-3] -= terms[t]
            terms[t-1] -= terms[t]
        return tuple(i%7 for i in terms[:3])
    root=(0,1,0)
    forbit=[]
    val=root
    for _ in range(3):
        forbit.append(val)
        res=(1,0,0)
        for _ in range(7):
            res=triple_mul(res,val)
        val=res
    assert len(set(forbit))==3 and root==val
    return {"two_division_cubic_at_0_to_6": values, "common_root_test_x": test,
            "F_343_Frobenius_orbit_in_cubic_power_basis": forbit,
            "cotangent_eigenvalue_exponents_on_omega_xomega_yomega_x2omega": [1,1,3,1]}


def product_example():
    # On each E the fixed odd corresponds to the origin and has a simple zero;
    # the fixed even corresponds to the other sigma-fixed two-torsion point.
    census = Counter()
    degrees = Counter()
    for odd in product([0,1],repeat=4):
        eta_exp = sum(e*w for e,w in zip(odd,[1,1,1,-1])) % 4
        degree = sum(odd)
        assert degree%2 == eta_exp%2
        census[eta_exp] += 1
        degrees[eta_exp,degree] += 1
    assert [census[k] for k in (0,2,1,3)] == [4,4,6,2]
    assert sum(n for (k,t),n in degrees.items() if t and k%2==0) == 7
    assert degrees[0,2] == 3 and degrees[2,4] == 1
    return {"model":"E^4, product theta and automorphism (i,i,i,-i)",
            "fixed_theta_counts_by_eta_exponent_and_exact_vanishing_order":
            {f"i^{e}_order_{d}":n for (e,d),n in sorted(degrees.items())}}


if __name__ == "__main__":
    out = {"curve":curve_and_division(), "binary_models":symplectic_model(),
           "trace_and_jets":trace_census(), "separate_decomposable_example":product_example(),
           "scope":"finite algebra, eigenspace counts and a decomposable comparison; no period or Hessian numerics"}
    print(json.dumps(out,ensure_ascii=False,indent=2))
