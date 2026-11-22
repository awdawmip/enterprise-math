#!/usr/bin/env python3
"""R284ED: measured complete frozen-Port readout costs on CPython.

Uses the immutable R284CO scientific definitions through the already certified
R284DX / R284EA / R284DS implementation. Standard library only.
Run beside those three scripts and their published dependencies.
"""
from bisect import bisect_right
from itertools import product
from pathlib import Path
import gc, hashlib, json, platform, statistics, sys, time
from R284DX_six_bit_full_quotient_checker import P, FROZEN_SHA, Q_TABLE, det, arcs, dist, core_key
from R284EA_nine_bit_exception_threshold_checker import score, bits_of
from R284DS_fast_labeled_sweep_checker import build_heap_envelope, query_profile

SOURCE_COMMIT = 'acba2d8667903434aaa2a10720f43637fcc2421b'
SOURCE_BLOB = 'b46e0f682b58e47c27094b4bea6fa4e55119a3ee'
METHODS = ('direct64', 'div_env', 'table_env', 'shift_T_env', 'shift_bits_env')
PACKED = ('div_packed_env', 'table_packed_T_env', 'table_packed_bits_env', 'shift_packed_T_env')


def core_shift(L):
    u1, a, x, _, u2, w, b, *_ = L
    t, s = 6-a, 13-b
    u, p1, p2 = t*s-x*w, s*u1+x*u2, t*u2+w*u1
    return (13788*u-4799*p1-4854*p2+14) >> 7


def packed_score(i):
    return (13*((i>>3)&1)+6*((i>>7)&1)+28*((i>>8)&1)
            +25*((i>>9)&1)+11*((i>>10)&1)+12*((i>>11)&1)
            +26*((i>>12)&1)+17*((i>>13)&1)+6*((i>>14)&1))


def observed(z, A, times, profiles, direct):
    if direct:
        ds = [dist(z, arc) for arc in A]
        d = max(ds)
        labels = tuple(j for j, v in enumerate(ds) if v == d)
    else:
        d, labels = query_profile(z, profiles[bisect_right(times, z)-1], len(A))
    assert d > 0 and len(labels) == 1
    return d, labels[0]


def run_method(method, states, A, times, profiles, record=False):
    h = hashlib.sha256() if record else None
    obs = hashlib.sha256() if record else None
    for state in states:
        L, top = state[:2]
        T = det(L, top)
        if method in ('direct64', 'div_env', 'div_packed_env'):
            z = T % P
        elif 'packed' in method:
            i = state[2]
            key = (i & 7) | ((i >> 1) & 0x38)
            assert not record or key == core_key(L)
            if method == 'table_packed_bits_env':
                guard = key == 63 and packed_score(i) >= 77
                q = Q_TABLE[key]-int(guard)
            elif method == 'table_packed_T_env':
                q = Q_TABLE[key]-int(key == 63 and T < 2879*P)
            elif method == 'shift_packed_T_env':
                q = core_shift(L)-int(key == 63 and T < 2879*P)
            else:
                raise ValueError(method)
            z = T-q*P
        else:
            key = core_key(L)
            if method == 'table_env':
                q = Q_TABLE[key]-int(key == 63 and T < 2879*P)
            elif method == 'shift_T_env':
                q = core_shift(L)-int(key == 63 and T < 2879*P)
            elif method == 'shift_bits_env':
                q = core_shift(L)-int(key == 63 and score(bits_of(L, top)) >= 77)
            else:
                raise ValueError(method)
            z = T-q*P
        assert 0 <= z < P
        d, label = observed(z, A, times, profiles, method == 'direct64')
        if record:
            h.update(z.to_bytes(8,'big'))
            obs.update(z.to_bytes(8,'big') + bytes((label,)) + d.to_bytes(8,'big'))
    return (h.hexdigest(), obs.hexdigest()) if record else None


def repeated_benchmark(methods, states, A, times, profiles):
    times_ms = {m: [] for m in methods}
    for turn in range(5):
        for method in methods[turn:] + methods[:turn]:
            enabled = gc.isenabled()
            gc.disable()
            t0 = time.perf_counter_ns()
            run_method(method, states, A, times, profiles)
            elapsed = (time.perf_counter_ns()-t0)/1e6
            if enabled: gc.enable()
            times_ms[method].append(elapsed)
    return {k: {'runs_ms': v, 'median_ms': statistics.median(v),
                'minimum_ms': min(v)} for k,v in times_ms.items()}


def main():
    t0 = time.perf_counter_ns()
    states = [(L, sum((v-1)<<j for j,v in enumerate(upper)))
              for upper in product((1,2),repeat=4)
              for L in product((1,2),repeat=12)]
    input_ms = (time.perf_counter_ns()-t0)/1e6
    t0 = time.perf_counter_ns()
    A = arcs()
    arc_ms = (time.perf_counter_ns()-t0)/1e6
    t0 = time.perf_counter_ns()
    times, profiles, _ = build_heap_envelope(A)
    envelope_ms = (time.perf_counter_ns()-t0)/1e6
    assert len(states)==65536 and len(A)==64 and len(times)==194 and len(profiles)==193

    t0 = time.perf_counter_ns()
    packed = [(L,top,(top<<12) | sum((L[j]-1)<<j for j in range(12)))
              for L,top in states]
    packed_extra_ms = (time.perf_counter_ns()-t0)/1e6
    hashes = {m: run_method(m,states,A,times,profiles,True) for m in METHODS}
    hashes.update({m: run_method(m,packed,A,times,profiles,True) for m in PACKED})
    assert all(z[0] == FROZEN_SHA for z in hashes.values())
    assert len({z[1] for z in hashes.values()}) == 1
    assert next(iter(hashes.values()))[1] == '4d15e6ffb1fa38e92f105fa54e5b7c8061301fadcb761ebc4feeb1c57b2a1cc8'
    runs = repeated_benchmark(METHODS,states,A,times,profiles)
    packed_runs = repeated_benchmark(PACKED,packed,A,times,profiles)
    certificate = {
        'schema':'R284ED_FULL_FROZEN_PORT_PIPELINE_BENCHMARK_V1',
        'status':'AUTHOR_EXACT_CHECKED / EMPIRICAL_BENCHMARK / NOT_REVIEWED',
        'frozen_source_commit': SOURCE_COMMIT,
        'frozen_source_git_blob_sha1': SOURCE_BLOB,
        'frozen_codeword_sha256': FROZEN_SHA,
        'ordered_residue_label_distance_sha256': next(iter(hashes.values()))[1],
        'whole_universe_verified': 65536,
        'arcs':len(A),
        'event_positions':len(times),
        'preprocessing_single_samples_ms':{'source_tuple_population':input_ms,
               'arc_construction':arc_ms, 'R284DS_heap_envelope_construction':envelope_ms,
               'extra_index_materialization':packed_extra_ms},
        'full_pipeline_runs':runs,
        'packed_state_runs':packed_runs,
        'timing_protocol':'five warm sequential runs per method, method-order rotation, GC disabled during run; same prepared state data within each comparison',
        'scope':'determinant+quotient+64-arc distance/unique winner or determinant+quotient+precomputed 193-interval event envelope/unique winner; source and arc prep excluded from measured loops',
        'environment':{'python':sys.version.split()[0],
                       'implementation':platform.python_implementation(),
                       'platform':platform.platform(), 'machine':platform.machine()},
        'unreviewed':True,
    }
    output=Path(__file__).with_name('R284ED_full_pipeline_benchmark_certificate.json')
    output.write_text(json.dumps(certificate,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
    print(json.dumps({k:certificate[k] for k in ('whole_universe_verified',
           'ordered_residue_label_distance_sha256','full_pipeline_runs','packed_state_runs')},ensure_ascii=False,indent=2))
    return certificate

if __name__ == '__main__': main()
