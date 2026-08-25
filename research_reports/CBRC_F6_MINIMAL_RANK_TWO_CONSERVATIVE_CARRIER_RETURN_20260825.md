# CBRC F6 — Minimal Rank-Two Conservative Carrier Classification Return

Researcher-ID: `EM-CBRCF6-D694C8`

Task-ID: `RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Taskbook source: `e5d3c761e291b3193ccbbd85a4a2b05c70338141`

Blind mathematical source: `research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`

Owner branch: `research/cbrc-f6-minimal-rank-two-conservative-carrier`

Status: `CHECKPOINT_A_DRAFT`

Primary verdict: `PENDING_UNARY_CLASSIFICATION`

## Epistemic boundary

This return uses only the F6 blind packet as mathematical input before raw freeze. No historical F1 torsion-free counterfactual, R063/R064/R065/FQ, downstream coherent-wave material, external quantum mechanics, named rank-two number system, ring/field/multiplication, norm/inner-product/quadratic law, splitter matrix, or known downstream rank-two answer was used.

## Q1 — additive carrier normal form

Let `C` be a finitely generated abelian group of torsion-free rank exactly `2`, with embedded

`j(C1) = Z e ⊕ <tau | 3 tau = 0>`,

and an additive retraction

`pi:C -> Z e`

satisfying `pi(e)=e`, `pi(tau)=0`.

Because `pi` is a retraction, the short exact sequence

`0 -> ker(pi) -> C -> Z e -> 0`

splits canonically through the given copy of `Z e`. Hence

`C = Z e ⊕ K`, where `K=ker(pi)`.

The group `K` has torsion-free rank `1`, so by the structure theorem for finitely generated abelian groups

`K ≅ Z f ⊕ T`

for a finite abelian group `T`. The embedded `tau` lies in `T` and has exact order `3`. Therefore every allowed carrier has typed normal form

`C ≅ Z e ⊕ Z f ⊕ T`, `tau in T`, `ord(tau)=3`, `pi(e)=e`, `pi(f)=0`, `pi(T)=0`.

Conversely every such pointed finite group `(T,tau)` produces an allowed carrier. Two such carriers are isomorphic preserving `j` and `pi` exactly iff their pointed finite torsion groups `(T,tau)` are isomorphic.

Equivalently, the nonminimal classification reduces exactly to the finite pointed torsion datum `(T,tau)`. In the `3`-primary component the marked order-three element has a well-defined `3`-height; a full retract to the upstream torsion exists precisely at height zero (proved below).

### Primitive old generator

The explicit primitivity assumption is redundant once `pi` is present: if `e=d x` in the free quotient with `|d|>1`, applying the integer-valued coefficient of the retraction gives `1=d*pi_coeff(x)`, impossible. Thus the old signed retraction itself forces primitivity.

### Minimal torsion

The embedded nonzero `tau` forces at least one `Z/3` torsion summand in the pointed sense. No additional torsion is forced: take

`T=<tau> ≅ Z/3`.

This realizes every upstream additive relation and leaves torsion-free rank exactly `2`. Since the F6 order minimizes additional torsion before any unary tie-breaker, every carrier with larger finite torsion is strictly worse than this model.

Thus the unique least typed additive carrier is

`C_min = Z e ⊕ Z f ⊕ <tau | 3 tau = 0>`

with `pi(e)=e`, `pi(f)=0`, `pi(tau)=0`.

This establishes:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`.

### Complement / gauge freedom

For `C_min`, after normalizing `f in ker(pi)`, every typed automorphism fixing the embedded upstream layer pointwise and preserving `pi` is

`g_{eps,a}(e)=e`, `g_{eps,a}(tau)=tau`, `g_{eps,a}(f)=eps f + a tau`,

where `eps in {+1,-1}` and `a in Z/3`.

Hence complement orientation and torsion shift are presentation freedom. The typed gauge group has six elements; it is the semidirect product `(Z/3) ⋊ {±1}` with inversion action.

## Q2 — conservative-extension notions

Three notions must be separated.

### (E) Embedding-only

Require only the embedded upstream `C1` with primitive old free generator. The rank-two additive carrier still has an abstract normal form `Z e ⊕ Z f ⊕ T` with marked order-three `tau`; an old signed retraction exists because the primitive free generator can be completed to a free basis, but it is not yet typed/canonical data.

### (P) Old-signed-retraction

Type a specific `pi:C->Z e` extending `pi1`. This selects the rank-one kernel `K=ker(pi)` and allows the canonical normalization `f in ker(pi)`. It does not force any additional torsion. The least carrier remains `C_min`.

### (R) Full upstream retract

A bare additive `r:C->C1` with `r j=id_C1` exists iff there is a homomorphism `phi:T->Z/3` with `phi(tau)=1`. This is equivalent to

`tau notin 3T`.

Necessity: every homomorphism to `Z/3` kills `3T`.

Sufficiency: if the class of `tau` in the `F3`-vector space `T/3T` is nonzero, extend it to a linear functional taking `tau` to `1`, then compose with `T->T/3T`.

Thus a marked `tau` buried as `3g` inside `Z/9` is an embedding-only / old-projection example with no full upstream retract, whereas the minimal `T=<tau>≅Z/3` automatically admits one.

On `C_min`, a bare retract is determined by

`r(f)=m e + b tau`, with `m in Z`, `b in Z/3`.

If one additionally requires compatibility with the already typed old projection,

`pi1 r = pi`,

then necessarily `m=0`, leaving exactly three presentation choices `r(f)=b tau`. Those three choices are related by allowed torsion shifts of the complement and do not create a new carrier isomorphism class. By contrast, if a non-projection-compatible bare retract is itself frozen as typed structure, the integer `|m|` is genuine extra retract data up to complement orientation.

Therefore F6 does not need to impose a full retract: the least carrier is unchanged whether one asks only for the embedding, for the old signed retraction, or additionally for existence of a projection-compatible full upstream retract. Choosing a particular retract would add avoidable structure.

This establishes:

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`.

## Checkpoint A conclusion

Additive normal form and conservativity have stabilized. The least carrier is already forced at the additive level:

`C_min = Z^2 ⊕ Z/3` with the typed upstream `e,tau` and old projection, without assigning any familiar rank-two number-system name.

Remaining F6 work after this checkpoint:

1. classify all inherited unary `R/J/S` lifts on `C_min`;
2. quotient them by the six-element typed complement gauge;
3. apply the F6 unary minimality tie-breaker;
4. complete ablations and depth-4 exact checker;
5. freeze source/target-leak audit, manifest, digests, and final verdict.
