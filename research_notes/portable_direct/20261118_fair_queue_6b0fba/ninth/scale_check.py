"""Rational, state-controlled positive Weighted-BRC replay on the specified periodic rings."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
KERNEL_SHA = '4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f'
L = F(1, 2)

def means(u, s):
    assert len(u) % s == 0
    return tuple((sum(u[j:j + s], F()) / s for j in range(0, len(u), s)))

def change(u, v):
    return tuple((a - b for a, b in zip(u, v)))

def l1mean(u):
    return sum(map(abs, u), F()) / len(u)

def tv(u):
    return sum((abs(a - u[j - 1]) for j, a in enumerate(u)))

def coarse_flux(U, right, lam, s):
    return tuple((m - lam * (right[j] ** 2 - right[j - 1] ** 2) / (2 * s) for j, m in enumerate(U)))

def moments_profile(u):
    return tuple((tuple(sorted(u[j:j + 2])) for j in range(0, len(u), 2)))

class ControlledMass:

    def __init__(self, brc):
        self.b = brc
        self.work = Counter()

    def lift(self, a):
        return self.b.cwm_edge(a) if a else self.b.CWM_ZERO

    def part(self, src, w):
        if not src.live or not w:
            return self.b.CWM_ZERO
        self.work['positive_branch_propagations'] += 1
        return self.b.cwm_propagate(src, self.b.cwm_edge(w))

    def apply(self, state, lam):
        # Both branch weights use site totals from the previous instant.
        flow = tuple((lam * v.total / 2 for v in state))
        out = tuple((self.b.cwm_recoalesce(self.part(v, 1 - flow[j]), self.part(state[j - 1], flow[j - 1])) for j, v in enumerate(state)))
        a = tuple((v.total for v in state))
        z = tuple((v.total for v in out))
        assert z == tuple((x - lam * (x * x - a[j - 1] ** 2) / 2 for j, x in enumerate(a)))
        assert all((0 <= b <= 1 for b in z)) and sum(a) == sum(z)
        return out

    def trajectory(self, u, lam, T):
        state = tuple(map(self.lift, u))
        path = [u]
        for _ in range(T):
            state = self.apply(state, lam)
            path.append(tuple((v.total for v in state)))
        return path

    def suffix(self, U, s, tail, lam):
        out = [U]
        while tail[0]:
            right = tuple((v[-1] for v in tail))
            U = coarse_flux(U, right, lam, s)
            out.append(U)

            def pull(left, here):
                return self.b.cwm_recoalesce(self.part(self.lift(here), 1 - lam * here / 2), self.part(self.lift(left), lam * left / 2)).total
            tail = [tuple((pull(l, h) for l, h in zip(v, v[1:]))) for v in tail]
        return out

def classify(kern, n, alphabet):
    classes = defaultdict(lambda: [set(), set()])
    states = 0
    for u in product(alphabet, repeat=n):
        states += 1
        f = kern.trajectory(u, L, 2)
        U = means(u, 2)
        a, b = (means(f[1], 2), means(f[2], 2))
        assert a == coarse_flux(U, u[1::2], L, 2)
        pair = classes[moments_profile(u)]
        pair[0].add(a)
        pair[1].add((a, b))
    hist = Counter()
    for profile, (one, two) in classes.items():
        gaps = [hi ** 2 - lo ** 2 for lo, hi in profile]
        k = sum((g > 0 for g in gaps))
        invisible1 = k == n // 2 and len(set(gaps)) == 1
        invisible2 = k == n // 2 and len(set(profile)) == 1
        assert len(one) == 2 ** k - int(invisible1) and len(two) == 2 ** k - int(invisible2)
        hist['one_step_fibres'] += len(one)
        hist['two_step_fibres'] += len(two)
        U = tuple(((a + b) / 2 for a, b in profile))
        mid = tuple(((a * a + b * b) / 2 for a, b in profile))
        predictor = tuple((x - L * (mid[j] - mid[j - 1]) / 4 for j, x in enumerate(U)))
        radius = L * max((w + gaps[j - 1] for j, w in enumerate(gaps))) / 8
        assert max((max((abs(a - b) for a, b in zip(v, predictor))) for v in one)) == radius
    return dict(states=states, profiles=len(classes), **hist)

def pairs(kern):
    u = tuple(map(F, (1, 0, 0, 1)))
    v = tuple(map(F, (0, 1, 1, 0)))
    assert moments_profile(u) == moments_profile(v)
    assert means(kern.trajectory(u, L, 1)[1], 2) == (F(5, 8), F(3, 8))
    assert means(kern.trajectory(v, L, 1)[1], 2) == (F(3, 8), F(5, 8))
    u = (F(0), F(1, 2), F(3, 8), F(5, 8))
    v = (u[1], u[0], u[3], u[2])
    assert moments_profile(u) == moments_profile(v)
    rows = [list(map(lambda x: means(x, 2), kern.trajectory(x, L, 2))) for x in (u, v)]
    assert rows[0][:2] == rows[1][:2]
    assert change(rows[0][2], rows[1][2]) == (F(-1, 128), F(1, 128))
    return rows

def scale_tests(kern):
    rows = []
    s = 4
    n = 8
    for T in (1, 2, 3):
        u = tuple((F(i == s - T) for i in range(n)))
        v = tuple((F(i == s - T - 1) for i in range(n)))
        assert all((sorted(u[j:j + s]) == sorted(v[j:j + s]) and u[j + s - T + 1:j + s] == v[j + s - T + 1:j + s] for j in range(0, n, s)))
        paths = []
        for x in (u, v):
            expected = list(map(lambda w: means(w, s), kern.trajectory(x, L, T)))
            tail = [x[j + s - T:j + s] for j in range(0, n, s)]
            got = kern.suffix(means(x, s), s, tail, L)
            assert got == expected
            paths.append(got)
        assert paths[0][:-1] == paths[1][:-1]
        delta = (L / 2) ** (2 ** T - 1) / s
        assert change(paths[0][-1], paths[1][-1]) == (-delta, delta)
        rows.append(dict(T=T, delta=str(delta), paths=paths))
    x = tuple(map(F, ('1/3', '0', '1', '2/3', '1/5', '4/5', '1/2', '1/4')))
    path = kern.trajectory(x, L, 5)
    costs = []
    for s in (2, 4):
        base = kern.trajectory(means(x, s), L / s, 5)
        bound = F()
        for i, (u, w) in enumerate(zip(path, path[1:]), 1):
            cu = means(u, s)
            cw = means(w, s)
            assert cw == coarse_flux(cu, u[s - 1::s], L, s)
            fU = kern.trajectory(cu, L / s, 1)[1]
            eta = l1mean(change(cw, fU))
            bound += eta
            assert tv(w) <= tv(u) and l1mean(change(cw, base[i])) <= bound <= 2 * L * (s - 1) * i * tv(x) / (s * len(x))
            if s == 4:
                m2 = means(u, 2)
                a = kern.trajectory(m2, L / 2, 1)[1]
                D1 = change(means(w, 2), a)
                D2 = change(means(a, 2), fU)
                assert change(cw, fU) == tuple((a + b for a, b in zip(means(D1, 2), D2)))
        costs.append(dict(width=s, error=str(l1mean(change(means(path[-1], s), base[-1]))), summed_defect=str(bound)))
    return (rows, costs)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', required=True, type=Path)
    p.add_argument('--json', type=Path)
    args = p.parse_args()
    f = args.repo / 'src/enterprise_math/brc_weighted.py'
    assert sha256(f.read_bytes()).hexdigest() == KERNEL_SHA
    sys.path.insert(0, str(args.repo / 'src'))
    from enterprise_math import brc_weighted
    kern = ControlledMass(brc_weighted)
    four = pairs(kern)
    pulse, stability = scale_tests(kern)
    finite = [classify(kern, 4, tuple(map(F, ('0', '1/4', '3/8', '1/2', '5/8', '1')))), classify(kern, 8, tuple(map(F, ('0', '1/2', '1'))))]
    data = dict(brc_sha256=KERNEL_SHA, lambda_value=str(L), four_step_two=four, finite=finite, eight_point_pulses=pulse, five_step_stability=stability, work=dict(kern.work))
    out = json.dumps(data, default=str, ensure_ascii=True, separators=(',', ':')) + '\n'
    if args.json:
        args.json.write_text(out)
    print('exact finite tables', finite, 'pulse gaps', [r['delta'] for r in pulse], 'sha256', sha256(out.encode()).hexdigest())
if __name__ == '__main__':
    main()
