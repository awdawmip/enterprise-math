#!/usr/bin/env python3
"""Five exact optimizer-language membership types, not scalar cancellation.
Run from the folder containing VERIFY_R5_JOINT_CLOSURE_OFFLINE.py in a checkout.
Python stdlib only. Frozen science pin is unchanged.
"""
import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from VERIFY_R5_JOINT_CLOSURE_OFFLINE import frozen, close, optimizer, language, E

# Bit 0: old; bit 1: cut 8/a; bit 2: cut 9/b. Joint membership implicit.
TYPES={0:'Q_joint_only',2:'a_only',4:'b_only',6:'P_intersection_surplus',7:'old'}

def signatures(old,a,b,joint):
    F=(old,a,b)
    assert len({x[2] for x in (old,a,b,joint)})==1
    D=defaultdict(int)
    for v in joint[0][0]:
        t=sum((1<<i) for i,x in enumerate(F) if v in x[0][0]);D[v,t]+=1
    for r,arcs in enumerate(joint[1]):
        N=defaultdict(int)
        for (v,t),cnt in D.items():
            for w in arcs[v]:
                u=t
                for i,x in enumerate(F):
                    if w not in x[0][r+1] or w not in x[1][r].get(v,()):u &= ~(1<<i)
                N[w,u]+=cnt
        D=N
    out=defaultdict(int)
    for (v,t),cnt in D.items():out[t]+=cnt
    assert set(out)<=set(TYPES),out
    assert out.get(7,0)>0
    return {k:out.get(k,0) for k in sorted(TYPES)}

def small_cases():
    samples=[([3,3,2],0,1,3),([3,2,3,2],0,2,3),
             ([3,2,3,3,2],0,2,4),([3,3,2,1,2,1,2],0,1,4)]
    result=[]
    for gaps,a,b,K in samples:
        Fs=[]; J=[]
        for mask in range(4):
            z=[0];d=list(gaps)
            if mask&1:d[a]-=1
            if mask&2:d[b]-=1
            for x in d:z.append(z[-1]+x)
            best=None;f=set()
            for S in combinations(range(len(z)),K):
                dist=[min(abs(z[t]-z[i]) for i in S) for t in range(len(z))]
                if max(dist)>2:continue
                c=sum(dist)
                if best is None or c<best:best=c;f={S}
                elif best==c:f.add(S)
            Fs.append(f);J.append(best)
        assert len(set(J))==1 and J[0] is not None
        typ=defaultdict(int)
        for S in Fs[3]:
            tag=sum(1<<i for i in range(3) if S in Fs[i]);typ[tag]+=1
        assert set(typ)<=set(TYPES)
        result.append({'gaps':gaps,'cuts':[a,b],'K':K,
                       'cost':J[0],'counts':{str(i):typ[i] for i in sorted(TYPES)}})
    assert [x['counts']['6'] for x in result]==[1,0,0,2]
    assert [x['counts']['0'] for x in result]==[0,1,2,2]
    return result

def run():
    x,cuts=frozen()
    dp={}
    for m in range(32):
        bitset=sum(1<<e for j,e in enumerate(E) if (m>>j)&1)
        dp[m]=optimizer(close(x,cuts,bitset))
    rows=[]
    for K in range(214,222):
        L={m:language(dp[m],K) for m in range(32)}
        for m in range(32):
            if m&6:continue
            typ=signatures(L[m],L[m|2],L[m|4],L[m|6])
            assert typ[0]==typ[6]==0,(K,m,typ)
            rows.append({'K':K,'old_effective_mask':m,
                         'old':str(typ[7]),'a_only':str(typ[2]),'b_only':str(typ[4]),
                         'P':str(typ[6]),'Q':str(typ[0])})
    assert len(rows)==64
    result={'status':'PASS_EXACT_R5_FIVE_TYPE_CARRIER',
            'scope':'954-event frozen radius-2 indexed-center derived 1D observer',
            'scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'five_membership_type_bits':TYPES,
            'small_cases':small_cases(),'all_64_P_Q_zero':True,
            'frozen_cases':64,'results':rows,
            'independent_review':'NOT_REVIEWED'}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':run()
