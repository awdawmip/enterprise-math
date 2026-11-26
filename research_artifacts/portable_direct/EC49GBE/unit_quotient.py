"""EC49GBE all-subset rank quotient, using frozen labels and exact Hall reference."""
from collections import Counter
from random import Random
from unit_slack import reduce_bank,enum_blocks
from reverse_tight import bits,banks
from residual_frontier import reference
import json

def reps(q,blocks,reverse=False):
    seen=set();p={}
    for t,w in (reversed(list(q.items())) if reverse else q.items()):
        b=next((b for b in blocks if w and w&~b==0),0)
        if not w or b and b in seen:continue
        if b:seen.add(b)
        p[t]=w
    return p

def main():
    rng=Random(492611270534);tests=0
    for _ in range(600):
        m=rng.randrange(1,8);c=[rng.randrange(1,4) for j in range(m)]
        u={str(i):rng.randrange(1<<m) for i in range(rng.randrange(13))}
        W,h,p,rc,keep=reduce_bank(u,c);bl,_,_=enum_blocks(p,rc)
        xs={f'x{i}':rng.randrange(1<<len(rc)) for i in range(rng.randrange(8))}
        keys=list(xs)
        for mask in range(1<<len(keys)):
            q={t:xs[t] for j,t in enumerate(keys) if mask>>j&1}
            r=reference(dict(p,**q),rc)
            for rev in (False,True):assert reference(dict(p,**reps(q,bl,rev)),rc)==r
            tests+=1
    records=json.load(open('witness_records.json'));stats=Counter();left=[]
    for i,r in enumerate(records):
        c=r['caps'];opts=r['opts'];w=len(c)//2;active=sum(1<<j for j,v in enumerate(c) if v);u={};blocks=[];W=0
        for j,(p,bc) in enumerate(banks(opts,c,[w,w])):
            bw,h,rp,rc,keep=reduce_bank(p,bc);bl,_,_=enum_blocks(rp,rc);W|=bw<<(j*w)
            blocks.extend(sum(1<<keep[k] for k in bits(b))<<(j*w) for b in bl)
            u.update({t:v<<(j*w) for t,v in p.items()})
        sh={t:v&active&~W for t,v in opts.items() if t not in u and v&active}
        x={t:v for t,v in sh.items() if v};p=reps(x,blocks);q=reps(x,blocks,True)
        H=reference(opts,c);base=reference(u,c)
        for a in (p,q):assert reference(dict(u,**{t:opts[t] for t in a}),c)==H
        stats.update(records=1,live_shared=len(x),representatives=len(p),loops=len(sh)-len(x),parallel_removed=len(x)-len(p))
        J=base+len(p)-H;assert J>=0
        if J:left.append([i,J])
    print(json.dumps(dict(random_graphs=600,random_subsets=tests,representative_order_checks=2*tests,stats=stats,remaining_residuals=left,mismatches=0),sort_keys=True))
if __name__=='__main__':main()
