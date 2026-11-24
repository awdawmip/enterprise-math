# The global minimum of the exact cost-nine class on R3

Research continuation v15, 2026-11-24 (Asia/Hong_Kong).
Researcher `EM-DIRECT-970E1C / TASK_RESEARCH`;
Activity `RA-D2EC212845B63844081F9A14`.
Author proof, shared-context collaborative mathematical checking, and actual
integer/native execution. Independent project Review and formal acceptance
are not claimed.

## 1. Integer object, costs and result

The native object is the full integer register at the fixed Heartbeat X6
anchor, with positive singleton BRC action `x -> 2x+1`, weight and
multiplicity one. Starting at `x0=a^2-1` gives

\[
F_n(a)=a^2 2^n-1\qquad(n\ge0).
\]

Let P be the inherited twenty-prime dictionary. The quantity delta_P(a)
minimizes the number of additional primes needed with P retained; tau(a^2)
minimizes the entire prime dictionary without requiring P. Every hit must
be a proper prime divisor. These are minima for the entire infinite
trajectory, not for an observed prefix.

The fixed 43-coordinate fiber is

\[
R_3=\{A_3+S_3j:j\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

**Theorem.** The whole exact-cost-nine class on R3 has the minimum

\[
\boxed{\min\{a\in R_3:\delta_P(a)=9\}=A_3+11380571075\,S_3.}
\tag{1}
\]

Its 151-digit value is

```text
4535953965311753528081323514270677649037193321945505620446333306332288510872289104091229337616491589657748499046945212207565221052351500539027726253413
```

For this root, denoted a9,

\[
\boxed{\delta_P(a_9)=9,\qquad\tau(a_9^2)=29.}
\tag{2}
\]

The root is the minimum over all R3 roots of exact supplemental cost
nine. It is not merely the minimum among dictionaries containing a fixed
seven-prime prefix, and it is not a minimum over the larger R1 or R2.

## 2. Why all primes reduce to the three W branches

The v14 all-prime basic-pair theorem forces 5 and 13 in every complete
supplement of at most nine primes. For a root of exact cost nine, a
minimum supplement is irredundant. Its intersection with W={19,73} has
zero, one or two elements.

The zero-W branch is the eight-type classification in `../zero/proof.md`.
The one-W classification and its complete minimum are in `../one/proof.md`.
The two-W branch is the complete canonical **root-existence** predicate
in `../both/proof.md`. In this last branch same-root replacements can
produce a dictionary containing fixed tail channels. Consequently its
canonical list exhausts roots, even though it is not a list of all raw
nine-prime dictionaries.

All of these are all-prime reductions, based on exact joint residual
incidence and complete effective-order inventories. The finite arithmetic
below therefore has no empirical prime-size cutoff.

## 3. Exhausting canonical CRT descriptions without losing later roots

For each canonical description, the fixed free-prime root residues r_q
impose

\[
j\equiv(r_q-A_3)S_3^{-1}\pmod q.
\tag{3}
\]

The free primes are distinct and coprime to S3. If their product is M,
there is a least nonnegative index j0 modulo M, and every root of that
description in R3 is

\[
A_3+S_3(j_0+kM),\qquad k\ge0.
\tag{4}
\]

In particular, no later root is smaller than its first representative.
When a first representative has cost eight, it would be invalid simply
to discard all its later representatives: another prime coordinate can
change along (4). The calculation avoids this problem as follows.

For each canonical family, first minimize over every signed CRT first
representative without filtering by cost. In each relevant family the
resulting minimum itself fails the **complete** budget-eight predicate,
including its zero-W alternative. It is therefore a cost-nine root and
minimizes that whole family. The only descriptions omitted beforehand
are structurally cost eight for every root: the old binary family and
the ternary descriptions using both members of D6. No incidental
first-root cost-eight event is used to discard a progression.

The exhaustive results are:

| Two-W canonical family | Signed CRT starts | Minimum exact-nine index j | Digits |
|---|---:|---:|---:|
| Five occupied mod-seven rows | 483840 | 183162559016 | 152 |
| Old binary completion | 120 | every root has cost at most eight | — |
| Binary refinement | 1920 | **11380571075** | **151** |
| Ternary Q7 completion | 80 | 282899156086651 | 156 |
| Three occupied mod-five columns | 4032 | 9783969331088138390 | 160 |
| Total | **489992** | | |

For the ternary family, eight signed descriptions always have cost eight;
the minimum over the other 72 is itself exact cost nine. All 80 are still
included in the enumeration count and retained in the family summary.
The minimum index of the old binary family is 63706, but none of its
roots belongs to the exact-nine class.

The complete one-W calculation exhausts 307200 signed starts and has
minimum index 811311504227722, which exceeds (1). The zero-W calculation
handles all 47 geometries of its eight types. It exhausts all prime and
sign assignments compatible with the strict bound

\[
0\le j<11380571075.
\]

At a partial CRT node j=x modulo M, with 0<=x<M, a nonnegative extension
has j=x+kM>=x. Pruning x at or above the bound therefore loses no smaller
root. Every later lift at a complete leaf would also be checked. The
actual calculation finds no complete candidate below the bound. Its
certificate records 2424 recursive nodes, 24765 nonnegative-index prunes
and 4995 repeated-prime prunes. This excludes the entire zero-W branch
below the winner without enumerating its 86,519,808 signed descriptions
one at a time.

Combining all three branches proves the global minimality in (1).

## 4. The winning nine-prime supplement

The supplement is

\[
Q_9=\{5,13,19,73,38737,487824887233,1153,3457,816769\}.
\tag{5}
\]

After P and {5,13,19,73}, write n=32+36w. The fixed 38737 channel
covers odd w, and 487824887233 covers w=2 modulo four. Thus only w=4t
remains. The three new free conditions are:

| Prime | Root residue | Base-two order | n zero phase | Restricted t phase |
|---:|---:|---:|---:|---|
| 1153 | 529 | 288 | 176 modulo 288 | 1 modulo 2 |
| 3457 | 2775 | 576 | 32 modulo 576 | 0 modulo 4 |
| 816769 | 737278 | 576 | 320 modulo 576 | 2 modulo 4 |

The t classes are a complete binary partition of the integers. Every
remaining old residual point is therefore covered. The checker also
verifies the whole dictionary directly on its exact common n-period
20160. The orders divide that period and every position has a hit.
All selected primes are less than a9^2-1; each hit is a proper divisor.
Hence delta_P(a9)<=9 and tau(a9^2)<=29.

## 5. Full-integer lower bounds for both minima

For each q in P union Q9, select the following exponent n_q:

```text
(5,6) (7,16) (13,12) (17,3) (19,152) (31,89) (41,5)
(71,293) (73,128) (97,117) (113,833) (127,113) (151,41)
(241,33) (257,87) (281,233) (337,773) (641,527) (673,333)
(1153,2480) (1321,257) (3457,2912) (14449,473) (29191,593)
(38737,140) (65537,95) (816769,320) (6700417,111)
(487824887233,2120)
```

The retained certificate stores each **full integer** F_n(a9), its proper
selected divisor and its exact cofactor. All 406 pairs have gcd one.
Consequently any prime dictionary covering the entire sequence must use
at least 29 different primes: one prime cannot divide two of these terms.
This proves tau(a9^2)>=29 without restricting a competitor to the displayed
dictionary or to the finite observer universe.

The nine witnesses assigned to Q9 are also coprime to the product of P.
Every supplement must cover each by a prime outside P, and their mutual
coprimality requires nine distinct such primes. Therefore delta_P(a9)>=9.
Together with Section 4 these prove (2). The complete eight-predicate
test used in the minimum enumeration is an additional check; the selected
root's lower bounds also follow directly from integer common factors.

## 6. A second root with the same supplemental cost and smaller total cost

The one-W minimum is

\[
a_{1W}=A_3+811311504227722\,S_3,
\]

and `../one/proof.md` proves

\[
\delta_P(a_{1W})=9,\qquad\tau(a_{1W}^2)=28.
\tag{6}
\]

The selected nine-prime supplement contains only 73 from W, together with
5,13,29,43,1429,5419,92737,649657. Their joint phases make the old prime
113 removable. A complete 28-prime cover gives the upper bound, and
28 pairwise coprime full integer terms give the matching lower bound.
A second 28-term witness set additionally makes all nine extra-prime
witnesses P-free, so delta_P=9 also has a direct integer proof.

The two roots (1) and (6) lie in the same R3 fiber. They share every
future residue at the 43 fixed prime channels, and have the same exact
supplemental cost, but different exact total costs. Thus tau=20+delta_P
is a property of specific coprimalized families, not an identity on R3.
The one-W proof also gives an infinite ordinary arithmetic progression
with the exact pair (delta_P,tau)=(9,28).

## 7. Actual native execution and reproduction

The checker uses four frozen native source modules from EM commit
`b1efc6c805661ed7b476e6e730107da6043176ee`, checking their Git blob IDs
before import:

| Module | Git blob |
|---|---|
| brc_transport.py | be1debe367263931bd5e93fd750be3ed54624fe1 |
| brc_histogram.py | 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1 |
| brc_rational_holonomy.py | 2591640fe348da9cd7f293a957bea9ae92c82943 |
| brc_weighted_recurrent.py | 4e6b3132580e3cd70a20a0d8bd4d28792b961afb |

It actually composes the positive singleton BRC step with itself,
checks the two-step effect x -> 4x+3 and unit weight/multiplicity, and
executes both full integer trajectories through their witness intervals.
Every native state agrees with the integer formula. Euclidean quotient
and remainder readouts are checked individually, and the joint readout
is recomposed into exactly the original integer.

Actual counts in this component are:

| Operation | Count |
|---|---:|
| One-step native updates | 9424 |
| Two-step composite evaluations | 4712 |
| Prime quotient/remainder readouts | 453040 |
| Joint readouts and recompositions | 9424 of each |
| Fixed-43 future residue comparisons | 405232 |
| Witness entries across three sets | 85 |
| Gcd-one checks across those sets | 1162 |

There are **two distinct roots and three witness sets**: 29 terms for the
global minimum, plus two separate 28-term sets for the same one-W root.
Counts across sets are actual checks, not a claim that all pairs or all
witness entries are distinct. Native execution covers the witness
intervals (through n=2912 and n=6512); whole-sequence covering is supplied
separately by the exact periodic argument and full-period calculation.

In the reproduction package, from its root run:

```sh
python research_notes/portable_direct/riesel_nine_complete_20261124/global/verify_global_minimum.py --source-dir src
```

The adjacent zero and one certificates must first be generated by their
respective scripts. The global checker records those dependencies,
recomputes every canonical two-W CRT start, verifies the two full-integer
lower bounds, and performs the native execution when `--source-dir` is
provided. It does not treat a certificate hash as a replacement for the
underlying branch proof.
