# OpenAI NS comparison, audit 2: singular-axis germ, annular residual carrier, and critical-norm lower bound

Record-ID: FINDING-EM-NS-OPENAI-AXIS-GERM-20260909-D5C00D
Progress-Event-ID: NS-OPENAI-AXIS-GERM-LERAY-20260909-D5C00D-02
Status: TESTING / SOURCE_FORENSIC / ORDINARY_PROOF / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-D5C00D
Research-Activity-ID: RA-D5C00DF7D77F4AA2ACE0
Session: local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0 (locally assigned, not a platform-authenticated identifier).
P000 unchanged. No theorem acceptance, Working Truth promotion, formal task claim, or independent validation of the OpenAI construction is asserted.

## 1. Frozen inputs and correction of audit-1 architecture

Own parent frontier:
- `research_notes/ns-openai-forcing-audit-20260909-d5c00d.md`.
- There we proved the forced heat-Gram continuation implication
  `integral Gamma_NL < infinity => continuation`, with
  `Gamma_NL=(I_NL)_+/(F_*+J+nu^2 K/4)`,
  for smooth compactly supported forcing.
- Consequently any correct singular candidate of that force class must have
  `integral Gamma_NL = infinity`.

OpenAI source is kept frozen at
`openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538`.
This audit does not switch to a newer source while deriving consequences.

The main correction to the previous verbal comparison is structural:

> The OpenAI correction cascade does not create the singularity. The singular
> axis behavior is already built into `FinalSlowBase.velocity`. Positive
> potential/direct corrections are annular and vanish as germs at the
> singular axis; the diagonal construction preserves the base germ. The
> carrier/cycle machinery repairs the residual while leaving the planted
> singular core unchanged.

Calling the actual annular carrier a "blowup carrier" conflates two different
branches. In this note it is called the **residual-repair carrier**.

## 2. Exact singular base

Let `h=ActualPrimary.h`. `BaseWitnessClosure.actual_axis_parameters` proves

`0 < h <= 1/1000`

and the selected axial seed `j=ActualPrimary.nominal.axis.j` is positive.

`CoordinateAlgebra` uses

`A(h)=1/2+h`, `D(h)=1/2-h`, so `A+D=1`.

`FinalSlowBase.leading_origin` identifies the zeroth axial coefficient at the
origin with the same positive `j`, and `FinalSlowBase.origin` gives the exact
axis formula

`u_base(t,0) = ((1-t)^(-A(h))*j) e_3`,  `t<1`.

Thus the endpoint speed blowup is already present before any positive correction
cycle is diagonalized.

The base residual is also explicit:

`NSResidual(u_base,p_base)=stressForce+error`.

`FinalSlowBase.error_allJetsFlat` makes the remaining `error` all-jets-flat at
the physical endpoint in the specified approach regions. At the same time,
`FinalSlowBase.normalizedStress_zero_left` makes the normalized leading stress
exactly zero for normalized radius

`X <= activeLeft`.

Since `BaseWitnessClosure.actual_annulus_order` gives `activeLeft>0`, the
singular axis `X=0` sits strictly inside a stress-free inner gap.

This is the first key separation:

`singular core`  !=  `annular residual-repair carrier`.

## 3. Positive correction stages preserve the core germ

`ActualPolarCoverage.active` is the inverse image of the closed annulus

`X in [activeLeft,activeRight]`.

The axis has `X=0`, hence is outside this set by a positive normalized gap.

The source proves more than pointwise vanishing:

- `MixedAxisPreservation.mixedDiagonal_eq_base_germ`:
  on the zeroth-cutoff plateau, the full mixed velocity is eventually equal on
  a neighborhood to the curl of the base.
- `mixedDiagonal_axis_jets`:
  every spacetime jet at the axis equals the corresponding base jet.
- `origin_eventually_base_germ`:
  for all sufficiently late `t<1`, the final prelocalized mixed velocity has
  the base germ near `(t,0)`.
- `ActualCandidateAssembly.particular_zero_germs` and
  `signed_zero_germs` give zero germs for the particular and signed corrections
  outside the active annulus.
- `positivePotential_axisZeroOn` packages the same statement for every positive
  velocity correction.

The pressure side has the analogous exterior structure at finite prefixes.
`ActualExteriorPrefix.ExteriorStages` states:

- potential stage zero equals the actual slow-base potential on the open
  exterior and all positive potential stages vanish there;
- every direct stage vanishes there;
- pressure stage zero equals `FinalSlowBase.pressure` there and every positive
  pressure stage vanishes there.

Its `prefix_germs` theorem therefore gives simultaneous velocity and pressure
base germs for every finite prefix on the open exterior. The final pressure
diagonal is locally finite under the selected schedule, so the same exterior
localization argument applies to the infinite pressure sum. I did not locate a
separately named Lean theorem whose title is literally "final pressure equals
base pressure germ"; the statement here is an ordinary deduction from the
generic local-finiteness mechanism plus `ExteriorStages`, not a claim about an
unread named theorem.

## 4. Spatial and time localization do not erase a shrinking inner cell

`SpatialLocalization` uses a fixed cutoff that equals one on the open plateau

`radialSquare(x)<1/32`, `|x_2|<1/8`.

On this plateau the periodized velocity and pressure are locally equal to the
unlocalized fields, including all jets. `TimeLocalization.activatedVelocity_eq_late`
is exactly the identity for `t>=3/4`.

Therefore any physical cell whose diameter tends to zero at the endpoint is
eventually entirely inside the spatial plateau and is unaffected by the time
switch.

## 5. A source-derived critical L3/Hdot(1/2) lower bound

This section is an ordinary proof from the frozen source identities. It has not
been added as a Lean theorem.

### 5.1 A fixed normalized cell

`BaseChartJets.bandPoint` is exactly

`t = 1-Q*T`,
`r = sqrt(Q)*R`,
`z = Q^D*Z`.

Moreover `bandPoint_chart` says that the physical chart is the scaled normalized
chart, and `axial_eq_normalized_velocity` says

`axial(Q,p) = Q^A * u_base,3(bandPoint(h,Q,p))`.

At `p0=(R0,(0,1))` with `R0>0` small, direct substitution gives normalized
coordinates `(rho,X,eta)=(1,R0^2/2,0)`. Since the zeroth axial coefficient is
continuous and equals the positive `j` at `(X,eta)=(0,0)`, choose `R0`, then a
fixed compact rectangle

`R in [R1,R2]`, `Z in [-Z0,Z0]`, `T=1`

such that throughout it:

- `0 < X < activeLeft`,
- `rho` stays in a fixed compact subinterval of `(0,infinity)`,
- the leading normalized axial field
  `rho^(-A) * d_axial,0(X,eta)` is bounded below by a constant `c0>0`.

`SlowBorelBase.normalized_correction_bound`, applied at jet order zero to the
actual axial coefficient sequence, gives uniform convergence of the true summed
normalized axial field to this leading field at rate `O(Q^(2h))` on the fixed
compact cell. Hence for all sufficiently small `Q`,

`|u_base,3(1-Q,x_Q)| >= c * Q^(-A)`

throughout the corresponding physical cell.

Because the cell has `X<activeLeft`, it lies in the open exterior of the active
correction annulus. `ActualExteriorPrefix` and the selected diagonal local
finiteness therefore identify the full prelocalized velocity with the slow base
there for small `Q`. Since the cell shrinks to the origin, spatial localization
is eventually the identity on it; since `1-Q>=3/4`, time localization is also
the identity.

Thus the same lower bound holds for the final localized candidate velocity on
this whole physical cell, conditional only on the frozen source theorem chain.

### 5.2 Physical volume and critical norm

At fixed `t=1-Q`, cylindrical coordinates give

`x_Q(R,theta,Z) = (sqrt(Q) R cos(theta), sqrt(Q) R sin(theta), Q^D Z)`,

hence

`dx = Q^(1+D) R dR dtheta dZ`.

The fixed normalized cell therefore has volume comparable to `Q^(1+D)`. On it
`|u| >= c Q^(-A)`. Consequently

`||u(t)||_L3^3 >= c1 * Q^(1+D-3A)`.

Using `A=1/2+h` and `D=1/2-h`,

`1+D-3A = -4h`.

Therefore

`||u(t)||_L3 >= c2 * Q^(-4h/3)`.

For the compactly supported whole-space candidate, the homogeneous Sobolev
embedding `Hdot^(1/2)(R3) -> L3(R3)` yields

`K(t)=||u(t)||_(Hdot^1/2)^2 >= c3 * Q^(-8h/3)`,  `Q=1-t`.       (A2.1)

This is a slow but genuine critical-norm divergence because `h>0`.
The same cell has L2-energy scale

`Q^(1+D-2A)=Q^(1/2-3h)`,

which tends to zero for the actual `h<=1/1000`. This explains how a vanishing
amount of local L2 energy can coexist with an unbounded critical norm and
pointwise speed.

Equivalently, the cell's scale-critical Lebesgue exponent is

`p_c=(1+D)/A=(3-2h)/(1+2h)<3`.

The construction is only slightly beyond the `L3`-critical balance, but the
strict inequality is enough to force the power `Q^(-4h/3)`.

## 6. Quantitative consequence for our heat-Gram injection gate

Audit 1 proved, with `G=F_*+J+nu^2 K/4`,

`d/dt log G <= Gamma_NL + b(t)`

in the integrated sense, where

`Gamma_NL=(I_NL)_+/G`

and `b` is integrable for the smooth compact force.

From (A2.1),

`G(t) >= c4 * (1-t)^(-8h/3)`.

Hence every correct realization of the frozen OpenAI candidate must satisfy

`integral_[t0,t] Gamma_NL(s) ds
 >= (8h/3)*log(1/(1-t)) - C`.                         (A2.2)

In particular, not only does `integral Gamma_NL` diverge; its cumulative
logarithmic divergence has a source-derived positive coefficient. A standard
contradiction argument also gives

`limsup_(t->1-) (1-t)*Gamma_NL(t) >= 8h/3`.            (A2.3)

No claim is made that the limit exists or that every late time has this rate.

Since `0<h<=1/1000`, the coefficient is small but strictly positive.

## 7. BRC-safe decomposition of the unresolved nonlinear injection

The new localization fact does NOT let us delete the off-axis corrections from
`I_NL`. Both the Leray projection and the heat semigroup in the heat-Gram
functional are nonlocal.

Write the final velocity before the harmless late localization as

`u=b+w`,

where `b` is the slow base branch and `w` is the sum of initialization and
positive correction branches. In the inner exterior cell, `w` and all local
derivatives vanish, but globally they do not.

For the rotational bilinear map

`M(a,c)=P(a cross curl(c))`,

retain ordered provenance:

`N(u)=M_bb+M_bw+M_wb+M_ww`.

Inside a zero-germ region the raw cross and correction terms vanish, but after
Leray projection their gradient-pressure tails can be nonzero because the
source lives outside the region. The induced scalar potential is harmonic in
the gap. Therefore "off-axis support" does not mean "absent from the critical
injection at the axis".

For the heat-Gram branch, define the symmetric bilinear kernel

`B_s(v,z)(tau) =
 -1/2 Lambda^(-1/2) [
   S_tau v_s cross Lambda S_tau z_s
   + S_tau z_s cross Lambda S_tau v_s ]`.

Then

`Phi_s(u)=B_s(u,u)`,
`J(u)=sum_s ||Phi_s(u)||^2`,
`DJ(u)[h]=4 Re sum_s <B_s(u,u), B_s(u,h)>`.

The exact provenance expansion has:

- 3 symmetric Gram sectors in `B(u,u)`:
  `bb`, `2bw`, `ww`;
- 8 ordered sectors in `B(u,N(u))`:
  `b/w` times `M_bb,M_bw,M_wb,M_ww`.

Thus there are 24 ordered provenance pairings before cancellation.
If the two cross orientations `M_bw+M_wb` are grouped only by correction degree,
this reduces to 18 degree-grouped pairings. The ordered 24-term ledger is the
BRC-safe object; the 18-term version is a later compression.

Also note the degree: `J` is quartic, `DJ` is cubic in the base point and linear
in the direction, and `N` is quadratic, so `I_NL=DJ(u)[N(u)]` is quintic in
velocity amplitude, not sextic.

The immediate target is now precise:

> locate which ordered provenance/shell/cycle sectors produce the
> `~1/(1-t)` normalized positive exposure forced by (A2.2)-(A2.3), while
> preserving complex phase and Leray/heat nonlocality.

## 8. Consequences for comparison with our route

1. The OpenAI construction does not directly refute the finite isolated-triad
   viscous gain bound. Its blowup is not assembled by repeatedly amplifying one
   closed triad. A singular anisotropic base is planted first, and the infinite
   network is used to legalize/repair its residual.

2. The word `carrier` was previously overloaded. The actual active annulus is
   a residual-repair carrier separated from the singular core by a normalized
   radial gap. Any comparison with our carrier language must keep those branches
   distinct.

3. The route-wide obstruction has moved from "can a local carrier blow up?" to
   "can the full unforced Fourier network pay the logarithmically divergent
   normalized quintic injection budget without an external source and while
   preserving all nonlocal pressure/heat couplings?"

4. The OpenAI formal consequences also prove its force is genuinely nonzero at
   some spacetime point before `t=1`; this is not accidentally an unforced
   solution. At the same time, audit 1 shows the direct smooth force is not the
   nonintegrable coefficient in our positive-metric inequality.

## 9. Status and next executable unit

Established in this audit:
- exact source-forensic role separation between singular base and annular
  correction carrier;
- finite-prefix velocity/pressure base-germ preservation on the open exterior;
- ordinary proof of the critical `L3` and `Hdot^1/2` lower bounds (A2.1);
- quantitative normalized-injection obligations (A2.2)-(A2.3);
- exact BRC-safe 24 ordered / 18 degree-grouped provenance decomposition.

Not established:
- independent correctness of the full OpenAI proof;
- a Lean formalization of the new `L3/Hdot^1/2` lower-bound lemma;
- a branchwise evaluation of the actual OpenAI `I_NL`;
- a proof that one specific provenance branch is individually positive or
  divergent;
- a universal unforced bound on `Gamma_NL`.

Next:
construct the 24-term injection ledger with shell/cycle labels and use the
OpenAI exterior/base identities to test whether the `bb` branch alone can carry
the required logarithmic exposure, or whether nonlocal `bw/wb/ww` branches are
essential. Do not collapse Leray or heat-semigroup provenance before this test.

REUSE_APPLIED: exact heat-Gram metric from audit 1; OpenAI axis-germ and exterior
prefix theorems; BRC typed provenance.
COMPOSE_APPLIED: source scaling cell + Sobolev critical norm + prior forced
Gronwall gate.
