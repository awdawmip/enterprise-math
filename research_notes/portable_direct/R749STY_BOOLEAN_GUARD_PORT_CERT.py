#!/usr/bin/env python3
"""Exact finite regression for a five-source boolean guard and lifetime POP."""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import factorial, comb
import json

ALPHABET = tuple(range(5))
GROUP = frozenset((0, 1))  # named equal-weight sources A, B
COMPLEMENT = frozenset(ALPHABET) - GROUP


def inventory(word):
    return tuple(word.count(i) for i in ALPHABET)


def signatures(word, r):
    """Exact theorem signature; popped labels are in observation order."""
    s = min(r, len(word))
    trace = tuple(reversed(word[-s:])) if s else ()
    color = None if s == len(word) else int(word[-s-1] in GROUP)
    return trace, color


def trace_no_append(word, r):
    """Independent legal read protocol: guard before and after every POP."""
    observations = []
    w = word
    for k in range(min(r, len(word)) + 1):
        observations.append((len(w), None if not w else int(w[-1] in GROUP)))
        if k < min(r, len(word)):
            observations.append(('pop', w[-1]))
            w = w[:-1]
    return tuple(observations)


def feasible_suffixes(n, s):
    def rec(c, remaining):
        if not remaining:
            yield ()
        else:
            for i in ALPHABET:
                if c[i]:
                    cc = list(c)
                    cc[i] -= 1
                    for t in rec(tuple(cc), remaining - 1):
                        yield (i,) + t
    yield from rec(n, s)


def guard_colors(c):
    choices = []
    if sum(c[i] for i in COMPLEMENT):
        choices.append(0)
    if sum(c[i] for i in GROUP):
        choices.append(1)
    return tuple(choices)


def count_from_suffix(n, r):
    ell = sum(n)
    s = min(r, ell)
    if s == ell:
        return factorial(ell) // __import__('math').prod(factorial(x) for x in n)
    total = 0
    for suffix in feasible_suffixes(n, s):
        c = tuple(n[i] - suffix.count(i) for i in ALPHABET)
        total += len(guard_colors(c))
    return total


@lru_cache(None)
def count_dp(c, remaining):
    if not remaining:
        return len(guard_colors(c)) if sum(c) else 1
    total = 0
    for i in ALPHABET:
        if c[i] > 0:
            cc = list(c)
            cc[i] -= 1
            total += count_dp(tuple(cc), remaining - 1)
    return total


def rank_signature(n, r, sig):
    popped, color = sig
    ell = sum(n)
    s = min(r, ell)
    assert len(popped) == s
    c = list(n)
    rank = 0
    for x, i in enumerate(popped):
        for j in ALPHABET:
            if j >= i:
                break
            if c[j] > 0:
                cc = c[:]
                cc[j] -= 1
                rank += count_dp(tuple(cc), s - x - 1)
        assert c[i] > 0
        c[i] -= 1
    choices = (None,) if s == ell else guard_colors(tuple(c))
    assert color in choices
    return rank + choices.index(color)


def unrank_signature(n, r, rank):
    ell = sum(n)
    s = min(r, ell)
    assert 0 <= rank < count_dp(n, s)
    c = list(n)
    popped = []
    for x in range(s):
        for i in ALPHABET:
            if c[i] == 0:
                continue
            cc = c[:]
            cc[i] -= 1
            width = count_dp(tuple(cc), s-x-1)
            if rank >= width:
                rank -= width
            else:
                c = cc
                popped.append(i)
                break
        else:
            raise AssertionError('unrank failed')
    choices = (None,) if s == ell else guard_colors(tuple(c))
    assert rank < len(choices)
    return tuple(popped), choices[rank]


def pop_only_count(n,r):
    return sum(1 for _ in feasible_suffixes(n, min(r,sum(n))))


def peek_one_count(n,r):
    return sum(1 for _ in feasible_suffixes(n,min(r+1,sum(n))))


def run():
    total_words = 0
    compositions = 0
    cases = 0
    rank_tests = 0
    for ell in range(8):
        groups = defaultdict(list)
        for word in product(ALPHABET,repeat=ell):
            groups[inventory(word)].append(word)
            total_words += 1
        for n,words in groups.items():
            compositions += 1
            for r in range(min(4,ell)+1):
                cases += 1
                sig_groups = defaultdict(set)
                pop_groups = defaultdict(set)
                for word in words:
                    sig = signatures(word,r)
                    sig_groups[sig].add(word)
                    pop_groups[trace_no_append(word,r)].add(word)
                    idx = rank_signature(n,r,sig)
                    assert unrank_signature(n,r,idx) == sig
                    rank_tests += 1
                assert set(map(frozenset,sig_groups.values())) == set(map(frozenset,pop_groups.values()))
                num = len(sig_groups)
                assert num == count_from_suffix(n,r) == count_dp(n,min(r,ell))
                assert pop_only_count(n,r) <= num <= peek_one_count(n,r)
                assert num <= 2*pop_only_count(n,r)
                assert sorted({rank_signature(n,r,sig) for sig in sig_groups}) == list(range(num))
    example = {}
    for n in ((2,1,1,1,1),(2,2,2,2,2)):
        example[''.join(map(str,n))] = [
            {'r':r,'pop_only_classes':pop_only_count(n,r),'boolean_guard_classes':count_dp(n,min(r,sum(n))),
             'full_peek_1_classes':peek_one_count(n,r), 'bits':(count_dp(n,min(r,sum(n)))-1).bit_length()}
            for r in range(min(6,sum(n))+1)]
    assert signatures((0,2),0) != signatures((2,0),0)
    assert signatures((0,2),0)[1] != signatures((2,0),0)[1]
    return {'schema':'R749STY_BOOLEAN_GUARD_EXACT_CERT_V1', 'status':'PASS',
            'alphabet':'A B C D E', 'guard_group':['A','B'], 'weight_vector':[1,1,2,3,6],
            'word_lengths_exhaustively_checked':[0,1,2,3,4,5,6,7],
            'r_per_word_length':'0..min(4,length)',
            'word_instances':total_words,'composition_fibers':compositions,
            'composition_resource_cases':cases,'rank_unrank_checks':rank_tests,
            'observation_trace':'all guard results before/after 0..r POP; no APPEND needed for finite independent oracle',
            'examples':example,
            'scope':'Exact finite regression only; all APPEND interleavings and all lengths follow separate proof.'}

if __name__ == '__main__':
    result=run()
    print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
