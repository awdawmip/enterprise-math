#!/usr/bin/env python3
"""EC49FPH: exact fixed mixed-observation minimum, native BRC class 16943.

Run: python VERIFY_EC49FPH.py PATH_TO_EC49FPG_EVIDENCE_DIR
Requires only Python >= 3.9 standard library and original frozen inputs.
All bitset comparisons use exact Python integer operations.
"""
import csv
import hashlib
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOTS = (3, 5, 6, 7)
INPUT_SHA256 = 'cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
PROFILE_SHA256 = 'a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f'
BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
assert hashlib.sha256((BASE/'frozen_original_master.txt').read_bytes()).hexdigest() == INPUT_SHA256
assert hashlib.sha256((BASE/'EC49FPG_PROFILE.csv').read_bytes()).hexdigest() == PROFILE_SHA256

with (BASE/'frozen_original_master.txt').open() as f:
    nfamilies, nwords, nconfigs = map(int, f.readline().split())
    assert (nfamilies, nwords, nconfigs) == (94, 178850, 38169)
    families = []
    for _ in range(nfamilies):
        m = [0]*4
        for _ in range(int(f.readline())):
            label, hex_bytes = f.readline().split()
            m[ROOTS.index(int(hex_bytes[:2],16))] |= 1 << int(label)
        families.append(m)
    configs = [tuple(map(int, f.readline().split())) for _ in range(nconfigs)]

def domain(config):
    d = [0]*24
    for family in config:
        for ri, mask in enumerate(families[family]):
            while mask:
                bit = mask & -mask
                d[bit.bit_length()-1] |= 1 << ri
                mask -= bit
    return tuple(d)

original_domain = domain(configs[16943])
class_ids = [i for i, c in enumerate(configs) if domain(c) == original_domain]
assert len(class_ids) == 310
original_class_set = set(class_ids)

costs = defaultdict(dict)
with (BASE/'EC49FPG_PROFILE.csv').open() as f:
    for entry in csv.DictReader(f):
        config = int(entry['config'])
        if config not in original_class_set:
            continue
        root, must, optional, subset, cost = [int(entry[k]) for k in ('root','must','opt','subset','cost')]
        assert (root, subset) not in costs[config]
        costs[config][root,subset] = (must, optional, cost)
assert len(costs) == 310
coords = sorted(costs[class_ids[0]])
assert len(coords) == 84
assert all(set(costs[c]) == set(coords) for c in class_ids)

options = [i for i, mask in enumerate(original_domain) if mask.bit_count()>1]
legal_roots = [tuple(r for j,r in enumerate(ROOTS) if mask & (1<<j)) for i,mask in enumerate(original_domain) if i in options]
actions = list(itertools.product(*legal_roots))
assert len(options)==6 and len(actions)==144

rooted_to_representative = {}
rooted_vectors = {}
terminal_vectors = {}
for c in class_ids:
    p = tuple(costs[c][key][2] for key in coords)
    rooted_to_representative.setdefault(p, c)
    rooted_vectors[c] = p
    row = []
    for allocation in actions:
        subsets = dict.fromkeys(ROOTS, 0)
        for label, root in zip(options, allocation):
            subsets[root] |= 1 << label
        row.append(sum(costs[c][r,subsets[r]][2] for r in ROOTS))
    terminal_vectors[c] = tuple(row)
rooted_reps = list(rooted_to_representative.values())
terminal_reps = list({terminal_vectors[c]:c for c in rooted_reps}.values())
assert len(rooted_reps)==141 and len(terminal_reps)==139

# Each query is a function from the 141 rooted states to an exact integer.
terminal_rows = [[terminal_vectors[c][i] for c in rooted_reps] for i in range(len(actions))]
root_rows = [[costs[c][root,subset][2] for c in rooted_reps] for root,subset in coords]
queries = [('terminal',i) for i in range(len(actions))] + [('named_root',r,s) for r,s in coords]
responses = terminal_rows+root_rows
assert len(responses)==228
pairs = list(itertools.combinations(range(len(rooted_reps)),2))
assert len(pairs)==9870
# Bit j=1 means pair j remains indistinguishable after this query.
indist = [sum(1<<i for i,(a,b) in enumerate(pairs) if q[a]==q[b]) for q in responses]
unique = {}
for i,m in enumerate(indist):
    unique.setdefault(m,i)
unique_masks = list(unique)
assert len(unique_masks)==209
assert all(m != 0 for m in unique_masks)

pair_intersections = {}
for i,left in enumerate(unique_masks):
    for j in range(i+1,len(unique_masks)):
        residual = left & unique_masks[j]
        assert residual != 0, ('two probes suffice', i,j)
        pair_intersections.setdefault(residual,(i,j))
assert len(pair_intersections)==19622
# All distinct remaining-pair masks after two probes overlap the
# indistinguishable pairs of every possible third probe.
triple_checks = 0
for residual in pair_intersections:
    for third in unique_masks:
        assert residual & third, ('three probes suffice',pair_intersections[residual])
        triple_checks+=1
assert triple_checks == 19622*209

# Explicit four-probe upper bound: terminal allocations 34,36,66;
# plus a named root05 query with the empty OPTIONAL demand subset.
root05_index = len(actions)+coords.index((5,0))
certificate_indices = [34,36,66,root05_index]
assert not (indist[34]&indist[36]&indist[66]&indist[root05_index])
signatures = [tuple(responses[q][i] for q in certificate_indices) for i in range(len(rooted_reps))]
assert len(set(signatures))==141

# The terminal-only observer admits two P-distinct but T-identical pairs.
term_only = {terminal_vectors[c] for c in rooted_reps}
assert len(term_only)==139
for a,b in [(17928,38165),(24541,38166)]:
    assert rooted_vectors[a] != rooted_vectors[b]
    assert terminal_vectors[a] == terminal_vectors[b]
    assert costs[a][5,0][2] != costs[b][5,0][2]

# Independent within-terminal-state exact bound: 139 distinct profiles;
# no three terminal queries distinguish all 139; four do.
term_rows = [[terminal_vectors[c][q] for c in terminal_reps] for q in range(len(actions))]
term_pairs = list(itertools.combinations(range(139),2))
term_masks = [sum(1<<i for i,(a,b) in enumerate(term_pairs) if vals[a]==vals[b]) for vals in term_rows]
term_pair_residuals = {term_masks[i]&term_masks[j] for i in range(144) for j in range(i+1,144)}
assert len(term_pair_residuals)==10153
assert all(r and all(r & m for m in term_masks) for r in term_pair_residuals)
assert (term_masks[64]&term_masks[140]&term_masks[72]&term_masks[31])==0

output = {
 'schema':'EC49FPH_EXACT_MINIMUM_MIXED_NATIVE_BRC_PROBE_CERTIFICATE_V1',
 'frozen_scientific_commit':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
 'input_sha256':INPUT_SHA256, 'rooted_profile_csv_sha256':PROFILE_SHA256,
 'original_class_representative':16943,
 'complete_source_configs':len(class_ids),
 'distinct_rooted_profiles':len(rooted_reps),
 'distinct_terminal_profiles':len(terminal_reps),
 'named_root_subset_coordinates':len(coords),
 'legal_complete_allocations':len(actions),
 'total_primitive_scalar_queries':len(queries),
 'distinct_query_indistinguishability_masks':len(unique_masks),
 'distinct_rooted_profile_pairs':len(pairs),
 'all_distinct_two_probe_intersections':len(pair_intersections),
 'three_probe_exclusion_intersection_checks':triple_checks,
 'minimum_nonadaptive_scalar_queries_in_228_query_menu':4,
 'four_query_witness':[queries[i] for i in certificate_indices],
 'terminal_action_maps':{str(q):dict(zip(map(str,options),actions[q])) for q in (34,36,66,64,140,72,31)},
 'all_141_rooted_profiles_distinguished_by_four':len(set(signatures))==141,
 'all_139_terminal_profiles_need_four_fixed_terminal_queries':True,
 'observer_fiber_nontrivial_witnesses':[[17928,38165],[24541,38166]],
 'scope':'Within complete original frozen legal-root-domain class16943; each scalar query is either a legal complete allocation terminal sum or one allowed native named-root/subset integer cost; nonadaptive fixed selection.'
}
print('EC49FPH_EXACT_FINITE_PROOF_PASS')
print(json.dumps(output, ensure_ascii=False, indent=2))
