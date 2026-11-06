# D25 — Original full-216 three-shell reduction with a first-order middle jet and a nonzero second shell

**Date:** 2026-11-06. **Scope:** TASK_RESEARCH, author-side portable mathematics under original scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`, publication \`TP2-B6F4FC938FF94941C1B7\`; logical Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`. This is a newly derived original-\`W_p\` finite modular theorem; it consumes the earlier original signed Clausen/Green frontiers, not a re-proof or substitution of the original-class H0/B0 native benchmark. **Status:** AUTHOR-PROVED, FINITE-VERIFIED, UNREVIEWED, NOT_ADMITTED.

## Statement (all primes p=6m+1>3)

Let
\[
a_n=\frac{(2n)!(3n)!}{216^n(n!)^5},\quad
W_p=\sum_{n=0}^{p-1}(6n+1)a_n,\quad
P_{2m+1}=\sum_{n=0}^{2m}(6n+1)a_n.
\]
All calculations occur in the localization \(\mathbb Z_{(p)}\), and every denominator in the auxiliary sequences below is a p-unit throughout the stated finite ranges.

For \`0<=j<m\`, define prime-independent rational sequences \`q_0=g_0=1\` with
\[
\frac{q_j}{q_{j-1}}=\frac{3j(6j+1)(3j+1)}{4(3j+2)^3},\qquad
\frac{g_j}{g_{j-1}}=\frac{j(6j-1)(6j+1)}{9(2j+1)^3}\qquad(1\le j<m).
\]
Define \(\sigma_0=0\) and
\[
\sigma_j=\sum_{t=1}^j\left(\frac{2}{6t+1}+\frac1{3t}+\frac1{3t+1}-\frac3{3t+2}\right).
\]
Set
\[
Q_0=\sum_{j=0}^{m-1}(6j+5)q_j,\quad
Q_1=\sum_{j=0}^{m-1}q_j\left[2+(6j+5)\left(\frac32+\sigma_j\right)\right],\quad
G_0=\sum_{j=0}^{m-1}(6j+4)g_j.
\]

**Theorem (original full-sum three-shell transfer).** For every prime \`p=6m+1>3\`:
\[
\boxed{W_p\equiv P_{2m+1}
 +\frac{p\,a_{2m}}{32}(Q_0+p Q_1)
 -\frac{p^2\,a_{2m}}{576}\,q_{m-1}G_0 \pmod{p^3}.}
\]
The formula requires \`P\` modulo p³, \`a_{2m}\` modulo p² in the p-linear term, \`Q_0\` modulo p², and \`Q_1,q_{m-1},G_0\` modulo p. The last term is an **actual generally nonzero p² shell**, not an arbitrary correction.

## Proof and exact p-adic populations

Write \(\gamma_n=\binom{2n}n^2\binom{3n}n\), so \(a_n=\gamma_n/216^n\) with
\[
\frac{a_n}{a_{n-1}}=\frac{(2n-1)(3n-2)(3n-1)}{36n^3}.
\]
Since \(n<p\), Legendre's formula yields
\[
v_p(a_n)=\lfloor2n/p\rfloor+\lfloor3n/p\rfloor=
\begin{cases}
0&0\le n\le 2m,\\
1&2m+1\le n\le3m,\\
2&3m+1\le n\le4m,\\
3&4m+1\le n\le6m.
\end{cases}
\]
Thus all four original bands must be classified; the valuation-three last band vanishes mod p³, while the *valuation-two band survives* at the required precision. A preliminary three-band cutoff that discarded indices \(3m+1,\ldots,4m\) fails already at p=7; the exact valuation formula repairs that shortcut.

At the first middle index \(n_0=2m+1=(p+2)/3\), substitution into the recurrence gives the exact rational identity
\[
\frac{a_{n_0}}p=a_{2m}\frac{(2p+1)(p+1)}{4(p+2)^3}
\equiv \frac{a_{2m}}{32}\left(1+\frac{3p}{2}\right)\pmod{p^2}.
\]
For \(1\le j<m\), the adjacent ratio at \(n_0+j\) is exactly
\[
r_j(p)=\frac{(6j+2p+1)(3j+p)(3j+p+1)}{4(3j+p+2)^3}.
\]
Its first-order p-adic expansion at zero is \(r_j(p)\equiv r_j(0)(1+p\,\delta_j)\pmod{p^2}\), where
\[
\delta_j=\frac{2}{6j+1}+\frac1{3j}+\frac1{3j+1}-\frac3{3j+2}.
\]
It follows by finite multiplication that
\[
\frac{a_{n_0+j}}p\equiv
\frac{a_{2m}}{32}\,q_j
\left(1+p\left(\frac32+\sigma_j\right)\right)\pmod{p^2}.
\]
Using the exact middle weight \(6(n_0+j)+1=6j+5+2p\) and summing gives the middle term \(p a_{2m}(Q_0+pQ_1)/32\).

The next index is \(n_1=3m+1=(p+1)/2\). The recurrence gives exactly
\[
\frac{a_{n_1}}p =a_{3m}\frac{9p^2-1}{18(p+1)^3};
\quad
\frac{a_{3m}}p\equiv\frac{a_{2m}q_{m-1}}{32}\pmod p.
\]
Consequently \(\frac{a_{n_1}}{p^2}\equiv-\frac{a_{2m}q_{m-1}}{576}\pmod p\).
At \(n=n_1+j\) the successive ratio modulo p equals \(j(6j-1)(6j+1)/[9(2j+1)^3]\); its weight modulo p is \(6j+4\). Summing \(0\le j<m\) gives exactly \(-p^2a_{2m}q_{m-1}G_0/576\). The last band has valuation at least three. Combining these original-index bands proves the theorem.

The q/g sequences are independent of p as rational functions in the local index, with m determining the truncation. The coefficient carrier retains \((n,v_p(a_n),p\text{-unit residue},\text{weight})\); operations retain p² middle jets and the signed original contribution from each band. **BRC: COMPOSE_APPLIED** for exact integer/valuation and branch-aware observer information. This is an external finite hypergeometric representation, not an Enterprise-native spatial 2D model.

## Executed verification

The standalone standard-library checker \`d25_original216_middle_shell_jet_check_20261106.py\` independently computes original coefficients using the rational recurrence modulo p³ and \(\binom{2n}n^2\binom{3n}n/216^n\) on selected inputs, and separately computes q, the first-order jet, g, and each band. It executed all **148** primes \(7\le p\le1999\), \(p\equiv1\bmod6\) (including **77** target primes \(p\equiv13,19\bmod24\)), with **zero failures**. All four raw bands were compared to their predicted contributions.

Representative raw \([p,P_{2m+1},M,G,H,W_p]\) modulo p³:
- \(p=7:\ [7,231,217,245,0,7]\), modulus 343;
- \(p=13:\ [13,780,1937,1690,0,13]\), modulus 2197;
- \(p=19:\ [19,5662,4826,3249,0,19]\), modulus 6859;
- \(p=373:\ [373,28094360,38687933,37008314,0,373]\), modulus 51895117.

At p=19 the p² gap contribution is \(3249=9\cdot19^2\), and at p=373 it is \(37008314=266\cdot373^2\); deleting it changes the original full evaluation at precisely the required modulus.

These raw W residues are **finite observations** consistent with the mother congruence, not a new uniform proof of \(W_p=p\bmod p^3\).

## New narrow mother-objective condition

On target primes the remaining original mother condition is exactly equivalent, by the theorem, to proving the original-low-and-middle congruence
\[
P_{2m+1}+\frac{p\,a_{2m}}{32}Q_0
\equiv p + p^2 a_{2m}
\left(\frac{q_{m-1}G_0}{576}-\frac{Q_1}{32}\right)\pmod{p^3}.
\]
This is a specified, finite **signed cancellation** problem with a single boundary seed, explicit first-order middle jet, and an independently present valuation-two gap. No terms from the original full sum are suppressed. Seek a finite adjoint or creative-telescoping certificate for this identity and compare the earlier Clausen \(S_p,K_p,J_p\) decomposition without equating the mixed-CM endpoint with \(W_p\). Test p=19 and p=373 first. This conditional reduction is the next task, not a proof of it.

The distinct native original-class p373 H0/B0 [X]U divided-power Frobenius/eta/kappa benchmark and independent replica remain **NOT_EXECUTED/PENDING_OWNER**, tracked at https://github.com/awdawmip/enterprise-math/issues/1559. Native queued Source request \`onhour11-20261106-1400-exact-research-lane-continuation\` was read by original ID, status QUEUED / EVENT_COLLECTION_IO; no current native Researcher authorization, claim, run or Result, and old staged items remain separate.
