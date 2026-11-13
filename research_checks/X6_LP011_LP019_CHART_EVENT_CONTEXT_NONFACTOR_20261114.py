#!/usr/bin/env python3
"""Exact finite cross-consumer check over all 20 X6 three-axis charts and six frames.

Original consumers (untouched):
  check_branch_selector_context.py blob bb8fd71bafa5b8c53c5170d2347baa0f2c06f5fb
  check_slice_frame_holonomy.py blob 44006c1f9f26907006820e7bbc17f24dd5a8cc04

A native signed edge has two geodesic midpoints, with event-kind-dependent
selection; changing the S3 chart frame cannot determine the event kind.
This finite corroboration is not a native benchmark of other X6 dynamics.
"""
import hashlib
import importlib.util
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCES = {
    'check_branch_selector_context': (
        'experiments/x6_branch_selector_context_v3_20260906/check_branch_selector_context.py',
        'bb8fd71bafa5b8c53c5170d2347baa0f2c06f5fb',
    ),
    'check_slice_frame_holonomy': (
        'experiments/x6_20_slice_holonomy_v2_20260906/check_slice_frame_holonomy.py',
        '44006c1f9f26907006820e7bbc17f24dd5a8cc04',
    ),
}

def load(name):
    relpath, expected_blob = SOURCES[name]
    source = HERE.parent / relpath
    if not source.is_file():
        # Original-byte copies are stored alongside the checker in a standalone replay package.
        source = HERE / (name + '.py')
    data = source.read_bytes()
    actual_blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert actual_blob == expected_blob, (name, actual_blob, expected_blob)
    spec = importlib.util.spec_from_file_location(name, source)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

selector = load('check_branch_selector_context')
charts = load('check_slice_frame_holonomy')
assert len(charts.CHARTS) == 20
assert len(charts.G) == 6  # every S3 chart frame change is represented

edge_conflicts = joint_checks = ordered_frames = 0
witnesses = []
for raw in charts.CHARTS:
    for S in permutations(sorted(raw)):
        ordered_frames += 1
        tokens = [selector.unit(i) for i in S]
        for phase in range(6):
            targets = [selector.q_action(S, x) for x in tokens]
            opts = [selector.branches(a, b) for a, b in zip(tokens, targets)]
            common = []
            for choices in product(('INNER', 'OUTER'), repeat=3):
                mids = [opts[t][choices[t]] for t in range(3)]
                if mids[0] == mids[1] == mids[2]:
                    common.append((choices, mids[0]))
                joint_checks += 1
            assert common == [(('INNER',)*3, selector.ZERO)]
            a, b = tokens[0], targets[0]
            paths = selector.branches(a, b)
            assert paths['INNER'] == selector.ZERO
            assert paths['OUTER'] == selector.add(a, b)
            assert paths['OUTER'] != paths['INNER']
            assert selector.l1(a, paths['INNER']) == selector.l1(paths['INNER'], b) == 1
            assert selector.l1(a, paths['OUTER']) == selector.l1(paths['OUTER'], b) == 1
            if len(witnesses) < 2:
                witnesses.append({'chart':S, 'phase':phase, 'a':a, 'b':b,
                                  'INNER':paths['INNER'], 'OUTER':paths['OUTER']})
            edge_conflicts += 1
            tokens = targets
        assert tokens == [selector.unit(i) for i in S]

assert ordered_frames == 120
assert joint_checks == 5760
assert edge_conflicts == 720
print('PASS_X6_CHART_FRAME_EVENT_KIND_NONFACTOR_EXACT')
print('raw_charts', len(charts.CHARTS))
print('ordered_S3_chart_frames', ordered_frames)
print('six_phase_edge_conflicts', edge_conflicts)
print('triadic_joint_midpoint_assignments', joint_checks)
print('smallest_witness', witnesses[0])
print('meaning','Event kind required beyond signed endpoints and chart frame on this restricted interface')
