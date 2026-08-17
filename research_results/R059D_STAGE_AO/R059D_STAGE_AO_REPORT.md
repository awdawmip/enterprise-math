# R059D Stage AO — Macroscopic BRC Density Profile and Limiting Measure Separation

Researcher-ID: `EM-R059D-AO-2D7C46`

Task: `RS-R059D-STAGE-AO-MACROSCOPIC-BRC-DENSITY-PROFILE-LIMIT`

Owner branch: `research/r059d-stage-ao-macroscopic-brc-density-profile-limit`

Frozen source: `454b57e4eab1c2d856074e653f5cb7db8c423e74`

Taskbook source: `3839dcfe0e6cfe819ec49fb6ffc9d3cdaa937a7f`

## Primary disposition

`FULL_MACROSCOPIC_BRC_DENSITY_PROFILE_PROVED__NONCONSTANT_RADON_NIKODYM_LIMIT__POSITIVE_LIMITING_VARIANCE`

## 1. Full macroscopic turn-density profile

The AL canonical first-sector frontier satisfies uniformly

`Q_E(a,b)=r^2+O(r)`.

In the source compatibility chart this gives

`a/r -> A(theta)=cos(theta)-sin(theta)/sqrt(3)`,

`b/r -> B(theta)=2sin(theta)/sqrt(3)`.

AK turn combinatorics gives exact cumulative identities:

- left half: turn index `n=b`;
- right half: turn index `n=M_N(r)-a`.

Therefore `N_r(theta)/r` converges uniformly to

`G(theta)=2sin(theta)/sqrt(3)` on `0<=theta<=pi_source/6`,

and

`G(theta)=beta-cos(theta)+sin(theta)/sqrt(3)` on `pi_source/6<=theta<=pi_source/3`,

where `3beta^2=4`, `beta>0`.

The piecewise density is

`g(theta)=2cos(theta)/sqrt(3)` on the left half,

`g(theta)=sin(theta)+cos(theta)/sqrt(3)` on the right half,

with D6-periodic/reflection continuation.

Its full mass is

`integral_full g dtheta=2*kappa_E`,

matching `T_r/r -> 2*kappa_E`.

## 2. Weak separation of target counting and source pushforward measures

On the common AM angular carrier,

`hat_nu_r=(1/T_r)sum_k delta_(theta_(r,k))`

converges weakly to

`d hat_nu_infty=[g(theta)/(2*kappa_E)]dtheta`.

The normalized source-arc pushforward measure converges to

`d hat_mu_infty=[1/(2*kappa_perp)]dtheta`.

Hence the limiting measures are mutually absolutely continuous but distinct, with

`d hat_mu_infty/d hat_nu_infty=kappa_E/[kappa_perp*g(theta)]`.

The derivative is nonconstant because `g(0)=2/sqrt(3)` while `g(pi_source/6)=1`.

This is a comparison theorem only. `kappa_perp` remains source typed and is not identified with `kappa_E`.

## 3. Generic individual-edge weights have a two-scale limit

The taskbook's possible pointwise formula `w_infty=1/g` is correct only as a local block average, not as the limit of every individual edge.

Exact symbol-conditioned limits are

`ell_1=(sqrt(3)cos(theta)-sin(theta))/2`,

`ell_2=(sqrt(3)cos(theta)+sin(theta))/2`,

`ell_3=sin(theta)`.

Local symbol densities are:

Left half:

`h_1=cos(theta)/sqrt(3)-sin(theta)`,

`h_2=sin(theta)+cos(theta)/sqrt(3)`.

Right half:

`h_2=2cos(theta)/sqrt(3)`,

`h_3=sin(theta)-cos(theta)/sqrt(3)`.

The correct local Young law is therefore

`Y_theta=(h_1/g)delta_(ell_1)+(h_2/g)delta_(ell_2)` on the left,

and

`Y_theta=(h_2/g)delta_(ell_2)+(h_3/g)delta_(ell_3)` on the right.

Its conditional mean is exactly

`integral w dY_theta=1/g(theta)`.

Thus the AN axis and center limits are recovered as the extrema of the macro block-average profile:

`w_macro(axis)=sqrt(3)/2`,

`w_macro(bisector)=1`.

## 4. Positive limiting variance

Let

`m_infty=kappa_perp/kappa_E`.

For the macro block-average profile,

`E_[hat_nu](w_macro^2)=(3/4)log(3)`.

Therefore

`Var_macro=(3/4)log(3)-m_infty^2>0`.

This confirms the taskbook candidate exactly at the macro-profile level.

For actual individual edges, the persistent Young microstructure increases the second moment. The exact limit is

`lim_r (1/T_r)sum_k w_(r,k)^2=5/6`.

Therefore

`Var_edge=5/6-m_infty^2>0`.

The difference

`Var_edge-Var_macro=5/6-(3/4)log(3)>0`

is the integrated conditional Young-measure variance.

No decimal evaluation of the standard source circle constant is used to establish positivity.

## 5. What AO resolves from AN

AN proved two distinguished persistent limits. AO proves they belong to the complete D6-periodic macro field:

- native turn density `g(theta)`;
- source/target limiting measure separation;
- macro weight `1/g(theta)`;
- symbol-level Young law around that macro mean;
- positive limiting macro and edge-level variances.

Thus the BRC distortion is not merely persistent at two special locations; it has a full nonconstant continuum density profile.

## 6. Semantic boundaries

Frozen:

- target canonicality remains AL and is not reopened;
- target circumference remains minimal turn count;
- source angle/trig/arc measure/log are compatibility-side only;
- AM fibers remain relational, not a bijection;
- `kappa_perp != kappa_E` is not asserted as a separate source theorem; they remain distinctly typed;
- no new theorem about standard real `pi` is claimed;
- generic individual-edge pointwise convergence is not claimed because the correct object is the proved Young law.

## 7. Deterministic validation

Frozen checker source:

`research_results/R059D_STAGE_AO/r059d_stage_ao_deterministic_checker.py`

Independent execution before history freeze:

- checks: `30763/30763 PASS`;
- digest: `187b3ae44600cf74bd0d48aedcf8bd84045f5a4aea5b21b61e96492be8015fa4`;
- radii: all `1..2048` plus checkpoints `4096,8192,16384`;
- exact shell, cumulative, support and reflection checks;
- profile CDF checks;
- weak target Fourier moments `cos(6theta)->1/35`, `cos(12theta)->-1/143`;
- normalized source `cos(6theta)->0`;
- edge second moment `->5/6`;
- macro second moment `->(3/4)log(3)`;
- local symbol-bin density checks;
- D6/reflection symmetry;
- target runtime/source-selection firewall.

Finite replay is implementation validation only. The theorem is the symbolic scaled-frontier/cumulative-density/Young-measure proof.

## Stop

Freeze for Driver review after history isolation, checker-output, manifest, and final checkpoint publication. No AP or later stage is consumed.
