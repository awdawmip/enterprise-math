"""Rebuild the section, precision and endpoint certificates using exact integer arithmetic."""
from math import comb, gcd, isqrt, prod
import json


def section(x, q, j, shifted):
    r = (x + q // 2) % q - q // 2
    twist = ((j + 2) * r + 2 * j) % 7 - 3 if shifted else 0
    return r + q * twist


def vp(x, p):
    if not x:
        raise ValueError("valuation needs a nonzero argument")
    value = 0
    while x % p == 0:
        x //= p
        value += 1
    return value


def carry(r, s, q, A):
    assert (r*r - s) % q == 0
    c = (r*r-s) // q
    return q*A*A + 2*r*A + c


def complete_domains():
    rows = []
    for q in (3, 5, 7, 9, 15):
        for k in (2, 3, 4):
            modulus = q**k
            tower = modulus // q
            for x in range(modulus):
                r = section(x,q,0,False)
                R = section(x,q,0,True)
                a, A = (x-r)//q % tower, (x-R)//q % tower
                for j in range(3):
                    s, S = section(r*r,q,j+1,False), section(R*R,q,j+1,True)
                    t, tnext = (R-r)//q, (S-s)//q
                    c, C = (r*r-s)//q, (R*R-S)//q
                    assert C == c + 2*r*t + q*t*t - tnext
                    assert (a-A-t) % tower == 0
                    old_a = a
                    a, A = carry(r,s,q,a)%tower, carry(R,S,q,A)%tower
                    direct = pow(x, 1 << (j+1), modulus)
                    assert (s + q*a)%modulus == direct == (S + q*A)%modulus
                    if k >= 3:
                        u, v = old_a%q, (old_a//q)%q
                        w = (2*r*u+c)%q
                        z = (2*r*v+u*u+(2*r*u+c-w)//q)%q
                        assert a % (q*q) == w+q*z
                    r, R = s, S
            rows.append({"q":q, "k":k, "all_residues":modulus,
                         "one_step_checks_per_section":3*modulus,
                         "nonunit_inputs":sum(gcd(x,q)>1 for x in range(modulus))})
    return rows


def batch_curvature():
    checks = 0
    for p in (3,5,7,11):
        for d in (1,2,3,4,6,10,12):
            e = 1 << d
            order = 1 + vp(e-1,p)
            for r in (1, p-1, 1-2*p):
                s = pow(r,e,p)
                for a in (-2,1,p,p*p):
                    for b in (-p,1,2,p*p):
                        power = order + vp(a*b,p)
                        # The physical numerator has one extra factor p.
                        modulus = p**(power+2)
                        for u in (-2,0,3):
                            def numerator(offset):
                                return pow(r+p*(u+offset),e,modulus)
                            diff = (numerator(a+b)-numerator(a)-numerator(b)+numerator(0))%modulus
                            assert vp(diff,p) == 1+power
                            affine = pow(r,e,modulus)-s + p*e*pow(r,e-1,modulus)*u
                            assert (numerator(0)-s-affine) % p**(order+1) == 0
                            checks += 1
    return checks


def higher_differences():
    orders_checked = truncations = 0
    for p in (3,5,7):
        for d in (1,2,3,4,6):
            e = 1 << d
            r, s = -1, 1
            for j in range(1,min(e,7)+1):
                order = j-1+vp(prod(range(e-j+1,e+1)),p)
                directions = [-1 if i%3==0 else (p if i%3==1 else 2) for i in range(j)]
                target_order = order + sum(vp(a,p) for a in directions)
                modulus = p**(target_order+2)
                mixed = 0
                for mask in range(1<<j):
                    a = 3+sum(v for i,v in enumerate(directions) if mask & (1<<i))
                    sign = (-1)**(j-mask.bit_count())
                    mixed += sign*pow(r+p*a,e,modulus)
                assert vp(mixed%modulus,p)==target_order+1
                orders_checked += 1
            for m in range(1,7):
                modulus = p**m
                vals = [(pow(r+p*a,e,p*modulus)-s)//p for a in range(e+1)]
                coeff = []
                while vals:
                    coeff.append(vals[0]%modulus)
                    vals = [(b-a)%modulus for a,b in zip(vals,vals[1:])]
                degree = max(j for j,c in enumerate(coeff) if c)
                expected = max(j for j in range(1,e+1)
                               if j-1+vp(prod(range(e-j+1,e+1)),p)<m)
                assert degree == expected
                for a in range(2*p+2):
                    y=sum(c*comb(a,i) for i,c in enumerate(coeff[:degree+1]) if i<=a)
                    assert (s+p*y-pow(r+p*a,e,p*modulus))%(p*modulus)==0
                truncations += 1
    return {"subsets_for_general_step_differences":orders_checked,
            "Newton_degree_and_truncation_parameter_sets":truncations}


def angular_precision():
    rows = 0
    for p in (3,5,7):
        for k in (2,3,4,5):
            for depth in (1,2,3):
                e = 1 << depth
                for s in range(k):
                    for leading in range(1,p):
                        start, step = leading*p**s, p**(s+1)
                        states = {pow(x,e,p**k) for x in range(start,p**k,step)}
                        assert len(states) == p**max(0,k-e*s-1)
                        rows += 1
    return rows


def known_factors():
    hits = [(0,3),(1,5),(2,17),(3,257),(4,65537),(5,641),(5,6700417),(6,274177)]
    rows = []
    for n,p in hits:
        assert p>=3 and all(p%d for d in range(2,isqrt(p)+1))
        F = (1 << (1 << n)) + 1
        assert F % p == 0
        h = (p-1)//(1 << n)
        for k in range(2,13):
            modulus = p**k
            tower = modulus//p
            Q = (pow(2,p-1,modulus)-1)//p
            U = (F//p) % tower
            assert ((pow(1-p*U,h,modulus)-1)//p - Q) % tower == 0
            lifted = (1-pow(1+p*Q,pow(h,-1,tower),modulus))%modulus
            assert lifted == F % modulus
            if k>=3:
                q2 = p*p
                approx = (-Q*pow(h,-1,q2)+p*comb(h,2)*pow(h,-3,q2)*Q*Q) % q2
                assert approx == U % q2
        rows.append({"n":n, "p":p, "h":h, "verified_k_max":12,
                     "U_mod_p3":(F//p)%p**3, "Q_mod_p3":(pow(2,p-1,p**4)-1)//p})
    return rows


def branch_bijections():
    tests = 0
    for n,p in ((0,3),(1,5),(2,17)):
        h = (p-1)//(1<<n)
        for k in (2,3,4):
            domain = p**(k-1)
            observed = set()
            for z in range(domain):
                x = 2+p*z
                modulus = p**k
                U = ((pow(x,1<<n,modulus)+1)//p)%domain
                Q = (pow(x,p-1,modulus)-1)//p
                assert ((1-pow(1+p*Q,pow(h,-1,domain),modulus))%modulus)//p == U
                observed.add(U)
                tests+=1
            assert len(observed)==domain
    return tests


def example_641():
    p, k = 641, 4
    rows = []
    x = 2
    for j in range(6):
        r = section(x,p,j,False)
        A = (x-r)//p
        rows.append({"j":j, "r":r, "A_digits_low_first":[(A//p**i)%p for i in range(k-1)],
                     "outgoing_c":None if j==5 else (r*r-section(r*r,p,j+1,False))//p})
        x *= x
    assert rows[-1]["A_digits_low_first"] == [44,197,16]
    return rows


def negative_controls():
    q, r, s, a = 5,2,-1,1
    good, omitted = carry(r,s,q,a), 2*r*a+(r*r-s)//q
    assert ((s+q*good)%125, (s+q*omitted)%125) == (49,24)
    shifted_r, shifted_a = 7,0
    assert carry(shifted_r,s,q,shifted_a) == good
    stale_c = (r*r-s)//q
    bad = q*shifted_a**2 + 2*shifted_r*shifted_a + stale_c
    assert s+q*bad == 4
    physical = carry(4,1,3,carry(1,4,3,0))
    wrong_batch = 8*(-1)+5
    assert physical%9==0 and wrong_batch%9==6
    return {"two_step_shifted_affine_deletion_mod9":[physical%9,wrong_batch%9],
            "inputs_2_7_squared_plus_one":[5,50], "full_vs_omit_qA2_mod125":[49,24],
            "reusing_old_c_after_section_change_mod125":[49,4],
            "A_5_shift_t_1_correct_digits":[4,0], "unchanged_high_digit":[4,1]}


def main():
    print(json.dumps({"invariant_certificate":{"complete_square_domains":complete_domains(),
                          "known_primes":known_factors(), "p641_rows":example_641()},
                      "representative_change":{"sections":"centered and r+q*((((j+2)*r+2*j)%7)-3)",
                          "controls":negative_controls()},
                      "precision_cost":{"mixed_difference_checks":batch_curvature(),
                          "higher_differences":higher_differences(),
                          "angular_ball_class_counts":angular_precision(),
                          "variable_base_inputs_in_full_branch_tests":branch_bijections()}},
                     ensure_ascii=False,indent=2))


if __name__ == "__main__":
    main()
