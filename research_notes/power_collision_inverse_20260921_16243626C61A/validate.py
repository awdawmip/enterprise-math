"""Run with PYTHONPATH=src; pass the frozen POWER source path explicitly."""
import argparse
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform
import statistics
import sys
import time
import tracemalloc

from enterprise_math.group_ring_inverse_quotient import inverse_collision_mass


def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def load_reference(path):
    content = path.read_bytes()
    if git_blob(content) != '11d4adf3ff6e56c440cfdd7974be6c28f8ff068a':
        raise ValueError('POWER reference differs from the audited original')
    spec = importlib.util.spec_from_file_location('frozen_power_reference', path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod.compute_group_ring_collision_mass


def full_with_same_identity_tail(n, a):
    """Ablation: ordinary full support, with the same g==1 readout shortcut."""
    m = max(4, (n*n-1).bit_length())
    counts, g = {1: 1}, a
    k = None
    for depth in range(m):
        if g == 1:
            k = counts.get(1, 0) << (2*(m-depth))
            break
        nxt, gi = {}, pow(g, -1, n)
        for u, c in counts.items():
            nxt[u] = nxt.get(u, 0)+2*c
            v = u*g % n
            nxt[v] = nxt.get(v, 0)+c
            v = u*gi % n
            nxt[v] = nxt.get(v, 0)+c
        counts, g = nxt, g*g % n
    k = counts.get(1, 0) if k is None else k
    q = 1 << m
    return (2*q*q+k)//(2*k), k, len(counts)


def elapsed(fn):
    times = []
    for _ in range(3):
        gc.collect()
        start = time.perf_counter()
        fn()
        times.append(time.perf_counter()-start)
    return statistics.median(times)


def peak_bytes(fn):
    gc.collect()
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--power-source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    original = load_reference(args.power_source)
    cases = prefix_comparisons = 0
    for n in range(3, 201):
        bases = [a for a in range(2, n) if math.gcd(n, a) == 1][:3]
        for a in bases:
            ref_order, ref_k, ref_support = original(n, a)
            result = inverse_collision_mass(n, a)
            assert result.status == 'COMPLETE'
            assert (result.certified_order, result.collision_mass,
                    result.full_support_by_depth[-1]) == (ref_order, ref_k, ref_support)
            assert result.orbit_states_by_depth[-1] == ref_order//2+1
            assert full_with_same_identity_tail(n, a) == (ref_order, ref_k, ref_support)
            cases += 1
            for m in (0, 1, 2, 4, 6):
                _, k, support = original(n, a, m=m)
                out = inverse_collision_mass(n, a, m=m)
                assert out.collision_mass == k and out.full_support_by_depth[-1] == support
                prefix_comparisons += 1
    bench = []
    for n, a in [(1009, 11), (10007, 5), (65537, 3)]:
        ref = original(n, a)
        out = inverse_collision_mass(n, a)
        assert (out.certified_order, out.collision_mass) == ref[:2]
        f, q = lambda: original(n, a), lambda: inverse_collision_mass(n, a)
        ft, qt = elapsed(f), elapsed(q)
        fb, qb = peak_bytes(f), peak_bytes(q)
        ablation = lambda: full_with_same_identity_tail(n, a)
        assert ablation() == ref
        at, ab = elapsed(ablation), peak_bytes(ablation)
        bench.append(dict(n=n, a=a, m=out.requested_m, order=ref[0],
                          full_support=ref[2], inverse_orbits=out.orbit_states_by_depth[-1],
                          collision_mass=out.collision_mass,
                          full_seconds_median=ft, orbit_seconds_median=qt,
                          full_peak_traced_bytes=fb, orbit_peak_traced_bytes=qb,
                          runtime_ratio_orbit_over_full=qt/ft,
                          memory_ratio_orbit_over_full=qb/fb,
                          full_with_tail_seconds_median=at,
                          full_with_tail_peak_traced_bytes=ab,
                          runtime_ratio_orbit_over_tail_full=qt/at,
                          memory_ratio_orbit_over_tail_full=qb/ab))
    result = dict(python=sys.version, platform=platform.platform(),
                  reference_git_blob='11d4adf3ff6e56c440cfdd7974be6c28f8ff068a',
                  default_reference_comparisons=cases,
                  explicit_window_comparisons=prefix_comparisons,
                  benchmarks=bench,
                  limitations=['one host', '3 time samples per variant; median',
                               'tracemalloc measured separately from timings',
                               'traced Python allocations, not process RSS',
                               'no RSA-270 run', 'no full repository tests'])
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
