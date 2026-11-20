#!/usr/bin/env python3
"""Stage461-B: two POP each; one P APPEND, optionally one Q APPEND.
Exact natural-number BRC support and masses, plus independent labeled full-future observer checks.
"""
from __future__ import annotations
from collections import defaultdict
from itertools import combinations
import json, sys, hashlib
from functools import lru_cache

A,B=0,1
DIRECTIONS=tuple(range(12))

def words(n):
    # 0=+e1, 1=-e1, and all B are nonadjacent and interior.
    out=[]
    for k in range((n-1)//2+1):
        for pos in combinations(range(1,n-1),k):
            if any(v-u==1 for u,v in zip(pos,pos[1:])):continue
            t=[A]*n
            for p in pos:t[p]=B
            out.append(tuple(t))
    return out

def deficiency(t):return t.count(B)
def mismatch(p,q):return sum(a!=b for a,b in zip(p,q))

def repair_positions(m,n):
    # zero-based coordinate indices; fixed first/last A allowed, dropped from variable key.
    ip=sorted(set((m-3,m-2)).intersection(range(1,m-1)))
    iq=sorted(set((m-2,m-1,m,n-3,n-2)).intersection(range(1,n-1)))
    return tuple(('P',i) for i in ip)+tuple(('Q',i) for i in iq)

def repair(p,q,positions):return tuple((p if src=='P' else q)[i] for src,i in positions)

def obs(p,q):
    # six signed endpoint coordinates and full 12x12 directed adjacency, represented sparsely without information loss.
    def src(w):
        endpoint=[0]*6
        edges=defaultdict(int)
        for s in w: endpoint[s//2]+=1 if s%2==0 else -1
        for i in range(1,len(w)):edges[(w[i-1],w[i])]+=1
        return (len(w),tuple(endpoint),tuple(sorted(edges.items())))
    return (src(p),src(q),sum(a==b for a,b in zip(p,q)))

class FutureOracle:
    def __init__(self,rp,rq):
        self.rp,self.rq=rp,rq
        self.intern={}
        self.cache={}
    def sig(self,p,q,bp=2,bq=2,ap=None,aq=None):
        if ap is None:ap=self.rp
        if aq is None:aq=self.rq
        k=(p,q,bp,bq,ap,aq)
        if k in self.cache:return self.cache[k]
        children=[]
        if bp and p:children.append(('POP_P',self.sig(p[:-1],q,bp-1,bq,ap,aq)))
        if bq and q:children.append(('POP_Q',self.sig(p,q[:-1],bp,bq-1,ap,aq)))
        if ap:
            for u in DIRECTIONS:children.append((('APPEND_P',u),self.sig(p+(u,),q,bp,bq,ap-1,aq)))
        if aq:
            for u in DIRECTIONS:children.append((('APPEND_Q',u),self.sig(p,q+(u,),bp,bq,ap,aq-1)))
        signature=(obs(p,q),tuple(children))
        idx=self.intern.get(signature)
        if idx is None:
            idx=len(self.intern)+1
            self.intern[signature]=idx
        self.cache[k]=idx
        return idx

def dp_mass(m,n,kp,kq,d,coordinates,key):
    fixed=dict(zip(coordinates,key))
    states={(0,0,0,-1,-1):1}
    for i in range(n):
        new=defaultdict(int)
        por=(0,) if i==0 or i==m-1 else (0,1)
        qor=(0,) if i==0 or i==n-1 else (0,1)
        if i>=m:por=(None,)
        if ('P',i) in fixed:por=(fixed['P',i],)
        if ('Q',i) in fixed:qor=(fixed['Q',i],)
        for (cp,cq,mm,pp,pq),val in states.items():
            for x in por:
                if x is not None and (cp+(x==1)>kp or pp==1 and x==1):continue
                for y in qor:
                    if cq+(y==1)>kq or pq==1 and y==1:continue
                    mm2=mm+(x!=y if x is not None else 0)
                    if mm2>d:continue
                    new[(cp+(x==1 if x is not None else 0),cq+(y==1),mm2,pp if x is None else x,y)]+=val
        states=new
        if not states:break
    return sum(v for (cp,cq,mm,_,_),v in states.items() if (cp,cq,mm)==(kp,kq,d))

def grouped(m,n,kp,kq,d):
    """Return exact BRC population/support oracle and rank/unrank, no raw or key roster."""
    coords=repair_positions(m,n)
    s=len(coords)

    @lru_cache(maxsize=None)
    def subtree(prefix):
        if len(prefix)==s:
            mass=dp_mass(m,n,kp,kq,d,coords,prefix)
            return (int(mass>0),mass)
        q0,m0=subtree(prefix+(0,))
        q1,m1=subtree(prefix+(1,))
        return q0+q1,m0+m1

    q,mass=subtree(())
    def population(key):
        if len(key)!=s or any(bit not in (0,1) for bit in key):raise ValueError('invalid key')
        return subtree(tuple(key))[1]
    def rank(key):
        key=tuple(key)
        if not population(key):raise ValueError('unsupported key')
        i=0;prefix=()
        for bit in key:
            if bit==1:i+=subtree(prefix+(0,))[0]
            prefix+=(bit,)
        return i
    def unrank(index):
        if not 0<=index<q:raise ValueError('rank out of bounds')
        prefix=()
        for j in range(s):
            left=subtree(prefix+(0,))[0]
            if index<left:prefix+=(0,)
            else:index-=left;prefix+=(1,)
        if index!=0 or population(prefix)==0:raise AssertionError('incorrect support rank')
        return prefix
    return {'q':q,'mass':mass,'positions':coords,'population':population,'rank':rank,'unrank':unrank,
            'cached_subtrees':subtree.cache_info().currsize}

def exhaustive(m,n,kmax=2,rp=1,rq=0):
    os={t:obs(t,()) for t in []}
    P=[w for w in words(m) if deficiency(w)<=kmax]
    Q=[w for w in words(n) if deficiency(w)<=kmax]
    fibers=defaultdict(list)
    for p in P:
        for q in Q:
            d=mismatch(p,q)
            fibers[(deficiency(p),deficiency(q),d)].append((p,q))
    oracle=FutureOracle(rp,rq)
    report={'m':m,'n':n,'rp':rp,'rq':rq,'fibers':0,'history_pairs':0,'class_checks':0,'future_pairs':0,'future_states':0,'distinct_future_trees':0,'first_error':None}
    for (kp,kq,d),histories in fibers.items():
        report['fibers']+=1
        report['history_pairs']+=len(histories)
        group=grouped(m,n,kp,kq,d)
        by_key=defaultdict(list);by_sig=defaultdict(set)
        for p,q in histories:
            r=repair(p,q,group['positions'])
            by_key[r].append((p,q))
            by_sig[oracle.sig(p,q)].add(r)
        explicit={k:len(v) for k,v in by_key.items()}
        if any(group['population'](k)!=v for k,v in explicit.items()) or len(by_sig)!=group['q'] or group['mass']!=len(histories) or any(len(v)!=1 for v in by_sig.values()):
            report['first_error']={'kp':kp,'kq':kq,'d':d,'keys':len(by_key),'sig':len(by_sig),'dp':group['q'],'population_ok':all(group['population'](k)==v for k,v in explicit.items()), 'sig_repair_sets':{str(k):[str(x) for x in v] for k,v in by_sig.items() if len(v)!=1}}
            raise AssertionError(report['first_error'])
        # Ensure each key yields one identical future signature (could multiple histories in same key).
        for key,raw in by_key.items():
            sigs={oracle.sig(*t) for t in raw}
            if len(sigs)!=1:raise AssertionError(('repair conflates distinct future',m,n,kp,kq,d,key,raw))
        for i,key in enumerate(sorted(by_key)):
            assert group['rank'](key)==i and group['unrank'](i)==key
        report['class_checks']+=len(by_key)
        report['future_pairs']+=len(histories)*(len(histories)-1)//2
    report['future_states']=len(oracle.cache)
    report['distinct_future_trees']=len(oracle.intern)
    return report

if __name__=='__main__':
    R={'stage':'461B','model':'X6_TWO_POP_BOTH_ONE_APPEND_P_OPTION_ONE_APPEND_Q','numeric_semantics':'exact nonnegative integers','cases':[],'large':[]}
    for m,n in [(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)]:
        for rp,rq in ((1,0),(1,1)) if m<=6 else ((1,0),):
            z=exhaustive(m,n,kmax=2,rp=rp,rq=rq)
            R['cases'].append(z)
            print('PASS',m,n,rp,rq,z['history_pairs'],z['future_states'],file=sys.stderr)
    for m,n,kp,kq,d in [(8,10,2,2,1),(64,80,15,17,1),(92,126,20,25,3)]:
        g=grouped(m,n,kp,kq,d)
        ranks=[0,g['q']//2,g['q']-1] if g['q'] else []
        for i in ranks:
            k=g['unrank'](i)
            assert g['population'](k)>0 and g['rank'](k)==i
        R['large'].append({'parameters':[m,n,kp,kq,d],'q':g['q'],'mass':str(g['mass']),'positions':[(src,i+1) for src,i in g['positions']], 'rank_unrank_checks':len(ranks),'cached_subtrees':g['cached_subtrees']})
        print('LARGE',m,n,g['q'],g['mass'],file=sys.stderr)
    R['passed']=True
    R['totals']={k:sum(z[k] for z in R['cases']) for k in ('fibers','history_pairs','class_checks','future_pairs','future_states')}
    print(json.dumps(R,ensure_ascii=False,indent=2))
