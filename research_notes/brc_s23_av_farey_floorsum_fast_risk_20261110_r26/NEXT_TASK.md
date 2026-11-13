# R26 continuation — turn fast rank evaluation into a fast event/epoch generator

Scientific input remains frozen: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Current author-side frontier: R26 `PROOF.md` / `VERIFY_R26.py` / `RUN_EVIDENCE.md` in this directory. R25 is a predecessor; consume rather than re-enumerate its 323,000 cuts.

## Exact problem

Given `m=128`, an irrational theta in the certified 24-digit interval and integer horizon `N<=10^12+128`, the new R26 evaluator directly computes `R_n=A+B theta` using Farey successor classes and exact Euclidean floor-sum counts in time independent of `n` except integer bit lengths. Construct from the same per-historical-arc count functions a **source-labelled direct generator of maximal constant-increment epochs**, including exact integer endpoints of all plateau and growth runs; seek complexity bounded by number of output epochs rather than `N`.

## Concrete starting subproblem

For a fixed Farey bracket `a/i<theta<c/j`, the three source-index windows are `[0,n-i)`, `[n-i,j)`, `[j,n)`. The m historical arcs are fixed. Express the next n at which some `C_u(I),C_v(I),C_w(I)` crosses zero, or the winning gap type changes. Use floor-sum-based prefix monotonicity and binary rank/select to locate the event without scanning all intermediate insertions. Each event should retain its historical arc `I=(s,e)`, old/new winning type, and exact `A+B theta` increment.

Demonstrate an exact nonenumerative derivation of the known 67/36/61 and `q-164` periods near denominator 154021, then apply the same generator at 630382 and 10^12. If the generic event rule needs splitting when two gap lengths tie, give the exact tie branch. Verify against R16 298-row affine table, the R25 exact epochs and the R26 endpoint rank query.

## Acceptance evidence

A proof with quantifiers, Farey-bracket interval certificate, exact integer arithmetic, source labels, future observer scope, full input/precision/preprocessing/query/output bit-cost accounting. Runnable code and a finite exact verification. The R16 table is a regression comparator, not the proof of the new generator; independent review remains a separate step. Preserve Task owner/CLAIM/Result boundaries.

## Existing reuse

BRC source-labelled historical fibres: COMPOSE_APPLIED. Farey/three-gap successor theorem and Euclidean floor sums: COMPOSE_APPLIED; avoid new untyped top-level method names. If a current toolbox implementation covers the required rank/select query, execute or extend it under its actual contract.
