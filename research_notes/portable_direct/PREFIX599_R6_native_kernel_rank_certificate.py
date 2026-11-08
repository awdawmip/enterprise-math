#!/usr/bin/env python3
"""PREFIX-599-R6: exact full-seven-reward/next-port native one-step kernels.

Imports the immutable PREFIX565 native kernel, uses standard-library Fraction.
Matrix rows are native original source ports, columns are exact outcome labels.
"""
from collections import Counter
from fractions import Fraction as Q
import json
from PREFIX565_positive_marginal_certificate import (
    SCIENCE_PIN,PHASES,NEXT,TARGET,ACTIONS,ROOTS,edge
)
assert SCIENCE_PIN == 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
assert len(PHASES)==48 and len(ROOTS)==9 and len(ACTIONS)==6
assert TARGET==4
P=(3,14,15)
assert {i for i,row in enumerate(NEXT) if TARGET in row}==set(P)
assert [NEXT[i].index(TARGET) for i in P]==[0,1,1]

def integer_rows(root, keep_action):
    rows=[]; keys=set()
    for port in range(96):
        C=Counter()
        for a in ACTIONS:
            j,w=edge(port,a,root)
            k=(a,j,w) if keep_action else (j,w)
            C[k]+=1;keys.add(k)
        rows.append(C)
    return rows,{k:i for i,k in enumerate(sorted(keys))}

def exact_rank(rows,ordered_keys):
    piv={}
    for C in rows:
        v={ordered_keys[k]:Q(n) for k,n in C.items()}
        while v:
            j=min(v)
            if j not in piv:
                t=v[j]
                piv[j]={k:z/t for k,z in v.items()}
                break
            w=piv[j];t=v[j]
            for k,z in w.items():
                a=v.get(k,Q(0))-t*z
                if a:v[k]=a
                elif k in v:del v[k]
    return len(piv)

def add_scaled(x,scale,C):
    for key,count in C.items():x[key]+=scale*count

def check_full_kernel_basis(rows,keep_action):
    basis=[]
    for p in range(48):
        if p not in P:basis.append({2*p:1,2*p+1:-1})
    if keep_action:
        basis.append({28:1,29:-1,30:-1,31:1})
    else:
        basis.append({6:1,7:-1,28:-1,29:1})
        basis.append({28:1,29:-1,30:-1,31:1})
    for vec in basis:
        c=Counter()
        for i,coeff in vec.items():add_scaled(c,coeff,rows[i])
        assert all(x==0 for x in c.values())
    return len(basis)

results=[]
for index,root in enumerate(ROOTS):
    for keep_action in (False,True):
        rows,keymap=integer_rows(root,keep_action)
        assert len(rows)==96
        assert len(keymap)==(194 if keep_action else 97)
        rank=exact_rank(rows,keymap)
        nullity=check_full_kernel_basis(rows,keep_action)
        assert rank==(50 if keep_action else 49)
        assert nullity==(46 if keep_action else 47)
        assert rank+nullity==96
        results.append(dict(root_index=index,primitive_action_observed=keep_action,
                            output_alphabet_size=len(keymap),exact_rational_rank=rank,
                            complete_explicit_null_basis_dimension=nullity))
assert len(results)==18
report=dict(status='ALL_CHECKS_PASS',
    science_pin=SCIENCE_PIN,
    native_module='PREFIX565_positive_marginal_certificate.py',
    native_source_git_blob='7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41',
    native_source_ports=96, source_phases=48, actions=6,
    frozen_allowed_roots=9, checked_root_observer_matrix_count=18,
    exact_arithmetic='fractions.Fraction rational Gaussian elimination',
    full_reward_exact_nextport_rank_without_action=49,
    full_reward_exact_nextport_rank_with_action=50,
    kernel_dim_without_action=47,kernel_dim_with_action=46,
    results=results)
print('ALL_CHECKS_PASS')
print(json.dumps(report,ensure_ascii=False,indent=2))
