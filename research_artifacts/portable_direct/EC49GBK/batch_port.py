"""GBK batch update: exact insertion of a finite multiset of fresh labels."""
from random import Random
from collections import Counter
import json
from port_observer import direct,compact
from sparse_port import step

def batch(p,es):
    if not es:return 0,p
    counts=Counter(es)
    cover={w:sum(n for e,n in counts.items() if e&~w==0) for w in p}
    d=max(cover[w]-v for w,v in p.items())
    q={w:v+d-cover[w] for w,v in p.items()}
    out={}
    for w,v in sorted(q.items(),key=lambda a:(a[1],-a[0].bit_count(),a[0])):
        if not any(w&~t==0 for t in out):out[w]=v
    return len(es)-d,out

def test():
    rng=Random(492611271126);st=Counter()
    for _ in range(2000):
        m=rng.randrange(1,8);c=[rng.randrange(4) for _ in range(m)]
        a=[rng.randrange(1<<m) for _ in range(rng.randrange(16))]
        es=[rng.randrange(1<<m) for _ in range(rng.randrange(13))]
        h,g=direct(a,c);p=compact(g,m);hh,gg=direct(a+es,c)
        inc,q=batch(p,es);assert inc==hh-h and q==compact(gg,m) and q.keys()<=p.keys()
        s=p;t=0
        for e in reversed(es):
            i,s=step(s,e);t+=i
        assert t==inc and s==q
        st['graphs']+=1;st['inserted_labels']+=len(es);st['coordinates']+=len(gg)
    return dict(st)
if __name__=='__main__':print(json.dumps(test(),sort_keys=True))
