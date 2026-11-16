"""Recover two landings from exact data by solving the two centered equations."""
from fractions import Fraction as Q
import json

from blind_center_decoder import rising, simulate, blind
from check_three_state import native_observations


def recover_two(r, c, g, h):
    if r != 2:
        raise ValueError("this integer search is specialized to two blocks")
    small, large = blind(2, c, g, h)[0]
    center_odds = [x / (1 - x) for x in (small, large)]
    smaller, larger = center_odds
    # From A(1+b/(1+dW)), A(1+b/(1+DW)), d=1/2, D=5.
    width = larger - smaller
    e = (10 * smaller - larger) / 9
    initial = rising(c + 6, 15)
    solutions = []
    for v in range(2, c+1):
        a_inv = Q(28 * (4+4*v)*rising(v+5,15), (v+4)*initial)
        if e <= a_inv:
            continue
        W = 2 * width / (9*(e - a_inv))
        product = 840*W
        if product.denominator != 1:
            continue
        lo, hi = 2, v
        while lo < hi:
            mid = (lo+hi)//2
            if (mid+2)*(mid+3)*(mid+4) < product:
                lo = mid+1
            else:
                hi = mid
        w = lo
        if (w+2)*(w+3)*(w+4) != product:
            continue
        b = Q((w+2)*rising(v+4,9),28*(4*w+2)*rising(w+3,9))
        if a_inv*(1+b/(1+W/2)) == larger and a_inv*(1+b/(1+5*W)) == smaller:
            solutions.append((v,w))
    return solutions


if __name__ == "__main__":
    reports = []
    for gaps in [(450,505,470),(1250,1294,1352),(721,533,837),(925,800,680)]:
        c = sum(gaps)+2
        if c <= 1500:
            g,h,_ = native_observations(gaps)
        else:
            g,h = simulate(gaps)
        actual = (c-gaps[0], c-gaps[0]-gaps[1])
        identified = recover_two(2,c,g,h)
        assert identified == [actual]
        reports.append(dict(c=c, possible_center_templates=c*(c-1)//2,
                            recovered_landings=identified[0], gaps=gaps))
    print(json.dumps(reports,indent=2))
