# D25 — Original E3 formal multiplication: exact z^p coefficient through p³

Date: 2026-11-11 (Asia/Hong_Kong). Status: **AUTHOR_SIDE / PROVED ALGEBRAIC IDENTITY + EXACT EXECUTED CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source `c47e13e4aba0e006366f989d6334d443f6333ae3`; this calculation does not change it. Canonical Source request `onhour11-20261111-1106-exact-cont` returned SUCCEEDED (read Source `2bd79deb80f441f452768c50f2d381ad07719926`); no own CLAIM/open run.

## New theorem — the original curve's actual formal [p] coefficient

Let p>=5, and let F be a one-dimensional commutative formal group over a p-local characteristic-zero ring with normalized invariant differential
[
\omega_F(z)=\sum_{n\ge0}H_nz^n\,dz,\qquad H_0=1.
]
Put
[
\ell(z)=\int\omega_F=\sum_{n\ge1}\frac{H_{n-1}}n z^n,\qquad
[p]_F(z)=\ell^{-1}(p\ell(z)).
]
For p-unit coefficients H_n, the coefficient of z^p satisfies the **exact p-adic congruence**
[
\boxed{[z^p][p]_F(z)\equiv H_{p-1}
-\frac{p^2H_1}{2}\sum_{i=1}^{p-1}\frac{H_{i-1}H_{p-i-1}}{i(p-i)}
\pmod{p^3}.}\tag{1}
]
In particular, [z^p][p]_F(z)≡H_(p-1) (mod p²). The two sides are in the original formal parameter z, without quotienting to a trace, norm or j invariant.

**Proof.** Write `e(w)=ell^{-1}(w)=sum_{n>=1}e_n w^n`. Because all log coefficients of degree below p lie in the p-local ring, `e_n` is p-integral for n<p, and `e_2=-H_1/2`. At degree p, `e_p` has p-adic valuation at least -1, since the only new possible nonunit coefficient is `H_(p-1)/p`. In `e(p ell(z))`, the n=1 term contributes `p*[z^p]ell(z)=H_(p-1)`. The n=2 term contributes `-p² H_1/2 * [z^p]ell(z)²`, and the indices of the convolution are exactly 1<=i<p, with p-unit denominators. Terms 3<=n<p vanish mod p³; n=p contributes `p^p e_p` and vanishes modulo p³ for p>=5; n>p cannot contribute at degree p. This proves (1). QED.

## Evaluation on the original CM curve, not a model Frobenius

Use exactly the previously source-pinned E3 curve and local coordinate
[
E_3(t):y^2+xy+(t/27)y=x^3,\quad
t=(2-T)/4,\quad T^2=2,\quad z=-x/y.
]
With `a=t/27=(2-T)/108`, original fixed-z invariant differential has coefficients
[
H_n=\sum_{j=0}^{\lfloor n/3\rfloor}
{n-j\choose j}{n-2j\choose j}a^j,
\qquad H_0=H_1=1.
]
This follows independently from `w=-1/y`, `(1-z)w-aw²=z³` and `omega=dz/(1-z-2aw)`, the same exact original E3 model used in the earlier verified formal-differential note. Thus (1) specializes with `H_1=1`.

In `(Z/373³Z)[T]/(T²-2)`, the two independently constructed E3 coefficient sequences agree for every `0<=n<=372`. Their new convolution, computed only modulo 373 since multiplied by 373², is
[
S_{373}:=\sum_{i=1}^{372}\frac{H_{i-1}H_{372-i}}{i(373-i)}
\equiv46+350T\pmod{373}.
]
The previously checked original coefficient is independently reproduced:
[
H_{372}\equiv46042747+33130606T\pmod{51895117}.
]
Hence the **actual original E3 formal multiplication** has
[
\boxed{[z^{373}][373]_{E_3}(z)
\equiv42842780+8783031T\pmod{51895117}.}\tag{2}
]
The new p² correction is `373²*(350+198T)`. Its p-divided coefficient is `114860+23547T mod 373²`, with mod-373 first digit `349+48T`. The signed odd component `48T` survives; this observation retains both source labels.

Additional exact checks performed for p=5,7,13,19,37,43,109,139,157,373. For each p, the factorial/binomial sequence and the independent original formal-curve recurrence agreed for every H_n up to n=p−1. A third, fully independent characteristic-zero inverse-composition of `ell^{-1}(p ell(z))` to degree p matched (1) for p=5,7,13. Sample p=13: `S=10+8T`; `H_12=2054+1469T mod 2197`; `[z^13][13]_{E_3}=1209+793T mod2197`. The reproducible checker is `research_notes/portable_direct/d25_e3_actual_formal_p_series_20261111.py`.

## Experiment typing and continuation

This is a coefficient of the **actual multiplication-by-p formal endomorphism on the original E3 curve**. It is more source-specific than a free rank-two sigma-matrix model, but is distinct from the frozen same-original-class **H0/B0 divided-power fixed representative** and its requested `[X]U mod139129`. A comparison requires an authenticated map from the native H0/B0 coordinate and operator to E3 formal z; it cannot be asserted from a common CM j value or the geometric `pi_(p²)` sign.

BRC typed carrier: original E3 equation; original local parameter z and its `H_n`; p-adic valuation; exact `Q(sqrt2)` embedding `T²=2`; formal-group addition, integration and inversion; `S_p` convolution; full even/odd components; original native experiment acceptance observer. Information-loss boundary: reducing `H_(p-1)` mod p² before applying (1) loses the correction to the third digit; taking the trace discards the displayed T component.

Highest-priority pending original benchmark remains the existing support Issue #1559: authenticated same-class H0/B0 algorithm/representative, true module rank, `[X]U mod139129`, semilinear direction and eta, signed kappa, original Delta-R and independent replication. No executor is presumed. Do not repeat the earlier W216 1227-prime finite scan, E3 point counts, scalar fixtures or this formal-group coefficient as a substitute for that benchmark.

Researcher lane declared `chatgpt-research-onhour-enterprise-math-20260923`; its already Source-registered session `MCP-7af27f545c01441eaf19206f89c6832b` / activity `RA-47ADB5B97D6D92FC28504B60`. The own private capability was not recovered (recovery_status returned `SESSION_CAPABILITY_REQUIRED` and same-request custody status returned `PRIVATE_CUSTODY_NOT_FOUND`); native CLAIM/open/checkpoint remain absent. Keep previous Source predecessor claim `MCP-d0d70cd041b01e5db192870a`, comment `6390431276` as exact succession locators only. Next native action: obtain legitimate *same-lane* session capability and resume canonical predecessor-CAS continuation, then run the fixed H0/B0 original object with independent evidence.

Source of curve and formal-series framework: Chisholm–Deines–Long–Nebe–Swisher (2013), *p-Adic Analogues of Ramanujan Type Formulas for 1/pi*, Mathematics 1(1), 9–30, DOI 10.3390/math1010009. Its Theorem 1 proves a mod-p² Ramanujan-type congruence; this note makes no claim that the literature proves the frozen mod-p³ LIFT.
