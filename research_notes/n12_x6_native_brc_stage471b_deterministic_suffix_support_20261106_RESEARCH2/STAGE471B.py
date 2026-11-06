"""Stage471-B: deterministic positive BRC support/mass and rank/unrank for t<=m-2.
Scientific pins in PROOF_STAGE471B.md. Python3 standard library only.
Original alphabet A=+E1 B=+E2 C=+E3, future APPEND all 12 signed X6,
with Stage469-B repair used as the proven semantic relation. No external libs.
"""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import product
from math import comb
import json

ABC=tuple(range(3)); A,B,C=ABC
ZERO=(0,)*9

def eidx(x,y):return 3*x+y

def edgecounts(w):
    c=[0]*9
    for x,y in zip(w,w[1:]): c[eidx(x,y)]+=1
    return tuple(c)

def full_observer(p,q):
    def one(w):
        disp=[0]*6; adj=[0]*144
        for v in w:disp[v]+=1
        for a,b in zip(w,w[1:]): adj[12*(2*a)+2*b]+=1
        return (len(w),tuple(disp),tuple(adj))
    return one(p),one(q),sum(a==b for a,b in zip(p,q))

def from_observer(phi):
    po,qo,k=phi; m,n=po[0],qo[0]
    assert 4<=m<n and 1<=k<=m
    ep=tuple(po[2][12*(2*a)+2*b] for a in ABC for b in ABC)
    eq=tuple(qo[2][12*(2*a)+2*b] for a in ABC for b in ABC)
    assert sum(ep)==m-1 and sum(eq)==n-1
    for ob,ev in [(po,ep),(qo,eq)]:
        assert sum(ob[2])==sum(ev)
        counts=tuple((i==A)+sum(ev[eidx(j,i)] for j in ABC) for i in ABC)
        assert ob[1] == counts+(0,0,0)
    return m,n,k,ep,eq

def minus(base, used):
    if any(x<y for x,y in zip(base,used)):return None
    return tuple(x-y for x,y in zip(base,used))

def add_edge(vec,x,y):
    c=list(vec);c[eidx(x,y)]+=1;return tuple(c)

def count_for_fiber(phi,t,rank_probes=()):
    """Integer-support DP; returns qF and sum of raw masses without listing all keys.
    The repair word order is Q_t,(P_{t+1},Q_{t+1}),...,(P_m,Q_m),Q_{m+1},...,Q_n.
    Stage469's P_{m-1},Q_m,Q_{m+1} tags are already contained when 1<=t<=m-2.
    """
    m,n,K,ep,eq=from_observer(phi)
    assert 1<=t<=m-2
    # Prefix histories: exact positive BRC mass, with both words starting at A.
    pre={(A,A,ZERO,ZERO,1):1}
    for pos in range(2,t+1):
        nxt=defaultdict(int)
        for (lp,lq,pe,qe,kp),mass in pre.items():
            for p in ABC:
                pe1=add_edge(pe,lp,p)
                if minus(ep,pe1) is None:continue
                for q in ABC:
                    qe1=add_edge(qe,lq,q)
                    if minus(eq,qe1) is None:continue
                    kk=kp+int(p==q)
                    if kk<=K:nxt[(p,q,pe1,qe1,kk)]+=mass
        pre=dict(nxt)
    # Terminal acceptance depends only on the visible tail's compact edge profile,
    # FIRST visible P symbol, Q_t, and tail match count; never on the suffix order.
    prefix_by_q=defaultdict(list)
    for (lp,lq,pe,qe,kp),mass in pre.items():
        prefix_by_q[lq].append((lp,pe,qe,kp,mass))
    boundary_cache={}
    def terminal(qt,pfirst,pevis,qevis,kv):
        key=(qt,pfirst,pevis,qevis,kv)
        if key in boundary_cache:return boundary_cache[key]
        remq=minus(eq,qevis)
        if remq is None:return 0
        remp=minus(ep,pevis)
        if remp is None:return 0
        acc=0
        for lp,pe0,qe0,kp,mass in prefix_by_q[qt]:
            if qe0!=remq or kp+kv!=K:continue
            # Internal P-tail edges are counted, but the P_t -> P_(t+1)
            # boundary step belongs to neither original segment.
            e=eidx(lp,pfirst)
            if all(pe0[i]+(i==e)==remp[i] for i in range(9)):
                acc+=mass
        boundary_cache[key]=acc
        return acc
    states=[0]
    # Recursion counts *distinct* visible repair words (not prefix multiplicities).
    @lru_cache(None)
    def suffix(j,qt,qp,pfirst,plast,pevis,qevis,kv):
        states[0]+=1
        if j==n:
            v=terminal(qt,pfirst,pevis,qevis,kv)
            return (int(v>0),v)
        nextj=j+1
        support=mass_sum=0
        for p,q in options(nextj):
            if j==t:
                npfirst=p; np=p; npep=pevis
            elif nextj<=m:
                npfirst=pfirst;np=p;npep=add_edge(pevis,plast,p)
            else:
                npfirst=pfirst;np=plast;npep=pevis
            nqe=add_edge(qevis,qp,q)
            nkv=kv+int(p==q) if p is not None else kv
            if nkv>K or minus(ep,npep) is None or minus(eq,nqe) is None:continue
            a,b=suffix(nextj,qt,q,npfirst,np,npep,nqe,nkv)
            support+=a;mass_sum+=b
        return support,mass_sum
    @lru_cache(None)
    def options(j):
        return tuple(product(ABC,ABC)) if j<=m else tuple((None,q) for q in ABC)
    startstates=[]
    for qt in ABC:
        startstates.append((t,qt,qt,-1,-1,ZERO,ZERO,0))
    subtotals=[suffix(*s) for s in startstates]
    qF=sum(a for a,_ in subtotals)
    population=sum(b for _,b in subtotals)
    def step(state,choice):
        j,qt,qp,pfirst,plast,pevis,qevis,kv=state
        p,q=choice; nextj=j+1
        if j==t:npfirst=p;np=p;npep=pevis
        elif nextj<=m:npfirst=pfirst;np=p;npep=add_edge(pevis,plast,p)
        else:npfirst=pfirst;np=plast;npep=pevis
        nqe=add_edge(qevis,qp,q)
        nkv=kv+(int(p==q) if p is not None else 0)
        if nkv>K or minus(ep,npep) is None or minus(eq,nqe) is None:return None
        return (nextj,qt,q,npfirst,np,npep,nqe,nkv)
    def evaluate_key(key):
        """key=(q_t,(p_(t+1),q_(t+1)),...,(p_m,q_m),q_(m+1),...,q_n)
        The rank is zero-based, over lexicographic raw-symbol tuples.
        """
        qt=key[0];state=startstates[qt];r=sum(subtotals[z][0] for z in ABC if z<qt)
        for j in range(t+1,n+1):
            want=key[j-t]
            opts=options(j)
            if j>m:want=(None,want)
            if want not in opts:return None
            for op in opts:
                if op>=want:break
                ns=step(state,op)
                if ns is not None:r+=suffix(*ns)[0]
            state=step(state,want)
            if state is None:return None
        support,mass=suffix(*state)
        return {'rank':r,'mass':mass} if support else None
    def unrank(r):
        if not 0<=r<qF:raise IndexError(r)
        key=[]
        for qt,st in enumerate(startstates):
            c=suffix(*st)[0]
            if r<c:
                key=[qt]; state=st;break
            r-=c
        for j in range(t+1,n+1):
            for op in options(j):
                ns=step(state,op)
                cnt=suffix(*ns)[0] if ns is not None else 0
                if r>=cnt:r-=cnt
                else:
                    key.append(op if j<=m else op[1]);state=ns;break
            else:raise AssertionError('no unrank branch')
        assert r==0
        return tuple(key)
    probes=[]
    for idx in rank_probes:
        if 0<=idx<qF:
            key=unrank(idx);chk=evaluate_key(key)
            assert chk is not None and chk['rank']==idx and chk['mass']>0
            probes.append({'rank':idx,'key':key,'mass':chk['mass']})
    return {'support':qF,'population':population,
            'prefix_states':len(pre),'suffix_states':suffix.cache_info().currsize,
            'terminal_profiles':len(boundary_cache),
            'rank_probes':probes,
            'evaluate_key':evaluate_key, 'unrank':unrank}

def repair(p,q,t):
    m,n=len(p),len(q)
    return (q[t-1],)+tuple((p[j-1],q[j-1]) for j in range(t+1,m+1))+tuple(q[j-1] for j in range(m+1,n+1))

def test_cases():
    stats=Counter(); examples=[]
    for m,n,t,cap in [(4,5,1,100),(4,5,2,100),(4,6,1,80),(4,6,2,80),
                      (5,6,1,50),(5,6,2,50),(5,6,3,50),(6,7,4,30)]:
        fibers=defaultdict(Counter)
        for ps in product(ABC,repeat=m-1):
            p=(A,)+ps
            for qs in product(ABC,repeat=n-1):
                q=(A,)+qs
                fibers[full_observer(p,q)][repair(p,q,t)]+=1
        # Order deterministically to cover nontrivial fibers first, and some singleton fibers.
        chosen=sorted(fibers.items(),key=lambda x:(-max(x[1].values()),-len(x[1]),-sum(x[1].values()),repr(x[0])))[:cap]
        for phi,actual in chosen:
            calculated=count_for_fiber(phi,t,rank_probes=(0,1,len(actual)//2,len(actual)-1))
            ordered=sorted(actual)
            assert calculated['support']==len(actual),(m,n,t,actual,calculated)
            assert calculated['population']==sum(actual.values())
            for idx,key in enumerate(ordered):
                obj=calculated['evaluate_key'](key)
                assert obj=={'rank':idx,'mass':actual[key]}
                assert calculated['unrank'](idx)==key
                stats['checked_classes']+=1
            stats['prefix_states']+=calculated['prefix_states']
            stats['suffix_states']+=calculated['suffix_states']
            stats['checked_fibers']+=1
            stats['max_class_mass']=max(stats['max_class_mass'],max(actual.values()))
            if len(actual)>1 and len(examples)<4:
                examples.append({'m':m,'n':n,'t':t,'K':phi[2],
                                 'P_edges':edge_snapshot(phi[0]),'Q_edges':edge_snapshot(phi[1]),
                                 'classes':len(actual),'population':sum(actual.values())})
        stats['configs']+=1
    return dict(stats),examples

def edge_snapshot(ob):return {f'{ABC[a]}{ABC[b]}':ob[2][12*2*a+2*b] for a in ABC for b in ABC if ob[2][12*2*a+2*b]}

def large_case():
    # Same complete full-observer fiber as Stage470, now Q may POP 48 steps,
    # so t=8 and the visible original Q suffix is 49 steps long.
    k,b,loops,m,t=26,14,3,35,8
    q=[A]
    for ix in range(k):q.extend([B if ix<b else C,A])
    q.extend([A]*loops)
    p=[A]*m
    phi=full_observer(tuple(p),tuple(q))
    s=count_for_fiber(phi,t,rank_probes=(0,1,2,100,1000))
    from hashlib import sha256
    result={k:v for k,v in s.items() if k not in ('evaluate_key','unrank')}
    result['rank_probes']=[{'rank':p['rank'],'mass':p['mass'],
          'key_sha256':sha256(repr(p['key']).encode()).hexdigest()} for p in s['rank_probes']]
    return result

if __name__=='__main__':
    small,ex=test_cases()
    big=large_case()
    assert big['population']==11154643500
    result={'stage':'471-B','domain':'P/Q original +E1/+E2/+E3, first A; 1<=t=n-h<=m-2, 4<=m<n, all signed X6 future appends; Stage469-B repair',
            'small_exhaustive':small,'witness_fibers':ex,'large_full_fiber':big,
            'all_assertions_passed':True}
    with open('/mnt/data/stage471b/STAGE471B_EXECUTED.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps(result,ensure_ascii=False,indent=2))
