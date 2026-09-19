"""Mass-only quotient bridge between finite control-port BRC and recurrent mass calculus."""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction


def _labels(state_count, labels):
    labels=tuple(labels)
    if len(labels)!=state_count or any(type(x) is not int or x<0 for x in labels):
        raise ValueError('one nonnegative label per state required')
    remap={}; out=[]
    for x in labels:
        if x not in remap: remap[x]=len(remap)
        out.append(remap[x])
    return tuple(out)


def control_mass_matrix(packet):
    n=packet.state_count
    if type(n) is not int or n<1: raise ValueError('positive finite state_count required')
    out=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    for source,target,hist in packet.blocks:
        if not (type(source) is type(target) is int and 0<=source<n and 0<=target<n):
            raise ValueError('control state outside layout')
        mass=hist.forget_effects().total_mass
        if mass<0: raise ValueError('positive-mass projection required')
        out[source][target]+=mass
    return tuple(tuple(row) for row in out)


def certify_control_mass_partition(packet, labels):
    labels=_labels(packet.state_count, labels)
    W=control_mass_matrix(packet)
    q=1+max(labels)
    classes={}
    for i,a in enumerate(labels): classes.setdefault(a,[]).append(i)
    rows=[]
    for i in range(packet.state_count):
        rows.append(tuple(sum(W[i][j] for j in range(packet.state_count) if labels[j]==b) for b in range(q)))
    for members in classes.values():
        first=rows[members[0]]
        if any(rows[i]!=first for i in members[1:]):
            raise ValueError('partition is not total-mass future safe')
    return labels


def quotient_control_mass_matrix(packet, labels):
    labels=certify_control_mass_partition(packet, labels)
    W=control_mass_matrix(packet); q=1+max(labels)
    representatives=[next(i for i,a in enumerate(labels) if a==b) for b in range(q)]
    return tuple(tuple(sum(W[i][j] for j in range(packet.state_count) if labels[j]==b) for b in range(q)) for i in representatives)

@dataclass(frozen=True)
class ControlMassQuotient:
    labels: tuple[int,...]
    full_mass_matrix: tuple[tuple[Fraction,...],...]
    quotient_mass_matrix: tuple[tuple[Fraction,...],...]

    @classmethod
    def compile(cls, packet, labels):
        labels=certify_control_mass_partition(packet, labels)
        return cls(labels, control_mass_matrix(packet), quotient_control_mass_matrix(packet, labels))
