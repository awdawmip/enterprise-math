# D25 / SECOND-DIGIT-LIFT: unique CM Gauss root lift and p=19 nonzero displacement

**Date:** 2026-11-01 Asia/Hong_Kong. **Proven arithmetic reduction / conditional composition of earlier author-side lemmas / 107-prime exact certificate / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_RUN.**

Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin: \`c47e13e4aba0e006366f989d6334d443f6333ae3\` (unchanged). Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`, **not** maintenance lane. Prior CM selection, Legendre parity and p=19 signed-tail results are reused at their historical author-proved/unreviewed status, not recredited.

## Chosen unfinished question and new theorem

For p>3 and the original two target classes p≡13,19 (mod 24), define in \(\mathbb Z_{(p)}[z]\)

\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k,\quad z_0=1/9,\quad
G_p=F_p(z_0),\quad H_p=G_p+16z_0F_p'(z_0).
\]

Consume the preceding CM(-24) / Legendre first-digit result: \(G_p\equiv0\pmod p\) and \(H_p\not\equiv0\pmod p\), for exactly these two classes. Define \(D_p=F_p'(z_0)\bmod p\), so \(D_p\equiv9H_p/16\not\equiv0\pmod p\).

**Universal arithmetic Hensel lemma (given this first-digit input):** precisely one \(d_p\in\mathbb F_p\) satisfies

\[
F_p(z_0+p d_p)\equiv0\pmod{p^2}.
\]

Its exact location is

\[
\boxed{d_p\equiv-\frac{G_p/p}{D_p}
       \equiv-\frac{16}{9H_p}\frac{G_p}{p}\pmod p.}\tag{HL}
\]

All p-local divisions are performed before reduction; \(p\mid G_p\), and \(9H_p/16\) is a unit. Proof: Taylor's *exact finite polynomial* expansion gives \(F_p(z_0+pu)\equiv G_p+puD_p\bmod p^2\); the coefficient of \(u\) is a unit. This is uniqueness among the \(p\) lifts of the same mod-p root, not a claim of a global polynomial root or an infinite-prime supercongruence.

## New full-class p≡19 mod24 displacement formula

For \(p\equiv19\pmod{24}\), reuse the existing author-side term-by-term \(T_{\beta,p}\equiv0\bmod p^2\) theorem and exact Clausen \(B_p=G_pH_p-T_{\beta,p}\). Guo–Zudilin, *A q-microscope for supercongruences* (arXiv:1803.01830; Adv. Math. 346, 2019), prove \(B_p\equiv p(\frac{-3}{p})\bmod p^3\), and here the symbol is +1. Thus \(G_pH_p\equiv p\bmod p^2\), giving \((G_p/p)H_p\equiv1\bmod p\).

Substitute this actual nonzero first digit into (HL):

\[
\boxed{d_p=-\frac{16}{9H_p^2}\ne0\pmod p,
\qquad p\equiv19\pmod{24}.}\tag{19D}
\]

The earlier even Legendre branch has \(n=(p-3)/4\) even, \(t_0^2=8/9\), and \(F_p(z)\equiv P_n(\sqrt{1-z})\bmod p\). At \(z_0\) the Legendre value vanishes; hence

\[
D_p=-\frac{P_n'(t_0)}{2t_0},\quad
H_p=16z_0D_p=-\frac{8P_n'(t_0)}{9t_0},\quad
H_pD_p=\tfrac12P_n'(t_0)^2.
\]

Therefore the **new derivative-only formula** is

\[
\boxed{d_p=-2\bigl(P_n'(t_0)^2\bigr)^{-1}\pmod p.}\tag{19L}
\]

Since \(n\) is even, \(P_n'\) is odd, so \(P_n'(t_0)^2\in\mathbb F_p\). It is a unit because \(H_p,D_p\) are. This gives a *uniform, provably nonzero* displacement of the exact lifted Gauss root **away** from the rational CM parameter \(1/9\) for every p=19 mod24. It is compatible with the previously proved nonzero \(G_p/p\); it does not assert \(G_p\equiv0\bmod p^2\) on this class.

## Remaining p≡13 mod24 obstruction as unique-root alignment

For \(p\equiv13\pmod{24}\), the old unproved first-lift conjecture becomes one exact geometric-arithmetic condition:

\[
\boxed{G_p\equiv0\bmod p^2\ \Longleftrightarrow\ d_p=0
\ \Longleftrightarrow\
20J_p-5K_b(a+p)-7K_a(b+p)\equiv0\bmod p^2.}\tag{13C}
\]

The last equivalence consumes the previously proved *Jacobi two-shift* congruence with \(a=(5p-1)/8,b=(7p-3)/8\); retain the two separately labeled derivative ports \(\Delta_a,\Delta_b\). If \(d_p=0\) and \(G_p=p^2g_{2,p}\bmod p^3\), there is precisely one second lift \(z_0+p^2 e_p\bmod p^3\) with

\[
\boxed{e_p=-g_{2,p}D_p^{-1}\pmod p.}\tag{13E}
\]

No all-p=13 proof of \(d_p=0\) is claimed: the full-class unknown is now a *specific CM parameter-lift alignment*, not an unqualified Hasse-zero assertion. The nonzero \(e_{13}\) example shows a p-adic zero need not stay at the same rational CM parameter for the next digit.

## Actual exact integer checks

The standard-library verifier \`research_notes/portable_direct/d25_cm_hensel_lift_20261101.py\` was executed **before publication**, covers **all 107 primes p≤3000** in the two classes (**53** p≡13, **54** p≡19), uses original hypergeometric coefficient recurrence, direct polynomial substitution at the shifted argument, and an independent Legendre three-term recursion for \(P_n'(t_0)^2\). Every assertion passed: the unique-root prediction, the independent polynomial evaluation, its nonzero derivative at the neighboring p-lift, both (19D)/(19L) for the 54 p19 instances, and finite \(d_p=0\) for the 53 p13 instances. Finite checks on p13 do not prove (13C).

| p | G mod p² | H mod p | D mod p | d (first root digit) | z0 mod p² | root mod p² | e (second digit, when computed) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 0 | 7 | 8 | 0 | 94 | 94 | 8 |
| 19 | 171 | 17 | 6 | **8** | 321 | **112** | — |
| 37 | 0 | 5 | 19 | 0 | 1217 | 1217 | 33 |
| 43 | 860 | 28 | 5 | **39** | 411 | **239** | — |
| 67 | 938 | 24 | 47 | **61** | 2494 | **2092** | — |
| 373 | 0 | 80 | 45 | 0 | 77294 | 77294 | 323 |

At p=19, \(F_{19}(112)=0\bmod361\) by the original polynomial; \(F_{19}(112+19)=19\cdot6\bmod361\), proving uniqueness of the nearby lifted root. At p=13, \(G_{13}\equiv169\bmod13^3\) and \(e_{13}=8\); third-digit permanence is false at this concrete input.

## BRC/source semantics and continuation

**BRC resolution COMPOSE_APPLIED:** carrier keeps \((p,z_0,G,H,D,d)\) together with the labeled Jacobi shifts, Gauss recurrence, Legendre branch and \(p\)-adic digits. The readout \(G\bmod p=0\) loses the unique second-digit displacement; only the corrected carrier \((G/p,D)\) determines that lift. No untyped quotient, native X6 transfer or original-class H0/B0 claim follows.

This is an **external p-adic arithmetic theorem/proof composition**, author-side and awaiting independent Source review. The mother LIFT remains \(A_p\equiv p\bmod p^3\) for p≡13,19 mod24; its higher affine 216/2304 bridge remains conjectural. The next scientific move is to prove or refute p13 root alignment \(d_p=0\) by a finite Jacobi/CM first-jet identity, then reconnect the original signed 216 source and frozen \(\Delta_p-R_p\). Original p373 H0/B0 divided-power \([X]U\bmod139129\), module rank, true semilinear Frobenius/eta, odd Green/Hesse, \(\kappa\), \(\Delta-R\) and independent replay remain **NOT_RUN / PENDING_OWNER**, as tracked by Issue #1559. An ordinary p-adic root of the scalar hypergeometric polynomial does not substitute for that native object.

At this run: gateway 0.6.11 reported \`research_authority_granted=false\`, \`executor_binding_configured=false\`; own checkpoint read was ACCESS_DENIED, old \`research-onhour-20261031-0205-dispatch-r15\` result was CONTROL_REQUEST_NOT_FOUND in this client scope. These establish no new valid claim/run. Older three staging artifacts retain their separate origins. **Author-side project persistence is distinct from native Source checkpoint/Result acceptance.** P000, ACTIVE worldview and frozen Source pin unchanged; do not modify existing task schedule or notifications.
