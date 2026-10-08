"""U9 candidate auxiliary-path dynamics, not a native force law.

A microstate keeps a labelled spanning tree and, for each link, two ordered
native paths ending at the same meeting Cell.  Endpoint motion is local;
trail editing/rewiring is an explicit algorithm, not calibrated transmission.
All scientific weights use the unchanged U8 -> U2 -> weighted-BRC chain.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
import hashlib, importlib.util, sys

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'connected_retention.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261008_cell_u8_connected_retention_5e91c4'/'connected_retention.py'
raw=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!='569e6171d0052fbfd41cf007b09a8327b339228b':
    raise RuntimeError('U8 dependency pin mismatch')
spec=importlib.util.spec_from_file_location('u9_pinned_u8',SRC)
u=importlib.util.module_from_spec(spec);sys.modules[spec.name]=u;spec.loader.exec_module(u)
r=u.r
Cell=tuple[int,...]
Word=tuple[int,...]


def endpoint(start:Cell,word:Word)->Cell:
    z=start
    for p in word:
        if type(p) is not int or p not in r.PORTS:raise ValueError('bad native port')
        z=r.advance(z,p)
    return z


def straight_word(a:Cell,b:Cell)->Word:
    # Declared ordered coordinate path, never a primitive diagonal.
    return tuple(p for j,(x,y) in enumerate(zip(a,b))
                 for p in [2*j+int(y<x)]*abs(y-x))


@dataclass(frozen=True)
class State:
    cells:tuple[Cell,...]
    # Each record is (i,j,word from i,word from j), with i<j.
    links:tuple[tuple[int,int,Word,Word],...]

    def table(self):return {(i,j):(a,b) for i,j,a,b in self.links}
    def length(self):return sum(len(a)+len(b) for i,j,a,b in self.links)
    def tree(self):return tuple((i,j) for i,j,a,b in self.links)


def make(cells,table)->State:
    return State(tuple(cells),tuple((i,j,tuple(a),tuple(b))
                 for (i,j),(a,b) in sorted(table.items())))


def validate(s:State)->None:
    u.validate_cells(s.cells);N=len(s.cells)
    if len(s.links)!=N-1 or len(s.table())!=N-1:raise ValueError('not tree-size')
    parent=list(range(N))
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    for i,j,a,b in s.links:
        if not 0<=i<j<N:raise ValueError('bad identities')
        ii,jj=root(i),root(j)
        if ii==jj:raise ValueError('cycle')
        parent[ii]=jj
        if endpoint(s.cells[i],a)!=endpoint(s.cells[j],b):raise ValueError('meeting mismatch')


def from_tree(cells,T,meeting=None)->State:
    """Explicitly prepared witness, not a selected physical state."""
    table={}
    for i,j in T:
        z=cells[j] if meeting is None else meeting
        table[i,j]=(straight_word(cells[i],z),straight_word(cells[j],z))
    s=make(cells,table);validate(s);return s


def material(s:State,a:int,p:int,grow:bool)->State|None:
    """Move a by ONE native edge. Every incident first leg is updated.

    Grow prepends -p at the new location; shrink needs common prefix +p.
    Reverse label is (a,-p,not grow). Other materials/meetings stay put.
    """
    new=r.advance(s.cells[a],p)
    if new in s.cells:return None
    table=s.table()
    for e,ww in tuple(table.items()):
        if a not in e:continue
        k=e.index(a);w=ww[k]
        if not grow and (not w or w[0]!=p):return None
        changed=(p^1,)+w if grow else w[1:]
        out=list(ww);out[k]=changed;table[e]=tuple(out)
    cells=list(s.cells);cells[a]=new
    return make(cells,table)


def meeting(s:State,e:tuple[int,int],p:int,grow:bool)->State|None:
    """Append/pop the same final edge on both legs. Reverse has same p."""
    table=s.table()
    if e not in table:return None
    a,b=table[e]
    if grow:table[e]=(a+(p,),b+(p,))
    elif a and b and a[-1]==b[-1]==p:table[e]=(a[:-1],b[:-1])
    else:return None
    return make(s.cells,table)


def detour(s:State,e:tuple[int,int],side:int,j:int,p:int,grow:bool)->State|None:
    """Insert/pop a backtrack at fixed word index j; reverse same j,p.

    Proposal index is geometric independently of current length. Uniformly
    selecting existing positions would need a nontrivial Hastings factor.
    """
    if j<0:raise ValueError('negative index')
    table=s.table()
    if e not in table:return None
    ww=list(table[e]);w=ww[side]
    if grow:
        if j>len(w):return None
        ww[side]=w[:j]+(p,p^1)+w[j:]
    elif w[j:j+2]==(p,p^1):ww[side]=w[:j]+w[j+2:]
    else:return None
    table[e]=tuple(ww);return make(s.cells,table)


def commute(s:State,e:tuple[int,int],side:int,j:int)->State|None:
    """Exchange two adjacent DIFFERENT-axis steps; native path relation."""
    table=s.table()
    if e not in table:return None
    ww=list(table[e]);w=ww[side]
    if j<0 or j+1>=len(w) or r.axis(w[j])==r.axis(w[j+1]):return None
    ww[side]=w[:j]+(w[j+1],w[j])+w[j+2:]
    table[e]=tuple(ww);return make(s.cells,table)


def slide(s:State,a:int,b:int,c:int)->State|None:
    """Tree slide ab,bc -> ac,bc when the two b legs are identical.

    This tests/reassigns relation records, NOT a certified three-force event.
    The shared trail and a common meeting are necessary witness data. Reverse
    (a,c,b) reconstructs the removed b leg from the retained bc record.
    """
    if len({a,b,c})!=3:return None
    table=s.table();ab=tuple(sorted((a,b)));bc=tuple(sorted((b,c)));ac=tuple(sorted((a,c)))
    if ab not in table or bc not in table or ac in table:return None
    if table[ab][ab.index(b)]!=table[bc][bc.index(b)]:return None
    wa=table[ab][ab.index(a)];wc=table[bc][bc.index(c)]
    del table[ab];table[ac]=(wa,wc) if a<c else (wc,wa)
    return make(s.cells,table)


class Weights:
    def __init__(self,lam=Q(1,48)):
        if not 0<lam<Q(1,12):raise ValueError('U8 summability range')
        self.lam=lam;self.unit=r.edge(lam);self.cache={0:r.brc.CWM_ONE}
    def power(self,n):
        if n<0:raise ValueError('negative physical-path count')
        while n not in self.cache:
            k=len(self.cache);self.cache[k]=r.serial(self.cache[k-1],self.unit)
        return self.cache[n]
    def weight(self,s):return self.power(s.length())
    def decision(self,delta):
        """Positive accept/reject weights from changed segment only.

        The exponent difference is an OBSERVER. No negative-length path or
        signed response is fed to BRC. Common factors have a proved ratio
        cancellation; unaffected path records are not deleted from state.
        """
        small=self.power(abs(delta));one=r.brc.CWM_ONE
        yes,no=(small,one) if delta>=0 else (one,small)
        normalizer=r.edge(1/r.merge(yes,no).total)
        return r.serial(yes,normalizer),r.serial(no,normalizer)


def position_query(s:State,weights:Weights,material_share=Q(1,4)):
    """EXACT one-query position law of the four-channel kernel.

    Meeting/word/slide channels do not move actors; aggregate them only for
    this position observer. Original grammar is required for future queries.
    No global K,W,Z or cutoff is evaluated here.
    """
    validate(s);N=len(s.cells);q=r.edge(material_share/Q(24*N))
    law={s.cells:r.edge(1-material_share)};rows=[]
    for a in range(N):
        for p in r.PORTS:
            for grow in (False,True):
                y=material(s,a,p,grow)
                if y is None:
                    law[s.cells]=r.merge(law[s.cells],q)
                    rows.append((a,p,grow,'INELIGIBLE',q));continue
                accept,reject=weights.decision(y.length()-s.length())
                wa,wr=r.serial(q,accept),r.serial(q,reject)
                law[y.cells]=r.merge(law.get(y.cells,r.brc.CWM_ZERO),wa)
                law[s.cells]=r.merge(law[s.cells],wr)
                rows.append((a,p,grow,y,wa,wr))
    return law,rows


def encode(x):
    if isinstance(x,State):return {'cells':x.cells,'links':x.links,'length':x.length()}
    if isinstance(x,r.brc.CWMState):return u.info(x)
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x
