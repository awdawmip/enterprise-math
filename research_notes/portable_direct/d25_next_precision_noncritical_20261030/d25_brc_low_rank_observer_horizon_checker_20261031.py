#!/usr/bin/env python3
"""Exact positive-integer BRC finite-observer horizon checks; author-side only."""
from fractions import Fraction
from itertools import product
from math import comb, factorial
import json
from pathlib import Path

Z = (1, -1, -1, 1)


def rank(a):
    a = [[Fraction(x) for x in row] for row in a]
    n = len(a)
    m = len(a[0])
    k = 0
    for col in range(m):
        pivot = next((i for i in range(k, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        p = a[k][col]
        a[k] = [v / p for v in a[k]]
        for i in range(n):
            if i != k and a[i][col]:
                q = a[i][col]
                a[i] = [a[i][j] - q * a[k][j] for j in range(m)]
        k += 1
        if k == n:
            break
    return k


def base(r):
    n = 2 * r - 1
    w = [comb(n, 2 * k) for k in range(r)]
    s = 1 + sum(w)
    t = [[int(i == j) + w[j] for j in range(r)] for i in range(r)]
    p = n + 1
    ja = [[p + (2 * k) * z for z in Z] for k in range(r)]
    jb = [[p + (n - 2 * k) * z for z in Z] for k in range(r)]
    return w, t, ja, jb, s, p


def clone_first(w, t, ja, jb):
    # Clone old label 0 as two identical positive labels. The aggregated
    # transition is 2T; aggregated initial source multiplicities are 2w.
    def clonerow(row):
        return [row[0], row[0]] + [2 * x for x in row[1:]]
    out_t = [clonerow(t[0]), clonerow(t[0])] + [clonerow(row) for row in t[1:]]
    out_w = [w[0], w[0]] + [2 * x for x in w[1:]]
    out_ja = [ja[0], ja[0]] + ja[1:]
    out_jb = [jb[0], jb[0]] + jb[1:]
    return out_w, out_t, out_ja, out_jb


def history(a, t, j, word):
    row = list(a)
    for y in word:
        row = [sum(row[i] * j[i][y] * t[i][k] for i in range(len(a))) for k in range(len(a))]
    return sum(row)


def run():
    counts = {"cases": 0, "complete_compared_words": 0,
              "first_split_witnesses": 0, "integer_history_evaluations": 0}
    cert = []
    for r in (2, 3, 4):
        w, t, ja, jb, s, p = base(r)
        a, tnew, jnewa, jnewb = clone_first(w, t, ja, jb)
        n = 2*r-1
        assert rank(t) == r and rank(tnew) == r
        assert len(tnew) == r+1 and all(x > 0 for row in tnew for x in row)
        assert all(x > 0 for tab in (jnewa,jnewb) for row in tab for x in row)
        assert all(sum(row) == 4*p for tab in (jnewa,jnewb) for row in tab)
        assert [sum(a[i]*tnew[i][k] for i in range(len(a)))
                for k in range(len(a))] == [2*s*x for x in a]
        total_words = 0
        for depth in range(n+1):
            for word in product(range(4), repeat=depth):
                aa = history(a, tnew, jnewa, word)
                bb = history(a, tnew, jnewb, word)
                counts["integer_history_evaluations"] += 2
                counts["complete_compared_words"] += 1
                total_words += 1
                if depth < n:
                    assert aa == bb, (r, word, aa, bb)
                else:
                    predicted = (2**(n+1)) * ((-1)**n) * s * factorial(n)
                    predicted *= (-1)**sum(y in (1,2) for y in word)
                    assert aa-bb == predicted, (r, word, aa, bb, predicted)
                    counts["first_split_witnesses"] += 1
        # Full distribution mass is exact because every hidden label emits
        # 4p total and every new transition row sums to 2s.
        expected_total = sum(a) * ((4*p)*(2*s))**n
        if r <= 3:
            total_a = sum(history(a,tnew,jnewa,word)
                          for word in product(range(4), repeat=n))
            total_b = sum(history(a,tnew,jnewb,word)
                          for word in product(range(4), repeat=n))
            assert total_a == total_b == expected_total
            counts["integer_history_evaluations"] += 2*4**n
        alpha = history(a,tnew,jnewa,(0,)*n)
        beta = history(a,tnew,jnewb,(0,)*n)
        l1 = (4**n) * abs(alpha-beta)
        cert.append({"transition_rank_each":r, "hidden_labels_each":r+1,
                     "stationary_eigenvalue":2*s,
                     "sharp_horizon":n, "first_all_zero_word_A":alpha,
                     "first_all_zero_word_B":beta,
                     "first_all_zero_word_difference":alpha-beta,
                     "all_words_at_first_split":4**n,
                     "full_distribution_L1":l1,
                     "each_total_raw_mass_at_split":expected_total,
                     "complete_depths_checked":list(range(n+1)),
                     "compared_words":total_words})
        counts["cases"] += 1
    assert cert[0]["first_all_zero_word_A"] == 1345280
    assert cert[0]["first_all_zero_word_B"] == 1345760
    assert cert[0]["full_distribution_L1"] == 30720
    out = {"schema":"D25_BRC_LOW_RANK_HORIZON_AUTHOR_EXACT_CHECK_V1",
           "status":"PASS", "scope":"positive-integer auxiliary four-port shared-label models; not native X6",
           "source_pin":"c47e13e4aba0e006366f989d6334d443f6333ae3",
           "arithmetic":"unbounded Python integers; Fraction rank only",
           "counts":counts,"certificates":cert,
           "project_status":"AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE"}
    target=Path(__file__).with_name('d25_brc_low_rank_observer_horizon_author_check_20261031.json')
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({"status":"PASS","counts":counts,"certificates":cert},ensure_ascii=False))

if __name__ == '__main__':
    run()
