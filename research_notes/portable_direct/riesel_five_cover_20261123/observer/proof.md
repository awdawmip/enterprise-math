# Complete cost-five residue observer and the least positive root

Status: author mathematical derivation and exact finite calculation in the existing direct research activity. Researcher `EM-DIRECT-970E1C`; Activity `RA-D2EC212845B63844081F9A14`. No independent project Review or formal admission is asserted.

## 1. Result and source scope

Keep the root family and old dictionary from the preceding work:

\[
F_n(a)=a^2 2^n-1,\qquad
a_*=690786768637635218740714348513373826260012289,
\]

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,
1321,14449,29191,65537,6700417\},
\]

\[
M=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281.
\]

Write \(\delta_P(a)\) for the minimum number of primes outside P in a proper-prime cover of every positive-index term. The Riesel coefficient is \(a^2\). The branch considered first is

\[
\mathcal B=\{a_*+6Mj:j\ge0\}.
\tag{1}
\]

It is exactly the positive old root class with \(3\mid a\). The other two thirds of the old root class have \(\delta_P=1\), so every cost-five root belongs to (1).

The companion [global five-channel proof](../global/proof.md) establishes the exhaustive all-prime classification used here: every five-prime supplement has the two primes 5 and 13 with opposite u-parities; the 13 phase has mod-3 residue 0 or 1; and the remaining three primes form exactly one of the two types described below. Its necessity proof has no prime-size cutoff. The previous four-channel gap theorem gives \(\delta_P\ge5\) throughout (1), so the existence of one such supplement is equivalent to \(\delta_P=5\).

The inherited hole set, four-channel gap and earlier nested minimum are reused from commit `a2ae4d93398425e67dacbb4c99b7f3a6755e5771` of `awdawmip/enterprise-math`, under `research_notes/portable_direct/riesel_observers_20261122/`: `staircase/proof.md` and `observer/proof.md`. Their assumptions are retained here.

Set

\[
U=\{11,61,331\},\qquad W=\{19,37,73,109\},
\]

\[
K=65\prod U=14436565,
\qquad
\boxed{L=65\prod U\prod W=80754838636615.}
\tag{2}
\]

**Theorem.** In \(\mathcal B\), the predicate \(\delta_P(a)=5\) is determined by \(a\bmod L\). Exactly

\[
\boxed{40693468800}
\tag{3}
\]

root residue classes modulo L satisfy it. Its relative natural density is

\[
\boxed{
\frac{40693468800}{80754838636615}
=\frac{8138693760}{16150967727323}.
}
\tag{4}
\]

Within the entire old root class, the relative density is one third of (4), namely

\[
\frac{2712897920}{16150967727323}.
\tag{5}
\]

The least positive additive period of this Boolean predicate in the parameter j is exactly L. Its least positive root in the entire old class is

\[
\boxed{
a_{\min,5}=39741911323337250951212360989279347168190786597922987443929.
}
\tag{6}
\]

This is the same 59-digit number previously proved least only in the nested-optimal subclass. The all-prime classification now extends its minimum property to **every** root with \(\delta_P=5\) in the fixed old class. It is not a minimum over all Riesel numbers or all square Riesel coefficients. The total cover size at this root is bounded above by 25; equality of the total minimum to 25 is not asserted.

## 2. Full phase dictionary

Let \(n=2u\), and let \(\varepsilon\in\{0,1\}\) denote the u-parity missed by 5 and hit by 13. Write \(r\in\{0,1\}\) for the mod-3 residue of the 13 phase. The basic phases are

\[
c_5=1-\varepsilon\pmod2,
\qquad
c_{13}\equiv\varepsilon\pmod2,\quad c_{13}\equiv r\pmod3.
\tag{7}
\]

The remaining holes lie on

\[
u=u_0+6v,
\qquad
u_0\equiv\varepsilon\pmod2,\quad u_0\equiv1-r\pmod3,
\quad0\le u_0<6.
\tag{8}
\]

The four cases are:

| \(\varepsilon\) | \(r\) | \(c_5\) | \(c_{13}\) | \(u_0\) | Remaining holes modulo 35 in v |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 0 | 4 | 13 |
| 1 | 0 | 0 | 3 | 1 | 13 |
| 0 | 1 | 1 | 4 | 0 | 23 |
| 1 | 1 | 0 | 1 | 3 | 23 |

For a prime q and an even-subsequence phase c, the root constraint is precisely

\[
\boxed{a\equiv\pm2^{-c}\pmod q.}
\tag{9}
\]

The two signs are distinct and have the same squared-root trajectory at q. Distinct phases modulo \(\operatorname{ord}_q4\) have disjoint root-residue pairs.

### Type I: the modulo 5 completion

This type occurs only when \(r=0\). Use all three primes in U and assign them bijectively to categories \(0,1,4\), the value of \(u\bmod5\) on the remaining fiber. For a prime assigned category b:

\[
\begin{array}{ll}
q=11:&c_q\equiv b\pmod5,\\
q=331:&c_q\equiv1\pmod3,\quad c_q\equiv b\pmod5,\\
q=61:&c_q\equiv\varepsilon\pmod2,\quad c_q\equiv1\pmod3,
\quad c_q\equiv b\pmod5.
\end{array}
\tag{10}
\]

The 13 residual positions have category sizes 5, 5, 3, so this is exactly the preceding nested-optimal family. There are \(2\cdot3!=12\) phase dictionaries.

### Type II: the modulo 3 completion

This type occurs for either \(r=0\) or \(r=1\). Choose three distinct primes from W and assign them bijectively to the relative categories \(v\bmod3=0,1,2\). Their even orders are

\[
d_{19}=d_{73}=9,
\qquad d_{37}=d_{109}=18.
\]

If q is assigned relative category b, its phase is

\[
\boxed{c_q\equiv u_0+6b\pmod{d_q}.}
\tag{11}
\]

All four primes have effective order \(\operatorname{ord}_q(2^{12})=3\) on the fiber (8). Three different relative phases cover every v, hence every residual hole. For each r there are

\[
2\binom43 3!=48
\]

phase dictionaries. Combined with Type I, the complete count is

\[
\boxed{12+48+48=108.}
\tag{12}
\]

These count unordered prime dictionaries with their assigned phases. They do not count all orders of adding their primes, and they do not count disjoint root classes modulo L.

## 3. Supporting residual-fiber proof

This section gives the complete conditional classification once the basic pair (7) is fixed; the companion global proof handles the necessity of that pair.

The old u-hole set H has period 105 and 36 elements. Its mod-3 classes have sizes 23, 13, 0. Within the size 13 class, the mod-5 counts are \((5,5,0,0,3)\), and the largest mod-7 count is 3. Within the size 23 class the maximum mod-5 count is 6 and the maximum mod-7 count is 4. These unchanged exact incidences are from the preceding staircase proof.

For a residual set of size h modulo 35, a class of effective period f has relative density

\[
\frac{K_g(c)}{h(f/g)},\qquad g=\gcd(f,35).
\tag{13}
\]

For eligible primes outside \(P\cup\{3,5,13\}\), effective periods 1 and 2 are impossible, by the complete factorization of \(2^{24}-1\).

### The thirteen-position fiber

Every remaining prime covers at most 5/13 of this fiber. If three primes cover it completely, each must contribute at least 3/13: the other two cover at most 10/13. Applying (13) for gcds 1, 5, 7, 35 therefore forces

\[
f\in\{3,4,5,7\}.
\tag{14}
\]

For example, at gcd 1 the density is at most 1/f, so f is 3 or 4; at gcd 5 it is at most \(5/(13(f/5))\), forcing f=5; at gcd 7 it is at most \(3/(13(f/7))\), forcing f=7; gcd 35 cannot reach 3/13.

Complete factorizations of \(2^{12f}-1\), followed by the exact-order and old-prime exclusions, give:

| Effective order f | Eligible primes |
|---:|---|
| 3 | 19,37,73,109 |
| 4 | none |
| 5 | 11,61,331 |
| 7 | 29,43,1429,5419 |

These factorizations are entirely checked by trial division in the companion calculation. No unresolved factor is discarded.

If at least one but fewer than three channels have order 3, some v-class modulo 3 is missed by all of them. Because 3 is coprime to 35, on that class the remaining order 5/7 channels would have to cover the entire 13-position set modulo 35. There are at most two such channels, and even two order 5 classes cover at most 10/13, a contradiction.

If all three channels have order 3, their three relative phases must be distinct, and this is exactly Type II.

If no channel has order 3, their orders lie in \(\{5,7\}\). At most one order 5 channel gives total coverage at most \((5+3+3)/13<1\). Two order 5 channels plus one order 7 channel can reach density 1 only if they attain the disjoint counts 5, 5, 3. The two order 5 channels must cover u-categories 0 and 1, leaving precisely

\[
u\equiv49,64,79\pmod{105}.
\]

Their residues modulo 7 are distinct. Fixing parity and passing to v is an invertible affine map modulo 7, so one order 7 class cannot cover all three. This case is impossible. Three order 5 channels must therefore be the three distinct primes of U, with categories 0, 1, 4: Type I.

### The twenty-three-position fiber

The density bound in this fiber is 1/3. Equality requires gcd 1 and effective period 3, since the other gcd columns have bounds 6/23, 4/23, 1/23, all strictly smaller. Three channels can cover only if each attains 1/3. They must therefore be three distinct W-primes with distinct relative phases. This is Type II, now with \(r=1\).

## 4. Root counts and overlaps

The affine map

\[
j\longmapsto a_*+6Mj\pmod L
\]

permutes all residues modulo L because \(\gcd(6M,L)=1\). Counting root tuples therefore gives relative density in (1).

Write

\[
U_0=\prod U=222101,
\qquad W_0=\prod W=5593771.
\]

For each fixed r, the basic pair has two parity choices and two signs at each of 5 and 13: eight root tuples modulo 65. The tuples for r=0 and r=1 are disjoint. For each prime in U or W, each specified category contains exactly two root residues, by (9).

There are

\[
3!\,2^3=48
\tag{15}
\]

U-tuples supporting Type I. For the W-tuples, Type II means that each of the three relative categories occurs at least once among four prime coordinates. Inclusion-exclusion gives

\[
\begin{split}
B
&=\prod_{q\in W}q
-3\prod_{q\in W}(q-2)
+3\prod_{q\in W}(q-4)
-\prod_{q\in W}(q-6)\\
&=10848.
\end{split}
\tag{16}
\]

At r=0, Types I and II may both hold at one root. Their union contains

\[
8(48W_0+U_0B-48B)=21418655616
\tag{17}
\]

classes modulo L. At r=1, only Type II is available, giving

\[
8U_0B=19274813184
\tag{18}
\]

classes. Summing the disjoint r-branches proves

\[
\begin{aligned}
8\bigl(48W_0+(2U_0-48)B\bigr)
&=8[48\cdot5593771+(2\cdot222101-48)\cdot10848]\\
&=40693468800.
\end{aligned}
\]

and hence (3)–(5).

The overlaps can also be completely counted. Exactly 10272 W-tuples support one Type II dictionary, and 576 support two; a tuple cannot support more because there are only four primes for three required categories. The first number is

\[
3!2^3\sum_{q\in W}(q-6)=10272,
\]

corresponding to three active categories and one outside coordinate. The second is

\[
3\binom42 2!2^4=576,
\]

corresponding to four active coordinates with one duplicated category. Combining this with the possible Type I dictionary gives:

| Number of complete five-prime dictionaries at a root | Root classes modulo L |
|---:|---:|
| 1 | 38,642,641,536 |
| 2 | 2,050,606,080 |
| 3 | 221,184 |

Their sum is (3). Thus simply adding 108 individual dictionary sizes would overcount some roots.

## 5. Exact least additive period

Sufficiency of a modulo L follows from the complete phase formulas. Every prime coordinate in L is essential to the Boolean cost-five predicate:

* Changing either the 5 or 13 coordinate of a satisfying Type I tuple to 0 destroys the required basic pair.
* For any U-coordinate, put the U-primes in the three Type I categories and put all W-coordinates at 0. Changing that U-coordinate to 0 changes the predicate from true to false.
* For any W-coordinate, put all U-coordinates at 0 and put that W-coordinate and two others in distinct relative categories, leaving the fourth at 0. Changing the chosen coordinate to 0 destroys Type II.

All these tuples are realized by CRT. The certificate records explicit true/false residues and corresponding j-residues for each of the nine essential primes.

If m were another positive additive period, then \(\gcd(L,m)\) would also be a period. A proper divisor of the squarefree L omits some prime coordinate; its translation subgroup includes changing that coordinate alone while keeping all others fixed. This contradicts essentiality. Hence L divides every period. Since multiplication by 6M is invertible modulo L, the same least period holds in j.

This is an exact least-period statement for the predicate \(\delta_P=5\). It neither bounds the information in the full integer state nor claims an absolutely smallest encoding among arbitrary functions.

## 6. Least root from a finite family of progressions

Each one of the 108 phase dictionaries specifies five distinct primes. For each of its 32 independent root-sign choices, solve

\[
a\equiv a_*\pmod{6M},
\qquad a\equiv\pm2^{-c_q}\pmod q
\quad(q\text{ in that dictionary}).
\tag{19}
\]

There is one least nonnegative representative modulo

\[
6M\prod_{q\text{ in the dictionary}}q.
\]

It is positive because its residue modulo 6M is the positive a_*. Every later positive representative is larger. Thus the least cost-five root is found by comparing exactly

\[
108\cdot32=3456
\tag{20}
\]

CRT progression starts. These progression descriptions have different moduli and can overlap; no disjointness is assumed in this minimum argument. There is no need to enumerate the roughly 80 trillion residues modulo L.

The least values within the three phase types are:

\[
\begin{array}{ll}
\mathrm{I},r=0:&39741911323337250951212360989279347168190786597922987443929,\\
\mathrm{II},r=0:&61222665924684986635031943105967801542609331745630965435461,\\
\mathrm{II},r=1:&62924692928616911047137866279148034266265445978646078445719.
\end{array}
\tag{21}
\]

The first is the global minimum in (6). Its two nested-optimal orders remain 5,13,11,61,331 and 5,13,61,11,331, with root residues \((4,5,6,29,269)\) at \((5,13,11,61,331)\).

For a concrete new non-nested pattern, the Type II,r=1 minimum uses

\[
(q,c_q)=(5,0),(13,1),(37,3),(19,0),(109,15),
\]

and root residues \((4,6,14,18,101)\) in that order. Here 13 first covers the smaller mod-3 class of the chosen parity, leaving 23 positions. The last three channels cover the three relative mod-3 phases. It is a full cost-five cover even though the first two channels do not attain the preceding universal budget-two optimum.

Every root from (19) is at least a_*, and every prime in these dictionaries is at most 331; the old primes are at most 6700417. Therefore \(2a^2-1\) exceeds all assigned primes, making all prime divisors proper. The four-channel gap proves exact additional cost 5 for every such root.

## 7. Reproduction and retained evidence

Run:

```sh
python verify_observer.py
```

The calculation uses only exact Python integers and rational numbers. It performs complete supporting factorizations for effective orders 3, 4, 5, 7; checks all phase-root pairs and exact small orders; verifies coverage and a private old-hole witness for each of the 108 phase dictionaries over its full hole period; enumerates all 3456 CRT sign choices; computes the exact root counts by weighted category tuples; and verifies each essential-coordinate witness.

The weighted enumeration uses 64 U-label tuples and 256 W-label tuples. Each label's weight is its exact root-residue cardinality, so this is a complete factorized count over all L root residues, not a sample. The certificate stores every phase dictionary, its 32-sign minimum, and the global minimum; the program reconstructs all individual starts.

The global all-prime necessity theorem and the inherited four-channel gap are mathematical dependencies. This finite calculation checks the complete dictionary after those proofs establish its exhaustiveness. The new minimum claim is therefore broader than the preceding nested-only minimum but retains the fixed old root class as its scope.

The native integer update, fixed X6 anchor, positive singleton BRC weight and multiplicity remain unchanged. This note concerns a particular observation of the original state and does not replace its integer or joint-cofactor information by residues. Parent integration separately records actual native execution of the new phase families.

## Appendix: complete new W-phase root-residue table

| epsilon | r13 | Prime | Relative category 0: phase; roots | Relative category 1: phase; roots | Relative category 2: phase; roots |
|---:|---:|---:|---|---|---|
| 0 | 0 | 19 | 4; {6, 13} | 1; {9, 10} | 7; {4, 15} |
| 0 | 0 | 37 | 4; {7, 30} | 10; {3, 34} | 16; {4, 33} |
| 0 | 0 | 73 | 4; {32, 41} | 1; {36, 37} | 7; {4, 69} |
| 0 | 0 | 109 | 4; {34, 75} | 10; {38, 71} | 16; {4, 105} |
| 0 | 1 | 19 | 0; {1, 18} | 6; {8, 11} | 3; {7, 12} |
| 0 | 1 | 37 | 0; {1, 36} | 6; {11, 26} | 12; {10, 27} |
| 0 | 1 | 73 | 0; {1, 72} | 6; {8, 65} | 3; {9, 64} |
| 0 | 1 | 109 | 0; {1, 108} | 6; {46, 63} | 12; {45, 64} |
| 1 | 0 | 19 | 1; {9, 10} | 7; {4, 15} | 4; {6, 13} |
| 1 | 0 | 37 | 1; {18, 19} | 7; {13, 24} | 13; {5, 32} |
| 1 | 0 | 73 | 1; {36, 37} | 7; {4, 69} | 4; {32, 41} |
| 1 | 0 | 109 | 1; {54, 55} | 7; {23, 86} | 13; {32, 77} |
| 1 | 1 | 19 | 3; {7, 12} | 0; {1, 18} | 6; {8, 11} |
| 1 | 1 | 37 | 3; {14, 23} | 9; {6, 31} | 15; {8, 29} |
| 1 | 1 | 73 | 3; {9, 64} | 0; {1, 72} | 6; {8, 65} |
| 1 | 1 | 109 | 3; {41, 68} | 9; {33, 76} | 15; {8, 101} |
