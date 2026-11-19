# R5 D14 — twenty further exact f=8 references extend certified plateau to 25,896 named pairs

Date: 2026-11-20 (Asia/Shanghai). Contribution provenance: `EM-DIRECT-4C3E47` / original Research Activity `RA-F2257922D00B2FE4C4818DBD`. Status: AUTHOR_EXACT_FINITE_CHECKED / PARTIAL_INDEPENDENT_CROSSCHECK / NOT_REVIEWED.

## Model and frozen basis

This is an auxiliary **scalar** adaptive-identification theorem using the original 256 named hypotheses and all 101 physical query prices `k=214,...,314`, observation condition `2|y-N_h(k)| <= tau`, and up to eight **unflagged** errors. The robust endpoint is `tau=58182461585441404127941754879`. The frozen integer center table is `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`, `EXACT_R5_ALL_101_BUDGETS.json` with SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. No scientific input was rebased.

Fix `W=(0,16,32,48,1,64,17,80,18,24,34,82)`. Consider all `C(244,2)=29,646` unordered pairs `{u,v}` of additional labels. The original joint interval-support census has exactly 1,906 *priced full-joint-signature classes*, with the deterministic index numbering given by `CENSUS_14_SIGNATURES.cpp` in source commit `c328562411f49bd9981d54b2eeb9b0220a66986c`. No pairwise-only approximation is used.

## Theorem — exact certified subset

With `f=8`, the new twenty class-representative Bellman computations each give `V_8(W ∪ {u,v})=8335`. The rooted classes and exact representatives are in `ROOTS_NEW20.csv`. Combined with the previous 32 exact reference classes, the exact D14 price-and-support preorder certifies:

**For every additional-label pair in the resulting 25,896-pair coverage set, `V_8(W ∪ {u,v})=8335`.** This covers 1,220 of 1,906 signatures. The remaining 3,750 pairs in 686 classes remain unresolved by this certificate.

### Proof

For every query `k`, construct the inclusion-maximal **joint** support masks of all 14 closed feedback intervals using frozen integer centers. Keep the least physical price per identical maximal support family. Use full 14-name error counters `e_i∈{0,...,9}` and the exact minimax Bellman recurrence; a terminal state has at most one `e_i<=8`, and every admissible nonstalling action strictly raises an error counter, so recursion terminates. The twenty reported root DPs returned 8335.

Apply D14 from `awdawmip/enterprise-math@c328562411f49bd9981d54b2eeb9b0220a66986c:research_notes/portable_direct/r5_fourteen_dominance_20261120/RESEARCH.md`. Namely, `A ≼ B` if, for every B action, A has an action of no greater cost whose every maximal joint support mask lies inside some B support mask; allow either the identity labeling or swapping the two extra labels. D14 proves `V_8(A)<=V_8(B)` by virtual-feedback simulation for any error budget. For each of the 1,220 covered classes, at least one of the 52 root signatures dominates it in this sense. Hence its cost is at most 8335. Because every such game contains W, the established monotonic lower bound `V_8(W)=8335` gives equality.

The complete directed support-dominance matrix has 38,127 edges. Starting from 32 old references, the observed coverage was 1,008 classes / 23,828 pairs. Recomputing the matrix and extending the reference set by exactly the twenty IDs listed in `ROOTS_NEW20.csv` yields 1,220 classes / 25,896 pairs; this is **212 newly certified classes and 2,068 newly certified named pairs**.

## Independent check and numerical boundary

A separately constructed doubled-left-endpoint action oracle, evaluated by an independent nibble-packed C++ Bellman solver, returned `V_8(W∪{114,120})=8335` using 2,056,586 memoized states and seven priced actions. This is an implementation cross-check on one selected root, not an independent review of all twenty.

The attempts on representatives `(128,144)` and `(128,160)` were terminated by a short computational limit and excluded from the certified set. No conclusion about their optimal value follows from timeout. The full 256-hypothesis bound stays `8335 <= C_8* <= 8343`. This scalar result does not claim an isomorphic native X6, signed-Port or BRC reduction: it retains all fourteen **named hypothesis identities, joint supports and physical query costs**. The 14-bit mask is observer bookkeeping, not fourteen physical dimensions.

## Reproduction and next problem

Read `REPRODUCE.md`; the checker `CERTIFY_52_REFS.cpp` regenerates the same exact certificate from the pinned predecessor solver and census code. Source code, result table, frozen inputs and the independent oracle have separate provenance and verification status; no claim of project mathematical admission or formal CLAIM/RUN is made.

Next: tackle the remaining 686 hard signature classes, especially the two computationally interrupted (128,*) representatives, using shared Bellman-state bounds or stronger **policy-level** simulation. Seek a strict `V_8>8335` lower-bound witness, rather than extrapolating from the plateau.
