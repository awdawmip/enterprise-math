"""Stdlib-only saved-record audit; no scientific imports or modular oracle.

Consumes recorded arithmetic outputs and column lookups, checks digit wiring
against the saved native catalog, and reassembles saved histogram transitions.
It does not execute the instrument or calculate pow/gcd/modular answers.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
sha = lambda b: hashlib.sha256(b).hexdigest()
packed = (ROOT/'RELATIVE_PORT_RESULTS.json.gz').read_bytes()
raw = gzip.decompress(packed)
data = json.loads(raw)
summary = json.loads((ROOT/'RELATIVE_PORT_SUMMARY.json').read_text(encoding='utf-8'))
assert len(raw) == summary['raw_bytes'] and sha(raw) == summary['raw_sha256']
assert sha(packed) == summary['gzip_sha256']
assert sha((ROOT/'native_relative_port.py').read_bytes()) == data['binding']['new_source_sha256']
assert sha((ROOT/'EXPERIMENT_PLAN.md').read_bytes()) == data['binding']['plan_sha256']
for path, expected in data['binding']['files'].items():
    assert sha(Path(path).read_bytes()) == expected
source_paths = {
    'histogram': Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py'),
    'sparse_modular': Path('D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py'),
    'typed_integer_prechecks': Path('D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py'),
    'vendor': Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py'),
}
checked_sources = {name: sha(path.read_bytes()) for name,path in source_paths.items()}
for name in ('sparse_modular','typed_integer_prechecks'):
    assert checked_sources[name] == data['binding']['native_arithmetic']['files_sha256'][name]
hraw=source_paths['histogram'].read_bytes()
assert hashlib.sha1(b'blob '+str(len(hraw)).encode()+b'\0'+hraw).hexdigest() == data['binding']['histogram_blob']
assert checked_sources['vendor'] == data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']
catalog = data['binding']['native_arithmetic']['native_adder']['columns']
counts = Counter()


def trace(t):
    """Check only retained wiring and links, not arithmetic via host operators."""
    if 'cells' in t:
        carry = 0
        low = 0
        assert len(t['cells']) == t['width']
        for bit, col, s, c in t['cells']:
            assert col == (((t['left'] >> bit) & 1) << 2) | (((t['right'] >> bit) & 1) << 1) | carry
            assert [s, c] == catalog[col]
            low |= s << bit
            carry = c
        assert (low, carry) == (t['low'], t['carry'])
        counts['checked_native_digit_cells'] += len(t['cells'])
        return Counter(adder_digit_replays=len(t['cells']), host_bit_wiring_operations=10*len(t['cells']))
    op = t['operation']
    if op == 'BRC_UNSIGNED_COMPARE':
        first, second = t['first_add'], t['second_add']
        assert t['bitwise_complement'] == (~t['right']) & ((1 << t['width'])-1)
        assert (first['left'], first['right'], first['width']) == (t['left'], t['bitwise_complement'], t['width'])
        assert (second['left'], second['right'], second['width']) == (first['low'], 1, t['width'])
        assert t['low_difference'] == second['low']
        nonnegative = bool(first['carry'] or second['carry'])
        assert t['nonnegative'] is nonnegative
        relation = 0 if nonnegative and second['low'] == 0 else 1 if nonnegative else -1
        assert relation == t['relation']
        return trace(first)+trace(second)+Counter(host_bit_wiring_operations=3,host_bit_length_calls_in_arithmetic=2)
    if op == 'BRC_UNSIGNED_SHIFT_ADD':
        result = Counter(host_bit_wiring_operations=3*len(t['steps']),host_bit_length_calls_in_arithmetic=3)
        value = 0
        assert len(t['steps']) == t['right'].bit_length()
        for bit, row in enumerate(t['steps']):
            assert row['bit'] == bit and row['input'] == value
            assert row['selected'] == ((t['right'] >> bit) & 1)
            assert row['wired_term'] == t['left'] << bit
            assert row['bypass'] is (not bool(row['selected']))
            if row['selected']:
                ad = row['adder']
                assert (ad['left'],ad['right'],ad['width']) == (value,row['wired_term'],t['width'])
                result += trace(ad)
                assert ad['carry'] == 0 and row['output'] == ad['low']
            else:
                assert row['adder'] is None and row['output'] == value
            value = row['output']
        assert t['value'] == value
        return result
    assert op == 'BRC_UNSIGNED_LONG_DIVISION'
    result = Counter(host_bit_wiring_operations=6*len(t['steps']),host_bit_length_calls_in_arithmetic=1)
    quotient = remainder = 0
    assert [v['bit'] for v in t['steps']] == list(reversed(range(t['value'].bit_length())))
    for row in t['steps']:
        assert row['input_remainder'] == remainder
        assert row['input_bit'] == (t['value'] >> row['bit']) & 1
        assert row['wired_shift'] == (remainder << 1) | row['input_bit']
        sub = row['subtract_modulus']
        assert (sub['left'],sub['right']) == (row['wired_shift'],t['modulus'])
        result += trace(sub)
        assert row['quotient_bit'] == int(sub['relation'] >= 0)
        assert row['output_remainder'] == (sub['low_difference'] if row['quotient_bit'] else row['wired_shift'])
        remainder = row['output_remainder']
        quotient = (quotient << 1) | row['quotient_bit']
    assert (quotient,remainder) == (t['quotient'],t['remainder'])
    return result


def stream(ops, cost):
    result = Counter(typed_operations=len(ops))
    counts['arithmetic_streams'] += 1
    for entry in ops:
        result += trace(entry['trace'])
        if entry['operation'] == 'add':
            result['host_bit_length_calls_in_arithmetic'] += 2
    for key in ('typed_operations','adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic'):
        assert result[key] == cost[key], (key,result,cost)
    counts['checked_top_level_operations'] += len(ops)
    return result


def inverse(cert, N, b):
    assert (cert['N'],cert['b'],cert['gcd'],cert['inverse_product']) == (N,b,1,1)
    ops=cert['arithmetic_operations']
    for row in cert['euclidean_steps']:
        div=ops[row['division_operation']]['trace']
        assert (div['value'],div['modulus'],div['quotient'],div['remainder']) == (row['r0'],row['r1'],row['quotient'],row['next_remainder'])
        ids=row['product_mod_operations']
        mul,red=ops[ids['multiply_operation']]['trace'],ops[ids['division_operation']]['trace']
        assert (mul['left'],mul['right']) == (row['quotient'],row['c1'])
        assert (red['value'],red['modulus'],red['remainder']) == (mul['value'],N,row['product_mod'])
    ids=cert['inverse_product_operations']
    mul,red=ops[ids['multiply_operation']]['trace'],ops[ids['division_operation']]['trace']
    assert (mul['left'],mul['right']) == (b,cert['inverse_multiplier'])
    assert (red['value'],red['modulus'],red['remainder']) == (mul['value'],N,1)
    return stream(ops,cert['cost'])


def gcd(cert, N, d):
    assert (cert['left'],cert['right']) == (d,N)
    assert cert['source'] == data['binding']['native_arithmetic']
    assert cert['gcd_source_sha256'] == data['binding']['files'][next(p for p in data['binding']['files'] if p.endswith('lazy_gcd.py'))]
    assert not cert['host_remainder_used'] and not cert['dense_euclidean_graph_used']
    a,b=d,N
    for row in cert['steps']:
        t=cert['arithmetic_operations'][row['division_operation']]['trace']
        assert (row['left'],row['right']) == (a,b)
        assert (t['value'],t['modulus'],t['quotient'],t['remainder']) == (a,b,row['quotient'],row['remainder'])
        a,b=b,row['remainder']
    assert b == 0 and a == cert['value']
    return stream(cert['arithmetic_operations'],cert['cost'])


def audit_route(route):
    N=route['N']
    parts={'direct':stream(route['arithmetic_operations'],route['arithmetic_stats']),
           'table_setup':Counter(),'columns':Counter(),'standalone_inverse':Counter(),'gcd':Counter()}
    for c,table in route['tables'].items():
        p=table['permutation']
        assert (p['N'],p['b']) == (N,int(c)) and p['source'] == data['binding']['native_arithmetic']
        assert sha(json.dumps(p,sort_keys=True,separators=(',',':')).encode()) == table['permutation_sha256']
        setup=inverse(p['inverse_certificate'],N,int(c)); parts['table_setup'] += setup
        columns=Counter()
        for col in table['queried_columns']:
            assert col['N'] == N and col['b'] == int(c) and not col['identity_tail']
            assert col['permutation_certificate_sha256'] == table['permutation_sha256']
            ids=col['product_operations']; ops=col['arithmetic_operations']
            mul,red=ops[ids['multiply_operation']]['trace'],ops[ids['division_operation']]['trace']
            assert (mul['left'],mul['right']) == (int(c),col['source'])
            assert (red['value'],red['modulus'],red['remainder']) == (mul['value'],N,col['target'])
            columns += stream(ops,col['arithmetic_cost'])
        parts['columns'] += columns
        for name in ('adder_digit_replays','host_bit_wiring_operations','host_bit_length_calls_in_arithmetic'):
            assert table['stats']['setup_'+name] == setup[name]
            assert table['stats']['column_'+name] == columns[name]
        assert table['stats']['computed_columns'] == len(table['queried_columns'])
        assert table['stats']['column_requests'] == table['stats']['cache_hits']+table['stats']['computed_columns']
    for b,cert in route['inverses'].items(): parts['standalone_inverse'] += inverse(cert,N,int(b))
    for d,cert in route['gcds'].items(): parts['gcd'] += gcd(cert,N,int(d))
    for g,cert in route['factor_checks'].items():
        t=route['arithmetic_operations'][cert['typed_division_operation']]['trace']
        assert (t['value'],t['modulus'],t['quotient'],t['remainder']) == (N,int(g),cert['cofactor'],0)
        assert cert['factor'] == int(g) and cert['remainder'] == 0 and 1<int(g)<N and 1<cert['cofactor']<N
    return {'name':route['name'],'parts':{k:dict(v) for k,v in parts.items()},
            'total':dict(sum(parts.values(),Counter())), 'calls':route['calls']}


class Records:
    """Consumes the recorded outer wiring without computing modular answers."""
    def __init__(self,r):
        self.r=r; self.pos=0; self.calls=Counter(); self.gs=set();self.fs=set();self.ii=set();self.ff={};self.tt=set();self.requests=Counter()
    def op(self,name):
        row=self.r['arithmetic_operations'][self.pos];self.pos+=1
        assert row['operation']==name
        return row['trace']
    def compare(self,a,b):
        t=self.op('compare');assert (t['left'],t['right'])==(a,b)
        return t['relation'],t['low_difference']
    def inv(self,u):
        self.calls['inverse_requests']+=1;self.ii.add(str(u))
        return self.r['inverses'][str(u)]['inverse_multiplier']
    def table(self,c):
        self.tt.add(str(c));return self.r['tables'][str(c)]
    def mul(self,c,u):
        self.calls['multiply_column']+=1;self.requests[str(c)]+=1
        cols=self.table(c)['queried_columns']
        matches=[v['target'] for v in cols if v['source']==u]
        assert len(matches)==1
        return matches[0]
    def fold(self,u):
        if u not in self.ff:
            v=self.inv(u);rel,_=self.compare(u,v);self.ff[u]=u if rel<=0 else v
        assert self.ff[u]==self.r['folds'][str(u)]
        return self.ff[u]
    def observe(self,x,y):
        rel,d=self.compare(x,y)
        if rel<0:
            ad=self.op('add');assert (ad['left'],ad['right'])==(x,self.r['N'])
            rel,d=self.compare(ad['low'],y);assert rel>=0
        self.calls['gcd_requests']+=1;self.gs.add(str(d));g=self.r['gcds'][str(d)]['value']
        if 1<g<self.r['N'] and g not in self.fs:
            t=self.op('divide');assert (t['value'],t['modulus'],t['remainder'])==(self.r['N'],g,0)
            self.fs.add(g)
        return g
    def square(self,c):
        m=self.op('multiply');assert (m['left'],m['right'])==(c,c)
        d=self.op('divide');assert (d['value'],d['modulus'])==(m['value'],self.r['N'])
        return d['remainder']
    def close(self):
        assert self.pos==len(self.r['arithmetic_operations'])
        assert dict(self.calls)=={k:v for k,v in self.r['calls'].items() if v}
        assert self.gs==set(self.r['gcds']) and self.ii==set(self.r['inverses']) and self.tt==set(self.r['tables'])
        assert {str(k):v for k,v in self.ff.items()}==self.r['folds']
        assert {str(v) for v in self.fs}==set(self.r['factor_checks'])
        for c in self.tt: assert self.requests[c]==self.r['tables'][c]['stats']['column_requests']


def decoded(rows):
    return {tuple(row['port']):Counter({Fraction(a,b):c for a,b,c in row['histogram']}) for row in rows}


def deposit(out,key,parent,atom,r=None):
    if r:
        r.calls['histogram_serial']+=1;r.calls['histogram_recoalesce']+=1
    packet=Counter()
    for a,c in parent.items():
        for b,d in atom.items():packet[a*b]+=c*d
    out.setdefault(key,Counter()).update(packet)


one=Counter({Fraction(1):1}); atom=Counter({Fraction(1,4):1}); double=Counter({Fraction(1,4):2})


def recorded_layer(state,c,depth,r,kind,mutant=False):
    out={}
    if kind!='pair': invc=r.table(c)['permutation']['inverse_certificate']['inverse_multiplier']
    for key,packet in state.items():
        if key[0]=='FACTOR':deposit(out,key,packet,one,r);continue
        if kind=='pair':
            x,y=key[1:];cx,cy=r.mul(c,x),r.mul(c,y)
            edges=[(x,y,atom),(cx,y,atom),(x,cy,atom),(cx,cy,atom)]
        else:
            u=key[1];edges=[(u,1,atom if mutant else double),(r.mul(c,u),1,atom),(r.mul(invc,u),1,atom)]
        for x,y,weight in edges:
            g=r.observe(x,y)
            if 1<g<r.r['N']:port=('FACTOR',g,depth)
            elif kind=='pair':port=('LIVE',x,y)
            else:port=('LIVE',r.fold(x) if kind=='fold' else x)
            deposit(out,port,packet,weight,r)
    return out


def project(state,r,fold=False):
    out={}
    for key,packet in state.items():
        if key[0]=='FACTOR':port=key
        elif fold:port=('LIVE',r.fold(key[1]))
        else:port=('LIVE',r.mul(r.inv(key[2]),key[1]))
        out.setdefault(port,Counter()).update(packet)
    return out


def observe_final(state):
    out={}
    for key,packet in state.items():out.setdefault(key if key[0]=='FACTOR' else ('FAIL',),Counter()).update(packet)
    return out


results=[]
for case in data['cases']:
    route_costs=[audit_route(r) for r in case['routes']]
    pair,rel,fold,schedule,validation=[Records(r) for r in case['routes']]
    states=[{('LIVE',1,1):one},{('LIVE',1):one},{('LIVE',1):one}]
    c=case['inputs']['a']
    for depth,saved in enumerate(case['layers'],1):
        assert saved['multiplier']==c==case['multipliers'][depth-1]
        states=[recorded_layer(s,c,depth,r,k) for s,r,k in zip(states,(pair,rel,fold),('pair','relative','fold'))]
        assert states[0]==decoded(saved['pair']) and states[1]==decoded(saved['relative']) and states[2]==decoded(saved['folded'])
        assert project(states[0],validation)==states[1]
        assert project(states[1],validation,True)==states[2]
        for state in states:assert sum(w*n for p in state.values() for w,n in p.items())==1
        counts['full_layer_histogram_equalities']+=2
        if depth<case['inputs']['layers']:c=schedule.square(c)
    for state in states:assert observe_final(state)==decoded(case['output'])
    for r in (pair,rel,fold,schedule,validation):r.close()
    results.append({'inputs':case['inputs'],'route_costs':route_costs})
negative_costs=[audit_route(r) for r in data['negative_routes']]
neg,mut=[Records(r) for r in data['negative_routes']]
for row in data['negative_gcd_key']:
    x,y=row['pair'];assert neg.observe(x,y)==row['before_gcd']
    assert neg.observe(neg.mul(2,x),y)==row['after_left_2_gcd']
assert data['negative_gcd_key'][0]['before_gcd']==data['negative_gcd_key'][1]['before_gcd']
assert data['negative_gcd_key'][0]['after_left_2_gcd']!=data['negative_gcd_key'][1]['after_left_2_gcd']
mutated=recorded_layer({('LIVE',1):one},2,1,mut,'relative',True)
assert sum(w*n for p in mutated.values() for w,n in p.items())==Fraction(data['mutant_mass']['numerator'],data['mutant_mass']['denominator'])!=1
neg.close();mut.close()
assert len(data['all_native_records'])==data['native_catalog_calls']==summary['total_native_calls']==1
report={'status':'PASS_SAVED_RECORD_CONSISTENCY_SHARED_CONTEXT_NOT_ADMITTED',
        'scientific_imports':0,'new_scientific_runs':0,'new_native_calls':0,
        'raw_sha256':sha(raw),'gzip_sha256':sha(packed),'raw_bytes':len(raw),'gzip_bytes':len(packed),
        'source_sha256':data['binding']['new_source_sha256'],'plan_sha256':data['binding']['plan_sha256'],
        'checked_dependency_sha256':checked_sources,
        'checked':dict(counts),'cases':results,'negative_route_costs':negative_costs,
        'total_cost':dict(sum((Counter(v['total']) for c in results for v in c['route_costs']),Counter())+sum((Counter(v['total']) for v in negative_costs),Counter())),
        'cost_boundary':'Recorded digit/wiring operations only. Route histogram counts exclude helper aggregations and Python overhead.',
        'scope':'Saved native columns and all digit/outer routing links checked. No independent modular/gcd reference or primitive core rerun.'}
out=ROOT/'NATIVE_PORT_REVIEW_RECORD.json'
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':report['status'],'checked':report['checked'],'total_cost':report['total_cost'],
                 'cost_by_case':[{**c['inputs'],'route_digits':{r['name']:r['total']['adder_digit_replays'] for r in c['route_costs']}} for c in results],
                 'review_record_sha256':sha(out.read_bytes())},indent=2))
