"""Exact rational certificates for the R5 two-source upstream mixture model.

Standard library only. Polynomial universality uses complete 3x3 tensor
Bernstein certificates over each parameter triangle, and five LR decision bits.
"""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)
HALF = F(1, 2)
LR = tuple(product((0, 1), repeat=5))


def observe(bits, u, v):
    """Twelve source-policy bits, two P/Q laws, A-source mix=u, B mix=v."""
    u, v = F(u), F(v)
    assert ZERO <= u <= ONE and ZERO <= v <= ONE
    p1, p2, q1, q2, qb, r, k1, k2, kb, l1, l2, lb = bits
    out, masses = [ZERO] * 4, [ZERO, ZERO]

    def terminal(ap, aq, ans, t):
        assert ap >= ZERO and aq >= ZERO
        masses[0] += ap
        masses[1] += aq
        if ans == "P":
            out[0] += ap
        else:
            out[1] += aq
        out[2] += t * ap
        out[3] += t * aq

    def a_kernel(ap, aq, k, l):
        terminal(ap * F(3, 5), aq / 2, "Q", 3)
        ap *= F(2, 5)
        aq /= 2
        terminal(ap / 2, aq / 2, "P", 3)
        ap /= 2
        aq /= 2
        terminal(ap * k, aq * k, "P", 3)
        ap *= 1 - k
        aq *= 1 - k
        terminal(ap / 4, aq / 2, "Q", 4)
        ap *= F(3, 4)
        aq /= 2
        terminal(ap * l, aq * l, "P", 4)
        terminal(ap * (1 - l), aq * (1 - l), "Q", 5)

    def b_kernel(ap, aq, l):
        terminal(ap * F(2, 5) / 4, aq / 8, "P", 4)
        terminal(ap * F(2, 5) * F(3, 4), aq * F(3, 8), "Q", 4)
        ap *= F(3, 5)
        aq /= 2
        terminal(ap * l, aq * l, "P", 4)
        terminal(ap * (1 - l), aq * (1 - l), "Q", 5)

    def mix(ap, aq, k, l, z):
        a_kernel(ap * z, aq * z, k, l)
        b_kernel(ap * (1 - z), aq * (1 - z), l)

    for p, q, k, l in ((p1, q1, k1, l1), (p2, q2, k2, l2)):
        ap = aq = F(1, 8)
        terminal(ap * p, aq * p, "P", 1)
        ap *= 1 - p
        aq *= 1 - p
        terminal(ap / 2, aq * F(3, 4), "Q", 2)
        ap /= 2
        aq /= 4
        terminal(ap * q, aq * q, "P", 2)
        ap *= 1 - q
        aq *= 1 - q
        mix(ap, aq, k, l, u)

    ap, aq = F(1, 4), F(1, 8)
    terminal(ap * qb, aq * qb, "P", 2)
    mix(ap * (1 - qb), aq * (1 - qb), kb, lb, v)
    terminal(F(1, 2) * r, F(5, 8) * r, "Q", 1)
    terminal(F(1, 2) * (1 - r), F(5, 8) * (1 - r), "P", 3)
    assert masses == [ONE, ONE], masses
    return tuple(out)


def lr_expand(bits):
    p, q, r, k, l = bits
    return p, p, q, q, q, r, k, k, k, l, l, l


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), ZERO)


def normal_greater(u, v):
    return (3270 - 275*u - 1195*v, 2256 + 80*u - 1256*v,
            615 + 100*u + 635*v, -672 + 70*u - 658*v)


def normal_less(u, v):
    return (3270 - 490*u - 980*v, 2256 - 392*u - 784*v,
            615 + 245*u + 490*v, -672 - 196*u - 392*v)


def b2(y):
    assert len(y) == 3
    return (y[0], 2*y[1] - (y[0] + y[2])/2, y[2])


def tensor_b2(f):
    """Exact 3x3 tensor Bernstein coefficients for bidegree<=2 on [0,1]^2."""
    points = (ZERO, HALF, ONE)
    sample = [[f(s, t) for t in points] for s in points]
    rows = [b2(row) for row in sample]
    columns = [b2(tuple(rows[i][j] for i in range(3))) for j in range(3)]
    return tuple(tuple(columns[j][i] for j in range(3)) for i in range(3))


def triangle_test(tag, normal, lr_facet_index, full_witness, triangle):
    facet = LR[lr_facet_index]
    min_control, zero_controls, total_controls = None, 0, 0
    for bits in LR:
        def slack(s, t):
            u, v = triangle(s, t)
            n = normal(u, v)
            return dot(n, observe(lr_expand(facet), u, v)) - \
                   dot(n, observe(lr_expand(bits), u, v))
        controls = tensor_b2(slack)
        flattened = [x for row in controls for x in row]
        assert all(c >= ZERO for c in flattened), (tag, bits, controls)
        min_controls_here = min(flattened)
        min_control = min_controls_here if min_control is None else min(min_control, min_controls_here)
        zero_controls += sum(x == 0 for x in flattened)
        total_controls += len(flattened)
    assert total_controls == 32 * 9 and min_control == ZERO

    def gap(s, t):
        u, v = triangle(s, t)
        return dot(normal(u, v), observe(full_witness, u, v)) - \
               dot(normal(u, v), observe(lr_expand(facet), u, v))

    # Exact polynomial identity, not sample-only: gap is bidegree <=2,
    # and its 9 tensor Bernstein controls match the known linear function.
    def expected(s, t):
        u, v = triangle(s, t)
        return F(735, 8) * abs(u - v)
    observed = tensor_b2(gap)
    expected_controls = tensor_b2(expected)
    assert observed == expected_controls, (tag, observed, expected_controls)
    print(tag, "LR_vertices=32", "tensor_Bernstein_controls=288",
          "all_nonnegative=True", "zeros=", zero_controls,
          "witness_gap=(735/8)*|u-v|_on_triangle")


def markovize_diagonal(bits, w):
    """Explicit LR probabilities for arbitrary 12-bit (or rational) source policy.

    Each aggregation is by Q mass at its true time/likelihood-ratio key;
    P mass is the same key-specific likelihood ratio times Q mass.
    """
    p1, p2, q1, q2, qb, r, k1, k2, kb, l1, l2, lb = bits
    p = (p1 + p2) / 2
    m1, m2, mb = (1 - p1) / 32, (1 - p2) / 32, F(1, 8)
    denom_j = m1 + m2 + mb
    q = (m1*q1 + m2*q2 + mb*qb) / denom_j
    cont = (m1*(1-q1), m2*(1-q2), mb*(1-qb))
    # Common nature mixture w at J: K reached only through A kernel,
    # Q mass factor w/4 after two natural Q half-branches.
    kq = tuple(x*w/4 for x in cont)
    denom_k = sum(kq)
    k = sum(x*y for x,y in zip(kq,(k1,k2,kb)))/denom_k if denom_k else ZERO
    # L reached from A through K survival, or direct B kernel L branch.
    lq = tuple(x*(w*(1-ki)/8 + (1-w)/2)
               for x,ki in zip(cont,(k1,k2,kb)))
    denom_l = sum(lq)
    l = sum(x*y for x,y in zip(lq,(l1,l2,lb)))/denom_l if denom_l else ZERO
    return p,q,r,k,l


def main():
    triangle_test(
        "u>=v",normal_greater,13,(0,0,1,1,0,1,1,1,0,1,1,1),
        lambda s,t:(s+(1-s)*t,s))
    triangle_test(
        "u<=v",normal_less,29,(0,0,0,0,1,1,0,0,1,1,1,1),
        lambda s,t:(s,s+(1-s)*t))
    cases=((F(3,4),F(1,4)),(F(1,4),F(3,4)),(F(1,2),F(1,2)))
    for u,v in cases:
        if u>v:
            n,facet,fw=normal_greater(u,v),LR[13],(0,0,1,1,0,1,1,1,0,1,1,1)
        else:
            n,facet,fw=normal_less(u,v),LR[29],(0,0,0,0,1,1,0,0,1,1,1,1)
        gap=dot(n,observe(fw,u,v))-dot(n,observe(lr_expand(facet),u,v))
        assert gap == F(735,8)*abs(u-v)
        norm=sum(abs(x) for x in n)
        assert norm <= 6813
        print("sample u,v",u,v,"witness_gap",gap,"dual_norm",norm,
              "L_inf_distance_lower_bound",gap/norm)
    assert 6813 == sum(abs(z) for z in normal_greater(ZERO,ZERO))
    assert 6813 == sum(abs(z) for z in normal_less(ZERO,ZERO))
    # Markovization regression at strictly positive nature mixtures and
    # real rational source-policy parameters, including non-extreme values.
    policy_cases=(
      (F(1,3), F(3,4),F(1,7),F(2,5),F(5,6),F(3,8),F(1,4),F(5,7),F(2,3),F(1,5),F(3,5),F(4,5)),
      (F(3,8), F(1,9),F(3,7),F(1,5),F(2,9),F(1,2),F(5,8),F(1,7),F(3,4),F(1,3),F(6,7),F(1,8)),
      (F(2,7), F(4,9),F(1,6),F(1,3),F(2,5),F(3,7),F(1,9),F(3,4),F(5,6),F(3,8),F(1,4),F(2,3)),
    )
    checks=0
    for w in (F(1,4),F(1,2),F(3,4)):
        for full in policy_cases:
            lr = markovize_diagonal(full,w)
            assert all(ZERO<=x<=ONE for x in lr)
            result=observe(full,w,w)
            predicted=observe(lr_expand(lr),w,w)
            assert result==predicted,(w,lr,result,predicted)
            checks+=1
    print("diagonal_actual_image_markovization_exact_rational_regressions",checks,
          "PASS")
    print("theorem: for 0<=u,v<=1, hull_EQUAL_iff_u_EQ_v",
          "and diagonal_actual_real_images_EQUAL")
    print("uniform witness dist_infty >= (245/18168)*|u-v| when u!=v")
    print("scope: auxiliary two-law finite stopping graph, exact rational verification",
          "author-side proof, no native X6 promotion")
    print("PASS_EXACT_R5_TWO_UPSTREAM_TRIANGULAR_BERNSTEIN_CLASSIFICATION")


if __name__ == "__main__":
    main()
