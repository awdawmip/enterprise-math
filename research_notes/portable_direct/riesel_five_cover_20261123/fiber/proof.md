# Sharp density staircases on two fixed observer fibers

Status: author mathematical derivation with exact finite arithmetic checks. This continues Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`; it is not an independent project Review or a formal promotion.

## 1. Objects, scope and statements

Write

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

and retain

\[
a_*=690786768637635218740714348513373826260012289,
\]

\[
\begin{split}
P=\{&7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,\\
&1321,14449,29191,65537,6700417\},
\end{split}
\]

\[
M=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281.
\]

The old root class is \(a\equiv a_*\pmod{2M}\), with positive roots. The old dictionary covers all odd indices. At even indices \(n=2u\), its holes are exactly

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}
\pmod{105}.
\end{split}
\]

Thus the initial uncovered density among all positive indices is \(36/210=6/35\).

For a finite set of new primes \(Q\subseteq\mathbb P\setminus P\), let

\[
\operatorname{gap}(a,Q)
=\operatorname{dens}\{n\ge1:\ p\nmid F_n(a)\text{ for every }p\in P\cup Q\}.
\]

This density exists because the indicated set is periodic. For a root family \(R\), define

\[
D_t(R)=\inf_{a\in R,\ |Q|\le t}\operatorname{gap}(a,Q).
\]

Every lower bound below holds for every ordinary integer root in the stated fiber and every set of at most \(t\) primes, without a search cutoff on primes or orders. Every listed bound is attained. A root *attains the budget-\(t\) bound* when some such dictionary has gap exactly \(D_t(R)\).

As before, \(\delta_P(a)\) is the minimum number of primes outside \(P\) in a full proper-prime cover, and \(\tau(a^2)\) is the minimum total number of primes. These are different minima. Adding all old primes never increases \(\delta_P\), so its study may use dictionaries of the form \(P\cup Q\).

Put

\[
U=\{11,61,331\},\quad V=\{5,13,11,61,331\},\quad
K=\prod V=14436565,
\]

\[
W=\{19,37,73,109\},\quad J=\prod W=5593771,\quad
L=KJ=80754838636615.
\]

The previous twenty-five-channel fiber is

\[
R_0=\{a>0:a\equiv a_*\pmod{2M},\ 3\mid a,\
a\equiv666303\pmod K\}.
\tag{1}
\]

Since \(3\mid a_*\), its first two constraints are equivalent to \(a\equiv a_*\pmod{6M}\). Its residues at \((5,13,11,61,331)\) are \((3,1,0,0,0)\).

The refined twenty-nine-channel fiber is

\[
R_1=\{a\in R_0:(a\bmod19,a\bmod37,a\bmod73,a\bmod109)
=(6,0,37,0)\}.
\tag{2}
\]

Equivalently, its new observer condition is

\[
a\equiv12926327728523\pmod L.
\tag{3}
\]

**Theorem A.** The sharp density staircases are

\[
\boxed{D_t(R_0)=\frac{(216,108,39,26,13,0)_t}{1260}
\quad(0\le t\le5),}
\tag{4}
\]

\[
\boxed{D_t(R_1)=\frac{(432,216,78,52,26,13,0)_t}{2520}
\quad(0\le t\le6).}
\tag{5}
\]

On \(R_0\), every five-prime completion consists of 5, 13 and three primes from \(W\), with the three distinct relative phases specified below. This classifies all five-prime completions in this fiber, not just extensions of a chosen optimal chain. On \(R_1\), every root has \(\delta_P(a)\ge6\); all dictionaries attaining its budget-five bound are classified below. The classification at budget six is only of nested simultaneous optima, not of every possible six-prime cover.

**Theorem B.** For every integer \(s\ge6\), infinitely many roots in \(R_1\) satisfy

\[
\boxed{\delta_P(a)=s,\qquad\tau(a^2)=20+s.}
\tag{6}
\]

All these roots have the same full residue-value trajectory in the twenty-nine channels \(P\cup V\cup W\), for every \(n\ge0\). The quantifiers are \(\forall s\ge6\,\exists^\infty a\); no single root with infinite covering cost is asserted.

## 2. Incidence formula and complete small-order exclusions

If a periodic set \(A\subseteq\mathbb Z/L_0\mathbb Z\) has size \(m\), its relative intersection density with one residue class \(x\equiv c\pmod d\) is

\[
\rho_A(c,d)=\frac{K_g(c)}{m(d/g)},\qquad
g=\gcd(d,L_0),\quad
K_g(c)=\#\{x\in A:x\equiv c\pmod g\}.
\tag{7}
\]

Indeed each compatible old residue has one solution in the combined period \(L_0d/g\). This proves (7) for every positive order, including orders larger than any checked range.

For \(H\), the exact incidence maxima are

| \(g\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\max K_g\) | 36 | 23 | 11 | 7 | 6 | 4 | 2 | 1 |

The mod-3 counts are \((23,13,0)\).

For an odd prime \(q\) having a zero on the even-index sequence, the zero set is one class \(u\equiv c\pmod{d_q}\), where \(d_q=\operatorname{ord}_q(4)\). On a fixed parity of \(u\), its effective period is \(e_q=\operatorname{ord}_q(16)\). On \(u=4+6v\), it is \(f_q=\operatorname{ord}_q(2^{12})\). If no zero class exists or is compatible with the chosen fiber, its contribution is zero.

The following are complete factorizations; the finite verifier checks every product and every prime factor by trial division:

\[
\begin{aligned}
2^{14}-1&=3\cdot43\cdot127,\\
2^{16}-1&=3\cdot5\cdot17\cdot257,\\
2^{18}-1&=3^3\cdot7\cdot19\cdot73,\\
2^{20}-1&=3\cdot5^2\cdot11\cdot31\cdot41,\\
2^{24}-1&=3^2\cdot5\cdot7\cdot13\cdot17\cdot241,\\
2^{36}-1&=3^3\cdot5\cdot7\cdot13\cdot19\cdot37\cdot73\cdot109,\\
2^{48}-1&=3^2\cdot5\cdot7\cdot13\cdot17\cdot97\cdot241\cdot257\cdot673,\\
2^{60}-1&=3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41\cdot61
\cdot151\cdot331\cdot1321,\\
2^{36}+1&=17\cdot241\cdot433\cdot38737.
\end{aligned}
\tag{8}
\]

On \(R_0\), the primes 3 and every member of \(U\) are inactive because they divide the root. The prime 2 never divides \(F_n(a)\).

### 2.1 A uniform bound on the old holes and on either parity

For a new active prime other than 5 and 13, the minimum possible \(d_q\), grouped by \(\gcd(d_q,105)\), is bounded below by

\[
(8,9,10,7,15,21,35,105).
\]

All smaller candidates are excluded by (8), membership in \(P\), or inactivity of 11. Formula (7) therefore gives

\[
\left(\frac18,\frac{23}{108},\frac{11}{72},\frac7{36},
\frac16,\frac19,\frac1{18},\frac1{36}\right).
\tag{9}
\]

In particular every such prime covers at most \(23/108\) of \(H\).

Exactly the same bound holds inside either parity of \(u\). To see this, use \(e_q=\operatorname{ord}_q(16)\). The values 1, 2, 3 and 6 give factors of \(2^{24}-1\); the value 4 gives factors of \(2^{16}-1\); and the only remaining outside prime at value 5 is inactive 11, by \(2^{20}-1\). The same minimum-period row and (9) apply. The affine change \(u=\epsilon+2j\) permutes residues mod 105 and preserves all incidence maxima.

### 2.2 The residual set after the fixed 5 and 13 channels

On \(R_0\), prime 5 covers \(u\equiv1\pmod2\), while prime 13 covers \(u\equiv0\pmod6\). Their complement within the old holes has

\[
u\equiv0\pmod2,\quad u\equiv1\pmod3,\quad u=4+6v.
\]

Its relative density in \(H\) is \(13/72\), and its density among all exponent indices is \(13/420\). The remaining condition is

\[
v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{10}
\]

For divisors \((1,5,7,35)\), the incidence maxima of \(A\) are \((13,5,3,1)\). The effective periods \(f_q=1,2\) give only old/basic primes by \(2^{24}-1\); \(f_q=5\) gives precisely the possible outside primes \(U\), all inactive. Consequently the bounds by gcd column are

\[
\left(\frac13,\frac5{26},\frac3{13},\frac1{13}\right).
\tag{11}
\]

Equality \(1/3\) is possible only at \(f_q=3\). The complete factorization of \(2^{36}-1\) shows that its outside primes are exactly \(W\); their actual base-2 orders are

\[
(\operatorname{ord}_{19}2,\operatorname{ord}_{37}2,
\operatorname{ord}_{73}2,\operatorname{ord}_{109}2)=(18,36,9,36).
\tag{12}
\]

Thus every maximizing channel after the basic pair is a member of \(W\), cutting out one class \(v\equiv r\pmod3\).

## 3. The complete R0 staircase and its equality conditions

The zero-prime entry of (4) is \(6/35\). Prime 5 uniquely attains coverage \(1/2\) of \(H\): prime 13 covers only \(23/72\), and all other active primes satisfy (9). Hence budget one has gap \(3/35\).

For budgets \(t=2,3,4\), classify a dictionary by whether it contains 5 and 13. If it contains neither, (9) gives

\[
\operatorname{gap}(a,Q)\ge\frac6{35}\left(1-t\frac{23}{108}\right).
\tag{13}
\]

If it contains exactly one, that prime misses an entire parity of \(u\), giving

\[
\operatorname{gap}(a,Q)\ge\frac3{35}
\left(1-(t-1)\frac{23}{108}\right).
\tag{14}
\]

Each of (13) and (14) is strictly greater than the corresponding claimed entry in (4). If it contains both, (11) gives

\[
\operatorname{gap}(a,Q)\ge\frac{13}{420}
\left(1-\frac{t-2}{3}\right).
\tag{15}
\]

This gives the three remaining positive entries of (4). Equality in (15) requires each new contribution to attain \(1/3\), and requires disjoint contributions. Thus the complete equality dictionaries are:

| Budget | Dictionary attaining the sharp bound |
|---:|---|
| 1 | \(\{5\}\) |
| 2 | \(\{5,13\}\) |
| 3 | \(\{5,13,q\}\), where \(q\in W\) has one compatible relative phase |
| 4 | \(\{5,13,q,q'\}\), with \(q,q'\in W\) occupying two distinct relative phases |

All three relative classes have positive density in (10), so two channels with the same phase overlap completely on this residual set and cannot attain budget four equality.

### 3.1 Every five-prime full cover in R0 contains the basic pair

If a five-prime dictionary contains exactly one of 5 and 13, (14) with \(t=5\) still gives a positive gap. To treat a dictionary containing neither, strengthen (9) using its only exceptional large columns.

The value \(d_q=9\) is possible outside the old/basic primes only for \(q=19,73\), by \(2^{18}-1\). These are the only possible channels exceeding \(1/6\) in the gcd-3 column. The value \(d_q=7\) is possible outside the old/basic primes only for \(q=43\), by \(2^{14}-1\). After removing these three candidates, every column of (9) is at most \(1/6\): in the gcd-3 column the next period is at least 12, giving \(23/144<1/6\), and in the gcd-7 column the next period is at least 14, giving \(7/72<1/6\). Therefore any five distinct primes omitting both 5 and 13 cover at most

\[
2\frac{23}{108}+\frac7{36}+2\frac16
=\frac{103}{108}<1
\tag{16}
\]

of \(H\). A full five-prime cover must contain the basic pair.

The other three primes must then cover all of (10). By (11), all three must be members of \(W\), must attain \(1/3\), and must occupy the three different relative phases. Conversely those conditions provide a full cover. This proves

\[
\boxed{\delta_P(a)=5\quad\Longleftrightarrow\quad
\text{the active W channels occupy all three relative phases}}
\qquad(a\in R_0).
\tag{17}
\]

The earlier positive budget-four bound rules out a smaller cost. All primes in these dictionaries are at most 109, so for roots in the stated old class all their assigned divisors are proper. This also shows that every five-prime completion in \(R_0\) can be ordered into a nested simultaneous optimum through budgets 1–5.

### 3.2 Exact root predicates, counts and least periods

A channel of period \(d_q\) has even-index phase \(c\) exactly when

\[
a\equiv\pm2^{-c}\pmod q.
\tag{18}
\]

For relative phase \(r=v\bmod3\), put \(c=4+6r\pmod{d_q}\). The complete root table is:

| Prime | \(d_q\) | Phase \(r=0\): root residues | Phase \(r=1\): root residues | Phase \(r=2\): root residues |
|---:|---:|---|---|---|
| 19 | 9 | 6, 13 | 9, 10 | 4, 15 |
| 37 | 18 | 7, 30 | 3, 34 | 4, 33 |
| 73 | 9 | 32, 41 | 36, 37 | 4, 69 |
| 109 | 18 | 34, 75 | 38, 71 | 4, 105 |

Every column has two residues at each prime, and these six residues are disjoint. All other \(q-6\) residues give no contribution on this residual fiber, even when the prime may have zeros elsewhere.

Let \(E_3,E_4\) denote attainment of (4) at budgets three and four. Their predicates are respectively presence of at least one and at least two distinct relative phases. Equation (17) requires all three. With \(P_j=\prod_{q\in W}(q-j)\), their exact counts per \(J\) are:

| Predicate on \(R_0\) | Exact CRT count | Count per \(J=5593771\) |
|---|---:|---:|
| \(E_3\) | \(J-P_6\) | 2,812,668 |
| \(E_4\) | \(J-3P_4+2P_6\) | 397,152 |
| \(\delta_P=5\) | \(J-3P_2+3P_4-P_6\) | 10,848 |

These follow by inclusion-exclusion on the three phase categories. Division by \(J\) gives exact relative natural densities inside the progression \(R_0\). Budgets zero through two are automatically attained at every root of \(R_0\).

Each of the three nonconstant predicates has least positive period \(J\) in the progression parameter of \(R_0\). To see necessity of every factor \(q\in W\), fix other coordinates to show respectively zero, one or two distinct phases; changing only the \(q\)-coordinate from inactive to a new phase changes the predicate. Thus the predicate depends essentially on every prime coordinate. Any integer period omitting a prime factor would, by taking multiples of that period, vary that coordinate while fixing the others, a contradiction. The progression step \(6MK\) is invertible mod \(J\), so the same conclusion holds in its integer parameter.

There are \(\binom43\,3!=24\) three-prime phase dictionaries. Enumerating their sign choices and their unrestricted fourth-prime residue gives 11,424 entries with repetition, exactly 10,848 distinct CRT classes. Complete enumeration yields the least positive \(R_0\) root with \(\delta_P=5\):

\[
\boxed{73841986537470627371286709939739215853723074973610308115228565383.}
\tag{19}
\]

Its \(W\)-residues are \((9,7,69,96)\). Adding the primes in the order \((5,13,37,19,73)\) gives uncovered counts \((216,108,39,26,13,0)\) per exponent period 1260. This compact CRT witness proves \(\delta_P=5\); no equality \(\tau=25\) is claimed for it.

## 4. The refined R1 fiber: exact budget-five gap and nested completion

In \(R_1\), the active \(W\)-channels are exactly 19 in relative phase 0 and 73 in relative phase 1. Primes 37 and 109 divide the root and are inactive. Every root therefore attains all entries of (5) through budget four, by inserting 5, 13, 19 and 73. The lower bounds follow from \(R_1\subset R_0\).

After these four channels, the remaining relative phase is \(v\equiv2\pmod3\). Write

\[
v=2+3w,\qquad u=16+18w.
\tag{20}
\]

Its density among all exponent indices is \(13/1260\). The condition on \(w\) is a thirteen-element set mod 35, with incidence maxima \((13,5,3,1)\), because multiplication by 3 permutes the mod-35 residues in (10).

### 4.1 Excluding every alternative budget-five equality case

If a five-prime dictionary omits both 5 and 13, (16) gives gap at least \(1/126\). If it contains exactly one, the missed-parity bound gives at least \(4/315\). Both exceed \(13/2520\).

Suppose it contains both. An active prime outside \(W\) has effective period \(f_q=\operatorname{ord}_q(2^{12})\) different from 1, 2, 3, 4 and 5: periods 1 and 2 are old/basic, period 3 gives only \(W\), period 4 gives only old/basic primes by \(2^{48}-1\), and period 5 gives the inactive \(U\). Its bounds on (10) are therefore

\[
\left(\frac16,\frac5{26},\frac3{13},\frac1{13}\right),
\tag{21}
\]

whose maximum is \(3/13\). If the three remaining channels use neither active \(W\)-prime, their uncovered density is at least

\[
\frac{13}{420}\left(1-3\frac3{13}\right)=\frac1{105}.
\]

If they use exactly one, it is at least

\[
\frac{13}{420}\left(1-\frac13-2\frac3{13}\right)=\frac2{315}.
\]

These also exceed \(13/2520\). Inactive channels only weaken coverage and are included in these bounds. Thus every equality dictionary must contain all four primes \(5,13,19,73\).

On their residual set (20), the effective period of an additional active prime is \(h_q=\operatorname{ord}_q(2^{36})\). The value 1 gives only old, already used or inactive primes, by \(2^{36}-1\). Formula (7) yields the column bounds

\[
\left(\frac12,\frac5{13},\frac3{13},\frac1{13}\right).
\tag{22}
\]

Hence at least half the residual set remains:

\[
\operatorname{gap}(a,Q)\ge\frac{13}{1260}\frac12
=\boxed{\frac{13}{2520}}.
\tag{23}
\]

Equality is possible only at \(h_q=2\). The factorization \(2^{72}-1=(2^{36}-1)(2^{36}+1)\) and (8) leave exactly

\[
B=\{433,38737\}.
\]

Both have exact base-2 order 72 and even-index period 36. They attain (23) precisely in one of the two parity classes of \(w\) in (20):

| Prime | \(w\equiv0\pmod2\), \(u\equiv16\pmod{36}\) | \(w\equiv1\pmod2\), \(u\equiv34\pmod{36}\) |
|---:|---|---|
| 433 | root residues 150, 283 | root residues 4, 429 |
| 38737 | root residues 2677, 36060 | root residues 4, 38733 |

Consequently the complete budget-five equality dictionaries on \(R_1\) are

\[
\{5,13,19,73,q\},\quad q\in B,
\]

with a root residue in the displayed table. This proves the positive budget-five entry of (5), including its all-prime equality classification. In particular every \(R_1\) root has \(\delta_P\ge6\).

### 4.2 Exactly which roots admit a nested optimum through six

Using both primes in \(B\) with opposite \(w\)-parities covers (20), and attains the last zero entry of (5). Conversely, consider a nested simultaneous optimum through six. Its first four channels must be 5, 13 and the two active \(W\)-primes; its fifth must be one of the two \(B\)-primes in a displayed phase. The remaining indices have the form

\[
n=32+36\epsilon+72z,
\]

where \(z\) ranges over a thirteen-element subset mod 35. Its mod-5 and mod-7 incidence maxima are 5 and 3, so this subset is not contained in a single class modulo either 5 or 7. The gcd of all differences of these exponent indices is therefore 72: their period contributes \(72\cdot35\), and the differences of the admissible residues have gcd 1 with 35. Any one prime dividing every remaining term must have base-2 order dividing 72. The complete factors in (8) leave only the other member of \(B\), in the opposite parity; old, inactive and already used primes cannot hit this remaining set.

Thus nested completion through six is equivalent to both \(B\)-channels occupying opposite displayed parities. This statement does not exclude a non-nested six-prime cover at some other \(R_1\) root, and is not a classification of all \(\delta_P=6\) roots.

Let \(Z=433\cdot38737=16773121\). The predicate \(E_5\) of attaining (23) is that at least one \(B\)-channel is in one of its four listed residues. Its exact count per \(Z\) is

\[
Z-(433-4)(38737-4)=156664.
\]

Nested completion through six has exactly \(2\cdot2^2=8\) residue classes per \(Z\). Both predicates have least period \(Z\) in the progression parameter of \(R_1\), by the same essential-coordinate argument used above. Their relative densities inside \(R_1\) are therefore \(156664/16773121\) and \(8/16773121\).

Complete enumeration of the eight classes gives the least positive nested-optimal root:

\[
\boxed{1597463687996365290740241630260436015028835427889255944107518938773290244463.}
\tag{24}
\]

Its residues at \((433,38737)\) are \((429,2677)\). In the order \((5,13,19,73,433,38737)\), it has uncovered counts \((432,216,78,52,26,13,0)\) per exponent period 2520. It has \(\delta_P=6\). Its total minimum \(\tau\) is not determined here, and (24) is not claimed to be the smallest of all \(R_1\) roots of additional cost six.

## 5. Every finite exact cost at least six occurs in R1

This section reuses the all-cost construction at commit
`af9e1a5e49386a28283781876e10742a71991036`, path
`research_notes/portable_direct/riesel_spectrum_20261121/spectrum/proof.md`,
and the twenty-five-channel transfer at commit
`a2ae4d93398425e67dacbb4c99b7f3a6755e5771`, path
`research_notes/portable_direct/riesel_observers_20261122/fixed_observer/proof.md`.
Their finite seeds, primitive-prime existence input, irredundant refinements and pairwise-coprimalization argument are unchanged.

For every \(s\ge5\), that construction uses a dictionary \(S=P\sqcup Q\), \(|Q|=s\), containing the four permanent seed channels

\[
(q,\operatorname{ord}_q2,c)=(5,4,1),(73,9,1),(13,12,0),(19,18,4).
\]

Their root residues are \(a\equiv3,37,1,6\) at \(q=5,73,13,19\), respectively. The cost-five seed also contains 109 of order 36. The cost-six, seven and eight seeds remove that row by binary refinements, whose child orders are at least 72. Every later five-child refinement replaces a largest even-index period \(d\) with requested base-2 orders \(2dm\), where

\[
d=18\cdot2^r12^h,\quad 0\le r\le3,\qquad m\in\{2,3,4,6,12\}.
\]

Thus every such child order is at least 72. The prime 37, whose order is 36, is never in \(S\). The prime 109 occurs only in the unrefined cost-five seed. For \(s=5+4h\ge9\), the first five-child refinement removes it; for the other three congruence classes it has already been removed in the seed. Therefore

\[
37,109\notin S\qquad\text{for every constructed }s\ge6.
\tag{25}
\]

This is an order argument for every depth, not a finite list extrapolation.

The twenty unchanged private old exponent indices include 5 and 41, and also 3 and 63. In the coprimalization construction,

\[
D=\operatorname{lcm}_{i<j}(2^{|n_i-n_j|}-1),\qquad
E=D\Big/\prod_{q\in S}q^{v_q(D)},
\]

and the CRT root satisfies \(E\mid a\). The difference \(41-5=36\) gives \(2^{36}-1\mid D\). By (25), neither 37 nor 109 is removed when forming \(E\), so

\[
37\cdot109\mid E\mid a\qquad(s\ge6).
\tag{26}
\]

Similarly, the difference \(63-3=60\) forces \(11\cdot61\cdot331\mid a\); none of their orders 10, 60 and 30 is among the retained orders 4, 9, 12, 18 or any later order divisible by 36. The existing forcing condition gives \(3\mid a\). Consequently every constructed root of cost at least six has exactly the observer residues in (1)–(3), with no extra CRT constraint or altered construction.

The previous pairwise-coprimalization proof makes all \(20+s\) private terms pairwise coprime. Every full cover needs at least \(20+s\) distinct primes, and the displayed dictionary supplies them; the \(s\) new private terms avoid \(P\), forcing at least \(s\) outside primes. Hence \(\delta_P=s\) and \(\tau=20+s\). The compatible CRT progression supplies infinitely many positive roots, with all sufficiently large roots having proper assigned divisors. This proves Theorem B.

Roots in this common fiber agree modulo every prime in \(P\cup V\cup W\). Consequently their values \([F_n(a)]_q\) agree in all twenty-nine coordinates for every \(n\ge0\), not merely in their zero patterns or on a finite prefix. The unchanged project-native scalar update is \(x\mapsto2x+1\), its double step is \(4x+3\), and its fixed X6 anchor and singleton positive weight/multiplicity remain unchanged. These prime coordinates are observation channels. The full integer state and joint divisibility relations remain available; the fixed projection omits information required to determine exact covering cost.

## 6. Finite certificate and exact reuse boundary

Run `python verify_fibers.py`. The verifier uses only the Python standard library. It checks complete factor products and trial primality, exact orders, all old zero phases and the full old union period 6720, the incidence tables and rational strict bounds, all weighted phase states, all 10,848 \(R_0\) cost-five CRT classes, the eight nested \(R_1\) classes, the least-period essential-coordinate witnesses, both compact minima, and their complete uncovered-set periods. These computations provide finite arithmetic inputs to the proofs; the all-prime and all-depth conclusions are the arguments above.

It also reads three already certified coprimalized roots and newly checks their exact membership in \(R_1\):

| Additional cost | Total cost | Decimal root digits | Existing pairwise gcd checks reused |
|---:|---:|---:|---:|
| 6 | 26 | 10,021 | 325 |
| 7 | 27 | 10,882 | 351 |
| 8 | 28 | 16,517 | 378 |

The cost-six and cost-seven roots come from the v8 fixed-observer certificate; the cost-eight root comes from the unchanged v7 spectrum certificate. Their exact hexadecimal roots remain at those sources. The new certificate records their decimal hashes, the source-file hashes, the common observer residue and the precise new check scope. It reuses the previous gcd, properness, coverage and native evidence rather than repeating it. Their newly checked residues at \((19,37,73,109)\) are all \((6,0,37,0)\).

The new compact roots (19) and (24) are ordinary-integer arithmetic witnesses in this certificate. Their actual `EffectHistogram` execution and pinned native-source binding are supplied by the separate round-nine native integration; this script does not claim to execute those project-native objects. The all-cost theorem and the distinctions between \(\delta_P\), \(\tau\), nested completion, and a single infinite-cost root are not enlarged by finite execution.
