# Navier–Stokes minority-helicity L3 critical criterion

Date: 2026-09-06
Projects: enterprise-math
Status: RESEARCH_FRONTIER / EXACT_COMMUTATOR_DERIVATION + CONDITIONAL_REGULARITY_CRITERION / NOT_MILLENNIUM_PROOF
Parent: `knowledge/projects/enterprise-math/pde-critical-helicity-double-null-20260906.md`.
Read snapshot before write: GLOBAL_KNOWLEDGE `main@e220c5bd83b0282184c69b2037e0e73a6b169087`.

## 1. Upgrade from Hdot^(1/2) minority size to L3 minority size

Use the parent notation

`u=v+w`, `v=P_+u`, `w=P_-u`,

and

`T(a,b,c)=integral (a·grad b)·Lambda c dx`.

Assume `w` is the smaller helical sector for the final symmetric estimate. Pure terms vanish:

`T(v,v,v)=T(w,w,w)=0`.

The six mixed terms are handled as follows.

### One-w terms

`T(v,v,w)+T(v,w,v)=<w,[Lambda,v·grad]v>`.

By the Calderón order-one commutator estimate and Holder,

`|...| <= C ||w||_3 ||grad v||_3^2`.

Also

`|T(w,v,v)| <= ||w||_3 ||grad v||_3 ||Lambda v||_3`.

### Two-w terms

Two terms already have `w` in the advecting slot:

`|T(w,w,v)| <= ||w||_3 ||grad w||_3 ||Lambda v||_3`,

`|T(w,v,w)| <= ||w||_3 ||grad v||_3 ||Lambda w||_3`.

For the remaining transport term use the exact full-order commutator identity

`boxed: T(v,w,w)=(1/2)<[Lambda,v·grad]w,w>`.

Indeed

`<Lambda(v·grad w),w>=T(v,w,w)`

while, by incompressibility of `v`,

`<v·grad Lambda w,w>=-T(v,w,w)`.

Therefore the same Calderón estimate yields

`|T(v,w,w)| <= C ||w||_3 ||grad v||_3 ||grad w||_3`.

The last mixed term is covered by the preceding list after expansion symmetry.

Since in 3D

`||grad f||_3 + ||Lambda f||_3 <= C ||f||_{Hdot^(3/2)}`

for smooth mean-zero periodic or sufficiently decaying fields, all six terms give

`boxed: |T(u,u,u)| <= C_L3 ||w||_3 ||u||_{Hdot^(3/2)}^2`.

Interchanging the two helicity sectors gives the symmetric form

`boxed: |T(u,u,u)| <= C_L3 min(||u^+||_3,||u^-||_3) ||u||_{Hdot^(3/2)}^2`.

This is scale critical: `L3` is invariant under the 3D Navier–Stokes scaling.

## 2. Conditional regularity and blow-up necessary condition

For the unforced system

`(1/2)d/dt ||u||_{Hdot^(1/2)}^2 + nu ||u||_{Hdot^(3/2)}^2 = -T(u,u,u)`.

Hence

`(1/2)A' + [nu-C_L3 m_3(t)] B <= 0`,

where

`m_3(t)=min(||u^+(t)||_3,||u^-(t)||_3)`.

If for some terminal interval `[t0,T)`

`sup_{t in [t0,T)} m_3(t) < nu/C_L3`,

then the critical Hdot^(1/2) norm stays bounded and the Hdot^(3/2) dissipation is time-integrable. Standard Fujita–Kato continuation excludes a singularity at `T`.

Therefore any finite-time singularity must satisfy the necessary mixed-helicity concentration condition

`limsup_{t->T} min(||u^+(t)||_3,||u^-(t)||_3) >= c_3 nu`

for the universal `c_3=1/C_L3` (up to the chosen normalization of the projectors and torus).

Interpretation: a single helical sector may be arbitrarily large without directly forcing critical growth; a breakdown requires both sectors to carry nontrivial critical `L3` mass near the singular time.

This criterion is stronger than the parent `Hdot^(1/2)` minority criterion because `Hdot^(1/2)` controls `L3`, not conversely.

## 3. Exact paired-source identity remains live

With

`X_+ = -<B(u,u),Lambda u^+>`,
`X_- = -<B(u,u),Lambda u^->`,

nonlinear helicity conservation gives

`X_+=X_-`.

Thus the total critical source is paired transfer into the two helicity sectors. The `L3` criterion says this paired source is perturbative whenever either one of the two critical spatial sectors remains below a universal viscous threshold.

BRC consequence: the signed helicity alone is not an adequate observer. One must retain the two helical branches (and, for Fourier null estimates, their shell/triad provenance) until cancellation has been justified.

## 4. Four-plane / six-axis dissipation form

Using the current FCC/STAR tight-frame identities from the parent Enterprise-coordinate route,

`||u||_{Hdot^(3/2)}^2 = (1/2) sum_{i=1}^6 ||Lambda^(1/2) D_i u||_2^2`

and equivalently

`= (3/8) sum_{T in {A,B,C,D}} ||Lambda^(1/2) grad_{P_T} u||_2^2`.

Therefore the upgraded estimate can be written as

`|T(u,u,u)| <= C_L3 m_3(t) * (3/8) sum_T ||Lambda^(1/2) grad_{P_T}u||_2^2`.

At carrier strength this is the clean critical statement matching the user's 3-versus-6 intuition:

- each 120-degree triad contributes a planar dissipative channel;
- the four overlapping triads / six unique FCC axes supply the complete isotropic critical dissipation;
- mixed-helicity critical growth can be absorbed by that complete six-axis dissipation whenever one helical sector is small in L3.

This is not an unconditional bound because the full equation may generate the minority sector above the threshold.

## 5. Next unresolved unit

The remaining hard task is to control generation of the minority `L3` sector itself. The parent double-null analysis shows that pure-helicity self-interaction generates the opposite sector only through a radial/shell commutator; on an equal-shell homochiral FCC state this source vanishes exactly (Beltrami baseline). A full proof would need to show that shell deformation, four-STAR overlap and viscosity prevent the minority sector from crossing the critical threshold, or replace the uniform-threshold hypothesis by a globally controlled aggregate estimate.

No such propagation theorem is proved here.
