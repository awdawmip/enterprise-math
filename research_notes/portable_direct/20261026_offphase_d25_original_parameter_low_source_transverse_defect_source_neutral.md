# D25/LIFT — original-series low-source transverse J defect beyond the diagonal observer

2026-10-26. **SOURCE-NEUTRAL / AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_SOURCE_CHECKPOINT.**

Frozen Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; mathematical Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` **unchanged**. This paper does **not** recredit the genuine bivariate Ward master `20261026_hourly_d25_bivariate_master_ward_r13.md`, the existing signed 3+2+1 genuine-face counterexample `20261026_offphase_d25_genuine_signed_ward_diagonal_kernel_source_neutral.md`, or the exact original-parameter scalar bridge `20261026_hourly_d25_original_parameter_diagonal_source_bridge_r15.md`. The incremental output is a **source-selective low-parameter response formula and two exact original-coefficient nonzero witnesses**, not another diagonal scalar proof.

## Original ordered source and exact defect

For prime `p=6m+1>=7`, let `R=Z_(p)`, `L=1-2m`, `N=2m-1` and use the existing genuinely source-labelled corrected-Clausen family
[
f_k(z)=\frac{(-m-z)_k(-2m-2z)_k}{(1-p/2-3z)_k k!},\quad 0\le k<p.
]
For the real finite carrier `1<=j,ell<=2m`, `ell-j=n`, set
[
A_n(x,y)=\sum f_j(x)f_{p-\ell}(y),\quad
B_n(x,y)=\sum j f_j(x)f_{p-\ell}(y),\quad
Y_n=B_n-\frac{p-n}{2}A_n.
]
The genuine lower-Hasse `k-1/k-2` source `J_n`, **not** a freely chosen model, is the one extracted from the published rank recurrence. Its eight terms collect exactly to
[
J_n(x,y)=3(x+y)(B_n-B_{n+1})-3y(p-n)A_n
+[4mx+(14m-3n)y+2(x^2-y^2)]A_{n+1}.
]
By substituting the actual `Y` and `p=6m+1`, this inherited source obeys the algebraic re-expression
[
\boxed{J_n=3(x+y)(Y_n-Y_{n+1})+(x-y)D_n,}
]
[
\boxed{D_n=\frac32(p-n)A_n+
\left(\frac{3n}{2}-5m+2(x+y)\right)A_{n+1}.}\tag{1}
]
These equations are exact rational formal-series identities on the **actual constrained ordered Hasse source**, not universal results inferred from samples. The diagonal `x=y` kills `(x-y)D_n`, as already implied by the previous bivariate master. It does **not** kill the subsequent low-source derivative: `\partial_x[J_n-3(x+y)(Y_n-Y_{n+1})]_{x=y=t}=D_n(t,t)`.

## New original-parameter-normalized observation

Freeze the high input at `y=theta=-p/6` but vary the low input `x`. The previously published exact original coefficient identification says
[
f_k(\theta)=\frac{(1/6)_k(1/3)_k}{(k!)^2}=2^k r_k,\qquad
\frac{r_{k+1}}{r_k}=\frac{(6k+1)(3k+1)}{36(k+1)^2}.
]
For `2m<k<p`, the same exact original source has `v_p(f_k(theta))=2`; set the p-local **unit** `beta_k=f_k(theta)/p^2`. Thus the real normalized low-high mass
[
V_n^0=\frac{A_n(\theta,\theta)}{p^2}
=\sum_{\ell-j=n}f_j(\theta)\beta_{p-\ell}
]
is exactly the carrier of the existing original-series scalar bridge, not newly manufactured data. Because the high factor is frozen and divisible by `p²`, `A_n(x,theta)/p²`, `Y_n(x,theta)/p²` and `J_n(x,theta)/p²` are regular p-local germs near `x=theta`.

Divide (1) by `p²` **only after** this exact tail divisibility. Differentiating with respect to the low parameter yields the following **new explicitly typed defect**:
[
\boxed{
\mathfrak D_n=
\left.\frac{d}{dx}\left[
\frac{J_n(x,\theta)-3(x+\theta)(Y_n(x,\theta)-Y_{n+1}(x,\theta))}{p^2}
\right]\right|_{x=\theta}
=\frac32(p-n)V_n^0+
\left(\frac{3n}{2}-5m-\frac{2p}{3}\right)V_{n+1}^0.}\tag{2}
]
It is an **authentic original-coefficient low-source sensitivity** outside the diagonal observer. It is not the full original `Q_p` and not a native elliptic/Frobenius derivative. At `n=0`, since every displayed denominator is a `p`-unit,
[
\boxed{\mathfrak D_0\equiv-5m V_1^0\pmod p.}\tag{3}
]
For all target primes `-5m` is a unit. Formula (3) does *not* assert `V_1^0` is nonzero for every prime.

The two exact original-series counterexamples to **a blanket claim of source-sensitive diagonal sufficiency** are:

| p | V_1^0 (mod p) | mathfrak D_0 (mod p) | mathfrak D_0 (mod p^3) |
| ---: | ---: | ---: | ---: |
| 13 | 9 | **1** | 443 |
| 733 | 513 | **61** | 91625794 |

For p13, `(-5m)V_1=3*9=1 mod 13`; for p733, `(-5m)V_1=123*513=61 mod 733`. At p733 an auxiliary geometric Ward scalar was previously resonant, but the separately typed original-parameter low-source derivative remains nonzero. This does not prove that all other Hasse/J/E/infinity/high-high sources fail to cancel in the final D25 target.

## Reproducible checks and exact next scientific unit

An **actually executed** Python stdlib integer checker used original Pochhammer products with denominator 18, higher-precision moduli `p^5`, certified exact `p²` high-tail division, and the real ordered `(j,ell)` population. An independent computation propagated the dual-number derivative of `f_j(x)` from its rational ratio (without dividing by a zero numerator), differentiated the authentic full `J_n/p²` source and subtracted the differentiated diagonal-compressed part. It matched (2) modulo `p³` for both `n=-1,0` at **10 primes p=7,13,19,31,37,43,61,67,73,733 — 20 comparisons PASS**. A complementary actual-Hasse coefficient checker also checked **264 genuine Ward source cells, 132 diagonal-degree equalities and 44 transverse contrasts** at p13,p19,p31 and selected p733 seam ranks. These are **author-side exact checks**, not independent mathematical review, formal acceptance or native CM experimentation. The universal identity (2) follows from the displayed algebra and exact factor valuation, not finite extrapolation.

BRC/进取坐标: `COMPOSE_APPLIED` to the actual ordered finite source carrier, source labels, p-adic valuation, and a declared future low-source derivative. The diagonal is a valid observer **only** for its already established scalar interface. These are external formal-rank/parameter coordinates, not physical native X6 axes or automatic three-dimensional-slice results; locked P000 is unchanged.

**Next smallest scientific unit:** insert (2) into the existing signed 3+2+1 original-source Ward interface; trace genuine separately labelled J/E finite faces, positive-infinity source and ordered high–high contribution and decide, by an exact source-preserving computation, whether this specific residual cancels under the *complete allowed output observer*. Do not re-prove the already published r13 bivariate master, r15 original diagonal Q, or earlier UR portable mathematics. Original-class H0/B0, [X]U mod p², semilinear Frobenius eta/kappa, comparison to Delta_p-R_p, native experiment and independent Driver review remain OPEN.

**Native control boundary:** This neutral GitHub storage is not a new Source checkpoint, predecessor completed_units, CLAIM, OPEN, Research-Activity registration, Result, review or theorem admission. Current authenticated Site reports `research_authority_granted=false`, `static_machine_readonly`, `write_relay_enabled=false`; exact continuation returned `CONTROL_QUOTA`, own checkpoint list `ACCESS_DENIED`. Source ownership conflicts remain handled by enterprise-math Issue #1558; no denied mutation, old session or request has been replayed. UR V2 original four-file 94,687-byte source and expected SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` remain **unrecovered**; upload pointers are not persistent Source bytes. If a future continuation seed is `CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS`, inputs must be completely read back and predecessor completed_units remains `[]`. The research scheduler/notifications were not modified.
