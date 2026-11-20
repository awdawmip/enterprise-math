#!/usr/bin/env python3
"""Stage393-B: exact typed signed-X6 BRC branch-turn refinement.
Frozen source: awdawmip/enterprise-math @ 2af3fc484eb11060b69e0afc1b562bcaf5ad1419
Source kernel: research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md §4.
All quantities are integers or fractions; no physical heartbeat propagator is used.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import factorial
from hashlib import sha256
from pathlib import Path
import json

A = tuple((axis, sign) for axis in range(6) for sign in (1, -1))
ZERO = (0,) * 6
OUT = Path(__file__).resolve().parent


def step(label):
    a, s = label
    z = [0] * 6
    z[a] = s
    return tuple(z)


def add(z, d):
    return tuple(a + b for a, b in zip(z, d))


def path_endpoint(w):
    z = ZERO
    for label in w:
        z = add(z, step(label))
    return z


def turns(w):
    return sum(w[i] != w[i - 1] for i in range(1, len(w)))


def relative_triples(z):
    out = []
    for i, j, k in combinations(range(6), 3):
        tri = (z[i], z[j], z[k])
        b = min(tri)
        out.append(tuple(x - b for x in tri))
    return tuple(out)


def can6(z):
    h = min(z)
    return tuple(v - h for v in z), h


def recover_from_relative_and_depth(z):
    r, h = can6(z)
    return tuple(x + h for x in r)


def integral_compositions(total, parts):
    if parts == 1:
        yield (total,)
    else:
        for j in range(total + 1):
            for suffix in integral_compositions(total - j, parts - 1):
                yield (j,) + suffix


def signed_endpoint_kernel(length, z, weights=None):
    """N_M(z) or W_M(z), evaluated from the frozen all-length BRC formula."""
    shortest = sum(abs(x) for x in z)
    if length < shortest or (length - shortest) % 2:
        return 0 if weights is None else Fraction(0)
    ksum = (length - shortest) // 2
    aa = [max(x, 0) for x in z]
    bb = [max(-x, 0) for x in z]
    total = Fraction(0)
    for ks in integral_compositions(ksum, 6):
        part = Fraction(1)
        for i in range(6):
            p, n = aa[i] + ks[i], bb[i] + ks[i]
            part /= factorial(p) * factorial(n)
            if weights is not None:
                part *= weights[(i, 1)] ** p * weights[(i, -1)] ** n
        total += part
    total *= factorial(length)
    if weights is None:
        assert total.denominator == 1
        return int(total)
    return total


def brc_dp(max_len, weights=None):
    """Direct signed-path BRC DP, independent of endpoint coefficient formula."""
    n = {ZERO: Fraction(1) if weights is not None else 1}
    history = [n]
    for m in range(max_len):
        t = defaultdict(Fraction if weights is not None else int)
        for z, val in n.items():
            for label in A:
                t[add(z, step(label))] += val * (weights[label] if weights else 1)
        n = dict(t)
        history.append(n)
    return history


def decorated_brc_dp(max_len, weights=None):
    """Exact F_M(z, turns, last), retaining typed terminal signed branch."""
    n = {(ZERO, 0, None): Fraction(1) if weights else 1}
    history = [n]
    for m in range(max_len):
        t = defaultdict(Fraction if weights else int)
        for (z, c, previous), val in n.items():
            for label in A:
                c_next = c + int(previous is not None and previous != label)
                t[(add(z, step(label)), c_next, label)] += val * (weights[label] if weights else 1)
        n = dict(t)
        history.append(n)
    return history


def verify_marginals(plain, decorated):
    count = 0
    for m in range(len(plain)):
        aggregate = defaultdict(int)
        for (z, c, last), multiplicity in decorated[m].items():
            assert multiplicity >= 0
            aggregate[z] += multiplicity
            count += 1
        assert dict(aggregate) == plain[m]
    return count


def advance_compressed(state, suffix):
    z, m, c, last = state
    for label in suffix:
        c += int(last is not None and last != label)
        z = add(z, step(label))
        m += 1
        last = label
    return z, m, c, last


def check_all_suffixes():
    words = [()]
    for m in range(1, 4):
        words.extend(product(A, repeat=m))
    suffixes = [()]
    for m in range(1, 3):
        suffixes.extend(product(A, repeat=m))
    checks = 0
    for word in words:
        z = path_endpoint(word)
        assert recover_from_relative_and_depth(z) == z
        state = z, len(word), turns(word), word[-1] if word else None
        for suffix in suffixes:
            actual = word + suffix
            out = advance_compressed(state, suffix)
            assert out == (path_endpoint(actual), len(actual), turns(actual), actual[-1] if actual else None)
            checks += 1
    return len(words), len(suffixes), checks


def check_twelve_witness():
    witnesses = {}
    obs = None
    for d in A:
        ax, sign = d
        j = (ax + 1) % 6
        alpha = (j, 1)
        neg_alpha = (j, -1)
        neg_d = (ax, -sign)
        w = (alpha, neg_alpha, neg_d, d)
        assert path_endpoint(w) == ZERO and turns(w) == 3 and len(w) == 4
        current_obs = (relative_triples(ZERO), 0, len(w), signed_endpoint_kernel(4, ZERO), turns(w))
        assert current_obs[3] == 396
        if obs is None:
            obs = current_obs
        assert current_obs == obs
        witnesses[d] = w
    pairs = 0
    for d, word in witnesses.items():
        for e, other in witnesses.items():
            if d != e:
                out_a = word + (d,)
                out_b = other + (d,)
                assert path_endpoint(out_a) == path_endpoint(out_b) == step(d)
                assert turns(out_a) == 3 and turns(out_b) == 4
                assert signed_endpoint_kernel(5, step(d)) == signed_endpoint_kernel(5, path_endpoint(out_b))
                pairs += 1
    assert len(witnesses) == 12 and pairs == 132
    return pairs, signed_endpoint_kernel(5, step(A[0]))


def check_exponential_family():
    b0 = ((0, 1), (1, 1), (1, -1), (0, -1))
    b1 = ((0, 1), (2, 1), (2, -1), (0, -1))
    assert b0 != b1
    checked = 0
    for n in range(1, 7):
        words = set()
        for flags in product((0, 1), repeat=n):
            w = tuple(y for f in flags for y in (b0 if f == 0 else b1))
            assert path_endpoint(w) == ZERO
            assert turns(w) == 4*n - 1
            assert len(w) == 4*n
            assert w[-1] == (0, -1)
            words.add(w)
        assert len(words) == 2**n
        checked += len(words)
    return checked


def check_restricted_alphabets():
    """Exact signatures for every one of 2^12 permitted future-step alphabets."""
    checked = 0
    for mask in range(1 << len(A)):
        allowed = {A[i] for i in range(len(A)) if mask & (1 << i)}
        signatures = {last if last in allowed else None for last in A}
        expected = len(allowed) + int(len(allowed) < len(A))
        assert len(signatures) == expected
        checked += 1
    return checked


def check_pop_boundary():
    plus = (0, 1)
    minus = (0, -1)
    w = (plus, plus, minus, plus)
    v = (plus, minus, plus, plus)
    assert path_endpoint(w) == path_endpoint(v) == (2, 0, 0, 0, 0, 0)
    assert turns(w) == turns(v) == 2 and w[-1] == v[-1] == plus
    assert signed_endpoint_kernel(4, path_endpoint(w)) == 64
    assert path_endpoint(w[:-1]) == path_endpoint(v[:-1]) == step(plus)
    assert signed_endpoint_kernel(3, step(plus)) == 33
    assert turns(w[:-1]) == 1 and turns(v[:-1]) == 2
    checked_shorter = 0
    for m in range(1, 4):
        bucket = {}
        for q in product(A, repeat=m):
            key = (path_endpoint(q), turns(q), q[-1])
            prefix_turns = turns(q[:-1])
            if key in bucket:
                assert bucket[key] == prefix_turns
            else:
                bucket[key] = prefix_turns
            checked_shorter += 1
    return checked_shorter


def main():
    dp = brc_dp(5)
    dec = decorated_brc_dp(5)
    marginals = verify_marginals(dp, dec)
    kernel_matches = 0
    for m, endpoints in enumerate(dp):
        assert sum(endpoints.values()) == 12**m
        for z, value in endpoints.items():
            assert signed_endpoint_kernel(m, z) == value
            kernel_matches += 1
    assert signed_endpoint_kernel(2, ZERO) == 12
    assert signed_endpoint_kernel(4, ZERO) == 396
    assert signed_endpoint_kernel(3, ZERO) == 0
    weights = {label: Fraction(i+2, i+3) for i, label in enumerate(A)}
    w_dp = brc_dp(4, weights)
    w_dec = decorated_brc_dp(4, weights)
    weighted_marginals = verify_marginals(w_dp, w_dec)
    weighted_matches = 0
    for m, endpoints in enumerate(w_dp):
        for z, value in endpoints.items():
            assert signed_endpoint_kernel(m, z, weights) == value
            weighted_matches += 1
    base_count, suffix_count, transition_checks = check_all_suffixes()
    witness_pairs, n5 = check_twelve_witness()
    exponential_checks = check_exponential_family()
    restricted_alphabets = check_restricted_alphabets()
    shorter_pop_words = check_pop_boundary()
    cert = {
        "schema":"STAGE393B_X6_TURN_REFINEMENT_EXACT_V1",
        "science_pin_em":"2af3fc484eb11060b69e0afc1b562bcaf5ad1419",
        "science_pin_p000_blob":"bcc2590d3168a28f72e8b9f0f9b1f76faadcd488",
        "source_kernel":"research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md#4",
        "native_axes":6,
        "signed_labels":12,
        "verified_length_range":[0,5],
        "kernel_endpoints_tested":kernel_matches,
        "decorated_states_tested":marginals,
        "weighted_length_range":[0,4],
        "weighted_endpoints_tested":weighted_matches,
        "weighted_decorated_states_tested":weighted_marginals,
        "path_prefixes_tested":base_count,
        "suffixes_tested":suffix_count,
        "append_compositions_checked":transition_checks,
        "return_2":signed_endpoint_kernel(2,ZERO),
        "return_4":signed_endpoint_kernel(4,ZERO),
        "after_one_step_endpoint_mass":n5,
        "common_fiber_size":12,
        "distinguishable_pairs_on_common_fiber":witness_pairs,
        "sharp_extra_bits_in_worst_fiber":4,
        "exponential_history_examples_checked":exponential_checks,
        "restricted_future_alphabets_exhaustively_classified":restricted_alphabets,
        "pop_one_step_exact_counterexample":"w=(+E1,+E1,-E1,+E1), v=(+E1,-E1,+E1,+E1): identical (z=2E1,m=4,N4=64,tau=2,last=+E1); after POP tau=1 vs 2 at z=E1,m=3,N3=33",
        "shorter_words_exhausted_for_pop_counterexample":shorter_pop_words,
        "exact_restricted_alphabet_repair_classes":"|L|+1 if L proper subset of the 12 signed steps; 12 if L is all steps",
        "unbounded_family_formula":"2^n histories of length 4n, endpoint 0, turns 4n-1 and last -E1, for each n>=1",
        "formal_all_words_proof":"one-step recurrence and induction; finite checks are corroboration only",
        "physical_dynamics_claimed":False,
        "native_source_result_or_review_claimed":False
    }
    encoded = (json.dumps(cert,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode()
    output = OUT / "CERTIFICATE_STAGE393B_X6_TURN_BRC.json"
    output.write_bytes(encoded)
    print("STAGE393B_X6_TURN_BRC_PASS")
    print("kernel_endpoints_tested="+str(kernel_matches))
    print("decorated_states_tested="+str(marginals))
    print("weighted_endpoints_tested="+str(weighted_matches))
    print("weighted_decorated_states_tested="+str(weighted_marginals))
    print("append_compositions_checked="+str(transition_checks))
    print("common_fiber_size=12;pair_separations="+str(witness_pairs))
    print("return_4=396;N_5(E1)="+str(n5))
    print("exponential_history_examples_checked="+str(exponential_checks))
    print("restricted_future_alphabets_exhaustively_classified="+str(restricted_alphabets))
    print("pop_counterexample=(4,2,64)->(3,1,33)/(3,2,33);shorter_words_exhausted="+str(shorter_pop_words))
    print("certificate_size="+str(len(encoded)))
    print("certificate_sha256="+sha256(encoded).hexdigest())

if __name__ == "__main__":
    main()
