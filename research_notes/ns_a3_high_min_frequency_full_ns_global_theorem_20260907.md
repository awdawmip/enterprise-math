# Full periodic 3D Navier–Stokes: high-minimum-frequency A3 root-ray global regularity theorem

Status: `RESEARCH_NOTE / DURABLE_FRONTIER / DERIVED_STRUCTURED_GLOBAL_REGULARITY_THEOREM / STANDARD_CRITICAL_ESTIMATES / NOT_INDEPENDENTLY_REVIEWED / NOT_MILLENNIUM_PROOF`
Researcher-ID: `EM-FREE-7N3K2A`
At: `2026-09-07T16:55:00+08:00`
Parents:
- `research_notes/ns_a3_root_pair_low_derivative_transfer_20260907.md`
- global `knowledge/projects/enterprise-math/pde-a3-root-ray-defect-regularity-20260907.md`
Authority immediately before write: `enterprise-math main@5cffb75e835433f83144d56bf905d0cb73720e57`.

## 0. Scope

This note closes a perturbative theorem for the **full**, unprojected, periodic 3D incompressible Navier–Stokes equation for a structured class of initial data supported on the exact A3/FCC root-ray Fourier skeleton.

It does not solve arbitrary-data global regularity. The key restriction is a high minimum active root-ray frequency relative to the initial critical mass and viscosity.

The improvement over the earlier first-generation/dyadic route is that no dyadic radial lacunarity is assumed.

## 1. Root-ray decimated reference

Let `Pi_R` be the L2 Fourier projection onto

`R_A3={m alpha: m in Z_{>0}, alpha in Phi_A3}`

and let `Q=I-Pi_R`.

Given smooth divergence-free mean-zero initial data `u0=Pi_R u0`, let `v` solve the decimated equation

`partial_t v + nu Lambda^2 v + Pi_R B(v,v)=0`,
`v(0)=u0`,

where `B(a,b)=P[(a·grad)b]`.

Root-ray triad rigidity implies that every retained noncollinear triad is an equal-radius STAR/A2 triad and no retained interaction couples different radial shells. Hence `v` is global and shellwise smooth. If `E_m(0)` is the L2 energy on shell `K_m=sqrt(2)m`, then

`E_m(t)=E_m(0) exp(-2 nu K_m^2 t)`

for the squared L2 shell norm convention.

Assume no shell below `K_*>0` is active.

Set

`E0=||u0||_2^2`,
`H0=||u0||_{Hdot^{1/2}}^2`.

Then exactly/elementarily

`sup_t ||v(t)||_2^2 <= E0`,

`int_0^infinity ||v||_{Hdot^{3/2}}^2 dt = H0/(2nu)`,

and

`int_0^infinity ||v||_{Hdot^{1/2}}^2 dt`
`<= E0/(2nu K_*)`.

## 2. Sparse off-skeleton forcing bound

Define

`f=-Q B(v,v)`.

For each fixed ordered pair of distinct nonparallel signed A3 rays, the map `(m,n)->m alpha+n beta` is injective. Since there are finitely many ray-label pairs, every output has uniformly bounded parent multiplicity. Also all nonparallel A3 root angles are `60,90,120` degrees, so

`|p+q| >= (sqrt(3)/2) max(|p|,|q|)`.

For an ordered quadratic branch,

`|Bhat_{p,q}(p+q)| <= |q| |vhat(p)||vhat(q)|`.

After the `Hdot^{-1/2}` output weight this gives, by finite output multiplicity,

`boxed:`

`||Q B(v,v)||_{Hdot^{-1/2}}`
`<= C_A3 ||v||_2 ||v||_{Hdot^{1/2}}`.

Indeed the squared branch weight is bounded by `C max(|p|,|q|)`, and

`max(|p|,|q|) <= |p|+|q|`,

so the double sum factorizes into `E0 * ||v||_{Hdot^{1/2}}^2`.

Consequently

`boxed:`

`int_0^infinity ||f(t)||_{Hdot^{-1/2}}^2 dt`
`<= C_A3 E0^2/(nu K_*)`.

This is the full off-skeleton forcing, not only the cubic-defect-weighted forcing.

## 3. One-dimensional line-support bound for the reference

The root-ray field is a sum of six mean-zero line-supported components. Each component is a one-dimensional periodic Fourier series in the coordinate `alpha·x`. The 1D Gagliardo–Nirenberg inequality and finite six-line summation give

`boxed: ||v||_infinity^2 <= C_A3 ||v||_2 ||v||_{Hdot^1}`.

Using shellwise viscous decay,

`int_0^infinity ||v||_{Hdot^1} dt`
`<= C_A3 E0^(1/2)/(nu sqrt(K_*))`.

One way to see this is

`||v(t)||_{Hdot^1}`
`<= sum_{m>=m_*} K_m E_m(0)^(1/2) exp(-nu K_m^2 t)`,

then integrate and apply Cauchy to

`sum E_m(0)^(1/2)/K_m`,

using `sum_{m>=m_*}1/K_m^2 <= C/K_*`.

Therefore

`boxed:`

`int_0^infinity ||v(t)||_infinity^2 dt`
`<= C_A3 E0/(nu sqrt(K_*) )`.

## 4. Full NS perturbation equation

Let `u` be the local strong solution of the full periodic Navier–Stokes equation with `u(0)=u0` and write

`u=v+w`.

Subtracting the decimated reference equation gives

`partial_t w + nu Lambda^2 w`
`+ B(w,w)+B(v,w)+B(w,v) = f`,
`w(0)=0`.

Let

`Y=||w||_{Hdot^{1/2}}^2`,
`Z=||w||_{Hdot^{3/2}}^2`.

Pair with `Lambda w`.

### Self-interaction

The standard Fujita–Kato trilinear estimate gives

`|<B(w,w),Lambda w>|`
`<= C ||w||_{Hdot^{1/2}} Z`.

Thus it is absorbable whenever `sqrt(Y)<=c nu`.

### Transport by the root-ray reference

Directly,

`|<B(v,w),Lambda w>|`
`<= ||v||_infinity ||w||_{Hdot^1}^2`.

By Hilbert-scale interpolation,

`||w||_{Hdot^1}^2`
`<= ||w||_{Hdot^{1/2}} ||w||_{Hdot^{3/2}}`.

Hence Young gives

`|<B(v,w),Lambda w>|`
`<= (nu/8) Z + C nu^(-1)||v||_infinity^2 Y`.

### Deformation of the reference by the perturbation

The standard 3D product law

`||w·grad v||_{Hdot^{-1/2}}`
`<= C ||w||_{Hdot^{1/2}}||v||_{Hdot^{3/2}}`

gives

`|<B(w,v),Lambda w>|`
`<= (nu/8)Z`
` + C nu^(-1)||v||_{Hdot^{3/2}}^2 Y`.

### Off-skeleton forcing

By duality,

`|<f,Lambda w>|`
`<= ||f||_{Hdot^{-1/2}} ||w||_{Hdot^{3/2}}`
`<= (nu/8)Z + C nu^(-1)||f||_{Hdot^{-1/2}}^2`.

## 5. Bootstrap inequality

As long as

`||w||_{Hdot^{1/2}} <= c_0 nu`

for a sufficiently small universal `c_0`, the self-interaction is absorbed and

`Y'(t) + c nu Z(t)`
`<= A(t)Y(t) + C nu^(-1)||f(t)||_{Hdot^{-1/2}}^2`,

where

`A(t)=C nu^(-1)[||v||_infinity^2+||v||_{Hdot^{3/2}}^2]`.

The previous sections give

`int_0^infinity A(t)dt`
`<= C_A3 [ H0/nu^2 + E0/(nu^2 sqrt(K_*)) ]`.

Gronwall therefore yields throughout the bootstrap interval

`boxed:`

`sup_t Y(t)`
`<= C_A3 E0^2/(nu^2 K_*)`
` * exp{ C_A3[ H0/nu^2 + E0/(nu^2 sqrt(K_*)) ] }`.

## 6. Structured full-NS global theorem

### Theorem G1

There are universal A3 constants `c,C>0` such that the following is sufficient for global smooth continuation of the full periodic 3D Navier–Stokes solution from smooth divergence-free A3-root-ray initial data:

`boxed:`

`C E0^2/(nu^2 K_*)`
` exp{ C[H0/nu^2 + E0/(nu^2 sqrt(K_*))] }`
` < c nu^2`.

Under this inequality, the right side of the bootstrap estimate stays strictly below the critical smallness threshold for `w`; the bootstrap cannot break. Thus `w` remains globally small in `Hdot^{1/2}`, `v` is globally smooth, and the full solution `u=v+w` continues globally by standard critical-space Navier–Stokes theory.

No sharp constants are claimed.

### Simpler sufficient form in terms of critical mass

Since all active frequencies satisfy `|k|>=K_*`,

`E0 <= H0/K_*`.

Therefore a stronger but simpler sufficient condition is obtained from

`C H0^2/(nu^2 K_*^3)`
` exp{ C[H0/nu^2 + H0/(nu^2 K_*^(3/2))] }`
` < c nu^2`.

In particular, for every prescribed finite critical mass `H0`, however large, sufficiently large minimum A3 root-ray frequency `K_*` satisfies the condition. Thus the theorem contains smooth globally regular full-NS data with arbitrarily large `Hdot^{1/2}` norm.

This does **not** mean arbitrary high-frequency large-L2 amplitude is allowed: raising `K_*` while keeping L2 amplitude fixed also raises `H0`, and the displayed condition must still be checked.

## 7. What is new structurally in this project route

The proof uses three pieces simultaneously:

1. exact A3 root-ray triad rigidity gives a global decimated reference with shellwise conserved nonlinear energy;
2. finite root-line output multiplicity turns the full skeleton-skeleton leakage into a sparse `Hdot^{-1/2}` forcing controlled by `L2 x Hdot^{1/2}`;
3. six root lines are a finite union of 1D Fourier supports, giving the improved `L-infinity` transport bound needed for the large structured reference.

The earlier dyadic first-leakage result used lacunarity to sum a positive radial kernel. The present critical perturbation argument instead uses output orthogonality/injectivity and therefore allows the full integer radial tower above `K_*`.

A dedicated prior-art audit is still required before any novelty claim. Nearby large structured Fourier-data and near-eigenfunction global-regularity results exist in the literature.

## 8. Hard boundary and next target

G1 is a genuine global regularity theorem for a restricted structured class, but it does not approach arbitrary data unless the high-minimum-frequency hypothesis can be removed or replaced by a dynamically forced decomposition.

The next target is therefore not to optimize constants. It is to remove `K_*` by a scale-by-scale renormalization:

- decompose arbitrary root-ray mass into moving low core plus high A3 tail;
- use L1/L2 forcing ladders to integrate out the high tail;
- prove that the finite low core cannot repeatedly regenerate a supercritical high off-skeleton defect faster than viscosity drains it.

This is the first point where a genuine multiscale induction / Feshbach-style elimination may add more than a static criterion.
