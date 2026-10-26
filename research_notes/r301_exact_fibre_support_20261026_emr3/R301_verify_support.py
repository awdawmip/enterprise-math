#!/usr/bin/env python3
"""R301 exact BRC fibre-support verifier (stdlib arbitrary-precision integers)."""
from collections import defaultdict
import json

MAX_N = 600
EDGES = (
    ((2, -1, -1), (2, +1, -1)),
    ((0, -1, -1), (0, +1, -1)),
    ((1, +1, +1), (2, +1, -1)),
)
SMALL = {
    0: {1: (0,), -1: ()}, 1: {1: (), -1: ()}, 2: {1: (), -1: ()},
    3: {1: (-1,), -1: ()},
    4: {1: (-2,), -1: (-2,)},
    5: {1: (-3,), -1: (-3,)},
    6: {1: (-4, -2), -1: (-4,)},
    7: {1: (-5, -3), -1: (-5, -3, -1)},
    8: {1: (-6, -4, 0), -1: (-6, -4, -2, 0)},
}

def expected(n, eps):
    if n <= 8:
        return set(SMALL[n][eps])
    return set(range(2-n, n-7, 2))

def witness(n, eps, k):
    assert n >= 9 and k in expected(n, eps)
    if eps == 1:
        if k == 2-n:
            return [('A', n-2)]
        if k == 4-n:
            return [('A', 1), ('A', n-5)]
        if k == 6-n:
            return [('A', 1), ('A', 1), ('A', n-8)]
        return [('B', (k+n-4)//2), ('B', (n-4-k)//2)]
    if k == 2-n:
        return [('B', n-2)]
    if k == 4-n:
        return [('B', 2), ('A', n-6)]
    return [('A', (k+n-4)//2), ('B', (n-4-k)//2)]

def evaluate_blocks(blocks):
    eps, shift, length = 1, 0, 0
    for typ, m in blocks:
        assert typ in ('A', 'B') and m >= (1 if typ == 'A' else 2)
        eta = 1 if typ == 'A' else -1
        eps, shift = eps * eta, eta * shift - m
        length += m + 2
    return length, eps, shift

def block_word(blocks):
    return ''.join(('1' if typ == 'A' else '0') + '1'*(m-1) + '01' for typ,m in blocks)

def eval_raw_word(word):
    q, eps, shift, last_zero = 0, 1, 0, False
    for bit_str in word:
        bit = int(bit_str)
        assert not (last_zero and bit == 0)
        q, eta, c = EDGES[q][bit]
        eps, shift, last_zero = eps*eta, eta*shift+c, bit == 0
    assert q == 0
    return len(word), eps, shift

def verify():
    states = {(0, 1, 0, False): 1}
    seen = 0
    witnesses = 0
    sample = {}
    for n in range(MAX_N+1):
        by_eps = {1: set(), -1: set()}
        for (q, eps, k, last_zero), count in states.items():
            assert count > 0
            if q == 0:
                by_eps[eps].add(k)
        for eps in (1,-1):
            predicted = expected(n, eps)
            assert by_eps[eps] == predicted, (n, eps, sorted(by_eps[eps]^predicted))
            seen += len(predicted)
            if n >= 9:
                for k in predicted:
                    blocks = witness(n, eps, k)
                    assert len(blocks) <= (3 if eps == 1 else 2)
                    assert evaluate_blocks(blocks) == (n, eps, k), (n,eps,k,blocks)
                    witnesses += 1
        if n in (9, 10, 81, 82, 600):
            sample[str(n)] = {'count_plus':len(by_eps[1]),'count_minus':len(by_eps[-1]),
                              'min_k':2-n,'max_k':n-8}
            for eps in (1,-1):
                for k in (2-n, 4-n, 6-n, n-8):
                    if k in by_eps[eps]:
                        blocks=witness(n,eps,k)
                        assert eval_raw_word(block_word(blocks)) == (n,eps,k)
        if n == MAX_N:
            break
        nxt = defaultdict(int)
        for (q, eps, k, last_zero), count in states.items():
            for bit, (nq, eta, c) in enumerate(EDGES[q]):
                if bit == 0 and last_zero:
                    continue
                nxt[(nq,eta*eps,eta*k+c,bit==0)] += count
        states=nxt
    # Sharpness: a + word with k=6-n requires >=3 blocks for n>=9.
    # 1 A returns k=2-n; any 2 A return k=4-n; any 2 B return k>=8-n.
    for n in range(9,MAX_N+1):
        assert evaluate_blocks(witness(n,1,6-n)) == (n,1,6-n)
    return {
        'schema':'EM_R301_EXACT_FIBRE_SUPPORT_V1',
        'status':'PASS',
        'method':'independent raw ordered six-edge DP with forbidden 00, exact integers; explicit first-return witness formulas',
        'checked_n':[0,MAX_N],
        'fibres_positive_tested':seen,
        'constructed_witnesses_tested':witnesses,
        'theorem': 'for all n>=9 and both signs, support is exactly k congruent n mod 2, 2-n<=k<=n-8',
        'small_support':{str(n):{'plus':list(SMALL[n][1]), 'minus':list(SMALL[n][-1])} for n in range(9)},
        'maximum_constructive_return_blocks':{'plus':3,'minus':2},
        'plus_three_block_sharp':'for every n>=9, k=6-n has no representation with <=2 blocks',
        'samples':sample,
        'scope': 'positive ordered six-edge BRC auxiliary q0-return fibres; not native X6 physics',
        'limitations': 'all-length theorem from combinatorial proof; code only checks n<=600; no native Source Result/Driver admission'
    }

if __name__ == '__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
