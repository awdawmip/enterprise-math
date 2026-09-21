"""Exact tests. No remote access; original POWER reference is optional external input."""
import math
from itertools import product
from fractions import Fraction

import pytest
from enterprise_math.group_ring_inverse_quotient import (
    inverse_collision_mass, certify_inverse_partition, cyclic_return_signatures,
)


def full_steps(n, a, m):
    counts, g = {1: 1}, a
    masses, sizes = [1], [1]
    for _ in range(m):
        nxt = {}
        gi = pow(g, -1, n)
        for u, weight in counts.items():
            for v, factor in ((u, 2), (u*g % n, 1), (u*gi % n, 1)):
                nxt[v] = nxt.get(v, 0) + weight*factor
        counts, g = nxt, g*g % n
        masses.append(counts.get(1, 0))
        sizes.append(len(counts))
    return tuple(masses), tuple(sizes)


def multiplicative_order(n, a):
    x = a % n
    for r in range(1, n):
        if x == 1:
            return r
        x = x*a % n
    raise AssertionError('finite unit order not found')


@pytest.mark.parametrize('n,a', [(15, 2), (21, 2), (7, 3), (29, 16), (101, 2), (1009, 11)])
def test_all_prefix_masses_and_support(n, a):
    result = inverse_collision_mass(n, a)
    mass, support = full_steps(n, a, result.requested_m)
    r = multiplicative_order(n, a)
    assert result.status == 'COMPLETE'
    assert result.collision_by_depth == mass
    assert result.full_support_by_depth == support
    assert result.certified_order == r
    assert result.orbit_states_by_depth[-1] == r//2 + 1
    assert result.full_support_by_depth[-1] == r


def test_symmetric_state_collisions_direct_pairs():
    # Pair enumeration is an independent definition, not the group-ring recurrence.
    for n in range(3, 45):
        for a in range(2, min(n, 6)):
            if math.gcd(n, a) != 1:
                continue
            for m in range(6):
                hist = {}
                for x in range(1 << m):
                    u = pow(a, x, n)
                    hist[u] = hist.get(u, 0)+1
                assert inverse_collision_mass(n, a, m).collision_mass == sum(c*c for c in hist.values())


@pytest.mark.parametrize('n,a', [(7, 3), (15, 2), (29, 16)])
def test_unchanged_brc_mass_checker(n, a):
    r = multiplicative_order(n, a)
    units = tuple(pow(a, j, n) for j in range(r))
    for j in range(4):
        certificate = certify_inverse_partition(n, units, pow(a, 1 << j, n))
        assert len(certificate.quotient_mass_matrix) == r//2+1
        assert all(sum(row) == 4 for row in certificate.quotient_mass_matrix)


def test_biased_orientation_is_rejected_by_existing_checker():
    with pytest.raises(ValueError, match='not total-mass future safe'):
        certify_inverse_partition(7, (1, 3, 2, 6, 4, 5), 3,
                                  positive_weight=2, negative_weight=1)


def test_oriented_atom_cannot_use_inverse_partition():
    # Same inverse orbit: 3 and 5. Under the +3 atom: 2 and 1, distinct orbits.
    n, g, u, ui = 7, 3, 3, 5
    key = lambda x: min(x, pow(x, -1, n))
    assert key(u) == key(ui)
    assert key(u*g % n) != key(ui*g % n)


def test_total_and_identity_mass_are_not_a_future_state():
    # Both symmetric histograms have total 2 and identity coefficient 0.
    left, right = {3: 1, 5: 1}, {2: 1, 4: 1}
    identity_after = lambda h: 2*h.get(1, 0)+h.get(3, 0)+h.get(5, 0)
    assert sum(left.values()) == sum(right.values()) == 2
    assert left.get(1, 0) == right.get(1, 0) == 0
    assert identity_after(left) == 2 and identity_after(right) == 0


def test_minimal_partition_and_linear_rank_triangular_witness():
    for r in range(1, 101):
        rows = cyclic_return_signatures(r)
        d = r//2
        assert len(set(rows)) == d+1
        for i in range(r):
            assert rows[i] == rows[-i % r]
            assert next(j for j, value in enumerate(rows[i]) if value) == min(i, r-i)
        # Representatives i=0..d form a nonsingular triangular matrix in times 0..d.
        assert all(rows[i][j] == 0 for i in range(d+1) for j in range(i))
        assert all(rows[i][i] > 0 for i in range(d+1))


def test_budget_preserves_last_complete_prefix():
    out = inverse_collision_mass(101, 2, 8, max_states=2)
    assert out.status == 'BUDGET_EXHAUSTED'
    assert out.completed_m == 1 and out.requested_m == 8
    assert out.collision_mass == 2 and out.certified_order is None
    assert max(out.orbit_states_by_depth) <= 2


def test_small_window_does_not_falsely_certify_order():
    out = inverse_collision_mass(15, 2, 1)
    assert out.collision_mass == 2 and out.certified_order is None
    assert inverse_collision_mass(15, 2).certified_order == 4


@pytest.mark.parametrize('args,kwargs', [
    ((2, 1), {}), ((15, 3), {}), ((15, True), {}), ((7, 3, -1), {}),
    ((7, 3), {'max_states': 0}), ((7, 3, False), {}),
])
def test_invalid_inputs(args, kwargs):
    with pytest.raises(ValueError):
        inverse_collision_mass(*args, **kwargs)


def test_certificate_rejects_nonclosed_population():
    with pytest.raises(ValueError, match='closed'):
        certify_inverse_partition(7, (1, 3), 3)


def test_identity_tail_is_exact_without_frontier_rescaling():
    out = inverse_collision_mass(17, 3, 100)
    assert out.status == 'COMPLETE' and out.completed_m == 100
    assert out.certified_order == 16
    assert out.collision_mass == (1 << 200)//16
    assert out.attempted_row_updates == sum(out.orbit_states_by_depth[:4])
    assert out.orbit_states_by_depth[-1] == 9


def test_fixed_terminal_readout_can_be_coarser_than_repeat_language():
    n, a, counts, g = 5, 2, {1: 1}, 2
    for _ in range(2):
        nxt = {}
        for u, c in counts.items():
            for v, w in ((u, 2), (u*g % n, 1), (u*pow(g, -1, n) % n, 1)):
                nxt[v] = nxt.get(v, 0)+w*c
        counts, g = nxt, g*g % n
    # Q=r=4: terminal kernel is constant, despite three inverse orbits.
    assert set(counts.values()) == {4} and len(counts) == 4
    assert len(set(cyclic_return_signatures(4))) == 3
