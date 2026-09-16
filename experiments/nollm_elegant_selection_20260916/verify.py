"""Independent integer checker for the 65,536-label elegant boundary experiment.
Run in EM: python experiments/nollm_elegant_selection_20260916/verify.py [outdir]
No source writes, network, Actions, floating geometry or prime-aware selection.
"""
from pathlib import Path
import csv
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'source_snapshot'))
sys.path.insert(0, str(ROOT.parents[1] / 'tools' / 'nollm_visual_toolkit'))
from nollm_visual_toolkit import core


def height(q, r):
    return max(abs(2*q+r), abs(q+2*r), abs(q-r))


def allowed(q, r, sign):
    pairs = ((2*q+r, r), (q+2*r, -q), (q-r, q+r))
    return all(abs(d) < 256 or abs(d) == 256 and sign*d*c < 0 for d, c in pairs)


def rotate(p):
    return (-p[1], p[0]+p[1])


def mirror(p):
    return (p[0]+p[1], -p[1])


def polygon(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    points = sorted(points)
    lo, hi = [], []
    for p in points:
        while len(lo) > 1 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in points[::-1]:
        while len(hi) > 1 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1]+hi[:-1]


def check(out):
    source = Path(core.__file__).read_bytes()
    assert hashlib.sha1(b'blob '+str(len(source)).encode()+b'\0'+source).hexdigest() == '7d7ee36b401e10469cb0a3c6a4a9fa33ba0f903e', 'Frozen core differs'
    data = core.demo_hex(65536)
    assert core.fingerprint(data) == '94df92927ff6952c86344ee2f38b428d273c7e749cb41343e25d5c2c5ae51160'
    inv = {(x['coord'][0] % 256, x['coord'][1] % 256): x['n'] for x in data['records']}
    assert len(inv) == 65536
    closed = {(q, r) for q in range(-256, 257) for r in range(-256, 257) if height(q, r) <= 256}
    families = {'strict': {p for p in closed if height(*p) < 256},
                'cw': {p for p in closed if allowed(*p, 1)},
                'ccw': {p for p in closed if allowed(*p, -1)}}
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    report = {'source_data_sha256': core.fingerprint(data), 'results': {}}
    for name, points in families.items():
        reps = {inv[(q % 256, r % 256)]: (q, r) for q, r in points}
        assert len(reps) == len(points)
        assert {rotate(p) for p in points} == points
        hull = polygon(points)
        area2 = abs(sum(q*b-r*a for (q, r), (a, b) in zip(hull, hull[1:]+hull[:1])))
        boundary = sum(math.gcd(abs(q-a), abs(r-b)) for (q, r), (a, b) in zip(hull, hull[1:]+hull[:1]))
        assert (area2+boundary+2)//2 == len(points)
        excluded = sorted(set(range(65536))-reps.keys())
        if name == 'strict':
            assert len(points) == 65281 and len(hull) == 6
            assert {mirror(p) for p in points} == points
        else:
            assert len(points) == 65533 and len(hull) == 18
            assert excluded == [16384, 32768, 49152]
            assert {mirror(p) for p in points} != points
        primes = [n for n in excluded if data['records'][n]['fields']['prime']]
        with (out / (name+'_excluded.csv')).open('w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(('n', 'is_prime', 'original_q', 'original_r'))
            for n in excluded:
                row = data['records'][n]
                writer.writerow((n, row['fields']['prime'], *row['coord']))
        report['results'][name] = {'kept': len(points), 'excluded': excluded,
                                  'excluded_primes': primes, 'hull_vertices': hull,
                                  'hull_sites': len(points), 'holes': 0}
    assert {mirror(p) for p in families['cw']} == families['ccw']
    assert len(report['results']['strict']['excluded_primes']) == 14
    shifted = sorted(inv[((q+1) % 256, (r+1) % 256)] for q, r in [(128, 0), (0, 128), (128, 128)])
    assert shifted == [16387, 32771, 49155]
    report['shifted_origin_n3_excluded'] = shifted
    report['shifted_origin_n3_excluded_primes'] = [n for n in shifted if data['records'][n]['fields']['prime']]
    assert report['shifted_origin_n3_excluded_primes'] == [32771]
    (out / 'independent_result.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('PASS: 65281/255 strict; 65533/3 chiral C6; no holes; 14 strict excluded primes; shifted-origin control')
    return report


if __name__ == '__main__':
    check(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'verified')
