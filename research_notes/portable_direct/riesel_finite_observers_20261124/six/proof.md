# Complete six-prime classification on the fixed twenty-nine-channel R1 fiber

Status: author mathematical proof with exact supporting arithmetic. Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is a continuation of the existing direct research, not an independent project Review or formal admission.

## 1. The exact statement

Retain

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

\[
a_*=690786768637635218740714348513373826260012289,
\]

and the old prime dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

Its product is

\[
M=1397394912916194098609132326092145093313722687204526281.
\]

Write

\[
U=\{11,61,331\},\quad V=\{5,13\}\cup U,\quad
W=\{19,37,73,109\},
\]

\[
L=\prod_{q\in V\cup W}q=80754838636615.
\]

The fixed fiber is

\[
R_1=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L\}.
\tag{1}
\]

Its root residues at \((5,13,11,61,331,19,37,73,109)\) are

\[
(3,1,0,0,0,6,0,37,0).
\tag{2}
\]

Thus 3, the three primes of U, 37 and 109 divide the root and are inactive. The active fixed new channels have even-index phases

\[
(q,d_q,c_q)=(5,2,1),(13,6,0),(19,9,4),(73,9,1),
\qquad d_q=\operatorname{ord}_q4.
\tag{3}
\]

A complete supplement is a set Q of distinct primes outside P such that P together with Q supplies a proper prime divisor of every positive-index term. Let \(\delta_P(a)\) be the smallest possible cardinality of Q, with infinity if no finite supplement exists. Let \(\tau(a^2)\) denote the minimum total number of covering primes; adding the whole old dictionary does not change the supplementary minimum.

**Theorem.** For every \(a\in R_1\), any complete supplement of at most six primes has exactly six primes, and its prime set is

\[
\boxed{Q_*=\{5,13,19,73,433,38737\}.}
\tag{4}
\]

The last two phases, modulo 36 in u, must be either

\[
(c_{433},c_{38737})=(16,34)
\quad\text{or}\quad(34,16).
\tag{5}
\]

Both phase dictionaries occur. Consequently every six-prime complete supplement in R1 can be ordered into a simultaneous optimum for all budgets zero through six. The previously classified nested family is now proved to be the complete cost-six family in R1.

This statement imposes no upper cutoff on prime size or multiplicative order. It is confined to the fixed fiber (1), and does not classify cost-six roots in other old-class fibers or all Riesel coefficients.

The reused sources are the round-nine proofs at commit `b1de1acbdc97b5e51d486127abd1fadd24babd99`:

- `research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md`, for the all-prime old-hole incidence bounds and complete small-order exclusions;
- `research_notes/portable_direct/riesel_five_cover_20261123/fiber/proof.md`, for the exact R1 trajectory, residual fibers, sharp density staircase and the earlier nested six-channel computation.

The new necessity argument is given in Sections 3–5. The old nested calculation is reused only after that argument proves the equality of the two classes.

## 2. Incidence data and the hierarchy of residual fibers

The old dictionary covers every odd exponent. Writing \(n=2u\), its uncovered residues modulo 105 are

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}.
\end{split}
\]

The counts in the u-classes modulo 3 are 23, 13 and 0. For

\[
g\in(1,3,5,7,15,21,35,105),
\]

the maximum number of H residues in one class modulo g is

\[
(36,23,11,7,6,4,2,1).
\tag{6}
\]

For a periodic set A of size m modulo N, a class \(x\equiv c\pmod d\) has relative density

\[
\rho_A(c,d)=\frac{K_g(c)}{m(d/g)},\qquad
g=\gcd(d,N),\quad K_g(c)=|\{h\in A:h\equiv c\pmod g\}|.
\tag{7}
\]

This follows by counting in the common period \(Nd/g\). It applies to every positive d. All union bounds below use actual intersection densities; no probabilistic independence is assumed.

After the fixed channels 5 and 13, the remaining indices have

\[
u=4+6v,\qquad
v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{8}
\]

For divisors \((1,5,7,35)\), A has incidence maxima \((13,5,3,1)\). Prime 19 covers \(v\equiv0\pmod3\), and prime 73 covers \(v\equiv1\pmod3\). After both, the remainder is

\[
v=2+3w,\qquad u=16+18w,
\tag{9}
\]

where w again lies in a 13-element set modulo 35 with the same incidence maxima. The transformations in (8) and (9) are invertible on the appropriate residual periods.

## 3. Every complete six-prime supplement contains 5 and 13

### 3.1 Omitting both basic primes is impossible

The round-nine all-prime bound states that outside P and \(\{3,5,11,13,19,43,73,331\}\), any active prime covers at most 1/9 of H. In R1 the U primes are inactive. Moreover the phases of 19 and 73 in (3) both satisfy \(u\equiv1\pmod3\). Each therefore covers exactly

\[
\frac{13}{108}
\]

of H, rather than the unrestricted maximum \(23/108\). Prime 43 covers at most \(7/36=21/108\).

Thus any six distinct new primes omitting both 5 and 13 cover at most

\[
\frac{21+13+13+12+12+12}{108}
=\frac{83}{108}<1.
\tag{10}
\]

The same upper bound covers smaller dictionaries and inactive channels. Hence at least one basic prime occurs.

### 3.2 Having exactly one basic prime is impossible

The sole basic prime misses an entire u-parity. Restrict to that parity, writing \(u=\epsilon+2z\). The old holes become an affine copy of H modulo 105. A compatible prime now has effective period

\[
e_q=\operatorname{ord}_q16.
\]

As already proved in round nine, effective periods 1 through 6 are excluded outside old/basic primes and inactive 11. The resulting general gcd-column bounds are

\[
\left(\frac18,\frac{23}{108},\frac{11}{72},\frac7{36},
\frac16,\frac19,\frac1{18},\frac1{36}\right).
\tag{11}
\]

Only the gcd-3 and gcd-7 columns can exceed 1/6. Both can be sharpened at the actual fixed R1 root.

For gcd 3, the only exceptional period is e=9. The complete factorization of \(2^{36}-1\) shows that the eligible primes with exact effective period 9 are 19, 37, 73 and 109. Of these, 37 and 109 are inactive. The remaining primes 19 and 73 each cover only \(13/108\) inside either u-parity, because their u-phase remains 1 modulo 3. For every other period in this column, e is at least 12, giving \(23/144<1/6\).

For gcd 7, the exceptional period is e=7. Here the relevant complete factorization is

\[
2^{28}-1=3\cdot5\cdot29\cdot43\cdot113\cdot127.
\tag{12}
\]

After old/basic exclusions, the eligible primes are exactly 29 and 43, and both have \(\operatorname{ord}_q16=7\). Each covers at most 7/36 of the parity fiber. All other periods in this column are at least 14, giving at most \(7/72<1/6\).

Every active new prime other than the two exceptions 29 and 43 therefore covers at most 1/6 of the missed parity. At most five remaining channels can cover at most

\[
2\frac7{36}+3\frac16=\frac89<1.
\tag{13}
\]

This rules out exactly one basic prime. Therefore both 5 and 13 must be in every complete supplement of size at most six. Their phases are fixed by R1, so the residual set is exactly (8).

## 4. Both active W primes, 19 and 73, are forced

There are now at most four channels left to cover the 13-position set A in (8). The only active effective-order-3 primes are 19 and 73; 37 and 109 are inactive. For every other active prime, let

\[
f_q=\operatorname{ord}_q(2^{12}).
\]

Effective orders 1, 2 and 4 give only old/basic primes, order 3 gives W, and order 5 gives the inactive U primes. Hence for a non-W channel the four gcd-column bounds from (7) are

\[
\left(\frac16,\frac5{26},\frac3{13},\frac1{13}\right),
\qquad g=1,5,7,35.
\tag{14}
\]

Its contribution is at most 3/13.

If neither active W prime is used, four channels cover at most \(12/13<1\), so this is impossible.

Suppose exactly one active W prime is used. It covers 1/3 of A. With at most two other channels the total is at most \(1/3+6/13<1\), so all three other slots must be present. In a complete cover, each of those three non-W channels must have individual contribution at least

\[
1-\frac13-2\frac3{13}=\frac8{39}.
\tag{15}
\]

In (14), the first, second and fourth entries are strictly smaller than 8/39. In the gcd-7 column, (7) gives \(3/(13(f_q/7))\), so (15) forces \(f_q=7\). The eligible primes are \(29,43,1429,5419\), by the complete factorization of \(2^{84}-1\) already established in round nine.

Each of the three remaining channels is therefore a single v-class modulo 7. Their union covers at most nine of A's thirteen residues modulo 35. Choose an A-residue missed by all three. Because 3 is coprime to 35, it has lifts in every class modulo 3; the one W channel misses two of them. Thus some old holes remain uncovered.

Equivalently, exact coprime-period counting bounds their total union by

\[
\frac13+\frac23\frac9{13}=\frac{31}{39}<1.
\tag{16}
\]

This excludes exactly one active W channel. Both 19 and 73 are therefore forced, leaving precisely the residual set (9).

## 5. The last two primes and their phases are forced

At most two channels remain. On (9), a new active prime has effective period

\[
h_q=\operatorname{ord}_q(2^{36}).
\]

Period 1 gives only old, already used or inactive primes, by the complete factors of \(2^{36}-1\). The four gcd-column bounds for the 13-element w-set are

\[
\left(\frac12,\frac5{13},\frac3{13},\frac1{13}\right).
\tag{17}
\]

Thus each channel covers at most half the remainder. Complete coverage requires exactly two channels, both attaining 1/2 with disjoint contributions. Equality in (17) is possible only at \(h_q=2\).

The factorization

\[
2^{72}-1=(2^{36}-1)(2^{36}+1),
\qquad
2^{36}+1=17\cdot241\cdot433\cdot38737
\tag{18}
\]

leaves precisely the two new primes 433 and 38737. Both have exact base-2 order 72. Their phases on (9) are the two parities of w, hence the two u-classes 16 and 34 modulo 36. They must occupy opposite parities. This proves (4) and (5), including the impossibility of a supplement of size at most five.

The exact root conditions are:

| Prime | u phase 16 modulo 36 | u phase 34 modulo 36 |
|---:|---|---|
| 433 | \(a\equiv150,283\pmod{433}\) | \(a\equiv4,429\pmod{433}\) |
| 38737 | \(a\equiv2677,36060\pmod{38737}\) | \(a\equiv4,38733\pmod{38737}\) |

The phases follow from \(a\equiv\pm2^{-c_q}\pmod q\). Since both new primes are coprime to \(6ML\), CRT realizes every displayed opposite-parity choice in an infinite progression of positive roots in R1. All such roots are at least a*, so all assigned old and new prime divisors are proper. This proves sufficiency as well as necessity.

## 6. Exact observer and minimum corollaries

Put

\[
Z=433\cdot38737=16773121.
\]

For \(a\in R_1\), the theorem gives the exact equivalence

\[
\delta_P(a)=6
\quad\Longleftrightarrow\quad
\begin{cases}
a\bmod433\in\{150,283\},\quad a\bmod38737\in\{4,38733\},\\
\text{or}\\
a\bmod433\in\{4,429\},\quad a\bmod38737\in\{2677,36060\}.
\end{cases}
\tag{19}
\]

There are exactly eight root classes modulo Z, so the relative natural density of cost-six roots inside R1 is \(8/Z\). Both coordinates are essential: place the other prime in one valid phase, and changing the chosen coordinate between the opposite phase and 0 changes the predicate. Hence Z is the least positive additive period in the R1 progression parameter, whose step \(6ML\) is invertible modulo Z.

The eight classes were already completely calculated for the nested predicate in the prior fiber certificate. They are

\[
3215175,\ 4263747,\ 5229491,\ 6278071,\ 10495050,\
11543630,\ 12509374,\ 13557946\pmod Z.
\tag{20}
\]

The prior least nested root therefore becomes the least positive root of **any** additional cost-six cover in R1:

\[
\boxed{
1597463687996365290740241630260436015028835427889255944107518938773290244463.
}
\tag{21}
\]

The eight-class minimum computation and its actual native execution are unchanged and are reused. The new statement is the all-prime necessity theorem identifying that previous class with the whole cost-six class. It does not establish \(\tau(a^2)=26\) for the compact minimum; the displayed cover proves \(\tau(a^2)\le26\). Exact total-cost identities for the separately coprimalized arbitrary-cost construction keep their existing scope.

## 7. Supporting calculation and retained native semantics

Run `python verify_six.py`. The standard-library calculation checks the new factorization (12), exact effective-order candidate sets needed in the sharpened parity argument, the fixed 19/73 densities inside both parity fibers, the new strict rational bounds, the unique high-capacity effective-order possibility in (15), and the two final phase dictionaries over a complete u-period of 1260. It supplies a private old-hole witness for every selected channel and checks the phase-root pairs.

Existing all-prime incidence arguments and previously complete small factorizations are reused at their stated scopes. The old eight-class count, minimum and native execution are explicitly marked as reused results, not a new search or new native run. `six_certificate.json` records the new finite arithmetic and the exact scope of that reuse. The written proof supplies the coverage over all primes and all positive indices.

The native integer state remains \(F_n(a)\), with fixed X6 anchor, positive singleton BRC weight and multiplicity one, and update \(x\mapsto2x+1\). Prime readouts are observations of that state; exponent index is an arithmetic update count. This theorem makes the finite observation sufficient for one cost predicate within R1. It does not replace the full integer state or its joint cofactor information by that finite observation.
