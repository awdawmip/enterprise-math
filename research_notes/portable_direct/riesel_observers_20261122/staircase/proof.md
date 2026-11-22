# Exact residual-density staircase and complete equality classification

Status: author mathematical derivation and exact arithmetic evidence in the existing direct research activity. Researcher `EM-DIRECT-970E1C`; Activity `RA-D2EC212845B63844081F9A14`. This is not an independent project Review or a formal admission result.

## 1. The question and the quantifiers

Keep the native integer register

\[
F_n(a)=a^2 2^n-1,\qquad n\ge1,
\]

at the existing X6 anchor. Its positive singleton BRC packet is \(x\mapsto2x+1\), with weight and multiplicity 1; the even packet is \(x\mapsto4x+3\). Prime observations retain their existing types. Nothing here adds a spatial axis, a native branch, or a physical-time interpretation to the arithmetic index.

Use the established root class

\[
a\equiv a_*\pmod{2M},\qquad a>0,
\]

where

\[
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

The old dictionary covers all odd indices. The old holes at even indices \(n=2u\) are exactly the following 36 classes modulo 105:

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}.
\end{split}
\]

Their density among all exponent indices is \(36/210=6/35\). Every term is composite: odd terms have the old proper divisor, while even terms factor as \((a2^u-1)(a2^u+1)\).

For a finite set Q of primes outside P, define

\[
d(a,Q)=\operatorname{dens}\{n\ge1:\ 
p\nmid F_n(a)\text{ for every }p\in P\cup Q\}.
\]

The density exists because a finite prime dictionary gives a periodic divisibility predicate. For a fixed root, set

\[
b_t(a)=\inf_{|Q|\le t}d(a,Q).
\]

The universal theorem below concerns roots with \(3\mid a\). Prime 3 is then inactive; prime 2 is always inactive. At roots with \(3\nmid a\), the one extra channel 3 already covers every old hole, so the positive-budget staircase below does not describe that branch.

**Theorem 1 — sharp budget staircase.** For every positive root in the old class with \(3\mid a\), and every finite set Q of at most t new prime channels,

\[
\boxed{
d(a,Q)\ge D_t,\qquad
(D_0,D_1,D_2,D_3,D_4,D_5)
=\frac1{420}(72,36,13,8,3,0).
}
\tag{1}
\]

For \(t\ge5\), the sharp universal lower bound remains zero. One fixed root, with one nested five-prime dictionary, attains every bound in (1) simultaneously. Thus each \(D_t\) is the exact best lower bound uniform over this root branch. It is not asserted that every individual root attains every \(D_t\).

**Theorem 2 — all equality cases for budgets 1–4.** Write \(c_q\) for the even zero phase, so an active q divides \(F_{2u}(a)\) precisely when

\[
u\equiv c_q\pmod{\operatorname{ord}_q4}.
\]

For a supplement of at most t new primes, equality in (1) holds exactly as follows. Each listed prime must be active with the stated phase; there is no room for an additional inactive or unused prime.

- **t = 1:** Q is \(\{5\}\). Either of its two even zero phases is allowed. Equivalently, \(5\nmid a\).
- **t = 2:** Q is \(\{5,13\}\). For some \(\varepsilon\in\{0,1\}\),
  \[
  c_5=1-\varepsilon\pmod2,\qquad
  c_{13}=3\varepsilon\pmod6.
  \tag{2}
  \]
  In particular, their zero parities are opposite and the 13 phase is 0 modulo 3.
- **t = 3:** The two channels in (2) are supplemented by one prime from
  \[
  U=\{11,61,331\}.
  \]
  On the remaining fiber \(u\equiv\varepsilon\pmod2\), \(u\equiv1\pmod3\), that prime covers exactly the class \(u\equiv r\pmod5\), where \(r=0\) or 1.
- **t = 4:** The two channels in (2) are supplemented by two distinct primes from U. On that same fiber, one covers \(u\equiv0\pmod5\), and the other covers \(u\equiv1\pmod5\).

All these phase systems are realizable by infinitely many positive roots in the old class with \(3\mid a\). There are respectively 2, 2, 12 and 12 phase dictionaries at budgets 1, 2, 3 and 4. Root signs are not counted as different phase dictionaries.

The conclusion is unrestricted in prime magnitude and order. A finite dictionary of equality candidates will be derived from the analytic bound; it is not assumed as a search range.

**Attainment at the sharp value.** For each fixed root and \(1\le t\le5\), the condition \(b_t(a)=D_t\) is equivalent to the existence of a dictionary attaining \(D_t\). To see the nontrivial direction, put \(\gamma=D_{t-1}-D_t>0\). Any Q with \(d(a,Q)<D_t+\gamma/2\) must use exactly t active channels. Removing any q leaves density at least \(D_{t-1}\), so q's unique contribution exceeds \(\gamma/2\). But a prime's even zero class has full-index density at most \(1/(2\operatorname{ord}_q4)\). Consequently \(\operatorname{ord}_q4<1/\gamma\). Only finitely many primes divide the numbers \(4^d-1\) with these bounded d, so all such near-optimal dictionaries lie in a finite family. An infimum equal to \(D_t\) must therefore be attained. This is a derived finiteness statement for a specified threshold, not an assumed prime cutoff.

## 2. The exact incidence identity

For \(A\subseteq\mathbb Z/L\mathbb Z\), \(|A|=K>0\), and a class \(c\pmod d\), put

\[
g=\gcd(d,L),\qquad e=d/g,\qquad
K_g(c)=|\{h\in A:h\equiv c\pmod g\}|.
\]

The relative density of this class inside the periodic set generated by A is

\[
\rho_A(c,d)=\frac{K_g(c)}{Ke}.
\tag{3}
\]

Indeed, in a common period \(\operatorname{lcm}(L,d)=Le\), the set generated by A has Ke positions, and each compatible residue contributes exactly one intersection by the elementary CRT. At fixed g, this expression decreases as d increases. For several channels, their union has density at most the sum of the individual densities; no independence assumption is used.

For H the complete incidence maxima are

| \(g\mid105\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\max_cK_g(c)\) | 36 | 23 | 11 | 7 | 6 | 4 | 2 | 1 |

The subset \(H_r=\{h\in H:h\equiv r\pmod3\}\) has sizes 23, 13 and 0 for r = 0, 1 and 2. The exact distributions modulo 5 are

| Subset | mod-5 class 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| \(H_0\) | 6 | 6 | 0 | 6 | 5 |
| \(H_1\) | 5 | 5 | 0 | 0 | 3 |

Their maximum incidences in a mod-7 class are 4 and 3 respectively. Thus the only mod-5 classes attaining the maximum 5 in \(H_1\) are 0 and 1.

The two u parities have equal relative density 1/2 inside H, because its period 105 is odd. A fixed parity together with mod-3 residue r occupies \(|H_r|/72\) of H.

## 3. Uniform channel bounds and their equality rigidity

An active odd prime q has exactly one even zero class modulo \(d_q=\operatorname{ord}_q4\). If there is no zero class, it contributes nothing. The following bounds allow every possible phase.

### 3.1. Without channels 5 and 13

For \(q\notin P\cup\{3,5,11,13\}\), we have \(d_q\ge7\). The complete prime-factor union of \(4^j-1\) for \(1\le j\le6\) is

\[
\{3,5,7,11,13,17,31\}.
\]

For the eight possible gcds \(\gcd(d_q,105)\), equation (3) gives the table

| gcd | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Minimum admissible d | 8 | 9 | 10 | 7 | 15 | 21 | 35 | 105 |
| Density bound in H | \(1/8\) | \(23/108\) | \(11/72\) | \(7/36\) | \(1/6\) | \(1/9\) | \(1/18\) | \(1/36\) |

Consequently these primes cover at most \(23/108\) of H. The exceptional prime 11, of period 5, covers at most \(11/36\). Any t distinct channels avoiding 3, 5 and 13 therefore leave at least

\[
1-\frac{11}{36}-(t-1)\frac{23}{108}
\tag{4}
\]

of H, for \(t\ge1\). This remains valid if fewer channels are present or 11 is absent.

### 3.2. Inside one parity

Parameterize \(u=\varepsilon+2v\). The hole set in v is an affine permutation of H, preserving the incidence maxima. A remaining prime has effective period

\[
e_q=\operatorname{ord}_q16.
\]

For \(q\notin P\cup\{3,5,13\}\), periods 1, 2, 3 and 6 are excluded, since any such prime would divide

\[
2^{24}-1=3^2\cdot5\cdot7\cdot13\cdot17\cdot241.
\]

The minimum periods in the eight gcd columns are now

\[
(4,9,5,7,15,21,35,105),
\]

and the bounds become

\[
\left(\frac14,\frac{23}{108},\frac{11}{36},\frac7{36},
\frac16,\frac19,\frac1{18},\frac1{36}\right).
\tag{5}
\]

Every remaining channel therefore covers at most \(11/36\) of either parity fiber.

**Rigidity of the largest entry.** Equality \(11/36\) in (5) forces \(e_q=5\): the other gcd columns have strictly smaller bounds, and increasing the period strictly decreases the bound in the gcd-5 column. Hence q divides \(16^5-1=2^{20}-1\). Its complete factorization is

\[
2^{20}-1=3\cdot5^2\cdot11\cdot31\cdot41.
\]

Outside \(P\cup\{3,5,13\}\), only q = 11 remains. Removing it, the gcd-5 minimum period increases to at least 10, so every other remaining prime covers at most 1/4 of either parity fiber. In particular, three distinct remaining primes cover at most

\[
\frac{11}{36}+\frac14+\frac14=\frac{29}{36}
\tag{6}
\]

of a parity fiber. The bound in (6) is deliberately sufficient rather than asserted sharp.

### 3.3. Inside a fixed parity and mod-3 fiber

Parameterize \(u=u_0+6v\), with \(u_0\equiv\varepsilon\pmod2\) and \(u_0\equiv r\pmod3\). Removing these two fixed coordinates leaves a set modulo 35 with size 23 for r = 0 and size 13 for r = 1. The effective prime period is

\[
f_q=\operatorname{ord}_q(4^6)=\operatorname{ord}_q(2^{12}).
\]

For \(q\notin P\cup\{3,5,13\}\), we have \(f_q\ge3\), since f = 1 or 2 would again imply \(q\mid2^{24}-1\). Equation (3), over gcds 1, 5, 7 and 35, gives

| Fiber | gcd 1 | gcd 5 | gcd 7 | gcd 35 | Maximum |
|---|---:|---:|---:|---:|---:|
| r = 0 | \(1/3\) | \(6/23\) | \(4/23\) | \(1/23\) | \(1/3\) |
| r = 1 | \(1/3\) | \(5/13\) | \(3/13\) | \(1/13\) | \(5/13\) |

**Rigidity in the r = 1 fiber.** Equality \(5/13\) forces \(f_q=5\), because only the gcd-5 column can attain it, with no extra period multiplier. Thus \(q\mid2^{60}-1\). The complete factorization is

\[
2^{60}-1
=3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41\cdot61
\cdot151\cdot331\cdot1321.
\tag{7}
\]

Outside \(P\cup\{3,5,13\}\), precisely \(11,61,331\) remain, and each has \(\operatorname{ord}_q(2^{12})=5\). Their orders of 4 are 5, 30 and 15. Their intersection with the fixed fiber is a whole mod-5 class. By the exact distribution in Section 2, maximal coverage occurs exactly for classes 0 or 1.

This proves the complete all-prime equality dictionary U. Neither a large-prime cutoff nor an unverified claim about the absence of further factors enters the reduction.

## 4. All budget cases

Measure gaps in this section relative to H. Inactive channels can be removed. At budget t, no equality can waste a channel because the proved optimal gaps strictly decrease from budget 0 through 5.

For t = 0 the gap is 1. At t = 1, prime 5 covers exactly one parity, giving gap 1/2. Prime 13 covers at most \(23/72\) of H, prime 11 at most \(11/36\), and every other eligible prime at most \(23/108\). Thus 5 alone is the unique channel capable of attaining the t = 1 optimum.

For \(t\in\{2,3,4\}\), the cases are exhaustive:

| Active status of 5 and 13 | Lower bound for gap in H |
|---|---:|
| Neither | \(1-11/36-(t-1)23/108\) |
| Exactly one | \(\tfrac12(1-(t-1)11/36)\) |
| Both, same zero parity | \(\tfrac12(1-(t-2)11/36)\) |
| Opposite parity, \(c_{13}\equiv0\pmod3\) | \(\tfrac{13}{72}(1-(t-2)5/13)\) |
| Opposite parity, \(c_{13}\equiv1\pmod3\) | \(\tfrac{23}{72}(1-(t-2)/3)\) |
| Opposite parity, \(c_{13}\equiv2\pmod3\) | \(\tfrac12(1-(t-2)11/36)\) |

The first row is (4). In the second row, examine the parity missed by the sole channel from \(\{5,13\}\) and use (5). In the third row, examine their common missed parity. In the remaining rows, 5 covers one parity completely, and 13 lies in the other parity. If its mod-3 phase is 0, the remaining fiber is \(H_1\); if its phase is 1, the remaining fiber is \(H_0\); if its phase is 2, it hits no old holes in that parity. Section 3 gives the respective bounds.

The minima in these three columns t = 2, 3, 4 are

\[
\frac{13}{72},\qquad\frac8{72},\qquad\frac3{72}.
\tag{8}
\]

For t = 2 or 3, every row except the opposite-parity, mod-3-zero row is strictly larger than its corresponding optimum. At t = 4 the coarse exactly-one row also gives \(3/72\), but (6) strengthens its gap to

\[
\frac12\left(1-\frac{29}{36}\right)=\frac7{72}>\frac3{72}.
\]

Thus at every budget 2–4, equality forces (2). At t = 3 the one remaining channel must attain \(5/13\) in the \(H_1\) fiber. By Section 3.3 this is precisely one prime from U in category 0 or 1. At t = 4 both remaining channels must attain \(5/13\), and their intersections with this fiber must be disjoint: equality in the union bound is necessary. They must therefore be distinct primes from U, occupying categories 0 and 1. Two copies of the same category overlap on the whole category and cannot attain equality.

Conversely, every listed configuration covers exactly the stated number of residues; hence these conditions suffice. Multiplying the relative gaps \(1,1/2,13/72,8/72,3/72\) by the original full-index density \(6/35\) proves (1) through t = 4. Nonnegativity gives the bound at every larger budget, and Section 6 supplies equality already at t = 5.

## 5. Explicit phases, equality patterns and realizability

For fixed \(\varepsilon\), the optimal first two phases are \(c_5=1-\varepsilon\) and \(c_{13}=3\varepsilon\). The phases selecting category r in the remaining fiber satisfy

\[
\begin{array}{lll}
q=11:&c_q\equiv r\pmod5;\\
q=331:&c_q\equiv1\pmod3,&c_q\equiv r\pmod5;\\
q=61:&c_q\equiv\varepsilon\pmod2,&c_q\equiv1\pmod3,\quad c_q\equiv r\pmod5.
\end{array}
\tag{9}
\]

For the three categories used in the optimal chain, these are:

| \(\varepsilon\) | Prime | Category 0 phase | Category 1 phase | Category 4 phase | Modulus |
|---:|---:|---:|---:|---:|---:|
| 0 or 1 | 11 | 0 | 1 | 4 | 5 |
| 0 or 1 | 331 | 10 | 1 | 4 | 15 |
| 0 | 61 | 10 | 16 | 4 | 30 |
| 1 | 61 | 25 | 1 | 19 | 30 |

Only categories 0 and 1 belong to the t = 3 and t = 4 equality classification. Category 4 is included to describe the explicit fifth-step completion; no classification of all five-prime completions is asserted here.

At t = 4, every equality dictionary leaves exactly one of two patterns:

\[
\begin{array}{c|c|c}
\varepsilon&\text{missing }u\pmod{210}&\text{missing }n\pmod{420}\\
\hline
0&64,154,184&128,308,368\\
1&49,79,169&98,158,338.
\end{array}
\tag{10}
\]

Indeed, the only remaining elements of \(H_1\) are \(49,64,79\pmod{105}\), its category 4. Lifting each to the prescribed parity gives (10).

For each listed prime and phase c, the exact root congruences are

\[
a\equiv\pm2^{-c}\pmod q.
\tag{11}
\]

Both signs solve \(a^24^c=1\), and over a prime field these are the only two solutions. The new primes are distinct, outside P and different from 3. Hence the CRT combines (11) independently with the old class and \(a\equiv0\pmod3\). Each allowed sign choice produces an infinite positive arithmetic progression of valid roots. The equality phase-dictionary counts are therefore

\[
2,\quad2,\quad2\cdot3\cdot2=12,\quad2\cdot3\cdot2=12.
\]

The last count selects the parity, the prime assigned to category 0, and a different prime assigned to category 1. Different root signs do not change the squared-root residue trajectory.

## 6. One root attains the whole staircase

Take

\[
a_0=8681796600341899699165924755002845830837950628236344137765453
\]

and the nested new-prime list

\[
(q,c_q)=(5,1),(13,0),(11,0),(61,16),(331,4).
\tag{12}
\]

This root obeys the old congruence and is divisible by 3. Its residues modulo the five primes are respectively

\[
3,\ 1,\ 1,\ 25,\ 269.
\]

For the first t rows in (12), the number of missing u positions in one period of length 210 is

\[
72,\ 36,\ 13,\ 8,\ 3,\ 0.
\]

Each such u contributes one missing even n in a period of length 420, proving simultaneous equality in all six budgets. Since a single root realizes the bounds, the universal sharpness is stronger than separate examples for separate budgets.

All roots in the progression

\[
a=a_0+
121041494945903853943122890515382691774327737794816871699188590\,j,
\qquad j\ge0,
\]

have exactly the same five-channel phase data and the same old observations. This progression therefore supplies infinitely many simultaneous sharp examples. After the fifth prime they have exact additional cover cost 5, by the positive four-channel obstruction. This does not assert an exact total cover cost for this particular compact root.

## 7. Reproducible evidence and scientific boundaries

Run `python verify_staircase.py` beside this file. It creates `staircase_certificate.json` and checks:

- the complete H incidence tables and all rational all-order bounds;
- the complete factorizations of \(2^{20}-1\), \(2^{24}-1\), \(2^{60}-1\), and the small \(4^j-1\) inputs;
- the two rigidity reductions to the prime sets \(\{11\}\) and \(\{11,61,331\}\);
- every budget case, including the strict t = 4 exactly-one case;
- every phase of every equality candidate dictionary after the analytic reduction: 12 phase systems at t = 2, 600 at t = 3, and 8100 at t = 4;
- equality with precisely the classified 2, 12 and 12 phase dictionaries, including both missing-residue patterns;
- the exact CRT root, its progression, and the full simultaneous staircase, with independent modular readouts of all five prefixes.

The fixed source for the old P trajectories is the earlier certificate at commit `e61a43115cf9dcbd0b3d8a746a5ac8086b8ca8fe`, path `research_notes/portable_direct/riesel_mixed_20261119/certificate.json`. The immediately preceding sharp four-channel proof and its full actual native BRC verification are at commit `af9e1a5e49386a28283781876e10742a71991036`, paths `research_notes/portable_direct/riesel_spectrum_20261121/gap/proof.md` and `gap/small_gap_certificate.json`. The native source remains frozen at `b1efc6c805661ed7b476e6e730107da6043176ee`.

The present calculation reuses that unchanged native semantics and verified old predicate. It supplies new arithmetic proofs and observer counts, without claiming a new native execution, formal proof checker result, or independent Review. The all-prime theorem is Sections 2–4; the finite phase enumeration verifies the equality dictionary after those sections prove it exhaustive.

This result explains an exact aspect of residual phase compatibility: the first two optimal channels force a parity and mod-3 fiber; the next two must occupy its two largest mod-5 categories. The resulting density staircase is an observable-specific quotient statement. It does not license replacing the full integer state or its cofactor and joint-gcd information by these few phase categories in other questions, especially the existence or minimum size of a complete cover at a different fixed root.
