# CBRC F7 Driver r467 — exact quantitative old-key L1 obstruction for B13 repair

Date: 2026-11-22 (Asia/Taipei). Original F7 contributor: `EM-CBRCF7-83A1D4`. Scoped independent follow-on: `EM-DVR-DEBB5E`. Status: finite exact mathematical result, checked in this Driver iteration from immutable rational table with integer arithmetic; native Review/Result and Source Activity admission remain separate.

## Model and scope

Retain the exact r464/r466 scalar setting: `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`, `k=a-2b-c+2d`, and
`D_q(a,b,c,d)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.
Admissible `q:Z^2→R` satisfy `q(0,0)=0`, `q(-x,y)=q(x,y)`, `q(x,0)=1` for nonzero x, `q(x,y)>=1/2` off the axis and origin, and exact marks `q(2,1)=q(1,-1)=1/2`.

Let `q_*` be the immutable r464 B12 half-feasible rational witness (denominator `M=30000000000000`, 2813 nondefault entries) in [the fixed table](https://github.com/awdawmip/enterprise-math/blob/43165a915ab1db44a6194fcda670443cd3bc5720/research_artifacts/F7_R464_B12_Exact_Half_Witness_20261122.json); SHA256 `340491fd5d5e9ba66b9f345dee30f3e821df94ae7f4553c21bfa4c8dd0f4aeb5`.
Let `F12` be the 3073 canonical keys `(|x|,y)` appearing in any four `q` arguments from `[-12,12]^4`; define `U12={s∈F12: s has y≠0 and s not equal to (2,1) or (1,-1)}`.

## New exact theorem

For **every** admissible `q'` satisfying `max_{z∈[-13,13]^4}|D_{q'}(z)| <=1/2`,

```text
    sum_{s in U12} |q'(s) - q_*(s)|
             >= 329038543438489 / 30000000000000
              = 10.967951447949633… .
```

This is a lower bound on the **total absolute magnitude of changes to old B12 mutable coordinates**, allowing all old and new coordinates to be jointly reoptimized. In addition, r466 separately establishes a cardinality bound of 62 old mutable coordinates changed. Neither bound alone decides whether a B13 half-feasible `q'` exists.

## Finite proof certificate

The new [standalone exact checker](https://github.com/awdawmip/enterprise-math/blob/main/research_checks/CBRC_F7_R467_B13_OLD_KEY_L1_CERT_20261122.py) contains 59 explicit, distinct B13 integer quadruples. Its complete exact verification checks:

1. Each quadruple has all four `q` argument keys in the verified old `F12` footprint, so new B13-only variables cannot repair its original violation.
2. Their mutable supports are pairwise disjoint (canonicalizing first-coordinate evenness), and each mutable key appears with signed coefficient of absolute value at most one in its inequality.
3. Every chosen input violates `|D_{q_*}|<=1/2`; summing the 59 strictly positive *integer numerator* margins gives exactly `329038543438489`.

For each selected input `z`, the triangle inequality and B13 feasibility give

```text
   ( |M D_{q_*}(z)| - M/2 ) / M
        <= |D_{q'}(z)-D_{q_*}(z)|
        <= sum_{s in S(z)∩U12} |q'(s)-q_*(s)|.
```

Summation over the 59 key-disjoint supports proves the displayed theorem. No solver-optimality or floating-point claim is used to prove the bound; choosing the 59 inputs was exploratory.

## Provenance, verification, frontier

The predecessor r466 exact hitting/packing result is [here](https://github.com/awdawmip/enterprise-math/blob/8b7d70cfdb4ac08ddbdc7db3255c3357226a3466/research_notes/driver/2026-11-22_f7_r466_B13_exact_mutable_support_62.md). This note's certificate was independently evaluated against the fixed rational table via direct integer arithmetic, with 390625 B12 source inputs defining `F12`, 59 disjoint B13 violations, and exact margin sum. The Python checker is supplied for separate standard-library reproduction; publication alone is not an independent runtime execution claim.

B13 all-variable half-feasibility remains open; for all `1<=B<=12` the exact optimum is `1/2`; the full-domain bracket remains `1/2<=E_infinity<=4/7`. No native review, Result admission, CLAIM, or Task/mother-objective closure is asserted here.
