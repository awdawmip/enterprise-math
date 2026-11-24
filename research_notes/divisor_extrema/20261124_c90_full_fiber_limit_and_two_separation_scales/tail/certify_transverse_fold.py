"""Exact rational certificate of a simple three-spectrum fold crossing.

All mathematical acceptance uses Fraction intervals, including derivative
bounds and centered face enclosures. Display floats carry no proof weight.
The outward-rounded interval arithmetic follows the C89 double-slope helper.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

SCALE = 10**100


def lower(x):
    x = Q(x)
    return Q((x * SCALE).numerator // (x * SCALE).denominator, SCALE)


def upper(x):
    return -lower(-Q(x))


class I:
    def __init__(self, lo, hi=None):
        if isinstance(lo, I):
            self.lo, self.hi = lo.lo, lo.hi
            return
        self.lo, self.hi = lower(lo), upper(lo if hi is None else hi)
        assert self.lo <= self.hi

    def __add__(self, other):
        other = I(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -I(other)

    def __rsub__(self, other):
        return I(other) + -self

    def __mul__(self, other):
        other = I(other)
        values = [x * y for x in (self.lo, self.hi)
                  for y in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = I(other)
        assert not other.lo <= 0 <= other.hi
        return self * I(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return I(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return I(1)
        if n % 2 == 0 and self.lo <= 0 <= self.hi:
            return I(0, max(self.lo**n, self.hi**n))
        values = [self.lo**n, self.hi**n]
        return I(min(values), max(values))

    def json(self):
        return [str(self.lo), str(self.hi)]

    def display(self):
        return [float(self.lo), float(self.hi)]


class D:
    """Value and its two first partial derivatives as interval enclosures."""
    def __init__(self, value, da=0, dd=0):
        if isinstance(value, D):
            self.v, self.da, self.dd = value.v, value.da, value.dd
            return
        self.v, self.da, self.dd = I(value), I(da), I(dd)

    def __add__(self, other):
        other = D(other)
        return D(self.v + other.v, self.da + other.da, self.dd + other.dd)

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, -self.da, -self.dd)

    def __sub__(self, other):
        return self + -D(other)

    def __rsub__(self, other):
        return D(other) + -self

    def __mul__(self, other):
        other = D(other)
        return D(self.v * other.v,
                 self.da * other.v + self.v * other.da,
                 self.dd * other.v + self.v * other.dd)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = D(other)
        return D(self.v / other.v,
                 (self.da * other.v - self.v * other.da) / other.v**2,
                 (self.dd * other.v - self.v * other.dd) / other.v**2)

    def __rtruediv__(self, other):
        return D(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        if n == 0:
            return D(1)
        return D(self.v**n, n * self.v**(n - 1) * self.da,
                 n * self.v**(n - 1) * self.dd)


def quantities(a, d):
    m = Q(7, 16) * a**4 * d
    n = m * a
    u, v = m / (1 + m), n / (1 + n)
    h = 1 / (a - 1) + 5 - 4 * u - 5 * v
    T = 4 * u * (1 - u) + 5 * v * (1 - v)
    N = a / (a - 1)**2 + 16 * u * (1 - u) + 25 * v * (1 - v)
    R = Q(14, 3) + d / (d - 1) - u - v
    Na = -(a + 1) / (a - 1)**3 + (
        64 * m * (1 - m) / (1 + m)**3
        + 125 * n * (1 - n) / (1 + n)**3) / a
    Nd = (16 * m * (1 - m) / (1 + m)**3
          + 25 * n * (1 - n) / (1 + n)**3) / d
    P = N * R - T * (h - Q(1, 5))
    K = N * d * Nd - a * T * Na
    return {'h': h, 'N': N, 'T': T, 'R': R, 'Na': Na, 'Nd': Nd,
            'P': P, 'K': K}


def root_a(level, d, side):
    lo, hi = (Q(1, 2), Q(9, 10)) if side == 'left' else (Q(6, 5), Q(2))
    assert quantities(lo, d)['h'] > level > quantities(hi, d)['h']
    for _ in range(150):
        mid = (lo + hi) / 2
        if quantities(mid, d)['h'] > level:
            lo = mid
        else:
            hi = mid
    return I(lo, hi)


def u15(a, d, side, negative_lobe):
    m = Q(7, 16) * a**4 * d
    n = m * a
    aa = 1 - a if side == 'left' else a - 1
    dd = 1 - d if negative_lobe else d - 1
    return a**57 * d**70 * aa**15 * dd**15 / (
        (1 + m)**15 * (1 + n)**15)


def other_branch_boxes(hbox, target, source_N):
    specs = [
        ('left_positive', 'left', '1.0578177', '1.0578178', False, 1),
        ('right_negative_rising', 'right', '0.3787012', '0.3787014', True, 1),
        ('right_negative_falling', 'right', '0.9718356', '0.9718358', True, -1),
        ('right_positive', 'right', '1.0238258', '1.0238260', False, 1),
    ]
    result = {}
    for name, side, dslo, dshi, negative, direction in specs:
        dlo, dhi = Q(dslo), Q(dshi)
        # h_A<0 and h_d<0 give both monotone endpoint enclosures.
        al = I(root_a(hbox.hi, dlo, side).lo,
               root_a(hbox.lo, dlo, side).hi)
        ah = I(root_a(hbox.hi, dhi, side).lo,
               root_a(hbox.lo, dhi, side).hi)
        vl, vh = u15(al, I(dlo), side, negative), u15(ah, I(dhi), side, negative)
        if direction == 1:
            assert vl.hi < target.lo <= target.hi < vh.lo
        else:
            assert vh.hi < target.lo <= target.hi < vl.lo
        abox, dbox = I(ah.lo, al.hi), I(dlo, dhi)
        q = quantities(abox, dbox)
        assert not q['P'].lo <= 0 <= q['P'].hi
        gap = q['N'] - source_N
        assert gap.lo > Q(1, 1000)
        result[name] = {
            'A': abox.json(), 'd': dbox.json(),
            'u15_at_dlo': vl.json(), 'u15_at_dhi': vh.json(),
            'fold_numerator_P': q['P'].json(),
            'N': q['N'].json(), 'N_minus_source_N': gap.json(),
            'display_N': q['N'].display(), 'display_gap': gap.display(),
        }
    return result


def certificate():
    ac = Q('0.606768297615534074525671270774251123919356')
    dc = Q('0.817439750408149842744396827269022350625456')
    ra = rd = Q(1, 10**12)
    abox, dbox = I(ac - ra, ac + ra), I(dc - rd, dc + rd)
    assert 0 < abox.lo < abox.hi < 1
    assert Q(8, 11) < dbox.lo < dbox.hi < Q(20, 23)
    box = quantities(D(abox, 1, 0), D(dbox, 0, 1))
    center = quantities(D(ac, 1, 0), D(dc, 0, 1))

    P, K, h = box['P'], box['K'], box['h']
    assert P.dd.hi < -160 and K.da.hi < -18
    # The mean-value theorem on the convex box gives these exact face bounds.
    p_low = center['P'].v + P.da * I(-ra, ra) - rd * P.dd
    p_high = center['P'].v + P.da * I(-ra, ra) + rd * P.dd
    k_low = center['K'].v - ra * K.da + K.dd * I(-rd, rd)
    k_high = center['K'].v + ra * K.da + K.dd * I(-rd, rd)
    assert p_low.lo > 0 > p_high.hi
    assert k_low.lo > 0 > k_high.hi

    det = P.da * K.dd - P.dd * K.da
    dk_along_fold = K.da - K.dd * P.da / P.dd
    dh_along_fold = h.da - h.dd * P.da / P.dd
    dk_dh = dk_along_fold / dh_along_fold
    assert -2934 < det.lo < det.hi < -2933
    assert dk_along_fold.hi < -18
    assert dh_along_fold.hi < 0
    assert 2 < dk_dh.lo < dk_dh.hi < Q(21, 10)

    # These verify the closed derivative expressions against interval AD.
    assert (box['Na'].v - box['N'].da).lo <= 0 <= (
        box['Na'].v - box['N'].da).hi
    assert (box['Nd'].v - box['N'].dd).lo <= 0 <= (
        box['Nd'].v - box['N'].dd).hi

    intervals = {
        'A_box': abox, 'd_box': dbox, 'h_box': h.v, 'N_box': box['N'].v,
        'P_at_center': center['P'].v, 'K_at_center': center['K'].v,
        'P_A': P.da, 'P_d': P.dd, 'K_A': K.da, 'K_d': K.dd,
        'P_lower_d_face': p_low, 'P_upper_d_face': p_high,
        'K_lower_A_face': k_low, 'K_upper_A_face': k_high,
        'det_D_P_K': det, 'dK_dA_on_P_zero': dk_along_fold,
        'dh_dA_on_P_zero': dh_along_fold, 'dK_dh_on_P_zero': dk_dh,
    }
    target_u15 = u15(abox, dbox, 'left', True)
    others = other_branch_boxes(h.v, target_u15, box['N'].v)
    return {
        'arithmetic': 'Fraction; outward rounding to a denominator 10^100',
        'root_existence': 'P_d<0 plus opposite d-face signs gives d(A); '
                          'K has opposite A-face signs and decreases on P=0',
        'root_uniqueness_in_box': True,
        'intervals': {key: value.json() for key, value in intervals.items()},
        'display': {key: value.display() for key, value in intervals.items()},
        'fold_target_u15': target_u15.json(),
        'four_other_regular_branches': others,
        'other_N_gaps_lower_bound': '1/1000',
    }


if __name__ == '__main__':
    result = certificate()
    destination = Path(__file__).with_name('transverse_fold_certificate.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    for key in ['A_box', 'd_box', 'h_box', 'det_D_P_K', 'dK_dh_on_P_zero']:
        print(key, result['display'][key])
    for name, value in result['four_other_regular_branches'].items():
        print(name, value['display_N'], value['display_gap'])
