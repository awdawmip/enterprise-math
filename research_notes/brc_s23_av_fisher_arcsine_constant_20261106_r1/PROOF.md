# S23 conditional AV — Fisher–arcsine reconstruction with an improved asymptotic overlap constant

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_DERIVATION / FINITE_EXACT_CHECKS_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent frontier: Draft PR #1777, `research_notes/brc_s23_av_uniform_beta_theta_20261106_r1/PROOF.md` at commit `960447e8c906f620e07bcdc08653c74f4b658358`.

## Model and theorem

For a,c in [1/2,7/8], write z=(1-a)c, q=(1-a)(1-c), P=(1-z-q,z,q) with tags (stop1, stop3, stop4). B=(1-z,z) has tags (other,stop3). In n independent repetitions the *same* unknown (a,c) is used. Define
`delta_n = inf_K sup_(a,c) TV(P_(a,c)^{tensor n}, B_z^{tensor n} K)`,
where K is an arbitrary parameter-independent stochastic reconstruction kernel.

Conditional on each compressed word, let M be the count of other positions and r=q/(1-z). Then
`1/57 <= r <= 1/3`, `1/16 <= z <= 7/16`, and `M ~ Bin(n,1-z)`.

**Theorem A (explicit full arcsine kernel).** Reconstruct every stop3 position unchanged. Independently draw ONE shared R ~ Beta(1/2,1/2), then fill each other position conditionally independently with stop4 probability R. Call this universal kernel K_arc,n. Then, uniformly over all lawful real a,c,

`sqrt(n/log n) * [1-TV(P_(a,c)^{tensor n}, B_z^{tensor n}K_arc,n)] -> (2/pi)/sqrt(1-z)`.

Consequently, with the infimum taken over the lawful parameter box,

`lim_(n->infinity) sqrt(n/log n) inf_(a,c) [1-TV(P^n, B^n K_arc,n)] = 8/(pi sqrt(15)) = 0.657498073665600...`.

**Theorem B (optimized padded Fisher-family lower bound).** Put
`I_* = 2 (arcsin sqrt(1/3) - arcsin sqrt(1/57)) = 0.965272185863044...`.
For each fixed `0<l<1/57`, `1/3<u<1`, replace the shared Beta draw by R with density
`w_(l,u)(t) = 1_[l,u](t) / (I_(l,u) sqrt(t(1-t)))`,
where `I_(l,u) = 2 (arcsin sqrt(u) - arcsin sqrt(l))`.
The resulting single shared-latent kernel satisfies

`lim_(n->infinity) sqrt(n/log n) inf_(a,c)[1-TV(P^n,B^n K_(l,u),n)] = 8/(I_(l,u) sqrt(15))`.

Taking the supremum over fixed padded intervals and then the asymptotic limit gives the new universal minimax deficiency bound:

**`liminf_(n->infinity) sqrt(n/log n) (1-delta_n) >= 8/(I_* sqrt(15)) = 2.139905353359433...`.**

The prior author-side Hoeffding multi-hypothesis upper bound remains `1-delta_n <= (28/3) sqrt(log n/n)+2/n^2` for n>=1000. The new coefficient is a lower bound on the minimax overlap; its optimal value is not yet determined.

## Exact BRC / beta-binomial branch count

For K_arc,n, conditional on a compressed word y with m other positions, the true stop4 count S has law `p_m(k)=C(m,k)r^k(1-r)^(m-k)`. The reconstructed count has the **exact integer** law

`Q_m(k) = C(2k,k)*C(2m-2k,m-k)/4^m`, 0<=k<=m.

Indeed, integration against Beta(1/2,1/2) yields
`C(m,k)*B(k+1/2,m-k+1/2)/pi = Q_m(k)`.
The integer convolution `sum_(k=0)^m C(2k,k)C(2m-2k,m-k)=4^m` follows from `(1-4x)^(-1/2)^2=(1-4x)^(-1)`. Conditional on count k, both true and reconstructed laws are uniform over the C(m,k) labeled subsets. Thus the full 3^n-word overlap reduces exactly to

`H_n(z,r)=E_(M~Bin(n,1-z))[h_M(r)]`,
`h_m(r)=sum_(k=0)^m min(p_m(k),Q_m(k))`.

This law keeps the observed stop3 positional branch trace, exact stop1/stop4 multiplicity, and ONE shared latent hidden-branch coordinate. Its finite rational weights form a BRC-compatible labeled positive-mass histogram, rather than a signed amplitude or a new native spatial primitive.

## General uniform local-overlap lemma (analytic)

Let J be a compact interval strictly inside (0,1), and let w be a probability density supported in (0,1), bounded on its support and strictly positive, continuously differentiable on a neighborhood of J. Draw one shared R~w and independently fill m hidden labels conditionally on R. Its count mixture is
`Q_m^w(k) = C(m,k) integral_0^1 t^k(1-t)^(m-k)w(t)dt`.

Then, **uniformly for r in J**,

`lim_(m->infinity) sqrt(m/log m)*sum_(k=0)^m min(Bin(m,r){k},Q_m^w(k)) = 2w(r)sqrt(r(1-r))`.   (L)

Proof. Set v=r(1-r), t=k/m and d_m=sqrt(m v log m). Uniformly in r in J and |k-mr|<=C d_m, beta-posterior concentration gives
`Q_m^w(k)=(w(r)+o(1))/m`:
`Q_m^w(k)=(m+1)^(-1) E[w(T)]` for T~Beta(k+1,m-k+1), and the posterior concentrates uniformly at k/m=r+o(1); bounded w handles the tails. Uniform Stirling expansion gives
`log p_m(k)=-(1/2)log(2pi m v)-(k-mr)^2/(2mv)+o(1)`.
For fixed epsilon in (0,1), `p_m(k)>Q_m^w(k)` throughout `|k-mr|<=(1-epsilon)d_m` once m is sufficiently large. The contribution of that interval to h_m is asymptotic to `2(1-epsilon)w(r)sqrt(v log m/m)`. For the upper bound, bound the central interval `|k-mr|<=(1+epsilon)d_m` by its Q mass, asymptotic to `2(1+epsilon)w(r)sqrt(v log m/m)`. Bound the remainder by the true Binomial tail. Chernoff's KL bound and uniform Taylor expansion of `D(r+d||r)=d^2/(2v)(1+O(d))` give a tail at most `2m^{-(1+epsilon)^2/2+o(1)}=o(sqrt(log m/m))`. Let epsilon decrease to zero; all errors are uniform on J. This proves (L).

For the *full* arcsine density `w(t)=1/(pi sqrt(t(1-t)))`, which is unbounded only at 0 and 1, the same argument applies uniformly on J by the exact integer expression for Q_m(k), or by uniform central Gamma-ratio asymptotics; near r in J it gives `Q_m(k)=(1+o(1))/(pi m sqrt(v))`. Therefore (L) holds for that case as well.

## Random compressed count and minimax constants

For lawful z, `M~Bin(n,1-z)` has `1-z in [9/16,15/16]`; Chernoff concentration ensures uniformly that `M/n=(1-z)+o_P(1)`. Also `0<=h_M<=1`; the exceptional event outside a fixed positive-width concentration window has exponentially small probability, which is negligible on the `sqrt(log n/n)` scale. Uniform lemma (L) therefore implies

`sqrt(n/log n)*H_n(z,r) -> 2w(r)sqrt(r(1-r))/sqrt(1-z)`

uniformly on lawful (z,r), for the chosen w. For full arcsine, `w(r)sqrt(r(1-r))=1/pi`; for padded Fisher, it equals `1/I_(l,u)`. The infimum over lawful pairs is attained asymptotically at smallest z=1/16, an actual lawful corner `(a,c)=(7/8,1/2)` with r=1/15. Hence the exact asymptotic infimum constants are `8/(pi sqrt(15))` and `8/(I_(l,u)sqrt(15))`, respectively. Since `delta_n` is an infimum over all kernels, any one construction bounds `1-delta_n` from below. Finally let l increase to 1/57 and u decrease to 1/3 **after** the n->infinity limit. This proves Theorems A and B.

## Validation, scope and next question

`VERIFY.py` executed 144 exact integer/Fraction assertions: normalization of the arcsine integer histogram for m=0..120, three lawful corner checks, and exact finite-m overlaps at three rational r. A separate floating-point diagnostic at m=100,1000,10000 illustrates convergence; it is not an analytic proof or a finite error certificate. The universal asymptotic claims rest on the argument above, awaiting independent review.

BRC reuse: exact positive rational labeled branch mass / multiplicity / count histogram from `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`; resolution `REUSE_APPLIED`. No new signed cancellation or native spatial interpretation is asserted. This is a source-conditional statistical auxiliary S23 result. The mother six-source/ten-label lawful encoder-decoder problem `R_beh(k,10)`, k=4,6, still needs a separately checked observation map.

Next: quantify the optimal prior allowed to depend measurably on the compressed z estimate; derive an upper matching leading constant, and inspect boundary fibers. The fixed-Fisher family already beats the full arcsine leading constant and the earlier uniform-R quantitative constant by a wide margin.
