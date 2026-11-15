#!/usr/bin/env python3
"""EC49FQE exact rational audit of native BRC16943 multiplicity-prior phase diagram.
Runs on the EC49FQE_CONFIG_PRICE_FULL evidence archive (which contains the frozen
sources and complete 15 Bellman endpoint/feasible-tree certificates).
Independent 310-configuration replay is handled by EC49FQA_INDEPENDENT_REPLAY.py.
This audit checks saved exhaustive-solver outputs, not the solver's implementation.
"""
from pathlib import Path
from fractions import Fraction
import json
import hashlib
import sys

base=Path(sys.argv[1])
report=json.loads((base/'notes/EC49FQE_MACHINE_SUMMARY.json').read_text())
assert report['scientific_input_pin']=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
assert hashlib.sha256((base/'source/frozen_original_master.txt').read_bytes()).hexdigest()==report['original_master_sha256']
assert hashlib.sha256((base/'source/EC49FPG_PROFILE.csv').read_bytes()).hexdigest()==report['root_costs_sha256']
P=[(item['R'],item['T']) for item in report['phases']]
B=[Fraction(s) for s in report['breakpoints']]
assert len(P)==16 and len(B)==15 and B==sorted(set(B))
assert P[0]==(1033,0) and P[-1]==(4,688)
for i,x in enumerate(B,1):
    prev,cur=P[i-1],P[i]
    assert Fraction(cur[1]-prev[1],prev[0]-cur[0])==x
    c=json.loads((base/'certificates'/f'EC49FQE_{x.numerator}_{x.denominator}.json').read_text())
    assert c['frozen_scientific_commit']==report['scientific_input_pin']
    assert c['source_master_sha256']==report['original_master_sha256']
    assert c['native_root_costs_sha256']==report['root_costs_sha256']
    assert c['observation_scope']=='all_228'
    assert (c['config_count'],c['profile_count'],c['terminal_actions'],c['named_root_actions'])==(310,141,144,84)
    a,b=c['prices']['root'],c['prices']['terminal']
    assert Fraction(a,b)==x
    cost=c['optimal_total_config_weighted']
    assert prev[0]*a+prev[1]*b==cost
    assert cur[0]*a+cur[1]*b==cost
    assert min(c['first_query_costs_weighted'])==cost
    tree=c['replay']['config_weighted']
    assert tree['weighted_root_observations']*a+tree['weighted_terminal_observations']*b==cost
    print('GLOBAL_BELLMAN_ENDPOINT_PASS',str(x),cost)

# Every phase line needs one tree actually realizing that pair.
witness={(1033,0)}
for x in B:
    c=json.loads((base/'certificates'/f'EC49FQE_{x.numerator}_{x.denominator}.json').read_text())
    t=c['replay']['config_weighted']
    witness.add((t['weighted_root_observations'],t['weighted_terminal_observations']))
assert set(P).issubset(witness),('missing feasible segment witness',set(P)-witness)

# For a piece [B[i-1],B[i]], the middle line has the same two endpoint
# values as its neighbors. Concavity of the global infimum of affine
# feasible-policy costs then establishes it at every real interior x.
for i in range(1,len(B)):
    x,y=B[i-1],B[i]
    R,T=P[i]
    assert R*x+T==P[i-1][0]*x+P[i-1][1]
    assert R*y+T==P[i+1][0]*y+P[i+1][1]
print('EC49FQE_ALL_15_ENDPOINTS_AND_16_PHASES_PASS')
