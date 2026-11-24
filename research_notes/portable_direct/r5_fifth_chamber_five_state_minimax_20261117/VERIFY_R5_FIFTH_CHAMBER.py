#!/usr/bin/env python3
"""Exact finite certificate for R5 fifth noise chamber; standard library only.
Usage: python VERIFY_R5_FIFTH_CHAMBER.py EXACT_R5_ALL_101_BUDGETS.json
"""
import hashlib, json, sys
from functools import lru_cache
from pathlib import Path
PIN='435e77af0d180eac32bd1f9c4c464bc4010b7551'
INPUT_SHA='50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b'
L=25845652773852463277015040000
U=58182461585441404127941754880
Q=(216,223,296)
STAR=(18,24,82,34)
FIVE=(18,24,82,34,17)
EXPECTED=(735,1685,2635,3585,4535,5485,6435,7385,8335,9285,10235)

def solve_restriction(table, masks, faults):
    n=len(masks); cap=faults+1
    actions={}
    for k in range(214,315):
        row=table[k]
        values=sorted((row[h],i) for i,h in enumerate(masks))
        all_windows=set()
        for v,_ in values:
            all_windows.add(sum(1<<i for w,i in values if v<=w<=v+L))
        maximal=tuple(sorted(m for m in all_windows if not any(m!=b and m&b==m for b in all_windows)))
        actions.setdefault(maximal,k)
    queries=tuple(sorted((k,masks_of_answers) for masks_of_answers,k in actions.items()))
    @lru_cache(None)
    def bellman(err):
        if sum(v<cap for v in err)<=1: return 0
        best=10**10
        for k,answers in queries:
            future=0
            possible=True
            for mask in answers:
                nxt=tuple(min(cap,err[i]+int(not (mask>>i&1))) for i in range(n))
                if nxt==err:
                    possible=False
                    break
                if sum(v<cap for v in nxt)>1:
                    future=max(future,bellman(nxt))
                if k+future>=best:
                    possible=False
                    break
            if possible: best=min(best,k+future)
        if best==10**10: raise ArithmeticError(('undecodable',err))
        return best
    result=bellman((0,)*n)
    return result,bellman.cache_info().currsize,len(queries)

def verify(input_file):
    b=Path(input_file).read_bytes()
    assert hashlib.sha256(b).hexdigest()==INPUT_SHA
    source=json.loads(b)
    table={int(k):tuple(map(int,row['counts'])) for k,row in source['counts_and_cohorts'].items()}
    assert set(table)==set(range(214,315)) and all(len(v)==256 for v in table.values())
    first={}
    for h in range(256):
        for j in range(h+1,256):
            x=next((k for k in range(214,315) if abs(table[k][h]-table[k][j])>L),None)
            assert x is not None
            first[x]=first.get(x,0)+1
    assert first=={214:31104,215:640,223:512,294:64,295:256,296:64}
    strong=[]; max_zero_diameter=0
    for h in STAR[1:]:
        strong.append(set(k for k in range(214,315) if abs(table[k][h]-table[k][STAR[0]])>L))
    assert [min(s) for s in strong]==[215,223,296]
    assert not (strong[0]&strong[1] or strong[1]&strong[2] or strong[0]&strong[2])
    for k in range(214,315):
        targets=[j+1 for j,s in enumerate(strong) if k in s]
        vals=[table[k][h] for j,h in enumerate(STAR) if j not in targets]
        max_zero_diameter=max(max_zero_diameter,max(vals)-min(vals))
    assert max_zero_diameter<=L
    fibers=[list(range(256))]; conditional={}
    for k in reversed(Q):
        gaps=[]; nxt=[]
        for fiber in fibers:
            values=sorted(set(table[k][h] for h in fiber))
            gaps.extend(y-x for x,y in zip(values,values[1:]))
            nxt.extend([[h for h in fiber if table[k][h]==v] for v in values])
        conditional[k]=min(gaps) if gaps else None
        assert conditional[k] is None or conditional[k]>=U
        fibers=nxt
    assert len(fibers)==256 and all(len(f)==1 for f in fibers)
    report=[]
    for f,expected in enumerate(EXPECTED):
        val,states,actions=solve_restriction(table,FIVE,f)
        assert val==expected==735+950*f,(f,val,expected)
        report.append({'f':f,'exact_five_state_minimax':val,'visited_Bellman_states':states,'distinct_query_response_families':actions,'full_256_upper':735+951*f})
    result={'schema':'R5_FIFTH_CHAMBER_FIVE_STATE_FINITE_CERT_V1',
      'source_pin':PIN,'input_sha256':INPUT_SHA,'tau_interval':[str(L),str(U)],
      'state_count':256,'budgets':101,'pair_count':32640,
      'earliest_strong_budget_histogram':{str(k):v for k,v in sorted(first.items())},
      'star_masks':list(STAR),'star_support_minima':[215,223,296],
      'star_zero_group_max_diameter':str(max_zero_diameter),
      'universal_f_lower':'734+949*f','universal_f_upper':'735+951*f',
      'five_state_masks':list(FIVE),'finite_lower':report,
      'descending_conditional_min_gaps':{str(k):str(v) for k,v in conditional.items()},
      'conclusion':'for 0<=f<=10: 735+950*f <= C_f <= 735+951*f',
      'status':'PASS_R5_FIFTH_CHAMBER_FIVE_STATE_MINIMAX_F0_TO_F10'}
    return result

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit(__doc__)
    x=verify(sys.argv[1]);
    (Path(__file__).parent/'RESULTS_R5_FIFTH_CHAMBER.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
    print(x['status'])
    print([(z['f'],z['exact_five_state_minimax']) for z in x['finite_lower']])
