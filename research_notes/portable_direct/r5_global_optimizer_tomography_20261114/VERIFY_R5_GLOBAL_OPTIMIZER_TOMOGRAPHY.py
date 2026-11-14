#!/usr/bin/env python3
"""Exact R5 optimizer-family tomography for all 214<=K<=954.
Scientific input frozen: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived 1D indexed-center radius-two observer; exact Python integers.
Usage: python VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py > proof_data.json
"""
import json
from collections import Counter
from fractions import Fraction

W = (336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0 = (-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF = 10**15

def frozen():
    pools = {3:set(),12:set(),15:set()}
    n = k = mask = 0
    for t in range(1,1<<15):
        bit=t&-t; i=bit.bit_length()-1; mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]; k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)] == [538,298,229]
    events=Counter(Fraction(p,q) for q, ps in pools.items() for p in ps)
    x=[0]
    for v in sorted(events): x.append(x[-1]+events[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and x[-1]==1065 and len(cuts)==28
    assert min(b-a for a,b in zip(cuts,cuts[1:]))==5
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for i in range(len(cuts)) if mask>>i&1}
    out=[]; shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in active:shift+=1
    return out

def spectrum(x,max_k):
    n=len(x);pred=[[] for _ in x];suffix=[INF]*n
    for j in range(n):
        for i in range(j-1,-1,-1):
            if x[j]-x[i]>7:break
            distances=[min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j)]
            if all(d<=2 for d in distances):pred[j].append((i,sum(distances)))
        if x[-1]-x[j]<=2:suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    c=[INF]*n;w=[0]*n;output={}
    for j in range(n):
        if x[j]-x[0]<=2:
            c[j]=sum(x[j]-x[t] for t in range(j));w[j]=1
    for k in range(1,max_k+1):
        if k>1:
            nc=[INF]*n;nw=[0]*n
            for j in range(n):
                for i,v in pred[j]:
                    if not w[i]:continue
                    z=c[i]+v
                    if z<nc[j]:nc[j]=z;nw[j]=w[i]
                    elif z==nc[j]:nw[j]+=w[i]
            c,w=nc,nw
        best=INF;count=0
        for j in range(n):
            if not w[j] or suffix[j]==INF:continue
            z=c[j]+suffix[j]
            if z<best:best=z;count=w[j]
            elif z==best:count+=w[j]
        if count:output[k]=(best,count)
    return output

def local_spectrum(x,cuts,bits,max_k):
    return {m:spectrum(close(x,cuts,sum((1<<bit) for j,bit in enumerate(bits) if m>>j&1)),max_k)
            for m in range(1<<len(bits))}

def main():
    x,cuts=frozen();whole=(1<<28)-1
    full=spectrum(close(x,cuts,whole),315)
    empty=spectrum(x,315)
    assert all(full[k][0]==empty[k][0] for k in range(214,316))
    need={k:[] for k in range(214,316)}
    for i in range(28):
        sp=spectrum(close(x,cuts,whole^(1<<i)),315)
        for k in need:
            assert sp[k][0]==full[k][0]
            assert sp[k][1]<=full[k][1]
            if sp[k][1]<full[k][1]:need[k].append(i)
    bands=[(214,221,[3,8,9,10,27]),(222,222,[27]),(223,291,[25,27]),
           (292,292,[]),(293,314,[15,17]),(315,315,[])]
    assert all(need[k]==bits for low,high,bits in bands for k in range(low,high+1))
    rows=[]
    for low,high,bits in bands:
        family=local_spectrum(x,cuts,bits,high)
        m=len(bits)
        for k in range(low,high+1):
            N={t:family[t][k][1] for t in family}
            assert set(family[t][k][0] for t in family)=={full[k][0]}
            assert N[0]==empty[k][1] and N[(1<<m)-1]==full[k][1]
            a={t:sum((-1)**((t^s).bit_count())*N[s] for s in range(1<<m) if (s&t)==s)
               for t in range(1<<m)}
            assert all(v>=0 for v in a.values()) and sum(a.values())==full[k][1]
            for b in N:
                assert N[b]==sum(a[s] for s in a if (s&b)==s)
            recognized={bits[j] for j in range(m) if any(a[s]>0 and s>>j&1 for s in a)}
            assert recognized==set(need[k])
            signatures={tuple(s for s in a if a[s]>0 and (s&b)==s) for b in N}
            row={'K':k,'J':full[k][0],'essential_cuts':bits,
                 'all_opt_count':str(full[k][1]),'nonzero_masks':sum(v>0 for v in a.values()),
                 'distinct_families':len(signatures)}
            if k in (214,221,222,223,291,292,294,314,315):
                row['a_mask']={','.join(str(bits[j]) for j in range(m) if s>>j&1):str(v)
                               for s,v in a.items() if v>0}
            if k in (214,223,294):
                row['distinct_scalar_counts']=len(set(N.values()))
                assert len(set(N.values()))==(1<<m)
            rows.append(row)
    assert next(z for z in rows if z['K']==214)['all_opt_count']=='4573020854769248525038387200000'
    assert next(z for z in rows if z['K']==292)['all_opt_count']=='247939829006869892620615680'
    assert next(z for z in rows if z['K']==294)['all_opt_count']==str(full[294][1])
    result={'status':'PASS_EXACT_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY',
            'model':'frozen 954-event derived 1D indexed-center radius-2 observer',
            'scientific_input_commit':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'cut_event_indices':cuts,'complete_K_scope':[214,954],
            'all_effective_cut_bits':[3,8,9,10,15,17,25,27],
            'scalar_count_decoder_budgets':[214,223,294],
            'combined_distinct_trajectories':256,
            'closures_per_trajectory':1048576,
            'rows_214_to_315':rows,
            'for_K_316_to_954':'optimizer families are invariant by prior exact endpoint-family theorem',
            'independent_review':'NOT_REVIEWED'}
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
