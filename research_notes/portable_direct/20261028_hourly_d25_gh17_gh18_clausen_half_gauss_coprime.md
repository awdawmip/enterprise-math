# D25/LIFT GH-17 / GH-18 — Clausen half-degree factorization and transversal roots

Status: `AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING / SYNC_DEBT`.

2026-10-28. Author-side auxiliary scalar mathematics; **not** a native task Result, Driver review, or formally authorized Source checkpoint. Research lane's historical logical conversation ID: `chatgpt-research-hourly-enterprise-math-20260923`; separate from `chatgpt-hourly-enterprise-math-20260921` (maintenance). Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; mother objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`, OPEN. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` retained without change.

## Previous precise input

Reuse GH-16's finite obstruction polynomial (project commit `6cd1699501c7a63844809607730f2e32677f39fb`):

\[
\mathcal H_d(z)=\sum_{r=0}^{d}(8r+5)z^r\frac{(3/4)_r^3}{r!(5/4)_r(3/2)_r},\quad p=4d+3.
\]

In the GH-15/GH-16 Laurent problem the coefficient of the genuine second-order polar term was shown to be
\(A_0=\alpha_p z^{2d+2}\mathcal H_d(z)/(z-1)\). The goal \(\mathcal H_d(9)=0\) is an **unproved general conjecture**. The finite rank parameter and these polynomial observers are not native six-dimensional X6 spatial coordinates or original W/S/Hasse sources.

## GH-17 — exact factorization in characteristic p

**Theorem.** Let \(p=8m+3\ge11\) be prime, \(k=\mathbb F_p\), and \(d=2m\). Set

\[
F_m(z)=\sum_{r=0}^{m}\frac{(-m)_r^2}{(2m+2)_r\,r!}z^r\in k[z],\qquad G_m(z)=16zF_m'(z)+5F_m(z).
\]

All denominators are nonzero in \(k\). Then

\[
\boxed{\mathcal H_{2m}(z)=F_m(z)G_m(z)\quad\text{in }k[z].}
\tag{GH-17}
\]

**Proof.** Apply the terminating Clausen formula over \(\mathbb Q\):

\[
 {}_2F_1(a,b;a+b+\tfrac12;z)^2
={}_3F_2(2a,2b,a+b;2a+2b,a+b+\tfrac12;z)
\]

with \(a=b=-m\). Both sides are polynomials of degree at most \(2m\). Since \(p=8m+3\), in \(k\) we have

\[
 -m=3/8,\quad -2m=3/4,\quad -4m=3/2,\quad \tfrac12-2m=5/4=2m+2.
\]

Their terminating numerator and denominator factors up to degrees \(m\) and \(2m\), respectively, are \(p\)-integral with unit denominators. Reduction therefore gives the *exact polynomial identity*

\[
F_m(z)^2=\sum_{r=0}^{2m}\frac{(3/4)_r^3}{r!(5/4)_r(3/2)_r}z^r.
\]

Apply \(8z\,d/dz+5\), and use the product rule:
\((8z\partial_z+5)F_m^2=F_m(16zF_m'+5F_m)\). This proves GH-17. This is not a global conversion of original W/S sources. QED.

## GH-18 — coprimality and simple roots

**Theorem.** For the same \(p,m,F_m,G_m\):

\[
\begin{aligned}
 64z(1-z)F_m''+(80-112z)F_m'-9F_m&=0,\\
 16zF_m'&=G_m-5F_m,\\
 \boxed{16z(1-z)G_m'=(7z+1)G_m+(z-5)F_m.}
\end{aligned}
\tag{GH-18a}
\]

\(F_m\) is squarefree and \(\gcd(F_m,G_m)=1\). Every root of \(G_m\) outside \(z=5\) is simple. If \(G_m(5)=0\), then its multiplicity is exactly two. Specifically, for the obstruction's special parameter

\[
\boxed{\mathcal H_{2m}(9)=0\ \Longrightarrow\ \mathcal H'_{2m}(9)\neq0.}
\tag{GH-18b}
\]

Whenever \(\mathcal H_{2m}(9)=0\), exactly one of the two Gauss channels \(F_m(9),G_m(9)\) vanishes and it vanishes to first order. The theorem does **not** assert the existence of that zero for all primes.

**Proof.** \(F_m={}_2F_1(-m,-m;2m+2;z)\) satisfies the terminating Gauss hypergeometric differential equation. In \(k\), \(-m=3/8\) and \(2m+2=5/4\), so it becomes the first displayed equation. Differentiate \(G_m=16zF'_m+5F_m\) and substitute for \(F''_m\); a direct rearrangement yields GH-18a.

\(F_m(0)=1\). Chu–Vandermonde for this terminating polynomial gives

\[
F_m(1)=\frac{(3m+2)_m}{(2m+2)_m}\neq0.
\]

Every factorial factor in that expression is a unit because \(p=8m+3\) and the largest numerator factor is \(4m+1<p\). Suppose \(\alpha\notin\{0,1\}\) is a root of multiplicity \(q\ge2\) of \(F_m\). Since \(q\le m<p\), comparing the lowest nonzero Taylor coefficient in the ODE gives \(\alpha(1-\alpha)q(q-1)=0\), contradiction. Therefore \(F_m\) is squarefree. If \(F_m(\alpha)=G_m(\alpha)=0\), then \(\alpha\ne0\) and \(G_m(\alpha)=16\alpha F'_m(\alpha)=0\), again a contradiction. Hence the factors are coprime.

At \(\beta\) with \(G_m(\beta)=0\), \(G_m(0)=5\ne0\), while the ODE at \(z=1\) yields \(8G_m(1)=4F_m(1)\ne0\). For other roots, GH-18a gives

\[
G_m'(\beta)=\frac{(\beta-5)F_m(\beta)}{16\beta(1-\beta)}.
\]

Thus every root except possibly \(5\) is simple, since \(F_m(\beta)\ne0\). If \(G_m(5)=0\), then also \(G_m'(5)=0\). Differentiating GH-18a at \(5\) gives \(-320G_m''(5)=F_m(5)\ne0\), so its multiplicity is exactly two (\(2!,320\) are units at every stated prime).

Finally \(9\notin\{0,1,5\}\) in \(k\). If \(F_m(9)=0\), then \(G_m(9)=144F_m'(9)\ne0\); if \(G_m(9)=0\), then \(G_m'(9)=4F_m(9)/[16\cdot9(1-9)]\ne0\). Thus any zero of \(F_mG_m=\mathcal H_{2m}\) at \(9\) is simple. QED.

## Precisely bounded numerical evidence

Ran companion Python standard-library script: `gh17_18_clausen_gauss_check.py` with exact modular integer arithmetic (no floating point). It printed:

```
PASS_GH17_EXACT_CLAUSEN_FACTOR_AND_COUPLED_ODE
PASS_GH18_COPRIME_ROOT_AND_Z9_TRANSVERSALITY
range: primes 11 <= p < 10000, p % 8 = 3: 310
finite observed split: F9=0 on p%24=19: 155; G9=0 on p%24=11: 155; exceptions: 0
exact full coefficient and every z in F_p: p < 1000
```

For 43 primes below 1000, it separately reconstructed *all coefficients* of \(\mathcal H_{2m}\), checked the factor identity, and checked the differential transport for every residue \(z\in\mathbb F_p\). For 310 primes below 10000, all special-point values and derivatives were checked. The split pattern (F-root for \(19\pmod{24}\); G-root for \(11\pmod{24}\)) is **finite observation, not a universal proof**.

## Scope, persistence, and continuation

BRC interface reuse: `REUSE_APPLIED` GH-16 polynomial and exact finite coefficient carrier; `COMPOSE_APPLIED` Clausen factor plus two-channel differential observer. Preserve \((p,m,z)\), factors \(F_m,G_m\), their derivatives and source rank, finite boundary, observer operations, original Hasse/W/S labels and valuations. No projection from these auxiliary scalar equalities to the Heartbeat World's native discrete six-dimensional X6 Cell dynamics is claimed.

Control-state evidence: earlier research recovery https://github.com/awdawmip/kimi-query-bridge/issues/6622 and exact continuation https://github.com/awdawmip/kimi-query-bridge/issues/6623; support https://github.com/awdawmip/enterprise-math/issues/1558. Those are historical and do not grant current ownership. On this run, gateway `em_status` reported version `0.6.11`, `research_authority_granted=false`, `executor_binding_configured=false`, `CODE_REVIEW_REQUIRED`, native active-job quota `5/5`. No native winning CLAIM/OPEN/run or Source checkpoint is proven. Prior session `MCP-06f7ad61a8d841d9ba1ba1ef4d088d94` remains historical, not successor authorization. No service mutation was submitted. Project remote write was attempted through the connected GitHub tool but blocked at host safety admission, followed by readback showing both intended remote paths absent. **This locally mounted proof and the executable program are the actual portable evidence, not a GitHub publication or Research-Activity registration.** Status `SYNC_DEBT`.

**Next smallest scientific unit:** prove or refute \(F_{(p-3)/8}(9)=0\) uniformly for primes \(p\equiv19\pmod{24}\), using a finite-field cubic/CM transformation, period-character sum, or prime-parameter WZ certificate. Separately characterize \(G_m(9)=0\) for \(p\equiv11\pmod{24}\). Do not infer either from finite checks. If the F-branch is proved, insert \(A_0=0\) into GH-15 and study its remaining \(B L\) term before returning to \(T_p=0\), GH-5/GH-10 next-digit moments and original R23/R36 source-faithful finite Green coupling. Native H0/B0, [X]U mod p^2, Frobenius eta/kappa, real p=373 native experiment, and independent Driver review remain OPEN. No scheduler or notification configuration was changed.
