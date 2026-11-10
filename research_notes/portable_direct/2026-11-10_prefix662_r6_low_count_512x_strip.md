# PREFIX-662-R6 — Low-count Bernstein certificate enlarges the unique BRC edge-maximizer strip by 512×

Date: 2026-11-10 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-82DD7D` / TASK_RESEARCH; Research-Activity-ID: `RA-6F7CCD285ACC73B911ADCC42`.
Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: **AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem 662.1 — 512× larger unique-maximizer strip

Let `V_q(p,z)=q² W(p,z)-q μ(p,z)`, with `μ=E[Y]` and `W=Var(Y)`, for the frozen 189-survivor-layer two-informative-direction BRC statistical observer of PREFIX-659–661. The two parameters are statistical observation probabilities; this is not a claim concerning physical native spatial dimensions. Let

```
I=[607/4096,609/4096],
R_new=[0,2^(-21)] × I,
q∈[12,24] (any real interpolation).
```

Then for EVERY `(p,z)∈R_new` and `q∈[12,24]`,

```
∂_p V_q(p,z) < -73404.
```

Writing `z_*(q)` for the unique moving edge maximizer on `I` certified by PREFIX-660 and `M_q=V_q(0,z_*(q))`, the UNIQUE maximizer over the entire `R_new` is `(0,z_*(q))`. Moreover

```
M_q - V_q(p,z) >= 73404*p + 6400000*(z-z_*(q))²
```

with strict inequality off the maximizer. PREFIX-661 certified the same maximum only on `[0,2^(-30)]×I`, so the newly certified two-dimensional area is EXACTLY 512 times larger. The rigorous `M_12,M_24` numerical brackets in PREFIX-660 remain valid on the enlarged rectangle.

## Proof: retain the lowest three signed-path multiplicities

For `n=0,...,188` let `A_n(k)` be the frozen surviving path multiplicities and `f_n(k)=A_n(k)/binom(n,k)∈[0,1]`. The original `wide(n,k)` filtering predicate is applied at every step. Because the path count index `k` only increases, the three entries `A_n(0),A_n(1),A_n(2)` can be computed exactly by the CLOSED recurrence

```
A_0(0)=1, A_0(1)=A_0(2)=0,
A_n(k)=wide(n,k)*(A_(n-1)(k)+A_(n-1)(k-1)), k=0,1,2.
```

Terms with out-of-range indices are zero. This is an exact projection of the full original integer recurrence for these three coordinates, not a replacement statistical model. The resulting nonzero low-count states are:

* `n=2,...,24`: `(A_n(0),A_n(1),A_n(2))=(1,n,binom(n,2))`;
* `n=25,...,33`: `(0,25,300+25(n-25))`;
* `n=34,...,41`: `(0,0,525)`;
* `n>=42`: `(0,0,0)`.

In particular `s_n'(0)=25` only for `n=25,...,33`, and zero otherwise. This is the exact boundary coefficient support independently used in PREFIX-659/661.

The Bernstein second-difference identity, for `n>=2`, is

```
s_n''(p)=n(n-1) E[Δ² f_n(K)],  K~Binomial(n-2,p),
Δ² f_n(k)=f_n(k+2)-2f_n(k+1)+f_n(k).
```

Since `|Δ² f_n(k)|<=2` and `P(K>=1)<= (n-2)p`, we obtain on `0<=p<=ε`

```
|s_n''(p)| <= n(n-1)*(|Δ² f_n(0)| + 2(n-2)p).
```

Exact integer/Fraction enumeration of the three-coordinate recurrence gives

```
A=Σ n(n-1)|Δ² f_n(0)|                   = 13800,
C=Σ (n+1)n(n-1)|Δ² f_n(0)|             = 485400,
B=2Σ n(n-1)(n-2)                       = 617937012,
E=2Σ (n+1)n(n-1)(n-2)                 = 93926425824.
```

All sums use `n=2,...,188` (zero terms allowed). The Poisson two-clock moment kernels multiply each `s_n(p)` by a nonnegative factor in `[0,1]` for `μ`, and in `[0,n+1]` for `H=E[Y²]/2`. Therefore, uniformly for all `z∈[0,1]`,

```
|μ_pp| <= A+Bp,      |H_pp| <= C+Ep.
```

Also the exact boundary support and nonnegative kernel yield `0<=μ_p(0,z)<=9*25=225`. Integrating,

```
|μ_p(p,z)| <= 225+Ap+(B/2)p².
```

The frozen clocks stop by level 189, so `0<=μ<=378`. With `W=2H-μ²`,

```
|W_pp| <= 2(C+Eε)+2(225+Aε+Bε²/2)²+756(A+Bε).
```

For `ε=2^-21`, set this last right-hand side to `K_W` and put `K=576 K_W+24(A+Bε)`. The standalone certificate proves the EXACT strict comparison

```
ε*K = 257162703256418492566176496126353 /
      79228162514264337593543950336 < 3246.
```

Hence for `12<=q<=24`, `|V_(q,pp)|<=K`.

PREFIX-661's exact whole-edge-band bounds are `V_(12,p)(0,z)<-76650` and `V_(24,p)(0,z)<-306490`. For fixed `z`, `V_(q,p)(0,z)/q=q W_p(0,z)-μ_p(0,z)` is affine in `q`. Both endpoint bounds imply `V_(q,p)(0,z)<-76650` for all real `12<=q<=24`. Moving from `p=0` to `0<=p<=ε` gives

```
V_(q,p)(p,z) < -76650 + K*ε < -73404.
```

PREFIX-660 proves `V_(q,zz)(0,z)<-12800000` and a unique `z_*(q)∈I`; integrating the p-gradient and the edge strong concavity gives the claimed stability and uniqueness. QED.

## Verification, reuse, next scientific question

`PREFIX662_R6_BOUNDARY_STRIP_512X_CERTIFICATE.py` verifies the exact frozen low-k predicate by integer bisection for `k<=2`, runs the closed integer recurrence, enumerates all 189 low-count rows, checks `A,B,C,E`, and proves the rational inequality `εK<3246`. It prints `ALL_CHECKS_PASS 569`; the companion `PREFIX662_R6_RESULTS.json` stores the exact unreduced variation fraction and statement scope. The 569 includes predicate checks; it is not 569 independent theorems.

BRC tool resolution: **COMPOSE_APPLIED**. This keeps signed-path multiplicities and the exact binomial observer, and uses a justified low-degree projection only for the local derivative bound. The remaining coefficients are bounded by the universal `[0,1]` coefficient law; their identities are not discarded from the underlying model. No original 96-port dynamics run is claimed.

Predecessors: PREFIX-660 and PREFIX-661 in `research_notes/portable_direct/`, verified on Source `main@ba84ca80a30885d84ebc9f2efb570eeb630ff3b2`, with the same frozen scientific pin. The new certificate rechecks its own load-bearing finite low-k identities; it uses the previously certified exact edge gradients and curvature. No independent review or formal Result/Review acceptance has occurred.

Next discriminating unit: exploit the low-count Bernstein boundary layer to derive a tighter `p`-gradient sign on a wider portion of the symmetry-reduced triangular chamber, or produce an explicit outside-strip competitor. The parent question remains global maximization of `V_12,V_24` on `[0,1]^2`.
