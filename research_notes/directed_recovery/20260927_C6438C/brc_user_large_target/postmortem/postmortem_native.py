"""Code-only post-hoc diagnostic; never a blind-search proposal or power run."""
from pathlib import Path
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
import re
import sys
import traceback

ROOT = Path(__file__).resolve().parent
STAGE = ROOT.parent
HELPER = STAGE / 'streaming_public_clock.py'
HELPER_SHA = 'e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b'
INTEGRITY_RAW_SHA = 'a5ec56bfd6423118fa822eeed923d384e38e52e873bb40ac9e34e688702f99a1'
INTEGRITY_SOURCE_SHA = '041032580718b64d2c9645015d04839062d4dca4e7001b1e6387bbe7d7b03e28'
SCHEMA = 'BRC_POSTHOC_PUBLIC_CLOCK_DIAGNOSTIC_V1'
ACTIVITY = 'RA-CAAAC604CB513AEA8BBC1DFC'
RESERVED = ('STARTED.json', 'SUMMARY.json', 'FAILED.json', 'EVIDENCE.jsonl.gz',
            'MEMBER_INDEX.jsonl', 'FAILED_PENDING_MEMBER.json.gz', 'FAILED_SERIALIZATION.txt')


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_hash(path):
    h, length = hashlib.sha256(), 0
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            length += len(block)
            h.update(block)
    return {'bytes': length, 'sha256': h.hexdigest()}


def read_json(path):
    return json.loads(path.read_bytes())


def write_json(path, value):
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        stream.write(json.dumps(value, sort_keys=True, indent=2) + '\n')
        stream.flush()
        os.fsync(stream.fileno())


def completed_block_gate():
    """Integrity gate only, not a replacement for the separate all-digit audit."""
    directory = STAGE / 'runs/block'
    summary, started = read_json(directory / 'SUMMARY.json'), read_json(directory / 'STARTED.json')
    require(summary['execution_status'] == 'COMPLETE', 'block must have completed first')
    require(summary['binding'] == started, 'block binding differs from STARTED')
    require(started['source']['sha256'] == HELPER_SHA, 'unexpected blind source')
    for name, field in [('EVIDENCE.jsonl.gz', 'evidence'), ('MEMBER_INDEX.jsonl', 'member_index')]:
        require(file_hash(directory / name) == summary[field], 'blind complete file mismatch: ' + name)
    position, count, last = 0, 0, None
    with (directory / 'MEMBER_INDEX.jsonl').open('rb') as index:
        for line in index:
            entry = json.loads(line)
            require(entry['sequence'] == count and entry['offset'] == position, 'blind index discontinuity')
            require(type(entry['compressed_bytes']) is int and entry['compressed_bytes'] > 0,
                    'invalid blind member length')
            position += entry['compressed_bytes']
            count += 1
            last = entry
    require(count == summary['member_count'] and position == summary['evidence']['bytes'],
            'blind index extent mismatch')
    require(last is not None and last['kind'] == 'complete_result', 'missing blind terminal record')
    with (directory / 'EVIDENCE.jsonl.gz').open('rb') as stream:
        stream.seek(last['offset'])
        packed = stream.read(last['compressed_bytes'])
    require(digest(packed) == last['compressed_sha256'], 'blind terminal compressed hash')
    raw = gzip.decompress(packed)
    require(len(raw) == last['raw_bytes'] and digest(raw) == last['raw_sha256'], 'blind terminal raw hash')
    terminal = json.loads(raw)
    require(terminal['sequence'] == last['sequence'] and terminal['kind'] == 'complete_result',
            'blind terminal sequence')
    require(terminal['result'] == summary['result'] and terminal['cost'] == summary['cost'],
            'blind terminal/summary mismatch')
    require(summary['result']['status'] == 'COMPLETE_MAIN_OBSERVERS', 'diagnostic needs saved main-clock pair')
    require(started['inputs']['k'] == 3 and summary['result']['setup']['status'] == 'REGULAR',
            'this diagnostic is restricted to the fixed regular k=3 block test')
    return summary, {name: file_hash(directory / name) for name in
                     ('SUMMARY.json', 'STARTED.json', 'EVIDENCE.jsonl.gz', 'MEMBER_INDEX.jsonl')}


def isolated_labels_after_gate(blind):
    """Read supplied labels only after the blind result is durably complete."""
    directory = STAGE / 'input_integrity_v2'
    raw = gzip.decompress((directory / 'INPUT_RESULTS.json.gz').read_bytes())
    require(digest(raw) == INTEGRITY_RAW_SHA, 'input-integrity raw pin')
    data = json.loads(raw)
    require(data['binding']['source_sha256'] == INTEGRITY_SOURCE_SHA, 'input-integrity source pin')
    require(data['status'] == 'COMPLETE_NATIVE_INPUT_CONSISTENCY_NOT_FACTORING', 'integrity status')
    inputs = data['binding']['inputs']
    p, q = inputs['supplied_p'], inputs['supplied_q']
    require(type(p) is int and type(q) is int and p > 5 and q > 5, 'diagnostic label range')
    require(data['product_equals_block'] is True, 'no certified block identity')
    require(data['product'] == blind['binding']['inputs']['N'] == inputs['displayed_block'],
            'factor labels are not the recorded block labels')
    operation = data['arithmetic_operations'][data['product_operation']]
    require(operation['operation'] == 'multiply', 'missing saved multiplication')
    require((operation['trace']['left'], operation['trace']['right'], operation['trace']['value']) ==
            (p, q, data['product']), 'saved p*q binding')
    return p, q, {'raw_sha256': digest(raw), 'gzip': file_hash(directory / 'INPUT_RESULTS.json.gz'),
                  'source_sha256': INTEGRITY_SOURCE_SHA,
                  'scope': 'previous source-bound typed multiplication; no new primality or multiplication run'}


class Diagnostic:
    def __init__(self, helper, lm, sink, N, p, q):
        self.helper, self.sink = helper, sink
        self.main = helper.Work(lm, sink, N)
        self.local = {'p': helper.Work(lm, sink, p), 'q': helper.Work(lm, sink, q)}
        self.stage = 'initialized'
        self.state = {}
        self.valuation_wiring = 0

    def euclid(self, name, left, right):
        ar = self.main.ar(name)
        begin = self.sink.emit('posthoc_euclid_begin', stream=name, left=left, right=right)
        while right:
            quotient, remainder, op_id = ar.divide(left, right)
            require(0 <= remainder < right, 'posthoc Euclid invariant')
            self.sink.emit('posthoc_euclid_step', begin=begin, stream=name, left=left, right=right,
                           quotient=quotient, remainder=remainder, operation_id=op_id)
            left, right = right, remainder
        end = self.sink.emit('posthoc_euclid_end', begin=begin, value=left)
        return {'value': left, 'producer': end}

    def two_part(self, role, value, producer):
        require(value > 0, 'positive two-part label')
        initial, shifts = value, []
        while True:
            odd = value & 1
            self.valuation_wiring += 1
            if odd:
                break
            following = value >> 1
            self.valuation_wiring += 1
            shifts.append({'input': value, 'output': following})
            value = following
        record = {'role': role, 'input': initial, 'producer': producer, 'shifts': shifts,
                  'v2': len(shifts), 'odd_part': value,
                  'cumulative_bit_wiring': self.valuation_wiring}
        record['receipt'] = self.sink.emit('posthoc_two_part', **record)
        return record

    def compute(self, blind, p, q):
        self.stage = 'public_label_orders'
        orders, decompositions = {}, {}
        for label, value in [('p', p), ('q', q)]:
            ar = self.main.ar('label_orders')
            relation, minus, mid = ar.compare(value, 1)
            require(relation > 0, 'positive label-minus-one')
            plus, pid = ar.add(value, 1)
            orders[label] = {'minus': minus, 'plus': plus}
            for sign, order, op_id in [('minus', minus, mid), ('plus', plus, pid)]:
                event = self.sink.emit('posthoc_label_order', label=label, sign=sign, input=value,
                                       output=order, stream='label_orders', operation_id=op_id)
                decompositions[label + '_' + sign] = self.two_part(label + '_' + sign, order, event)
        self.stage = 'four_cross_gcds'
        crosses = {}
        for psign in ('minus', 'plus'):
            for qsign in ('minus', 'plus'):
                key = psign + '_' + qsign
                item = self.euclid('cross_' + key, orders['p'][psign], orders['q'][qsign])
                item['two_part'] = self.two_part('cross_' + key, item['value'], item['producer'])
                crosses[key] = item
        self.state.update(orders=orders, crosses=crosses)
        self.stage = 'local_characters'
        characters = {}
        for label in ('p', 'q'):
            value, receipt = self.helper.jacobi_stream(self.local[label], 'posthoc_jacobi_' + label, 5)
            characters[label] = {'jacobi_5': value, 'producer': receipt,
                                 'legendre_interpretation_requires_prime_label': True}
        self.state['characters'] = characters
        self.stage = 'saved_pair_projection'
        pair = blind['result']['terminal_pair']
        values = {'V_E': pair[0], 'V_E_plus_1': pair[1]}
        for sign in ('identity', 'antipodal'):
            values[sign + '_tau'] = blind['result']['readouts'][sign]['tau']
            values[sign + '_w'] = blind['result']['readouts'][sign]['w']
        projections = {}
        for label, modulus in [('p', p), ('q', q)]:
            stream = 'projection_' + label
            projected = {}
            for role, value in values.items():
                quotient, remainder, op_id = self.main.ar(stream).divide(value, modulus)
                event = self.sink.emit('posthoc_projection', role=role, label=label,
                                       input=value, modulus=modulus, quotient=quotient,
                                       residue=remainder, stream=stream, operation_id=op_id)
                projected[role] = {'residue': remainder, 'producer': event}
            projected['identity_return'] = (projected['identity_tau']['residue'] == 0 and
                                             projected['identity_w']['residue'] == 0)
            projected['antipodal_return'] = (projected['antipodal_tau']['residue'] == 0 and
                                              projected['antipodal_w']['residue'] == 0)
            self.sink.emit('posthoc_projected_return', label=label, result=projected)
            projections[label] = projected
        self.state['projections'] = projections
        selected = None
        if all(characters[label]['jacobi_5'] in (-1, 1) for label in ('p', 'q')):
            signs = ['minus' if characters[label]['jacobi_5'] == 1 else 'plus' for label in ('p', 'q')]
            selected = signs[0] + '_' + signs[1]
        result = {'status': 'COMPLETE_POSTHOC_DIAGNOSTIC', 'saved_public_E': blind['result']['E'],
                  'saved_global_characters': blind['result']['characters'], 'orders': orders,
                  'order_two_parts': decompositions, 'four_cross_gcds': crosses,
                  'local_characters': characters, 'selected_cross_key_if_prime_labels': selected,
                  'saved_pair_projections': projections, 'primality_proved': False,
                  'new_local_power_performed': False, 'blind_search_success_claimed': False,
                  'conditional_interpretation': 'The two-prime public-clock theorem requires distinct odd prime p,q. No such primality proof is produced here.'}
        self.stage = 'complete'
        return result

    def stats(self):
        groups = {'diagnostic': self.main.stats(), **{k: w.stats() for k, w in self.local.items()}}
        keys = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
                'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
        total = {key: sum(group['all_arithmetic_totals'][key] for group in groups.values()) for key in keys}
        return {'groups': groups, 'all_arithmetic_totals': total,
                'two_part_label_bit_wiring': self.valuation_wiring,
                'jacobi_label_bit_wiring': sum(group['jacobi_label_bit_wiring_total'] for group in groups.values()),
                'scope': 'All new post-hoc work, separate from blind production and prior input-integrity costs'}


def run(args):
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    output = ROOT / 'run'
    output.mkdir(exist_ok=True)
    for name in RESERVED:
        require(not (output / name).exists(), 'refuse existing diagnostic artifact: ' + name)
    require(re.fullmatch('[0-9a-f]{64}', args.plan_sha256) is not None, 'plan pin format')
    require(re.fullmatch('[0-9a-f]{40}', args.global_knowledge_sha) is not None, 'knowledge pin format')
    require(file_hash(ROOT / 'PLAN.md')['sha256'] == args.plan_sha256, 'plan pin')
    guard_path = Path(args.guard_file).resolve()
    guard = read_json(guard_path)
    require(guard['activity_id'] == ACTIVITY and guard['activity_allowed'] is True and
            guard['persistence_allowed'] is True and guard['sync_debt_events'] == [], 'guard not clear')
    require(guard['record_sha256'] == args.guard_record_sha256, 'guard record pin')
    require(file_hash(HELPER)['sha256'] == HELPER_SHA, 'frozen helper pin')
    blind, blind_files = completed_block_gate()
    p, q, integrity = isolated_labels_after_gate(blind)
    spec = importlib.util.spec_from_file_location('postmortem_frozen_streaming_helper', HELPER)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)  # Verified module top level is stdlib-only.
    helper.check_dependencies()
    binding = {'schema': SCHEMA, 'purpose': 'post-hoc diagnosis with disclosed labels; never a blind trial',
               'source': file_hash(Path(__file__)), 'plan': file_hash(ROOT / 'PLAN.md'),
               'helper': file_hash(HELPER), 'blind_block_files': blind_files,
               'blind_block_result': blind['result'], 'integrity_input': integrity,
               'disclosed_labels': {'p': p, 'q': q}, 'dependencies': helper.EXPECTED,
               'guard_path': str(guard_path), 'guard_file': file_hash(guard_path), 'guard': guard,
               'coordinator_actual_knowledge_sha': args.global_knowledge_sha,
               'user_target_confirmation': file_hash(STAGE / 'USER_TARGET_CONFIRMATION.md'),
               'author_review_context_sha': 'b3047603607cebcbd3f39e7028bf707f199c3f48'}
    write_json(output / 'STARTED.json', binding)
    sink = lm = diagnostic = None
    try:
        sink = helper.EvidenceSink(output)
        sink.emit('postmortem_binding', postmortem_schema=SCHEMA, binding=binding)
        lm = helper.load_arithmetic()
        native = lm.source_binding()
        sink.emit('native_catalog_admission', source=native, all_native_records=lm.CALLS)
        diagnostic = Diagnostic(helper, lm, sink, blind['binding']['inputs']['N'], p, q)
        result = diagnostic.compute(blind, p, q)
        for path, expected in [(Path(__file__), binding['source']), (ROOT / 'PLAN.md', binding['plan']),
                               (HELPER, binding['helper']), (guard_path, binding['guard_file'])]:
            require(file_hash(path) == expected, 'diagnostic binding changed: ' + str(path))
        for name, expected in blind_files.items():
            require(file_hash(STAGE / 'runs/block' / name) == expected, 'blind artifact changed: ' + name)
        require(file_hash(STAGE / 'USER_TARGET_CONFIRMATION.md') == binding['user_target_confirmation'],
                'target confirmation changed')
        require(file_hash(STAGE / 'input_integrity_v2/INPUT_RESULTS.json.gz') == integrity['gzip'],
                'isolated integrity evidence changed')
        helper.check_dependencies()
        sink.emit('native_catalog_final', all_native_records=lm.CALLS)
        sink.emit('postmortem_complete', result=result, cost=diagnostic.stats(),
                  native_catalog_calls=len(lm.CALLS), postmortem_schema=SCHEMA)
        members, decoded = sink.next_sequence, sink.raw_bytes
        sink.close()
        summary = {'schema': SCHEMA, 'execution_status': 'COMPLETE', 'binding': binding,
                   'result': result, 'cost': diagnostic.stats(), 'native_catalog_calls': len(lm.CALLS),
                   'member_count': members, 'decoded_bytes': decoded,
                   'evidence': file_hash(output / 'EVIDENCE.jsonl.gz'),
                   'member_index': file_hash(output / 'MEMBER_INDEX.jsonl')}
        write_json(output / 'SUMMARY.json', summary)
        print(json.dumps(summary, sort_keys=True))
    except BaseException:
        failure = {'schema': SCHEMA, 'execution_status': 'FAILED_NOT_RESUMABLE', 'binding': binding,
                   'traceback': traceback.format_exc(), 'stage': None if diagnostic is None else diagnostic.stage,
                   'state': None if diagnostic is None else diagnostic.state,
                   'cost': None if diagnostic is None else diagnostic.stats(),
                   'catalog_records': [] if lm is None else lm.CALLS,
                   'committed_members': None if sink is None else sink.next_sequence}
        if sink is not None:
            sink.close()
        try:
            if sink is not None and sink.pending is not None:
                with (output / 'FAILED_PENDING_MEMBER.json.gz').open('xb') as raw:
                    with gzip.GzipFile(fileobj=raw, mode='wb', filename='', mtime=0) as gz:
                        for chunk in helper.json_chunks(sink.pending):
                            gz.write(chunk)
                    raw.flush()
                    os.fsync(raw.fileno())
            failure['preserved_files'] = {name: file_hash(output / name) for name in
                                          ('EVIDENCE.jsonl.gz', 'MEMBER_INDEX.jsonl', 'FAILED_PENDING_MEMBER.json.gz')
                                          if (output / name).exists()}
            write_json(output / 'FAILED.json', failure)
        except BaseException:
            with (output / 'FAILED_SERIALIZATION.txt').open('xb') as stream:
                stream.write((failure['traceback'] + '\nFailure serialization:\n' + traceback.format_exc()).encode())
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--guard-file', required=True)
    parser.add_argument('--guard-record-sha256', required=True)
    parser.add_argument('--global-knowledge-sha', required=True)
    run(parser.parse_args())
