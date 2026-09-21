#!/usr/bin/env python3
"""R12 exact outside-carrier counter certificate.

Scope: finite complex arrays and routing only. This does not certify spectralDNS,
Navier-Stokes, or any PDE statement.

Invariant for fixed carrier C:
    q(x) = #{i notin C : x[i] != 0}.
If q is initialized exactly and every mutation is mediated, the update
    q <- q + 1[new != 0] - 1[old != 0]     (i notin C)
preserves the invariant. Hence q == 0 iff support(x) is a subset of C.
"""
from dataclasses import dataclass
import itertools, json, platform, statistics, sys, time
import numpy as np
from numba import njit


@dataclass
class ExactOutsideCounter:
    values: np.ndarray
    carrier: np.ndarray
    outside_nonzero: int

    @classmethod
    def make(cls, values, carrier):
        values = np.asarray(values, dtype=np.complex128).copy()
        carrier = np.asarray(carrier, dtype=bool).copy()
        if values.ndim != 1 or carrier.shape != values.shape:
            raise ValueError("shape mismatch")
        return cls(values, carrier, int(np.count_nonzero(values[~carrier])))

    def write(self, i, z):
        i, z = int(i), np.complex128(z)
        old = self.values[i]
        if not self.carrier[i]:
            self.outside_nonzero += int(z != 0) - int(old != 0)
        self.values[i] = z

    def eligible(self):
        return self.outside_nonzero == 0

    def brute_q(self):
        return int(np.count_nonzero(self.values[~self.carrier]))

    def assert_exact(self):
        assert self.outside_nonzero == self.brute_q()
        assert self.eligible() == (self.brute_q() == 0)


def exhaustive():
    # state + Source; 30 possible actions; all traces of length 1..3.
    N = 5
    carrier = np.array([1, 1, 0, 0, 0], bool)
    actions = [(obj, i, z)
               for obj in (0, 1)
               for i in range(N)
               for z in (0+0j, 1+0j, -1+0j)]
    traces = checks = 0
    for L in (1, 2, 3):
        for trace in itertools.product(actions, repeat=L):
            state = ExactOutsideCounter.make(np.zeros(N, complex), carrier)
            source = ExactOutsideCounter.make(np.zeros(N, complex), carrier)
            for obj, i, z in trace:
                (state if obj == 0 else source).write(i, z)
                state.assert_exact(); source.assert_exact()
                brute = state.brute_q() == 0 and source.brute_q() == 0
                assert (state.eligible() and source.eligible()) == brute
                checks += 1
            traces += 1
    return {"traces": traces, "step_checks": checks, "passed": True}


def controls():
    carrier = np.array([1, 1, 0, 0], bool)
    x = ExactOutsideCounter.make(np.zeros(4, complex), carrier)
    x.write(2, 1e-300)
    tiny = x.outside_nonzero == 1 and not x.eligible()
    x.write(2, 0)
    reentry = x.outside_nonzero == 0 and x.eligible() and x.brute_q() == 0

    x = ExactOutsideCounter.make(np.zeros(4, complex), carrier)
    for z in (1, -1, 0):
        x.write(2, z)
    duplicate = x.outside_nonzero == 0 and x.brute_q() == 0

    x = ExactOutsideCounter.make(np.zeros(4, complex), carrier)
    raw = x.values
    raw[3] = 1
    raw_alias_false_accept = x.eligible() and x.brute_q() == 1

    assert tiny and reentry and duplicate and raw_alias_false_accept
    return {
        "tiny_1e-300_detected": tiny,
        "safe_reentry_after_exact_clear": reentry,
        "duplicate_sequential_writes_exact": duplicate,
        "raw_alias_negative_control_false_accepts": raw_alias_false_accept,
    }


@njit
def apply_counter(values, carrier, q, inds, zs):
    for j in range(inds.shape[0]):
        i, new = inds[j], zs[j]
        old = values[i]
        if not carrier[i]:
            oldnz = old.real != 0.0 or old.imag != 0.0
            newnz = new.real != 0.0 or new.imag != 0.0
            q += (1 if newnz else 0) - (1 if oldnz else 0)
        values[i] = new
    return q


@njit
def apply_plain(values, inds, zs):
    for j in range(inds.shape[0]):
        values[inds[j]] = zs[j]


@njit
def full_scan(values, carrier):
    anynz = False
    for i in range(values.shape[0]):
        if not carrier[i]:
            z = values[i]
            if z.real != 0.0 or z.imag != 0.0:
                anynz = True
    return not anynz


def benchmark(seed=20260921):
    v = np.zeros(10, complex); c = np.zeros(10, bool)
    inds = np.array([1, 2], np.int64); zs = np.array([1+0j, 0+0j])
    apply_counter(v, c, 0, inds, zs); apply_plain(v, inds, zs); full_scan(v, c)

    N, K = 405_504, 384
    carrier = np.zeros(N, bool); carrier[:K] = True
    pool = np.arange(K, N)
    rng = np.random.default_rng(seed)
    rows = {}
    for W in (2, 8, 32, 128, 512, 2048, 8192, 16384, 32768,
              65536, 131072, 262144, 404000):
        chosen = rng.choice(pool, size=W//2, replace=False)
        inds = np.repeat(chosen, 2).astype(np.int64)
        zs = np.empty(W, np.complex128)
        zs[0::2] = rng.standard_normal(W//2) + 1j*rng.standard_normal(W//2)
        zs[1::2] = 0
        inner = 1000 if W <= 2048 else 500 if W <= 16384 else 150 if W <= 65536 else 25
        groups = 7 if W <= 65536 else 5
        ct, st = [], []
        for _ in range(groups):
            vc = np.zeros(N, complex); q = 0
            t0 = time.perf_counter_ns()
            for _ in range(inner):
                q = apply_counter(vc, carrier, q, inds, zs)
                assert q == 0
            ct.append((time.perf_counter_ns()-t0)/inner)

            vp = np.zeros(N, complex)
            t0 = time.perf_counter_ns()
            for _ in range(inner):
                apply_plain(vp, inds, zs)
                assert full_scan(vp, carrier)
            st.append((time.perf_counter_ns()-t0)/inner)
            assert np.array_equal(vc, vp)

        mc, ms = statistics.median(ct)/1e6, statistics.median(st)/1e6
        rows[str(W)] = {
            "counter_total_median_ms": mc,
            "plain_writes_plus_full_scan_median_ms": ms,
            "scan_over_counter_ratio": ms/mc,
        }
    return {
        "N": N, "carrier_size": K, "seed": seed,
        "note": "warm Numba; compilation excluded; each batch sets then clears W/2 outside coordinates",
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps({
        "schema": "RS_CFD_R12_EXACT_OUTSIDE_COUNTER_V1",
        "scope": "finite-array routing certificate only",
        "precondition": "complete write mediation; raw mutable aliases forbidden/revoked",
        "exhaustive": exhaustive(),
        "controls": controls(),
        "benchmark": benchmark(),
        "environment": {
            "python": sys.version.split()[0],
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }, indent=2, sort_keys=True))
