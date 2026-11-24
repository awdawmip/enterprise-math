# Two permanent ternary channels: a stronger consecutive-cost construction

Author collaboration for the Riesel residual-composition research, 2026-11-24.
This is a written mathematical extension with exact arithmetic support. It is
not an independent Enterprise Math Review or a formal-proof acceptance.

## 1. Result and inherited setting

The integer state is unchanged:

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1.
\]

This is the existing integer register at a fixed native X6 anchor, with positive
singleton BRC weight and multiplicity one. Prime residues are observations of
that integer; the proof below retains its divisibility and common-factor
relations. The index is the arithmetic update count.

Use the same old root and dictionary as the preceding research:

\[
\begin{aligned}
a_*&=690786768637635218740714348513373826260012289,\\
M&=\prod_{p\in P}p
=1397394912916194098609132326092145093313722687204526281,\\
L&=80754838636615.
\end{aligned}
\]

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

\[
R_1=\{a>0:a\equiv a_*\pmod{6M},\quad
a\equiv12926327728523\pmod L\},
\]

\[
R_2=\{a\in R_1:a\equiv0\pmod{433},\quad
a\equiv38733\pmod{38737}\}.
\]

Here \(\delta_P(a)\) is the minimum number of primes outside P needed in a
complete proper-prime cover of all \(F_n(a), n\ge1\). The minimum total size
without requiring P is \(\tau(a^2)\); an absent finite cover has value infinity.
The old dictionary covers the odd indices; the even terms factor as
\((a2^u-1)(a2^u+1)\). Thus the square coefficients in these fibers already have
the established Riesel property.

For any positive integer N put

\[
B_N=\max\bigl(\{1\}\cup\{\operatorname{ord}_q2:
q\mid N,\ q\text{ odd prime}\}\bigr).
\]

**Theorem.** For \(i=1,2\) define

\[
j_N^{(1)}=\min\{j\ge0:72\,2^j>B_N\},\qquad
j_N^{(2)}=\min\{j\ge1:72\,2^j>B_N\}.
\tag{1}
\]

There exists a residue \(r_N^{(i)}\pmod N\) such that every integer
\(s\ge j_N^{(i)}+7\) is attained by infinitely many positive roots satisfying

\[
a\in R_i,\qquad a\equiv r_N^{(i)}\pmod N,\qquad
\delta_P(a)=s,\qquad\tau(a^2)=20+s.
\tag{2}
\]

Each fixed s contains an arithmetic progression after removing finitely many
initial terms. The observation residue is fixed before s varies. Its full
future trajectory is \(r_N^{(i)2}2^n-1\pmod N\).

Consequently, with the same maximum-prime-order observer metric as before,

\[
\boxed{\Omega_b(R_1)\ge\frac9{16}2^b\quad(b\ge7)},\qquad
\boxed{\Omega_b(R_2)\ge\frac9{16}2^b\quad(b\ge8)}.
\tag{3}
\]

The existing upper bound \(105\,2^b\) still applies. The lower constant in (3)
is \(4/3\) times the preceding \(27/64\) constant and \(32/3\) times the
earlier \(27/512\) constant. No optimality claim is made for these constants.

## 2. A simpler cover of every consecutive size

The fixed supplementary prefix is

\[
(q,d,c)=(5,2,1),(13,6,0),(19,9,4),(73,9,1),
\tag{4}
\]

where the row covers \(u\equiv c\pmod d\), with \(n=2u\).
Its root residues are 3, 1, 6, 37. After P and this prefix, the exact residual
positions are

\[
u=16+18w,\qquad n=32+36w,\qquad
w\in B\pmod{35},
\tag{5}
\]

\[
B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}.
\]

For every \(k\ge0\), take the following \(k+3\) rows in w:

\[
\begin{array}{ll}
w\equiv2^{j-1}\pmod{2^j},&1\le j\le k,\\
w\equiv1\pmod3,&\\
w\equiv2\pmod3,&\\
w\equiv0\pmod{3\,2^k}.&
\end{array}
\tag{6}
\]

The empty dyadic list at k=0 leaves the three residue classes modulo three.

The dyadic rows cover all integers not divisible by \(2^k\). Their complement
is \(w=2^k t\). If that w is 1 or 2 modulo three it is covered by its permanent
ternary row. If it is 0 modulo three, then \(3\mid t\), so the last row covers
it. Thus (6) covers every integer w.

Every row has a private cell in the common period \(G_k=3\,2^k\):

* the j-th dyadic row has private cell \(w_j=3\,2^{j-1}\);
* the permanent row of phase 1 has private cell
  \(2^k\) for even k and \(2^{k+1}\) for odd k;
* the permanent row of phase 2 has the other of these two cells;
* the last row has private cell 0.

For the dyadic cells the exact two-adic valuation selects one dyadic row, their
residue modulo three avoids the permanent rows, and they are nonzero modulo
\(G_k\). The other three cells are multiples of \(2^k\) in three different
classes modulo three. This proves irredundancy for every k.

## 3. A consistent prime realization

Fix the following choices once for the entire sequence:

| Row | Prime and exact base-two order | Chosen root residue |
|---|---|---|
| permanent \(w=1\pmod3\) | \(U=87211\), order 54 | \(2^{-34}\pmod U\) |
| permanent \(w=2\pmod3\) | \(V=279073\), order 108 | \(2^{-52}\pmod V\) |
| dyadic row j | \(D_j\), order \(36\,2^j\) | \(2^{-(16+18\,2^{j-1})}\pmod{D_j}\) |
| last row at size k | \(T_k\), order \(108\,2^k\) | \(2^{-16}\pmod{T_k}\) |

Use \(D_1=38737\), \(D_2=487824887233\), \(T_0=246241\), and
\(T_1=33975937\). These are prime and have the displayed exact orders; the
calculator checks primality by trial division and orders by their complete
prime-divisor tests. The two order-108 primes V and T0 are explicitly distinct.
All remaining required orders exceed six, so the inherited base-two
primitive-prime theorem supplies a prime of each such order. It is the same
existence input as in the preceding constructions, with no new multiplicity
assumption.

The D orders have three-adic valuation two and the T orders have three-adic
valuation three. U has order 54, below all T orders; only V and T0 share an order
and their primes were explicitly distinguished. This makes every dictionary
prime distinct. The old dictionary's largest exact order is 105; the only
smaller new orders, 54 and 72, use the explicit primes U and D1 outside P.

For every ordinary row with modulus m in (6), an exact order \(36m\) and root
\(2^{-(16+18b)}\) gives the even zero class
\(u=16+18b\pmod{18m}\), hence exactly \(w=b\pmod m\) on (5).

U is the sole smaller-order row. Its zeros are

\[
u\equiv34\equiv7\pmod{27}.
\tag{7}
\]

On (5), (7) is exactly \(w\equiv1\pmod3\). U can also hit positions outside
(5); those extra hits do not affect the coverage argument. They will be checked
against the private witnesses rather than discarded by projection. The chosen
root residue uses the literal exponent 34, so its sign is also fixed throughout
the sequence and at every observed prime-power precision.

Let \(S_k\) consist of P, the four prefix primes, the k dyadic primes, U, V,
and T_k. Then \(|S_k|=27+k\).

## 4. Private witnesses in the entire exponent sequence

For the old primes, in the displayed order of P, retain the old private positive
indices

\[
37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111.
\tag{8}
\]

All are odd. Every new tail prime has even base-two order and an even zero
phase, so none hits these witnesses. Among the prefix primes, 5, 13 and 19 have
the same parity exclusion; 73 has zero phase 2 modulo nine, which no index in
(8) has. Their old-prime privacy is preserved.

The four prefix primes retain private u-witnesses 3, 6, 76, 10, respectively,
or exponent indices 6, 12, 152, 20. Each is an old hole and lies in precisely its
assigned prefix class. All ordinary tail rows are confined to \(u=16\pmod{18}\),
which excludes these four witnesses. U's larger zero set (7) also excludes them:

\[
(3,6,76,10)\pmod{27}=(3,6,22,10),\qquad7\text{ is absent}.
\]

For each private w-cell of (6), solve

\[
w\equiv w_i\pmod{G_k},\qquad w\equiv0\pmod{35}.
\tag{9}
\]

CRT applies because \(\gcd(G_k,35)=1\). Choose its nonnegative representative.
Then \(n=32+36w\) is positive and lies in the exact residual set (5), since
\(0\in B\). The prime assigned to that row is its sole divisor from S_k.
This remains true for U because its restriction to (5) is its stated ternary
row. Thus there are \(27+k\) distinct private exponent indices for S_k.

## 5. The changed-order threshold is \(72\,2^k\)

The transition \(S_k\longrightarrow S_{k+1}\) retains every prime except
T_k, and all retained primes have identical literal root exponents. It removes
T_k and adds D_{k+1}, T_{k+1}. Their exact orders are

\[
\begin{array}{c|c}
\text{removed}&108\,2^k\\
\text{new dyadic}&72\,2^k\\
\text{new last}&216\,2^k.
\end{array}
\tag{10}
\]

Every step increases the supplementary size by one. The minimum changed order
is \(72\,2^k\), including k=0. Once this exceeds B_N, no subsequently changed
prime divides N. Hence the intersection of S_k with the observed prime set is
constant for every \(k\ge j_N^{(i)}\), with all its root residues constant.

This improvement comes from preserving both ternary side rows. In the previous
construction one shorter ternary row was repeatedly retired, giving a minimum
changed order of \(54\,2^k\).

## 6. Fixed prime-power observations and exact minima

Choose j as in (1). For every \(q^e\Vert N\), fix the root residue as follows:

| Coordinate | Root modulo \(q^e\) |
|---|---|
| q=2 or q in P | \(a_*\) |
| q in \(S_j\setminus P\) | the literal root residue \(2^{-c_q}\) from the table above or the fixed prefix |
| odd q outside S_j | 0 |

This defines a single residue \(r_N\pmod N\). It remains compatible with every
S_k for \(k\ge j\), by (10). It chooses a compatible root lift; it does not
claim that a phase modulo q already fixes a phase modulo every power of q.

Fix such a k. Let \(n_p\) be the private exponent for each \(p\in S_k\), and
put

\[
D=\operatorname{lcm}_{p\ne p'\in S_k}(2^{|n_p-n_{p'}|}-1),\qquad
E=D\Big/\prod_{p\in S_k}p^{v_p(D)}.
\tag{11}
\]

Impose

\[
a\equiv a_*\pmod{2M},\qquad
a\equiv2^{-c_q}\pmod q\ (q\in S_k\setminus P),\qquad
E\mid a,\qquad a\equiv r_N\pmod N.
\tag{12}
\]

These conditions are compatible prime by prime. E is odd and coprime to every
dictionary prime. An observed dictionary prime has the unchanged compatible
lift specified above. An observed odd prime outside the dictionary was assigned
zero modulo its observed power, which is compatible with any higher or lower
power dividing E. Thus generalized CRT gives a nonempty arithmetic progression.

For completeness, the old forcing factor \(T_{3,1}\) used in previous work can
also be imposed without conflict: none of the supplementary orders divides
210. It is unnecessary for (12), since the R1 restrictions below already
follow from E.

If a prime \(\ell\) divides two private terms, then \(\ell\nmid2a\), and
cancellation gives \(\ell\mid2^{|n_p-n_{p'}|}-1\). Therefore \(\ell\mid D\).
If \(\ell\in S_k\), privacy forbids both divisibilities. Otherwise
\(\ell\mid E\mid a\), contradicting \(F_n(a)=-1\pmod\ell\).
The private terms are pairwise coprime.

Any complete prime cover must therefore use at least \(27+k\) different primes.
The \(7+k\) supplementary private terms also avoid every prime of P, so they
force at least \(7+k\) primes outside P. S_k supplies exactly those two upper
bounds. Once a is large enough that \(2a^2-1>\max S_k\), all covering divisors
are proper, and

\[
\delta_P(a)=7+k,\qquad\tau(a^2)=27+k.
\tag{13}
\]

## 7. The fixed root fibers are preserved

The permanent prefix gives the four active R1 residues. The other five
coordinates of R1 are the inactive primes 11, 61, 331, 37, 109, whose exact
base-two orders are 10, 60, 30, 36, 36. None is in S_k. The old private-index
differences \(63-3=60\) and \(41-5=36\) show that E is divisible by all five.
They are therefore forced to zero in (12), as required.

The same differences imply \(3\mid E\); also \(3\mid a_*\) and
\(3\nmid2M\). Thus \(a\equiv a_*\pmod{2M}\) strengthens to
\(a\equiv a_*\pmod{6M}\). This proves membership of R1 for every k.

For \(k\ge1\), D1=38737 is permanent at u-phase 34, with root residue
\(2^{-34}=38733\pmod{38737}\). The difference \(113-41=72\) in (8)
forces the other order-72 prime 433 into E, since it is absent from S_k.
Thus \(a=0\pmod{433}\), proving membership of R2 for every \(k\ge1\).

At k=0, 38737 is also absent and is forced into E, so this initial member lies
in R1 and not in R2. That explains the different lower bounds on j in (1).

Combining (12) and (13) establishes (2), with the same observation residue for
all the asserted costs and a cofinite arithmetic progression for each cost.

## 8. Observer-order consequence

Suppose a modulus N decides \(\delta_P(a)\le b\) on all of R1 and
\(B_N<72\,2^{b-7}\), with \(b\ge7\). Then \(j_N^{(1)}\le b-7\).
Equation (2) places an exact-cost-b root and an exact-cost-(b+1) root in the
same observed residue. They have opposite predicate values, a contradiction.

The same argument on R2 applies for \(b\ge8\), because then \(b-7\ge1\).
This proves (3). Since identical root residues give identical full trajectories,
the same lower bound applies when the observer is allowed to watch every
future residue value.

## 9. Exact support and dependencies

Run `python verify_permanent_ternary.py` beside this proof. The script checks:

* the inherited old-prime zero classes and private witnesses;
* exact primality and orders for the named seed primes;
* every cell of the complete covers for k=0 through 12 and every displayed
  private witness;
* retained phases and all three changed orders for consecutive values in that
  range;
* two complete numerical exponent periods of length 60,480, with 27 and 28
  private terms, for k=0 and k=1;
* strict threshold boundaries and three higher-prime-power CRT fixtures.

The universal quantifiers are proved in Sections 2–8; the finite calculations
check the explicit inputs and examples. The native state dynamics are reused
unchanged; this script is an exact arithmetic checker, not a new native BRC run.

Primary internal dependencies:

* [v10 finite-observer proof](https://github.com/awdawmip/enterprise-math/blob/f57dd6fd49d5b3f0a12abb3703c76edd6dbd37b5/research_notes/portable_direct/riesel_finite_observers_20261124/finite/proof.md), for the fixed root-family and common-factor framework;
* [v11 consecutive-cover proof](https://github.com/awdawmip/enterprise-math/blob/a88e3e001275269cae93c40d77e6984b1ef2970f/research_notes/portable_direct/riesel_seven_cover_20261124/finite/proof.md), for the immediate preceding 54-order construction;
* [v11 classification entry](https://github.com/awdawmip/enterprise-math/blob/a88e3e001275269cae93c40d77e6984b1ef2970f/research_notes/portable_direct/riesel_seven_cover_20261124/README.md), for the fixed fibers and existing finite-budget upper bound.

The base-two primitive-prime existence input is the unchanged Bang theorem
already credited and scoped in those sources: every requested order here is
greater than six. This extension requires only one prime per new order.
