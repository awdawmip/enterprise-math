#!/usr/bin/env python3
"""EC49FAQ: H2-root BRC observer rigidity and exact key/cost certificates.
Frozen scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Run: python VERIFY_EC49FAQ.py > EXACT_REPORT_EC49FAQ.json
"""
import itertools, json, math
from fractions import Fraction
from collections import defaultdict, Counter

OPS={'a':(-1,-1),'b':(-2,-2),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
     'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
START=(('N',0),('N',1),('N',2),('A',0),('A',2),
       ('B',0),('B',1),('AB',0),('BA',0))
BUCKET=('N','A','B','AB','BA')
B2=('de','ed','ce','ec'); B3=('feg','gef')
CASES={
1512:{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgg','geffgg'],7:['fegfggg','geffggg']},
1513:{4:['defg','edfg','fegc','gefc'],5:['fegfg','geffg'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']},
2200:{4:['fegg','gefg'],5:['feggd','gefgd','feggc','gefgc'],6:['fegggf','gefggf'],7:['fegggfg','gefggfg']},
2203:{4:['fegf','geff'],5:['fegfd','geffd','fegfc','geffc'],6:['fegfgf','geffgf'],7:['fegfgff','geffgff']}}

def steps(w): return tuple(x for op in w for x in OPS[op])
def key(st): return tuple(st.count(i) for i in range(1,7))
def net(st): return tuple(st.count(i)-st.count(-i) for i in range(1,7))
def observer(st):
    result=[]
    for state,prev in START:
        for s in st:
            if prev==1 and s==2:
                if state=='N':state='A'
                elif state=='B':state='BA'
            elif prev==2 and s==1:
                if state=='N':state='B'
                elif state=='A':state='AB'
            prev=s
        result.append(BUCKET.index(state))
    return tuple(result)

def rank_q(sigs):
    rows=[[Fraction(int(sig[j]==v)) for j in range(9)] for sig in sigs for v in range(5)]
    rk=0
    for c in range(9):
        pos=next((i for i in range(rk,len(rows)) if rows[i][c]),None)
        if pos is None:continue
        rows[rk],rows[pos]=rows[pos],rows[rk]
        a=rows[rk][c]
        rows[rk]=[v/a for v in rows[rk]]
        for i in range(rk+1,len(rows)):
            if rows[i][c]:
                a=rows[i][c];rows[i]=[x-a*y for x,y in zip(rows[i],rows[rk])]
        rk+=1
    return rk

def zero_suffixes(n):
    # zero signed-X6 net => b absent and multiplicities of a/e identical
    for item in itertools.product('acdefg',repeat=n):
        if item.count('a')==item.count('e'):yield ''.join(item)

def reachable_keys(h):
    result=set()
    for k in range((h-2)//2+1):
        for p in range(1,h-2*k):
            for q in range(h-2*k-p):
                r=h-1-2*k-p-q
                if r<0:continue
                result.add((2*(k+1)+p+q,p+r,k+1,0,0,0))
    return result

def prefix_set(words):
    return {steps(w)[:j] for w in words for j in range(1,len(steps(w))+1)}

def run():
    six=[]
    for cid,src in CASES.items():
        by={2:B2,3:B3,**src}
        for h in range(2,8):
            assert len({key(steps(w)) for w in by[h]})==1
            assert rank_q({observer(steps(w)) for w in by[h]})==9
            assert all(net(steps(w))==(2,0,0,0,0,0) for w in by[h])
        sigs={observer(steps(w)) for words in by.values() for w in words}
        assert len(sigs)==6
        if not six:six=sorted(sigs)
        assert sigs==set(six)
    base_obs={r:observer(steps(r)) for r in B2}
    assert len(set(base_obs.values()))==4
    assert rank_q(base_obs.values())==9
    assert {rank_q(combo) for combo in itertools.combinations(base_obs.values(),3)}=={7}
    # After H2 there is no N; A->AB, B->BA are the only changes.
    monotone={1:{1,3},2:{2,4},3:{3},4:{4}}
    for r,sig in base_obs.items():
        compatible=[t for t in six if all(v in monotone[u] for u,v in zip(sig,t))]
        assert compatible==[sig],(r,compatible)
    overlap={}
    for cid,src in CASES.items():
        by={2:B2,3:B3,**src}
        bp=prefix_set([w for words in by.values() for w in words])
        assert len(bp)==72
        overlap[cid]={r:max(len(p)-len(steps(r)) for p in bp
                             if p[:len(steps(r))]==steps(r)) for r in B2}
        assert overlap[cid] == ({r:4 if r in ('de','ed') else 0 for r in B2}
                                if cid in (1512,1513) else {r:0 for r in B2})
    horizons=[]
    for h,expected_z in ((8,13236),(9,73392)):
        groups=defaultdict(lambda:defaultdict(set))
        retained=0; total_suf=0
        for suffix in zero_suffixes(h-2):
            total_suf+=1
            for root in B2:
                w=root+suffix
                st=steps(w)
                assert net(st)==(2,0,0,0,0,0)
                sig=observer(st)
                if sig in six:
                    assert sig==base_obs[root]
                    groups[key(st)][root].add(sig)
                    retained+=1
        assert total_suf==expected_z
        expected=reachable_keys(h)
        assert set(groups)==expected
        assert all(set(roots)==set(B2) for roots in groups.values())
        assert all(rank_q([next(iter(roots[r])) for r in B2])==9
                   for roots in groups.values())
        assert len(groups)==(50 if h==8 else 70)
        analytic=sum(math.comb(h-2*k,2) for k in range((h-2)//2+1))
        assert analytic==len(groups)
        horizons.append({'h':h,'suffix_length':h-2,'zero_net_suffixes':total_suf,
            'eligible_h2_rooted_words_counted_with_root':retained,
            'reachable_full_key_count':len(groups),
            'analytic_key_count':analytic,
            'distinct_allowed_signatures_per_key':4,
            'exact_Q_rank_of_four_signatures':9})
    exclusion={str(cid):{'max_old_extra_per_root':overlap[cid],
        'lower_bound_H8_new_edges_if_all_H8_words_H2_rooted':4*12-sum(overlap[cid].values()),
        'resulting_total_edge_lower_bound':72+4*12-sum(overlap[cid].values())}
        for cid in CASES}
    return {'result':'PASS','unit':'EC49FAQ H2 root observer rigidity',
        'scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
        'parent':'EC49FAP@be53f6d8f2fd26c1920ac50adec16817615e6d1b',
        'allowed_observer_signature_count':len(six),
        'base_H2_root_signatures':{r:list(base_obs[r]) for r in B2},
        'rational_ranks_of_H2_root_signature_subsets':{str(n):sorted({rank_q(x) for x in itertools.combinations(base_obs.values(),n)}) for n in range(1,5)},
        'all_horizon_key_count_formula':'sum_{k=0..floor((h-2)/2)} binom(h-2*k,2)',
        'all_horizon_key_feasibility_condition':'full legal key and x+y>=h+2',
        'horizons':horizons,'scoped_H2_only_H8_cost_exclusion':exclusion,
        'scope':'All-h analytic key/observer theorem; complete h8/h9 finite check; H2-only H8 lower bound for four fixed H2..H7 schedules. Mixed H2..H6 search open.'}
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2,sort_keys=True))
