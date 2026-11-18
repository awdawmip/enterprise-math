# S23 n=3: exact global algebraic maximum of the near-optimal 36-variable fixed kernel

Date: 2026-11-07. Frozen scientific source: `enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is an author-side proof and executed exact-arithmetic certificate, pending independent mathematical review. The kernel is unchanged from PR #1777 @ `72c42391354a2decdacca583134e8f1f97130dc0`; its complete 4×10 integer matrix is in the predecessor `research_notes/brc_s23_av_n3_adaptive_bernstein_20261107_research1/VERIFY.py` (Git blob `e98d4379ff49754a9b946c88353da9345f878f62`).

## Exact statement

Let `a,c∈[1/2,7/8]` be real and `z=(1-a)c`. The true three-trial ordered ternary output law is `p(a,c)^⊗3` with `p=(a,z,(1-a)(1-c))`. Its compressed binary input law is `b(a,c)^⊗3`, `b=(z,1-z)`; the *same* unknown parameter pair governs all trials. The previously published parameter-independent 4×10 histogram kernel `T`, distributed uniformly among the `27` ordered ternary outputs in each orbit, defines an 8×27 stochastic kernel `K_full`. Write `E_K(a,c)=TV(p^⊗3,b^⊗3 K_full)`.

**Theorem.** The exact continuous maximum of this fixed kernel is

```text
sup_{a,c in [1/2,7/8]} E_K(a,c) = f(alpha)
alpha = [17858287858 + sqrt(17858287858^2
                           + 4*117051801689*27161727783)]/(2*117051801689)
alpha = 0.564000807741161103059938090753592679098057696720558132282420...
f(x) = (-819362611823*x^3 +187512022509*x^2
        +570396283443*x -112812037553)/512000000000
f(alpha) = 0.237382038860788688796186540996421995832765492810771699736795...
```

Equality is achieved at `(a,c)=(alpha,7/8)`. Consequently, using the earlier exact-fiber lower bound,

```text
5211/21952 <= delta_3 <= f(alpha).
```

The remaining minimax interval width is approximately `4.7909402484039968508e-7`. This theorem settles the exact maximum of the *specified kernel*; optimizing over all kernels is the next question.

## Proof (one local analytic rectangle and an exact exterior cover)

1. **Exact histogram observer.** Let `H={(h0,h1,h2)∈N^3:h0+h1+h2=3}` (ten orbits), `m(h)=3!/(h0!h1!h2!)`, and `M=10^9`. The integer 4×10 `T` has nonnegative entries and row sums `M`. For an input binary word `y` with `k` non-z labels and an ordered ternary output `x` with histogram `h`, put `K_full(y,x)=T[k,h]/(M*m(h))`. Since both output measures are exchangeable within an output orbit, their *full 27-label* total variation equals `E_K(a,c)=sum_{h∈H}max(0,R_h(a,c))`, with
   `R_h=m(h)*a^h0*z^h1*((1-a)*(1-c))^h2 - sum_{k=0}^3 binom(3,k)*z^(3-k)*(1-z)^k*T[k,h]/M`.
   The residuals sum to zero and are bivariate polynomials of degree at most three in each argument.

2. **Exact subdivision.** Set `u=(a-1/2)/(3/8)`, `v=(c-1/2)/(3/8)`, so the lawful parameter box is `[0,1]^2`. Reuse the exact tensor-cubic Bernstein coefficients and integer midpoint de Casteljau updates from the preceding verified `VERIFY.py`. On any rectangle, `E_K ≤ max_{i,j} sum_h max(0,beta_{h,i,j})`, because the same sixteen nonnegative tensor Bernstein weights sum to one and positive part is convex.

3. **Certified exterior.** Let `L=[5/32,6/32]×[31/32,1]` in `(u,v)`, equivalently `a∈[143/256,73/128]`, `c∈[221/256,7/8]`. Define the exact rational witness
   `W=1899056310874087867/8000000000000000000=E_K(141/250,7/8)`.
   The verifier starts at the entire unit square and alternates exact midpoint subdivision in `u,v`. A leaf is accepted if it is wholly within `L`; otherwise it is accepted if the integer Bernstein-hull inequality `hull*den(W)≤num(W)*den(hull)` holds. This terminates with **39 leaves, 38 splits, max depth 17**: one leaf equals `L`, 38 other leaves collectively cover its exterior. The largest exterior hull is exactly `52200830649622141951/219902325555200000000 = 0.23738189451988612... < W`. The leaves partition the entire original square, including boundaries.

4. **Analytic local signs.** The local rectangle `L` is selected exactly by five binary splits of each variable. Its tensor Bernstein coefficient signs for `R_h`, indexed by lexicographic `H`, are `(-,-,-,0,-,-,+,-,+,-)` everywhere: all nonzero signed controls are strictly positive after multiplication by their indicated sign (minimum integer numerator `120755729937220596791` over denominator `281474976710656000000000`). Thus on `L`, `E_K=R_6+R_8` identically. The Bernstein controls of `∂(R_6+R_8)/∂v` are strictly positive (minimum integer numerator `2791909083517799228280` over the same coefficient denominator). Consequently for each fixed `a` in `L`, `E_K(a,c)` is strictly increasing in `c`; its maximum over `L` occurs at `c=7/8`.

5. **Algebraic boundary maximum.** On `c=7/8`, exact Lagrange interpolation of `R_6+R_8` gives the stated cubic `f(a)`. Its derivative is
   `f'(a)=-21*(117051801689*a^2-17858287858*a-27161727783)/512000000000`.
   Throughout `a∈[143/256,73/128]`, `f''(a)<0`, and exact rational signs give `f'(141/250)>0`, `f'(282001/500000)<0`. Therefore the unique stationary point `alpha∈(141/250,282001/500000)` is the unique strict maximum in the local interval, and `f(alpha)>f(141/250)=W`.

6. The exterior cover gives `E_K≤W<f(alpha)` off `L`, and steps 4–5 establish `E_K≤f(alpha)` in `L`, attained at the specified boundary point. This completes the exact all-real theorem.

## Computation, provenance, and scope

The accompanying `VERIFY.py` extends the existing verified exact Bernstein module, checks the exact kernel entries, all local residual signs, positive local `c` derivative, the continuous-domain exterior partition, boundary coefficients, rational isolating bracket and strict concavity. Its `Fraction`/unbounded-integer assertions provide the proof certificate; decimal output is diagnostic only. `RUN_EVIDENCE.txt` records the actual execution. The previous 60-leaf bound remains a reusable independent upper-bound check, but this proof needs only 39 rectangles plus the analytic local argument.

BRC relevance: the compressed binary observer merges latent output sources; the 4×10 construction explicitly retains histogram multiplicity and the 27 ordered output labels, rather than treating their branch masses as interchangeable. The result is for the stated conditional-AV auxiliary observer, with frozen scientific inputs. A lawful encoder/decoder/observer bridge to the original six-source/ten-label mother problem `R_beh(k,10)` remains a separate research route.

Native task-control read returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH` and `operation_sent=false`; the formal activity, owner and CLAIM were not obtained. Artifacts are author-side proof for review and continuation, not a formal Result or independent review.

## Next

Find a new symmetric rational kernel with `sup E_K<f(alpha)` by a finite rational cutting-plane/LP certificate, or construct a finite-support signed-TV dual lower certificate above `5211/21952`, then attempt matched minimax closure. See `NEXT_TASK.md`.
