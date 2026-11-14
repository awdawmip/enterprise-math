#!/usr/bin/env python3
"""EC49FGB: exact BRC signed-X6 witness, rational observer and 64-mode census.
Uses only the standard library. Scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
"""
from collections import Counter, defaultdict
from itertools import product
from fractions import Fraction
import json

OPS = 'acdefg'
T = ((1,2,3,1,4,5),(1,6,7,1,1,1),(2,2,8,2,2,2),
     (3,8,3,3,3,3),(4,2,7,4,4,4),(5,6,3,5,5,5),
     (6,6,8,6,6,6),(7,8,7,7,7,7),(8,8,8,8,8,8))
SIG = (0,0,4,1,16,32,8,2,0)
STEPS = {'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
         'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
BUCKET = {
  1:(2,3,2,3,3,2,4,3,4),2:(2,2,2,3,3,2,2,3,4),
  4:(1,1,4,1,3,4,4,3,4),8:(1,1,1,1,1,4,4,3,4),
  16:(0,0,2,1,3,2,2,3,4),32:(0,1,0,1,1,2,4,3,4)}
W = {
  (2,1):'de',(2,2):'ed',(2,4):'ce',(2,8):'ec',
  (3,16):'feg',(3,32):'gef',
  (4,16):'fegf',(4,32):'geff',
  (5,16):'fegfg',(5,32):'geffg',
  (6,1):'geffgd',(6,2):'fegfgd',(6,4):'fegfgc',(6,8):'geffgc',
  (7,16):'fegfgfg',(7,32):'geffgfg',
  (8,1):'geffgfgd',(8,2):'fegfgfgd',(8,4):'fegfgfgc',(8,8):'geffgfgc',
  (9,16):'fegfgfgfg',(9,32):'geffgfgfg'}

def observe(w):
    state = 0
    for op in w: state = T[state][OPS.index(op)]
    return SIG[state]

def steps(w):
    return tuple(s for op in w for s in STEPS[op])

def key(w):
    s = steps(w)
    return tuple(s.count(i) for i in range(1,7))

def rank_Q(outputs):
    sigs = sorted(set(outputs))
    A = [[Fraction(BUCKET[s][i] == b) for s in sigs for b in range(5)] for i in range(9)]
    k = 0
    for j in range(len(A[0])):
        pivot = next((i for i in range(k,9) if A[i][j]),None)
        if pivot is None: continue
        A[k],A[pivot] = A[pivot],A[k]
        v = A[k][j]
        for c in range(j,len(A[0])): A[k][c] /= v
        for i in range(k+1,9):
            f = A[i][j]
            if f:
                for c in range(j,len(A[0])): A[i][c] -= f*A[k][c]
        k += 1
        if k == 9: break
    return k

def witness():
    expected = {2:{1,2,4,8},3:{16,32},4:{16,32},5:{16,32},
                6:{1,2,4,8},7:{16,32},8:{1,2,4,8},9:{16,32}}
    prefix=set();keys=set();progress=[]
    for h in range(2,10):
        got=set();perkey=set()
        for (depth,output),w in sorted(W.items()):
            if depth!=h: continue
            assert len(w)==h and observe(w)==output, (h,output,w)
            assert Counter(w)['e']==Counter(w)['a']+1
            st=steps(w)
            assert tuple(st.count(i)-st.count(-i) for i in range(1,7))==(2,0,0,0,0,0)
            K=key(w); assert K[3:]==(0,0,0) and min(K[:3])>0
            keys.add(K); perkey.add(K);got.add(output)
            prefix.update(st[:i] for i in range(1,len(st)+1))
        assert got==expected[h] and rank_Q(got)==9 and len(perkey)==1
        progress.append(len(prefix))
    assert len(keys)==5 and progress==[28,42,46,50,66,72,88,94]
    return {'distinct_full_keys':sorted(keys),'prefix_progress':progress,
            'native_prefixes':len(prefix),'word_count':len(W),'rational_rank_each_horizon':9}

def allowed(h,mode):
    """Enumerate every legal word in the e=1,a=0,r∈{0,1} family."""
    r = int(mode=='L')
    target = {16,32} if mode=='H' else {1,2,4,8}
    out={}
    for f in range(h-r):
        g=h-1-r-f
        K=(2+r+f,r+g,1)
        found=set()
        for c in range(r+1):
            left={'c':c,'d':r-c,'e':1,'f':f,'g':g}
            def rec(depth,state):
                if depth==h:
                    found.add(SIG[state]);return
                for ch in 'cdefg':
                    if left[ch]:
                        q=T[state][OPS.index(ch)]
                        if q==8: continue
                        left[ch]-=1;rec(depth+1,q);left[ch]+=1
            rec(0,0)
        if target<=found: out[K]=True
    return set(out)

def modes():
    feasible={(h,m):allowed(h,m) for h in range(4,10) for m in 'HL'}
    result=[]
    for profile in map(''.join,product('HL',repeat=6)):
        horizons=range(4,10)
        allkeys=sorted(set().union(*(feasible[h,m] for h,m in zip(horizons,profile))))
        dp={0:(0,[])}
        for k in allkeys:
            covers=sum(1<<idx for idx,(h,m) in enumerate(zip(horizons,profile)) if k in feasible[h,m])
            for mask,(size,prior) in list(dp.items()):
                newmask=mask|covers
                if newmask not in dp or size+1<dp[newmask][0]:
                    dp[newmask]=(size+1,prior+[k])
        assert 63 in dp,profile
        count=1+dp[63][0]
        result.append({'profile':profile,'min_full_keys_including_H2_H3':count,
                       'one_key_cover_H4_H9':dp[63][1]})
    from collections import Counter as C
    histogram={str(x):count for x,count in sorted(C(z['min_full_keys_including_H2_H3'] for z in result).items())}
    assert histogram=={'4':1,'5':21,'6':35,'7':7},histogram
    assert [z['profile'] for z in result if z['min_full_keys_including_H2_H3']==4]==['LHLHLH']
    assert sum(z['min_full_keys_including_H2_H3']<=5 for z in result)==22
    return {'histogram':histogram,'five_key_feasible':22,'total_profiles':64,'rows':result}

def main():
    report={'schema':'EC49FGB_AUTHOR_FINITE_AUDIT_V1',
            'frozen_scientific_pin':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
            'witness':witness(),'mode_census':modes(),'audit':'PASS'}
    with open('EXACT_REPORT_EC49FGB.json','w',encoding='utf-8') as f:
        json.dump(report,f,indent=2,ensure_ascii=False);f.write('\n')
    print('PASS',report['witness']['native_prefixes'],report['mode_census']['histogram'])

if __name__=='__main__':main()
