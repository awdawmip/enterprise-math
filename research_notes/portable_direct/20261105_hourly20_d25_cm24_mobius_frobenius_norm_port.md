# D25: CM(−24) quartic Frobenius–Möbius and norm-compressed first-jet certificate

Date: 2026-11-05. Scope: author-side portable exact algebra, not native H0/B0 experiment. Research lane: `chatgpt-research-hourly-enterprise-math-20260923`. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; original scientific input pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Author proof / finite exact check; UNREVIEWED / NOT_ADMITTED.

## 1. Exact Frobenius–Möbius theorem

Let (p\ge5) be prime with (p\equiv5\pmod8), and let
[
Q(t)=t^4-140t^3+294t^2-140t+1,qquad A_p=\mathbb F_p[t]/(Q).
]
The discriminant of (Q) is (2^{32}3^6), so its four roots are distinct for all these primes. In (A_p), set
[
I(t)=1/t,quad F(t)=\frac{5-7t}{7-5t},quad G(t)=\frac{7-5t}{5-7t}=I(F(t)).
]
These maps preserve the four roots and generate a transitive Klein four-group. Explicitly:
[
Q(F(t))=\frac{576Q(t)}{(5t-7)^4},\quad
Q(G(t))=\frac{576Q(t)}{(7t-5)^4}.
]
Both denominators are units on (Q=0) in characteristic (p\ge5). The exact Frobenius action is
[
\boxed{t^p=
\begin{cases}
F(t)&p\equiv13\pmod{24},\\
G(t)&p\equiv5\pmod{24}.
\end{cases}}
	ag{1}
]
The cross-multiplied, denominator-free certificates are
[
(7-5t)t^p-(5-7t)=0\quad(p\equiv13\pmod{24}),
]
[
(5-7t)t^p-(7-5t)=0\quad(p\equiv5\pmod{24}).
]

**Proof.** Over (mathbb Q(\sqrt2,\sqrt3)), the four roots of (Q) are the independent sign conjugates of
[
35+24\sqrt2+20\sqrt3+14\sqrt6.
]
The transformation (I) negates the (\sqrt3) and (\sqrt6) components; (F) negates the (\sqrt2) and (\sqrt6) components; (G=IF) negates (\sqrt2) and (\sqrt3). These identities follow by direct substitution (equivalently by the displayed polynomial transformations). For (p\equiv5\pmod8), ((2/p)=-1); furthermore ((3/p)=+1) for (p\equiv13\pmod{24}) and ((3/p)=-1) for (p\equiv5\pmod{24}). Applying Frobenius to the radical expressions establishes (1) for all four roots, and therefore in the étale quotient algebra. QED.

## 2. Inversion-covariant Hasse first-jet defect

Let (m=(p-1)/2=4q+2), and retain the original Legendre Hasse polynomial
[
H_p(t)=\sum_{k=0}^{m}\binom mk^2t^k.
]
The previous author-side three-band Hasse–Jacobi result identified the candidate split-class derivative equation
[
\boxed{C_p(t):=16t(1-t^2)H'_p(t)+(1+2t-7t^2)H_p(t)=0\quad(Q(t)=0).}\tag{2}
]
By binomial symmetry (H_p(1/t)=t^{-m}H_p(t)), differentiating gives, exactly after replacing (2m+1=p=0),
[
\boxed{C_p(t^{-1})=t^{-m-2}C_p(t)\quad\text{in }A_p.}\tag{3}
]

**All-or-none corollary (proved).** For every eligible prime, either (Q\mid C_p) in (mathbb F_p[t]), or (gcd(Q,C_p)=1). Indeed, (C_p) has coefficients in (mathbb F_p), so its zero set among the four roots is Frobenius-stable; (3) makes it inversion-stable. By (1), Frobenius together with inversion acts transitively on the four roots. Hence the zero set is either empty or all four. This strengthens the first-jet observer's branch accounting without presupposing that the split-class conjecture is true.

## 3. Two-coordinate norm compression (proved)

Since (m+2=4q+4), put (r=(m+2)/2=2q+2) and define
[
D_p(t)=t^{-r}C_p(t),\qquad y=t+t^{-1}.
]
Equation (3) gives (D_p(t^{-1})=D_p(t)). The fixed subalgebra of inversion in (A_p) is (mathbb F_p[y]), because (t
e t^{-1}) on (Q=0), and
[
\boxed{y^2-140y+292=0.}
]
Its discriminant (18432=2^{11}3^2) is a nonsquare modulo every prime (p\equiv5\pmod8). Thus this fixed subalgebra is the quadratic **field** (mathbb F_{p^2}). There are unique (d_0,d_1\in\mathbb F_p) with
[
\boxed{D_p=d_0+d_1y.}\tag{4}
]
Consequently the exact single-scalar test
[
\boxed{
Q\mid C_p
\quad\Longleftrightarrow\quad
d_0^2+140d_0d_1+292d_1^2=0\pmod p.
}\tag{5}
]
holds for **all** primes (p\ge5,\ p\equiv5\pmod8). The right side is (N_{\mathbb F_{p^2}/\mathbb F_p}(D_p)). A field norm is zero exactly for the zero element, so (5) is an equivalence, not a numerical heuristic.

For reproducible extraction, (t^{-1}=-t^3+140t^2-294t+140\pmod Q). Write the degree-≤3 representative (D_p=a_0+a_1t+a_2t^2+a_3t^3); then
[
d_1=-a_3,qquad d_0=a_0+140a_3
]
and the remaining coordinates satisfy (a_1=-293d_1, a_2=140d_1). This gives an exact BRC provenance-preserving two-coordinate observer: the four CM roots are retained via the étale algebra while the inversion-invariant defect is compressed with an explicit inverse/readout.

## 4. Executed finite exact test

The Python standard-library checker `d25_cm24_mobius_frobenius_20261105.py` was run locally. For every one of the 569 primes (5\le p\le20000, p\equiv5\pmod8), it evaluated in the exact quotient ring (A_p): the Frobenius identity (1), original binomial Hasse coefficients and derivative, inversion covariance (3), the unique two-coordinate extraction (4), and norm equivalence (5). All 569 passed. In the **finite tested sample only**, the split-class equation (C_p=0) held at all 281 primes (p\equiv5\pmod{24}), while all 288 inert-class primes had (C_p\ne0).

| prime | class | `d0` | `d1` | scalar norm |
|---:|---:|---:|---:|---:|
| 5 | split | 0 | 0 | 0 |
| 13 | inert | 1 | 10 | 12 |
| 29 | split | 0 | 0 | 0 |
| 37 | inert | 19 | 21 | 30 |
| 53 | split | 0 | 0 | 0 |
| 373 | inert | 239 | 40 | 332 |

Theorems (1), (3), the all-or-none corollary, and (4)–(5) have algebraic proofs. The **uniform** split-class vanishing of (5) remains open: the finite table and exact reduction do not prove it.

## 5. Source/observer boundary and next action

This is an auxiliary external elliptic-CM/Hasse first-jet calculation; it retains the chosen CM root, its reciprocal orbit and its first derivative as separate provenance. It is **not** a native P000 X6 transfer, nor the fixed 373 H0/B0 divided-power crystalline experiment. The current Source-native D25 checkpoint, signed odd Hesse/Green observation and the frozen \(\Delta_p-R_p\) task remain untouched.

**Smallest next mathematical unit:** seek a finite CM isogeny, WZ, Jacobi or coefficient argument proving the scalar norm in (5) vanishes for *all* (p\equiv5\pmod{24}). Its two-coordinate form is more compact than an unspecialized quartic first-jet equation, and the inert-class nonzero test remains an independent diagnostic. Subsequently connect a proved split-jet identity to the previously recorded (p^2) Jacobi–Green–Wronskian correction, then return to the frozen \(\Delta_p-R_p\) native comparison. Author result requires independent review before admission.

Sources: canonical Source continuation read `rhourly20-20261105-0048-current-cont-read` (SUCCEEDED, Source `d3f43d7a4721c7aa786f708d36b90d855990b960`), previous author-side note `research_notes/portable_direct/20261104_hourly20_d25_hasse_three_band_cm_selection.md`, and actual local exact checker. No native new CLAIM/OPEN/Source checkpoint is represented.
