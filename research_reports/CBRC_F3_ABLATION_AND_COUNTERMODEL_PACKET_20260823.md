# CBRC F3 — Ablation and Countermodel Packet

Researcher-ID: `EM-CBRC-F3-7B31A9`

Canonical current-carrier witness:

`C1 = Z e ⊕ <tau | 3 tau=0>`

`A=[[2,3],[3,4]]`, `B=0`, `D=I`

`q_delta(n,a)=f(n)+delta*1_{3|n and a!=0}`, `delta>=0`,

with `f` six-periodic:

`[f(0),f(1),f(2),f(3),f(4),f(5)] = [0,1,1/2,1/2,1/2,1]`.

## A1. Remove M3 reversibility

Take the additive free map

`N=[[2,3],[3,2]]`.

Its determinant is `-5`, so it is not an automorphism of `Z^2`.

Nevertheless the same balanced six-periodic free scalar satisfies

`f(2x+3y)+f(3x+2y)=f(x)+f(y)`

for all integers `x,y`, because the identity is exact on residues modulo `6` and `f` is six-periodic.

The elementary split is still

`e -> (2e,3e)`

with scalar `1/2+1/2`.

Therefore reversibility is load-bearing for information preservation and inverse recoalescence, not for balanced scalar conservation by itself.

`ABLATION_M3 = STRICTLY_ENLARGES_CLASS`.

## A2. Remove M4 marker-relabeling choice independence

Before balance is imposed, the canonical reversible `A` conserves the exact one-parameter free scalar family

- `f_t(0)=0`,
- `f_t(±1)=1`,
- `f_t(±2)=t`,
- `f_t(3)=1-t`,

periodic modulo `6`, with `0<=t<=1`.

For example `t=1/4` gives

`q(2e)=1/4`, `q(3e)=3/4`.

The elementary total is conserved but one branch is preferred by scalar content. Marker-choice independence together with M5 is what removes this orientation parameter by forcing `t=1/2`.

`ABLATION_M4 = BALANCE_ORIENTATION_PARAMETER_SURVIVES`.

## A3. Remove M5 balanced two-nonzero-output condition

If no genuine two-branch positive balanced split is required, all signed-monomial free transports and many torsion-assisted cross-slot automorphisms become admissible.

Example cross-slot torsion automorphism with identity free block:

`(n1,a1;n2,a2) -> (n1,a1; n2,a2+n1)`.

It is invertible and nontrivially transfers hidden torsion information between slots, but

`(e,0) -> (e,tau)`.

Any marked scalar depending only on whether the free coordinate is zero has output scalars `(1,0)`, so it is not a genuine balanced split.

`ABLATION_M5 = DEGENERATE_TORSION_ASSISTED_MIXING_REENTERS`.

## A4. Remove M6 exact marked scalar conservation

Define an accepted-orbit-invariant nonnegative assignment on free coefficients by

- `q_bad(0)=0`,
- `q_bad(±1)=1`,
- `q_bad(±2)=q_bad(±3)=1/2`,
- `q_bad(±4)=7`,
- all other nonzero free magnitudes assigned `1`,

and ignore torsion wherever M2 requires it.

The elementary split of the canonical `M` still looks balanced:

`q_bad(2e)+q_bad(3e)=1`.

But on `(2e,0)`,

`M(2e,0)=(4e,6e)`

and

`q_bad(4e)+q_bad(6e)=7+1=8 != 1/2`.

Thus orbit labels alone do not propagate elementary balance into a conserved scalar geometry.

`ABLATION_M6 = MASSIVE_UNDERDETERMINATION`.

## A5. Remove M7 composition/refinement consistency

For the canonical witness there is no change: M3 already gives a global automorphism, so powers, inverse cancellation, and direct-sum pair embeddings are exact.

M7 becomes load-bearing only against partial one-shot rules that are not defined as one global additive bijection or against an attempt to identify different overlapping pair-operation sequences without preserving their operation order.

`ABLATION_M7 = REDUNDANT_FOR_CANONICAL_GLOBAL_AUTOMORPHISM; PROTECTIVE_FOR_PARTIAL_LAWS`.

## A6. Remove M8 sign-dark and relative non-sign compatibility

No change in current-carrier existence. Any automorphism of the unchanged carrier keeps `tau` nonzero and preserves exact signed additive structure as structure.

M8 matters if one later proposes an extension/quotient that would identify or destroy the accepted discriminator. Since F3 does not require an extension, it does not select among current survivors.

`ABLATION_M8 = NON_LOAD_BEARING_FOR_CURRENT_CARRIER_EXISTENCE`.

## A7. Remove M9 fixed scalar / no hidden rescaling

Under the formal F3 definition, M6 already states conservation using one fixed `q`. Therefore M9 does not cut down the mathematical canonical family further.

Its independent role is semantic/governance: it forbids reinterpreting the scalar unit after each reversible presentation change and then calling the result conserved.

`ABLATION_M9 = FORMALLY_REDUNDANT_WITH_FIXED_Q_M6; SEMANTIC_GUARD`.

## A8. Remove strict positivity on the split outputs

Under the strong derived balance condition

`q(a)=q(b)`

and normalization/conservation

`q(a)+q(b)=q(e)=1`,

strict positivity of the two split outputs is automatic:

`q(a)=q(b)=1/2`.

So this particular clause is redundant once branch-exchange equality is adopted.

However **global** strict positivity is not implied. For every `delta>=0` in the canonical exact family,

`q_delta(6e)=0`

although `6e != 0`.

`ABLATION_SPLIT_POSITIVITY = REDUNDANT_AFTER_EQUAL_BALANCE; GLOBAL_POSITIVITY_NOT_FORCED`.

## A9. Remove minimal-extension requirement

No effect on the present verdict because no extension is needed. The current carrier itself already contains a valid family.

Without minimality, arbitrarily large supercarriers could of course be adjoined, but they add no necessity evidence.

`ABLATION_MINIMAL_EXTENSION = NON_LOAD_BEARING_AFTER_CURRENT_CARRIER_SURVIVES`.

## A10. Counterfactual: arbitrary orbit label, no conservation requirement

The `q_bad` model in A4 is the explicit countermodel.

It satisfies zero normalization, elementary normalization, accepted absolute transport invariance, and can be assigned equal positive values to the two elementary split outputs, but it fails exact conservation immediately away from the elementary test state.

Therefore M6 adds a genuine infinite-domain functional constraint. It is the condition that propagates local balance to all generated marked states.

## A11. Balance-source ablation map

The logical dependence found in F3 is:

`M4 class-level marker covariance`

`+ M5 no branch preference`

`+ M1/M2 scalar presentation invariance`

`=> q(a)=q(b)` for the elementary split.

Then

`q(a)=q(b)`

`+ M6 exact conservation`

`+ q(e)=1`

`=> q(a)=q(b)=1/2`.

This is why no numerical half-split was assumed in advance; the half value is derived after equality and conservation.

## A12. Deterministic evidence

All exact finite claims used above are checked by

`scripts/cbrc_f3_validate_balanced_mixing_forward.py`

with deterministic digest

`aa2b1736c163362b9dbd179d09e85183ab5a46c335db316f46754c95ec37d3a8`.

`ABLATION_PACKET_COMPLETE = true`.
