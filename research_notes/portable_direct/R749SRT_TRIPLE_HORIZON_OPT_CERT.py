#!/usr/bin/env python3
"""Exhaustive three-read offset optimization under 0<a<b<=12, exact arithmetic."""
import json
from itertools import combinations
from fractions import Fraction as Q
from R749SRT_MULTIREAD_DECODER_CERT import counts, residual, PHASE, tail_certificate

def run():
    C,T=counts()
    assert len(tail_certificate(C,T))==6
    Y=[None]+[residual(r,C,T) for r in range(1,524)]
    rows=[]
    for a,b in combinations(range(1,13),2):
        shifts=(0,a,b)
        signatures=[tuple(PHASE[(phase+h)%6] for h in shifts) for phase in range(6)]
        distinct=list(dict.fromkeys(signatures))
        if len(distinct)!=6:
            rows.append({'shifts':list(shifts),'states':len(distinct),'reason':'not full-phase distinguishing'})
            continue
        sep=min(max(abs(x-y) for x,y in zip(S1,S2)) for S1,S2 in combinations(distinct,2))
        assert sep>=Q(35,6)
        fails=[]
        for r in range(1,512):
            observed=tuple(Y[r+h] for h in shifts)
            distances=[max(abs(x-y) for x,y in zip(observed,S)) for S in signatures]
            margin=min(distances[ph]-distances[r%6] for ph in range(6) if ph!=r%6)
            if margin<=0:fails.append(r)
        assert fails
        tau=fails[-1]+1
        rows.append({'shifts':list(shifts),'states':6,'separation':str(sep),'sharp_threshold':tau,'last_failure_r':fails[-1]})
    allfull=[row for row in rows if row['states']==6]
    opt=min(row['sharp_threshold'] for row in allfull)
    winners=[r['shifts'] for r in allfull if r['sharp_threshold']==opt]
    best_by_horizon={str(h):min((r['sharp_threshold'],r['shifts']) for r in allfull if r['shifts'][-1]<=h) for h in range(2,13)}
    assert opt==35 and winners==[[0,1,5]]
    assert len(rows)==66
    return {'status':'PASS','proof':'positive polynomial tail r>=512 plus finite exhaustive exact nearest-signature comparisons 1..511',
        'search_domain':'0<a<b<=12; three observations and six distinguishable ideal signatures',
        'total_triplets':66,'full_phase_triplets':len(allfull),'other_triplets':len(rows)-len(allfull),
        'exact_finite_comparisons':len(allfull)*511,'optimal_threshold':opt,'unique_best_sets':winners,
        'best_by_max_offset':{h:{'threshold':v[0],'shifts':list(v[1])} for h,v in best_by_horizon.items()},
        'all_candidates':rows,'review':'AUTHOR_EXACT_NOT_REVIEWED'}

if __name__=='__main__':print(json.dumps(run(),indent=2,ensure_ascii=False))
