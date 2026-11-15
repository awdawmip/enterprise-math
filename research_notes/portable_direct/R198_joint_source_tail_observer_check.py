#!/usr/bin/env python3
"""R198 exact finite witness: joint last-occurrence source and native X6 suffix.

Independent integer/Fraction reference for the declared bounded observer.
Not a native enterprise_math package test and not a physical X6 dynamics claim.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, perm
from random import Random
import json


def partial_orders(items):
    items = tuple(items)
    for r in range(len(items)+1):
        yield from permutations(items,r)


def nsource(k):
    return sum(perm(k,r) for r in range(k+1))


def last_occurrence(word,k):
    seen=set()
    out=[]
    for a in reversed(word):
        if a<k and a not in seen:
            seen.add(a)
            out.append(a)
    return tuple(reversed(out))


def tail(word,L):
    return tuple(word[-L:]) if L else ()


def observer(word,m,k,L):
    assert 0 <= k <= m and L >= 0
    assert all(0<=x<m for x in word)
    return (last_occurrence(word,k),tail(word,L))


def star(s,u):
    found=set(u)
    return tuple(a for a in s if a not in found)+u


def combine(left,right,L):
    s,t=left; u,v=right
    return star(s,u), tail(t+v,L)


def exact_size(m,k,L):
    if L==0:
        return nsource(k)
    ans=sum(m**ell for ell in range(L))
    for r in range(k+1):
        # exactly r of the k selected labels appear in the L-letter tail
        tail_count=comb(k,r)*sum((-1)**j*comb(r,j)*(m-k+r-j)**L for j in range(r+1))
        ans += tail_count*nsource(k-r)
    return ans


def accessible_pairs(m,k,L):
    """Full image generation for small L; yields unique observation states."""
    if L==0:
        for s in partial_orders(range(k)):
            yield (s,())
        return
    for ell in range(L):
        for t in product(range(m),repeat=ell):
            yield last_occurrence(t,k),t
    for t in product(range(m),repeat=L):
        sts=last_occurrence(t,k)
        available=tuple(a for a in range(k) if a not in set(sts))
        for prefix in partial_orders(available):
            yield prefix+sts,t


def exhaustive_reachability(m,k,L):
    """Any state is realized by a word of length at most L+k."""
    actual=set()
    for ell in range(L+k+1):
        actual.update(observer(w,m,k,L) for w in product(range(m),repeat=ell))
    expected=set(accessible_pairs(m,k,L))
    assert actual==expected,(m,k,L,len(actual),len(expected))
    assert len(actual)==exact_size(m,k,L)
    return len(expected)


def family_brc_plus(P,Q):
    out=defaultdict(int,P)
    for key,count in Q.items():out[key]+=count
    return dict(out)


def family_brc_times(P,Q,L):
    # atomic key=(weight, physical affine a,b, joint state), count positive
    out=defaultdict(int)
    for (w,a,b,obs),c in P.items():
        for (v,d,e,obs2),f in Q.items():
            # x -> a*x+b, then x -> d*x+e
            out[(w*v,d*a,d*b+e,combine(obs,obs2,L))]+=c*f
    return dict(out)


def run():
    out={"schema":"EM_R198_JOINT_SOURCE_X6_SUFFIX_EXACT_V1",
         "backend":"independent_integer_fraction_reference",
         "frozen_scientific_input":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
         "status":"PASS", "exact_arithmetic":"integer and Fraction, no floats",
         "exhaustive_reachable_rows":[],"exhaustive_transition_pairs":0,
         "exact_joint_codec_roundtrips":0,
         "random_triple_associativity":0,"future_context_checks":0,
         "brc_alternative_and_serial_checks":0,"resource_rows":[]}
    for m in (2,3,4,5):
        for k in range(0,min(m,3)+1):
            for L in range(0,4):
                if m**(L+k+1)>60000:continue
                states=exhaustive_reachability(m,k,L)
                out["exhaustive_reachable_rows"].append({"m":m,"k":k,"L":L,"states":states})
    # Reversible minimal-width enumerative fixed code, for the declared joint image.
    # This is a finite table encoder, not an assertion of constant-space indexing.
    for m,k,L in ((3,2,2),(4,3,2),(12,6,1)):
        admissible=list(accessible_pairs(m,k,L))
        assert len(admissible)==len(set(admissible))==exact_size(m,k,L)
        rank_index={s:i for i,s in enumerate(admissible)}
        for i,s in enumerate(admissible):
            assert admissible[rank_index[s]]==s
            assert 0<=i<2**((len(admissible)-1).bit_length())
        out["exact_joint_codec_roundtrips"]+=len(admissible)
    rng=Random(198)
    for m,k,L in ((2,2,0),(2,2,1),(3,2,2),(3,3,1),(4,2,2)):
        states=list(accessible_pairs(m,k,L))
        tset=set(states)
        for a in states:
            for b in states:
                assert combine(a,b,L) in tset
                out["exhaustive_transition_pairs"]+=1
        for _ in range(1000):
            a,b,c=(rng.choice(states) for _ in range(3))
            assert combine(combine(a,b,L),c,L)==combine(a,combine(b,c,L),L)
            out["random_triple_associativity"]+=1
        for _ in range(1000):
            w=tuple(rng.randrange(m) for j in range(rng.randrange(0,20)))
            v=tuple(rng.randrange(m) for j in range(rng.randrange(0,20)))
            assert observer(w+v,m,k,L)==combine(observer(w,m,k,L),observer(v,m,k,L),L)
            out["future_context_checks"]+=1
        identity=observer((),m,k,L)
        for a in states:
            assert combine(identity,a,L)==a==combine(a,identity,L)
        H={
            (F(1,2),F(1),F(2,3),observer((0,1),m,k,L)):2,
            (F(2,3),F(3,2),F(1,5),observer((1,),m,k,L)):3,
        }
        J={
            (F(1),F(1),F(0),observer((0,),m,k,L)):1,
            (F(3,2),F(1,2),F(2),observer((),m,k,L)):2,
        }
        K={
            (F(5,4),F(2),F(3),observer((1,0),m,k,L)):1,
        }
        assert family_brc_times(family_brc_times(H,J,L),K,L)==family_brc_times(H,family_brc_times(J,K,L),L)
        assert family_brc_times(family_brc_plus(H,J),K,L)==family_brc_plus(family_brc_times(H,K,L),family_brc_times(J,K,L))
        assert family_brc_times(H,family_brc_plus(J,K),L)==family_brc_plus(family_brc_times(H,J,L),family_brc_times(H,K,L))
        out["brc_alternative_and_serial_checks"]+=3
    for L in range(0,7):
        n=exact_size(12,6,L)
        naive=nsource(6)*sum(12**j for j in range(L+1))
        out["resource_rows"].append({"k":6,"native_direction_alphabet":12,"suffix_horizon":L,
                                      "reachable_joint_states":n,"minimum_fixed_code_bits":(n-1).bit_length(),
                                      "naive_cartesian_states":naive,"naive_code_bits":(naive-1).bit_length(),
                                      "states_saved":naive-n})
    return out


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
