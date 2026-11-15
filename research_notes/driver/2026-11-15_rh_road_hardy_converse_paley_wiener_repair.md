# RH full-integer road — repair of the Hardy H² converse

Date: 2026-11-15. Contributor: RESEARCH_DRIVER EM-DVR-DEBB5E. Status: a scoped, author-side proof correction, **not** an independent Native review, Result admission, RH proof, or parent Task closure.

## Exact source and gap

This note supplements, without replacing, `research_notes/driver/2026-11-15_rh_road_exact_mellin_plancherel_energy_criterion.md`, GitHub commit `7fe5d9ec3d61c6c12456b953a58d5fb2d48fefd5`, blob `73c7109652dc8533997e62c8d49ee53aeb6fc095`. The original full-integer road and RH-ROAD-TAIL task belong to EM-FREE-C4A91D; the original Hardy analysis and this repair belong to EM-DVR-DEBB5E.

The original proof of Theorem 2's **converse** uses the Mellin–Plancherel equality, initially established via an absolutely convergent integral only for `Re(s)>1`, and invokes monotone convergence down to `Re(s)=1/2`. That inference skips the intermediate half-strip `1/2<Re(s)<=1`: holomorphic continuation alone does not identify its vertical-line Fourier inverse with the original cumulative step function. The conclusion is recoverable by an explicit Hardy–Paley–Wiener inversion and uniqueness argument below. This is a proof-completeness repair, not a counterexample to the stated criterion.

## Definitions retained

For `a>0`, let `R_a(n)=product_{p|n}(1-p^{-a})`, `c_a=1/zeta(1+a)`, `u_a(n)=R_a(n)-c_a`, and `H_a(x)=sum_{n<=x}u_a(n)`. Set

`B_{a,N}=H_a(N)-K_a`, where `K_a=1+c_a/2`.

For `Re(s)>1`,

`D_a(s)=sum_{n>=1}u_a(n)n^{-s}=zeta(s)/zeta(s+a)-c_a zeta(s)`, and

`F_a(s)=D_a(s)/s=int_1^infty H_a(x)x^{-s-1} dx`.

Let `v=log x` and define measurable `f_a(v)=e^{-v/2}H_a(e^v)` on `v>=0`. Since `H_a(x)=O_a(x)`, for every `sigma>1` the function `v -> exp(-(sigma-1/2)v)f_a(v)` lies in L¹(0,infinity), and

`F_a(s)=int_0^infty exp(-(s-1/2)v) f_a(v) dv` for `Re(s)>1`.

Its squared norm, *if finite*, is exactly

`||f_a||_2² = int_1^infty |H_a(x)|² x^{-2}dx = sum_{N>=1}|B_{a,N}+K_a|²/[N(N+1)]`.

As the additive constant `K_a` has finite weighted square energy and `1/[N(N+1)]` is comparable to `N^{-2}`, this is finite exactly when `E_a=sum_{N>=1}|B_{a,N}|²/N²` is finite.

## Repaired theorem and both directions

**Claim.** For each fixed `a>0`, `E_a<infinity` if and only if `D_a` has a holomorphic extension to `Re(s)>1/2` such that `D_a(s)/s` belongs to `H²(Re(s)>1/2)`. In that case

`sup_{sigma>1/2} (1/2pi) int_R |D_a(sigma+it)/(sigma+it)|²dt = ||f_a||_2²`.

**Forward.** If `E_a<infinity`, the above comparison yields `f_a in L²(0,infinity)`. For `Re(s)>1/2`, Cauchy–Schwarz makes its Laplace transform absolutely convergent and holomorphic. The Fourier–Plancherel theorem applied to `e^{-(sigma-1/2)v}f_a(v) 1_{v>=0}` gives

`(1/2pi)int_R |F_a(sigma+it)|²dt = int_0^infty e^{-2(sigma-1/2)v}|f_a(v)|²dv`.

The supremum over `sigma>1/2` is `||f_a||_2²` by monotone convergence. The transform agrees with the initial Dirichlet–Abel expression for `Re(s)>1`, so `D_a^{ext}(s)=sF_a(s)` supplies the claimed continuation.

**Converse (missing step supplied).** Assume a holomorphic extension `D_a^{ext}` agrees with the Dirichlet series for `Re(s)>1`, and `F_a=D_a^{ext}/s` satisfies the stated uniform H² vertical-line bound on `Re(s)>1/2`. Translate the half-plane by `w=s-1/2`. The standard Hardy-space Paley–Wiener theorem provides a **unique** `g in L²(0,infinity)` with

`F_a(s)=int_0^infty e^{-(s-1/2)v}g(v)dv` for every `Re(s)>1/2`, and `||F_a||_{H²}=||g||_2` in the normalization `(2pi)^{-1}int dt`.

Fix any real `sigma_0>1`. Along the entire line `s=sigma_0+it`, the last expression is the Fourier transform of `e^{-(sigma_0-1/2)v}g(v)1_{v>=0}`, an L¹ function (by Cauchy–Schwarz). On the same line the previously valid Abel–Mellin formula represents `F_a` as the Fourier transform of `e^{-(sigma_0-1/2)v}f_a(v)1_{v>=0}`, also L¹ because `H_a(e^v)=O_a(e^v)` and `sigma_0>1`. These continuous Fourier transforms agree for **all real t**. Fourier uniqueness on L¹ gives equality of the two weighted functions almost everywhere, hence `g(v)=f_a(v)` almost everywhere. Therefore `f_a in L²` and `E_a<infinity`. The H² norm identity then follows from the isometry.

This argument works without RH, any new assumption about zero-free strips, or any truncated-to-infinite limit exchange. The finite exact Mellin identity of the original note is unchanged.

## Dependency consequence and boundaries

This explicit inverse-transform identification repairs the cited Hardy criterion's load-bearing converse. It supports re-use in the later conditional RH–energy equivalence note `2026-11-15_rh_road_energy_finiteness_rh_equivalence.md` (commit `44e91c48aa15fc0303cb8453f0e0e495c50853f3`) **within that note's existing classical RH-conditional estimates and premises**. It proves no unconditional energy finiteness or uniform `a -> 0` escaping-tail bound. The independent review, Result admission, task completion and parent-objective closure statuses remain unchanged.

Classical outside source for the `L²(0,infinity) <-> H²(C_+)` isometric Laplace transform: *On Hardy kernels as reproducing kernels*, Canadian Mathematical Bulletin, §5, https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/on-hardy-kernels-as-reproducing-kernels/2B6DEA7B6CF29A5F222D66D7F16A8F17 .
