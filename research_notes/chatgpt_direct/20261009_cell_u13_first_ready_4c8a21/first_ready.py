"""U13: single-use stored-arrival routing, not native triadic force.

The normalized ADVANCE/HOLD protocol below is NEW. It is not U12's unnormalized
all-path grammar. A READY result only reserves routing occurrences; native
incidence, firing, material reaction and physical clock are not supplied.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import hashlib, importlib.util, sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT/'synchronized_events.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261008_cell_u12_synchronous_routing_93f4c2'/'synchronized_events.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='4ba3187b38bba59d55eb00974de4f71a6e39938e':
    raise RuntimeError('U12 source pin mismatch')
spec=importlib.util.spec_from_file_location('u13_pinned_u12',SRC)
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)
r,m=s.r,s.m
ZERO,ONE=r.brc.CWM_ZERO,r.brc.CWM_ONE

def lift(q):
    if q<0:raise ValueError('positive observer required')
    return ZERO if q==0 else r.edge(q)

def add(table,key,w):
    if w.live:table[key]=r.merge(table.get(key,ZERO),w)

@dataclass(frozen=True)
class Plan:
    identity:str
    source:tuple[int,...]
    word:tuple[int,...]

@dataclass(frozen=True)
class State:
    progress:tuple[int,...]
    oldest:int|None=None
    outcome:str='PENDING'

class Protocol:
    def __init__(self,plans,advance=(Q(1,2),)*3,window=None):
        self.plans=tuple(plans);self.a=tuple(map(Q,advance));self.H=window
        if len(self.plans)!=3 or len({p.identity for p in self.plans})!=3:
            raise ValueError('three distinct one-use source occurrences')
        if len(self.a)!=3 or any(not 0<a<=1 for a in self.a):
            raise ValueError('three positive advance probabilities at most one')
        if window is not None and (type(window) is not int or window<0):
            raise ValueError('integer nonnegative residence window or None')
        if any(not p.identity or not p.word for p in self.plans):
            raise ValueError('nonempty named routes required')
        self.lengths=tuple(len(p.word) for p in self.plans)
        ends=tuple(m.endpoint(p.source,p.word) for p in self.plans)
        if len(set(ends))!=1:raise ValueError('routes need one common meeting')
        self.target=ends[0]
        if len({r.axis(p.word[-1]) for p in self.plans})!=3:
            raise ValueError('this candidate requires three distinct final axes')
        for p in self.plans:
            if any(m.endpoint(p.source,p.word[:k])==self.target for k in range(len(p.word))):
                raise ValueError('premature route visit needs a different capture rule')
        self.factors=tuple((lift(1-a),lift(a)) for a in self.a)
        self.closure_records=[]
        self.row=lru_cache(None)(self._row)
        self.solve=lru_cache(None)(self._solve)

    def initial(self):return State((0,0,0))

    def step(self,x,bits):
        if x.outcome!='PENDING':raise ValueError('one-use attempt already finalized')
        if len(x.progress)!=3 or any(type(j) is not int or not 0<=j<=n for j,n in zip(x.progress,self.lengths)):
            raise ValueError('invalid source progress')
        if len(bits)!=3 or any(type(b) is not int or b not in (0,1) for b in bits):
            raise ValueError('one advance/hold bit per source')
        if any(j==n and b for j,n,b in zip(x.progress,self.lengths,bits)):
            raise ValueError('captured occurrence cannot advance again')
        oldcaptured=any(j==n for j,n in zip(x.progress,self.lengths))
        if oldcaptured != (x.oldest is not None) or (x.oldest is not None and (type(x.oldest) is not int or x.oldest<0)):
            raise ValueError('missing or inconsistent arrival age')
        if self.H is not None and x.oldest is not None and x.oldest>=self.H:
            raise ValueError('expired pending state')
        y=tuple(min(n,j+b) for j,n,b in zip(x.progress,self.lengths,bits))
        captured=any(j==n for j,n in zip(y,self.lengths))
        age=None if not captured else (0 if not oldcaptured else x.oldest+1)
        # All arrival ages are reconstructible from the retained branch grammar.
        # For this fixed common-window first-ready observer only their max matters.
        if self.H is None:age=0 if captured else None
        if all(j==n for j,n in zip(y,self.lengths)):
            outcome='READY_RESERVED'
        elif self.H is not None and age is not None and age>=self.H:
            outcome='EXPIRED_RETAINED'
        else:outcome='PENDING'
        return State(y,age,outcome)

    def _row(self,x):
        if x.outcome!='PENDING':return ()
        active=tuple(i for i,(j,n) in enumerate(zip(x.progress,self.lengths)) if j<n)
        rows=[]
        for selected in product((0,1),repeat=len(active)):
            bits=[0]*3;w=ONE
            for i,b in zip(active,selected):bits[i]=b;w=r.serial(w,self.factors[i][b])
            if w.live:rows.append((tuple(bits),self.step(x,tuple(bits)),w))
        if r.total(w for _,_,w in rows).total!=1:raise AssertionError('branch loss')
        return tuple(rows)

    def _solve(self,x):
        """Exact TOTAL observers via positive one-state loop closures on a DAG.

        Returns success/failure masses and their first tick moments. A closed
        rational is a TOTAL observer, not a finite CWM count for infinite paths.
        Finite prefix C/W/M is provided separately by prefixes().
        """
        if x.outcome=='READY_RESERVED':return Q(1),Q(0),Q(0),Q(0)
        if x.outcome=='EXPIRED_RETAINED':return Q(0),Q(1),Q(0),Q(0)
        loop=ZERO;off=[ZERO]*4
        for bits,y,w in self.row(x):
            if y==x:loop=r.merge(loop,w);continue
            values=self.solve(y)
            for i,value in enumerate(values):off[i]=r.merge(off[i],r.serial(w,lift(value)))
        factor=ONE
        if loop.live:
            r.CALLS['one_state_recurrent_cwm']+=1
            closure=r.brc.one_state_recurrent_cwm([loop.total])
            if not closure.total_mass_stable:raise AssertionError('nonterminating local loop')
            factor=r.edge(closure.total_mass_closure)
        suc=r.serial(off[0],factor);fail=r.serial(off[1],factor)
        ms=r.serial(r.merge(suc,off[2]),factor)
        mf=r.serial(r.merge(fail,off[3]),factor)
        vals=tuple(w.total for w in (suc,fail,ms,mf))
        if vals[0]+vals[1]!=1:raise AssertionError('absorption mass lost')
        self.closure_records.append({'state':x,'self_loop':loop.total,'observers':vals})
        return vals

    def prefixes(self,horizon):
        live={self.initial():ONE};hit=[];expired=[];survival=[]
        for t in range(1,horizon+1):
            nxt={};yes=no=ZERO
            for x,w in live.items():
                for bits,y,q in self.row(x):
                    term=r.serial(w,q)
                    if y.outcome=='READY_RESERVED':yes=r.merge(yes,term)
                    elif y.outcome=='EXPIRED_RETAINED':no=r.merge(no,term)
                    else:add(nxt,y,term)
            live=nxt;hit.append(yes);expired.append(no);survival.append(r.total(live.values()))
        return {'hit':hit,'expired':expired,'survival':survival,'last_live':live}

    def trace(self,choices):
        x=self.initial();arrivals=[None]*3;records=[];weight=ONE
        for t,bits in enumerate(choices,1):
            if x.outcome!='PENDING':raise ValueError('same occurrences cannot be reused')
            if len(bits)!=3 or any(b not in (0,1) for b in bits):raise ValueError('bad advance bits')
            q=ONE
            for i,(j,n,b) in enumerate(zip(x.progress,self.lengths,bits)):
                if j==n:
                    if b:raise ValueError('captured occurrence cannot travel again')
                else:q=r.serial(q,self.factors[i][b])
            if not q.live:raise ValueError('zero-weight prepared branch')
            y=self.step(x,bits);weight=r.serial(weight,q)
            for i,(j,n) in enumerate(zip(y.progress,self.lengths)):
                if j==n and arrivals[i] is None:arrivals[i]=t
            cells=tuple(m.endpoint(p.source,p.word[:j]) for p,j in zip(self.plans,y.progress))
            records.append({'tick':t,'state':y,'cells':cells,'arrival_ticks':tuple(arrivals),
                'ages':tuple(None if a is None else t-a for a in arrivals),
                'occurrences':tuple(p.identity for p in self.plans),'weight':weight,
                'native_closure_certified':False,'native_firing_performed':False})
            x=y
        return records

def first_arrivals(length,a,horizon):
    """Single-source negative-binomial family using actual positive paths."""
    a=Q(a);factors=(lift(1-a),lift(a));live={0:ONE};hit=[]
    for _ in range(horizon):
        nxt={};yes=ZERO
        for j,w in live.items():
            for b in (0,1):
                val=r.serial(w,factors[b])
                if j+b==length:yes=r.merge(yes,val)
                else:add(nxt,j+b,val)
        hit.append(yes);live=nxt
    return hit

def joined_first_curve(lengths,probs,window,horizon):
    """Positive last-arrival partition; every successful history occurs once."""
    f=[first_arrivals(n,a,horizon) for n,a in zip(lengths,probs)]
    result=[]
    for t in range(1,horizon+1):
        lo=1 if window is None else max(1,t-window)
        earlier=[r.total(fi[lo-1:t-1]) for fi in f]
        val=ZERO
        for count in (1,2,3):
            for last in combinations(range(3),count):
                w=ONE
                for i in range(3):w=r.serial(w,f[i][t-1] if i in last else earlier[i])
                val=r.merge(val,w)
        result.append(val)
    return result

def example_plans():
    x=r.ZERO;y=r.advance(x,4)
    return (Plan('A:one-use-0',x,(4,)),Plan('R:one-use-0',x,(7,4,6)),
            Plan('C:one-use-0',r.advance(y,9),(8,)))

def encode(obj):
    if isinstance(obj,State):return {'progress':obj.progress,'oldest':obj.oldest,'outcome':obj.outcome}
    if isinstance(obj,Plan):return {'identity':obj.identity,'source':obj.source,'word':obj.word}
    if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [encode(v) for v in obj]
    return s.encode(obj)
