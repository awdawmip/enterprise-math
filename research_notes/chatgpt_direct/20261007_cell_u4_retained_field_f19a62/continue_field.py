"""U4: retained positive-BRC field, passive recharts, and fresh-arrival probes.

No native force law is asserted. The U3 trial selector is reused unchanged.
Old commands remain recorded but are outside each explicitly fresh-only probe.
The positive field is NEVER re-seeded, translated with its source, or cancelled.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from dataclasses import asdict
import hashlib, importlib.util, sys

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'occupancy.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261007_cell_u3_occupancy_c8a461'/'occupancy.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='3d7860df3ec93507cf7217bcea47867d809692fb':
    raise RuntimeError('U3 source pin mismatch')
spec=importlib.util.spec_from_file_location('u4_pinned_occupancy',SRC)
o=importlib.util.module_from_spec(spec);sys.modules[spec.name]=o;spec.loader.exec_module(o)
r=o.r

class RetainedField:
    """Typed extension of the unchanged U2 transport tables.

    A field key is (birth-source, absolute raw Cell, incoming port).
    The step's occupied SET controls the fixed material/bulk table.
    A source label is not a command to relocate previously emitted field.
    """
    def __init__(self,rho=Q(1,4)):
        self.rho=rho
        self.material,self.bulk=r.transport_tables(rho)
        self.retire=r.edge(1-rho)

    def advance(self,field,cells,stage):
        cells=tuple(cells)
        if len(cells)!=len(set(cells)):
            raise ValueError('duplicate occupied Cells')
        occupied=set(cells); nxt={}; retired={}
        for (source,z,p),value in field.items():
            retired[stage,source,z,p]=r.serial(value,self.retire)
            for q,w in self.material[p] if z in occupied else self.bulk:
                key=(source,r.advance(z,q),q^1)
                nxt[key]=r.merge(nxt.get(key,r.brc.CWM_ZERO),r.serial(value,w))
        return nxt,retired


def fresh_probe(field,cells,stage):
    """A non-consuming readout of the latest field; not duplicate response mass.

    Demand IDs identify observed arrival events. Old request disposition records
    and all old anchors survive elsewhere; this probe does not replay them.
    """
    who={z:a for a,z in enumerate(cells)}
    return tuple(o.Demand((stage,s,who[z],p),s,who[z],z,p,v)
                 for (s,z,p),v in sorted(field.items())
                 if z in who and who[z]!=s and v.live)


def passive_rechart(field,origin):
    """Bijective change of raw chart only: no physical path or weight update."""
    return {(s,tuple(a-b for a,b in zip(z,origin)),p):v
            for (s,z,p),v in field.items()}


def undo_rechart(chart,origin):
    return {(s,tuple(a+b for a,b in zip(z,origin)),p):v
            for (s,z,p),v in chart.items()}


def historical_target(token):
    return token.destination


def residual_readout(token,current_cell):
    return tuple(y-x for x,y in zip(current_cell,historical_target(token)))


def total_readout(field):
    return r.total(field.values()).total


def row(field,source,cell):
    return tuple(field.get((source,cell,p),r.brc.CWM_ZERO) for p in r.PORTS)


def difference_readout(left,right):
    # A contrast between TWO positive fields, not a signed physical carrier.
    return {k:left.get(k,r.brc.CWM_ZERO).total-right.get(k,r.brc.CWM_ZERO).total
            for k in left.keys()|right.keys()
            if left.get(k,r.brc.CWM_ZERO).total!=right.get(k,r.brc.CWM_ZERO).total}


def encode(x):
    if isinstance(x,o.Demand): return {k:encode(v) for k,v in asdict(x).items()}
    if isinstance(x,r.brc.CWMState):return r.to_json(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple,set,frozenset)):return [encode(v) for v in x]
    return x
