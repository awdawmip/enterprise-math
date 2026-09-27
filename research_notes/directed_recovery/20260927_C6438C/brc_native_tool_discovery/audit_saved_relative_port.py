"""Audit already saved receipts; never call a scientific propagator or sampler."""
from pathlib import Path
import gzip, hashlib, json

OUT = Path(__file__).resolve().parent
raw = gzip.decompress((OUT/'RELATIVE_PORT_RESULTS.json.gz').read_bytes())
data = json.loads(raw)
summary = json.loads((OUT/'RELATIVE_PORT_SUMMARY.json').read_bytes())
assert hashlib.sha256(raw).hexdigest() == summary['raw_sha256']
assert hashlib.sha256((OUT/'RELATIVE_PORT_RESULTS.json.gz').read_bytes()).hexdigest() == summary['gzip_sha256']
assert hashlib.sha256((OUT/'native_relative_port.py').read_bytes()).hexdigest() == data['binding']['new_source_sha256']
assert hashlib.sha256((OUT/'EXPERIMENT_PLAN.md').read_bytes()).hexdigest() == data['binding']['plan_sha256']
catalog = data['binding']['native_arithmetic']['native_adder']['columns']
if isinstance(catalog, dict):
    catalog = {int(k):v for k,v in catalog.items()}
checked = 0

def inspect(value):
    global checked
    if isinstance(value, dict):
        if 'cells' in value and 'low' in value and 'carry' in value:
            for _, code, digit, carry in value['cells']:
                assert catalog[code] == [digit, carry]
                checked += 1
        for item in value.values():
            inspect(item)
    elif isinstance(value, list):
        for item in value:
            inspect(item)

inspect(data)

def cost(route):
    digits = route['arithmetic_stats']['adder_digit_replays']
    digits += sum(t['stats']['setup_adder_digit_replays'] + t['stats']['column_adder_digit_replays']
                  for t in route['tables'].values())
    digits += sum(i['cost']['adder_digit_replays'] for i in route['inverses'].values())
    digits += sum(g['cost']['adder_digit_replays'] for g in route['gcds'].values())
    return {'route': route['name'], 'adder_digit_replays': digits, 'calls': route['calls'],
            'distinct_tables': len(route['tables']), 'distinct_inverses': len(route['inverses']),
            'distinct_gcd_observations': len(route['gcds'])}

cases = [{'inputs': c['inputs'], 'routes': [cost(r) for r in c['routes']]} for c in data['cases']]
negative = [cost(r) for r in data['negative_routes']]
reported = sum(r['adder_digit_replays'] for c in cases for r in c['routes'])
reported += sum(r['adder_digit_replays'] for r in negative)
assert reported == checked, (reported, checked)
assert data['native_catalog_calls'] == len(data['all_native_records']) == 1
assert data['all_native_records'][0]['entrypoint'] == 'recurrent_mass_power'
assert data['all_native_records'][0]['states'] == 12
assert data['all_native_records'][0]['depth'] == 1
result = {'status': 'FULL_SAVED_DIGIT_RECORD_AUDIT_PASS', 'native_catalog_calls': 1,
          'all_saved_digit_cells_checked': checked, 'all_costed_digit_replays': reported,
          'cases': cases, 'paid_negative_routes': negative,
          'scope': 'No scientific rerun; exact native catalog-cell matches and source/plan/raw hash audit. Histogram laws were tested by the recorded actual execution.'}
(OUT/'SAVED_RECORD_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
