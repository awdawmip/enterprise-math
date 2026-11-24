# All four-prime tails in R3, conditional on retaining 5, 13, 19 and 73

Research continuation, 2026-11-24 (Asia/Hong_Kong). Author proof with shared-context mathematical assistance and exact arithmetic; existing Researcher `EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is not an independent project Review.

## 1. Scope and result

Retain the square-Riesel trajectory \(F_n(a)=a^2 2^n-1\), the twenty-prime old dictionary P and the fixed 43-prime observation fiber R3 from the v12 `fiber/proof.md`. The full native integer register remains at a fixed Heartbeat X6 anchor with positive singleton BRC update \(x\mapsto2x+1\). All residue coordinates below observe that state.

The result here assumes that the supplementary dictionary contains

\[
Q_0=\{5,13,19,73\}.
\tag{1}
\]

It classifies every complete supplement of at most eight primes satisfying (1), across every positive root in R3 and every possible prime. The hypothesis is essential: there are eight-prime supplements on R3 which omit 19 and 73. The separate basic-pair result forces 5 and 13 but does not force the whole set (1) at budget eight.

After P and (1), the exact remaining exponents are

\[
n=32+36w,
\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{2}
\]

Among the small effective-order tail channels, the R3 conditions leave exactly these fixed active channels:

| Prime | Effective w-period | Fixed zero phase |
|---:|---:|---:|
| 38737 | 2 | 1 |
| 246241 | 3 | 1 |
| 487824887233 | 4 | 2 |

All other previously identified period-two, period-three, period-four and period-five candidates are old, already in (1), or inactive in R3. In particular, 577 and the six old modulo-five-tail candidates divide a and contribute no zeros.

Define

\[
\begin{aligned}
\mathcal B_8={}&\{193,1153,6337,22253377,38941695937,278452876033\},\\
\mathcal D_6={}&\{33975937,138991501037953\},\\
\mathcal C_{10}={}&\{61681,4562284561,168692292721,469775495062434961\}.
\end{aligned}
\]

**Theorem.** Every complete four-prime tail after (1) includes 38737. Its other three primes have exactly one of the following forms:

| Family | Fixed tail primes | Free primes and phases | Phase dictionaries | Signed CRT descriptions |
|---|---|---|---:|---:|
| Binary | 38737 and 487824887233 | Two distinct primes in \(\mathcal B_8\), assigned w=0 and w=4 modulo 8 | 30 | 120 |
| Ternary | 38737 and 246241 | Both primes in \(\mathcal D_6\), assigned w=0 and w=2 modulo 6 | 2 | 8 |
| Modulo five | 38737 | Three distinct primes in \(\mathcal C_{10}\), assigned w=0,6,8 modulo 10 | 24 | 192 |
| Total | | | **56** | **320** |

The phase assignments are bijections to the listed phases. For each free prime q assigned phase b, the exact root requirement is

\[
a\equiv\pm2^{-(16+18b)}\pmod q.
\tag{3}
\]

All twelve free primes are outside the R3 progression modulus, so CRT realizes every row and sign choice. Their root families can overlap, and the 320 progression descriptions are not disjoint residue classes. Every resulting root has exact supplementary cost eight by the inherited complete seven-cover obstruction on R3.

## 2. Incidence formula for all primes

An active prime q on the progression in (2) has one zero class modulo

\[
h=\operatorname{ord}_q(2^{36}).
\]

For any class w=c modulo h, put \(g=\gcd(h,35)\), and let

\[
K_g(c)=|\{b\in B:b\equiv c\pmod g\}|.
\]

Exact common-period counting gives its density relative to (2):

\[
\mu_B(w\equiv c\pmod h)=\frac{K_g(c)}{13(h/g)}.
\tag{4}
\]

The maxima of K for g=1,5,7,35 are respectively 13,5,3,1. Prime 2 and any prime dividing a are inactive. This calculation counts compatible lifts and does not assume independent phases when moduli have common factors.

After the three fixed active primes in Section 1 are removed, every other available prime has w-period at least six, with period five entirely inactive. Formula (4) bounds every such channel by 3/13. Moreover, a channel whose period is not seven has density at most 5/26:

| gcd(h,35) | Generic admissible period | Maximum density |
|---:|---|---:|
| 1 | h at least 6 | 1/6 |
| 5 | h at least 10 | 5/26 |
| 7 | h=7, or h at least 14 | 3/13, or 3/26 |
| 35 | h at least 35 | 1/13 |

The complete small-period inventories needed for these exclusions are verified from the exact products in Section 6.

## 3. The odd-w channel 38737 is compulsory

Suppose a tail with at most four primes omits 38737. Separate the other two fixed active primes R=246241 and U=487824887233.

If both R and U are absent, the union density is at most \(4(3/13)=12/13<1\). If only U is present, it is at most

\[
\frac14+3\frac3{13}=\frac{49}{52}<1.
\]

If both R and U are present, their union has exact density

\[
\frac13+\frac14-\frac1{12}=\frac12.
\]

The last equality holds relative to B because its period 35 is coprime to 12. The two other channels add at most 6/13, giving \(25/26<1\).

It remains to consider R present and U absent. If any of the three other channels has period different from seven, (4) gives

\[
\frac13+2\frac3{13}+\frac5{26}=\frac{77}{78}<1.
\tag{5}
\]

Thus all three would have to have period seven. They cover at most nine of the thirteen B residues, leaving some entire class \(w=b\pmod{35}\) uncovered by them. Its lifts run through all three classes modulo three, since gcd(35,3)=1. The single R phase w=1 modulo three misses some of these lifts. Hence this last case also fails.

Every complete four-prime tail therefore contains 38737. This is an all-prime deduction; no prime-size cutoff has been imposed.

## 4. Classify the remaining three primes on even w

Put w=2z. The residual set becomes

\[
z\in B'=\{0,4,5,13,14,15,19,20,25,28,29,33,34\}\pmod{35}.
\tag{6}
\]

Its incidence maxima remain 13,5,3,1. Its counts modulo five are

\[
(5,0,0,3,5).
\tag{7}
\]

The fixed R channel has z=2 modulo three; the fixed U channel has z=1 modulo two. For any further prime, the effective z-period is \(e=\operatorname{ord}_q(2^{72})\). There is no unselected active period-one prime. U is the only available active period-two prime.

### 4.1 U is selected: exactly the binary family

U covers odd z. On its even complement write z=2t, hence w=4t. The remaining residue set is a multiplication of B by the inverse of four modulo 35 and has the same incidence maxima. A further prime has effective period \(f=\operatorname{ord}_q(2^{144})\).

No unselected active prime has f=1. Each remaining channel therefore covers at most one half of this complement. Equality is possible only at f=2: the other gcd columns in the analogue of (4) are bounded by 5/13,3/13,1/13, all strictly below one half.

Two primes can complete the cover only when both have f=2 and take opposite t-parities. The complete factorization of \(2^{288}-1\) leaves precisely \(\mathcal B_8\) after old, fixed-inactive and already-used primes are removed. Their w-phases are 0 and 4 modulo eight. Any two distinct primes assigned these opposite phases suffice. This gives \(6\cdot5=30\) phase dictionaries and \(30\cdot4=120\) signed descriptions.

In particular, the two primes of base-two order 96, namely 193 and 22253377, must be included. Their effective period on w is eight, just as for the four primes of order 288. Restricting the inventory to primitive order-288 divisors would omit valid dictionaries.

### 4.2 U is not selected: all-prime reduction to periods 3,4,5,7

Without U, every one of the remaining three channels covers at most 5/13 of the z remainder. If one covered less than 3/13, the other two could not make the union complete. Therefore every channel has relative density at least 3/13.

Apply (4), now with e and B'. In the gcd-one column, \(1/e\ge3/13\) forces e at most four; periods one and two have been excluded. In the gcd-five column, \(5/[13(e/5)]\ge3/13\) forces e=5. In the gcd-seven column it forces e=7. The gcd-35 column never reaches 3/13. Hence

\[
e\in\{3,4,5,7\}.
\tag{8}
\]

This finite reduction precedes the factorization step and covers all possible primes.

### 4.3 Period four and period seven are impossible

A period-four class contributes one quarter. If either of the other two classes is not period five, the union density is at most

\[
\frac14+\frac5{13}+\frac13=\frac{151}{156}<1.
\]

Thus both would have to have period five. Two such classes cover at most ten of the thirteen B' residues, leaving an entire class modulo 35. Its lifts visit all four period-four phases, so one period-four channel cannot cover them.

A period-seven class contributes at most 3/13. Complete coverage would require both others to attain 5/13, using the two maximal period-five classes 0 and 4. The remaining B' residues are

\[
13,28,33\pmod{35}.
\]

Their residues modulo seven are 6,0,5, respectively. One period-seven class cannot cover all three. Thus period seven is impossible as well.

### 4.4 Periods three and five cannot be mixed

A mixed triple has only one or two period-five classes. Those leave some whole B' class modulo 35 uncovered. Its lifts visit every residue modulo three, and at most two period-three classes cannot cover all lifts. Thus a complete triple is either entirely period three or entirely period five.

A pure period-three triple takes all phases 0,1,2. The full \(2^{216}-1\) inventory leaves only R=246241 and the two primes in \(\mathcal D_6\) active and unselected. R already has z-phase two, so the two new primes take z-phases zero and one. These are w-phases zero and two modulo six. There are two assignments and four independent sign choices, giving 2 dictionaries and 8 descriptions.

A pure period-five triple must take precisely the occupied B' phases 0,3,4. The complete \(2^{360}-1\) inventory leaves exactly the four primes in \(\mathcal C_{10}\). Selecting and assigning three of them gives \(4\cdot3\cdot2=24\) dictionaries; the independent root signs give 192 descriptions. Their z-phases correspond to w=0,6,8 modulo ten.

This exhausts the cases after the compulsory 38737 row and proves the classification theorem.

## 5. Exact orders and realizable root conditions

The required order table is:

| Family | Prime | Exact base-two order | Effective w-order |
|---|---:|---:|---:|
| Binary | 193 | 96 | 8 |
| Binary | 1153 | 288 | 8 |
| Binary | 6337 | 288 | 8 |
| Binary | 22253377 | 96 | 8 |
| Binary | 38941695937 | 288 | 8 |
| Binary | 278452876033 | 288 | 8 |
| Ternary | 33975937 | 216 | 6 |
| Ternary | 138991501037953 | 216 | 6 |
| Modulo five | 61681 | 40 | 10 |
| Modulo five | 4562284561 | 120 | 10 |
| Modulo five | 168692292721 | 360 | 10 |
| Modulo five | 469775495062434961 | 360 | 10 |

The exact effective periods are obtained by dividing the base-two order by its gcd with 36. For a fixed prime, the required phases have disjoint two-element root categories (3). CRT with the R3 progression and the selected free primes realizes each category assignment. Every compact prime appearing here is much smaller than the least R3 root, so its zero hits are proper divisors throughout the positive progression.

For clarity, the theorem characterizes the predicate

\[
\mathsf A^{Q_0}_8(a):
\text{there exists a complete supplement of at most eight primes containing }Q_0.
\]

It implies \(\delta_P(a)=8\) whenever true. A false value does not exclude a cost-eight dictionary which omits 19 or 73. The full cost-eight predicate remains a distinct classification problem.

## 6. Complete finite-order inventories and primality certificates

The calculator retains and verifies these full products:

\[
\begin{aligned}
2^{216}-1={}&3^4\cdot5\cdot7\cdot13\cdot17\cdot19\cdot37\cdot73\cdot109\cdot241\cdot433\cdot38737\\
&\cdot87211\cdot246241\cdot262657\cdot279073\cdot33975937\cdot138991501037953;\\[2mm]
2^{288}-1={}&3^3\cdot5\cdot7\cdot13\cdot17\cdot19\cdot37\cdot73\cdot97\cdot109\cdot193\cdot241\cdot257\cdot433\\
&\cdot577\cdot673\cdot1153\cdot6337\cdot38737\cdot65537\cdot22253377\cdot38941695937\\
&\cdot278452876033\cdot487824887233;\\[2mm]
2^{360}-1={}&3^3 5^2\cdot7\cdot11\cdot13\cdot17\cdot19\cdot31\cdot37\cdot41\cdot61\cdot73\cdot109\cdot151\cdot181\\
&\cdot241\cdot331\cdot433\cdot631\cdot1321\cdot23311\cdot38737\cdot54001\cdot61681\cdot18837001\\
&\cdot29247661\cdot4562284561\cdot168692292721\cdot469775495062434961.
\end{aligned}
\]

Every displayed factor is proved prime by deterministic odd trial division except the following two, for which a complete n-minus-one certificate is shorter:

| n | Complete factorization of n−1 | Witness a |
|---:|---|---:|
| 138991501037953 | \(2^7 3^3\cdot79\cdot509081623\) | 5 |
| 469775495062434961 | \(2^4 3^2\cdot5\cdot7\cdot151\cdot617280951149\) | 19 |

Each factor of n−1 is itself proved prime by deterministic trial division. The calculator checks \(a^{n-1}\equiv1\pmod n\) and, for every prime p dividing n−1,

\[
\gcd(a^{(n-1)/p}-1,n)=1.
\]

Here is the complete elementary justification of the certificate. If r is any prime divisor of n, the first equality makes the order of a modulo r divide n−1. The gcd conditions force that order to contain the full power of every prime p in n−1. Thus its order is n−1, which divides r−1. Consequently r is at least n and n must be prime. No probabilistic primality claim is used.

After product and primality verification, filtering by exact effective order identifies every possible prime in Sections 2–4. For example, \(\operatorname{ord}_q(2^{72})=5\) implies q divides \(2^{360}-1\), so the complete third product rules out an omitted candidate of that order.

## 7. Reproduction and evidence scope

Run `python verify_tail_eight.py`. The standard-library calculator checks all complete products and primality certificates; every required exact order and excluded small-period inventory; the incidence counts and strict rational bounds; the exact half-density union used to force 38737; all reduced three-class patterns in (8); every one of the 56 full tail phase dictionaries; and every two-root category used by those dictionaries.

The output `tail_eight_certificate.json` records 30 binary, 2 ternary and 24 modulo-five dictionaries, with 120,8,192 respective signed descriptions. The universal completeness assertion comes from the all-prime argument in Sections 2–4, not from a bounded search over prime sizes.

This component does not rerun native BRC trajectories or compare the 320 CRT starts. Those computations can consume its complete phase/root table. The mathematical scope remains conditional on (1).
