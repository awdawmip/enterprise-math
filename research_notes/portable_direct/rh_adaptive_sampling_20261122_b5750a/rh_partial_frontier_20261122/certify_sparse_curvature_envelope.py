#!/usr/bin/env python3
"""Sparse-observation upper/lower envelopes on the existing q road.

The adaptive rule sees only the samples it requests.  The first execution
extracts those observations from the already existing certified cache; later
executions replay the saved observation table without reading the full cache.
No complete road is generated here.  Query counts do not measure the original
cost of generating the historical cache or a fresh full-prefix sample.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import heapq
import json
import pickle
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'rh_joint_certificate'))
from certify_joint_energy import (A,B,DIGITS,SCALE,ZERO,add,sub,scale,square,
    positive,isum,record,interval_from_record,rat)

SOURCE=ROOT/'rh_triangle_certificate_20261122/dyadic_triangle_certificate.json'
REFERENCE=ROOT/'rh_reference_certificate_20261122/reference_split_certificate.json'
OBS=OUT/'sparse_sample_observations.json'
CACHE=ROOT/'rh_joint_certificate/_scratch_arrays.pkl'
TOL=F(1,10000)
EPS_D=F(1,1000000)
C=1+F(1,2*A*A)+EPS_D
LOWER_SOURCE=F(-12)


def main():
    started=time.perf_counter()
    if OBS.exists():
        obs_doc=json.loads(OBS.read_text())
        available={x['n']:interval_from_record(x['value']) for x in obs_doc['samples']}
        provenance=obs_doc['provenance']
        summary=obs_doc['source_summary']
        source_mode='replay previously extracted sparse observations only'
        cache_q=None
    else:
        source=json.loads(SOURCE.read_text())
        reference=json.loads(REFERENCE.read_text())
        tree_path=ROOT/'rh_tree_order_20261122/optimal_tree_order_certificate.json'
        signed_path=ROOT/'rh_signed_subtree_20261122/signed_frontier_certificate.json'
        tree=json.loads(tree_path.read_text())
        signed=json.loads(signed_path.read_text())['roads']['q']
        summary={'backbone':source['partition']['backbone'],
            'eta_B':reference['pointwise_matching']['eta_B'],
            'actual_energy_for_audit_only':source['roads']['q']['energies']['actual_positive_energy_closed'],
            'benchmark_records_for_audit_only':{
                'old_positive_packet_budget':source['roads']['q']['energies']['closed_squared_budget_J_plus_local_packets_plus_actual_local_remainder'],
                'free_tree_budget':tree['closed_optimal_tree_budget'],
                'signed_25_budget':next(r['closed_squared_budget'] for r in signed['energy_frontier_dp'] if r['node_budget']==25),
                'full_38_fine_budget':signed['baselines']['full_signed_interpolant']}}
        if not CACHE.exists():
            raise SystemExit('Missing sparse_sample_observations.json and original cache; no road regeneration is performed.')
        cache_bytes=CACHE.read_bytes()
        data=pickle.loads(cache_bytes)
        assert (data['A'],data['B'],data['SCALE'])==(A,B,SCALE)
        cache_q=data['q']
        available={}
        provenance={'cache_path':str(CACHE.relative_to(ROOT)),
            'cache_sha256':hashlib.sha256(cache_bytes).hexdigest(),
            'triangle_certificate_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            'source_summary_inputs':[{'path':str(p.relative_to(ROOT)),
                'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [SOURCE,REFERENCE,tree_path,signed_path]],
            'extraction':'Existing outward interval q entries at requested integer points; no D/source/full-road recomputation.'}
        source_mode='extract requested samples from the existing certified cache'
        del data,cache_bytes
    eta=interval_from_record(summary['eta_B'])
    assert eta[1]*EPS_D.denominator<=EPS_D.numerator*SCALE
    queried={};query_order=[]

    def query(n):
        assert n not in queried
        v=available[n] if cache_q is None else tuple(cache_q[n])
        queried[n]=v;query_order.append(n)
        return v

    # H[n]=n*H_n is a completely rational, source-independent potential:
    # Delta^2 H[n]=1/n.  Outward arithmetic encloses the exact rational.
    potential=[ZERO]*(B+1)
    harmonic=ZERO
    for n in range(1,B+1):
        harmonic=add(harmonic,rat(F(1,n)))
        potential[n]=scale(harmonic,n)

    cells={};heap=[];build_checks=0;split_checks=0

    def cell(a,b):
        nonlocal build_checks
        h=b-a;qa,qb=queried[a],queried[b]
        upper=[qa];lower=[qa];up_terms=[];lo_terms=[]
        for n in range(a+1,b+1):
            if n==b:
                u=l=qb
            else:
                alpha=F(b-n,h);beta=F(n-a,h)
                chord=add(scale(qa,alpha),scale(qb,beta))
                chord_h=add(scale(potential[a],alpha),scale(potential[b],beta))
                v=positive(sub(chord_h,potential[n]))
                u=add(chord,scale(v,C))
                l=add(chord,scale(v,LOWER_SOURCE))
                assert l[0]<=u[1]
                build_checks+=1
            upper.append(u);lower.append(l)
            up_terms.append(scale(square(positive(u)),F(1,n*n)))
            lo_terms.append(scale(square(positive(l)),F(1,n*n)))
        eu=isum(up_terms);el=isum(lo_terms)
        gap=positive(sub(eu,el))
        obj={'a':a,'b':b,'upper':upper,'lower':lower,'eu':eu,'el':el,'gap':gap}
        cells[(a,b)]=obj
        if h>1 and gap[1]>0:
            heapq.heappush(heap,(-gap[1],a,b))
        return obj

    bones=summary['backbone']
    for n in bones:query(n)
    end_a=scale(square(positive(queried[A])),F(1,A*A))
    for a,b in zip(bones,bones[1:]):cell(a,b)
    actual=interval_from_record(summary['actual_energy_for_audit_only'])
    thresholds={k:interval_from_record(v) for k,v in summary['benchmark_records_for_audit_only'].items()}
    crossed={};snapshots=[];milestones={6,16,32,44,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096}
    monotone_up=True;monotone_lo=True;minimum_observed_upper_gap=None
    eu=add(end_a,isum(o['eu'] for o in cells.values()))
    el=add(end_a,isum(o['el'] for o in cells.values()))
    previous_up=eu;previous_lo=el
    while True:
        count=len(queried)
        assert el[1]<actual[0] and actual[1]<eu[0]
        new_cross=[]
        for name,value in thresholds.items():
            if name not in crossed and eu[1]<value[0]:
                crossed[name]={'sample_count':count,'upper_energy':record(eu)}
                new_cross.append(name)
        certified_gap=eu[1]-el[0]
        if count in milestones or new_cross or certified_gap*TOL.denominator<=TOL.numerator*SCALE:
            snapshots.append({'sample_count':count,'cell_count':len(cells),
                'lower_energy':record(el),'upper_energy':record(eu),
                'enclosure_gap_upper':record((certified_gap,certified_gap)),
                'crossed_at_this_step':new_cross})
        if certified_gap*TOL.denominator<=TOL.numerator*SCALE:
            break
        if not heap:
            raise AssertionError('All cells resolved before requested gap was attained.')
        _,a,b=heapq.heappop(heap)
        old=cells.pop((a,b));x=(a+b)//2
        qx=query(x)
        e_up=sub(old['upper'][x-a],qx)
        e_lo=sub(qx,old['lower'][x-a])
        assert e_up[0]>0 and e_lo[0]>0
        if minimum_observed_upper_gap is None or e_up[0]<minimum_observed_upper_gap:
            minimum_observed_upper_gap=e_up[0]
        left=cell(a,x);right=cell(x,b)
        for n in range(a+1,b):
            new=left if n<=x else right
            alpha=F(n-a,x-a) if n<=x else F(b-n,b-x)
            predicted_up=sub(old['upper'][n-a],scale(e_up,alpha))
            predicted_lo=add(old['lower'][n-a],scale(e_lo,alpha))
            measured_up=new['upper'][n-new['a']]
            measured_lo=new['lower'][n-new['a']]
            assert max(predicted_up[0],measured_up[0])<=min(predicted_up[1],measured_up[1])
            assert max(predicted_lo[0],measured_lo[0])<=min(predicted_lo[1],measured_lo[1])
            split_checks+=1
        eu=add(sub(eu,old['eu']),add(left['eu'],right['eu']))
        el=add(sub(el,old['el']),add(left['el'],right['el']))
        monotone_up=monotone_up and eu[0]<=previous_up[1]
        monotone_lo=monotone_lo and el[1]>=previous_lo[0]
        previous_up,previous_lo=eu,el
    assert monotone_up and monotone_lo
    direct_eu=add(end_a,isum(o['eu'] for o in cells.values()))
    direct_el=add(end_a,isum(o['el'] for o in cells.values()))
    assert max(eu[0],direct_eu[0])<=min(eu[1],direct_eu[1])
    assert max(el[0],direct_el[0])<=min(el[1],direct_el[1])
    # Data extraction is a separate historical input fact.  A replay reads
    # this table alone; the adaptive selector never sees future values.
    if not OBS.exists():
        obs_doc={'schema':'EM_SPARSE_Q_OBSERVATIONS_V1','provenance':provenance,
            'source_summary':summary,
            'window':{'A':A,'B':B},'denominator_power_of_10':DIGITS,
            'query_order':query_order,
            'samples':[{'n':n,'value':record(queried[n])} for n in query_order]}
        OBS.write_text(json.dumps(obs_doc,ensure_ascii=False,indent=2)+'\n')
    else:
        assert query_order==obs_doc['query_order']
        assert set(queried)==set(available)
    output={'schema':'EM_SPARSE_CURVATURE_ENVELOPE_V1','status':'PASS',
        'science_freeze':'9fc068244e4f1117f1e75df5eb0285c6697d21d7',
        'scope':'Certified sparse-observation simulation on the existing full-integer q road. No road generation, no arithmetic query-time saving claim, no optimal adaptive-query claim, no RH conclusion.',
        'window':{'A':A,'B':B,'full_integer_count':B-A+1},
        'arithmetic':{'denominator_power_of_10':DIGITS,'method':'outward integer intervals and exact rational source/geometry'},
        'source_bounds':{'epsilon_D':str(EPS_D),'independent_D_matching_bound_eta_B':record(eta),
            'upper_f':'C/n','C':str(C),'lower_f':'-12/n',
            'proof':'|D-Lambda|<=eta_D<=eta_B<10^-6 by the direct D interpolation bound; kappa<=1+1/(2A^2); Lambda>=0 and Lambda<=log n; log B<45/4.'},
        'potential':'H(n)=n*sum_(k<=n)1/k, Delta^2 H=1/n; U=linear(samples)+C*(linear(H)-H); L=linear(samples)-12*(linear(H)-H)',
        'selection':'Take the cell with largest current certified energy-gap upper endpoint; ties by (a,b); query integer midpoint. Future sample values are not used.',
        'stopping_rule':{'absolute_energy_enclosure_gap':str(TOL)},
        'sample_count':len(queried),'interior_new_queries':len(queried)-len(bones),
        'final_lower_energy':record(direct_el),'final_upper_energy':record(direct_eu),
        'actual_energy_old_certificate_for_audit_only':record(actual),
        'crossed_benchmarks':crossed,'snapshots':snapshots,
        'final_partition':sorted({n for p in cells for n in p}),
        'checks':{'upper_lower_order_and_source_barrier_point_evaluations':build_checks,
            'split_tent_identity_interval_consistency_points':split_checks,
            'monotone_upper_and_lower_energy_interval_consistency':monotone_up and monotone_lo,
            'all_observed_split_gaps_strictly_positive':True,
            'minimum_upper_query_gap_lower':record((minimum_observed_upper_gap,minimum_observed_upper_gap)),
            'direct_partition_cost_matches_incremental_cost':True,
            'all_snapshot_brackets_contain_old_complete_energy_interval':True},
        'oracle_source_mode':source_mode,
        'historical_source_provenance':provenance,
        'inputs':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in [OBS,ROOT/'rh_joint_certificate/certify_joint_energy.py',
                ROOT/'rh_correlation_rational/certify_matched_nodes.py']],
        'runtime_seconds':time.perf_counter()-started}
    target=OUT/'sparse_curvature_envelope_certificate.json'
    target.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'PASS','sample_count':len(queried),
        'lower':record(direct_el),'upper':record(direct_eu),
        'crossed':{k:v['sample_count'] for k,v in crossed.items()},
        'elapsed_seconds':output['runtime_seconds'],'output_bytes':target.stat().st_size},ensure_ascii=False))


if __name__=='__main__':
    main()
