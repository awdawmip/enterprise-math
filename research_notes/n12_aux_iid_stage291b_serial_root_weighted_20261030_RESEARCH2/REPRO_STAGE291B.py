#!/usr/bin/env python3
"""Stage291-B: rational BRC two-fiber word kernels and root-label obstruction.

Standard-library Fraction only. This program checks the DECLARED finite witness;
the real-measure and arbitrary finite-history theorem is proved separately.
"""
from collections import defaultdict
from fractions import Fraction as F

T = (F(1, 64), F(1, 32), F(31, 32), F(63, 64))
Z = (0, 0, 1, 1)  # certified nearest roots of f6 (0, alpha, beta, 1)
PLUS = tuple(F(k, 256) for k in (4, 126, 2, 124))
MINUS = tuple(F(k, 256) for k in (124, 2, 126, 4))
SOURCES = {'P': (F(1, 3), F(2, 3)), 'Q': (F(2, 5), F(3, 5))}
NAMES = ('0', '10', '11')


def f6(t):
    return t * (1 - t) * (t * t - t + F(1, 8)) ** 2


def stop2(t):
    assert F(0) <= t <= F(1)
    return {'0': 1 - t, '10': t * (1 - t), '11': t * t}


def incr(d, k, val):
    d[k] += val


def tv(a, b):
    return sum((abs(a.get(k, F(0)) - b.get(k, F(0)))
                for k in set(a) | set(b)), F(0)) / 2


def two_fiber_source(weights, source, adaptive=False, project=False):
    """Output (source, upstream label, A root, A word, B root, B word).

    The two Bernoulli trials at A revisit one latent T_A; the two at B
    revisit one latent T_B. No source/ancestor/word state is pooled.
    """
    result = defaultdict(F)
    for r, pr in enumerate(SOURCES[source]):
        for t, z, wt in zip(T, Z, weights):
            b = (F(63, 64) if z == 1 else F(1, 64)) if adaptive else F(1, 64)
            zb = 1 if b == F(63, 64) else 0
            ta = F(z) if project else t
            tb = F(zb) if project else b
            for wa, pwa in stop2(ta).items():
                for wb, pwb in stop2(tb).items():
                    incr(result, (source, r, z, wa, zb, wb), pr * wt * pwa * pwb)
    return dict(result)


def without_root(d):
    out = defaultdict(F)
    for (i, r, z, wa, zb, wb), m in d.items():
        incr(out, (i, r, wa, wb), m)
    return dict(out)


def bmarg(d):
    out = defaultdict(F)
    for key, mass in d.items():
        incr(out, key[-1], mass)
    return dict(out)


def amom(weights, k):
    return sum((w * t ** k for w, t in zip(weights, T)), F(0))


def full_source_check():
    assert all(0 < t < 1 for t in T)
    assert all(w > 0 for w in PLUS + MINUS)
    assert sum(PLUS) == sum(MINUS) == 1
    assert set(Z) == {0, 1}
    assert len(SOURCES) == 2 and all(sum(p) == 1 and all(x > 0 for x in p)
                                      for p in SOURCES.values())
    assert [amom(PLUS, k) for k in range(3)] == [
        F(1), F(1, 2), F(3909, 8192)]
    assert [amom(MINUS, k) for k in range(3)] == [
        F(1), F(1, 2), F(3909, 8192)]
    eps_a_plus = sum((w * f6(t) for w, t in zip(PLUS, T)), F(0))
    eps_a_minus = sum((w * f6(t) for w, t in zip(MINUS, T)), F(0))
    eps_b = f6(F(1, 64))
    assert eps_a_plus == eps_a_minus == F(31368319, 137438953472)
    assert eps_b == F(12700863, 68719476736)
    disp_a = sum((w * min(t, 1 - t) for w, t in zip(PLUS, T)), F(0))
    assert disp_a == F(3, 128)
    assert sum((w * min(t, 1 - t) for w, t in zip(MINUS, T)), F(0)) == disp_a
    disp_b = F(1, 64)
    bound_exact_transport = 2 * (disp_a + disp_b)
    assert bound_exact_transport == F(5, 64)

    report = []
    for source in SOURCES:
        for adaptive in (False, True):
            a = two_fiber_source(PLUS, source, adaptive)
            b = two_fiber_source(MINUS, source, adaptive)
            ap = two_fiber_source(PLUS, source, adaptive, project=True)
            bp = two_fiber_source(MINUS, source, adaptive, project=True)
            assert len(a) == len(b) == 2 * 2 * 3 * 3  # all 36 retained-label paths positive
            assert all(x > 0 for x in a.values())
            assert all(x > 0 for x in b.values())
            assert sum(a.values()) == sum(b.values()) == 1
            assert tv(a, b) == F(1, 64)
            pooled = tv(without_root(a), without_root(b))
            expected = F(31, 2048) if adaptive else F(0)
            assert pooled == expected
            assert tv(bmarg(a), bmarg(b)) == expected
            assert tv(a, ap) <= bound_exact_transport
            assert tv(b, bp) <= bound_exact_transport
            report.append((source, 'adaptive' if adaptive else 'baseline',
                           len(a), tv(a, b), pooled, tv(a, ap), tv(b, bp)))
    assert tv(stop2(F(1, 64)), stop2(F(63, 64))) == F(31, 32)

    # Ordinary stagewise localizer-based bound; deliberately looser.
    c = F(7, 32768)
    # Avoid floating point: verify the rational exact-displacement bound
    # and the squared Jensen/weighted-root premise independently.
    assert c * disp_a ** 2 <= eps_a_plus
    assert c * disp_b ** 2 <= eps_b
    for src, mode, paths, full, pooled, pa, pb in report:
        print(f'{src} {mode}: positive_paths={paths}, full_root_TV={full}, '
              f'pooled_TV={pooled}, projected_plus_TV={pa}, '
              f'projected_minus_TV={pb}')
    print('A_first_moments=', tuple(str(amom(PLUS, k)) for k in range(3)))
    print('A_localizer_defect=', eps_a_plus, 'B_localizer_defect=', eps_b)
    print('weighted_exact_displacement_A=', disp_a,
          'B=', disp_b, 'two_fiber_TV_upper_bound=', bound_exact_transport)

    # Ancestor-dependent raw Y_A access: no descent through retained root.
    for d in (F(1, 16), F(1, 64), F(1, 256)):
        assert f6(d) == f6(1 - d) and f6(d) > 0
        future_tv = tv(stop2(d), stop2(1 - d))
        assert future_tv == 1 - 2 * d
        print(f'raw_ancestor_probe_d={d}: A_and_B_localizer={f6(d)}, '
              f'B_word_TV={future_tv}, B_hidden_root_TV=1')
    print('STAGE291B_TWO_FIBER_ROOT_WEIGHTED_EXACT_PASS')


if __name__ == '__main__':
    full_source_check()
