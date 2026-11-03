# D25 signed-prefix: rational Gosper obstruction and full Green observer rank

Date: 2026-11-03 (+08). Author-side TASK_RESEARCH, frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Logical lane `chatgpt-research-hourly-enterprise-math-20260923` (not maintenance `chatgpt-hourly-enterprise-math-20260921`). Status: **AUTHOR-DERIVED / ALGEBRAICALLY PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Consumes earlier signed-prefix Green note at `6e566d86091cd675165e316e850574feb6720dd6` and the independent onhour far-strip author note at `b7509e56ebfab1cfd855e88bb08f57b25a8cd71f`. Neither is reclassified as this run's native predecessor contribution.

## Theorem 1: no p-independent rational single-index antidifference for any nonzero affine weight

Let `b_k=(1/2)_k(1/3)_k(2/3)_k/(2^k(k!)^3)=binom(2k,k)^2 binom(3k,k)/216^k`. For `alpha,beta in Q`, a rational function `R(k) in Q(k)` satisfying
```
(2k+1)(3k+1)(3k+2) R(k+1) - 36(k+1)^3 R(k)
    =36(k+1)^3 (alpha*k+beta)                     (1)
```
exists **iff** `alpha=beta=0`. This excludes the simple rational Gosper boundary `R(k)b_k` for the original signed weight `6k+1`, without excluding p-dependent identities or genuine two-variable WZ/contiguous certificates.

**Proof.** The exact ratio is `b_(k+1)/b_k=a(k)/B(k)`, with `a=(2k+1)(3k+1)(3k+2)`, `B=36(k+1)^3`. If a rational solution has poles, take a pole `z_min` of smallest real part over C. At `k=z_min-1` only `R(k+1)` has a pole; polynomiality of the right side forces `a(z_min-1)=0`, hence `z_min in {1/2,1/3,2/3}`. At a pole `z_max` of largest real part, only `R(k)` has a pole; this forces `B(z_max)=0`, so `z_max=-1`. Contradiction. Therefore R is a polynomial. Since leading terms of `a R(k+1)-B R(k)` at degree `deg(R)+3` are `-18` times its leading coefficient, `deg R<=1`. Write `R(k)=Ak+B0`. Comparing `k^4,k^3` gives `A=-2alpha` and `B0=alpha-2beta`. Comparing `k^2,k^1` gives `-53alpha+54beta=0` and `-89alpha+82beta=0`, with determinant `460`. Thus `alpha=beta=0`; the zero case has `R=0`. For the original weight `alpha=6,beta=1`, the forced `R=-12k+4` has exact nonzero equation residual `-264k^2-452k-196`. QED.

## Theorem 2: full polynomial Green readout is injective; signed scalar has kernel dimension r-1

Let `p=6r+1>=13` be prime and work over F_p. For 0<=t<=r, `a_t=(1/2)_t(1/3)_t(2/3)_t/(t!)^3` and `b_t=a_t 2^{-t}` are units. For a **formal** arbitrary source vector `q=(q_1,...,q_r)`, define
```
K_t(q)=-(a_t/3)*sum_(j=t+1)^r q_j/(j^2*a_j), 0<=t<r,
O_w(q)=(1/2)*sum_(t=0)^(r-1) w(t)*2^(-t)*K_t(q)
      =-(1/6)*sum_(j=1)^r q_j/(j^2*a_j)*sum_(t=0)^(j-1) w(t)*b_t.    (2)
```
For the **actual** Gauss source `q_j=ell_j=binom(r,j)binom(2r,j)`, `O_(6t+1)(ell)` is exactly the previously proved signed-prefix Clausen defect E_p. Formal perturbations q used below are an information-observer test, not claimed to be independently realizable Gauss data.

The r readouts `O_(t^m)(q)`, m=0,...,r-1, determine q uniquely: the q-to-K matrix is upper triangular with diagonal `-a_t/[3(t+1)^2 a_(t+1)]` (units); the K-to-readout matrix is Vandermonde at distinct residues 0,...,r-1 times unit column factors `2^{-t}/2`. Consequently the full polynomial observer rank is r.

By contrast, `O_(6t+1)` is nonzero because the q_1 coefficient `C_1=-1/(6a_1)` is a unit, so this scalar map has rank 1, kernel dimension r-1. Set `T_(j-1)=sum_(t<j)(6t+1)b_t`, `C_j=-T_(j-1)/(6j^2a_j)`. The nonzero source perturbation `q_1=C_2,q_2=-C_1,q_3=...=0` lies in its kernel while changing K (injectivity). Thus the scalar is sufficient for its own fixed readout but not for every later polynomial-weight operation. The full source remains available via (2) and the actual ordered t<j geometry.

**Examples (mod p):** p=13: r=2, (C1,C2)=(5,2), q=(2,8), K0=3; p=19: (8,13), K0=2; p=37: (17,8), K0=14; p=373: (185,92), K0=57.

## Verification, scope and next scientific action

Standard-library exact arithmetic was actually run for all **77 target primes p<=2000, p mod24 in {13,19}**: the characteristic-zero polynomial residual, independently formed b/a coefficient ratios, original/adjoint double evaluation of (2) for both actual ell and artificial source, and the explicit nonzero kernel perturbation. All PASS. These finite checks accompany the written general proof; they are not independent mathematical review.

The fixed mother objective remains `W_p(1)=p (mod p^3)` for p mod24 in {13,19}, equivalent to `Delta_p-R_p=0 (mod p)`. Next executable scientific step: test a **two-index or p-dependent** terminating WZ/CM certificate for the four-source fixed-base second carry from onhour `b7509e56ebfab1cfd855e88bb08f57b25a8cd71f`: low/mid Gauss + far Gauss + Gauss square + original signed Clausen prefix, including signs and H2 provenance at p=13,19,373. Theorems 1-2 establish route scope and information requirements; they do not prove universal fixed-base cancellation.

Native status on 2026-11-03: `em_status 0.6.11`, `UPSTREAM_CODE_REVIEW_REQUIRED`, `research_authority_granted=false`, `executor_binding_configured=false`, `active_jobs=5/5`. Own previous recovery #6637 succeeded as a read-only projection: historical session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, no run, no own unpublished uploads, two preserved neutral archives; original continuation #6638 definitively failed `UPSTREAM_CODE_REVIEW_REQUIRED`. No replay, new session/claim/open, Source checkpoint, Result, formal admission, or scheduler/notification change is claimed. Support #1558 is control; #1559 is the unexecuted native benchmark.
