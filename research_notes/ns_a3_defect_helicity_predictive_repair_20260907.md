# Navier–Stokes A3 defect is not dynamically closed: helicity/polarization repair

Status: `RESEARCH_NOTE / DURABLE_FRONTIER / EXACT_NO-GO + EXACT_SINGLE-SHELL_REPAIR / NOT_PROMOTED / NOT_MILLENNIUM_PROOF`
Researcher-ID: `EM-FREE-7N3K2A`
At: `2026-09-07T15:55:00+08:00`
Parents:
- `research_notes/ns_a3_cubic_defect_multiplier_frontier_20260907.md`
- `research_notes/ns_a3_cubic_defect_symbol_audit_20260907.md`
- global frontier `knowledge/projects/enterprise-math/pde-critical-helicity-double-null-20260906.md`
Authority immediately before write: `enterprise-math main@196bb8f85a8883952a3138c01f38adfdbde76219`.

## 0. Question

Can the four A3 cubic defect multipliers by themselves form a dynamically closed small quantity under the full Navier–Stokes equation?

Answer: no. Exact root-ray support is a nonlinear null set for instantaneous enstrophy production, but it is not invariant under the unprojected quadratic dynamics. A further polarization/helicity observable is genuinely necessary.

This is an operation-safe quotient/BRC issue, not merely an analytic-estimate issue.

## 1. Explicit zero-defect data with nonzero first defect forcing

Work on the periodic lattice and take the two primitive A3 roots

`p=(1,1,0)`, `q=(1,-1,0)`,

so `p·q=0` and `k=p+q=(2,0,0)` is an axis-defect output.

Choose divergence-free unit polarizations

`a=(0,0,1)` at `p`,

`b=(1,1,0)/sqrt(2)` at `q`.

Indeed `a·p=0` and `b·q=0`. Add the conjugate coefficients at `-p,-q` to obtain a real smooth field.

Both input frequencies lie exactly on A3/FCC root lines, so all four cubic defect multipliers annihilate the initial field:

`T_j u_0=0` for `j=0,x,y,z`.

At the output `k=(2,0,0)`, the Leray-projected quadratic coefficient is

`P_k[(a·q)b+(b·p)a]`.

Here

`a·q=0`, `b·p=sqrt(2)`,

and `a` is already orthogonal to `k`, hence the coefficient equals

`sqrt(2) a != 0`

(up to the conventional Fourier factor `i`).

For the cubic defect frame,

`mu_x(k)=1`, `mu_0(k)=mu_y(k)=mu_z(k)=0`.

Therefore

`T_x P[(u_0·grad)u_0]` has a nonzero Fourier coefficient at `k` of magnitude `sqrt(2)` in this unit-amplitude normalization.

So an exact zero-defect A3 state can immediately generate off-A3 defect under the full equation.

## 2. No-go for multiplicative defect closure

Any proposed estimate of the schematic form

`|| T P[(u·grad)u] ||_X <= C * Def_A3(u) * Phi(u)`

with `Def_A3(u)=0` on the exact root-ray skeleton is false for any norm `X` that detects the explicit output above, unless `Phi` is allowed to be singular/infinite on this smooth datum.

Likewise, one cannot prove an autonomous Gronwall inequality

`d E_D/dt <= C(u) E_D`

that is supposed to preserve `E_D=0` for the full unprojected NS dynamics. The decimated A3 model is invariant only because the off-skeleton quadratic output is projected away.

This separates two exact statements that must not be conflated:

`A3 ROOT SKELETON -> ZERO INSTANTANEOUS ENSTROPHY PRODUCTION`

but

`A3 ROOT SKELETON -/-> INVARIANT MANIFOLD OF FULL NS`.

## 3. Quadratic escape of defect energy

Let

`z_j=T_j u`,

`E_D=(1/2) sum_j ||z_j||_2^2`.

For root-ray-supported initial data, `z_j(0)=0`. The exact defect transport equation gives

`z_j'(0) = - T_j P[(u_0·grad)u_0]`.

Therefore

`E_D(0)=0`, `E_D'(0)=0`,

and exactly

`E_D''(0) = sum_j ||T_j P[(u_0·grad)u_0]||_2^2`.

The explicit two-root datum in Section 1 makes this quantity strictly positive. Thus the full flow leaves the zero-defect manifold quadratically in defect energy (linearly in defect amplitude).

## 4. Exact single-shell helicity repair

Now assume `u` is supported on one Fourier sphere `|xi|=K`, and decompose it into helical sectors

`u=v+w`,

`curl v=K v`, `curl w=-K w`.

Using

`(u·grad)u = grad(|u|^2/2) - u x curl u`,

and

`curl u=K(v-w)`,

one obtains exactly

`P[(u·grad)u] = 2K P(v x w)`.

Indeed the pure `v-v` and `w-w` contributions are gradients/zero after Leray projection. Hence same-shell nonlinear forcing is exactly bilinear in the two opposite-helicity sectors.

For initial data that is simultaneously

1. supported on a single A3/FCC root shell, and
2. annihilated by all four cubic defect multipliers,

we therefore have

`z_j'(0) = -2K T_j P(v x w)`

and

`E_D''(0)=4K^2 sum_j ||T_j P(v x w)||_2^2`.

Consequences:

- if `w=0` or `v=0`, the field is Beltrami and the full quadratic forcing vanishes identically;
- mixed helicity is necessary for same-shell A3 defect leakage;
- mixed helicity is not sufficient for positive leakage because phases/polarizations can still cancel, but the explicit witness in Section 1 shows positive leakage occurs.

This recovers the global shell-coherence/Beltrami frontier in a new form: helicity is not merely a regularity diagnostic; it is an operation-safety repair variable for the A3 geometric defect observer.

## 5. Observer-completeness witness

Consider two smooth single-shell A3 states with the same geometric observation

`Def_A3=0`.

- A homochiral state has `P[(u·grad)u]=0` and therefore zero defect forcing.
- The explicit state of Section 1 has nonzero defect forcing.

Hence the quotient that retains only A3 geometric defect is not predictive for even the first nonlinear future step.

At minimum a dynamics-safe branch state must retain

`(A3 root-line label, radial shell, helicity/polarization, complex amplitude/phase)`.

Helicity sign alone is enough to certify the pure Beltrami null sector on one shell, but not enough to reconstruct arbitrary mixed-sector leakage amplitudes; phase/polarization information remains relevant.

BRC resolution:

- geometric defect alone -> `INSUFFICIENT_OBSERVER_FOR_DYNAMICS`;
- add helical branch identity and phase/amplitude -> `COMPOSE_APPLIED`;
- compressing to positive total defect before the nonlinear step -> operation-unsafe.

## 6. Multi-shell boundary

The single-shell identity does not say that homochiral root-ray data on several radii is leakage-free. If `v` contains modes with different `|xi|`, then `curl v=Lambda v` but not `curl v=K v` for a common scalar `K`; pure-helicity interactions can then be nonzero. The earlier shell-difference/Waleffe factors show that radial mismatch becomes the second forcing coordinate.

Thus the repaired nonlinear state has a double-null structure:

`A3 DEFECT FORCING REQUIRES`

`(HELICITY MIXING) OR (SHELL INEQUALITY)`

with additional A3 pair geometry controlling whether the generated output is itself defective.

For a STAR pair, the output cubic defect already contains an exact radial factor `(m-n)`; in a homochiral Waleffe branch the interaction coefficient contains another `(m-n)` factor. Therefore the homochiral near-equal-shell STAR leakage has a **quadratic radial mismatch zero** at the symbol level. This is stronger than the single shell-difference null alone.

## 7. Next executable unit

The next useful object is a branch-resolved forcing functional, not `Def_A3` alone. For root-ray inputs `p=m alpha`, `q=n beta`, retain

`(alpha,beta,m,n,s_p,s_q,complex amplitudes)`

until after applying both factors:

1. output A3 defect `mu_j(p+q)`;
2. helical interaction factor `s_p|p|-s_q|q|` and geometric polarization coefficient.

The immediate finite task is to classify the complete primitive-shell mixed-helicity pair orbits (`dot=0` axis and `dot=+1` 211 outputs) and determine whether summing the signed four-channel forcing over the tetrahedral/A3 incidence network yields any cancellation for arbitrary admissible amplitudes. If an explicit amplitude choice defeats every proposed orbit cancellation, record a no-go and move to a quantitative minority-helicity forcing estimate instead.
