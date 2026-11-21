"""PREFIX-978: exact two-residual source-port revival checker."""
from collections import Counter
import json

def masks(p):
    out = {}
    for i in range(p):
        for j in range(p):
            for sign in (+1, -1):
                c = (1 << i) - sign * (1 << j)
                P, M = out.get(c, (0, 0))
                out[c] = (P | (1 << j), M) if sign == 1 else (P, M | (1 << j))
    return out

def active(pair, x, p):
    P, M = pair
    return ((P & ~x) | (M & x)) & (((1 << p) - 1) & ~1)

def cross(u, v, p):
    P, M = u
    Q, R = v
    return ((P & R) | (M & Q)) & (((1 << p) - 1) & ~1)

def can_walk(pair_a, pair_b, x, p, length):
    states = {x}
    for t in range(length):
        pair = pair_a if t % 2 == 0 else pair_b
        new = set()
        for state in states:
            bits = active(pair, state, p)
            while bits:
                bit = bits & -bits
                bits -= bit
                new.add(state ^ bit)
        states = new
        if not states:
            break
    return bool(states)

def verify_witness(a, b, p, j, rounds=25):
    bit = 1 << j
    P, M = a
    Q, R = b
    if P & R & bit:
        x = 1
    else:
        assert M & Q & bit
        x = 1 | bit
    initial = x
    for t in range(2 * rounds):
        pair = a if t % 2 == 0 else b
        assert active(pair, x, p) & bit
        x ^= bit
    assert x == initial
    return initial

def analyze(p, exhaustive=False):
    d = masks(p)
    A = ((1 << p) - 1) & ~1
    nonpersistent = [(c, m) for c, m in sorted(d.items()) if not (m[0] & m[1] & A)]
    hist = Counter()
    no_cross_state_checks = 0
    max_nonzero_support = 0
    labelled_loops = 0
    for c, u in nonpersistent:
        for C, v in nonpersistent:
            mask = cross(u, v, p)
            n = mask.bit_count()
            hist[n] += 1
            if n:
                while mask:
                    bit = mask & -mask
                    mask -= bit
                    verify_witness(u, v, p, bit.bit_length()-1)
                    labelled_loops += 1
            else:
                if c and C:
                    support = ((u[0]|u[1]|v[0]|v[1]) & A).bit_count()
                    assert support <= 4
                    max_nonzero_support = max(max_nonzero_support, support)
                if exhaustive:
                    for x in range(1, 1 << p, 2):
                        assert not can_walk(u, v, x, p, p), (p,c,C,x)
                        no_cross_state_checks += 1
    assert sum(hist.values()) == len(nonpersistent)**2
    return dict(p=p, residuals=len(d), individual_nonpersistent=len(nonpersistent),
                ordered_nonpersistent_pairs=len(nonpersistent)**2,
                ordered_reviving_pairs=sum(v for k,v in hist.items() if k>0),
                cross_port_histogram=dict(sorted(hist.items())),
                labelled_repeating_port_loops_checked=labelled_loops,
                full_no_cross_pairs_x_horizon_p_checks=no_cross_state_checks,
                nonzero_no_cross_max_port_support=max_nonzero_support)

def main():
    small = [analyze(p, p <= 6) for p in range(3,9)]
    big = analyze(19)
    assert big["residuals"] == 499
    assert big["individual_nonpersistent"] == 483
    assert big["ordered_reviving_pairs"] == 10960
    assert big["cross_port_histogram"] == {0:222329,1:10686,2:274}
    assert big["labelled_repeating_port_loops_checked"] == 11234
    assert big["nonzero_no_cross_max_port_support"] == 4
    big["two_step_cycle_state_port_witness_mass_all_odd_inputs"] = 11234 * (1<<17)
    for p in (3,4,8,19):
        d = masks(p)
        assert cross(d[0],d[4],p) & 2
        assert not (d[0][0]&d[0][1]&~1)
        assert not (d[4][0]&d[4][1]&~1)
        assert verify_witness(d[0],d[4],p,1,100) == 1
    d = masks(19)
    assert cross(d[4],d[16],19)==0
    x = 11
    for c,j in [(4,1),(16,3),(4,2),(16,4)]:
        assert active(d[c],x,19) & (1<<j)
        x ^= 1<<j
    assert x == 21
    result = dict(schema="PREFIX978_R6_ALTERNATING_REVIVAL_EXACT_V1",
                  status="AUTHOR_PROOF_EXACT_INTEGER_CHECKED_NOT_REVIEWED",
                  frozen_science_pin="awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d",
                  full_small_domain=small,p19=big,
                  example={"residuals":[0,4],"port":1,"states":[1,3],"infinite":True},
                  sharp_finite_example={"residuals":[4,16],"start":11,"ports":[1,3,2,4],"end":21},
                  review="NOT_REVIEWED",native_x6_bridge="NOT_ESTABLISHED")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result
if __name__=="__main__":
    main()
