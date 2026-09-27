"""Saved-record-only audit. No scientific module import or numerical oracle."""
from pathlib import Path
from collections import Counter
import ast
import gzip
import hashlib
import json
import sys
import traceback
import zlib

ROOT = Path(__file__).resolve().parent
STAGE = ROOT.parent
BASE = STAGE / 'read_streamed_records.py'
BASE_SHA = '0823b9b2b1410db4fdac1fd3ef88420bd6b61a1e1e16cb6b0fdb23b7daa8e8c7'
NATIVE_READER = STAGE.parent / 'sep27-brc-native-tool-discovery/read_native_port_review.py'
NATIVE_READER_SHA = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
SOURCE_SHA = '656d26f613f14c61542f0a1d2bc8ef3a50d491c1c006ae1fc1493976cb2d3202'
PLAN_SHA = '34a70aab6273482538b303cc6f8ebb7a442fa6d21279d9a6b1687f13bf08a87c'
HELPER_SHA = 'e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b'
INTEGRITY_RAW_SHA = 'a5ec56bfd6423118fa822eeed923d384e38e52e873bb40ac9e34e688702f99a1'
SCHEMA = 'BRC_STREAMED_PUBLIC_CLOCK_V1'  # Frozen shared transport schema.
POSTHOC_SCHEMA = 'BRC_POSTHOC_PUBLIC_CLOCK_DIAGNOSTIC_V1'
METRICS = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
           'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
counts = Counter()
catalog = None


def load_record_functions():
    raw = BASE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA
    names = {'sha', 'hash_file', 'unique_pairs', 'decode', 'canonical', 'same', 'fields',
             'native_schema', 'members', 'Recorded'}
    nodes = [node for node in ast.parse(raw).body
             if isinstance(node, (ast.FunctionDef, ast.ClassDef)) and node.name in names]
    assert {node.name for node in nodes} == names
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(BASE) + '::<pure record definitions>', 'exec'), globals())
    native = NATIVE_READER.read_bytes()
    assert sha(native) == NATIVE_READER_SHA
    nodes = [node for node in ast.parse(native).body if isinstance(node, ast.FunctionDef) and node.name == 'trace']
    assert len(nodes) == 1
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(NATIVE_READER) + '::<trace only>', 'exec'), globals())


def make_reader(directory, summary, N):
    class PosthocRecords(Recorded):
        def __init__(self):
            self.rows = iter(members(directory, summary))
            self.pending = {}
            self.next_ids = Counter()
            self.costs = {}
            self.labels = {}
            self.N = N
            self.two_part_wiring = 0

        def euclid(self, stream, left, right):
            start = self.event('posthoc_euclid_begin', stream=stream, left=left, right=right)['sequence']
            while right:
                row = self.event('posthoc_euclid_step', begin=start, stream=stream, left=left, right=right)
                div = self.op({'stream': stream, 'operation_id': row['operation_id']},
                              'divide', value=left, modulus=right)
                fields(row, quotient=div['quotient'], remainder=div['remainder'])
                assert 0 <= div['remainder'] < right
                left, right = right, div['remainder']
            end = self.event('posthoc_euclid_end', begin=start, value=left)
            return {'value': left, 'producer': end['sequence']}

        def two_part(self, role, value, producer):
            assert value > 0
            initial, shifts = value, []
            while True:
                odd = value & 1
                self.two_part_wiring += 1
                if odd:
                    break
                following = value >> 1
                self.two_part_wiring += 1
                shifts.append({'input': value, 'output': following})
                value = following
            record = {'role': role, 'input': initial, 'producer': producer, 'shifts': shifts,
                      'v2': len(shifts), 'odd_part': value, 'cumulative_bit_wiring': self.two_part_wiring}
            row = self.event('posthoc_two_part', **record)
            record['receipt'] = row['sequence']
            return record

        def grouped_cost(self):
            groups = {}
            for group in ('diagnostic', 'p', 'q'):
                if group == 'diagnostic':
                    names = [s for s in self.costs if s not in ('posthoc_jacobi_p', 'posthoc_jacobi_q')]
                    labels = {}
                else:
                    names = ['posthoc_jacobi_' + group]
                    labels = {names[0]: self.labels[names[0]]}
                streams = {name: {'stream': name, 'stats': {key: self.costs[name][key] for key in METRICS},
                                  'completed_operation_ids': self.next_ids[name],
                                  'durably_committed_operations': self.next_ids[name],
                                  'unwritten_operation_pending': False} for name in names}
                total = {key: sum(self.costs[name][key] for name in names) for key in METRICS}
                groups[group] = {
                    'streams': streams, 'all_arithmetic_totals': total,
                    'production_arithmetic_totals': total, 'validation_arithmetic_totals': {key: 0 for key in METRICS},
                    'jacobi_label_bit_wiring_operations': labels, 'jacobi_label_bit_wiring_total': sum(labels.values()),
                    'native_catalog_admission_counted_separately': True,
                    'host_control_serialization_io_and_resource_monitoring_excluded': True}
            return {'groups': groups,
                    'all_arithmetic_totals': {key: sum(group['all_arithmetic_totals'][key] for group in groups.values()) for key in METRICS},
                    'two_part_label_bit_wiring': self.two_part_wiring,
                    'jacobi_label_bit_wiring': sum(self.labels.values()),
                    'scope': 'All new post-hoc work, separate from blind production and prior input-integrity costs'}
    return PosthocRecords()


def outer(r, blind, p, q):
    orders, decompositions = {}, {}
    for label, value in [('p', p), ('q', q)]:
        orders[label] = {}
        for sign in ('minus', 'plus'):
            row = r.event('posthoc_label_order', label=label, sign=sign, input=value, stream='label_orders')
            op = r.op({'stream': 'label_orders', 'operation_id': row['operation_id']},
                      'compare' if sign == 'minus' else 'add', left=value, right=1)
            if sign == 'minus':
                assert op['relation'] > 0
                order = op['low_difference']
            else:
                order = op['low']
            fields(row, output=order)
            orders[label][sign] = order
            decompositions[label + '_' + sign] = r.two_part(label + '_' + sign, order, row['sequence'])
    crosses = {}
    for psign in ('minus', 'plus'):
        for qsign in ('minus', 'plus'):
            key = psign + '_' + qsign
            item = r.euclid('cross_' + key, orders['p'][psign], orders['q'][qsign])
            item['two_part'] = r.two_part('cross_' + key, item['value'], item['producer'])
            crosses[key] = item
    characters = {}
    global_N = r.N
    for label, modulus in [('p', p), ('q', q)]:
        r.N = modulus
        assert type(modulus) is int and modulus > 5 and modulus & 1
        value, receipt = r.jacobi('posthoc_jacobi_' + label, 5)
        characters[label] = {'jacobi_5': value, 'producer': receipt,
                             'legendre_interpretation_requires_prime_label': True}
    r.N = global_N
    pair = blind['result']['terminal_pair']
    values = {'V_E': pair[0], 'V_E_plus_1': pair[1]}
    for sign in ('identity', 'antipodal'):
        values[sign + '_tau'] = blind['result']['readouts'][sign]['tau']
        values[sign + '_w'] = blind['result']['readouts'][sign]['w']
    projections = {}
    for label, modulus in [('p', p), ('q', q)]:
        stream, projected = 'projection_' + label, {}
        for role, value in values.items():
            row = r.event('posthoc_projection', role=role, label=label, input=value, modulus=modulus, stream=stream)
            div = r.op({'stream': stream, 'operation_id': row['operation_id']}, 'divide', value=value, modulus=modulus)
            fields(row, quotient=div['quotient'], residue=div['remainder'])
            projected[role] = {'residue': div['remainder'], 'producer': row['sequence']}
        projected['identity_return'] = (projected['identity_tau']['residue'] == 0 and projected['identity_w']['residue'] == 0)
        projected['antipodal_return'] = (projected['antipodal_tau']['residue'] == 0 and projected['antipodal_w']['residue'] == 0)
        r.event('posthoc_projected_return', label=label, result=projected)
        projections[label] = projected
    selected = None
    if all(characters[label]['jacobi_5'] in (-1, 1) for label in ('p', 'q')):
        signs = ['minus' if characters[label]['jacobi_5'] == 1 else 'plus' for label in ('p', 'q')]
        selected = signs[0] + '_' + signs[1]
    return {'status': 'COMPLETE_POSTHOC_DIAGNOSTIC', 'saved_public_E': blind['result']['E'],
            'saved_global_characters': blind['result']['characters'], 'orders': orders,
            'order_two_parts': decompositions, 'four_cross_gcds': crosses, 'local_characters': characters,
            'selected_cross_key_if_prime_labels': selected, 'saved_pair_projections': projections,
            'primality_proved': False, 'new_local_power_performed': False, 'blind_search_success_claimed': False,
            'conditional_interpretation': 'The two-prime public-clock theorem requires distinct odd prime p,q. No such primality proof is produced here.'}


def check_binding(summary):
    binding = summary['binding']
    same(binding, decode((ROOT / 'run/STARTED.json').read_bytes()))
    fields(binding, schema=POSTHOC_SCHEMA)
    assert binding['source']['sha256'] == SOURCE_SHA
    assert binding['plan']['sha256'] == PLAN_SHA
    assert binding['helper']['sha256'] == HELPER_SHA
    for name, path in [('source', ROOT / 'postmortem_native.py'), ('plan', ROOT / 'PLAN.md'),
                       ('helper', STAGE / 'streaming_public_clock.py'),
                       ('user_target_confirmation', STAGE / 'USER_TARGET_CONFIRMATION.md')]:
        same(hash_file(path), binding[name])
    same(hash_file(Path(binding['guard_path'])), binding['guard_file'])
    guard = decode(Path(binding['guard_path']).read_bytes())
    same(guard, binding['guard'])
    fields(guard, activity_id='RA-CAAAC604CB513AEA8BBC1DFC', activity_allowed=True,
           persistence_allowed=True, sync_debt_events=[])
    helper_tree = ast.parse((STAGE / 'streaming_public_clock.py').read_bytes())
    maps = [ast.literal_eval(node.value) for node in helper_tree.body if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == 'EXPECTED' for target in node.targets)]
    assert len(maps) == 1
    same(binding['dependencies'], maps[0])
    for name, pin in binding['dependencies'].items():
        assert hash_file(STAGE.parent / name)['sha256'] == pin
    for name, expected in binding['blind_block_files'].items():
        same(hash_file(STAGE / 'runs/block' / name), expected)
    assert set(binding['blind_block_files']) == {'SUMMARY.json', 'STARTED.json', 'EVIDENCE.jsonl.gz', 'MEMBER_INDEX.jsonl'}
    blind = decode((STAGE / 'runs/block/SUMMARY.json').read_bytes())
    fields(blind, execution_status='COMPLETE')
    same(blind['binding'], decode((STAGE / 'runs/block/STARTED.json').read_bytes()))
    same(blind['result'], binding['blind_block_result'])
    assert blind['binding']['source']['sha256'] == HELPER_SHA
    assert blind['result']['status'] == 'COMPLETE_MAIN_OBSERVERS'
    assert blind['binding']['inputs']['k'] == 3
    rawfile = STAGE / 'input_integrity_v2/INPUT_RESULTS.json.gz'
    same(hash_file(rawfile), binding['integrity_input']['gzip'])
    raw = gzip.decompress(rawfile.read_bytes())
    assert sha(raw) == binding['integrity_input']['raw_sha256'] == INTEGRITY_RAW_SHA
    data = decode(raw)
    p, q = data['binding']['inputs']['supplied_p'], data['binding']['inputs']['supplied_q']
    same(binding['disclosed_labels'], {'p': p, 'q': q})
    same(data['binding']['source_sha256'], binding['integrity_input']['source_sha256'])
    assert data['status'] == 'COMPLETE_NATIVE_INPUT_CONSISTENCY_NOT_FACTORING'
    assert data['product_equals_block'] is True
    assert data['product'] == blind['binding']['inputs']['N'] == data['binding']['inputs']['displayed_block']
    operation = data['arithmetic_operations'][data['product_operation']]
    fields(operation, operation='multiply')
    fields(operation['trace'], left=p, right=q, value=data['product'])
    return binding, blind, p, q


def main():
    global catalog
    assert not sys.flags.optimize, 'assertions must be enabled'
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    output = ROOT / 'POSTMORTEM_RECORD_REVIEW.json'
    assert not output.exists() and not output.with_suffix('.FAILED.json').exists(), 'refuse previous audit artifact'
    load_record_functions()
    directory = ROOT / 'run'
    summary = decode((directory / 'SUMMARY.json').read_bytes())
    fields(summary, schema=POSTHOC_SCHEMA, execution_status='COMPLETE')
    assert not any((directory / name).exists() for name in ('FAILED.json', 'FAILED_PENDING_MEMBER.json.gz', 'FAILED_SERIALIZATION.txt'))
    binding, blind, p, q = check_binding(summary)
    r = make_reader(directory, summary, blind['binding']['inputs']['N'])
    r.event('postmortem_binding', postmortem_schema=POSTHOC_SCHEMA, binding=binding)
    admission = r.event('native_catalog_admission')
    catalog = admission['source']['native_adder']['columns']
    assert type(catalog) is list and len(catalog) == 8
    assert all(type(col) is list and len(col) == 2 and all(type(bit) is int and bit in (0, 1) for bit in col) for col in catalog)
    native = admission['all_native_records']
    assert len(native) == 1
    fields(native[0], entrypoint='recurrent_mass_power', states=12, depth=1)
    for name, relative in [('lazy_modular', 'sep26-shor-general/optimization/lazy_modular/lazy_modular.py'),
                           ('sparse_modular', 'sep26-shor-general/sparse/sparse_modular.py'),
                           ('typed_integer_prechecks', 'sep26-shor-general/completion/typed_integer_prechecks.py')]:
        same(admission['source']['files_sha256'][name], binding['dependencies'][relative])
    vendor = STAGE.parent / 'sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py'
    assert hash_file(vendor)['sha256'] == admission['source']['native_adder']['vendor']['sha256']
    result = outer(r, blind, p, q)
    r.event('native_catalog_final', all_native_records=native)
    cost = r.grouped_cost()
    r.event('postmortem_complete', result=result, cost=cost, native_catalog_calls=len(native), postmortem_schema=POSTHOC_SCHEMA)
    assert not r.pending, 'unused primitive record'
    assert next(r.rows, None) is None, 'unexpected trailing records'
    same(summary['result'], result)
    same(summary['cost'], cost)
    same(summary['native_catalog_calls'], len(native))
    assert counts['event_posthoc_euclid_begin'] == counts['event_posthoc_euclid_end'] == 4
    assert counts['event_posthoc_projection'] == 12
    assert counts['event_jacobi_begin'] == counts['event_jacobi_end'] == 2
    assert counts['event_posthoc_two_part'] == 8
    report = {'status': 'PASS_COMPLETE_POSTHOC_SAVED_RECORDS_ONLY', 'reader': hash_file(Path(__file__)),
              'record_definitions_sha256': BASE_SHA, 'native_record_definitions_sha256': NATIVE_READER_SHA,
              'source_sha256': SOURCE_SHA, 'plan_sha256': PLAN_SHA,
              'summary': hash_file(directory / 'SUMMARY.json'), 'evidence': summary['evidence'],
              'member_index': summary['member_index'], 'counts': dict(counts), 'cost': cost, 'result': result,
              'scope': 'All post-hoc member bytes, native cells, typed/Euclid/projection links, Jacobi wiring, eight two-part labels and full accounting. Earlier blind and integrity evidence are source-bound historical inputs, not recomputed.',
              'not_performed': ['scientific import or native rerun', 'host gcd/modulo/product/power reference',
                                'primality proof', 'new blind proposal', 'new local power'],
              'admission': 'shared-context record audit, not independent formal admission'}
    with output.open('x', encoding='utf-8') as stream:
        json.dump(report, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({'status': report['status'], 'counts': report['counts'], 'cost': cost['all_arithmetic_totals'], 'output': str(output)}))


if __name__ == '__main__':
    try:
        main()
    except BaseException:
        with (ROOT / 'POSTMORTEM_RECORD_REVIEW.FAILED.json').open('x', encoding='utf-8') as stream:
            json.dump({'status': 'SAVED_RECORD_AUDIT_FAILED', 'traceback': traceback.format_exc(), 'counts': dict(counts)}, stream, indent=2)
        raise
