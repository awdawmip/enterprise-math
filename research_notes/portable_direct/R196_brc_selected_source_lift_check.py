#!/usr/bin/env python3
"""R196: exact source-observer lift of BRC EffectHistogram.

Runs against the real enterprise_math.brc_transport when it is installed;
otherwise --reference uses an independently coded Fraction-exact API mirror.
The reported backend always discloses which implementation actually ran.
No floating point, stochastic input, or unpublished native execution is assumed.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import permutations
import json


def reference_backend():
    @dataclass(frozen=True, order=True)
    class Affine:
        a: tuple[tuple[F, ...], ...]
        b: tuple[F, ...]

        @classmethod
        def identity(cls, n):
            return cls(tuple(tuple(F(i == j) for j in range(n)) for i in range(n)), (F(0),) * n)

        @property
        def dim(self):
            return len(self.b)

        def apply(self, x):
            return tuple(sum((a*y for a, y in zip(row, x)), F(0)) + z for row,z in zip(self.a,self.b))

        def then(self, later):
            n = self.dim
            assert n == later.dim
            mat = tuple(tuple(sum((later.a[i][h]*self.a[h][j] for h in range(n)), F(0))
                              for j in range(n)) for i in range(n))
            return Affine(mat, later.apply(self.b))

    @dataclass(frozen=True)
    class EffectHistogram:
        dim: int
        entries: tuple

        @classmethod
        def from_terms(cls, dim, terms):
            counts = defaultdict(int)
            for w, a, c in terms:
                assert F(w)>0 and a.dim==dim and isinstance(c,int) and c>=0
                if c: counts[(F(w),a)]+=c
            return cls(dim, tuple((w,a,c) for (w,a),c in sorted(counts.items())))

        def alternatives(self, other):
            assert self.dim == other.dim
            return self.from_terms(self.dim,self.entries+other.entries)

        def then(self, other):
            assert self.dim == other.dim
            return self.from_terms(self.dim,((w*v,a.then(b),c*d)
                for w,a,c in self.entries for v,b,d in other.entries))
    return Affine,EffectHistogram


def states(k):
    yield ()
    for r in range(1,k+1):
        yield from permutations(range(k),r)


def star(u,v):
    other=set(v)
    return tuple(i for i in u if i not in other)+tuple(v)


def features(k):
    return [(i,) for i in range(k)] + [(i,j) for i in range(k) for j in range(i+1,k)]


def bits(s,k):
    out=[]
    for U in features(k):
        current=next((u for u in reversed(s) if u in U),None)
        if current is None: out.append(1)
        else: out.append(0 if len(U)==1 or current==U[0] else 1)
    return tuple(out)


def decode(v,k):
    U=features(k); flags=v[:k]
    seen=[i for i in range(k) if flags[i]==0]
    pair_values={tuple(a):v[idx] for idx,a in enumerate(U) if len(a)==2}
    def cmp(a,b):
        lo,hi=sorted((a,b))
        later=lo if pair_values[(lo,hi)]==0 else hi
        return 1 if a==later else -1
    return tuple(sorted(seen,key=cmp_to_key(cmp)))


def reset_affine(Affine,s,k):
    d=len(features(k))
    status=[None]*d
    for i in s:
        for f, U in enumerate(features(k)):
            if i in U: status[f]=0 if len(U)==1 or i==U[0] else 1
    a=tuple(tuple(F(int(status[i] is None and i==j)) for j in range(d)) for i in range(d))
    b=tuple(F(x or 0) for x in status)
    return Affine(a,b)


def block(Affine,physical,observer):
    n=physical.dim;d=observer.dim
    zero_n=(F(0),)*n;zero_d=(F(0),)*d
    return Affine(tuple(row+zero_d for row in physical.a)+
                  tuple(zero_n+row for row in observer.a),physical.b+observer.b)


def truncate(Affine,joined,n):
    return Affine(tuple(row[:n] for row in joined.a[:n]),joined.b[:n])


def tag_hist(Affine,terms):
    counts=defaultdict(int)
    for w,a,c,s in terms:
        assert isinstance(w,(int,F)) and F(w)>0 and a.dim>=1 and c>=0
        if c: counts[(F(w),a,tuple(s))]+=c
    return counts


def tag_alt(h,j):
    out=defaultdict(int,h)
    for key,c in j.items():out[key]+=c
    return out


def tag_then(h,j):
    out=defaultdict(int)
    for (w,a,s),c in h.items():
        for (v,b,t),d in j.items():
            out[(w*v,a.then(b),star(s,t))]+=c*d
    return out


def forget(EffectHistogram,n,tag):
    return EffectHistogram.from_terms(n,((w,a,c) for (w,a,s),c in tag.items()))


def lift(Affine,EffectHistogram,n,k,tag):
    dim=n+len(features(k))
    for (_w,a,s),_c in tag.items():
        if a.dim != n or len(set(s)) != len(s) or any(not isinstance(i,int) or not 0<=i<k for i in s):
            raise ValueError('invalid tagged source word or physical dimension')
    return EffectHistogram.from_terms(dim,((w,block(Affine,a,reset_affine(Affine,s,k)),c)
                                                for (w,a,s),c in tag.items()))


def project(Affine,EffectHistogram,n,packet):
    return EffectHistogram.from_terms(n,((w,truncate(Affine,a,n),c) for w,a,c in packet.entries))


def recover(Affine,packet,n,k):
    out=defaultdict(int)
    for w,a,c in packet.entries:
        s=decode(a.apply((F(0),)*n+(F(1),)*len(features(k)))[n:],k)
        physical=truncate(Affine,a,n)
        if a != block(Affine,physical,reset_affine(Affine,s,k)):
            raise ValueError('noncanonical or cross-coupled BRC lift')
        out[(w,physical,s)]+=c
    return out


def run(Affine,EffectHistogram,backend):
    totals={'states':0,'unique_orbits':0,'generator_appends':0,'ordered_products':0}
    rows=[]
    for k in range(1,6):
        S=list(states(k)); d=len(features(k)); seen=set()
        for s in S:
            v=bits(s,k); assert decode(v,k)==s
            seen.add(v)
            I=Affine.identity(d)
            R=reset_affine(Affine,s,k)
            assert R.apply((F(1),)*d)==v
            for i in range(k):
                x=reset_affine(Affine,(i,),k)
                assert R.then(x)==reset_affine(Affine,star(s,(i,)),k)
                totals['generator_appends']+=1
        assert len(seen)==len(S)
        if k<=4:
            reset={s:reset_affine(Affine,s,k) for s in S}
            for s in S:
                for t in S:
                    assert reset[s].then(reset[t)]==reset[star(s,t)]
                    totals['ordered_products']+=1
        totals['states']+=len(S);totals['unique_orbits']+=len(seen)
        rows.append({'k':k,'d':d,'states':len(S)})
    k=3;n=1
    I=Affine.identity(n)
    shift=Affine(((F(1),),),(F(1),))
    scale=Affine(((F(2),),),(F(1),))
    h=tag_hist(Affine,[(F(1,2),I,2,(0,1)),(F(3,2),shift,1,(1,))])
    j=tag_hist(Affine,[(F(2,3),scale,3,(2,0)),(F(1),I,2,(0,))])
    LH=lift(Affine,EffectHistogram,n,k,h)
    LJ=lift(Affine,EffectHistogram,n,k,j)
    assert recover(Affine,LH,n,k)==h
    assert recover(Affine,LJ,n,k)==j
    assert project(Affine,EffectHistogram,n,LH)==forget(EffectHistogram,n,h)
    assert lift(Affine,EffectHistogram,n,k,tag_alt(h,j))==LH.alternatives(LJ)
    assert lift(Affine,EffectHistogram,n,k,tag_then(h,j))==LH.then(LJ)
    assert project(Affine,EffectHistogram,n,LH.then(LJ)) == forget(EffectHistogram,n,h).then(forget(EffectHistogram,n,j))
    # A one-atom native histogram loses the difference between a and b.
    ca=tag_hist(Affine,[(F(1),I,1,(0,))]);cb=tag_hist(Affine,[(F(1),I,1,(1,))])
    assert forget(EffectHistogram,n,ca)==forget(EffectHistogram,n,cb)
    assert ca!=cb
    # Same physical marginal AND same source marginal; different joint correlation.
    cross1=tag_hist(Affine,[(F(1),I,1,(0,)),(F(1),shift,1,(1,))])
    cross2=tag_hist(Affine,[(F(1),I,1,(1,)),(F(1),shift,1,(0,))])
    assert forget(EffectHistogram,n,cross1)==forget(EffectHistogram,n,cross2)
    def marg(h):
        o=defaultdict(int)
        for (w,a,s),c in h.items():o[s]+=c
        return o
    assert marg(cross1)==marg(cross2)
    def conditioned(h):
        o=defaultdict(int)
        for (w,a,s),c in h.items():o[(a.apply((F(0),)),s,w)]+=c
        return o
    assert conditioned(cross1)!=conditioned(cross2)
    assert recover(Affine,lift(Affine,EffectHistogram,n,k,cross1),n,k)==cross1
    assert recover(Affine,lift(Affine,EffectHistogram,n,k,cross2),n,k)==cross2
    return {'schema':'EM_R196_BRC_SOURCE_LIFT_EXACT_V1','status':'PASS',
            'backend':backend,'frozen_scientific_input':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
            'arithmetic':'Fractions and integer tuple enumeration; no floats',
            'rows':rows,'totals':totals,
            'native_api_laws_checked':['Affine.then','EffectHistogram.from_terms','alternatives','then','positive rational weights','multiplicity'],
            'conditional_counterexamples':['single-atom physical fiber','two-by-two joint correlation'],
            'native_integration_executed':backend=='enterprise_math.brc_transport',
            'limitation':'reference backend mirrors stated methods, native package integration requires --native run in installed project' if backend!='enterprise_math.brc_transport' else 'native installed module verified'}


def main():
    p=argparse.ArgumentParser();p.add_argument('--reference',action='store_true');p.add_argument('--native',action='store_true');args=p.parse_args()
    if args.reference and args.native: p.error('choose exactly one execution backend')
    if not args.reference:
        try:
            from enterprise_math.brc_transport import Affine,EffectHistogram
            backend='enterprise_math.brc_transport'
        except ImportError:
            if args.native:raise
            Affine,EffectHistogram=reference_backend();backend='exact_reference_mirror'
    else:
        Affine,EffectHistogram=reference_backend();backend='exact_reference_mirror'
    print(json.dumps(run(Affine,EffectHistogram,backend),ensure_ascii=False,indent=2))
if __name__=='__main__':main()
