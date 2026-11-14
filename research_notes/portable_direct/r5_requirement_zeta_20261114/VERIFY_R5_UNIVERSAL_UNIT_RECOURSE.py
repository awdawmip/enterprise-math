#!/usr/bin/env python3
"""R5: exact universal one-swap recourse for closure bits 15 and 17, K=293..314.
Requires the original pinned VERIFY_R5_REQUIREMENT_ZETA.py beside this file.
Only the frozen derived radius-two integer-index-center observer is studied.
"""
import json
from collections import Counter
from VERIFY_R5_REQUIREMENT_ZETA import frozen,close,INF


def graph(z):
    n=len(z); inc=[[] for _ in z]; out=[[] for _ in z]
    pref=[INF]*n;tail=[INF]*n
    for j in range(n):
        if z[j]-z[0]<=2:pref[j]=sum(z[j]-z[t] for t in range(j))
        if z[-1]-z[j]<=2:tail[j]=sum(z[t]-z[j] for t in range(j+1,n))
        for i in range(j-1,-1,-1):
            if z[j]-z[i]>7:break
            mid=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
            if max(mid,default=0)<=2:
                w=sum(mid);inc[j].append((i,w));out[i].append((j,w))
    return inc,out,pref,tail


def paths_dp(z,max_k=314):
    inc,out,pref,tail=graph(z);n=len(z)
    C=[pref]
    for m in range(1,max_k):
        prior=C[-1];C.append([min((prior[i]+w for i,w in inc[j]),default=INF) for j in range(n)])
    D=[tail]
    for m in range(1,max_k):
        prior=D[-1];D.append([min((w+prior[q] for q,w in out[j]),default=INF) for j in range(n)])
    J=[min(C[k-1][j]+tail[j] for j in range(n)) for k in range(1,max_k+1)]
    return out,C,D,J


def patterns(dp,k,i,rad=9):
    out,C,D,J=dp;l=i-rad;r=i+rad;best=J[k-1]
    seen=set();pats=set();nodes=set()
    def walk(t,j,P):
        nodes.add((t,j))
        if t>=k:return
        for q,w in out[j]:
            if C[t][q]!=C[t-1][j]+w or C[t][q]+D[k-t-1][q]!=best:continue
            if q>r:pats.add(P)
            else:walk(t+1,q,P+(q,))
    for t in range(1,k):
        for j in range(max(0,l-7),l):
            if C[t-1][j]+D[k-t][j]==best:
                seen.add((t,j));walk(t,j,())
    assert pats and seen
    return pats,len(seen),len(nodes)


def repair(P,new,old,i):
    chosen=set(P);events=range(i-6,i+8)
    def cost(z,S):
        ds=[min((abs(z[t]-z[j]) for j in S),default=INF) for t in events]
        return max(ds),sum(ds)
    original=cost(new,chosen)
    assert original[0]<=2
    if cost(old,chosen)==original:return 0,None
    for p in chosen:
        if not i-4<=p<=i+5:continue
        for q in range(i-4,i+6):
            if q in chosen:continue
            T=(chosen-{p})|{q}
            if cost(old,T)==original:return 1,(p,q)
    raise AssertionError(('NO_LOCAL_SINGLE_SWAP',i,tuple(P)))


def main():
    x,cuts=frozen();assert len(x)==954 and len(cuts)==28
    masks={'none':0,'15':1<<15,'17':1<<17,'both':(1<<15)|(1<<17)}
    z={name:close(x,cuts,mask) for name,mask in masks.items()}
    dp={name:paths_dp(z[name]) for name in ('15','17','both')}
    transitions=(('15','none',15),('17','none',17),('both','17',15),('both','15',17))
    rows=[];unique_patterns=0
    for k in range(293,315):
        row={'K':k,'transitions':{}}
        for newer,older,bit in transitions:
            i=cuts[bit];P,starts,nodes=patterns(dp[newer],k,i)
            status=Counter();repl=Counter()
            for p in P:
                num,swap=repair(p,z[newer],z[older],i)
                status[num]+=1
                if swap:repl[f'{swap[0]}->{swap[1]}']+=1
            assert status[1]>0
            key=f'{newer}_to_{older}'
            row['transitions'][key]={'patterns':len(P),'old_compatible':status[0],
                 'one_swap':status[1],'start_states':starts,'visited_states':nodes,
                 'swap_types':dict(sorted(repl.items()))}
            unique_patterns+=len(P)
        rows.append(row)
    checks={'budgets':len(rows),'transitions':len(rows)*len(transitions),
           'local_patterns':unique_patterns,'all_one_swap_or_already_old':True,
           'positive_strict_cases':len(rows)*len(transitions)}
    print(json.dumps({'status':'PASS_EXACT_R5_UNIT_RECOURSE_ALL_BACKGROUNDS',
        'input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'events':len(x),'cut_positions':{'15':cuts[15],'17':cuts[17]},
        'budgets':[293,314],'R_15':1,'R_17':1,
        'checks':checks,'rows':rows,'independent_review':'NOT_REVIEWED'},
        ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
