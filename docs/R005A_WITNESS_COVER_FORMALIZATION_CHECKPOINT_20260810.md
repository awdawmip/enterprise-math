# R005-A — Witness Cover Formalization Checkpoint

Status: `PROVED GENERIC STRUCTURE / LEAN CANDIDATE / LOCAL_LEAN_PENDING`  
Date: `2026-08-10`  
Owner: `R005-A — Enterprise Prime Algorithm Lab`  
Predecessor: `docs/R005A_PRIME_ALGORITHM_LAB_RESEARCH_CHECKPOINT_20260810.md`

## 1. Structural compression

The predecessor checkpoint separated four phenomena:

1. prime-sound descent iff rejection supports cover every composite;
2. pseudoprime = uncovered composite all-pass fiber;
3. root-factor witnesses have a unique least bounded basis;
4. bounded Miller–Rabin minimum bases can form a non-unique antichain.

This checkpoint identifies the generic mechanism behind the difference between (3) and (4).

For a witness `w`, call a composite `x` an **exclusive collision** when:

- `w` rejects `x`;
- every other witness passes `x`.

Call `w` **forced** when it has at least one exclusive collision.  Call `w` **mandatory** when every composite-covering witness family contains it.

## 2. New generic theorem family

Let `X` be any state type, `W` any witness type, `Prime : X -> Prop`, and `Pass : W -> X -> Prop`.

### T-A1 — support-cover descent

If the witness language is prime-sound, then exact all-pass primality descent holds iff the selected witness family covers every composite by rejection.

Equivalently:

`pseudoprime = uncovered composite in the all-pass fiber`.

### T-A2' — forced iff mandatory

Assume the full witness universe `Set.univ` covers every composite.

Then:

`MandatoryWitness(w) <-> ForcedWitness(w)`.

The nontrivial direction is a removal argument.  If `w` has no exclusive collision, every composite rejected by `w` has another rejector, so deleting `w` from the full universe leaves a cover.  Therefore `w` cannot be mandatory.

### T-A2'' — exact least-basis criterion

Let:

`ForcedBasis = {w : ForcedWitness(w)}`.

Under the same full-universe cover assumption:

> a least safe witness family under inclusion exists iff `ForcedBasis` itself covers every composite.

When it exists, `ForcedBasis` is the unique least family.

This distinguishes two notions that must not be conflated:

- **least under inclusion** — a family contained in every safe family;
- **minimum cardinality** — an optimization solution, possibly one member of an antichain.

## 3. Root-factor and Miller–Rabin as opposite instances

### Root-factor observer

On bounded `X_N`, let witness prime `p` reject `n` exactly when:

`p | n` and `p^2 <= n`.

For each `p <= sqrt(N)`, `p^2` is an exclusive collision for `p`: no other prime witness divides `p^2`.  Conversely a witness `p > sqrt(N)` rejects no bounded state.  Hence the forced basis is exactly:

`{p prime : p <= sqrt(N)}`.

Every bounded composite has a prime factor at most its square root, so this forced basis covers every composite.  The generic least-basis theorem therefore recovers the unique least root-factor basis.

The focused executable probe exhausts every witness subset for `N=30`.  With witness universe

`[2,3,5,7,11,13,17,19,23,29]`,

it finds forced basis `[2,3,5]`, exactly `128` safe families, and confirms that all safe families contain `[2,3,5]` while `[2,3,5]` itself is safe.

The root-horizon semantics also produces mixed exclusive collisions before larger prime witnesses activate; e.g. witness `2` exclusively rejects `6` because the witness `3` is not active until `3^2 <= n`.  The square `p^2` remains the clean universal necessity witness.

### Miller–Rabin candidate language

For candidate bases

`[2,3,5,7,11,13,17,19,23,29]`

through `N=100000`, the exact probe finds:

- fourteen different minimum two-base safe families;
- no candidate base has an exclusive composite collision relative to the full candidate universe;
- therefore the forced basis is empty;
- the empty basis does not cover the nonempty composite universe;
- therefore **no least safe subset under inclusion exists**.

This gives a structural explanation for why the existing P018/P023 unique-least action basis cannot be generalized to arbitrary witness systems.

## 4. T-A3 — rejection strength is not binary partition refinement

Define pass-strength by pass-set inclusion.  Define binary partition refinement by kernel inclusion: equality of the stronger observation bit must force equality of the weaker observation bit.

If `Pass(f)` is a strict subset of `Pass(g)`, some state passes `f`, and some state fails `g`, then the two one-bit partitions are incomparable.

Concrete finite witness domain:

- `341`: Fermat base 2 PASS, MR base 2 FAIL;
- `17`: both PASS;
- `9`: both FAIL.

Thus MR2 is the stronger rejection filter on this domain, but neither one-bit partition refines the other.

## 5. Artifacts

### Lean candidate

`EnterpriseMath/Prime/WitnessCover.lean`

contains generic definitions and theorem candidates for:

- prime-sound all-pass descent;
- pseudoprime/uncovered-fiber equivalence;
- forced and mandatory witnesses;
- forced-basis least-cover criterion;
- pass-strength versus binary-partition refinement.

No `EnterpriseMath.lean` root import is added yet.

This execution environment has no Lean/Lake binary.  Therefore the only correct status is:

`LOCAL_LEAN_PENDING`

and none of these declarations is advertised as `LEAN_CHECKED`.

### Exact executable probe

`experiments/r005a_witness_cover_probe.py`

was executed independently before publication; all hard assertions passed.

## 6. Layering boundary

The new `RejectionSupport` is a unary subset of states rejected by one witness.  It is **not** automatically the existing A4 radius-indexed binary admissible relation support.  Any A4 bridge requires a separate reduction theorem.

The P018/P023 power-free action-basis theorem remains its own canonical specialization.  Its existing boundary-forcing theorem exhibits the same generic pattern — a boundary that can only be separated by one action — but this checkpoint does not duplicate or seize that theorem family.

## 7. Foundation feedback candidate

`FF-R005A-6 — Forced-witness criterion for least observation bases`

Weakest current assumptions:

1. arbitrary state type;
2. arbitrary witness type;
3. exact truth predicate;
4. arbitrary binary pass relation;
5. the full witness universe covers every false/composite state.

Candidate reusable result:

- mandatory witness iff exclusive false-state collision;
- a least covering witness family exists iff the forced/mandatory witness set itself covers;
- when it exists, that set is the unique least family.

Status:

`PROVED GENERIC STRUCTURE / LEAN CANDIDATE / PRIOR-ART NOVELTY UNVERIFIED`

No claim is made that the underlying general set-cover fact is new mathematics.  The research question is whether the exact precision/witness/fiber packaging and cross-route use justify Foundation extraction.

## 8. Next

1. run actual Lean validation on `EnterpriseMath/Prime/WitnessCover.lean`;
2. if compiler-clean, formalize the concrete bounded root-factor instance;
3. test whether the generic forced-witness theorem can consume the existing P018/P023 boundary-forcing theorem without duplicating it;
4. only then decide Foundation/A2 promotion versus R005-local retention.
