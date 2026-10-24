#!/usr/bin/env python3
"""Independent exact-integer check of a finite-state BRC reset theorem.
Only the declared formal R268/R270 auxiliary automaton is modeled.
"""
from collections import defaultdict
import json

Q_STEPS = {
    0: ((2, -1, -1), (2, +1, -1)),
    1: ((0, -1, -1), (0, +1, -1)),
    2: ((1, +1, +1), (2, +1, -1)),
}

def after_r(r, a):
    if r == 2:
        return 2
    return (1 if a == 0 else 0) if r == 0 else (2 if a == 0 else 0)

def step(q, r, eps, k, a):
    nq, eta, b = Q_STEPS[q][a]
    return nq, after_r(r, a), eta * eps, eta * k + b

def states_by_depth(max_depth):
    hist = {(0, 0, 1, 0): 1}
    yield 0, hist
    for n in range(1, max_depth + 1):
        nxt = defaultdict(int)
        for (q, r, eps, k), value in hist.items():
            for a in (0, 1):
                nxt[step(q, r, eps, k, a)] += value
        hist = nxt
        yield n, hist

def formula_a(n):
    f, g = 0, 1
    for _ in range(n):
        f, g = g, f + g
    rho = 3 * (-1) ** (n // 2) if n % 2 == 0 else -(-1) ** ((n - 1)//2)
    numerator = 2 * g - f + rho
    assert numerator % 5 == 0
    return numerator // 5

def raw_word_check(max_depth):
    for n in range(max_depth + 1):
        counts = defaultdict(int)
        for word in range(1 << n):
            state = (0, 0, 1, 0)
            for i in range(n - 1, -1, -1):
                state = step(*state, (word >> i) & 1)
            counts[state] += 1
        reference = dict(next(hist for depth, hist in states_by_depth(n) if depth == n))
        assert counts == reference, (n, len(counts), len(reference))

def main():
    raw_word_check(12)
    table = []
    common_table = []
    max_reset_by_m = {}
    b7 = (2,2,3,1,1,9)
    b8 = (1,6,1,9,2,16)
    b9 = (1,19,2,20,4,28)
    for n, hist in states_by_depth(90):
        assert sum(hist.values()) == (1 << n)
        reset = {(e,k): v for (q,r,e,k),v in hist.items() if q == 0 and r == 0}
        count = sum(reset.values())
        if reset: max_reset_by_m[n] = max(reset.values())
        channel_order = ((0,0),(0,1),(1,0),(1,1),(2,0),(2,1))
        channel_index = {c:i for i,c in enumerate(channel_order)}
        by_effect = defaultdict(lambda: [0]*6)
        for (q,r,e,k),v in hist.items():
            by_effect[(e,k)][channel_index[(q,int(r==2))]] += v
        common_max = max((min(v) for v in by_effect.values()),default=0)
        if n>=10:
            assert common_max>=max_reset_by_m[n-7], (n,common_max,max_reset_by_m[n-7])
        ff0, ff1 = 0, 1
        for _ in range(n+2): ff0,ff1=ff1,ff0+ff1
        assert common_max <= ff0
        if n in (7,8,9,10,15,20,37,67,90):
            common_table.append(dict(n=n,max_six_channel_bottleneck=common_max,fibonacci_upper=ff0,amplifier_lower=max_reset_by_m.get(n-7),pigeonhole_lower=(((formula_a(n-7)+2*(n-6)-1)//(2*(n-6))) if n>=10 else None)))
        assert count == formula_a(n), (n,count,formula_a(n))
        if n < 3: assert count == (1 if n == 0 else 0)
        if n >= 3: assert count > 0
        if n in (7,8,9):
            expected_g = {7:(1,-3),8:(1,0),9:(-1,-1)}[n]
            expected = {7:b7,8:b8,9:b9}[n]
            q_order=((0,0),(0,1),(1,0),(1,1),(2,0),(2,1))
            found=tuple(sum(v for (q,r,e,k),v in hist.items() if q==q0 and (r==2)==bool(h) and (e,k)==expected_g) for q0,h in q_order)
            assert found==expected,(n,found,expected)
        if n in (3,4,5,7,10,20,30,40,60,80,90):
            gmax, mmax = max(reset.items(),key=lambda kv: kv[1])
            candidate_lower = (count + 2*(n+1) - 1)//(2*(n+1))
            assert mmax >= candidate_lower
            assert all(k % 2 == n % 2 and abs(k)<=n for (e,k) in reset)
            table.append(dict(m=n,reset_total=count,max_reset=mmax,best_effect=list(gmax),effect_count=len(reset),pigeonhole_lower=candidate_lower))
        if n==30: assert reset[(1,-4)]==16482
    print(json.dumps({"status":"PASS","raw_binary_words_checked":sum(1<<j for j in range(13)),"DP_depth_max":90,"reset_table":table,"common_fibre_table":common_table},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
