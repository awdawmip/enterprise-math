#!/usr/bin/env python3
"""Exact interval Green reconstruction of eleven previously saved road anchors."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(a, c):
    vals = a[0] * c, a[1] * c
    return min(vals), max(vals)


def sub(a, b):
    return add(a, scale(b, -1))


def pos(a):
    return max(a[0], 0), max(a[1], 0)


def decimal_bound(x, upper=False, digits=32):
    z = x * 10**digits
    n = -((-z.numerator) // z.denominator) if upper else z.numerator // z.denominator
    sign = '-' if n < 0 else ''
    s = str(abs(n)).zfill(digits + 1)
    return sign + s[:-digits] + '.' + s[-digits:]


def record(v):
    return {'lower': decimal_bound(v[0]), 'upper': decimal_bound(v[1], True),
            'exact_bounds': list(map(str, v))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prior', type=Path, required=True)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('saved_anchor_certificate.json'))
    args = parser.parse_args()
    sample_path = args.prior / 'prior/riemann_cumulative_haar_20261123/inputs/rh_partial_frontier_20261122/sparse_sample_observations.json'
    source = json.loads(sample_path.read_text())
    q = {r['n']: tuple(F(int(v), 10**r['value']['denominator_power_of_10'])
                      for v in r['value']['integer_bounds']) for r in source['samples']}
    knots = [1024, 1536, 2048, 3072, 4096, 6144, 8192, 12288, 16384, 24576, 32768]
    assert all(a in q for a in knots)
    moments = []
    for i in range(1, len(knots) - 1):
        l, x, r = knots[i - 1:i + 2]
        assert r == 2*l
        t = sub(scale(sub(q[x], q[l]), F(1, x-l)), scale(sub(q[r], q[x]), F(1, r-x)))
        moments.append({'L': l, 'x': x, 'R': r, 'kind': 'within_block' if i % 2 else 'seam',
                        't': t})
    left, right = knots[0], knots[-1]
    rows = []
    for x in knots:
        chord = add(scale(q[left], F(right-x, right-left)), scale(q[right], F(x-left, right-left)))
        recon, upper, lower = chord, chord, chord
        for row in moments:
            z, t = row['x'], row['t']
            green = F((min(x,z)-left)*(right-max(x,z)), right-left)
            recon = add(recon, scale(t, green))
            upper = add(upper, scale(pos(t), green))
            lower = sub(lower, scale(pos(scale(t, -1)), green))
        assert recon[0] <= q[x][0] <= q[x][1] <= recon[1]
        assert lower[0] <= q[x][0] <= q[x][1] <= upper[1]
        rows.append({'x': x, 'actual': record(q[x]), 'boundary_chord': record(chord),
                     'signed_green_reconstruction': record(recon),
                     'positive_moment_upper': record(upper), 'negative_moment_lower': record(lower)})
    # A scoped information witness: affine inside every dyadic block, free anchors.
    values = {1024: F(0), 2048: F(1), 4096: F(0), 8192: F(0), 16384: F(0), 32768: F(0)}
    def witness(x):
        for a,b in zip(sorted(values), sorted(values)[1:]):
            if a <= x <= b:
                return (F(b-x)*values[a]+F(x-a)*values[b])/(b-a)
        raise ValueError(x)
    geometry_path = args.prior / 'directed_arithmetic/fixed_triangle_geometry.json'
    geometry = json.loads(geometry_path.read_text())
    old_count = 0
    for block in geometry['blocks']:
        for level in block['levels']:
            for p in level['packets']:
                l,x,r = p['L'],p['x'],p['R']
                assert (witness(x)-witness(l))/(x-l) == (witness(r)-witness(x))/(r-x)
                old_count += 1
    seam_witness = []
    for row in moments:
        l,x,r = row['L'],row['x'],row['R']
        t = (witness(x)-witness(l))/(x-l)-(witness(r)-witness(x))/(r-x)
        seam_witness.append({'L':l,'x':x,'R':r,'t':str(t)})
    assert any(F(r['t']) for r in seam_witness)
    result = {'schema':'RH_SAVED_ANCHOR_GREEN_V1','status':'PASS',
              'scope':'Finite author certificate on saved actual road; generic witness is an observation-sufficiency example, not a counterexample to the actual arithmetic estimate.',
              'old_sample_count':len(q),'used_anchor_count':len(knots),'new_q_queries':0,
              'within_block_moments':5,'seam_moments':4,'all_input_intervals_contained':True,
              'input_files':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [sample_path,geometry_path]],
              'moments':[{**{k:v for k,v in row.items() if k != 't'},'t':record(row['t'])} for row in moments],
              'anchors':rows,'generic_witness':{'all_old_moments_zero':old_count,'nonzero_anchor':2048,'new_moments':seam_witness}}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','used_anchor_count','new_q_queries','within_block_moments','seam_moments']}))


if __name__ == '__main__':
    main()
