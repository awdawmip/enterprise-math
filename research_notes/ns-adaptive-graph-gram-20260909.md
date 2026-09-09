# 相位保真的图范数自适应因果求解与 A3 认证区域扩大

Record-ID: FINDING-EM-PDE-ADAPTIVE-GRAPH-GRAM-20260909
Status: TESTING / ORDINARY_PROOFS_AND_EXACT_FINITE_CHECKS / NOT_INDEPENDENTLY_REVIEWED
Researcher-ID: EM-DIRECT-F00A51
Research-Activity-ID: RA-076944AE1950A916ACC95399
Proposed event: NS-ADAPTIVE-GRAPH-GRAM-20260909-08 (NOT remotely registered by this run)
Date: 2026-09-09
Global read snapshot: 9a284373b128dfb6a03f49996bc22cf9e53e632b
EM read snapshot: 141f8e547192b6ae9448c614664cc5023eca3ecd
Locally assigned session key: local-ns-jitter-901c9f34161ce0f1; not a platform session ID.

## 0. Scope and recovery

Continue the explicit user-selected Navier--Stokes/BRC research. P000 remains unchanged; the normalized classical three-torus and FCC/A3 frequency carrier below do not construct or verify the complete native X6 dynamics. All solution claims concern smooth real divergence-free mean-zero periodic data and the stated viscosity. No arbitrary-data NS theorem or historical priority is claimed.

Remote recovery establishes that the preceding inexact-Newton work IS now represented by the seventh checkpoint. Its current source is `research_notes/ns-inexact-newton-error-ledger-20260909.md` at `8c39f2b5d6a0b792e657cc6365def90a46e84945`; manifest at `6cf0edabb2b1d5551ba30e8efc27044363d9ed1f`. That current record uses final error radius 19/1000000. The older uploaded local package uses another valid but different enclosure and is not silently substituted for that current checkpoint.

The current canonical coefficient backend `research_notes/ns-inexact-newton-error-ledger-20260909/exact_packets.py` was read through GitHub and copied byte-for-byte for execution. SHA256: `0ffab938427c4827700876fbd9f9c371a59d07aa89edefd5a6447071ec48d25d`; Git blob: `bfe8cea9975dae711f259ad76ff68c94e080c33f`.

Prior analytic dependencies: full all-mode inverse and trajectory product from `ns-causal-inverse-newton-basin-20260909.md`; the certified constant C*=9503/1000 from `brc-critical-lattice-gram-newton-20260909.md`; inexact-error recurrence from the current seventh checkpoint. The local copy of the earlier inexact checker supplies rational radical enclosures and the independently checked helical initial-data constructor. No acceptance depends on its older final-radius declaration.

Classical least squares, graph norms, Galerkin approximation and inexact Newton are established mathematics. This note composes them with the phase/rate-resolved exact carrier, the all-mode inverse and a concrete enlarged A3 certificate. It is not a new accepted top-level BRC toolbox family.

## 1. Known analytic interface

Write D0=partial_t+nu Lambda^2, B(f,g)=P((f.grad)g), N(f,g)=-B(f,g), Lambda=(-Delta)^(1/2). For a prescribed admissible reference v, let

D_v h=D0 h+B(v,h)+B(h,v), h(0)=0.

The parent gives a causal inverse G_v:Y->X, with

Y=L2(0,T;Hdot^-1/2),
||h||_X^2=sup_t [||h(t)||_Hdot^1/2^2+c int_0^t ||h||_Hdot^3/2^2], c=3nu/4,
||G_v||<=L, ||B(f,g)||_Y<=C_B||f||_X||g||_X,
C_B=C*/sqrt(2c).

T may be infinity under the parent's global reference hypotheses. The inverse is analytic and all-mode, not a finite matrix inverse. For the two numerical cases below, nu=1.

A reference with full residual f_v generates the linear correction problem D_v d=g=-f_v. If d is approximate and e=D_v d-g, then

||d-G_v g||_X<=L||e||_Y.                                            (1)

Thus the appropriate norm for choosing linear corrections is ||D_v d||_Y, not a coefficient count or the Euclidean length of a packet vector.

## 2. Graph-norm least squares with exact identities

Let psi_1,...,psi_m be causal trial trajectories with zero initial values. Set A_j=D_v psi_j and d_c=sum c_j psi_j, with real coefficients c_j to preserve real-field conjugacy. All A_j include their full Fourier outputs. Define

G_ij=Re<A_i,A_j>_Y, b_i=Re<A_i,g>_Y, R=||g||_Y^2.

Then exactly

||D_v d_c-g||_Y^2=R-2 b^T c+c^T G c.                              (2)

If the A_j are independent, G is positive definite. The minimizer solves G c=b and has residual squared R-b^T G^-1 b. Redundant directions are removed or treated by the Moore--Penrose inverse; no negative residual or rank conclusion is inferred from floating-point roundoff.

For nested trial spaces and exact minimizers d_m, the orthogonal-projection identity is

||e_m||_Y^2=||e_(m+1)||_Y^2+||D_v(d_(m+1)-d_m)||_Y^2.             (3)

So refining the trial space cannot increase its optimal full residual. This does not state that a raw heat/Picard coefficient choice is monotone; the minimization and the full-output metric are essential.

For one added direction A, remove its projection on the old image space: A_perp=(I-P_m)A. If A_perp!=0, the exact marginal reduction is

|<e_m,A_perp>|^2/||A_perp||^2.                                   (4)

This is a principled ranking score for candidate directions. The executed example below refines a fixed three-direction family and tests tolerances; it does NOT execute a search over every possible next branch.

### Certified coefficient precision

A high-precision numerical solve is only a proposal. For rational coefficients c_tilde and a verified lower bound lambda_*<=lambda_min(G),

0 <= E(c_tilde)-min E <= ||G c_tilde-b||^2/lambda_*.                (5)

This follows by writing the difference as (c_tilde-c_*)^T G(c_tilde-c_*). All actual acceptance tests in this package evaluate (2) with outward rational radical intervals; no unvalidated floating-point eigenvalue is used. Interval LDL also validates positive rank and (5).

## 3. Each fixed admissible linear problem admits finite certified refinement

The statement here is conditional on the known reference/inverse interface, NOT a theorem that every nonlinear outer reference stays admissible.

Let v and g have finite explicitly computable Fourier/time representations, v satisfy the parent bounds, and g in Y. For every epsilon>0 there exists a finite, zero-initial, real solenoidal trial d such that

||D_v d-g||_Y<epsilon.                                           (6)

A complete dictionary can use finite integer Fourier modes with rational solenoidal polarizations and continuous compactly supported piecewise-polynomial time coefficients with rational knots and coefficients. The separate three-direction heat family in Section 5 is NOT asserted complete.

Proof of density: h=G_vg exists in X. Since D0 h=g-B(v,h)-B(h,v) and the trajectory product bound applies, h_t belongs to L2 Hdot^-1/2. For T=infinity first set h_R=chi_R h, with chi_R=1 through R, chi_R=0 after 2R and |chi_R'|<=2/R. Then

D_v h_R-g=(chi_R-1)g+chi_R' h.

Both terms tend to zero in Y; use h in L2 Hdot^3/2, the torus spectral gap, and g in Y. The cutoff is continuous so it creates no distributional jump. On a compact time interval truncate Fourier modes; convergence holds in L2 Hdot^3/2 and H1 Hdot^-1/2, and in C Hdot^1/2 by the Hilbert-triple energy estimate. The product bound makes D_v continuous in this graph topology. Approximate the finitely many time coefficients in H1 by continuous rational piecewise polynomials, preserving zero initial and terminal trace, conjugacy and divergence. This yields (6).

For computable finite-packet inputs, the residual of each such trial has finite output support. Its finite-window integrals, plus the explicit source tail, can be enclosed to arbitrary precision. Enumerate a nested complete dictionary and rational coefficient proposals (or use least squares with a complete fallback), refining interval precision as needed. Some finite proposal has residual <epsilon/2; its strict acceptance test is eventually resolved. Thus this idealized adaptive inner algorithm terminates for each positive tolerance.

No uniform runtime, Fourier cutoff, bit complexity, greedy-selection completeness or outer all-data basin is proved. This separates FINITE TOLERANCE ATTAINABILITY for a fixed linear problem from a universal nonlinear NS solver.

## 4. Why BRC packet ordering matters

For fhat(k,t)=sum_j a_(k,j) t^m_j exp(-lambda_j t), retain output, rate, time degree, helical/polarization labels and complex amplitude before taking a norm. Then

||f||_Y^2=sum_(k!=0) |k|^-1 sum_(i,j) Re<a_(k,i),a_(k,j)>
             (m_i+m_j)!/(lambda_i+lambda_j)^(m_i+m_j+1).           (7)

Different output frequencies are orthogonal; different rates at the SAME output generally are not. For example

int_0^infinity (exp(-x t)-exp(-y t))^2 dt
=(x-y)^2/[2xy(x+y)], x,y>0.                                      (8)

Discarding the cross term destroys the near-rate cancellation. Using a positive norm bound after (7) is legitimate; replacing (7) by a diagonal mass sum is a different and potentially much worse observer.

A finite graph-norm approximation is a CONTROLLED-ERROR representation, not an exact safe quotient. The error certificate (1) must remain attached. It licenses the declared linear solve and, via the inexact-Newton error ledger, its subsequent nonlinear use; it is not equality under arbitrary future operations.

## 5. Executed adaptive inner solve: amplitude 1/10

Use wavevectors (1,1,0),(1,0,1),(0,1,1),(2,-2,0), plus conjugates. For each positive vector k choose the unit positive-helicity polarization

h_+(k)=[e+i(k cross e)/|k|]/sqrt(2),

where e is the coordinate unit vector at the zero coordinate of k. Coefficients are initially 1/10. This is the previously specified rank-three two-shell A3 initial field, not a new definition of native six-dimensional space.

Fix its heat reference v and g=N(v,v). With H=D0^-1 the zero-initial heat inverse and K_v h=N(v,h)+N(h,v), build

psi_1=Hg, psi_(j+1)=H K_v psi_j, j=1,2.

Every psi_j and A_j=D_v psi_j is a finite exact Fourier/exponential-polynomial packet family. We solve the 1-, 2- and 3-direction least-squares problems at 80 decimal digits only to propose coefficients, round coefficients to denominator 10^12, and independently validate the complete residual using exact algebra and rational intervals.

Results (percentages are readouts; acceptance uses exact rational endpoints):

m=1: 20 correction packets; 142 full residual packets; 68 output frequencies; relative residual 0.025137322052450395.
m=2: 216 correction packets; 886 full residual packets; 184 outputs; relative residual 0.0006960805758992771.
m=3: 1080 correction packets; 3940 full residual packets; 398 outputs; relative residual 0.000021710857030463298.

The last residual reaches squared Fourier radius 146. All these outputs are included, and all cross-rate terms are retained. The independently re-evaluated complete packet norm agrees exactly with the quadratic Gram formula.

The tolerance controller chooses m=1 for 10%, m=2 for 1% and 0.1%, and m=3 for 0.01%. These are smallest passing dimensions in THIS tested nested family, not global minimum-complexity claims.

The accepted m=3 coefficients are

999999731929/10^12, 999426205269/10^12, 998454393421/10^12.

Using the parent's L<=33/10, the error to the EXACT linear Newton correction is

||d_3-G_vg||_X < 364/10^9 = 3.64e-7.                             (9)

This is a linear-response error, not an additional outer nonlinear step or the final true-NS trajectory error. The present calculation executed one inner solve with three successively richer trial spaces.

## 6. A strictly enlarged concrete amplitude certificate: 3/25

Use the SAME eight-mode shape, now with each initial coefficient a=3/25=0.12 and nu=1. Repeat the three-direction graph solve at this amplitude; do not reuse numerical coefficients from the smaller-amplitude solve.

The canonical all-mode coefficient bound gives

B_infinity=a[3sqrt(2)(1/2+sqrt(1+sqrt(2)))
               +(sqrt(2)/2)(1/2+sqrt(1+2sqrt(2)))].

Rational nested-radical and exponential bounds prove

4 < L=e^B_infinity/sqrt(3/4) < 41/10,
31 < L C*/sqrt(3/2) < 32.                                      (10)

Let d be the accepted finite graph approximation, e=D_v d-g and F=D0d. Because d(0)=0, pure heat energy gives ||d||_X<=||F||_Y. Full coherent calculation then proves

||F||_Y < 0.0072981825081953... (exact outward endpoint is in JSON),
||e||_Y < 2.736575032e-7,
||G_vg||_X <= ||F||_Y+(41/10)||e||_Y < 73/10000.                 (11)

Take alpha=32, eta=73/10000 and r=3/250. Exact rational arithmetic gives

4alpha eta=584/625=0.9344<1,
r-eta-alpha r^2=23/250000>0,
2alpha r=96/125=0.768<1.                                       (12)

The inherited full nonlinear contraction theorem therefore yields a global smooth solution of this specified full NS initial-value problem, with

sup_(t>=0) [||u(t)-v(t)||_Hdot^1/2^2
        +(3/4)int_0^t ||u-v||_Hdot^3/2^2 ds] <= (3/250)^2.       (13)

The initial state is not a single-shell Beltrami solution. The theorem does not project away other helicities or any generated mode.

For comparison, the preceding ONE-response enclosure was

eta_old=a^2 sqrt(cR)+L a^3 sqrt(c3),
cR=0.2568344745..., c3=0.0162392455... .

The verified lower bounds sqrt(cR)>0.506, sqrt(c3)>0.127, L>4 and alpha_exact>31 imply

4 alpha_exact eta_old > 4*31*[a^2*(506/1000)+4a^3*(127/1000)] >1. (14)

Thus that specific previous test fails at 0.12 whereas (12) passes. Failure is of a sufficient estimator, not of NS regularity. No claim is made that all other known tests fail or that the amplitude threshold is optimal. The new radius 0.012 concerns the LARGER initial field; it is not compared as an accuracy improvement to the 0.1 field's prior nonlinear radius.

## 7. Link to the nonexact outer algorithm

Suppose a common admissible tube already supplies ||G_V||<=Lbar and ||B(f,g)||_Y<=C_B||f||_X||g||_X. For each current residual norm bound r_n, an accepted inner solve with defect epsilon_n gives

r_(n+1)<=epsilon_n+C_B Lbar^2(r_n+epsilon_n)^2.                   (15)

The parent also controls the sum of correction norms to keep references inside the tube. Section 3 supplies finite tolerance attainability for each such fixed admissible reference, so an idealized certified dense inner solver can implement the parent's prescribed forcing sequence rather than merely assuming exact solves.

The remaining restrictions are crucial: the initial state must pass a tube/basin certificate; the trial dictionary must be complete or have a certified complete fallback; coefficient and integration precision must be allowed to grow; the entire full residual, including time joins and out-of-core modes, is checked. Neither a fixed Krylov prefix nor a fixed arithmetic precision has a universal success guarantee.

## 8. Verification and persistence

Executed: current canonical packet backend unchanged and hash-checked; inherited initial/source oracle comparison; full heat-resolvent equations; conjugacy and divergence; six complete Gram entries; all same-output/cross-rate terms; independent final residual norm; outward rational LDL rank checks; a posteriori coefficient rounding loss; tolerance controller; enlarged-amplitude inverse and nonlinear ball inequalities. No PDE grid/time sampling was used.

LDL verifies all three Grams positive definite. Rounding suboptimality is bounded using (5) and is less than 10^-6 of each corresponding squared residual. This is not a floating-point optimality claim.

T0_BRC: REUSE_APPLIED; T6 operation-safe quotient: COMPOSE_APPLIED with an explicit nonzero error budget; current exact_packets.py: REUSE_EXECUTED; prior inverse and reference theorem: REUSE_APPLIED; adaptive graph Gram: EXTEND_EXISTING_TOOL. No Foundation promotion or mathematical acceptance is implied.

At this turn's GitHub discovery, the installed connector exposed reads but no create/update/commit action. Current seventh checkpoint was verified; the new eighth event is prepared locally and NOT claimed published. Publication must refresh both heads, check exact target-path absence, use a real write/CAS action, verify immutable bytes, and append a checkpoint without changing the first seven. Do not upload a duplicate of the old local seventh-package version: the canonical seventh source already exists.

## Primary context

- Dembo, Eisenstat, Steihaug (1982), Inexact Newton Methods, DOI 10.1137/0719025.
- Morosi and Pizzocchero, On approximate solutions of the incompressible Euler and Navier--Stokes equations, arXiv:1104.3832.

These acknowledge established general methods, not independent verification or priority of this note's constants or example. The current target remains practical adaptive efficiency and wider verified basins, not a universal all-data theorem.
