#!/usr/bin/env python3
"""Fused DP integer check for R5 high-budget exact scalar readouts.
Original scientific input pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
No native X6 inference; derived indexed-event radius-two observer only.
"""
from collections import Counter
from fractions import Fraction
import json

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF=10**15
U=(3,8,9,10,15,17,25,27)
PLANS=((214,223,294),(214,290,294),(214,291,294))

def frozen():
    pools={3:set(),12:set(),15:set()}; n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t; i=bit.bit_length()-1; mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]; k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools: pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,ps in pools.items() for p in ps)
    x=[0]
    for v in sorted(events): x.append(x[-1]+events[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and x[-1]==1065 and len(cuts)==28
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for j,i in enumerate(U) if mask>>j&1}
    out=[];shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in active: shift+=1
    return out

def prepare(x):
    n=len(x); pred=[[] for _ in x]; suffix=[INF]*n
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>7:break
            if all(min(x[t]-x[i],x[j]-x[t])<=2 for t in range(i+1,j)):
                pred[j].append((i,sum(min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j))))
        if x[-1]-x[j]<=2:
            suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    return pred,suffix

def sweep(x, budgets):
    budgets=tuple(sorted(set(budgets))); pred,suffix=prepare(x); n=len(x)
    c=[INF]*n;w=[0]*n
    for j in range(n):
        if x[j]-x[0]<=2:
            c[j]=sum(x[j]-x[t] for t in range(j));w[j]=1
    attempted=0;accepted=0;sum_bits=0
    results={}; layers=[]
    for k in range(1,max(budgets)+1):
        if k>1:
            nc=[INF]*n;nw=[0]*n
            for j in range(n):
                for i,v in pred[j]:
                    if not w[i]:continue
                    attempted+=1
                    sum_bits+=w[i].bit_length()
                    z=c[i]+v
                    if z<nc[j]:nc[j]=z;nw[j]=w[i];accepted+=1
                    elif z==nc[j]:nw[j]+=w[i];accepted+=1
            c,w=nc,nw
        if k in budgets:
            best=INF;count=0
            for j in range(n):
                if not w[j] or suffix[j]==INF:continue
                z=c[j]+suffix[j]
                if z<best:best=z;count=w[j]
                elif z==best:count+=w[j]
            if count:results[k]=(best,count)
        if k in (214,223,290,291,294):layers.append({'k':k,'transitions_considered_cumulative':attempted,'min_equal_updates_cumulative':accepted,'operand_bits_cumulative':sum_bits})
    return {'counts':{str(k):{'min_cost':results[k][0], 'number':str(results[k][1]), 'bits':results[k][1].bit_length()} for k in budgets},
            'layers':max(budgets)-1,'predecessor_edges':sum(map(len,pred)),
            'attempted_transitions':attempted,'relax_or_tie_updates':accepted,
            'operand_bit_volume':sum_bits,'checkpoints':layers}

def main():
    x,cuts=frozen();examples=[]
    for mask in (0,255):
        z=close(x,cuts,mask)
        fused=sweep(z,(214,223,290,291,294))
        separate={str(k):sweep(z,(k,)) for k in (214,223,290,291,294)}
        for k in (214,223,290,291,294):
            assert fused['counts'][str(k)]==separate[str(k)]['counts'][str(k)]
        m=[]
        for plan in PLANS:
            assert plan[-1]==294
            budget=fused
            independent=sum(separate[str(k)]['attempted_transitions'] for k in plan)
            independent_bits=sum(separate[str(k)]['operand_bit_volume'] for k in plan)
            # Output bits of all three exact integer counts
            bits=sum(fused['counts'][str(k)]['bits'] for k in plan)
            m.append({'plan':plan,'raw_count_bits':bits,'independent_DP_transitions':independent,
                      'fused_DP_transitions':fused['attempted_transitions'],
                      'independent_operand_bit_volume':independent_bits,
                      'fused_operand_bit_volume':fused['operand_bit_volume'],
                      'saved_transitions':independent-fused['attempted_transitions']})
        examples.append({'effective_mask':mask,'events':len(z),'max_budget':294,'pred_edges':fused['predecessor_edges'],
                         'fused_layers':fused['layers'],'fused_transitions':fused['attempted_transitions'],
                         'fused_operand_bit_volume':fused['operand_bit_volume'],
                         'plans':m,'checkpoints':fused['checkpoints']})
    out={'status':'PASS_R5_FUSED_DP_EXACT','scope':'derived indexed-event R2 integer nearest-center observer',
         'input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
         'test_masks':[0,255], 'candidate_plans':PLANS,
         'meaning':'Full fused recurrence through K=294 is identical for all listed plans; the proof is algebraic and these two masks are checks, not exhaustive mask tests',
         'examples':examples}
    print(json.dumps(out,sort_keys=True,indent=2))

if __name__=='__main__':main()
