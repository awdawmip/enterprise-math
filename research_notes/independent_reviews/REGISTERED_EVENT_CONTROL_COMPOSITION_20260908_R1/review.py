"""Bounded independent replay of the three registered-event revision fixes.

Usage: python -B review.py /path/to/exact-reviewed-enterprise-math-checkout
Writes only adjacent review.json. No network, Git mutation, or source editing.
"""
from __future__ import annotations
import argparse
import ast
from datetime import datetime, timedelta, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('repo', type=Path, help='checkout containing the exact reviewed candidate files')
ROOT = parser.parse_args().repo.resolve()
OUT = Path(__file__).resolve().parent
if not __debug__:
    raise RuntimeError('Normal Python assertions are required; do not use -O.')
BASE = '86a04d17cbffd687b1ef74ab4990cf6b2b7e093a'
BASE_TREE = '7ab67689a86e47a2c0be43ca2fb5e2c4feefdfc5'
MANIFEST_SHA256 = '3d6055a3cffc9b7de99cabeebeb1a8e2e6b92230ebe8f77dc6794984973fb266'
PINS = {'.github/workflows/control-plane-pr-focused-validation.yml': 'f9044cee50fce642ef12580249b05865757a41e5ea4859a88121cc18a9cbad9e', 'docs/RESEARCH_SCHEDULING_PROTOCOL.en.md': 'a2a814f81a951e37c6bf6c60ed26fc73cf19470966d6f731f9e51ef93b054a9b', 'tests/test_exact_invalid_result_authority_isolation_20260907.py': 'f97ff49e6498c79bab49a807e412a035046f7e2f9611671b238e5588aabc6a67', 'tests/test_result_handoff_dispatch_guard.py': 'e4fbf92a486713c30f19b964ec76ecedf034ce0b480e6ff6a55f5a8c54f18b8d', 'tools/research_dispatch.py': 'ac5991215550c95b4dcb4059b53a63fc727d6933beb077f25b15096144b3675a', 'tools/research_runtime_reducer.py': 'b44513708ea9099e369aa445769a6db56fb3b78f68dfcd6692f6b7a782ea0c55', 'tests/test_registered_event_control_composition_20260908.py': '004a732d6ab80dd26610741814448acf7049e6c32797644e5540689e05d8ae13', 'tests/test_registered_event_publication_time_gate.py': 'f7759fa830a39b101875fc7784dd58ddfd49c343ccbe1ac7d1f0add5f509a598', 'tests/test_registered_handoff_scope_guard.py': 'd25c551b123f2c21e75c1a35c03c0a70148d7d3675d87561cdba570b4a4b6828', 'research_notes/OWNER_REGISTERED_EVENT_CONTROL_COMPOSITION_20260908.md': 'e06af64e291af8cd53bd38b3a0dca12a6e30a9939cc29e566b0ae4822aa09c07', 'tools/research_dispatch_core.py': 'e0aad8b3a54c4812d45348a6eef3137756ba629428e4a95c2f40c4293f4153a8'}
CHANGED_TRACKED = ['.github/workflows/control-plane-pr-focused-validation.yml', 'docs/RESEARCH_SCHEDULING_PROTOCOL.en.md', 'tests/test_exact_invalid_result_authority_isolation_20260907.py', 'tests/test_result_handoff_dispatch_guard.py', 'tools/research_dispatch.py', 'tools/research_dispatch_core.py', 'tools/research_runtime_reducer.py']
PRESERVED_WRAPPERS = ['_bind_intent_claim_publications', '_event_source_index', '_post_review_runtime_transition', '_overlay_result_state', '_overlay_active_cohort', '_dispatch_result_read_snapshot']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frozen_inputs():
    actual = {rel: sha(ROOT.joinpath(rel).read_bytes()) for rel in PINS}
    assert actual == PINS, 'reviewed candidate input hashes changed'
    return actual


before = frozen_inputs()
public_tree = subprocess.run(['git', 'rev-parse', BASE + '^{tree}'], cwd=ROOT,
                             capture_output=True, check=True, text=True).stdout.strip()
assert public_tree == BASE_TREE
# One bounded collection proves the source boundary relative to the public base.
entries = subprocess.run(['git', 'ls-tree', '-r', '-z', BASE], cwd=ROOT,
                         capture_output=True, check=True).stdout
paths = {}
for entry in entries.split(b'\0'):
    if entry:
        info, path = entry.split(b'\t', 1)
        mode, kind, oid = info.split()
        assert kind == b'blob'
        paths[path.decode()] = oid.decode()
ids = list(dict.fromkeys(paths.values()))
raw = subprocess.run(['git', 'cat-file', '--batch'], cwd=ROOT,
                     input=('\n'.join(ids) + '\n').encode(), capture_output=True, check=True).stdout
stream = io.BytesIO(raw)
blobs = {}
for oid in ids:
    header = stream.readline().split()
    assert header[0].decode() == oid and header[1] == b'blob'
    blobs[oid] = stream.read(int(header[2]))
    assert stream.read(1) == b'\n'
changed = sorted(rel for rel, oid in paths.items() if ROOT.joinpath(rel).read_bytes() != blobs[oid])
assert changed == sorted(CHANGED_TRACKED) and len(paths) == 4556


def functions(source):
    return {node.name: ast.get_source_segment(source, node)
            for node in ast.parse(source).body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))}


dispatch_rel = 'tools/research_dispatch.py'
base_dispatch = blobs[paths[dispatch_rel]].decode()
new_dispatch = ROOT.joinpath(dispatch_rel).read_text(encoding='utf-8')
old_functions, new_functions = functions(base_dispatch), functions(new_dispatch)
for name in PRESERVED_WRAPPERS:
    assert old_functions[name] == new_functions[name], name
held_marker = '    if held and _core._is_registered(task):'
old_filter, new_filter = old_functions['_filter_registered_events'], new_functions['_filter_registered_events']
assert old_filter[old_filter.index(held_marker):] == new_filter[new_filter.index(held_marker):]


def captured_core_call(source):
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == '_ORIGINAL_FILTER_REGISTERED_EVENTS':
            return ast.get_source_segment(source, node)
    raise AssertionError('missing held-aware original core call')


assert captured_core_call(base_dispatch) == captured_core_call(new_dispatch)
core_rel = 'tools/research_dispatch_core.py'
base_core = blobs[paths[core_rel]].decode()
new_core = ROOT.joinpath(core_rel).read_text(encoding='utf-8')
added_signature = '    *,\n    resolved_lease_minutes: int | None = None,\n'
added_call = '        resolved_lease_minutes=lease,\n'
assert new_core.count(added_signature) == new_core.count(added_call) == 1
assert new_core.replace(added_signature, '', 1).replace(added_call, '', 1) == base_core

sys.path.insert(0, str(ROOT))
from tests import test_registered_event_control_composition_20260908 as fixture
from tools import research_dispatch as dispatch
from tools import research_runtime_reducer as reducer
fixture.setUpModule()
case = fixture.RegisteredEventControlCompositionTests('test_all_composed_core_hooks_remain_live')
case.setUp()
checks = []


def state_case(name, expected, evaluate):
    try:
        state = evaluate()
        actual = state.get('dispatch_state')
        passed = actual == expected
        checks.append({'case': name, 'expected_dispatch_state': expected,
                       'actual_dispatch_state': actual, 'pass': passed,
                       'hard_block': state.get('hard_block'), 'ignored_events': state.get('ignored_events', [])})
    except Exception as error:
        checks.append({'case': name, 'expected_dispatch_state': expected, 'pass': False,
                       'exception': type(error).__name__, 'message': str(error)})


try:
    task = case.unheld_definition()
    start = reducer.parse_time(fixture.PUBLISHED)
    owner = case.claim(task, 9001, start)
    malformed = case.event(task, 'HANDOFF', 9002, start + timedelta(minutes=1),
                           claim_id='cross-owner', next_action='invalid machine scope', handoff_scope={})
    state_case('postcutover_mapping_scope_public_path', 'BLOCKED', lambda: dispatch.reduce_definition(
        task, [owner, malformed], now=start + timedelta(hours=3), root=case.root))
    legacy = case.event(task, 'HANDOFF', 9002, start + timedelta(minutes=1),
                        claim_id='cross-owner', next_action='legacy mapping field', terminal_candidate={})
    state_case('mapping_legacy_candidate_pure_reducer', 'LEASED', lambda: reducer.reduce_task(
        task, [owner, legacy], default_lease_minutes=120, now=start + timedelta(minutes=2)))

    for lease, progress_minute, terminal_minute, expected in [(120, 10, 110, 'BLOCKED'), (10, 5, 20, 'NEEDS_DISPATCH')]:
        definition = {**task, 'claim_lease_minutes': lease}
        claim = case.claim(definition, 9101, start)
        claim['lease_minutes'] = lease
        progress = case.event(definition, 'PROGRESS', 9102, start + timedelta(minutes=progress_minute),
                              claim_id='cross-owner', progress_ref='durable fixture update')
        ambiguous = case.event(definition, 'HANDOFF', 9103, start + timedelta(minutes=terminal_minute),
                               claim_id='cross-owner', next_action='ambiguous owner return')
        state_case('default_renewal_' + str(lease) + '_minute_claim', expected,
                   lambda: dispatch.reduce_definition(definition, [claim, progress, ambiguous],
                                                      now=start + timedelta(hours=4), root=case.root))

    for scoped in [False, True]:
        extra = {'handoff_scope': 'CONTINUATION'} if scoped else {}
        mismatched = case.event(task, 'HANDOFF', 9202, start + timedelta(minutes=1),
                                claim_id='cross-owner', researcher_id='EM-OTHER-ABC123',
                                next_action='wrong researcher', **extra)
        state_case('mismatched_researcher_' + ('typed' if scoped else 'ambiguous'), 'NEEDS_DISPATCH',
                   lambda: dispatch.reduce_definition(task, [case.claim(task, 9201, start), mismatched],
                                                      now=start + timedelta(hours=3), root=case.root))

    # Extra checks are confined to the new parameter's consumers and publication scope.
    definition = {**task}
    definition.pop('claim_lease_minutes', None)
    claim = case.claim(definition, 9301, start)
    claim['lease_minutes'] = 37
    heartbeat = case.event(definition, 'HEARTBEAT', 9302, start + timedelta(minutes=5), claim_id='cross-owner')
    done = case.event(definition, 'DONE', 9303, start + timedelta(minutes=43), claim_id='cross-owner')
    state_case('custom_caller_default_37_through_heartbeat_and_done', 'NEEDS_DISPATCH',
               lambda: dispatch.reduce_definition(definition, [claim, heartbeat, done],
                                                  now=start + timedelta(hours=4), default_lease_minutes=37, root=case.root))
    direct_done = case.event(task, 'DONE', 9401, start, claim_id='historical-direct-owner')
    rejected = [{'index': 0, 'reason': 'registered DONE requires a frozen result with terminal Driver review'}]
    state_case('legacy_five_argument_direct_hook', 'BLOCKED', lambda: dispatch._block_unreviewed_registered_done(
        task, {'state': 'READY', 'dispatch_state': 'NEEDS_DISPATCH'}, [direct_done], rejected, None))
    try:
        dispatch._event_had_live_claim(task, direct_done, [])
    except dispatch.DispatchError as error:
        checks.append({'case': 'replay_context_without_resolved_lease_rejected',
                       'pass': 'requires the dispatch resolved lease' in str(error), 'reason': str(error)})
    else:
        checks.append({'case': 'replay_context_without_resolved_lease_rejected', 'pass': False})
    wrong_publication = case.claim(task, 9501, start)
    wrong_publication['publication_id'] = 'TP2-INDEPENDENT-OLD'
    ambiguous = case.event(task, 'HANDOFF', 9502, start + timedelta(minutes=1),
                           claim_id='cross-owner', next_action='old generation cannot block current generation')
    state_case('wrong_publication_claim_cannot_supply_terminal_barrier', 'NEEDS_DISPATCH',
               lambda: dispatch.reduce_definition(task, [wrong_publication, ambiguous],
                                                  now=start + timedelta(hours=3), root=case.root))
finally:
    case.tearDown()
    case.doCleanups()

assert frozen_inputs() == before
assert len(checks) == 10
passed = all(row['pass'] for row in checks)
report = {
    'schema': 'owner_registered_event_revision1_independent_review_v1',
    'status': 'PASS_BOUNDED_REVISION_REVIEW' if passed else 'FAIL_BOUNDED_REVISION_REVIEW',
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'scope': 'Original three root causes, resolved-lease consumers and exact task/publication/researcher boundaries; no full suite or mathematical review.',
    'public_base_commit': BASE, 'public_base_tree': public_tree,
    'candidate_manifest_sha256': MANIFEST_SHA256, 'candidate_source_sha256': before,
    'script_sha256': sha(Path(__file__).read_bytes()), 'python': sys.version.split()[0],
    'checks': checks,
    'source_protection': {'base_tracked_count': len(paths), 'changed_tracked_paths': changed,
                          'other_tracked_bytes_identical': len(paths) - len(changed),
                          'six_wrappers_exact_source_equal': True, 'held_tail_and_core_call_equal': True,
                          'core_changes_exactly_three_added_lines': True},
    'admission_boundary': 'Internal control review only. Published exact-head reference chain, eight quality shards and expected-head main admission remain owner work.',
    'global_knowledge_sync': 'main@990d7c1 / GLOBAL_KNOWLEDGE_V1'
}
output = OUT.joinpath('review.json')
output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8', newline='\n')
print(json.dumps({'status': report['status'], 'checks': len(checks), 'passed': sum(row['pass'] for row in checks),
                  'report': str(output), 'report_sha256': sha(output.read_bytes()),
                  'source_protection': report['source_protection']}))
if not passed:
    raise SystemExit(1)
