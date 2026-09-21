"""R13 exact sparse re-entry epoch certificate.

Finite reference model only. It proves/test-checks the routing contract; it is
not a spectralDNS implementation or a performance claim.
"""
from itertools import product
import json

N = 4
CARRIER = frozenset((0, 1))
VALUES = (0, 1, -1)


def outside_nonzero_count(a):
    return sum(1 for i, v in enumerate(a) if i not in CARRIER and v != 0)


def cache_reference(u, source):
    # Representative exact sparse-derived cache. Keeping the carrier values
    # themselves makes equality a semantic exactness check rather than a hash.
    ids = sorted(CARRIER)
    return tuple(u[i] for i in ids) + tuple(source[i] for i in ids)


class EpochGuard:
    """Exact certificate under complete mediated writes and atomic route/use."""

    def __init__(self):
        self.u = [0] * N
        self.source = [0] * N
        self.q_u = 0
        self.q_source = 0
        self.epoch = 0
        self.cache = None
        self.cache_epoch = None
        self.cache_valid = False
        self.mode = "dense"

    def write(self, field, i, new):
        arr = self.u if field == "u" else self.source
        old = arr[i]
        if i not in CARRIER:
            q_name = "q_u" if field == "u" else "q_source"
            q = getattr(self, q_name)
            q += int(new != 0) - int(old != 0)
            setattr(self, q_name, q)
        if new != old:
            self.epoch += 1
            self.cache_valid = False
        arr[i] = new

    def route_boundary(self):
        if self.q_u == 0 and self.q_source == 0:
            # Rebuild from current authoritative arrays at the synchronization
            # boundary and stamp with the same mutation epoch.
            self.cache = cache_reference(self.u, self.source)
            self.cache_epoch = self.epoch
            self.cache_valid = True
            self.mode = "sparse"
        else:
            self.cache_valid = False
            self.mode = "dense"
        return self.mode

    def exact_sparse_certificate(self):
        return (
            self.q_u == outside_nonzero_count(self.u)
            and self.q_source == outside_nonzero_count(self.source)
            and self.q_u == 0
            and self.q_source == 0
            and self.cache_valid
            and self.cache_epoch == self.epoch
            and self.cache == cache_reference(self.u, self.source)
        )


def exhaustive():
    actions = [
        (field, i, value)
        for field in ("u", "source")
        for i in range(N)
        for value in VALUES
    ]
    traces = 0
    step_checks = 0
    for length in (1, 2, 3):
        for trace in product(actions, repeat=length):
            g = EpochGuard()
            for action in trace:
                g.write(*action)
                mode = g.route_boundary()
                assert g.q_u == outside_nonzero_count(g.u)
                assert g.q_source == outside_nonzero_count(g.source)
                if mode == "sparse":
                    assert g.exact_sparse_certificate()
                else:
                    assert g.q_u > 0 or g.q_source > 0
                    assert not g.cache_valid
                step_checks += 1
            traces += 1
    return traces, step_checks


def stale_cache_negative_control():
    g = EpochGuard()
    assert g.route_boundary() == "sparse"
    stale = g.cache

    # Dense escape, an inside-carrier semantic mutation, then exact support
    # re-entry. q returns to zero, but the pre-dense cache is stale.
    g.write("u", 2, 1)
    g.write("u", 0, 1)
    g.write("u", 2, 0)

    assert g.q_u == 0 and g.q_source == 0
    assert stale != cache_reference(g.u, g.source)
    support_only_false_accept = True

    # The epoch/rebuild protocol refuses stale use and safely rebuilds.
    assert not g.cache_valid
    assert g.route_boundary() == "sparse"
    assert g.exact_sparse_certificate()
    return support_only_false_accept


def raw_alias_negative_control():
    g = EpochGuard()
    assert g.route_boundary() == "sparse"
    # Simulate a raw mutable alias bypassing write(). Neither q nor epoch sees
    # this mutation, demonstrating why complete mediation is a hard premise.
    g.u[2] = 1
    false_accept = (
        g.q_u == 0
        and g.q_source == 0
        and g.cache_valid
        and g.cache_epoch == g.epoch
    )
    assert false_accept
    assert outside_nonzero_count(g.u) == 1
    return false_accept


def check_use_race_negative_control():
    g = EpochGuard()
    g.write("u", 0, 1)
    assert g.route_boundary() == "sparse"
    checked_epoch = g.cache_epoch
    # A mediated mutation after routing invalidates/stamps a new epoch. A caller
    # that caches only the route decision and then uses the old cache without an
    # atomic boundary or recheck can be wrong.
    g.write("u", 1, 1)
    assert g.epoch != checked_epoch
    unchecked_route_would_be_stale = g.cache != cache_reference(g.u, g.source)
    assert unchecked_route_would_be_stale
    assert not g.exact_sparse_certificate()
    assert g.route_boundary() == "sparse"
    assert g.exact_sparse_certificate()
    return True


def tiny_nonzero_control():
    g = EpochGuard()
    g.write("source", 3, 1e-300)
    assert g.q_source == 1
    assert g.route_boundary() == "dense"
    g.write("source", 3, 0.0)
    assert g.q_source == 0
    assert g.route_boundary() == "sparse"
    assert g.exact_sparse_certificate()
    return True


if __name__ == "__main__":
    traces, checks = exhaustive()
    result = {
        "finite_model": {
            "N": N,
            "carrier": sorted(CARRIER),
            "value_alphabet": list(VALUES),
            "trace_lengths": [1, 2, 3],
            "traces": traces,
            "per_step_checks": checks,
        },
        "stale_cache_support_only_false_accept": stale_cache_negative_control(),
        "raw_alias_false_accept_if_mediation_bypassed": raw_alias_negative_control(),
        "check_use_race_requires_atomic_boundary_or_epoch_recheck": check_use_race_negative_control(),
        "tiny_nonzero_1e-300_detected_exactly": tiny_nonzero_control(),
        "status": "PASS",
    }
    print(json.dumps(result, sort_keys=True, indent=2))
