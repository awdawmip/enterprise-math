# D25 — Forced Gauss Wronskian with one Cartier integration constant

2026-11-07 · TASK_RESEARCH author-side · **EXACT FINITE-FIELD THEOREM / EXECUTED SYMBOLIC CERTIFICATES / UNREVIEWED / NOT_ADMITTED**. Research logical lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 excluded. Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Sources and definitions

Consume the hourly20 independent two-endpoint normalized Gauss forced ODE at commit 69f820fb2bcd8673f6bff8eb390526783059daab, and the same-lane reflected BRC prefix-jet calculation at the preceding author-side commit 10635cfb1086d1c59ba7ca61a03a6f87c6744a5e. This is a new algebraic consequence; it neither repeats the earlier ODE nor adopts another lane's identity.

Let p≡13,19 (mod24). Work in F_p[z] with L=θ²-z(θ+a)(θ+b), θ=z d/dz. In the A stream p=6m+1, (a,b)=(1/6,1/3), h=2m+1, and Q_A=Σ_(i=0)^m binom(m,i)binom(2m,i) z^i. In B, p=8k+3 or 8k+5, h=3k+2, (a,b)=(1/8,3/8) or (5/8,7/8), Q_B=Σ_(i=0)^k binom(k,i)binom(3k+1,i)z^i. Let R be the respective *existing normalized p² Gauss tail* in degrees h,...,p-1. Then LQ=0 and LR=λz^h+μz^p, where

\[
(\lambda,\mu)_A=\left({(-1)^m\over18\binom{2m}m},-{1\over18}\right),
\quad
(\lambda,\mu)_B=\left(-{3\over64\binom{3k+1}k},-{3\over64}\right).
\]

The B5 Euler (1-z) factor remains a separately typed source when moving from these Gauss streams to the full 2304 model.

## Theorem — one Cartier scalar in the forced Wronskian

Let r be the integer representative of a+b modulo p: r=(p+1)/2 for A or B3, r=(p+3)/2 for B5. Define H=(1-z)^(r-1),

\[
J(z)=z(1-z)^r\bigl(QR'-Q'R\bigr),\qquad
F(z)=H(z)Q(z)\left(\lambda z^{h-1}+\mu z^{p-1}\right).
\]

Then exactly in F_p[z],

\[
\boxed{J'(z)=F(z),\qquad [z^{p-1}]F(z)=0.}\tag{1}
\]

Moreover deg(J)<2p and deg(F)<2p-1. Define the *canonical non-Cartier primitive*

\[
I(z)=\sum_{\substack{0\le n<2p-1\\n\ne p-1}}
{[z^n]F(z)\over n+1}\,z^{n+1}.
\]

The denominators occurring here are nonzero in F_p. There is exactly one c_p in F_p satisfying

\[
\boxed{J(z)=I(z)+c_pz^p,\qquad c_p=[z^p]J(z).}\tag{2}
\]

For any x∈F_p\{0,1} satisfying Q(x)=0, this yields the *exact* derived derivative readout

\[
\boxed{(xQ'(x))R(x)=-{I(x)+c_px\over(1-x)^r}.}\tag{3}
\]

Proof. In ordinary derivatives, Ly=z²(1-z)y''+z[1-(1+a+b)z]y'-abzy. Therefore T=QR'-Q'R satisfies z(1-z)T'+[1-(1+a+b)z]T=Q(LR)/z. Multiplication by the characteristic-p integrating factor (1-z)^(r-1) gives (1). Since the coefficient of z^(p-1) of any formal polynomial derivative vanishes, [z^(p-1)]F=0. One can also check directly: H Q has degree p-h with leading coefficient -μ/λ, so the lower injection λz^(h-1) cancels the upper μz^(p-1) at degree p-1. Because deg J<2p, the polynomial kernel of d/dz in this degree range consists of constants and multiples of z^p. J(0)=I(0)=0, proving unique (2). Evaluating J at Q(x)=0 and using x^p=x gives (3). QED.

The constant c_p is a particular characteristic-p Wronskian/Cartier integration constant, *not yet identified* with the Dwork unit root or the Fricke full-series homogeneous normalization.

## Independent exact computational checks

The companion standard-library Python checker reconstructs Q and normalized R independently from the factorial recurrences, multiplies polynomials over F_p, and checks every coefficient of J'=F, [z^(p-1)]F=0, and J-I=c_pz^p. It additionally checks the CM-root instance (3) at x=1/2 for A, x=1/9 for B. Executed and **PASS** for each of A/B at p=13,19,43,67,373.

| p | c_A | c_B | (xQ'_A)R_A | (xQ'_B)R_B |
| ---: | ---: | ---: | ---: | ---: |
| 13 | 2 | 0 | 4 | 7 |
| 19 | 14 | 11 | 10 | 9 |
| 43 | 22 | 15 | 11 | 11 |
| 67 | 54 | 50 | 21 | 56 |
| 373 | 355 | 150 | 234 | 319 |

At p=13 the two source-normalized terminal charges have the same form, but the extracted Cartier scalars are distinct, c_A=2 and c_B=0. This is a discriminating exact witness against identifying the two homogeneous constants solely from the common terminal charge. Source-labeled lower injections, the Euler flag, and the Fricke pullback must be included in any proposed bridge.

## Continuation

Combine this newly computed c_A/c_B port with the source-preserving projected-overflow E_A/E_B and the known nonzero lower-source mismatch. Seek a Fricke gauge/adjoint identity for (G_A-G_B)/p²+E_A-E_B mod p at 13,19,43,67,373. The mother W_p=p mod p³ for p≡13,19 mod24 and the independent original p373 H0/B0 divided-power/Frobenius/Hesse κ benchmark with independent review (#1559) remain outstanding.

Original native request onhour11-20261106-1400-exact-research-lane-continuation preserved. Read-only native result at 2026-11-07T13:05Z was BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE, operation_sent=false, while Site remained CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. Prior receipt: QUEUED / EVENT_COLLECTION_IO / Error. No native session/CLAIM/run/checkpoint/Result/admission verified; REGISTER_PENDING / SYNC_DEBT. No mutation replay or maintenance-lane action.
