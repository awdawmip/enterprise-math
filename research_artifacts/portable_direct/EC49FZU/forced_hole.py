from functools import lru_cache
from itertools import combinations
from random import Random
from collections import Counter
import csv,json,time
from gen import F,physical
from fourth import fibers
from quotient_opt import optimum
from dominance import constraints,reduce

def bits(x):
    while x:
        b=x&-x;yield b;x^=b

def child(f,r,j,yes,hmax):
    out=[]; bit=1<<j
    for v,b,a in f:
        active=bool(v>>r&1)
        if yes:
            if not active or b&bit:continue
            a&=~bit
        elif active:
            if not a&bit:continue
            b|=bit
        if b.bit_count()>hmax:continue
        if b.bit_count()==hmax:a=b
        out.append((v,b,a))
    return out

def opt(f,u,h,nr,nc,hmax):
    b=next(b for v,b,a in f if v==u);o=h&~b
    assert h.bit_count()==hmax
    q=[(u^v,c&~h) for v,c,a in f if v!=u and (c|o).bit_count()<=hmax]
    full=(1<<len(q))-1
    row=[sum(1<<i for i,(d,l) in enumerate(q) if d>>r&1) for r in range(nr)]
    live={sum(1<<i for i,(d,l) in enumerate(q) if l&j):j for j in bits(((1<<nc)-1)&~h)};live.pop(0,None)
    by=[[v for v in live if v>>i&1] for i in range(len(q))]
    @lru_cache(None)
    def tau(e):
        if not e:return 0,0
        i=min((b.bit_length()-1 for b in bits(e)),key=lambda i:len(by[i]))
        return min(((1+n,p|live[v]) for v in by[i] for n,p in [tau(e&~v)]),default=(100,0))
    best=(100,0,0); cov=[0]*(1<<nr)
    for t in range(1<<nr):
        if t:
            v=t&-t;cov[t]=cov[t^v]|row[v.bit_length()-1]
        p=(t&u).bit_count();n=(t&~u).bit_count()
        if p+n>=best[0]:continue
        l,P=tau(full&~cov[t]);c=n+max(p,l)
        if c<best[0]:best=(c,t,P)
    c,t,P=best
    assert all(t&d or P&l for d,l in q)
    return c+o.bit_count(),t,P,o

def obs(x,r,j):return bool(x[0]>>r&1) and not bool(x[1]>>j&1)

def explicit(f,hmax):
    out=[]
    for v,b,a in f:
        for k in range(min(hmax-b.bit_count(),(a&~b).bit_count())+1):
            for cs in combinations(list(bits(a&~b)),k):out.append((v,b|sum(cs)))
    return out

def brute(st,x,nr,nc):
    rivals=[y for y in st if y!=x];full=(1<<len(rivals))-1
    masks=[sum(1<<i for i,y in enumerate(rivals) if obs(y,r,j)!=obs(x,r,j)) for r in range(nr) for j in range(nc)]
    @lru_cache(None)
    def dp(e):
        if not e:return 0
        bit=e&-e
        return min(1+dp(e&~m) for m in masks if m&bit)
    return dp(full)

def main():
    rng=Random(16943); totals=Counter()
    # Genuine histories starting at a common positive anchor (0,0).
    for nr,nc,hmax in [(3,4,2),(4,5,3)]:
        allf=[(u,0,((1<<nc)-1)^1) for u in range(1,1<<nr,2)]
        for i in range(60):
            x=rng.choice([x for x in explicit(allf,hmax) if x[1].bit_count()==hmax]); f=allf[:]
            for _ in range(rng.randrange(6)):
                r,j=rng.randrange(nr),rng.randrange(nc);f=child(f,r,j,obs(x,r,j),hmax)
            st=explicit(f,hmax)
            for x in rng.sample([x for x in st if x[1].bit_count()==hmax],min(2,sum(h.bit_count()==hmax for u,h in st))):
                for r in range(nr):
                    for j in range(nc):
                        g=child(f,r,j,obs(x,r,j),hmax); s=[y for y in st if obs(y,r,j)==obs(x,r,j)]
                        assert sorted(s)==sorted(explicit(g,hmax))
                        c,t,P,o=opt(g,*x,nr,nc,hmax)
                        assert c==brute(s,x,nr,nc)
                        assert [y for y in s if not ((y[0]^x[0])&t or y[1]&P or o&~y[1])]==[x]
                        totals['small_fixed_checks']+=1
    print(dict(totals),flush=True)
    roots=json.load(open('fourth.json')); ids=list(range(0,len(roots),31))
    with open('u_cert.csv','w') as out:
        w=csv.writer(out,lineterminator='\n')
        for i in ids:
            n,key,_,_=roots[i];r,mask,other=key;f=list(fibers(key)); st=physical([mask,*other],14,r,0);assert len(st)==n
            sat=[x for x in st if x[1].bit_count()==14];x=sat[(i*16943)%len(sat)];u,h=x
            # Compare original FZO, then exact child optimizer with explicit physical replay.
            b,o,q=constraints(f,u,h);c,*_=optimum(u,b,o,reduce(q));z,*_=opt(f,u,h,10,25,14);assert c==z;totals['fzo_root_checks']+=1
            for qid in rng.sample(range(250),4):
                r,j=divmod(qid,25);g=child(f,r,j,obs(x,r,j),14);s=[y for y in st if obs(y,r,j)==obs(x,r,j)]
                assert sorted(s)==sorted(explicit(g,14))
                cost,t,P,o=opt(g,u,h,10,25,14)
                assert [y for y in s if not ((y[0]^u)&t or y[1]&P or o&~y[1])]==[x]
                assert 1+cost>=z
                w.writerow((i,u,h,r,j,int(obs(x,r,j)),len(s),z,1+cost,t,P,o));totals['frozen_fixed_checks']+=1;totals['frozen_state_replays']+=len(s)
            out.flush()
    print(dict(totals))
if __name__=='__main__':main()
