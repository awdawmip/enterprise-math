#!/usr/bin/env python3
"""R5 exact 8-bit predecessor-kernel decomposition; freeze 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Derived integer-indexed radius-two observer, not a native X6/BRC theorem.
"""
from collections import Counter
from fractions import Fraction
import json

W=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K0=(-432,0,0,0,0,-108,0,0,0,0,540,0,0,0,0)
U=(3,8,9,10,15,17,25,27)

def source():
    p={3:set(),12:set(),15:set()}; n=k=m=0
    for t in range(1,32768):
        b=t&-t;i=b.bit_length()-1;m^=b
        s=1 if m&b else -1
        n+=s*W[i];k+=s*K0[i]
        if n>=3 and k%36==0 and k//36 in p:p[k//36].add(n)
    assert tuple(len(p[z]) for z in (3,12,15))==(538,298,229)
    c=Counter(Fraction(n,q) for q,ss in p.items() for n in ss)
    x=[Fraction(0)]
    for v in sorted(c):x.append(x[-1]+c[v])
    cuts=[i for i in range(len(x)-1) if x[i+1]-x[i]==3]
    assert (len(x),x[-1],len(cuts))==(954,1065,28)
    return x,cuts

def close(x,cuts,mask):
    active={cuts[i] for j,i in enumerate(U) if mask>>j&1}
    out=[];shift=0
    for j,v in enumerate(x):
        out.append(v-shift)
        if j in active:shift+=1
    return out

def kernel(z):
    n=len(z);p=[{} for _ in z];suffix=[None]*n
    for j in range(n):
        for i in range(j-1,-1,-1):
            if z[j]-z[i]>7:break
            d=[min(z[t]-z[i],z[j]-z[t]) for t in range(i+1,j)]
            if all(t<=2 for t in d):p[j][i]=sum(d)
        if z[-1]-z[j]<=2:suffix[j]=sum(z[t]-z[j] for t in range(j+1,n))
    initial=[None if z[j]-z[0]>2 else sum(z[j]-z[t] for t in range(j)) for j in range(n)]
    return p,suffix,initial

def main():
    x,cuts=source();base,s0,h0=kernel(close(x,cuts,0));cond=[];examples=[]
    for b,u in enumerate(U):
        c=cuts[u];p,s,h=kernel(close(x,cuts,1<<b))
        assert (s,h)==(s0,h0)
        change=[]
        for j in range(len(x)):
            for i in p[j].keys()|base[j].keys():
                if p[j].get(i)!=base[j].get(i):
                    assert i<=c<j and i not in base[j] and i in p[j]
                    change.append((i,j,p[j][i]))
        change.sort();assert len(change)==2
        cond.append(change)
        examples.append({'effective_cut':u,'gap_index':c,
                         'conditional_arcs':[{'from':i,'to':j,'cost':int(v)} for i,j,v in change]})
    sep=[]
    for a,b in zip(U,U[1:]):
        # A path crossing both gap-3 cuts has length >=2+inter-cut-distance+2.
        gap=x[cuts[b]]-x[cuts[a]+1]
        sep.append({'left':a,'right':b,'inter_cut_distance':int(gap),
                    'minimum_simultaneously_closed_span':int(gap+4)})
        assert gap+4>7
    checked=0;edge_counts=[]
    for mask in range(256):
        pred,s,h=kernel(close(x,cuts,mask))
        expect=[d.copy() for d in base]
        for bit in range(8):
            if mask>>bit&1:
                for i,j,v in cond[bit]:expect[j][i]=v
        assert pred==expect and s==s0 and h==h0
        edge_counts.append(sum(len(p) for p in pred))
        assert edge_counts[-1]==4383+2*mask.bit_count()
        checked+=1
    out={'status':'PASS_R5_EIGHT_SWITCH_KERNEL_EXHAUSTIVE',
         'science_input_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
         'events':len(x),'cuts_all':len(cuts),'effective_cut_ids':list(U),
         'baseline_arcs':sum(len(p) for p in base),'added_arcs_per_enabled_bit':2,
         'all_enabled_arcs':edge_counts[-1],'configurations_checked':checked,
         'minimum_arcs':min(edge_counts),'maximum_arcs':max(edge_counts),
         'initial_and_terminal_kernels_invariant':True,
         'nearest_cut_pair_separations':sep,'two_arc_switches':examples,
         'scope':'derived indexed-event radius-two predecessor graph only; no claim of DP solution locality or native X6 equivalence'}
    print(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2))

if __name__=='__main__':main()
