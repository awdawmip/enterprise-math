# The complete thirteen-coordinate nine-budget observer on R4

Research continuation, 2026-11-24. Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. Author derivation with shared-context
collaborative mathematical checking. This is not an independent project
Review, formal-proof acceptance, or a new native BRC execution.

## 1. Original state, fixed fiber and exact result

The original object remains the full typed integer register at the fixed
Heartbeat X6 anchor, with positive singleton BRC weight and multiplicity one:

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1.
\]

The residues below observe this integer. The joint covering and common-factor
relations are retained. Let P be the inherited twenty-prime dictionary,
\(\delta_P(a)\) its supplementary proper-prime covering cost, and
\(\tau(a^2)\) the unrestricted total covering cost.

The historical R3 family fixes 43 prime coordinates. Its complete cost-eight
observer, proved at science commit
`e78c84e2516caff59d206123bdc5e348e9733a6a`, consists of 31 additional primes
with product \(T_8\). Define the same fixed fiber as in the new spectrum
construction:

\[
R_4=\{a\in R_3:a\equiv0\pmod{T_8}\}
=\{A_4+S_4j:j\ge0\},\qquad S_4=S_3T_8.
\tag{1}
\]

It has 74 fixed prime observations, and the complete eight-budget predicate
is false throughout it. Therefore \(\delta_P(a)\ge9\) on R4.

Define the following three disjoint sets of free prime coordinates:

\[
\begin{aligned}
\mathcal G={}&\{92737,649657,77158673929,40388473189,118750098349\},\\
\mathcal R={}&\{209924353,4261383649,24929060818265360451708193\},\\
\mathcal H={}&\{4278255361,394783681,46908728641,8369281,\\
&\hspace{16mm}750016890283777055704738227247474485366338380663681\}.
\end{aligned}
\tag{2}
\]

Let

\[
M_9=\prod_{q\in\mathcal G\cup\mathcal R\cup\mathcal H}q.
\tag{3}
\]

Every prime in (2) is coprime to \(S_4\). Their primality, orders, complete
inventory and the tail classification are certified by the companion files.

**Complete observer theorem.** For every positive integer N, each of the
following is equivalent to \(M_9\mid N\):

* the root residue \([a]_N\) decides \(\delta_P(a)\le9\) throughout R4;
* the complete future residue trajectory \(([F_n(a)]_N)_{n\ge1}\) decides
  that predicate throughout R4.

Every one of the thirteen coordinates is essential. Every necessity
obstruction can be witnessed by two ordinary positive roots of finite exact
costs nine and ten. In the maximum observed base-two prime-order metric,

\[
\boxed{\Omega_9(R_4)=\widehat\Omega_9(R_4)=720.}
\tag{4}
\]

Consequently, for each \(i=1,2,3\),

\[
\Omega_9(R_i)\ge720,\qquad\widehat\Omega_9(R_i)\ge720.
\tag{5}
\]

In particular the preceding exact eight-budget result now gives

\[
\boxed{\Omega_8(R_3)=420<720\le\Omega_9(R_3).}
\tag{6}
\]

Equality for the nine-budget observer on all of R3 is not asserted. The
classification used here is on the particular fixed R4 fiber.

## 2. Why every nine-prime supplement on R4 contains Q0

Put \(Q_0=\{5,13,19,73\}\). The companion basic-pair theorem proves that
every complete supplement of size at most nine on R1 contains 5 and 13,
hence the same holds on R4. Since no supplement of size at most eight exists
on R4, every nine-prime supplement there is inclusion-minimal.

The companion complete one-W theorem, with \(W=\{19,73\}\), says that an
inclusion-minimal supplement of size at most nine on R3 containing exactly
one W prime must contain all four primes \(29,43,1429,5419\). All four are
zero coordinates on R4, so that case is impossible.

For completeness, the branch omitting both W primes can be excluded by an
all-order bound, without classifying nine-covers. After P,5,13 the residual
exponents are

\[
n=8+12v,\qquad
v\in A=\{1,2,10,11,12,16,17,22,25,26,30,31,32\}\pmod{35}.
\tag{7}
\]

The fibers v=0 and v=1 modulo three must both be covered. Normalize the
residual A-mass of each fiber to one, so their required total is two. At most
seven supplementary channels remain.

For a prime q put \(f=\operatorname{ord}_q(2^{12})\). If 3 does not divide f,
the same channel can meet both fibers. Its effective period on either one
is f, and the affine coordinate change preserves the incidence maxima for
the gcd columns 1,5,7,35, namely 13,5,3,1.

The complete f=7 inventory is inactive on R4; it consists of the four primes
just mentioned after removing old primes. The f=8 inventory has base-two
orders 32 and 96, giving old 65537 and the now-inactive 193,22253377. The
f=10 inventory has base-two orders 40 and 120, giving the now-inactive
61681,4562284561. Smaller eligible periods are old, basic or inactive.
The remaining sufficient bounds per fiber are therefore:

| gcd(f,35) | Sufficient lower f | Relative capacity |
|---:|---:|---:|
| 1 | 11 | 1/11 |
| 5 | 20 | 5/52 |
| 7 | 14 | 3/26 |
| 35 | 35 | 1/13 |

Each is at most 3/26. The combined contribution to the two fibers is at most
3/13. Some remaining candidates are also inactive on R4; allowing them only
weakens the upper bound. No independence of the two induced phases is used.

If 3 divides f, the channel can hit at most one of the two fibers. Its period
there is \(h=f/3=\operatorname{ord}_q(2^{36})\). The fixed R3 small-order
inventory, after omitting both W primes, gives h at least six on these two
fibers: the other fixed active small-order channels lie in v=2 modulo three,
and every useful h=5 channel is inactive. The same four gcd columns give
bounds

\[
1/6,\qquad5/26,\qquad3/13,\qquad1/13,
\]

all at most 3/13. The other fiber receives zero from this channel.

Thus all seven channels together have combined mass at most
\(7(3/13)=21/13<2\), which cannot cover both fibers. This also gives a
sufficient full-exponent gap of at least

\[
\frac{13}{12\cdot3\cdot35}\left(2-\frac{21}{13}\right)
=\frac1{252}.
\]

Both excluded cases are impossible, so

\[
\boxed{Q_0\subseteq Q\quad
\text{for every complete }Q\text{ of size at most nine on }R_4.}
\tag{8}
\]

This forces four fixed primes, not all seven fixed active supplementary
primes. The distinction is essential for the remaining classification.

## 3. The complete cost-nine predicate in thirteen coordinates

After P and Q0, the residual coordinate is

\[
n=32+36w,\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{9}
\]

Its occupied classes modulo seven are
\(\mathcal B_7=\{0,1,2,3,5\}\). For a listed prime q and phase b define
the two-element root category

\[
\mathcal E_{q,b}
=\{2^{-(16+18b)},-2^{-(16+18b)}\}\pmod q.
\tag{10}
\]

Define the following predicates:

\[
\begin{aligned}
J_G(a)&:\quad
\forall b\in\{0,1,2,3,5\}\ \exists q\in\mathcal G:
a\bmod q\in\mathcal E_{q,b},\\
J_R(a)&:\quad
\forall b\in\{0,8\}\ \exists q\in\mathcal R:
a\bmod q\in\mathcal E_{q,b},\\
J_H(a)&:\quad
\forall b\in\{0,8,16\}\ \exists q\in\mathcal H:
a\bmod q\in\mathcal E_{q,b}.
\end{aligned}
\tag{11}
\]

The effective w-periods in these three groups are respectively 7,12,20.
At each prime the required phase categories are disjoint: equality of their
squared residues would give \(2^{36(b-b')}=1\pmod q\), which forces equality
of the corresponding phases modulo that effective period. Hence different
required phases automatically use different primes.

The companion complete five-tail classification, combined with (8), gives

\[
\boxed{\delta_P(a)=9\iff\delta_P(a)\le9
\iff J_G(a)\lor J_R(a)\lor J_H(a),\qquad a\in R_4.}
\tag{12}
\]

The dictionary supporting JG is Q0 plus all five G primes. The dictionary
supporting JR is Q0, the three fixed active tail primes
\(38737,246241,487824887233\), and the two R primes supplying phases 0 and 8.
The dictionary supporting JH is Q0, fixed 38737 and 487824887233, and three
H primes supplying phases 0,8,16.

The full dictionary classification also contains a fourth type: Q0, fixed
38737 and 487824887233, and all three R primes at phases 0,4,8 modulo twelve.
Every root of that type already satisfies JR because the two required phases
0 and 8 are present. Thus it contributes no fourth root predicate to (12).

The four dictionary types have 192 phase descriptions and 4392 signed CRT
descriptions. The three-predicate normal form retains 186 phase descriptions
and 4344 signed descriptions before overlaps are removed. Neither number is
a count of disjoint root residue classes. Exact density must count the union
in (12), including within-family and between-family overlaps.

## 4. A common ten-cover for all essential-coordinate counterexamples

Choose any one prime \(p\in\mathcal R\) and assign it w-phase eight modulo
twelve. Let

\[
X=68016300334849,
\]

```text
C = 7311824282729722035859309520826138827918372038863677678267962656996811009
```

The spectrum proof establishes the exact product
\(XC=2^{288}-2^{144}+1\), \(\gcd(X,C)=1\), primality of X, and the fact
that every prime divisor of C has exact base-two order 864. Fix the ordinary
prime \(\ell\) to be the least prime divisor of C. Then X and \(\ell\)
are distinct order-864 primes and lie outside all fixed R4 and observer
coordinates.

Impose the three root conditions

\[
a\equiv2^{-160}\pmod p,\qquad
a\equiv2^{-232}\pmod X,\qquad
a\equiv2^{-16}\pmod\ell.
\tag{13}
\]

On w, these give the phases 8 modulo twelve, 12 modulo twenty-four, and zero
modulo twenty-four, respectively. The seven fixed active supplementary primes
Q0,38737,246241,487824887233 leave just w=0,8 modulo twelve. The first new
prime p covers the phase-eight class; X and \(\ell\) partition the
phase-zero class into its two lifts modulo twenty-four.

Thus (13) gives a complete ten-prime supplement:

\[
Q_0\cup\{38737,246241,487824887233,p,X,\ell\}.
\tag{14}
\]

Every sufficiently large positive root satisfying those phases has cost at
most ten. No primality assertion for C is used: only one actual prime divisor
\(\ell\) is counted in (14). For numerical CRT certificates, imposing the
stronger last condition \(a\equiv2^{-16}\pmod C\) supplies (13) and avoids
the need to factor C.

## 5. Every one of the thirteen coordinates is essential

All assignments below preserve R4. Every unmentioned observer coordinate is
set to zero, and (13) is imposed in both members of a pair. The prime p in
(13) may be chosen separately for each pair.

**A target q in G.** Assign the five G coordinates bijectively to the five
phases \(0,1,2,3,5\), with q supplying one required phase. Set all H
coordinates to zero. Choose any \(p\in\mathcal R\) at phase eight and
set the other two R coordinates to zero. Then JG is true, while JR and JH
are false. Changing only the root residue at q to zero destroys JG. Four
remaining G coordinates cannot supply all five distinct required categories.

**A target q in H.** Use two different companion H coordinates for phases
zero and eight, and q for phase sixteen. Set the other H coordinates and all
G coordinates to zero. Again choose just one R coordinate p at phase eight,
so JR is false. Changing q to zero destroys JH, and all three predicates then
fail.

**A target q in R.** Choose \(p\in\mathcal R\setminus\{q\}\), give p
phase eight and q phase zero, and set the third R coordinate and every G and
H coordinate to zero. JR is true. Changing q to zero makes it false, and the
other two predicates remain false.

Every true assignment has exact supplementary cost nine by (12). Every false
assignment has cost greater than nine by the complete classification, and
has cost at most ten by (14). Therefore it has exact cost ten. These are
comparisons between two ordinary finite-cost integer roots, not conditional
claims about a formal residue vector or an unknown infinite cost.

All assignments are compatible by CRT: the thirteen observer primes are
mutually distinct and coprime to \(S_4X\ell\), and p already receives the
same phase in (11) and (13). Retaining either sign in a category is possible;
the constructive argument can choose the literal positive inverse-power
residue throughout.

## 6. Arbitrary finite moduli, including arbitrary prime powers

If \(M_9\mid N\), the residue \([a]_N\) supplies every coordinate of
(11), so it decides the full budget predicate by (12).

Conversely, suppose that a prime \(q\mid M_9\) does not divide N. Take the
true assignment from Section 5 and a sufficiently large positive CRT root
\(a_+\in R_4\). Define

\[
K=\operatorname{lcm}(S_4,N,M_9/q,X\ell).
\tag{15}
\]

Since q divides none of these factors, \(\gcd(K,q)=1\). CRT therefore gives
arbitrarily large positive ordinary roots \(a_-\) satisfying

\[
a_-\equiv a_+\pmod K,\qquad a_-\equiv0\pmod q.
\tag{16}
\]

They preserve every other observer coordinate and all three conditions (13),
and switch exactly the target coordinate from true to false in Section 5.
Thus

\[
\delta_P(a_+)=9,\qquad\delta_P(a_-)=10,
\qquad a_+\equiv a_-\pmod N.
\tag{17}
\]

This disproves sufficiency of N. Any finite prime-power precision at other
coordinates can be included in the lcm in (15); it cannot replace the missing
prime coordinate q. The construction also works with C in place of
\(\ell\) in (15), since every prime factor of C has order 864 and is
therefore different from q.

Equal root residues imply equal entire future trajectories, so (17) proves
necessity for that stronger observation as well. For sufficiency, \(M_9\)
is odd, and the observed first term recovers

\[
a^2\equiv2^{-1}(F_1(a)+1)\pmod{M_9}.
\tag{18}
\]

Every root category in (10) is a sign pair, and is equivalently the square
condition \(a^2\equiv2^{-(32+36b)}\pmod q\). Hence the entire predicate
(12) is determined by that square. This proves the observer theorem with
the same exact divisor condition in both versions.

## 7. The sharp maximum order and the role of the other fixed fibers

The exact base-two orders, in the order listed in (2), are:

| Group | Orders | Maximum |
|---|---|---:|
| G | 63,63,126,252,252 | 252 |
| R | 432,432,432 | 432 |
| H | 80,240,240,720,720 | 720 |

Every sufficient modulus includes every prime in (2), including the two
order-720 primes. Conversely \(N=M_9\) is sufficient and has maximum order
720. This proves (4). An observation sufficient throughout any of R3,R2,R1
must be sufficient on its subfamily R4, proving (5) and (6).

The coordinate count is thirteen additional prime coordinates, or 87 when
the 74 fixed R4 coordinates are also counted. A single composite-modulus
observation can package those thirteen coordinates. The least positive
sufficient additional modulus is \(M_9\). The least period of the predicate
in the progression parameter j is also \(M_9\), because \(S_4\) is
invertible modulo it and every prime coordinate is essential. A root
translation preserving the R4 progression has least positive period
\(S_4M_9\). These are different observer-cost notions and are not identified
with the maximum-prime-order metric.

The arbitrary-finite-observation spectrum theorem remains valid on exactly
this same R4 fiber. Its bound \(\Omega_9\ge432\) is now sharpened to the
exact value 720 by the full classification and coordinate necessity. Its
unbounded finite spectrum and its \((9/16)2^b\) lower bound for b at least
ten are unaffected. None of these results alone classifies every nine-cover
on the larger R3 family.

## 8. Evidence and dependencies

The complete basic-pair and one-W results come from this batch's
`nine_prefix_v14/proof.md`; the two-fiber exclusion in Section 2 is a direct
all-order proof. The complete five-tail classification on R4 is in the
companion `tail_proof.md`. Its exhaustive order inventories and deterministic
prime certificates support exactly the sets in (2). All-prime completeness
rests on those written arguments, not on a prime-size search.

The special order-864 construction and the common ten-cover are also proved
in `nine_observer_v14/proof.md`, with the exact product, small-prime Lucas
certificates and two actually evaluated coprimalized examples in
`nine_spectrum_certificate.json`. The present coordinate witnesses need no
extra coprimalization: the complete nine-budget predicate gives the lower
bound for each false member, and (14) gives its matching upper bound.

The accompanying classifier calculation records the exact frequency,
descriptions, minimum CRT starts and concrete single-coordinate root pairs.
The arbitrary-N and full-future statements are the proofs in Sections 5–7.
Those results remain valid independently of the choice of compact numerical
representatives for the witness pairs.
