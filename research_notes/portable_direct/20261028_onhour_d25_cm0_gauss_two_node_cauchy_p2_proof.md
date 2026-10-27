# D25/SECOND-DIGIT-LIFT — Gauss–Legendre two-node proof of the target Cauchy second-digit congruence

**Date:** 2026-10-28 Asia/Hong_Kong. **Logical Research lane:** `chatgpt-research-onhour-enterprise-math-20260923` (not maintenance or the other research lane). **Mother:** `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. **Task:** `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`. **Publication:** `TP2-B6F4FC938FF94941C1B7`. **Frozen scientific Source pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged.

**Author-side status:** A NEW ALL-TARGET-PRIME CONDITIONAL-ON-ACCEPTED-CM0 ALGEBRAIC PROOF, exact finite-field checks performed, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This discharges the *auxiliary Cauchy* \(\mathcal T_p=6\) obligation in both frozen target classes. It is **not** a Source-native Result, **not** a proof of the higher \(W_p\equiv p\pmod{p^3}\) LIFT, and **not** execution of the original H0/B0 divided-power benchmark.

## 1. Exact consumed inputs; no repeated predecessor work

Let \(p=6m+1\) be prime, \(n=2m=(p-1)/3\), and work over \(k=\mathbb F_p\). Retain the original signed coefficients, cutoff and moment:

\[
t_j=\frac{\binom{2j}{j}^2\binom{3j}{j}}{216^j},\quad
f_j=(6j+1)t_j,\quad
u_s=\frac{8^s}{(2s+1)\binom{2s}{s}},\quad
\mathcal T_p=\sum_{j=0}^{n}f_j\sum_{s=0}^{j-1}u_s\in k.
\]

The already established Clausen and quadratic-Legendre transports are consumed at their actual mod-p observer scope:

\[
A_m(z)=\sum_{j=0}^{m}\binom mj\binom{2m}j(z/2)^j,\quad
A_m(z)^2=\sum_{j=0}^{n}t_jz^j,\quad
A_m(2(1-x^2))=P_n(x),
\]
\[
F_m(z)=(1+6z\partial_z)A_m(z)^2,\quad
q_m(z)=\frac{F_m(1)-F_m(z)}{1-z},\quad
\mathcal T_p=\int_0^1 q_m(2(1-x^2))\,dx.
\]

Here \(P_n\) is the ordinary even Legendre polynomial; the integral is the *finite coefficient functional* \(\int_0^1x^jdx=1/(j+1)\) on the polynomial degrees used, with no analytic approximation. The earlier onhour exact bridge (commit `5ef218482be024c01d4be19bd4a0e4a6fd9c7f36`) proves this finite identity; its inverse-binomial normalization erratum is retained.

**Only inherited CM0 input:** the already accepted original E3 Hasse zero for the target primes \(p\equiv13,19\pmod{24}\): for \(T^2=2\) and \(c=(2-T)/108\), \(H_p(\sigma(c))\equiv0\pmod p\), with exact coefficient identification \(H_p(C)=P_n(1-54C)\pmod p\). Thus for \(\alpha=-T/2\), \(\alpha^2=1/2\) and \(P_n(\alpha)=0\). Since \(P_n\) is even, both \(\pm\alpha\) are roots. The polynomial \(D(x)=2x^2-1\) therefore divides \(P_n(x)\) in \(k[x]\). **The accepted CM0 is cited as a premise, not re-proved or silently broadened.**

## 2. New theorem (all p in either frozen target class)

\[
\boxed{\mathcal T_p=6\pmod p\quad\text{for every prime }p\equiv13,19\pmod{24}.}\tag{G1}
\]

In fact the same conclusion holds for any \(p=6m+1\) where \(D\mid P_{2m}\); this conditional variant makes the exact dependency visible.

**Proof.** Let \(P=P_n\), \(R=P/D\in k[x]\), and \(V=P'/x\in k[x]\). Here \(n=2m\) is even, so \(P,V,R\) are even; \(\deg R=n-2\). Under CM0, \(A_m(1)=P(\alpha)=0\), hence \(F_m(1)=0\). The previously proved signed quotient formula specializes *as a polynomial identity* to

\[
\begin{aligned}
Q_p(x)&:=q_m(2(1-x^2))\\
&=\frac{-P(x)^2+3(1-x^2)(P(x)^2)'/x}{D(x)}\\
&=\boxed{-P(x)R(x)+6(1-x^2)R(x)V(x)}.
\end{aligned}\tag{G2}
\]

All degrees in (G2) are at most \(2n-2=4m-2<p-1\), so the finite integration functional has unit denominators. Classical Legendre orthogonality remains valid over \(k\), because its coefficientwise rational proof uses only denominators less than \(p\). In particular, since \(\deg R<n\),

\[
\int_{-1}^{1}P(x)R(x)\,dx=0.\tag{G3}
\]

Define the even polynomial \(h(x)=(1-x^2)R(x)V(x)\), of degree \(\le2n-2\). The *exact n-node Gaussian quadrature identity* is valid over an algebraic closure of \(k\) at this degree:

\[
\int_{-1}^{1}h(x)\,dx
=\sum_{P(a)=0}\frac{2h(a)}{(1-a^2)P'(a)^2}.\tag{G4}
\]

For clarity, (G4) does not require real-order, positivity or numerical integration. In characteristic \(p\), \(n<p\), \(2n<p\), and the Legendre ODE forces all roots of \(P\) to be simple: no root is \(\pm1\), and a common zero of \(P,P'\) away from \(\pm1\) forces all derivatives through order \(n\) to vanish since their factorials are \(p\)-units, contradicting \(P(1)=1\). Thus the Lagrange quadrature construction works. Its weights follow directly from the Christoffel–Darboux identity and \((1-a^2)P'(a)=nP_{n-1}(a)\) at \(P(a)=0\):

\[
\frac1{P'(a)}\int_{-1}^{1}\frac{P(x)}{x-a}\,dx
=\frac{2}{nP_{n-1}(a)P'(a)}
=\frac{2}{(1-a^2)P'(a)^2}.
\]
The required Legendre recurrences, norms and orthogonality involve denominators \(\le2n+1<p\), so these field identities have no hidden bad denominator.

At every root \(a\ne\pm\alpha\), \(D(a)\ne0\) and \(R(a)=P(a)/D(a)=0\), hence \(h(a)=0\). At each of the **two distinguished roots** \(a=\pm\alpha\), whose squares equal \(1/2\), differentiation of \(P=DR\) gives

\[
R(a)=\frac{P'(a)}{4a},\quad V(a)=\frac{P'(a)}a,\quad
h(a)=\frac{(1-a^2)P'(a)^2}{4a^2}=\frac{P'(a)^2}{4}.
\]

The corresponding quadrature weight is \(4/P'(a)^2\), so **each root contributes exactly 1**. Therefore \(\int_{-1}^1 h=2\). Since \(h\) is even, \(\int_0^1h=1\). Combining (G2), (G3) and the already proved moment bridge:

\[
\boxed{\mathcal T_p=\int_0^1Q_p=-\int_0^1PR+6\int_0^1h=6.}
\]
This is an all-prime proof under the declared accepted CM0 input. QED.

## 3. Actual consequence and sharp scope boundary

The preceding all-prime second-digit reflection theorem (commit `0da414086b6f2c60f531423b1e490a6b8adb1de6`) states

\[
2S_{p-1}\equiv\chi_2W_{p-1}+p(\mathcal T_p-3)\pmod{p^2}.
\]

For the two target classes, \(\chi_2=(2/p)=-1\) and the previously accepted first-digit UR gives \(W_{p-1}\equiv p\pmod{p^2}\). Substitution of the **now-proved** (G1) yields

\[
\boxed{S_{p-1}\equiv p\pmod{p^2}\quad(p\equiv13,19\pmod{24}).}\tag{G5}
\]

Thus the target-class case of the *auxiliary finite Cauchy conjecture* is settled within the previously accepted CM0/UR dependencies. It **does not** prove the distinct frozen original LIFT/JT2, equivalent to \(W_{p-1}\equiv p\pmod{p^3}\); neither result provides the required original H0/B0 coefficient or full native Frobenius operator. Nor does this prove the split-character conjecture \(\mathcal T_p=0\) for \(p\equiv1,7\pmod{24}\): there \(D\nmid P\) in the checked controls, and (G4) cannot be used with the same reduction.

The BRC information audit is **COMPOSE_APPLIED**: carrier labels \((p,j,s,t_j,6j+1,u_s,\mathrm{cutoff},\mathrm{CM0\ root\ branch})\), exact operations Clausen → Legendre → polynomial division → finite-field quadrature, and observer only \(\mathcal T_p\bmod p\) with its Cauchy \(S\bmod p^2\) consequence. The signed coefficients, both roots/branch multiplicity, index limits, source provenance and residual \(\Delta_p-R_p\) are not erased. The auxiliary one-variable polynomial is **not** a native X6 coordinate or physical calculation.

## 4. Exact executable checks (separate from proof)

Companion `research_notes/portable_direct/d25_legendre_gauss_quadrature_cm0_20261028.py` was actually run using Python standard-library integer arithmetic. For \(p=13,19,37,43,61,67,211,373\), it independently computes \(P\), exact division \(P/D\), \(P'/x\), the **original nested signed** \((j,s)\) sum, and the two integration components. In all eight instances: `D remainder=0`, `integral P·R=0`, `integral h=1`, `original T=6`. At \(p=373\), \(n=124\) and \(373^2=139129\), the same tuple passes. Control primes \(p=7,31\), outside the CM0 classes, have nonzero remainders \(2,21\) respectively. The execution ends `PASS_D25_CM0_GAUSS_TWO_NODE_FULL_TARGET_CLASS_PROOF_GUARD`. No Lean theorem checker or native H0/B0 program was run; the proof is mathematical, not exhaustive finite enumeration.

## 5. Immutable scientific and control continuation

- **Mother/Task/publication:** as in heading. **Frozen pin:** `c47e13e4aba0e006366f989d6334d443f6333ae3`, unchanged.
- **Newly completed author-side unit:** Gauss–Legendre characteristic-p two-node proof of \(\mathcal T_p=6\) and auxiliary \(S_{p-1}\equiv p\pmod{p^2}\) in *both* target classes, conditional on the explicitly inherited accepted CM0 and first-unit UR. Independent formal review/admission remains OPEN.
- **Do not redo:** D24 CM0, first-digit UR, earlier Cauchy boundary/R2/Clausen/Legendre bridges, bulk prime scans, or the author-side Gauss polynomial reduction.
- **Highest unchanged native evidence debt:** `awdawmip/enterprise-math#1559` — authorized original-class H0/B0 divided-power experiment at \(p=373\), true \([X]U\bmod139129\), actual module rank and semilinear Frobenius direction/\(\eta\), signed odd Green/Hesse, original \(\kappa\), and \(\Delta_p-R_p\), with independent source-pinned reproducible raw output. No native execution is claimed; ownership remains pending unless separately verified.
- **Open mathematics:** original all-prime \(W_{p-1}\equiv p\pmod{p^3}\) / \(\Delta_p-R_p=0\) proof or falsifier (not the now-closed target auxiliary \(\mathcal T=6\) problem). Precise next science action is the *original frozen* third-digit signed-cutoff/CM interface, with no change of object.
- **Role/receipt isolation:** use Research logical ID above only. Historical bridge recovery in `awdawmip/kimi-query-bridge#6575` is a local session pointer, not a current winning CLAIM. Dispatch #6576 terminated FAILED/TimeoutExpired; successful older exact continuation did not authorize execution. Site `em_status` observed on 2026-10-28 still has `research_authority_granted=false`, `executor_binding_configured=false`, active native jobs 5/5. No session/claim/open/Source checkpoint/Result/review attempted here; the 3 preserved legacy staging records remain distinct. Status `AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`. Resume protected work only upon current exact Source authorization and same-subject claim verification; unknown requests reconcile by original ID.
