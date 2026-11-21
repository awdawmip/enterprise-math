"""Quickly audit the merged receipts; this does not rerun the search."""
from pathlib import Path
import argparse, hashlib, json
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--bundle', type=Path, default=Path(__file__).resolve().parent)
a = p.parse_args(); h = a.bundle
read = lambda f: json.loads((h / f).read_text())
r = read('result_q2.json'); cases = read('completed_q2.json'); chunks = read('frame_chunks_q2.json')
plan = read('profiles_q2.json'); jobs = {j['key']: j for j in read('inheritance.json')['jobs']}
key = lambda P, E: ','.join(map(str, P)) + '__' + ','.join(map(str, E))
planned = {key(P, E): [P, E, f, B] for P, E, f, B in plan['rows']}
assert plan['q'] == 2 and plan['cap'] == 12043
assert r['complete_exclusion'] and r['candidate_test_includes_equality'] and r['all_bound_pruning_strict']
assert set(cases) == set(jobs) == set(planned) and len(cases) == 775 and len(chunks) == 2029
source = hashlib.sha256((h / 'search.cpp').read_bytes()).hexdigest()
assert source == r['source_sha256'] == '12035b70ca89275d7c8ff381436277c535ae44a2682456a35cfe4b892c323ad9'
parts = {k: [] for k in cases}; identities = set()
for c in chunks:
    s = c['spec']; k = s['key']; j = jobs[k]; P, E, f, B = planned[k]
    assert s['source_sha256'] == source and c['returncode'] == 0 and c['stdout'] == ''
    assert s['minimum_cost'] == j['minimum_cost'] and s['maximum_cost'] == B and s['embedded_floor'] == f
    frame = r['canonical_frame_catalogues'][f'f{len(E)}_{sum(E)}']
    assert s['frame_sha256'] == frame['sha256']
    first, end = s['first'], s['end']; identity = k, first, end
    assert identity not in identities and 0 <= first < end <= frame['canonical_rows']; identities.add(identity)
    assert c['counts'] == list(map(int, c['stderr'].split())) and c['counts'][0] == end - first and c['counts'][-1] == 0
    parts[k].append(c)
totals = [0] * 5
for k, entries in parts.items():
    entries.sort(key=lambda c: c['spec']['first']); cursor = 0; total = [0] * 5; ranges = []
    for c in entries:
        first, end = c['spec']['first'], c['spec']['end']; assert first == cursor; cursor = end
        total = [x + y for x, y in zip(total, c['counts'])]; ranges.append([first, end])
    E = jobs[k]['E']; expected = r['canonical_frame_catalogues'][f'f{len(E)}_{sum(E)}']['canonical_rows']
    assert cursor == expected == total[0] and total == cases[k]['counts'] and ranges == cases[k]['ranges']
    assert cases[k]['complete_profile_exclusion'] and cases[k]['source_sha256'] == source and cases[k]['job'] == jobs[k]
    totals = [x + y for x, y in zip(totals, total)]
assert totals == [r['family_profile_placements'], r['search_nodes'], r['class_emissions'], r['settlement_calls'], 0]
assert totals[0] == 7758668
summary = read('summary.json')
assert summary['complete_exclusion'] and summary['completed_profiles'] == summary['planned_profiles'] == 775
assert summary['source_sha256'] == source and not summary['witnesses'] and summary['completed_frame_chunks'] == 2029
assert summary['completed_profile_frames'] == totals[0] and summary['completed_profile_search_nodes'] == totals[1]
b = read('all_bound_verifications.json'); i = read('bound_identity.json')
assert b['complete_bound_verification'] and set(b['records']) == set(jobs)
assert i['active_source_sha256'] == source and i['verified_source_sha256'] == b['search_source_sha256']
assert hashlib.sha256((h / 'bound_reference_search.cpp').read_bytes()).hexdigest() == i['verified_source_sha256']
text = (h / 'search.cpp').read_text(); start = text.index(' // Complete single-class spectrum, typed as proper (0), embedded (1),'); end = text.index(' bool assign(', start)
assert hashlib.sha256(text[start:end].encode()).hexdigest() == i['fragment_sha256']
assert hashlib.sha256((h / 'typed_catalog.txt').read_bytes()).hexdigest() == b['typed_catalog_sha256']
for k, v in b['records'].items():
    assert v['verified'] and v['q'] == 2 and v['total_cost_window'] == [jobs[k]['minimum_cost'], jobs[k]['q2_ceiling']]
g = read('bound_regeneration.json')
assert g['complete_bound_verification'] and g['tables_regenerated'] == 775 and g['search_source_sha256'] == source
assert g['bound_fragment_sha256'] == i['fragment_sha256'] and set(g['records']) == set(jobs)
for k, v in g['records'].items():
    assert v['input_binding_verified'] and v['P'] == jobs[k]['P'] and v['E'] == jobs[k]['E'] and v['embedded_floor'] == jobs[k]['embedded_floor']
    assert v['table_sha256'] == b['records'][k]['table_sha256'] and v['total_cost_window'] == b['records'][k]['total_cost_window']
u = read('uniform_inherited_windows.json')
assert u['verified'] and u['q'] == 0 and u['profiles'] == 13 and u['total_frames'] == 52
assert {v['key'] for v in u['records']} == {k for k, j in jobs.items() if 'uniform_excluded_through' in j}
print(json.dumps({'verified': True, 'profiles': 775, 'chunks': 2029, 'counts': totals,
                  'equality_included': True, 'independent_bound_inequalities': b['total_bellman_inequalities']}, indent=2), flush=True)
