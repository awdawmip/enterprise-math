#!/usr/bin/env python3
"""Exact conservative X6 network and precision audit; not a native physical law.

No floats, renormalization, amplitude cutoff, environment reset or remote I/O.
Each state stores integer amplitudes with the declared common denominator 3^t.
Quantum assumptions are explicit. The unchanged event-16 partial-trace/basis
helpers are executed for quantum witnesses, not reported as a new tool family.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import permutations, product
import json
from pathlib import Path
import random
import sys
import sympy as sp

D = 6
ZERO = (0,) * D
H = ((-1, 2, 2), (2, -1, 2), (2, 2, -1))
EVENT = 'NS-CONSERVATIVE-NETWORK-PRECISION-20260916-D5C00D-17'
HERE = Path(__file__).resolve().parent
PARENT_HASH = 'd7784336c350e5d3795c3c3163f55a1477752a264b842edc49af14cbdf0bddd1'
State = dict[tuple[tuple[int, ...], int], int]


def load_parent():
    path = HERE.parent / 'ns_dense_residual_d5c00d/check_dense_residual.py'
    if sha256(path.read_bytes()).hexdigest() != PARENT_HASH:
        raise ValueError('Changed parent: re-audit before reuse')
    spec = spec_from_file_location('event16_exact_reused', path)
    if spec is None or spec.loader is None:
        raise RuntimeError('Cannot load exact parent')
    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def shift(z, j, s, period=None):
    out = list(z)
    out[j] += s
    if period is not None:
        out[j] %= period
    return tuple(out)


def coin_numerators(state: State) -> State:
    cells = defaultdict(lambda: [0, 0, 0])
    for (z, k), v in state.items():
        if len(z) != D or k not in (0, 1, 2) or type(v) is not int:
            raise ValueError('Invalid signed-coordinate/integer amplitude state')
        cells[z][k] = v
    out = {}
    for z, v in cells.items():
        for k in range(3):
            a = sum(H[k][j] * v[j] for j in range(3))
            if a:
                out[(z, k)] = a
    return out


def step(state: State, axis: int, period=None) -> State:
    if axis not in range(D):
        raise ValueError('Expected a native axis index')
    out = {}
    for (z, k), v in coin_numerators(state).items():
        target = z if k == 0 else shift(z, axis, 1 if k == 1 else -1, period)
        key = (target, k)
        if key in out:
            raise AssertionError('Register streaming is not a permutation')
        out[key] = v
    return out


def inverse_step(state: State, axis: int) -> State:
    unshifted = {(z if k == 0 else shift(z, axis, -1 if k == 1 else 1), k): v
                 for (z, k), v in state.items()}
    raw = coin_numerators(unshifted)
    if any(v % 9 for v in raw.values()):
        raise AssertionError('Backward state did not have the certified denominator')
    return {key: v // 9 for key, v in raw.items() if v}


def density(state: State):
    out = defaultdict(int)
    for (z, _), a in state.items():
        out[z] += a*a
    return dict(out)


def dephased_step(population, axis):
    out = defaultdict(int)
    for (z, j), value in population.items():
        for k in range(3):
            target = z if k == 0 else shift(z, axis, 1 if k == 1 else -1)
            out[target, k] += H[k][j]**2 * value
    return {key: v for key, v in out.items() if v}


def local_balance(before, after, axis):
    prev = density(before)
    new = density(after)
    moved = coin_numerators(before)
    sites = set(prev) | set(new) | {z for z, _ in moved}
    for z in sites:
        flux = (moved.get((shift(z, axis, -1), 1), 0)**2
                - moved.get((z, 1), 0)**2
                + moved.get((shift(z, axis, 1), 2), 0)**2
                - moved.get((z, 2), 0)**2)
        assert new.get(z, 0) - 9*prev.get(z, 0) == flux
    return len(sites)


def act(state, perm, translation=ZERO):
    out = {}
    for (z, k), v in state.items():
        q = [0]*D
        for j in range(D):
            q[perm[j]] = z[j]
        out[(tuple(q[j]+translation[j] for j in range(D)), k)] = v
    return out


def history(frame, steps):
    state = {(ZERO, 0): 1}
    states = [state]
    for t in range(steps):
        state = step(state, frame[t % D])
        states.append(state)
    return states


def transport_permutation_test():
    # Two oppositely moving register tracks, not unpaired global translation.
    L = 7
    slots = tuple((z, k) for z in range(L) for k in (1, 2))
    local = {(z, k): (z, 3-k) for z, k in slots}
    edge = {}
    for z in range(L):
        a, b = (z, 2), ((z+1) % L, 1)
        edge[a], edge[b] = b, a
    final = {x: edge[local[x]] for x in slots}
    assert all(final[z, k] == ((z+(1 if k == 1 else -1)) % L, k)
               for z, k in slots)
    count = 0
    indices = {x: i for i, x in enumerate(slots)}
    for bits in range(1 << len(slots)):
        out = sum(((bits >> i) & 1) << indices[final[x]]
                  for i, x in enumerate(slots))
        assert out.bit_count() == bits.bit_count()
        count += 1
    return {'ring_cells': L, 'registers': len(slots), 'basis_states': count,
            'primitive_edge_swap_layer': True}


def quantum_tests(parent, source_probabilities):
    G = sp.Matrix(H)/3
    U = sp.eye(8)
    ids = (4, 2, 1)
    for i in range(3):
        for j in range(3):
            U[ids[i], ids[j]] = G[i, j]
    N = sp.diag(*[i.bit_count() for i in range(8)])
    assert U.H*U == sp.eye(8) and U*N == N*U
    # Explicit new extension, not the old gate reinterpreted on a dense state.
    flip = sp.zeros(8)
    for i in range(8):
        flip[7-i, i] = 1
    dense_gate = U*flip*U*flip
    assert dense_gate.H*dense_gate == sp.eye(8)
    assert dense_gate*N == N*dense_gate
    assert dense_gate*flip == flip*dense_gate
    assert dense_gate*parent.basis(8, 7) == parent.basis(8, 7)
    assert dense_gate*parent.basis(8, 0) == parent.basis(8, 0)
    assert dense_gate*parent.basis(8, 3) == flip*U*parent.basis(8, 4)
    assert U*parent.basis(8, 3) == parent.basis(8, 3)
    assert dense_gate*parent.basis(8, 4) == U*parent.basis(8, 4)
    psi = U*parent.basis(8, 4)
    rho = parent.ptrace(psi*psi.H, 3, (1, 2))
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    measurements = (X, Y, (3*X+4*Y)/5, (3*X-4*Y)/5)
    bell = (sp.kronecker_product(measurements[0], measurements[2]+measurements[3])
            + sp.kronecker_product(measurements[1], measurements[2]-measurements[3]))
    assert sp.trace(rho*bell) == sp.Rational(112, 45)

    # At the first propagation step the local code is vacuum plus three modes.
    # Basis = vacuum, resting-origin, right-moving, left-moving. No postselection.
    V = sp.Matrix([[1, 0], [0, -sp.Rational(1, 3)],
                   [0, sp.Rational(2, 3)], [0, sp.Rational(2, 3)]])
    assert V.H*V == sp.eye(2)
    J = sp.kronecker_product(V, V)
    propagated = J*rho*J.H
    encoded = [V*A*V.H + sp.eye(4)-V*V.H for A in measurements]
    assert all(A.H == A and sp.simplify(A*A-sp.eye(4)) == sp.zeros(4) for A in encoded)
    full_bell = (sp.kronecker_product(encoded[0], encoded[2]+encoded[3])
                 + sp.kronecker_product(encoded[1], encoded[2]-encoded[3]))
    assert sp.simplify(sp.trace(propagated*full_bell)) == sp.Rational(112, 45)
    assert J.H*propagated*J == rho

    # Physically embed each local vacuum/one-excitation code into three qubits
    # and execute the unchanged parent partial-trace operation independently.
    E = sp.zeros(8, 4)
    for col, row in enumerate((0, 4, 2, 1)):
        E[row, col] = 1
    six = sp.kronecker_product(E, E)*propagated*sp.kronecker_product(E.H, E.H)
    actual_reduced = parent.ptrace(six, 6, (0, 3))

    p = sp.Symbol('p', nonnegative=True)
    reduced = sp.Matrix([[1-8*p/9, 0, 0, 0],
                         [0, 4*p/9, 4*p/9, 0],
                         [0, 4*p/9, 4*p/9, 0],
                         [0, 0, 0, 0]])
    assert actual_reduced == reduced.subs(p, sp.Rational(1, 9))
    assert sp.trace(reduced) == 1
    assert sp.simplify(sp.trace(reduced*bell)) == 112*p/45
    pt = sp.zeros(4)
    for a, b, c, d in product(range(2), repeat=4):
        pt[2*a+d, 2*c+b] = reduced[2*a+b, 2*c+d]
    assert sp.simplify(pt.extract((0, 3), (0, 3)).det()) == -16*p*p/81
    reduced_records = []
    for t, probability in enumerate(source_probabilities):
        reduced_records.append({'tick': t, 'receiver_probability': str(probability),
                                'equatorial_CHSH': str(Fraction(112, 45)*probability),
                                'PT_minor': str(-Fraction(16, 81)*probability**2)})
    # Local channels cannot change the remote marginal, including correlations.
    I = sp.eye(2)
    channels = [(I,), (X,), ((I+X)/2, (I-X)/2)]
    ns = 0
    for ks in channels:
        assert sum((k.H*k for k in ks), sp.zeros(2)) == I
        changed = sum((sp.kronecker_product(k, I)*rho*sp.kronecker_product(k.H, I)
                       for k in ks), sp.zeros(4))
        assert parent.ptrace(changed, 2, (1,)) == parent.ptrace(rho, 2, (1,))
        ns += 1
    return {'full_local_gate_dimension': 8, 'unitary': True,
            'explicit_hole_extension': {'parent_one_hole_gate_is_identity': True, 'new_gate_complement_symmetric': True, 'commutes_with_number': True, 'filled_and_empty_local_backgrounds_fixed': True, 'one_hole_equals_one_excitation': True}, 'commutes_with_number': True,
            'encoded_two_lab_CHSH': '112/45', 'one_step_single_receiver_CHSH': '112/405',
            'receiver_minor_formula': '-16*p^2/81', 'receiver_CHSH_formula': '112*p/45',
            'explicit_six_qubit_receiver_trace': True, 'no_postselection': True,
            'local_channel_non_signalling_cases': ns, 'receiver_records': reduced_records}


def precision_four_ports():
    G = sp.Matrix(H)/3
    def gate(ids):
        T = sp.eye(4)
        for i, a in enumerate(ids):
            for j, b in enumerate(ids):
                T[a, b] = G[i, j]
        return T
    W = gate((1, 2, 3))*gate((0, 1, 2))
    M = 9*W
    assert W.T*W == sp.eye(4)
    assert M == sp.Matrix([[-3, 6, 6, 0], [2, 5, -4, 6],
                           [2, -4, 5, 6], [8, 2, 2, -3]])
    v = sp.Matrix([1, 0, 0, 0])
    records = []
    for t in range(1, 33):
        v = M*v
        assert all(int(v[i]) % 3 == 2 for i in (1, 2, 3))
        assert sum(x*x for x in v) == 9**(2*t)
        for i in (1, 2, 3):
            assert (v[i]/9**t).q == 9**t
        if t <= 4:
            records.append({'pairs_of_gates': t, 'state': [str(x/9**t) for x in v]})
    return {'integer_update_matrix': [[int(x) for x in row] for row in M.tolist()],
            'pairs_checked': 32, 'exact_denominator_formula': '9^t in components 2,3,4',
            'mod3_residue_after_first_pair': [0, 2, 2, 2],
            'first_states': records, 'unit_norm': True,
            'infinite_reachable_set_in_fixed_four_modes': True,
            'not_closed_on_any_fixed_finite_amplitude_alphabet': True}


def run(steps):
    parent = load_parent()
    old_integer = parent.load_parent()
    x, scaled = (1, 0, 0), (3, 0, 0)
    def quantum_ray(v):
        q = sp.Matrix(v)
        return q*q.T / (q.T*q)[0]
    assert quantum_ray(x) == quantum_ray(scaled)
    cx, cy = old_integer.reflect3(x), old_integer.reflect3(scaled)
    assert cx == x and cy == (-1, 2, 2)
    assert quantum_ray(cx) != quantum_ray(cy)
    ray_obstruction = {'input_integer_vectors': [x, scaled], 'same_normalized_input_density': True,
                       'output_integer_vectors': [cx, cy], 'first_output_probability': ['1', '1/9'],
                       'interpretation': 'Guarded integer reflection does not descend through normalization to a pure quantum state update; retain scale or prove a different bridge.'}
    assert sp.Matrix(H).T*sp.Matrix(H) == 9*sp.eye(3)
    frame = tuple(range(D))
    states = history(frame, steps)
    population = {(ZERO, 0): 1}
    probabilities = []
    records = []
    flux_checks = 0
    first_interference = None
    for t, state in enumerate(states):
        assert sum(x*x for x in state.values()) == 9**t
        assert all(sum(abs(a) for a in z) <= t for z, _ in state)
        p = Fraction(sum(v*v for (z, _), v in state.items() if z == ZERO), 9**t)
        probabilities.append(p)
        if t:
            axis = frame[(t-1) % D]
            flux_checks += local_balance(states[t-1], state, axis)
            assert inverse_step(state, axis) == states[t-1]
            population = dephased_step(population, axis)
            assert sum(population.values()) == 9**t
            frontier = tuple((t+5-j)//6 for j in range(6))
            assert state.get((frontier, 1)) == 2*(-1)**(t-1)
            assert Fraction(state[frontier, 1], 3**t).denominator == 3**t
        difference = sum(abs(state.get(key, 0)**2 - population.get(key, 0))
                         for key in set(state) | set(population))
        if difference and first_interference is None:
            first_interference = t
        records.append({'tick': t, 'nonzero_modes': len(state),
                        'nonzero_cells': len({z for z, _ in state}),
                        'source_cell_probability': str(p),
                        'coherent_vs_dephased_l1': str(Fraction(difference, 9**t)),
                        'largest_numerator_bits': max(abs(x).bit_length() for x in state.values())})
    assert probabilities[:7] == [Fraction(1, 9**t) for t in range(7)]
    assert probabilities[7] == Fraction(129, 3**14)
    assert probabilities[7]/probabilities[6] == Fraction(43, 3)
    assert first_interference == 8
    assert states[8].get((ZERO, 0)) == 33
    population8 = {(ZERO, 0): 1}
    for t in range(8):
        population8 = dephased_step(population8, frame[t % D])
    assert population8[ZERO, 0] == 513
    # Before the eighth coin, deleting relative phases changes this output.
    assert population is not None
    # Exact echo with the actual inverse sequence; not an external spontaneous return.
    back = states[-1]
    for t in range(steps-1, -1, -1):
        back = inverse_step(back, frame[t % D])
    assert back == states[0]

    covariance = 0
    for perm in permutations(range(D)):
        transformed = history(perm, 3)
        assert all(transformed[t] == act(states[t], perm) for t in range(4))
        covariance += 4
    translations = 0
    for shift0 in ((4, -2, 1, 0, 5, -3), (1,)*6, (-2,)*6):
        v = act(states[0], frame, shift0)
        for t in range(8):
            v = step(v, frame[t % D])
            assert v == act(states[t+1], frame, shift0)
            translations += 1
    # The finite torus agrees with the infinite-space calculation before wrapping.
    L = 2*steps+3
    v = states[0]
    for t in range(steps):
        v = step(v, frame[t % D], L)
        expected = {(tuple(x % L for x in z), k): a for (z, k), a in states[t+1].items()}
        assert len(expected) == len(states[t+1]) and v == expected
    # Additional signed finite inputs, testing exact conservation and local law.
    rng = random.Random(170916)
    general = 0
    for trial in range(24):
        w = {}
        for _ in range(15):
            z = tuple(rng.randrange(-1, 2) for _ in range(D))
            k = rng.randrange(3)
            w[z, k] = rng.randrange(-5, 6)
        w = {key: a for key, a in w.items() if a}
        for axis in range(D):
            v = step(w, axis)
            assert sum(a*a for a in v.values()) == 9*sum(a*a for a in w.values())
            assert inverse_step(v, axis) == w
            local_balance(w, v, axis)
            general += 1
    return {'schema': 'EM_CONSERVATIVE_NETWORK_PRECISION_RESULTS_V1', 'event_id': EVENT,
            'status': 'EXACT_FINITE_CALCULATIONS_WITH_ORDINARY_PROOFS_NOT_NATIVE_PHYSICS',
            'parent_file_sha256': PARENT_HASH, 'law_sha256': sha256((HERE/'law_specification.json').read_bytes()).hexdigest(),
            'source_snapshot': '7101de468735f6e0b6a74c8f1bb1cf0fb29a8712',
            'hole_extension_sha256': sha256((HERE/'hole_extension.json').read_bytes()).hexdigest(),
            'steps': steps, 'trajectory': records,
            'execution_corrections': ['Used symbolic simplification before testing encoded-observable square identity; the original structural equality test rejected an unexpanded but identically zero expression. No gate or state was changed.'],
            'local_continuity_equalities': flux_checks, 'axis_covariance_equalities': covariance,
            'translation_equalities': translations, 'general_signed_inputs_steps': general,
            'finite_torus_period': L, 'finite_torus_steps_equal_without_wrap': steps,
            'exact_reverse_echo': True, 'first_phase_sensitive_tick_for_this_seed': first_interference,
            'native_swaps': transport_permutation_test(),
            'quantum_transport': quantum_tests(parent, probabilities),
            'four_port_precision': precision_four_ports(),
            'guarded_integer_quantum_readout_obstruction': ray_obstruction,
            'nonclaims': ['Quantum tensors/amplitudes/Born rule are extra comparison assumptions.',
                          'Dense resident slots do not imply dense excitation or a derived force law.',
                          'Number conservation is not conservation of a full implementation Hamiltonian.',
                          'Neither rational amplitudes nor finite dimension imply fixed resolution.',
                          'Encoded-lab Bell measurements may require coherent phase references.',
                          'No physical force, NS conclusion, independent review or Lean validation.',
                          'An intentional inverse-sequence echo is not a claim of automatic global recurrence.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--steps', type=int, default=12)
    parser.add_argument('--output', type=Path, default=Path('results_17.json'))
    args = parser.parse_args()
    if not 8 <= args.steps <= 14:
        parser.error('Executed finite checker is bounded to 8 <= steps <= 14')
    report = run(args.steps)
    text = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    args.output.write_text(text, encoding='utf-8')
    for row in report['trajectory']:
        print(row)
    print('four-mode denominator:', report['four_port_precision']['exact_denominator_formula'])
    print('exact checks completed')

if __name__ == '__main__':
    main()
