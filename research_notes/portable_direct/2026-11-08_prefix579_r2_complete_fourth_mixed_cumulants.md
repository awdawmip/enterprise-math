# PREFIX-579-R2 — Complete fourth-order joint cumulants of the native X6–BRC axes 5, 6 and gate

**Date:** 2026-11-08, Asia/Shanghai. **Status:** AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. Scientific input frozen at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Applicable control snapshot at study selection: EM main@7f2fd0941d6ee89a253b8dfc3c6a959058305f25; GK main@478fe3d59b50fe4787235dee4ba6f877e7bfb331. These are *normative read points*, not new scientific source pins.

## Mathematical population and observer

Use the frozen four-STAR native six-axis BRC kernel: 48 phases, 96 signed/branched native ports, six equally likely labeled actions per port. Keep all six native axis rewards and the branch/gate bit in the generating carrier. Observe R5(d), R6(d) and K(d), the two cumulative axis rewards and gate count after d ordered native actions. The PREFIX566 37-class future-exact quotient preserves the selected (R5,R6,K) observer across all legal future steps; its partition growth is 1,4,13,21,33,37. The original gate edges are 7→9,29→9,31→9. No physical time interpretation is assigned to d.

For any rational a,b,c define κ4(a,b,c)=lim_{d→∞} d^{-1} Cum_4(aR5(d)+bR6(d)+cK(d)), where Cum_4(X)=E[X^4]-4E[X^3]E[X]-3E[X^2]^2+12E[X^2]E[X]^2-6E[X]^4.

## Theorem 579.1 — Exact homogeneous fourth cumulant form

For every native initial port and all nine frozen roots (zero and ±e1,...,±e4), this limit exists and equals

    κ4(a,b,c)=A(a⁴+b⁴)+B(a³b+ab³)+Ca²b²
               +D(a³+b³)c+E(a²b+ab²)c
               +F(a²+b²)c²+Gabc²+H(a+b)c³+Ic⁴,

with *exact rational* coefficients:

    A=-659/93312             B=85/5832
    C=-191/15552             D=319/746496
    E=-149/248832            F=39167/28311552
    G=-7031/4718592         H=-3378511/1528823808
    I=434651857/97844723712.

The 15 symmetric coordinate multisets form nine axis-swap classes:

| Index multisets | Exact rate |
|---|---:|
| 5555, 6666 | -659/93312 |
| 5556, 5666 | 85/23328 |
| 5566 | -191/93312 |
| 555K, 666K | 319/2985984 |
| 556K, 566K | -149/2985984 |
| 55KK, 66KK | 39167/169869312 |
| 56KK | -7031/56623104 |
| 5KKK, 6KKK | -3378511/6115295232 |
| KKKK | 434651857/97844723712 |

In particular, Cum(R5,R6,K,K)/d→−7031/56623104 while Cum(R5,R5,K,K)/d→39167/169869312. The fourth rates of S=R5+R6 and D=R5−R6 are 2/729 and −1/18 respectively.

## Proof

For a fixed direction (a,b,c), form the 37×37 weighted transition matrix P(t), where each labeled edge i→j of weight m carries the factor m exp[t(ar5+br6+cg)]/6. This is an exact moment-generating *observer* of original native BRC paths. Its Taylor coefficients M_j=P^(j)(0)/j! are finite rational matrices with entries Σ_edges m(ar5+br6+cg)^j/(6j!). No floating-point evaluation of the exponential is required.

The frozen quotient is an irreducible Markov chain of period two, its stationary row vector being π_i=|class_i|/96. The eigenvalue 1 of P(0) is algebraically simple, so Z=I−P(0)+1π is invertible. The positive Perron eigenvalue λ(t) is analytic near t=0. Decomposing each of the two cyclic parity classes gives the path MGF from any starting port as λ(t)^d times a locally analytic nonzero prefactor, with bounded derivatives of its logarithm. Therefore the normalized asymptotic fixed-order cumulants are the derivatives of log λ(t).

Normalize the right eigenvector by πv(t)=1 and expand v(t)=1+Σ_j v_j t^j, λ(t)=1+Σ_j l_j t^j. For j=1,2,3,4 set

    u_j = Σ_{k=1}^j M_k v_{j−k},
    l_j = πu_j,
    Z v_j = u_j−l_j·1−Σ_{k=1}^{j−1} l_k v_{j−k},
    πv_j = 0.

Coefficient comparison of P(t)v(t)=λ(t)v(t) gives these identities exactly; uniqueness follows from invertibility of Z. The fourth derivative of the logarithm is

    24 l4 − 24 l1 l3 − 12 l2² + 24 l1² l2 − 6 l1⁴.

Every linear equation and normalization is checked with exact integer/rational arithmetic for the computed directions.

The native 5↔6 axis involution fixes K and implies that the fourth homogeneous polynomial has the nine coefficient groups A,...,I. Use the nine directions R5,S,D,K,R5+K,R5−K,R5+2K,D+K,S+K. The recovery is triangular: A=κ4(R5), I=κ4(K), B=(κ4(S)−κ4(D))/4, C=(κ4(S)+κ4(D))/2−2A. Write U+=κ4(R5+K)−A−I, U−=κ4(R5−K)−A−I and U2=κ4(R5+2K)−A−16I. Then F=(U++U−)/2, V=(U+−U−)/2, H=(U2−4F−2V)/6, D=V−H, G=2A−2B+C+2F+I−κ4(D+K), and E=[κ4(S+K)−(2A+2B+C+2D+2F+G+2H+I)]/2. Substituting exact eigenvalue derivatives yields the coefficients in the theorem. This interpolation is exact and uniquely determines every coefficient.

Four additional independent directional calculations (R6,D−K,S−K,R5+3K) reproduce the predicted fourth polynomial exactly. All thirteen directions also reproduce the complete published third-order homogeneous cumulant form of PREFIX578-R2, and the pure-gate fourth equals PREFIX577-R2's 434651857/97844723712. The frozen root-gauge theorem (PREFIX577 root endpoint relation) conjugates the weighted transfer matrices under allowed root changes, hence all nine frozen roots have identical spectral pressure and fixed-order asymptotic cumulants. This proves the theorem.

## Verification and executable artifacts

The research branch includes:

- PREFIX579_R2_native_kernel.py — importable frozen native 96-port edge kernel and 37-state quotient, mechanically factored from the published PREFIX578-R2 exact certificate; the underlying Git source is unchanged scientifically.
- PREFIX579_R2_fourth_cumulants.py — executable SymPy exact perturbation, nine-direction recovery, four independent extra-direction checks, third-order regression, pure-gate regression.
- PREFIX579_R2_independent_depth4.py — separate exact integer raw-moment DP on all 96 original native ports, degrees 0..4, with all six labeled actions.
- PREFIX579_R2_results.json — exact coefficients and an execution summary. The locally executed complete raw result files are also preserved in the downloadable research bundle linked in the corresponding run.

The locally executed full variant of the perturbation certificate reported ALL_ASSERTIONS_PASS (9 base and 4 independent prediction directions; every normalized rational linear system checked). The separately executed native 96-port DP reported ALL_ASSERTIONS_PASS for d=1,2,4,8,16,32,64,128. For uniformly averaged starting ports, the finite-depth fourth rates at depth 128 are:

| Direction | Finite rate (12-digit display) | Exact limit |
|---|---:|---:|
| R5 | -0.007376016304 | -659/93312 |
| S | 0.002547010745 | 2/729 |
| D | -0.058503327546 | -1/18 |
| K | 0.004443377691 | 434651857/97844723712 |
| S+K | 0.003499134374 | determined by the above homogeneous form |

The finite-depth DP checks implementation agreement; the limit follows from the spectral argument and the exact recursion. Model scope is an exact finite BRC path-count probability observer, rather than a physical stochastic claim. The native 96-port carrier retains provenance and all six axis rewards; the 37-state quotient is applied only to the stated three-reward observer.

Published sources: frozen native PREFIX565/566 kernel; PREFIX578-R2 third tensor (research PR #1793, commit 8e85ed62f13190c7b78e0455858e25ca82d46a4c); canonical main PREFIX578-R6 complete six-axis third cumulants (main@7f2fd0941d6ee89a253b8dfc3c6a959058305f25); gate-only fourth from PREFIX577-R2 (commit 6675bfa4a8c838b7223382ae5f6831de95552683). No new P000 assumptions, proof status elevation, or changes to frozen roots are used.

## Smallest next new unit

Compute fourth joint cumulants involving the six-axis gate residual Y=K−β·(R1,...,R6), where β=(5,−1,5,−1,−4,−4)/192 comes from the independently published complete six-axis covariance. Use the *96-port* chain (the 37-class q5/q6/gate observer loses the other four rewards). A first validation target is agreement of its 5/6/K principal subtensor with all nine exact classes above. Next calculate Cum(Y,Y,R_i,R_j)/d and investigate the fourth-order residual signature after second-order orthogonal projection.

## Current identity and persistence

GitHub current user awdawmip has admin access to both repositories. Native Enterprise Math status, task-owner listing, and session-start endpoints returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE with operation_sent=false. This author-side branch records scientific evidence but creates no native claim, Researcher-ID, activity registration or Driver review. The formal task owner, Result and canonical admission remain unconfirmed.
