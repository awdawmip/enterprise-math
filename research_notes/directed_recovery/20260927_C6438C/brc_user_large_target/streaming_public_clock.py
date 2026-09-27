"""Code-only candidate: streamed actual typed public-clock main observers.

Importing this module loads stdlib only. Scientific dependencies are loaded by
run(), after exact input/plan/guard binding and the exclusive STARTED marker.
"""
from pathlib import Path
from fractions import Fraction
import argparse
import gzip
import hashlib
import json
import os
import re
import sys
import traceback

ROOT = Path(__file__).resolve().parent
TEMP = ROOT.parent
SCHEMA = 'BRC_STREAMED_PUBLIC_CLOCK_V1'
ACTIVITY = 'RA-CAAAC604CB513AEA8BBC1DFC'
EXPECTED = {
    'sep26-shor-general/optimization/lazy_modular/lazy_modular.py':
        '08df3595a2a56dc2501bb481828093481bf76e4ac53c8b966990d233fefac1e4',
    'sep26-shor-general/sparse/sparse_modular.py':
        'fd9cbb019418a3c00890ba6e8cca5760e7e4d792bfd7b48306a71a66de301c46',
    'sep26-shor-general/completion/typed_integer_prechecks.py':
        '0a817aa8124cceb5440233d543073dae71de6ac1d0d4e5d50f4ee2b4808d99eb',
    'sep27-qft-research/character_certificates/typed_jacobi.py':
        'ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402',
    'sep27-brc-adjacent-trace/adjacent_trace.py':
        'd1b0d497ecf8c028e6f4cec8b8322f47d30fa2437c2828825bd79f727d3dda87',
    'sep27-brc-adjacent-trace/PUBLIC_JACOBI_CLOCK_FIBERS.md':
        'd3fbce534cc26e41146242cc97a7527b92054fa67eddae50fd7b15854094c3e9',
    'sep27-brc-adjacent-trace/CONIC_RESIDUAL_COCYCLE.md':
        '2bda2beb4ef90fbc93078c1c52efe1b23872379cca3b53cdd1414a550cddd491',
    'sep27-brc-hbw-free-trace/TRANSLATED_TRACE_MARK.md':
        'a3562a0b3151c86a7d5c1767af876daafa245ea7426da7dc387c70f0db9f0c6c',
}
RESERVED = ('STARTED.json', 'EVIDENCE.jsonl.gz', 'MEMBER_INDEX.jsonl',
            'SUMMARY.json', 'FAILED.json', 'FAILED_PENDING_MEMBER.json.gz',
            'FAILED_SERIALIZATION.txt')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def plain(value):
    if isinstance(value, Fraction):
        return {'numerator': value.numerator, 'denominator': value.denominator}
    raise TypeError(type(value).__name__)


def json_chunks(value):
    encoder = json.JSONEncoder(sort_keys=True, separators=(',', ':'),
                               ensure_ascii=True, allow_nan=False, default=plain)
    buffer = bytearray()
    for part in encoder.iterencode(value):
        buffer.extend(part.encode('utf-8'))
        if len(buffer) >= 65536:
            yield bytes(buffer)
            buffer.clear()
    buffer.extend(b'\n')
    if buffer:
        yield bytes(buffer)


def write_new_json(path, value):
    with path.open('xb') as stream:
        for chunk in json_chunks(value):
            stream.write(chunk)
        stream.flush()
        os.fsync(stream.fileno())


def file_hash(path):
    digest = hashlib.sha256()
    size = 0
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            size += len(chunk)
            digest.update(chunk)
    return {'bytes': size, 'sha256': digest.hexdigest()}


class MemberWriter:
    """Hash only the bytes emitted by one completed gzip member."""
    def __init__(self, raw):
        self.raw = raw
        self.digest = hashlib.sha256()
        self.bytes = 0

    def write(self, data):
        written = self.raw.write(data)
        require(written == len(data), 'short evidence write')
        self.digest.update(data)
        self.bytes += written
        return written

    def flush(self):
        self.raw.flush()

    def tell(self):
        return self.raw.tell()


class EvidenceSink:
    """One JSON record per independently closed, durable gzip member.

    The data member is fsynced before its index line is committed. A crash
    between them may leave a valid unindexed member; it never licenses claiming
    the missing index was committed. No old bytes are overwritten or truncated.
    """
    def __init__(self, directory):
        self.directory = directory
        self.raw = (directory / 'EVIDENCE.jsonl.gz').open('xb')
        try:
            self.index = (directory / 'MEMBER_INDEX.jsonl').open('xb')
        except BaseException:
            self.raw.close()
            raise
        self.next_sequence = 0
        self.raw_bytes = 0
        self.poisoned = False
        self.pending = None

    def emit(self, kind, **payload):
        require(not self.poisoned, 'evidence sink failed; no continuing writes')
        seq = self.next_sequence
        record = {'schema': SCHEMA, 'sequence': seq, 'kind': kind, **payload}
        self.pending = record
        start = self.raw.tell()
        writer = MemberWriter(self.raw)
        raw_hash, raw_bytes = hashlib.sha256(), 0
        try:
            with gzip.GzipFile(fileobj=writer, mode='wb', filename='', mtime=0,
                               compresslevel=6) as compressed:
                for chunk in json_chunks(record):
                    raw_hash.update(chunk)
                    raw_bytes += len(chunk)
                    compressed.write(chunk)
            self.raw.flush()
            os.fsync(self.raw.fileno())
            entry = {'sequence': seq, 'kind': kind, 'offset': start,
                     'compressed_bytes': writer.bytes,
                     'compressed_sha256': writer.digest.hexdigest(),
                     'raw_bytes': raw_bytes, 'raw_sha256': raw_hash.hexdigest()}
            if kind == 'typed_operation':
                entry.update(stream=payload['stream'], operation_id=payload['operation_id'])
            for chunk in json_chunks(entry):
                self.index.write(chunk)
            self.index.flush()
            os.fsync(self.index.fileno())
        except BaseException:
            self.poisoned = True
            raise
        self.next_sequence += 1
        self.raw_bytes += raw_bytes
        self.pending = None
        return seq

    def close(self):
        for stream in (self.raw, self.index):
            try:
                stream.close()
            except BaseException:
                pass


def streaming_arithmetic_class(lm):
    """Reuse scientific operations literally; change only receipt retention."""
    class StreamingArithmetic(lm.Arithmetic):
        def __init__(self, name, sink):
            super().__init__()
            del self.operations  # No accumulating parent list or reusable len-ID.
            self.name, self.sink = name, sink
            self.next_operation_id = 0
            self.committed_operations = 0
            self.pending_operation = None

        def _retain(self, operation, trace, calls_before):
            op_id = self.next_operation_id
            self.next_operation_id += 1
            cost = lm.trace_cost(trace)
            if operation == 'add':
                cost['host_bit_length_calls_in_arithmetic'] += 2
            self.stats['typed_operations'] += 1
            for key, value in cost.items():
                self.stats[key] += value
            delta_calls = len(lm.CALLS) - calls_before
            self.stats['native_kernel_calls_delta'] += delta_calls
            self.pending_operation = {'stream': self.name, 'operation_id': op_id,
                                      'operation': operation, 'trace': trace,
                                      'cost': cost, 'native_kernel_calls_delta': delta_calls}
            self.sink.emit('typed_operation', **self.pending_operation)
            self.committed_operations += 1
            self.pending_operation = None
            return op_id

        def summary(self):
            return {'stream': self.name, 'stats': dict(self.stats),
                    'completed_operation_ids': self.next_operation_id,
                    'durably_committed_operations': self.committed_operations,
                    'unwritten_operation_pending': self.pending_operation is not None}
    return StreamingArithmetic


class Work:
    def __init__(self, lm, sink, N):
        self.lm, self.sink, self.N = lm, sink, N
        self.arithmetic_type = streaming_arithmetic_class(lm)
        self.streams = {}
        self.stage = 'initialized'
        self.state = {}
        self.label_cost = {}

    def ar(self, name):
        if name not in self.streams:
            self.streams[name] = self.arithmetic_type(name, self.sink)
        return self.streams[name]

    def link(self, stream, op_id):
        return {'stream': stream, 'operation_id': op_id}

    def addmod(self, stream, role, x, y):
        ar = self.ar(stream)
        total, add_id = ar.add(x, y)
        quotient, value, div_id = ar.divide(total, self.N)
        seq = self.sink.emit('addmod', role=role, inputs=[x, y], N=self.N,
                             add=self.link(stream, add_id), division=self.link(stream, div_id),
                             quotient=quotient, output=value)
        return value, seq

    def submod(self, stream, role, x, y):
        value, links = self.ar(stream).modsubtract(x, y, self.N)
        seq = self.sink.emit('submod', stream=stream, role=role, inputs=[x, y],
                             N=self.N, operations=links, output=value)
        return value, seq

    def modmul(self, stream, role, x, y):
        value, links = self.ar(stream).modmul(x, y, self.N)
        seq = self.sink.emit('modmul', stream=stream, role=role, inputs=[x, y],
                             N=self.N, operations=links, output=value)
        return value, seq

    def gcd(self, stream, role, values):
        current = self.N
        start = self.sink.emit('common_gcd_begin', stream=stream, role=role,
                               N=self.N, coordinates=list(values))
        for position, coordinate in enumerate(values):
            left, right = current, coordinate
            while right:
                quotient, remainder, op_id = self.ar(stream).divide(left, right)
                require(0 <= remainder < right, 'Euclid remainder invariant')
                self.sink.emit('gcd_step', begin=start, coordinate_index=position,
                               left=left, right=right, quotient=quotient,
                               remainder=remainder, division=self.link(stream, op_id))
                left, right = right, remainder
            current = left
            self.sink.emit('gcd_coordinate_done', begin=start, coordinate_index=position,
                           output=current)
        seq = self.sink.emit('common_gcd_end', begin=start, value=current)
        return current, seq

    def factor(self, divisor, producer):
        if divisor == 1:
            return {'class': 'UNIT', 'divisor': divisor, 'producer': producer}
        if divisor == self.N:
            return {'class': 'SATURATED', 'divisor': divisor, 'producer': producer}
        require(1 < divisor < self.N, 'invalid observed divisor')
        quotient, remainder, op_id = self.ar('factor_division').divide(self.N, divisor)
        require(remainder == 0 and 1 < quotient < self.N, 'proper-factor division failed')
        record = {'class': 'PROPER_FACTOR', 'divisor': divisor, 'cofactor': quotient,
                  'remainder': remainder, 'producer': producer,
                  'division': self.link('factor_division', op_id)}
        record['receipt'] = self.sink.emit('proper_factor_certificate', **record)
        return record

    def stats(self):
        streams = {name: ar.summary() for name, ar in self.streams.items()}
        keys = ('typed_operations', 'adder_digit_replays',
                'host_bit_wiring_operations', 'host_bit_length_calls_in_arithmetic',
                'native_kernel_calls_delta')
        totals = {key: sum(ar.stats[key] for ar in self.streams.values()) for key in keys}
        validation = dict(self.streams['validation'].stats) if 'validation' in self.streams else {
            key: 0 for key in keys}
        production = {key: totals[key] - validation[key] for key in keys}
        return {'streams': streams, 'all_arithmetic_totals': totals,
                'production_arithmetic_totals': production,
                'validation_arithmetic_totals': validation,
                'jacobi_label_bit_wiring_operations': dict(self.label_cost),
                'jacobi_label_bit_wiring_total': sum(self.label_cost.values()),
                'native_catalog_admission_counted_separately': True,
                'host_control_serialization_io_and_resource_monitoring_excluded': True}


def jacobi_stream(work, stream, numerator):
    """Explicit streamed version of the bound generic algorithm, no monkeypatch.

    Our admitted numerators are nonnegative principal residues; the old generic
    negative-numerator extension is not part of this wrapper's input domain.
    """
    require(type(numerator) is int and 0 <= numerator < work.N, 'Jacobi principal numerator')
    ar = work.ar(stream)
    wiring = 1  # denominator oddness label, as in the generic primitive
    require(work.N & 1, 'Jacobi denominator is odd')
    work.label_cost[stream] = wiring
    quotient, residue, div_id = ar.divide(numerator, work.N)
    start = work.sink.emit('jacobi_begin', stream=stream, numerator=numerator,
                           denominator=work.N, initial_quotient=quotient, initial_residue=residue,
                           division=work.link(stream, div_id), label_cost_so_far=wiring)
    x, n, sign = residue, work.N, 1
    work.label_cost[stream] = wiring
    while x:
        before_x, before_n, before_sign = x, n, sign
        shifts = []
        while True:
            odd = x & 1
            wiring += 1
            work.label_cost[stream] = wiring
            if odd:
                break
            following = x >> 1
            wiring += 1
            work.label_cost[stream] = wiring
            shifts.append({'input': x, 'output': following})
            x = following
        n_mod8, exponent_parity = n & 7, len(shifts) & 1
        x_mod4, n_mod4 = x & 3, n & 3
        wiring += 4
        work.label_cost[stream] = wiring
        two_flip = exponent_parity == 1 and n_mod8 in (3, 5)
        reciprocal_flip = x_mod4 == 3 and n_mod4 == 3
        if two_flip:
            sign = -sign
        if reciprocal_flip:
            sign = -sign
        # Persist label work even if the subsequent primitive does not return.
        labels = work.sink.emit('jacobi_labels', begin=start, input_numerator=before_x,
                                input_denominator=before_n, input_sign=before_sign,
                                factor_two_shifts=shifts, odd_numerator=x,
                                denominator_mod8=n_mod8, numerator_mod4=x_mod4,
                                denominator_mod4=n_mod4, exponent_parity=exponent_parity,
                                two_flip=two_flip, reciprocal_flip=reciprocal_flip,
                                output_sign=sign, cumulative_label_wiring=wiring)
        quotient, remainder, div_id = ar.divide(n, x)
        require(0 <= remainder < x, 'Jacobi remainder invariant')
        work.sink.emit('jacobi_step', begin=start, labels=labels, numerator=n, denominator=x,
                       quotient=quotient, remainder=remainder, division=work.link(stream, div_id))
        n, x = x, remainder
    value = sign if n == 1 else 0
    seq = work.sink.emit('jacobi_end', begin=start, value=value, terminal_gcd=n,
                         terminal_sign=sign, label_wiring=wiring)
    return value, seq


def setup(work, k):
    work.stage = 'setup'
    quotient, parity, op_id = work.ar('setup').divide(work.N, 2)
    work.sink.emit('odd_modulus_check', N=work.N, quotient=quotient, remainder=parity,
                   division=work.link('setup', op_id))
    require(parity == 1, 'odd modulus required')
    two, _ = work.addmod('setup', 'two', 1, 1)
    four, _ = work.addmod('setup', 'four', two, two)
    k2, _ = work.modmul('setup', 'k_square', k, k)
    delta, delta_link = work.submod('setup', 'discriminant', k2, four)
    gcd, gcd_link = work.gcd('setup_gcd', 'discriminant_gcd', [delta])
    result = {'k': k, 'two': two, 'four': four, 'delta': delta,
              'delta_producer': delta_link, 'gcd': gcd, 'gcd_producer': gcd_link}
    result['setup_factor'] = work.factor(gcd, gcd_link)
    result['status'] = 'REGULAR' if gcd == 1 else 'SETUP_FACTOR' if gcd < work.N else 'DEGENERATE'
    work.sink.emit('setup_result', result=result)
    return result


def adjacent_power(work, parameters, E):
    bits = format(E, 'b')
    pair = [parameters['two'], parameters['k']]
    work.sink.emit('adjacent_power_begin', E=E, public_bits=bits, initial=pair)
    work.state.update(E=E, pair=list(pair), completed_bits=0)
    for index, bit in enumerate(bits):
        work.stage = 'power_bit_' + str(index)
        before = list(pair)
        work.sink.emit('adjacent_bit_begin', bit_index=index, bit=bit, before=before)
        product, product_link = work.modmul('power', 'cross', pair[0], pair[1])
        odd, odd_link = work.submod('power', 'odd_trace', product, parameters['k'])
        selected = pair[0] if bit == '0' else pair[1]
        square, square_link = work.modmul('power', 'selected_square', selected, selected)
        even, even_link = work.submod('power', 'even_trace', square, parameters['two'])
        pair = [even, odd] if bit == '0' else [odd, even]
        work.sink.emit('adjacent_bit_end', bit_index=index, bit=bit, before=before, after=pair,
                       product=product_link, odd=odd_link, square=square_link, even=even_link)
        work.state.update(pair=list(pair), completed_bits=index + 1)
    work.sink.emit('adjacent_power_end', pair=pair, bits=len(bits),
                   multiplications_per_bit=2, orientation='ordered; no folding')
    return pair


def residual_validation(work, parameters, pair):
    """Paid consistency check; chronology is still required for a power claim."""
    work.stage = 'terminal_conic_validation'
    v, w = pair
    v2, _ = work.modmul('validation', 'v_square', v, v)
    w2, _ = work.modmul('validation', 'w_square', w, w)
    vw, _ = work.modmul('validation', 'v_times_w', v, w)
    kvw, _ = work.modmul('validation', 'k_times_vw', parameters['k'], vw)
    total, _ = work.addmod('validation', 'v2_plus_w2', v2, w2)
    total, _ = work.submod('validation', 'subtract_kvw', total, kvw)
    defect, link = work.addmod('validation', 'add_discriminant', total, parameters['delta'])
    work.sink.emit('terminal_conic_result', defect=defect, producer=link,
                   history_certificate_sufficient=False)
    require(defect == 0, 'terminal conic consistency failed')
    return {'defect': defect, 'producer': link,
            'scope': 'consistency only; initial state and every typed bit step remain required'}


def main_observers(work, parameters, pair):
    result = {}
    for label in ('identity', 'antipodal'):
        work.stage = label + '_main_observer'
        if label == 'identity':
            tau, tl = work.submod('expressions', label + '_tau', pair[0], parameters['two'])
            w, wl = work.submod('expressions', label + '_w', pair[1], parameters['k'])
        else:
            tau, tl = work.addmod('expressions', label + '_tau', pair[0], parameters['two'])
            w, wl = work.addmod('expressions', label + '_w', pair[1], parameters['k'])
        divisor, gl = work.gcd('main_gcd', label, [tau, w])
        factor = work.factor(divisor, gl)
        item = {'tau': tau, 'w': w, 'expression_producers': [tl, wl],
                'joint_divisor': divisor, 'joint_producer': gl, 'factor_certificate': factor}
        work.sink.emit('signed_main_result', label=label, result=item)
        result[label] = item
        work.state['readouts'] = dict(result)
    return result


def compute(work, k):
    parameters = setup(work, k)
    work.state['setup'] = parameters
    if parameters['status'] != 'REGULAR':
        return {'status': parameters['status'], 'setup': parameters,
                'characters_and_clock_evaluated': False}
    work.stage = 'dual_characters'
    jd, jd_link = jacobi_stream(work, 'jacobi_delta', parameters['delta'])
    kplus, plus_link = work.addmod('character_inputs', 'k_plus_two', k, parameters['two'])
    je, je_link = jacobi_stream(work, 'jacobi_plus', kplus)
    require(jd in (-1, 1) and je in (-1, 1), 'regular character must be nonzero')
    work.sink.emit('dual_character_result', j_delta=jd, j_plus=je,
                   delta_producer=parameters['delta_producer'], plus_producer=plus_link,
                   jacobi_receipts=[jd_link, je_link], rejected_by_filter=False)
    work.stage = 'public_clock'
    if jd == -1:
        E, clock_id = work.ar('clock').add(work.N, 1)
        clock_operation = 'add'
    else:
        relation, E, clock_id = work.ar('clock').compare(work.N, 1)
        require(relation > 0, 'positive public-clock subtraction')
        clock_operation = 'compare_low_difference'
    work.sink.emit('public_clock', N=work.N, j_delta=jd, E=E,
                   operation=clock_operation, producer=work.link('clock', clock_id))
    work.state.update(characters={'j_delta': jd, 'j_plus': je}, E=E)
    pair = adjacent_power(work, parameters, E)
    validation = residual_validation(work, parameters, pair)
    readouts = main_observers(work, parameters, pair)
    return {'status': 'COMPLETE_MAIN_OBSERVERS', 'setup': parameters,
            'characters': {'j_delta': jd, 'j_plus': je}, 'E': E, 'terminal_pair': pair,
            'validation': validation, 'readouts': readouts,
            'factor_or_order_input': False, 'second_clock_evaluated': False,
            'rate_or_shor_completion_claimed': False}


def check_dependencies():
    for relative, expected in EXPECTED.items():
        require(file_hash(TEMP / relative)['sha256'] == expected, 'dependency mismatch: ' + relative)


def load_arithmetic():
    path = TEMP / 'sep26-shor-general/optimization/lazy_modular'
    sys.path.insert(0, str(path))
    import lazy_modular as lm
    require(Path(lm.__file__).resolve() == (path / 'lazy_modular.py').resolve(), 'wrong module object')
    require(file_hash(Path(lm.sparse.__file__))['sha256'] == EXPECTED[
        'sep26-shor-general/sparse/sparse_modular.py'], 'loaded sparse source mismatch')
    require(file_hash(Path(lm.typed.__file__))['sha256'] == EXPECTED[
        'sep26-shor-general/completion/typed_integer_prechecks.py'], 'loaded typed source mismatch')
    return lm


def parse_inputs(path):
    data = json.loads(path.read_bytes())
    require(type(data) is dict and set(data) in ({'N'}, {'N', 'k'}),
            'input must contain only public decimal N and optional public decimal k')
    values = {}
    for key, text in (('N', data['N']), ('k', data.get('k', '3'))):
        require(type(text) is str and re.fullmatch(r'0|[1-9][0-9]*', text) is not None,
                'canonical unsigned decimal string required: ' + key)
        values[key] = int(text)
    require(values['N'] > 2 and 0 <= values['k'] < values['N'], 'input range')
    return values


def runtime_binding(args):
    require(re.fullmatch('[0-9a-f]{64}', args.guard_record_sha256) is not None, 'guard record pin')
    require(re.fullmatch('[0-9a-f]{40}', args.global_knowledge_sha) is not None, 'knowledge pin')
    require(re.fullmatch('[0-9a-f]{64}', args.plan_sha256) is not None, 'frozen plan pin')
    output = Path(args.output_dir).resolve()
    output.mkdir(parents=True, exist_ok=True)
    for name in RESERVED:
        require(not (output / name).exists(), 'refuse rerun/overwrite: ' + name)
    input_path, plan_path, guard_path = (Path(p).resolve() for p in
                                        (args.input_json, args.plan, args.guard_file))
    inputs = parse_inputs(input_path)
    require(file_hash(plan_path)['sha256'] == args.plan_sha256, 'plan hash mismatch')
    guard = json.loads(guard_path.read_bytes())
    require(guard['activity_id'] == ACTIVITY, 'wrong research activity')
    require(guard['activity_allowed'] is True and guard['persistence_allowed'] is True,
            'guard does not permit execution/persistence')
    require(guard['sync_debt_events'] == [], 'guard sync debt')
    require(guard['record_sha256'] == args.guard_record_sha256, 'guard record mismatch')
    check_dependencies()
    binding = {'schema': SCHEMA, 'source': file_hash(Path(__file__)),
               'inputs': inputs, 'input_path': str(input_path), 'input_file': file_hash(input_path),
               'plan_path': str(plan_path), 'plan_file': file_hash(plan_path),
               'guard_path': str(guard_path), 'guard_file': file_hash(guard_path), 'guard': guard,
               'dependencies': EXPECTED, 'coordinator_actual_read_sha': args.global_knowledge_sha,
               'author_actual_read_sha': 'a668c148c80cf836ff7e520ccb57e8d0e919b731',
               'scope': 'single public proposal; all outcomes retained; no random rate inference'}
    return output, binding


def end_binding(binding):
    require(file_hash(Path(__file__)) == binding['source'], 'source changed during run')
    for prefix in ('input', 'plan', 'guard'):
        require(file_hash(Path(binding[prefix + '_path'])) == binding[prefix + '_file'],
                prefix + ' file changed during run')
    check_dependencies()


def run(args):
    if hasattr(sys, 'set_int_max_str_digits'):
        sys.set_int_max_str_digits(0)
    output, binding = runtime_binding(args)
    write_new_json(output / 'STARTED.json', binding)
    sink = work = lm = None
    try:
        sink = EvidenceSink(output)
        sink.emit('binding', binding=binding)
        lm = load_arithmetic()
        native = lm.source_binding()  # Actual complete catalog admission, after STARTED.
        sink.emit('native_catalog_admission', source=native, all_native_records=lm.CALLS)
        work = Work(lm, sink, binding['inputs']['N'])
        result = compute(work, binding['inputs']['k'])
        work.stage = 'final_source_check'
        end_binding(binding)
        sink.emit('native_catalog_final', all_native_records=lm.CALLS)
        sink.emit('complete_result', result=result, cost=work.stats(),
                   native_catalog_calls=len(lm.CALLS))
        count, raw_bytes = sink.next_sequence, sink.raw_bytes
        sink.close()
        summary = {'schema': SCHEMA, 'execution_status': 'COMPLETE', 'binding': binding,
                   'result': result, 'cost': work.stats(), 'native_catalog_calls': len(lm.CALLS),
                   'member_count': count, 'decoded_bytes': raw_bytes,
                   'evidence': file_hash(output / 'EVIDENCE.jsonl.gz'),
                   'member_index': file_hash(output / 'MEMBER_INDEX.jsonl'),
                   'memory_scope': 'one full returned primitive trace plus serialization buffers; not constant memory',
                   'validation_scope': 'typed chronology and terminal conic consistency, no full-matrix rerun'}
        write_new_json(output / 'SUMMARY.json', summary)
        print(json.dumps(summary, sort_keys=True, default=plain))
    except BaseException:
        failure = {'schema': SCHEMA, 'execution_status': 'FAILED_NOT_RESUMABLE',
                   'traceback': traceback.format_exc(), 'binding': binding,
                   'work_stage': None if work is None else work.stage,
                   'last_completed_state': None if work is None else work.state,
                   'cost': None if work is None else work.stats(),
                   'catalog_records': [] if lm is None else lm.CALLS,
                   'committed_members': None if sink is None else sink.next_sequence,
                   'scope': 'complete durable members and available returned primitive; unreturned primitive may lack its final trace'}
        if sink is not None:
            sink.close()
        try:
            if sink is not None and sink.pending is not None:
                with (output / 'FAILED_PENDING_MEMBER.json.gz').open('xb') as raw:
                    with gzip.GzipFile(fileobj=raw, mode='wb', filename='', mtime=0) as gz:
                        for chunk in json_chunks(sink.pending):
                            gz.write(chunk)
                    raw.flush()
                    os.fsync(raw.fileno())
                failure['pending_member_file'] = file_hash(output / 'FAILED_PENDING_MEMBER.json.gz')
            failure['preserved_files'] = {name: file_hash(output / name)
                                          for name in ('EVIDENCE.jsonl.gz', 'MEMBER_INDEX.jsonl')
                                          if (output / name).exists()}
            write_new_json(output / 'FAILED.json', failure)
        except BaseException:
            text = failure['traceback'] + '\nFailure serialization also failed:\n' + traceback.format_exc()
            with (output / 'FAILED_SERIALIZATION.txt').open('xb') as stream:
                stream.write(text.encode('utf-8'))
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-json', required=True)
    parser.add_argument('--plan', required=True)
    parser.add_argument('--plan-sha256', required=True)
    parser.add_argument('--guard-file', required=True)
    parser.add_argument('--guard-record-sha256', required=True)
    parser.add_argument('--global-knowledge-sha', required=True)
    parser.add_argument('--output-dir', required=True)
    run(parser.parse_args())
