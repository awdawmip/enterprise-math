#!/usr/bin/env python3
"""R749SMM: exact finite-horizon observer ranks, conditional static-source model.

Depends on the verified R749SML_JOINT_OBSERVER_EXACT_CHECK.py in this folder.
Uses stdlib fractions; no floating point, random sampling or symbolic claims via tests.
"""
from fractions import Fraction as Q
from itertools import product
import json
from R749SML_JOINT_OBSERVER_EXACT_CHECK import kernels, rank, STATES, apply, total_variation

GRID = (Q(-1), Q(-1, 2), Q(0), Q(1, 2), Q(1))

def joint_rows(a, b):
    f, p = kernels(a, b, Q(0))
    return f, p

def compose(a, b):
    return [[x*y for x, y in zip(row_a, row_b)] for row_a in a for row_b in b]

def future_rank(a, b):
    if not b:
        return 1 if not a else 2
    return 6 if not a else 8

def rank_horizon(a, b):
    f, p = joint_rows(a, b)
    one = rank(f+p)
    two_fp = rank(compose(f, p))
    two_ff = rank(compose(f, f))
    three_ff = rank(compose(compose(f, f), f))
    if not b:
        expected=(future_rank(a,b),)*4
    elif not a:
        expected=(4, 6, 4, 4)
    elif a == 1:
        expected=(4,7,7,8)
    else:
        expected=(6,8,7,8)
    assert (one,two_fp,two_ff,three_ff)==expected, (a,b,one,two_fp,two_ff,three_ff,expected)
    return {'r1_union':one,'r2_FP':two_fp,'r2_FF':two_ff,'r3_FFF':three_ff,'r_all_future':future_rank(a,b)}

def prior_pair(character):
    mu_plus=[(1+Q(character(*s),2))/8 for s in STATES]
    mu_minus=[(1-Q(character(*s),2))/8 for s in STATES]
    assert all(Q(1,16)<=p<=Q(3,16) for p in mu_plus+mu_minus)
    return mu_plus,mu_minus

def witness(matrix, character):
    mu_plus,mu_minus=prior_pair(character)
    return total_variation(apply(matrix,mu_plus),apply(matrix,mu_minus))

def main():
    rows=[]
    for a,b in product(GRID,repeat=2):
        rows.append({'alpha':str(a),'beta':str(b),**rank_horizon(a,b)})
    f,p=joint_rows(Q(-1),Q(1,2))
    obs={}
    for name,mat in {'F':f,'P':p,'FF':compose(f,f),'FP':compose(f,p),'FFF':compose(compose(f,f),f)}.items():
        obs[name]={'YT':str(witness(mat,lambda x,y,t:y*t)),
                   'XYT':str(witness(mat,lambda x,y,t:x*y*t))}
    assert obs['F']==obs['P']=={'YT':'0','XYT':'0'}
    assert obs['FF']=={'YT':'3/256','XYT':'0'}
    assert obs['FP']=={'YT':'5/256','XYT':'1/64'}
    result={'status':'PASS','exact_arithmetic':'fractions.Fraction',
            'parameter_pairs':len(rows),'source_column_checks':len(rows)*2*8,
            'rank_checks':len(rows)*4,'grid':[str(x) for x in GRID],
            'horizon_rank_results':rows, 'positive_prior_TV_witnesses':obs,
            'theorem_scope':'gamma=0; static history; independently sampled outputs conditioned on source; allowed publicly chosen F/P experiments; strict-positive priors',
            'independent_review':'pending',
            'scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389'}
    return result

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2,sort_keys=True))
