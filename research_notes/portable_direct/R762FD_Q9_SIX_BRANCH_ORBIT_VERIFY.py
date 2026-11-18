#!/usr/bin/env python3
"""Reproducible exact S3 x C2 orbit quotient of the six positive BRC steps.

Only a six-labelled *positive counting* carrier is used. Unlabelled terminal
count observations are reconstructed exactly. No native signed X6 claim.
"""
import json
from itertools import product
from math import comb

BRANCHES=((0,0,0),(1,0,0),(0,0,1),(1,1,0),(0,1,1),(1,1,1))
V=(1,-1,1)
SIGNED_STEPS=tuple(tuple(v*(2*b-1) for v,b in zip(V,branch)) for branch in BRANCHES)
assert set(SIGNED_STEPS)=={s for s in product((-1,1),repeat=3) if len(set(s))==2}


def index(g,q):
    x,y,z=g
    return (x*q+y)*q+z


def key_u(u,q):
    u=tuple(v%q for v in u)
    return min(tuple(sorted(u)),tuple(sorted((-v)%q for v in u)))


def key_g(g,n,q):
    return key_u((v*(2*x-n) for v,x in zip(V,g)),q)


def build(q):
    assert q%2==1
    coords=list(product(range(q),repeat=3))
    keys=sorted({key_u(u,q) for u in coords})
    expected=(comb(q+2,3)+(q+1)//2)//2
    assert len(keys)==expected
    positions={k:i for i,k in enumerate(keys)}
    # The representative 'key' is itself a valid u-vector. The six signed
    # increments are invariant under S3 permutation and global negation.
    T=[[positions[key_u((v-s for v,s in zip(k,step)),q)]
       for step in SIGNED_STEPS] for k in keys]
    labels=[]
    for n in range(q):
        labels.append([positions[key_g(g,n,q)] for g in coords])
    return coords,keys,T,labels


def full_update(state,coords,q):
    return [sum(state[index(tuple((x-b)%q for x,b in zip(g,branch)),q)]
                for branch in BRANCHES) for g in coords]


def reduced_update(vector,T):
    return [sum(vector[j] for j in row) for row in T]


def check(q,max_n):
    coords,keys,T,labels=build(q)
    v=[int(k==(0,0,0)) for k in keys]
    full=[0]*(q**3)
    full[0]=1
    checks=0
    checksum=0
    max_values=0
    for n in range(max_n+1):
        indexed=labels[n%q]
        for i,actual in enumerate(full):
            assert actual==v[indexed[i]],(q,n,i,actual,v[indexed[i]])
            checks+=1
        assert sum(full)==6**n,(q,n,'mass')
        max_values=max(max_values,len(set(full)))
        checksum=(checksum*1000003+sum((i+1)*(x%1000000007) for i,x in enumerate(full)))%1000000007
        if n!=max_n:
            full=full_update(full,coords,q)
            v=reduced_update(v,T)
    # Check closure/equivariance for arbitrary orbit-constant (not only P^n)
    # data in every residue class of n mod q.
    trial=[(173*j*j+31*j+7)%1009 for j in range(len(keys))]
    expect=reduced_update(trial,T)
    for n in range(q):
        raw=[trial[j] for j in labels[n]]
        nxt=full_update(raw,coords,q)
        assert all(nxt[i]==expect[labels[(n+1)%q][i]] for i in range(q**3))
    return {
        'q':q,'n_inclusive':[0,max_n],
        'raw_terminal_count':q**3,'orbit_state_count':len(keys),
        'matrix_nonzero_entries':sum(len(set(row)) for row in T),
        'matrix_weighted_branch_edges':sum(map(len,T)),
        'full_coefficient_checks':checks,
        'max_distinct_coefficient_values_seen':max_values,
        'direct_BRC_vs_reduced':'PASS',
        'arbitrary_orbit_input_all_time_phases':'PASS',
        'mass_conservation':'PASS',
        'rolling_checksum_mod_1000000007':checksum
    }


def main():
    outcomes=[check(3,72),check(9,90),check(27,12)]
    q=9
    # One fixed named branch update fails to descend to the quotient.
    assert key_g((0,0,0),1,q)==key_g((1,1,1),1,q)
    assert key_g((1,0,0),2,q)!=key_g((2,1,1),2,q)
    data={
      'schema':'R762FD_POSITIVE_BRC_S3_C2_STATIONARY_ORBIT_V1',
      'scope':'all odd q and all n>=0; six positive named BRC branches',
      'branches':[list(b) for b in BRANCHES],
      'signed_centered_steps':[list(s) for s in SIGNED_STEPS],
      'observer':'u=(2x-n,n-2y,2z-n) mod q; canonical = min(sorted(u),sorted(-u))',
      'orbit_count':'(C(q+2,3)+(q+1)/2)/2',
      'transition':'T[k,j] counts centered signed steps s with canonical(k-s)=j; T is independent of n',
      'q9_period_window_full_comparisons':729*127,
      'q9_period_window_reduced_comparisons':85*127,
      'q9_saving_exact':'81788/92583=644/729',
      'q9_fixed_named_branch_non_descent':{
        'n':1,'input_endpoints':[[0,0,0],[1,1,1]],
        'appended_branch':[1,0,0],
        'output_endpoints':[[1,0,0],[2,1,1]],
        'output_orbits_equal':False},
      'outcomes':outcomes,
      'evidence':'unbounded theorem proved by exact branch-word bijection, finite checks only as stated',
      'review':'AUTHOR_PROVED / EXACT_INTEGER_CHECK_PASS / NOT_REVIEWED'
    }
    print(json.dumps(data,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
