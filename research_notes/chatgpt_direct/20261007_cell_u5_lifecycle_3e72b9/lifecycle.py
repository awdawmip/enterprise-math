"""U5 response-lifecycle diagnostics, NOT native force or calibrated time.

Pinned U4/U3/U2 BRC operations are actually used. The all-future estimates
apply only to the OLD fresh-only, no-source trial law. Local dormant release
is an explicitly NEW positive-response circuit, never inferred material physics.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import hashlib, importlib.util, sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'continue_field.py'
if not SRC.exists():
    SRC = ROOT.parent / '20261007_cell_u4_retained_field_f19a62' / 'continue_field.py'
raw = SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != 'c2f0749382ad4a6997b3a951a60d20713200fb20':
    raise RuntimeError('U4 source pin mismatch')
spec = importlib.util.spec_from_file_location('u5_pinned_u4', SRC)
c = importlib.util.module_from_spec(spec); sys.modules[spec.name] = c
spec.loader.exec_module(c)
r, o = c.r, c.o


def merge_field(*fields):
    """CWM addition; key retains birth-source, absolute Cell, incoming port."""
    out = {}
    for field in fields:
        for key, value in field.items():
            out[key] = r.merge(out.get(key,r.brc.CWM_ZERO),value)
    return out


def split_field(field, share):
    """An explicit positive RESPONSE partition; NOT a force-quantum division."""
    if not Q(0) <= share <= Q(1):
        raise ValueError('share outside [0,1]')
    chosen, kept = {}, {}
    yes = r.edge(share) if share else r.brc.CWM_ZERO
    no = r.edge(1-share) if share < 1 else r.brc.CWM_ZERO
    for key, value in field.items():
        if share:
            chosen[key] = r.serial(value, yes)
        if share < 1:
            kept[key] = r.serial(value, no)
    return chosen, kept


def local_release_step(active, dormant, cells, stage, transport, release=Q(1,8)):
    """One explicitly NEW circuit step; no external source and no teleport.

    OLD dormant response releases at its actual stored Cell and port; the
    remaining old store is retained. Newly retired response cannot release in
    this same stage. Coalescing retirement ages is justified ONLY for this
    age-blind release/total-CWM observation language. Every old branch extends
    by one labelled LIVE/STORE choice; the recurrence is the path grammar.
    The caller retains returned retirement/release partitions as evidence.
    """
    next_live, retired_tagged = transport.advance(active, cells, stage)
    retired = {(s,z,p): value for (n,s,z,p),value in retired_tagged.items()}
    released, held = split_field(dormant,release)
    return (merge_field(next_live,released), merge_field(held,retired),
            {'retired':retired_tagged,'released':released,'held_old':held})


def probe_law(arrivals,cells,stage,kappa):
    demands = c.fresh_probe(arrivals,cells,stage)
    branches = o.successor_branches(cells,demands,wait=kappa)
    law = {}
    for branch in branches:
        key=branch['cells']
        law[key]=r.merge(law.get(key,r.brc.CWM_ZERO),branch['measure'])
    return law, branches


def pulled_arrivals(field,cells,transport):
    """Exact next cross-source arrival rows via the SAME BRC edge table.

    Every selected target row has a unique previous Cell for each incoming
    port. This evaluates all its source/previous-port contributions and keeps
    finite CWM statistics. It is NOT a substitute full field or future solver.
    Valid for the immediate fresh query; the original field and grammar remain.
    """
    occupied=set(cells); out={}
    sources=sorted({s for s,z,p in field})
    table={p:dict(transport.material[p]) for p in r.PORTS}
    bulk=dict(transport.bulk)
    for a,target in enumerate(cells):
        for source in sources:
            if source==a:
                continue
            for incoming in r.PORTS:
                previous=r.advance(target,incoming)
                outgoing=incoming^1
                value=r.brc.CWM_ZERO
                for old_port in r.PORTS:
                    old=field.get((source,previous,old_port))
                    edge=table[old_port].get(outgoing) if previous in occupied else bulk[outgoing]
                    if old is not None and edge is not None:
                        value=r.merge(value,r.serial(old,edge))
                if value.live:
                    out[source,target,incoming]=value
    return out


def two_query_path_law(field,cells,stage,transport,kappa):
    """EXACT two-query labelled-occupancy law, with feedback and no reset.

    First propagation preserves the whole field. Since the query is
    non-consuming, this next field is common to all first-query outcomes.
    Proposal/conflict histories may be aggregated ONLY for the declared future
    fresh-only law: they do not rearm held events. Second propagation is an
    exact pullback of all needed rows, not a full second field computation.
    """
    first_field, retired=transport.advance(field,cells,stage+1)
    first_law, first_branches=probe_law(first_field,cells,stage+1,kappa)
    paths={}; final={}; rows={}; branch_count=0
    for next_cells,first_weight in sorted(first_law.items()):
        arrivals=pulled_arrivals(first_field,next_cells,transport)
        second_law,bs=probe_law(arrivals,next_cells,stage+2,kappa)
        rows[next_cells]=arrivals; branch_count+=len(bs)
        for last_cells,second_weight in second_law.items():
            weight=r.serial(first_weight,second_weight)
            paths[next_cells,last_cells]=weight
            final[last_cells]=r.merge(final.get(last_cells,r.brc.CWM_ZERO),weight)
    return {'first_field':first_field,'retired':retired,'first_law':first_law,
            'first_branches':first_branches,'second_arrival_rows':rows,
            'paths':paths,'final_law':final,'second_resolution_branches':branch_count}


def l1_contrast(left,right):
    """Observer-only contrast of TWO positive carriers, never physical mass."""
    return sum((abs(left.get(k,r.brc.CWM_ZERO).total-right.get(k,r.brc.CWM_ZERO).total)
                for k in left.keys()|right.keys()),Q(0))


def tv_contrast(left,right):
    return l1_contrast(left,right)/2


def geometric_budget(value,rho,kappa,depth=1,horizon=None):
    """Actual one-state positive BRC comparison path-series certificate.

    value is a nonnegative total-response or norm-bound observation, not a
    signed field. At depth1 the next experiment first propagates, then queries.
    The bound may exceed one; callers cap it for a probability/TV bound.
    """
    if value<0 or not 0<rho<1 or kappa<=0 or depth<0:
        raise ValueError('invalid bound input')
    r.CALLS['one_state_recurrent_cwm']+=1
    series=r.brc.one_state_recurrent_cwm([rho])
    initial=r.serial(r.edge(value) if value else r.brc.CWM_ZERO,r.edge(1/kappa))
    if horizon is None:
        return r.serial(r.serial(initial,series.depth(depth)),
                        r.edge(series.total_mass_closure)).total
    if horizon<0:
        raise ValueError('negative horizon')
    return r.total(r.serial(initial,series.depth(n)) for n in range(depth,depth+horizon)).total


def two_sector_budget(initial_live,initial_dormant,rho,release,steps):
    """Exact positive-BRC sector recurrence, not a matrix-exponential solver."""
    if initial_live < 0 or initial_dormant < 0:
        raise ValueError('negative initial response')
    live = r.edge(initial_live) if initial_live else r.brc.CWM_ZERO
    store = r.edge(initial_dormant) if initial_dormant else r.brc.CWM_ZERO
    keep_live, retire = r.edge(rho), r.edge(1-rho)
    awaken, keep_store = r.edge(release), r.edge(1-release)
    out=[(live,store)]; emissions=[]
    for _ in range(steps):
        returned=r.serial(store,awaken); emissions.append(returned)
        live,store=(r.merge(r.serial(live,keep_live),returned),
                    r.merge(r.serial(live,retire),r.serial(store,keep_store)))
        out.append((live,store))
    return out,emissions
