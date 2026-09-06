# Navier–Stokes critical helicity double-null and FCC shell-coherence frontier

Date: 2026-09-06
Projects: enterprise-math
Status: RESEARCH_FRONTIER / EXACT_CLASSICAL_IDENTITIES + CONDITIONAL_REGULARITY_CRITERION / NOT_MILLENNIUM_PROOF
Parent frontiers:
- `knowledge/projects/enterprise-math/pde-six-axis-tetrahedral-fourier-triad-frontier-20260906.md`
- `knowledge/projects/enterprise-math/pde-tetrahedral-edge-face-shell-deformation-nullform-20260906.md`
Read snapshot before write: GLOBAL_KNOWLEDGE `main@82c11529edb17db6852c749a808c1e873c5033a8`; enterprise-math current read in this phase `main@f2b6a751b82b1bc71389be1527da0f88dbf39117`.

## 1. Critical helical masses

Let `Lambda=(-Delta)^(1/2)` and use the standard divergence-free helical projectors

`P_+ = (I + Lambda^(-1) curl)/2`,
`P_- = (I - Lambda^(-1) curl)/2`.

Write

`u=v+w`, `v=P_+u`, `w=P_-u`.

Define positive critical masses and dissipation

`A_+ = ||Lambda^(1/2)v||_2^2`,
`A_- = ||Lambda^(1/2)w||_2^2`,
`A=A_++A_-=||u||_{Hdot^(1/2)}^2`,
`B=||Lambda^(3/2)u||_2^2`.

The signed helicity is

`H=<u,curl u>=A_+-A_-`.

Hence the exact helicity-purity defect is

`delta_H := A-|H| = 2 min(A_+,A_-)`.

This is a BRC observer-preservation point: `H` alone discards two positive branch masses that may be simultaneously large. The pair `(A_+,A_-)` is the adequate carrier for the present critical-growth question.

## 2. Pure-helicity critical cubic term is exactly zero

For the trilinear form

`T(a,b,c)=integral (a·grad b)·Lambda c dx`,

a positive helical field satisfies `curl v=Lambda v`, and a negative helical field satisfies `curl w=-Lambda w`.

Using `(a·grad)a=grad(|a|^2/2)-a x curl a` and integration of a gradient against a curl,

`T(v,v,v)=0`,
`T(w,w,w)=0`.

Thus the nonlinear derivative of the critical norm contains only mixed-helicity terms. This is the physical-space form of the helical branch fact that the critical `Hdot^(1/2)` weight equals the sign-definite helicity weight on a homochiral sector.

## 3. Minority-helicity commutator estimate

Assume without loss of generality that `w` is the smaller critical sector. Expanding `T(u,u,u)` leaves six mixed terms. Two exact reorganizations are

`T(v,v,w)+T(v,w,v) = < w, [Lambda, v·grad] v >`,

and

`T(v,w,w) = < [Lambda^(1/2), v·grad] w, Lambda^(1/2)w >`,

because the corresponding transported `L2` term vanishes for divergence-free `v`.

The other three mixed terms have `w` directly in the advecting slot.

Using the 3D critical Sobolev embedding `Hdot^(1/2) -> L^3`, together with standard Calderón/Kato–Ponce commutator estimates, gives a universal constant `C_*` such that for smooth periodic or sufficiently decaying divergence-free fields

`|T(u,u,u)| <= C_* ||w||_{Hdot^(1/2)} ||u||_{Hdot^(3/2)}^2`.

By symmetry between the two helical sectors,

`boxed: |T(u,u,u)| <= C_* sqrt(min(A_+,A_-)) B`

or equivalently, after absorbing `sqrt(2)` into the constant,

`boxed: |T(u,u,u)| <= C_H sqrt(delta_H) B`.

This is a scale-critical estimate. It is stronger than the usual bound with the full `sqrt(A)` in the coefficient whenever the flow is close to a sign-definite helical sector.

## 4. Conditional regularity / necessary blow-up mixing threshold

The unforced Navier–Stokes critical energy identity is

`(1/2) dA/dt + nu B = -T(u,u,u)`.

Therefore

`(1/2)dA/dt + [nu-C_* sqrt(min(A_+,A_-))] B <= 0`.

Consequently, if on a time interval `[t0,T)`

`sup_t min(A_+(t),A_-(t)) < (nu/C_*)^2`,

then `A` is bounded and `integral B dt` is finite on that interval. By the standard Fujita–Kato continuation mechanism this excludes a singularity at `T`.

Equivalently, any finite-time breakdown would necessarily satisfy the critical helicity-mixing condition

`limsup_{t->T} min(A_+(t),A_-(t)) >= c_* nu^2`

for a universal `c_*>0` determined by the commutator constant.

In purity-defect form, a blow-up requires `delta_H` to reach a universal viscous critical threshold. This is a conditional/necessary criterion, not a proof that the threshold cannot be reached.

## 5. Equal nonlinear creation of the two critical helical masses

Project the equation onto the two helical sectors. Let

`X_+ = -<B(u,u),Lambda u^+>`,
`X_- = -<B(u,u),Lambda u^->`.

Nonlinear helicity conservation implies

`X_+=X_-=:X`.

Thus

`(1/2)dA_+/dt + nu B_+ = X`,
`(1/2)dA_-/dt + nu B_- = X`,

while

`(1/2)dA/dt + nu(B_++B_-)=2X`.

Hence nonlinear growth of the unsigned critical mass is literally paired creation/transfer of positive and negative helical critical mass. Signed helicity alone can hide this because it observes the difference rather than the two positive branches.

## 6. A second exact null structure: shell commutator

For every divergence-free `u`, energy conservation gives

`< (u·grad)u, u>=0`.

Self-adjointness of `Lambda` and integration by parts give the exact identity

`boxed: T(u,u,u) = (1/2)< [Lambda,u·grad]u, u >`.

Thus critical growth is also a radial/shell commutator. If all active Fourier modes lie on one sphere `|k|=K`, then `Lambda u=K u` and the critical nonlinear term is zero, regardless of helicity.

Combining Sections 2 and 6:

`CRITICAL_GROWTH_REQUIRES_HELICITY_MIXING AND SHELL_INEQUALITY`.

This is the current double-null principle.

## 7. Per-triad observer-rank determinant

For one helical Fourier triad with side lengths `(a,b,c)` and helicity signs `(s_a,s_b,s_c)`, let the three branch observers be

`e=(1,1,1)`  (energy weight),
`h=(s_a a,s_b b,s_c c)`  (helicity weight),
`kappa=(a,b,c)`  (critical Hdot^(1/2) weight).

The elementary transfer direction is proportional to

`e x h = (s_c c-s_b b, s_a a-s_c c, s_b b-s_a a)`.

Therefore the critical source factor is, up to orientation sign,

`Psi = -det[[1,1,1],[s_a a,s_b b,s_c c],[a,b,c]]`.

Equivalently, if `d_tau` is the Euclidean distance of `kappa` from `span{e,h}`, then

`|critical triad production| = d_tau ||T_tau||`.

This is the exact BRC observer-factorization test for a three-mode branch: the critical observer cannot change when it lies in the span of the two locally conserved observers.

Two major rank-drop loci are immediate:

1. homochiral triad: `h=+/-kappa`, so `Psi=0`;
2. equal-shell triad: `kappa=K e`, so `Psi=0`.

For a nonzero equal-shell zero-sum wavevector triad, the geometry is exactly 120 degrees. Thus the P000-selected 120-degree primitive carrier closure appears in the classical Fourier equation as one of the exact observer-rank null loci.

For the four relative helicity classes (global sign ignored), exact factorization is

`+++ : Psi=0`,
`-++ : Psi=2 a(b-c)`,
`+-+ : Psi=-2 b(a-c)`,
`++- : Psi=2 c(a-b)`.

This also proves that a single generic local mixed-helicity non-equilateral triad has no further exact quadratic-invariant obstruction: on that interior shape class the three observer rows are independent. Any full proof must therefore exploit multi-triad aggregation, viscosity, or an additional geometric/dynamical constraint; single-triad conservation alone cannot close the Millennium problem.

## 8. Sharpened Waleffe critical branch bound

For ordered triangle sides `0<a<=b<=c<=a+b`, let `g` be Waleffe's scale-invariant helical geometric coefficient. Combining the exact `Psi` factors with Heron/triangle inequalities gives, for every heterochiral branch,

`|g Psi| <= 2 a c`,

and also

`|g Psi| <= 3 c(c-a)`.

Hence

`boxed: |gPsi|/c^2 <= min(2a/c, 3(1-a/c)) <= 6/5`.

So the critical source is depleted at both ends:

- strongly nonlocal triads `a/c -> 0`;
- equal-shell/equilateral 120-degree triads `a/c -> 1`.

Only local-in-scale, non-equilateral, heterochiral interior shapes retain order-one critical strength. This is now the smallest unresolved Fourier class.

## 9. Minimal FCC shell: local triad closure becomes global six-line Beltrami coherence

On the periodic integer Fourier lattice, the first shell admitting a nonzero equal-shell zero-sum triad is `|k|^2=2`, exactly the 12 FCC rays / six unoriented line families. Modulo conjugation the equal-shell triads are exactly the four current STAR triad types.

For a real field, a primitive complex triad `{k,p,q}` requires the six signed modes `{+/-k,+/-p,+/-q}`. This is a real-field completion, not a new force-arity axiom.

Assign one helical sign to each of the six FCC line families (with the usual real curl-eigenfield conjugation convention). For any equal-magnitude input pair the Waleffe coefficient contains

`s_p |p|-s_q |q|`.

Therefore same-helicity equal-length inputs have zero nonlinear coefficient, whereas opposite-helicity equal-length inputs generically permit off-shell output.

Requiring every one of the four overlapping STAR triads to be structurally leakage-free under its real signed completion forces every face to be homochiral. Because the four faces overlap in a connected six-line incidence system, this forces all six line-family helicity labels to have the same sign.

The resulting full shell-2 field satisfies

`curl u = +/-sqrt(2) u`.

Thus it is a Beltrami field and

`P[(u·grad)u]=0`.

Its unforced Navier–Stokes evolution is exactly linear viscous decay for arbitrary amplitude.

The six-line helicity-label frustration has an exact finite gap. For signs `h_e in {+/-1}` define

`Q_h = sum_{co-STAR adjacent e<f} (h_e-h_f)^2`.

Across all 64 sign assignments the values occur as

`Q_h=0` for 2 assignments,
`Q_h=16` for 12 assignments,
`Q_h=24` for 32 assignments,
`Q_h=32` for 18 assignments.

Hence `Q_h=0` iff all six signs agree; every mixed line-label pattern has a nonzero combinatorial leakage/frustration gap. Amplitude-weighted impurity remains continuous, so this finite sign gap is not by itself a PDE coercivity estimate.

This is the cleanest current resolution of the user's 3-versus-6 intuition at spectral-carrier strength:

- `3` = primitive local 120-degree complex triadic closure;
- `6 signed modes` = minimal real completion of one primitive spectral triad;
- `6 FCC line families + 4 overlapping triads` = full minimal-shell carrier atlas;
- global leakage-free coherence of that full shell forces a single helicity sign and yields an exact Beltrami/linear NS solution.

None of these replaces P000's primitive stable force arity 3.

## 10. Current unresolved target

The current obstruction has been narrowed to

`LOCAL_IN_SCALE + MIXED_HELICITY + NON_EQUILATERAL/NOT_120_DEGREE + MULTI_TRIAD NETWORK`.

The next potentially decisive question is whether the mixed-helicity critical source admits a scale-local aggregate estimate stronger than the single-triad bound, using the tetrahedral edge/face incidence constraints and cancellation between neighboring triads before absolute values are taken.

A target strong enough for full regularity would be an estimate of the form

`|T(u,u,u)| <= theta nu B + R(t)`

with `theta<1` and `R` globally time-integrable from energy/helicity/native admissible data, without assuming the helicity-purity threshold in Section 4.

No such unconditional bound is established here.

## 11. Verification / external comparison

Exact symbolic checks in this phase verified the `Psi` determinant/factorizations and the 64 FCC line-helicity frustration counts. The commutator proof uses standard Kato–Ponce/Calderón estimates and the critical embedding `Hdot^(1/2)->L^3`.

External comparison:
- Biferale–Titi (2013) proves global regularity for the helical-decimated sign-definite model because helicity becomes a positive `H^(1/2)`-equivalent invariant; this supports the critical role of the sign-definite boundary but does not prove regularity of full NS.
- The full Navier–Stokes Millennium problem remains officially unsolved as of 2026-09-06.
