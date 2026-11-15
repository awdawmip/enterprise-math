#!/usr/bin/env python3
"""R749SRW: exact sharp ±2 marked-total error threshold for 3-read six-phase decoding.

Requires the R749SRV_INTEGER_MARKED_COUNT_CERT.py precursor in same directory;
all calculations integer and fractions.Fraction, no floating-point math or network.
"""
from fractions import Fraction as F
from itertools import product
import json
from R749SRV_INTEGER_MARKED_COUNT_CERT import counts, R, OFFSETS, SIGNATURES, certify_tail

LOWER = 65
TAIL_START = 523
BOUND = F(2 * 112500 * TAIL_START**3, (TAIL_START-1)**5)
assert BOUND < F(5, 6)
assert F(2 * 112500 * (TAIL_START-1)**3, (TAIL_START-2)**5) >= F(5, 6)


def case(r, eps, C, T):
    y = tuple(R(r+h, C, T, eps[i]) for i,h in enumerate(OFFSETS))
    distances = tuple(max(abs(y[i]-SIGNATURES[b][i]) for i in range(3)) for b in range(6))
    true = r%6
    competitor, d_bad = min(((b, distances[b]) for b in range(6) if b!=true), key=lambda x:(x[1],x[0]))
    margin = d_bad - distances[true]
    winners = [b for b,x in enumerate(distances) if x==min(distances)]
    return margin, competitor, winners, distances, y


def main():
    C,T=counts(600)
    tails=certify_tail(C,T)  # original 6-residue all-r positive coefficients
    best=None; error_vectors=0
    for r in range(LOWER,TAIL_START):
        for errors in product(range(-2,3),repeat=3):
            margin, competitor, winners, *_ = case(r, errors, C, T)
            assert margin>0 and winners==[r%6],(r,errors,margin,winners)
            item=(margin,r,errors,competitor)
            if best is None or item<best:best=item
            error_vectors+=1
    assert error_vectors==(TAIL_START-LOWER)*125
    eps=(-2,2,-2)
    margin, competitor,winners,distances,y=case(64,eps,C,T)
    assert margin<0 and 64%6==4 and competitor==3 and winners==[3]
    # Distinct ideal 3-read signatures have min L_inf distance 15/2.
    sep=min(max(abs(x-z) for x,z in zip(SIGNATURES[a],SIGNATURES[b]))
            for a in range(6) for b in range(a+1,6))
    assert sep==F(15,2)
    return {
        'status':'PASS','research_unit':'R749SRW',
        'frozen_scientific_pin':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'predecessor':'R749SRV / same branch source',
        'model_weights':[1,1,2,3,6],'marked_source_index':0,
        'read_offsets':list(OFFSETS),'integer_error_budget_per_marked_total':2,
        'denominator_counts':'exact unperturbed prefix C_r',
        'theorem':'For all integer r>=65 and all 125 error triples epsilon in [-2,2]^3, unique nearest phase is r mod 6; r=64 has a wrong-decoding vector, so 65 is the least all-integer cutoff.',
        'finite_range':[LOWER,TAIL_START-1],
        'finite_r_count':TAIL_START-LOWER,
        'error_vectors_per_r':125,
        'finite_error_vectors_verified':error_vectors,
        'finite_signature_distances_verified':error_vectors*6,
        'minimum_success_margin':[str(best[0]),best[1],list(best[2]),best[3]],
        'sharp_counterexample':{'r':64,'true_phase':4,'error':list(eps),
            'rival_phase':competitor,'decoded_phase':winners[0],
            'true_distance':str(distances[4]),'rival_distance':str(distances[3]),
            'rival_minus_true':str(margin),'observed_scaled_residuals':[str(v) for v in y]},
        'tail_range':f'all integer r>={TAIL_START}',
        'tail_rational_noise_bound_start':str(BOUND),
        'tail_noise_bound_general':'2*112500*r^3/(r-1)^5 decreasing strictly for r>1',
        'tail_residual_certificate':'six exact positive-coefficient residue polynomials from R749SRV show 0<R-P<35/12 for every r>=512',
        'tail_signature_min_separation':str(sep),
        'tail_half_separation':str(sep/2),
        'tail_verified_positive_polynomials':tails,
        'review':'AUTHOR_EXACT_NOT_REVIEWED'
    }

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
