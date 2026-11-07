#!/usr/bin/env python3
"""Exact integer check of the BRC strictly-positive label-mixing sharpness theorem.

All words are exhaustively enumerated for m in 1..4 and c,d from a declared
three-element set. Numbers count original positive-integer paths, not probabilities.
"""
from itertools import product
from math import comb, factorial
from json import dump
from pathlib import Path

Z = (1, -1, -1, 1)
PARAMS = ((1, 1), (2, 1), (1, 2))


def model(m, even, c, d):
    N = 2 * m - 1
    P = N + 1
    tags = tuple(j for j in range(N + 1) if (j % 2 == 0) == even)
    weights = tuple(comb(N, j) for j in tags)
    assert len(tags) == m
    W = sum(weights)
    S = c + d * W
    T = tuple(tuple(c * (a == b) + d * weights[b] for b in range(m)) for a in range(m))
    assert all(v > 0 for row in T for v in row)
    assert all(sum(row) == S for row in T)
    assert all(weights[a] * T[a][b] == weights[b] * T[b][a]
               for a in range(m) for b in range(m))
    if m > 1:
        assert all(T[a][b] > 0 for a in range(m) for b in range(m) if a != b)
    kernels = tuple(tuple(P + tags[a] * Z[y] for y in range(4)) for a in range(m))
    assert all(v > 0 for row in kernels for v in row)
    assert all(sum(row) == 4 * P for row in kernels)
    return weights, kernels, T, W, S


def count_word(model_data, word):
    weights, kernels, T, _W, _S = model_data
    state = weights
    for y in word:
        emitted = [state[a] * kernels[a][y] for a in range(len(weights))]
        state = tuple(sum(emitted[a] * T[a][b] for a in range(len(weights)))
                      for b in range(len(weights)))
    return sum(state)


def main():
    cases = []
    n_words = 0
    n_path_evaluations = 0
    n_transition_terms = 0
    for m in range(1, 5):
        N = 2 * m - 1
        P = N + 1
        W = 2 ** (N - 1)
        for c, d in PARAMS:
            A = model(m, True, c, d)
            B = model(m, False, c, d)
            S = c + d * W
            case = {"m": m, "N": N, "P": P, "c": c, "d": d,
                    "source_weight_each_type": W, "transition_row_mass": S,
                    "horizon": [], "example_all_zero_word": None}
            for t in range(N + 1):
                gap_l1 = 0
                total_a = total_b = 0
                count_words_t = 0
                for word in product(range(4), repeat=t):
                    val_a = count_word(A, word)
                    val_b = count_word(B, word)
                    assert val_a >= 0 and val_b >= 0
                    predicted_delta = (S * c ** (N - 1) * ((-1) ** N)
                                       * factorial(N) * product_z(word)) if t == N else 0
                    assert val_a - val_b == predicted_delta, (m,c,d,t,word,val_a,val_b,predicted_delta)
                    if t == N and all(y == 0 for y in word):
                        case["example_all_zero_word"] = {"A":val_a,"B":val_b,"signed_gap":val_a-val_b}
                    gap_l1 += abs(val_a - val_b)
                    total_a += val_a
                    total_b += val_b
                    count_words_t += 1
                    n_words += 1
                    n_path_evaluations += 2
                    n_transition_terms += 2 * t * (m ** 2)
                predicted_total = W * (4 * P * S) ** t
                predicted_l1 = (4 ** N * S * c ** (N - 1) * factorial(N)) if t == N else 0
                assert total_a == total_b == predicted_total
                assert gap_l1 == predicted_l1
                assert count_words_t == 4 ** t
                case["horizon"].append({"t":t,"words":count_words_t,"total_each":predicted_total,"l1":gap_l1})
            # The stochastic normalization is a derived observer, not primitive branch mass.
            # TV_N = N! (c/S)^(N-1) / (2^N P^N) exactly, recorded as a rational pair.
            tv_num = factorial(N) * c ** (N - 1)
            tv_den = (2 ** N) * (P ** N) * (S ** (N - 1))
            from math import gcd
            g = gcd(tv_num, tv_den)
            case["first_split_tv_exact"] = {"numerator": tv_num//g, "denominator": tv_den//g}
            cases.append(case)

    payload = {
        "status":"PASS", "scope":"AUXILIARY_BRC_INTEGER_MODEL_AUTHOR_CHECK_ONLY",
        "statement":"Strictly positive reversible mixing preserves uniform 2m-1 horizon sharpness",
        "parameter_domain":{"m":[1,2,3,4],"c_d_pairs":list(map(list,PARAMS)),
                            "word_lengths":"0..2m-1, all 4^t ordered joint-output words"},
        "case_count":len(cases), "word_pair_checks":n_words,
        "raw_integer_history_evaluations":n_path_evaluations,
        "integer_transition_products":n_transition_terms,
        "cases":cases,
        "proof_scope":"General m>=1 by symbolic finite differences and renewal block decomposition",
        "admission":"UNREVIEWED_NOT_ADMITTED_NOT_NATIVE"
    }
    dest = Path(__file__).with_name("d25_strict_positive_mixing_sharp_author_check_20261031.json")
    with dest.open("w",encoding="utf-8") as f:
        dump(payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("PASS", "cases",len(cases),"word_pair_checks",n_words,
          "history_evaluations",n_path_evaluations,"transition_products",n_transition_terms)
    print("m2 c1 d1:",[(x["example_all_zero_word"],x["first_split_tv_exact"])
                        for x in cases if x["m"]==2 and x["c"]==1 and x["d"]==1])


def product_z(word):
    ans = 1
    for y in word:
        ans *= Z[y]
    return ans


if __name__ == "__main__":
    main()
