"""R67 exact subtree-certificate cache. Python 3.10+, standard library only.
Frozen auxiliary S23 circle model, not native-X6 arithmetic.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from math import floor
from bisect import bisect_right
from random import Random
from collections import Counter
from time import perf_counter
import json
PIN='43ec6098b1330ae86d0a7863be336c5d97f6ef34'
def fr(x): return x-floor(x)
def ce(x): return -floor(-x)
def avoid(a,b,L,U):
    x,y=a+b*L,a+b*U
    return x.denominator!=1 and y.denominator!=1 and floor(x)==floor(y)
def history(th,m):
    h=sorted((fr(k*th),k) for k in range(m))
    if len({p for p,z in h})!=m: raise ValueError('history collision')
    return h
@dataclass(frozen=True,eq=False)
class N:
    k:tuple; p:int; l:object; r:object; count:int; lo:F; hi:F; tlo:int; thi:int
def node(k,p,l=None,r=None):
    xs=[k[0]]+([l.lo] if l else [])+([r.lo] if r else [])
    ys=[k[0]]+([l.hi] if l else [])+([r.hi] if r else [])
    ts=[k[1]]+([l.tlo] if l else [])+([r.tlo] if r else [])
    us=[k[1]]+([l.thi] if l else [])+([r.thi] if r else [])
    return N(k,p,l,r,1+(l.count if l else 0)+(r.count if r else 0),min(xs),max(ys),min(ts),max(us))
def split(n,k):
    if n is None:return None,None
    if n.k<k:
        a,b=split(n.r,k);return node(n.k,n.p,n.l,a),b
    a,b=split(n.l,k);return a,node(n.k,n.p,b,n.r)
def merge(a,b):
    if not a:return b
    if not b:return a
    if a.p>b.p:return node(a.k,a.p,a.l,merge(a.r,b))
    return node(b.k,b.p,merge(a,b.l),b.r)
def add(n,k,p):
    if n is None:return node(k,p)
    if k==n.k:raise ValueError('duplicate branch')
    if p>n.p:
        a,b=split(n,k);return node(k,p,a,b)
    if k<n.k:return node(n.k,n.p,add(n.l,k,p),n.r)
    return node(n.k,n.p,n.l,add(n.r,k,p))
def erase(n,k):
    if n is None:raise KeyError(k)
    if k==n.k:return merge(n.l,n.r)
    if k<n.k:return node(n.k,n.p,erase(n.l,k),n.r)
    return node(n.k,n.p,n.l,erase(n.r,k))
def events(n):
    return events(n.l)+[(n.k[1],n.k[2])] +events(n.r) if n else []
def nominal(n,a,j,x,z,nxt,stat):
    if n is None:return None
    stat['nominal_nodes']+=1
    lo,hi=fr((j+z)*a-x),fr((j+nxt)*a-x)
    if lo<hi:
        if n.hi<lo or n.lo>=hi:return None
        if lo<=n.lo and n.hi<hi:return n.thi
    else:
        if hi<=n.lo and n.hi<lo:return None
        if n.hi<hi or n.lo>=lo:return n.thi
    v=[nominal(n.l,a,j,x,z,nxt,stat),nominal(n.r,a,j,x,z,nxt,stat)]
    inside=(lo<=n.k[0]<hi) if lo<hi else (n.k[0]>=lo or n.k[0]<hi)
    if inside:v.append(n.k[1])
    return max((w for w in v if w is not None),default=None)
def exclusion(n,a,L,U,j,x,z,nxt,stat):
    stat['subtree_checks']+=1
    ds=(L-a,U-a)
    ts=[t*d for t in (n.tlo,n.thi) for d in ds]
    sl,sh=n.lo+min(ts),n.hi+max(ts)
    ql=fr((j+z)*a-x);qh=fr((j+nxt)*a-x)
    if qh<=ql:qh+=1
    as_=[ql+(j+z)*d for d in ds]
    cs_=[qh+(j+nxt)*d for d in ds]
    if any(not 0<c-b<1 for b,c in zip(as_,cs_)):return False
    return ce(sl-max(cs_))>floor(sh-min(as_))
class Cache:
    def __init__(self):self.data={}
    def excluded(self,n,a,L,U,j,x,m,z,nxt,stat):
        # Node object is held strongly by dict: its identity and all immutable extrema survive.
        signature=(a,j,x,m,z,nxt)
        key=(n,signature)
        for l,u in self.data.get(key,()):
            if l<=L<=U<=u:
                stat['cache_hits']+=1;stat['saved_events']+=n.count;return True
        v=exclusion(n,a,L,U,j,x,z,nxt,stat)
        if v:self.data.setdefault(key,[]).append((L,U))
        return v
def certify(root,a,L,U,m,j,x,z,stat,cache=None):
    if not L<=a<=U:return 'INCONCLUSIVE',None
    h=history(a,m);labs=[z for _,z in h]
    if not all(avoid(F(0),F(v-w),L,U) for v,w in zip(labs,labs[1:]+labs[:1])):
        return 'INCONCLUSIVE',None
    nxt=labs[(labs.index(z)+1)%m]
    w=nominal(root,a,j,x,z,nxt,stat)
    if w is not None:
        stat['winner_boundary_tests']+=2
        if not all(avoid(x,F(w-j-v),L,U) for v in (z,nxt)):
            return 'INCONCLUSIVE',w
    def walk(n):
        if n is None:return True
        stat['walk_nodes']+=1
        if w is not None and n.thi<=w:
            stat['time_prunes']+=1;return True
        exclude=(cache.excluded(n,a,L,U,j,x,m,z,nxt,stat) if cache is not None
                 else exclusion(n,a,L,U,j,x,z,nxt,stat))
        if exclude:
            stat['subtree_prunes']+=1;stat['subtree_events']+=n.count;return True
        if not walk(n.l):return False
        if w is None or n.k[1]>w:
            stat['leaf_boundary_tests']+=2
            # A local boundary equality remains INCONCLUSIVE, even at a single endpoint.
            if not all(avoid(x,F(n.k[1]-j-v),L,U) for v in (z,nxt)):
                return False
        return walk(n.r)
    return ('CERTIFIED' if walk(root) else 'INCONCLUSIVE'),w
def oracle(th,ev,m,j,x,z):
    h=history(th,m);ps=[p for p,_ in h];zs=[v for _,v in h]
    return max((t for t,b in ev if zs[bisect_right(ps,fr(x+(t-j)*th))-1]==z),default=None)
def run():
    rng=Random(20261111); cache=Cache();base=Counter();reuse=Counter()
    tests=passes=changes=0; builds=0; build_s=plain_s=cache_s=oracle_s=0.0; max_time_bits=0; max_den_bits=0
    cross_version_hits=0
    extra=Counter(); version_savings=[]
    for case in range(120):
        denom=rng.choice((101,103,107,109,113,127));a=F(rng.randrange(2,denom-2),denom)
        m=rng.randrange(2,10);j=rng.randrange(50,120);x=F(rng.randrange(1,29),rng.randrange(31,67))
        root=None;old=None;ev=[];prior=set()
        st=perf_counter()
        for i in range(35):
            t=rng.randrange(-70,j);b=i%7
            if (t,b) in prior:continue
            prior.add((t,b));ev.append((t,b));root=add(root,(fr(t*a),t,b),rng.getrandbits(96));builds+=1
            max_time_bits=max(max_time_bits,abs(t).bit_length())
        old=root;old_ev=list(ev)
        # Force independent branches at the same time and a divergent later version.
        t=old_ev[0][0];b=10000+case
        if (t,b) not in prior:
            root=add(root,(fr(t*a),t,b),rng.getrandbits(96));ev.append((t,b));builds+=1
        changed=root; changed_ev=list(ev)
        assert (t,b) in events(changed) and old_ev[0] in events(changed)
        root=erase(root,(fr(t*a),t,b));assert events(root)==sorted(old_ev,key=lambda e:(fr(e[0]*a),e[0],e[1]))
        assert (t,b) not in events(root) and old_ev[0] in events(root)
        build_s+=perf_counter()-st
        # Stable-root and old-root queries; shared persistent subtrees reuse their proof.
        for version_number,(version,active) in enumerate(((old,old_ev),(changed,changed_ev),(root,old_ev))):
            hits_before=reuse['cache_hits']
            z=rng.randrange(m)
            eps=F(1,10**7); L=max(F(1,10**10),a-eps);U=min(F(1)-F(1,10**10),a+eps)
            for depth in range(5):
                low=a+(L-a)/2**depth;high=a+(U-a)/2**depth
                max_den_bits=max(max_den_bits,low.denominator.bit_length(),high.denominator.bit_length())
                # Same input, same output: exact matched cached / uncached baselines.
                s=perf_counter();p,v=certify(version,a,low,high,m,j,x,z,base);plain_s+=perf_counter()-s
                before_hits=reuse['cache_hits']
                s=perf_counter();c,w=certify(version,a,low,high,m,j,x,z,reuse,cache);cache_s+=perf_counter()-s
                if version_number>0 and depth==0:cross_version_hits+=reuse['cache_hits']-before_hits
                assert (p,v)==(c,w),(case,depth,p,v,c,w)
                tests+=1
                if c=='CERTIFIED':
                    passes+=1
                    s=perf_counter()
                    for th in (low,(low+high)/2,high):assert oracle(th,active,m,j,x,z)==w
                    oracle_s+=perf_counter()-s
            # Same root, altered observation: cache signature must be disjoint.
            version_savings.append({'version':version_number,'hits':reuse['cache_hits']-hits_before})
            other=x+F(case*2+version_number+1,1000003)
            # A previously unseen observation must begin without a cache hit.
            assert not any(sig[1]==j and sig[2]==other and sig[3]==m and sig[4]==z for node,sig in cache.data)
            before=extra['cache_hits']
            q,w=certify(version,a,L,U,m,j,other,z,extra,cache)
            assert extra['cache_hits']==before
            changes+=1
    # Explicit exact boundary-root case: cannot certify whole interval across a changed winner.
    a=F(1,30);U=F(1003,30000);j=10000;x=F(8,15);m=13;z=12
    witness=[(9,0),(15,0),(6042,0)];wroot=None
    for i,(t,b) in enumerate(witness):wroot=add(wroot,(fr(t*a),t,b),100-i)
    assert oracle(a,witness,m,j,x,z)==6042 and oracle(U,witness,m,j,x,z)==15
    v,w=certify(wroot,a,a,U,m,j,x,z,extra,cache)
    assert v=='INCONCLUSIVE'
    # Exact collision root: endpoint boundary equality is treated as an interval failure.
    assert not avoid(F(0),F(4),F(1,4),F(1,4))
    # A large-time regime: keep all phase, interval and winner arithmetic exact.
    bigbase=10**18;ta=F(23,101);tm=17;tj=bigbase+1000;tx=F(7,19)
    broot=None;bev=[]
    for i in range(100):
        t=bigbase+i-80;b=i%4;bev.append((t,b));broot=add(broot,(fr(t*ta),t,b),rng.getrandbits(96))
    bL=ta-F(1,10**24);bU=ta+F(1,10**24);bigvalid=0;bigintervals=0
    for label in range(17):
        for d in range(3):
            L=ta+(bL-ta)/2**d;U=ta+(bU-ta)/2**d
            p,v=certify(broot,ta,L,U,tm,tj,tx,label,base)
            c,w=certify(broot,ta,L,U,tm,tj,tx,label,reuse,cache)
            assert (p,v)==(c,w)
            bigintervals+=1
            if c=='CERTIFIED':
                bigvalid+=1
                for th in (L,(L+U)/2,U):assert oracle(th,bev,tm,tj,tx,label)==w
    # Frozen S23/AV sparse labels, no science re-pin or full risk recomputation.
    fp=262204504569236716045286;fq=10**24;fa=F(fp,fq);fm=128;fj=226;fx=F(0)
    froot=None;fev=[(t,0) for t in range(1,226)]
    for i,(t,b) in enumerate(fev):froot=add(froot,(fr(t*fa),t,b),rng.getrandbits(96))
    fverified=0
    for label in (0,31,63,127):
        for scale in (0,1,2):
            e=F(1,10**(12+scale));L=fa-e;U=fa+e
            p,v=certify(froot,fa,L,U,fm,fj,fx,label,base)
            c,w=certify(froot,fa,L,U,fm,fj,fx,label,reuse,cache)
            assert (p,v)==(c,w)
            if c=='CERTIFIED':
                fverified+=1
                for th in (L,(L+U)/2,U):assert oracle(th,fev,fm,fj,fx,label)==w
    max_time_bits=max(max_time_bits,bigbase.bit_length())
    max_den_bits=max(max_den_bits,bL.denominator.bit_length(),(fa+F(1,10**14)).denominator.bit_length())
    result={'science_pin':PIN,'cases':120,'matched_interval_queries':tests,'certified_queries':passes,
            'old_root_observation_checks':changes,'cross_version_hits_on_first_interval':cross_version_hits,
            'baseline':dict(base),'cached':dict(reuse),
            'extra_observation_checks':dict(extra),'large_time':{'intervals':bigintervals,'certified':bigvalid},
            'frozen_s23':{'intervals':12,'certified':fverified},
            'version_hits':version_savings,
            'build_inserts':builds,'maximum_time_bits':max_time_bits,
            'maximum_parameter_denominator_bits':max_den_bits,
            'wall_seconds':{'build':round(build_s,6),'uncached':round(plain_s,6),
                            'cached':round(cache_s,6),'oracle_validation':round(oracle_s,6)},
            'cache_entries':sum(map(len,cache.data.values())),
            'r64_winner_change_detected':True,'integer_collision_boundary_checked':True}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
    return result
if __name__=='__main__':run()
