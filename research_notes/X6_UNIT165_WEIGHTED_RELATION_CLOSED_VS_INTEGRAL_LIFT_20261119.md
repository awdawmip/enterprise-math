# X6 Unit165 — A3 weighted relation-field: exact integral-lift obstruction and typed consumer boundary

- Date: 2026-11-19
- Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`
- Mother objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`
- Researcher: `EM-X6-FB6990`; own session `MCP-082892eb480e45dea6d4b9fcc0491034`
- Frozen scientific pin: `59538f585d037d09ef687b28715c4bc1a3f9fe03`
- Frozen comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`
- Status: AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED. This derived A3 relation field is not the native X6 N-BRC path-count carrier.

## Exact source and observed caller

At the immutable comparison commit:
- `src/enterprise_math/weighted_relation_field.py` blob `e50bf991e4dc4280063556a7aad1028f9f9404ed`: constructor lines 71–82 computes `Z_ij=m_j*c_i-m_i*c_j`; closure validator 85–110 checks integer antisymmetry and weighted three-block closure; total recovery lines 113–139 additionally checks divisibility by `M`; coarsening 142–172 checks closedness.
- `tests/test_weighted_relation_field.py` blob `51748dfe340c385907c4f2218fa1ae5ae2260522`: generated-field closure 23–29, recovery 30–39, coarsening 40–74, merge 75–88 and binary split 89–101. These tests use fields generated from integer totals; they do not establish that every closed integer array has an integer lift.

## Theorem: sharp integer-lift criterion

Let `n>=1`, positive integer capacities `m=(m_1,...,m_n)`, `g=gcd(m_1,...,m_n)`, and integer matrix `Z` such that `Z_ii=0`, `Z_ji=-Z_ij`, and

`m_k Z_ij + m_i Z_jk + m_j Z_ki = 0` for all `i,j,k`.

Then the following are equivalent:

1. There are integer totals `c_i` with `Z_ij=m_j c_i-m_i c_j` for every pair.
2. `g | Z_ij` for every pair.
3. There exists an integer `C` such that `m_i C + R_i ≡ 0 (mod M)` for every `i`, where `M=sum_i m_i`, `R_i=sum_j Z_ij`.

If an integral lift `c^(0)` exists, **all** integer lifts are precisely `c^(0)+t(m/g)` for `t in Z`. Consequently, its achievable grand totals constitute the single residue class `C^(0) (mod M/g)`.

### Proof

Necessity of (2): every `m_i` is a multiple of `g`, so every `m_j c_i-m_i c_j` is divisible by `g`.

Sufficiency: write `u_i=m_i/g` and `Q_ij=Z_ij/g` (integers). Choose integer Bézout coefficients `v_j` such that `sum_j v_j u_j=1`. Define `c_i=sum_j v_j Q_ij`. From weighted closure,

`u_k Q_ij = u_j Q_ik - u_i Q_jk`.

Multiply by `v_k` and sum `k` to obtain `Q_ij=u_j c_i-u_i c_j`. Multiplying by `g` gives `Z_ij=m_j c_i-m_i c_j`.

For (1) iff (3), summing the defining relation over `j` gives `R_i=M c_i-m_i C` with `C=sum c_i`. Conversely, weighted closure summed over `k` gives `M Z_ij=m_j R_i-m_i R_j`. For any `C` satisfying the stated congruences, let `c_i=(m_i C+R_i)/M`. These are integers, their sum equals `C` because `sum_i R_i=0`, and they reproduce `Z`.

If `c,c'` are two lifts, put `d=c-c'`. Then `u_j d_i=u_i d_j`. Since `u` is primitive, Bézout implies `d=t u` with integer `t`. The grand-total statement follows from summing coordinates. For `n=1`, closure forces `Z=[0]` and the same statement holds.

### Exact counterexample and consumer meaning

Take `m=(2,2)`, `Z=((0,1),(-1,0))`. The validator's weighted closure is satisfied (no nontrivial three-block constraint), but `g=2` fails to divide `Z_12=1`; integer totals are impossible. Over rational totals `(1/2,0)` it is realizable, so this is **an integrality residual, not a failure of rational closure**. Coarsening the two blocks into a single block yields `m'=(4)`, `Z'=(0)`, for which an integer lift exists; this quotient loses the original obstruction.

The current function `weighted_relation_field_is_closed` promises closure, and `recover_totals_from_weighted_field` separately verifies integrality for a supplied `C`: no wrong native path-count call is proved by this example. Consumers must not treat `is_closed=True` alone as proof of an integer-valued source state; if that stronger guarantee is needed, apply the sharp `g | Z` test (or the existing supplied-`C` recovery).

Here `Z` is a signed derived A3 relation entry; its differences and cancellations are **not** subtraction of nonnegative native N-BRC path multiplicities. This checked historical production/test pair is therefore not evidence for the unresolved LP019 wrongful native path-count subtraction. LP011 alleged native argmax also remains unresolved.

## Independent exact computation

An integer-only standalone checker exhausts:
- `n in {2,3}`, each capacity `m_i in {1,2,3}`, each independent antisymmetric entry `Z_ij in {-5,...,5}`: 36,036 arrays.
- Of these 1,362 satisfy weighted closure: 1,192 integrally lift and 170 do not.
- Every closed case agrees across three independent tests: `g | all Z_ij`; solvability of the row-sum congruences `C mod M`; and solvability of the pivot congruences `m_i t ≡ -Z_i0 (mod m_0)`.
- Every positive witness is reconstructed and checked against all entries. Zero disagreement. Normal Python, `-O` and `-OO` all pass.

Checker: `research_checks/X6_UNIT165_WEIGHTED_RELATION_INTEGRAL_LIFT_CHECK_20261119.py`; result: `research_checks/X6_UNIT165_WEIGHTED_RELATION_INTEGRAL_LIFT_RESULTS_20261119.json`.

## Original task implications / continuation

New source-level coverage: A3 weighted relation field constructor → closure / recovery / coarsening → actual tests, with a necessary and sufficient integer-realizability refinement and a concrete quotient-information-loss witness. This is scoped to the derived relation-field type; no physical/native X6 transfer or defect allegation follows. Prior research on valid generated integer fields is reused.

Maintain exact historical-source provenance for LP011 and LP019 as UNRESOLVED_PROVENANCE, continue remaining 28-LP production consumer coverage, preserve Units149–152 semantic-link debt, original R063 benchmark evidence, and independent Driver review. The unit is author-level, not admitted.
