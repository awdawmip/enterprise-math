# R5 fifth noise chamber — exhaustive single-mask extension obstruction at f=8

Date: 2026-11-17. Frozen scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Derived observer: 256 named masks, 101 integer-cost queries k=214,...,314. Exact 25,856-count input table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## New theorem (precisely scoped)

For hypothesis set H, let C_f(H;tau) be the minimum worst-case sum of physical query costs of a finite adaptive tree identifying a member of H, where uncorrupted real answers y satisfy |y-N_h(k)| <= tau/2, and at most f answers are arbitrary, unmarked corruptions. Fix f=8, left endpoint L=25845652773852463277015040000, and H0=(18,24,82,34,17).

**For every h in {0,...,255} outside H0, C_8(H0 union {h};L)=8335.**

All **251** six-mask games were computed exactly, using all 101 physical query choices. In all 251 cases the restricted minimax root equals 8335. Therefore expanding the existing five-mask left-endpoint lower-bound witness by **one** actual named state does not strengthen its f=8 certificate. The full 256-mask game's existing bound throughout L<=tau<U=58182461585441404127941754880 remains 8335<=C_8^*(tau)<=8343. This is a method-specific lower-bound obstruction at L; its six-mask equality alone is neither a full-game upper construction nor a statement for all larger tau. A larger lower certificate would need a different base witness, at least two additional named masks, or another lower-bound method.

## Exact exhaustive proof

For each h not in H0, form ordered H=(18,24,82,34,17,h). At each query k=214,...,314, fetch all six integer centers from the original pinned 101x256 table. Each real answer's normal-compatibility support consists of centers lying in an interval of width L. Enumerating closed intervals [c,c+L] with c one of the six observed centers generates all inclusion-maximal supports after dropping proper subsets. Equal maximal-support families induce identical successors at every mismatch vector; retain the cheapest k per equal family. Every original query is included before this exact dominance quotient.

Represent transcript ambiguity by six counters e_i=min(9,number of incompatible answers for hypothesis i). The sentinel 9 eliminates a hypothesis. If at most one counter is <=8, the game is won and V(e)=0. Otherwise exact Bellman minimax is

```
V(e) = min_k (k + max_{A in MaxSupports(k)} V(T_A(e))),
T_A(e)_i = min(9,e_i+1[i not in A]).
```

Queries permitting a self-loop cannot win against a repetitive adversary and are omitted. Every retained transition increases a live mismatch counter, so recurrence is finite and acyclic. C++17 packs six 4-bit counters into an exact unsigned key and uses full equality in the memo; no floating point, hashing approximation or numerical tolerance enters the proof.

The 251 independent executions returned a root value of 8335 in each case. The per-game memo states range 39,312..258,748, totaling 28,297,865 across the separate games. Exactly 59 cases have seven distinct cheapest maximal-support families and 192 cases have eight families.

Reproduction programs: `SWEEP_SIX.py` and `VERIFY_SIX.cpp` in this directory. They require `EXACT_R5_ALL_101_BUDGETS.json` from the pinned R5 reproducibility package, verify its SHA-256, recompute all 101 supports, run the complete six-state minimax, and emit all 251 per-mask results. Local full-result JSON SHA-256: `57be8a7aeab470efd7c7e72aafb3d473ff93c5bec83f4b48b31cd5afad6b411e`. Canonical digest over ordered rows `h:cost:states:family_count`, comma-separated: `c57bbe5837a4161fdd654060b5f2a07ed80bfa9b8d8354337fee4277f32410d0`.

Crosschecks: for added h=0,48,160, all f=0,...,8 reproduced the existing 735+950f series; seven additional *sampled* seven-mask sets H0+{0,h} for h=1,16,32,48,80,160,255 each had value 8335 at f=8. The latter are not an exhaustive seven-state conclusion.

## Next discriminating question

Compute a full 256-state f=8 upper strategy at 8335 or seek a different lower bound incorporating interactions among at least two additional states. An f=8 bitplane solver must detect eliminated sentinel 9 as binary `1001`; the f=7 shortcut (eliminated when high plane is set, sentinel 8) is invalid at f=8. Preserve the derived-scalar versus native X6/BRC-provenance interface and the frozen scientific input.

Original native registration receipt `r5-20261117-2144-turn11-author-session-start-v1` was read back as SUCCEEDED, researcher `EM-DIRECT-AEEFF0`, Activity `RA-B1A5102AD1877F18B4C40118`. Publication here is independent GitHub science preservation, not a formal CLAIM, protected PROGRESS/Result/Review, or P000 change.
