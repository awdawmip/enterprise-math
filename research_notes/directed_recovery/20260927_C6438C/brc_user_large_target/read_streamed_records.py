"""Complete saved-record audit, stdlib only; never imports the scientific runner.

Scientific results are consumed from their recorded native operations. Host
bit wiring reconstructs saved cells; no modular power/product/gcd is an oracle.
Only COMPLETE directories are admitted by this reader version.
"""
from pathlib import Path
from collections import Counter
import argparse
import ast
import hashlib
import json
import sys
import traceback
import zlib

ROOT = Path(__file__).resolve().parent
SCHEMA = 'BRC_STREAMED_PUBLIC_CLOCK_V1'
SOURCE_SHA = 'e4cde846c1d5c0238b881e05f3128c184fb599366f7da1f3e55161c8fbf5b86b'
PLAN_SHA = 'd861ea6b08801f457816e7a18752409d053f6e13174b2070320e0206511f87af'
NATIVE_READER = ROOT.parent / 'sep27-brc-native-tool-discovery/read_native_port_review.py'
NATIVE_READER_SHA = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
METRICS = ('typed_operations', 'adder_digit_replays', 'host_bit_wiring_operations',
           'host_bit_length_calls_in_arithmetic', 'native_kernel_calls_delta')
catalog = None
counts = Counter()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def hash_file(path):
    d, size = hashlib.sha256(), 0
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1048576), b''):
            d.update(block)
            size += len(block)
    return {'bytes': size, 'sha256': d.hexdigest()}


def unique_pairs(pairs):
    out = {}
    for key, value in pairs:
        assert key not in out, 'duplicate JSON key'
        out[key] = value
    return out


def decode(raw):
    return json.loads(raw, object_pairs_hook=unique_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def same(actual, expected):
    assert canonical(actual) == canonical(expected), (actual, expected)


def fields(record, **expected):
    for key, value in expected.items():
        same(record[key], value)


def load_native_reader():
    raw = NATIVE_READER.read_bytes()
    assert sha(raw) == NATIVE_READER_SHA
    nodes = [node for node in ast.parse(raw).body
             if isinstance(node, ast.FunctionDef) and node.name == 'trace']
    assert len(nodes) == 1
    # Only the already reviewed record-only function is compiled. No imports,
    # old top-level readback, catalog generation or scientific entrypoint runs.
    exec(compile(ast.Module(body=nodes, type_ignores=[]), str(NATIVE_READER)+'::<trace only>', 'exec'), globals())


def native_schema(value, key=None):
    """Strengthen exact scalar types and bit-index coverage before old reader."""
    if isinstance(value, dict):
        if 'cells' in value:
            assert type(value['width']) is int and value['width'] >= 1
            for bit, cell in enumerate(value['cells']):
                assert type(cell) is list and len(cell) == 4
                assert all(type(x) is int for x in cell)
                assert cell[0] == bit and 0 <= cell[1] < 8 and cell[2] in (0, 1) and cell[3] in (0, 1)
            assert len(value['cells']) == value['width']
            assert 0 <= value['left'] < (1 << value['width'])
            assert 0 <= value['right'] < (1 << value['width'])
        op = value.get('operation')
        if op == 'BRC_UNSIGNED_COMPARE':
            assert value['width'] == max(value['left'].bit_length(), value['right'].bit_length(), 1)+1
        elif op == 'BRC_UNSIGNED_SHIFT_ADD':
            assert value['width'] == max(1, value['left'].bit_length()+value['right'].bit_length())
        elif op == 'BRC_UNSIGNED_LONG_DIVISION':
            assert value['modulus'] > 0 and 0 <= value['remainder'] < value['modulus']
        for name, child in value.items():
            native_schema(child, name)
    elif isinstance(value, list):
        for child in value:
            native_schema(child, key)
    elif key == 'operation':
        assert type(value) is str
    elif key in ('bypass', 'nonnegative'):
        assert type(value) is bool
    elif value is not None:
        assert type(value) is int, (key, type(value))


def members(directory, summary):
    packed_path, index_path = directory/'EVIDENCE.jsonl.gz', directory/'MEMBER_INDEX.jsonl'
    same(hash_file(packed_path), summary['evidence'])
    same(hash_file(index_path), summary['member_index'])
    offset = decoded_bytes = member_count = 0
    with packed_path.open('rb') as stream, index_path.open('rb') as index:
        for seq, line in enumerate(index):
            entry = decode(line)
            fields(entry, sequence=seq, offset=offset)
            assert type(entry['compressed_bytes']) is int and entry['compressed_bytes'] > 0
            packed = stream.read(entry['compressed_bytes'])
            assert len(packed) == entry['compressed_bytes'] and sha(packed) == entry['compressed_sha256']
            decoder = zlib.decompressobj(16+zlib.MAX_WBITS)
            raw = decoder.decompress(packed)+decoder.flush()
            assert decoder.eof and not decoder.unused_data and not decoder.unconsumed_tail
            assert len(raw) == entry['raw_bytes'] and sha(raw) == entry['raw_sha256']
            assert raw.endswith(b'\n') and raw.count(b'\n') == 1
            record = decode(raw)
            fields(record, schema=SCHEMA, sequence=seq, kind=entry['kind'])
            if entry['kind'] == 'typed_operation':
                fields(entry, stream=record['stream'], operation_id=record['operation_id'])
            offset += len(packed)
            decoded_bytes += len(raw)
            member_count += 1
            counts['gzip_members'] += 1
            counts['maximum_decoded_member_bytes'] = max(counts['maximum_decoded_member_bytes'], len(raw))
            yield record
        assert stream.read(1) == b'', 'unindexed or trailing evidence bytes'
    same(member_count, summary['member_count'])
    same(decoded_bytes, summary['decoded_bytes'])


class Recorded:
    def __init__(self, directory, summary):
        self.rows = iter(members(directory, summary))
        self.pending = {}
        self.next_ids = Counter()
        self.costs = {}
        self.labels = {}
        self.N = summary['binding']['inputs']['N']

    def event(self, kind, **expected):
        while True:
            row = next(self.rows)
            if row['kind'] != 'typed_operation':
                break
            self.typed(row)
        fields(row, kind=kind, **expected)
        counts['event_'+kind] += 1
        return row

    def typed(self, row):
        global counts
        stream, index, op, t = row['stream'], row['operation_id'], row['operation'], row['trace']
        same(index, self.next_ids[stream])
        self.next_ids[stream] += 1
        native_schema(t)
        expected_kind = {'compare': 'BRC_UNSIGNED_COMPARE', 'multiply': 'BRC_UNSIGNED_SHIFT_ADD',
                         'divide': 'BRC_UNSIGNED_LONG_DIVISION'}
        if op == 'add':
            assert 'cells' in t and t['width'] == max(t['left'].bit_length(), t['right'].bit_length(), 1)+1
            assert t['carry'] == 0
        else:
            assert op in expected_kind and t['operation'] == expected_kind[op]
        cost = trace(t)
        if op == 'add':
            cost['host_bit_length_calls_in_arithmetic'] += 2
        same(row['cost'], {key: cost[key] for key in METRICS[1:4]})
        same(row['native_kernel_calls_delta'], 0)  # catalog was paid before arithmetic
        cost['typed_operations'] = 1
        self.costs.setdefault(stream, Counter()).update(cost)
        compact = {key: value for key, value in t.items()
                   if key not in ('cells', 'steps', 'first_add', 'second_add')}
        self.pending[(stream, index)] = (op, compact)
        counts['typed_operations'] += 1
        counts['maximum_pending_compact_operations'] = max(counts['maximum_pending_compact_operations'], len(self.pending))

    def op(self, link, name, **expected):
        assert set(link) == {'stream', 'operation_id'} and type(link['operation_id']) is int
        op, row = self.pending.pop((link['stream'], link['operation_id']))
        assert op == name
        fields(row, **expected)
        counts['consumed_operation_links'] += 1
        return row

    def add(self, stream, role, x, y):
        row = self.event('addmod', role=role, inputs=[x,y], N=self.N)
        assert row['add']['stream'] == row['division']['stream'] == stream
        ad = self.op(row['add'], 'add', left=x, right=y)
        div = self.op(row['division'], 'divide', value=ad['low'], modulus=self.N)
        fields(row, quotient=div['quotient'], output=div['remainder'])
        return row['output'], row['sequence']

    def sub(self, stream, role, x, y):
        row = self.event('submod', stream=stream, role=role, inputs=[x,y], N=self.N)
        ids = row['operations']
        cp = self.op({'stream':stream,'operation_id':ids['comparison']}, 'compare', left=x, right=y)
        if cp['relation'] >= 0:
            same(ids, {'comparison':ids['comparison'],'add_modulus':None})
            value = cp['low_difference']
        else:
            assert set(ids) == {'comparison','add_modulus','subtract_after_extension'}
            ad = self.op({'stream':stream,'operation_id':ids['add_modulus']}, 'add', left=x, right=self.N)
            final = self.op({'stream':stream,'operation_id':ids['subtract_after_extension']}, 'compare', left=ad['low'], right=y)
            assert final['relation'] >= 0
            value = final['low_difference']
        fields(row, output=value)
        assert 0 <= value < self.N
        return value, row['sequence']

    def mul(self, stream, role, x, y):
        row = self.event('modmul', stream=stream, role=role, inputs=[x,y], N=self.N)
        ids = row['operations']
        assert set(ids) == {'multiply_operation','division_operation'}
        mul = self.op({'stream':stream,'operation_id':ids['multiply_operation']}, 'multiply', left=x, right=y)
        div = self.op({'stream':stream,'operation_id':ids['division_operation']}, 'divide', value=mul['value'], modulus=self.N)
        fields(row, output=div['remainder'])
        return row['output'], row['sequence']

    def gcd(self, stream, role, values):
        begin = self.event('common_gcd_begin', stream=stream, role=role, N=self.N, coordinates=values)['sequence']
        current = self.N
        for position, coordinate in enumerate(values):
            left, right = current, coordinate
            while right:
                row = self.event('gcd_step', begin=begin, coordinate_index=position, left=left, right=right)
                assert row['division']['stream'] == stream
                div = self.op(row['division'], 'divide', value=left, modulus=right)
                fields(row, quotient=div['quotient'], remainder=div['remainder'])
                assert 0 <= row['remainder'] < right
                left, right = right, row['remainder']
            self.event('gcd_coordinate_done', begin=begin, coordinate_index=position, output=left)
            current = left
        end = self.event('common_gcd_end', begin=begin, value=current)
        return current, end['sequence']

    def factor(self, divisor, producer):
        if divisor == 1:
            return {'class':'UNIT','divisor':divisor,'producer':producer}
        if divisor == self.N:
            return {'class':'SATURATED','divisor':divisor,'producer':producer}
        assert 1 < divisor < self.N
        row = self.event('proper_factor_certificate', **{'class':'PROPER_FACTOR'}, divisor=divisor,
                         producer=producer, remainder=0)
        assert row['division']['stream'] == 'factor_division'
        div = self.op(row['division'], 'divide', value=self.N, modulus=divisor, remainder=0)
        fields(row, cofactor=div['quotient'])
        assert 1 < div['quotient'] < self.N
        return {key: row[key] for key in ('class','divisor','cofactor','remainder','producer','division')} | {'receipt':row['sequence']}

    def jacobi(self, stream, numerator):
        row = self.event('jacobi_begin', stream=stream, numerator=numerator, denominator=self.N, label_cost_so_far=1)
        assert row['division']['stream'] == stream
        div = self.op(row['division'], 'divide', value=numerator, modulus=self.N)
        fields(row, initial_quotient=div['quotient'], initial_residue=div['remainder'])
        begin, x, n, sign, wiring = row['sequence'], div['remainder'], self.N, 1, 1
        while x:
            labels = self.event('jacobi_labels', begin=begin, input_numerator=x, input_denominator=n, input_sign=sign)
            shifts = []
            while True:
                odd = x & 1
                wiring += 1
                if odd:
                    break
                following = x >> 1
                wiring += 1
                shifts.append({'input':x,'output':following})
                x = following
            n8, ep, x4, n4 = n & 7, len(shifts) & 1, x & 3, n & 3
            wiring += 4
            tf, rf = ep == 1 and n8 in (3,5), x4 == 3 and n4 == 3
            if tf: sign = -sign
            if rf: sign = -sign
            fields(labels, factor_two_shifts=shifts, odd_numerator=x, denominator_mod8=n8,
                   numerator_mod4=x4, denominator_mod4=n4, exponent_parity=ep,
                   two_flip=tf, reciprocal_flip=rf, output_sign=sign, cumulative_label_wiring=wiring)
            step = self.event('jacobi_step', begin=begin, labels=labels['sequence'], numerator=n, denominator=x)
            assert step['division']['stream'] == stream
            div = self.op(step['division'], 'divide', value=n, modulus=x)
            fields(step, quotient=div['quotient'], remainder=div['remainder'])
            n, x = x, div['remainder']
        value = sign if n == 1 else 0
        end = self.event('jacobi_end', begin=begin, value=value, terminal_gcd=n, terminal_sign=sign, label_wiring=wiring)
        self.labels[stream] = wiring
        return value, end['sequence']

    def cost(self):
        streams = {name:{'stream':name,'stats':{key:cost[key] for key in METRICS},
                         'completed_operation_ids':self.next_ids[name],
                         'durably_committed_operations':self.next_ids[name],
                         'unwritten_operation_pending':False} for name,cost in self.costs.items()}
        total = {key:sum(cost[key] for cost in self.costs.values()) for key in METRICS}
        validation = {key:self.costs.get('validation',Counter())[key] for key in METRICS}
        return {'streams':streams,'all_arithmetic_totals':total,
                'production_arithmetic_totals':{key:total[key]-validation[key] for key in METRICS},
                'validation_arithmetic_totals':validation,
                'jacobi_label_bit_wiring_operations':self.labels,
                'jacobi_label_bit_wiring_total':sum(self.labels.values()),
                'native_catalog_admission_counted_separately':True,
                'host_control_serialization_io_and_resource_monitoring_excluded':True}


def read_algorithm(r, k):
    odd = r.event('odd_modulus_check', N=r.N)
    assert odd['division']['stream'] == 'setup'
    div = r.op(odd['division'], 'divide', value=r.N, modulus=2, remainder=1)
    fields(odd, quotient=div['quotient'], remainder=1)
    two, _ = r.add('setup','two',1,1)
    four, _ = r.add('setup','four',two,two)
    k2, _ = r.mul('setup','k_square',k,k)
    delta, dl = r.sub('setup','discriminant',k2,four)
    g, gl = r.gcd('setup_gcd','discriminant_gcd',[delta])
    factor = r.factor(g,gl)
    status = 'REGULAR' if g == 1 else 'SETUP_FACTOR' if g < r.N else 'DEGENERATE'
    setup = {'k':k,'two':two,'four':four,'delta':delta,'delta_producer':dl,
             'gcd':g,'gcd_producer':gl,'setup_factor':factor,'status':status}
    r.event('setup_result', result=setup)
    if status != 'REGULAR':
        return {'status':status,'setup':setup,'characters_and_clock_evaluated':False}
    jd,jdl = r.jacobi('jacobi_delta',delta)
    kp,kpl = r.add('character_inputs','k_plus_two',k,two)
    je,jel = r.jacobi('jacobi_plus',kp)
    assert jd in (-1,1) and je in (-1,1)
    r.event('dual_character_result',j_delta=jd,j_plus=je,delta_producer=dl,plus_producer=kpl,
            jacobi_receipts=[jdl,jel],rejected_by_filter=False)
    clock = r.event('public_clock',N=r.N,j_delta=jd,
                    operation='add' if jd == -1 else 'compare_low_difference')
    assert clock['producer']['stream'] == 'clock'
    op = r.op(clock['producer'],'add' if jd == -1 else 'compare',left=r.N,right=1)
    if jd == 1: assert op['relation'] > 0
    E = op['low'] if jd == -1 else op['low_difference']
    fields(clock,E=E)
    bits,pair = format(E,'b'),[two,k]
    r.event('adjacent_power_begin',E=E,public_bits=bits,initial=pair)
    for i,bit in enumerate(bits):
        before = list(pair)
        r.event('adjacent_bit_begin',bit_index=i,bit=bit,before=before)
        product,pl = r.mul('power','cross',pair[0],pair[1])
        odd,ol = r.sub('power','odd_trace',product,k)
        selected = pair[0] if bit == '0' else pair[1]
        square,sl = r.mul('power','selected_square',selected,selected)
        even,el = r.sub('power','even_trace',square,two)
        pair = [even,odd] if bit == '0' else [odd,even]
        r.event('adjacent_bit_end',bit_index=i,bit=bit,before=before,after=pair,product=pl,odd=ol,square=sl,even=el)
        counts['checked_adjacent_bits'] += 1
    r.event('adjacent_power_end',pair=pair,bits=len(bits),multiplications_per_bit=2,orientation='ordered; no folding')
    v,w = pair
    v2,_ = r.mul('validation','v_square',v,v)
    w2,_ = r.mul('validation','w_square',w,w)
    vw,_ = r.mul('validation','v_times_w',v,w)
    kvw,_ = r.mul('validation','k_times_vw',k,vw)
    total,_ = r.add('validation','v2_plus_w2',v2,w2)
    total,_ = r.sub('validation','subtract_kvw',total,kvw)
    defect,link = r.add('validation','add_discriminant',total,delta)
    assert defect == 0
    r.event('terminal_conic_result',defect=defect,producer=link,history_certificate_sufficient=False)
    validation = {'defect':defect,'producer':link,
                  'scope':'consistency only; initial state and every typed bit step remain required'}
    readouts = {}
    for label in ('identity','antipodal'):
        method = r.sub if label == 'identity' else r.add
        tau,tl = method('expressions',label+'_tau',pair[0],two)
        w,wl = method('expressions',label+'_w',pair[1],k)
        d,gl = r.gcd('main_gcd',label,[tau,w])
        factor = r.factor(d,gl)
        item = {'tau':tau,'w':w,'expression_producers':[tl,wl],'joint_divisor':d,
                'joint_producer':gl,'factor_certificate':factor}
        r.event('signed_main_result',label=label,result=item)
        readouts[label] = item
    return {'status':'COMPLETE_MAIN_OBSERVERS','setup':setup,'characters':{'j_delta':jd,'j_plus':je},
            'E':E,'terminal_pair':pair,'validation':validation,'readouts':readouts,
            'factor_or_order_input':False,'second_clock_evaluated':False,
            'rate_or_shor_completion_claimed':False}


def main(directory, destination):
    global catalog
    assert not sys.flags.optimize, 'reader assertions must be enabled'
    assert not destination.exists(), 'refuse overwrite readback'
    if hasattr(sys,'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
    summary = decode((directory/'SUMMARY.json').read_bytes())
    fields(summary,schema=SCHEMA,execution_status='COMPLETE')
    binding = summary['binding']
    same(decode((directory/'STARTED.json').read_bytes()),binding)
    assert not any((directory/name).exists() for name in ('FAILED.json','FAILED_SERIALIZATION.txt','FAILED_PENDING_MEMBER.json.gz'))
    assert binding['source']['sha256'] == SOURCE_SHA == hash_file(ROOT/'streaming_public_clock.py')['sha256']
    source_tree = ast.parse((ROOT/'streaming_public_clock.py').read_bytes())
    maps = [ast.literal_eval(node.value) for node in source_tree.body
            if isinstance(node,ast.Assign) and any(isinstance(target,ast.Name) and target.id == 'EXPECTED'
                                                  for target in node.targets)]
    assert len(maps) == 1
    same(binding['dependencies'],maps[0])
    assert binding['plan_file']['sha256'] == PLAN_SHA
    for prefix in ('input','plan','guard'):
        same(hash_file(Path(binding[prefix+'_path'])),binding[prefix+'_file'])
    guard = decode(Path(binding['guard_path']).read_bytes())
    same(guard,binding['guard'])
    fields(guard,activity_id='RA-CAAAC604CB513AEA8BBC1DFC',activity_allowed=True,persistence_allowed=True,sync_debt_events=[])
    supplied = decode(Path(binding['input_path']).read_bytes())
    assert set(supplied) == {'N','k'} and all(type(v) is str for v in supplied.values())
    same(binding['inputs'],{key:int(value) for key,value in supplied.items()})
    for relative,pin in binding['dependencies'].items():
        assert hash_file(ROOT.parent/relative)['sha256'] == pin
    load_native_reader()
    r = Recorded(directory,summary)
    r.event('binding',binding=binding)
    admission = r.event('native_catalog_admission')
    catalog = admission['source']['native_adder']['columns']
    assert type(catalog) is list and len(catalog) == 8
    assert all(type(c) is list and len(c) == 2 and all(type(b) is int and b in (0,1) for b in c) for c in catalog)
    native = admission['all_native_records']
    assert len(native) == 1
    fields(native[0],entrypoint='recurrent_mass_power',states=12,depth=1)
    for name,relative in (('lazy_modular','sep26-shor-general/optimization/lazy_modular/lazy_modular.py'),
                          ('sparse_modular','sep26-shor-general/sparse/sparse_modular.py'),
                          ('typed_integer_prechecks','sep26-shor-general/completion/typed_integer_prechecks.py')):
        assert admission['source']['files_sha256'][name] == binding['dependencies'][relative]
    vendor = ROOT.parent/'sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py'
    assert hash_file(vendor)['sha256'] == admission['source']['native_adder']['vendor']['sha256']
    result = read_algorithm(r,binding['inputs']['k'])
    r.event('native_catalog_final',all_native_records=native)
    cost = r.cost()
    r.event('complete_result',result=result,cost=cost,native_catalog_calls=len(native))
    assert not r.pending, 'unconsumed primitive operations'
    assert next(r.rows,None) is None, 'trailing records'
    same(summary['result'],result)
    same(summary['cost'],cost)
    same(summary['native_catalog_calls'],len(native))
    report = {'status':'PASS_COMPLETE_SAVED_NATIVE_RECORD_AUDIT_NOT_SCIENTIFIC_REPLAY',
              'schema':SCHEMA,'reader':hash_file(Path(__file__)),'source_sha256':SOURCE_SHA,
              'plan_sha256':PLAN_SHA,'native_record_reader_sha256':NATIVE_READER_SHA,
              'summary':hash_file(directory/'SUMMARY.json'),'evidence':summary['evidence'],
              'member_index':summary['member_index'],'counts':dict(counts),'cost':cost,'result':result,
              'scope':'all indexed gzip bytes, native cells, typed links, Jacobi wiring, ordered bit chronology, both main gcds and actual factor division',
              'not_performed':['native kernel rerun','host modular-power or gcd oracle','second-clock calculation','probability or general factoring inference'],
              'admission':'shared-context author record review, not independent formal admission'}
    with destination.open('x',encoding='utf-8') as handle:
        json.dump(report,handle,indent=2,sort_keys=True)
        handle.write('\n')
    print(json.dumps({'status':report['status'],'counts':report['counts'],'output':str(destination)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',required=True)
    parser.add_argument('--output',required=True)
    args = parser.parse_args()
    try:
        main(Path(args.run_dir).resolve(),Path(args.output).resolve())
    except BaseException:
        failure = Path(args.output).resolve().with_suffix('.FAILED.json')
        with failure.open('x',encoding='utf-8') as handle:
            json.dump({'status':'RECORD_REVIEW_FAILED','traceback':traceback.format_exc(),'counts':dict(counts)},handle,indent=2)
        raise
