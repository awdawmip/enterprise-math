# D25 / AF4 — original low-band Hasse micro-deformation and quadratic finite boundary

Date: 2026-11-09. Original frozen task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance. AUTHOR-SIDE EXACT DERIVATION / FINITE INTEGER VERIFICATION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.

This is a new, directly usable **finite WZ/differential boundary** for the original missing low carrier `ell_p`. It retains signed weight and the first FOUR p-adic digits, and complements the already proved W2 first-jet and signed grade3 reciprocal tail. No alternative H0/B0 experiment is claimed.

## 1. Exact low-carrier construction

Let p=6m+1 be prime, p>3, and
`A_n=(2n)!(3n)!/((n!)^5 216^n)`, `C_n=(4n)!/((n!)^4 2304^n)`.
Write theta=z d/dz. Use the following three affine parameters over Z_(p)[X]:

* W: (`-3m+X/2`, `-2m+X/3`, `-4m+2X/3`); `N_W=3m`, `z_W=1/2`, `s_W=6`.
* V, p=4t+1: (`-t+X/4`, `-2t+X/2`, `-3t+3X/4`); `N_V=2t`, `z_V=1/9`, `s_V=8`.
* V, p=4t+3: (`-3t-2+3X/4`, `-2t-1+X/2`, `-t+X/4`); `N_V=2t+1`, `z_V=1/9`, `s_V=8`.

For each model Y define the **finite polynomial in X and z**
```
F_Y(X,z) = sum_{n=0}^{N_Y} z^n prod_{i=1}^3 (alpha_i(X))_n/(n!)^3,
G_Y(X,z) = (1+s_Y theta) F_Y(X,z).
```
At X=p the parameters equal respectively (1/2,1/3,2/3) and (1/4,1/2,3/4), so the following are exact rational identities, not p-adic approximations:
```
W_0,p + W_1,p = G_W(p,1/2),
V_0,p + V_1,p = G_V(p,1/9).
```
The low-band cutoffs are exactly the grade-0/grade-1 cutoffs for the original coefficients. For n<p all denominators n! and 2,3,4,9 are p-units. Thus Hasse coefficients `H_{Y,j}(z)=[X^j]G_Y(X,z)` (j=0..3) give the exact mod-p^4 equality
```
W_low - 2 V_low + p chi_p
  = sum_{j=0}^3 p^j (H_{W,j}(1/2)-2 H_{V,j}(1/9))
    +p chi_p                      (mod p^4)
```
with chi_p=(-3/p)=1 for p=1 (mod 6). Coefficients are computed in Z/p^4Z; no floating arithmetic, p-division of individual coefficients or inferred valuation is used. The grade of each original n is retained by the index and original model label. The two high bands remain separately represented by the existing b_p,t_p witnesses; the actual carry c_p remains required.

## 2. Exact finite hypergeometric boundary, not merely a new evaluation

Let `u_n(X)=prod_i (alpha_i(X))_n/(n!)^3` and `D_X=theta^3-z prod_i(theta+alpha_i(X))`. The original coefficient recurrence proves, as an EXACT polynomial identity in Q[X,z],
```
D_X F_Y(X,z) = - z^(N_Y+1) u_{N_Y}(X) prod_i(N_Y+alpha_i(X)).
```
Proof: the coefficients of z^n for 1<=n<=N cancel via
`n^3 u_n=prod_i(n-1+alpha_i)u_(n-1)`; the sole uncancelled coefficient is at z^(N+1).

The right-hand boundary is DIVISIBLE BY X^2 (over Q[X,z]), for BOTH models. One X factor is present in u_N because the shortest negative-integer numerator parameter crossed its zero before n=N. The other X comes from the middle negative-integer root, exactly at n=N, in `prod_i(N+alpha_i(X))`. This establishes the precise boundary-entry order: `[X^0]B=[X^1]B=0`, while `[X^2]B` is explicit and nonzero as a rational function. The two lowest Hasse-jet equations are boundary-free; the second- and third-order equations retain the exact endpoint forcing.

Writing `B=-z^(N+1)u_N prod_i(N+alpha_i)`, its explicit quadratic coefficient is:

* W, p=6m+1:
  `[X^2]B_W = m (2m)! (4m)!/[6 ((3m)!)^2] z^(3m+1)`.
* V, p=4t+1:
  `[X^2]B_V = (-1)^t t^2 (t-1)! (3t)!/[8 ((2t)!)^2] z^(2t+1)`.
* V, p=4t+3:
  `[X^2]B_V = (-1)^t (t+1) t! (3t+2)!/[8 ((2t+1)!)^2] z^(2t+2)`.

These identities follow by removing the one vanishing factor from `u_N(X)`, multiplying the remaining factorial blocks, and using the middle-root product derivative `-m^2/2`, `-t^2/2`, or `-(t+1)^2/2`, respectively. All displayed factorials are below p; after specialization to z=1/2 or 1/9 the leading quadratic boundary is a p-unit times a nonzero index factor.

For Hasse coefficient vectors `F_j=[X^j]F`, expand `D_X=D_0+X D_1+X^2 D_2+X^3 D_3`. Then the finite boundary supplies the directly testable differential system
`D_0 F_j = B_j - sum_{i=1}^j D_i F_(j-i)` for j=0,1,2,3,
with `B_0=B_1=0` and the explicit `B_2` above. This is an original-weight finite telescoping entry for a possible WZ/Fricke matching; it is not a proof of uniform AF4 cancellation.

## 3. Exact p^4 experiments / independent original coefficients

A deterministic Python integer-only program computed the 4-column Hasse carriers modulo p^4, evaluated at X=p, independently recomputed original integer binomial low sums for all listed p<=373, and verified each quadratic boundary by a SECOND multiplication path using the original affine factors plus the closed factorial formula. All 80 primes p=6m+1 in 7<=p<=1000 passed the Hasse and boundary checks. All eligible primes <=373 also passed the direct original-integer binomial comparisons.

p | W_low mod p^4 | V_low mod p^4 | ell_p=(W_low-2V_low+p)/p^2 mod p^2 | B2_W mod p | B2_V mod p
---|---:|---:|---:|---:|---:
13 | 24687 | 4407 | 94 | 2 | 6
19 | 127091 | 20596 | 238 | 5 | 6
37 | 428534 | 810485 | 498 | 18 | 14
43 | 3274622 | 2862295 | 524 | 40 | 10
73 | 19674741 | 12059600 | 4495 | 1 | 55
373 | 7176413322 | 6953946051 | 90746 | 57 | 79

The ell values are precisely those of the previous independently published native-original-grade low/high carry interface (20261109_onhour_d25_AF4_low_high_carry_boundary.md). At p373, ell=90746, existing signed b=33463 and tail t=40 reproduce ell+b+373t=139129; preserve base-p carry c=1.

## 4. Research value, original benchmark and continuation

This makes the previously missing low band a pair of finite hypergeometric boundary problems with explicit quadratic endpoint forcing, instead of recomputing grade-wise Wilson corrections. Next discriminating step: derive/evaluate a Fricke or WZ morphism between the two perturbed D_X systems that matches the low Hasse coefficients at z=1/2 and z=1/9, including the B2 endpoint and third-order carry. Test the specific morphism at p13/p19 first, then p373; only after a valid identity attempt both frozen congruence classes. A failure of a selected morphism tests only that morphism.

Highest native gap remains EXACT original same-class p373 H0/B0 divided-power [X]U mod139129, module rank, true semilinear Frobenius direction/eta, signed kappa and Delta-R with independent reproduction. Existing support issue #1559, no verified executor. This purely finite-binomial author-side mathematical result does not stand in for that experiment.

Source execution: old continuation receipt onhour11-20261109-1615-current-task-continuation SUCCEEDED; new request onhour11-20261109-1826-continuation was QUEUED at preparation, to be reconciled by its original request_id. Own recovery query returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED, no current valid own session/claim/run checked. Author-side GitHub-only evidence, UNREVIEWED / NOT_ADMITTED / NOT_NATIVE. No scheduler mutation.
