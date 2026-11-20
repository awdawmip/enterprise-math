"""Stage475-B exact positive BRC: fixed k=3, ternary native X6 originals, t>=m-1.
Enumerates raw histories only in short test fibers; large cases use integer DP.
Future APPEND semantics (all 12 signed directions) are handled by the Stage474
repair theorem, currently awaiting independent project review.
"""
from collections import defaultdict, Counter
from functools import lru_cache
from itertools import product
from hashlib import sha256
import json
D=(0,1,2); A=0; Z=(0,)*9
def ix(x,y): return 3*x+y
def edges(w):
    out=list(Z)
    for a,b in zip(w,w[1:]): out[ix(a,b)]+=1
    return tuple(out)
def add(e,a,b):
    v=list(e); v[ix(a,b)]+=1
    return tuple(v)
def fits(a,b): return all(x<=y for x,y in zip(a,b))
def diff(a,b): return tuple(x-y for x,y in zip(a,b)) if fits(b,a) else None
def observer(p,q):
    return len(p),len(q),edges(p),edges(q),sum(a==b for a,b in zip(p,q))
def last(e):
    f=[sum(e[ix(a,b)] for b in D)-sum(e[ix(b,a)] for b in D) for a in D]
    cs=[c for c in D if all(f[a]==int(a==A)-int(a==c) for a in D)]
    assert len(cs)==1
    return cs[0]
def tags(m,n,t):
    return (m-3,m-2,m-1),tuple(j for j in range(m-2,min(n,m+3)+1) if j<t)
def repair_key(p,q,t):
    m,n=len(p),len(q); pt,qt=tags(m,n,t)
    return tuple(p[j-1] for j in pt)+tuple(q[j-1] for j in qt)+tuple(q[t-1:])
def solve(phi,t,probes=()):
    m,n,EP,EQ,K=phi
    assert 4<=m<n and m-1<=t<=n
    Pm=last(EP); pt,qt=tags(m,n,t)
    root=(A,A,Z,Z,1,tuple(A if j==1 else -1 for j in pt),tuple(A if j==1 else -1 for j in qt))
    pre={root:1}
    for j in range(2,t+1):
        nxt=defaultdict(int)
        pvals=(Pm,) if j==m else D if j<m else (None,)
        for (lp,lq,pe,qe,k,pp,qq),mass in pre.items():
            for p in pvals:
                px=add(pe,lp,p) if p is not None else pe
                if not fits(px,EP): continue
                for q in D:
                    qx=add(qe,lq,q)
                    if not fits(qx,EQ): continue
                    kk=k+(int(p==q) if p is not None else 0)
                    if kk>K: continue
                    np=tuple(p if pos==j else z for pos,z in zip(pt,pp))
                    nq=tuple(q if pos==j else z for pos,z in zip(qt,qq))
                    nxt[(p if p is not None else lp,q,px,qx,kk,np,nq)]+=mass
        pre=dict(nxt)
    hidden=defaultdict(list)
    for (lp,lq,pe,qe,k,pp,qq),mass in pre.items():
        if t==m-1: pe=add(pe,lp,Pm)
        if pe!=EP: continue
        assert -1 not in pp and -1 not in qq
        hidden[pp+qq+(lq,)].append((qe,k,mass))
    heads=sorted(hidden)
    @lru_cache(None)
    def terminal(head,used,extra):
        need=diff(EQ,used)
        if need is None: return 0
        return sum(mass for qe,k,mass in hidden[head] if qe==need and k+extra==K)
    @lru_cache(None)
    def suffix(head,j,prev,used,extra):
        if j==n:
            w=terminal(head,used,extra)
            return int(w>0),w
        total=pop=0
        for q in D:
            qe=add(used,prev,q)
            if not fits(qe,EQ): continue
            ke=extra+(int(Pm==q) if t==m-1 and j+1==m else 0)
            if ke>K: continue
            a,b=suffix(head,j+1,q,qe,ke)
            total+=a; pop+=b
        return total,pop
    roots={h:(h,t,h[-1],Z,0) for h in heads}
    totals={h:suffix(*st) for h,st in roots.items()}
    support=sum(a for a,b in totals.values())
    population=sum(b for a,b in totals.values())
    def step(st,q):
        h,j,prev,used,extra=st
        used=add(used,prev,q)
        if not fits(used,EQ): return None
        extra+=int(Pm==q) if t==m-1 and j+1==m else 0
        return (h,j+1,q,used,extra) if extra<=K else None
    def unrank(rank):
        if not 0<=rank<support: raise IndexError(rank)
        for h in heads:
            if rank<totals[h][0]: break
            rank-=totals[h][0]
        st=roots[h]; seq=list(h)
        while st[1]<n:
            for q in D:
                next_st=step(st,q)
                if next_st is None: continue
                a=suffix(*next_st)[0]
                if rank>=a: rank-=a
                else: st=next_st; seq.append(q); break
            else: raise AssertionError('unrank')
        assert rank==0
        return tuple(seq)
    def rankmass(key):
        headsize=len(pt)+len(qt)+1
        if len(key)!=headsize+n-t: return None
        head=tuple(key[:headsize])
        if head not in roots: return None
        rank=sum(totals[h][0] for h in heads if h<head)
        st=roots[head]
        for q in key[headsize:]:
            if q not in D: return None
            for x in D:
                if x>=q: break
                next_st=step(st,x)
                if next_st: rank+=suffix(*next_st)[0]
            st=step(st,q)
            if st is None: return None
        a,mass=suffix(*st)
        return (rank,mass) if a else None
    checks=[]
    for r in probes:
        if 0<=r<support:
            k=unrank(r); z=rankmass(k)
            assert z and z[0]==r and z[1]>0
            checks.append({"rank":r,"mass":z[1],"key_sha256":sha256(repr(k).encode()).hexdigest()})
    return {"support":support,"population":population,"prefix_states":len(pre),
            "heads":len(heads),"suffix_states":suffix.cache_info().currsize,
            "terminals":terminal.cache_info().currsize,"probes":checks,
            "_rankmass":rankmass,"_unrank":unrank}
def small_checks():
    cfg=[(4,5,3,60),(4,5,4,60),(4,5,5,60),
         (4,6,3,50),(4,6,4,50),(4,6,5,50),(4,6,6,50),
         (5,6,4,35),(5,6,5,35),(5,6,6,35),
         (5,7,4,25),(5,7,5,25),(5,7,6,25),(5,7,7,25)]
    cache={}; stats=Counter()
    for m,n,t,lim in cfg:
        if (m,n) not in cache:
            f=defaultdict(list)
            for pp in product(D,repeat=m-1):
                p=(A,)+pp
                for qq in product(D,repeat=n-1):
                    q=(A,)+qq
                    f[observer(p,q)].append((p,q))
            cache[m,n]=f
        for phi,hist in sorted(cache[m,n].items(),key=lambda v:(-len(v[1]),repr(v[0])))[:lim]:
            expected=Counter(repair_key(p,q,t) for p,q in hist)
            z=solve(phi,t)
            assert z['support']==len(expected) and z['population']==len(hist)
            for r,(k,mass) in enumerate(sorted(expected.items())):
                assert z['_rankmass'](k)==(r,mass)
                assert z['_unrank'](r)==k
                stats['classes']+=1
            stats['fibers']+=1; stats['cached_suffix_states']+=z['suffix_states']
        stats['configs']+=1
    return dict(stats)
def big_checks():
    m,n=35,56; p=(A,)*m; q=(A,)
    for v in (1,)*14+(2,)*12: q+=(v,A)
    q+=(A,)*3
    phi=observer(p,q)
    assert phi[-1]==18
    out=[]
    for t in (34,35,36,37,38,39,40,41,56):
        z=solve(phi,t,probes=(0,1,10,100,1000))
        assert z['population']==11154643500
        out.append({'t':t,**{x:y for x,y in z.items() if not x.startswith('_')}})
    assert all(out[j]['support']>=out[j+1]['support'] for j in range(len(out)-1))
    return out
def plateau_end_witness():
    p=(A,)*35; q=[A]*56
    for j in range(2,29,2): q[j-1]=1
    for j in (30,32,34,36,39,42,44,46,48,50,52,54): q[j-1]=2
    r=q.copy(); r[19],r[38]=r[38],r[19]
    q=tuple(q); r=tuple(r)
    assert observer(p,q)==observer(p,r)
    assert repair_key(p,q,40)==repair_key(p,r,40)
    assert repair_key(p,q,39)!=repair_key(p,r,39)
    assert q[38]!=r[38]
    return {'swap':[20,39],'same_initial':True,'equal_t40':True,
            'different_t39':True,'Q_POP_to_length_39':17}
if __name__=='__main__':
    data={'stage':'475-B','scope':'k=3,t>=m-1,integer positive BRC',
          'small':small_checks(),'big':big_checks(),
          'strict_witness':plateau_end_witness(),'assertions_passed':True}
    with open('STAGE475B_GITHUB_EXECUTED.json','w') as f:json.dump(data,f,indent=2)
    print(json.dumps({'small':data['small'],'big_support':[(x['t'],x['support']) for x in data['big']],
                      'strict_witness':data['strict_witness']},indent=2))
