"""U3 finite response-to-occupancy CANDIDATE, not native force admission.

A finite marked pulse is followed by one proposed joint occupancy transaction.
Demand tokens are indivisible requests, NOT primitive force quanta. The finite
branch measure is a specified trial rule, NOT an empirical physical probability.
All response fields, pending tokens, and conflict records survive explicitly.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product, combinations
from fractions import Fraction as Q
from collections import Counter
from pathlib import Path
import hashlib, importlib.util, sys
_here=Path(__file__).resolve().parent
_router=_here/'packet_router.py'
if not _router.exists():
    _router=_here.parent/'20261007_cell_closure_u2_7f21d8'/'packet_router.py'
_bytes=_router.read_bytes()
if hashlib.sha1(b'blob '+str(len(_bytes)).encode()+b'\0'+_bytes).hexdigest()!='7465f5aa16cbb8fba61ba4be80f8a6884b879c53':
    raise RuntimeError('U2 router blob mismatch')
_spec=importlib.util.spec_from_file_location('cell_u3_pinned_router',_router)
r=importlib.util.module_from_spec(_spec);sys.modules[_spec.name]=r
_spec.loader.exec_module(r)

@dataclass(frozen=True)
class Demand:
    key: tuple
    source: int
    actor: int
    born_at: tuple
    port: int
    response: object

    @property
    def destination(self):
        return r.advance(self.born_at, self.port)


def marked_pulse(cells, depth=1, rho=Q(1,4)):
    """U2's unchanged default transport, but expose full source-resolved state.

    This is the exact depth-L term, not a truncated stationary Green solution.
    Complete joint packet routing is retained by the pinned transition grammar;
    the unary table is used only for this specified linear pulse propagation.
    No new incidence is silently substituted. No physical time is inferred.
    """
    cells = tuple(map(tuple,cells)); occupied = set(cells)
    if len(cells) != len(occupied) or depth < 1:
        raise ValueError('distinct cells and positive pulse depth required')
    mat, bulk = r.transport_tables(rho)
    seed = r.edge(Q(1,12)); retained_edge = r.edge(1-rho)
    layer = {(b,z,p):seed for b,z in enumerate(cells) for p in r.PORTS}
    layers = [layer]; inactive = {}
    for n in range(depth):
        nxt = {}
        for (source,z,p),state in layer.items():
            inactive[n,source,z,p] = r.serial(state,retained_edge)
            for q,transition in mat[p] if z in occupied else bulk:
                key=(source,r.advance(z,q),q^1)
                nxt[key]=r.merge(nxt.get(key,r.brc.CWM_ZERO),r.serial(state,transition))
        layer=nxt; layers.append(layer)
    demands=[]; nonacting={}; who={z:a for a,z in enumerate(cells)}
    for (b,z,p),state in sorted(layer.items()):
        a=who.get(z)
        if a is not None and a!=b:
            demands.append(Demand((depth,b,a,p),b,a,z,p,state))
        else:
            nonacting[b,z,p]=state  # self-return AND field at empty sites stay here
    return {'cells':cells,'depth':depth,'rho':rho,'layers':layers,
            'inactive':inactive,'nonacting':nonacting,'demands':tuple(demands)}


def compatible(cells, selected):
    """Declared exclusion: unique successor cells and no head-on swaps.

    A following move into a vacated cell IS allowed. These are extra trial
    assumptions, not P000 consequences. Only native single-axis edges are used.
    """
    dest=list(cells)
    for a,token in selected.items():
        if token.actor!=a or token.born_at!=cells[a]:
            raise ValueError('stale/unbound token; do not silently rebase stored requests')
        dest[a]=token.destination
    if len(dest)!=len(set(dest)):
        return False
    for a,b in combinations(selected,2):
        if dest[a]==cells[b] and dest[b]==cells[a]:
            return False
    return True


def maximal_subsets(cells, proposals):
    """All inclusion-maximal compatible subsets, without label-priority bias.

    This is a finite joint relation, not an already-realized local protocol or
    an instantaneous physical coordinator. Enumeration is bounded in our tests.
    """
    actors=tuple(sorted(proposals))
    feasible=[]
    for bits in product((False,True),repeat=len(actors)):
        subset=frozenset(a for a,b in zip(actors,bits) if b)
        if compatible(cells,{a:proposals[a] for a in subset}):
            feasible.append(subset)
    return tuple(s for s in feasible if not any(s<t for t in feasible))


def successor_branches(cells, demands, wait=Q(1,48)):
    """Actual positive-BRC weighted finite relation; no postselection.

    Local wait budget kappa and arrival total I give choices kappa/Z,I/Z.
    All joint proposals remain. A contested proposal branches uniformly over
    its maximal compatible subsets; rejected requests remain held. Original
    response CWM is NOT replaced by this separately typed branch measure.
    """
    if wait<=0:
        raise ValueError('positive declared waiting budget required')
    cells=tuple(map(tuple,cells)); demands=tuple(demands)
    options=[]
    for a in range(len(cells)):
        own=tuple(t for t in demands if t.actor==a)
        weights=(r.edge(wait),)+tuple(r.edge(t.response.total) for t in own)
        Z=r.total(weights).total
        normalizer=r.edge(Q(1)/Z)
        options.append(tuple((token,r.serial(w,normalizer))
                             for token,w in zip((None,)+own,weights)))
    out=[]
    for proposal_id,choice in enumerate(product(*options)):
        joint=r.brc.CWM_ONE
        selected={}
        for a,(token,w) in enumerate(choice):
            joint=r.serial(joint,w)
            if token is not None: selected[a]=token
        maxima=maximal_subsets(cells,selected)
        tie=r.edge(Q(1,len(maxima)))
        for accepted in maxima:
            measure=r.serial(joint,tie)
            used=tuple(selected[a] for a in sorted(accepted))
            used_keys={t.key for t in used}
            held=tuple(t for t in demands if t.key not in used_keys)
            rejected=tuple(selected[a].key for a in selected if a not in accepted)
            dest=list(cells)
            for t in used: dest[t.actor]=t.destination
            out.append({'proposal_id':proposal_id,'proposal':tuple(
                            None if t is None else t.key for t,w in choice),
                        'accepted':tuple(sorted(accepted)), 'measure':measure,
                        'cells':tuple(dest),'used':used,'held':held,'rejected':rejected,
                        'interaction_log':tuple((t.key,t.source,t.actor,t.born_at,t.destination)
                                                for t in used)})
    return tuple(out)


def summarize(branches,initial):
    projected={}
    for b in branches:
        key=b['cells'];projected[key]=r.merge(projected.get(key,r.brc.CWM_ZERO),b['measure'])
    moving=r.total(b['measure'] for b in branches if b['accepted'])
    return {'proposals':len({b['proposal_id'] for b in branches}),
            'resolved_branches':len(branches),'moving_branches':sum(bool(b['accepted']) for b in branches),
            'occupancy_outcomes':len(projected),'moving_measure':str(moving.total),
            'total_measure':str(r.total(b['measure'] for b in branches).total),
            'outcomes':[{'cells':cells,'measure':str(w.total),'selector_count':w.count}
                        for cells,w in sorted(projected.items())],
            'all_labels_returned':all(b['cells']==initial for b in branches),
            'physical_probability_claimed':False}
