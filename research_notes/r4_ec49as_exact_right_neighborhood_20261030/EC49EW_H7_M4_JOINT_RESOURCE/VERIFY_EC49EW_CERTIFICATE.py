#!/usr/bin/env python3
"""Deterministic structural audit of the EC49EW finite certificates.

This checks the reported exhaustive-case coverage, witness arithmetic,
and lossy-free JSON encoding. Execute the exact DP sources to independently
recompute the mathematical lower bounds; this auditor is not a DP substitute.
"""
from pathlib import Path
import base64,gzip,json
from collections import Counter
root=Path(__file__).resolve().parent

def load(name):
    encoded=(root/(name+'.json.gz.b64')).read_text().strip()
    raw=gzip.decompress(base64.b64decode(encoded,validate=True))
    return json.loads(raw.decode('utf-8'))

s4=load('EC49EW_M4_S4_FULL_EXECUTED')
assert s4['status']=='PASS'
assert s4['all_horizon_4key_schedules']==752
assert s4['distinct_H6_prefixes_exactly_DP_solved']==389
assert s4['screened_by_exact_H6_plus_four_terminal_edge_bound']==686
assert s4['full_H7_trie_DP_solved']==66
rows=s4['cases']
assert len(rows)==66 and len({r['schedule_id'] for r in rows})==66
assert min(r['H7_exact_cost'] for r in rows)==92
assert all(r['H7_exact_cost']>=r['H6_exact_cost']+4 for r in rows)
assert sum(s4['DP_cost_frequency'].values())==66
assert dict(Counter(str(r['H7_exact_cost']) for r in rows))==s4['DP_cost_frequency']

mixed=load('EC49EW_T2T4_EXACT_EXECUTED')
assert mixed['status']=='PASS'
assert mixed['all_candidate_key_schedules']==72
assert mixed['complete_exact_DP_case_count']==72
assert mixed['minimum_E_in_subfamily']==72
assert len(mixed['all_cases'])==72
assert len({r['index'] for r in mixed['all_cases']})==72
assert all(r['exact_E']>=72 for r in mixed['all_cases'])
assert sum(r['exact_E']==72 for r in mixed['all_cases'])==4

ind=json.loads((root/'EC49EW_INDEPENDENT_EXECUTED.json').read_text())
assert ind['status']=='PASS'
assert ind['fully_enumerated_return_words']=={str(h):n for h,n in zip(range(2,8),[8,51,304,1770,10224,58947])}
assert ind['witness_S4']['E']==92 and ind['witness_S4']['M']==4 and ind['witness_S4']['S']==4
assert ind['witness_S6']['E']==72 and ind['witness_S6']['M']==4 and ind['witness_S6']['S']==6
assert all(d['rank']==9 for w in ('witness_S4','witness_S6') for d in ind[w]['horizons'].values())
milp=json.loads((root/'EC49EW_MILP_EXECUTED.json').read_text())
assert milp['status']=='PASS' and [c['expected'] for c in milp['cases']]==[92,72]
assert all(c['gap']==0 and c['solver_status']==0 and c['total_E']==c['dual_lower_bound']==c['expected'] for c in milp['cases'])
print(json.dumps({'status':'PASS','S4_full_schedules':752,'S4_exact_H6_prefixes':389,'S4_screened_H7':686,'S4_exact_H7':66,'S4_min_E':92,'mixed_full_schedules':72,'mixed_min_E':72,'independent_signed_X6':'PASS','MILP_witness_schedule':'PASS'},sort_keys=True))
