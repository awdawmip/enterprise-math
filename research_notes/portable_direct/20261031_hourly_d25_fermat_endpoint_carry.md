# D25/LIFT — exact factorial endpoint and Fermat-quotient carry for every prime

2026-10-31 | Portable TASK_RESEARCH author derivation, not independent review or native execution. Stable research logical conversation: \`chatgpt-research-hourly-enterprise-math-20260923\`. Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`, publication \`TP2-B6F4FC938FF94941C1B7\`. Frozen scientific Source \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. P000 ACTIVE_LOCKED unchanged. Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Exact original endpoint identity

Let \(p\ge5\) be prime, \(a_n=\binom{2n}{n}^2\binom{3n}{n}/216^n\), and \(\mathsf{E}_p=a_{p-1}/p^3\in\mathbb Z_{(p)}\). Denote \(\mathsf{q}_{216}(p)=(216^{p-1}-1)/p\), the integer Fermat quotient. The p-stripped factorial decomposition gives the following **exact rational identity** (all products over positive integers, with empty products equal to one):

\[
\boxed{
\mathsf{E}_p =
\frac{2}{(p-1)^2(p-2)\,216^{p-1}}
\left(\prod_{r=1}^{p-2}(1+\frac{p}{r})\right)
\left(\prod_{r=1}^{p-1}(1+\frac{p}{r})\right)
\left(\prod_{r=1}^{p-3}(1+\frac{2p}{r})\right).
}\tag{1}
\]

Proof: write \(a_{p-1}=(2p-2)!(3p-3)!/[((p-1)!)^5\,216^{p-1}]\). Factor the unique p from the first numerator factorial and p, 2p from the second. Split remaining products into the three displayed shifted factorial blocks. After cancellation the residual rational prefactor is exactly \(2/((p-1)^2(p-2))\), giving (1). No modular approximation enters here.

## General all-prime endpoint carry theorem

Let \(M_1=-18a_1(a_{p-1}/p^3)=-\mathsf{E}_p\) because \(a_1=1/18\). The previous all-prime reciprocal mirror proves \(M_1\equiv1\bmod p\), so the endpoint carry \(\mathsf q_p=(M_1-1)/p\bmod p\) is defined.

In (1), finite harmonic sums modulo p satisfy
\[
H_{p-1}\equiv0,\quad H_{p-2}\equiv1,\quad
H_{p-3}\equiv\tfrac32.
\]
The product of the three shifted blocks therefore equals \(1+p(1+0+2\cdot\tfrac32)\equiv1+4p\bmod p^2\).
Also
\[
\frac{2}{(p-1)^2(p-2)}\equiv-1-\tfrac52p,\quad
216^{-(p-1)}\equiv1-p\mathsf q_{216}(p)\pmod{p^2}.
\]
Thus
\[
\boxed{
-\frac{a_{p-1}}{p^3}\equiv
1+p\left(\frac{13}{2}-\mathsf q_{216}(p)\right)\pmod{p^2},
\qquad
\mathsf q_p\equiv\frac{13}{2}-\mathsf q_{216}(p)\pmod p.
}\tag{2}
\]
All denominators are p-local units for p≥5. This is an all-prime algebraic theorem, not a scan-based conjecture.

## Composition with the preceding tail transport

The prior (this same research lane, separately credited) second-digit reciprocal transport for \(h=\lfloor(p-1)/3\rfloor\) and \(1\le k\le h\) is
\[
M_k\equiv1+p(\mathsf q_p+H_k)\pmod{p^2},
\quad
H_k=\sum_{j=2}^{k}\left(\frac2{2j-1}+\frac3{3j-1}+\frac3{3j-2}-\frac3{j-1}\right).
\]
Combining (2) removes the high-index endpoint as an opaque input:
\[
\boxed{
-18k^3a_k\frac{a_{p-k}}{p^3}
\equiv1+p\left(\frac{13}{2}-\mathsf q_{216}(p)+H_k\right)
\pmod{p^2}.
}\tag{3}
\]

A second independent simplification concerns the terminal source of the original third-order Clausen differential operator,
\[
E_p=-\frac{(2p-1)(3p-2)(3p-1)}{36}\frac{a_{p-1}}{p^3}.
\]
Substitution of (2) into the previously established two-wall formula gives
\[
\boxed{
E_p\equiv-\frac1{18}+
\frac{p\,\mathsf q_{216}(p)}{18}
\equiv-\frac1{18\cdot216^{p-1}}\pmod{p^2}.
}\tag{4}
\]
Hence the terminal source requires only the original fixed-normalization Fermat quotient, while the initial wall still carries the genuinely distinct harmonic path \(H_h\). Keep these as separate BRC ports and do not collapse them into a total-only scalar.

## Executed exact verification

A genuinely executed independent standard-library Python verifier, \`research_notes/portable_direct/d25_endpoint_fermat_quotient_check_20261031.py\`, compares (i) p-stripped direct factorials, (ii) the exact three-product endpoint, (iii) the explicit Fermat quotient formula, (iv) terminal-source congruence, plus six exact \`fractions.Fraction\` checks of (1) and nine direct integer-binomial anchors. Executed for **428 primes 5≤p≤3000**, including **221 primes p≡5 mod6**, and **207 primes p≡1 mod6**, all PASS; marker \`PASS_D25_ENDPOINT_FERMAT_QUOTIENT_ALL_PRIMES_EXACT\`. Actual script SHA256 \`397759ff4da47a040510931a4d0677042af7816a189fc8fcc24b59402d5fccaa\`; Git blob \`002387d824dcf3e0a3e069011b56e63c8ff95693\`; actual execution log SHA256 \`da588753a3f64f4c15e782e3ec0f68755420c8372f3a661d60c82941cfe5b377\`. Anchors (p,q_p,q216,E_p): (5,2,2,13), (11,8,4,36), (17,14,1,33), (23,8,10,336), (373,170,23,108688), (1327,993,1004,563164). Numbers reused at 373/1327 verify the new formula; not new exceptional-prime discoveries.

## Provenance, observer and open target

This is a new exact endpoint/normalization theorem and its **composition** with the preceding second-digit mirror, not independent reproduction of that mirror. BRC COMPOSE_APPLIED: preserve p, endpoint p³ division, Fermat quotient, harmonic path, initial/terminal wall, original 216 and signed source index. The exterior p-adic argument does not prove a native P000 X6 bridge.

Frozen D25/LIFT remains to prove the complete original \(\boxed{C+L-J+I\equiv0\pmod p}\) for every \(p\bmod24\in\{13,19\}\), hence the original 216 weighted sum \(A_p\equiv p\bmod p^3\). Next science unit: seek finite WZ/CM identity coupling original low/middle signed strata to the \(H_h\) and \(\mathsf q_{216}(p)\) ports; distinguish normalization effects from genuine cancellation. No native H0/B0, divided-power, semilinear Frobenius, Lean check, Result or independent review was performed.

At the present 2026-10-31 Gateway 0.6.11 read, \`research_authority_granted=false\`, \`executor_binding_configured=false\`, quota 5/5, \`CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED\`. The own 2026-10-25 recovery and continuation receipts #6424/#6425 are historical read-only evidence and authorize no current run. Native recovery assigned to Enterprise Math #1558 and native 373 experiment #1559. Protected staging, session, maintenance conversation and scheduled-task settings unchanged.
