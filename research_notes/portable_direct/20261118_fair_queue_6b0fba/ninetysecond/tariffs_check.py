"""Read frozen records only. No policy or scientific worker is imported."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile

INTAKE='1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d'
ORIGINAL='4514051d6564462eb24610e63040a35742344dd4c77aca76b271151de2c244d4'
ANALYSIS='2e866b6c29879469c9ca57dc858fbd18f91e3fc811477111dc3622250cc7b106'
FIELDS=('copied_terms','coefficient_visits','shifted_terms','merge_row_visits','transform_row_visits')
GROUPS=((11,5,8),(44,41,47),(39,42,45,48))


def digest(data):
    return sha256(data).hexdigest()


def qi(q):
    return str(Q(q))


def tariff_classes(vectors):
    A0,B0,C0=GROUPS
    def signs(prices):
        sums={r:sum(a*b for a,b in zip(prices,v)) for r,v in vectors.items()}
        assert all(x!=0 for x in sums.values())
        return tuple(sorted(r for r,x in sums.items() if x>0))
    assert all(x>0 for x in vectors[38])
    for group in (A0,B0):
        assert all(vectors[i][1:]==vectors[group[0]][1:] for i in group)
        assert all(vectors[i][0]>vectors[j][0] for i,j in zip(group,group[1:]))
    assert len({vectors[i] for i in C0})==1
    assert 25297*12058<70678*23735 and 25297*11590<16840*23735
    witnesses=[]
    for i,A in enumerate((9000,11000,12000,13000)):
        for j,B in enumerate((17000,17500,18200,19000)):
            z=Q(1,100)
            y=(B-A-1562*z)/2092
            t=A+11590*y-23735*z
            prices=(1,y,z,t/43008,t/43008)
            assert min(prices)>0
            good=signs(prices)
            assert set(good)=={38,*A0[:i],*B0[:j]}
            witnesses.append((good,[qi(x) for x in prices]))
    prices=(1,1,1,4,4)
    good=signs(prices)
    assert len(good)==11
    witnesses.append((good,[qi(x) for x in prices]))
    assert len(set(a for a,b in witnesses))==17
    radii={i:Q(abs(sum(v)),sum(map(abs,v))) for i,v in vectors.items()}
    total=tuple(map(sum,zip(*vectors.values())))
    assert total==(-326119,-75914,273581,268800,236544)
    return dict(chamber_count=len(witnesses),attainable_benefit_counts=sorted({len(a) for a,b in witnesses}),
                strict_rational_witnesses=witnesses,unit_price_vector_radius=qi(min(radii.values())),
                unit_price_radius_by_event={k:qi(v) for k,v in radii.items()},
                aggregate_radius=qi(Q(sum(total),sum(map(abs,total)))))


def score(ref,history,u,direction):
    f=(Q(1)+sum(Q(max(0,A+direction*u),B) for A,B in history))/(len(history)+1)
    return ref*max(Q(1,4),min(Q(4),Q(f)))


def request(z,events,interaction):
    step=z['step']
    assert z['snapshot_before_source_build_and_online_execution']
    # The final tuple order is the frozen within-list order on a remaining tie.
    items=[('full_fft',z['full_reference_base'],z['full_training_steps'],z['full_reference_key_sha256'],
            Q(*z['full_calibrated']),(0,))]
    for idx,c in enumerate(z['candidates']):
        items.append((c['candidate_signature'],c['reference_base'],c['training_steps'],
                      c['reference_key_sha256'],Q(*c['calibrated_total']),(1,*c['decision_tie_key'],idx)))
    obs={}
    for sig,reference,steps,key,value,tie in items:
        available=[e['step'] for e in events[:step] if e['reference_key_sha256']==key][-8:]
        assert steps==available and all(events[i]['origin']=='SELECTED_ONLINE' for i in steps)
        h=tuple((events[i]['actual'],events[i]['reference_base']) for i in steps)
        assert score(reference,h,0,0)==value
        if key in obs:
            assert obs[key]==h
        obs[key]=h
    anchor_fields=[(z['full_anchor_base'],z['full_raw'])]+[(c['anchor_base'],c['raw_total']) for c in z['candidates']]
    for (_,_,steps,_,actual,_),(B0,Bt) in zip(items,anchor_fields):
        stable=[(events[i]['actual'],B0) for i in steps]
        moving=[(events[i]['actual'],events[i]['raw_base']) for i in steps]
        f0=score(1,moving,0,0)
        f1=score(1,stable,0,0)
        mixed=(B0-Bt)*(f1-f0)
        assert B0*f1-Bt*f0==(B0-Bt)*f0+Bt*(f1-f0)+mixed
        assert actual==(B0*f1 if z['reference_mode']=='stable' else Bt*f0)
        interaction['positive' if mixed>0 else 'negative' if mixed<0 else 'zero']+=1
    winner=min(items,key=lambda r:(r[4],r[5]))
    assert winner[0]==z['selected_candidate_signature']
    sig,ref,steps,key,best,tie=winner
    ranks=[r for r in items if r[0]!=sig]
    # Distinct offers with the same old training key keep their order exactly.
    rivals=[r for r in ranks if r[3]!=key]
    if not ranks:
        return None,None,len(items)
    raw_margin=min(r[4] for r in ranks)-best
    max_base=max([1]+[B for h in obs.values() for A,B in h])
    big=max([36*max_base]+[A for h in obs.values() for A,B in h])
    def can_flip(u):
        high=(score(ref,obs[key],u,1),tie)
        return any((score(r[1],obs[r[3]],u,-1),r[5])<high for r in rivals)
    assert not can_flip(0)
    if not can_flip(big):
        return None,raw_margin,len(items)
    lo,hi=0,big
    while hi-lo>1:
        mid=(lo+hi)//2
        if can_flip(mid):
            hi=mid
        else:
            lo=mid
    assert not can_flip(hi-1) and can_flip(hi)
    return hi,raw_margin,len(items)


def main(intake,analysis):
    assert digest(intake.read_bytes())==INTAKE
    evidence_hash=digest(analysis.read_bytes())
    assert evidence_hash in (ANALYSIS,ORIGINAL)
    with ZipFile(intake) as z:
        sup=json.loads(z.read('evidence/S15_MINIMAL_SUPPLEMENT.json'))
        d=json.loads(z.read('evidence/S14_S15_INDEPENDENT_RESULT_EM_S15SUPPORT_866CDE_20261001.json'))
    cases=sup['per_request_certificate_availability']
    stats=cases['stats']
    assert len(cases['requests'])==768 and all(r[-1]=='U0' for r in cases['requests'])
    h=d['request_decomposition']['eleven_choice_changes']
    assert len(h)==11 and len(cases['all_44_aligned_choice_changes'])==44
    assert all(len({e[2] for e in cases['all_44_aligned_choice_changes'] if tuple(e[:2])==rb})==11
               for rb in {tuple(e[:2]) for e in cases['all_44_aligned_choice_changes']})
    vectors={r['request_one_based']:tuple(r['moving_minus_stable_selected_scientific_vector'][c] for c in FIELDS) for r in h}
    out=tariff_classes(vectors)
    assert sum(sum(v)>0 for v in vectors.values())==7
    out['diagnostic_thresholds']={}
    for c in d['cost_accounting']['comparisons']:
        S=c['science_saved_sum'];extra=c['fixed_alternative_diagnostic_work_increase']
        assert S==376892 and c['online_pair_verifier_science_increase']==extra-S
        out['diagnostic_thresholds'][c['budget_records']]=qi(Q(S,extra))
    source=cases['sources']
    hist=defaultdict(list)
    counts=Counter()
    interaction=Counter()
    with ZipFile(analysis) as arch:
        def member(meta):
            prefix='inputs/s15/' if evidence_hash==ANALYSIS else ''
            raw=arch.read(prefix+meta['archive_member'])
            assert len(raw)==meta['bytes'] and digest(raw)==meta['sha256']
            return raw
        for k,info in sorted(source.items()):
            if info['study']!='S15' or info['role']!='frozen_predictions':
                continue
            events=json.loads(member(source[info['training_source_id']]))
            rows=[json.loads(x) for x in member(info).splitlines()]
            assert len(rows)==len(events)==48 and all(e['step']==i for i,e in enumerate(events))
            budget=info['policy']
            for row in rows:
                radius,margin,offers=request(row,events,interaction)
                hist[budget].append((radius,None if margin is None else qi(margin)))
                counts['requests']+=1;counts['offers']+=offers
    assert counts['requests']==stats['S15']['frozen_requests']==384
    assert counts['offers']==stats['S15']['prediction_offers']==1952
    summary={}
    for mode,rows in sorted(hist.items()):
        assert len(rows)==96 and rows[:48]==rows[48:]
        representative=rows[:48];finite=[r for r,m in representative if r is not None]
        summary[mode]=dict(finite=len(finite),infinite=48-len(finite),
                           smallest_finite=min(finite,default=None),largest_finite=max(finite,default=None),
                           raw_zero_margin=sum(m=='0' for r,m in representative),
                           infinite_despite_raw_tie=sum(r is None and m=='0' for r,m in representative),
                           first_admissible_integer_error=[r for r,m in representative])
    out['request_summary']=summary
    out['offerwise_fixed_history_interaction_signs']=dict(interaction)
    out['scope']=dict(S15_requests=384,S14_source_status_rows=384,changed_comparisons=44,
                      differing_request_indices=11,calibrated_offers=1952,true_online_certificates=0)
    return out


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--intake',type=Path,required=True);p.add_argument('--records',type=Path,required=True,help='pinned original S15 archive or pinned independent archive containing its unchanged logs')
    args=p.parse_args()
    print(json.dumps(main(args.intake,args.records),ensure_ascii=False,indent=2,sort_keys=True))
