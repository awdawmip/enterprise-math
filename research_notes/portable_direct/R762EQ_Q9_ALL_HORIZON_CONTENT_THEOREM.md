# R762EQ — All-horizon q=9 BRC content and a finite-to-infinite 3-adic recurrence certificate

**Date:** 2026-11-18. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. **Scientific inputs:** original frozen six-named positive-terminal BRC group-ring model, original P000 and taskbook pins. **Status:** AUTHOR-PROVED WITH EXPLICIT EXACT FINITE CERTIFICATE / NOT_REVIEWED.

## Statement (every horizon, no induction cutoff)

Let
\[
G_q=(\mathbb Z/q\mathbb Z)^3,\quad
R_q=\mathbb Z[G_q],\quad
P=1+X+Z+XY+YZ+XYZ.
\]
The six summands are the six separately named positive BRC branches. Set \(c_q(n)=\gcd_{g\in G_q}[g]P^n>0\). For the complete three-coordinate q=9 terminal-observer group ring, **for every integer \(n\ge0\)**,
\[
\boxed{c_9(n)=3^{\max(0,\lfloor n/3\rfloor-2)}.}                 \tag{1}
\]

For \(n\ge9\), set \(k(n)=\lfloor n/3\rfloor-2\) and take the coefficientwise mod-3 shadow
\[
S_n=3^{-k(n)}P^n\bmod3\in\mathbb F_3[G_9].
\]
It is defined integrally at every horizon and satisfies **for every \(n\ge9\)**,
\[
\boxed{S_{n+18}=S_n.}                                         \tag{2}
\]
Its 18-vector orbit \(S_9,\ldots,S_{26}\) consists of nonzero vectors of \(\mathbb F_3^{729}\), spans dimension 17, and satisfies
\[
\boxed{2S_{11}+S_{14}+S_{20}+S_{26}=0.}                        \tag{3}
\]
The exact gcd formula (1) is now an all-horizon theorem for q=9, rather than the finite window in predecessor R762EP. The proof does not rely on the unreviewed 127-factor q=9 spectral computation R762EM.

## 1. General cyclotomic integral-power lemma (all powers of 3)

**Lemma.** Let \(q=3^a\) (\(a\ge1\)), \(d=3^{a-1}\) and \(\zeta\) a primitive \(q\)th root. For every character triple \((i,j,k)\), the algebraic number
\[
\beta_{ijk}=\frac{P(\zeta^i,\zeta^j,\zeta^k)^d}{3}
\]
is integral at the prime 3. Consequently, the group-ring convolution operator \(B=P^d/3\in\mathbb Q[G_q]\) satisfies a monic degree-\(q^3\) polynomial
\[
F_q(B)=0,\qquad F_q(T)\in\mathbb Z_{(3)}[T].
\]
Here \(\mathbb Z_{(3)}=\{r/s:r,s\in\mathbb Z,\ 3\nmid s\}\).

**Proof.** In \(\mathbb Q_3(\zeta)\), the element \(\pi=\zeta-1\) is a uniformizer and \(v_\pi(3)=\varphi(q)=2d\). Every \(\zeta^i-1\) belongs to \(\pi\mathcal O\) (also for \(i=0\)). Set \(x=\zeta^i-1\), \(y=\zeta^j-1\), \(z=\zeta^k-1\). Expansion of the *six named terms* yields
\[
P(1+x,1+y,1+z)
=6+3x+3y+3z+\text{terms of total degree at least two in }x,y,z.
\]
Thus every evaluation \(\lambda_{ijk}\) lies in \(\pi^2\mathcal O\) (the constant and linear terms are even more divisible). Hence \(\lambda_{ijk}^d/3\in\mathcal O\), since \(2d=v_\pi(3)\).

Define \(F_q(T)=\prod_{i,j,k=0}^{q-1}(T-\beta_{ijk})\), including repeated roots and zeros. The coefficients are symmetric polynomials in 3-integral elements, hence 3-integral. The multiset of roots is Galois stable, so the coefficients are rational; rational numbers integral at 3 belong to \(\mathbb Z_{(3)}\). Fourier characters diagonalize multiplication by \(P\) and by \(B\) over \(\mathbb Q(\zeta)\), thus \(F_q(B)=0\). Its degree is exactly \(q^3\), without an assertion that it is minimal. QED.

**Finite-to-infinite consequence.** For every \(v\in\mathbb Q[G_q]\), the vector sequence \(B^t v\) obeys a monic order-\(q^3\) recurrence with coefficients in \(\mathbb Z_{(3)}\). If its first \(q^3\) vectors belong to \(\mathbb Z_{(3)}[G_q]\), every subsequent vector does too. If two such sequences have a difference vanishing modulo 3 for any \(q^3\) consecutive times after their 3-integrality has been established, that difference remains zero modulo3 at every later time. This is elementary forward induction on the same monic recurrence. It is a reusable exact BRC finite-certification mechanism at q=3,9,27,... .

## 2. The q=9 recurrence-lifting proof

Now \(q=9\), \(d=3\) and \(|G_9|=729\). Write \(B=P^3/3\). For each \(r=0,1,2\) define a rational group-ring sequence
\[
V_t^{(r)}=9B^tP^r=3^{\,2-t}P^{\,3t+r},\qquad t\ge0. \tag{4}
\]
Each of the three sequences satisfies the *same* monic 729-order recurrence from \(F_9(B)=0\).

**Integrality step.** The accompanying exact program computes every coefficient of \(P^n\) modulo \(3^{744}\) for each \(0\le n\le2213\), using the six original named BRC shifts. It verifies
\[
P^{3t+r}\equiv0\pmod{3^{\max(0,t-2)}}\quad
\text{coefficientwise for all }0\le t\le728,\ r\in\{0,1,2\}.
\]
Therefore each \(V_t^{(r)}\in\mathbb Z_{(3)}[G_9]\) for its first 729 times (for \(t\le2\), (4) is already integral). The monic recurrence propagates this integrality to *every* \(t\ge0\). For \(t\ge3\) it states that \(3^{t-2}\) divides every coefficient of \(P^{3t+r}\).

**Period step.** The same exact program verifies \(S_{n+18}=S_n\) for all integers \(9\le n\le2195\) (the later check \(n=2195\) compares with \(n=2213\)). Equivalently it checks
\[
\overline{V}_{t+6}^{(r)}-\overline{V}_t^{(r)}=0
\quad\text{for }t=3,4,\ldots,731;\quad r=0,1,2, \tag{5}
\]
where bars reduce coefficients of the 3-integral vectors modulo3. This is **729 consecutive times for each of three residues**, or 2187 comparisons. Each difference sequence satisfies the monic 729-order recurrence, and integrality permits reduction of its coefficients modulo 3. Thus (5) implies
\[
\bar V_{t+6}^{(r)}=\bar V_t^{(r)}\qquad(\forall t\ge3,\ r=0,1,2).
\]
This is precisely (2), now *for all n>=9*.

**Exactness of the content bound.** The program verifies each of the 18 base vectors \(S_9,\ldots,S_{26}\) has at least one nonzero coefficient. By the period theorem, every \(S_n\) for \(n\ge9\) has a nonzero coefficient. Therefore the 3-adic valuation of the integer coefficient gcd is exactly \(\lfloor n/3\rfloor-2\). For \(0\le n\le8\), the coefficient of the identity endpoint is 1 (no nonidentity branch can wrap any of three q=9 coordinates to zero in fewer than nine steps), so the gcd is 1.

Finally, the independent all-odd-q lemma proved in R762EP excludes any factor 2: the gcd divides \(\sum_g[g]P^n=6^n\), and the characteristic-two character with \(X=Y=1,\ Z=z\ne1\) a qth root evaluates \(P\) to \(1+z\ne0\). This completes (1).

## 3. Fully specified finite certificate and verification range

Companion file \`R762EQ_Q9_ALL_HORIZON_CONTENT_VERIFY.py\` directly evaluates the **entire 729-component q=9 coefficient vector** at 2214 consecutive horizons \(n=0,\ldots,2213\), modulo \(3^{744}\). It checks:

- 2214 exact augmentation/mass identities \(\sum_g C_9(n;g)\equiv6^n\pmod{3^{744}}\).
- 2214 independently propagated q=3 observer reductions, full 27 components per time.
- 2214 coefficientwise divisibility conditions plus one explicit nonzero normalized mod3 witness per time.
- 2187 exact 729-component shadow recurrences comparing \(S_n\) with \(S_{n-18}\) for \(27\le n\le2213\).
- 18 base vectors, rank 17 over \(\mathbb F_3\), and the explicit relation (3).

The maximum exact content exponent tested is 735, strictly less than the 744-digit 3-adic modulus precision. All branch shifts are exact modular integer operations, and calculation uses no floating point, trigonometry or non-BRC propagation. In particular the finite arithmetic conditions suffice to discharge the hypotheses of the symbolically proved order-729 recurrence-lifting lemma; neither numerical fitting nor an unproved assumption of universal period is used.

The concatenation of the 18 ordered length-729 mod3 vectors (lexicographic \((u,v,w)\)) has SHA-256:
\`fb37bdb7463e493b32dbd5d43157621dfaab2b8f92381a062c25da7b9f4798a4\`.
Their supports are
\[
(27,162,486,717,108,324,525,522,468,18,108,324,519,360,468,237,450,324).
\]
Companion \`R762EQ_Q9_ALL_HORIZON_EVIDENCE.json\` includes the exact range, conditions, proof bridge and SHA. The script is self-contained, standard-library Python; its output can be reproduced without any proprietary credential.

**Status:** author symbolic proof plus exact exhaustive finite certificate **PASS**; independent mathematical review \`NOT_REVIEWED\`; Lean/formalization \`NOT_PERFORMED\`.

## 4. Scope, provenance, and the next genuine frontier

This result settles the full all-horizon integer content and normalized 18-step q=9 period for the **positive six-branch three-terminal BRC observer**. The full named branch set and all coefficient positions are retained. The terminal coefficient operation is a declared observer within frozen P000's native signed-six-axis Heartbeat World; this theorem does not postulate a native event license or collapse signed provenance, joint composite directions, Cell identity or future operations.

The all-q cyclotomic integral-power lemma supplies an exact candidate route for **q=27**, with \(d=9\) and a degree-\(27^3=19683\) monic 3-integral recurrence. A sharper, smaller invariant module or factor certificate would greatly reduce the finite horizon necessary for q27. Separately, the original parent Task still requires the authentic \`TRIADIC_CLOSURE_E\` signed Cell/Link/Port legality and V17/V29/V39 future-operation transport.

**Frozen science:** project P000 @ \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`; Task book @ \`e3f42efac29a2da2d95be391f3231a664e2fade0\`. **Predecessors:** R762EP finite theorem, and R762EM/EN/EO portable notes. **Role provenance:** historical Researcher \`EM-X6-3050F6\`; current native Source owner/claim authorization is governed by the authenticated control state and is not implied by this GitHub Draft PR. No new Source PROGRESS, Result, formal review or Foundation admission is asserted.
