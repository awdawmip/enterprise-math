"""GAW: Hall threshold witnesses, exact subset zeta, and prefix-order comparison."""
from collections import Counter
from math import comb
from random import Random
from time import perf_counter_ns
import json
import threshold_hall as prev
from peel_hall import cut_reference
from gal_path_hall import Bound


def verify(opts,caps,L,ans,w):
    if ans:
        if L>=len(opts): return w==[]
        if L<0 or len(set(w))!=len(w) or any(t not in opts for t in w): return False
        u=0
        for t in w: u|=opts[t]
        return len(w)-sum(c for j,c in enumerate(caps) if u>>j&1)>=len(opts)-L
    if L<0: return w==[]
    used=Counter()
    for t,j in w:
        if t not in opts or not (0<=j<len(caps)) or not (opts[t]>>j&1):return False
        used[j]+=1
    return len(w)>L and len({t for t,j in w})==len(w) and all(v<=caps[j] for j,v in used.items())


def prefix(opts,caps,L,st,order='degree'):
    n=len(opts); st['calls']+=1;st['targets']+=n
    if L<0:return False,[]
    if L>=n:return True,[]
    active=sum(1<<j for j,c in enumerate(caps) if c)
    masks={t:m&active for t,m in opts.items()}
    def mass(m):return sum(c for j,c in enumerate(caps) if m>>j&1)
    if order=='mass': key=lambda t:(mass(masks[t]),masks[t].bit_count(),masks[t])
    elif order=='density':
        freq=Counter(masks.values())
        # integer comparison surrogate: small capacity per identical-neighborhood group first
        key=lambda t:(mass(masks[t])*n//freq[masks[t]],mass(masks[t]),masks[t])
    else:key=lambda t:masks[t].bit_count()
    targets=sorted(opts,key=key); owners=[[] for c in caps]; free=active; unmatched=[]; h=0
    def augment(t):
        nonlocal free
        seen=0
        def dfs(u):
            nonlocal seen,free
            a=masks[u]&free
            if a:
                j=(a&-a).bit_length()-1;owners[j].append(u)
                if len(owners[j])==caps[j]:free&=~(1<<j)
                return True
            a=masks[u]&~seen
            while a:
                bit=a&-a;j=bit.bit_length()-1;seen|=bit
                for i,v in enumerate(owners[j]):
                    if dfs(v):owners[j][i]=u;return True
                a&=~seen
            return False
        return dfs(t)
    for i,t in enumerate(targets,1):
        st['processed']+=1
        if augment(t):h+=1
        else:unmatched.append(t)
        if h>L:
            st['lower_stop']+=1;return False,[(u,j) for j,o in enumerate(owners) for u in o]
        if i-h>=n-L:
            st['upper_stop']+=1
            seen=0; reach=set(unmatched); todo=list(unmatched)
            while todo:
                a=masks[todo.pop()]&~seen
                while a:
                    bit=a&-a;j=bit.bit_length()-1;seen|=bit;a^=bit
                    for u in owners[j]:
                        if u not in reach:reach.add(u);todo.append(u)
            st['witness_targets']+=len(reach)
            return True,sorted(reach)
    raise AssertionError('unreachable')


def minimum_upper(opts,caps,L):
    """Exact minimum cardinality upper witness; None if no such witness. For small m."""
    n=len(opts);k=n-L
    if k<=0:return []
    m=len(caps);s=1<<m;counts=[0]*s
    for v in opts.values():counts[v]+=1
    for j in range(m):
        bit=1<<j
        for i in range(s):
            if i&bit:counts[i]+=counts[i^bit]
    mass=[0]*s;best=None
    for i in range(s):
        if i:
            b=i&-i;mass[i]=mass[i^b]+caps[b.bit_length()-1]
        if counts[i]>=mass[i]+k and (best is None or mass[i]<mass[best]):best=i
    if best is None:return None
    return [t for t,v in opts.items() if v&~best==0][:mass[best]+k]


def run():
    rng=Random(49261129); syn=Counter();checks=0
    for _ in range(1000):
        m=rng.randrange(1,8);n=rng.randrange(0,12);caps=[rng.randrange(5) for j in range(m)];opts={t:rng.randrange(1<<m) for t in range(n)};h=cut_reference(opts,caps)
        # independently enumerate target subsets once to determine min witness cardinality for all deficits
        smallest={}
        for mask in range(1<<n):
            a=[t for t in opts if mask>>t&1];u=0
            for t in a:u|=opts[t]
            d=len(a)-sum(c for j,c in enumerate(caps) if u>>j&1)
            if d>0:
                for k in range(1,d+1):smallest[k]=min(smallest.get(k,n+1),len(a))
        for L in range(-1,n+1):
            ans,w=prefix(opts,caps,L,syn);assert ans==(h<=L) and verify(opts,caps,L,ans,w)
            z=minimum_upper(opts,caps,L)
            assert (z is not None)==ans
            if ans:assert verify(opts,caps,L,True,z) and len(z)==(0 if L>=n else smallest[n-L])
            checks+=1
    rows=[]; totals={}; old=json.load(open('gap_target.json'))['rows']; records=[]
    for mode in ('degree','mass','density'):
        agg=Counter(); timings=0; cts=Counter(); mode_rows=[]
        def wrapped(opts,caps,L,st):
            ans,w=prefix(opts,caps,L,st,mode); assert verify(opts,caps,L,ans,w)
            if mode=='degree':
                rec={'opts':opts,'caps':caps,'L':L,'ans':ans,'w':w};records.append(rec)
                if ans:
                    z=minimum_upper(opts,caps,L);assert z is not None and verify(opts,caps,L,True,z) and len(z)<=len(w)
                    st['min_witness_targets']+=len(z);st['strictly_smaller']+=len(z)<len(w);rec['min']=z
            return ans
        prev.at_most=wrapped
        for i,line in enumerate(open('ga_nodes.txt')):
            k,n,*a=map(int,line.split());st=list(zip(a[::2],a[1::2]));b=Bound(st)
            for j in range(2):
                d=k+j;row=old[2*i+j];assert (row['i'],row['d'])==(i,d)
                o=prev.ThresholdOracle(b,st);t0=perf_counter_ns();assert o.v(b.full,d,b.full)==row['cap'];assert o.graphs(d,row['qs'],row['goals'])==row['adj'];timings+=perf_counter_ns()-t0
                agg.update(o.threshold_stats);cts.update(o.stats);mode_rows.append(dict(o.threshold_stats))
            b.clear()
        totals[mode]={'stats':dict(agg),'search':dict(cts),'time_ns_includes_witness_checks':timings,'rows':mode_rows}
    assert totals['degree']['search']==totals['mass']['search']==totals['density']['search']
    with open('witness_records.json','w') as f:json.dump(records,f,separators=(',',':'))
    print(json.dumps({'synthetic_models':1000,'synthetic_thresholds':checks,'modes':totals},separators=(',',':')))
if __name__=='__main__':run()
