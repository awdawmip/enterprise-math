# All two-prime completions after the fixed seven-prime prefix in R3

Research continuation, 2026-11-24 (Asia/Hong_Kong). Researcher
`EM-DIRECT-970E1C`, continuing Activity `RA-D2EC212845B63844081F9A14`.
This file contains an author derivation,
shared-context mathematical assistance, and exact computation. Independent
project Review, Foundation promotion, and formal proof acceptance are not
claimed.

## 1. Scope and result

Retain the native integer trajectory at the fixed Heartbeat X6 anchor,

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1\quad(n\ge1).
\]

The positive singleton BRC has weight and multiplicity one. Root residues,
exponent classes, and periodic coverage are observations of this integer
state. They do not replace its type or its common-divisor relationships.

Let P be the old twenty-prime dictionary. The supplementary cover cost is
\(\delta_P(a)\), and the unrestricted total cover cost is \(\tau(a^2)\).
Use the same fixed 43-prime trajectory R3 as v12 and v13:

\[
R_3=\{A_3+S_3j:j\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

Define the fixed seven-prime supplementary prefix

\[
Q_7=\{5,13,19,73,38737,246241,487824887233\}.
\]

All roots in R3 have the same phases at these seven primes. A cover counted
below explicitly contains every member of Q7 and adds two distinct primes
outside \(P\cup Q_7\).

> **Theorem 1: complete two-tail classification.** There are exactly fifty
> phase dictionaries for such a cover, comprising two types:
>
> 1. Two distinct primes from
>    \[
>    \mathcal B=\{193,1153,6337,22253377,38941695937,278452876033\}
>    \]
>    occupy opposite t-parities. This gives thirty phase dictionaries and
>    120 signed CRT descriptions.
> 2. Two distinct primes from
>    \[
>    \mathcal E=\{33975937,209924353,4261383649,
>                    138991501037953,24929060818265360451708193\}
>    \]
>    occupy t-phases zero and two modulo three. This gives twenty phase
>    dictionaries and eighty signed CRT descriptions.
>
> Here \(w=4t\), the relation to the original exponent is
> \(n=32+36w\), and each sign means one of the two square-root residues
> giving the stated zero phase. There are no further primes or period
> types, regardless of prime size.

The first type always has supplementary cost eight, because 246241 can be
omitted. In the second type, assigning both order-216 primes also always
gives cost eight, because 487824887233 can be omitted. The remaining
eighteen phase dictionaries have 72 signed CRT descriptions. All 72 first
positive CRT representatives have exact cost nine; the full progression of
one description may also contain roots with incidental cost-eight covers.

> **Theorem 2: minimum inside this complete conditional family.** Among
> all roots in R3 with exact supplementary cost nine that admit a cover
> containing Q7, the smallest is
>
> ```text
> 112755110470612891256156246069109596727720684467884590849485136661471023397130974501713495184000901218767521913670185762743636668514043005915407753161112053
> ```
>
> It has 156 decimal digits and equals
> \(A_3+282899156086651S_3\). Its extra two primes are 33975937 and
> 4261383649, with respective w-phases zero modulo six and eight modulo
> twelve. The theorem concerns this complete conditional family; it does
> not assert the minimum over all cost-nine roots in R3.

The lower cost bound in Theorem 2 uses the **complete** v13 budget-eight
observer, including the branch omitting both 19 and 73. It is not based on
assuming the four-prime prefix remains forced at budget nine.

## 2. Prior inputs and the exact residual set

The prior inputs are the v12 definition of R3 and exclusion of costs at
most seven (`observer_frontier/proof.md`), the v13 hole calculation and
four-tail classification (`eight_tail_v13/proof.md`), and the full v13
eight-budget theorem and observer (`eight_prefix_v13/proof.md` and
`eight_observer_v13/proof.md`). The new checker reproduces the relevant
root data and observer predicate without importing those scripts.

After P and \(Q_0=\{5,13,19,73\}\), every uncovered exponent has

\[
n=32+36w,\qquad
w\bmod35\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}.
\tag{1}
\]

The three fixed extra tails have phases

| Prime | Effective w-period | Zero phase |
|---:|---:|---:|
| 38737 | 2 | 1 |
| 246241 | 3 | 1 |
| 487824887233 | 4 | 2 |

Consequently, after Q7 the remaining points have

\[
w\equiv0,8\pmod{12}.
\]

They can be written \(w=4t\), where

\[
t\equiv0,2\pmod3,\qquad
t\bmod35\in B_4=\{0,2,7,10,14,17,20,24,25,27,30,32,34\}.
\tag{2}
\]

The set C of residues modulo 105 in (2) has 26 elements. It is exactly

```text
0,2,14,17,20,24,27,30,32,35,42,45,59,60,62,65,69,72,77,80,84,87,90,95,102,104.
```

## 3. An all-prime capacity bound

For any odd prime q that hits this residual set, the zero set on t is one
class modulo

\[
e_q=\operatorname{ord}_q(2^{144}).
\]

Indeed \(F_{32+144t}(a)\equiv0\pmod q\) is equivalent to
\(a^2 2^{32}(2^{144})^t\equiv1\pmod q\). A prime dividing a has no hits;
the prime two has none either.

Let \(g=\gcd(e_q,105)\), and let K be the number of elements of C
compatible modulo g with the selected q-class. By the Chinese remainder
theorem, the proportion of C covered by that one class is

\[
\frac{K}{26(e_q/g)}.
\tag{3}
\]

This is an exact density calculation over a common period. The maxima of K
are:

| g | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Maximum compatible C residues | 26 | 13 | 10 | 6 | 5 | 3 | 2 | 1 |

The complete factorization of \(2^{144}-1\), checked inside the complete
\(2^{288}-1\) inventory, is

\[
\begin{aligned}
2^{144}-1={}&3^3\cdot5\cdot7\cdot13\cdot17\cdot19\cdot37\cdot73
\cdot97\cdot109\cdot241\cdot257\cdot433\\
&\cdot577\cdot673\cdot38737\cdot487824887233.
\end{aligned}
\]

Every one of these primes is in P, already in Q7, or inactive in R3.
In particular 3 divides the root a, and the other inactive coordinates
have root residue zero. Thus a new prime hitting C cannot have e=1.

For g=1, equation (3) is at most \(1/e_q\le1/2\), with equality only
when e=2. For g=3, it is at most \(1/(2(e_q/3))\), with equality only
when e=3. Every other column has K strictly below 13, so its capacity is
strictly below one half. We have proved, uniformly over all primes:

\[
\text{one new prime covers at most half of C, with equality only for
effective period 2 or 3.}
\tag{4}
\]

Two channels covering all of C must both attain equality and have disjoint
hits on C. Two period-two channels must occupy opposite parities; two
period-three channels must occupy phases zero and two. A period-two class
and a period-three equality class meet in exactly one quarter of C:
parity is independent of the odd modulus 105. Their union therefore has
relative density three quarters. This excludes the mixed case and proves
the complete period reduction in Theorem 1.

No upper bound on prime size, and no finite experimental prime search,
enters this reduction.

## 4. Complete prime inventories and deterministic certificates

If \(\operatorname{ord}_q(2^{144})=2\), then q divides
\(2^{288}-1\); if that order equals three, q divides
\(2^{432}-1\). The checker verifies full factorizations of these two
integers and primality of every displayed factor. Filtering by exact
effective order gives:

| Effective t-order | Complete prime inventory |
|---:|---|
| 2 | 193, 1153, 6337, 65537, 22253377, 38941695937, 278452876033 |
| 3 | 87211, 246241, 262657, 279073, 33975937, 209924353, 4261383649, 138991501037953, 24929060818265360451708193 |

The period-two inventory loses 65537, which is in P. The period-three
inventory loses the already selected 246241 and the three inactive
coordinates 87211, 262657, 279073. The remaining effective-period-two
primes are exactly \(\mathcal B\), and the period-three primes exactly
\(\mathcal E\).

Their base-two orders are:

| Primes | \(\operatorname{ord}_q2\) | Effective w-period |
|---|---:|---:|
| 193, 22253377 | 96 | 8 |
| 1153, 6337, 38941695937, 278452876033 | 288 | 8 |
| 33975937, 138991501037953 | 216 | 6 |
| 209924353, 4261383649, 24929060818265360451708193 | 432 | 12 |

The new factor identity is

\[
\begin{aligned}
\Phi_{432}(2)
&=2^{144}-2^{72}+1\\
&=22300745198530623141530995906165491860766721\\
&=209924353\cdot4261383649\cdot24929060818265360451708193.
\end{aligned}
\tag{5}
\]

The full 432 inventory is reconstructed using

\[
2^{432}-1=(2^{216}-1)(2^{72}+1)\Phi_{432}(2),
\]

where

\[
2^{72}+1=97\cdot257\cdot577\cdot673\cdot487824887233.
\]

The largest new prime is certified recursively by complete n−1
factorizations. The certificate includes these rows:

| n | Factorization of n−1 | Witness |
|---:|---|---:|
| 209924353 | \(2^8 3^3 11^2 251\) | 10 |
| 4261383649 | \(2^5 3^3 71\cdot69467\) | 7 |
| 24929060818265360451708193 | \(2^5 3^4\cdot9617693216923364371801\) | 15 |
| 9617693216923364371801 | \(2^3 3\cdot5^2\cdot6959\cdot2303418407080367\) | 11 |
| 2303418407080367 | \(2\cdot1151709203540183\) | 5 |
| 1151709203540183 | \(2\cdot7\cdot17\cdot907481\cdot5332469\) | 5 |

All leaves are proved prime by trial division. For each row with witness z,
the verifier checks \(z^{n-1}\equiv1\pmod n\) and

\[
\gcd(z^{(n-1)/p}-1,n)=1
\quad\text{for every prime }p\mid n-1.
\]

For any prime divisor of n, these conditions force the order of z to be
n−1, so that prime divisor is at least n. Therefore n is prime. This
explains why the checks are deterministic proofs rather than probable-prime
tests. Exact base-two orders are checked by the full divisor criterion;
for order 432 the proper exponent checks are 216 and 144.

## 5. Phases, counts, and signed CRT descriptions

A prime q having zero phase w=b imposes precisely the two root residues

\[
a\equiv\pm2^{-(16+18b)}\pmod q.
\tag{6}
\]

For the binary type, use b=0 and b=4. For the ternary type, use b=0 and b=8.
At an order-216 prime, b=8 is of course the same phase as b=2 modulo six;
at an order-432 prime it is the phase eight modulo twelve. Equation (6)
works in both cases without changing coordinates.

The two phase slots are distinguished, and each prime occupies exactly one
slot. Hence the binary type has \(6\cdot5=30\) assignments, the ternary
type \(5\cdot4=20\), and each assignment has four independent sign
choices. All selected primes are coprime to S3. CRT gives a nonempty
positive progression for every choice. The 200 descriptions are retained
as descriptions, not asserted to be pairwise disjoint root sets.

For every root in one of these progressions, the displayed primes cover
all n≥1. They are proper divisors: already at n=1,
\(2A_3^2-1\) exceeds every prime used, and all subsequent terms are
larger. No finite execution extrapolation is needed for coverage.

The binary dictionaries already cover all positions without 246241. The
ternary dictionary using both order-216 primes covers everything without
487824887233. The previously proved R3 lower bound \(\delta_P\ge8\)
makes the cost exactly eight in those 128 signed descriptions. None of
those descriptions can contain a cost-nine root.

The other 72 signed descriptions contain at least one order-432 prime.
They provide covers of size nine. They do not alone prove that the root's
minimum cost is nine: a root may satisfy other eight-cover residue
conditions. The checker therefore evaluates the complete v13 predicate at
each first positive CRT representative. All 72 evaluations are false,
so all these first representatives have exact cost nine.

## 6. The conditional minimum in R3

Each signed description yields a least positive root r and modulus m, and
all its positive roots are \(r+km\) with k≥0. The smallest r among the 72
nonstructurally-eight descriptions is the 156-digit root in Theorem 2.
Its exact extra congruences are

\[
a\equiv6170892\pmod{33975937},\qquad
a\equiv46284028\pmod{4261383649}.
\]

The first is \(+2^{-16}\) and the second \(+2^{-160}\). Together with
\(a\equiv A_3\pmod{S_3}\), they give

```text
modulus = 57706755959915970634486211006880297375733908140224159179263692531382253057599283112319319657201299932695611162684208940579360612432141785929354402096474171070
```

For this root, every prefix branch of the complete budget-eight predicate
is false: the binary, order-216-pair, and modulo-five tests all fail. In
the branch omitting both 19 and 73, only one of the four mandatory primes
\(\{29,43,1429,5419\}\) has a permissible phase (29 has v-phase four).
The other three do not. That branch also fails.

Thus the candidate has \(\delta_P=9\). Any smaller positive root
admitting a Q7-containing nine-prime dictionary would have to lie in one
of the same 72 progressions, whose first roots have all been compared, or
in a structurally-eight progression. Both possibilities are excluded.
This proves the exact minimum over the stated class, including future
roots of every progression.

The two-tail argument alone gives \(\tau(a^2)\le29\). The companion
v14 result `exact_total_v14/proof.md` supplies 29 full integer terms of
this same compact root that are pairwise coprime, with greatest index 2048.
Its 406 pairwise gcds are one. Any covering prime can divide at most one
of those terms, so that separate certificate proves the stronger equality
\(\tau(a^2)=29\), as well as an independent lower bound
\(\delta_P(a)\ge9\). Its lower-bound mechanism is separate from the
complete-observer comparison used above for the 72 CRT starts.

## 7. The observer-zero subfiber R4

Let \(T_8\) be the product of the 31 necessary free prime coordinates of
the complete v13 eight-budget observer, and define

\[
R_4=\{a\in R_3:a\equiv0\pmod{T_8}\}.
\]

Its positive CRT progression is computed in the certificate as A4 modulo
S4. The complete observer is false identically on R4, so
\(\delta_P(a)\ge9\) there.

All six binary candidates and both order-216 candidates are coordinates
of this observer and are inactive on R4. Theorem 1 consequently specializes
to the following complete statement:

> Among covers containing Q7, the two added primes on R4 must be two
> distinct members of
> \(\{209924353,4261383649,24929060818265360451708193\}\), one at
> w=0 and the other at w=8 modulo twelve. These are exactly six phase
> dictionaries and 24 signed CRT descriptions. Every root they describe
> has exact supplementary cost nine.

The least positive root in this entire conditional class is

```text
41827204235278113102728963989385111219996616875810967006685409379631973239368404676825708932524338584566302489346933611334268092964973257823581835136481095570798758906669004270819218885649203203304534183167368156237584516628895469357035618923674786027207678768467525149076136384266734275127645336612154683885541594283259752136216244695264672084525880943271789328244084723
```

It has 371 digits, with

\[
a\equiv2295006346\pmod{4261383649}\quad(w=0),
\qquad
a\equiv37380361\pmod{209924353}\quad(w=8).
\]

This is the minimum for the Q7-containing class in R4, without a claim
about other cost-nine cover structures in R4. The code verifies all 24
signed minima, including those involving the largest order-432 prime.

## 8. Exact frequency of the conditional cost-nine class

All frequencies in this section are natural relative densities among the
positive roots of the stated arithmetic progression. They count roots,
not signed descriptions; overlapping descriptions are counted only once.

Let K mean that both required t-colors are present among the five primes
of \(\mathcal E\). Let D mean that the two old order-216 primes alone
have both colors. Let B, C, and Z mean respectively the v13 binary,
modulo-five, and zero-W cost-eight alternatives. The exact event for a
cost-nine root admitting a Q7-containing cover is

\[
(K\setminus D)\cap B^c\cap C^c\cap Z^c.
\tag{7}
\]

In particular, the 72 nonstructurally-eight CRT progressions must have all
their incidental cost-eight points removed to obtain the exact cost-nine
set. Their first representatives happen to require no removal, but that
finite fact is not used as a statement about their full progressions.

For a prime set S with k disjoint required colors, each occupying exactly
two root residues per coordinate, the number of residue assignments with
every color present is

\[
C_k(S)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}\prod_{q\in S}(q-2j).
\tag{8}
\]

Its density is \(C_k(S)/\prod_{q\in S}q\). Here

\[
\rho_K=\frac{C_2(\mathcal E)}{\prod_{q\in\mathcal E}q},\qquad
\rho_D=\frac8{33975937\cdot138991501037953}.
\]

The K and D coordinates are disjoint from all B, C, and Z coordinates;
these latter three groups are also pairwise disjoint. All these free
moduli are coprime to S3. CRT therefore makes their residue distributions
independent on R3. Since D is a subset of K, (7) gives the exact formula

\[
\boxed{\rho_{9,Q_7}^{R_3}=(\rho_K-\rho_D)(1-\rho_B)(1-\rho_C)(1-\rho_Z).}
\tag{9}
\]

The checker recomputes all factors by inclusion-exclusion. For Z it uses
the complete v13 split: a specified missing mod-seven class has 384
root-sign assignments at the four period-seven primes; five such classes
permit the period-14 completion, and two additionally permit the
period-35 completion. Thus, writing \(p_{14}\) and \(p_{35}\) for the
corresponding two-color densities,

\[
\rho_Z=\frac{384}{29\cdot43\cdot1429\cdot5419}
\bigl(5p_{14}+2(1-p_{14})p_{35}\bigr).
\]

The exact reduced numerator and denominator in (9) are:

```text
numerator = 1271839397512734869888736370843042411314181724342668665255971030225088191213150802715054516703334641422287915289020565175397409319656804995097675652584740705501798816357645293791546344212280059090563771317546769754030876082996112271020544360
denominator = 1072565521901500379198406676943629042890674188689712212827573693028012640460212954792475180834386822786796077432875381953451340062037148173687797942811833119968950448910575862157820150760051778610197426415041796272480358308963617387853024689968052622697093
```

Numerically,

\[
\rho_{9,Q_7}^{R_3}
=1.18579179690388641099113117471811134137766291606165\ldots\times10^{-15}.
\]

On R4 the eight-budget alternatives are identically false, and only the
three order-432 coordinates remain. The conditional family's relative
density in R4 is therefore

\[
\boxed{\rho_{9,Q_7}^{R_4}
=\frac{199432486546122919384129512}
{22300745198530623141530995906165491860766721}}
=8.94286198827397722288587021648160\ldots\times10^{-18}.
\tag{10}
\]

Neither (9) nor (10) is claimed to count every cost-nine root in its
ambient fiber. Both count exactly the complete Q7-containing family.

## 9. Reproduction and limits

Run with a standard Python 3 interpreter:

```bash
python nine_tail_v14/verify_two_tail.py
```

`two_tail_certificate.json` contains both complete factorizations, every
primality certificate and exact order, all fifty reduced-period covering
dictionaries, all 200 signed CRT representatives, the complete eight-budget
predicate values needed for the minima, and the R4 specialization. The
script performs no network access and requires no third-party packages.

This closes the full two-prime problem after the fixed seven-prime prefix.
It does not classify every five-tail cover after Q0, every nine-prime
supplement in R3, or every cost-nine root in R4. Those broader statements
would require additional forcing arguments and case classifications.
