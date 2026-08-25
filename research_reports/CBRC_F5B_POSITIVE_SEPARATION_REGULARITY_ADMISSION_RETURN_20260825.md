# CBRC F5B — Positive-Separation Regularity Axiom Admission Return

Status: `CHECKPOINT_A_RAW_MATH_FREEZE`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`
Owner branch: `research/cbrc-f5b-positive-separation-regularity-axiom-admission`
Taskbook source: `11c5c651df54cf0117f936d5dbf421e37b9b7a34`

## 0. Source scope

Mathematics used before this raw freeze is restricted to the three taskbook-whitelisted sources:

1. `research_inputs/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_PACKET_20260825.md@1cdfb6b1f8fb0806507c9a4ce72278461246034b`;
2. `driver_reviews/CBRC_F4_POSITIVE_SEPARATION_RANK_LIFT_DRIVER_REVIEW_20260823.md@54fefbc20ad485ce3a7cab95ca6146f6c711b7c1`;
3. `driver_reviews/CBRC_F5AR_INDEPENDENT_BRANCH_ONTOLOGY_AXIOM_ADMISSION_DRIVER_REVIEW_20260825.md@0c983a5c98456a4d9c4b6be29b9a988631984842`.

No downstream source is used.

## 1. Canonical notation

At the accepted rank-one scope write the canonical retraction as

`pi : C -> Z e`

with finite kernel `T = ker(pi)`, so a presentation `C ~= Z e + T` may be used for calculations but is not part of the proposed axiom.

For `n in Z`, define the finite-fiber envelope

`f(n) = min { q(z) : pi(z)=n e }`.

Because `q >= 0` and `0` lies in the zero fiber, `f(0)=0`.

The six issued candidates are:

- P0: `z != 0 => q(z)>0`;
- P1: `pi(z) != 0 => q(z)>0`;
- P2: `n != 0 => f(n)>0`;
- P3: `n != 0 => q(n e)>0`;
- P4: every nonzero active retained branch has positive scalar;
- P5: both outputs of an authorized elementary balanced split have positive scalar.

## 2. Q1 — exact candidate lattice

### 2.1 Scalar/fiber lattice

For finite `T`:

`P0 => P1 <=> P2 => P3`.

All displayed non-equivalence arrows are strict whenever a nontrivial finite kernel is available.

Proof of `P1 => P2`: for fixed `n != 0`, the finite fiber `pi^{-1}(n e)` consists entirely of positive scalar values under P1; a finite set of positive real numbers has positive minimum.

Proof of `P2 => P1`: every member of a fiber is at least its minimum, so a positive minimum forces every point in that fiber positive.

`P1 => P3` is the specialization to the embedded old copy. `P0 => P1` is immediate.

Strictness witnesses:

- `P1 !=> P0`: take `C=Z e + Z/2`, and set `q(n e+t)=1` when `n != 0`, `q(t)=0` when `n=0`. Then every nonzero free fiber is positive but the nonzero pure-kernel state has scalar zero.
- `P3 !=> P1`: take `C=Z e + Z/2`, set `q(n e)=1` for every `n != 0`, and set `q(n e+tau)=0` on the nontrivial torsion label. The old copy is nondegenerate while a nonzero free fiber contains scalar zero.

These are rank-one coefficient countermodels; no dynamic conclusion is inferred from them.

Without finiteness, P2 in its literal minimum form may be undefined because a minimum need not be attained. If P2 is replaced by the uniform form `inf_{pi(z)=ne} q(z)>0`, that uniform form still implies P1, but P1 does not imply it. An infinite torsion fiber with positive values `1/(k+1)` along a sequence is the exact obstruction. Thus finiteness is used for the equivalence, not for the intrinsic statement of P1.

### 2.2 Typed branch relations

P4 and P5 are not pure carrier predicates; their implications depend on the active-branch typing.

At the already admitted F5AR A0 scope, each elementary old-refining output has nonzero `pi` projection. Therefore:

- `P1 => P5`;
- `P4 => P5` for elementary outputs, because A0 makes those outputs nonzero active states;
- `P0 => P4` and hence `P0 => P5`.

The converses fail strictly. P4 or P5 can hold on the typed elementary outputs while an inactive nonzero free-coordinate state has scalar zero. Conversely P1 need not imply unrestricted P4 if a pure-kernel state is independently typed active, because P1 intentionally imposes no condition on `ker(pi)`.

Consequently P1 and unrestricted P4 are incomparable. P3 is likewise incomparable with P4/P5 once finite torsion labels and typing are allowed.

The only implication from P4/P5 that matters to the rank-one obstruction is negative: neither rule controls every nonzero free fiber.

### 2.3 Two weaker proof-side regularities discovered

The accepted F4 theorem produces a nonzero period of `f` for every non-signed-permutation free block. This exposes two rules strictly weaker than P2:

`P6_ZERO_SUBGROUP_EXCLUSION`:

`for every p != 0, there exists k>=1 with f(k p)>0`.

Equivalently, the zero set of `f` contains no nonzero subgroup `p Z`.

`P7_ENVELOPE_APERIODICITY`:

`f` has no nonzero period.

Relations:

`P2 => P6 => P7`, both strict.

Strictness examples:

- P6 without P2: set `f(2)=0`, `f(0)=0`, and `f(n)>0` for every other nonzero integer. No nonzero subgroup is contained in the zero set.
- P7 without P6: set `f(2k)=0` for every integer `k`, set `f(1)=1`, and assign a distinct positive value pattern on the remaining odd integers so that `1` is the unique point of value `1`. The zero set contains `2Z`, so P6 fails, while the unique value at `1` rules out every nonzero period.

Both P6 and P7 are sufficient to contradict the F4 period conclusion. They are therefore important proof-theoretic intermediates. They are not selected as working-extension axioms here because they are global arithmetic shape conditions on the already-formed envelope rather than local zero-separation semantics for coefficient states. P7 in particular can allow entire nonzero free fibers to have scalar zero. They are retained as model-relative proof-side conditions, not as the admission target.

## 3. Q2 — minimal serious free-block regularity

The exact positivity used by the accepted F4 contradiction is:

`f(p)>0`

at a nonzero period `p` forced by a non-signed-permutation `A in GL_2(Z)`.

Indeed, period `p != 0` and `f(0)=0` imply `f(p)=f(0)=0`; P2 contradicts this immediately.

Thus P2 is exactly sufficient for the accepted arbitrary finite-torsion F4 mechanism. By finite-fiber equivalence, P1 is equally strong at the issued rank-one scope.

Among the issued local separation candidates, P1/P2 are minimal:

- P0 adds positivity on pure-kernel states and is unnecessary;
- P3 controls only one selected point of each fiber and does not control the envelope minimum;
- P4 and P5 control typed branch states, not all free-coordinate fibers.

A fixed-block condition that merely requires positivity at one period produced for a particular `A` is formally weaker, but is target-dependent and is not a reusable regularity axiom. P6/P7 are reusable but nonlocal envelope-shape conditions and are classified as model-relative rather than admitted ontology.

### 3.1 Exact dynamic survivor when P1/P2 are removed

There is an exact torsion-free rank-one survivor with no finite-kernel complication:

`C = Z e`.

Let `q(n e)=h(n mod 6)` with

`h(0)=0, h(1)=1, h(2)=1/4, h(3)=3/4, h(4)=1/4, h(5)=1`.

Let the free block be

`A = [[-4,-3],[-3,-2]]`, with determinant `-1`.

It is not a signed permutation. Direct enumeration of the 36 residue pairs shows

`h(x)+h(y)=h(-4x-3y)+h(-3x-2y)` modulo 6,

so the marked scalar is exactly conserved for all integer pairs.

For the elementary input `(e,0)`, the first column is `(-4,-3)`, so both old projections are nonzero: A0 holds. Moreover

`q(-4 e)=1/4`, `q(-3 e)=3/4`,

so P5 holds and elementary active-output positivity holds. Nevertheless `q(6e)=0`, hence P1/P2/P3 fail and the non-signed free block survives.

This is the decisive dynamic witness that A0 plus P4/P5 cannot replace free-fiber/envelope separation.

### 3.2 Uniform coordinate omission family

For every integer `m>=2`, define

`q_m(n e)=0` when `m` divides `n`, and `q_m(n e)=1` otherwise,

and

`A_m=[[1,m],[m,1+m^2]]`.

Then `det(A_m)=1`, `A_m` is non-signed-permutation, `A_m` is the identity modulo `m`, and therefore the two-slot scalar is conserved exactly. This family shows that any local rule which simply omits an arbitrary prescribed nonzero coordinate magnitude from separation can be defeated at that omitted period. The reason P6/P7 evade this family is precisely that they constrain the zero-set/period structure globally rather than pointwise at every coordinate.

## 4. Q3 — rank-one closure with admitted A0

Assume the issued finite-torsion rank-one scope, balanced reversible marked conservation, P1, and admitted A0.

1. By finite-fiber equivalence, P1 gives P2.
2. By the accepted F4 period obstruction, every non-signed-permutation free block is impossible.
3. Hence any surviving rank-one free quotient block must be a signed permutation.
4. The first column of a signed-permutation `2 x 2` block has exactly one nonzero old coordinate and one zero old coordinate.
5. A0 requires both elementary old-refining output projections to be nonzero.
6. Contradiction.

Therefore no issued-scope torsion-free-rank-one balanced reversible conserving model survives P1+A0.

Conditional theorem status:

`A0 + FREE_PROJECTION_ZERO_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

`STATUS = WORKING_EXTENSION_THEOREM`.

No rank-two carrier is constructed or classified.

## 5. Q4 — conservativity and intrinsic formulation

The proposed local rule is

`FREE_PROJECTION_ZERO_SEPARATION`:

`pi(z) != 0 => q(z)>0`.

This is P1 stated intrinsically.

Conservativity audit:

- pure-kernel states `pi(z)=0` remain legal with scalar zero or positive scalar;
- exact signed cancellation remains legal: two pre-erasure states can each have nonzero projection and positive scalar while their recoalesced coefficient is zero, where `q(0)=0` remains mandatory;
- canonical Path/N/Boolean objects are unchanged because the rule constrains only the enriched marked-coefficient layer;
- no choice of splitting `C ~= Z e + T` is required in the axiom; only the canonical retraction `pi` is referenced;
- finite torsion is not required to state P1, but is required by the currently accepted P1-to-envelope-minimum route. For an infinite fiber one needs the stronger uniform-infimum form if the same envelope proof is desired;
- future enrichments acquire only one local scalar-separation obligation: a state retaining nonzero old signed projection may not have scalar zero. Pure enrichment directions remain unconstrained.

Compared with P0, this removes exactly the unnecessary pure-kernel positivity cost.

Compared with P2, it avoids making a finite minimum construction part of the axiom while remaining equivalent to P2 at the issued finite-torsion scope.

## 6. Checkpoint-A classification

Frozen mathematical classifications:

`F5B_POSITIVE_SEPARATION_REGULARITY_LATTICE_CLASSIFIED`.

`F5B_MINIMAL_FREE_BLOCK_OBSTRUCTION_REGULARITY_CLASSIFIED`.

`F5B_WORKING_EXTENSION_RANK_ONE_CLOSURE_CLASSIFIED`.

`F5B_POSITIVE_SEPARATION_CONSERVATIVITY_AND_ONTOLOGY_COST_CLASSIFIED`.

Provisional admission selection, pending source/target leak audit and exact pushed checker:

`F5B_ADMIT_RESTRICTED_FREE_FIBER_POSITIVITY_ONLY`.

The rule is not promoted to native Foundation truth.

## 7. Raw freeze

`RAW_MATH_FREEZE = true`.

No additional mathematical source is needed for the remaining checker, leak-audit, manifest and publication-liveness work.
