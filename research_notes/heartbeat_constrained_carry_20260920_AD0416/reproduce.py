#!/usr/bin/env python3
"""Reproduce finite examples; general claims are proved in RESEARCH_NOTE.md.

Run from the repository root with PYTHONPATH=src. --write saves RESULTS.json.
"""
from __future__ import annotations
import argparse
from dataclasses import asdict
from fractions import Fraction as F
import json
from pathlib import Path
import platform
import sympy
from enterprise_math.brc_transport import Affine, eye, matrix, mm, inv, sm
from enterprise_math.brc_control_port import ControlPacket, certify_control_partition, refine_control_partition
from enterprise_math.brc_control_mass import quotient_control_mass_matrix
from enterprise_math.heartbeat_switching_carry import linear_carry_spread, split_feedback_packet, growing_block_state
from enterprise_math.heartbeat_lattice_search import find_phase_lattice
from enterprise_math.heartbeat_constrained_carry import (LinearEdge, ControlGraph,
    packet_control_graph, find_graph_lattices, verify_graph_lattice_result,
    classify_monomial_carry, verify_monomial_carry_result, replay_graph_word)


def diagonal(xs):
    return matrix([[x if i == j else 0 for j in range(6)] for i, x in enumerate(xs)])


def rotation(p):
    return matrix([[(p if i == 0 else 1) if j == (i-1) % 6 else 0 for j in range(6)] for i in range(6)])


def graph1(actions):
    return ControlGraph(1, tuple(LinearEdge(0, 0, a) for a in actions))


def fraction_json(x):
    if isinstance(x, F):
        return x.numerator if x.denominator == 1 else f'{x.numerator}/{x.denominator}'
    raise TypeError(type(x).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    result = {'status': 'EXACT_COMPUTED_EXAMPLES_NOT_UNIVERSAL_TEST_PROOF',
              'environment': {'python': platform.python_version(), 'sympy': sympy.__version__},
              'transient': [], 'nonperiodic_balanced': [], 'mixed_radix': {}}
    for p in (2, 3, 5):
        t = matrix([[int(i == j)+int(j == i+1) for j in range(6)] for i in range(6)])
        a = mm(mm(t, diagonal((p**6, 1, 1, 1, 1, 1))), inv(t))
        g = ControlGraph(2, (LinearEdge(0, 0, eye(6)), LinearEdge(1, 1, eye(6)),
                             LinearEdge(0, 1, eye(6)), LinearEdge(0, 1, a)))
        r0 = find_graph_lattices(g, p, depth_budget=0)
        r1 = find_graph_lattices(g, p, depth_budget=1)
        assert verify_graph_lattice_result(g, r0) and verify_graph_lattice_result(g, r1)
        result['transient'].append({'prime': p, 'R0': r0.status, 'R1': r1.status,
            'R1_rounds': r1.rounds, 'potential': r1.certificate.volume_potential,
            'edge_slacks': r1.certificate.edge_slacks, 'bound': r1.certificate.all_path_spread_bound,
            'attained': linear_carry_spread(a, p), 'source_digest': g.digest})
        h = rotation(p)
        balanced = graph1((h, mm(h, h), sm(p, inv(h)), eye(6)))
        answer = classify_monomial_carry(balanced, p)
        assert verify_monomial_carry_result(balanced, answer)
        result['nonperiodic_balanced'].append({'prime': p, 'bound': answer.exact_spread_bound,
            'old_generic_H_only_bound': find_phase_lattice((h,), p, depth_budget=1).all_word_spread_bound,
            'attaining_path': asdict(answer.attaining_path)})
    g = graph1((rotation(2), rotation(3)))
    _, c = replay_graph_word(g, 0, (0, 1, 1, 1, 1, 1))
    result['mixed_radix']['six_step_product'] = c
    for p in (2, 3):
        answer = classify_monomial_carry(g, p)
        assert verify_monomial_carry_result(g, answer)
        result['mixed_radix'][str(p)] = {'status': answer.status,
            'prefix': asdict(answer.cycle_prefix), 'cycle': asdict(answer.positive_cycle),
            'explicit_repetitions': {str(n): linear_carry_spread(
                matrix([[int(x) for x in row] for row in (sympy.Matrix(c)**n).tolist()]), p)
                for n in (1, 3, 8)}}
    packet, _, _ = split_feedback_packet()
    graph = packet_control_graph(packet)
    result['existing_feedback'] = {
        'all_initial_ports': classify_monomial_carry(graph, 2).exact_spread_bound,
        'center_only': classify_monomial_carry(graph, 2, initial_states=(1,)).exact_spread_bound}
    identity = Affine.identity(6)
    changed = Affine(diagonal((64, 1, 1, 1, 1, 1)), (1, -2, 3, -4, 5, -6))
    packet = ControlPacket.from_edges(2, 0, 1, (
        (0, 0, F(1,4), identity, 2), (0,1,F(1,4), identity,1),
        (0,1,F(1,8), changed,2), (1,1,F(1), identity,1)))
    try:
        certify_control_partition(packet, (0,0))
    except ValueError:
        rejected = True
    else:
        rejected = False
    serial = ControlPacket.identity(2)
    trace = []
    for n in range(1, 13):
        serial = serial.then(packet.at(serial.end))
        out = serial.evaluate(0, (0,)*6)
        total = sum(hist.total_mass for hist in out.values())
        stay = sum(hist.total_mass for (s,_), hist in out.items() if s == 0)
        assert total == 1 and stay == F(1,2)**n
        trace.append({'n': n, 'total_mass': total, 'port0_mass': stay})
    result['BRC_observer_separation'] = {
        'mass_quotient': quotient_control_mass_matrix(packet, (0,0)),
        'effect_quotient_rejected': rejected,
        'effect_refinement': refine_control_partition((packet,), (0,0)), 'trace': trace}
    result['selected_schedule_peaks'] = [
        {'tick': k*k, 'debt': growing_block_state(k*k).debt, 'unrestricted_worst': k*k}
        for k in (1,2,5,10,20)]
    text = json.dumps(result, indent=2, ensure_ascii=False, default=fraction_json)+'\n'
    if args.write:
        Path(__file__).with_name('RESULTS.json').write_text(text, encoding='utf-8')
    print(text, end='')


if __name__ == '__main__':
    main()
