#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

class NaiveGenerationGuard:
    def __init__(self, n, carrier):
        self.x = np.zeros(n, dtype=np.complex128)
        self.carrier = frozenset(carrier)
        self.generation = 0
        self.certified_generation = 0
    def tracked_write(self, i, value):
        self.x[i] = value
        self.generation += 1
    def accepts_without_scan(self):
        return self.generation == self.certified_generation

class ExactBarrierGuard:
    def __init__(self, n, carrier):
        self.x = np.zeros(n, dtype=np.complex128)
        self.carrier = frozenset(carrier)
        self.escape_latched = False
        self.raw_view_exposed = False
        self.writes_checked = 0
    def write(self, i, value):
        self.writes_checked += 1
        self.x[i] = value
        if i not in self.carrier and value != 0:
            self.escape_latched = True
    def expose_raw_view(self):
        self.raw_view_exposed = True
        return self.x
    def accepts_without_scan(self):
        return (not self.raw_view_exposed) and (not self.escape_latched)
    def full_exact_recertify(self):
        outside = [i for i in range(self.x.size) if i not in self.carrier]
        escaped = bool(np.any(self.x[outside] != 0))
        self.escape_latched = escaped
        self.raw_view_exposed = False
        return not escaped

def run_certificate():
    n = 257
    carrier = set(range(31))
    j = 200
    naive = NaiveGenerationGuard(n, carrier)
    assert naive.accepts_without_scan()
    naive.x[j] = 1e-300 + 0j
    assert naive.generation == naive.certified_generation
    assert naive.accepts_without_scan()
    assert naive.x[j] != 0

    exact = ExactBarrierGuard(n, carrier)
    exact.write(j, 1e-300 + 0j)
    assert not exact.accepts_without_scan()
    assert exact.escape_latched

    zero = ExactBarrierGuard(n, carrier)
    zero.write(j, 0j)
    assert zero.accepts_without_scan()

    inside = ExactBarrierGuard(n, carrier)
    for i in range(31):
        inside.write(i, complex(i + 1, -i))
    assert inside.accepts_without_scan()
    assert inside.writes_checked == 31

    raw = ExactBarrierGuard(n, carrier)
    view = raw.expose_raw_view()
    assert not raw.accepts_without_scan()
    view[j] = 2 + 3j
    assert not raw.full_exact_recertify()
    assert raw.escape_latched

    latched = ExactBarrierGuard(n, carrier)
    latched.write(j, 1 + 0j)
    latched.write(j, 0j)
    assert latched.escape_latched
    assert not latched.accepts_without_scan()

    small_n = 8
    small_carrier = {0, 1, 2}
    values = [0j, 1+0j, -1+0j, 1j]
    checked_traces = 0
    for i in range(small_n):
        for v in values:
            g = ExactBarrierGuard(small_n, small_carrier)
            g.write(i, v)
            escaped = i not in small_carrier and v != 0
            assert g.accepts_without_scan() == (not escaped)
            checked_traces += 1
    for i in range(small_n):
        for v in values:
            for k in range(small_n):
                for w in values:
                    g = ExactBarrierGuard(small_n, small_carrier)
                    g.write(i, v)
                    g.write(k, w)
                    escaped = ((i not in small_carrier and v != 0) or
                               (k not in small_carrier and w != 0))
                    assert g.accepts_without_scan() == (not escaped)
                    checked_traces += 1

    return {
        "status": "PASS",
        "n_modes": n,
        "carrier_modes": len(carrier),
        "outside_modes": n - len(carrier),
        "naive_generation_counterexample": {
            "outside_index": j,
            "value": "1e-300+0j",
            "counter_unchanged": True,
            "false_accept": True
        },
        "exact_barrier_checks": {
            "tiny_nonzero_escape_caught": True,
            "exact_zero_outside_allowed": True,
            "inside_writes_without_full_scan": 31,
            "raw_view_revokes_certificate": True,
            "permanent_escape_latch": True,
            "exhaustive_traces_checked": checked_traces
        },
        "logical_result": "O(changed coefficients) exact support certification is possible only under a complete write-mediation contract; a generation counter that can be bypassed by raw mutable-array writes is not a sound certificate."
    }

if __name__ == "__main__":
    print(json.dumps(run_certificate(), indent=2, sort_keys=True))
