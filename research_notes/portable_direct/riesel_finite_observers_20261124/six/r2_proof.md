# Sharp budget six on R2 and the failure of nested optimal dictionaries

Status: author mathematical proof with exact supporting arithmetic in the existing direct research Activity `RA-D2EC212845B63844081F9A14`, Researcher `EM-DIRECT-970E1C`. The derivation and its shared-context checks do not constitute an independent project Review, formal acceptance or Foundation promotion.

## 1. The fixed fiber and the optimization problem

Use the square-Riesel sequence

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

the twenty-prime dictionary P, root a*, and product M defined in the [complete-six companion](proof.md). In particular,

\[
a_*=690786768637635218740714348513373826260012289,
\qquad
M=1397394912916194098609132326092145093313722687204526281.
\]

Let

\[
L=80754838636615,
\qquad
R_1=\{a>0:a\equiv a_*\pmod{6M},\
a\equiv12926327728523\pmod L\}.
\]

The fixed 31-channel fiber is

\[
R_2=\{a\in R_1:a\equiv0\pmod{433},\
a\equiv38733\pmod{38737}\}.
\tag{1}
\]

Its additional modulus and residue are

\[
L_2=1354510679787418425415,
\qquad a\equiv602924359709868072943\pmod{L_2}.
\tag{2}
\]

Every root in R2 has the same complete residue-value trajectory at the 31 primes \(P\cup\{5,13,11,61,331,19,37,73,109,433,38737\}\). This follows from the fixed root congruences, not from a finite sampling of future indices.

For a finite set Q of primes outside P, let \(\operatorname{gap}(a,Q)\) denote the natural density, among all positive exponent indices n, of terms not divisible by any prime in \(P\cup Q\). The relevant zero sets are periodic, so this density exists. Every term is already composite on the old root class, by the old odd-index cover and the even-index factorization. Thus a prime dividing a term here is a proper divisor.

Define the sharp uniform budget value

\[
D_t(R_2)=\inf_{a\in R_2,\ |Q|\le t}\operatorname{gap}(a,Q).
\tag{3}
\]

The root and the dictionary may vary when taking this infimum. A statement that one specified root attains an entry is made separately below. The exact supplementary cost \(\delta_P(a)\) is the minimum size of a complete supplement, with infinity if none exists.

**Theorem.** The sharp values for budgets zero through seven are

\[
\boxed{(D_0,\ldots,D_7)
=\frac1{5040}(864,432,156,104,52,26,12,0).}
\tag{4}
\]

Every budget-six equality dictionary contains exactly the four fixed primes

\[
5,13,19,73
\]

and two distinct primes from

\[
\mathcal C=\{181,631,23311,54001,18837001,29247661\}.
\tag{5}
\]

On the residual coordinate w introduced below, those two primes must occupy respectively the classes 0 and 3 modulo 5. There are exactly \(6\cdot5=30\) phase dictionaries. Each can be realized by CRT.

Every budget-five equality dictionary in R2 is

\[
Q_5^*=\{5,13,19,73,38737\}.
\tag{6}
\]

Any extension of (6) by one prime has gap at least \(13/5040\), strictly larger than the unrestricted budget-six optimum \(12/5040\). Therefore no nested chain of dictionaries can attain both the fifth and sixth sharp values in (4).

The classification is over all primes and orders. It does not impose a numerical prime cutoff. A conditional classification of a seventh prime extending a budget-six equality dictionary is proved in Section 7; no classification of all seven-prime covers is asserted.

## 2. Exact residual sets and their incidence bounds

The inherited old holes have density \(6/35\). The fixed prime 5 covers \(u\equiv1\pmod2\), and 13 covers \(u\equiv0\pmod6\), where n=2u. After both, the remaining indices have

\[
u=4+6v,\qquad
v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{7}
\]

Their density among n is \(13/420\). The A-incidence counts modulo 7 are

\[
(0,2,3,3,3,2,0).
\tag{8}
\]

Prime 19 covers \(v\equiv0\pmod3\), and prime 73 covers \(v\equiv1\pmod3\). The other W primes 37 and 109 divide the root and are inactive. After both active W primes, put

\[
v=2+3w,\qquad u=16+18w,
\]

so that

\[
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{9}
\]

This remainder has density \(13/1260\) among n. Its counts modulo 5 are

\[
(5,3,0,5,0).
\tag{10}
\]

For either 13-element set A or B, the maximal incidence counts in classes modulo \(g=1,5,7,35\) are respectively \(13,5,3,1\). More generally, if S has m residues modulo 35, then the relative density of a class \(x\equiv c\pmod d\) within S is

\[
\frac{K_g(c)}{m(d/g)},\qquad
g=\gcd(d,35),\quad
K_g(c)=|\{s\in S:s\equiv c\pmod g\}|.
\tag{11}
\]

This is exact counting in the common period. All bounds below are consequences of (11), actual root phases, and complete small-order exclusions. No independence assumption is made where periods have a common factor.

The reused source for the old holes, small-order exclusions, and complete budget-five equality theorem is commit `b1de1acbdc97b5e51d486127abd1fadd24babd99`, paths
`research_notes/portable_direct/riesel_five_cover_20261123/global/proof.md` and `fiber/proof.md`. The new fixed-phase bounds for omitting 5 or 13 are proved in the present batch's [complete-six note](proof.md), Section 3.

## 3. Any budget-six equality dictionary contains 5 and 13

Suppose Q has at most six primes and omits both 5 and 13. The companion all-prime bound says its union covers at most \(83/108\) of the old holes in R1, hence also in R2. Thus

\[
\operatorname{gap}(a,Q)
\ge\frac6{35}\left(1-\frac{83}{108}\right)
=\frac5{126}>\frac1{420}.
\tag{12}
\]

If Q contains exactly one of 5 and 13, that prime misses an entire u-parity, whose old-hole density is \(3/35\) among n. At most five other channels can cover at most \(8/9\) of that parity's old holes, by the sharpened fixed-phase argument in the same companion. Therefore

\[
\operatorname{gap}(a,Q)
\ge\frac3{35}\left(1-\frac89\right)
=\frac1{105}>\frac1{420}.
\tag{13}
\]

Consequently every dictionary attaining or improving on \(1/420\) contains both basic primes, and its remaining task is to cover (7) with at most four primes.

## 4. Both active W primes are forced at budget-six equality

For any active non-W prime after (7), put

\[
f_q=\operatorname{ord}_q(2^{12}).
\]

Effective orders 1,2,4 yield only old/basic primes, order 3 yields W, and order 5 yields the inactive primes 11,61,331. The inherited four gcd-column upper bounds on A are therefore

\[
\left(\frac16,\frac5{26},\frac3{13},\frac1{13}\right)
\quad(g=1,5,7,35).
\tag{14}
\]

### 4.1 Neither active W prime is present

There are at most four non-W slots. An active channel can exceed \(5/26\) only when \(f_q=7\): the gcd-7 column at any larger such period is at most \(3/26\), and the other three columns in (14) are at most \(5/26\).

If all four slots have effective period 7, they are four classes modulo 7. By (8), even the four largest incidence classes contain only \(3+3+3+2=11\) of A's thirteen residues. Their union therefore misses density at least

\[
\frac{13}{420}\left(1-\frac{11}{13}\right)
=\frac1{210}>\frac1{420}.
\tag{15}
\]

If at least one slot has another effective period, is inactive, or is absent, the union bound is at most \(3(3/13)+5/26=23/26\). Thus the gap is at least

\[
\frac{13}{420}\left(1-\frac{23}{26}\right)
=\frac1{280}>\frac1{420}.
\tag{16}
\]

### 4.2 Exactly one active W prime is present

This prime covers exactly one third of A, corresponding to one v-class modulo 3. Each of at most three remaining non-W channels contributes at most \(1/6\) of the original A outside that W class. To prove this stronger bound, separate two cases.

If 3 does not divide \(f_q\), CRT makes the channel's A-hits equally distributed among the three v-classes modulo 3, since \(3\nmid35f_q\). Exactly two thirds survive outside W. By (14), their density relative to A is at most

\[
\frac23\frac3{13}=\frac2{13}<\frac16.
\]

If 3 divides \(f_q\), its class either lies inside the selected W class, contributing zero outside, or lies entirely outside. For the latter case, (11), \(f_q\ge6\), and \(3\mid f_q/g\) give the four respective bounds

\[
\left(\frac16,\frac5{39},\frac1{13},\frac1{39}\right).
\tag{17}
\]

Their maximum is \(1/6\). Hence the total union covers at most \(1/3+3/6=5/6\) of A, leaving

\[
\operatorname{gap}(a,Q)
\ge\frac{13}{420}\left(1-\frac56\right)
=\frac{13}{2520}>\frac1{420}.
\tag{18}
\]

The alternatives are exhausted. Every budget-six equality dictionary must contain 5,13,19,73, leaving at most two slots to cover (9).

## 5. The last two slots: exact value and all equality cases

In R2, prime 38737 covers \(w\equiv1\pmod2\); prime 433 is inactive.

### 5.1 Retaining 38737 is strictly suboptimal at budget six

After 38737, the missed part has w even. Write w=2z. The resulting z-condition is an affine 13-element set modulo 35 with the same incidence maxima. A further active prime has effective period \(\operatorname{ord}_q(2^{72})\). Period one can provide no new hits: every prime dividing \(2^{72}-1\) is old, already used, or inactive in this fiber. Formula (11) therefore bounds a new prime's contribution by at most one half of this remainder; the other gcd columns are at most \(5/13,3/13,1/13\).

It follows that every one-prime extension of the fixed five-prime dictionary has

\[
\operatorname{gap}(a,Q)
\ge\frac{13}{1260}\frac12\frac12
=\frac{13}{5040}>\frac1{420}.
\tag{19}
\]

The bound is attainable at appropriate roots by an order-144 prime in the appropriate z-parity, as the concrete binary route in Section 6 demonstrates. It is therefore the sharp uniform value conditional on retaining (6).

### 5.2 Omitting 38737

For each available active prime on (9), write

\[
h_q=\operatorname{ord}_q(2^{36}).
\]

Period one contributes no new channel. Period two gives only 433 and 38737 outside old/used primes, and both are unavailable in this case. Thus the gcd-column bounds become

\[
\left(\frac13,\frac5{13},\frac3{13},\frac1{13}\right).
\tag{20}
\]

Every channel covers at most \(5/13\) of B. Two channels therefore leave at least

\[
\frac{13}{1260}\left(1-2\frac5{13}\right)
=\boxed{\frac1{420}=\frac{12}{5040}}.
\tag{21}
\]

Equality requires two channels, both attaining \(5/13\), with disjoint contributions. In (20) this is possible only when \(h_q=5\). The complete factorization used by the calculator is

\[
\begin{split}
2^{180}-1={}&3^3 5^2\cdot7\cdot11\cdot13\cdot19\cdot31\cdot37
\cdot41\cdot61\cdot73\cdot109\cdot151\cdot181\\
&\cdot331\cdot631\cdot1321\cdot23311\cdot54001
\cdot18837001\cdot29247661.
\end{split}
\tag{22}
\]

After old, used and inactive primes are excluded, the exact effective-order-five candidates are precisely the six primes in (5). Their base-2 and even-index orders are:

| Prime q | \(\operatorname{ord}_q2\) | \(\operatorname{ord}_q4\) |
|---:|---:|---:|
| 181 | 180 | 90 |
| 631 | 45 | 45 |
| 23311 | 45 | 45 |
| 54001 | 180 | 90 |
| 18837001 | 90 | 45 |
| 29247661 | 180 | 90 |

By (10), the only w-classes of size five are 0 and 3 modulo 5. Two channels with the same class overlap completely on B, so equality requires one of each. A prime cannot occupy both classes at one root, so the two primes are distinct. This proves the necessity of the stated 30 dictionaries.

Conversely, for distinct \(q_0,q_3\in\mathcal C\), impose the u-phases

\[
c_{q_b}\equiv16+18b\pmod{\operatorname{ord}_{q_b}4},
\qquad b=0,3.
\]

Each phase is realized by

\[
a\equiv\pm2^{-c_{q_b}}\pmod{q_b}.
\tag{23}
\]

The primes in C are coprime to the fixed R2 progression modulus. CRT therefore supplies an infinite root progression for every pair of phases and every independent choice of signs. Each has exactly the residual density in (21). This proves sharpness and exhaustiveness over all prime sizes and orders.

The inherited sharp lower bounds for budgets zero through five remain valid on R2. Its fixed channels 5,13,19,73,38737 attain all those entries at every root. A complete seven-prime example is given below, proving the final zero in (4). Since (21) is positive, every root in R2 satisfies \(\delta_P(a)\ge7\).

## 6. A single root exhibits crossing optimal choices

The inherited budget-five equality classification on R1 allows only 433 or 38737 after the four mandatory primes. In R2 only 38737 is active. Thus (6) is the only budget-five equality prime set. All budget-six equality dictionaries from Section 5 omit it. There is consequently no inclusion chain \(Q_5\subset Q_6\) that attains both optima, at any root in R2.

The phenomenon occurs even when the underlying integer root is held fixed. Consider

\[
a=5638859082119336258239285976823481197493104557616679794390344515886945665210917791971325889059624133.
\tag{24}
\]

Besides its R2 residues, this root has the following additional phases and root residues:

| Prime | u phase | Root residue |
|---:|---:|---:|
| 181 | 16 | 13 |
| 631 | 25 | 485 |
| 23311 | 34 | 2048 |
| 577 | 16 | 546 |
| 487824887233 | 52 | 487823838657 |

Both routes below begin with 5,13,19,73. The binary route then uses 38737,577,487824887233. The modulo-five route instead uses 181,631,23311. Their exact uncovered counts, in the common exponent period 5040, are:

| Budget | Binary route | Modulo-five route | Sharp value, in units of \(1/5040\) |
|---:|---:|---:|---:|
| 0 | 864 | 864 | 864 |
| 1 | 432 | 432 | 432 |
| 2 | 156 | 156 | 156 |
| 3 | 104 | 104 | 104 |
| 4 | 52 | 52 | 52 |
| 5 | 26 | 32 | 26 |
| 6 | 13 | 12 | 12 |
| 7 | 0 | 0 | 0 |

Thus the same root attains every sharp budget value when its dictionary may be reselected at each budget. An append-only continuation of its budget-five optimum misses the sixth optimum by at least \(1/5040\). Both displayed routes are complete seven-prime supplements, so \(\delta_P(a)=7\). They give \(\tau(a^2)\le27\), without proving equality of the total minimum.

The two zero rows are statements of complete periodic coverage, not extrapolations from a prefix. Their concrete arithmetic is checked by `r2_verify.py`; actual native BRC execution, if included by the parent integration, is recorded separately.

## 7. Complete seventh-prime extensions of a budget-six equality dictionary

After the C channels at w-classes 0 and 3, the remainder of (9) is

\[
w\equiv21,26,31\pmod{35}.
\]

Equivalently its exponent indices are

\[
n\equiv788,968,1148\pmod{1260}.
\tag{25}
\]

The gcd of all differences among these indices is 180: the displayed pairwise differences include 180 and the common period is \(1260=7\cdot180\). If one prime q divides every term on this remainder, then comparing any two of its zero congruences gives

\[
\operatorname{ord}_q2\mid180.
\]

The complete factors (22), after excluding old, used and inactive primes, leave exactly C. The two already selected C primes cannot contribute to the remainder because their zero w-classes are fixed at 0 and 3. A third distinct member must occupy w-class 1 modulo 5. Conversely that class covers (25) completely.

The conditional seven-prime dictionaries are therefore exactly

\[
\{5,13,19,73,q_0,q_3,q_1\},
\qquad q_0,q_3,q_1\in\mathcal C\text{ distinct},
\tag{26}
\]

with the indicated phases. There are \(6\cdot5\cdot4=120\) phase dictionaries. Each has eight root-sign progressions and each root has exact supplementary cost seven, because budget six always leaves a positive gap.

This is an exhaustive classification of seventh-prime extensions of a budget-six equality dictionary. It is not an exhaustive classification of all seven-prime complete supplements. For example, the binary route in Section 6 is a seven-prime dictionary outside (26).

## 8. Exact finite observers, counts and scoped minima

For each q in C, the three relevant phase categories b=0,3,1 each contain two root residues given by (23); their six residues are distinct. All other q-residues are placed in the remaining category. Let

\[
T=\prod_{q\in\mathcal C}q=79208819702303143625098260481.
\tag{27}
\]

Define E6 to mean that a root in R2 admits a budget-six equality dictionary, and N7 to mean that it admits a complete seven-prime dictionary extending such an equality dictionary. Then

\[
E6\iff\text{categories 0 and 3 both occur among the C coordinates},
\]

\[
N7\iff\text{categories 0, 3 and 1 all occur among the C coordinates}.
\tag{28}
\]

Inclusion-exclusion gives the exact true root-class counts modulo T:

\[
\begin{aligned}
|E6|&=T-2\prod_{q\in\mathcal C}(q-2)
       +\prod_{q\in\mathcal C}(q-4)\\
&=5823767115854050658573528,\\[2mm]
|N7|&=T-3\prod_{q\in\mathcal C}(q-2)
       +3\prod_{q\in\mathcal C}(q-4)
       -\prod_{q\in\mathcal C}(q-6)\\
&=2068723011224822069760.
\end{aligned}
\tag{29}
\]

Their relative natural densities inside R2 are these counts divided by T, since the R2 progression step is coprime to T.

Every C coordinate is essential for each predicate. For E6, fix one other coordinate in category 3 and all remaining coordinates outside the relevant categories; changing the selected coordinate from inactive to category 0 changes the truth value. For N7, fix two other coordinates in categories 0 and 3, and change the selected coordinate from inactive to category 1. CRT realizes these choices. If d were any smaller positive additive period, then gcd(d,T) would also be a period and would be a proper divisor of T. Since T is squarefree, this would omit some essential prime coordinate, a contradiction. Hence the least positive additive period in the R2 progression parameter is exactly T for each predicate. This is a period statement for the specified predicates, not a claim about arbitrary encodings of the full integer state.

The calculator compares every CRT progression start: 30 phase dictionaries times four sign choices for E6, and 120 times eight for N7. It obtains:

| Predicate | Least positive root in the specified R2 subclass | Root digits |
|---|---|---:|
| E6 | 74907363161629215503412103697786153275793084337120229356960030843718156640718393 | 80 |
| N7 | 168515727251568031139784117408423468924151126118048106286760549300706338389494633573 | 84 |

The E6 minimum has q=181 in category 0, residue 13, and q=631 in category 3, residue 146. No exact full-cover cost is inferred from E6 alone. The N7 minimum has q=631 in category 0, q=23311 in category 3, and q=181 in category 1, with residues 337,22892,178. Its supplementary cost is seven and its total cost is at most 27. Its minimum scope is only N7, not all roots of supplementary cost seven.

The complete phase/root table, category weights and CRT data are retained in `r2_certificate.json`.

## 9. Evidence, reuse and native interpretation

Run

```sh
python r2_verify.py
```

The calculator verifies the complete factorization (22) using exact integer products and deterministic trial primality of every factor; it verifies the exact multiplicative orders of all six C primes. It checks the strict rational inequalities separating every prefix alternative, the full phase dictionaries over their complete common periods, all 4096 weighted category tuples for (29), every CRT progression start used for the two minima, and both complete routes at the same root (24).

The all-prime result rests on the written incidence and effective-order argument in Sections 3–5. It is not inferred from enumerating finitely many candidate primes before proving the reduction. The conditional seventh-prime result rests on the difference-gcd argument in Section 7. Old small-order exclusions, old hole geometry and the budget-five equality theorem are reused at their pinned scientific scope. The calculator does not claim a new independent native execution or pairwise-coprimality computation for the compact roots.

The [observer companion](../observer/proof.md) separately proves that every finite supplementary cost at least seven occurs in this same R2 fiber, with total cost exactly 20 plus that supplementary cost for its coprimalized families. That construction requires its stated modified seeds; it is not a consequence of the density staircase alone.

The native state remains the typed integer register with fixed X6 anchor, positive singleton BRC weight and multiplicity one, and update \(x\mapsto2x+1\). Prime channels are readouts of that one state. The new result says that optimal finite prime dictionaries for a specified task need not be nested as the permitted dictionary size increases. It does not add branches or axes to the native state, and it does not identify the full integer or joint cofactor information with the 31 fixed readouts.
