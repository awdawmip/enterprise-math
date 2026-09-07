# Post-#1161 Binary First-Return — Driver/Steward Admission Packet

Status: `FREE_RESEARCH_ADMISSION_CANDIDATE / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Researcher: `EM-FREE-G61R8`
Date: `2026-09-08`
Parent: issue `#1161`

## 1. Decision requested

The reusable residue of the post-#1161 work should **not** be inserted wholesale into the positive/non-negative Weighted-BRC theorem ledger.

Recommended shared object after Driver/Steward acceptance:

`brc.binary_first_return_predictive_rg`

as a typed `T0_BRC` subtool that composes with:

- `T6_OPERATION_SAFE_QUOTIENT`;
- `T5_PRECISION_REFINEMENT`;
- `T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA`;
- `T7_FINITE_SYMMETRY_EQUIVARIANCE`.

The narrow theorem-promotion target is:

1. `BFR-T04-ALL-HORIZON-PREDICTIVE-MINIMALITY`;
2. `BFR-T05-FINITE-HORIZON-CLASS-COUNTS`;
3. `BFR-T06-GRADED-PREDICTIVE-QUOTIENT`.

Everything else is support, specialization, domain application, or a negative boundary.

## 2. BRC observer/provenance audit

Population: two concrete branch witnesses `A,B` retained as path/provenance objects before recoalescence.

Branch-resolved memory:

`M_D = Z^D / Z*1`, temporarily coordinated by `z=#A-#B`.

Witness swap acts by `z -> -z`.

The unlabeled positive first-return observer sees only

`d=|z|`.

Information erased by the positive/unlabeled quotient:

- which witness is majority;
- the sign of the branch imbalance;
- any signed/phase cancellation data.

Information retained:

- exact first-hit future counts for the declared unlabeled observer;
- exact finite-horizon predictive class;
- equal-mass first-return probability.

Therefore:

`POSITIVE_FIRST_RETURN_MASS != SIGNED_BRANCH_MEMORY`.

`BOOLEAN_RECOALESCENCE != MULTIPLICITY_OR_SIGN_RECONSTRUCTION`.

## 3. Deduplication against current tool families

### T0 / BRC

`REUSE_APPLIED`.

The two concrete paths are retained at path/multiplicity strength before positive mass projection. The candidate is a new typed specialization under T0, not a replacement for Boolean or Weighted-BRC.

### T6 / predictive quotient

`EXTEND_EXISTING_TOOL`.

Existing `predictive_quotient.py` computes predictive partitions on a declared **finite** state set. The new capability is an exact closed-form predictive tower for an **unbounded one-counter process**:

`Q_h={0,1,...,h,FAR}`.

The all-horizon state is infinite (`d in N_0`), while every finite horizon is finite and minimal.

### T5 / precision refinement

`COMPOSE_APPLIED`.

The horizon family forms an exact precision chain. Projections compose and commute with the horizon-changing kernel.

### T7 / finite symmetry

`REUSE_APPLIED`.

The K4/FCC 24-to-12 ordered-witness cover is already an equivariant-section problem. Existing stabilizer-fixed-lift calculus proves the no-section result; no new symmetry tool is needed.

### T4 / fiber capacity

`COMPOSE_APPLIED`.

Same visible `(Cell,time)` with distinct future signatures gives the hidden-fiber capacity lower bound. No new capacity tool family is needed.

## 4. Theorem admission matrix

| ID | Recommendation | Reason |
|---|---|---|
| BFR-T01 | support lemma only | Catalan first-return enumeration is classical; retain exact implementation, no novelty claim |
| BFR-T02 | support lemma only | renewal/Catalan formal-series identity supports the tool and AGM facade |
| BFR-T03 | typed specialization | rank-one signed memory belongs to signed/group-completion + symmetry typing, not positive Weighted-BRC |
| **BFR-T04** | **promote** | exact minimal all-horizon predictor for the unbounded first-return process + fixed-finite-state no-go |
| **BFR-T05** | **promote** | closed-form minimal finite-horizon quotient with `h+2` / `2h+2` class counts |
| **BFR-T06** | **promote highest priority** | explicit graded operation-safe quotient and cross-horizon naturality; strongest reusable interface |
| BFR-T07 | T4 application / regression | useful hidden-fiber lower bound but no new capacity calculus |
| BFR-T08 | T7 application / observer boundary | swap-invariant scalar descent is a symmetry/observer consequence |

## 5. Core candidate theorems

### BFR-T04 — all-horizon predictive minimality

For still-alive two-branch histories under the first-hit/first-balance observer, the complete unlabeled future factors through

`d=|#A-#B|`.

Distinct `d` are distinguishable because the earliest possible return time is `d` (with parity respected). Hence no fixed finite exact predictive automaton can encode all horizons.

This is observer-relative and does not assert a universal lower bound for unrelated branch systems.

### BFR-T05 — finite-horizon exact quotient

For remaining horizon `h`, the exact unlabeled quotient is

`Q_h={0,1,...,h,FAR_h}`

with `h+2` classes. The branch-resolved labeled-future quotient has `2h+2` classes.

This is stronger than merely running a finite partition-refinement oracle: it gives the quotient in closed form for an infinite source process.

### BFR-T06 — graded quotient naturality

Let `K` be the absorbing nonnegative-counter kernel and `q_h` the projection to `Q_h`. There is an exact rational horizon-changing kernel

`K_h: Q_h -> Prob(Q_{h-1})`

such that

`q_{h-1} K = K_h q_h`.

For `1<=k<=h`, the precision projection also satisfies

`pi_{h-1,k-1} K_h = K_k pi_{h,k}`.

Thus the finite predictive tower is operation-safe and natural across horizons.

## 6. AGM domain facade

`src/enterprise_math/agm_first_return_rg.py` is deliberately thin. It uses the generic binary-return subtool to provide:

- `F_N(s)`;
- `T_N(s)=F_N/(2-F_N)`;
- one-shell `T_1=s^2/(4-s^2)`;
- finite-depth error bounds;
- standard-orbit adaptive depth;
- K4/S4 scalar state cost.

AGM-specific conclusions remain domain results. In particular, the facade does not independently identify the endogenous completion constant with classical `pi`.

## 7. Admission boundaries

Do **not** on this packet alone:

- modify `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_THEOREM_LEDGER_20260902.json`;
- claim positive Weighted-BRC carries signed branch-majority data;
- promote N1/path memory to instantaneous G0/N0 Cell state;
- register a new top-level tool family;
- claim the AGM Pareto certificate is a universal complexity lower bound;
- claim novelty for Catalan enumeration or the formal renewal identity.

## 8. Verification surface

Executable candidate:

- `src/enterprise_math/brc_binary_first_return.py`;
- `tests/test_brc_binary_first_return.py`.

AGM facade:

- `src/enterprise_math/agm_first_return_rg.py`;
- `tests/test_agm_first_return_rg.py`.

The generic tests cover:

- first-return shell counts and rational masses;
- 64 renewal coefficients;
- signed/common-shift/swap laws;
- finite-horizon predictive class counts;
- exact full-counter factorization;
- graded projection/dynamics naturality.

The AGM facade tests cover:

- one-shell formula;
- positive-shape monotonicity and quadratic bounds;
- exact `s=0` degeneration;
- finite geometric-channel monotonicity;
- standard adaptive schedule/state cost;
- exact rational return masses.

## 9. Recommended Driver/Steward disposition

If the targeted tests and typing audit pass on current `main`:

1. accept `brc.binary_first_return_predictive_rg` as a **GLOBAL_SUBTOOL under T0_BRC**, not a new top-level family;
2. publish a typed binary-first-return theorem subledger containing `BFR-T04~T06` plus support/negative boundaries;
3. expose `T01/T02` as support lemmas without novelty claims;
4. keep `T03`, `T07`, `T08` as typed specialization/reuse results;
5. keep the AGM facade as a domain operator;
6. leave P000 and the positive Weighted-BRC ledger unchanged unless a separate Steward theorem explicitly changes those surfaces.
