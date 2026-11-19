"""Exact first-hit checks. Optional --source /path/to/enterprise-math verifies the frozen six-axis rows."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


def states(k, radius):
    depth = max(0, radius - k - 2)
    return [(d, a) for a in range(depth + 1) for d in range(1 - radius, radius)
            if max(0, d - k - 1) <= a <= min(depth, (radius + d - 1) // 2)]


def directions(k, radius, d, a):
    """Next predictor and surviving numerator out of 2 given the named direction."""
    up = ((d + 1, max(a, d - k, 0)), 2) if d + 1 < radius else (None, 0)
    if d - 1 == -radius:
        return up, (None, 0)
    next_a = min(a, (radius + d - 2) // 2)
    return up, ((d - 1, next_a), 2 if next_a == a else 1)


def chain(k, radius):
    ss = states(k, radius)
    index = {s: i for i, s in enumerate(ss)}
    rows, hits = [], []
    for d, a in ss:
        row = [(index[target], weight) for target, weight in directions(k, radius, d, a)
               if target is not None]
        rows.append(row)
        hits.append(4 - sum(w for j, w in row))
    return ss, rows, hits


def apply(rows, v):
    return [sum(w * v[j] for j, w in row) for row in rows]


def prefixes(k, radius, steps):
    ss, rows, v = chain(k, radius)
    start = ss.index((0, 0))
    result = []
    for t in range(1, steps + 1):
        result.append(v[start])
        v = apply(rows, v)
    return result


def shell_tests(k, radius):
    """Test every named edge on the exact uniform coset; use actual marked U/T/V numerators."""
    D = max(0, radius - k - 2)
    modulus = 1 << D
    checked = 0
    for d, a in states(k, radius):
        for sign, (target, surviving) in zip((1, -1), directions(k, radius, d, a)):
            observed = Counter()
            for x in range(0, modulus, 1 << (D - a)):
                if sign == -1:
                    dest = [(x, 2)]
                elif d == radius - 1:
                    dest = []
                else:
                    dest = [(x, 1), ((x + (1 << (k + D - d))) % modulus, 1)]
                for y, w in dest:
                    e = D - (y & -y).bit_length() + 1 if y else 0
                    h = d + sign
                    if max(h, 2 * e - h) < radius:
                        observed[y] += w
            assert sum(observed.values()) == surviving * (1 << a)
            if target is not None:
                h, b = target
                assert set(observed) == set(range(0, modulus, 1 << (D - b)))
                assert len(set(observed.values())) == 1
            else:
                assert not observed
            checked += 1
    return checked


def direct_word_law(k, radius, steps):
    """Direct products of the original two by two diagonal/shear blocks, with pruning only at hit/stop."""
    data = {(1, 0, 1): 1}
    result = []
    for t in range(1, steps + 1):
        nxt = Counter()
        hit = 0
        for (a, b, c), mass in data.items():
            for A, B, C, w in ((2*a, 2*b, c, 1), (2*a, 2*b + (2 << k)*c, c, 1),
                               (a, b, 2*c, 2)):
                # All determinants are 2**t. The smaller Smith valuation is v2(gcd(entries)).
                lowbit = min(v & -v for v in (A, B, C) if v)
                if t - 2 * (lowbit.bit_length() - 1) >= radius:
                    hit += w * mass
                else:
                    nxt[A, B, C] += w * mass
        result.append(hit)
        data = nxt
    return result


def charpoly(rows):
    # Newton identities applied to traces of powers of the actual integer matrix 8P.
    n = len(rows)
    powers = [[int(i == j) for i in range(n)] for j in range(n)]
    coeff, traces = [1], []
    for r in range(1, n + 1):
        powers = [apply(rows, col) for col in powers]
        traces.append(sum(col[i] for i, col in enumerate(powers)))
        z = -sum(coeff[r-i] * traces[i-1] for i in range(1, r + 1))
        assert z % r == 0
        coeff.append(z // r)
    return coeff


def transfer_check(rows):
    # For w=z/8, det(I-w*8P) times F(z)/w has degree at most dim(P)-1.
    den = charpoly(rows)
    while den[-1] == 0:
        den.pop()
    seq = prefixes(1, 4, len(rows))
    num = [sum(den[j] * seq[t-j] for j in range(min(t+1, len(den))))
           for t in range(len(rows))]
    while num[-1] == 0:
        num.pop()
    assert num == [0,0,0,32,0,-640,0,3712,0,-5632]
    assert den == [1,0,-36,0,464,0,-2560,0,5632,0,-3584]
    # Coprime modulo 3, with leading terms retained. Hence coprime over Q.
    x, y = [a%3 for a in num], [a%3 for a in den]
    while y:
        while len(x) >= len(y):
            degree = len(x)-len(y)
            c = x[-1] * pow(y[-1], -1, 3)
            for j,b in enumerate(y):
                x[degree+j] = (x[degree+j]-c*b)%3
            while x and x[-1] == 0:
                x.pop()
        x,y = y,x
    assert len(x) == 1
    return {"numerator_F_over_w_ascending":num,"denominator_ascending":den,
            "coprimality_modulus":3}

def perron_box(rows):
    v = [1] * len(rows)
    for _ in range(500):
        w = apply(rows, v)
        v = [x + y for x, y in zip(v, w)]  # I + 8P is primitive.
    ratios = [F(x, 8*y) for x, y in zip(apply(rows, v), v)]
    scale = 10**10
    lo = int(min(ratios) * scale)
    hi = -int((-max(ratios) * scale) // 1)
    assert hi - lo <= 2
    return [lo, hi, scale]


def native_verify(repo, cases, steps):
    path = repo / 'src' / 'enterprise_math'
    receipt = repo / 'research_notes/heartbeat_weighted_lift_20260927_AD0416/RESULTS.json'
    digests = json.loads(receipt.read_text())['frozen_brc_sources']
    for name, digest in digests.items():
        assert sha256((path/name).read_bytes()).hexdigest() == digest
    sys.path.insert(0, str(path.parent))
    from enterprise_math.brc_control_port import ControlPacket
    from enterprise_math.brc_transport import Affine, eye, matrix, mm
    from enterprise_math.heartbeat_carry_peak import compile_carry_peak, first_passage_prefix
    def repeat(block):
        return matrix([[block[i%2][j%2] if i//2 == j//2 else 0 for j in range(6)] for i in range(6)])
    U, V = repeat(((2,0),(0,1))), repeat(((1,0),(0,2)))
    I = Affine(eye(6), (0,)*6)
    for k, radius in cases:
        E = repeat(((1,1 << k),(0,1)))
        for split in (False, True):
            labels = ((U,1), (mm(U,E),1), (V,2)) if split else ((U,2),(V,2))
            packet = ControlPacket.from_edges(2, 0, 1, [(0,0,F(w,8),Affine(g,(0,)*6),1)
                for g,w in labels]+[(0,1,F(1,2),I,1),(1,1,1,I,1)])
            aut = compile_carry_peak(packet, 2, radius, max_states=2048)
            assert aut.complete
            out = first_passage_prefix(packet, aut, steps)
            assert not out['unknown_mass']
            numerators = prefixes(k if split else radius, radius, steps)
            assert list(out['hit_by_step']) == [F(0)]+[F(y,8**t) for t,y in enumerate(numerators,1)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path)
    args = parser.parse_args()
    edges = total = 0
    for k in range(1, 13):
        for radius in range(1, k+10):
            D = max(0, radius-k-2)
            ss = states(k, radius)
            assert len(ss) == (D+1)*(2*radius-1-D) - D*(D+1)//2
            edges += shell_tests(k, radius)
            total += 1
    samples = [(1,2),(1,3),(1,4),(1,5),(2,5),(2,7),(3,7)]
    for k, radius in samples:
        assert direct_word_law(k, radius, 15) == prefixes(k, radius, 15)
    n = 30
    ss, rows, hit = chain(1,4)
    bs, baseline, b_hit = chain(4,4)
    base_index = [bs.index((d,0)) for d,a in ss]
    diffs = {}
    for t in range(1,n+1):
        i = ss.index((0,0))
        diff = hit[i] - b_hit[base_index[i]]
        if t%2 == 0:
            diffs[str(t)] = diff
        expected = 0 if t%2 or t<8 else 1 if t<=24 else -1
        assert (diff>0) - (diff<0) == expected
        if t == n:
            slack = [b_hit[j]-v for j,v in zip(base_index, hit)]
            assert all((z>0 if (d+n)%2==0 else z==0) for z,(d,a) in zip(slack,ss))
        else:
            hit = apply(rows, hit)
            b_hit = apply(baseline, b_hit)
    checks = [(1,2),(1,3),(1,4),(1,5),(2,5),(2,6)]
    if args.source:
        native_verify(args.source, checks, n)
    print(json.dumps({
        "shell_parameter_pairs":total,"marked_direction_rows":edges,
        "direct_integer_word_cases":samples,"direct_integer_word_steps":15,
        "source_crosscheck_cases_when_enabled":checks,
        "source_steps_when_enabled":n,"source_variants_per_case":2,
        "k1_R4":{"state_order_d_a":ss,"delta_times_8_power_t":diffs,
                 "baseline_minus_split_times_8_power_30":slack,"charpoly_8P_descending":charpoly(rows),
                 "transfer_w_equals_z_over_8":transfer_check(rows),
                 "Perron_interval_over_common_denominator":perron_box(rows),
                 "baseline_Perron_interval_over_common_denominator":perron_box(baseline)}
    },sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
