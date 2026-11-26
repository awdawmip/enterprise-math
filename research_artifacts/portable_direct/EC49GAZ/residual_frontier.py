"""EC49GAZ: exact shared-cut frontier, independent full-cut reference."""
import json
from collections import Counter
from random import Random
from time import perf_counter


def cut_costs(caps):
    c = [0]*(1 << len(caps))
    for w in range(1, len(c)):
        b = w & -w
        c[w] = c[w-b] + caps[b.bit_length()-1]
    return c


def counts(masks, m):
    f = [0]*(1 << m)
    for w in masks:
        f[w] += 1
    for j in range(m):
        b = 1 << j
        for w in range(len(f)):
            if w & b:
                f[w] += f[w-b]
    return f


def reference(opts, caps):
    return len(opts)-max(f-c for f,c in zip(counts(opts.values(),len(caps)),cut_costs(caps)))


def bank(exclusive, shared, caps, st):
    costs=cut_costs(caps)
    f=counts(exclusive,len(caps))
    deficit=max(a-b for a,b in zip(f,costs))
    best={}
    for w,(a,b) in enumerate(zip(f,costs)):
        p=deficit-a+b
        # A cut with p >= coverage cannot contribute positive joint residual.
        s=sum(1<<i for i,mask in enumerate(shared) if mask & ~w == 0)
        if p < s.bit_count():
            best[s]=min(best.get(s,p),p)
    st['cuts']+=len(costs);st['distinct_positive_candidates']+=len(best)
    # Keep only nondominated coverage sets, preferring superset with lower cost.
    out=[]
    for s,p in sorted(best.items(),key=lambda kv:(kv[1],-kv[0].bit_count(),kv[0])):
        if not any(s & ~t == 0 for t,q in out):
            out.append((s,p))
    st['frontier']+=len(out)
    return deficit,out


def residual(opts,caps,q,st):
    active=sum(1<<j for j,c in enumerate(caps) if c)
    mask=(1<<q)-1
    u=[];v=[];a=[];b=[];z=0
    for w in opts.values():
        w &= active
        l=w&mask;r=w>>q
        if l and r:a.append(l);b.append(r)
        elif l:u.append(l)
        elif r:v.append(r)
        else:z+=1
    da,fa=bank(u,a,caps[:q],st)
    db,fb=bank(v,b,caps[q:],st)
    B=len(opts)-z-da-db
    J=0
    for s,p in fa:
        for t,r in fb:
            st['pairs']+=1
            J=max(J,(s&t).bit_count()-p-r)
    st['zero_by_empty_frontier']+=not fa or not fb
    return B,J


def main():
    rng=Random(492611270030);st=Counter();hist=Counter();test=0
    for _ in range(3000):
        q=rng.randrange(1,5);r=rng.randrange(1,5);caps=[rng.randrange(5) for _ in range(q+r)]
        opts={i:rng.randrange(1<<(q+r)) for i in range(rng.randrange(25))}
        B,J=residual(opts,caps,q,st);assert B-J==reference(opts,caps);test+=1
    print(json.dumps({'random_graphs':test,'random_stats':dict(st)},sort_keys=True))
    st=Counter();allthreshold=0;miss=0;positive=[];records=json.load(open('witness_records.json'))
    for i,r in enumerate(records):
        opts=r['opts'];caps=r['caps'];B,J=residual(opts,caps,len(caps)//2,st)
        H=reference(opts,caps);assert B-J==H and (H<=r['L'])==r['ans']
        hist[J]+=1;allthreshold+=len(opts)+1;miss+=J
        if J:positive.append([i,B,H,r['L']])
    print(json.dumps({'records':len(records),'histogram':dict(hist),'all_integer_thresholds':allthreshold,'exclusive_bound_missed_thresholds':miss,'stats':dict(st),'positive_records':positive},sort_keys=True))

if __name__=='__main__':main()
