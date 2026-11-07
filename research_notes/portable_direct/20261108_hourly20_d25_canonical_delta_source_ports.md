# D25 — Canonical Delta_p divided second digit via native 216 Gauss source ports

Date 2026-11-08, lane chatgpt-research-hourly-enterprise-math-20260923 (not maintenance), TASK_RESEARCH author-side portable, UNREVIEWED / NOT_ADMITTED; native session/claim/run not verified. Parent Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3, taskbook blob 53a3ef039325534e3715add837f0eee332289984.

This unit directly targets the frozen scalar
\[
\Delta_p=(G_p h-1)/p,\qquad G_p=g/p,\quad
g=\sum_{n=0}^{p-1}B_n,\quad
h=\sum_{n=0}^{p-1}(12n+1)B_n,
\]
with \(B_0=1\) and \(B_{n+1}/B_n=(6n+1)(3n+1)/(36(n+1)^2)\), exactly as fixed in the accepted parent research return. The *second-digit objective* is \(\Delta_p-R_p=0\bmod p\), NOT an unconstrained second-order relation between the auxiliary A/B models.

## Exact source-resolved formula (PROVED, conditional only on the accepted first-digit UR)

Put \(m=(p-1)/6,\ x=1/2,\ Q(z)=\sum_{n=0}^m\binom mn\binom{2m}n z^n\). Reuse the previously **proved coefficientwise** A-Gauss port theorem for the actual \(p\)-term Gauss polynomial \(g(z)=\sum_{n<p}(1/6)_n(1/3)_n z^n/(n!)^2\):
\[
g(z)=Q(z)+pP(z)+p^2S(z)\pmod{p^3},\qquad
P=L+T,\quad S=S_0+S_1+S_2.
\]
Here \(Q,L,T,S_0,S_1,S_2\) are source-labelled explicit binomial/factorial/harmonic polynomials from the same snapshot, **not** freely chosen corrections. Evaluation at \(x=1/2\) is over \(\mathbb Z_{(p)}\). Define
\[
Z=\frac{Q(x)+pP(x)}p\bmod p^2,\quad
H_0=(1+12D)Q(x)\bmod p^2,\quad
H_1=(1+12D)P(x)\bmod p,\quad D=z\partial_z.
\]
The CM0 input makes the \(Z\) numerator divisible by \(p\). The accepted UR first digit implies \(ZH_0\equiv1\bmod p\), so the following integer/p-adic divided residue is defined:
\[
\boxed{\displaystyle
\Delta_p\equiv
\frac{Z H_0-1}{p}+S(x)H_0+Z H_1\pmod p.}\tag{D25-SOURCE-DELTA}
\]

**Complete proof:** By the exact coefficientwise expansion, \(G_p=g(x)/p\equiv Z+pS(x)\pmod{p^2}\). Applying the original, fixed weighted observer \(1+12D\) BEFORE the quotient gives
\(h\equiv H_0+pH_1\pmod{p^2}\). Multiply:
\(G_ph\equiv ZH_0+p(SH_0+ZH_1)\pmod{p^2}\).
Accepted UR makes \(ZH_0-1\) divisible by \(p\); subtract 1 and divide by \(p\). No auxiliary B-model, hypothetical Fricke coefficient lift, or approximation enters.

Consequently the **original frozen LIFT is exactly equivalent**, at its own prescribed observer and without asserting its truth, to
\[
\boxed{\frac{ZH_0-1}{p}+S H_0+Z H_1-R_p=0\pmod p.}\tag{D25-CERT}
\]
This is a source-typed equal-complexity reformulation / concrete algebraic certificate, not yet a demonstrated strictly lower-complexity certificate or an all-prime proof. It carries \(R_p\) as the original frozen symbolic target and does not fill its value from numerical \(\Delta_p\).

## Independent exact finite check

A standard-library checker calculates \(Z,H_0,H_1\) from the explicit binomial/harmonic first-lift ports, \(S\) from the independently verified low, one-zero, and two-zero coefficientwise second-lift ports, and computes \(g,h\) **again** via the original recurrence at precision \(p^3,p^2\). For all 94 target primes \(p<2500\), direct \((g/p)h\) and (D25-SOURCE-DELTA) give the same divided second digit.

| p | \(\Delta_p\) | \((ZH_0-1)/p\) | \(S H_0\) | \(Z H_1\) |
|---:|---:|---:|---:|---:|
| 13 | 0 | 0 | 9 | 4 |
| 19 | 12 | 16 | 11 | 4 |
| 43 | 15 | 16 | 0 | 42 |
| 67 | 21 | 41 | 27 | 20 |
| 373 | 196 | 81 | 12 | 103 |

All numeric entries are modulo their row prime. At \(p=373\), the retained A-side second-order source is \(S=288\), with \(Z\bmod p=24\), \(H_0\bmod p=171\), \(H_1\bmod p=82\). Thus \(81+288\cdot171+24\cdot82=196\bmod373\). Replacing the weighted observer \(1+12D\) by the unweighted value, or forgetting \(ZH_1\), changes the actual \(\Delta\) certificate.

## Information-loss audit and next exact unit

The carrier is \((Q,L,T,S_0,S_1,S_2;Z,H_0,H_1;R_p)\), with retained rational/integer lifts and original 216 coefficient source. The observer is \(\Delta_p-R_p\bmod p\), which first requires \(g\bmod p^3\), \(h\bmod p^2\), p-division, then multiplication. A coarse \(g/p\bmod p\) readout cannot preserve \(ZH_0/p\). This is COMPOSE_APPLIED reuse of existing BRC source typing, not a new accepted theorem or P000 change.

The remaining scientific target is now the exact (D25-CERT) sum. Retrieve the frozen explicit \(R_p\) functional from the original parent interface with its provenance, and attack its relation to the three displayed source terms at p=19 and p=373, then universally. Exact 94-prime agreement with \(\Delta\) does **not** test \(\Delta-R\) independently and does not close LIFT or JT2. The original native p373 H0/B0/divided-power/Hesse-kappa benchmark #1559 is still pending and is not replaced by this external number-theoretic calculation.

Original native same-lane request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 remained WAITING_RESOURCE/EVENT_COLLECTION_IO with no verified own-session CLAIM/open/checkpoint. One earlier reconcile returned QUEUED, then the continuation resource wait recurred; preserve original requests and UNKNOWN old session/staging. Support owner #1558.