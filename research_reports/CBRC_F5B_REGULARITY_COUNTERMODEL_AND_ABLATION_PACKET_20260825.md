# CBRC F5B — Regularity Countermodel and Ablation Packet

Status: `CHECKPOINT_A_RAW_MATH_FREEZE`
Researcher-ID: `EM-CBRCF5B-B8E421`
Task-ID: `RS-CBRC-F5B-POSITIVE-SEPARATION-REGULARITY-AXIOM-ADMISSION`

## 1. Purpose

This packet separates three distinct questions:

1. logical implication among P0–P5;
2. actual sufficiency for the accepted F4 non-signed-free-block obstruction;
3. sufficiency for total rank-one closure after adding the already admitted elementary branch rule A0.

Typing-only countermodels below prove logical non-implication only. The period-6 model is the full dynamic survivor used to prove insufficiency of branch-local positivity.

## 2. Atomic strictness witnesses

### W0 — `P1 !=> P0`

Carrier:

`C = Z e + Z/2`, with nontrivial torsion element `tau`.

Scalar:

`q(n e+t)=1` if `n != 0`; `q(t)=0` if `n=0`.

Then P1, P2 and P3 hold, while `q(tau)=0`; hence P0 fails.

This is minimal in kernel size: a nontrivial kernel is necessary to distinguish P0 from P1, and `Z/2` is the smallest nontrivial finite kernel.

### W1 — `P3 !=> P1/P2`

Carrier:

`C = Z e + Z/2`.

Scalar:

- `q(n e)=1` for every `n != 0`;
- `q(n e+tau)=0` for every integer `n`;
- `q(0)=0`.

Then P3 holds, but the nonzero free fiber over `e` contains `e+tau` of scalar zero, so P1 and P2 fail.

Again `Z/2` is the smallest finite kernel that can separate the selected old copy from its full free fiber.

### W2 — `P1 !=> unrestricted P4`

Use W0 and type the pure-kernel state `tau` as an active retained enriched branch outside the elementary old-refining A0 scope. P1 still holds, while P4 fails because `q(tau)=0`.

This shows why P1 implies only the elementary-output positivity needed after A0, not a global active-branch positivity law for every possible enriched branch type.

### W3 — `P5 !=> P4`

Take an elementary old-refining pair whose two outputs have nonzero old projections and positive scalar, then add an unrelated active pure-kernel state of scalar zero. P5 continues to hold on the elementary pair while P4 fails on the extra active state.

No larger algebraic carrier is needed than `Z e + Z/2`.

### W4 — `P4/P5 !=> P3/P1/P2`

The exact dynamic period-6 survivor in Section 3 supplies the stronger witness: the elementary outputs are positive and may be the only states typed active in the declared elementary refinement, while `q(6e)=0`.

### W5 — `P3 !=> P5`

The distinction is possible only once a nontrivial fiber is present. On `Z e + Z/2`, keep `q(n e)>0` on the embedded old copy but allow an elementary A0-compatible output with nonzero old projection and nontrivial torsion label to have scalar zero; another elementary output carries the conserved scalar. P3 remains true while P5 fails. This is a typing/scalar strictness witness, not a full F4 dynamic survivor.

The full dynamic insufficiency statement does not rely on W5; it relies on Section 3.

## 3. Exact period-6 dynamic survivor

Carrier:

`C = Z e`, torsion-free rank one.

Scalar is periodic modulo 6:

| residue `r` | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| `h(r)` | 0 | 1 | 1/4 | 3/4 | 1/4 | 1 |

Set `q(n e)=h(n mod 6)`.

Free block:

`A=[[-4,-3],[-3,-2]]`, `det(A)=-1`.

Facts checked exactly over all 36 residue pairs:

`h(x)+h(y)=h(-4x-3y)+h(-3x-2y)`.

Hence the same equality holds for all integer pairs.

The matrix is not a signed permutation. For the elementary old input `(e,0)`, the two old projections are `-4` and `-3`, so A0 holds. The two scalar outputs are respectively `1/4` and `3/4`, so P5 holds and their scalar sum is exactly `1=q(e)`.

But `q(6e)=0`. Therefore P1, P2 and P3 fail.

Conclusion:

`A0 + P5` does not close rank one.

If the active-branch typing is restricted to these elementary retained outputs, the same model also satisfies P4 at that declared scope. Thus branch-local scalar positivity cannot replace free-fiber/envelope separation.

## 4. Pointwise-omission family

For every integer `m>=2`, let

`q_m(n e)=0` iff `m | n`, otherwise `q_m(n e)=1`,

and

`A_m=[[1,m],[m,1+m^2]]`.

Then:

- `det(A_m)=1`;
- `A_m` is non-signed-permutation;
- `A_m` is coordinatewise the identity modulo `m`;
- therefore `q_m(x)+q_m(y)` is exactly conserved by `A_m`;
- `q_m(e)=1`;
- `q_m(m e)=0`.

This proves that a local separation rule which simply omits an arbitrary coordinate magnitude `m>=2` can be defeated at that omitted period.

## 5. Intermediate-rule strictness

### P6 — zero-subgroup exclusion

`forall p != 0, exists k>=1 : f(kp)>0`.

P2 implies P6. Strict witness:

`f(0)=0`, `f(2)=0`, and `f(n)>0` for every other nonzero integer. P2 fails, but no nonzero subgroup lies entirely in the zero set, so P6 holds.

### P7 — envelope aperiodicity

There is no `p != 0` with `f(n+p)=f(n)` for every `n`.

P6 implies P7 because a period `p` and `f(0)=0` force `f(kp)=0` for every integer `k`, violating P6.

Strict witness for `P7 !=> P6`:

- `f(2k)=0` for every integer `k`;
- `f(1)=1`;
- every other odd integer receives a positive value different from `1` in a nonperiodic pattern.

Then `2Z` is contained in the zero set, so P6 fails; the unique value at `1` rules out every nonzero period, so P7 holds.

Both P6 and P7 contradict the F4 period conclusion and therefore are proof-theoretically sufficient. They are not selected as axioms because they are global envelope-shape restrictions rather than local scalar separation semantics.

## 6. Mandatory ablations

### ABL-1 — remove finiteness of the torsion fiber

With an infinite torsion fiber, P1 is only pointwise positivity. A sequence of fiber values `1/(k+1)` stays positive while its infimum is zero. Therefore the currently accepted finite-minimum route from P1 to P2 fails.

Effect:

- free-block obstruction from P1 alone: `FAILS_TO_FOLLOW`;
- repair: require actual minimum attainment or the uniform infimum version of P2;
- P1 intrinsic formulation: still meaningful.

### ABL-2 — remove positivity on pure-kernel states

This is exactly the weakening P0 -> P1.

Effect:

- free-block obstruction: `UNCHANGED`;
- rank-one closure with A0: `UNCHANGED`;
- conservativity: `IMPROVED`;
- pure enrichment states may remain scalar-zero.

This ablation is the main reason P0 is rejected as overstrong.

### ABL-3 — remove positivity on all nonzero free-coordinate fibers

The period-6 survivor gives an exact failure even with A0 and P5.

Effect:

- free-block obstruction: `FAILS`;
- rank-one closure: `FAILS`;
- interpretability: local branch positivity does not control the envelope zero set.

### ABL-4 — remove finite-copy nondegeneracy P3

Under P1, P3 is already implied. Removing P3 as a separate axiom has no effect.

Conversely, W1 proves P3 alone is insufficient because it does not control the minimum over a torsion fiber.

Effect under admitted P1:

- free-block obstruction: `UNCHANGED`;
- rank-one closure: `UNCHANGED`.

### ABL-5 — remove active-branch positivity P4

The F4 period proof does not use P4. Under P1+A0, elementary old-refining outputs have nonzero old projection and therefore positive scalar automatically.

Effect:

- free-block obstruction: `UNCHANGED`;
- elementary rank-one closure: `UNCHANGED`;
- no reason to constrain unrelated pure-kernel active states.

### ABL-6 — remove elementary-output positivity P5

Again P5 is derived at the elementary old-refining scope from P1+A0 and need not be independently admitted.

Effect:

- free-block obstruction: `UNCHANGED`;
- rank-one closure: `UNCHANGED` under P1+A0.

The period-6 survivor shows the converse is false: P5 without P1 is insufficient.

### ABL-7 — allow step-dependent scalar law/rescaling

The F4 mechanism passes one fixed scalar law to one fixed envelope `f` and derives a period from exact conservation. If the scalar can be replaced or rescaled from step to step, there is no single envelope functional equation to which the period theorem applies.

Effect:

- free-block obstruction by the accepted route: `FAILS`;
- rank-one closure by this route: `NOT DERIVABLE`;
- interpretation: no single marked invariant is being conserved.

### ABL-8 — remove exact marked conservation

Without

`Q(M(x,y))=Q(x,y)`

there is no induced free-envelope conservation equation, so the accepted period theorem cannot be invoked.

Effect:

- free-block obstruction: `FAILS`;
- rank-one closure: `FAILS BY THIS ROUTE`.

### ABL-9 — remove A0 branch-projection nondegeneracy

The free-block obstruction remains: P1/P2 still force the free quotient to be signed permutation.

But the accepted F4 torsion-mediated survivor remains available. Its elementary boundary witness is

`M(e,0)=((1,1),(0,1))` on `Z e + Z/2`;

the second output is a nonzero enriched state with zero old projection.

Effect:

- free-block obstruction: `UNCHANGED`;
- total rank-one closure: `FAILS`;
- exact remaining loophole: pure-kernel elementary retained output.

## 7. Ablation matrix

| Ablation | Free-block obstruction | Rank-one closure | Conservativity / interpretation |
|---|---|---|---|
| finite torsion | P1 route loses positive minimum | needs uniform P2/attainment | P1 remains meaningful |
| pure-kernel positivity | unchanged | unchanged | improves conservativity |
| all nonzero free-fiber positivity | fails | fails even with A0+P5 | branch-local rules insufficient |
| P3 | redundant under P1 | redundant under P1 | no extra cost |
| P4 | not used | elementary case derived | avoids global active-state burden |
| P5 | not used | derived from P1+A0 | no separate axiom |
| fixed scalar law | fails | not derivable | no common envelope |
| exact conservation | fails | fails by this route | no invariant equation |
| A0 | unchanged | fails | F4 torsion loophole returns |

## 8. Countermodel freeze

`PERIODIC_WEAK_SCALAR_RANK_ONE_SURVIVOR = EXACT`.

`A0_PLUS_P5_IS_INSUFFICIENT = true`.

`P0_PURE_KERNEL_POSITIVITY_IS_UNNECESSARY = true`.

`P3_SELECTED_COPY_POSITIVITY_IS_INSUFFICIENT_FOR_ENVELOPE_CONTROL = true`.

`P1_EQUIV_P2_FOR_FINITE_TORSION = true`.

`P6_P7_DISCOVERED_AS_WEAKER_MODEL_RELATIVE_PROOF_SIDE_RULES = true`.
