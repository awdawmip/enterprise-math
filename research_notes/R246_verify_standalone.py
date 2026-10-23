#!/usr/bin/env python3
"""R246 exact standalone semantics checker (NOT an import of EM Source)."""
from __future__ import annotations
from dataclasses import dataclass
from itertools import product
import json

D = 6
M = tuple(tuple(int(i == j) for j in range(D)) for i in range(D))
ZERO = (0,)*D

@dataclass(frozen=True)
class Affine:
    a: tuple[tuple[int, ...], ...]
    b: tuple[int, ...]
    @classmethod
    def identity(cls): return cls(M, ZERO)
    def then(self, later):
        # self first, later second: later(self(x))
        A = tuple(tuple(sum(later.a[i][k]*self.a[k][j] for k in range(D)) for j in range(D)) for i in range(D))
        b = tuple(sum(later.a[i][k]*self.b[k] for k in range(D))+later.b[i] for i in range(D))
        return Affine(A, b)
    def at(self, x):
        return tuple(sum(self.a[i][j]*x[j] for j in range(D))+self.b[i] for i in range(D))
    def compact(self): return {'a':self.a,'b':self.b}

I = Affine.identity()
N = Affine(tuple(tuple(0 if (i==j==0) else M[i][j] for j in range(D)) for i in range(D)), ZERO)
C = Affine(M, (1,0,0,0,0,0))
R = Affine(tuple(tuple(-1 if (i==j==0) else M[i][j] for j in range(D)) for i in range(D)), ZERO)

# Control state index 8*x + 4*a + 2*c + r
def bit(s,k): return (s>>k)&1
def pi(s): return 4*bit(s,3)+2*(bit(s,2)^bit(s,1))+bit(s,0)
def G3(s): return s ^ (8*(bit(s,2)^bit(s,1)))
def G2(s): return s ^ (8*bit(s,0))
G = {'3':G3,'2':G2}
initial = tuple(pi(s) for s in range(16))

def make_effects(variant):
    es = {g:[I for _ in range(16)] for g in G}
    for s in (2,4):
        for g in G: es[g][s]=N
    if variant == 'delayed':
        for s in (10,12): es['2'][s]=C
    es['3'][12]=R
    assert es['3'][10]==I
    return es

def run(s, word, es):
    action=I
    for g in word:
        action=action.then(es[g][s])
        s=G[g](s)
    return pi(s),action

def witnesses(es,max_depth):
    answer={}
    for h in range(1,max_depth+1):
        for w in product(tuple(G),repeat=h):
            if run(2,w,es)!=run(4,w,es) and h not in answer:
                x0=run(2,w,es);x1=run(4,w,es)
                answer[h]={'word':''.join(w),'q2':x0[0],'q4':x1[0],
                           'at_origin_s2':x0[1].at(ZERO),'at_origin_s4':x1[1].at(ZERO)}
    return answer

def refinement(es):
    labels=initial
    rounds=[]
    while True:
        sig=[]
        for s in range(16):
            sig.append((labels[s], tuple((labels[G[g](s)],es[g][s]) for g in G)))
        names={}; new=[]
        for v in sig:
            if v not in names: names[v]=len(names)
            new.append(names[v])
        new=tuple(new)
        rounds.append({'classes':len(set(new)), 'q0_paired':new[2]==new[4], 'q1_paired':new[10]==new[12]})
        if new==labels:
            return rounds,new
        labels=new

def trace_splits(es, bound=7):
    split=[]
    for s in range(16):
        t=s^6
        if s>t: continue
        witness=None
        for depth in range(1,bound+1):
            for word in product(tuple(G), repeat=depth):
                if run(s,word,es)!=run(t,word,es):
                    witness=''.join(word)
                    break
            if witness is not None: break
        if witness is not None:
            split.append({'fiber':pi(s),'sources':(s,t),'first_witness':witness})
    return split

def check():
    assert len(set(initial))==8
    assert all(pi(s)==pi(s^6) for s in range(16))
    assert all(G[g](s^6)==(G[g](s)^6) for g in G for s in range(16))
    assert I.then(R).at((1,0,0,0,0,0)) == (-1,0,0,0,0,0)
    assert N.at((14,3,0,0,0,0))==(0,3,0,0,0,0)
    assert N.then(R)==N
    assert N.then(C).then(R).at(ZERO)==(-1,0,0,0,0,0)
    assert N.then(C).at(ZERO)==(1,0,0,0,0,0)
    answer={'schema':'EM_R246_STANDALONE_EXACT_CHECK_V1',
            'scope':'finite typed positive unit-weight BRC-affine algebra, 16 nonspatial controls, X6 affine maps',
            'not_native_source_import':True,
            'operators':{'N':'set first spatial coordinate to 0, rank 5',
                         'C':'translate first spatial coordinate by +1',
                         'R':'reflect first spatial coordinate, full-rank'},
            'initial_partition_classes':8}
    for variant in ('delayed','masked'):
        es=make_effects(variant)
        rounds,labels=refinement(es)
        witnesses_by_len=witnesses(es,7)
        result={'refinement_rounds':rounds, 'strong_congruence_classes':len(set(labels)),
                'q0_two_sources_equal_under_strong_refinement':labels[2]==labels[4],
                'q1_two_sources_equal_under_strong_refinement':labels[10]==labels[12],
                'witnesses_by_length':witnesses_by_len}
        splits=trace_splits(es)
        result['trace_splits_checked_up_to_7']=splits
        result['trace_classes_checked_up_to_7']=8+len(splits)
        if variant=='delayed':
            assert sorted(witnesses_by_len)[0]==3
            assert witnesses_by_len[3]['word']=='323'
            assert result['trace_classes_checked_up_to_7']==10
            assert witnesses_by_len[3]['at_origin_s2'] != witnesses_by_len[3]['at_origin_s4']
            assert len(set(labels))==10
            result['first_distinguishing_length']=3
        else:
            # Infinite equivalence is a proof by H0 invariance, NOT depth-7 testing.
            assert witnesses_by_len == {}
            assert len(set(labels))==10
            assert result['trace_classes_checked_up_to_7']==9
            result['first_distinguishing_length_up_to_7']='none'
            result['all_future_equivalence']='proved by invariant: first gate forces x1=0; all subsequent I/N/R effects preserve x1=0, so paired total affine effects coincide; control quotients agree'
            result['trace_equivalence_classes']=9
        answer[variant]=result
    return answer

if __name__=='__main__':
    print(json.dumps(check(),ensure_ascii=False,sort_keys=True,indent=2))
