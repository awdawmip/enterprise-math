"""U8 candidate connected-overlap law, not native mechanics.

Positive weighted path computations call unchanged source-pinned BRC.  A link
is a pair of paths meeting at a Cell, NOT a primitive two-force balance. Trees
are explicitly declared alternative connectivity witnesses, not new spatial
edges. Scores and normalized trials are not force, energy or physical chance.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import hashlib, importlib.util, sys

PIN='7465f5aa16cbb8fba61ba4be80f8a6884b879c53'
_here=Path(__file__).resolve().parent
_router=_here/'packet_router.py'
if not _router.exists():
    _router=_here.parent/'20261007_cell_closure_u2_7f21d8'/'packet_router.py'
raw=_router.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=PIN:
    raise RuntimeError('unchanged U2 adapter pin mismatch')
_spec=importlib.util.spec_from_file_location('cell_u8_pinned_router',_router)
r=importlib.util.module_from_spec(_spec);sys.modules[_spec.name]=r;_spec.loader.exec_module(r)
ZERO=r.brc.CWM_ZERO
ONE=r.brc.CWM_ONE

def canonical(v):
    if len(v)!=6 or any(type(x) is not int for x in v):
        raise ValueError('six signed integer chart components required')
    return tuple(sorted(map(abs,v)))

def difference(a,b): return tuple(x-y for x,y in zip(a,b))

def scale(value,w): return r.serial(value,r.edge(w)) if w else ZERO

def info(v): return {'count':v.count,'total':str(v.total),'dominant':str(v.dominant)}

class Overlap:
    def __init__(self,lam=Q(1,48)):
        if not Q(0)<lam<Q(1,12): raise ValueError('requires 0<lambda<1/12')
        self.lam=lam;self.rho=12*lam;self.edge=r.edge(lam)
        r.CALLS['one_state_recurrent_cwm']+=1
        self.series=r.brc.one_state_recurrent_cwm([lam]*12)
        self.closure=r.edge(self.series.total_mass_closure)
        self.full_link_mass=r.serial(self.closure,self.closure).total
        # Cache is local to this parameter instance; no cross-parameter reuse.
        self.walk=lru_cache(None)(self._walk)
        self.link=lru_cache(None)(self._link)

    def _walk(self,n,v):
        """One exact endpoint, not an orbit mass. All 12 last edges are summed.

        Only homogeneous bulk walk coefficients are quotient by signed axis
        permutations. The actual requested endpoints/source labels survive in
        caller records; the pinned recurrence reconstructs ordered words.
        """
        if n<0: raise ValueError('negative path depth')
        d=sum(v)
        if d>n or (n-d)%2:return ZERO
        if n==0:return ONE if d==0 else ZERO
        return r.total(r.serial(self.walk(n-1,canonical(r.advance(v,p))),self.edge)
                       for p in r.PORTS)

    def g(self,n,v): return self.walk(n,canonical(v))

    def _link(self,L,v):
        # Each split position is a distinct branch, NOT a scalar count multiplier.
        return r.total(self.walk(n,v) for n in range(L+1) for split in range(n+1))

    def k(self,L,v): return self.link(L,canonical(v))

    def tail(self,L):
        """Uniform omitted TOTAL mass via positive one-state path closure.

        K = sum_n (n+1) G_n. Bound the tail by unrestricted native words.
        This comparison carrier is not mistaken for realized missing response.
        """
        first=self.series.depth(L+1)
        a=scale(r.serial(first,self.closure),Q(L+2))
        b=r.serial(r.serial(r.serial(first,r.edge(self.rho)),self.closure),self.closure)
        return r.merge(a,b).total

    def interval(self,L,v):
        low=self.k(L,v)
        return low, r.merge(low,r.edge(self.tail(L)))

@lru_cache(None)
def trees(N):
    if N<2:raise ValueError('at least two material identities')
    out=[];edges=tuple(combinations(range(N),2))
    for es in combinations(edges,N-1):
        parent=list(range(N))
        def root(i):
            while parent[i]!=i:i=parent[i]
            return i
        valid=True
        for i,j in es:
            a,b=root(i),root(j)
            if a==b:valid=False;break
            parent[a]=b
        if valid:out.append(es)
    return tuple(out)

def validate_cells(cells):
    cells=tuple(tuple(x) for x in cells)
    if len(cells)<2 or len(set(cells))!=len(cells):
        raise ValueError('distinct labelled material Cells required')
    for x in cells:canonical(x)
    return cells

class Candidate:
    def __init__(self,overlap,L=24):
        self.o=overlap;self.L=L;self._scores={}
    def score(self,cells):
        cells=validate_cells(cells)
        # Preserve order of material IDs; translation is only a chart choice.
        rel=tuple(difference(x,cells[0]) for x in cells)
        if rel in self._scores:return self._scores[rel]
        ls={e:self.o.interval(self.L,difference(cells[e[0]],cells[e[1]]))
            for e in combinations(range(len(cells)),2)}
        rows=[]
        for T in trees(len(cells)):
            lower,upper=ONE,ONE
            for e in T:
                lower=r.serial(lower,ls[e][0]);upper=r.serial(upper,ls[e][1])
            rows.append({'tree':T,'lower':lower,'upper':upper})
        low=r.total(x['lower'] for x in rows);high=r.total(x['upper'] for x in rows)
        result={'lower':low,'upper':high,'trees':rows,'links':ls}
        self._scores[rel]=result
        return result

    def one_query(self,cells):
        """All one-step proposals, not a sampled trajectory or exact infinity.

        Reports intervals for the TRUE infinite-link Barker rule. Also executes
        a rational surrogate using finite positive prefixes, with an explicit
        one-query TV certificate. It is never iterated into artificial walls.
        """
        cells=validate_cells(cells);N=len(cells);old=self.score(cells)
        if not old['lower'].live:raise ValueError('increase link depth; no zero-score cutoff allowed')
        q=r.edge(Q(1,12*N));records=[];branches=[];tv=Q(0)
        for i in range(N):
            for p in r.PORTS:
                y=list(cells);y[i]=r.advance(cells[i],p);y=tuple(y)
                if len(set(y))!=N:
                    records.append({'actor':i,'port':p,'collision':True,'accept':('0','0')})
                    branches.append({'actor':i,'port':p,'accepted':False,'cells':cells,'weight':q})
                    continue
                new=self.score(y)
                if not new['lower'].live:raise ValueError('uncertified remote proposal, not a reflecting wall')
                ol,ou=old['lower'].total,old['upper'].total
                nl,nu=new['lower'].total,new['upper'].total
                lo=nl/(ou+nl);hi=nu/(ol+nu)
                denom=r.total((old['lower'],new['lower']))
                norm=r.edge(1/denom.total)
                wa=r.serial(q,r.serial(new['lower'],norm))
                wr=r.serial(q,r.serial(old['lower'],norm))
                a=wa.total/q.total
                tv+=q.total*max(a-lo,hi-a)
                records.append({'actor':i,'port':p,'collision':False,'accept':(str(lo),str(hi)),
                                'surrogate_accept':str(a),'proposed_cells':y,'proposed_score':new})
                branches.extend(({'actor':i,'port':p,'accepted':True,'cells':y,'weight':wa},
                                 {'actor':i,'port':p,'accepted':False,'cells':cells,'weight':wr}))
        return {'cells':cells,'score':old,'records':records,'branches':branches,
                'surrogate_mass':r.total(b['weight'] for b in branches),
                'surrogate_move':r.total(b['weight'] for b in branches if b['accepted']),
                'true_query_TV_from_surrogate_upper':tv}

def encode(x):
    if isinstance(x,r.brc.CWMState):return info(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x
