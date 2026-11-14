#!/usr/bin/env python3
"""Exact index-set recourse on frozen R5 and exhaustive small-gap tests."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json, sys

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'brc_r5_universal_cut_15_17_20261114'))
from VERIFY_R5_UNIVERSAL_CUT_15_17 import frozen, close, score, shortest_center_paths
INF=(10**12,10**12)


def optimum_sets(x):
    n=len(x); out={}
    for m in range(1,1<<n):
        s=tuple(j for j in range(n) if m>>j&1)
        r,c=score(x,s)
        if r>2:continue
        k=len(s)
        if k not in out or c<out[k][0]:out[k]=(c,[s])
        elif c==out[k][0]:out[k][1].append(s)
    return out


def recourse_dp(x,k,reference):
    """Lexicographic minimum: (old objective, changed centers)."""
    n=len(x); chosen=set(reference)
    assert len(chosen)==k
    prev=[INF]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            prev[j]=(sum(x[j]-x[t] for t in range(j)),int(j not in chosen))
    for count in range(2,k+1):
        cur=[INF]*n
        for j in range(n):
            for i in range(j-1,-1,-1):
                if x[j]-x[i]>7:break
                if prev[i]==INF:continue
                ds=[min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)]
                if any(d>2 for d in ds):continue
                trial=(prev[i][0]+sum(ds),prev[i][1]+int(j not in chosen))
                if trial<cur[j]:cur[j]=trial
        prev=cur
    return min(((prev[j][0]+sum(x[t]-x[j] for t in range(j+1,n)),prev[j][1])
                for j in range(n) if prev[j]!=INF and x[-1]-x[j]<=2),default=INF)


def exhaustive():
    summary={}; first={}
    for n in range(2,8):
        runs=0; checked=0; maxdistance=0
        for steps in product((1,2,3),repeat=n-1):
            cuts=[j for j,d in enumerate(steps) if d==3]
            if not cuts:continue
            x=[0]
            for d in steps:x.append(x[-1]+d)
            old=optimum_sets(x)
            for i in cuts:
                runs+=1
                y=[v-(j>i) for j,v in enumerate(x)]
                new=optimum_sets(y)
                for k,(cost,oldsets) in old.items():
                    if k not in new or new[k][0]!=cost:continue
                    for s in new[k][1]:
                        checked+=1
                        distance=min(k-len(set(s)&set(t)) for t in oldsets)
                        assert recourse_dp(x,k,s)==(cost,distance)
                        maxdistance=max(maxdistance,distance)
                        if distance in (2,3) and str(distance) not in first:
                            first[str(distance)]={'x':x,'y':y,'cut':i,'k':k,
                                'cost':cost,'old_optima':[list(t) for t in oldsets],
                                'new_optimum':list(s),'replacements':distance}
        summary[str(n)]={'transitions':runs,'new_optimum_checks':checked,'max_replacements':maxdistance}
    assert sum(row['transitions'] for row in summary.values())==2005
    assert [summary[str(n)]['max_replacements'] for n in range(2,8)]==[0,1,2,2,2,3]
    return summary,first


def r5():
    x,cuts=frozen()
    assert len(x)==954 and len(cuts)==28
    out={}
    for i in (15,17):
        j=cuts[i]; y=close(x,cuts,1<<i)
        c,ws=shortest_center_paths(y,293,forced=j+1,
                forbidden={j-2,j-1,j},recover=(293,))
        s=tuple(ws[293]); assert c[293]==741
        assert score(y,s)==(2,741) and score(x,s)[0]>2
        cost,replacements=recourse_dp(x,293,s)
        assert (cost,replacements)==(741,1)
        out[str(i)]={'boundary':j,'budget':293,'cost':cost,'minimum_replacements':replacements}
    return out


def main():
    table,witnesses=exhaustive()
    print(json.dumps({'status':'PASS_EXACT_RECONFIGURATION_LEX_DP',
     'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
     'all_small_transitions':2005,'by_n':table,'minimal_witnesses':witnesses,
     'frozen_r5_k293':r5(),'review':'NOT_REVIEWED'},indent=2,sort_keys=True))

if __name__=='__main__':main()
