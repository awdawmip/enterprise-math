"""U11 finite identified resources: counting and local material-prefix transfer.

Resource units are declared record resources, NOT primitive force quanta.
Resource phases are auxiliary labels, NOT extra spatial dimensions.  Every
scientific sum/product uses the unchanged pinned U9 -> U8 -> U2 -> BRC chain.
The implemented transport is one isolated material grow/shrink transaction;
it is not a distributed implementation of every U9 channel.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from itertools import permutations, product
import hashlib, importlib.util, sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'local_latent.py'
if not SRC.exists():
    SRC = ROOT.parent / '20261008_cell_u9_local_latent_4b7e62' / 'local_latent.py'
raw = SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() != '67408af5b977bed7295f7225cdd3f550c41b9729':
    raise RuntimeError('U9 source pin mismatch')
spec = importlib.util.spec_from_file_location('u11_pinned_u9', SRC)
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m
spec.loader.exec_module(m)
r,u = m.r,m.u
ZERO,ONE = r.brc.CWM_ZERO,r.brc.CWM_ONE


def count_family(n: int):
    """n distinct unit alternatives: preserves count, total and dominant."""
    if type(n) is not int or n < 0: raise ValueError('nonnegative count')
    return r.total(ONE for _ in range(n))


def multiplicity(B: int, L: int, q: int):
    """(B)_L q^(B-L) actual labelled-inventory counting family."""
    if type(B) is not int or type(L) is not int or B < 0 or L < 0:
        raise ValueError('nonnegative inventory and length')
    if type(q) is not int or q < 1: raise ValueError('positive alphabet size')
    if L > B: return ZERO
    ans=ONE
    for k in range(L): ans=r.serial(ans,count_family(B-k))
    choices=count_family(q)
    for _ in range(B-L): ans=r.serial(ans,choices)
    return ans


def ratio_family(B: int,L: int,d: int,q: int):
    """Number of distinct new allocations versus released free phase words."""
    if min(B,L,d)<0 or q<1 or L>B: raise ValueError('bad inventory')
    choices=ONE;phases=ONE
    for k in range(d):
        choices=r.serial(choices,count_family(max(0,B-L-k)))
        phases=r.serial(phases,count_family(q))
    return choices,phases


def depletion(B: int,L: int):
    """(B)_L/B^L as a positive without-replacement acceptance observer."""
    if B<1 or L<0: raise ValueError('B>=1 and L>=0')
    ans=ONE
    for k in range(L):
        if k>=B:return ZERO
        ans=r.serial(ans,r.edge(Q(B-k,B)))
    return ans


@dataclass(frozen=True)
class Inventory:
    """One token assignment per ordered path occurrence, plus free phases.

    Bound tokens are in the unique assembly phase. Free tokens have q labels;
    only phase0 may bind. Other labels never get erased on binding.
    Tuple order of paths is the existing sorted U9 link/side order.
    """
    state: m.State
    tokens: tuple[tuple[int,...],...]
    free: tuple[tuple[int,int],...]
    B: int
    q: int
    reservoir_cell: tuple[int,...]


def paths(s):
    return tuple(w for i,j,a,b in s.links for w in (a,b))


def validate(s: Inventory):
    m.validate(s.state)
    u.canonical(s.reservoir_cell)
    if type(s.B) is not int or s.B<0 or type(s.q) is not int or s.q<1:
        raise ValueError('invalid capacity/alphabet')
    ww=paths(s.state)
    if len(s.tokens)!=len(ww) or any(len(t)!=len(w) for t,w in zip(s.tokens,ww)):
        raise ValueError('each occurrence needs exactly one resource')
    bound=[t for leg in s.tokens for t in leg]
    free=dict(s.free)
    if len(free)!=len(s.free) or any(not 0<=v<s.q for v in free.values()):
        raise ValueError('duplicate or invalid free phase')
    if len(set(bound))!=len(bound) or set(bound)&set(free):
        raise ValueError('resource copied or multiply allocated')
    if set(bound)|set(free)!=set(range(s.B)):
        raise ValueError('resource missing or invented')
    if tuple(sorted(s.free))!=s.free:raise ValueError('canonical free table')


def prepared(state,B,q,free_phase=0,reservoir_cell=None):
    if state.length()>B or not 0<=free_phase<q:raise ValueError('insufficient resources')
    n=0;ts=[]
    for w in paths(state):ts.append(tuple(range(n,n+len(w))));n+=len(w)
    ans=Inventory(state,tuple(ts),tuple((i,free_phase) for i in range(n,B)),B,q,
                  state.cells[0] if reservoir_cell is None else reservoir_cell)
    validate(ans);return ans


def phase_shift(s: Inventory,token: int,shift: int):
    validate(s)
    if not 0<=token<s.B or not 0<=shift<s.q:raise ValueError('label outside universe')
    f=dict(s.free)
    if token in f:f[token]=(f[token]+shift)%s.q
    return Inventory(s.state,s.tokens,tuple(sorted(f.items())),s.B,s.q,s.reservoir_cell)


def incident_slots(state,a):
    return tuple(2*k+int(a==j) for k,(i,j,wa,wb) in enumerate(state.links) if a in (i,j))


def transaction(s: Inventory,a: int,p: int,grow: bool,chosen: tuple[int,...]):
    """Isolated resource transaction, all failures retain the original state.

    Grow reserves phase0 resources at the old actor Cell, carries them ONE
    edge with the material, then attaches the reverse prefixes locally.
    Shrink detaches those prefixes, carries the resources with the material
    to the old tail head, and deposits phase0 resources there. The reservoir
    is the explicitly declared Cell at that tail head; it is not teleported.
    During partial assembly the endpoint/head mismatches are retained.
    Trace ticks are protocol ticks, not force events or physical heartbeats.
    """
    validate(s)
    if not 0<=a<len(s.state.cells) or p not in r.PORTS:raise ValueError('bad material/port')
    js=incident_slots(s.state,a);d=len(js)
    if len(chosen)!=d or len(set(chosen))!=d or any(not 0<=t<s.B for t in chosen):
        raise ValueError('one distinct token per incident occurrence')
    y=m.material(s.state,a,p,grow)
    f=dict(s.free);ts=list(s.tokens)
    if y is None:return None,[]
    if grow and any(f.get(t)!=0 for t in chosen):return None,[]
    if not grow and any(not ts[j] or ts[j][0]!=t for j,t in zip(js,chosen)):return None,[]
    old=s.state.cells[a];new=y.cells[a]
    reservoir=old if grow else new
    if s.reservoir_cell!=reservoir:return None,[]
    heads=[s.state.cells[(i,j)[side]] for i,j,wa,wb in s.state.links for side in (0,1)]
    current_words=list(paths(s.state));physical=list(s.state.cells)
    held=[];trace=[];unit=r.edge(1);weight=ONE
    def emit(kind,token=None,hop=None):
        nonlocal weight
        weight=r.serial(weight,unit)
        bound=tuple(t for leg in ts for t in leg)
        # Existing meetings are compared to actual path heads, not replaced.
        mismatches=tuple(j for j in js if heads[j]!=physical[a])
        trace.append({'kind':kind,'token':token,'hop':hop,'material_cells':tuple(physical),
          'free':tuple(sorted(f.items())),'held':tuple(held),'bound':bound,
          'heads':tuple(heads),'words':tuple(current_words),'unattached_slots':mismatches,
          'reservoir_cell':reservoir,'trace_weight':weight})
    if grow:
        for t in chosen:
            del f[t];held.append(t);emit('RESERVE',t)
        physical[a]=new;emit('CARRY_ONE_EDGE',hop=(old,new))
        for j,t in zip(js,chosen):
            ts[j]=(t,)+ts[j];current_words[j]=(p^1,)+current_words[j];heads[j]=new
            held.remove(t);emit('ATTACH_PREFIX',t)
    else:
        for j,t in zip(js,chosen):
            ts[j]=ts[j][1:];current_words[j]=current_words[j][1:];heads[j]=new
            held.append(t);emit('DETACH_PREFIX',t)
        physical[a]=new;emit('CARRY_ONE_EDGE',hop=(old,new))
        for t in chosen:
            held.remove(t);f[t]=0;emit('RELEASE',t)
    out=Inventory(y,tuple(ts),tuple(sorted(f.items())),s.B,s.q,s.reservoir_cell)
    validate(out)
    if tuple(current_words)!=paths(y) or held:raise AssertionError('unfinished local update')
    return out,trace


def pair_universe(base,other,B,q):
    """Complete finite resource fibre above a declared two-configuration test."""
    ans=[]
    for state in (base,other):
        L=state.length()
        if L>B:continue
        for assigned in permutations(range(B),L):
            free_ids=tuple(sorted(set(range(B))-set(assigned)))
            ts=[];k=0
            for w in paths(state):ts.append(assigned[k:k+len(w)]);k+=len(w)
            for cols in product(range(q),repeat=B-L):
                item=Inventory(state,tuple(ts),tuple(zip(free_ids,cols)),B,q,base.cells[0])
                validate(item);ans.append(item)
    return tuple(ans)


def pair_step(s,base,other,kind,token,shift=0):
    """Fixed label universe: B grow, B shrink, and B*q phase-shift labels.

    Only the base->other material +E3 move and its inverse are enabled. All
    proposals outside that pair wait; this is NOT the full U9 four-channel law.
    Free-phase changes are declared reversible auxiliary operations, no energy
    equivalence or physical recharging cost is inferred.
    """
    if kind=='phase':return phase_shift(s,token,shift)
    if kind=='grow' and s.state==base:
        y,_=transaction(s,0,4,True,(token,));return y or s
    if kind=='shrink' and s.state==other:
        y,_=transaction(s,0,5,False,(token,));return y or s
    return s


def encode(x):
    if isinstance(x,Inventory):
        return {'state':m.encode(x.state),'tokens':x.tokens,'free':x.free,'B':x.B,'q':x.q,'reservoir_cell':x.reservoir_cell}
    if isinstance(x,dict):return {str(k):encode(w) for k,w in x.items()}
    if isinstance(x,(tuple,list)):return [encode(w) for w in x]
    return m.encode(x)
