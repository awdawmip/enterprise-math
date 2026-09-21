from collections import Counter
from math import gcd
from types import SimpleNamespace
import random
import pytest
from enterprise_math.group_ring_terminal_response import (
    terminal_responses, suffix_responses, cyclic_terminal_value,
    terminal_class_count, invert_collision_mass, collision_order_search,
)
from enterprise_math.group_ring_inverse_quotient import inverse_collision_mass
from enterprise_math.brc_control_mass import ControlMassQuotient


def triangular_direct(n, b, length, u):
    return sum(length-abs(d) for d in range(1-length, length)
               if u*pow(b, d, n) % n == 1)


def actual_order(n, b):
    r, z = 1, b
    while z != 1:
        z = z*b % n; r += 1
    return r


def forward(n, b, bits, initial=None):
    out = {1: 1} if initial is None else dict(initial)
    for _ in range(bits):
        nxt = Counter(); bi = pow(b, -1, n)
        for u, w in out.items():
            nxt[u] += 2*w; nxt[u*b % n] += w; nxt[u*bi % n] += w
        out = dict(nxt); b = b*b % n
    return out


@pytest.mark.parametrize('length', [1, 2, 3, 4, 5, 8, 13, 16, 31, 32, 65])
def test_triangular_mass_arbitrary_residues(length):
    for n, b in [(7, 3), (15, 4), (21, 2), (11, 3), (17, 3)]:
        states = tuple(range(n))
        result = terminal_responses(n, b, length, states)
        assert result.status == 'COMPLETE'
        assert result.values == tuple(triangular_direct(n, b, length, u) for u in states)


def test_repeated_baby_residues_and_tail():
    # order 2, width 7: several offsets share each residue; tail has its own moments.
    r = terminal_responses(15, 4, 16, (1, 4), baby_width=7)
    assert r.values == (128, 128)
    assert r.table_entries == 4
    assert terminal_responses(15, 4, 17, (1, 4), baby_width=7).values == (145, 144)


def test_all_block_widths():
    for length in range(1, 35):
        want = tuple(triangular_direct(21, 2, length, u) for u in range(21))
        for width in range(1, length+1):
            assert terminal_responses(21, 2, length, range(21), baby_width=width).values == want


def test_suffix_contracts_with_arbitrary_prefix_masses():
    rng = random.Random(20260921)
    for _ in range(150):
        n = rng.choice([7, 11, 15, 17, 21, 31])
        a = rng.choice([u for u in range(1, n) if gcd(u,n)==1])
        bits = rng.randrange(8); cut = rng.randrange(bits+1)
        prefix = forward(n, a, cut, {u:rng.randrange(5) for u in range(n)})
        response = suffix_responses(n, a, bits, cut, prefix.keys())
        got = sum(w*v for w,v in zip(prefix.values(), response.values))
        want = forward(n, pow(a, 1 << cut, n), bits-cut, prefix).get(1,0)
        assert got == want


def test_terminal_classes_formula():
    for order in range(1, 61):
        for length in range(1, 81):
            values = [cyclic_terminal_value(order, length, j) for j in range(order)]
            assert len(set(values)) == terminal_class_count(order, length)
            assert sum(values) == length*length


def test_known_order_formula_matches_unknown_order_matcher():
    for n,b in [(7,3),(11,3),(15,2),(35,2),(65,2)]:
        order=actual_order(n,b)
        for length in range(1,40):
            states=tuple(pow(b,j,n) for j in range(order))
            assert terminal_responses(n,b,length,states).values == tuple(
                cyclic_terminal_value(order,length,j) for j in range(order))


def test_terminal_classes_not_stepwise_lumpable():
    # order 5, L=4: terminal readout [4,3,3,3,3].  Nonidentity classes cannot
    # merge for another unrestricted T_b. Existing BRC checker rejects them.
    class Mass:
        def __init__(self,w): self.total_mass=w
        def forget_effects(self): return self
    blocks=[]
    for i in range(5):
        for j,w in ((i,2),((i+1)%5,1),((i-1)%5,1)):
            blocks.append((i,j,Mass(w)))
    with pytest.raises(ValueError, match='future safe'):
        ControlMassQuotient.compile(SimpleNamespace(state_count=5,blocks=blocks), (0,1,1,1,1))
    assert terminal_responses(11,3,4,tuple(pow(3,j,11) for j in range(5))).values == (4,3,3,3,3)


def test_small_mass_exact_inversion():
    assert invert_collision_mass(8,16)==4
    assert invert_collision_mass(4,4) is None
    assert collision_order_search(15,2).order==4
    for length in range(1,101):
        for order in range(1,length+3):
            mass=cyclic_terminal_value(order,length,0)
            got=invert_collision_mass(length,mass)
            assert got==(order if order<length else None)


def test_adaptive_matches_direct_orders_and_prior_kernel():
    for n in range(3,81):
        for a in [x for x in range(2,n) if gcd(x,n)==1][:3]:
            res=collision_order_search(n,a)
            order=actual_order(n,a)
            assert res.status=='COMPLETE' and res.order==order
            length,mass,*_=res.history[-1]
            assert order<length<=2*order
            old=inverse_collision_mass(n,a,length.bit_length()-1)
            assert old.status=='COMPLETE' and old.collision_mass==mass


def test_budget_never_returns_zero_or_fake_order():
    r=terminal_responses(101,2,1 << 80,max_baby_steps=10,max_scan_steps=100)
    assert r.status=='BUDGET_EXHAUSTED' and r.values is None and r.executed_scan_steps==0
    r=collision_order_search(101,2,max_scan_steps=5)
    assert r.status=='BUDGET_EXHAUSTED' and r.order is None and r.scans<=5
    r=collision_order_search(15,2,max_bits=2)
    assert r.status=='WINDOW_LIMIT' and r.order is None and r.order_lower_bound==4
    assert terminal_responses(15,1,1 << 100,(1,2),max_scan_steps=0).values==(1 << 200,0)


def test_input_sequence_and_nonunits():
    assert terminal_responses(15,4,16,(u for u in [4,1,4,0,3])).values==(128,128,128,0,0)
    assert terminal_responses(15,4,16,()).values==()


@pytest.mark.parametrize('args', [(True,2,4),(7,0,4),(7,7,4),(15,3,4),(7,3,0),(7,3,True)])
def test_bad_parameters(args):
    with pytest.raises(ValueError): terminal_responses(*args)


def test_bad_states_and_false_mass():
    with pytest.raises(ValueError): terminal_responses(7,3,4,[True])
    with pytest.raises(ValueError): terminal_responses(7,3,4,[7])
    with pytest.raises(ValueError): terminal_responses(7,3,4,baby_width=5)
    with pytest.raises(ValueError): suffix_responses(7,3,3,4)
    with pytest.raises(ValueError): suffix_responses(7,3,1_000_001,0)
    with pytest.raises(ValueError): invert_collision_mass(8,17)
    with pytest.raises(ValueError): invert_collision_mass(8,65)
