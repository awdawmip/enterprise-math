# R152–R152B: Coprime phase observability and finite first-period absence

Date: 2026-11-14 (Asia/Shanghai). Frozen science pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34, unchanged. Scope: external S23 finite Sturmian-word scalar observation. Predecessors: R146 exact phase-fiber count/affine period (commit b02b0c242b274bc6a82111dbd3600126a2867319) and R151/R151B gauge obstruction/normal form (commit 26ceeda4e695d738a90ac8289698a2a22e43190b). Mathematical status: author-side proof, NOT_REVIEWED.

## 1. Original observer and cuts

For a binary word w of length M, let p_0=0 and p_j be the sum of its first j bits. Its free-intercept open slope support has bounds

\[
\alpha=\max(0,\max_{0\le i<j\le M}(p_j-p_i-1)/(j-i)),\quad
\beta=\min(1,\min_{0\le i<j\le M}(p_j-p_i+1)/(j-i)).
\]

For an actual finite Sturmian word \(\alpha<\beta\). In reduced form write \(\alpha=a/b\), \(\beta=c/d\), and define absolute intercept cuts

\[
U=\min_{0\le j\le M}\{b(p_j+1)-ja\},\qquad V=\max_{0\le j\le M}\{dp_j-jc\}.
\]

R146's exact integer-phase count for \(K=L+1\ge2\) is

\[
C_w(L+1)=\left\lceil\frac{cL-V}{d}\right\rceil-
\left\lfloor\frac{aL-U}{b}\right\rfloor-1\ge0. \tag{1}
\]

The proofs below use the retained cuts and joint period in (1).

## 2. Theorem R152 — Coprime boundary-phase injectivity

Fix reduced rational interior endpoints \(0<a/b<c/d<1\) with \(b,d\ge2\), and assume \(\gcd(b,d)=1\). For *arbitrary* integer cuts U,V, define C by the expression on the right of (1) (even if the cuts do not correspond to a finite word). Define \(D_{U,V}(L)=C(L+2)-C(L+1)\), for all integer L.

**Theorem.** D is periodic with period \(P=bd\), depends only on \((U\bmod b,V\bmod d)\), and the map

\[
(U\bmod b,V\bmod d)\longmapsto (D(0),\ldots,D(P-1)) \tag{2}
\]

is injective. Thus exactly bd increment waveforms occur in the unrestricted cut population, and any lossless fixed-width code for this observer requires at least \(\lceil\log_2(bd)\rceil\) bits.

**Proof.** Put

\[
A_U(L)=\left\lfloor\frac{a(L+1)-U}{b}\right\rfloor-
\left\lfloor\frac{aL-U}{b}\right\rfloor,\quad
B_V(L)=\left\lceil\frac{c(L+1)-V}{d}\right\rceil-
\left\lceil\frac{cL-V}{d}\right\rceil.
\]

Then \(D=B_V-A_U\). The sequences A and B have periods b and d; adding b to U or d to V leaves them unchanged. If two pairs have equal full D, then

\[
A_U-A_{U'}=B_V-B_{V'}.
\]

The left side is b-periodic and the right side d-periodic. Since the periods are coprime, their common function is constant. Telescoping a full b-period gives \(\sum A_U=\sum A_{U'}=a\), hence this constant is zero. Consequently \(A_U=A_{U'}\) and \(B_V=B_{V'}\).

The marking rule for A is \(A_U(L)=1\) exactly when \((aL-U)\bmod b\) lies in the proper nonempty cyclic interval \(\{b-a,\ldots,b-1\}\). The unit a modulo b visits every residue; no nonzero translation of a proper contiguous cyclic interval stabilizes it. Hence \(U\equiv U'\pmod b\). Similarly \(B_V(L)=1\) exactly when \((cL-V)\bmod d\) lies in the cyclic interval \(\{0,d-c+1,\ldots,d-1\}\), of length c. Because c is a unit modulo d, equality of the B signals forces \(V\equiv V'\pmod d\). This proves injectivity. Every one of the bd residue pairs is permitted by the declared arbitrary-cut population, completing the cardinality and coding lower bound. QED.

**Observer meaning.** With coprime endpoint denominators, the mixed R147–R151 CRT lag covariance is the same zero waveform for every pair of cuts (gcd g=1), while (2) distinguishes bd states. This quantifies the phase information lost by the covariance-only observer when the downstream readout is the full sequence of count increments. Once the increments are known, one integer count anchor (for example C(2)) reconstructs all multiplicities. The actual finite-word cut population is a subset, to be classified separately; its optimal coding size is not claimed here.

## 3. Theorem R152B — Exact first-period certificate for all absence events

For an actual word \(w\), put \(P_w=\operatorname{lcm}(b,d)\) and \(Q_w=P_w(\beta-\alpha)\).

**Theorem.** \(Q_w=(bc-ad)/\gcd(b,d)\) is a positive integer, and for every integer L,

\[
C_w(L+P_w+1)=C_w(L+1)+Q_w. \tag{3}
\]

Every absent coefficient in the domain \(K=L+1\ge2\) lies within \(1\le L\le P_w\). The exact permanent-presence threshold therefore equals

\[
T_w=2+\max(\{L\in\{1,\ldots,P_w\}:C_w(L+1)=0\}\cup\{0\}), \tag{4}
\]

and the complete length-M finite-language threshold is \(T(M)=\max_{w\in W_M}T_w\).

**Proof.** From the reduced endpoints, \(bc-ad>0\), and \(g=\gcd(b,d)\) divides bc and ad, so \(Q_w=(bc-ad)/g\) is a positive integer. Translation by P increases the ceiling term in (1) by \(Pc/d\in\mathbb Z\) and its floor term by \(Pa/b\in\mathbb Z\), yielding (3).

For actual words, (1) counts integer phase labels, so \(C_w(L+1)\ge0\) whenever \(L\ge1\). If \(L>P\) and \(C_w(L+1)=0\), (3) would give \(C_w(L-P+1)=-Q_w<0\), a contradiction. Hence all zero counts occur in the first P positions. If the last missing coefficient corresponds to \(L=L_*\), it is \(K=L_*+1\), so the smallest forever-present K is \(L_*+2\). When no zeros occur, the threshold in the declared \(K\ge2\) domain is 2. Maximizing over the complete finite Sturmian language proves the final statement. QED.

Equation (4) is an exact, finite, endpoint-adaptive decision certificate. It retains the integer offset cuts and their lcm clock, providing an independent finite-horizon route alongside R141's global sufficient bound.

## 4. Exact reproducible verification and next mathematics

Companion program check_r152.py uses Python unlimited integers and fractions.Fraction. It exhaustively checks all coprime \(2\le b,d\le10\), all reduced interior rational pairs \(a/b<c/d\), and all modulo-b/modulo-d cut pairs: **306 valid endpoint pairs; 14,508 distinct full-period increments; zero collisions**. It independently enumerates all \(2^M\) binary words, \(1\le M\le12\); retains exactly those with \(\alpha<\beta\); checks (3), nonnegativity, and a second absence-free period. It obtains

\[
(T(1),\dots,T(12))=(2,2,3,4,7,9,16,19,29,33,46,51).
\]

The finite values agree with R140's independently reported values in their overlapping domain. The general proofs do not depend on the finite enumeration limit.

**Next scientific unit:** characterize the actual Sturmian-word subset of the unrestricted cut classes, then seek a symbolic bound on the last-zero positions in (4), aiming at the still-open proposed all-length exact formula \(T(M)=(M-2)\lfloor(M-1)/2\rfloor+1\) for \(M\ge5\). No native X6 equivalence or formal CLAIM/Result/Review is asserted by this author-side note.
