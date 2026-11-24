# The complete budget-eight observer on R3

Research continuation, 2026-11-24 (Asia/Hong_Kong). Author derivation and exact
arithmetic with shared-context mathematical collaboration. Researcher
`EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is not an
independent project Review or a new native BRC execution.

## 1. Native object, fixed fiber and theorem

The original state is the full typed integer register at the fixed Heartbeat X6
anchor, with positive singleton BRC weight and multiplicity one:

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1.
\]

Residue channels observe that integer. The arguments retain its joint
divisibility relations. Let P be the original twenty-prime dictionary, and let
\(\delta_P(a)\) be the minimum number of additional primes in a complete
proper-prime cover. Infinity denotes absence of a finite cover.

Retain exactly the fixed 43-prime fiber R3 of the
[preceding source](https://github.com/awdawmip/enterprise-math/blob/5cfe4d64429f284232029341c6ba774e2eb6f727/research_notes/portable_direct/riesel_eight_spectrum_20261124/fiber/proof.md).
It is the positive progression \(a=A_3+S_3j\), \(j\ge0\), where

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The complete seven-cover result gives \(\delta_P(a)\ge8\) throughout R3.
The companion prefix and tail proofs now classify all eight-prime supplements.
They are the mathematical completeness input of this note; the finite residue
counts below do not supply that all-prime classification by themselves.

Write \(J_8(a)\) for the predicate that a complete eight-prime supplement
**containing all four primes \(5,13,19,73\)** exists. Write \(Z_8(a)\) for
the branch that omits both 19 and 73. The one-of-two branch is impossible. Thus

\[
\boxed{\delta_P(a)=8\iff\delta_P(a)\le8
\iff J_8(a)\lor Z_8(a),\qquad a\in R_3.}
\tag{1}
\]

The two predicates use disjoint sets of respectively twelve and nineteen free
prime coordinates. Let \(T_8\) be the product of these 31 primes, listed below.
All are coprime to \(S_3\).

**Complete observer theorem.** For every positive integer N, each of the
following is equivalent to \(T_8\mid N\):

* the root residue \([a]_N\) determines \(\delta_P(a)\le8\) throughout R3;
* the complete future residue sequence \(([F_n(a)]_N)_{n\ge1}\) determines
  that predicate throughout R3.

Every one of the 31 prime coordinates is essential. Under the maximum
base-two-prime-order metric,

\[
\boxed{\Omega_8(R_3)=\widehat\Omega_8(R_3)=420.}
\tag{2}
\]

The count is 31 additional prime or prime-power channels, or 74 including the
43 fixed channels. A single observation modulo the composite number \(T_8\)
packages those 31 additional coordinates.

## 2. The two branches as explicit finite predicates

### 2.1 The four-prefix branch

After P and \(5,13,19,73\), write \(n=32+36w\). Define three disjoint sets:

\[
\begin{aligned}
\mathcal B&=\{193,1153,6337,22253377,38941695937,278452876033\},\\
\mathcal D&=\{33975937,138991501037953\},\\
\mathcal C&=\{61681,4562284561,168692292721,469775495062434961\}.
\end{aligned}
\tag{3}
\]

For a prime q and listed w-phase b, its two root residues are

\[
\mathcal R_{q,b}=\{2^{-(16+18b)},-2^{-(16+18b)}\}\pmod q.
\tag{4}
\]

Let \(E_{\mathcal B}\) require that phases 0 and 4 are both present among
the \(\mathcal B\) coordinates; let \(E_{\mathcal D}\) require phases 0 and
2 among \(\mathcal D\); let \(E_{\mathcal C}\) require phases 0,6,8 among
\(\mathcal C\). A phase is present when at least one coordinate has its root
residue in (4). Categories at one prime are disjoint, so different required
phases automatically require different primes. The tail theorem gives

\[
J_8=E_{\mathcal B}\lor E_{\mathcal D}\lor E_{\mathcal C}.
\tag{5}
\]

The respective fixed tail support is \(38737,487824887233\),
\(38737,246241\), and 38737. These fixed coordinates are already known in R3.

### 2.2 The branch omitting 19 and 73

After P,5,13 write \(n=8+12v\). The residual v set is

\[
A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{6}
\]

Its occupied residue classes modulo seven are \(\{1,2,3,4,5\}\). Define

\[
\mathcal G=\{29,43,1429,5419\},\qquad
\mathcal H=\{3361,15790321,88959882481\},
\tag{7}
\]

\[
\mathcal I=\{211,421,86171,106681,122921,152041,664441,1564921,
7416361,47392381,146919792181,1041815865690181\}.
\tag{8}
\]

Their effective v-orders are respectively 7,14,35. For their phase b put

\[
\mathcal V_{q,b}=\{2^{-(4+6b)},-2^{-(4+6b)}\}\pmod q.
\tag{9}
\]

For \(c\in\{1,2,3,4,5\}\), let \(G_c\) mean that all four primes in
\(\mathcal G\) occupy different phases, exactly the four occupied classes
other than c. These five events are mutually exclusive: four distinct phases
leave a unique missing class.

Let \(H_c\) require phases c and c+7 among the three \(\mathcal H\)
coordinates. For c=1 let \(I_1\) require phases 1 and 22 among
\(\mathcal I\), and for c=5 let \(I_5\) require phases 12 and 26. For
c=2,3,4 set \(I_c=\mathrm{false}\). These special pairs are exactly the two
A points in the indicated class modulo seven. Then the prefix theorem gives

\[
Z_8=\bigvee_{c=1}^5\bigl(G_c\land(H_c\lor I_c)\bigr).
\tag{10}
\]

The 31 free primes are precisely the union of (3), (7), and (8). Equations
(5), (10), and (1) are the full budget-eight predicate.

## 3. Exact frequency, with all overlaps counted

For a set of prime coordinates \(\mathcal X\) and k disjoint required phase
categories, each containing two root residues at every coordinate, the number
of residue vectors containing all k categories is

\[
C_k(\mathcal X)=\sum_{j=0}^k(-1)^j\binom kj
\prod_{q\in\mathcal X}(q-2j).
\tag{11}
\]

This is inclusion-exclusion on missing categories. The checker also counts it
by a weighted category-mask recurrence, giving an independent arithmetic
calculation of the same finite count.

Put

\[
U_X=\prod_{q\in\mathcal X}q\quad
(\mathcal X=\mathcal B,\mathcal D,\mathcal C),
\]

\[
N_B=C_2(\mathcal B),\quad N_D=C_2(\mathcal D)=8,\quad
N_C=C_3(\mathcal C),\qquad U=U_BU_DU_C.
\]

The three events in (5) use disjoint prime sets. Thus

\[
N_J=U-(U_B-N_B)(U_D-N_D)(U_C-N_C).
\tag{12}
\]

For the zero-W branch put

\[
V_7=\prod_{q\in\mathcal G}q,\quad
V_{14}=\prod_{q\in\mathcal H}q,\quad
V_{35}=\prod_{q\in\mathcal I}q,\quad V=V_7V_{14}V_{35},
\]

\[
N_{14}=C_2(\mathcal H),\qquad N_{35}=C_2(\mathcal I).
\]

For each missing c, exactly \(4!\,2^4=384\) root vectors at \(\mathcal G\)
realize \(G_c\). If c=2,3,4, the completion count on the other coordinates
is \(N_{14}V_{35}\). If c=1 or 5, it is

\[
N_{14}V_{35}+N_{35}V_{14}-N_{14}N_{35}.
\]

The five \(G_c\) events are disjoint, so the exact count is

\[
\boxed{N_Z=384\bigl(5N_{14}V_{35}+2N_{35}V_{14}
-2N_{14}N_{35}\bigr).}
\tag{13}
\]

Finally J and Z use disjoint free-prime sets. With \(T_8=UV\), the complete
budget-eight count is

\[
\boxed{N_8=T_8-(U-N_J)(V-N_Z).}
\tag{14}
\]

Because \(\gcd(S_3,T_8)=1\), uniform residue counting modulo \(T_8\) is the
exact natural frequency along the positive R3 progression. Consequently

\[
\boxed{\lim_{X\to\infty}
\frac{|\{a\le X:a\in R_3,\ \delta_P(a)=8\}|}
{|\{a\le X:a\in R_3\}|}
=\frac{N_8}{T_8}
\approx0.0000435545391699103709469567710912452495191598684430.}
\tag{15}
\]

Selected intermediate values are:

| Event | Exact definition of frequency | Decimal |
|---|---|---|
| Four-prefix success J | \(N_J/U\) | 0.0000435545318369500170388017925192803037627534215572 |
| Zero-W success Z | \(N_Z/V\) | \(7.33327975147455983819709598918882667934086074\times10^{-12}\) |
| Zero-W success with J false | \((U-N_J)N_Z/T_8\) | \(7.33296035390815497857196494575640644688584330083\times10^{-12}\) |

These are frequencies within R3. The full integer numerator, denominator,
reduced fraction, each family count and the four disjoint J/Z states are in
`eight_observer_certificate.json`. Formula (14), rather than addition of CRT
progression descriptions, handles both within-family and between-family
overlaps.

## 4. All 31 coordinates are necessary

Every construction below changes one free prime q and leaves all other free
coordinates fixed. All omitted coordinates are set to root residue zero.

* If q is in \(\mathcal B,\mathcal D\), or \(\mathcal C\), make the other
  two J families false. Use companion coordinates in q's family to supply all
  but one required phase, and let q supply the last. Set all \(\mathcal G\)
  coordinates to zero, making Z false. Changing q to zero switches (1).
* If q is in \(\mathcal G\), give the other three G coordinates phases 2,3,4,
  give q phase 5, and use two H coordinates in phases 1 and 8. This makes
  \(G_1\land H_1\) true. Changing q to zero leaves fewer than four G phases,
  so Z fails. Set all J coordinates to zero.
* If q is in \(\mathcal H\), make \(G_2\) true. Give another H coordinate
  phase 2 and q phase 9. For c=2 the I alternative is absent, so changing q to
  zero switches Z. Set all J and other H coordinates to zero.
* If q is in \(\mathcal I\), make \(G_1\) true. Set all H coordinates to
  zero, give another I coordinate phase 1 and q phase 22. Changing q to zero
  switches Z. Set all J and other I coordinates to zero.

The complete classification makes these true/false statements about the full
budget predicate, including all possible supplementary primes, rather than
only about the selected dictionaries.

All assignments are realized in R3 by CRT. Section 6 below adds the same two
order-432 coordinates to both assignments; both outcomes then have finite
exact costs, respectively eight and nine. The certificate contains positive
integer representatives for every one of these 31 pairs and checks the
predicates and coordinate congruences exactly.

Among the 76 displayed prime coordinates (43 historically fixed, 31 free
observer coordinates, and the two added order-432 coordinates), each such
pair differs at exactly q. Consequently, **75 prime residue trajectories
agree for all future n**. The certificate lists the common coordinates and
the single differing coordinate for every pair; this counts only the
displayed universe and makes no assertion about all other primes.

## 5. Every sufficient modulus and the sharp order threshold

If \(T_8\mid N\), equations (5), (10), and (1) give the budget decision from
\([a]_N\).

Conversely, let \(q\mid T_8\) but \(q\nmid N\). Use the essential-coordinate
assignment just constructed and choose a positive true root \(a_+\in R_3\).
The modulus

\[
K=\operatorname{lcm}(S_3,N,T_8/q,Q_{432})
\]

is coprime to q, where \(Q_{432}\) is the product of the two distinct primes
in Section 6. CRT gives a positive root \(a_-\) satisfying

\[
a_-\equiv a_+\pmod K,\qquad a_-\equiv0\pmod q.
\tag{16}
\]

It has the opposite budget truth value, while its root residue modulo N is
identical. This excludes sufficiency of N. The construction permits arbitrary
powers of the other primes in N; increasing their precision cannot supply the
missing q coordinate. The additional order-432 coordinates are held fixed, so
the two roots have finite exact costs eight and nine.

Equal root residues give equal entire future trajectories, proving necessity
for that observer as well. For sufficiency, the odd divisor \(T_8\) allows

\[
a^2\equiv2^{-1}(F_1(a)+1)\pmod{T_8}.
\]

Every category in (4) and (9) is a sign pair and is determined by this square.
Thus the full future trajectory decides the same predicate exactly when
\(T_8\mid N\).

The exact base-two orders are:

| Group | Prime orders in the order listed in (3), (7), (8) | Maximum |
|---|---|---:|
| B | 96,288,288,96,288,288 | 288 |
| D | 216,216 | 216 |
| C | 40,120,360,360 | 360 |
| G | 28,14,84,42 | 84 |
| H | 168,56,168 | 168 |
| I | 210,420,70,105,35,105,210,210,140,140,420,420 | 420 |

Every sufficient N contains a prime of order 420. Taking \(N=T_8\) attains
maximum order 420, proving (2).

The smallest additional sufficient root modulus is \(T_8\). The least
positive period in the R3 progression parameter j is also \(T_8\), since
\(S_3\) is invertible modulo it: a smaller period would, after taking its
gcd with \(T_8\), omit an essential prime coordinate. A root translation that also preserves the
fixed R3 progression has least positive period \(S_3T_8\). These three
statements keep their different domains explicit.

## 6. Two high-order channels provide a universal nine-cover on a subfiber

Within R3, the seven fixed active supplementary channels are

\[
\{5,13,19,73,38737,246241,487824887233\}.
\]

After the four-prefix reduction, 38737 covers odd w, 487824887233 covers
\(w=2\pmod4\), and 246241 covers \(w=1\pmod3\). Their complement is

\[
w\equiv0,8\pmod{12}.
\tag{17}
\]

The two primes

\[
q_0=209924353,\qquad q_8=4261383649
\tag{18}
\]

have exact base-two order 432. The checker proves primality by trial division
through their integer square roots and verifies \(2^{432}=1\),
\(2^{216}\ne1\), and \(2^{144}\ne1\) modulo each. Thus their effective
w-order is twelve. Fix

\[
a\equiv2^{-16}\pmod{q_0},\qquad
a\equiv2^{-160}\pmod{q_8}.
\tag{19}
\]

These cover the two classes in (17), giving a complete nine-prime supplement.
The primes (18) are distinct from all 74 fixed or newly essential observer
coordinates. Therefore (19) can be imposed together with any of the finite
assignments in Section 4.

For a true assignment, the full classification gives cost eight. For a false
assignment, it gives cost greater than eight; the nine-cover then gives cost
exactly nine. Thus all essential-coordinate obstructions can be witnessed by
two finite-cost ordinary integer roots.

## 7. The earlier twelve-coordinate prefix observer fails for the full budget

The J predicate alone has least sufficient modulus U and maximum order 360:
its twelve coordinates are independently essential by the first construction
of Section 4. The full predicate requires the other nineteen coordinates too.

Here is a concrete same-observation pair with finite exact costs. Set all
twelve J coordinates to zero. For the cost-eight root, use v-phases

\[
29:2,\quad43:3,\quad1429:4,\quad5419:5\pmod7,
\]

\[
3361:1,\qquad15790321:8\pmod{14}.
\tag{20}
\]

Their root residues are the positive choices \(2^{-(4+6b)}\). Set all other
free coordinates to zero. This is a Z-type eight-cover, using

\[
\{5,13,29,43,1429,5419,3361,15790321\}.
\]

For the cost-nine root, set all 31 free observer coordinates to zero. In both
roots impose the identical two additional coordinates (19). Positive CRT
representatives are:

**Exact cost eight**

```text
391788515469728721084738954256114848630686943762171634986481945773497578501171082022263915672435995255796570755542386791026086623765051499046904994042811847885724386893786966327543715585661657714496283392317096809654251491840261439516332753312655721078998827014980955756417835785690429443110001338344916134469777890593679741501016018882889650962325614529906644747925955393
```

**Exact cost nine**

```text
309457965512310514118802009084014040413367975789004695161723648896562637587561858891790349391146964158056174741665215664733132508662427547296641613723832179035681455853946520911840102916277425759200431293662584148975284009989987572657389628675784422028449540156392538622528361613065635846746285499848736523687627327334270710123572238396597036546837587290595836273765410333
```

Both are 372-digit ordinary integers. They have identical root residues modulo
\(S_3Uq_0q_8\), so their original 43 trajectories, all twelve J trajectories,
and the two new order-432 trajectories agree for every n. In fact, within
the displayed 76-prime universe they differ at just the six coordinates
\(29,43,1429,5419,3361,15790321\). Hence **70 prime residue trajectories
agree for all future n, with exact costs eight and nine**; the named
57-coordinate observation is a subset of these. Their J coordinates are all
zero, so J is false for both roots; Z distinguishes them.

The eight-cover was checked over its complete scalar prime-residue period of
6,720 positions, and the nine-cover over 60,480 positions. Congruence of the
roots, rather than extrapolation from these finite runs, proves the all-future
equality of all 70 listed common observations. The total covering costs of these compact
examples have upper bounds 28 and 29; this note does not claim equality for
their unrestricted total minima.

**An exact one-prime penalty for retaining the four-prime prefix.** Define
\(\delta_P^{Q_0}(a)\) to be the minimum size of a complete supplementary
dictionary required to contain \(Q_0=\{5,13,19,73\}\). For the displayed
cost-eight root, J is false, while the common nine-cover in Section 6 contains
all of \(Q_0\). Therefore the same ordinary integer root satisfies

\[
\boxed{\delta_P(a)=8,\qquad\delta_P^{Q_0}(a)=9.}
\]

The all-prime bifurcation excludes a dictionary containing exactly one of
19 and 73. Hence every eight-prime supplement for this root omits both, and
retaining the four-prime prefix imposes an exact penalty of one prime. This
is a cost comparison for one fixed integer root, not a comparison between
different roots or between density-only approximations.

## 8. An independent finite candidate bound

The following bound uses only the already-proved necessity of 5 and 13, and
does not assume the present complete classification.

**Lemma.** In an inclusion-minimal supplementary dictionary of size at most
eight on R1, every prime other than 5 and 13 satisfies

\[
\operatorname{ord}_q(2^{420})\le32,
\qquad\operatorname{ord}_q2\le13440.
\tag{21}
\]

After P,5,13, the residual sequence has the thirteen progressions
\(n=8+12h+420t\), with \(h\in A\). At most six remaining channels cover them.
Take a private point for one of these channels, on one progression, and let s
be the number of remaining channels, \(s\le6\). Its effective period there is
\(e=\operatorname{ord}_q(2^{420})\). If \(e>2^{s-1}\), it misses the next
\(2^{s-1}\) consecutive positions after its private point. The other at most
s-1 congruence classes cover that interval. The Crittenden–Vanden Eynden
interval theorem makes those classes a complete cover, contradicting privacy.
Thus \(e\le2^{s-1}\le32\). Finally,

\[
\operatorname{ord}_q2
=e\gcd(\operatorname{ord}_q2,420)\le32\cdot420.
\]

In particular all potential free budget-eight primes divide the explicit
finite product

\[
\prod_{e=1}^{32}(2^{420e}-1).
\tag{22}
\]

The exact 31-prime classifier reduces this broad candidate set to the primes
that can actually occur on R3. The two primes (18) have effective order 36 in
(21), so they are automatically excluded from any eight-prime dictionary and
are suitable for the common nine-cover witnesses. No huge product or root from
(22) was generated for this result; the proof and the moderate CRT examples
already supply the necessary evidence.

## 9. Reproduction and evidence scope

Run `python verify_eight_observer.py`. The script is self-contained and uses
only the Python standard library. It verifies exact orders of the 31 inherited
prime coordinates, disjoint root categories, the weighted counts and their
inclusion-exclusion formulas, all five missing-class counts, and the complete
J/Z overlap partition. Primality of the 31-classification inventory is reused
from the companion deterministic certificates; primality of the two new
order-432 primes is checked here.

It also constructs 31 positive true/false CRT pairs, verifies their full finite
predicates, and confirms that each pair agrees at every coordinate other than
the intended one. Both members include the same two order-432 coordinates,
which give a uniform nine-cover. Finally it directly checks the two selected
counterexample covers on complete scalar periods and stores their exact roots.

All-prime completeness rests on the companion prefix/tail proofs. Arbitrary-N
necessity, the all-future observer equivalence, natural-frequency interpretation
and finite candidate bound are established by the written arguments above.
No finite scan of primes is substituted for those universal claims.

Internal dependencies: v11 seven-cover source
`cadc7197ec1f1169aba937894a5988e05ed5ed24`; v12 source
`5cfe4d64429f284232029341c6ba774e2eb6f727`; this batch's complete prefix and tail
classification notes. The interval theorem in Section 8 is the same credited
external input as in the preceding finite-budget proof. A primary paper with
its short proof is [Balister et al., Covering intervals with arithmetic
progressions](https://par.nsf.gov/servlets/purl/10165575), Theorem 1 and
Corollary 2.
