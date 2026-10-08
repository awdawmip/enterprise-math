"""U12 common-clock path arrivals and a source-accounted prefix preparation.

This is a conditional routing/interface model, not native force or a physical
clock. A routing gate never issues TRIADIC_CLOSURE_E or an F_E certificate.
Scientific positive weights use the unchanged source-pinned U11/U9/U8/U2 BRC.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib, importlib.util, sys
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'resource_lift.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261008_cell_u11_resource_reaction_c7e4a1'/'resource_lift.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='0a7e0890eb08dc722d2e85fb3ad1a7b2d6b29621':
    raise RuntimeError('U11 source pin mismatch')
spec=importlib.util.spec_from_file_location('u12_pinned_u11',SRC)
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
m,r,u=v.m,v.r,v.u
ZERO,ONE=r.brc.CWM_ZERO,r.brc.CWM_ONE
WAIT=None
Cell=tuple[int,...]

def parity(z: Cell):return sum(z)%2

def add(x,y):return tuple(a+b for a,b in zip(x,y))

def difference(x,y):return tuple(a-b for a,b in zip(x,y))

def put(table,key,value):
    if value.live:table[key]=r.merge(table.get(key,ZERO),value)

class ClockKernel:
    """One tick: stay with weight eta OR walk one of twelve edges with lambda.

    A stay is not a thirteenth spatial direction. Equal-clock families keep
    source/clock provenance in the outer records and grammar. All returned
    endpoint CWM values refer to one endpoint, never the size of its orbit.
    """
    def __init__(self,lam=Q(1,48),eta=Q(0)):
        if not 0<lam<Q(1,12) or not 0<=eta<1-12*lam:raise ValueError('subcritical positive range')
        self.lam,self.eta=lam,eta
        self.move=r.edge(lam);self.hold=r.edge(eta) if eta else ZERO
        self.s=12*lam+eta
        shares=[lam]*12+([eta] if eta else [])
        r.CALLS['one_state_recurrent_cwm']+=1
        self.series=r.brc.one_state_recurrent_cwm(shares)
        self.step=r.total([self.move]*12+([self.hold] if eta else []))
        self.pair_step=r.serial(self.step,self.step)
        r.CALLS['one_state_recurrent_cwm']+=1
        self.pair_series=r.brc.one_state_recurrent_cwm([self.pair_step.total])
        self.walk=lru_cache(None)(self._walk)
    def _walk(self,t,z):
        if t<0:raise ValueError('negative clock')
        if sum(z)>t:return ZERO
        if t==0:return ONE if sum(z)==0 else ZERO
        parts=[r.serial(self.walk(t-1,u.canonical(r.advance(z,p))),self.move) for p in r.PORTS]
        if self.eta:parts.append(r.serial(self.walk(t-1,z),self.hold))
        return r.total(parts)
    def endpoint(self,t,z):return self.walk(t,u.canonical(z))
    def pair(self,horizon,z):
        # One midpoint split per even-length timed word. NOT U8's n+1 splits.
        return r.total(self.endpoint(2*t,z) for t in range(horizon+1))
    def pair_tail(self,horizon):
        return r.serial(self.pair_series.depth(horizon+1),r.edge(self.pair_series.total_mass_closure)).total
    def pair_interval(self,horizon,z):
        if not self.eta and parity(z):return Q(0),Q(0)
        lo=self.pair(horizon,z);return lo.total,lo.total+self.pair_tail(horizon)
    def total_pair_mass(self):return self.pair_series.total_mass_closure
    def full_layers(self,horizon,start=None):
        start=r.ZERO if start is None else start
        layers=[{start:ONE}]
        for _ in range(horizon):
            nxt={}
            for z,w in layers[-1].items():
                for p in r.PORTS:put(nxt,r.advance(z,p),r.serial(w,self.move))
                if self.eta:put(nxt,z,r.serial(w,self.hold))
            layers.append(nxt)
        return layers
    def arrivals(self,previous):
        """Only FRESH final-edge arrivals; a wait is not a new incoming port."""
        out={}
        for z,w in previous.items():
            for p in r.PORTS:put(out,(r.advance(z,p),p),r.serial(w,self.move))
        return out
    def witness_weight(self,words):
        weights=[]
        for word in words:
            val=ONE
            for p in word:
                if p is not None and p not in r.PORTS:raise ValueError('bad port')
                val=r.serial(val,self.hold if p is None else self.move)
            weights.append(val)
        out=ONE
        for val in weights:out=r.serial(out,val)
        return out

def pair_join(layer1,layer2):
    return r.total(r.serial(w,layer2[z]) for z,w in layer1.items() if z in layer2)

def triple_join(layers):
    if len(layers)!=3:raise ValueError('three distinct source populations')
    common=layers[0].keys() & layers[1].keys() & layers[2].keys()
    return r.total(r.serial(r.serial(layers[0][z],layers[1][z]),layers[2][z]) for z in sorted(common))

def port_gate(arrivals,target=None):
    """Permissive equal-canonical-frame NECESSARY port gate only.

    Three distinct axes and fresh same-clock co-location DO NOT by themselves
    certify native closure. The caller retains source occurrence identities.
    """
    tables=[]
    for aa in arrivals:
        by={}
        for (z,p),w in aa.items():
            if target is None or z==target:by.setdefault(z,{})[p]=w
        tables.append(by)
    common=tables[0].keys() & tables[1].keys() & tables[2].keys()
    mass=ZERO;rows=[]
    for z in sorted(common):
        for p,q,s in product(*(tuple(t[z]) for t in tables)):
            if len({r.axis(p),r.axis(q),r.axis(s)})!=3:continue
            val=r.serial(r.serial(tables[0][z][p],tables[1][z][q]),tables[2][z][s])
            mass=r.merge(mass,val);rows.append((z,(p,q,s),val))
    return mass,rows

def tree_score_interval(cells,kernel,horizon):
    u.validate_cells(cells)
    lo=hi=ZERO;rows=[]
    for tree in u.trees(len(cells)):
        a=b=ONE
        for i,j in tree:
            ll,hh=kernel.pair_interval(horizon,difference(cells[i],cells[j]))
            a=r.serial(a,r.edge(ll)) if ll else ZERO
            b=r.serial(b,r.edge(hh)) if hh else ZERO
        lo=r.merge(lo,a);hi=r.merge(hi,b);rows.append((tree,a,b))
    return {'lower':lo,'upper':hi,'trees':rows}

@dataclass(frozen=True)
class Signal:
    identity:str
    role:str
    source_cell:Cell
    word:tuple[int|None,...]
    quantum:Q=Q(1)
    launch:int=0

def signal_trace(sig):
    if not sig.identity or sig.quantum<=0:raise ValueError('named positive candidate quantum')
    u.canonical(sig.source_cell)
    z=sig.source_cell;out=[{'tick':sig.launch,'cell':z,'port':None}]
    for t,p in enumerate(sig.word,1):
        if p is not None:
            if p not in r.PORTS:raise ValueError('bad port')
            z=r.advance(z,p)
        out.append({'tick':sig.launch+t,'cell':z,'port':p})
    return out

def prepare_gate(signals):
    if len(signals)!=3:raise ValueError('exactly three source occurrences required')
    if len({s.identity for s in signals})!=3:raise ValueError('an occurrence cannot be used twice')
    traces=[signal_trace(s) for s in signals]
    tails=[t[-1] for t in traces]
    reasons=[]
    if len({t['tick'] for t in tails})!=1:reasons.append('CLOCK_MISMATCH')
    if len({t['cell'] for t in tails})!=1:reasons.append('CELL_MISMATCH')
    if len({s.quantum for s in signals})!=1:reasons.append('UNEQUAL_CANDIDATE_QUANTA')
    pp=[t['port'] for t in tails]
    if any(p is None for p in pp):reasons.append('NO_FRESH_ARRIVAL')
    elif len({r.axis(p) for p in pp})!=3:reasons.append('CANONICAL_DISTINCT_AXIS_PRECONDITION')
    return {'routing_ready':not reasons,'reasons':reasons,'arrivals':tails,'traces':traces,
      'occurrence_ids':tuple(s.identity for s in signals),'native_closure_certified':False,
      'material_reaction_derived':False,'status':'ROUTING_ONLY_NATIVE_EVENT_AND_UPDATE_STILL_REQUIRED'}

def prefix_preparation(base,lam=Q(1,48),eta=Q(1,48),p=4,q=6,s=8):
    """Three real source records are delivered, not a fabricated native lift.

    One leaf actor A, one U11 free record token R at x, and a SEPARATE prepared
    support token C at y-d(s). All reach y at tick3 along three distinct last-port axes.
    The third token is retained at y in the output; it is not reset at source.
    The final bound-prefix state is a conditional DATA update, not F_E.
    """
    m.validate(base)
    if len(v.incident_slots(base,0))!=1:raise ValueError('this minimal protocol is for a leaf')
    if len({r.axis(p),r.axis(q),r.axis(s)})!=3:raise ValueError('three distinct axes')
    x=base.cells[0];y=r.advance(x,p)
    if y in base.cells:raise ValueError('target must be vacant')
    support=r.advance(y,s^1)
    inventory=v.prepared(base,base.length()+1,1,reservoir_cell=x)
    token=inventory.free[0][0]
    signals=(Signal('actor-0:occurrence-0','MATERIAL_ACTION_CANDIDATE',x,(None,None,p)),
             Signal(f'record-token:{token}:occurrence-0','RECORD_ACTION_CANDIDATE',x,(q^1,p,q)),
             Signal('support-token:occurrence-0','CELL_ACTION_CANDIDATE',support,(None,None,s)))
    gate=prepare_gate(signals)
    if not gate['routing_ready']:raise AssertionError('prepared route failed')
    # Commit only a model data transition. All native authority flags stay false.
    yy=m.material(base,0,p,True)
    tokens=list(inventory.tokens);slot=v.incident_slots(base,0)[0];tokens[slot]=(token,)+tokens[slot]
    out=v.Inventory(yy,tuple(tokens),(),inventory.B,inventory.q,x);v.validate(out)
    support_ledger={'id':'support-token','source':support,'current_cell':y,
                    'status':'HELD_FOR_CANDIDATE_EVENT_NOT_REISSUABLE', 'native_fired':False}
    frames=[]
    old_bound=tuple(t for leg in inventory.tokens for t in leg)
    for tick in range(4):
        frames.append({'tick':tick,'material_cell':gate['traces'][0][tick]['cell'],
           'record_cell':gate['traces'][1][tick]['cell'],
           'support_cell':gate['traces'][2][tick]['cell'],
           'record_free':(token,) if tick==0 else (),
           'record_held':() if tick==0 else (token,),
           'record_bound':old_bound,'support_id':'support-token',
           'support_reserved':True,'native_event_fired':False,
           'prefix_head_unmatched':tick==3})
    return {'before':inventory,'conditional_after':out,'signals':signals,'gate':gate,'frames':frames,
            'support_after':support_ledger,'ticks':3,'spatial_moves':5,'waits':4,
            'candidate_history_weight':ClockKernel(lam,eta).witness_weight([s.word for s in signals]),
            'native_commit_performed':False,'third_source_is_separate_inventory':True}

def encode(x):
    if isinstance(x,Signal):return {'id':x.identity,'role':x.role,'source_cell':x.source_cell,
        'word':x.word,'quantum':str(x.quantum),'launch':x.launch}
    if isinstance(x,dict):return {str(k):encode(w) for k,w in x.items()}
    if isinstance(x,(tuple,list)):return [encode(w) for w in x]
    return v.encode(x)
