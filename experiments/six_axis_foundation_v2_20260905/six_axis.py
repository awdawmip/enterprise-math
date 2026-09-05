"""Six-axis derived atlas v1. Exact counts/flags; NOT native Cell ontology.

Uses the unchanged 2026-09-05 atlas_brc implementation. All arithmetic here is
integer/rational. Frame actions and chart-sign transport are distinct types.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Mapping, Sequence
from vendor import atlas_brc as brc

EDGES, STARS, GROUP = brc.EDGES, brc.STARS, brc.GROUP
IDENTITY = brc.IDENTITY
TETRA = ((1,-1,-1), (-1,1,-1), (-1,-1,1), (1,1,1))
FLAGS = tuple((v,e) for v in range(4) for e in STARS[v])


def integers(values, size):
    out = tuple(values)
    if len(out) != size or any(type(x) is not int for x in out):
        raise ValueError(f'expected {size} exact integers')
    return out


def vertex(v):
    if type(v) is not int or not 0 <= v < 4:
        raise ValueError('chart vertex must be an integer from 0 to 3')
    return v


def parity(g):
    g = brc.permutation(g)
    return (-1)**sum(g[i]>g[j] for i in range(4) for j in range(i+1,4))


def rotation_matrix(g):
    """Proper FCC carrier rotation. Not a native six-dimensional matrix."""
    g = brc.permutation(g)
    a = tuple(tuple(parity(g)*sum(TETRA[g[v]][i]*TETRA[v][j]
                                 for v in range(4)) for j in range(3))
              for i in range(3))
    if any(x % 4 for row in a for x in row):
        raise AssertionError('tetrahedral matrix must be integral after /4')
    return tuple(tuple(x//4 for x in row) for row in a)


def flag_ray(v, edge):
    """Integer FCC ray for an incidence flag; native negative axes not used."""
    vertex(v)
    if type(edge) is not int or edge not in STARS[v]:
        raise ValueError('edge is not incident to the chart')
    u,w = EDGES[edge]
    other = w if v == u else u
    a,b = TETRA[v], TETRA[other]
    c = (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
         a[0]*b[1]-a[1]*b[0])
    return tuple(-x//2 for x in c)


def rotate_flag(v, edge, g):
    flag_ray(v,edge)  # strict domain validation
    g = brc.permutation(g)
    return g[v], brc.edge_action(g)[edge]


def _signs(values, size):
    out = integers(values,size)
    if any(x not in (-1,1) for x in out):
        raise ValueError('signs must be exact +1 or -1')
    return out


@dataclass(frozen=True)
class ChartSignConnection:
    """Scalar sign bundle on the chart graph, NOT native spatial transport."""
    signs: tuple[int,...] = (-1,)*6

    def __post_init__(self):
        object.__setattr__(self,'signs',_signs(self.signs,6))

    def gauge(self, eps):
        eps = _signs(eps,4)
        return ChartSignConnection(tuple(eps[u]*self.signs[e]*eps[v]
                                         for e,(u,v) in enumerate(EDGES)))

    def walk_product(self, walk, *, closed=True):
        walk = tuple(vertex(v) for v in walk)
        if not walk or (closed and walk[0] != walk[-1]):
            raise ValueError('nonempty closed chart walk required')
        s = 1
        for u,v in zip(walk,walk[1:]):
            if u == v:
                raise ValueError('chart graph has no loop edges')
            s *= self.signs[brc.EDGE_INDEX[tuple(sorted((u,v)))]]
        return s

    def double_cover(self):
        states = tuple((v,s) for v in range(4) for s in (-1,1))
        edges = frozenset(frozenset(((u,s),(v,s*self.signs[e])))
                          for e,(u,v) in enumerate(EDGES) for s in (-1,1))
        return states,edges


def normalize_counts(n):
    """Return common min-zero SIX-count residual and separate depth."""
    n = brc.naturals(n,6)
    h = min(n)
    return tuple(x-h for x in n),h


def local_charts(n):
    n = brc.naturals(n,6)
    return tuple(tuple(n[e]-min(n[f] for f in star) for e in star)
                 for star in STARS)


def _parse_charts(charts: Mapping[int,Sequence[int]]):
    if not isinstance(charts,Mapping) or len(charts) not in (3,4):
        raise ValueError('three or four labeled charts are required')
    out = {}
    for v,values in charts.items():
        vertex(v)
        values = brc.naturals(values,3)
        if min(values) != 0:
            raise ValueError('each input chart must have minimum zero')
        out[v] = dict(zip(STARS[v],values))
    return out


def reconstruct(charts: Mapping[int,Sequence[int]]):
    """Unique min-zero six-count lift, or ValueError with a cycle witness.

    Each triple is ordered by STARS[v]. Works with any THREE of the four
    stars, or all four. The omitted chart is reconstructed, not set to zero.
    This is a derived count-observer lift, not a native Cell decoder.
    """
    d = _parse_charts(charts)
    root = min(d)
    m = {root:0}
    for v in d:
        if v != root:
            e = brc.EDGE_INDEX[tuple(sorted((root,v)))]
            m[v] = d[root][e]-d[v][e]
    for u,v in combinations(sorted(d),2):
        e = brc.EDGE_INDEX[(u,v)]
        defect = d[u][e]-d[v][e] - (m[v]-m[u])
        if defect:
            raise ValueError(f'incompatible chart cycle through {root},{u},{v}: defect={defect}')
    raw = []
    for e,(u,v) in enumerate(EDGES):
        w = u if u in d else v
        raw.append(d[w][e]+m[w])
    bottom = min(raw)
    return tuple(x-bottom for x in raw)


@dataclass(frozen=True)
class CountAtlas:
    """Lossless normalized-chart encoding of N^6, with retained common depth.

    This is NOT an assertion that all N^6 are admissible native Cell addresses.
    """
    charts: tuple[tuple[int,...],...]
    depth: int

    def __post_init__(self):
        charts = tuple(tuple(c) for c in self.charts)
        if len(charts) != 4:
            raise ValueError('four complete charts required')
        brc.naturals((self.depth,),1)
        reconstruct(dict(enumerate(charts)))
        object.__setattr__(self,'charts',charts)

    @classmethod
    def encode(cls,n):
        n = brc.naturals(n,6)
        return cls(local_charts(n),min(n))

    def decode(self):
        n0 = reconstruct(dict(enumerate(self.charts)))
        return tuple(x+self.depth for x in n0)

    def rotate(self,g):
        """Direct chart/flag relabeling, independent of decode-encode."""
        g = brc.permutation(g)
        eg = brc.edge_action(g)
        rows = [[0]*3 for _ in range(4)]
        for v,star in enumerate(STARS):
            for e,x in zip(star,self.charts[v]):
                rows[g[v]][STARS[g[v]].index(eg[e])] = x
        return CountAtlas(tuple(tuple(r) for r in rows),self.depth)

    def add_in_frame(self,other,g=IDENTITY):
        if not isinstance(other,CountAtlas):
            raise TypeError('expected CountAtlas')
        m = brc.rotate_axes(other.decode(),g)
        return CountAtlas.encode(tuple(a+b for a,b in zip(self.decode(),m)))


def depth_carry(r,s,g=IDENTITY):
    """Common-depth carry; distinct from the old optimal-extraction K-carry."""
    r,s = brc.naturals(r,6),brc.naturals(s,6)
    if min(r) or min(s):
        raise ValueError('carry requires min-zero six-count residuals')
    return min(a+b for a,b in zip(r,brc.rotate_axes(s,g)))


@dataclass(frozen=True)
class TypedArrow:
    """Source/target-typed BRC descriptor; an observer, not full path history."""
    source: str
    target: str
    key: brc.BranchKey

    def __post_init__(self):
        if not isinstance(self.source,str) or not isinstance(self.target,str):
            raise TypeError('state names must be strings')
        if not isinstance(self.key,brc.BranchKey):
            raise TypeError('key must be the pinned BranchKey type')

    def then(self,other):
        if not isinstance(other,TypedArrow):
            raise TypeError('expected TypedArrow')
        if self.target != other.source:
            raise ValueError('path endpoints do not compose')
        return TypedArrow(self.source,other.target,self.key.then(other.key))


def arrow_product(left,right):
    """Category-algebra product: noncomposable pairs contribute zero."""
    for h in (left,right):
        if any(not isinstance(k,TypedArrow) or type(c) is not int or c<=0
               for k,c in h.items()):
            raise ValueError('typed arrows and positive integer multiplicities required')
    out = {}
    for x,c in left.items():
        for y,d in right.items():
            if x.target == y.source:
                z = x.then(y)
                out[z] = out.get(z,0)+c*d
    return out


def quadratic_extension(n,c=Fraction(0)):
    """CONDITIONAL derived quadratic family, never the canonical native metric."""
    n = integers(n,6)
    if isinstance(c,bool) or not isinstance(c,(int,Fraction)):
        raise TypeError('c must be exact rational')
    c = Fraction(c)
    if not -1 < c < 1:
        raise ValueError('positive definite extension requires -1<c<1')
    return sum(x*x for x in n)+2*c*(n[0]*n[5]+n[1]*n[4]+n[2]*n[3])


def verify_finite_axis_lift(state_count, transitions, actions):
    """Exhaustive finite model verifier, not a native 6D existence certificate.

    transitions=(source,axis_index,target); actions maps each S4 element to
    a permutation of states. Checks the WHOLE action, not just carrier rays.
    """
    if type(state_count) is not int or state_count<1:
        raise ValueError('positive state count required')
    if set(actions) != set(GROUP):
        raise ValueError('all 24 labeled group actions required')
    acts = {}
    for g,p in actions.items():
        brc.permutation(g)
        p = integers(p,state_count)
        if set(p) != set(range(state_count)):
            raise ValueError('state action is not a permutation')
        acts[g] = p
    if acts[IDENTITY] != tuple(range(state_count)):
        raise ValueError('identity action failure')
    edges = set()
    for edge in transitions:
        i,e,j = integers(edge,3)
        if not(0<=i<state_count and 0<=j<state_count and 0<=e<6):
            raise ValueError('invalid labeled transition')
        edges.add((i,e,j))
    for g in GROUP:
        for h in GROUP:
            if tuple(acts[g][acts[h][i]] for i in range(state_count)) != acts[brc.compose(g,h)]:
                raise ValueError(f'group composition failure: {g},{h}')
        eg = brc.edge_action(g)
        moved = {(acts[g][i],eg[e],acts[g][j]) for i,e,j in edges}
        if moved != edges:
            raise ValueError(f'adjacency/axis covariance failure: {g}')
    return {'group_state_checks':576*state_count,'transition_checks':24*len(edges)}


def verify_finite_brc_lift(state_count, branches, state_actions, branch_actions):
    """Exact lift audit for named positive-weight branch OCCURRENCES.

    branches maps a unique string ID to (source,axis_index,target,weight).
    branch_actions[g] is the permutation of branch positions in insertion
    order. Preserves the full multigraph, not merely its support relation.
    Weights here are fixed exact rationals and must be rotation-invariant.
    """
    if not isinstance(branches,Mapping) or not branches or any(not isinstance(k,str) for k in branches):
        raise ValueError('nonempty mapping of unique string branch IDs required')
    records=[]
    for bid,record in branches.items():
        record=tuple(record)
        if len(record)!=4:
            raise ValueError('branch requires source,axis,target,weight')
        i,e,j=integers(record[:3],3)
        w=record[3]
        if isinstance(w,bool) or not isinstance(w,(int,Fraction)) or w<=0:
            raise ValueError('branch weights must be positive exact rationals')
        records.append((i,e,j,Fraction(w)))
    result=verify_finite_axis_lift(state_count,[r[:3] for r in records],state_actions)
    if set(branch_actions)!=set(GROUP):
        raise ValueError('all 24 branch actions required')
    M=len(records);actions={}
    for g,p in branch_actions.items():
        brc.permutation(g)
        p=integers(p,M)
        if set(p)!=set(range(M)):
            raise ValueError('branch action is not a permutation')
        actions[g]=p
    if actions[IDENTITY]!=tuple(range(M)):
        raise ValueError('identity branch action failure')
    for g in GROUP:
        for h in GROUP:
            if tuple(actions[g][actions[h][i]] for i in range(M))!=actions[brc.compose(g,h)]:
                raise ValueError('branch group composition failure')
        eg=brc.edge_action(g)
        for pos,(i,e,j,w) in enumerate(records):
            if records[actions[g][pos]]!=(state_actions[g][i],eg[e],state_actions[g][j],w):
                raise ValueError('branch occurrence/weight covariance failure')
    result.update({'branch_group_checks':576*M,'branch_covariance_checks':24*M})
    return result
