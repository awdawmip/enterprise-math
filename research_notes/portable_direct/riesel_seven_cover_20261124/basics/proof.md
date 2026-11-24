# The basic pair 5 and 13 is forced in every seven-prime completion

Status: author mathematical derivation and exact small arithmetic in the existing Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. Shared-context verification is not an independent project Review or formal acceptance.

## 1. Statement and inherited objects

Retain the square-Riesel sequence

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the old twenty-prime dictionary P and the fixed 29-channel root fiber R1 from the [complete-six proof](https://github.com/awdawmip/enterprise-math/blob/f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5/research_notes/portable_direct/riesel_finite_observers_20261124/six/proof.md). In particular,

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

The fixed root residues at \((5,13,11,61,331,19,37,73,109)\) are

\[
(3,1,0,0,0,6,0,37,0),
\]

and \(3\mid a\). Thus 3,11,61,331,37,109 are inactive. Writing n=2u, the fixed phases of 5,13,19,73 are respectively

\[
u\equiv1\pmod2,\quad0\pmod6,\quad4\pmod9,\quad1\pmod9.
\tag{1}
\]

The 31-channel fiber R2 additionally fixes \(a\equiv0\pmod{433}\) and \(a\equiv38733\pmod{38737}\). The proof below does not need those two extra conditions: it already holds throughout R1.

**Theorem.** For every \(a\in R_1\), every complete supplementary prime dictionary Q with \(Q\cap P=\varnothing\) and \(|Q|\le7\) contains both 5 and 13. In particular, every complete seven-prime supplement in R2 contains this basic pair. Here completeness means that every exponent left uncovered by P is covered by some prime in Q; a prime that divides a is inactive, and 2 is inactive because every \(F_n(a)\) is odd.

This necessity result concerns all primes and all multiplicative orders. It makes no prime-size cutoff and does not by itself classify the remaining five primes.

## 2. Old-hole incidences

The old dictionary covers every odd exponent. Its even-index holes are the 36 residues

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}
\pmod{105}.
\end{split}
\]

They have density \(6/35\) among all positive n. On either u-parity, write \(u=\epsilon+2z\). Since 2 is invertible modulo 105, the old holes become an affine copy \(H_\epsilon\) of H with the same incidence maxima:

| \(g\mid105\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Maximum number of compatible hole residues | 36 | 23 | 11 | 7 | 6 | 4 | 2 | 1 |

For a nonempty channel on the parity fiber, its effective z-period is

\[
e_q=\operatorname{ord}_q16.
\]

A z-class modulo e, with \(g=\gcd(e,105)\), covers relative density at most

\[
\frac{K_g}{36(e/g)}
\tag{2}
\]

inside the parity's old holes. This is exact CRT counting over the common period; no statistical independence is assumed. The old holes on either parity have density \(3/35\) among all positive exponent indices.

The old-hole formula, incidence table, exclusions of effective periods 1 through 6, and the global bound used in Section 3 are inherited from the [complete-five proof](https://github.com/awdawmip/enterprise-math/blob/b1de1acbdc97b5e51d486127abd1fadd24babd99/research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md), Sections 1–2. The new refinement is the effective-period exclusion and resulting three-exception bound in Section 4.

## 3. A seven-prime supplement cannot omit both basic primes

Away from old primes and \(\{3,5,11,13,19,43,73,331\}\), the inherited all-prime bound is 1/9 of H. At the fixed R1 phases, 19 and 73 each cover exactly \(13/108\) of H, while 43 covers at most \(7/36=21/108\). The U primes 11,61,331 and 3 are inactive.

Consequently at most seven primes omitting both 5 and 13 cover no more than

\[
\frac{21+13+13+12+12+12+12}{108}
=\frac{95}{108}<1
\tag{3}
\]

of H. Their full-exponent gap is at least

\[
\frac6{35}\left(1-\frac{95}{108}\right)=\frac{13}{630}>0.
\]

Thus at least one basic prime must occur.

## 4. A sharper parity bound with only three exceptional primes

**Lemma.** On either u-parity in R1, every active supplementary prime other than \(5,13,29,43,61681\) covers at most 1/8 of that parity's old holes. The two exceptions 29 and 43 cover at most 7/36 each; 61681 covers at most 11/72.

The proof considers every effective period in (2). The already established small-order exclusion removes e=1 through 6 outside old/basic and inactive primes. The following complete factorizations identify the only further exceptional cases:

\[
\begin{aligned}
2^{28}-1&=3\cdot5\cdot29\cdot43\cdot113\cdot127,\\
2^{36}-1&=3^3\cdot5\cdot7\cdot13\cdot19\cdot37\cdot73\cdot109,\\
2^{40}-1&=3\cdot5^2\cdot11\cdot17\cdot31\cdot41\cdot61681,\\
2^{48}-1&=3^2\cdot5\cdot7\cdot13\cdot17\cdot97\cdot241\cdot257\cdot673,\\
2^{60}-1&=3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41\cdot61
\cdot151\cdot331\cdot1321.
\end{aligned}
\tag{4}
\]

The first two factorizations were already used in the complete-six proof. The final three supply the new sharpening.

- At e=7, the only eligible primes are 29 and 43; both have exact effective order seven. Formula (2) gives \(7/36\).
- At e=9, the only eligible primes are 19,37,73,109. The primes 37 and 109 are inactive. Both active fixed phases in (1) have u congruent to 1 modulo 3. Therefore each of 19 and 73 covers exactly \(13/108<1/8\) inside either u-parity.
- At e=10, (4) leaves only 61681 outside old/basic and inactive primes. It has exact base-2 order 40, hence exact effective order ten, and its capacity is at most \(11/72\).
- At e=12, every factor in (4) is old/basic or inactive, so no available supplementary channel has that period.
- At e=15, every factor in (4) is old/basic or inactive, so this period is excluded as well.

After the three exceptional primes 29,43,61681 are removed, all remaining effective periods satisfy the following bounds. In the gcd-3 column, the fixed e=9 case is kept separately; e=12 has just been excluded, and the next possible period is at least 18.

| \(g=\gcd(e,105)\) | Eligible period information | Coverage upper bound |
|---:|---|---:|
| 1 | \(e\ge8\) | \(1/8\) |
| 3 | e=9 with fixed phases; otherwise \(e\ge18\) | \(\max(13/108,23/216)=13/108\) |
| 5 | e=10 removed, so \(e\ge20\) | \(11/144\) |
| 7 | e=7 removed, so \(e\ge14\) | \(7/72\) |
| 15 | e=15 excluded, so \(e\ge30\) | \(1/12\) |
| 21 | \(e\ge21\) | \(1/9\) |
| 35 | \(e\ge35\) | \(1/18\) |
| 105 | \(e\ge105\) | \(1/36\) |

Every entry is at most 1/8. This proves the lemma over all primes and orders. Inactive primes contribute zero and obey the same bound.

## 5. Exactly one basic prime is impossible with seven slots

Suppose Q contains exactly one of 5 and 13. Its channel is contained in one u-parity by (1), and misses the other parity entirely. At most six other channels must cover all old holes on that missed parity.

The lemma allows at most two distinct exceptions with capacity 7/36, one exception with capacity 11/72, and at most three further contributions of capacity 1/8. If an exception is absent, replacing it by the generic bound only decreases this upper estimate. Thus the total union covers no more than

\[
2\frac7{36}+\frac{11}{72}+3\frac18
=\frac{11}{12}<1.
\tag{5}
\]

At least 1/12 of the missed parity's holes remain. In the full exponent variable this gives the positive gap

\[
\frac3{35}\cdot\frac1{12}=\frac1{140}.
\tag{6}
\]

This excludes exactly one basic prime. Together with Section 3 it proves that both 5 and 13 occur in every complete supplement of at most seven primes throughout R1, hence throughout R2.

The estimate does not need to be sharp. It is a strict uniform obstruction sufficient for the forced-pair theorem. In R2 the previously proved six-budget gap is positive, so a complete dictionary of at most seven primes has exactly seven primes; the present theorem fixes two of them.

## 6. Arithmetic and native scope

Run `python verify_basics.py`. The calculator checks the complete factorization identities used above by exact multiplication and deterministic trial primality, the exact orders of 29,43,61681 and the e=9 candidate list, the two fixed phase contributions on both complete parity periods, the incidence maxima, and the strict rational union bounds. Its certificate records the proven exclusions and their scope.

The finite calculations certify the explicit factorization and density inputs. The all-prime conclusion is the eight-column analytic argument; it is not inferred by enumerating a bounded list of primes.

The native state remains the fixed-X6 typed integer register, with positive singleton BRC weight and multiplicity one and update \(x\mapsto2x+1\). The parity coordinate is an arithmetic restriction of the exponent. Prime residues are observations of that integer state, and the full integer and joint cofactor relations are retained. No new native execution is required for this strengthened analytic exclusion, and none is claimed in this note.
