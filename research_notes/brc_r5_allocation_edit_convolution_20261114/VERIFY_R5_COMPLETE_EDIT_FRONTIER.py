#!/usr/bin/env python3
"""Exact R5 741-transition edit frontier, extends frozen PR #2329.
Run in this directory: python VERIFY_R5_COMPLETE_EDIT_FRONTIER.py
Needs its sibling VERIFY_R5_ALLOCATION_EDIT.py, standard library only.
"""
import csv, json
from collections import Counter
from VERIFY_R5_ALLOCATION_EDIT import frozen_blocks, local_dp, minimum_removed

X,B=frozen_blocks()
D=[local_dp(b) for b in B]
M=[min(dp[0]) for dp in D]
assert len(X)==954 and len(B)==29 and sum(M)==213
assert sum(dp[0][m][0] for dp,m in zip(D,M))==1070
G=[[dp[0][k][0]-dp[0][k+1][0] for k in range(M[i],len(B[i]))]
   for i,dp in enumerate(D)]
assert all(g[j]>=g[j+1] for g in G for j in range(len(g)-1))
histogram=Counter(v for g in G for v in g)
assert histogram=={1:603,2:36,3:23,4:70,5:8,6:1}
all_gains=sorted((v for g in G for v in g),reverse=True)
assert len(all_gains)==741

# The unique gain-six transition needs exactly three old deletions.
indices6=[i for i,g in enumerate(G) if 6 in g]
assert len(indices6)==1 and G[indices6[0]].count(6)==1
ix6=indices6[0]
r6=minimum_removed(B[ix6],D[ix6],M[ix6],M[ix6]+1,3)
assert r6 is not None and r6[0]==3

# Each of the eight local gain-five transitions excludes one deletion.
g5_cert=[]
for i,g in enumerate(G):
    for t,v in enumerate(g):
        if v!=5:continue
        k=M[i]+sum(z>5 for z in g)+sum(z==5 for z in g[:t])
        assert minimum_removed(B[i],D[i],k,k+1,1) is None
        g5_cert.append((i,k))
assert len(g5_cert)==8 and G[19].count(5)==2
# Two successive tied transitions in block 19 suffice for all 8 global ranks.
for u in (0,1):
    k=M[19]+sum(z>5 for z in G[19])+u
    res=minimum_removed(B[19],D[19],k,k+1,2)
    assert res is not None and res[0]==2

# Block 28 covers all 70 gain-four ranks with 54 one-deletion local witnesses.
assert G[28].count(4)==54
assert sum(g.count(4) for i,g in enumerate(G) if i!=28)==16
for u in range(54):
    k=M[28]+sum(z>4 for z in G[28])+u
    res=minimum_removed(B[28],D[28],k,k+1,1)
    assert res is not None and res[0]==1

# Gains two/three have 59 explicit global nesting certificates in the
# preceding CLASSIFY_R5_NESTING.py; unit gains have a universal nesting proof.
rho_hist=Counter()
for gain in all_gains:
    rho_hist[{6:3,5:2,4:1,3:0,2:0,1:0}[gain]]+=1
assert rho_hist=={0:662,1:70,2:8,3:1}
summary={
 'status':'PASS_EXACT_PRODUCT','scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
 'integer_boundaries':954,'activation_events':1065,'blocks':29,'budgets':742,
 'transitions':741,'gain_histogram':dict(sorted(histogram.items())),
 'exact_rho_histogram':dict(sorted(rho_hist.items())),
 'rho_ranges':{'213':3,'214-221':2,'222-291':1,'292-953':0},
 'gain_6_block':ix6,'gain_5_local_checks':len(g5_cert),
 'gain_5_all_one_deletion_infeasible':True,
 'gain_5_two_deletion_witness_block':19,'gain_5_witness_local_steps':2,
 'gain_4_one_deletion_witness_block':28,'gain_4_witness_local_steps':54,
 'gain_4_other_tied_units':16,
 'prior_gain_2_or_3_global_nesting_certificate':'PR2329 CLASSIFY_R5_NESTING.py'}
print(json.dumps(summary,sort_keys=True,indent=2))
