"""Stage296-B: exact rational witnesses for explicitly typed Bernoulli interfaces.

Only finite examples are checked here; continuum theorems are proved in PROOF_STAGE296B.md.
"""
from fractions import Fraction as F
from itertools import product

D = lambda a, b=1: F(a, b)
WORDS2 = tuple(product((0, 1), repeat=2))
WORDS3 = tuple(product((0, 1), repeat=3))


def tv(p, q):
    assert set(p) == set(q)
    return sum((abs(p[x] - q[x]) for x in p), F(0)) / 2


def source_laws(a):
    h, r, s = a * (1-a), (1-a)**2, a**2
    return ({(0,0): h, (0,1):r, (1,0):s, (1,1):h},
            {(0,0): h, (0,1):s, (1,0):r, (1,1):h})


def midpoint(p, q):
    return {key: (p[key]+q[key])/2 for key in p}


def parity_mix(equal_weight):
    # Draw an unobserved fair bit U, then B=U in E mode or B=1-U in X mode.
    return {(0,0): equal_weight/2, (1,1): equal_weight/2,
            (0,1): (1-equal_weight)/2, (1,0): (1-equal_weight)/2}


def adaptive_history(a):
    # First draw A ~ Bernoulli(1/2); then retune B using visible A.
    h = a*(1-a)
    pb1_if_a0, pb1_if_a1 = 1-2*h, 2*h
    return {(0,0): (1-pb1_if_a0)/2, (0,1): pb1_if_a0/2,
            (1,0): (1-pb1_if_a1)/2, (1,1): pb1_if_a1/2}


def moment(mix, degree):
    return sum((weight * theta**degree for theta, weight in mix), F(0))


def ordered_law(mix, n):
    return {word: sum((weight * theta**sum(word) * (1-theta)**(n-sum(word))
                       for theta, weight in mix), F(0))
            for word in product((0, 1), repeat=n)}


def first_success_stop(mix, n):
    # Terminal label is 1,...,n on first success, or F after n failures.
    ans = {k: sum((w * (1-t)**(k-1) * t for t,w in mix), F(0))
           for k in range(1, n+1)}
    ans['F'] = sum((w * (1-t)**n for t,w in mix), F(0))
    return ans


def assert_law(p):
    assert all(value >= 0 for value in p.values())
    assert sum(p.values(), F(0)) == 1


def check_two_stage():
    for a in [D(0), D(1,16), D(1,8), D(1,4), D(3,8), D(1,2)]:
        p0, p1 = source_laws(a)
        free = midpoint(p0,p1)
        phys = {w: D(1,4) for w in WORDS2}
        h = a*(1-a)
        coupled = parity_mix(2*h)
        adapt = adaptive_history(a)
        for p in (p0, p1, free, phys, coupled, adapt):
            assert_law(p)
        assert free == coupled == adapt
        free_risk = (tv(p0,free)+tv(p1,free))/2
        physical_risk = (tv(p0,phys)+tv(p1,phys))/2
        assert free_risk == D(1,2)-a
        assert physical_risk == (1-a)**2-D(1,4)
        assert physical_risk-free_risk == (D(1,2)-a)**2
        assert free[(1,1)]-D(1,4) == -(D(1,2)-a)**2
        print(f"two_stage a={a} free={free_risk} iid_mixed={physical_risk} "
              f"gap={physical_risk-free_risk} parity_weight={2*h}")
    assert parity_mix(D(1)) != parity_mix(D(3,8))
    assert parity_mix(D(0)) != parity_mix(D(3,8))
    assert adaptive_history(D(1,4))[(0,1)] * 2 == D(5,8)
    assert adaptive_history(D(1,4))[(1,1)] * 2 == D(3,8)


def check_three_stage():
    lo = [(D(0), D(1,3)), (D(3,4), D(2,3))]
    hi = [(D(1,4), D(2,3)), (D(1), D(1,3))]
    for mix in (lo,hi):
        assert sum((weight for _,weight in mix), F(0)) == 1
        assert moment(mix,1) == D(1,2)
        assert moment(mix,2) == D(3,8)
    l3, u3 = moment(lo,3), moment(hi,3)
    assert (l3,u3) == (D(9,32), D(11,32))
    assert u3-l3 == D(1,16)
    a3,b3 = ordered_law(lo,3),ordered_law(hi,3)
    a2,b2 = ordered_law(lo,2),ordered_law(hi,2)
    for p in (a3,b3,a2,b2,first_success_stop(lo,3),first_success_stop(hi,3)):
        assert_law(p)
    assert tv(a2,b2) == 0
    assert tv(a3,b3) == D(1,4)
    stop_tv = tv(first_success_stop(lo,3),first_success_stop(hi,3))
    assert stop_tv == D(1,16)
    mid = [(t,w/2) for mix in (lo,hi) for t,w in mix]
    assert moment(mid,3) == D(5,16)
    mid3 = ordered_law(mid,3)
    assert tv(a3,mid3) == tv(b3,mid3) == D(1,8)
    smid = first_success_stop(mid,3)
    assert tv(first_success_stop(lo,3), smid) == D(1,32)
    for k in range(9):
        lam = D(k,8)
        interpolated = [(t,(1-lam)*w) for t,w in lo] + [(t,lam*w) for t,w in hi]
        assert moment(interpolated,1) == D(1,2)
        assert moment(interpolated,2) == D(3,8)
        assert l3 <= moment(interpolated,3) <= u3
        assert tv(ordered_law(lo,3),ordered_law(interpolated,3)) == lam*D(1,4)
    print(f"three_stage m1=1/2 m2=3/8 m3_range=[{l3},{u3}] "
          f"full_word_tv_diameter={tv(a3,b3)} stop_tv_diameter={stop_tv} "
          f"full_minimax_radius={tv(a3,mid3)}")
    print("three_stage_lower:", a3)
    print("three_stage_upper:", b3)


if __name__ == '__main__':
    check_two_stage()
    check_three_stage()
    print('STAGE296B_COUPLING_AND_CUBIC_MOMENT_EXACT_PASS')
