# D25 — Discriminating the derivative-ratio Fricke second-digit lift

Date: 2026-11-08. TASK_RESEARCH author-side portable; no native Researcher authority; UNREVIEWED / NOT_ADMITTED. Logical lane: chatgpt-research-hourly-enterprise-math-20260923 (not CONTROL_PLANE_MAINTENANCE). Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Exact question

The preceding certified port expansion establishes
\[
G_X/p\equiv (Q_X+pL_X+pT_X)/p+p(S_{0,X}+S_{1,X}+S_{2,X})\pmod{p^2}.
\]
The onhour companion first-digit research defines \(J_X=(zQ_X')|_{x_X}\) and signed Fricke coefficients
\[
(t_0,r_0)=
\begin{cases}
(J_A/(6J_B),\ 2/9)&p\equiv19\bmod24,\\
(-J_A/(8J_B),\ -4/27)&p\equiv13\bmod24.
\end{cases}
\]
These are **finite-field first-digit** coefficients, not yet canonically lifted through \(p^2\). Their first-digit scalar cancellation is supported by the existing finite checks and independently held source inputs; this note does not upgrade it to a universal theorem.

We test exactly one specified candidate lift: compute \(J_A,J_B\) as the *same integral Hasse-polynomial derivatives* at \(1/2,1/9\), but evaluate the displayed rational ratios directly in \(\mathbb Z/p^2\mathbb Z\), preserving the B3/B5 sign. Keep \(r_0\)'s rational expression at the same precision. Call the resulting particular candidates \(\widehat t,\widehat r\). Their resulting scalar residual is
\[
D_p^{\mathrm{cand}}=
\frac{\widehat t (G_A/p)-\widehat r (G_B/p)}p\bmod p
\]
whenever the numerator vanishes modulo \(p\). This is a **test of one lift construction**, not the original canonical \(W_p,V_p\) supercongruence, and not a test of native X6/H0/B0.

## Proved source-port decomposition

Define the base divided lift \(B_X=(Q_X+pL_X+pT_X)/p\bmod p^2\) and the three-stratum second-order source \(S_X=S_{0,X}+S_{1,X}+S_{2,X}\bmod p\). Because the first-digit relation holds for every tested prime, the two divided residuals below are defined:
\[
D_{\mathrm{base}}=\frac{\widehat t B_A-\widehat r B_B}{p}\bmod p,\qquad
D_S=(\widehat t\bmod p)S_A-(\widehat r\bmod p)S_B\bmod p.
\]
The already proved source expansion yields **exactly**
\[
\boxed{D_p^{\mathrm{cand}}=D_{\mathrm{base}}+D_S\pmod p.}
\]
This identity holds for every prime where the stated divided quantities are defined; the theorem itself is formal algebra, not a statistical fit. It tells the next Fricke proof precisely where the two new order-\(p^2\) Gauss sources enter.

## Exact finite discrimination: candidate is not an automatic second-digit identity

The independent standard-library verifier uses integer Hasse binomial derivatives modulo \(p^2\) and the previously checked direct Gauss coefficient recurrence modulo \(p^3\). All **94** target primes \(p<2500\), \(p\equiv13,19\bmod24\), have first-digit cancellation for this candidate and satisfy the proved decomposition. At **93/94** primes the second-digit residual is nonzero. The sole zero in this range is \(p=499\).

| \(p\) | \(D_{\mathrm{base}}\) | \(D_S\) | \(D_p^{\mathrm{cand}}\) |
|---:|---:|---:|---:|
| 13 | 8 | 1 | 9 |
| 19 | 16 | 16 | 13 |
| 43 | 38 | 31 | 26 |
| 67 | 61 | 28 | 22 |
| 373 | 365 | 125 | 117 |

At \(p=373\), \((J_A,J_B)=(119654,115671)\bmod 373^2\), \((\widehat t,\widehat r)=(314\cdot373+106,\ 345\cdot373+138)\bmod373^2\), and \((G_A/p,G_B/p)=(65672,36167)\bmod373^2\). The second-order source ports contribute \(S_A=288,S_B=23\); thus \(D_S=106\cdot288-138\cdot23=125\bmod373\), and \(D_{\mathrm{base}}+D_S=365+125=117\bmod373\).

In particular, \(p=13\) is an exact counterexample to the narrow **candidate** statement that this specific Hasse-derivative-ratio lift always makes \(D_p^{\mathrm{cand}}=0\). It is **not a counterexample** to the canonical second-digit LIFT of the mother task. That canonical target uses its own geometrically specified signed Fricke/Cartier normalization, Euler B5 source, and original \(p^3\) weighted sums. The tested naive lift need not equal that normalization.

## Independent algebraic warning: lifts change the divided residual

For \(\widehat t\to\widehat t+pa\), \(\widehat r\to\widehat r+pb\), the divided residual changes by \(a\,g_A-b\,g_B\), where \(g_X=(G_X/p)\bmod p\). This is exact. Since \(g_A=24,g_B=359\) at \(p=373\), the second digit is not invariant under arbitrary re-lifting. Choosing \(a,b\) to force a zero would be an empty gauge choice rather than a proof; the required coefficient lift must be derived from an actual Fricke/CM connection.

## Follow-up

The next scientific unit is to derive the **actual** \(p^2\)-level Fricke/Cartier transport (including the signed \(s^2=2\) eigenspace and B5 Euler factor), not merely extrapolate the derivative-ratio formula. For p=19 and p=373 compare its resulting lift corrections with the witness \((D_{\mathrm{base}},D_S)\), then seek a general proof connecting to the existing \(\Gamma_p+E_A-E_B\) source interface. Do not rerun the prior 94-prime expansion or reopen accepted D24 first digit. BRC resolution: COMPOSE_APPLIED; provenance labels remain explicit. Original native p373 benchmark #1559 remains outstanding.

Control: original same-lane request receipts em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 were read as WAITING_RESOURCE/EVENT_COLLECTION_IO and reconciled *under their original IDs* to QUEUED. Old native session/claim/run/staging remains UNKNOWN_PRESERVE; author-side GitHub evidence is not a formal checkpoint, claim, freeze or accepted result. Support path issue #1558.