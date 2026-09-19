"""Finite typed control-port BRC over exact affine effect histograms.

This T0 extension is for finite non-spatial control state (phase, resource,
environment class, etc.).  Control states are not extra spatial dimensions.
A quotient is safe only when the declared current observer already factors
through its initial partition AND every supplied future packet has identical
exact effect-valued transition rows from merged source states into retained
target classes.  No hidden-state, occupancy, semantic or infinite-state claim.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence
from .brc_transport import Affine, EffectHistogram, MomentState, ma


def _nat(name, value, *, positive=False):
    if type(value) is not int or value < (1 if positive else 0):
        raise ValueError(f'{name} must be a {"positive" if positive else "nonnegative"} integer')
    return value


def _partition(state_count: int, labels: Sequence[int]) -> tuple[int, ...]:
    labels=tuple(labels)
    if len(labels)!=state_count or any(type(v) is not int or v<0 for v in labels):
        raise ValueError('one nonnegative partition label per control state required')
    remap={}; out=[]
    for label in labels:
        if label not in remap: remap[label]=len(remap)
        out.append(remap[label])
    return tuple(out)


@dataclass(frozen=True)
class ControlPacket:
    state_count: int
    start: int
    duration: int
    blocks: tuple[tuple[int,int,EffectHistogram], ...]

    def __post_init__(self):
        _nat('state_count',self.state_count,positive=True); _nat('start',self.start); _nat('duration',self.duration)
        if type(self.blocks) is not tuple: raise TypeError('immutable blocks required')
        keys=[]
        for source,target,hist in self.blocks:
            if type(source) is not int or type(target) is not int or not 0<=source<self.state_count or not 0<=target<self.state_count:
                raise ValueError('control state outside declared finite layout')
            if not isinstance(hist,EffectHistogram) or hist.dim!=6: raise ValueError('six-axis EffectHistogram required')
            keys.append((source,target))
        if keys!=sorted(set(keys)): raise ValueError('unique canonical control blocks required')

    @classmethod
    def from_edges(cls,state_count,start,duration,edges: Iterable):
        groups={}
        for source,target,weight,action,count in edges:
            if not isinstance(action,Affine) or action.dim!=6: raise ValueError('six-axis Affine required')
            groups.setdefault((source,target),[]).append((weight,action,count))
        blocks=tuple((s,t,EffectHistogram.from_terms(6,terms)) for (s,t),terms in sorted(groups.items()))
        return cls(state_count,start,duration,blocks)

    @classmethod
    def deterministic(cls, transition: Sequence[int], *, start=0, duration=1, effects: Sequence[Affine]|None=None):
        transition=tuple(transition); n=len(transition); _nat('state_count',n,positive=True)
        if effects is None: effects=(Affine.identity(6),)*n
        effects=tuple(effects)
        if len(effects)!=n: raise ValueError('one effect per source state required')
        return cls.from_edges(n,start,duration,((s,t,1,effects[s],1) for s,t in enumerate(transition)))

    @property
    def end(self): return self.start+self.duration

    def at(self,start): return ControlPacket(self.state_count,start,self.duration,self.blocks)

    @classmethod
    def identity(cls,state_count,start=0):
        return cls.deterministic(tuple(range(state_count)),start=start,duration=0)

    def alternatives(self,other):
        if (self.state_count,self.start,self.duration)!=(other.state_count,other.start,other.duration):
            raise ValueError('parallel control/time ports must match')
        blocks={(s,t):h for s,t,h in self.blocks}
        for s,t,h in other.blocks:
            blocks[s,t]=blocks.get((s,t),EffectHistogram.zero(6)).alternatives(h)
        return ControlPacket(self.state_count,self.start,self.duration,tuple((s,t,h) for (s,t),h in sorted(blocks.items())))

    def then(self,later):
        if self.state_count!=later.state_count or self.end!=later.start: raise ValueError('serial control/time ports must match')
        outgoing={}
        for s,t,h in later.blocks: outgoing.setdefault(s,[]).append((t,h))
        blocks={}
        for r,s,h in self.blocks:
            for t,g in outgoing.get(s,()):
                key=(r,t); joined=h.then(g)
                blocks[key]=blocks.get(key,EffectHistogram.zero(6)).alternatives(joined)
        return ControlPacket(self.state_count,self.start,self.duration+later.duration,tuple((s,t,h) for (s,t),h in sorted(blocks.items())))

    def evaluate(self,control:int,x):
        if type(control) is not int or not 0<=control<self.state_count: raise ValueError('unknown control state')
        out={}
        for source,target,hist in self.blocks:
            if source!=control: continue
            for point,weights in hist.evaluate(x).items(): out[target,point]=weights
        return out

    def moment_action(self,states: Mapping[int,MomentState]):
        out={}
        for source,target,hist in self.blocks:
            if source not in states: continue
            state=states[source]
            if not isinstance(state,MomentState) or state.dimension!=6: raise ValueError('six-axis MomentState required')
            term=hist.moment_action(state.to_matrix())
            out[target]=ma(out[target],term) if target in out else term
        return {t:MomentState.from_matrix(m) for t,m in out.items()}


def _rows(packet: ControlPacket, labels: tuple[int,...]):
    rows=[{} for _ in range(packet.state_count)]
    for source,target,hist in packet.blocks:
        q=labels[target]
        rows[source][q]=rows[source].get(q,EffectHistogram.zero(6)).alternatives(hist)
    return rows


def certify_control_partition(packet: ControlPacket, labels: Sequence[int]) -> tuple[int,...]:
    """Exact effect-valued transition descent for one packet.

    The caller remains responsible for making labels refine the declared current
    observer.  This function certifies future packet descent, not observer loss.
    """
    if not isinstance(packet,ControlPacket): raise TypeError('ControlPacket required')
    labels=_partition(packet.state_count,labels); rows=_rows(packet,labels)
    classes={}
    for state,label in enumerate(labels): classes.setdefault(label,[]).append(state)
    for members in classes.values():
        expected=tuple((q,h.entries) for q,h in sorted(rows[members[0]].items()) if h.entries)
        for state in members[1:]:
            actual=tuple((q,h.entries) for q,h in sorted(rows[state].items()) if h.entries)
            if actual!=expected: raise ValueError('control partition is not effect-future safe for this packet')
    return labels


def refine_control_partition(packets: Iterable[ControlPacket], initial: Sequence[int]) -> tuple[int,...]:
    packets=tuple(packets)
    if not packets: raise ValueError('nonempty packet family required')
    n=packets[0].state_count
    if any(not isinstance(p,ControlPacket) or p.state_count!=n for p in packets): raise ValueError('common finite control layout required')
    labels=_partition(n,initial)
    while True:
        rowsets=[_rows(p,labels) for p in packets]
        signatures=[]
        for state in range(n):
            signatures.append((labels[state],tuple(tuple((q,h.entries) for q,h in sorted(rows[state].items()) if h.entries) for rows in rowsets)))
        ids={}; new=[]
        for sig in signatures:
            if sig not in ids: ids[sig]=len(ids)
            new.append(ids[sig])
        new=tuple(new)
        if new==labels:
            for p in packets: certify_control_partition(p,labels)
            return labels
        labels=new
