# The complete one-W minimum on R3 and a strict gap between the two costs

Research date: 2026-11-24, Asia/Hong_Kong. This continues researcher
`EM-DIRECT-970E1C / TASK_RESEARCH`, Activity `RA-D2EC212845B63844081F9A14`.
This is an author derivation with exact computation and shared-context
collaboration. It does not claim independent project Review or formal proof
acceptance.

## 1. Integer state, scope and inherited complete classifications

At the same fixed Heartbeat X6 anchor, retain the full positive singleton
BRC integer register

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad
F_n(a)=a^2 2^n-1.
\]

The residue channels below are observations of this integer state. Its
common-divisor relationships remain part of the state used in the proof.
The displayed execution is scalar arithmetic; no additional native BRC run
is claimed here.

Let P be the old twenty-prime dictionary. The supplemental cost delta_P
allows all P primes to remain, and counts only new primes. The total cost
tau allows the entire dictionary to be chosen anew. These two optimization
problems have different admissible sets.

Use the fixed 43-prime fiber

\[
R_3=\{A_3+S_3j:j\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The exact fixed residues are embedded in the checker; it verifies
S3=6*product(FIXED43) and every A3 residue. In this note the admissible
one-W set is

\[
\mathcal A_{1W}=
\{a\in R_3:\delta_P(a)=9,\ \text{some nine-prime supplement
contains exactly one of }19,73\}.
\]

Two previously proved complete results are reused:

1. The v14 one-W classification:
   `9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/prefix/proof.md`.
   Every inclusion-minimal one-W nine-prime supplement has the structure
   recalled in Section 2. This is an all-prime theorem, not a prime-size
   search restriction.
2. The complete v13 budget-eight predicate:
   `e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124/observer/proof.md`.
   It includes both the retained-W and zero-W alternatives. Its exact
   31-coordinate predicate is embedded in the new checker.

## 2. Complete finite domain and a minimum without progression truncation

Put

\[
Z=\{29,43,1429,5419\},\qquad
K=\{92737,649657,77158673929,40388473189,118750098349\}.
\]

Writing n=8+12v, the selected W prime fixes v=0 modulo three for W=19,
or v=1 modulo three for W=73. The four Z primes have four distinct phases
from {1,2,3,4,5} modulo seven, leaving one missing row c. Two different K
primes occupy the two phases b modulo 21 such that b=c modulo seven and
b differs from the W phase modulo three.

There are therefore

\[
2\cdot5\cdot4!\cdot5\cdot4=4800
\]

phase dictionaries. Each of the six free prime residues has two signs,
so there are 307200 signed CRT descriptions. The six free primes are all
coprime to S3. For a prime q at v phase b the two residues are

\[
a\equiv\pm2^{-(4+6b)}\pmod q.
\tag{1}
\]

For a fixed description, let M be the product of its six free primes.
The root index j must satisfy

\[
j\equiv(r_q-A_3)S_3^{-1}\pmod q.
\tag{2}
\]

Its least CRT index j0 is in [0,M). Consequently

\[
a_0=A_3+S_3j_0\in(0,S_3M)
\]

is the least positive root of that description. Every later positive root
is a0+k*S3*M with k>=0, hence is at least a0.

The checker enumerates all 307200 descriptions, grouped into 100 cases
indexed by W, c and the unordered K pair. Each group has 3072 starts; its
minimum and achieving phase/sign data are retained in the certificate.
The global least first root is

\[
\boxed{a_{1W}=A_3+811311504227722\,S_3.}
\tag{3}
\]

Its complete decimal value is

```text
323364408543007321903311572653400317900622306273030390762905871847856938179871543582589560419967265786024995230650782386881939058243788541171427741450118743
```

It has 156 digits. Its achieving supplementary dictionary is

\[
Q=\{5,13,73,29,43,1429,5419,92737,649657\}.
\tag{4}
\]

The free conditions are:

| q | v period | v phase | root residue | sign in (1) |
|---:|---:|---:|---:|---|
| 29 | 7 | 1 | 16 | minus |
| 43 | 7 | 2 | 32 | minus |
| 1429 | 7 | 5 | 256 | minus |
| 5419 | 7 | 3 | 2709 | plus |
| 92737 | 21 | 11 | 47093 | minus |
| 649657 | 21 | 18 | 633273 | minus |

Thus W=73 and c=4. The complete eight predicate is false: all three
retained-prefix alternatives are false, the f=14 missing-row alternative
is false, and the f=35 alternative is inapplicable because the missing
row has three occupied positions. The entire predicate and all 31 actual
root residues are retained, rather than only a subset of its alternatives.

The period check gives a proper P+Q cover, hence delta_P(a1W)<=9. The
complete eight exclusion gives delta_P(a1W)>=9. Therefore a1W is in
A1W. Since it was already the global minimum over all the unfiltered
signed first roots, every member of A1W is at least it:

\[
\boxed{\min\mathcal A_{1W}=a_{1W},\qquad\delta_P(a_{1W})=9.}
\tag{5}
\]

No progression has been discarded because its first root happened to have
cost eight. Such a discarded-progression shortcut would be invalid in
general. Here the least unfiltered first root itself has exact cost nine,
so all later roots in every progression are automatically irrelevant to
the minimum.

The earlier Q7-containing cost-nine minimum has R3 index
282899156086651, strictly smaller than 811311504227722. Hence the whole
one-W branch cannot improve that already known global R3 candidate. This
comparison alone does not settle the zero-W or both-W branches.

## 3. The old prime 113 is redundant at this minimum

The full P+Q dictionary has 29 primes, but 113 has no private position.
The following exact congruence cover gives a short explanation.

At every R3 root, the 113 zero class is n=21 modulo 28. Write

\[
n=21+28t.
\]

At a1W the following selected prime classes cover every integer t:

| selected prime | zero class in t |
|---:|---|
| 7 | t=1 modulo 3 |
| 92737 | t=2 modulo 9 |
| 649657 | t=5 modulo 9 |
| 73 | t=8 modulo 9 |
| 241 | t=3 modulo 6 |
| 97 | t=0 modulo 12 |
| 673 | t=6 modulo 12 |

The middle three modulo-nine classes cover t=2 modulo three. The last
three classes cover t=0 modulo three: the 241 class covers odd multiples
of three, and the 97 and 673 classes cover even multiples. Along with
the first row, they cover all integers. Each claimed zero phase is checked
against the full root.

Consequently

\[
(P\setminus\{113\})\cup Q
\]

is a proper complete dictionary of 28 primes, and

\[
\tau(a_{1W}^2)\le28.
\tag{6}
\]

This does not lower delta_P: that cost counts how many new primes are
required while P is available, and the complete eight predicate has
already excluded all supplements of size at most eight.

## 4. Twenty-eight full coprime terms prove the matching total lower bound

The full residue period of the displayed selected dictionaries is 20160.
The checker actually advances all 29 residue registers through this
period, performs 584640 scalar recurrence readouts, and finds no uncovered
position even after deleting 113. Each of the remaining 28 primes has
private positions relative to that reduced dictionary.

Choosing the 649657 witness first, and then taking the first compatible
private item in increasing prime order, gives the following full integer
terms F_n(a1W):

| assigned prime | exponent n | assigned prime | exponent n |
|---:|---:|---:|---:|
| 649657 | 413 | 281 | 233 |
| 5 | 6 | 337 | 248 |
| 7 | 16 | 641 | 207 |
| 13 | 12 | 673 | 237 |
| 17 | 3 | 1321 | 257 |
| 29 | 440 | 1429 | 320 |
| 31 | 89 | 5419 | 212 |
| 41 | 125 | 14449 | 53 |
| 43 | 32 | 29191 | 593 |
| 71 | 293 | 65537 | 63 |
| 73 | 812 | 92737 | 2912 |
| 97 | 117 | 6700417 | 111 |
| 127 | 113 | 151 | 41 |
| 241 | 33 | 257 | 87 |

The greatest exponent is 2912. The certificate retains all 28 full
integers in hexadecimal, their assigned-prime quotients and zero
remainders, and all

\[
\binom{28}{2}=378
\]

pairwise gcds. Every gcd is exactly one. One prime can divide at most one
of these terms, so every complete prime dictionary needs at least 28
different primes. Combining this with (6),

\[
\boxed{\delta_P(a_{1W})=9,\qquad\tau(a_{1W}^2)=28.}
\tag{7}
\]

The initial increasing-prime greedy attempt failed at 649657. Placing
that item first succeeds; the verified finite list, not any universal
claim about greedy algorithms, is the evidence. The checker retains the
rejections from the successful search order.

### 4.1 A stronger seed with nine P-free witnesses

The short certificate above is sufficient for tau=28. Its 649657 witness
at n=413 also has the old factor 113, so it does not by itself furnish a
direct nine-new-prime lower bound. A second search restricts the nine
supplemental witnesses to terms coprime to the product of all P primes,
while still requiring all 28 selected terms to be pairwise coprime.

It succeeds within the same period, using the following exponents in the
same prime-selection order as the first certificate:

```text
(649657,728), (5,6), (7,16), (13,12), (17,3), (29,860),
(31,89), (41,125), (43,1040), (71,293), (73,560), (97,21),
(127,113), (151,41), (241,33), (257,87), (281,233), (337,248),
(641,207), (673,237), (1321,257), (1429,320), (5419,6512),
(14449,53), (29191,593), (65537,63), (92737,2912), (6700417,111).
```

All 378 pairwise gcds are one. For each of the nine assigned primes in Q,
the witness also has gcd one with product(P). These nine mutually coprime
terms therefore force at least nine new primes in every supplement,
independently of the complete eight observer. The maximum index of this
stronger set is 6512. Both finite witness sets and their full integer
values are preserved; they concern the same root and are not two distinct
root examples.

One useful refinement invariant is particularly simple. On the 1429
channel write n=68+84i. Among P, only the following channels can hit:

| prime | i phase |
|---:|---|
| 31 | 4 modulo 5 |
| 151 | 2 modulo 5 |
| 29191 | 0 modulo 5 |

Thus P-freeness is exactly i=1 or 3 modulo five. Among the other
supplemental channels, only 73 can hit, at i=2 modulo three. Consequently
the private P-free part of this channel is exactly

\[
i\equiv1,3,6,13\pmod{15}.
\tag{7a}
\]

Every pure binary residue class of i meets this set, because its period
is coprime to 15. The period check obtains 64 such positions among the
240 parent-channel positions in the original full period. This is a
verified seed property for a later refinement construction; this note
does not claim an unbounded cost-gap family from it.

## 5. An infinite arithmetic progression with the same strict cost gap

Let n1,...,n28 be the exponents in Section 4 and let T8 be the product of
the complete 31-prime budget-eight observer. Define the explicit integer

\[
L=\operatorname{lcm}\Bigl(S_3,T_8,92737\cdot649657,
\{2^{|n_i-n_j|}-1:1\le i<j\le28\}\Bigr).
\tag{8}
\]

The checker constructs this integer exactly. It has 106703 bits; its
full hexadecimal representation and all 269 distinct positive witness
differences are retained.

For every integer t>=0 put a=a1W+Lt. The fixed S3 congruence keeps a in
R3. The T8 congruence preserves the false complete eight predicate. All
selected prime residues are also preserved, so the same reduced
28-prime cover remains valid and gives delta_P<=9, tau<=28.

For n<m, the terms are odd and the elementary exact gcd identity is

\[
\gcd(F_n(a),F_m(a))
=\gcd(F_n(a),2^{m-n}-1).
\tag{9}
\]

Indeed F_m(a)=2^(m-n)F_n(a)+(2^(m-n)-1), and F_n(a) is odd. Since L is
divisible by each 2^|ni-nj|-1, the right side for every witness pair is
unchanged from a1W, where it equals one. Thus all 28 witnesses remain
pairwise coprime along the entire progression. Properness also persists
because a>=a1W and a1W^2-1 exceeds every selected prime. Therefore

\[
\boxed{\forall t\ge0:\quad
\delta_P(a_{1W}+Lt)=9,\qquad
\tau((a_{1W}+Lt)^2)=28.}
\tag{10}
\]

This infinite conclusion follows algebraically from fixed congruences
and the finite coprime witness set; it is not an extrapolation from a
finite execution.

## 6. Consequence for joint residual information

The earlier 156-digit Q7-containing minimum has exact delta_P=9 and
tau=29, proved at
`9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/totals/proof.md`.
It and a1W lie in the same R3 fiber, hence have the same complete future
trajectories at all 43 fixed prime coordinates. They also have the same
supplementary cost, but different total costs:

\[
(\delta_P,\tau)=(9,29)\quad\hbox{and}\quad(9,28).
\]

Thus the exact supplementary cost alone does not determine the total
cover cost even on this one fixed 43-channel trajectory. The new example
also proves that the equality tau=20+delta_P in the earlier coprimalized
families is a feature of those families, not a universal identity on R3.
Here one of the old channels is absorbed by joint phases of other old
and new channels.

## 7. Reproduction and evidence boundaries

Run:

```sh
python verify_one_w_minimum.py
```

The script uses only Python's standard library. It deterministically
trial-verifies all primes needed for the displayed classification's new
choices and the selected dictionary; the complete one-W classification
and complete eight observer retain their cited earlier all-order proofs.
It exhausts 307200 CRT first roots, retains all 100 group minima, checks
the selected root against the whole eight predicate, checks the full
20160 period, and evaluates all 28 full integer witnesses and 378 gcds.
It also constructs the explicit modulus in (8) and verifies every required
divisibility. The additional P-free seed performs a further 378 full gcd
checks on its own 28-term list, verifies that all nine supplemental terms
avoid every P prime, and checks the exact private geometry (7a).

The resulting `one_w_minimum_certificate.json` records exact integers,
including large values as decimal or hexadecimal strings where needed.
It does not treat an unrestricted prime search as finite without proof,
does not claim native execution, and does not claim a global minimum on
the still larger class of all R3 cost-nine roots.
