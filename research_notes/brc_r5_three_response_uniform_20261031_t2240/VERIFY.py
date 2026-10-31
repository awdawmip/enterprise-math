"""Exact R5 three-terminal-response obstruction; author verification, not native X6."""
from fractions import Fraction as F
from itertools import product

ALPHA = (F(1, 4), F(1, 5))
KAPPA = (F(3, 4), F(1, 6))
KEYS = {'A': (1, F(1)), 'D': (2, F(1, 2)), 'Y': (2, F(3, 2)),
        'C': (2, F(1)), 'DH': (3, F(1, 4)), 'YH': (3, F(2)),
        'L': (3, F(1)), 'L4': (4, F(1))}
FULL_KEYS = ('A', 'D', 'Y', 'LD', 'LY', 'LC')
LR_KEYS = ('A', 'D', 'Y', 'L')
V0, W0 = F(1, 8), F(1, 4)
H_LO = (100, 180, -130, 107)
H_HI = (102, 79, 35, -54)
ZSTAR = F(1922, 4835)
MARGIN = F(26581, 77360)


def flow(action):
    leaves = {name: F(0) for name in KEYS}
    for i, (a, k) in enumerate(zip(ALPHA, KAPPA)):
        origin = F(1, 2)
        if not action(i, 'A'):
            leaves['A'] += origin
            continue
        d = y = origin * a
        c = origin * (1 - 2*a)
        if action(i, 'D'):
            leaves['DH'] += d*F(2, 3)
            leaves['L4' if action(i, 'LD') else 'L'] += d*F(1, 3)
        else:
            leaves['D'] += d
        if action(i, 'Y'):
            leaves['YH'] += y*F(1, 2)
            leaves['L4' if action(i, 'LY') else 'L'] += y*F(1, 2)
        else:
            leaves['Y'] += y
        leaves['C'] += c*(1-k)
        leaves['L4' if action(i, 'LC') else 'L'] += c*k
    assert sum(leaves.values()) == 1
    assert sum((q*KEYS[key][1] for key, q in leaves.items()), F(0)) == 1
    assert all(q >= 0 for q in leaves.values())
    return leaves


def full(bits):
    actions = [dict(zip(FULL_KEYS, bits[6*i:6*(i+1)])) for i in (0, 1)]
    return flow(lambda i, name: actions[i][name])


def lr(bits):
    actions = dict(zip(LR_KEYS, bits))
    return flow(lambda i, name: actions['L' if name in ('LD', 'LY', 'LC') else name])


def data(leaves):
    t_p = sum((q*t*lam for key, q in leaves.items()
               for t, lam in (KEYS[key],)), F(0))
    t_q = sum((q*t for key, q in leaves.items()
               for t, lam in (KEYS[key],)), F(0))
    return t_p, t_q, leaves['DH'], leaves['L4'], leaves['YH']


def observe(f, v, w, z):
    tp, tq, x, y, u = data(f)
    return (F(1, 2)+v*x/F(4)+w*y+2*z*u,
            F(1, 2)+v*x+w*y+z*u, tp, tq)


def coeff(f, h):
    p, q, a, b = h
    tp, tq, x, y, u = data(f)
    intercept = F(p+q, 2) + F(p, 4)*V0*x + q*V0*x + (p+q)*W0*y + a*tp + b*tq
    return intercept, (2*p+q)*u


def det4(rows):
    a = [[F(x) for x in row] for row in rows]
    result = F(1)
    for j in range(4):
        piv = next((i for i in range(j, 4) if a[i][j] != 0), None)
        if piv is None:
            return F(0)
        if piv != j:
            a[j], a[piv] = a[piv], a[j]
            result = -result
        val = a[j][j]
        result *= val
        for i in range(j+1, 4):
            fac = a[i][j]/val
            for k in range(j, 4):
                a[i][k] -= fac*a[j][k]
    return result


def main():
    assert [(1+k*(1-2*a))/a for a, k in zip(ALPHA, KAPPA)] == [F(11, 2)]*2
    all_lr = {bits:lr(bits) for bits in product((0, 1), repeat=4)}
    assert len(all_lr) == 16
    lo_full = full((1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0))
    hi_full = full((1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0))
    assert coeff(lo_full, H_LO) == (F(3819, 32), F(0))
    assert coeff(hi_full, H_HI) == (F(1037, 16), F(283, 16))
    for h, expected in ((H_LO, {F(0):F(117), F(171, 4):F(16321, 160)}),
                        (H_HI, {F(0):F(143, 2), F(2547, 80):F(4547, 80)})):
        groups = {}
        for leaves in all_lr.values():
            a, b = coeff(leaves, h)
            groups[b] = max(a, groups.get(b, a))
        assert groups == expected, (h, groups)
    def gap_lo(z):
        return min(F(75, 32), F(1387, 80)-F(171, 4)*z)
    def gap_hi(z):
        return min((283*z-107)/16, (319-566*z)/40)
    assert gap_lo(ZSTAR) == gap_hi(ZSTAR) == MARGIN
    assert gap_lo(F(-1, 2)) >= MARGIN
    assert gap_hi(F(1, 2)) == F(9, 10) >= MARGIN
    assert F(-1, 2) < ZSTAR < F(1, 2)
    # Real interval is proved in RESEARCH.md by monotonicity and concavity.
    for k in range(-50, 51):
        z = F(k, 100)
        assert max(gap_lo(z), gap_hi(z)) >= MARGIN
        for h, witness, lower in ((H_LO, lo_full, gap_lo(z)),
                                  (H_HI, hi_full, gap_hi(z))):
            val = sum(a*b for a, b in zip(h, observe(witness, V0, W0, z)))
            best_lr = max(sum(a*b for a, b in zip(h, observe(f, V0, W0, z)))
                          for f in all_lr.values())
            assert val-best_lr == lower
    # Rank-one z update implies the four-by-four minor is affine in z.
    rank_bits = ((0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0))
    def minor(z):
        obs = [observe(all_lr[b], V0, W0, z) for b in rank_bits]
        return det4([[obs[i+1][j]-obs[0][j] for j in range(4)] for i in range(4)])
    assert minor(F(0)) == F(152361, 1310720000)
    assert minor(F(1, 8)) == 0
    assert minor(F(1, 4)) == -F(152361, 1310720000)
    for leaves in all_lr.values():
        ep, eq, tp, tq = observe(leaves, V0, W0, F(1, 8))
        assert 8*(ep-eq)-tp+tq == 0
    x_max = y_max = F(0)
    for bits in product((0, 1), repeat=12):
        f = full(bits)
        _, _, x, y, _ = data(f)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    assert (x_max, y_max) == (F(3, 20), F(17, 40))
    drift_lo = F(123, 4)/1000 + F(119)/1000
    drift_hi = F(627, 40)/1000 + F(3077, 40)/1000
    assert drift_lo == F(599, 4000) and drift_hi == F(463, 5000)
    robust = MARGIN - max(drift_lo, drift_hi)
    assert robust == F(749817, 3868000) > 0
    print('PINNED_BASELINE v=1/8 w=1/4; theta0=theta1=11/2')
    print('LR_H_LO = max(117, 16321/160 + 171*z/4)')
    print('LR_H_HI = max(143/2, 4547/80 + 2547*z/80)')
    print('W_LO=(3819/32, 0*z); W_HI=(1037/16, 283*z/16)')
    print(f'z_cross={ZSTAR}; minimum_two_direction_witness_gap={MARGIN}')
    print('LR_four_rank iff z != 1/8; at z=1/8: 8(eP-eQ)-TP+TQ=0')
    print(f'FULL_x_max={x_max}; FULL_y_max={y_max}; full_policies=4096; lr_policies=16')
    print('robust_box |v-1/8|<=1/1000, |w-1/4|<=1/1000, |z|<=1/2')
    print(f'uniform_support_gap_in_box>={robust}; uniform_infinity_distance>={robust/517}')
    print('PASS_EXACT_R5_THREE_RESPONSE_UNIFORM_RECTANGLE_NO_GO')


if __name__ == '__main__':
    main()
