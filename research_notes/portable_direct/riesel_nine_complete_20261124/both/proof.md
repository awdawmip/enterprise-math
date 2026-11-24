# The complete Q0-retaining ninth-budget root predicate on R3

Research continuation v15, 2026-11-24 (Asia/Hong_Kong). Existing Researcher
`EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`.
Author derivation, shared-context mathematical checking, and exact computation;
independent project Review and formal acceptance are not claimed.

The state is the full integer register at the fixed Heartbeat X6 anchor,
with positive singleton BRC action x -> 2x+1, weight and multiplicity one:

\[
x_0=a^2-1,\qquad F_n(a)=a^22^n-1.
\]

Congruences below observe that register. Its integer type, proper-divisor
meaning and common-factor relationships are retained.

## 1. Domain and the result

Use the old twenty-prime dictionary P and the fixed 43-prime fiber

\[
R_3=\{A_3+S_3j:j\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The present theorem concerns the existence of a supplement with at most
nine primes **containing**

\[
Q_0=\{5,13,19,73\}.
\tag{1}
\]

It is a complete root predicate on R3. It is not a claim that every
nine-prime dictionary has the displayed canonical form. Replacing a
dictionary by another equally small dictionary on the same root is used
explicitly below. The other W branches are handled separately.

Write A=38737, R=246241 and U=487824887233. In the w coordinate
n=32+36w, their fixed phases on R3 are

\[
A:w=1\pmod2,\quad R:w=1\pmod3,\quad U:w=2\pmod4.
\tag{2}
\]

Define these disjoint free-prime groups:

\[
\begin{aligned}
Z={}&\{29,43,1429,5419\},\\
G={}&\{92737,649657,40388473189,77158673929,118750098349\},\\
B_8={}&\{193,1153,6337,22253377,38941695937,278452876033\},\\
D_6={}&\{33975937,138991501037953\},\\
C_{10}={}&\{61681,4562284561,168692292721,469775495062434961\},\\
R_{12}={}&\{209924353,4261383649,24929060818265360451708193\},\\
H_{20}={}&\{8369281,394783681,4278255361,46908728641,\\
&\hspace{16mm}750016890283777055704738227247474485366338380663681\},\\
F_{16}={}&\{3457,816769,18446744069414584321,\\
&\hspace{16mm}1562985901350085709953,1422346738975853644793916289\}.
\end{aligned}
\tag{3}
\]

Put G9=Z union G, E5=D6 union R12, and J9=C10 union H20. The
subscripts here record either inherited w-periods or set sizes as shown;
they do not denote a new sequence index.

> **Theorem.** For a in R3, there is a complete supplement of at most
> nine primes containing Q0 if and only if at least one row of the
> following table holds. All assigned free primes in a row are distinct.
> In the last four rows t=w/4.

| Canonical root condition | Fixed tails | Free assignments | Phase descriptions | Signed CRT descriptions |
|---|---|---|---:|---:|
| Five mod-seven rows | none | Five of G9 assigned w=0,1,2,3,5 modulo 7 | 15120 | 483840 |
| Old binary cover | A,U | Two of B8 assigned t=0,1 modulo 2 | 30 | 120 |
| Binary refinement | A,U | One B8 at t=b modulo 2; two F16 at t=1-b,3-b modulo 4; b=0 or 1 | 240 | 1920 |
| Ternary Q7 cover | A,R,U | Two of E5 assigned t=0,2 modulo 3 | 20 | 80 |
| Three mod-five columns | A,U | Three of J9 assigned t=0,2,4 modulo 5 | 504 | 4032 |
| Total | | | **15914** | **489992** |

Every phase at a free prime q is realized by the two root residues

\[
a=\pm2^{-(16+18b)}\pmod q
\tag{4}
\]

when b is its w phase. A t phase b is a w phase 4b. The required
prime coordinates are outside S3, and the categories for different
phases at a fixed prime are disjoint. CRT realizes each description.
The descriptions may overlap as root sets.

The old binary row has cost eight. The other rows can also have incidental
eight-prime alternatives. Therefore the **exact** cost-nine subset of
this branch is the displayed predicate together with the negation of the
complete v13 budget-eight predicate, including its zero-W branch.

All free prime orders in this theorem are at most 720. No unrestricted
total-cost equality is asserted merely from this classification.

## 2. Inherited exact residual and complete inventories

After P and Q0, the holes are

\[
n=32+36w,\qquad
w\bmod35\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}.
\tag{5}
\]

The occupied mod-seven rows are 0,1,2,3,5, of sizes 3,2,2,3,3;
the occupied mod-five columns are 0,1,3, of sizes 5,3,5.
Every occupied row has at most one entry in a given column and includes
both five-entry columns. These are joint incidence facts, not independent
marginal assumptions.

For a set D modulo L and a class of period h, let g=gcd(h,L). Its
relative mass on D is exactly

\[
\frac{K_{D,g}(b)}{|D|(h/g)},\qquad
K_{D,g}(b)=|\{x\in D:x=b\pmod g\}|.
\tag{6}
\]

This follows by exact compatible-lift counting over lcm(h,L).

The available small effective w-periods h=ord_q(2^36) on R3 are:

| h | Available active prime channels outside P and Q0 |
|---:|---|
| 1 | none |
| 2 | A only |
| 3 | R only |
| 4 | U only |
| 5 | none |
| 6 | D6, two primes |
| 7 | G9, nine primes |
| 8 | B8, six primes |
| 10 | C10, four primes |

The checker proves these inventories from full cyclotomic products and
the fixed 43 coordinates. In particular, it restores all the old free
coordinates that were set to zero in R4. The R4 five-tail exclusion cannot
be reused unchanged as a theorem on R3.

The inherited residual and four-tail results are at
`e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124/tail/proof.md`.
The complete Q7 two-tail result and its order-432 inventory are at
`9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/tail/proof.md`.

## 3. Omitting A forces all five occupied mod-seven rows

Suppose a tail of at most five primes omits A. Select the distinct occupied
mod-seven rows hit by period-seven channels, delete them from B, and call
the remainder D. Let m be the number of deleted rows and r=|D|.
Repeated or empty rows only consume slots and do not improve D.

For a non-seven channel outside A,R,U, formula (6) gives the absolute
mass, measured in units of a B residue, at most

\[
E(D)=\max\{r/6,c_5/2,c_7/2,1\},
\tag{7}
\]

where c5 and c7 are the maximum remaining column and row sizes.
The four terms come from gcd(h,35)=1,5,7,35 and the least remaining
periods 6,10,14,35, respectively. This handles arbitrarily large periods.

The fixed R and U channels cover respectively 1/3 and 1/4 of D; jointly
they cover exactly one half, because gcd(35,12)=1. If a of these fixed
tails are selected, put p=0,1/3,1/4,1/2 as appropriate. A necessary
condition is

\[
pr+(5-a-m)E(D)\ge r.
\tag{8}
\]

For m=1,2,3,4, every possible subset of the five occupied rows and every
admissible fixed-tail choice instead gives a strict inequality in the
opposite direction. The exact bounds use only the displayed 13-point
set. `verify_both_tail.py` retains all 115 strictly positive differences
in the certificate. Thus m is either zero or five.

When m=0 and neither R nor U is selected, five generic channels supply
at most 5*(5/2)=25/2<13. The other m=0 cases are excluded by restricting
to the holes of the selected fixed tails:

| Selected fixed tails | Remaining period and size | Maximum mass of one further non-seven channel | Consequence |
|---|---|---|---|
| R only | 26 residues modulo 105 | 1/4, only at h=6 | Four h=6 primes required, but only two exist |
| U only | 39 residues modulo 140 | 10/39 at h=10; other h at most 2/9 | All four remaining primes would have h=10 |
| R and U | 78 residues modulo 420 | 1/3 at h=6; other h at most 10/39 | Three h=6 primes required, but only two exist |

For the U-only row, three maximum channels and one outside period ten
give at most 3*(10/39)+2/9=116/117<1. Four period-ten channels still
cannot cover: the U holes contain all six pairs consisting of a parity
and one of the three occupied mod-five columns. A period-ten class
covers only one such pair.

The table is an all-period bound: for each g dividing the residual
period L, (6) decreases with h/g. The checker considers the least h>=6
outside the excluded periods with gcd(h,L)=g and all residue counts
K(D,g); every larger h in that gcd column has a weaker bound.

Consequently m=5. All five slots are period-seven channels covering the
five occupied rows, which gives exactly the first root predicate in
Section 1. Its counts are 9*8*7*6*5 phase descriptions and 32 signs per
description.

## 4. The finite-period lemma used for the remaining geometry

We use the established Crittenden-Vanden Eynden interval theorem: k
congruence classes covering 2^k consecutive integers cover all integers.
A primary modern proof stating the theorem is Balister, Bollobas, Morris,
Sahasrabudhe and Tiba, *Covering intervals with arithmetic progressions*,
Acta Math. Hungar. 161(1) (2020), 197-200,
<https://par.nsf.gov/servlets/purl/10165575>.

Consider an inclusion-minimal cover of a periodic set D modulo 35 by at
most t classes, with a class of period e and a private point. On the
private point's progression modulo 35, that class has effective period

\[
f=e/\gcd(e,35).
\]

If f>2^(t-1), the next 2^(t-1) positions are covered by the other at
most t-1 classes. The interval theorem makes them cover the entire
progression, contradicting the private point. Therefore

\[
e/\gcd(e,35)\le2^{t-1}.
\tag{9}
\]

All covering predicates are periodic, so a private point may be translated
into the nonnegative-index range before using this argument.

This is a finite reduction on effective periods, not on prime size. For
t=4 it leaves the 26 periods listed in the certificate, all dividing
29400. For t=3, all remaining periods divide 420. The reductions are
exhaustive for all possible primes.

## 5. If A is selected, U can always be inserted at this budget

After A, write w=2z. The holes are

\[
z\bmod35\in B_2=\{0,4,5,13,14,15,19,20,25,28,29,33,34\}.
\tag{10}
\]

U is the only available period-two z channel, at z=1 modulo 2.
If U is omitted, at most four further channels of period at least three
must cover B2. Their inclusion-minimal geometric covers have precisely
the following forms:

| Periods | Phases | Number of geometries |
|---|---|---:|
| 3,3,3 | all phases modulo 3 | 1 |
| 3,3,6,6 | two mod-three phases; split the missing phase c into c,c+3 modulo 6 | 3 |
| 4,4,4,4 | all phases modulo 4 | 1 |
| 5,5,5 | the occupied phases 0,3,4 modulo 5 | 1 |
| 5,5,10,10 | two occupied mod-five phases; split the missing phase c into c,c+5 modulo 10 | 3 |

Here is a short geometric reduction, also checked exhaustively using
(9). One class must have mass at least one quarter, so its period is
3,4, or 5; period five must be one of the two five-point columns. Applying
the same average-mass bound to the remainder gives:

| First two selected periods | Possible inclusion-minimal outcome |
|---|---|
| 3,3 | 3,3,3 or 3,3,6,6 |
| 3,5 | only a complete three-class period-three or period-five cover, with the other selected class redundant |
| 4,3 | the complete three-class period-three cover |
| 4,4 | 4,4,4,4 |
| 4,5 | the complete three-class period-five cover |
| 5,5 | 5,5,5 or 5,5,10,10 |

For example, after two distinct period-three phases, the last phase is
either supplied as a whole or split between two period-six classes:
every other available class covers strictly less than half of it.
After two occupied period-five columns, the remaining column contains
three or five distinct mod-seven rows. A nontrivial two-class completion
again requires two halves, hence period ten. A single mod-seven row can
cover at most one of those entries. The mixed rows in the second table
leave a whole arithmetic progression whose lifts require the remaining
period-three or period-five phase; this makes the extra mixed class
redundant.

For a fully reproducible finite proof check, (9) with t=4 yields 731
nonempty classes on B2 modulo 29400. At a state with k slots left and
remainder D, some class of any successful cover has at least |D|/k hits.
Branching over every such class is exhaustive. The checker visits 318
nodes and returns exactly the nine geometries in the first table,
checking a private point for every retained class. No unsupported prime
cutoff occurs in this verification.

Now insert U, which covers all odd z, and restrict to z=2t. In the
3,3,6,6 geometry, exactly one of the split period-six classes is on even
z; discard the odd one. The remaining three restricted classes all have
t-period three. The 5,5,10,10 geometry similarly becomes three
t-period-five classes. Four period-four classes reduce to the two even
z classes, of t-period two. A three-class period-three or period-five
cover restricts to three classes of that same period. In every case,
adding U and discarding the unused odd classes leaves at most five tails
including A.

Thus any Q0-retaining ninth-budget root which has a cover using A has an
equally small cover using both A and U. This is a root-level replacement
statement; it does not assert that U belonged to the original dictionary.

## 6. With A and U, the remaining three-class cover is completely classified

The holes now have w=4t and

\[
t\bmod35\in B_4=\{0,2,7,10,14,17,20,24,25,27,30,32,34\}.
\tag{11}
\]

The occupied mod-five phases are 0,2,4, with counts 5,5,3. There is no
unselected active period-one channel. All inclusion-minimal covers by
at most three further congruence classes have these five geometries:

| Periods | Phases | Geometries |
|---|---|---:|
| 2,2 | opposite parities | 1 |
| 2,4,4 | b modulo 2, and 1-b,3-b modulo 4 | 2 |
| 3,3,3 | all phases | 1 |
| 5,5,5 | phases 0,2,4 | 1 |

If a period-two class is present, its complement is another progression
with the same 13-point incidence geometry. A second opposite period-two
class already completes it. Otherwise every remaining channel covers at
most half of the complement, with equality only at effective period two
on that progression, namely period four in t. This gives the binary
refinement.

If no period-two class is present, each channel has mass at most 5/13.
Each of three channels must consequently have mass at least 3/13. The
incidence formula reduces the possible t-periods to 3,4,5,7. A period-four
class would require both others to be period five; their uncovered
mod-35 progression cannot be filled by one of its four phase lifts.
A period-seven class would require the two maximal period-five columns;
the remaining t=14,24,34 points have three different mod-seven residues,
so one period-seven class cannot cover them. Finally periods three and
five cannot mix: one or two mod-five columns leave a whole mod-35
progression, which needs all three mod-three phases. The only remaining
triples are the pure period-three and pure period-five triples.

The independent finite check from (9), now t=3, returns exactly these
five geometries on the complete common period 420.

## 7. Translating the geometry to actual primes

The complete active effective t-period inventories are:

| t-period | Available primes |
|---:|---|
| 2 | B8 |
| 3 | fixed R, D6, R12 |
| 4 | F16 |
| 5 | C10, H20 |

For t-period three, the fixed R channel already covers t=1 modulo 3.
In a triple of free period-three classes, replace its phase-one prime
by R. Thus the root-existence predicate reduces to two different primes
of E5=D6 union R12 at phases zero and two. This recovers the complete
Q7 two-tail ternary family, including its cost-eight subfamily.

For t-period five, all nine primes of J9=C10 union H20 must be allowed.
Restricting this inventory to H20 would incorrectly use the stronger
R4 condition on the larger R3 fiber. Selecting three distinct primes and
assigning them to 0,2,4 gives 9*8*7=504 descriptions, with eight signs
each.

The genuinely new inventory in this continuation is t-period four. If
d=ord_q(2), then d/gcd(d,144)=4 forces

\[
d\in\{64,192,576\}.
\]

The complete products are

\[
\begin{aligned}
\Phi_{64}(2)&=641\cdot6700417,\\
\Phi_{192}(2)&=18446744069414584321,\\
\Phi_{576}(2)&=3457\cdot816769\cdot1562985901350085709953\\
&\hspace{12mm}\cdot1422346738975853644793916289.
\end{aligned}
\tag{12}
\]

Both order-64 primes are in P. The remaining five primes form F16. The
order-192 prime is the third listed member of F16; all other members
have order 576. `prime_inventory.json` contains deterministic recursive
n-minus-one certificates. The verifier checks every complete product,
every certificate and every exact base-two order; discovery factoring
software is not used as a primality oracle by the verifier.

More generally the verifier checks all 50 cyclotomic values needed for
the inventories in Sections 2 and 7. To reconstruct an inventory for
ord_q(2^b)=h, it enumerates exactly

\[
d=hg,\qquad g\mid b,\qquad\gcd(h,b/g)=1,
\]

factors the already specified full cyclotomic values, filters by actual
order, and removes P,Q0 and the fixed inactive coordinates. Thus the
finite prime inventories are complete, including any nonprimitive small
factor in a cyclotomic value. There are 75 certified root primes and 147
verified certificate nodes.

Every free prime is coprime to S3. All displayed primes are smaller than
A3^2-1, so their divisibility hits are proper divisors throughout the
positive R3 progression. This proves sufficiency and completes the
root-predicate theorem.

## 8. Exact-cost scope, observations and reproduction

This theorem gives a finite sufficient coordinate set for the Q0-retaining
budget-nine predicate. It does not alone determine all ninth-budget
roots on R3, because one-W and zero-W dictionaries also occur. For an
exact-cost-nine statement, evaluate the complete v13 budget-eight
predicate rather than merely its Q0-retaining part.

The canonical family counts count descriptions, not disjoint root
classes. No natural density is obtained by simply adding those counts.
The theorem also does not assert tau=29: a complete nine-prime supplement
can coexist with a smaller unrestricted total cover after deleting an
old P prime. Such total-cost statements require separate integer lower
bounds.

Run:

```sh
python verify_both_tail.py
```

The standard-library checker writes `both_tail_certificate.json`. It
checks the complete prime inventory, 115 row-deletion inequalities, the
all-order gcd-column bounds, both exhaustive finite geometric reductions,
root-category disjointness and CRT compatibility, and the canonical
description counts. The all-prime reduction and same-root replacement
arguments are proved above. No new native BRC execution is claimed by
this component.
