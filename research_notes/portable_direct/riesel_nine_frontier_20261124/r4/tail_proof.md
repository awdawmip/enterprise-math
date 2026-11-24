# All five-prime tails after Q0 in the observer-zero fiber R4

Research continuation, 2026-11-24. Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. This is an author derivation with
shared-context mathematical checking. Independent project Review and
formal proof acceptance are not claimed.

The integer state remains the fixed-X6 typed register, with positive
singleton BRC update \(x\mapsto2x+1\), weight and multiplicity one,
\(x_0=a^2-1\), and \(F_n(a)=a^2 2^n-1\). The congruences below are
observations of that state and retain the full integer divisor meaning.

## 1. Scope, notation, and the four dictionary types

R3 is the historical fixed 43-prime root progression. Let T8 be the product
of the 31 necessary free coordinates of the complete v13 budget-eight
observer, and define

\[
R_4=\{a\in R_3:a\equiv0\pmod{T_8}\}.
\]

Thus every root in R4 has supplementary cover cost at least nine. In this
note a displayed cover includes the permanent four-prime prefix

\[
Q_0=\{5,13,19,73\}.
\]

The forcing of Q0 for every nine-prime R4 cover is a separate prefix
argument. Combining it with the present theorem gives the full R4
budget-nine classification; no prefix forcing is assumed for the larger
R3 fiber.

Write

\[
A=38737,\qquad R=246241,\qquad U=487824887233,
\]

and define three free prime groups:

\[
\begin{aligned}
\mathcal G={}&\{92737,649657,40388473189,77158673929,118750098349\},\\
\mathcal R={}&\{209924353,4261383649,24929060818265360451708193\},\\
\mathcal H={}&\{8369281,394783681,4278255361,46908728641,\\
&\hspace{18mm}750016890283777055704738227247474485366338380663681\}.
\end{aligned}
\]

> **Tail theorem.** On R4, every complete supplement consisting of Q0
> and at most five further primes has exactly five further primes. Its
> five-tail dictionary is one of the following four types. Each listed
> type is sufficient, and all its sign assignments are compatible with
> R4.

| Type | Fixed tails | Free prime assignment | w-phases | Phase dictionaries | Signed CRT descriptions |
|---|---|---|---|---:|---:|
| G | none | all five primes of \(\mathcal G\) | 0,1,2,3,5 modulo 7, one each | 120 | 3840 |
| RR | A,R,U | two distinct primes of \(\mathcal R\) | 0,8 modulo 12 | 6 | 24 |
| RRR | A,U | all three primes of \(\mathcal R\) | 0,4,8 modulo 12, one each | 6 | 48 |
| HHH | A,U | three distinct primes of \(\mathcal H\) | 0,8,16 modulo 20, one each | 60 | 480 |
| Total | — | — | — | **192** | **4392** |

For every listed free prime q at w-phase b, its two root residues are

\[
a\equiv\pm2^{-(16+18b)}\pmod q.
\tag{1}
\]

As root sets, the RRR type is contained in the RR type: replace the
w=4 modulo 12 prime by the already fixed R channel, retaining the
w=0 and w=8 primes. Hence there are exactly three root-existence
alternatives: G, RR, or HHH. The root descriptions can intersect, so their
frequencies require union counting rather than adding the description
counts.

All roots described by these types have exact supplementary cost nine,
because R4 has no eight-prime supplement. This assertion does not require
an unrestricted total-cost lower bound.

## 2. Residual geometry and small-period inventories

After P and Q0, the uncovered exponents have

\[
n=32+36w,\qquad
w\bmod35\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}.
\tag{2}
\]

The five occupied modulo-seven rows have residues 0,1,2,3,5 and sizes
3,2,2,3,3. The three occupied modulo-five columns have residues 0,1,3
and sizes 5,3,5. Each occupied row has at most one point in a given
column; every row contains one point in each of the two five-point
columns.

The fixed tails have w-phases

\[
A:w\equiv1\pmod2,\qquad
R:w\equiv1\pmod3,\qquad
U:w\equiv2\pmod4.
\tag{3}
\]

Let \(h_q=\operatorname{ord}_q(2^{36})\). The complete small-period
inventories on R4 are as follows, after old primes and inactive
coordinates are removed:

| h | Available prime channels |
|---:|---|
| 1 | none |
| 2 | A |
| 3 | R |
| 4 | U |
| 5 | none |
| 6 | none; both order-216 primes are killed by the eight-observer condition |
| 7 | exactly the five primes of \(\mathcal G\) |
| 8 | none; all free order-96 and order-288 primes are killed |
| 10 | none; all four old modulo-five-tail primes are killed |

For h=7, solving \(d/\gcd(d,36)=7\) gives \(d=7g\) with
\(g\mid36\). The old dictionary removes 127,337,113,14449, of respective
orders 7,21,28,84, and T8 removes \(\{29,43,1429,5419\}\). The
remaining orders 63,126,252 give precisely \(\mathcal G\). Their complete
factorizations are recorded in the companion inventory certificate and
the budget-nine prefix proof.

The changes of coordinate used later give the following inventories:

| Coordinate | Effective period | Available channels |
|---|---:|---|
| z=w/2 | 1 | none other than selected A |
| z | 2 | U |
| z | 3 | R |
| z | 4 or 5 | none |
| t=w/4 | 1 | none other than selected A,U |
| t | 2 | none |
| t | 3 | R and the three primes of \(\mathcal R\) |
| t | 5 | the five primes of \(\mathcal H\) |

These are order inventories, not searches up to a prime-size cutoff. For
the new effective-t-period-five inventory, solving
\(d/\gcd(d,144)=5\) gives \(d=5g\) with \(g\mid144\). Every old
case is in P or fixed inactive on R4. The remaining three cyclotomic
values are

\[
\begin{aligned}
\Phi_{80}(2)&=4278255361,\\
\Phi_{240}(2)&=394783681\cdot46908728641,\\
\Phi_{720}(2)&=8369281\cdot
750016890283777055704738227247474485366338380663681.
\end{aligned}
\tag{4}
\]

The companion checker verifies these complete products, primality, and
exact orders. Their w-periods are all twenty. Likewise the three
\(\mathcal R\) primes have exact base-two order 432 and w-period twelve,
as certified in the complete Q7 two-tail theorem.

## 3. All-prime mass formula

For a residual set D modulo L, a channel of period h, and
\(g=\gcd(h,L)\), the absolute mass in units of one residue modulo L is

\[
\frac{K_{D,g}(b)}{h/g},\qquad
K_{D,g}(b)=|\{x\in D:x\equiv b\pmod g\}|.
\tag{5}
\]

It follows by CRT over the full common period. Sums of channel masses are
upper bounds for their union; independence is not assumed.

For B or any subset obtained by deleting whole modulo-seven rows, write
\(r=|D|\), \(c_5=\max_bK_{D,5}(b)\), and
\(c_7=\max_bK_{D,7}(b)\). Any available channel outside A,R,U and
period seven has mass at most

\[
E(D)=\max\{r/9,\ c_5/3,\ c_7/2,\ 1\}.
\tag{6}
\]

Indeed, after the killed periods are removed, the four gcd columns
\(1,5,7,35\) have minimum possible h respectively 9,15,14,35. The last
column contains at most one point per residue modulo 35. Formula (6)
therefore handles every remaining prime order, including arbitrarily
large ones.

## 4. If A is omitted, all five tails are the period-seven family

Let m be the number of different occupied modulo-seven rows supplied by
selected period-seven channels. Delete those rows and call the remaining
set D. Empty or duplicate rows use slots without helping D, so ignoring
their wasted slots only enlarges the possible upper bound.

The fixed channel R covers exactly r/3 of the mass of D, and U covers
exactly r/4. If both are selected, their union has mass exactly r/2:
their intersection has mass r/12. These statements remain exact after
row deletion, since both 3 and 4 are coprime to 35.

Let a be the number of selected fixed tails among R,U. Put
\(p=0,1/3,1/4,1/2\) according as neither, only R, only U, or both are
selected. At most \(5-a-m\) further non-seven channels remain. Their
total union mass on D is bounded above by

\[
pr+(5-a-m)E(D).
\tag{7}
\]

The row geometry supplies these sufficient bounds:

| m | Remaining r | Bound for E(D) |
|---:|---|---:|
| 0 | 13 | 5/3 |
| 1 | 10 or 11 | 3/2 |
| 2 | 7,8,9 | 3/2 |
| 3 | 4 | 1 |
| 3 | 5 or 6 | 3/2 |
| 4 | 2 | 1 |
| 4 | 3 | 3/2 |

For every admissible row of this table and every fixed-tail choice,
(7) is strictly below r. For example, with neither fixed tail selected
the bounds are \(25/3<13\), \(6<10\), \(9/2<7\),
\(2<4\) or \(3<5\), and \(r/2<r\). Adding a fixed tail removes
one generic slot and gives the corresponding third- or quarter-mass
contribution; direct substitution still gives strict inequalities. With
both fixed tails selected the possible m values stop at three, and even
the m=0 upper bound is \(13/2+3(5/3)=23/2<13\).

The exact independent row-subset calculation in `tail_review.md` verifies
every choice in (7); the displayed inequalities already give the analytic
all-order exclusion. The only remaining possibility is m=5, which spends
all five slots on different occupied period-seven rows. The complete
inventory has exactly five available primes, namely \(\mathcal G\),
so all must be used and assigned bijectively to 0,1,2,3,5. This is type G.

## 5. If A is selected, at least one of R,U is selected

Remove the odd w positions and write w=2z. The residual set is

\[
z\bmod35\in B_2=\{0,4,5,13,14,15,19,20,25,28,29,33,34\}.
\tag{8}
\]

Its incidence maxima in the four gcd columns are again 13,5,3,1.
The fixed R phase is z=2 modulo three, and the fixed U phase is z=1
modulo two. If neither is selected, the four remaining channels have
effective z-period at least six. Formula (5) gives each relative capacity
at most 3/13: the gcd-one column is at most 1/6, the gcd-five column at
most 5/26, the gcd-seven column at most 3/13, and the last at most 1/13.
Four such channels cover at most 12/13. This case is impossible.

## 6. R without U is impossible

Suppose A and R are selected but U is omitted. On z, the remaining set
has z not congruent to two modulo three and z modulo 35 in B2. There
are 26 residual classes modulo 105. Their incidence maxima for gcd
columns 1,3,5,7,15,21,35,105 are

\[
26,13,10,6,5,3,2,1.
\]

Each of the three further channels has z-period e≥6. Formula (5),
normalized by the residual mass 26, gives capacity at most one quarter.
For the gcd-three column the maximum is attained only at e=6; the
gcd-seven column is at most 3/13 and every other column is smaller.
Thus all three together cover at most three quarters of the remainder.
This case is impossible.

## 7. A and U without R: three periods must all be three or all be five

Now suppose A and U are selected, while R is omitted. The holes have
w=4t with

\[
t\bmod35\in B_4=\{0,2,7,10,14,17,20,24,25,27,30,32,34\}.
\tag{9}
\]

There is no unselected active period-one channel and all period-two
channels are inactive. The remaining three channels consequently each
have relative capacity at most 5/13. For a complete union, each must
cover at least 3/13: otherwise the other two cannot supply the missing
mass. Formula (5) reduces every possible effective t-period to

\[
e\in\{3,4,5,7\}.
\tag{10}
\]

This reduction is uniform over all primes. It precedes prime inventory
enumeration.

If period four occurs, at least one other non-five period would give
union mass at most \(1/4+5/13+1/3=151/156<1\). Thus both other
periods would have to be five. Their two classes leave a whole B4
residue class modulo 35 uncovered, whose lifts visit all four period-four
phases. A single period-four class cannot cover it.

If period seven occurs, the other two classes must attain their maximum
5/13. They are the two five-point modulo-five columns, with phases zero
and two. The remaining B4 points are 14,24,34; their modulo-seven
residues 0,3,6 are different. One period-seven class cannot cover them.

Periods three and five cannot be mixed either. One or two period-five
classes leave a whole B4 point modulo 35; its lifts visit all three
period-three phases, which fewer than three period-three channels cannot
cover.

Therefore all three periods are three, or all are five.

For period three, the phases must be t=0,1,2. Because R is excluded in
this case, the complete inventory leaves exactly the three primes of
\(\mathcal R\). They occupy w=0,4,8 modulo twelve. This is type RRR.

For period five, the phases must be t=0,2,4, which are precisely the
three occupied columns of B4. The complete inventory leaves
\(\mathcal H\), and three distinct members occupy w=0,8,16 modulo
twenty. This is type HHH.

## 8. A,R,U selected: the complete two-tail theorem applies

The remaining holes have w=4t with t=0 or two modulo three and
t modulo 35 in B4. The complete Q7 two-tail theorem proves that two
channels must both have effective t-period two or both have effective
t-period three. Period two is inactive on R4. The old order-216 primes
are inactive as well. Only the three primes of \(\mathcal R\) remain,
and the two chosen primes must occupy t=0 and t=2, or equivalently w=0
and w=8 modulo twelve. This is type RR.

Sections 4–8 exhaust every possible use of A,R,U and every remaining
prime order. They prove the complete tail classification.

## 9. Sufficiency, irredundancy, CRT, and the root predicate

Each of the four types covers B by inspection of its phase rows. Type G
covers every occupied modulo-seven row. The other types cover odd w by
A, then the appropriate complement by the listed fixed and free tails.
Together with P and Q0, they cover every positive exponent.

Every listed prime is outside the R4 progression modulus, except the
already fixed A,R,U. The two root residues in (1) are distinct and
different required phases have disjoint root pairs. CRT therefore
realizes every assignment by infinitely many ordinary positive roots.
All selected primes are smaller than the first R4 term, so all are
proper divisors at their zero positions.

R4 has no complete supplement of size at most eight. Hence every
displayed nine-prime dictionary is inclusion-minimal, and every root
realizing one has exact supplementary cost nine. This also explains why
no extra useless prime can occur in a dictionary counted by the theorem.

As a root predicate, exact budget nine is the union of:

1. All five colors 0,1,2,3,5 modulo seven are present among
   \(\mathcal G\).
2. Both colors 0,8 modulo twelve are present among \(\mathcal R\).
3. All three colors 0,8,16 modulo twenty are present among
   \(\mathcal H\).

This predicate is conditional on Q0 unless coupled with the separate
R4 prefix-forcing theorem. The three prime groups are disjoint, so their
root events are independent on R4 by CRT. The RRR dictionary type
requires all three colors 0,4,8 among \(\mathcal R\), which implies
the second event and adds no new root. The full dictionary count is
192 phases and 4392 signed descriptions; retaining only the three root
alternatives gives 186 phases and 4344 descriptions before overlap
correction.

This proof supplies the analytic all-prime classification. The companion
scripts certify complete small-order factors and primality, reduced
covering rows, signed CRT minima, and observer counts. These separate
computations do not replace any infinite-order step in the proof.
