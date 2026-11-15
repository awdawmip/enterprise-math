# R762BI — Exact star-Port observer repair and error-correction tradeoff

Author-side research note, 2026-11-15. Task RS-X6-TRIADIC-CLOSURE-DYNAMICS / publication TP2-8B7E13C5904A2D6F1142. Previous conditional frontier R762BG (PR #2485) and R762BH (PR #2489). **Status: AUTHOR_PROVED_AND_EXACT_FINITE_CHECKED / NOT_REVIEWED.**

## Domain, typed inputs and claim

The P000 source pins are held fixed. This result studies the **explicitly conditional signed orientation observer** of R762BF/BG, not an already admitted native TRIADIC_CLOSURE_E predicate. Let X=F_2^6 with labeled native axes 1,...,6. Each hypothetical triad query T (a 3-element subset) reads the binary parity y_T(x)=sum_{i in T} x_i mod 2. P000's six axes, selected Cell anchor and primitive signed directions remain unchanged; none of the triad queries is assumed physically executable.

Fix one labeled observed source/Port axis, say axis 1, and retain all ten *star* triad queries B={T: |T|=3,1 in T}. The remaining ten queries N={T: |T|=3,1 not in T} are potential repair probes. Let H=B union E, E subseteq N, k=|E|. Define A_H:F_2^6 -> F_2^{10+k} by these labeled query rows and C_H=im(A_H). Exact Boolean error correction refers to Hamming distance; positive BRC branch multiplicity/provenance are separate data.

## Theorem 1 — Exact source kernel and word spectrum

A_B has rank five and kernel K=span{v}, where v=(0,1,1,1,1,1). Its image is the binary linear [10,5,4] code with distinct-codeword weight enumerator

    W_B(z) = 1 + 15 z^4 + 15 z^6 + z^10.

*Proof.* The ten homogeneous relations x_1+x_i+x_j=0, 2<=i<j<=6, imply that the five variables x_2,...,x_6 are equal; any two such relations identify their shared indices and force x_1=0. Hence K={0,v}. For t=x_1=0 and s of the five remaining coordinates equal to 1, the number of nonzero rows is s(5-s). For t=1 the number is 10-s(5-s). Binomial multiplicities C(5,s), divided by the kernel size two, give the displayed enumerator and minimum nonzero weight four. QED.

## Theorem 2 — Minimal noiseless repair and sharp distance spectrum

For every nonempty E, the kernel of A_H is trivial and rank(A_H)=6, because any non-star triple intersects the five ones of v in exactly three places and hence evaluates to 1. For every k>=1, the word A_H(v) has weight k, so d(C_H)<=k. Every other nonzero input has at least four nonzero star queries; therefore

    min(4,k) <= d(C_H) <= k,

and in particular d(C_H)=k for 1<=k<=4.

The complete classification of the finite family of all 2^10 choices E (each of the 64 inputs evaluated exactly) is:

| k | total queries | dimension | distances: number of E |
|---:|---:|---:|---|
| 0 | 10 | 5 | 4:1 |
| 1 | 11 | 6 | 1:10 |
| 2 | 12 | 6 | 2:45 |
| 3 | 13 | 6 | 3:120 |
| 4 | 14 | 6 | 4:210 |
| 5 | 15 | 6 | 4:90, 5:162 |
| 6 | 16 | 6 | 4:15, 5:180, 6:15 |
| 7 | 17 | 6 | 5:60, 6:60 |
| 8 | 18 | 6 | 6:45 |
| 9 | 19 | 6 | 7:10 |
| 10 | 20 | 6 | 8:1 |

Theorem 2's universal bounds are symbolic. The remaining census is a complete, reproducible finite classification: every E is represented by one 10-bit mask; the checker computes all 64 GF(2) outputs, verifies image rank and exact positive minimum Hamming weight; it checks every binomial-class total and its hard-coded expected spectrum. This is an exhaustive proof within this finite six-axis family, not a sampling claim.

Consequently, **with the ten labeled star probes retained**, the minimum total numbers of queries to uniquely recover all six bits after t arbitrary Boolean query errors are 11, 13, 15, 19 for t=0,1,2,3, respectively. For two-error correction, exactly 162 of the C(10,5)=252 five-query repair sets work. One witness is

    E={234,235,236,245,345} (axes indexed 1,...,6),

for which C_H is a [15,6,5] code. By the standard Hamming decoding bound d>=2t+1, this corrects any two flipped query outputs. For three-error correction the sharp [19,6,7] certificate agrees with R762BH; the new contribution is the fixed-star observer repair spectrum and the 15-probe/two-error construction.

## Theorem 3 — Exact BRC observer quotient and rotation obstruction

For the **named star Boolean observer**, x and x' are indistinguishable iff x'-x belongs to K={0,v}. The 64 source orientation states therefore form **32 distinct observer fibers of size two**. This quotient remains sufficient for future star readings under any transformations x->g x+a with g in the S5 axis-permutation subgroup fixing axis 1 and arbitrary fixed a in F_2^6: the linear kernel K is invariant under all such g, and translations cancel on differences.

Under the full P000 S6 *axis-permutation skeleton*, the coarser star-only quotient is no longer sufficient for the same future star observer. A permutation swapping axis 1 with axis 2 maps v to a different nonzero vector g(v) not in K. Thus a star probe detects A_B(gv) != A_B(0), although A_B(v)=A_B(0). In fact

    intersection_{g in S6} g^{-1} K = {0},

because two distinct one-dimensional GF(2) subspaces have zero intersection. The minimal sufficient source state for arbitrary subsequent S6 relabelings and star Boolean queries has **64 fibers (six bits)**. This holds already with one future permutation followed by one star-query round.

This theorem is an exact observer-and-future-operations statement. For BRC weighted or labeled branch counts, two source histories in one Boolean fiber may still require distinct provenance or weights; no total-mass collapse is licensed without a further fiber-constancy certificate.

## Reproduction and boundaries

Run the adjacent R762BI_STAR_PORT_VERIFY.js under Node.js >=18 and compare its stdout with R762BI_STAR_PORT_EVIDENCE.json. The checker asserts the full finite census over 1,024 probe sets and 65,536 state-vector evaluations, the rank/distance classes, and a concrete S6 source-kernel failure witness. The theorem assumes exact GF(2) booleans; it says nothing about unverified sign/phase amplitudes or noisy physical sensors.

Frozen input references:
- P000 machine, awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json
- P000 discrete triadic balance, same commit:definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md
- Current immutable Task Source: awdawmip/enterprise-math@b1e45f7e7b8513038bfa53c83c7074722204115b:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md
- Previous conditional code: PR #2485@480954c317acfaabe582a7f7f67af84d77627a8f
- Previous puncture theorem: PR #2489@c3f93be388175b2f5bb4d7eb953c2f1930684fe9

## Unfinished native question

Identify source-authenticated lawful signed TRIADIC_CLOSURE_E Cell/Link/Port incidence and actual V17/V29/V39 transport, then determine the genuine physically queryable subset H and admissible future operations g. Apply Theorem 3's exact kernel-stability test, and recalculate rank/distance after restriction. In particular check whether a native localized Port observer necessarily has ten star queries, fewer, or different typed incidences. Preserve the third source and its BRC path/provenance before observer collapse.

Researcher source identity: EM-X6-44BACF, session MCP-8b844b9054c94d40aaed0131426d3935 (historically verified; live CLAIM must be separately read). No native Result or independent Driver review asserted.
