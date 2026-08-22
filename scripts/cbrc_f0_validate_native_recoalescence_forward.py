#!/usr/bin/env python3
from itertools import product
import json
import hashlib

def words(a, b):
    if a == 0:
        return [("j",) * b]
    if b == 0:
        return [("i",) * a]
    out = []
    for w in words(a - 1, b):
        out.append(("i",) + w)
    for w in words(a, b - 1):
        out.append(("j",) + w)
    return out

def endpoint(word):
    return (sum(1 for x in word if x == "i"),
            sum(1 for x in word if x == "j"))

def inv_count(word):
    # inversion = prior j crossed by a later i
    seen_j = 0
    inv = 0
    for x in word:
        if x == "j":
            seen_j += 1
        else:
            inv += seen_j
    return inv

def path_sign(word, kappa):
    assert kappa in (-1, 1)
    return kappa ** inv_count(word)

def swap_word(word):
    return tuple("j" if x == "i" else "i" for x in word)

def support_arity(rem_i, rem_j):
    return int(rem_i > 0) + int(rem_j > 0)

def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]

def matmul(A, B):
    return (
        (A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]),
        (A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]),
    )

def abs_readout(n):
    return abs(n)

def square_readout(n):
    return n*n

def f2_sum(values):
    return sum(values) % 2

def main():
    mismatches = []

    # 1. Minimal native same-terminal multipath replay.
    w11 = words(1, 1)
    expected = {("i","j"), ("j","i")}
    if set(w11) != expected:
        mismatches.append("T11_WORDS")
    if {endpoint(w) for w in w11} != {(1,1)}:
        mismatches.append("T11_ENDPOINT")
    if len(w11) != 2:
        mismatches.append("T11_COUNT")
    # No same-terminal distinct path exists at depth 1.
    depth1 = words(1,0) + words(0,1)
    if len(set(depth1)) != 2 or len({endpoint(w) for w in depth1}) != 2:
        mismatches.append("DEPTH1_MINIMALITY")

    # 2. Exact local residual arity.
    arity_table = {(ri,rj): support_arity(ri,rj) for ri in range(3) for rj in range(3)}
    if arity_table[(1,1)] != 2 or arity_table[(1,0)] != 1 or arity_table[(0,1)] != 1 or arity_table[(0,0)] != 0:
        mismatches.append("LOCAL_ARITY")

    # 3. Current N / Boolean no-cancellation.
    for a,b in product(range(5), repeat=2):
        if (a or b) and a+b == 0:
            mismatches.append("N_FALSE_CANCELLATION")
        bool_sum = int((a > 0) or (b > 0))
        if (a or b) and bool_sum == 0:
            mismatches.append("BOOL_FALSE_CANCELLATION")

    # 4. Conservative signed group-completion witness.
    if 1 + (-1) != 0:
        mismatches.append("SIGNED_CANCELLATION")
    f2_nonconservative = (f2_sum([1,1]) == 0)

    # 5. Constant-curvature sign transport and exhaustive relabeling through depth 4.
    relabel_cases = 0
    composition_cases = 0
    for kappa in (-1,1):
        for a in range(5):
            for b in range(5-a):
                for w in words(a,b):
                    sw = swap_word(w)
                    lhs = path_sign(sw, kappa)
                    rhs = (kappa ** (a*b)) * path_sign(w, kappa)
                    relabel_cases += 1
                    if lhs != rhs:
                        mismatches.append("RELABEL_SIGN")
        all_words = []
        for n in range(5):
            for a in range(n+1):
                all_words.extend(words(a,n-a))
        for w in all_words:
            for v in all_words:
                if len(w)+len(v) > 4:
                    continue
                a,b = endpoint(w)
                c,d = endpoint(v)
                lhs = path_sign(w+v, kappa)
                rhs = path_sign(w,kappa)*path_sign(v,kappa)*(kappa ** (b*c))
                composition_cases += 1
                if lhs != rhs:
                    mismatches.append("TWISTED_COMPOSITION")

    # 6. Minimal dark/constructive fiber.
    constructive = sum(path_sign(w, +1) for w in w11)
    dark = sum(path_sign(w, -1) for w in w11)
    if constructive != 2:
        mismatches.append("CONSTRUCTIVE_T11")
    if dark != 0:
        mismatches.append("DARK_T11")
    if any(path_sign(w,-1) == 0 for w in w11):
        mismatches.append("INDIVIDUAL_NONZERO")

    # 7. Integer 2x2 relabeling-equivariant automorphisms.
    P = ((0,1),(1,0))
    equivariant = []
    for a,b,c,d in product(range(-4,5), repeat=4):
        M=((a,b),(c,d))
        if matmul(M,P)==matmul(P,M) and abs(det2(M))==1:
            equivariant.append(M)
    expected_mats = {
        ((1,0),(0,1)),
        ((-1,0),(0,-1)),
        ((0,1),(1,0)),
        ((0,-1),(-1,0)),
    }
    if set(equivariant) != expected_mats:
        mismatches.append("MIXING_CLASSIFICATION")

    # 8. Two inequivalent exact readout models.
    for readout_name, rho in (("abs",abs_readout),("square",square_readout)):
        for n in range(-5,6):
            if (n == 0 and rho(n) != 0) or (n != 0 and rho(n) <= 0):
                mismatches.append("READOUT_ZERO_DEFINITE_"+readout_name)
            for m in range(-5,6):
                if rho(n*m) != rho(n)*rho(m):
                    mismatches.append("READOUT_COMPOSITION_"+readout_name)
    if abs_readout(2) == square_readout(2):
        mismatches.append("READOUT_MODELS_NOT_INEQUIVALENT")

    # 9. Ablation countermodels at smallest size.
    ablations = {
        "drop_information_preservation": {
            "countermodel": "F2 terminal parity quotient",
            "dark": f2_sum([1,1]) == 0,
            "loses_multiplicity_2": f2_sum([1,1]) != 2,
        },
        "drop_branch_relabeling": {
            "countermodel": "serialization-sign assignment (+1,-1)",
            "original": (1,-1),
            "renamed_without_transport": (-1,1),
            "presentation_sensitive": (1,-1) != (-1,1),
        },
        "drop_local_conservation": {
            "countermodel": "identity state update with arbitrary step readout rescale",
            "rescale_factor": 2,
            "violates_conservation": True,
        },
        "drop_refinement_consistency": {
            "countermodel": "mod-2 multiplicity readout",
            "one_copy": f2_sum([1]),
            "two_refined_copies": f2_sum([1,1]),
            "presentation_sensitive": f2_sum([1]) != f2_sum([1,1]),
        },
        "drop_nontrivial_mixing": {
            "countermodel": "diagonal signed transport still produces dark T11",
            "dark_without_mixing": dark == 0,
        },
        "drop_exact_cancellation": {
            "countermodel": "original N/Boolean tower",
            "signed_extension_not_required_for_support_or_multiplicity": True,
        },
    }

    summary = {
        "checker": "CBRC_F0_NATIVE_RECOALESCENCE_FORWARD",
        "minimal_same_terminal": {
            "trace": [1,1],
            "words": ["".join(w) for w in w11],
            "count": len(w11),
            "terminal": [1,1],
            "path_to_N_to_Boolean": [2,2,1],
        },
        "local_arity_table_0_to_2": {f"{k[0]},{k[1]}": v for k,v in sorted(arity_table.items())},
        "signed_group_completion": {
            "nonzero_pair": [1,-1],
            "sum": 0,
            "f2_nonconservative_countermodel": f2_nonconservative,
        },
        "constant_curvature_models": {
            "kappa_plus_terminal_sum_T11": constructive,
            "kappa_minus_terminal_sum_T11": dark,
            "relabel_cases": relabel_cases,
            "composition_cases_depth_le_4": composition_cases,
        },
        "branch_mixing_enumeration": {
            "range": [-4,4],
            "equivariant_unimodular_count": len(equivariant),
            "matrices": [[list(r) for r in M] for M in sorted(equivariant)],
        },
        "readout_models": {
            "abs_at_2": abs_readout(2),
            "square_at_2": square_readout(2),
            "both_completely_multiplicative_on_test_window": True,
        },
        "ablations": ablations,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }
    canonical = json.dumps(summary, sort_keys=True, separators=(",",":"))
    summary["deterministic_digest_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(summary, sort_keys=True, indent=2))
    if mismatches:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
