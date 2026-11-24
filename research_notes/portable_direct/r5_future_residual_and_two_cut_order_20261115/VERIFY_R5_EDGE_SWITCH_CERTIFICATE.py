#!/usr/bin/env python3
"""Linear-time edge-level direct Boolean-diamond criterion for trimmed DAGs.
Imports adjacent exact frozen solver and five-type signature verifier.
"""
import json
from collections import defaultdict
from VERIFY_R5_JOINT_CLOSURE_OFFLINE import frozen, close, optimizer, language, E
from VERIFY_R5_FIVE_TYPE_CARRIER import signatures

def edges(L):
    V,A,_=L;K=len(V)
    e={(-1,-1,v) for v in V[0]}
    for r,row in enumerate(A):e.update((r,u,v) for u,vs in row.items() for v in vs)
    e.update((K-1,v,-2) for v in V[-1])
    return e

def trim_intersection(A,B,K):
    e=A&B;next=defaultdict(list);prev=defaultdict(list)
    for r,u,v in e:
        next[r,u].append((r+1,v));prev[r+1,v].append((r,u))
    start={(-1,-1)};queue=[(-1,-1)]
    for u in queue:
        for v in next[u]:
            if v not in start:start.add(v);queue.append(v)
    finish={(K,-2)};queue=[(K,-2)]
    for v in queue:
        for u in prev[v]:
            if u not in finish:finish.add(u);queue.append(u)
    return {t for t in e if (t[0],t[1]) in start and (t[0]+1,t[2]) in finish}

def switching_path(Z,A,B,K):
    nxt=defaultdict(list)
    for e in Z:nxt[e[0],e[1]].append(e)
    states={(-1,-1,0)}
    for r in range(-1,K):
        states={(r+1,e[2],flags | (1 if e in A and e not in B else 0)
                                   | (2 if e in B and e not in A else 0))
                for rr,u,flags in states for e in nxt[rr,u]}
    return (K,-2,3) in states

def certificate(old,a,b,joint):
    K=len(old[0]);O,A,B,Z=map(edges,(old,a,b,joint))
    assert O<=A&B and A<=Z and B<=Z
    excess=trim_intersection(A,B,K)-O
    neutral=Z-(A|B)
    switched=switching_path(Z,A,B,K)
    return {'P_zero':not excess,'Q_zero':not neutral and not switched,
            'intersection_excess_edges':len(excess),'joint_neutral_edges':len(neutral),
            'joint_a_exclusive':len((A-B)&Z),'joint_b_exclusive':len((B-A)&Z),
            'switch_path':switched,'joint_edges':len(Z)}

def switch_only_counterexample():
    old={(2,4,8)};a=old|{(0,3,6)};b=old|{(1,3,7)}
    joint=a|b|{(0,3,7),(1,3,6)}
    graphs=[]
    for F in (old,a,b,joint):
        V=[{S[r] for S in F} for r in range(3)]
        A=[{u:tuple(sorted({S[r+1] for S in F if S[r]==u})) for u in V[r]}
           for r in range(2)]
        graphs.append((V,A,0))
    c=certificate(*graphs);s=signatures(*graphs)
    assert c['P_zero'] and not c['Q_zero'] and not c['joint_neutral_edges']
    assert c['switch_path'] and s[0]==2 and s[6]==0
    return {'families':{'old':sorted(old),'a':sorted(a),'b':sorted(b),'joint':sorted(joint)},
            'certificate':c,'signatures':s,'scope':'synthetic DAG, not geometric claim'}

def run():
    abstract=switch_only_counterexample();x,cuts=frozen();dp={}
    for m in range(32):
        mask=sum(1<<e for j,e in enumerate(E) if (m>>j)&1)
        dp[m]=optimizer(close(x,cuts,mask))
    rows=[]
    for K in range(214,222):
        L={m:language(dp[m],K) for m in range(32)}
        for m in range(32):
            if m&6:continue
            c=certificate(L[m],L[m|2],L[m|4],L[m|6])
            sig=signatures(L[m],L[m|2],L[m|4],L[m|6])
            assert c['P_zero']==(sig[6]==0) and c['Q_zero']==(sig[0]==0)
            assert c['P_zero'] and c['Q_zero']
            rows.append({'K':K,'old_effective_mask':m,**c})
    assert len(rows)==64
    print(json.dumps({'status':'PASS_EXACT_R5_EDGE_SWITCH_CERTIFICATE',
       'scientific_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
       'abstract_switch_only_case':abstract,'frozen_cases':len(rows),
       'both_exclusive_colors_present':sum(r['joint_a_exclusive']>0 and r['joint_b_exclusive']>0 for r in rows),
       'max_joint_edges':max(r['joint_edges'] for r in rows),
       'rows':rows,'independent_review':'NOT_REVIEWED'},indent=2,sort_keys=True))

if __name__=='__main__':run()
