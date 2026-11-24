# A complete finite cost-gap-one spectrum on the fixed R3 trajectory

Research continuation v15, 2026-11-24, Asia/Hong_Kong. Researcher
`EM-DIRECT-970E1C / TASK_RESEARCH`, Activity `RA-D2EC212845B63844081F9A14`.
This is an author proof with shared-context mathematical checking and exact
integer computation. It does not claim independent project Review or
formal acceptance.

## 1. Main theorem and native integer meaning

Keep the same full integer register at the fixed Heartbeat X6 anchor:

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad
F_n(a)=a^2 2^n-1.
\]

It is the positive singleton BRC action with weight and multiplicity one.
Residues below are observations of that register. The proof of lower
bounds retains the common factors of complete integer terms.

Let P be the old twenty-prime dictionary, and let R3 be the unchanged
fixed 43-prime fiber a=A3 modulo S3, with a positive. Its exact constants
and fixed coordinates are embedded in the checker and in the companion
one-W minimum proof. In particular A3=3 modulo six, so every root is odd
and divisible by three.

**Theorem.** For every integer s>=9 there are infinitely many ordinary
integer roots a in R3 such that

\[
\boxed{\delta_P(a)=s,\qquad\tau(a^2)=s+19.}
\tag{1}
\]

For each fixed s, the construction gives an explicit arithmetic
progression after a finite initial segment. The supplementary cost counts
new primes while P remains available; the total cost allows all primes
to be reselected. Equation (1) is therefore a strict gap of one from
the additive value 20+delta_P.

The earlier exact-total construction gives, for every s>=9, infinitely
many roots in R3 with (delta_P,tau)=(s,s+20). Combining it with (1), the
same fixed 43-channel trajectory has both joint cost values

\[
\boxed{(s,s+19)\quad\text{and}\quad(s,s+20)
\quad\text{for every integer }s\ge9.}
\tag{2}
\]

This statement does not classify all possible pairs of costs on R3.

## 2. The seed and why an attempted ternary refinement fails

The companion one-W minimum result proves that the ordinary root

\[
a_{1W}=A_3+811311504227722S_3
\]

has exact costs (9,28). Its displayed supplementary dictionary is

\[
Q=\{5,13,73,29,43,1429,5419,92737,649657\}.
\]

The old prime 113 can be deleted, leaving a 28-prime complete cover.
Its 28 pairwise-coprime witnesses and complete false eight-budget
predicate yield an infinite fixed-cost (9,28) progression, as proved
in `../one/proof.md`. This supplies s=9 in (1).

We now remove the parent prime 1429. Its zero class is

\[
n=68+84i.
\tag{3}
\]

On that class, the selected prime 73 covers i=2 modulo three. A tempting
refinement adds a permanent i=1 modulo-three channel and a dyadic chain
on i=0 modulo three. It does not preserve the proposed cost: the fixed
but unselected prime 19 hits every i=1 modulo-three position. It also
hits every P-free private term of the old 649657 channel. Thus the
permanent channel and the old 649657 channel can both be replaced,
relative to the existing old/basic cover, by the single prime 19.
Their two P-free witnesses would also necessarily share 19.

This is an actual fixed-phase obstruction. It is removed by the purely
dyadic construction in the next section, which does not add such a
permanent ternary channel.

## 3. Pure dyadic replacement using two different base-order families

For every k>=1 partition all parent indices i into the k+1 classes

\[
\begin{aligned}
D_j &: i\equiv3+2^{j-1}\pmod{2^j},\quad1\le j\le k,\\
T_k &: i\equiv3\pmod{2^k}.
\end{aligned}
\tag{4}
\]

For i not equal to 3 modulo 2^k, its first differing binary position
selects exactly one D_j. All other i belong to T_k. Thus (4) is a
disjoint cover of every integer i.

Choose an ordinary prime p_j with

\[
\operatorname{ord}_{p_j}2=84\cdot2^j
\]

for D_j, and an ordinary prime t_k with

\[
\operatorname{ord}_{t_k}2=28\cdot2^k
\tag{5}
\]

for T_k. Every specified order is greater than six, so the inherited
Bang primitive-prime-divisor theorem supplies such a prime. The precise
input is the existence of an odd prime of exact base-two order d for
every d>6, as stated in Filaseta--Finch--Kozek, Lemma 12 in the cited
JNT draft:
https://www.whittier.edu/sites/default/files/media/academics/math/Kozek_Sierpinski_JNTdraft(2008).pdf.
The least prime having each indicated order is one concrete choice;
the theorem does not require a computational factorization for every k.

These orders are all different. An equality between a D order and the
terminal order would give 3=2^(k-j), which is impossible. Thus the primes
are different without any assumption about two primes having the same
order. On the parent progression (3), the effective orders are

\[
\operatorname{ord}_{p_j}(2^{84})=2^j,
\qquad
\operatorname{ord}_{t_k}(2^{84})=2^k.
\tag{6}
\]

For a row with parent phase b prescribe either root sign

\[
a\equiv\pm2^{-(34+42b)}\pmod q.
\tag{7}
\]

This realizes exactly that row on the parent progression. The full D_j
zero classes are contained in n=68 modulo 84. A terminal prime may also
hit outside that parent class because its base order omits the factor
three. Every such hit still has n=12 modulo 28, hence n=0 modulo four.
If its n residue modulo twelve is eight, it is in the parent class.
The other possibilities are n=0 or 4 modulo twelve. The former is already
covered by the fixed basic prime 13 and the latter by the old prime 7.
Therefore the extra terminal hits preserve the old covering argument.

All new primes are outside the fixed R3 modulus. Its 43 primes have
base-two orders at most 180, with none of orders 56,112,168. The first
two possible terminal orders are 56,112, and the first D order is 168;
all remaining indicated orders exceed 180. The additional five free
seed primes {29,43,5419,92737,649657} have orders {28,14,42,63,63}, also
different from every new order. These are exact order comparisons,
not a comparison of prime magnitudes.

Put

\[
\mathcal B=(P\setminus\{113\})
\cup\{5,13,73,29,43,5419,92737,649657\}.
\]

This is the 27-prime dictionary left after deleting 1429 from the seed.
Keeping its root phases and adding (4)--(7) gives a complete dictionary
of 28+k primes, of which 9+k lie outside P. Consequently

\[
\delta_P(a)\le9+k,\qquad\tau(a^2)\le28+k.
\tag{8}
\]

It remains to establish matching lower bounds while respecting every
fixed R3 prime, including primes not selected in this dictionary.

## 4. Fixed-prime-safe private witness geometry

### 4.1 Twenty-seven old witness positions

Keep the following private positions for the primes of B:

| prime | exponent | prime | exponent |
|---:|---:|---:|---:|
| 5 | 6 | 257 | 87 |
| 7 | 37 | 281 | 233 |
| 13 | 72 | 337 | 773 |
| 17 | 3 | 641 | 207 |
| 29 | 4640 | 673 | 237 |
| 31 | 89 | 1321 | 257 |
| 41 | 5 | 5419 | 2480 |
| 43 | 32 | 14449 | 53 |
| 71 | 293 | 29191 | 593 |
| 73 | 308 | 65537 | 63 |
| 97 | 117 | 92737 | 2912 |
| 127 | 113 | 649657 | 728 |
| 151 | 41 | 6700417 | 111 |
| 241 | 33 | — | — |

The finite base-phase check verifies all the following exact properties:

1. Every position is hit by exactly its assigned prime in B.
2. Every exponent differs from 12 modulo 28. It is therefore missed by
   every future D or T prime, independently of k.
3. Each of the eight outside-P witnesses avoids every P prime.
4. For each selected P prime, its witness is odd and the only fixed
   R3 prime hitting it is that same prime. The witnesses for 5,13,73
   are likewise hit only by their corresponding fixed prime.
5. The witnesses for 29,43,5419,92737 are hit by no fixed R3 prime.
   The witness for 649657 is hit by exactly the fixed prime 19.

In particular the old witnesses all avoid 38737,246241,487824887233,
and no fixed prime is used by two old witnesses. This removes the
fixed-channel conflicts that a naive retention of earlier witnesses
would have introduced.

### 4.2 New witness positions for every level

For a D_j row choose i_j by CRT from

\[
i_j\equiv3+2^{j-1}\pmod{2^j},\qquad i_j\equiv21\pmod{45}.
\tag{9}
\]

For T_k choose u_k with

\[
u_k\equiv3\pmod{2^{\max(k,2)}},\qquad u_k\equiv21\pmod{45}.
\tag{10}
\]

The moduli in each pair are coprime. Take their least nonnegative CRT
representatives and use the exponents 68+84i_j and 68+84u_k. The stronger
modulo-four condition in (10) matters at k=1.

On (3), avoiding P is exactly i=1 or 3 modulo five, and being private
relative to B is additionally i not equal to 2 modulo three. Conditions
(9)--(10) give i=1 modulo five and i=0 modulo three, so all new witnesses
are P-free and missed by B. By the partition (4), each is hit by exactly
its own new prime.

The only remaining active fixed-prime possibilities are:

| fixed prime | hit condition on i |
|---:|---|
| 19 | 1 modulo 3 |
| 38737 | 0 modulo 6 |
| 246241 | 0 modulo 9 |
| 487824887233 | 9 modulo 12 |

The selected prime 73 hits i=2 modulo three; the other selected basic
primes do not hit (3). All inactive fixed primes have a=0 modulo their
prime and never hit any term.

Our i values satisfy i=3 modulo nine, so neither 19 nor 246241 hits a
new witness. D1 is even, while every D_j for j>=2 and the terminal is
odd. Thus 38737 hits precisely the D1 witness. D2 has i=1 modulo four,
and every D_j for j>=3 and the terminal has i=3 modulo four. Among the
new i values, all divisible by three, the prime 487824887233 therefore
hits precisely D2 when k>=2, and none at k=1. This proves for every k
that **each fixed R3 prime hits at most one of all 28+k witnesses**.
It also proves that every selected prime hits exactly its assigned
witness and no other witness.

For illustration the first choices are:

| k | D indices i | terminal i | new exponents |
|---:|---|---:|---|
| 1 | 66 | 111 | 5612, 9392 |
| 2 | 66, 21 | 111 | 5612, 1832, 9392 |
| 3 | 66, 21, 111 | 291 | 5612, 1832, 9392, 24512 |
| 4 | 66, 21, 111, 651 | 291 | 5612, 1832, 9392, 54752, 24512 |

The formulas, rather than this finite table, establish the general
fixed-prime incidence claim.

## 5. Coprimalization preserves all imposed phases

Fix k. Let M0 be the lcm of S3 and all the selected prime moduli. By the
disjointness of the new orders and the seed/free-prime inventories,
CRT gives a residue a0 modulo M0 preserving R3, all 27 old phases,
and all new phases (7). Let n1,...,n_(28+k) be the distinct witness
indices from Section 4, and put

\[
B=\operatorname{lcm}_{i<j}(2^{|n_i-n_j|}-1).
\tag{11}
\]

Remove every prime-power factor of B whose prime divides M0. Denote the
remaining integer by C. This is explicit without factoring B: start
with C=B, and repeatedly divide C by gcd(C,M0) until that gcd is one.
Each nontrivial division strictly decreases C, so it terminates, leaving

\[
\gcd(C,M_0)=1,
\]

and every prime factor of B/C divides M0. Now impose

\[
a\equiv a_0\pmod{M_0},\qquad a\equiv0\pmod C.
\tag{12}
\]

These conditions are compatible and give an arithmetic progression of
ordinary integers. In particular no selected covering phase or fixed
R3 residue is changed by the coprimalization step.

Suppose a prime p divided two witness terms. The exact identity

\[
F_m(a)=2^{m-n}F_n(a)+(2^{m-n}-1)
\]

for m>n would imply p divides B. If p divides C, condition (12) gives
F_n(a)=-1 modulo p, a contradiction. Otherwise p divides M0. Every odd
prime factor of M0 other than three is a fixed or selected prime, and
Section 4 proves it can hit at most one witness. The factor three is
also harmless: every R3 root has a=0 modulo three, so F_n(a)=-1 modulo
three. The factor two never divides the positive-index witness terms.
Thus no such common prime exists.

All 28+k witness terms are consequently pairwise coprime. Each of the
9+k witnesses assigned to an outside-P prime is also P-free. Every
complete dictionary therefore needs at least 28+k primes, and every
supplement to P needs at least 9+k new primes. With (8),

\[
\boxed{\delta_P(a)=9+k,\qquad\tau(a^2)=28+k.}
\tag{13}
\]

Take the positive part of (12) beyond a^2-1>max(selected primes). All
displayed divisors are then proper, and this still leaves infinitely
many roots. This proves (1) for s>=10. The companion cost-nine
progression supplies s=9. Neither lower bound for k>=1 uses a
classification of higher-budget covers or any finite prime-search cap.

## 6. Actual examples for costs ten and eleven

The checker verifies the fixed-prime geometry, the exact small orders,
all full-period covering upper bounds, the saturation construction, and
complete integer gcd certificates for:

| k | D primes | terminal prime | root size | (delta_P,tau) | witnesses | gcd pairs |
|---:|---|---:|---:|---|---:|---:|
| 1 | 3361 | 15790321 | 603889 bits | (10,29) | 29 | 406 |
| 2 | 3361,2017 | 5153 | 639638 bits | (11,30) | 30 | 435 |

Their exact orders are respectively 168,56 in the first case and
168,336,112 in the second. Deterministic trial division certifies these
small new primes. In both cases the complete scalar covering period is
20160, and every position is covered. The largest witness exponent is
9392. All 406 or 435 pairwise gcds are one; the ten or eleven
supplemental witnesses also have gcd one with product(P).

The full roots, collision cofactor C and final progression moduli are
retained in hexadecimal. Every witness term is exactly specified by
that full root and its retained exponent. The script actually constructs
the complete integers F_n(a), performs proper-divisor division, and
computes each pair gcd through the exact equality

\[
\gcd(F_n(a),F_m(a))
=\gcd(F_{\min(n,m)}(a),2^{|n-m|}-1).
\]

The certificate does not duplicate every large F_n as a separate
hexadecimal string; its exact defining root and index retain that
integer without loss. These are exact integer computations, not residue
agreement extrapolated to a gcd claim.

Run:

```sh
python verify_gap_spectrum.py
```

The script uses only Python's standard library and the adjacent fixed
`base_geometry.json`. Its result is `gap_spectrum_certificate.json`.
There is no new native BRC execution claim for these large examples.
The statement for every k is the written proof in Sections 3--5; the
executed examples are k=1,2.

## 7. Dependencies and exact strength

The compact cost-nine seed and its infinite (9,28) progression are the
companion `../one/proof.md` with `one_w_minimum_certificate.json`.
The inherited finite (s,s+20) spectrum on R3 is preserved at
`5cfe4d64429f284232029341c6ba774e2eb6f727:research_notes/portable_direct/riesel_eight_spectrum_20261124`
and strengthened on R4 in
`9b3680ea1c07b1364af5464a3469313ee616d408:research_notes/portable_direct/riesel_nine_frontier_20261124/spectrum/proof.md`.
The latter already suffices for the second half of (2), since R4 is a
subset of R3 and s>=9 here.

The new theorem establishes two cofinal families of joint exact finite
costs. It does not assert that these are the only possible pairs, that
one ordinary root has infinite cost, or that its large constructed
examples minimize root size at their budgets.
