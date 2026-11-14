#!/usr/bin/env python3
"""Exact R5 radius-two optimizer requirement filters and zeta counts.
Frozen science: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived one-dimensional event-index observer only. Python standard library.
"""
import json
from collections import Counter
from fractions import Fraction
from itertools import product

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF=10**18

def frozen():
    pools={3:set(),12:set(),15:set()}; n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t; i=bit.bit_length()-1; mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i];k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,values in pools.items() for p in values)
    x=[0]
    for v in sorted(events): x.append(x[-1]+events[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert (len(x),x[-1],len(cuts))==(954,1065,28)
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for i in range(len(cuts)) if mask>>i&1}
    out=[];shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in active:shift+=1
    return out

def spectrum(x,K):
    n=len(x);incoming=[[] for _ in range(n)];suffix=[INF]*n
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>7:break
            ds=[min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)]
            if all(v<=2 for v in ds): incoming[j].append((i,sum(ds)))
        if x[-1]-x[j]<=2:suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    cost=[INF]*n;ways=[0]*n;out={}
    for j in range(n):
        if x[j]-x[0]<=2:
            cost[j]=sum(x[j]-x[t] for t in range(j));ways[j]=1
    for k in range(1,K+1):
        if k>1:
            nxt=[INF]*n;cnt=[0]*n
            for j in range(n):
                for i,w in incoming[j]:
                    if not ways[i]:continue
                    val=cost[i]+w
                    if val<nxt[j]:nxt[j]=val;cnt[j]=ways[i]
                    elif val==nxt[j]:cnt[j]+=ways[i]
            cost,ways=nxt,cnt
        best=INF;count=0
        for j in range(n):
            if not ways[j] or suffix[j]==INF:continue
            val=cost[j]+suffix[j]
            if val<best:best=val;count=ways[j]
            elif val==best:count+=ways[j]
        if count:out[k]=(best,count)
    return out

def score(z,s):
    cs=[z[j] for j in range(len(z)) if s>>j&1]
    if not cs:return None
    ds=[min(abs(v-u) for u in cs) for v in z]
    return sum(ds) if max(ds)<=2 else None

def exhaustive_small():
    # Verify unique prerequisite masks, cost invariance and max-min reduction.
    words=filters=cost_checks=minimax_checks=0
    for n in range(2,9):
        for steps in product((1,2,3),repeat=n-1):
            cuts=[i for i,d in enumerate(steps) if d==3]
            if any(b==a+1 for a,b in zip(cuts,cuts[1:])):continue
            words+=1;m=len(cuts);full=(1<<m)-1
            xs=[]
            for B in range(1<<m):
                z=[0]
                for i,d in enumerate(steps):
                    z.append(z[-1]+d-int(i in {cuts[t] for t in range(m) if B>>t&1}))
                xs.append(z)
            optimum={};optcost={};req={}
            for s in range(1,1<<n):
                values=[score(z,s) for z in xs]
                if values[full] is None:
                    assert all(v is None for v in values)
                    continue
                mask=sum(1<<i for i in range(m) if values[full^(1<<i)] is None)
                req[s]=mask
                for B,v in enumerate(values):
                    assert (v is not None)==(mask&B==mask)
                    if v is None:continue
                    assert v==values[full]
                    cost_checks+=1;key=(B,s.bit_count())
                    if key not in optcost or v<optcost[key]:
                        optcost[key]=v;optimum[key]={s}
                    elif v==optcost[key]:optimum[key].add(s)
            for k in range(1,n+1):
                if not all((B,k) in optcost and optcost[(B,k)]==optcost[(full,k)] for B in range(1<<m)):
                    continue
                allopt=optimum[(full,k)];filters+=1
                for B in range(1<<m):
                    assert optimum[(B,k)]=={s for s in allopt if req[s]&B==req[s]}
                for i in range(m):
                    direct=0
                    for B in range(1<<m):
                        if B>>i&1:continue
                        for s in optimum[(B|(1<<i),k)]:
                            direct=max(direct,min(k-(s&t).bit_count() for t in optimum[(B,k)]))
                    reduced=max((min(k-(s&t).bit_count() for t in optimum[(req[s]&~(1<<i),k)])
                                 for s in allopt if req[s]>>i&1),default=0)
                    assert direct==reduced;minimax_checks+=1
    return dict(words=words,constant_cost_budget_cases=filters,feasible_set_cost_checks=cost_checks,
                max_min_recourse_checks=minimax_checks)

def main():
    x,cuts=frozen()
    assert min(b-a for a,b in zip(cuts,cuts[1:]))==5
    masks={'none':0,'15':1<<15,'17':1<<17,'both':(1<<15)|(1<<17),'all':(1<<28)-1}
    spectra={key:spectrum(close(x,cuts,B),315) for key,B in masks.items()}
    rows=[]
    for k in range(292,316):
        values={key:spectra[key][k] for key in masks}
        assert len({v[0] for v in values.values()})==1
        assert values['both'][1]==values['all'][1]
        N0=values['none'][1];N15=values['15'][1];N17=values['17'][1];Nboth=values['both'][1]
        coeffs=[N0,N15-N0,N17-N0,Nboth-N15-N17+N0]
        assert min(coeffs)>=0
        rows.append({'K':k,'J':values['none'][0],
                     'a_empty':str(coeffs[0]),'a_15':str(coeffs[1]),
                     'a_17':str(coeffs[2]),'a_15_17':str(coeffs[3]),
                     'N_both_equals_N_all':True})
    assert rows[1]['a_15']==rows[1]['a_17']=='495879658013739785241231360'
    assert rows[1]['a_15_17']=='0'
    assert all(int(row['a_15_17'])>0 for row in rows if 294<=row['K']<=313)
    assert all(int(row['a_15'])==int(row['a_17'])==int(row['a_15_17'])==0
               for row in rows if row['K'] in (292,315))
    print(json.dumps({'status':'PASS_EXACT_R5_REQUIREMENT_ZETA',
        'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'model':'derived radius-2 integer-index-center observer',
        'frozen_events':954,'frozen_cuts':28,'cut_index_min_separation':5,
        'budget_range_computed':[292,315], 'coefficients':rows,
        'small_exhaustive':exhaustive_small(),'independent_review':'NOT_REVIEWED'},
        ensure_ascii=False,sort_keys=True,indent=2))
if __name__=='__main__':main()
