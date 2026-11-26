"""GBB maximum cut via reverse reachability; integer labeled matching observer."""
from collections import Counter, deque
from random import Random
from time import perf_counter
import json
from residual_frontier import counts, cut_costs

def bits(w):
    while w:
        b=w&-w; w^=b
        yield b.bit_length()-1

def reverse_tight(opts,caps):
    # opts are local positive-resource masks; empty masks allowed.
    owners=[[] for _ in caps]
    def aug(t,seen):
        for j in bits(opts[t]):
            if j in seen: continue
            seen.add(j)
            if len(owners[j])<caps[j]:
                owners[j].append(t); return True
            for k,u in enumerate(owners[j]):
                if aug(u,seen):
                    owners[j][k]=t; return True
        return False
    h=sum(aug(t,set()) for t in opts)
    pred=[0]*len(caps)
    for j,group in enumerate(owners):
        for t in group:
            for k in bits(opts[t]): pred[k]|=1<<j
    free=sum(1<<j for j,c in enumerate(caps) if len(owners[j])<c)
    reach=free; todo=free
    while todo:
        b=todo&-todo;todo^=b
        new=pred[b.bit_length()-1]&~reach
        reach|=new;todo|=new
    W=((1<<len(caps))-1)^reach
    assert sum(w&~W==0 for w in opts.values())-sum(caps[j] for j in bits(W))==len(opts)-h
    return W,h

def enum_tight(opts,caps):
    d=[a-b for a,b in zip(counts(opts.values(),len(caps)),cut_costs(caps))]
    mx=max(d);W=0
    for j,v in enumerate(d):
        if v==mx:W|=j
    return W,len(opts)-mx

def banks(opts,caps,widths):
    active=sum(1<<j for j,c in enumerate(caps) if c)
    offsets=[];off=0
    for w in widths:offsets.append(off);off+=w
    masks=[((1<<w)-1)<<o for w,o in zip(widths,offsets)]
    groups=[{} for _ in widths]
    for t,mask in opts.items():
        mask&=active
        ids=[i for i,b in enumerate(masks) if mask&b]
        if len(ids)==1:
            i=ids[0];groups[i][t]=mask>>offsets[i]
    return [(u,caps[o:o+w]) for u,o,w in zip(groups,offsets,widths)]

def main():
    rng=Random(492611270330);random_banks=0
    for i in range(3000):
        m=rng.randrange(0,10);caps=[rng.randrange(4) for _ in range(m)]
        active=sum(1<<j for j,c in enumerate(caps) if c)
        opts={t:rng.randrange(1<<m)&active for t in range(rng.randrange(26))}
        a=reverse_tight(opts,caps);b=enum_tight(opts,caps);assert a==b
        # Matching order independence, same exact maximal cut.
        assert reverse_tight(dict(reversed(list(opts.items()))),caps)==b
        random_banks+=1
    records=json.load(open('witness_records.json'))
    cases=[g for r in records for g in banks(r['opts'],r['caps'],[len(r['caps'])//2]*2)]
    ref=[enum_tight(*g) for g in cases];new=[reverse_tight(*g) for g in cases];assert new==ref
    timings=[]
    for repeat in range(4):
        row={}
        for f in ([enum_tight,reverse_tight] if repeat%2==0 else [reverse_tight,enum_tight]):
            start=perf_counter();out=[f(*g) for g in cases];row[f.__name__]=perf_counter()-start;assert out==ref
        timings.append(row)
    hist=Counter(len(c) for u,c in cases)
    print(json.dumps(dict(random_banks=random_banks,random_order_checks=random_banks,records=len(records),bank_checks=len(cases),width_hist=dict(hist),enum_cuts=sum(1<<len(c) for u,c in cases),resource_vertices=sum(len(c) for u,c in cases),exclusive_targets=sum(len(u) for u,c in cases),timings=timings,mismatches=0),sort_keys=True))
    # A wide sparse bank, exponential enumeration not used. Each of 200 resources
    # in the first block has one dedicated target, others have free capacity.
    caps=[1]*400;opts={i:1<<i for i in range(200)}
    W,h=reverse_tight(opts,caps);assert W==(1<<200)-1 and h==200
    print(json.dumps(dict(wide_bank=400,rank=h,blocked=W.bit_count(),reference='analytic')))
if __name__=='__main__':main()
