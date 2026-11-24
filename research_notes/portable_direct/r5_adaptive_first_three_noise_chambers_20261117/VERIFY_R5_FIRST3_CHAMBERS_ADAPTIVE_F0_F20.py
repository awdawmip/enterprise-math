#!/usr/bin/env python3
"""R5 three noise chambers, sharp adaptive f=0..20 finite star minimax certificate.

Default checks the compact project-native count-center and window certificate;
--full-table checks ALL source counts and complete witness supports against the
original immutable frozen full-table file (SHA256 checked before parsing).
"""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def projection(mask, indices):
    return sum(1<<i for i,p in enumerate(indices) if (mask>>p)&1)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--full-table',type=Path)
    parser.add_argument('--f-max',type=int,default=20)
    args=parser.parse_args()
    assert 0<=args.f_max<=20
    cert=json.loads((ROOT/'CERTIFICATE_COMPACT_INPUT.json').read_text())
    assert cert['frozen_science_pin']=='435e77af0d180eac32bd1f9c4c464bc4010b7551'
    assert cert['witness_base_mask']==16 and cert['witness_alternatives']==[17,80,32]
    N={}
    for k,row in cert['query_rows'].items():
        vals=tuple(map(int,row['counts'].split(',')))
        axes=row['effective_bit_indices']
        assert len(vals)==(1<<len(axes))
        N[int(k)]=tuple(vals[projection(mask,axes)] for mask in range(256))
    assert set(N)=={214,223,294,295,296}
    full=None
    if args.full_table:
        data=args.full_table.read_bytes()
        assert hashlib.sha256(data).hexdigest()==cert['original_full_101_table_sha256']
        full={int(k):tuple(map(int,v['counts'])) for k,v in json.loads(data)['counts_and_cohorts'].items()}
        assert set(full)==set(range(214,315))
        assert all(len(v)==256 for v in full.values())
        assert all(full[k]==v for k,v in N.items())
    report={'schema':'R5_FIRST3_ADAPTIVE_NOISE_F0_F20_EXACT_V2',
      'frozen_science_pin':cert['frozen_science_pin'],
      'input_sha256':cert['original_full_101_table_sha256'],
      'original_full_table_crosschecked':bool(full),
      'chambers':[], 'review':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'}
    for idx,ch in enumerate(cert['noise_chambers']):
        lo,hi=int(ch['L']),int(ch['U'])
        Q=tuple(ch['Q'])
        assert lo>=0 and hi>lo and len(Q)==3 and tuple(sorted(Q))==Q
        windows=cert['witness_strong_windows_by_chamber'][idx]
        assert len(windows)==3
        assert [w[0] for w in windows]==list(Q)
        assert len({k for a,b in windows for k in range(a,b+1)})==sum(b-a+1 for a,b in windows)
        for leaf,(a,b) in enumerate(windows):
            assert 214<=a<=b<=314
            if full:
                actual=[k for k in range(214,315)
                        if abs(full[k][cert['witness_alternatives'][leaf]]-full[k][16])>lo]
                assert actual==list(range(a,b+1)),(idx,leaf,actual,(a,b))
            assert abs(N[Q[leaf]][cert['witness_alternatives'][leaf]]-N[Q[leaf]][16])>=hi
        center_gaps={}
        for k in Q:
            vals=sorted(set(N[k]))
            assert len(vals)>1
            gap=min(y-x for x,y in zip(vals,vals[1:]))
            assert gap>=hi,(idx,k,gap,hi)
            center_gaps[str(k)]=str(gap)
        worst_pair=min(max(abs(N[k][a]-N[k][b]) for k in Q)
                       for a in range(256) for b in range(a+1,256))
        assert worst_pair>=hi,(idx,worst_pair,hi)
        low,mid,high=Q
        assert mid<=2*low and high<=mid+2*low
        total=sum(Q)
        row={'chamber_index':idx+1,'two_eta_interval_left_closed_right_open':[str(lo),str(hi)],
          'optimal_test_min_costs':list(Q),'original_mask_pair_count_checked':32640,
          'full_256_mask_minimax_gap':str(worst_pair),
          'per_budget_min_distinct_center_gap':center_gaps,
          'witness_strong_windows_at_left':windows,
          'all_f_constructive_upper':f'{total}+{total+low}f',
          'finite_minimax':[]}
        for f in range(args.f_max+1):
            cap=f+1
            @lru_cache(None)
            def V(state):
                if sum(x<cap for x in state)<=1:return 0
                options=[]
                for j,cost in enumerate(Q,1):
                    values=[];stutter=False
                    for answer in (0,1,2):
                        nxt=tuple(min(cap,x+(answer!=int(h==j))) for h,x in enumerate(state))
                        if nxt==state:
                            stutter=True;break
                        if any(x<cap for x in nxt):values.append(V(nxt))
                    if values and not stutter:options.append(cost+max(values))
                assert options,state
                return min(options)
            exact=V((0,0,0,0))
            upper=total+f*(total+low)
            assert exact==upper,(idx+1,f,exact,upper)
            row['finite_minimax'].append({'f':f,'optimal_cost':exact,
                                           'exhaustive_states':V.cache_info().currsize})
        report['chambers'].append(row)
    report['status']='PASS_R5_FIRST_THREE_NOISE_CHAMBERS_ADAPTIVE_F0_TO_F'+str(args.f_max)
    (ROOT/'RESULTS_FIRST3_ADAPTIVE_EXACT.json').write_text(
        json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(report['status'])
    for row in report['chambers']:
        print(row['chamber_index'],row['all_f_constructive_upper'],
              'f1=',row['finite_minimax'][1]['optimal_cost'],
              'fmax=',row['finite_minimax'][-1]['optimal_cost'])
if __name__=='__main__':main()
