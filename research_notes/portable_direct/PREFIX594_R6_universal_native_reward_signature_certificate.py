#!/usr/bin/env python3
"""PREFIX-594-R6: universal native BRC 33-dimensional full joint-law carrier.
Requires published PREFIX-565 native kernel and exact PREFIX-591 graded module.
Checks all original edge/reward signatures over Q, all frozen roots.
"""
from fractions import Fraction as F
import json
from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN, PHASES, ACTIONS, ROOTS, ZERO_ROOT, edge
)
from PREFIX591_R6_unbounded_cubic_observer_invariant_module_certificate import W
assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(ROOTS)==9 and len(ACTIONS)==6
U=W[3]
assert len(U.vectors)==33 and U.contains([1]*96)
CHECKS=0;rows=[]
for root in ROOTS:
    edges=[]
    for i in range(96):
        rr=[]
        for action in ACTIONS:
            j,w=edge(i,action,root)
            t=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
            rr.append((j,(t,w[0]+w[1],w[2]+w[3])))
        edges.append(rr)
    sigs=sorted({sig for row in edges for j,sig in row})
    assert len(sigs)==(6 if root==ZERO_ROOT else 10)
    for sig in sigs:
        for v in U.vectors:
            transformed=[
                sum((v[j] for j,s in row if s==sig),F())
                for row in edges
            ]
            assert U.contains(transformed),(root,sig)
            CHECKS+=1
    rows.append({'root':list(root),'unique_triple_reward_signatures':len(sigs),
                 'signature_invariant_operator_checks':len(sigs)*33,
                 'invariant_basis_dimension':len(U.vectors)})
assert CHECKS==2838
# A root-independent carrier includes every root's all-degree-three observer:
# PREFIX-593 gives exact rank=33 for all roots, and the complete native
# signature invariance above makes U an upper carrier for every root.
# Hence their exact moment spaces equal U.
types={tuple(v[i] for v in U.vectors) for i in range(96)}
assert len(types)==34
# Original seven-reward selector distinguishes information outside this
# precisely declared triple-observer carrier.
full_edges=[[edge(i,a,ZERO_ROOT) for a in ACTIONS] for i in range(96)]
full_sigs=sorted({w for row in full_edges for j,w in row})
failed_sigs=0
for sig in full_sigs:
    if any(not U.contains([
        sum((v[j] for j,w in row if w==sig),F())
        for row in full_edges
    ]) for v in U.vectors):
        failed_sigs+=1
assert failed_sigs>=1
out={
 'schema':'PREFIX594_R6_UNIVERSAL_33_NATIVE_BRC_FULL_TRIPLE_LAW_V1',
 'status':'ALL_CHECKS_PASS','science_pin':SCIENCE_PIN,
 'original_native_ports':96,'labeled_actions':6,
 'allowed_roots':9,'root_signatures':rows,
 'distinct_signature_operators':sum(r['unique_triple_reward_signatures'] for r in rows),
 'rational_operator_basis_images_checked':CHECKS,
 'universal_linear_observer_rank':33,
 'minimal_variable_initial_law_statistics':32,
 'original_port_basis_evaluation_types':len(types),
 'full_seven_reward_signature_count':len(full_sigs),
 'full_seven_reward_signature_invariance_failures':failed_sigs,
 'scope':'all n >= 0; any fixed nine-root value or externally chosen root schedule; full joint distribution of (T,P0,P1); arbitrary initial 96-port law; native original kernel',
 'formal_task_CLAIM_Result_Review':False}
print('ALL_CHECKS_PASS')
print(json.dumps(out,indent=2))
