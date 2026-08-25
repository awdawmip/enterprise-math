# CBRC F5B — Regularity Countermodel and Ablation Packet

Status: `FINAL_FROZEN`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`

## 1. Scalar/fiber strictness witnesses

### W0 — P1 does not imply P0

Take `C=Z e + Z/2` with nontrivial torsion element `tau` and define

`q(n e+t)=1` for `n != 0`, and `q(t)=0` for `n=0`.

Then P1, P2 and P3 hold but `q(tau)=0`, so P0 fails. `Z/2` is the smallest finite kernel that can separate P0 from P1.

### W1 — P3 does not imply P1/P2

On `C=Z e + Z/2`, define

- `q(n e)=1` for every `n != 0`;
- `q(n e+tau)=0` for every `n`;
- `q(0)=0`.

Then P3 holds, but the fiber over `e` contains a scalar-zero state, so P1 and P2 fail.

## 2. Typed-branch strictness

P4/P5 are typing predicates.

- P1 need not imply unrestricted P4: under W0, a pure-kernel scalar-zero state may be independently typed active outside the elementary old-refining A0 scope.
- P5 need not imply P4: elementary outputs can be positive while an unrelated active pure-kernel state is scalar-zero.
- P4/P5 need not imply P1/P2/P3: the exact period-6 survivor below has positive elementary outputs but a nonzero free coordinate with scalar zero.
- At the admitted A0 elementary scope, P1 implies P5 and P4 implies P5.

These logical witnesses are separate from the full dynamic survivor below.

## 3. Exact period-6 rank-one survivor

Let

`C=Z e`

and define `q(n e)=h(n mod 6)` by

`h(0)=0, h(1)=1, h(2)=1/4, h(3)=3/4, h(4)=1/4, h(5)=1`.

Let

`A=[[-4,-3],[-3,-2]]`.

Then:

- `det(A)=-1`;
- `A` is not a signed permutation;
- exact checking of all 36 residue pairs gives
  `h(x)+h(y)=h(-4x-3y)+h(-3x-2y)`;
- on `(e,0)`, both old projections `-4,-3` are nonzero, so A0 holds;
- the elementary output scalars are `1/4` and `3/4`, so P5 holds;
- `q(6e)=0`, so P1/P2/P3 fail.

Therefore:

`A0 + P5` does not close rank one.

If only those elementary outputs are typed active, elementary P4 also holds, so P4 is not a substitute for free-fiber separation.

## 4. Uniform pointwise-omission family

For every `m>=2`, define

`q_m(n e)=0` iff `m|n`, and `q_m(n e)=1` otherwise,

with

`A_m=[[1,m],[m,1+m^2]]`.

Then `det(A_m)=1`, `A_m` is non-signed-permutation, and `A_m` is the identity modulo `m`; therefore the two-slot scalar is exactly conserved. Yet `q_m(m e)=0`.

So any local rule that simply leaves some prescribed nonzero coordinate magnitude unprotected can be defeated at that period.

## 5. Weaker global intermediates

### P6 — zero-subgroup exclusion

`forall p != 0, exists k>=1 : f(kp)>0`.

P2 implies P6, strictly. Example: `f(0)=f(2)=0` and all other nonzero values positive satisfies P6 but not P2.

### P7 — envelope aperiodicity

`f` has no nonzero period.

P6 implies P7, strictly. Example: set every even value to zero, make `f(1)=1`, and assign the remaining odd values a nonperiodic positive pattern with `1` unique. Then P7 holds while P6 fails because `2Z` is zero.

Both P6 and P7 are sufficient against the F4 period conclusion, but they are global envelope-shape conditions and are not admitted as local separation axioms.

## 6. Mandatory ablations

| Ablation | Free-block obstruction | Rank-one closure | Conservativity / interpretation |
|---|---|---|---|
| 1. finite torsion fiber | P1 no longer gives a positive minimum without uniform gap/attainment | needs uniform-infimum P2 or finite attainment | P1 remains intrinsically meaningful |
| 2. pure-kernel positivity | unchanged | unchanged | improves conservativity; this is P0 -> P1 |
| 3. positivity on every nonzero free fiber | fails: period-6 survivor | fails even with A0+P5 | branch-local positivity is insufficient |
| 4. P3 finite-copy nondegeneracy | redundant under P1 | redundant under P1 | no separate cost |
| 5. P4 active-branch positivity | not used | elementary case follows from P1+A0 | no need to constrain unrelated kernel branches |
| 6. P5 elementary-output positivity | not used | follows from P1+A0 | no separate axiom |
| 7. fixed scalar law | accepted F4 envelope equation is lost if step-dependent | not derivable by that route | no common scalar invariant |
| 8. exact marked conservation | period theorem cannot be invoked | fails by that route | no invariant equation |
| 9. A0 projection nondegeneracy | unchanged | fails: accepted F4 torsion loophole returns | weaker extension |

## 7. A0 ablation boundary witness

The accepted F4 boundary witness is

`M(e,0)=((1,1),(0,1))` on `Z e + Z/2`.

Both enriched outputs are nonzero, but the second has old projection zero. Thus removing A0 leaves the signed-permutation torsion loophole even if P1/P2 have already eliminated non-signed free blocks.

## 8. Freeze

`PERIODIC_WEAK_SCALAR_RANK_ONE_SURVIVOR = EXACT`.

`A0_PLUS_P5_IS_INSUFFICIENT = true`.

`P0_PURE_KERNEL_POSITIVITY_IS_UNNECESSARY = true`.

`P3_SELECTED_COPY_POSITIVITY_IS_INSUFFICIENT = true`.

`P1_EQUIV_P2_FOR_FINITE_TORSION = true`.

`P6_P7_MODEL_RELATIVE_PROOF_SIDE_RULES = true`.
