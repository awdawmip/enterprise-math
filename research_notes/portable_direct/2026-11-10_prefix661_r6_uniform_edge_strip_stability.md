# PREFIX-661-R6 — Unique BRC maximum on a two-dimensional boundary strip

Date 2026-11-10 (Asia/Shanghai). Frozen scientific input `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Researcher-ID `EM-DIRECT-5DFA63` / TASK_RESEARCH; Research-Activity-ID `RA-F8AD12FF4F5A07E9388F1939`.
Evidence level: **AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.

## Theorem 661.1 — The full two-dimensional thin strip has an exact unique maximum

Let `V_q(p,z)=q^2 Var(Y(p,z))-q E[Y(p,z)]` be the **frozen 189-layer BRC two-direction statistical observer** of PREFIX-659 and PREFIX-660; the parameters are statistical probabilities, not physical native axes. Set

```
I = [607/4096,609/4096],
R = [0,2^(-30)] x I,
12 <= q <= 24  (all real interpolated slot values).
```

For every `(p,z) in R` and real `12<=q<=24`, the first-coordinate gradient has the **strict uniform sign**

```
partial_p V_q(p,z) < -73000.
```

Consequently the maximum of `V_q` over all of `R` is uniquely attained at

```
(p_*(q),z_*(q))=(0,z_*(q)),
```

where `z_*(q)` is the strictly increasing unique edge stationary point proved in PREFIX-660. If `M_q=V_q(0,z_*(q))`, then a quantitative stability inequality holds on the *whole rectangle*:

```
M_q - V_q(p,z) >= 73000 p + 6400000 (z-z_*(q))^2,
```

strict whenever `(p,z)` differs from the unique maximizer. This connects the moving boundary optimum to an authentic two-dimensional region. The full-domain maximum on `[0,1]^2` remains open.

In particular, certified numerical maximum intervals for this rectangle at the actual slots remain the exact PREFIX-660 values:

```
86048.1065484294 < M_12 < 86048.1065484353
346340.5678394088 < M_24 < 346340.5678394320.
```

## Proof — exact first-coordinate derivative polynomial

PREFIX-659 identifies the boundary Bernstein first-derivative rows:

```
d s_n(p)/dp at p=0 = 25 for n=25,...,33, and zero otherwise.
```

Using `w(n,m)=binom(n+m,n)/2^(n+m+1)`, the exact edge derivatives of the Poissonized first two moments are

```
mu_p(0,z)=25 sum_{n=25}^{33} [
  1 - sum_{m=0}^{188} w(n,m) s_m(z)
],
H_p(0,z)=25 sum_{n=25}^{33} [
  (n+1) - (1/2)sum_{m=0}^{188}(n+m+1)w(n,m)s_m(z)
].
W_p(0,z)=2H_p(0,z)-2mu(0,z)mu_p(0,z).
V_{q,p}(0,z)=q^2 W_p(0,z)-q mu_p(0,z).
```

Here `s_m(z)=sum_k A_m(k)z^k(1-z)^(m-k)` uses the **same frozen integer survivor rows**. The sibling exact certificate reconstructs them and proves boundary Gamma(25,1); no change to the scientific input is made.

All coefficients of `mu,mu_p,H_p` are dyadic with denominator dividing `S=2^225`. Expand them in the integer power basis and then form `P_q(z)=S^2 V_{q,p}(0,z)`:

```
P_q(z) = 2q^2 S H_p_scaled(z) - q S mu_p_scaled(z)
         - 2q^2 mu_scaled(z) mu_p_scaled(z).
```

Expand `P_q(z0+h)=sum_{k=0}^{376}c_{q,k}h^k` at `z0=19/128`. For every `|h|<=1/4096`, exact `Fraction` arithmetic gives

```
|V_{q,p}(0,z0+h)-V_{q,p}(0,z0)|
 <= S^(-2) sum_{k=1}^{376} |c_{q,k}|/4096^k.
```

The 13-check companion certificate proves the following strict rational comparisons:

| q | exact p-derivative at z0 | Taylor band error, strictly below | entire edge band |
|---|---|---:|---|
| 12 | -77040.007814... | 389 | partial_p V_12(0,z) < -76650 |
| 24 | -308045.118936... | 1554 | partial_p V_24(0,z) < -306490 |

These correct center derivatives are within the wider bounds recorded in PREFIX-659. Fractional diagnostics use an explicitly signed decimal formatter; finite rational inequalities are the actual proof.

To transfer the inequality to `p>0`, note that `f_n(k)=A_n(k)/binom(n,k)` lies in `[0,1]`, and the second difference in the Bernstein basis satisfies

```
|s_n''(p)|<=2n(n-1), for all p in [0,1].
```

The exact nonnegative two-clock moment kernels are bounded by 1 for `mu` and by `n+1` for `H`. Thus uniformly over the full square,

```
|mu_p| <= M1 = sum_{n=0}^{188} n = 17766,
|mu_pp|<= M2 = 2 sum n(n-1) = 4429656,
|H_pp| <= H2 = 2 sum n(n-1)(n+1) = 631225980.
```

Also `mu<=378`. Since `W=2H-mu^2`,

```
|W_pp|<=2H2+2M1^2+2(378)M2=5242533408.
|V_{q,pp}|<=q^2|W_pp|+q|mu_pp|
            <=3019805554752  (12<=q<=24).
```

Therefore, moving from `p=0` into the strip of width `2^-30` changes `V_{q,p}` by less than `3019805554752/2^30 <2813`.

Because `V_{q,p}/q=qW_p-mu_p` is affine in `q`, the two proven endpoint-slot inequalities imply

```
V_{q,p}(0,z)/q < -76650/12, for every 12<=q<=24.
```

Combining these estimates yields on all of `R`:

```
V_{q,p}(p,z)<-76650+2813<-73000.
```

Now integrate in `p` from 0 to the chosen `p`, and use PREFIX-660's uniform strong concavity `V_{q,zz}(0,z)<-12800000` for every real `q in [12,24]`. At its unique interior critical point `z_*(q)`, integration gives the claimed lower bound

```
V_q(0,z_*)-V_q(p,z)>73000 p + 6400000(z-z_*)^2
```

away from the maximizer; equality holds at `(0,z_*)`. This proves existence, uniqueness and quantitative stability on the closed two-dimensional strip.

## Evidence, provenance, remaining work

Executable certificate: `PREFIX661_R6_STRIP_CERTIFICATE.py`, **ALL_CHECKS_PASS 13**. JSON: `PREFIX661_R6_RESULTS.json`. It imports the sibling PREFIX660 exact survivor-row and centered-polynomial helpers. The polynomial and second-difference bounds are entirely rational/integer; no floating-point proof premises. The original 96-port dynamics were not rerun.

Required predecessor: PREFIX-660 at `research_notes/portable_direct/2026-11-10_prefix660_r6_moving_edge_maximum.md` and its exact certificate (read alongside this note); preceding model at PREFIX-659, commit `65536b12a268b619e0e1e89f685de3fb2162bea3`. All share the frozen scientific pin above. BRC interface: exact signed multiplicities, first-stop observer, Bernstein derivative structure (`COMPOSE_APPLIED`). This artifact is an independently testable author certificate but has not received independent mathematical review, formal Task Result, or Foundation admission.

**Next unit:** replace the conservative global second-derivative budget by local Bernstein-restricted mixed partial coefficients to enlarge the 2D strip, and compare its certified maximum against the remaining symmetry-reduced triangular chamber. The parent problem is still complete-domain maximization of the frozen observer.
