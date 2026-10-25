#!/usr/bin/env python3
"""C312: Oracle-free exact zero-extra-content certificates on 106 C293 paths.

Source-only author computation in C195/H168 79-branch auxiliary scalar model.
Scientific conclusions conditional on the C300/C305 factorized numerator identity.
Does not claim native BRC/X6 equivalence, formal Owner/CLAIM or Driver admission.
"""
from __future__ import annotations
import argparse, json, hashlib, time
from pathlib import Path
from math import gcd
from functools import reduce
import C311_COMPOSITE_CERTIFICATE as prev
import C310_JOINT_BRANCH_PRIME_CERT as c310

HERE = Path(__file__).resolve().parent
EXCEPTIONAL = frozenset(c310.EXCEPTIONAL)
INDICES = tuple(i for i in range(125) if i not in EXCEPTIONAL)
assert len(INDICES)==106


def certificate_for_path(i, path, k24, W):
    s, groups, terms, cancels, d = c310.c305.prepare(i,path,k24,W)
    L=c310.term_content_lower(s,terms)
    assert L>0 and s%L==0
    S=s//L
    prime_powers,H=prev.smooth_decompose(S)
    assert S == H*reduce(lambda v,pe: v*pe[0]**pe[1], prime_powers,1)
    witnesses=[]
    for p,e in prime_powers:
        # Exact coefficient arithmetic over F_p[t]. Nonzero coeff rules out p.
        coeff, surviving,vanishing,degree = c310.poly_branch_mod(p,groups,terms,L)
        w=next(((j,int(v)%p) for j,v in enumerate(coeff) if int(v)%p!=0),None)
        if w is None:
            raise AssertionError(f'Unexpected small-prime obstruction: path {i}, prime {p}')
        witness={'prime':p,'exponent_in_S':e,'degree':w[0],'residue':w[1]}
        if p<=11:
            # F_p[t]/(t^p-t): x^j -> x^(1+(j-1)%(p-1)) for j>0.
            remainder=[0]*p
            for j,a in enumerate(coeff):
                dest=0 if j==0 else 1+(j-1)%(p-1)
                remainder[dest]=(remainder[dest]+int(a))%p
            all_samples_zero=True
            for t in range(p):
                v=0
                for a in reversed(coeff):v=(v*t+int(a))%p
                if v:all_samples_zero=False
            assert all_samples_zero==(not any(remainder))
            witness['all_integer_samples_zero_mod_p']=all_samples_zero
            witness['divisible_by_t_power_p_minus_t_mod_p']=all_samples_zero
        witnesses.append(witness)
    # This single modular evaluation excludes ALL, possibly unfactored,
    # prime divisors of H. No primality assumption on H is made.
    c=None
    if H>1:
        primitive_terms=prev.prepared_int_terms(terms,L)
        r=prev.eval_R_mod(H,1,groups,primitive_terms)
        if gcd(H,r)!=1:
            raise AssertionError(f'Unexpected composite obstruction path {i}, gcd {gcd(H,r)}')
        inv=pow(r,-1,H)
        assert r*inv%H==1
        c={'T':1,'R_mod_H_dec':str(r),'inverse_mod_H_dec':str(inv)}
    return {'path_index':i,'degree_reduced':d,'L_dec':str(L),
            'S_dec':str(S),'S_bits':S.bit_length(),
            'small_prime_powers':witnesses,'H_dec':str(H),
            'H_bits':H.bit_length(),'composite_bezout':c,
            'determined_gcd_s_content_P_dec':str(L),
            'factorized_branch_count':len(terms)}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--indices',default='all')
    ap.add_argument('--output',default='C312_106_ZERO_EXTRA_CONTENT_CERT.json')
    ap.add_argument('--posthoc-oracle',action='store_true')
    args=ap.parse_args()
    rr=json.loads((c310.c305.ROOT/'C293_125_REFINED_BRACKETS.json').read_text())
    assert rr['records_sha256']=='03083a77480e6be5615797c2f4ffc503eee6603e9e60cbad1f11fb3ea83b3c89'
    paths,_=c310.c305.c288.build_paths()
    W,_=c310.c305.src.floor_fixed_masses()
    indices=INDICES if args.indices=='all' else tuple(int(x) for x in args.indices.split(','))
    if not set(indices)<=set(INDICES):raise ValueError('Only the 106 remaining paths')
    oracle=None
    if args.posthoc_oracle:
        ob=json.loads((HERE/'C309_BRANCH_CONTENT_PROBE_125.json').read_text())
        oracle={r['index']:r['oracle_dec'] for r in ob['rows']}
    rows=[]
    for i in indices:
        t=time.monotonic()
        assert rr['records'][i][0]==i
        row=certificate_for_path(i,paths[i],int(rr['records'][i][1]),W)
        if oracle is not None:
            assert row['determined_gcd_s_content_P_dec']==oracle[i]
            row['posthoc_C306_match']=True
        rows.append(row)
        print('C312_AUTHOR_PASS',i,'primes',len(row['small_prime_powers']),
              'Hbits',row['H_bits'],'degree',row['degree_reduced'],
              'secs',round(time.monotonic()-t,3),flush=True)
    out={'schema':'C312_ZERO_EXTRA_CONTENT_106_V1',
      'path_count':len(rows),
      'scope':'106 nonexceptional C293 paths; C195/H168 79-branch auxiliary scalar; C300/C305 factorized identity inherited author-level premise',
      'frozen_C293_records_sha256':rr['records_sha256'],
      'trial_primes_lt':10000,
      'basis':'Gauss primitive-factor lemma, exact coefficient nonzero mod each explicit small prime, modular Bezout evaluation T=1 for entire composite H',
      'historical_oracle_used_as_proof':False,
      'posthoc_oracle_comparison_performed':bool(args.posthoc_oracle),
      'indices':list(indices),'rows':rows,
      'small_prime_fixed_divisor_obstructions':{str(p):sum(1 for row in rows for w in row['small_prime_powers'] if w['prime']==p and w.get('all_integer_samples_zero_mod_p')) for p in (2,3,5,7,11)},
      'small_prime_witness_counts':{str(p):sum(1 for row in rows for w in row['small_prime_powers'] if w['prime']==p) for p in (2,3,5,7,11)}}
    (HERE/args.output).write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
    print('C312_ALL',len(rows),'PASS',flush=True)
if __name__=='__main__':main()
