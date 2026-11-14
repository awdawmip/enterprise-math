#!/usr/bin/env python3
"""R762AI: exact ranked source-provenance codec for the R762AH sliding transcript.
All counts are positive integer BRC branch multiplicities in a conditional star,
not signed force amplitudes or an admitted P000 force-event update.
"""
import json
from collections import defaultdict
from functools import lru_cache
from itertools import permutations
from math import comb, factorial


def tail_count(n, k):
    """Number of bijections with k distinct forbidden diagonal pairs."""
    return sum((-1)**r * comb(k, r) * factorial(n-r) for r in range(k+1))


def transitions(B, bits):
    """Weighted AH transition, indexed by next (B-1)-bit window."""
    high = 1 << (B-2)
    c = B-1-bits.bit_count()
    d = defaultdict(int)
    if c:
        d[(bits >> 1) | high] += c
    for r in range(1, B-1):
        if bits & (1 << r):
            d[((bits ^ (1 << r)) >> 1) | high] += 1
    d[bits >> 1] += 1
    return d


def suffix_table(m, B):
    assert 2 <= B <= m
    num_main = m-B+1
    N = 1 << (B-1)
    C = [[0] * N for _ in range(num_main+1)]
    for S in range(N):
        C[num_main][S] = tail_count(B-1, S.bit_count())
    for j in range(num_main-1, -1, -1):
        for S in range(N):
            C[j][S] = sum(mult*C[j+1][target]
                          for target, mult in transitions(B, S).items())
    return C


def word(m, B):
    w=[('I', i) for i in range(B)]
    for j in range(m-B+1):
        w.append(('O', j))
        if B+j < m:
            w.append(('I', B+j))
    w.extend(('O', j) for j in range(m-B+1,m))
    assert len(w) == 2*m
    return w


def update_state(B, j, S, source):
    """Main-output transition for an individual source, not a bundled multiplicity."""
    if source < j:
        return (S >> 1) | (1 << (B-2))
    if source == j+B-1:
        return S >> 1
    r=source-j
    assert 1 <= r <= B-2 and S & (1 << r)
    return ((S ^ (1 << r)) >> 1) | (1 << (B-2))


def branch_options(m, B, j, unused, S, C):
    """Sorted individual source choices and exact number of completions."""
    num_main=m-B+1
    if j < num_main:
        available=sorted(unused | {j+B-1})
        return [(i, C[j+1][update_state(B,j,S,i)])
                for i in available if i != j]
    future=set(range(j+1,m))
    n=m-j-1
    return [(i,tail_count(n,len((unused-{i}) & future)))
            for i in sorted(unused) if i != j]


def encode(m,B,assigned):
    """Rank of destination-ordered source sequence, zero-based lexicographic."""
    C=suffix_table(m,B)
    S=(1 << (B-1))-1
    unused=set(range(B-1))
    rank=0
    for j,i in enumerate(assigned):
        options=branch_options(m,B,j,unused,S,C)
        options=[(src,k) for src,k in options if k]
        choices=[src for src,k in options]
        assert i in choices, (j,i,choices)
        rank += sum(k for src,k in options if src < i)
        if j < m-B+1:
            unused.add(j+B-1)
            S=update_state(B,j,S,i)
        unused.remove(i)
    assert not unused
    assert 0 <= rank < C[0][(1<<(B-1))-1]
    return rank


def decode(m,B,rank):
    C=suffix_table(m,B)
    total=C[0][(1<<(B-1))-1]
    if not (0 <= rank < total):
        raise ValueError('rank out of fiber')
    S=(1<<(B-1))-1
    unused=set(range(B-1))
    result=[]
    for j in range(m):
        options=branch_options(m,B,j,unused,S,C)
        for i,k in options:
            if rank < k:
                break
            rank-=k
        else:
            raise AssertionError('completion-count inconsistent')
        result.append(i)
        if j < m-B+1:
            unused.add(j+B-1)
            S=update_state(B,j,S,i)
        unused.remove(i)
    assert rank==0 and not unused
    return tuple(result)


def brute_fiber(m,B):
    """Independent direct permutation oracle: no codec or transfer recurrence."""
    entered={}
    for t,(kind,j) in enumerate(word(m,B)):
        if kind=='I':
            entered[j]=t
    out_time={j:t for t,(kind,j) in enumerate(word(m,B)) if kind=='O'}
    return sorted(p for p in permutations(range(m)) if all(
        p[j] != j and entered[p[j]] < out_time[j] for j in range(m)))


def run():
    exhaustive=[]
    for B, max_m in ((2,10),(3,10),(4,8)):
        for m in range(B,max_m+1):
            C=suffix_table(m,B)
            N=C[0][(1<<(B-1))-1]
            oracle=brute_fiber(m,B)
            assert N==len(oracle),(B,m,N,len(oracle))
            assert all(decode(m,B,k)==p and encode(m,B,p)==k
                       for k,p in enumerate(oracle)), (B,m)
            exhaustive.append({'B':B,'m':m,'fiber':N,'rank_codes_verified':N,
                'minimal_fixed_bits': (N-1).bit_length()})
    sampled=[]
    for B in (2,3,4,5,6):
        for m in (max(B,9), max(B,14),max(B,18),max(B,32)):
            C=suffix_table(m,B)
            N=C[0][(1<<(B-1))-1]
            indexes=sorted(k for k in {0,1,N//3,N//2,(2*N)//3,N-2,N-1} if 0<=k<N)
            for k in indexes:
                p=decode(m,B,k)
                assert encode(m,B,p)==k
            sampled.append({'B':B,'m':m,'fiber':str(N),
                'sampled_codes':len(indexes),'minimal_fixed_bits':(N-1).bit_length()})
    arr=[suffix_table(m,3)[0][3] for m in range(3,33)]
    for i in range(4,len(arr)):
        assert arr[i]==2*arr[i-1]+arr[i-2]+arr[i-3]+arr[i-4]
    return {'schema':'R762AI_SLIDING_SOURCE_FIBER_ENUMERATIVE_CODEC_V1',
      'model':'R762AH conditional unit-port star, ordered source-blind sliding I/O log, no home return',
      'proof_scope':'All B>=2, m>=B; lexicographic bijection to [0,f_(m,B)); fixed-length optimum ceil(log2 f)',
      'precompute_arithmetic_operations':'O(m * B * 2^(B-1))',
      'rank_unrank_arithmetic_operations':'O(m * B * log(B) + B^3) after suffix table, including sorted candidate choices',
      'exact_exhaustive_oracle':exhaustive,
      'sampled_larger':sampled,
      'B3_first_ten_m3_to_m12': [{'m':m,'count':str(suffix_table(m,3)[0][3]),
       'bits':(suffix_table(m,3)[0][3]-1).bit_length()} for m in range(3,13)],
      'native_admission':False,'formal_acceptance':False}


if __name__=='__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False))
