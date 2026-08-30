#!/usr/bin/env python3
from itertools import product, combinations
from math import gcd
import json

PRIMES = [3, 5, 7, 11, 13, 17]
SEMIPRIMES = [(p, q, p*q) for p, q in combinations(PRIMES, 2)]
ENTRY_VALUES = [-2, -1, 0, 1, 2]
MAX_STEPS = 7

def gcd_clean(N, x):
    g = gcd(N, abs(int(x)))
    return g == 1 or g == N

def det2(B):
    return B[0][0]*B[1][1] - B[0][1]*B[1][0]

def gcd_entries(B):
    g = 0
    for row in B:
        for x in row:
            g = gcd(g, abs(x))
    return g

def rank_q_2x2(B):
    if det2(B) != 0:
        return 2
    if any(x != 0 for row in B for x in row):
        return 1
    return 0

def rank_mod_2x2(B, r):
    vals = [[x % r for x in row] for row in B]
    d = (vals[0][0]*vals[1][1] - vals[0][1]*vals[1][0]) % r
    if d != 0:
        return 2
    if any(x % r != 0 for row in vals for x in row):
        return 1
    return 0

def top_delta(B):
    rq = rank_q_2x2(B)
    if rq == 2:
        return abs(det2(B))
    if rq == 1:
        return gcd_entries(B)
    return 0

def clone(B):
    return [row[:] for row in B]

def row_add(B, dst, src, k):
    C = clone(B)
    C[dst][0] += k*C[src][0]
    C[dst][1] += k*C[src][1]
    return C

def col_add(B, dst, src, k):
    C = clone(B)
    C[0][dst] += k*C[0][src]
    C[1][dst] += k*C[1][src]
    return C

def row_swap(B):
    return [B[1][:], B[0][:]]

def col_swap(B):
    return [[B[0][1], B[0][0]], [B[1][1], B[1][0]]]

def row_sign(B, i):
    C = clone(B)
    C[i][0] = -C[i][0]
    C[i][1] = -C[i][1]
    return C

def col_sign(B, j):
    C = clone(B)
    C[0][j] = -C[0][j]
    C[1][j] = -C[1][j]
    return C

def repN(x, N):
    return x % N

def adaptive_unimodular_trace(B0, N):
    """
    Public non-ring control:
      - canonical representatives,
      - quotient/remainder,
      - carry,
      - history,
      - variable stopping.
    Data-plane updates are elementary unimodular row/column operations.
    The checker audits scalar-clean admissibility; it never branches on gcd.
    """
    B = clone(B0)
    history = 1
    transcript = []
    for t in range(MAX_STEPS):
        i = t & 1
        j = (t // 2) & 1
        a = repN(B[i][j] + history, N)
        b = repN(B[1-i][1-j] + 2*history + t, N)
        d = 2 + (t % 3)
        quo, rem = divmod(a, d)
        carry = 1 if a + b >= N else 0
        k = quo - rem + carry + ((history % 5) - 2)
        scalars = {
            "a": a,
            "b": b,
            "d": d,
            "quo": quo,
            "rem": rem,
            "carry": carry,
            "k": k,
            "history": history,
        }
        transcript.append(scalars)

        mode = (a + 2*b + quo + 3*carry + history + t) % 6
        if mode == 0:
            B = row_add(B, 0, 1, k)
        elif mode == 1:
            B = row_add(B, 1, 0, k)
        elif mode == 2:
            B = col_add(B, 0, 1, k)
        elif mode == 3:
            B = col_add(B, 1, 0, k)
        elif mode == 4:
            B = row_swap(B) if ((quo + carry) & 1) == 0 else row_sign(B, i)
        else:
            B = col_swap(B) if ((rem + carry) & 1) == 0 else col_sign(B, j)

        history = repN(history + quo + 3*rem + 5*carry + a + 2*b + t, N)
        if t >= 1 and ((history + carry + rem) % 7 == 0):
            break
    return B, transcript

def transcript_clean(N, transcript):
    for step in transcript:
        for x in step.values():
            if not gcd_clean(N, x):
                return False
    return True

def product_naturality_break_witness():
    # Carry semantics: c_m(a,b)=1 iff rep_m(a)+rep_m(b)>=m.
    # N=15, a=1, b=2 are scalar-clean.
    N, p, q = 15, 3, 5
    a, b = 1, 2
    def carry(m):
        return 1 if (a % m) + (b % m) >= m else 0
    cN, cp, cq = carry(N), carry(p), carry(q)
    assert (cN, cp, cq) == (0, 1, 0)

    U0 = [[1, 1], [0, 1]]
    U1 = [[1, 0], [1, 1]]
    global_p = [[x % p for x in row] for row in U0]
    global_q = [[x % q for x in row] for row in U0]
    component_p = [[x % p for x in row] for row in (U1 if cp else U0)]
    component_q = [[x % q for x in row] for row in (U1 if cq else U0)]

    assert global_p != component_p
    assert global_q == component_q
    assert det2(U0) == det2(U1) == 1
    assert gcd_clean(N, a) and gcd_clean(N, b)
    return {
        "N": N,
        "p": p,
        "q": q,
        "a": a,
        "b": b,
        "carry_N": cN,
        "carry_p": cp,
        "carry_q": cq,
        "global_branch": 0,
        "component_branches": [cp, cq],
        "det_U0": det2(U0),
        "det_U1": det2(U1),
        "scalar_clean": True,
        "crt_product_naturality_broken": True,
        "hidden_rank_asymmetry_created": False,
    }

def main():
    total_seed_cases = 0
    prior_support_rejected = 0
    scalar_transcript_rejected = 0
    admitted_clean_traces = 0
    rank_channel_checks = 0
    delta_invariance_checks = 0
    equal_rank_preservation_checks = 0
    longest_trace = 0

    for p, q, N in SEMIPRIMES:
        for vals in product(ENTRY_VALUES, repeat=4):
            B0 = [[vals[0], vals[1]], [vals[2], vals[3]]]
            total_seed_cases += 1

            # All raw seed entries are scalar-clean for odd N with entries in {-2,-1,0,1,2}.
            assert all(gcd_clean(N, x) for x in vals)

            delta0 = top_delta(B0)
            if not gcd_clean(N, delta0):
                prior_support_rejected += 1
                continue

            rp0 = rank_mod_2x2(B0, p)
            rq0 = rank_mod_2x2(B0, q)
            # Clean top determinantal support forces equal hidden rank in this 2x2 seed census.
            assert rp0 == rq0

            B1, transcript = adaptive_unimodular_trace(B0, N)
            longest_trace = max(longest_trace, len(transcript))

            # Exact integer determinantal-divisor invariance holds even on traces later rejected
            # by the scalar-clean firewall.
            assert top_delta(B1) == delta0
            delta_invariance_checks += 1
            assert rank_mod_2x2(B1, p) == rp0
            assert rank_mod_2x2(B1, q) == rq0
            rank_channel_checks += 2

            if not transcript_clean(N, transcript):
                scalar_transcript_rejected += 1
                continue

            admitted_clean_traces += 1
            assert rank_mod_2x2(B1, p) == rank_mod_2x2(B1, q)
            equal_rank_preservation_checks += 1
            assert gcd_clean(N, top_delta(B1))

    witness = product_naturality_break_witness()

    expected = {
        "total_seed_cases": 9375,
        "prior_support_rejected": 480,
        "scalar_transcript_rejected": 8020,
        "admitted_clean_traces": 875,
        "rank_channel_checks": 17790,
        "delta_invariance_checks": 8895,
        "equal_rank_preservation_checks": 875,
        "longest_realized_trace": 7,
    }
    observed = {
        "total_seed_cases": total_seed_cases,
        "prior_support_rejected": prior_support_rejected,
        "scalar_transcript_rejected": scalar_transcript_rejected,
        "admitted_clean_traces": admitted_clean_traces,
        "rank_channel_checks": rank_channel_checks,
        "delta_invariance_checks": delta_invariance_checks,
        "equal_rank_preservation_checks": equal_rank_preservation_checks,
        "longest_realized_trace": longest_trace,
    }
    assert observed == expected, (observed, expected)

    certificate = {
        "schema": "N_COUPLED_CRT_PRODUCT_NATURALITY_BREAK_UNIMODULAR_OBSTRUCTION_CERTIFICATE_V1",
        "semiprimes": len(SEMIPRIMES),
        "prime_set": PRIMES,
        "seed_entry_values": ENTRY_VALUES,
        "total_seed_cases": total_seed_cases,
        "prior_support_rejected": prior_support_rejected,
        "scalar_transcript_rejected": scalar_transcript_rejected,
        "admitted_clean_traces": admitted_clean_traces,
        "rank_channel_checks": rank_channel_checks,
        "delta_invariance_checks": delta_invariance_checks,
        "equal_rank_preservation_checks": equal_rank_preservation_checks,
        "max_steps": MAX_STEPS,
        "longest_realized_trace": longest_trace,
        "product_naturality_break_witness": witness,
        "expected_counts": expected,
        "symbolic_laws_guarded": [
            "B_T = U B_0 V with U,V integer-unimodular for every realized history/carry/quotient trace",
            "I_k(U B V) = I_k(B) for every determinantal ideal I_k",
            "top determinantal divisor is invariant under integer-unimodular equivalence",
            "rank_F_r(B_T mod r) = rank_F_r(B_0 mod r) for every prime r dividing N",
            "non-ring CRT-product naturality failure of the control transcript does not imply hidden-channel rank asymmetry",
            "any one-sided full-carrier rank defect after this grammar was already present in the seed support",
        ],
        "checker_execution": "PASS",
        "proof_role": "FINITE_REGRESSION_ONLY_NOT_GENERAL_PROOF",
    }
    print(json.dumps(certificate, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
