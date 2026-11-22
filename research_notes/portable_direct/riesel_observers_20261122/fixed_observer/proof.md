# Unbounded exact covering cost at one fixed twenty-five-channel trajectory

Status: author mathematical derivation with exact finite witnesses, continuing Researcher `EM-DIRECT-970E1C` and Activity `RA-D2EC212845B63844081F9A14`. This is not an independent project Review or a formal promotion.

## 1. Statement

Retain the old root, dictionary and product

\[
a_*=690786768637635218740714348513373826260012289,
\]

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
1321,14449,29191,65537,6700417\},
\]

\[
M=1397394912916194098609132326092145093313722687204526281.
\]

Let \(F_n(a)=a^2 2^n-1\), and let \(\delta_P(a)\) be the least number of primes outside P needed in a full proper-prime cover. Let \(\tau(a^2)\) be the least total number of primes in such a cover. A missing finite cover has value infinity. These are different minima.

Put

\[
V=\{5,13,11,61,331\},\qquad K=\prod_{q\in V}q=14436565.
\]

**Theorem.** For every integer \(s\ge5\), infinitely many positive odd roots satisfy

\[
\boxed{
a\equiv a_*\pmod{2M},\quad 3\mid a,\quad
a\equiv666303\pmod K,\quad
\delta_P(a)=s,\quad\tau(a^2)=20+s.
}
\tag{1}
\]

Consequently every one of these roots has the same complete joint residue trajectory

\[
\mathcal O(a,n)=\bigl([F_n(a)]_q\bigr)_{q\in P\cup V},\qquad n\ge0,
\tag{2}
\]

while its exact covering costs range over every finite value specified in (1).

In particular, the finite observer introduced for the sharp small-budget predicates cannot determine exact covering cost, nor give a uniform finite upper bound for that cost on this observer fiber. The assertion is about this specific observer. It does not claim that every finite dictionary has this property, since a dictionary already containing a full cover supplies its own finite upper bound.

## 2. The preserved construction

The established all-cost theorem is at commit
`af9e1a5e49386a28283781876e10742a71991036`, path
`research_notes/portable_direct/riesel_spectrum_20261121/spectrum/proof.md`.
It gives, for every \(s\ge5\), an irredundant dictionary \(S=P\sqcup Q\) with \(|Q|=s\), private old and new witnesses, and a compatible CRT construction that makes all \(20+s\) private terms pairwise coprime. This preceding theorem, its complete seed calculations, and its classical primitive-prime existence input are reused unchanged.

The four retained extra seed rows have base-2 orders

\[
4,9,12,18
\]

and primes \(5,73,13,19\), respectively. Every remaining seed or later refinement channel has base-2 order divisible by 36. Indeed the initial refinable order is 36, the binary refinements multiply it by powers of 2, and later requested orders are \(2dm\), where \(d=18\cdot2^r12^h\) and \(m\in\{2,3,4,6,12\}\).

The three primes

\[
11,61,331
\]

have base-2 orders \(10,60,30\). None of these orders is among \(4,9,12,18\), and none is a multiple of 36. Therefore these three primes lie outside every constructed S, including all refinement depths. No finite search over the depths is used for this statement.

The unchanged 5 and 13 seed constraints are

\[
a\equiv3\pmod5,\qquad a\equiv1\pmod{13}.
\tag{3}
\]

## 3. Why all three other new observer coordinates are already zero

Among the twenty retained old private exponent indices are 3 and 63. They are private for old channels 17 and 65537 respectively, and remain private under every refinement.

For the private indices \(n_i\), the coprimalization construction forms

\[
D=\operatorname{lcm}_{i<j}(2^{|n_i-n_j|}-1),\qquad
E=D\Big/\prod_{q\in S}q^{v_q(D)}.
\tag{4}
\]

Because \(|63-3|=60\),

\[
2^{60}-1\mid D.
\]

The complete factorization is

\[
2^{60}-1
=3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41\cdot61
\cdot151\cdot331\cdot1321.
\tag{5}
\]

By the order argument above, none of 11, 61 and 331 is stripped out in (4). Thus

\[
11\cdot61\cdot331\mid E.
\tag{6}
\]

The preceding CRT construction already imposes \(E\mid a\). It also imposes \(T_{3,1}\mid a\), with

\[
T_{3,1}=(2^{210}-1)\Big/\prod_{p\in P}p^{v_p(2^{210}-1)},
\]

so \(3\mid a\). No new forcing condition, change of seed, or additional compatibility hypothesis is needed.

Combining (3) and (6), every constructed root satisfies

\[
(a\bmod5,a\bmod13,a\bmod11,a\bmod61,a\bmod331)
=(3,1,0,0,0).
\tag{7}
\]

Exact CRT identifies (7) with \(a\equiv666303\pmod K\).

## 4. Exact cost and full-trajectory equality

For completeness, the coprimalization argument proves the lower bounds as follows. If a prime \(\ell\) divided two private terms, the defining congruences would imply

\[
\ell\mid2^{|n_i-n_j|}-1\mid D.
\]

If \(\ell\in S\), the private-witness property rules this out. Otherwise \(\ell\mid E\mid a\), but then \(F_n(a)\equiv-1\pmod\ell\), again impossible. Thus all \(20+s\) private terms are pairwise coprime. Any full cover requires at least \(20+s\) different primes, while S provides exactly that many. Among these witnesses the s new private terms avoid every old prime, so at least s outside primes are necessary. This proves both exact equalities in (1).

The source construction supplies infinitely many compatible positive roots, and all sufficiently large ones make every assigned divisor proper. The extra observation (7) holds for all of them because it was already enforced by their existing E constraint.

Two roots in (1), even with different values of s, agree modulo each prime in \(P\cup V\). Hence their squares and all values of \(a^22^n-1\) agree in every one of those prime coordinates for every \(n\ge0\). This proves (2) as equality of the full residue values, not just of zero/nonzero indicators and not merely on a finite prefix.

The quantifiers remain

\[
\forall s\ge5\quad\exists^\infty a.
\]

They do not supply a single ordinary integer root with infinite covering cost. Such a conclusion would need an additional argument and is not obtained by making s arbitrarily large across different roots.

## 5. Relation to the optimal-budget observer

The companion observer proof shows that the specific predicates of attaining the universal density bounds at budgets 1 through 4, and of admitting a nested simultaneous optimum through budget 5, factor through a modulo K. At residue 666303 their values are

\[
E_1=E_2=\mathrm{true},\qquad E_3=E_4=N=\mathrm{false}.
\]

The theorem above therefore gives one fixed finite observer fiber on which those predicates are constant but full covering complexity is unbounded. A quotient can be exact for its stated observable while omitting information required by a different question.

In the project-native interpretation, the fixed X6 anchor, typed integer register, positive singleton weight and multiplicity remain unchanged. The scalar update is \(x\mapsto2x+1\). Prime channels observe that state; they do not add axes or branches. The full integer state and joint cofactor information are retained. The lost information is in the chosen projection, not a disappearance of those integer relations.

## 6. Exact finite witnesses

Run `python verify_fixed_observer.py`.

The verifier reconstructs the existing seed CRTs for exact costs 5, 6 and 7 and records their full roots and progression moduli in hexadecimal. Their roots have respectively 9,671, 10,021 and 10,882 decimal digits. It checks all 976 pairwise gcds across the three private-witness families, verifies proper private divisors and old-hole avoidance, and verifies the common residue 666303 modulo K.

The cost-eight root and its previous 378 gcd checks and native execution are reused from the unchanged published certificate; the new check verifies that it also lies in this same larger observer fiber. Its full value remains at that dependency and is not copied into this certificate.

These finite examples illustrate and check the arithmetic construction. The universal all-cost conclusion is the order and divisibility argument in Sections 2–4 together with the established refinement theorem, not an extrapolation from four examples.
