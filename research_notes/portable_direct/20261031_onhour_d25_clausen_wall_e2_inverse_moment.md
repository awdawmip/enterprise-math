# D25 / SECOND-DIGIT-LIFT — Clausen mirror wall and E.2 inverse-moment bridge

Date: 2026-10-31 Asia/Hong_Kong. Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923, independent of maintenance. Classification: AUTHOR-SIDE / PROVED ALGEBRAIC WALL THEOREM / EXECUTED EXACT 330-PRIME CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_EXECUTED / REGISTER_PENDING.

Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** unchanged. P000/ACTIVE X6-time worldview unchanged. This is classical p-adic arithmetic, not an X6 native assertion.

## Original sources and valuation ledger

For prime p=6l+1≥7 let m=(p−1)/3=2l and h=(p−1)/2=3l. Keep the original distinct sources

\[
a_n=\frac{(1/2)_n(1/3)_n(2/3)_n}{2^n(n!)^3}
=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},
\quad A_p=\sum_{n=0}^{p-1}(6n+1)a_n,
\]
\[
b_n=(-1)^n\frac{(1/3)_n^3}{(n!)^3},
\quad B_p=\sum_{n=0}^{m}(6n+1)b_n.
\]

The original p-adic valuations are exactly 0 for 0≤n≤m, 1 for m<n≤h, 2 for h<n≤2m, 3 for 2m<n<p. Proof: the three Pochhammer factors (1/3),(1/2),(2/3) first cross p at n=m+1,h+1,2m+1, respectively; n! and 2 stay p-units. In the E.2 source b_n, the omitted tail n>m is divisible by p³.

## Theorem: a single arithmetic wall in the Clausen prime-index mirror

Define for 1≤k≤h the p-local unit

\[
M_k=-18k^3\,\frac{a_ka_{p-k}}{p^3}.
\]

The two coefficient valuations sum to 3: (0,3) for 1≤k≤m and (1,2) for m<k≤h. The exact rational coefficient recurrence is

\[
\frac{a_{n+1}}{a_n}=\frac{(2n+1)(3n+1)(3n+2)}{36(n+1)^3}.
\]

Consequently for each 2≤k≤h the following *exact* ratio identity holds (not merely mod p):

\[
\frac{M_k}{M_{k-1}}=
\frac{(1-p/(k-1))^3}{
(1-2p/(2k-1))(1-3p/(3k-1))(1-3p/(3k-2))}.
\tag{R}
\]

The only exceptional step is k=m+1, where 3k−2=p **exactly**. Its last denominator factor is 1−3p/p=−2, a p-unit, and the others reduce to 1. Hence the reduced ratio there is −1/2; at every other step it is 1. One must not expand the exceptional factor as 1+O(p).

Endpoint: a_1=1/18, a_{p−1}/p³≡−1 modp. Indeed, each (α)_{p−1}, α∈{1/2,1/3,2/3}, has exactly one p-factor (p/2,p/3,2p/3); the other p−2 factors have residues all F_p^× except α−1, so their product is 1/(1−α) by Wilson. These unit products multiply to 9, the selected factors to p³/9; the denominator ((p−1)!)³2^{p−1} reduces to −1. Thus M_1≡1. Multiplying (R) proves the all-prime theorem

\[
\boxed{M_k\equiv
\begin{cases}
1 & 1\le k\le m,\\
-1/2 & m<k\le h
\end{cases}\pmod p.}\tag{W}
\]

The portion k≤m reuses the other Research lane's author-side mirror; the **crossing k=m+1 and the second stratum** are the new result.

## Corollary: inverse middle-stratum moment for the original signed high strip

For m<k≤h, let u_k=a_k/p, a p-local unit. (W) implies

\[
\boxed{\frac{a_{p-k}}{p^2}\equiv\frac1{36k^3u_k}\pmod p.}\tag{I}
\]

Keep the *original* term index and signed weight through n=p−k, so 6n+1≡1−6k modp. The second-valuation original strip

\[
S_2=\sum_{h<n\le 2m}(6n+1)a_n
\]
obeys the proven all-prime law
\[
\boxed{\frac{S_2}{p^2}\equiv\mathcal I_p:=
\sum_{k=m+1}^{h}\frac{1-6k}{36k^3(a_k/p)}\pmod p.}\tag{IM}
\]
Each inverse is a genuine p-unit; coefficient source, precision, observer and reflection direction are retained.

Define independent-source low and middle parts
\[
D_0=\sum_{n=0}^{m}(6n+1)(a_n-b_n),\qquad
D_1=\sum_{m<n\le h}(6n+1)a_n.
\]
The remaining n>2m part of A_p vanishes modp³, so the original E.2 bridge has the unconditional algebraic decomposition
\[
\boxed{A_p-B_p\equiv D_0+D_1+p^2\mathcal I_p\pmod{p^3}.}\tag{BR}
\]
The global bridge is now equivalent to TWO unproved obligations: (i) D_0+D_1≡0 modp² and (ii) under (i),
\[
\boxed{(D_0+D_1)/p^2+\mathcal I_p\equiv0\pmod p.}\tag{OPEN}
\]
Neither (i) nor (ii) is established for all primes here. A theorem giving B_p≡p modp³ (Van Hamme E.2) would settle the original p≡13,19 mod24 LIFT **only after** both bridge conditions are proved.

## Exact execution

Executed the accompanying Python-stdlib program d25_middle_wall_crossing_guard_20261031.py. Independently computed a_n modp⁴ and b_n modp³ with their *different* original recurrences. Exhaustively checked all 330 primes p≡1 mod6, 7≤p≤5000 (including 166 frozen targets), each valid mirror M_k and the unique −1/2 wall, valuations, exact D0/D1/S2 decomposition, inverse moment, first-/second-digit bridges and the original full A_p and B_p. Terminal marker PASS_D25_CLAUSEN_WALL_E2_BRIDGE. The numerical bridge over 330 primes is finite evidence, **not** an all-prime proof. All 166 target primes had nonzero inverse moment and nonzero complementary carry.

| p | D0 modp³ | D1 modp³ | S2 modp³ | ((D0+D1)/p²) modp | I_p modp |
|---:|---:|---:|---:|---:|---:|
|13|767|1937|1690|3|10|
|19|5643|4826|3249|10|9|
|373|28093987|38687933|37008314|107|266|

Both signed contributions are nonzero and cancel, e.g. 107+266=373 at p373. For p373, p²=139129. The check operates in scalar integer mod rings, **not** original native H0/B0.

## Provenance, BRC and unresolved work

BRC=COMPOSE_APPLIED: carrier (p, original n, reflected k, source labels a/b, valuations, signed weights, normalized units, precision), with exact reflection, unit inversion and signed aggregation. Full-source equality is *not* inferred from the scalar observer quotient.

Consumed unreviewed author-side sources: other lane research_notes/portable_direct/20261031_hourly_d25_lifted_prime_index_mirrors.md at enterprise-math commit 06257b8f444eed359c77e93bd8acf9c75a1f08c2; this lane's E.2 candidate at commit 42fae018032be0be1b496b749472ead751d624a2. No authorship reassignment.

Higher-priority native #1559 is OPEN/PENDING_OWNER: same-original-class p373 H0/B0 divided-power [X]U mod139129, rank, true semilinear Frobenius/eta, odd signed Green/Hesse and κ, and independent verification remain NOT_EXECUTED. Own recovery #6632 confirmed no own Source-authorized CLAIM/run; original dispatch #6633 FAILED UPSTREAM_CODE_REVIEW_REQUIRED. Current native gateway reports research_authority_granted=false, write_relay_enabled=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED and full active job capacity. Historic staging SD-d7c23e7984c2ddaac60a preserved separately. No new CLAIM, Source checkpoint, Result, release or admission is claimed; activity registration = SYNC_DEBT. Request IDs stay unchanged for lawful reconciliation.

Next science: establish the global first-digit bridge (i) and construct a signed WZ/CM finite transformation that proves (OPEN), or find a counterexample; do not erase I_p or replace the native benchmark with scalar coefficients. Native #1559 needs a real authorized native evaluator and reproducible original-object evidence, not another equivalent-looking arithmetic proxy.
