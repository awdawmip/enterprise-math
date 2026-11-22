#!/usr/bin/env python3
"""PREFIX-1003: typed Z2 phase BRC cover for the fixed Stage46 12-port candidate.
Scientific input: P000 V5 frozen at f42f2906; Stage46 C[h,d]=1/6-delta[h,d].
One negative native-axis step; anchor 0, incoming-neighbour -e1.
"""
from collections import defaultdict
from fractions import Fraction
import json

N = 6
ORIGIN = (0,) * N
E1 = (1,) + (0,) * (N - 1)
INITIAL_INCOMING = N  # -e1; an incoming-neighbour direction, not last travelled direction


def shift(x, direction):
    y = list(x)
    y[direction % N] += 1 if direction < N else -1
    return tuple(y)


def brc_cover(steps, blocked=False, positive_only=False):
    # State=(cell, incoming-neighbour port, negative-branch count, Z2 phase).
    # Value is a nonnegative integer positive-weight BRC cover coefficient.
    states = {(ORIGIN, INITIAL_INCOMING, 0, 0): 1}
    for _ in range(steps):
        next_states = defaultdict(int)
        for (cell, incoming, negatives, phase), coefficient in states.items():
            for outgoing in range(N if positive_only else 2 * N):
                negative_count = negatives + int(outgoing >= N)
                if negative_count > (0 if positive_only else 1):
                    continue
                if blocked and ((cell == ORIGIN and outgoing == 0) or
                                (cell == E1 and outgoing == N)):
                    continue
                turn_back = incoming == outgoing
                mag = 5 if turn_back else 1
                next_state = (shift(cell, outgoing), (outgoing + N) % (2 * N),
                              negative_count, phase ^ int(turn_back))
                next_states[next_state] += mag * coefficient
        states = next_states
    # Z2 character applied only after retaining the native endpoint and last port.
    output = defaultdict(int)
    for (cell, incoming, negative_count, phase), magnitude in states.items():
        if negative_count == (0 if positive_only else 1):
            output[(cell, incoming)] += (-1 if phase else 1) * magnitude
    return {key: val for key, val in output.items() if val}


def translated(packet):
    return {(tuple(xi + di for xi, di in zip(cell, E1)), port): value
            for (cell, port), value in packet.items()}


def packet_mass(packet, steps):
    return Fraction(sum(value * value for value in packet.values()), 36 ** steps)


def check(steps):
    free = brc_cover(steps)
    masked = brc_cover(steps, blocked=True)
    recovered = defaultdict(int, free)
    if steps >= 2:
        for key, value in translated(brc_cover(steps - 1)).items():
            recovered[key] -= value
    if steps >= 3:
        for key, value in translated(brc_cover(steps - 3, positive_only=True)).items():
            recovered[key] += 25 * value
    recovered = {key: val for key, val in recovered.items() if val}
    assert recovered == masked, (steps, len(masked), len(recovered))
    return {'n': steps,
            'unmasked_first_interior_mass': str(packet_mass(free, steps)),
            'masked_first_interior_mass': str(packet_mass(masked, steps)),
            'fibre_count_unmasked': len(free),
            'fibre_count_masked': len(masked),
            'signed_fibre_comparison': 'PASS'}


def prefix_third_amplitude():
    # Paths first blocked at step 3, exactly one negative step in that prefix.
    counts = defaultdict(int)
    for d0 in range(12):
        for d1 in range(12):
            for d2 in range(12):
                dirs = [d0, d1, d2]
                if sum(d >= 6 for d in dirs) != 1:
                    continue
                x, incoming, numerator = ORIGIN, INITIAL_INCOMING, 1
                first_forbidden = None
                for idx, d in enumerate(dirs, 1):
                    if (x == ORIGIN and d == 0) or (x == E1 and d == 6):
                        first_forbidden = first_forbidden or idx
                    numerator *= -5 if incoming == d else 1
                    x = shift(x, d)
                    incoming = (d + 6) % 12
                if first_forbidden == 3:
                    counts[(x, incoming)] += numerator
    return {'matching_fibre_count': len(counts),
            'terminal_cell_and_port': [[list(x), p, v] for (x, p), v in counts.items()],
            'signed_total_numerator': sum(counts.values())}


def main():
    assert prefix_third_amplitude()['signed_total_numerator'] == -25
    results = [check(n) for n in range(1, 9)]
    doc = {'schema': 'PREFIX1003_BRC_PORT_PHASE_COVER_CERTIFICATE_V1',
           'input': {'axis_count': 6, 'port_count': 12,
                     'initial_incoming_direction': '-e1',
                     'blocked_directed_links': ['0 -> +e1', '+e1 -> 0'],
                     'grade_sector': 'exactly one negative primitive step',
                     'semiring': 'N-weighted Z2 phase cover; observe by signed character per (cell,last-port)'},
           'proof_obligations': {'time_grade_lemma': 't=grade+2*negative_steps',
                                 'third_step_forbidden_signed_numerator': -25},
           'prefix': prefix_third_amplitude(), 'checked': results,
           'operation': 'typed_phase_cover_finite_branch_recurrence',
           'canonical_stage46_module_invoked': False,
           'mathematical_status': 'AUTHOR_PROOF_EXACT_CHECK_NOT_REVIEWED'}
    with open('PREFIX1003_R6_EXACT_RESULTS.json', 'w', encoding='utf-8') as fp:
        json.dump(doc, fp, ensure_ascii=False, indent=2)
        fp.write('\n')
    print(json.dumps({'status': 'PASS', 'n_range': [1, 8], 'prefix': doc['prefix'],
                      'masked_masses': [r['masked_first_interior_mass'] for r in results]},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
