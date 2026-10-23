"""Audit complete K=11/12/13/14 census and directly verify every optimal witness.

The two C++ implementations share the producer-search idea; they are not an
independent mathematical review. This checker uses integer tuple sumsets for
positive witnesses and exact row/decision comparison for negative searches.
"""
import argparse
from collections import Counter
import hashlib
from itertools import combinations
import json
from pathlib import Path
import re

from boolean_sumset_tools import layers, simplex, sumset


def read_decisions(path, raw, expected_budget):
    pattern = re.compile(r'\S+ row=(\d+) Q=([0-9,]+) base_uncovered=(\d+) K=(\d+) answer=(YES|NO|UNKNOWN) nodes=(\d+) W=([0-9,]*)')
    decisions = []
    for i, line in enumerate(path.read_text().splitlines()):
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError('invalid census line at '+str(i))
        row, q, missing, budget, status, nodes, w = match.groups()
        ids = tuple(map(int, q.rstrip(',').split(',')))
        if int(row) != i or int(budget) != expected_budget or ids != tuple(raw[i*27:i*27+9]):
            raise ValueError('census row/budget differs from frozen input')
        if status == 'UNKNOWN':
            raise ValueError('incomplete search cannot certify an optimum')
        witness = tuple(map(int, w.rstrip(',').split(','))) if w else ()
        decisions.append({'status':status,'nodes':int(nodes),'w':witness})
    if len(decisions)*27 != len(raw):
        raise ValueError('census does not cover the complete input')
    return decisions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    run=args.run_dir
    raw=(run/'distance3_remove1264_180.bin').read_bytes()
    eligible=(run/'eligible_no_support_obstruction_180.bin').read_bytes()
    rows=list(map(int,(run/'eligible_original_row_numbers_180.txt').read_text().splitlines()))
    q0={0,1,2,3,4,51,64,71,74};outside=sorted(set(range(84))-q0)
    expected=b''.join(bytes(sorted((q0-{1,2,64})|set(a)))+bytes(18)
                      for a in combinations(outside,3))
    assert raw==expected and len(raw)==67525*27
    assert len(set(rows))==646 and len(eligible)==646*27
    assert eligible==b''.join(raw[i*27:(i+1)*27] for i in rows)
    d11=read_decisions(run/'primary_180.log',raw,11)
    assert all(d['status']=='NO' for d in d11)
    d12=read_decisions(run/'eligible_k12_results_180.log',eligible,12)
    d13=read_decisions(run/'fresh_k13_results.log',eligible,13)
    d14=read_decisions(run/'fresh_k14_results.log',eligible,14)
    assert all(d['status']=='YES' for d in d14)
    second=(run/'fresh_independent_k13.log').read_text().splitlines()
    independent_yes={int(re.match(r'YES Qindex=(\d+)',s)[1]) for s in second[:-1]}
    assert independent_yes=={i for i,d in enumerate(d13) if d['status']=='YES'}
    assert 'rows=646 feasible=216 impossible=430 budget=13' in second[-1]
    low,x3,x4=layers(8)
    target=set(simplex(16))
    optimum=[]
    for i in range(646):
        k=12 if d12[i]['status']=='YES' else (13 if d13[i]['status']=='YES' else 14)
        chosen={12:d12,13:d13,14:d14}[k][i]['w']
        assert len(set(chosen))==len(chosen)==k
        q=tuple(eligible[i*27:i*27+9])
        actual=sumset(low+tuple(x3[j] for j in q)+tuple(x4[j] for j in chosen))
        assert actual==target and len(actual)==969
        optimum.append({'eligible_row':i,'original_row':rows[i],'q':q,'minimum_w':k,
                        'total_states':54+k,'optimal_witness':chosen,
                        'witness_sumset_exactly_delta16':True})
    counts=Counter(row['minimum_w'] for row in optimum)
    assert counts=={12:1,13:215,14:430}
    historical={line.split('  ',1)[1]:line.split('  ',1)[0]
                for line in (run/'SHA256SUMS_PREFIX180.txt').read_text().splitlines()}
    recovered=[]
    for name in ['distance3_remove1264_180.bin','eligible_no_support_obstruction_180.bin',
                 'eligible_original_row_numbers_180.txt','primary_180.log','eligible_k12_results_180.log']:
        data=(run/name).read_bytes();sha=hashlib.sha256(data).hexdigest()
        assert sha==historical[name]
        recovered.append({'path':name,'bytes':len(data),'sha256':sha,'matches_historical_digest':True})
    certificate={'schema':'EM_PREFIX180_RECONSTRUCTED_COMPLETE_OPTIMUM_V1',
        'researcher_id':'EM-RECOVERY-0AD96A','status':'AUTHOR_PROVED_AND_EXACT_COMPUTATION_CHECKED_UNREVIEWED',
        'population':{'frozen_q_family':67525,'uncompletable_for_any_w':66879,'completable':646},
        'minimum_w_distribution':dict(sorted(counts.items())),
        'minimum_total_states_distribution':{'66':1,'67':215,'68':430},
        'arithmetic':'integer tuple sums and exact finite Boolean producer masks',
        'primary_search_nodes':{'11':sum(d['nodes'] for d in d11),'12':sum(d['nodes'] for d in d12),
                                '13':sum(d['nodes'] for d in d13),'14':sum(d['nodes'] for d in d14)},
        'k13_second_implementation_summary':second[-1],
        'negative_proof_basis':'complete producer branching with sound disjoint-union lower bound; K13 rowwise YES set agrees with second implementation',
        'positive_proof_basis':'each of all 646 chosen optimal witnesses separately checked by integer tuple sumset equality',
        'recovered_files':recovered,'configurations':optimum,
        'excluded_claims':['unrestricted global beta_4(8) lower bound','PREFIX179 joint-family cardinality',
                           'native full-X6 dynamics','independent Driver review','formal proof assistant verification']}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(certificate,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in certificate.items() if k!='configurations'},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
