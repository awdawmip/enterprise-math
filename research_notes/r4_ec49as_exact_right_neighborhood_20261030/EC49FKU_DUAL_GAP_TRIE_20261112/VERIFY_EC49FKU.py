#!/usr/bin/env python3
"""EC49FKU: solver-free exact <=93 exclusion for frozen BRC six-key cases 0,3.

Requires original unmodified EC49FGW_RADIUS5_SCREEN.py / witness JSON,
EC49FKS_COMPACT_CERT.json and CHECK_EC49FKS_COMPACT.py in this folder,
or in their sibling PR #1730 directories (see README).
All scientific arithmetic is exact typed BRC / rational certificate checking.
"""
import collections
import json
import pathlib
import sys
from fractions import Fraction as Q

HERE = pathlib.Path(__file__).resolve().parent
SIB = HERE.parent
for p in (HERE, SIB / 'EC49FKS_EXACT_FRACTIONAL_BARRIER_20261112',
          SIB / 'EC49FJD_RELEASE_B11_COMPLETE_20261111'):
    if p.exists():
        sys.path.insert(0, str(p))
from EC49FGW_RADIUS5_SCREEN import PIN, all_words, pref, raw_key
from CHECK_EC49FKS_COMPACT import check as validate_existing_primal_dual

BASE = {(2,1,1),(3,0,1),(3,1,1),(4,2,1)}
EXTRA = [((5,4,1),(5,5,1)), ((5,4,1),(6,4,1)),
         ((6,3,1),(6,4,1)), ((6,3,1),(7,3,1))]
cert_path = HERE / 'EC49FKS_COMPACT_CERT.json'
if not cert_path.exists():
    cert_path = SIB / 'EC49FKS_EXACT_FRACTIONAL_BARRIER_20261112' / cert_path.name
C = json.loads(cert_path.read_text())
assert PIN == C['frozen_science_pin'] == 'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'

def optimal_cost(group):
    """Exact trie DP: full observation mask -> smallest selected prefix union."""
    labels = sorted({a for a, ps in group})
    assert len(labels) == 12
    li = {a:i for i,a in enumerate(labels)}
    root, child, obs = 0, collections.defaultdict(dict), collections.defaultdict(int)
    count = 1
    for a, prefixes in group:
        cur = root
        for p in prefixes:  # literal ordered signed-X6 prefix, including first step
            if p not in child[cur]:
                child[cur][p] = count
                count += 1
            cur = child[cur][p]
        obs[cur] |= 1 << li[a]
    def dp(u):
        choices = {0:0}
        if obs[u]: choices[obs[u]] = 0
        for v in child[u].values():
            cp = dp(v)
            merged = {}
            for a,ca in choices.items():
                for b,cb in cp.items():
                    mask = a|b
                    cost = ca+cb
                    if cost < merged.get(mask, 1000000000):
                        merged[mask] = cost
            choices = merged
        if u != root:
            choices = {m: c+(m!=0) for m,c in choices.items()}
        return choices
    result = dp(root)
    return result[(1<<12)-1], count-1, len(result)

def certify(idx):
    rec = C['certificates'][str(idx)]
    # This also independently checks the exact rational LP optimum (primal & dual).
    pre = validate_existing_primal_dual(idx, rec)
    keys = BASE | set(EXTRA[idx])
    words = [(a,pref(w)) for a,w in all_words() if raw_key(w) in keys]
    labels = sorted({a for a,_ in words})
    nodes = sorted({p for a,ps in words for p in ps},key=lambda p:(len(p),p))
    assert len(words)==4366 and len(nodes)==19962 and len(labels)==24
    ix = {p:j for j,p in enumerate(nodes)}
    parent = [ix.get(p[:-1],-1) for p in nodes]
    terminals = collections.defaultdict(set)
    for a,ps in words: terminals[a].add(ix[ps[-1]])
    weights = list(map(Q,rec['weights']))
    charge = [Q(0)]*len(nodes)
    for lab, weight in zip(labels,weights):
        for j in terminals[lab]: charge[j] += weight
    in_flow = [Q(0)]*len(nodes)
    red_cost = [Q(0)]*len(nodes)
    edge_flow = [Q(0)]*len(nodes)
    for j in range(len(nodes)-1,-1,-1):
        excess = charge[j]+in_flow[j]-1
        if parent[j]>=0:
            edge_flow[j] = max(Q(0),excess)
            in_flow[parent[j]] += edge_flow[j]
        else:
            assert excess <= 0
        red_cost[j] = 1-charge[j]-in_flow[j]+edge_flow[j]
        assert red_cost[j]>=0
    lower = sum(weights)
    assert lower == Q(1105,12) == Q(rec['objective'])
    gap = Q(93)-lower
    assert gap == Q(11,12)
    banned = {j for j,c in enumerate(red_cost) if c>gap}
    good = [(a,ps) for a,ps in words if all(ix[p] not in banned for p in ps)]
    groups = collections.defaultdict(list)
    for a,ps in good: groups[ps[0]].append((a,ps))
    assert set(groups)=={b'\x05',b'\x06'}
    cost_rows=[]
    for root,group in sorted(groups.items()):
        cost,node_count,states = optimal_cost(group)
        cost_rows.append({'root_step':root.hex(),'words':len(group),
                          'labels':len({a for a,_ in group}),
                          'trie_nodes':node_count,'optimum':cost,
                          'terminal_masks':states})
    assert sum(row['labels'] for row in cost_rows)==24
    assert {a for a,_ in good}==set(labels)
    assert len(banned)==5231 and len(good)==170
    assert [row['optimum'] for row in cost_rows]==[49,49]
    assert sorted(row['words'] for row in cost_rows)==[61,109]
    return {'case':idx,'frozen_scientific_pin':PIN,'lp_bound':str(lower),
            'integer_target_max':93,'dual_gap':str(gap),
            'original_words':len(words),'forbidden_nodes':len(banned),
            'surviving_words':len(good),'forced_singleton_demands':sum(
                sum(a==b for b,_ in good)==1 for a in labels),
            'split_dp':cost_rows,'min_cost_with_dual_gap_word_filter':98,
            'excludes_at_most_93':True,'prior_lp_cert_verified':pre['optimum']}

if __name__=='__main__':
    result = [certify(idx) for idx in (0,3)]
    print(json.dumps(result,sort_keys=True,indent=2))
    print('EC49FKU_TWO_SIX_KEY_CASES_93_EXCLUDED_EXACT_PASS')
