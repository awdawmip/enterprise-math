"""U14 retained cyclic register: conditional interface, NOT native force.

Uses the unchanged U13 routing/BRC sources. The common cyclic storage map and
phase-coincidence gate are new assumptions. Accepted means routing/phase READY,
never native TRIADIC_CLOSURE_E or physical action. All positive path masses use
original edge/serial/recoalesce; infinite closures are TOTAL observers only.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, combinations
from pathlib import Path
import hashlib, importlib.util, sys

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'first_ready.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261009_cell_u13_first_ready_4c8a21'/'first_ready.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='06eb1bae314e017038d951fdf4b1c32625c439f9':
    raise RuntimeError('U13 input pin mismatch')
spec=importlib.util.spec_from_file_location('u14_pinned_u13',SRC)
f=importlib.util.module_from_spec(spec);sys.modules[spec.name]=f;spec.loader.exec_module(f)
r,m=f.r,f.m
ZERO,ONE=f.ZERO,f.ONE
lift,add=f.lift,f.add
OUTCOMES=('READY_RESERVED','PHASE_BLOCKED_RETAINED','EXPIRED_RETAINED')

@dataclass(frozen=True)
class State:
    progress:tuple[int,...]
    phases:tuple[int|None,...]
    oldest:int|None=None
    outcome:str='PENDING'

class Protocol:
    def __init__(self,modulus=2,advance=(Q(1,2),)*3,window=None,plans=None):
        if type(modulus) is not int or modulus<1:raise ValueError('positive integer register period')
        self.k=modulus
        self.base=f.Protocol(f.example_plans() if plans is None else plans,advance,window)
        self.plans=self.base.plans;self.a=self.base.a;self.H=window
        self.lengths=self.base.lengths;self.factors=self.base.factors
        self.closure_records=[]
        self.row=lru_cache(None)(self._row)
        self.solve=lru_cache(None)(self._solve)

    def initial(self):return State((0,0,0),(None,None,None))

    def validate(self,x):
        if len(x.progress)!=3 or len(x.phases)!=3:raise ValueError('three source states required')
        for j,n,phi in zip(x.progress,self.lengths,x.phases):
            if type(j) is not int or not 0<=j<=n:raise ValueError('bad route progress')
            if (j==n)!=(phi is not None):raise ValueError('phase exists iff captured')
            if phi is not None and (type(phi) is not int or not 0<=phi<self.k):raise ValueError('bad phase')
        captured=any(v is not None for v in x.phases)
        if captured!=(x.oldest is not None):raise ValueError('oldest capture missing')
        if x.oldest is not None and (type(x.oldest) is not int or x.oldest<0):raise ValueError('bad age')
        if self.H is not None and x.outcome=='PENDING' and x.oldest is not None and x.oldest>=self.H:
            raise ValueError('expired pending state')

    def step(self,x,bits):
        self.validate(x)
        if x.outcome!='PENDING':raise ValueError('one-use query already terminated')
        if len(bits)!=3 or any(type(b) is not int or b not in (0,1) for b in bits):raise ValueError('bad bits')
        if any(j==n and b for j,n,b in zip(x.progress,self.lengths,bits)):
            raise ValueError('captured source cannot travel again')
        pp=tuple(j+b for j,b in zip(x.progress,bits))
        ph=tuple((phi+1)%self.k if phi is not None else (0 if j==n else None)
                 for phi,j,n in zip(x.phases,pp,self.lengths))
        age=None if all(v is None for v in ph) else (0 if x.oldest is None else x.oldest+1)
        if self.H is None:age=0 if age is not None else None
        if all(j==n for j,n in zip(pp,self.lengths)):
            out='READY_RESERVED' if len(set(ph))==1 else 'PHASE_BLOCKED_RETAINED'
        elif self.H is not None and age is not None and age>=self.H:out='EXPIRED_RETAINED'
        else:out='PENDING'
        return State(pp,ph,age,out)

    def _row(self,x):
        if x.outcome!='PENDING':return ()
        active=[i for i,(j,n) in enumerate(zip(x.progress,self.lengths)) if j<n]
        rows=[]
        for bb in product((0,1),repeat=len(active)):
            bits=[0]*3;w=ONE
            for i,b in zip(active,bb):bits[i]=b;w=r.serial(w,self.factors[i][b])
            if w.live:rows.append((tuple(bits),self.step(x,tuple(bits)),w))
        if r.total(w for _,_,w in rows).total!=1:raise AssertionError('lost row mass')
        return tuple(rows)

    def _solve(self,x):
        """All-time outcome TOTALS, removing positive common-rotation cycles.

        Progress increases on every off-orbit transition. Finite-age layers
        increase between captures. At infinite age, no-advance cycles have
        period k (period1 before capture). We close their k-fold hold weight
        by the original one_state_recurrent_cwm, never a matrix inverse.
        """
        if x.outcome in OUTCOMES:return tuple(Q(int(x.outcome==o)) for o in OUTCOMES)
        self.validate(x)
        orbit=[];where={};cur=x
        while cur not in where:
            where[cur]=len(orbit)
            row=self.row(cur)
            looprows=[(y,w) for bits,y,w in row if not any(bits)]
            off=[ZERO]*3
            for bits,y,w in row:
                if not any(bits):continue
                for i,val in enumerate(self.solve(y)):off[i]=r.merge(off[i],r.serial(w,lift(val)))
            if not looprows:
                orbit.append((cur,off,ZERO,None));break
            nxt,ell=looprows[0]
            orbit.append((cur,off,ell,nxt))
            if nxt.outcome!='PENDING':break
            cur=nxt
        # Every nonterminating hold-only orbit closes at its initial state.
        last=orbit[-1];end=last[3]
        prefix=ONE;total=[ZERO]*3
        for _,off,ell,_ in orbit:
            for i,w in enumerate(off):total[i]=r.merge(total[i],r.serial(prefix,w))
            prefix=r.serial(prefix,ell)
        closure=ONE;period=None
        if end is not None and end.outcome!='PENDING':
            for i,val in enumerate(self.solve(end)):total[i]=r.merge(total[i],r.serial(prefix,lift(val)))
        elif end is not None:
            if end!=x:raise AssertionError('unexpected preperiod in hold orbit')
            period=len(orbit)
            if prefix.live:
                r.CALLS['one_state_recurrent_cwm']+=1
                cert=r.brc.one_state_recurrent_cwm([prefix.total])
                if not cert.total_mass_stable:raise AssertionError('nonterminating hold orbit')
                closure=r.edge(cert.total_mass_closure)
        vals=tuple(r.serial(w,closure).total for w in total)
        if sum(vals)!=1:raise AssertionError(('absorption mass',x,vals))
        self.closure_records.append({'state':x,'hold_orbit_length':len(orbit),'cyclic_period':period,
                                     'cycle_weight':prefix.total if period else None,'outcomes':vals})
        return vals

    def prefixes(self,horizon):
        live={self.initial():ONE};hits=[];blocks=[];expired=[];survival=[]
        for _ in range(horizon):
            nxt={};stops={o:ZERO for o in OUTCOMES}
            for x,w in live.items():
                for bits,y,q in self.row(x):
                    ww=r.serial(w,q)
                    if y.outcome in stops:stops[y.outcome]=r.merge(stops[y.outcome],ww)
                    else:add(nxt,y,ww)
            live=nxt;hits.append(stops[OUTCOMES[0]]);blocks.append(stops[OUTCOMES[1]])
            expired.append(stops[OUTCOMES[2]]);survival.append(r.total(live.values()))
        return {'hit':hits,'phase_block':blocks,'expired':expired,'survival':survival,'last_live':live}

    def trace(self,choices):
        x=self.initial();arr=[None]*3;out=[];w=ONE
        for t,bits in enumerate(choices,1):
            chosen=[(y,q) for bb,y,q in self.row(x) if bb==tuple(bits)]
            if len(chosen)!=1:raise ValueError('not a positive active branch')
            x,q=chosen[0];w=r.serial(w,q)
            for i,j in enumerate(x.progress):
                if j==self.lengths[i] and arr[i] is None:arr[i]=t
            cells=tuple(m.endpoint(p.source,p.word[:j]) for p,j in zip(self.plans,x.progress))
            out.append({'tick':t,'state':x,'arrival_ticks':tuple(arr),'ages':tuple(None if a is None else t-a for a in arr),
                        'cells':cells,'weight':w,'occurrences':tuple(p.identity for p in self.plans),
                        'native_firing':False})
        return out

def power(a,n):
    if n<0:raise ValueError('nonnegative power')
    val=ONE
    for _ in range(n):val=r.serial(val,lift(a))
    return val

def convolve_residues(a,b):
    if len(a)!=len(b):raise ValueError('same cyclic register')
    k=len(a);out=[ZERO]*k
    for i,w in enumerate(a):
        for j,v in enumerate(b):out[(i+j)%k]=r.merge(out[(i+j)%k],r.serial(w,v))
    return tuple(out)

def arrival_residues(length,a,k):
    """Residues of a sum of length geometric advance times. TOTAL law.

        Every representative r=1..k carries a*(1-a)^(r-1) and independent
        complete k-hold cycles. No complex roots-of-unity filter is used.
    """
    a=Q(a)
    if type(length) is not int or length<1 or type(k) is not int or k<1 or not 0<a<=1:
        raise ValueError('positive finite route and period')
    b=1-a;cycle=power(b,k);closure=ONE
    if cycle.live:
        r.CALLS['one_state_recurrent_cwm']+=1
        closure=r.edge(r.brc.one_state_recurrent_cwm([cycle.total]).total_mass_closure)
    one=[ZERO]*k
    for t in range(1,k+1):one[t%k]=r.serial(r.serial(lift(a),power(b,t-1)),closure)
    law=tuple([ONE]+[ZERO]*(k-1))
    for _ in range(length):law=convolve_residues(law,one)
    if r.total(law).total!=1:raise AssertionError('residue law lost mass')
    return law

def infinite_phase_success(lengths,probs,k):
    laws=[arrival_residues(n,a,k) for n,a in zip(lengths,probs)]
    pieces=[r.serial(r.serial(laws[0][j],laws[1][j]),laws[2][j]) for j in range(k)]
    return r.total(pieces).total,laws

def joined_curve(lengths,probs,k,H,horizon):
    """First-completion partition restricted by one common arrival residue."""
    fs=[f.first_arrivals(n,a,horizon) for n,a in zip(lengths,probs)]
    ans=[]
    for t in range(1,horizon+1):
        lo=1 if H is None else max(1,t-H)
        earlier=[r.total(fi[u-1] for u in range(lo,t) if (t-u)%k==0) for fi in fs]
        total=ZERO
        for size in (1,2,3):
            for last in combinations(range(3),size):
                w=ONE
                for i in range(3):w=r.serial(w,fs[i][t-1] if i in last else earlier[i])
                total=r.merge(total,w)
        ans.append(total)
    return ans

def common_shift(phases,k):return tuple((p+1)%k for p in phases)

def exchange_align(phases,memories,k,inverse=False):
    """A NEW coupled local logical update, not passive storage or native force.

    Two explicitly supplied local memory registers exchange relative phases
    with A and C while the reference R advances once. Blank memories align
    the three readouts; previous offsets are preserved in the memory outputs.
    This finite bijection is not a primitive five-force event or a duration
    calibration. It requires a separate native realization and resource source.
    """
    if len(phases)!=3 or len(memories)!=2 or any(type(p) is not int or not 0<=p<k for p in phases+memories):
        raise ValueError('three cyclic phases and two cyclic record registers')
    a,b,c=phases;u,v=memories
    if inverse:
        oldb=(b-1)%k
        return ((oldb+u)%k,oldb,(oldb+v)%k),((a-b)%k,(c-b)%k)
    newb=(b+1)%k
    return ((newb+u)%k,newb,(newb+v)%k),((a-b)%k,(c-b)%k)

def encode(obj):
    if isinstance(obj,State):return {'progress':obj.progress,'phases':obj.phases,'oldest':obj.oldest,'outcome':obj.outcome}
    if isinstance(obj,dict):return {str(k):encode(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [encode(v) for v in obj]
    return f.encode(obj)
