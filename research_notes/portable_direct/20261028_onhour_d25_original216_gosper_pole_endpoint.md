# D25/LIFT — original 216 rational-Gosper no-go, finite-field pole cost and exact p-adic endpoint

At: 2026-10-28 17:00 Asia/Hong_Kong.
Status: **AUTHOR-SIDE / EXACT ALL-PRIME ALGEBRAIC NO-GO AND BOUNDARY IDENTITIES / 13 EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_EXECUTED.**

Mother objective: \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`; task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; last known publication \`TP2-B6F4FC938FF94941C1B7\`. Ordinary-control Research logical lane \`chatgpt-research-onhour-enterprise-math-20260923\`, separate from maintenance. **Frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged.** The project P000 and ACTIVE Heartbeat X6 six-axis Cell/worldview are starting constraints; the present single integer index is an **external scalar arithmetic observer**, not a native X6 axis, plane, H0/B0 operator or full state.

## 0. Consumed sources; exact unfinished target

Original weighted-216 model, without changing the cutoff or weight:

\[
t_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\quad
w_n=(6n+1)t_n,\quad W_p=\sum_{n=0}^{p-1}w_n.
\]

For \(p\equiv13,19\bmod24\), the original D25 LIFT target remains \(W_p\equiv p\bmod p^3\), with the separately pinned \(\Delta_p-R_p\) source interface. Reuse the prior exact \(p\)-valuation bands, reflected middle/high unit law, Clausen/Legendre source ports and accepted D24 UR/CM0; do not recredit their proofs. This work consumes the previous p-adic upper-tail observation \(\nu_p(t_{p-1})=3,\ t_{p-1}/p^3\equiv-1\bmod p\). Methodological comparison: the other hourly lane's GH-11/GH-12 pole-orbit analysis concerns a *different* auxiliary \(C_r\) coefficient; nothing below identifies its scalar with original \(t_n\).

## 1. Theorem A — no characteristic-zero rational single-term antidifference

Define
\[
a(x)=(2x+1)(3x+1)(3x+2),\qquad b(x)=36(x+1)^3,
\]
so \(t_{n+1}/t_n=a(n)/b(n)\) exactly.

**For every \(R(x)\in\mathbb Q(x)\)**, the rational identity
\[
a(x)R(x+1)-b(x)R(x)=b(x)(6x+1) \tag{G}
\]
is impossible.

**Proof by a finite-pole orbit.** Suppose \(R\) has a nonempty finite pole set in \(\mathbb C\). At a pole with *largest real part* \(\alpha\), \(R(x+1)\) has no pole at \(x=\alpha\), so (G) forces \(b(\alpha)=0\), hence \(\alpha=-1\). At a pole with *smallest real part* \(\beta\), \(R(x)\) has no pole at \(x=\beta-1\); (G) forces \(a(\beta-1)=0\), hence \(\beta\in\{1/2,2/3,1/3\}\). This contradicts \(\operatorname{Re}\beta\le\operatorname{Re}\alpha\). Thus \(R\) is a polynomial.

For a nonzero polynomial of degree \(d\), the leading coefficient of \(a(x)R(x+1)-b(x)R(x)\) is \(-18\operatorname{lc}(R)x^{d+3}\), while the RHS has degree four. Thus \(d=1\). Write \(R(x)=Ax+B\). Degree-four and degree-three coefficients force \(A=-12,\ B=4\). But direct integer expansion gives the **nonzero residual**
\[
\boxed{a(x)(4-12(x+1))-b(x)(4-12x)-b(x)(6x+1)
=-4(66x^2+113x+49).}\tag{A}
\]
This completes the rational-function impossibility proof. The result rules out an exact one-index rational Gosper antidifference; it does not rule out character sums, p-dependent multisource WZ, nonlocal CM or a native computation.

## 2. Theorem B — original-index finite-field global pole lower bound

For every prime \(p=6m+1>3\), if \(R\in\mathbb F_p(x)\) solves (G) as a **global rational identity** and \(R=P/Q\) is reduced, then
\[
\boxed{\deg Q\ge 2m=\frac{p-1}{3}.}\tag{B}
\]
No solution is asserted to exist.

**Proof.** A polynomial solution is impossible: the degree and coefficient calculation above works in characteristic \(p>3\), and \(66x^2+113x+49\) is not the zero polynomial modulo any prime \(p>3\) since \(\gcd(66,113,49)=1\). Thus \(R\) has a pole over \(\overline{\mathbb F}_p\).

Translation \(x\mapsto x+1\) forms cycles of length \(p\). If the poles contain a whole cycle, \(\deg Q\ge p\). Otherwise take one maximal noncyclic consecutive run of poles \(z,z+1,\ldots,w\). At its left end, \(a(z-1)=0\), hence \(z\in\{1/2,2/3,1/3\}\), all inside \(\mathbb F_p\); at the right end, \(b(w)=0\), hence \(w=-1\). The three forward distances modulo \(p=6m+1\) are respectively \(3m-1,4m-1,2m-1\). The run contains at least \(2m\) distinct poles. This proves (B), including any poles on algebraic extension cycles. At \(p=373\), any such rational global certificate needs **at least 124 denominator poles**. This is a lower bound on this exact search route, not a lower bound on all possible proofs.

## 3. Theorem C — exact finite endpoint decomposition and mandatory p-local repair

Put \(g(n)=66n^2+113n+49\), \(R(n)=4-12n\). Equation (A) implies the *exact rational termwise identity*:
\[
\boxed{(6n+1)t_n=R(n+1)t_{n+1}-R(n)t_n+
\frac{g(n)}{9(n+1)^3}t_n.}\tag{C1}
\]
Therefore, for **every** integer \(N\ge0\),
\[
\boxed{\sum_{n=0}^N w_n=R(N+1)t_{N+1}-4+
\sum_{n=0}^N\frac{g(n)t_n}{9(n+1)^3}.}\tag{C2}
\]
This is a true source-preserving sum identity, not the sought supercongruence.

At \(N=p-1\) and \(p\ge5\), every residual summand is \(p\)-integral. The exceptional last denominator \((n+1)^3=p^3\) is repaired by the actual **original coefficient** \(t_{p-1}\in p^3\mathbb Z_{(p)}\). Do not use a modular inverse of \(p\). The preexisting exact Wilson result gives
\[
\boxed{\frac{g(p-1)t_{p-1}}{9p^3}\equiv-\frac29\pmod p.}\tag{C3}
\]

Using the classical Wolstenholme–Ljunggren congruences \(\binom{2p}p\equiv2,\ \binom{3p}p\equiv3\pmod{p^3}\) for primes \(p\ge5\), the distinct upper boundary is
\[
t_p=\binom{2p}p^2\binom{3p}p 216^{-p}
\equiv12\cdot216^{-p}\pmod{p^3}.
\]
Consequently \(R(p)t_p\equiv+2/9\pmod p\). The two separately labelled endpoint contributions cancel **modulo \(p\)**:
\[
\boxed{R(p)t_p+\frac{g(p-1)t_{p-1}}{9p^3}\equiv0\pmod p.}\tag{C4}
\]
Their cancellation is not an assertion about the interior sum at \(p^3\).

Define the new explicitly typed residual observer
\(S_p=\sum_{n=0}^{p-1}g(n)t_n/[9(n+1)^3]\in\mathbb Z_{(p)}\). Then (C2) is the genuine uniform \(p^3\)-precision transport
\[
\boxed{W_p\equiv(4-12p)\,12\cdot216^{-p}-4+S_p\pmod{p^3}.}\tag{C5}
\]
For the frozen target classes, the **still-unproved** LIFT is equivalent to
\[
\boxed{S_p\stackrel{?}{\equiv}
p+4-(4-12p)\,12\cdot216^{-p}\pmod{p^3}.}\tag{C6}
\]
This reformulation isolates a non-Gosper interior observer with a precisely controlled, nonzero upper endpoint. It cannot be proved by asserting a polynomial antidifference or discarding the \(n=p-1\) branch.

## 4. Executed exact certificate

The Python **standard-library-only** checker \`research_notes/portable_direct/d25_original216_gosper_pole_endpoint_guard_20261028.py\` was actually run. It compares independently (i) original integer-binomial coefficients and (ii) the forward hypergeometric recurrence at every \(n<p\); verifies the exact rational-polynomial defect by five evaluations (degree at most four), the finite-field pole distances, independently evaluates \(t_p\), computes the upper \(n=p-1\) residual by **exact integer division by \(p^3\)**, and checks (C2), (C3), (C4) modulo \(p^3\). All 13 tested primes \(5,7,11,13,19,31,37,43,61,67,73,211,373\) passed. Marker:

\`PASS_D25_ORIGINAL216_GOSPER_POLE_BOUNDARY 13 exact primes\`.

Fixed \(p=373\), modulus \(373^3=51895117\), yields independently:
\[
\begin{aligned}
W_{373}&=373,\\
t_{373}&=30221434,\\
R(373)t_{373}-4&=36526933,\\
S_{373}&=15368557,\\
\text{last residual at }n=372&=15368180
\end{aligned}
\quad(\bmod 51895117).
\]
Thus \(36526933+15368557\equiv373\bmod51895117\). The degree-bound witness is \(\deg Q\ge124\). Finite original target checks are **not** proofs of the target for all primes.

## 5. BRC/source boundary and next action

**BRC REUSE_APPLIED:** retain the integer index, signed \(6n+1\), original \(t_n\), source-wise rational residue \(g(n)\), \(p\)-valuations, characteristic, \(p\)-local endpoint divide, pole orbit and observer \(W_p\bmod p^3\). The exceptional original \(n=p-1\) residual and the \(t_p\) boundary are distinguishable; they may cancel only at the proved modulus \(p\). The scalar reduction has no certified preservation of the actual H0/B0 divided-power module, native Frobenius, odd signed Green/Hesse, \(\kappa\) or complete native X6/heartbeat update.

**Native priority remains unchanged:** \`awdawmip/enterprise-math#1559\` was read OPEN/unassigned at the current run; the original fixed \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), actual module rank, true semilinear direction/eta, signed odd Green/Hesse, same-definition \(\kappa,\Delta_p-R_p\), raw code and source pin still require a genuine authorized native executor. This one-step rational no-go is a proof-search discriminator, never a substitute experiment.

**Actual recovery/authority:** original logical research bridge #6575 is an old local ACTIVE session pointer with \`source_authority_verified=false\`, zero own runs and zero own winning claims; original #6576 ended FAILED/TimeoutExpired. Current Site v0.6.11 reports \`research_authority_granted=false\` and \`write_relay_enabled=false\`. One bounded exact continuation attempt in this run returned \`CONTROL_QUOTA\`; no new dispatch/request replay, CLAIM/open, Source checkpoint, Result, review or borrowed identity occurred. The three historical neutral staging items remain independently sourced.

**Next specific mathematical action** only if a lawful canonical portable continuation permits it: derive an **independent** special-value/character-sum evaluation of \(S_p\) in (C6) or a genuine falsifier, preserving the \(p\)-integral upper endpoint; do not rerun low-complexity Gosper searches or recredit D24/earlier GH. Native #1559 remains the highest scientific evidence obligation, with an actual owner still to be established. D25/LIFT/JT2 remains OPEN; Source pin and P000 untouched.