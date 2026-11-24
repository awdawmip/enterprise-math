# Budget eight has a genuine prefix bifurcation in the fixed R3 fiber

Research continuation, 2026-11-24. Author proof with collaborative mathematical checking. The native object remains the full integer register at the fixed Heartbeat X6 anchor, with positive singleton BRC update x -> 2x+1. Exponent fibers and prime phases are observations of that integer; its full state and joint divisor relations are retained.

## 1. Statement and inherited input

Use F_n(a)=a^2 2^n-1, the old twenty-prime dictionary P, and exactly the fixed 43-prime root fiber R3 of the preceding cost-eight theorem. Its progression is A3+S3 j, j>=0, with

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The complete seven-prime theorem gives delta_P(a)>=8 throughout R3. The budget-eight basic-pair theorem forces 5 and 13 in any complete supplement of at most eight primes throughout R1, hence throughout R3. Every budget-eight complete dictionary here is consequently inclusion-minimal.

**Theorem.** If a belongs to R3 and Q is a complete supplementary prime dictionary with |Q|<=8, then |Q|=8 and:

1. Q contains both 5 and 13.
2. Q contains either both or neither of 19 and 73; exactly one is impossible.
3. In the branch omitting both, its other six primes have exactly the following structure.

Let

\[
Z=\{29,43,1429,5419\},\qquad J=\{3361,15790321,88959882481\},
\]

\[
U=\{211,421,86171,106681,122921,152041,664441,1564921,
7416361,47392381,146919792181,1041815865690181\}.
\]

After P,5,13 write n=8+12v. The four primes in Z cover four different classes from v=1,2,3,4,5 modulo 7. Let c be the omitted class.

| Family | Last two primes | Required phases | Phase dictionaries |
|---|---|---|---:|
| Split the remaining mod-seven class | Two distinct primes in J | v=c and c+7 modulo 14, one per prime; c may be any of 1,2,3,4,5 | 720 |
| Cover its two individual residues | Two distinct primes in U | For c=1 take v=1,22 modulo 35; for c=5 take v=12,26 modulo 35 | 6,336 |

Thus this branch has exactly 7,056 phase dictionaries and 451,584 sign-specific CRT progression descriptions. Different descriptions may overlap as root sets. Every displayed dictionary is realized by infinitely many positive roots in R3 with exact supplementary cost eight.

In particular, the four-prime prefix {5,13,19,73} is not forced at budget eight. Its conditional classification is the other branch of the complete question.

## 2. Residual geometry and complete small-order input

After P,5,13 the remaining positions are exactly

\[
n=8+12v,\qquad v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{1}
\]

Their nonempty mod-seven rows are:

| v modulo 7 | A residues | v modulo 5 |
|---:|---|---|
| 1 | 1,22 | 1,2 |
| 2 | 2,16,30 | 2,1,0 |
| 3 | 10,17,31 | 0,2,1 |
| 4 | 11,25,32 | 1,0,2 |
| 5 | 12,26 | 2,1 |

Each row contains at most one point of each mod-five category. The row sizes are 2,3,3,3,2. Modulo five the counts are (3,5,5,0,0).

An active prime q gives one v-class of period

\[
f_q=\operatorname{ord}_q(2^{12}).
\]

For any residual subset R of A, set g=gcd(f,35), e=f/g. Its absolute residual contribution, measured in units of one entire residue class modulo 35, is

\[
\frac{K_{R,g}(c)}e,
\qquad K_{R,g}(c)=|\{r\in R:r\equiv c\pmod g\}|.
\tag{2}
\]

R itself has total mass |R|. This exact common-period formula handles overlap by a union upper bound and retains all lifts of each residue. On a fixed r modulo 35, the channel is either incompatible or covers one lift class of period e.

The fixed W phases are 19 at v=0 modulo 3 and 73 at v=1 modulo 3. The other active small-order channels fixed by R3 all lie in v=2 modulo 3:

\[
38737:v=5\pmod6,\qquad246241:v=5\pmod9,
\qquad487824887233:v=8\pmod{12}.
\tag{3}
\]

On a progression v=r+3z the effective period is h=ord_q(2^36). The complete inventories from the seven-cover proof show: h=1 supplies only old/basic/W/inactive primes; h=2 has only 38737 active; h=3 has only 246241 active; h=4 has only 487824887233 active; every eligible h=5 prime is inactive. In the latter inventory both 11,61,331 and the six primes of the preceding modulo-five completion family have root residue zero. Therefore on v=0 or v=1 modulo 3, every active channel other than its matching W prime has h>=6. The set A becomes an invertible affine copy modulo 35, preserving the row/column incidence properties just displayed.

The complete original-v inventories needed below are

\[
f=7:\ Z=\{29,43,1429,5419\},\qquad
f=10:\ \{61681,4562284561\}.
\tag{4}
\]

These are complete multiplicative-order inventories, rather than cutoffs on prime size. The proof reuses their factorization and exact-order certificates.

## 3. A five-class lemma using the residual row/column mass

**Lemma.** Let A be (1), or any invertible affine copy modulo 35. At most five congruence classes, each with period at least six, cover every lift of A only if they are exactly five period-seven classes, one on each occupied row modulo seven.

Delete redundant classes if necessary. The period-seven rows are then nonempty and distinct. Let m be their count. If m<=4, their complement R consists of 5-m entire occupied rows. A remaining period h is not seven and is at least six. Formula (2) bounds its mass by

\[
\max\left\{\frac{|R|}{6},\frac{c_5(R)}2,
\frac{c_7(R)}2,1\right\},
\tag{5}
\]

where c5 and c7 are the largest column and row sizes. Indeed, the gcd-one column has h>=6; the gcd-five column has h>=10; the gcd-seven column has h>=14; the gcd-35 column contains at most one compatible point, including its possible lift period one.

The table exhausts all m<=4:

| m | Residual size | c5(R) bound | c7(R) bound | Mass of all remaining at most 5-m rows |
|---:|---|---:|---:|---|
| 0 | 13 | 5 | 3 | at most 25/2 < 13 |
| 1 | 10 or 11 | 4 | 3 | at most 8, strictly below the residual size |
| 2 | 7 through 9 | 3 | 3 | at most 9/2, strictly below the residual size |
| 3 | 4 through 6 | 2 | 3 | at most 3, strictly below the residual size |
| 4 | 2 or 3 | 1 | the residual size | at most half the residual size |

Each row uses the full-lift mass (2). In particular, a period-35 channel with e=1 is retained as mass one; it is not discarded. Thus m cannot be at most four. Five period-seven rows must cover exactly the five occupied categories, proving the lemma. The same argument excludes every cover using fewer than five classes.

## 4. Exactly one W prime is impossible

Suppose Q contains exactly one of 19,73. After 5,13 and that prime, at most five channels remain. Restrict to the other W phase: v=1 modulo 3 if 19 was used, and v=0 modulo 3 if 73 was used. The inventory in Section 2 and the five-class lemma force all five remaining channels to have h=ord_q(2^36)=7, with distinct occupied mod-seven phases.

Their original periods satisfy f/gcd(f,3)=7, so each is f=7 or f=21. The other uncovered W phase is v=2 modulo 3. Each occupied mod-seven category has exactly one of these five channels assigned to it. An f=21 channel is confined to the first missing v phase, so it cannot cover the second. Every one of the five channels would therefore have to have f=7. Inventory (4) contains only four such primes. This contradiction rules out exactly one W prime.

## 5. The zero-W branch has no period divisible by three

Suppose Q omits both W primes. Its six channels besides 5,13 are all necessary. Let a count the channels with 3 not dividing f, and let b_r count the other channels whose v-phase is r modulo 3. The former are compatible with every v-phase; the latter with just their one phase.

The five-class lemma on v=0 and v=1 modulo 3 gives

\[
a+b_0\ge5,\qquad a+b_1\ge5,
\qquad a+b_0+b_1+b_2=6.
\]

Thus a>=4. If a=4, necessarily b0=b1=1 and b2=0. The restricted five-row covers force all four common rows to have f=7. They cover only four occupied mod-seven categories, so the remaining category has no cover on v=2 modulo 3. If a=5, one of the first two v-phases has only the five common rows. The lemma forces all five to have f=7, contradicting (4). Hence a=6: all six f values are not divisible by three.

## 6. All four period-seven primes are compulsory in this branch

Let m count the f=7 channels. By irredundancy, they have different occupied mod-seven phases; empty or duplicate phases would make a prime removable after P,5,13. Inventory (4) gives m<=4.

Outside f=7,10, a channel with 3 not dividing f has relative capacity in A at most 1/8. The gcd-one column starts at f=8, while the other column bounds are 5/52,3/26,1/13. Only two primes have f=10. Thus m=0 has capacity at most

\[
2\frac5{26}+4\frac18=\frac{23}{26}<1,
\]

and m=1 has capacity at most

\[
\frac3{13}+2\frac5{26}+3\frac18=\frac{103}{104}<1.
\]

For m=2, the residual R comprises three occupied mod-seven rows, so 7<=|R|<=9 and c5(R),c7(R)<=3. Each of the four remaining non-seven channels has absolute mass at most

\[
\max\{|R|/8,c_5(R)/2,c_7(R)/2,1\}\le3/2.
\]

Their total is at most six, strictly below |R|. This includes every period and the e=1 period-35 case.

For m=3, R comprises two rows, with 4<=|R|<=6 and c5(R)<=2. If |R| is five or six, each remaining channel has mass at most 3/2, so the three channels total at most 9/2<|R|. If |R|=4, both rows have size two, making each remaining contribution at most one. The total is at most three, again too small.

All cases below four are excluded. Necessarily m=4, and all four primes in Z occur.

## 7. The final two rows have exactly two possible geometries

The four period-seven rows leave one occupied class c, with two or three A points having different mod-five residues. If neither remaining row has lift period e=1, both must have e=2 and be compatible with every remaining point in order to cover all their lifts. The possible periods 2,10,14,70 leave only f=14: f=2 is unavailable, f=10 cannot be compatible with different mod-five values, and f=70 cannot be compatible with multiple mod-35 points. The two f=14 phases must be c and c+7 modulo 14.

If a remaining row has e=1, it has f=35 and covers one individual point. With three points in the remaining row, the other channel would have to cover every lift of two distinct points of that row. Its period must divide 35 and their difference, hence divide seven; f=1 is unavailable and f=7 contradicts m=4. If the row has two points, the other channel must cover the second point completely, forcing another f=35 channel. Exactly c=1 and c=5 have two points, giving phases (1,22) and (12,26) modulo 35.

These two geometries are sufficient as well as necessary. No empirical prime bound has been used.

## 8. Complete inventories and CRT realization

For f=14, the possible base-two orders are 56 and 168. Complete factorization and exact-order checks give exactly J, with orders 168,56,168 respectively.

For f=35, the possible base-two orders are 35,70,105,140,210,420. The complete cyclotomic factorizations are:

| d | Factorization of Phi_d(2) |
|---:|---|
| 35 | 71 * 122921 |
| 70 | 281 * 86171 |
| 105 | 106681 * 29191 * 152041 |
| 140 | 7416361 * 47392381 |
| 210 | 211 * 1564921 * 664441 |
| 420 | 421 * 146919792181 * 1041815865690181 |

The auxiliary inventory certificate supplies complete recursive n-1 primality certificates and explicit Lucas witnesses; integer product and exact-order checks identify the full prime sets. Removing the old primes 71,281,29191 leaves the twelve members of U. All six chosen tail primes in either family are distinct from the 43 fixed observations, and hence are coprime to S3.

For a prime q assigned v phase b, the root constraint is exactly

\[
a\equiv\pm2^{-(4+6b)}\pmod q.
\tag{6}
\]

CRT realizes every dictionary and every one of its 64 independent root-sign choices, preserving R3. The first positive term 2a^2-1 is greater than every classified prime, so the selected factors are proper. The old lower bound eight gives exact supplementary cost eight.

The counts are 5*4!*3*2=720 and 2*4!*12*11=6336. Their sum is 7056 phase dictionaries; multiplying by 64 gives 451584 CRT progression descriptions. The explicit subfamily using only 3361 and 15790321 in the first type has 240 phase dictionaries and 15360 signed progressions. Taking its least CRT start is a minimum within that stated subfamily, not by itself a minimum among all roots in R3.

## 9. A directly calculated counterexample

The calculator enumerated all 15,360 sign-specific CRT starts of the stated subfamily using J primes 3361 and 15790321. Its minimum is the 157-digit root

```text
2328897241113208259139956245185224592525672755074106541724691892931740569592108042808841670530672584946713250794691431302234925522619676019002796424675837883
```

Its R3 progression index is 5843132620540248. Its supplementary dictionary is

\[
\{5,13,29,43,1429,3361,5419,15790321\}.
\]

The six tail phases and root residues are:

| q | Effective v period | v phase | a modulo q |
|---:|---:|---:|---:|
| 29 | 7 | 1 | 16 |
| 43 | 7 | 2 | 11 |
| 1429 | 7 | 5 | 256 |
| 5419 | 7 | 4 | 127 |
| 3361 | 14 | 10 | 56 |
| 15790321 | 14 | 3 | 64 |

The complete covering predicate has period 840. The scalar calculator actually executed the selected 28-prime dictionary's complete residue-value cycle of length 6,720, found no uncovered index, and retained a private index for every dictionary prime. This is scalar arithmetic, not a new native BRC run. All 43 fixed R3 coordinates remain unchanged by the CRT construction. The lower bound on R3 proves delta_P=8; the displayed dictionary gives tau<=28.

The minimum is scoped to this explicit subfamily. A separately proved global minimum can use the complete zero-W classification together with the conditional two-W classification; it need not enumerate all 451,584 zero-W descriptions.

## 10. Verification and scientific scope

The exact geometry checker verifies the incidence table, all residual row subsets in the five-class lemma and in Section 6, all rational capacities, and both surviving covering geometries over their complete common periods. The prime inventory has a separate deterministic arithmetic certificate. The explicit counterexample construction checks its full root congruences and complete scalar covering period.

The all-prime result is the analytic classification above. It rules out the one-W branch and completely classifies the zero-W branch. The two-W branch is the independently supplied conditional four-prime-prefix classification. Compact roots from these dictionaries have exact supplementary cost eight and total cost at most 28; no total-minimum equality follows merely from irredundancy.

Dependencies: the v11 seven-cover source at its verified immutable commit supplies the original incidences and period inventories; v12 source `5cfe4d64429f284232029341c6ba774e2eb6f727` supplies the fixed R3 cost-eight lower bound and the forced basic pair. The residual-mass simplification of Sections 3 and 6 was developed jointly with the observer_eight_frontier collaborator.
