# X6 internal/channel V3: triadic-state-induced C3 channel circulation

Status: `FREE_RESEARCH / EXACT CONDITIONAL CLASSIFICATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-CELL-CHANNEL-INTERNAL-STATE`
Depends on:
- `X6_CELL_TRIADIC_PORT_FRAME_INTERNAL_STATE_V1_20260906.md`;
- `X6_AXIS_CHANNEL_FRAME_GAUGE_AND_FLAT_TRANSPORT_V2_20260906.md`;
- current triadic C6/C12 internal dynamics.

## 1. Question

V2 proved that bare pure spatial translation cannot generate a nontrivial deterministic channel permutation if the rule is translation-invariant and fully `S6`-equivariant: the transport is forced to identity.

The next question is whether the already-existing triadic internal state supplies enough symmetry breaking to permit a nontrivial local channel law without inventing a new spatial coordinate or external field.

It does.

## 2. Reference ordered triad and residual symmetry

Fix a global axis-channel gauge frame so channel labels and native axis labels can be compared.

Take a reference **ordered underlying-axis triad**

`tau_0=(1,2,3)`.

For this note the channel permutation rule is sign-blind: the signs of the three force ports remain separate internal provenance and do not change which unsigned channels participate.

The subgroup of `S6` fixing the ordered triad pointwise is

`H = Sym({4,5,6}) ~= S3`.

It permutes only the complementary inactive axes.

An `S6`-equivariant deterministic local channel rule

`tau -> U_tau in S6`

must satisfy

`U_{g tau}=g U_tau g^{-1}`.

At `tau_0`, every `h in H` fixes `tau_0`, so equivariance forces

`U_tau0 = h U_tau0 h^{-1}`.

Thus `U_tau0` lies in the centralizer `C_{S6}(H)`.

## 3. Centralizer theorem: the active triad is exactly the allowed nontrivial channel block

**Theorem.**

`C_{S6}(H) = Sym({1,2,3})`,

with every element fixing `{4,5,6}` pointwise.

### Proof

The common fixed-point set of `H` is exactly `{1,2,3}`. If `u` commutes with `H`, then for every active label `a` and every `h in H`,

`h u(a)=u h(a)=u(a)`.

Hence `u(a)` is fixed by every `h` and therefore lies in `{1,2,3}`. So `u` preserves the active and inactive blocks.

On the inactive block, `u` must commute with the full natural `S3` action. The centralizer of `S3` inside its own symmetric group is its center, which is trivial. Hence `u` fixes the inactive block pointwise.

On the active block there is no further restriction, so any `S3` permutation is allowed. QED.

Therefore an ordered active triad changes the symmetry-forced channel law from

`identity only`

to

`one arbitrary S3 permutation inside the active three-channel block`.

No extra spatial dimension is required.

## 4. Classification of sign-blind S6-equivariant triad-conditioned channel laws

The orbit of ordered distinct-axis triads under `S6` is transitive. Hence every sign-blind `S6`-equivariant rule is determined uniquely by one element

`u in S3_active`.

There are exactly six such rules:

- identity;
- three transpositions;
- two 3-cycles.

For a general ordered triad `tau=(a,b,c)`, transport the chosen reference element by any `g` with `g tau_0=tau`. The centralizer theorem guarantees the result is independent of the choice of `g`.

## 5. Cyclic token-origin invariance reduces S3 to C3

An oriented triadic passage has no distinguished starting token: the ordered triples

`(a,b,c)`, `(b,c,a)`, `(c,a,b)`

represent the same cyclic ordering with a different token-origin convention.

Require the unsigned channel rule to be invariant under this cyclic reindexing:

`U_(a,b,c)=U_(b,c,a)=U_(c,a,b)`.

At the reference triad this means the chosen `u in S3` commutes with the cycle

`c=(1 2 3)`.

The centralizer of `C3=<c>` in `S3` is exactly `C3`.

Therefore the cyclic-origin-invariant rules are exactly

- identity;
- forward cycle `(1 2 3)`;
- reverse cycle `(1 3 2)`.

If the law is required to be nontrivial circulation, exactly two possibilities remain, related by reversal/chirality.

## 6. PF-10 passage cycle is precisely the nontrivial solution

For a full ordered signed triadic port frame

`tau=(d_0,d_1,d_2)`,

let `a_r` denote the underlying unsigned channel/axis label of `d_r`.

The V1 PF-10 instantaneous directed passage relation is

`a_0 -> a_1 -> a_2 -> a_0`.

This is exactly the forward `C3` channel rule from Section 5.

Reversing the triad order changes it to the inverse 3-cycle.

Thus the existing PF-10 directed passage is not an arbitrary decoration: among deterministic sign-blind, S6-equivariant, cyclic-token-origin-invariant nontrivial permutations, it is one of the only two possible laws.

## 7. The passage orientation is conserved along the internal R orbit

Recall the internal triadic update

`R(d_0,d_1,d_2)=(-d_1,-d_2,-d_0)`.

After forgetting signs, this is only the cyclic reindexing

`(a_0,a_1,a_2) -> (a_1,a_2,a_0)`.

Therefore

`U_{R tau}=U_tau`

for the cyclic-origin-invariant channel law.

So the unsigned directed passage 3-cycle is constant throughout the six-phase `R` orbit, even though the full ordered signed triad frame moves through six distinct states.

This explains exactly why the PF-10 directed passage readout is too coarse to recover the C6 internal phase: the channel circulation is a conserved quotient of that phase dynamics.

## 8. Exact quotient hierarchy revisited

For the 960 full ordered signed triad frames:

- active unsigned support: 20 values;
- directed unsigned `C3` passage: 40 values (`20 subsets * 2 chiralities`);
- full ordered signed frame: 960 values.

Each directed passage therefore has a 24-element fiber:

`3 cyclic token-origin phases * 8 sign patterns`.

The present theorem identifies the 40-state passage space as the exact nontrivial symmetry-allowed channel-circulation quotient of the full internal state.

## 9. Spatial transport and internal channel evolution now separate cleanly

Under the V2 full-symmetry theorem:

- pure spatial channel parallel transport is identity after a global gauge frame is chosen;
- active triadic internal state permits a nontrivial `C3` permutation inside its three active channels;
- the inactive three channels remain fixed by the local rule.

Thus nontrivial channel dynamics can be sourced by internal relation state while the bare spatial connection remains flat.

This is the smallest positive example of the V2 statement that nontrivial twisting requires extra internal/context data.

## 10. State-dependent channel holonomy

For a sequence of internal triadic events `tau_1,...,tau_m`, define the unsigned channel update

`U_path = U_tau_m ... U_tau_1`.

If all events use the same active triad and same passage chirality, then

`U_path = c^m`

inside that active `C3`. Hence the channel state has exact period three under repeated unsigned passage updates.

The physical/internal C6 and decorated C12 periods can therefore coexist with a coarser C3 channel-circulation period.

If active triads change between events, the products need not commute; genuine channel holonomy can then arise from the **internal-state history**, not from bare spatial translation.

The order/provenance of such events must be retained unless an operation-safe quotient is proved.

## 11. Sign dependence remains a separate open layer

This note classified sign-blind channel permutations. The eight sign patterns of one active triad are retained in the 24-fold PF-10 passage fiber.

A future channel law may depend on signed force orientation, amplitudes, or other internal variables. Such dependence can break the present quotient further and is not ruled out.

Therefore:

`UNSIGNED_C3_CHANNEL_CIRCULATION != COMPLETE_SIGNED_INTERNAL_STATE`.

## 12. Current channel frontier

Closed under the declared permutation model:

- bare spatial S6 symmetry forces flat identity channel transport;
- an ordered active triad enlarges the symmetry-allowed local channel update exactly to `S3_active`;
- cyclic token-origin invariance reduces this to `C3`;
- nontrivial deterministic circulation has exactly two chiral choices;
- the current PF-10 directed passage realizes precisely one such choice;
- passage orientation is invariant along the internal six-phase `R` orbit;
- nontrivial channel holonomy can be generated by changing internal triadic states rather than spatial translation.

Open:

1. signed/state-amplitude-dependent channel laws;
2. coupling between neighboring Cells carrying different active triads;
3. physical calibration of channel species/traffic;
4. whether channel holonomy has a direct observable/field interpretation.

No Foundation promotion is made.
