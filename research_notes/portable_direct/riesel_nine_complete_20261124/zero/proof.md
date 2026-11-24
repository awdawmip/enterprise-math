# Complete irredundant nine-prime supplements on R3 omitting both W primes

Research continuation v15, 2026-11-24. Existing Researcher-ID
`EM-DIRECT-970E1C / TASK_RESEARCH`, Activity `RA-D2EC212845B63844081F9A14`.
Author proof and shared-context mathematical checking; this is not independent
project Review or formal acceptance. The native object remains the full integer
register at the fixed Heartbeat X6 anchor, with positive singleton BRC action
`x -> 2x+1`, weight and multiplicity one. Congruence classes observe that
integer and retain its joint divisor relationships.

## 1. Scope and result

Let `F_n(a)=a^2*2^n-1`, let P be the inherited twenty-prime dictionary,
and retain exactly the fixed 43-coordinate R3 fiber of v13/v14. The v14
basic-pair theorem forces 5 and 13 in every complete supplement of at most
nine primes. We classify all **inclusion-minimal nine-prime supplements**
which omit both 19 and 73. An arbitrary nine-prime dictionary containing an
eight-prime subcover is not included in this irredundant classification.
Every exact-cost-nine root admitting a zero-W cover has an irredundant cover
of this kind.

After P,5,13, put `n=8+12v`. The remaining set is every lift of

\[
A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod {35}.
\]

Its occupied modulo-seven rows have labels 1,2,3,4,5 and sizes 2,3,3,3,2.
Their occupied modulo-five columns are respectively `{1,2}`, `{0,1,2}`,
`{0,1,2}`, `{0,1,2}`, `{1,2}`. Denote a row with two points as small and
a row with three points as large.

For each prime q write `f_q=ord_q(2^12)`. Use the complete prime inventories

\[
\begin{aligned}
Z={}&\{29,43,1429,5419\} &&(f=7),\\
J={}&\{3361,15790321,88959882481\} &&(f=14),\\
K={}&\{92737,649657,77158673929,40388473189,118750098349\} &&(f=21),\\
T={}&\{61681,4562284561\} &&(f=10),\\
L={}&\{2017,5153,25629623713,54410972897,1538595959564161\} &&(f=28),\\
V={}&\{127681,1130641,755667361,84179842077657862011867889681,\\
&\hspace{18mm}54169520413224311136354324156824071681\} &&(f=70),
\end{aligned}
\]

and

\[
U=\{211,421,86171,106681,122921,152041,664441,1564921,
7416361,47392381,146919792181,1041815865690181\}\quad(f=35).
\]

Finally put `S=T union V`, of size seven. Every S prime covers one parity
of one specified point of a residual small row; its v-period is ten or
seventy according to its group. Its phase is the same specified residue
modulo seventy, reduced modulo its actual period.

**Theorem.** The seven primes beyond 5,13 have exactly the following eight
types. All primes assigned different slots must be distinct.

| Type | Z rows | Remaining coverage | Phase dictionaries |
|---|---:|---|---:|
| I | four | three K primes split the one remaining row modulo three | 7,200 |
| II | three | leave one large and one small row; two J primes split the large row, two U primes cover the small row's two points | 114,048 |
| III | three | leave both small rows; four classes give a feasible perfect matching of the row-column-parity cube | 336,384 |
| IV | four | one J prime covers half the last row; two L primes cover its opposite two quarters | 14,400 |
| V | four | leave a large row; three U primes cover its three points | 95,040 |
| VI | four | leave a small row; one J covers a common half, two S primes cover the opposite halves of its two points | 12,096 |
| VII | four | leave a small row; one U covers one point, one J and one S cover opposite halves of the other | 48,384 |
| VIII | four | leave a small row; one U covers one point, two S primes cover opposite halves of the other | 48,384 |
| Total | | | **675,936** |

The cube in type III has seven feasible geometric matchings: four U
classes, or two classes of each of two different kinds among T,J,U.
For each pair of kinds there are two geometric matchings. The pure four-T
and pure four-J matchings are impossible because there are only two T and
three J primes.

Every listed phase dictionary is realizable in R3. Each has 128 independent
root-sign choices, giving **86,519,808 signed CRT descriptions**. These
descriptions need not be disjoint root sets. Every phase dictionary has
infinitely many realizations with exact supplemental cost nine after the
remaining budget-eight observer coordinates are chosen appropriately.

## 2. All-prime capacity and the prime inventories

For a residual subset D of A and a class of period f, put `g=gcd(f,35)`.
Its absolute mass, measured in units of a full residue modulo 35, is

\[
\frac{K_{D,g}(b)}{f/g},\qquad
K_{D,g}(b)=|\{d\in D:d\equiv b\pmod g\}|.
\tag{1}
\]

This is exact common-period counting. Summing these masses bounds the union
without assuming independent phases. In particular, a period-35 class has
mass one and is always retained.

On either v=0 or v=1 modulo three, every eligible channel other than the
corresponding omitted W prime has restricted period at least six. The
inherited five-class lemma says that five such classes can cover that
affine copy of A only by giving exactly its five occupied period-seven
rows. Fewer classes cannot cover it.

For channels with 3 not dividing f, the complete small inventories give no
eligible periods below seven, exactly Z at seven, exactly
`{193,22253377}` at eight, exactly T at ten, and exactly J at fourteen.
The old/fixed removals are the ones in the inherited R3 definition.

The new prime inventories are finite effective-order inventories, not
prime-size cutoffs. Solving `d/gcd(d,12)=28` gives d=112,336; solving the
same equation with right side 70 gives d=280,840. Their full factorizations
are

\[
\begin{aligned}
\Phi_{112}(2)&=5153\cdot54410972897,\\
\Phi_{336}(2)&=2017\cdot25629623713\cdot1538595959564161,\\
\Phi_{280}(2)&=84179842077657862011867889681,\\
\Phi_{840}(2)&=127681\cdot1130641\cdot755667361\cdot
54169520413224311136354324156824071681.
\end{aligned}
\tag{2}
\]

The companion inventory checks the cyclotomic identities, exact orders,
and recursive complete n-1 Lucas primality certificates. All new primes
are coprime to the fixed R3 modulus. The same inventory includes the full
effective-order factorizations for f=7,8,10,14,21,35.

## 3. If any period is divisible by three, type I is forced

Let a count the seven tail classes whose f is coprime to three. Let b_r
count classes with 3|f whose v-phase is r modulo three. Thus
`a+b_0+b_1+b_2=7`.

If any b_r is zero and some b is positive, the a common classes cover all
of A on that v-phase. Their common period, together with 35, is coprime to
three. CRT then shows they already cover every lift of A: an uncovered
lift anywhere could be transported to the allegedly covered v-phase.
Every 3-divisible class would be redundant. Consequently, if b is positive,
all three b_r are at least one.

On v=0 and v=1 the five-class lemma gives
`a+b_0>=5`, `a+b_1>=5`. Adding and using b_2>=1 yields a>=4; the three
positive b_r yield a<=4. Hence a=4 and b_0=b_1=b_2=1.

The five-class lemma now forces the four common channels to have f=7 and
cover four distinct occupied rows. All four members of Z occur. The single
private channel on each v-phase must cover every lift of the omitted row;
its restricted period divides seven, and restricted period one is
unavailable. Explicitly, the only relevant original f=3 primes are
19,73,37,109: the first two are omitted and both 37 and 109 divide every
R3 root. Original f=1 also supplies no eligible tail. Thus it has
restricted period seven and original f=21.
These are three different K primes, one per v-phase. This is precisely I.

## 4. Otherwise at least three period-seven channels are forced

Assume all seven f are coprime to three, and let m count the f=7 classes.
Irredundancy makes their row labels distinct and occupied. Thus 0<=m<=4.

For m=0, at most two f=10 classes have mass 5/2 each, and at most two f=8
classes have mass 13/8 each. Every other non-seven class has mass at most
3/2: the four gcd columns 1,5,7,35 give respectively 13/11,5/4,3/2,1.
Consequently the seven classes have total mass at most

\[
2\cdot\frac52+2\cdot\frac{13}8+3\cdot\frac32
=\frac{51}4<13.
\]

For m=1, the complement D has r=10 or 11 points, with c5<=4,c7<=3.
There are at most two f=10 classes, each of mass at most two; at most
three f=14 classes, each of mass at most 3/2; at most two f=8 classes,
each of mass r/8. Every other class has mass at most one. The six remaining
slots therefore have total mass at most

\[
4+\frac92+\frac r8<r\qquad(r=10,11).
\]

This uses the largest possible six contributions in the correct order;
it does not force the dictionary to spend slots on period-eight classes.

For m=2, the complement consists of three rows and has r=7,8 or 9 points.
Every remaining class has mass at most 3/2, so five classes cannot cover
r=8 or 9. If r=7, the row sizes are 2,2,3. All classes except f=10 and
f=14 have mass at most one. To reach seven, at least four of the five
classes would need mass greater than one. Only the two f=10 primes and
f=14 classes on the unique large row can do so. Irredundancy allows at
most two distinct f=14 phases on that row. Thus both f=10 primes and both
opposite f=14 phases are required. After removing the large row covered
by those two f=14 classes, the two f=10 classes contribute at most one
each on the remaining four points, and the fifth class contributes at
most one. Their mass is at most three, a contradiction.

Therefore m is three or four.

## 5. Three period-seven channels: types II and III

The complement consists of two rows, and four classes remain.

If both rows are large, each non-f14 class has mass at most one. Since
there are only three J primes, total mass is at most `3*(3/2)+1<6`.

If the rows have sizes three and two, every class other than an f=14
class on the large row contributes at most one. At least two such f=14
classes are needed. They have opposite parities, cover the large row
completely, and consume two distinct J primes. The last two classes must
cover the two small-row points. Two-class coverage of all their lifts
either uses two opposite f=14 classes or two f=35 point classes. The first
would require four J primes in total. The second gives type II.

If both rows are small, they are exactly rows one and five. Every class
has mass at most one, so all four must attain one and their intersections
on the residual set must be empty. The only attaining periods are ten,
fourteen and thirty-five. Resolve the four points by row, column, and
parity. A period-ten class joins the two row choices at fixed column and
parity; a period-fourteen class joins the two column choices at fixed row
and parity; a period-thirty-five class joins the two parities at one point.
Thus the four classes form a perfect matching of the cube with eight
vertices. Its nine perfect matchings are three parallel-axis matchings
and two mixed matchings for each pair of axes. The pure T and pure J
matchings exceed their prime inventories; the other seven give type III.

## 6. Four period-seven channels: types IV--VIII

One row c remains, containing r=2 or 3 points in different modulo-five
columns. Each of the last three classes either meets all these points
(a common class, gcd(f,35)=1 or 7), or meets exactly one (a point class,
gcd(f,35)=5 or 35). Its lift period at a compatible point is `e=f/gcd(f,35)`.

A common class cannot have e=1, because all four period-seven primes have
already been used and period one is unavailable. A point class has e=1
exactly when it is an f=35 class. A common class of e=2 comes from J;
one of e=4 comes from L. A point class of e=2 comes from S=T union V.
All e are coprime to three.

If all three are common, an irredundant three-class cover of the integers
with periods coprime to three must have periods 2,4,4. Indeed, if no period
two occurs, the sum of densities is at most 3/4. After the period-two class
is chosen, the two remaining classes must cover its opposite parity.
A second period-two class would already complete the cover, violating
irredundancy. Therefore the two induced periods are both two, and the
original periods are both four, with opposite quarter phases. This is IV.

If exactly one class is a point class, the other two common classes must
cover another point entirely. They necessarily are opposite period-two
classes and hence cover every point; the point class is redundant.

If exactly two are point classes and r=3, the sole common class would have
to cover the third point alone, impossible. If r=2, the point classes must
be assigned one to each point. At least one of them has e>1, otherwise the
common class is redundant. At that point the two-class cover forces the
common and point periods both to be two and their phases opposite.
The other point class either has e=2 as well (VI), or e=1 (VII).

If all three are point classes and r=3, each point must receive one full
period-one class, giving V. If r=2, one point gets one full period-one
class and the other gets two opposite period-two classes, giving VIII.
These exhaust all possibilities.

## 7. Counts and exact-cost realization

For a prime q assigned v phase b, the root residues are exactly

\[
a\equiv\pm 2^{-(4+6b)}\pmod q.
\tag{3}
\]

All selected tail primes are outside the fixed 43-prime modulus, hence CRT
realizes every listed assignment and its independent seven signs.

The eight counts are, in the order of the theorem,

\[
\begin{aligned}
&5\cdot4!\cdot(5)_3=7200,\\
&6\cdot(4)_3\cdot(3)_2\cdot(12)_2=114048,\\
&(4)_3\big((12)_4+2(2)_2(3)_2+2(2)_2(12)_2+2(3)_2(12)_2\big)=336384,\\
&5\cdot2\cdot4!\cdot3\cdot(5)_2=14400,\\
&3\cdot4!\cdot(12)_3=95040,\\
&2\cdot2\cdot4!\cdot3\cdot(7)_2=12096,\\
&2\cdot2\cdot2\cdot4!\cdot3\cdot12\cdot7=48384,\\
&2\cdot2\cdot4!\cdot12\cdot(7)_2=48384.
\end{aligned}
\]

Here `(t)_j=t(t-1)...(t-j+1)`. The seven group slots always use distinct
primes, and within each geometry the phases identify the slot, so the
counts do not duplicate dictionaries. Different dictionaries can describe
the same root.

To realize exact cost nine, retain the selected coordinates and set every
unselected coordinate of the complete v13 eight-budget observer to zero.
The two-W eight predicate is false: no B8 or D6 coordinate occurs, and at
most two of its four C10 primes occur. For the zero-W eight predicate,
types II and III have only three active Z coordinates. Type I has no J
or U; type IV has only one J; type V leaves a large row, for which the
two-U eight-cover is impossible; types VI--VIII have at most one J and
at most one U. Thus no eight-cover remains. All roots in the resulting
CRT progression have delta_P=9 by the displayed cover and the inherited
complete eight-budget theorem. A sufficiently large positive segment
ensures the listed divisors are proper. There are infinitely many such
ordinary integer roots for each phase dictionary.

This argument does not claim that every root in every original nine-cover
description has exact cost nine: incidental eight-covers are possible.
The full predicate is existence of one of the nine-cover descriptions
combined with negation of the complete eight-budget predicate.

## 8. Verification and inherited sources

The companion arithmetic verifies all residual row cases, complete prime
inventories, cube matchings, representative phase geometries, irredundancy,
counts, CRT realizations and the complete eight-budget predicate. The
all-prime exclusion is the argument above; no finite search extrapolation
is used. New executable outputs explicitly state whether a native BRC
execution has occurred.

Inherited scientific inputs are the complete v13 eight classification at
`e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124`
and the v14 forced basic pair and one-W inventory at
`9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124`.

## 9. Exact exclusion below the global candidate index

The companion `verify_minimum_below_bound.py` checks all forty-seven
geometric patterns of the theorem at the strict R3 index bound

\[
0\le j<11380571075,\qquad a=A_3+S_3j.
\tag{4}
\]

For each slot (q,b), each root sign gives the exact condition

\[
j\equiv (\pm2^{-(4+6b)}-A_3)S_3^{-1}\pmod q.
\]

The search considers every allowed prime and sign, rejecting only repeated
prime assignments and a nonnegative partial CRT representative at least
the bound. This last pruning is exact: if the partial condition is
`j=x mod M`, with `0<=x<M`, every nonnegative extension has index `x+kM>=x`.
At any complete leaf the program also considers every later lift below
the bound, rather than checking just the first representative.

The actual calculation completed all forty-seven patterns and found
**no complete CRT representative below (4)**. Therefore no zero-W
irreducible nine-cover can improve the 151-digit candidate supplied by
the two-W branch. This is stronger than rejecting low candidates by the
eight-budget predicate: no candidate at all reaches that final check.

This section establishes a lower exclusion for this entire branch, not a
global minimum inside the zero-W branch beyond the tested bound. The
all-prime completeness input is the proved classification, which reduces
the problem to the explicitly exhausted finite CRT union.
