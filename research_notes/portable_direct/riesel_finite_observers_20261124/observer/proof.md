# Complete cost-six observation and a fixed 31-channel finite-cost spectrum

Status: author mathematical derivation and exact finite arithmetic in the existing direct research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. This note makes no independent project Review or formal-admission claim.

## 1. Objects and dependency boundary

Retain the square Riesel family

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the old root

\[
a_*=690786768637635218740714348513373826260012289,
\]

and the twenty-prime dictionary

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

Its product is

\[
M=1397394912916194098609132326092145093313722687204526281.
\]

The old root class has \(a\equiv a_*\pmod{2M}\). Write \(\delta_P(a)\) for the minimum number of outside-P primes in a proper-prime cover of every term, and \(\tau(a^2)\) for the minimum total number of covering primes. If no finite cover exists, the corresponding value is infinity.

Set

\[
V=\{5,13,11,61,331\},\qquad W=\{19,37,73,109\},
\]

\[
L=\prod_{q\in V\cup W}q=80754838636615.
\]

The fixed 29-channel fiber from the preceding work is

\[
R_1=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L\}.
\tag{1}
\]

Its V residues are \((3,1,0,0,0)\), and its W residues, ordered as above, are \((6,0,37,0)\). Thus 3,11,61,331,37,109 divide the root and have no zero-readout channel.

The [companion complete-six theorem](../six/proof.md) proves the following exhaustive statement on R1: every supplement of at most six primes has exactly the six primes

\[
\{5,13,19,73,433,38737\},
\tag{2}
\]

and the two final primes have opposite binary phases on the remaining old holes. The prior sharp budget-five gap \(13/2520\) excludes smaller supplements. Consequently existence of one cover (2) is equivalent to \(\delta_P(a)=6\).

The exhaustive necessity of (2) is the new mathematical dependency of Sections 2–3. Those sections reuse the already checked eight CRT classes, minimum and native membership from commit `b1de1acbdc97b5e51d486127abd1fadd24babd99`, in `research_notes/portable_direct/riesel_five_cover_20261123/fiber/` and `native/`. They do not infer exhaustiveness from the finite classes or repeat the old native run.

## 2. The complete cost-six observer

The first four channels 5,13,19,73 leave the old holes on

\[
u=16+18w,\qquad n=2u,
\tag{3}
\]

where w satisfies a thirteen-position condition modulo 35. Put

\[
B=\{433,38737\},\qquad Z=433\cdot38737=16773121.
\]

Both primes have base-2 order 72. Their two admissible phase categories on (3) are:

| Prime | \(w\equiv0\pmod2\), equivalently \(u\equiv16\pmod{36}\) | \(w\equiv1\pmod2\), equivalently \(u\equiv34\pmod{36}\) |
|---:|---|---|
| 433 | \(a\equiv150,283\pmod{433}\) | \(a\equiv4,429\pmod{433}\) |
| 38737 | \(a\equiv2677,36060\pmod{38737}\) | \(a\equiv4,38733\pmod{38737}\) |

This table is obtained from \(a\equiv\pm2^{-c}\pmod q\). By the complete-six theorem, the exact predicate is

\[
\boxed{\delta_P(a)=6
\iff\text{both B coordinates occupy opposite displayed categories},
\qquad a\in R_1.}
\tag{4}
\]

There are two phase dictionaries and four independent root-sign choices for each. Thus there are exactly eight true classes modulo Z:

\[
\begin{split}
3215175,&\ 4263747,\ 5229491,\ 6278071,\\
10495050,&\ 11543630,\ 12509374,\ 13557946.
\end{split}
\tag{5}
\]

These are residues of a modulo Z; the fixed constraints (1) are imposed simultaneously by CRT. The progression step \(6ML\) of R1 is coprime to Z, so the exact relative natural density inside R1 is

\[
\boxed{\frac8{16773121}.}
\tag{6}
\]

Both prime coordinates are essential. For example, keeping the 38737 coordinate in category 0 and changing the 433 coordinate from inactive to category 1 changes the predicate; the reverse construction handles the other coordinate. Since Z is squarefree, a proper divisor of Z as an additive period would omit one essential coordinate, a contradiction. The least positive additive period in the R1 progression parameter is therefore exactly Z. The preceding certificate already records explicit true/false CRT witnesses for this argument, which are reused in the present certificate.

This establishes a minimal additive period for the named predicate. It does not claim an absolutely smallest arbitrary encoding of the entire integer state.

### 2.1 The prior minimum now covers all cost-six roots in R1

The previous eight-class calculation proved the least root among nested simultaneous optima through budget six. Equation (4) now shows that this is the entire cost-six class in R1. Therefore its previously computed minimum has the stronger interpretation

\[
\boxed{
\min\{a\in R_1:\delta_P(a)=6\}
=1597463687996365290740241630260436015028835427889255944107518938773290244463.
}
\tag{7}
\]

The root has 76 decimal digits. Its residues at (433,38737) are (429,2677). Its actual native membership and complete period-count row

\[
(432,216,78,52,26,13,0)/2520
\]

are already present in the preceding `native/native_certificate.json`, case `R1_least_nested_optimal_six_root`, and are reused without rerunning them.

The new assertion is the enlarged minimum scope, supplied by the exhaustive theorem. It is not a minimum over all Riesel coefficients or all roots in the original larger old class. This compact root has \(\tau(a^2)\le26\); equality of its total minimum to 26 is not asserted.

## 3. Five-budget optimality is substantially weaker than cost six

Let E5 mean that a root in R1 admits a five-prime dictionary attaining the sharp gap \(13/2520\). The previous equality theorem says exactly that at least one B coordinate occupies one of its displayed phase categories.

At prime q, each category contains two residues, while the remaining \(q-4\) residues contribute no zero on (3). Complete weighted counting of the nine category-label pairs gives:

| B-coordinate state | Root classes modulo Z | E5 | \(\delta_P=6\) |
|---|---:|---|---|
| Neither coordinate is in a displayed phase | 16,616,457 | false | false |
| Exactly one coordinate is in a displayed phase | 156,648 | true | false |
| Both coordinates occupy the same phase | 8 | true | false |
| Both coordinates occupy opposite phases | 8 | true | true |

For example, the first count is \((433-4)(38737-4)\), the second is \(4(433-4)+4(38737-4)\), and each of the last two is \(2\cdot2^2\). Their sum is Z.

Thus E5 holds in exactly 156664 classes, but 156656 of them do not admit a six-prime complete supplement. Conditional on E5, the relative density of cost-six roots is

\[
\boxed{\frac8{156664}=\frac1{19583}.}
\tag{8}
\]

Whenever (4) is false, the extra cost is at least seven, allowing infinity if no finite cover exists. A false predicate alone does not settle finite-cover existence. The next section constructs one explicit 31-channel subfiber lying in the E5-true, cost-six-false part, where every finite cost at least seven occurs.

## 4. A fixed 31-channel fiber

Define

\[
R_2=\{a\in R_1:a\equiv0\pmod{433},\quad
a\equiv38733\pmod{38737}\}.
\tag{9}
\]

The value 38733 is the positive inverse

\[
2^{-34}\equiv38733\pmod{38737}.
\]

The other sign 4 gives the same squared-root phase, but (9) is chosen to agree with the actual positive-inverse cost-seven and cost-eight roots already computed in earlier rounds.

Writing

\[
L_2=LZ=1354510679787418425415,
\]

the observer condition (9) is equivalently

\[
a\equiv602924359709868072943\pmod{L_2}.
\tag{10}
\]

Together with the old branch constraint, R2 is the positive progression with first root

\[
9807947978443488306255509703402695727949968778703073231931137913705883712843
\]

and step

\[
11356718000553566643685496313583434507970452519839503606327232707476034989690.
\]

All roots in R2 have the same complete residue-value trajectory in the 31 channels \(P\cup V\cup W\cup B\), at every index \(n\ge0\). E5 holds automatically because the 38737 coordinate has the displayed phase 1. Prime 433 is inactive, so (4) is false. Hence

\[
\delta_P(a)\ge7\qquad(a\in R_2).
\tag{11}
\]

### 4.1 A compact exact-cost-seven example

The previously certified distinct primes 577 and 487824887233 both have base-2 order 144. On the part missed by the active 38737 phase, their opposite phases are

\[
u\equiv16,52\pmod{72}.
\]

Using them together with 5,13,19,73,38737 gives a seven-prime supplement. One compact CRT root is

\[
142182133093029631521252488222753720130073171510309885943518183289197140261893115365205303.
\tag{12}
\]

It has 90 decimal digits, with residues 31 at 577 and 1048576 at 487824887233. The ordered rows are

\[
(q,c_q)=(5,1),(13,0),(19,4),(73,1),(38737,34),(577,16),(487824887233,52).
\]

Over the complete coverage period of 5040 exponent indices, the uncovered counts are

\[
(864,432,156,104,52,26,13,0).
\tag{13}
\]

The lower bound (11) and this cover prove \(\delta_P=7\). The calculation also checks that each assigned divisor is proper and supplies a private old-hole index for each selected channel. The immediate total-cost conclusion is only \(\tau(a^2)\le27\).

The root (12) is the least among the eight progressions formed by these two binary completions and their independent signs. This comparison has deliberately limited scope: it does not classify all seven-prime covers, does not prove a global cost-seven minimum, and does not assert that the intermediate counts in (13) are density-optimal. Other prime dictionaries can have better intermediate density reduction.

## 5. Every finite cost at least seven occurs in R2

**Theorem.** For every integer \(s\ge7\), there are infinitely many ordinary positive roots in R2 satisfying

\[
\boxed{\delta_P(a)=s,\qquad\tau(a^2)=20+s.}
\tag{14}
\]

The existing arbitrary-cost theorem at commit `af9e1a5e49386a28283781876e10742a71991036`, path `research_notes/portable_direct/riesel_spectrum_20261121/spectrum/proof.md`, supplies the private-cover refinement and coprimalization argument. A small explicit seed modification is needed to preserve the exact 38737 phase for all four cost residue classes. It would be incorrect to claim that the original unmodified family automatically lies in R2: its first five-child refinement from the cost-five seed uses the order-72 child at phase 16, whereas R2 fixes phase 34.

### 5.1 Four seeds of costs 7, 8, 9 and 10

All seeds retain these four rows, written as \((q,d,c)\) with d the even-index period:

\[
(5,2,1),(13,6,0),(19,9,4),(73,9,1).
\tag{15}
\]

The cost-seven and cost-eight seeds are unchanged from the earlier proof. Their other rows are

\[
\begin{array}{c|l}
7 &(38737,36,34),(577,72,16),(487824887233,72,52),\\
8 &(38737,36,34),(487824887233,72,52),
    (1153,144,16),(6337,144,88).
\end{array}
\tag{16}
\]

The explicit primality and exact-order proofs for these named primes are reused from the earlier seed certificate.

To obtain a suitable cost-nine seed, start from the cost-five parent's class \(u\equiv16\pmod{18}\), writing \(u=16+18v\). Translate the earlier private five-class cover by one, giving

\[
v\equiv1\pmod2,\quad v\equiv1\pmod3,\quad
v\equiv2\pmod4,\quad v\equiv0\pmod6,\quad
v\equiv8\pmod{12}.
\tag{17}
\]

This is a complete cover with respective private residues \(3,4,2,12,8\). A full period of length 12 verifies these facts. The child orders, periods and phases are

| Required base-2 order | Even-index period | Phase | Chosen prime |
|---:|---:|---:|---|
| 72 | 36 | 34 | 38737 |
| 108 | 54 | 34 | Any prime of exact order 108 |
| 144 | 72 | 52 | Any prime of exact order 144 |
| 216 | 108 | 16 | Any prime of exact order 216 |
| 432 | 216 | 160 | Any prime of exact order 432 |

The inherited primitive-prime theorem supplies the four order-labelled primes; the orders are distinct, so these primes are distinct. None of these orders belongs to an old prime, and the required order-72 prime has explicitly been chosen to be 38737 rather than 433. The cost increases from five to nine, and the desired phase 34 is retained.

For cost ten, start from the cost-six seed. Keep its \((38737,36,34)\) row, and replace its \((433,36,16)\) row by the original five-class cover

\[
(m,b)=(2,0),(3,0),(4,1),(6,5),(12,7).
\tag{18}
\]

Its new even-index periods and phases are

\[
(72,16),(108,16),(144,52),(216,196),(432,268),
\]

with distinct requested base-2 orders 144,216,288,432,864. Again the inherited primitive-prime theorem applies, all primes are fresh, and the cost becomes ten. Prime 433 has been removed, while 38737 remains at phase 34.

The common hole period of each seed equals 35 times its largest even-index period. The new finite calculation checks the full hole periods and a private old-hole witness for every row in all four seeds. The old twenty private odd witnesses remain valid because the only odd-order extra prime is the unchanged 73, and all those witnesses avoid its exponent phase \(n\equiv2\pmod9\).

### 5.2 Every larger cost and preservation of the fixed coordinates

Every integer \(s\ge7\) can be written uniquely as

\[
s=b+4h,\qquad b\in\{7,8,9,10\},\quad h\ge0.
\]

From the corresponding seed, repeatedly refine a largest-period row by (18). If the parent period is d, the requested child base-2 orders are \(2dm\), for \(m=2,3,4,6,12\). Each replacement adds four channels and multiplies the largest period by twelve.

The largest seed periods are 72,144,216,432, all strictly above 36. Therefore the retained 38737 row is never selected for a largest-period refinement. Every later child order is at least 288, so 433, of order 72, never reappears. Primes 37 and 109, both of order 36, also never appear. The U-prime orders 10,60,30 are absent as well.

The private-witness proof from the earlier theorem applies unchanged. On a parent private fiber, the new coordinate varies by steps of 35, which is invertible modulo 12, so each child has a private old-hole witness. Unaffected rows retain theirs. All new orders are distinct and exceed the current largest order; the primitive-prime theorem therefore supplies fresh primes at every depth. Their orders do not divide 210, preserving the earlier forcing condition's compatibility.

### 5.3 Exact costs and the automatic 31-channel congruence

Let \(S=P\sqcup Q\) be a constructed cover, and use its twenty old private odd indices and s new private even indices. The old list includes

\[
5,41;\qquad3,63;\qquad41,113,
\]

with differences 36,60,72. Form the usual coprimalization quantities

\[
D=\operatorname{lcm}_{i<j}(2^{|n_i-n_j|}-1),\qquad
E=D\Big/\prod_{q\in S}q^{v_q(D)}.
\]

Impose \(E\mid a\), along with the old root residues, the positive inverse root residues for every new channel, and the previous forcing condition \(T_{3,1}\mid a\). These CRT constraints are compatible by the earlier theorem.

Because 37,109,11,61,331,433 are absent from S, the displayed old-index differences force

\[
37\cdot109\cdot11\cdot61\cdot331\cdot433\mid E\mid a.
\]

The four permanent new rows give the residues 3,1,6,37 at 5,13,19,73. The retained 38737 row gives residue 38733. The forcing condition gives \(3\mid a\). These are exactly the R2 conditions (1), (9), with no additional inconsistent constraint.

If a prime divided two private terms, it would divide D. An S-prime is ruled out by privacy; any other prime divides E and hence a, forcing every \(F_n(a)\equiv-1\) modulo it. Thus all \(20+s\) private terms are pairwise coprime. Every full cover needs at least \(20+s\) distinct primes, and the displayed dictionary attains that bound. The s new private terms avoid all of P, giving the exact additional minimum s as well.

The compatible CRT progression gives infinitely many positive roots. All sufficiently large representatives have every assigned prime as a proper divisor. This proves (14).

The conclusion has quantifiers \(\forall s\ge7\,\exists^\infty a\in R_2\). It does not produce a single ordinary root of infinite cost. It proves that the finite spectrum in this one 31-channel fiber is exactly the integers at least seven, while possible infinite cost remains a separate question.

## 6. Exact calculation and reused evidence

Run

```sh
python verify_observer.py
```

The standard-library calculator checks the nine exact B-category states and their cardinalities, the conditional density in (8), the true CRT classes against the previous certificate, the combined R2 residue and progression, the translated five-class cover, complete old-hole coverage and private witnesses for the four modified seeds, and the compact seven-prime example over its full period.

It also newly checks the R2 membership of the existing large roots. The earlier cost-six root has B residues (150,38733), so it is outside R2. The already certified cost-seven and cost-eight roots both have (0,38733), hence lie in R2. Their existing exact costs, pairwise-gcd checks and native evidence are reused rather than rerun. The new certificate records the root hashes and the precise congruence-only scope of this new check.

The global cost-six minimum calculation and native membership are reused from the previous eight-class certificate. The strengthened minimum scope comes from the companion exhaustive theorem. The compact example (12) is checked arithmetically here; actual native execution, if performed by the parent integration, is a separate recorded operation.

The native scalar dynamics, fixed X6 anchor and positive singleton weight and multiplicity remain unchanged. These prime residues are observation coordinates of the integer state. Agreement in all 31 coordinates for every future index does not identify the full integer or its joint cofactor relations. The new fiber supplies exact finite-cost differences under that same observation.
