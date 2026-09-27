"""Stdlib-only audit of saved conic/trace records; no scientific imports/run.

Reuses only selected AST definition nodes of a hash-pinned saved-record reader.
The old reader's top-level I/O and experiment audit are not executed. All
modular, inverse and gcd values come from saved typed traces/catalog columns.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import ast
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
sha = lambda b: hashlib.sha256(b).hexdigest()
READER_PIN = 'dc88b155de7ec5bf8222b940a942f08d4963e478f9a5bf66c5826d244b7d2825'
OLD_GZ = '5a9c055dc879a9a8b33620055183b41131d739d03c735ff37a1ed67704aeca26'
OLD_RAW = '6a111ca626f3330d16d513a15bfc31923a8c990723108e99c65b61fa5d229d28'
PINS = {
    'conic_transport': ('CONIC', 'conic_transport.py',
        '420ab2e9502fd45fd2dab85da09a69a129f8a63e95fee17eb9d895d6a9c18d65',
        'b8ce9ebb39124c4a2eba25ad24ad4b998bff9601aa4c79affb617e62483622e5',
        '2ab5d7853310c2a1b9240c51f629b3374ee938f8a4eb75ef0d88a2711c253c75',
        'fc18630a78ffbec5d89d59ac84d8ab21f884f028631e3ac0d4a4c1522c9e8b4e'),
    'trace_conflict': ('TRACE', 'trace_conflict.py',
        '1d90a5f0842b33cc42c7b693b9ed10d3984cdfa46d878df798e862fd16737fe6',
        'c858812b1c05a8d25e8dbb9aaa318752de3aac90f8f7f04fafa86df20688cf55',
        'ddf89398fe9b7f9c3ffc9eae107ad52c56ba4629456b65b237bb22e8047b340f',
        '3ef68050df8f49a4e232a82b082b4e1a703076651fa0f0ffbd9af4718717600f'),
}
reader = (ROOT/'read_native_port_review.py').read_bytes()
assert sha(reader) == READER_PIN
oldgz = (ROOT/'RELATIVE_PORT_RESULTS.json.gz').read_bytes()
oldraw = gzip.decompress(oldgz)
assert (sha(oldgz),sha(oldraw)) == (OLD_GZ,OLD_RAW)
baseline = json.loads(oldraw)
data = {'binding': baseline['binding']}
catalog = data['binding']['native_arithmetic']['native_adder']['columns']
counts = Counter()
selected = {'trace','stream','inverse','gcd','audit_route','Records','decoded',
            'deposit','observe_final'}
tree = ast.parse(reader)
nodes = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))
         and n.name in selected]
assert {n.name for n in nodes} == selected
exec(compile(ast.Module(body=nodes,type_ignores=[]),'<frozen-record-reader-definitions>','exec'),globals())

for path,pin in data['binding']['files'].items():
    assert sha(Path(path).read_bytes()) == pin
assert sha((ROOT/'native_relative_port.py').read_bytes()) == data['binding']['new_source_sha256']
assert sha((ROOT/'EXPERIMENT_PLAN.md').read_bytes()) == data['binding']['plan_sha256']
for name,path in {
    'sparse_modular': 'D:/em/TEMP/sep26-shor-general/sparse/sparse_modular.py',
    'typed_integer_prechecks': 'D:/em/TEMP/sep26-shor-general/completion/typed_integer_prechecks.py',
}.items():
    assert sha(Path(path).read_bytes()) == data['binding']['native_arithmetic']['files_sha256'][name]
hp=Path('D:/em/TEMP/sep26-local-takeover/activity_closeout/src/enterprise_math/brc_histogram.py').read_bytes()
assert hashlib.sha1(b'blob '+str(len(hp)).encode()+b'\0'+hp).hexdigest()==data['binding']['histogram_blob']
vp=Path('D:/em/TEMP/sep26-local-takeover/intake_brc/stage87-source/stage45/vendor/brc_weighted_recurrent.py').read_bytes()
assert sha(vp)==data['binding']['native_arithmetic']['native_adder']['vendor']['sha256']

loaded={}; summaries={}; pins={}
for directory,(prefix,source,sourcepin,planpin,rawpin,gzpin) in PINS.items():
    folder=ROOT/directory
    compressed=(folder/(prefix+'_RESULTS.json.gz')).read_bytes()
    raw=gzip.decompress(compressed); payload=json.loads(raw)
    summary=json.loads((folder/(prefix+'_SUMMARY.json')).read_bytes())
    assert sha(raw)==rawpin==summary['raw_sha256']
    assert sha(compressed)==gzpin==summary['gzip_sha256']
    assert len(raw)==summary['raw_bytes']
    assert sha((folder/source).read_bytes())==sourcepin==payload['binding']['source_sha256']
    assert sha((folder/'EXPERIMENT_PLAN.md').read_bytes())==planpin==payload['binding']['plan_sha256']
    assert sha((ROOT/'STARTUP_GUARD.json').read_bytes())==payload['binding']['guard_sha256']
    started=json.loads((folder/'STARTED.json').read_bytes())
    assert started=={k:v for k,v in payload['binding'].items() if k!='reused_interfaces'}
    assert payload['binding']['reused_interfaces']==data['binding']
    assert len(payload['all_native_records'])==payload['native_catalog_calls']==summary['native_catalog_calls']==1
    call=payload['all_native_records'][0]
    assert (call['entrypoint'],call['states'],call['depth'])==('recurrent_mass_power',12,1)
    assert isinstance(call['elapsed_ns'],int) and call['elapsed_ns']>=0
    loaded[directory]=payload; summaries[directory]=summary
    pins[directory]={'source_sha256':sourcepin,'plan_sha256':planpin,
        'raw_sha256':rawpin,'raw_bytes':len(raw),'gzip_sha256':gzpin,
        'gzip_bytes':len(compressed),'summary_sha256':sha((folder/(prefix+'_SUMMARY.json')).read_bytes()),
        'native_records':payload['all_native_records']}
guard=json.loads((ROOT/'STARTUP_GUARD.json').read_bytes())
assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
assert guard['record_sha256']=='aad2a53ba51160513368bd8a966fce8c6d20c2d37a21c7348f59a280d3fe8db6'
conic=loaded['conic_transport']; trace_payload=loaded['trace_conflict']
assert trace_payload['binding']['conic_raw_sha256']==PINS['conic_transport'][4]
assert trace_payload['binding']['conic_gzip_sha256']==PINS['conic_transport'][5]
assert conic['binding']['saved_baseline']=={'native_relative_port.py':data['binding']['new_source_sha256'],
                                          'RELATIVE_PORT_RESULTS.json.gz':OLD_GZ}


def modmul(r,a,b,ids=None):
    start=r.pos
    m=r.op('multiply'); assert (m['left'],m['right'])==(a,b)
    d=r.op('divide'); assert (d['value'],d['modulus'])==(m['value'],r.r['N'])
    if ids is not None:
        assert ids=={'multiply_operation':start,'division_operation':start+1}
    return d['remainder']


def trace_key(r,point,receipt):
    assert receipt['point']==list(point)
    start=r.pos
    a=r.op('add'); assert (a['left'],a['right'])==tuple(point)
    d=r.op('divide'); assert (d['value'],d['modulus'])==(a['low'],r.r['N'])
    assert (receipt['addition'],receipt['reduction'])==(start,start+1)
    assert receipt['key']==d['remainder']
    return receipt['key']


def classify(r,u,v):
    g=r.observe(u,v)
    return {'left_unit':u,'right_unit':v,'gcd':g,
            'kind':'SAME' if g==r.r['N'] else 'INVERSE' if g==1 else 'FACTOR'}


def digits(route):
    return (route['arithmetic_stats']['adder_digit_replays']
            +sum(x['stats']['setup_adder_digit_replays']+x['stats']['column_adder_digit_replays'] for x in route['tables'].values())
            +sum(x['cost']['adder_digit_replays'] for x in route['inverses'].values())
            +sum(x['cost']['adder_digit_replays'] for x in route['gcds'].values()))


one=Counter({Fraction(1):1}); atom=Counter({Fraction(1,4):1}); double=Counter({Fraction(1,4):2})
conic_records=[]; total=Counter(); category=Counter(); checked_live=0
for case,old,summary in zip(conic['cases'],baseline['cases'],summaries['conic_transport']['cases'],strict=True):
    assert case['inputs']==old['inputs']==summary['inputs']
    audits=[audit_route(r) for r in case['routes']]
    for r,audit in zip(case['routes'],audits):
        assert audit['total']['adder_digit_replays']==digits(r)==summary['new_costs'][r['name']]
        total.update(audit['total']); category[r['name']]+=audit['total']['adder_digit_replays']
    assert summary['saved_baseline_costs']=={r['name']:digits(r) for r in old['routes']}
    r,schedule,validator=[Records(r) for r in case['routes']]
    assert not r.r['inverses'] and not r.r['folds']
    state={('LIVE',1,1):one}; c=case['inputs']['a']; layer_records=[]
    for depth,(saved,previous) in enumerate(zip(case['layers'],old['layers'],strict=True),1):
        assert saved['depth']==depth and saved['multiplier']==c==previous['multiplier']
        invc=r.table(c)['permutation']['inverse_certificate']['inverse_multiplier']
        out={}
        for key,packet in sorted(state.items()):
            if key[0]=='FACTOR': deposit(out,key,packet,one,r); continue
            u,v=key[1:]
            candidates=[(u,v,double),(r.mul(c,u),r.mul(invc,v),atom),(r.mul(invc,u),r.mul(c,v),atom)]
            for x,y,weight in candidates:
                g=r.observe(x,1)
                if 1<g<r.r['N']: destination=('FACTOR',g,depth)
                else:
                    relation,_=r.compare(x,y)
                    destination=('LIVE',x,y) if relation<=0 else ('LIVE',y,x)
                deposit(out,destination,packet,weight,r)
        state=out; assert state==decoded(saved['states'])
        live=[key for key in sorted(state) if key[0]=='LIVE']
        assert len(live)==len(saved['invariant_receipts'])
        for key,receipt in zip(live,saved['invariant_receipts'],strict=True):
            assert receipt['point']==list(key[1:])
            assert modmul(validator,*key[1:],receipt['operation'])==receipt['product']==1
            checked_live+=1
        projection={}
        for key,packet in state.items():
            dest=key if key[0]=='FACTOR' else ('LIVE',key[1])
            projection.setdefault(dest,Counter()).update(packet)
        assert projection==decoded(previous['folded'])
        assert saved['saved_folded_histogram_equal'] is True
        assert sum(w*n for packet in state.values() for w,n in packet.items())==1
        layer_records.append({'depth':depth,'live_count':len(live),'full_histogram_equal':True})
        if depth<case['inputs']['layers']: c=schedule.square(c)
    assert observe_final(state)==decoded(case['output'])==decoded(old['output'])==decoded(summary['output'])
    for record in (r,schedule,validator): record.close()
    conic_records.append({'inputs':case['inputs'],'layers':layer_records,'route_audits':audits,
                          'saved_costs':summary['saved_baseline_costs']})
negative=conic['negative']; na=audit_route(negative['route']); nr=Records(negative['route'])
assert modmul(nr,*negative['point'],negative['operation'])==negative['product']!=1
assert negative['rejected'] is True and negative['N']==nr.r['N']==15
nr.close();total.update(na['total']);category['negative_nonconic']+=na['total']['adder_digit_replays']
assert category['negative_nonconic']==summaries['conic_transport']['negative_digits']

cut_records=[]; trace_cost=Counter(); trace_total=Counter()
all_cuts=[(case,layer) for case in conic['cases'] for layer in case['layers']]
for cut,(case,layer),summary in zip(trace_payload['cuts'],all_cuts,summaries['trace_conflict']['cuts'],strict=True):
    assert cut['inputs']==case['inputs']==summary['inputs'] and cut['depth']==layer['depth']==summary['depth']
    audit=audit_route(cut['route']); r=Records(cut['route'])
    rows=[row for row in layer['states'] if row['port'][0]=='LIVE']
    assert len(rows)==len(cut['trace_points'])
    reps={}; collisions=[]
    for row,record in zip(rows,cut['trace_points'],strict=True):
        point=row['port'][1:]
        assert any(x['point']==point and x['product']==1 for x in layer['invariant_receipts'])
        assert record['histogram']==row['histogram']
        key=trace_key(r,point,record)
        if key in reps:
            previous=reps[key]
            collisions.append({'key':key,'left_point':previous,'right_point':point,**classify(r,previous[0],point[0])})
        else: reps[key]=point
    assert collisions==cut['collisions']==summary['collisions']
    r.close()
    assert audit['total']['adder_digit_replays']==summary['added_readout_digits']
    trace_total.update(audit['total']); trace_cost['cut_readout']+=audit['total']['adder_digit_replays']
    cut_records.append({'inputs':cut['inputs'],'depth':cut['depth'],'trace_points':len(rows),
                        'collisions':collisions,'route_audit':audit})
fixture_records=[]
fixtures=[(7,2,2),(7,2,4),(15,2,8),(25,1,6),(35,2,4)]
for f,(N,u,v),summary in zip(trace_payload['fixtures'],fixtures,summaries['trace_conflict']['fixtures'],strict=True):
    audit=audit_route(f['route']); r=Records(f['route'])
    assert f['N']==N==r.r['N']==summary['N']
    p=[u,r.inv(u)];q=[v,r.inv(v)]
    first=trace_key(r,p,f['left']);second=trace_key(r,q,f['right'])
    result=classify(r,u,v) if first==second else {'kind':'DISTINCT_TRACE'}
    assert result==f['result']==summary['result'] and p==summary['left'] and q==summary['right']
    r.close(); assert audit['total']['adder_digit_replays']==summary['all_fixture_digits']
    trace_total.update(audit['total']);trace_cost['fixtures']+=audit['total']['adder_digit_replays']
    fixture_records.append({'N':N,'left':p,'right':q,'result':result,'route_audit':audit})
assert [x['result']['kind'] for x in fixture_records]==['SAME','INVERSE','FACTOR','FACTOR','DISTINCT_TRACE']
collisions=[(c['inputs'],c['depth'],x) for c in cut_records for x in c['collisions']]
assert collisions==[({'N':35,'a':2,'layers':3},3,{'key':20,'left_point':[2,18],
    'right_point':[23,32],'kind':'FACTOR','left_unit':2,'right_unit':23,'gcd':7})]
all_total=total+trace_total
assert all_total['adder_digit_replays']==counts['checked_native_digit_cells']
assert all_total['typed_operations']==counts['checked_top_level_operations']
report={'status':'PASS_STDLIB_SAVED_GEOMETRIC_RECORD_REVIEW_NOT_ADMISSION',
    'reader_sha256':sha(Path(__file__).read_bytes()),'frozen_helper_sha256':READER_PIN,
    'source_pins':pins,'baseline_raw_sha256':OLD_RAW,'baseline_gzip_sha256':OLD_GZ,
    'guard_sha256':sha((ROOT/'STARTUP_GUARD.json').read_bytes()),
    'complete_counts':dict(counts),'conic_totals':dict(total),'conic_digit_categories':dict(category),
    'trace_totals':dict(trace_total),'trace_digit_categories':dict(trace_cost),'combined_totals':dict(all_total),
    'retained_conic_points_checked':checked_live,'conic_cases':conic_records,
    'trace_cuts':cut_records,'trace_fixtures':fixture_records,'population_collisions':collisions,
    'scope':['No scientific imports, pow/mod/gcd reference calculation or kernel rerun.',
             'Saved arithmetic digit wiring checked against saved source-bound native full-adder columns.',
             'Both actual global native records retained; no new native calls in this review.',
             'Histogram reconstruction is saved-record verification, not a new scientific experiment.',
             'Cut readout cost excludes the separately paid population generation.',
             'Local factor discovery on two retained branches is not an end-to-end success probability.']}
target=ROOT/'GEOMETRIC_EXECUTION_REVIEW_RECORD.json'
target.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ('status','complete_counts','conic_digit_categories','trace_digit_categories','combined_totals','population_collisions')},indent=2))
