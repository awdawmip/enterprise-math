#!/usr/bin/env python3
"""R5 first three noise chambers: sharp adaptive unmarked errors f=0..20.

Use the supplied compact certificate. Optional --full-table <file> performs an
exact byte-bound crosscheck against the frozen full 101-budget R5 input.
Only standard-library arbitrary-precision integer arithmetic is used.
"""
import argparse, hashlib, json
from functools import lru_cache
from pathlib import Path

BASE=Path(__file__).resolve().parent

def bitproj(mask,positions):
    return sum(1<<i for i,p in enumerate(positions) if (mask>>p)&1)

def main():
    cli=argparse.ArgumentParser()
    cli.add_argument('--full-table',type=Path)
    cli.add_argument('--f-max',type=int,default=20)
    args=cli.parse_args()
    assert 0<=args.f_max<=20
    cert=json.loads((BASE/'CERTIFICATE_COMPACT_INPUT.json').read_text())
    assert cert['frozen_science_pin']=='435e77af0d180eac32bd1f9c4c464bc4010b7551'
    N={}
    for k,item in cert['query_rows'].items():
        pos=item['effective_bit_indices']
        counts=list(map(int,item['counts']))
        assert len(counts)==2**len(pos)
        N[int(k)]=tuple(counts[bitproj(mask,pos)] for mask in range(256))
    d={int(k):tuple(map(int,v)) for k,v in cert['witness_differences'].items()}
    assert set(d)==set(range(214,315)) and len(d)==101
    assert cert['witness_base_mask']==16 and cert['witness_alternatives']==[17,80,32]
    if args.full_table is not None:
        raw=args.full_table.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==cert['original_full_101_table_sha256']
        full=json.loads(raw)['counts_and_cohorts']
        assert set(map(int,full))==set(d)
        for k,v in full.items():
            k=int(k);a=tuple(map(int,v['counts']))
            assert len(a)==256
            if k in N: assert a==N[k]
            assert tuple(a[q]-a[16] for q in (17,80,32))==d[k]

    report={'schema':'R5_FIRST_THREE_CHAMBERS_ADAPTIVE_F0_F20_V1',
            'frozen_science_pin':cert['frozen_science_pin'],
            'input_sha256':cert['original_full_101_table_sha256'],
            'full_table_crosschecked':args.full_table is not None,
            'semantics':'real scalar observations; absolute error <=eta; <=f unmarked arbitrary corruptions',
            'chambers':[], 'author_review':'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED'}
    for j,ch in enumerate(cert['noise_chambers'],1):
        lo,hi=int(ch['L']),int(ch['U']);Q=tuple(ch['Q']);S=sum(Q)
        assert 0<=lo<hi and len(Q)==3 and Q==tuple(sorted(Q))
        wins=[[k for k in sorted(d) if abs(d[k][h])>lo] for h in range(3)]
        assert all(w for w in wins)
        assert len({k for w in wins for k in w})==sum(map(len,wins))
        cheapest=tuple(min(w) for w in wins)
        assert cheapest==Q, (j,cheapest,Q)
        assert all(abs(d[k][h])>=hi for h,k in enumerate(Q))
        center_gaps={}
        for k in Q:
            u=sorted(set(N[k]))
            assert len(u)>1
            gap=min(b-a for a,b in zip(u,u[1:]))
            assert gap>=hi,(j,k,gap,hi)
            center_gaps[str(k)]=str(gap)
        pair_gaps=[]
        for a in range(256):
            for b in range(a+1,256):
                pair_gaps.append(max(abs(N[k][a]-N[k][b]) for k in Q))
        assert len(pair_gaps)==32640
        min_pair=min(pair_gaps)
        assert min_pair>=hi,(j,min_pair,hi)
        high,mid,lowcost=Q[::-1]
        assert mid<=2*lowcost and high<=mid+2*lowcost
        entry={'stage':j,'two_eta_interval':['['+str(lo),str(hi)+')'],
               'budgets':list(Q),'full_256_state_minimax_pair_gap':str(min_pair),
               'per_budget_min_center_gap':center_gaps,
               'witness_strong_windows_at_left':[[min(w),max(w),len(w)] for w in wins],
               'all_f_constructive_upper':f'{S}+f*{S+lowcost}',
               'finite_exact':[]}
        for f in range(args.f_max+1):
            cap=f+1
            @lru_cache(None)
            def V(dstate):
                if sum(x<cap for x in dstate)<=1:return 0
                actions=[]
                for leaf,cost in enumerate(Q,1):
                    children=[];selfloop=False
                    for answer in (0,1,2):
                        nxt=tuple(min(cap,x+(answer != int(h==leaf))) for h,x in enumerate(dstate))
                        if nxt==dstate:
                            selfloop=True;break
                        if any(x<cap for x in nxt):children.append(V(nxt))
                    if children and not selfloop:actions.append(cost+max(children))
                assert actions,dstate
                return min(actions)
            lower=V((0,0,0,0))
            upper=S+f*(S+lowcost)
            assert lower==upper,(j,f,lower,upper)
            entry['finite_exact'].append({'f':f,'optimal_worst_cost':lower,
                                          'bellman_states':V.cache_info().currsize})
        report['chambers'].append(entry)
    report['status']=f'PASS_R5_FIRST_THREE_NOISE_CHAMBERS_ADAPTIVE_F0_TO_F{args.f_max}'
    (BASE/'RESULTS_FIRST3_ADAPTIVE_EXACT.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print(report['status'])
    for ch in report['chambers']:
        print('chamber',ch['stage'],'Q',ch['budgets'],'f=1',
              ch['finite_exact'][1]['optimal_worst_cost'],'f='+str(args.f_max),
              ch['finite_exact'][-1]['optimal_worst_cost'])
if __name__=='__main__':main()
