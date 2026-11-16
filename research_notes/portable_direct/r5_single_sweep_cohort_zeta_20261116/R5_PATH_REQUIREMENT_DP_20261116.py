#!/usr/bin/env python3
"""One all-closed shortest-path sweep with exact 8-bit requirement-mask cohorts.
Frozen input 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived radius-two 954-event indexed-center observer only; not native X6.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json, time

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
U=(3,8,9,10,15,17,25,27)
BUDGETS=(214,223,291,294)
INF=10**15

def frozen():
    pools={3:set(),12:set(),15:set()}; n=k=bits=0
    for t in range(1,1<<15):
        bit=t&-t;idx=bit.bit_length()-1;bits^=bit
        sg=1 if bits&bit else -1
        n+=sg*W[idx];k+=sg*K0[idx]
        if n>=3 and k%36==0 and k//36 in pools: pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    counter=Counter(Fraction(n,q) for q, ps in pools.items() for n in ps)
    x=[0]
    for v in sorted(counter): x.append(x[-1]+counter[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert (len(x), x[-1], len(cuts))==(954,1065,28)
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for j,i in enumerate(U) if mask>>j&1}
    out=[];shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in active: shift+=1
    return out

def kernel(x):
    n=len(x);pred=[{} for _ in x];suffix=[INF]*n;init=[INF]*n
    for j in range(n):
        if x[j]-x[0]<=2:init[j]=int(sum(x[j]-x[t] for t in range(j)))
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>7:break
            if all(min(x[t]-x[i],x[j]-x[t])<=2 for t in range(i+1,j)):
                pred[j][i]=int(sum(min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)))
        if x[-1]-x[j]<=2:suffix[j]=int(sum(x[t]-x[j] for t in range(j+1,n)))
    return pred,init,suffix

def parametric_kernel(x,cuts):
    base,init,suffix=kernel(x)
    full,fi,fs=kernel(close(x,cuts,255))
    assert init==fi and suffix==fs
    requirements={}
    for bit,u in enumerate(U):
        one,oi,os=kernel(close(x,cuts,1<<bit))
        assert (oi,os)==(init,suffix)
        additions=0
        for j in range(len(x)):
            for i,c in one[j].items():
                if i not in base[j]:
                    key=(i,j)
                    assert key not in requirements
                    requirements[key]=1<<bit
                    assert full[j][i]==c
                    additions+=1
                else:
                    assert base[j][i]==c
        assert additions==2
    assert sum(len(q) for q in base)==4383
    assert sum(len(q) for q in full)==4399
    for j in range(len(x)):
        assert set(full[j])==set(base[j])|{i for (i,h) in requirements if h==j}
    pred=[[(i,c,requirements.get((i,j),0)) for i,c in row.items()] for j,row in enumerate(full)]
    return pred,init,suffix,requirements

def zeta(cohorts):
    a=[cohorts.get(i,0) for i in range(256)]
    for j in range(8):
        for m in range(256):
            if m&(1<<j):a[m]+=a[m^(1<<j)]
    return a

def masked_cost_count(x,cuts,mask,ks):
    z=close(x,cuts,mask);p,init,suf=kernel(z)
    w=[int(c<INF) for c in init];d=init[:]; answers={}
    for k in range(1,max(ks)+1):
        if k>1:
            nw=[0]*len(z);nd=[INF]*len(z)
            for j,arcs in enumerate(p):
                for i,c in arcs.items():
                    if not w[i]:continue
                    v=d[i]+c
                    if v<nd[j]:nd[j]=v;nw[j]=w[i]
                    elif v==nd[j]:nw[j]+=w[i]
            w,d=nw,nd
        if k in ks:
            best=INF;count=0
            for j,s in enumerate(suf):
                if s==INF or not w[j]:continue
                t=d[j]+s
                if t<best:best=t;count=w[j]
                elif t==best:count+=w[j]
            answers[k]=(best,count)
    return answers

def main():
    t0=time.perf_counter();x,cuts=frozen();pred,init,suf,requirements=parametric_kernel(x,cuts)
    n=len(x);old_cost=init[:];old_poly=[({0:1} if d<INF else {}) for d in init]
    answers={};tight=0;arcs=0;mask_adds=0;max_entries=0
    for k in range(1,max(BUDGETS)+1):
        if k>1:
            new_cost=[INF]*n
            # First compute minima; avoid propagating path polynomials on losing arcs.
            for j,ps in enumerate(pred):
                best=INF
                for i,c,req in ps:
                    if old_cost[i]!=INF:
                        v=old_cost[i]+c
                        if v<best:best=v
                new_cost[j]=best
            new_poly=[{} for _ in range(n)]
            for j,ps in enumerate(pred):
                best=new_cost[j]
                if best==INF:continue
                target=new_poly[j]
                for i,c,req in ps:
                    arcs+=1
                    if old_cost[i]+c!=best:continue
                    tight+=1
                    for m,v in old_poly[i].items():
                        key=m|req
                        target[key]=target.get(key,0)+v
                        mask_adds+=1
            old_cost,old_poly=new_cost,new_poly
        if k in BUDGETS:
            best=INF;cohorts={}
            for j,s in enumerate(suf):
                if s==INF or old_cost[j]==INF:continue
                val=old_cost[j]+s
                if val<best:best=val;cohorts={}
                if val==best:
                    for m,c in old_poly[j].items():cohorts[m]=cohorts.get(m,0)+c
            counts=zeta(cohorts)
            assert counts[255]==sum(cohorts.values())
            union=0
            for m,v in cohorts.items():
                if v:union|=m
            answers[k]={'global_opt_cost':best,'all_closed_opt_count':str(counts[255]),
                        'cohort_positive_count':sum(v>0 for v in cohorts.values()),
                        'effective_cut_ids':[U[i] for i in range(8) if union>>i&1],
                        'cohorts':{str(m):str(v) for m,v in sorted(cohorts.items()) if v},
                        'counts_all_256':[str(q) for q in counts]}
            max_entries=max(max_entries,sum(map(len,old_poly)))
    assert answers[214]['all_closed_opt_count']=='4573020854769248525038387200000'
    assert answers[214]['cohort_positive_count']==20
    assert answers[214]['effective_cut_ids']==[3,8,9,10,27]
    assert answers[223]['effective_cut_ids']==[25,27]
    assert answers[294]['effective_cut_ids']==[15,17]
    assert len({tuple(answers[k]['counts_all_256'][m] for k in (214,223,294)) for m in range(256)})==256
    for mask in (0,1,2,16,64,128,170,255):
        independent=masked_cost_count(x,cuts,mask,BUDGETS)
        for k,(cost,num) in independent.items():
            assert cost==answers[k]['global_opt_cost'],(mask,k,cost,answers[k]['global_opt_cost'])
            assert str(num)==answers[k]['counts_all_256'][mask],(mask,k,num,answers[k]['counts_all_256'][mask])
    metric={'status':'PASS_R5_GLOBAL_MASK_COHORT_SINGLE_SWEEP',
            'frozen_input':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'model':'derived indexed-event one-dimensional radius-2 observer',
            'events':n,'original_cuts':len(cuts),'effective_cuts':list(U),'base_arcs':4383,
            'switch_arcs':len(requirements),'all_closed_arcs':4399,
            'layer_updates':max(BUDGETS)-1,'arcs_eligible_evaluated_on_tight_pass':arcs,
            'tight_arcs':tight,'integer_cohort_additions':mask_adds,
            'max_cohort_entries_at_sampled_layers':max_entries,
            'independent_mask_checks':[0,1,2,16,64,128,170,255],
            'triplet_signatures':256,'elapsed_seconds_local_measurement':round(time.perf_counter()-t0,3),
            'budgets':answers,
            'scope':'Single full-closed cost DP and requirement-signature count propagation; exact counts for all 256 masks at four K under established high-K cost invariance; not native X6/BRC.'}
    print(json.dumps(metric,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
