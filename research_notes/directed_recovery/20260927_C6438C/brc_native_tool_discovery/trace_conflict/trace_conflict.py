"""Paid trace-fiber readout of immutable native conic evidence."""
from pathlib import Path
import gzip, hashlib, json, sys, traceback

OUT = Path(__file__).resolve().parent
BASE = OUT.parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def save_new(name, raw):
    with (OUT/name).open('xb') as stream:
        stream.write(raw)


def main():
    guard_raw = (BASE/'STARTUP_GUARD.json').read_bytes()
    guard = json.loads(guard_raw)
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    assert guard['activity_id'] == 'RA-CAAAC604CB513AEA8BBC1DFC'
    source = BASE/'conic_transport/CONIC_RESULTS.json.gz'
    compressed = source.read_bytes()
    assert sha(compressed) == 'fc18630a78ffbec5d89d59ac84d8ab21f884f028631e3ac0d4a4c1522c9e8b4e'
    raw = gzip.decompress(compressed)
    assert sha(raw) == '2ab5d7853310c2a1b9240c51f629b3374ee938f8a4eb75ef0d88a2711c253c75'
    assert sha((BASE/'native_relative_port.py').read_bytes()) == '0821cf958b99988b5dbb95f5a42b97629155ca80c07e1f5bee8e2e9165bc39a8'
    binding = {'source_sha256':sha(Path(__file__).read_bytes()),
               'plan_sha256':sha((OUT/'EXPERIMENT_PLAN.md').read_bytes()),
               'guard_sha256':sha(guard_raw), 'conic_raw_sha256':sha(raw),
               'conic_gzip_sha256':sha(compressed)}
    save_new('STARTED.json', (json.dumps(binding,indent=2)+'\n').encode())
    try:
        execute(binding,json.loads(raw))
    except BaseException:
        save_new('FAILED.txt',traceback.format_exc().encode())
        raise


def execute(binding, saved):
    sys.path.insert(0,str(BASE))
    import native_relative_port as old
    binding['reused_interfaces'] = old.source_check()

    def trace(point, route):
        total, addition = route.arithmetic.add(*point)
        quotient, remainder, reduction = route.arithmetic.divide(total, route.N)
        return remainder, {'point':point, 'key':remainder, 'addition':addition, 'reduction':reduction}

    def classify(u,v,route):
        d = route.observe(u,v)
        return {'kind':'SAME' if d == route.N else 'INVERSE' if d == 1 else 'FACTOR',
                'left_unit':u, 'right_unit':v, 'gcd':d}

    cuts = []
    for case in saved['cases']:
        N = case['inputs']['N']
        for layer in case['layers']:
            route = old.Route(N, 'trace_cut_readout')
            representatives, traces, collisions = {}, [], []
            for row in layer['states']:
                if row['port'][0] != 'LIVE':
                    continue
                point = row['port'][1:]
                certificate = next(r for r in layer['invariant_receipts'] if r['point'] == point)
                assert certificate['product'] == 1
                key, receipt = trace(point,route)
                traces.append({**receipt,'histogram':row['histogram']})
                if key in representatives:
                    previous = representatives[key]
                    result = classify(previous[0],point[0],route)
                    collisions.append({'key':key,'left_point':previous,'right_point':point,**result})
                else:
                    representatives[key] = point
            cuts.append({'inputs':case['inputs'],'depth':layer['depth'],
                         'trace_points':traces,'collisions':collisions,'route':route.export()})

    fixtures=[]
    for N,u,v in [(7,2,2),(7,2,4),(15,2,8),(25,1,6),(35,2,4)]:
        route=old.Route(N,'typed_fixture')
        p,q=[u,route.inv(u)],[v,route.inv(v)]
        first,first_receipt=trace(p,route)
        second,second_receipt=trace(q,route)
        result=classify(u,v,route) if first == second else {'kind':'DISTINCT_TRACE'}
        fixtures.append({'N':N,'left':first_receipt,'right':second_receipt,
                         'result':result,'route':route.export()})
    # Assert interface classification, never supply factors to the classifier.
    assert [f['result']['kind'] for f in fixtures] == ['SAME','INVERSE','FACTOR','FACTOR','DISTINCT_TRACE']
    payload={'status':'PASS_TRACE_FIBER_READOUT_AUTHOR_NOT_ADMITTED','binding':binding,
             'cuts':cuts,'fixtures':fixtures,'native_catalog_calls':len(old.CALLS),
             'all_native_records':old.CALLS}
    raw=(json.dumps(payload,sort_keys=True,default=old.plain,separators=(',',':'))+'\n').encode()
    compressed=gzip.compress(raw,mtime=0)
    save_new('TRACE_RESULTS.json.gz',compressed)

    def cost(route):
        return (route['arithmetic_stats']['adder_digit_replays']
                +sum(t['stats']['setup_adder_digit_replays']+t['stats']['column_adder_digit_replays'] for t in route['tables'].values())
                +sum(i['cost']['adder_digit_replays'] for i in route['inverses'].values())
                +sum(g['cost']['adder_digit_replays'] for g in route['gcds'].values()))
    summary={'status':payload['status'],'raw_bytes':len(raw),'raw_sha256':sha(raw),
             'gzip_sha256':sha(compressed),'native_catalog_calls':len(old.CALLS),
             'cuts':[{'inputs':c['inputs'],'depth':c['depth'],'collisions':c['collisions'],
                      'added_readout_digits':cost(c['route'])} for c in cuts],
             'fixtures':[{'N':f['N'],'left':f['left']['point'],'right':f['right']['point'],
                          'result':f['result'],'all_fixture_digits':cost(f['route'])} for f in fixtures],
             'generation_cost_scope':'Input populations came from paid frozen conic execution; these readout-only costs are not end-to-end factorization costs.'}
    save_new('TRACE_SUMMARY.json',(json.dumps(summary,indent=2)+'\n').encode())
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
