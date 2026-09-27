"""Author complete saved-evidence readback. Standard-library I/O only.
Reads retained outputs and receipts; never imports a scientific module,
recomputes a scalar scientific answer, or repeats any experiment.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import ast, gzip, hashlib, json
ROOT = Path(__file__).resolve().parent
SCHEMA = 'BRC_TOP_BIT_GENERAL_MODULUS_V1'
DEGREES = {f'{p},{e}' for e in range(4) for p in range(4-e)}
RAW_PIN = '4f6fae5355d3a809b765af17c6be7b2ac709cf63ec2e6fbd4e5b81a35cf79dc9'
GZIP_PIN = 'ba39feafb35e6d902c1ba1de8c7e64aba581eca7d02e429064c389f6d79e9dc0'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True)


def same(a, b):
    assert canonical(a) == canonical(b)


def semantic(cert):
    cert = deepcopy(cert)
    stats = cert['actual_integer_evidence']['arithmetic_stats']
    assert type(stats['native_kernel_calls_delta']) is int and stats['native_kernel_calls_delta'] >= 0
    stats['native_kernel_calls_delta'] = 0
    return canonical(cert)


def trace_accounting(evidence):
    """Recount retained cells/host metadata, without executing their arithmetic."""
    total = Counter(adder_digit_replays=0, host_bit_wiring_operations=0,
                    host_bit_length_calls_in_arithmetic=0)
    columns = evidence['native_source']['native_adder']['columns']
    assert len(columns) == 8
    def visit(item):
        if type(item) is dict:
            if {'cells', 'low', 'carry'} <= set(item):
                cells = item['cells']
                assert len(cells) == item['width']
                for bit, cell in enumerate(cells):
                    assert len(cell) == 4 and cell[0] == bit
                    assert type(cell[1]) is int and 0 <= cell[1] < len(columns)
                    same(cell[2:], columns[cell[1]])
                if cells:
                    same(item['carry'], cells[-1][3])
                total['adder_digit_replays'] += len(cells)
                total['host_bit_wiring_operations'] += 10*len(cells)
                return
            kind = item.get('operation')
            if kind == 'BRC_UNSIGNED_COMPARE':
                total['host_bit_wiring_operations'] += 3
                total['host_bit_length_calls_in_arithmetic'] += 2
            elif kind == 'BRC_UNSIGNED_SHIFT_ADD':
                total['host_bit_wiring_operations'] += 3*len(item['steps'])
                total['host_bit_length_calls_in_arithmetic'] += 3
            elif kind == 'BRC_UNSIGNED_LONG_DIVISION':
                total['host_bit_wiring_operations'] += 6*len(item['steps'])
                total['host_bit_length_calls_in_arithmetic'] += 1
            for child in item.values():
                visit(child)
        elif type(item) is list:
            for child in item:
                visit(child)
    for operation in evidence['arithmetic_operations']:
        assert operation['operation'] in ('add', 'compare', 'multiply', 'divide')
        visit(operation['trace'])
        if operation['operation'] == 'add':
            total['host_bit_length_calls_in_arithmetic'] += 2
    for key, count in total.items():
        assert count == evidence['arithmetic_stats'][key]
    return dict(total)


class RecordedCursor:
    """A cursor over already saved outputs, not an arithmetic evaluator."""
    def __init__(self, evidence):
        self.evidence = evidence
        self.ops = evidence['signed_operations']
        self.i = 0
        self.node_map = {}
        self.seen_tables = 0
        self.empty_progressions = 0
        nodes = evidence['moment_nodes']
        for index, node in enumerate(nodes):
            key = tuple(node['parameters'])
            assert key not in self.node_map and len(key) == 4
            assert set(node['moments']) == DEGREES
            assert 0 <= node['signed_operations_start'] <= node['signed_operations_stop'] <= len(self.ops)
            assert node['branch'] in ('empty', 'normalize_signed_coefficients',
                'normalized_constant_zero', 'normalized_zero_height', 'transpose_lattice')
            if node['child'] is not None:
                child_index, child = self.node_map[tuple(node['child'])]
                assert child_index < index
                assert child['signed_operations_stop'] <= node['signed_operations_stop']
            self.node_map[key] = (index, node)
        assert evidence['stats']['moment_requests'] == len(nodes) + evidence['stats']['cache_hits']

    def take(self, kind, inputs):
        op = self.ops[self.i]
        assert op['operation'] == kind
        same(op['inputs'], inputs)
        self.i += 1
        return op['result']

    def add(self, x, y):
        return self.take('signed_add', [x, y])

    def sub(self, x, y):
        return self.take('signed_add', [x, -y])

    def mul(self, x, y):
        return self.take('signed_multiply', [x, y])

    def div(self, x, y):
        return self.take('signed_euclidean_division', [x, y])

    def total(self, terms):
        value = 0
        for term in terms:
            value = self.add(value, term)
        return value

    def recorded(self, record, operation):
        assert record['signed_operations_start'] == self.i
        value = operation()
        same(value, record['value'])
        assert record['signed_operations_stop'] == self.i
        return value

    def exact(self, record, numerator, denominator):
        same(record['numerator'], numerator)
        same(record['denominator'], denominator)
        assert record['signed_operation_index'] == record['signed_operations_start'] == self.i
        value, remainder = self.div(numerator, denominator)
        assert remainder == record['remainder'] == 0
        same(value, record['value'])
        assert record['signed_operations_stop'] == self.i
        return value

    def table(self, record, n, P, R, b):
        same(record['inputs'], {'n': n, 'm': P, 'a': R, 'b': b})
        assert record['signed_operations_start'] == self.i
        stop = record['signed_operations_stop']
        assert self.i <= stop <= len(self.ops)
        index, node = self.node_map[(n, P, R, b)]
        same(record['outputs'], node['moments'])
        new_indices = record['new_moment_node_indices']
        if new_indices:
            same(new_indices, list(range(new_indices[0], new_indices[-1]+1)))
            assert new_indices[-1] == index
            for j in new_indices:
                part = self.evidence['moment_nodes'][j]
                assert self.i <= part['signed_operations_start'] <= part['signed_operations_stop'] <= stop
            assert node['signed_operations_start'] == self.i and node['signed_operations_stop'] == stop
        else:
            assert self.i == stop and node['signed_operations_stop'] <= stop
        before, after = record['stats_before'], record['stats_after']
        assert after['moment_requests'] - before['moment_requests'] == len(new_indices) + after['cache_hits'] - before['cache_hits']
        assert after['max_recursion_depth'] >= before['max_recursion_depth']
        assert after['max_observed_integer_bits'] >= before['max_observed_integer_bits']
        self.i = stop
        self.seen_tables += 1
        return record['outputs']

    def progression(self, record, head, orientation, req):
        same(record['head'], head)
        assert record['orientation'] == orientation and record['multiplicity'] == 1
        assert record['signed_operations_start'] == self.i
        R, L, U, P, b = req['inputs']['R'], req['L'], req['U'], req['P'], head['value']
        same(record['step'], R)
        z = self.recorded(record['last_minus_head'], lambda: self.sub(self.sub(L, 1), b))
        if z < 0:
            assert record['empty'] is True and record['n'] == 0 and record['table_calls'] == []
            answer = self.recorded(record['zero'], lambda: self.add(0, 0))
            self.empty_progressions += 1
        else:
            assert record['empty'] is False
            length = record['length_receipt']
            assert length['signed_operations_start'] == self.i
            q, remainder = self.div(z, R)
            n = self.add(q, 1)
            same([q, remainder, n], [length['quotient'], length['remainder'], length['value']])
            same(n, record['n'])
            assert length['signed_operations_stop'] == self.i
            assert len(record['table_calls']) == 2
            M = self.table(record['table_calls'][0], n, P, R, b)
            shifted = self.recorded(record['shifted_offset'], lambda: self.add(b, U))
            Mp = self.table(record['table_calls'][1], n, P, R, shifted)
            delta = {}
            for key in ('0,1', '1,1', '0,2', '1,2', '0,3'):
                delta[key] = self.recorded(record['deltas'][key], lambda key=key: self.sub(Mp[key], M[key]))
            D01, D11, D02, D12, D03 = [delta[k] for k in ('0,1', '1,1', '0,2', '1,2', '0,3')]
            nums, exact = record['division_numerators'], record['exact_divisions']
            numerator = self.recorded(nums['qdelta'], lambda: self.sub(D02, D01))
            qdelta = self.exact(exact['qdelta'], numerator, 2)
            numerator = self.recorded(nums['jqdelta'], lambda: self.sub(D12, D11))
            jqdelta = self.exact(exact['jqdelta'], numerator, 2)
            numerator = self.recorded(nums['q2delta'], lambda: self.total((self.mul(2, D03), self.mul(-3, D02), D01)))
            q2delta = self.exact(exact['q2delta'], numerator, 6)
            weighted = record['weighted_sums']
            d = self.recorded(weighted['d'], lambda: self.add(self.mul(b, n), self.mul(R, M['1,0'])))
            dq = self.recorded(weighted['dq'], lambda: self.add(self.mul(b, M['0,1']), self.mul(R, M['1,1'])))
            dd = self.recorded(weighted['ddelta'], lambda: self.add(self.mul(b, D01), self.mul(R, D11)))
            dqd = self.recorded(weighted['dqdelta'], lambda: self.add(self.mul(b, qdelta), self.mul(R, jqdelta)))
            factors = {'n': n, 'q': M['0,1'], 'dq': dq, 'q2': M['0,2'], 'd': d,
                'ddelta': dd, 'dqdelta': dqd, 'q2delta': q2delta, 'qdelta': qdelta, 'delta': D01}
            same(factors, record['term_factors'])
            names = ('n', 'q', 'dq', 'q2', 'd', 'ddelta', 'dqdelta', 'q2delta', 'qdelta', 'delta')
            terms = [self.recorded(record['terms'][name], lambda name=name:
                self.mul(req['coefficients'][name]['value'], factors[name])) for name in names]
            answer = self.recorded(record['sumA'], lambda: self.total(terms))
        same(answer, record['value'])
        assert record['signed_operations_stop'] == self.i
        return answer


def costs(evidences):
    rows = list(evidences)
    keys = ('adder_digit_replays','typed_operations','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic')
    total = {key: sum(r['arithmetic_stats'][key] for r in rows) for key in keys}
    total.update(signed_operations=sum(len(r['signed_operations']) for r in rows),
                 moment_nodes=sum(len(r['moment_nodes']) for r in rows),
                 window_queries=sum(len(r['window_weight_queries']) for r in rows),
                 moment_requests=sum(r['stats']['moment_requests'] for r in rows),
                 cache_hits=sum(r['stats']['cache_hits'] for r in rows))
    maxima = {key: max(r['stats'][key] for r in rows) for key in ('max_recursion_depth','max_observed_integer_bits')}
    return {'receipts':len(rows),'sum':total,'max':maxima,
            'native_calls_counted_from_disjoint_process_intervals':True}


def signed_typed_links(evidence):
    """Bind saved signed results to saved typed output fields, not evaluation."""
    typed = evidence['arithmetic_operations']
    same([j for op in evidence['signed_operations'] for j in op['typed_operation_indices']],
         list(range(len(typed))))
    for operation in evidence['signed_operations']:
        steps = [typed[j] for j in operation['typed_operation_indices']]
        at = 0
        def take(kind, left, right):
            nonlocal at
            row = steps[at]
            at += 1
            assert row['operation'] == kind
            t = row['trace']
            if kind == 'divide':
                same([t['value'], t['modulus']], [left, right])
                return t['quotient'], t['remainder']
            same([t['left'], t['right']], [left, right])
            if kind == 'add':
                assert t['carry'] == 0
                return t['low']
            if kind == 'multiply':
                return t['value']
            assert kind == 'compare'
            return t['relation'], t['low_difference']
        x, y = operation['inputs']
        if operation['operation'] == 'signed_add':
            if (x < 0) == (y < 0):
                mag = take('add', abs(x), abs(y))
                result = -mag if x < 0 else mag
            else:
                relation, mag = take('compare', abs(x), abs(y))
                if relation < 0:
                    _, mag = take('compare', abs(y), abs(x))
                    result = -mag if y < 0 else mag
                else:
                    result = -mag if x < 0 else mag
        elif operation['operation'] == 'signed_multiply':
            mag = take('multiply', abs(x), abs(y))
            result = -mag if (x < 0) != (y < 0) else mag
        else:
            assert operation['operation'] == 'signed_euclidean_division' and y > 0
            quotient, remainder = take('divide', abs(x), y)
            if x < 0:
                if remainder:
                    quotient = take('add', quotient, 1)
                    _, remainder = take('compare', y, remainder)
                quotient = -quotient
            result = [quotient, remainder]
        same(result, operation['result'])
        assert at == len(steps)
    assert len(typed) == evidence['arithmetic_stats']['typed_operations']


def decode_keys(item):
    if type(item) is dict:
        assert set(item) == {'object_entries'}
        out = {}
        for entry in item['object_entries']:
            key = entry['key']
            assert type(key).__name__ == entry['key_type'] and key not in out
            out[key] = decode_keys(entry['value'])
        return out
    if type(item) is list:
        return [decode_keys(x) for x in item]
    return item


def inspect_evidence(e,native):
    signed_typed_links(e)
    if 'native_source' in e:
        same(e['native_source'],native)
    assert e['window_weight_queries']==[]
    return trace_accounting({**e,'native_source':native})


def encode_keys(item):
    if type(item) is dict:
        return {'object_entries':[{'key_type':type(k).__name__,'key':k,'value':encode_keys(v)} for k,v in item.items()]}
    if type(item) is list:
        return [encode_keys(x) for x in item]
    return item

def inspect_pairs(record, inputs):
    c = TopCursor(record['actual_integer_evidence'])
    same(c.power(inputs['g']), record['length'])
    low, high = record['low_scale'], record['high_scale']
    same(c.power(inputs['ell']), low)
    same(c.power(inputs['k']), high)
    rows = record['digit_observations']
    assert len(rows) == record['length']
    for x, row in enumerate(rows):
        assert row['label'] == x and row['signed_operations_start'] == c.i
        lq, lr = c.div(x, low)
        _, lb = c.div(lq, 2)
        hq, hr = c.div(x, high)
        _, hb = c.div(hq, 2)
        summed = c.add(lb, hb)
        _, parity = c.div(summed, 2)
        same([lq, lr, lb, hq, hr, hb, summed, parity], [row[k] for k in
             ('low_quotient','low_remainder','low_bit','high_quotient','high_remainder','high_bit','bit_sum','parity')])
        assert row['signed_operations_stop'] == c.i
    buckets = [0 for _ in range(inputs['R'])]
    pairs = iter(record['pair_observations'])
    count = 0
    for x in range(record['length']):
        for y in range(record['length']):
            row = next(pairs)
            assert row['x'] == x and row['y'] == y and row['signed_operations_start'] == c.i
            diff = c.sub(y, x)
            quotient, residue = c.div(diff, inputs['R'])
            sign = 1 if rows[x]['parity'] == rows[y]['parity'] else -1
            same([diff, quotient, residue, sign], [row[k] for k in ('difference','quotient','residue','sign')])
            same(row['bucket_before'], buckets[residue])
            buckets[residue] = c.add(buckets[residue], sign)
            same(buckets[residue], row['bucket_after'])
            assert row['signed_operations_stop'] == c.i
            count += 1
    assert next(pairs, None) is None and c.i == len(c.ops)
    assert record['all_residue_buckets_from_one_pair_pass'] is True
    return buckets, count

class TopCursor(RecordedCursor):
    def power(self, exponent):
        value=1
        for _ in range(exponent): value=self.add(value,value)
        return value

    def division(self, record, x, m):
        same([record['numerator'],record['denominator']],[x,m])
        assert record['signed_operations_start']==self.i
        q,r=self.div(x,m)
        same([q,r],[record['quotient'],record['remainder']])
        assert record['signed_operations_stop']==self.i
        return q,r

    def length(self, record, head, step, limit):
        same([record['head'],record['step'],record['exclusive_limit']],[head,step,limit])
        t=self.recorded(record['last_minus_head'],lambda:self.sub(self.sub(limit,1),head))
        if t<0:
            assert record['empty'] is True
            n=self.recorded(record['zero'],lambda:self.add(0,0))
            assert n==0
        else:
            assert record['empty'] is False
            q,_=self.division(record['division'],t,step)
            n=self.recorded(record['length_addition'],lambda:self.add(q,1))
        same(n,record['n'])
        return n

    def coefficients(self, record, piece, V, M):
        assert record['piece']==piece and record['signed_operations_start']==self.i
        if piece=='low':
            ops=(('a0',lambda:self.mul(V,M)),('a1',lambda:self.sub(3,self.mul(2,M))),
                ('b0',lambda:self.sub(self.mul(self.mul(2,V),M),self.mul(6,V))),
                ('b1',lambda:self.add(6,0)),('c',lambda:self.mul(-6,V)))
        else:
            assert piece=='high'
            ops=(('a0',lambda:self.mul(-1,self.mul(V,M))),('a1',lambda:self.sub(self.mul(2,M),1)),
                ('b0',lambda:self.sub(self.mul(2,V),self.mul(self.mul(2,V),M))),
                ('b1',lambda:self.add(-2,0)),('c',lambda:self.mul(2,V)))
        p={name:self.recorded(record['primitive'][name],fn) for name,fn in ops}
        a0,a1,b0,b1,c=[p[key] for key in ('a0','a1','b0','b1','c')]
        ops=(('n',lambda:self.mul(3,a0)),('d',lambda:self.mul(3,a1)),
            ('q',lambda:self.mul(6,b0)),('dq',lambda:self.mul(6,b1)),('q2',lambda:self.mul(12,c)),
            ('delta1',lambda:self.sub(self.add(self.mul(-6,a0),self.mul(3,b0)),c)),
            ('ddelta1',lambda:self.add(self.mul(-6,a1),self.mul(3,b1))),
            ('delta2',lambda:self.add(self.mul(-6,b0),self.mul(6,c))),
            ('ddelta2',lambda:self.mul(-6,b1)),('delta3',lambda:self.mul(-8,c)))
        coeff={name:self.recorded(record['coefficients'][name],fn) for name,fn in ops}
        assert record['signed_operations_stop']==self.i
        return coeff

    def segment(self, record, P, V, R, coefficients):
        assert record['signed_operations_start']==self.i
        n,b=record['n'],record['head']['value']
        if n==0:
            assert record['empty'] is True and record['table_calls']==[]
            answer=self.recorded(record['zero'],lambda:self.add(0,0))
        else:
            assert n>0 and record['empty'] is False and len(record['table_calls'])==2
            table=self.table(record['table_calls'][0],n,P,R,b)
            offset=self.recorded(record['shifted_offset'],lambda:self.add(b,V))
            shifted=self.table(record['table_calls'][1],n,P,R,offset)
            delta={key:self.recorded(record['deltas'][key],lambda key=key:self.sub(shifted[key],table[key]))
                for key in ('0,1','1,1','0,2','1,2','0,3')}
            weighted={
                'd':lambda:self.add(self.mul(b,table['0,0']),self.mul(R,table['1,0'])),
                'dq':lambda:self.add(self.mul(b,table['0,1']),self.mul(R,table['1,1'])),
                'ddelta1':lambda:self.add(self.mul(b,delta['0,1']),self.mul(R,delta['1,1'])),
                'ddelta2':lambda:self.add(self.mul(b,delta['0,2']),self.mul(R,delta['1,2']))}
            w={key:self.recorded(record['weighted_sums'][key],fn) for key,fn in weighted.items()}
            factors={'n':table['0,0'],'d':w['d'],'q':table['0,1'],'dq':w['dq'],
                'q2':table['0,2'],'delta1':delta['0,1'],'ddelta1':w['ddelta1'],
                'delta2':delta['0,2'],'ddelta2':w['ddelta2'],'delta3':delta['0,3']}
            same(factors,record['term_factors'])
            terms=[self.recorded(record['terms'][key],lambda key=key:self.mul(coefficients[key],factors[key]))
                for key in factors]
            numerator=self.recorded(record['three_sum_numerator'],lambda:self.total(terms))
            answer=self.exact(record['exact_third'],numerator,3)
        same(answer,record['value'])
        assert record['signed_operations_stop']==self.i
        return answer

    def orientation(self, record, L, H, P, V, R, coefficients):
        assert record['signed_operations_start']==self.i
        b=record['head']['value']
        whole=self.length(record['whole_length'],b,R,L)
        if record['whole_length']['empty']:
            assert record['empty'] is True and record['segments']==[]
            answer=self.recorded(record['zero'],lambda:self.add(0,0))
        else:
            assert record['empty'] is False and len(record['segments'])==2
            low=self.length(record['low_length'],b,R,H)
            high=self.recorded(record['high_count'],lambda:self.sub(whole,low))
            assert high>=0
            head=self.recorded(record['high_head'],lambda:self.add(b,self.mul(R,low)))
            values=[]
            for seg,piece,h,n in zip(record['segments'],('low','high'),(b,head),(low,high)):
                same([seg['piece'],seg['head']['value'],seg['n'],seg['step'],seg['coefficient_piece']],
                    [piece,h,n,R,piece])
                same(seg['head'],record['head'] if piece=='low' else record['high_head'])
                same([seg['displacement_lower_bound'],seg['displacement_exclusive_upper_bound']],
                    [0,H] if piece=='low' else [H,L])
                if n:
                    assert seg['displacement_lower_bound']<=h<seg['displacement_exclusive_upper_bound']
                values.append(self.segment(seg,P,V,R,coefficients[piece]))
            answer=self.recorded(record['total'],lambda:self.total(values))
        same(answer,record['value'])
        assert record['signed_operations_stop']==self.i
        return answer

    def requests(self, cert):
        for request in cert['requests']:
            start_tables=self.seen_tables
            assert request['signed_operations_start']==self.i
            inp=request['inputs'];g,ell,k,R,r=[inp[x] for x in ('g','ell','k','R','r')]
            assert all(type(x) is int for x in inp.values())
            assert g>=2 and 0<=ell<k<g and k==g-1 and R>0 and 0<=r<R and inp['stride']==1
            V=self.power(ell);M=self.power(g-ell);L=self.mul(V,M);P=self.add(V,V)
            H=self.exact(request['half_length'],L,2)
            same([V,M,L,P],[request[x] for x in ('V','M','L','P')])
            assert request['scales_operations_stop']==self.i
            coefficients={p:self.coefficients(request['coefficients'][p],p,V,M) for p in ('low','high')}
            o=request['orientations'];assert len(o)==2
            self.recorded(o[0]['head'],lambda:self.add(r,0))
            self.recorded(o[1]['head'],lambda:self.sub(R,r))
            values=[]
            for record,label in zip(o,('nonnegative_difference','negative_difference_magnitude')):
                assert record['orientation']==label and record['multiplicity']==1
                values.append(self.orientation(record,L,H,P,V,R,coefficients))
            result=self.recorded(request['final_addition'],lambda:self.total(values))
            same(result,request['value'])
            assert request['signed_operations_stop']==self.i
            assert self.seen_tables-start_tables==request['top_level_table_calls']<=8
            assert request['raw_denominator_exponent']==2*g and request['modulus_alignment_required'] is False
            assert request['route']=='TOP_BIT_TWO_PIECE_FLOOR_MOMENTS'
        assert self.i==len(self.ops)


def raw_digit_count(item):
    if type(item) is dict:
        if {'cells','low','carry'}<=set(item): return len(item['cells'])
        return sum(raw_digit_count(v) for v in item.values())
    if type(item) is list: return sum(raw_digit_count(v) for v in item)
    return 0


def production_hotspots(cert):
    e=cert['actual_integer_evidence'];ops=e['signed_operations'];labels=['routing_and_final']*len(ops)
    def mark(name,start,stop):
        assert 0<=start<=stop<=len(labels)
        labels[start:stop]=[name]*(stop-start)
    for req in cert['requests']:
        mark('scales',req['signed_operations_start'],req['scales_operations_stop'])
        for p,coef in req['coefficients'].items():
            mark('coefficients_'+p,coef['signed_operations_start'],coef['signed_operations_stop'])
        for o in req['orientations']:
            for s in o['segments']:
                mark('empty_segments' if s['empty'] else 'segment_outer',s['signed_operations_start'],s['signed_operations_stop'])
                for table in s['table_calls']:
                    mark('moment_tables',table['signed_operations_start'],table['signed_operations_stop'])
    counters={name:Counter(signed_operations=0,typed_operations=0,adder_digit_replays=0) for name in set(labels)}
    for label,op in zip(labels,ops):
        counters[label]['signed_operations']+=1
        counters[label]['typed_operations']+=len(op['typed_operation_indices'])
        counters[label]['adder_digit_replays']+=sum(raw_digit_count(e['arithmetic_operations'][i]['trace']) for i in op['typed_operation_indices'])
    assert sum(c['adder_digit_replays'] for c in counters.values())==e['arithmetic_stats']['adder_digit_replays']
    return {key:dict(counters[key]) for key in sorted(counters)}


def cost_record(e):
    return {'arithmetic_stats':e['arithmetic_stats'],'typed_operations':len(e['arithmetic_operations']),
        'signed_operations':len(e['signed_operations']),'moment_nodes':len(e['moment_nodes']),
        'window_queries':len(e['window_weight_queries']),'moment_stats':e['stats']}


def source_pins(cert):
    targets={'source_sha256':ROOT/'top_bit_general.py','proof_sha256':ROOT/'TOP_BIT_GENERAL_MODULUS.md',
        'proof_review_sha256':ROOT/'guard_review/TOP_BIT_GENERAL_MODULUS_REVIEW.md',
        'direct_source_sha256':ROOT.parent/'sep27-qft-gap-direct/direct_gap/direct_signed_gap.py',
        'direct_proof_sha256':ROOT.parent/'sep27-qft-gap-direct/DIFFERENCE_AUTOCORRELATION.md',
        'floor_moment_source_sha256':ROOT.parent/'sep27-qft-adaptive/nonzero_structure/typed_floor_moments.py',
        'baseline_helper_source_sha256':ROOT.parent/'sep27-qft-signedgap/signed_gap/signed_gap.py'}
    for field,path in targets.items(): assert digest(path.read_bytes())==cert[field]
    return {k:{'path':str(v),'sha256':cert[k]} for k,v in targets.items()}


def inspect_partial(cert, original, native):
    assert cert['schema']=='INCOMPLETE_'+SCHEMA and cert['complete_certificate'] is False
    assert cert['inflight_request'] is None and len(cert['requests'])==1
    assert cert['source_sha256']==original['source_sha256']
    same(cert['requests'],original['requests'][:1])
    e=cert['actual_integer_evidence'];inspect_evidence(e,native);TopCursor(e).requests(cert)
    stop=cert['requests'][0]['signed_operations_stop']
    old=original['actual_integer_evidence']
    same(e['signed_operations'],old['signed_operations'][:stop])
    typed_stop=len(e['arithmetic_operations'])
    same(e['arithmetic_operations'],old['arithmetic_operations'][:typed_stop])
    same(e['moment_nodes'],old['moment_nodes'][:len(e['moment_nodes'])])


def main():
    compressed=(ROOT/'TOP_BIT_GENERAL_RESULTS.json.gz').read_bytes();raw=gzip.decompress(compressed)
    assert digest(raw)==RAW_PIN and digest(compressed)==GZIP_PIN
    data=json.loads(raw);summary=json.loads((ROOT/'TOP_BIT_GENERAL_SUMMARY.json').read_bytes())
    assert data['status']==summary['status']=='PASS'
    assert summary['payload_sha256']==RAW_PIN and summary['artifact_sha256']==GZIP_PIN
    assert summary['raw_bytes']==len(raw) and summary['gzip_bytes']==len(compressed)
    same(data['source_sha256'],summary['source_sha256'])
    for path,pin in data['source_sha256'].items():assert digest((ROOT/path).read_bytes())==pin
    guard=(ROOT/'STARTUP_GUARD.json').read_bytes();assert digest(guard)==data['startup_guard']['sha256']
    same(json.loads(guard),data['startup_guard']['receipt'])
    g=data['startup_guard']['receipt']
    assert g['activity_allowed'] is True and g['persistence_allowed'] is True
    assert g['activity_id']=='RA-CAAAC604CB513AEA8BBC1DFC' and g['sync_debt_events']==[]
    assert g['mode']=='TASK_RESEARCH' and g['boundary']=='startup'
    comp=data['comparator_source'];same(comp,summary['comparator_source'])
    template=Path(comp['template_path']).read_bytes();assert digest(template)==comp['template_sha256']
    source=(ROOT/'check_top_bit_general.py').read_text(encoding='utf-8-sig')
    def function(text,name):
        return ast.get_source_segment(text,next(n for n in ast.parse(text).body if isinstance(n,ast.FunctionDef) and n.name==name))
    template_function=function(template.decode('utf-8-sig'),'typed_pair_histogram')
    assert template_function==function(source,'typed_pair_histogram')
    assert digest(template_function.encode())==comp['copied_function_sha256']
    assert comp['exact_source_text_equal'] is True and comp['historical_checker_imported_or_executed'] is False
    native=data['cases'][0]['certificate']['actual_integer_evidence']['native_source']
    native_files={'lazy_modular':'sep26-shor-general/optimization/lazy_modular/lazy_modular.py',
        'sparse_modular':'sep26-shor-general/sparse/sparse_modular.py',
        'typed_integer_prechecks':'sep26-shor-general/completion/typed_integer_prechecks.py'}
    for key,path in native_files.items():assert digest((ROOT.parent/path).read_bytes())==native['files_sha256'][key]
    groups={key:[] for key in ('production','typed_pair_comparator','positive_replay','negative_replay')}
    cases=[];total_pairs=0;coverage=Counter();all_hotspots={};segment_lengths=Counter()
    for index,case in enumerate(data['cases']):
        cert=case['certificate'];replay=case['verification']['replay_certificate'];brute=case['typed_enumeration']
        assert cert['schema']==SCHEMA and cert['source_sha256']==data['source_sha256']['top_bit_general.py']
        pins=source_pins(cert)
        assert semantic(cert)==semantic(replay)
        same(case['inputs'],{k:cert['requests'][0]['inputs'][k] for k in ('g','ell','k','R')})
        assert len(cert['requests'])==case['inputs']['R']
        assert [req['inputs']['r'] for req in cert['requests']]==list(range(case['inputs']['R']))
        for item,cat,field in ((cert,'production','production_cost'),(replay,'positive_replay','positive_replay_cost'),(brute,'typed_pair_comparator','typed_enumeration_cost')):
            e=item['actual_integer_evidence'];inspect_evidence(e,native);groups[cat].append(e)
            same(cost_record(e),case[field])
        TopCursor(cert['actual_integer_evidence']).requests(cert)
        TopCursor(replay['actual_integer_evidence']).requests(replay)
        values,pairs=inspect_pairs(brute,case['inputs']);total_pairs+=pairs
        same(values,case['values']);same(values,[req['value'] for req in cert['requests']])
        assert case['all_residues_equal'] is True and case['verification']['verified'] is True
        assert case['verification']['requests_replayed']==case['inputs']['R']
        same(case['verification']['replay_arithmetic_stats'],replay['actual_integer_evidence']['arithmetic_stats'])
        hotspots=production_hotspots(cert)
        for name,row in hotspots.items():all_hotspots.setdefault(name,Counter()).update(row)
        metric=Counter()
        for req in cert['requests']:
            metric['requests']+=1;metric['top_level_tables']+=req['top_level_table_calls']
            for o in req['orientations']:
                metric['orientations']+=1;metric['empty_orientations']+=int(o['empty'])
                for s in o['segments']:
                    metric['segments']+=1;metric['empty_segments']+=int(s['empty'])
                    metric['nonempty_segments']+=int(not s['empty'])
                    segment_lengths[s['n']]+=1
                    if not s['empty']:metric['exact_thirds']+=1
        coverage.update(metric)
        cases.append({'inputs':case['inputs'],'values':values,'typed_pairs_read':pairs,
            'production_digits':case['production_cost']['arithmetic_stats']['adder_digit_replays'],
            'typed_comparator_digits':case['typed_enumeration_cost']['arithmetic_stats']['adder_digit_replays'],
            'positive_replay_digits':case['positive_replay_cost']['arithmetic_stats']['adder_digit_replays'],
            'structural_counts':dict(metric),'production_hotspots':hotspots})
    assert len(cases)==6 and total_pairs==720 and coverage['requests']==37
    for key in ('requests','segments','nonempty_segments'):assert data['coverage'][key]==coverage[key]
    assert data['coverage']['top_level_table_calls']==coverage['top_level_tables']
    same(data['coverage'],summary['coverage'])
    boundary=data['production_boundary_rejection']
    assert boundary['rejected'] is True and boundary['reuse_completed_by_original_grid'] is True
    assert boundary['state_and_paid_evidence_unchanged'] is True
    assert boundary['additional_native_calls']==boundary['additional_typed_operations']==0
    same(boundary['before'],boundary['after'])
    inspect_partial(boundary['before'],data['cases'][0]['certificate'],native)
    assert boundary['native_subinterval']['start']==boundary['native_subinterval']['stop']
    for row in data['input_rejections']:
        assert row['rejected'] is True and row['actual_typed_operations']==0
        assert row['call_interval']['start']==row['call_interval']['stop']
    assert len(data['input_rejections'])==12
    negrows=[];negkinds=Counter()
    for row in data['negative_checks']:
        assert row['rejected'] is True
        original=data['cases'][row['source_case_index']]['certificate']
        attempted=decode_keys(row['attempted_certificate_typed_key_encoding'])
        assert row['attempted_certificate_typed_key_encoding']!=encode_keys(original)
        captures=row['actual_replay_certificates'];negkinds[row['kind']]+=1
        if row['name'].endswith('_early'):
            assert not captures and row['call_interval']['start']==row['call_interval']['stop']
            if row['name']=='bool_input_early':assert type(attempted['requests'][0]['inputs']['g']) is bool
            if row['name']=='nonstring_key_early':assert 0 in attempted['requests'][0]
        else:
            assert len(captures)==1
            capture=captures[0]
            if row['name']=='valid_prefix_then_invalid_non_top':
                inspect_partial(capture,original,native)
                assert attempted['requests'][1]['inputs']['g']==4
            else:
                assert semantic(capture)==semantic(original)
                inspect_evidence(capture['actual_integer_evidence'],native)
                TopCursor(capture['actual_integer_evidence']).requests(capture)
            groups['negative_replay'].append(capture['actual_integer_evidence'])
        negrows.append({'name':row['name'],'kind':row['kind'],'error':row['error'],
            'receipts':len(captures),'digits':sum(c['actual_integer_evidence']['arithmetic_stats']['adder_digit_replays'] for c in captures)})
    assert len(negrows)==14 and len(groups['negative_replay'])==10
    same(dict(negkinds),summary['negative_kinds'])
    resources={key:costs(rows) for key,rows in groups.items()}
    same(resources,data['cost_categories']);same(resources,summary['cost_categories'])
    frontier=0;native_by=Counter()
    for row in data['call_intervals']:
        assert row['start']==frontier and row['stop']>=frontier
        native_by[row['category']]+=row['stop']-row['start'];frontier=row['stop']
    assert frontier==len(data['actual_core_calls'])==summary['actual_core_call_count']==1
    same(dict(native_by),data['native_calls_by_category']);same(dict(native_by),summary['native_calls_by_category'])
    same(data['call_intervals'],summary['call_intervals'])
    assert sum(e['arithmetic_stats']['native_kernel_calls_delta'] for rows in groups.values() for e in rows)==1
    assert data['actual_core_calls'][0]['states']==12 and data['actual_core_calls'][0]['depth']==1
    assert data['actual_core_calls'][0]['entrypoint']=='recurrent_mass_power'
    assert data['new_typed_pair_comparator_executions']==6 and data['historical_science_reexecuted'] is False
    log=(ROOT/'TOP_BIT_GENERAL_EXECUTION_LOG.txt').read_bytes()
    text=log.decode('utf-8-sig');lines=[json.loads(line) for line in text.splitlines() if line.strip().startswith('{')]
    assert len([line for line in lines if line.get('stage')=='CASE_COMPLETE'])==6
    same(lines[-1],summary)
    total=sum(row['sum']['adder_digit_replays'] for row in resources.values())
    result={'status':'PASS_FULL_AUTHOR_SAVED_EVIDENCE_READBACK','scientific_execution_performed':False,
        'reader_sha256':digest(Path(__file__).read_bytes()),'source_sha256':data['source_sha256'],
        'proof_and_helper_pins':pins,'comparator_source':comp,'payload_sha256':RAW_PIN,'artifact_sha256':GZIP_PIN,
        'raw_bytes':len(raw),'gzip_bytes':len(compressed),'summary_sha256':digest((ROOT/'TOP_BIT_GENERAL_SUMMARY.json').read_bytes()),
        'log_sha256':digest(log),'guard_sha256':digest(guard),'case_rows':cases,'cost_categories':resources,
        'all_disjoint_current_streams_read':sum(len(rows) for rows in groups.values()),'current_total_adder_digits':total,
        'typed_pair_records_read':total_pairs,'structural_counts':dict(coverage),
        'production_segment_length_counts':{str(k):v for k,v in sorted(segment_lengths.items())},
        'production_hotspots':{k:dict(v) for k,v in sorted(all_hotspots.items())},
        'negative_checks':negrows,'negative_kinds':dict(negkinds),'input_rejections':12,
        'boundary_before_after_equal':True,'boundary_cost_counted_once_inside_first_production':True,
        'native_source':native,'actual_core_calls':data['actual_core_calls'],'native_calls_by_category':dict(native_by),
        'elapsed_seconds_before_serialization':data['elapsed_seconds_before_serialization'],
        'production_below_typed_comparator_cases':sum(c['production_digits']<c['typed_comparator_digits'] for c in cases),
        'failure_artifact_present':(ROOT/'TOP_BIT_GENERAL_FAILED_EXECUTION.json.gz').exists(),
        'scope':'All retained outer expression links, signed-to-typed outputs, native cells, 720 recorded pair updates, complete/partial replay and disjoint cost accounting. No scientific recomputation.',
        'admission':'AUTHOR_SHARED_CONTEXT_READBACK_NOT_FORMAL_ADMISSION'}
    target=ROOT/'TOP_GENERAL_COST_READBACK.json'
    with target.open('x',encoding='utf-8') as f:f.write(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'reader_sha256':result['reader_sha256'],
        'record_sha256':digest(target.read_bytes()),'streams':result['all_disjoint_current_streams_read'],
        'digits':total,'production_hotspots':result['production_hotspots']}))


if __name__=='__main__':
    main()
