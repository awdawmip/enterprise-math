#!/usr/bin/env python3
"""Exact integer R5 high-budget three-scalar-query decoder classification.
Source pin 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Self-contained Python standard library; no floating point or MILP.
"""
import json
from collections import Counter
from fractions import Fraction

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
INF=10**15

def frozen():
    pools={3:set(),12:set(),15:set()}
    n=k=mask=0
    for t in range(1,1<<15):
        bit=t&-t; i=bit.bit_length()-1; mask^=bit
        sign=1 if mask&bit else -1
        n+=sign*W[i]; k+=sign*K0[i]
        if n>=3 and k%36==0 and k//36 in pools:
            pools[k//36].add(n)
    assert [len(pools[q]) for q in (3,12,15)]==[538,298,229]
    events=Counter(Fraction(p,q) for q,ps in pools.items() for p in ps)
    x=[0]
    for v in sorted(events): x.append(x[-1]+events[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert len(x)==954 and x[-1]==1065 and len(cuts)==28
    return x,cuts

def close(x,cuts,bits,mask):
    active={cuts[bit] for j,bit in enumerate(bits) if mask>>j&1}
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
            if all(min(x[t]-x[i],x[j]-x[t])<=2 for t in range(i+1,j)):
                pred[j].append((i,sum(min(x[t]-x[i],x[j]-x[t]) for t in range(i+1,j))))
        if x[-1]-x[j]<=2:suffix[j]=sum(x[t]-x[j] for t in range(j+1,n))
    c=[INF]*n; w=[0]*n; output={}
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
        if count: output[k]=(best,count)
    return output

def main():
    x,cuts=frozen()
    specs={}
    for name,lo,hi,bits in [('A',214,221,[3,8,9,10,27]),('B',223,291,[25,27]),('C',293,314,[15,17])]:
        data=[spectrum(close(x,cuts,bits,m),hi) for m in range(1<<len(bits))]
        specs[name]={k:[d[k][1] for d in data] for k in range(lo,hi+1)}
    A,B,C=(specs[x] for x in 'ABC')
    valid_A=[k for k,v in A.items() if all(len({v[m] for m in range(32) if (m>>4&1)==b})==16 for b in (0,1))]
    valid_B=[k for k,v in B.items() if len(set(v))==4]
    valid_C=[k for k,v in C.items() if len(set(v))==4]
    assert valid_A==list(range(214,220))
    assert valid_B==list(range(223,292))
    assert valid_C==list(range(294,314))
    projections=[((x&15)|((x>>7&1)<<4),(x>>6)&3,(x>>4)&3) for x in range(256)]
    valid=0; bad={}
    for ka,va in A.items():
        for kb,vb in B.items():
            for kc,vc in C.items():
                sig={(va[a],vb[b],vc[c]) for a,b,c in projections}
                if len(sig)==256:valid+=1
                elif (ka,kb,kc) in [(214,223,293),(220,223,294),(221,223,294)]:
                    bad[f'{ka},{kb},{kc}']=len(sig)
    assert valid==8280 and bad=={'214,223,293':192,'220,223,294':240,'221,223,294':128}
    assert A[220][9]==A[220][12]==38336726601491749449844654080000
    assert C[293][1]==C[293][2]==13102659259476980304288153600
    result={'status':'PASS_R5_ALL_TRIPLE_DECODERS_EXACT','input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
            'domain':'954 indexed events; K=214..954','valid_A_budgets':valid_A,
            'valid_B_range':[min(valid_B),max(valid_B)],'valid_C_range':[min(valid_C),max(valid_C)],
            'structurally_eligible_triples':len(A)*len(B)*len(C),
            'exact_decoder_triples':valid,'failed_triples':len(A)*len(B)*len(C)-valid,
            'witness_collision_A_220':str(A[220][9]),'witness_collision_C_293':str(C[293][1]),
            'failing_example_distinct_signatures':bad,
            'scope':'exact derived scalar-count classification; no native X6 observer admission'}
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
