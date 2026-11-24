# All three-prime completions of the fixed R2 prefix

Status: author mathematical proof and exact arithmetic in Research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. These shared-context calculations do not constitute independent project Review, formal acceptance, native BRC execution or Foundation promotion.

## 1. Fixed fiber, scope and result

The sequence is

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1.
\]

Use the old twenty-prime dictionary P and the fixed fiber R2 from commit `f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5`, path `research_notes/portable_direct/riesel_finite_observers_20261124/six/r2_proof.md`. Explicitly,

\[
\begin{aligned}
a_*&=690786768637635218740714348513373826260012289,\\
M&=1397394912916194098609132326092145093313722687204526281,\\
L&=80754838636615,\\
R_2&=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L,\\
&\hspace{42mm}a\equiv0\pmod{433},\quad
a\equiv38733\pmod{38737}\}.
\end{aligned}
\]

This note classifies supplements whose four specified primes are

\[
Q_{\rm prefix}=\{5,13,19,73\}.
\]

The separate prefix arguments are responsible for deciding whether every seven-prime cover must contain these four primes. The result here is exhaustive conditional on that prefix; it imposes no bound on the size of the three further primes.

Put n=2u. The prefix phases are respectively

\[
(d_q,c_q)=(2,1),(6,0),(9,4),(9,1),
\qquad u\equiv c_q\pmod{d_q}.
\]

After the old dictionary and these four channels, all remaining indices have

\[
u=16+18w,\qquad n=32+36w,
\]

where

\[
B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{1}
\]

This is an exact periodic reduction, inherited from the cited source. The remaining exponent density is 13/1260. Prime 433 is inactive; prime 38737 has the fixed phase w=1 mod 2.

**Theorem.** The three-prime completions of (1) are exactly the following three families. Assignments in each row are bijections between the selected primes and the listed phases.

| Family | Tail primes | Required w phases | Phase dictionaries | Sign-specific CRT progressions |
|---|---|---|---:|---:|
| Binary | 38737, 577, 487824887233 | 38737: 1 mod 2; the other two: 0,2 mod 4 | 2 | 8 |
| Ternary | Any three distinct primes in D | 0,1,2 mod 3 | 24 | 192 |
| Modulo five | Any three distinct primes in C | 0,1,3 mod 5 | 120 | 960 |

Here

\[
\begin{aligned}
D&=\{87211,246241,262657,279073\},\\
C&=\{181,631,23311,54001,18837001,29247661\}.
\end{aligned}
\tag{2}
\]

Thus there are **146 phase dictionaries**, realized by **1,160 sign-specific CRT progression descriptions**. The descriptions need not be disjoint as root sets: a root may support more than one dictionary. The family totals must not be added as root densities without accounting for overlap.

The new family relative to the preceding budget-six analysis is D. The earlier modulo-five extension family and the binary example together did not exhaust the seven-prime possibilities.

## 2. Incidence formula and small-period exclusions

For an active odd prime q, its hits on the w progression are either empty or exactly one class modulo

\[
h_q=\operatorname{ord}_q(2^{36}).
\]

Prime 2 never divides F_n(a). If q divides a it is inactive. For a class w=c mod h, let g=gcd(h,35) and

\[
K_g(c)=|\{b\in B:b\equiv c\pmod g\}|.
\]

The exact density relative to B is

\[
\mu_B(w\equiv c\pmod h)
=\frac{K_g(c)}{13(h/g)}.
\tag{3}
\]

This follows by counting the common-period lifts of each compatible residue in (1). It includes all overlap constraints; no probabilistic independence is assumed.

For g=1,5,7,35 the maximal K_g values are 13,5,3,1. In particular,

\[
(K_5(0),\ldots,K_5(4))=(5,3,0,5,0).
\tag{4}
\]

There are no available active period-one channels. The only available active period-two channel is 38737. These statements follow from the complete prime factors of 2^36−1 and 2^72−1, all of which occur in the complete factorization of 2^144−1 below. After excluding P and the already used prefix, the other relevant small-order primes are inactive at the fixed root. In particular 433 divides every root in R2.

Consequently, when 38737 is omitted, the four columns of (3) have upper bounds

\[
\left(\frac13,\frac5{13},\frac3{13},\frac1{13}\right),
\tag{5}
\]

and every channel covers at most 5/13 of B.

## 3. Complete reduction when 38737 is omitted

Suppose three channels cover B and none is 38737. If any one of them covered less than 3/13, the other two, each bounded by 5/13, could not complete the cover. Thus every channel has relative density at least

\[
1-2\cdot\frac5{13}=\frac3{13}.
\tag{6}
\]

Combine (6) with the four gcd columns of (3).

* If g=1, then 1/h is at least 3/13, so h is at most 4. Periods one and two have been excluded, leaving h=3 or 4.
* If g=5, then 5/[13(h/5)] is at least 3/13, which forces h/5=1 and h=5.
* If g=7, then 3/[13(h/7)] is at least 3/13, which forces h=7.
* If g=35, the upper bound is only 1/13, so this column is impossible.

Thus the all-prime problem has already reduced to

\[
\boxed{h\in\{3,4,5,7\}}.
\tag{7}
\]

This is an analytic necessity, not a search cutoff.

### 3.1 Period four is impossible

A period-four channel covers 1/4 of B. If either of the other channels has period other than five, the total union bound is at most

\[
\frac14+\frac5{13}+\frac13=\frac{151}{156}<1.
\]

Therefore both other channels would have to have period five. Two classes modulo five cover at most ten of the thirteen residues of B, so some whole class w=b mod 35 remains. Since gcd(4,35)=1, its lifts run through all four classes modulo four. One period-four channel cannot fill it. Hence h=4 cannot occur.

### 3.2 Period seven is impossible

A period-seven channel covers at most 3/13. Covering all of B requires both remaining channels to attain 5/13, because

\[
\frac3{13}+\frac5{13}+\frac5{13}=1.
\]

By (4), they must occupy the two distinct maximal period-five classes 0 and 3. The residual B positions are then

\[
21,26,31\pmod{35}.
\tag{8}
\]

Their residues modulo seven are 0,5,3. A single class modulo seven cannot contain all three. Thus h=7 is impossible.

### 3.3 Periods three and five cannot be mixed

Only h=3 and h=5 remain. If a triple uses both periods, its one or two period-five channels leave at least one B residue b mod 35 uncovered. By gcd(3,35)=1, the lifts of that residue visit every class modulo three. The available one or two period-three channels cannot cover all three classes. This excludes every mixed triple.

A pure period-three triple must use all phases 0,1,2, once each. A pure period-five triple must use precisely the occupied B classes 0,1,3, once each. These conditions are also sufficient. Section 5 identifies all primes capable of the required effective orders.

## 4. Complete reduction when 38737 is used

The fixed channel 38737 covers w odd. For the remaining w even, put w=2z. The residual z set is a multiplication of B by the inverse of 2 modulo 35. Its incidence maxima remain 13,5,3,1.

The effective order of a further prime on this restricted progression is

\[
e_q=\operatorname{ord}_q(2^{72}).
\]

There is no available period-one prime: all factors of 2^72−1 are old, already used or inactive. Formula (3), with z replacing w, then bounds a new channel by 1/2 of this remainder. Equality requires e=2, since the other gcd columns have maxima 5/13,3/13,1/13, all smaller than 1/2.

Two remaining channels can cover the whole remainder only if both attain 1/2 and use opposite z parities. Therefore both satisfy e=2. The complete factorization of 2^144−1 leaves exactly the two primes

\[
E=\{577,487824887233\}
\]

after the stated exclusions. Both have exact base-two order 144. Opposite z parities are exactly w=0 and w=2 mod 4. This gives the two binary dictionaries and excludes every other triple containing 38737.

## 5. Exact finite arithmetic identifying the primes

The calculator verifies the following complete products and the primality of every displayed factor by deterministic trial division:

\[
\begin{aligned}
2^{108}-1={}&3^4\cdot5\cdot7\cdot13\cdot19\cdot37\cdot73\cdot109\\
&\cdot87211\cdot246241\cdot262657\cdot279073;\\
2^{144}-1={}&3^3\cdot5\cdot7\cdot13\cdot17\cdot19\cdot37\cdot73\\
&\cdot97\cdot109\cdot241\cdot257\cdot433\cdot577\cdot673\\
&\cdot38737\cdot487824887233;\\
2^{180}-1={}&3^3 5^2\cdot7\cdot11\cdot13\cdot19\cdot31\cdot37\cdot41\\
&\cdot61\cdot73\cdot109\cdot151\cdot181\cdot331\cdot631\cdot1321\\
&\cdot23311\cdot54001\cdot18837001\cdot29247661.
\end{aligned}
\tag{9}
\]

If h=3, then ord_q(2) divides 108. Removing excluded factors of the first line of (9) leaves exactly D. If h=5, the base-two order divides 180, and the third line leaves exactly C. For the binary case e=2, the base-two order divides 144 but not 72; the second line leaves exactly E.

The exact base-two orders and resulting w orders are:

| Prime q | ord_q(2) | ord_q(2^36) |
|---:|---:|---:|
| 87211 | 54 | 3 |
| 246241 | 108 | 3 |
| 262657 | 27 | 3 |
| 279073 | 108 | 3 |
| 181 | 180 | 5 |
| 631 | 45 | 5 |
| 23311 | 45 | 5 |
| 54001 | 180 | 5 |
| 18837001 | 90 | 5 |
| 29247661 | 180 | 5 |
| 577 | 144 | 4 |
| 487824887233 | 144 | 4 |

For each claimed order t, the verifier checks 2^t=1 mod q and 2^(t/p)≠1 mod q for each prime p dividing t. No unverified probable-prime or inferred-order input remains in the certificate.

## 6. Realization, complete periods and counts

For a prime q assigned the phase b, put

\[
d_q=\operatorname{ord}_q4,\qquad
c_q\equiv16+18b\pmod{d_q}.
\]

Its phase is realized by the two root residues

\[
a\equiv\pm2^{-c_q}\pmod q.
\tag{10}
\]

Different indicated w phases give disjoint root-residue pairs. All free primes in (2) and E are coprime to the fixed R2 progression step. Hence CRT realizes every listed assignment with every independent sign choice.

For D, the complete root pairs are especially small to display. The listed pair is the two possible residues of a modulo q.

| q | w=0 mod 3 | w=1 mod 3 | w=2 mod 3 |
|---:|---:|---:|---:|
| 87211 | 2048,85163 | 2044,85167 | 4,87207 |
| 246241 | 63608,182633 | 63612,182629 | 4,246237 |
| 262657 | 2048,260609 | 2052,260605 | 4,262653 |
| 279073 | 67720,211353 | 67716,211357 | 4,279069 |

The dictionary counts are

\[
2,\qquad 4\cdot3\cdot2=24,\qquad6\cdot5\cdot4=120.
\]

Only the binary family has two free primes; its third prime 38737 is fixed in R2. Its two dictionaries each have four independent sign choices. The other dictionaries each have eight. Thus

\[
2\cdot4+24\cdot8+120\cdot8=1160.
\]

The complete w periods are respectively 140,105,35, giving complete exponent coverage periods 5040,3780,1260. These are sufficient periods of the coverage predicate after the old dictionary, not claims about the least period of every individual prime-value readout.

The verifier enumerates every stated dictionary over its complete w period, checks zero uncovered positions and positive private coverage for each tail prime, and evaluates every one of the 1,160 sign-specific CRT starts. There is no extrapolation from an initial interval.

## 7. Scoped minima and exact supplementary cost

Write R2 as a positive progression with start and step

\[
\begin{aligned}
A_2&=9807947978443488306255509703402695727949968778703073231931137913705883712843,\\
S_2&=11356718000553566643685496313583434507970452519839503606327232707476034989690.
\end{aligned}
\]

Every additional phase/sign prescription is one progression modulo S2 times its selected free primes. Comparing its least positive CRT representatives gives:

| Family | Least positive root in that family | Digits |
|---|---|---:|
| Binary | 142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303 | 90 |
| Ternary | 1046533155647696956851681902279650889819246480725727047415947079817885251912744029965820233 | 91 |
| Modulo five | 168515727251568031139784117408423468924151126118048106286760549300706338389494633573 | 84 |

The minimum over the three families is therefore the previously obtained modulo-five minimum. In this note its scope is all seven-prime supplements containing the stated prefix. A separate proof that every seven-prime supplement contains the prefix upgrades it to the minimum of all roots in R2 with supplementary cost seven.

The cited v10 result proves every six-prime supplement on R2 leaves exponent density at least 1/420. Each root supporting any dictionary here therefore has

\[
\delta_P(a)=7.
\]

Every divisor assigned in these compact examples is proper: the minimum positive term 2a²−1 exceeds every displayed prime. These dictionaries imply the total cover bound tau(a²)≤27. No equality for the total minimum is inferred merely from the supplementary minimum; the separate coprimalization construction has different hypotheses and scope.

## 8. Reproduction and interpretation

Run

```sh
python verify_tail.py
```

This writes `tail_certificate.json`. In addition to (9), exact orders, phase/root tables and CRT counts, it checks all reduced three-class patterns with h in {3,4,5,7} over their full common periods. Only the pure ternary and pure modulo-five patterns survive. This enumeration confirms the reduced arithmetic after Sections 2–4 have proved the all-prime reduction.

The native state remains the fixed-X6 typed integer register, positive singleton BRC weight and multiplicity one, with update x↦2x+1 and even composition 4x+3. The coordinate w indexes specified integer states. Prime phases are readouts of that state, not additional axes. The result classifies three ways of completing the residual covering task while retaining the full integer and joint cofactor information. It neither changes the native state space nor substitutes finite readouts for that complete information.
