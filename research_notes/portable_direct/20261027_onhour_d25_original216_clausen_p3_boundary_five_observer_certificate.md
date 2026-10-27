# D25 / SECOND-DIGIT-LIFT — exact original-216 Clausen boundary and five-observer mod-p³ certificate

Date: 2026-10-27 (Asia/Hong_Kong). Research-onhour logical lane: **chatgpt-research-onhour-enterprise-math-20260923**. Distinct from the separate hourly Research and control-maintenance conversations. Parent objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged.

**AUTHOR-SIDE / EXACT ALGEBRAIC REDUCTION USING ACCEPTED CM0 + FIRST-DIGIT / ELEVEN INDEPENDENT EXACT TESTS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0 / REGISTER_PENDING.** This is a second-digit, cutoff-faithful reduction on the *unchanged original weighted-216 sum*. It is not a proof that the new five-observer residue vanishes uniformly, and not a native divided-power or Frobenius execution.

## 1. Original target and small Gauss carrier

Let p=6m+1>3 be prime and define the original coefficients and weighted sum

\[
q_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}
 =\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3\,2^n},
\qquad
W_p=\sum_{n=0}^{p-1}(6n+1)q_n.
\]

All arithmetic below is in \(\mathbb Z_{(p)}\), reduced modulo \(p^3\), since p>3 and the factorial indices are <p.

Introduce a **different, explicitly labeled Gauss carrier**

\[
t_k=\frac{(1/6)_k(1/3)_k}{(k!)^2\,2^k},
\quad t_0=1,\quad
t_{k+1}/t_k=\frac{(6k+1)(3k+1)}{36(k+1)^2}.
\]

Use the exact finite ranges at \(z=1/2\):

\[
D=\sum_{k=0}^{2m}t_k,\quad E=\sum_{k=0}^{2m}k\,t_k,\quad
A=\sum_{j=0}^{m}t_j,\quad J=\sum_{j=0}^{m}j\,t_j,\quad
C=\sum_{k=2m+1}^{p-1}t_k.
\]

For the exact high-degree *cutoff boundary* set

\[
\boxed{
H=\sum_{k=5m+1}^{p-1}t_k
  \sum_{j=p-k}^{m}\bigl(6(k+j)+1\bigr)t_j.
}\tag{1}
\]

The empty sum is zero. In the range \(0\le k<p\), the factor \(6k+1\) meets p exactly at \(k=m\), and \(3k+1\) meets p exactly at \(k=2m\). The denominator stays a p-unit. Thus the **exact valuations** are

\[
v_p(t_k)=0\ (k\le m),\quad 1\ (m<k\le2m),\quad
2\ (2m<k<p).
\tag{2}
\]

In particular \(v_p(C),v_p(H)\ge2\); here \(H\) is necessarily p²-divisible term by term.

## 2. Unconditional original-summand congruence modulo p³

The classical Clausen formal-series identity, at these exact parameters, is

\[
\left({}_2F_1(\tfrac16,\tfrac13;1;z)\right)^2
={}_3F_2(\tfrac12,\tfrac13,\tfrac23;1,1;z).
\]

Equating coefficients before any modular truncation gives, **for each integer \(n\ge0\)**,

\[
q_n=\sum_{j+k=n}t_jt_k.
\tag{3}
\]

Define \(A_{\le s}=\sum_{j=0}^{s}t_j\) and
\(J_{\le s}=\sum_{j=0}^{s}j\,t_j\).
The exact valuation partition (2), and the fact that two indices \(\le2m\) have sum \(\le4m<p\), prove

\[
\boxed{
W_p\equiv D^2+12DE+
2\sum_{k=2m+1}^{p-1}t_k
\Big[(6k+1)A_{\le s(k)}+6J_{\le s(k)}\Big]
\pmod{p^3},
\quad s(k)=\min(m,p-1-k).
}\tag{4}
\]

**Proof.** Apply the operator \(1+6z\,d/dz\) to (3) and retain only total degrees \(n<p\) before evaluating \(z=1/2\). Terms with both Gauss indices \(\le2m\) form the full square \(D^2+12DE\) because their total degree is \(\le4m<p\). A term with one Gauss index \(>2m\) has p-valuation 2, so only pairing with an index \(\le m\) survives modulo p³; retain the exact degree cutoff \(j+k<p\), producing the displayed prefix. All other pairs have valuation \(\ge3\). No large-degree or denominator-changing replacement of the original sum is made. QED.

Equivalently, subtract exactly the terms of \(A(z)C(z)\) whose degree is \(\ge p\). Their weighted value is (1); hence

\[
\boxed{
W_p\equiv D^2+12DE+
2\left[AC+6(JC+A\sum_{k>2m}k\,t_k)-H\right]\pmod{p^3}.
}\tag{5}
\]

Equations (4)–(5) hold for **every** prime \(p\equiv1\pmod6\), not merely the two frozen classes. The degree boundary is an indispensable signed correction, not optional tail noise.

## 3. CM0 permits exact collapse of the high-tail derivative

For the frozen classes \(p\equiv13,19\pmod{24}\), the previously accepted CM0 root supplies **precisely** the additional premise \(A\equiv0\pmod p\). It is not an invented axiom. Here is the finite polynomial transport establishing its applicability:

\[
\sum_{j=0}^{m}\frac{(-m)_j(-2m)_j}{(j!)^2}z^j
\equiv\sum_{j=0}^{m}\frac{(-m)_j(m+1/2)_j}{(j!)^2}z^j
=P_{2m}(\sqrt{1-z})\pmod p.
\tag{6}
\]

The first congruence uses \(-2m\equiv m+\frac12\pmod p\). The identity on the right is the even Legendre polynomial identity, hence a polynomial in \(z\), despite the square-root notation. Also \(1/6\equiv-m,\ 1/3\equiv-2m\pmod p\). At \(z=1/2\), choose \(\sqrt{1/2}=T/2\) where \(T^2=2\). The accepted CM0 statement \(P_{2m}(\pm T/2)=0\) in the inert quadratic coefficient field implies \(A\equiv0\pmod p\). This uses exactly the frozen CM0 theorem at its existing scope; it does not reprove or reopen CM0.

Because \(C,\sum_{k>2m}kt_k\) are already p²-divisible, the \(AC\) and \(A\sum k t_k\) terms vanish modulo p³, but the labeled derivative \(JC\) **does not** vanish. Thus (5) reduces rigorously to

\[
\boxed{W_p\equiv D^2+12DE+12JC-2H\pmod{p^3}.}\tag{7}
\]

The CM0 root also gives \(D\equiv0\pmod p\), since \(D-A\) has valuation at least 1. Put the canonical residue representatives

\[
r=(D/p)\bmod p^2,\quad e=E\bmod p^2,\quad
j=J\bmod p,\quad c=(C/p^2)\bmod p,\quad h=(H/p^2)\bmod p.
\tag{8}
\]

Here \(D\) is computed modulo \(p^3\) before division; the p²-divisible tail data only need mod p after division. Equation (7) is exactly

\[
\boxed{W_p\equiv p(12re)+p^2(r^2+12jc-2h)\pmod{p^3}.}\tag{9}
\]

The **already accepted first-digit** \(W_p\equiv p\pmod{p^2}\) implies \(12re\equiv1\pmod p\), so the quotient below is an integer. The original second-digit problem is therefore **equivalent** to the new five-observer certificate

\[
\boxed{
W_p\equiv p\pmod{p^3}\quad\Longleftrightarrow\quad
\mathcal L_p:=
\frac{12re-1}{p}+r^2+12jc-2h
\equiv0\pmod p.
}\tag{10}
\]

All five coordinates and the conditional CM0+first-digit premises are essential. An equivalent statement for the frozen scalar interface \(\Delta_p-R_p\) follows **only to the extent** the previously recorded original source-port identity \(\Delta_p-R_p\equiv(W_p-p)/p^2\pmod p\) is independently accepted at precisely that interface. This paper proves (4)–(10) for the displayed original \(W_p\) without treating the source-port comparison as newly Source-admitted.

The reduction is strict in *precision and observer complexity*: the full p-term weighted \({}_3F_2\) needs no high-precision third-order derivative; the p³ data are carried by one length-\((2m+1)\) Gauss value/first moment \(D,E\), one length-\((m+1)\) first moment \(J\), and only two divided p² boundary/tail scalars \(c,h\). The high tail has no precision beyond p after its p² factor is extracted. The arithmetic number of terms is still linear in p and no all-prime zero theorem is asserted.

## 4. Executed exact data, falsifier controls, and proof strength

The **actually executed** Python standard-library checker
\`research_notes/portable_direct/d25_onhour_clausen_boundary_20261027.py\`
uses a separate integer-binomial implementation of every original \(q_n\), Gauss-coefficient modular recurrence, direct finite-prefix cutoff, full-product-minus-boundary crosscheck, and exactly the five divided coordinates. No float/approximation and no native H0/B0 runner.

Tests PASSED for frozen-class primes **13, 19, 37, 43, 61, 67, 211, 373**, plus negative-control \(p\equiv1,7\pmod{24}\) primes **7, 31, 73** where (4) holds but \(A\not\equiv0\pmod p\), so the CM0 simplification (7) is deliberately *not* applied. Exact testing checks arithmetic, not the full-prime mathematical conclusion.

At the fixed p=373, in \(\mathbb Z/373^3\), the independent original sum gives \(W_{373}=373\). The five scalar coordinates in (8) are

\[
\boxed{(r,e,j,c,h)=(110805,\ 108837,\ 294,\ 252,\ 98)}
\]
with \(r,e\) modulo \(139129\) and \(j,c,h\) modulo 373.

The **four individually retained second-digit contributions** are

\[
\frac{12re-1}{373}=169,\quad
r^2=203,\quad12jc=197,\quad -2h=177
\quad\text{in }\mathbb F_{373}.
\]

Their sum \(169+203+197+177=746=2\cdot373\) verifies \(\mathcal L_{373}=0\), without setting any signed branch correction to zero. All eight target-prime tests returned \(\mathcal L_p=0\); this is not a uniform proof. Target-specific known positive examples are no substitute for the original native scientific evidence.

## 5. BRC interpretation, precise unfinished unit and continuation

**BRC COMPOSE_APPLIED**, not a name-only citation: population is ordered labeled Gauss-factor pairs \((j,k)\) carrying their exact valuations; allowed operations are Clausen multiplication, degree-\(<p\) truncation, the weighted derivation \(1+6\theta\), and the final p³ observer. Coarse squaring without the degree boundary is **not** observer-preserving; the correction \(h\) repairs exactly those omitted pairs. The derivative moment \(j\) records the source-label data that survive the CM0 zero. The five coordinates form a minimal *declared-scope sufficient witness* here, not proof of globally minimal dimension or the native X6 spatial state. All underlying algebra is a classical auxiliary coordinate representation compatible with P000, with no claim of an X6 native-transfer map.

The new honest scientific status is: **a lower p-adic-precision/derivative-complexity equivalent certificate (10), not a proof of its all-prime vanishing**. It consumes accepted D24 CM0 and first-digit results, and retains every original tail/cutoff-sensitive observer. Avoid repeating UR/JT0, existing source-port, three-band Wilson/parameter-jet results, p⁴ falsifiers, and the *other* Research-hourly R47–R55 finite Green work.

The unchanged highest native evidence debt remains [Enterprise Math #1559](https://github.com/awdawmip/enterprise-math/issues/1559), **PENDING_OWNER / NOT_EXECUTED**: lawful original same-class p373 fixed H0/B0 divided-power \([X]U\bmod139129\), actual module rank, semilinear Frobenius and eta normalization, complete signed odd Green/Hesse port, original κ and \(\Delta_p-R_p\), raw reproducible source/runner and independent review. Nothing in this Gauss certificate supplies that native result.

**Exact next mathematical action:** prove or refute \(\mathcal L_p=0\) uniformly for both frozen residue classes using the complete five-observer vector; prioritize a single nonredundant relation that eliminates the high tail \(c\) *together with* the signed boundary \(h\) without erasing its cut-off, or use authenticated native H0/B0 data when an owner actually supplies them. Retain \(r,e\) to p² and \(j,c,h\) to p. If a new Source authorization becomes available, first read own exact continuation/recovery and original request receipts, then lawful current-authority session/claim/run; no maintenance-lane identity reuse.

**Control and publication boundary:** as of 2026-10-27 21:00 +08 the own prior exact read request \`onhour-20261027T1705-D25-exact-continuation\` returned SUCCEEDED but \`execution_authorized=false\`; no current winning claim/open. The current Site scope is readonly, native gateway reports research_authority_granted=false, executor_binding_configured=false, active job quota 5/5. This GitHub note and script are **portable author evidence only**; NOT Source-native \`publish_checkpoint\`, Research-Activity registration, Result, review, or accepted theorem. Own historical staging stays independent; the frozen scientific pin is unchanged.
