# A fixed 74-prime observation with every exact finite cost from nine onward

Research continuation, 2026-11-24. Researcher `EM-DIRECT-970E1C`, Activity
`RA-D2EC212845B63844081F9A14`. Author proof, shared-context collaborative
checking, and exact scalar arithmetic. No independent project Review,
formal-proof acceptance, or new native BRC execution is asserted here.

## 1. Native state and the new fixed fiber

Retain the full typed integer register at the fixed Heartbeat X6 anchor,
with positive singleton BRC weight and multiplicity one:

\[
x_0=a^2-1,\qquad x_{n+1}=2x_n+1,\qquad F_n(a)=a^2 2^n-1.
\]

The exponent is the update count. Residue channels observe the same original
integer and its joint divisor relations. Let P be the inherited twenty-prime
dictionary, \(\delta_P(a)\) the minimum number of supplementary primes in a
complete proper-prime cover, and \(\tau(a^2)\) the unrestricted total minimum.
The convention infinity means that no finite cover exists.

Use exactly the historical R3 progression \(a=A_3+S_3j\), \(j\ge0\), of the
[complete cost-eight source](https://github.com/awdawmip/enterprise-math/blob/e78c84e2516caff59d206123bdc5e348e9733a6a/research_notes/portable_direct/riesel_eight_classification_20261124/observer/proof.md).
Its complete cost-eight predicate depends on 31 free primes, whose product
was denoted \(T_8\). Define

\[
\boxed{R_4=\{a\in R_3:a\equiv0\pmod{T_8}\}.}
\tag{1}
\]

Thus all 43 historical prime coordinates are preserved and all 31 new
cost-eight coordinates are made inactive. This is one fixed 74-prime root
trajectory, with positive progression \(a=A_4+S_4j\), where

\[
S_4=S_3T_8,\qquad
A_4=A_3+S_3\bigl((-A_3)S_3^{-1}\bmod T_8\bigr).
\tag{2}
\]

Both integers have 354 decimal digits; their complete values and every fixed
prime residue are in the accompanying certificate. Since every alternative of
the complete eight-cover predicate requires at least one of these now-zero
coordinates,

\[
\delta_P(a)\ge9\qquad(a\in R_4).
\tag{3}
\]

This implication uses the complete all-prime classification, not a truncated
prime search. The square coefficients remain Riesel by the inherited odd-index
prime cover and the even-index factorization.

**Finite spectrum theorem.**

\[
\boxed{\forall s\ge9\quad\exists^\infty a\in R_4:
\delta_P(a)=s,\qquad\tau(a^2)=20+s.}
\tag{4}
\]

For every s the constructed roots include an arithmetic progression after
deleting finitely many initial terms. Consequently the finite cost spectrum
of this particular 74-prime observation is exactly \(9,10,11,\ldots\).
No individual root with infinite cost is claimed.

## 2. Two distinct primes of order 864, without a multiplicity assumption

The first refinement needs two distinct prime channels of the same order.
The usual Bang theorem supplies only one and cannot by itself justify this
step. Use the explicit integer identity

\[
2^{288}-2^{144}+1=X C,
\qquad X=68016300334849,
\tag{5}
\]

```text
C = 7311824282729722035859309520826138827918372038863677678267962656996811009
```

The checker verifies the product, \(\gcd(X,C)=1\), and \(C>1\), and gives a
complete recursive n-minus-one primality certificate for X. Its exact base-two
order is 864. The small factor in (5) is also listed in the primary
[Cunningham table, 2-plus entry 432](https://homes.cerias.purdue.edu/~ssw/cun/pmain1126.txt).
The construction does **not** assume that C is prime.

In fact every prime divisor p of the left side of (5) has exact order 864.
To see this, put \(x=2^{144}\pmod p\). The identity
\((x+1)(x^2-x+1)=x^3+1\) gives \(2^{432}=-1\pmod p\). Also p is neither
2 nor 3, since the left side of (5) is odd and is 1 modulo three. Thus its
order d divides 864 and does not divide 432; the possibilities are
\(32,96,288,864\). For any of the first three, \(x^2=1\), and
\(x^2-x+1=0\) forces \(x=2\), so \(p\mid3\), a contradiction.

Fix once and for all

\[
T_3=\text{the least prime divisor of }C.
\tag{6}
\]

Then \(\operatorname{ord}_{T_3}2=864\) and \(T_3\ne X\). This is a fully
specified ordinary prime; no factorization of C or primality claim for C is
needed. Two certified smaller seed primes are

\[
Q=4261383649,\qquad T_2=209924353,
\qquad \operatorname{ord}_{Q}2=\operatorname{ord}_{T_2}2=432.
\tag{7}
\]

The checker supplies full recursive n-minus-one certificates and exact-order
checks for (7) as well.

## 3. A cover of each consecutive size preserving all fixed observations

After P and the four permanent primes \(5,13,19,73\), the residual exponents
are

\[
n=32+36w,\qquad
w\in B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}\pmod{35}.
\tag{8}
\]

Three further active fixed R3 channels have the rows

\[
D_1=38737:\ w=1\pmod2,\qquad
D_2=487824887233:\ w=2\pmod4,\qquad
R=246241:\ w=1\pmod3.
\tag{9}
\]

Keep Q from (7) permanently at \(w=8\pmod{12}\). For k=2 the whole tail is

\[
(m,b)=(2,1),(4,2),(3,1),(12,8),(12,0),
\tag{10}
\]

using \(D_1,D_2,R,Q,T_2\) in that order. It covers every integer w, hence
the residual set (8). Its five tail primes and the four-prefix primes give
supplementary size nine.

For each \(k\ge3\), use instead the following \(k+3\) tail rows:

| Row | w class | Exact base-two order |
|---|---|---:|
| D1 | 1 modulo 2 | 72 |
| D2 | 2 modulo 4 | 144 |
| R | 1 modulo 3 | 108 |
| Q | 8 modulo 12 | 432 |
| X | 12 modulo 24 | 864 |
| Dj, for 4 through k | \(2^{j-1}\) modulo \(2^j\) | \(36\,2^j\) |
| Tk | 0 modulo \(3\,2^k\) | \(108\,2^k\) |

The Dj range is empty at k=3, and T3 is exactly the prime in (6). For j at
least four choose Dj of order \(36\,2^j\), and for k at least four choose
Tk of order \(108\,2^k\), once for the entire sequence. Bang's primitive-prime
theorem supplies one prime at every such order, all of which exceed six.
No further repeated-order assumption is used. The Dj orders have three-adic
valuation two; the Tk orders have three-adic valuation three. Different
orders, (5), and (7) ensure that all primes in each dictionary are distinct.

To prove coverage, first avoid D1 and D2; then \(4\mid w\). On this
progression R covers \(w=1\pmod3\), and Q covers \(w=2\pmod3\).
The remaining integers are exactly \(w=0\pmod{12}\). Among those, X covers
the integers of two-adic valuation two, Dj covers valuation j minus one for
\(4\le j\le k\), and Tk covers all remaining multiples of \(3\,2^k\).
This proves coverage for every k, not only the checked initial values.

For every row \(w=b\pmod m\), assign the literal root residue

\[
a\equiv2^{-(16+18b)}\pmod q,
\qquad \operatorname{ord}_q2=36m.
\tag{11}
\]

Its zeros in the full exponent sequence are precisely
\(n\equiv32+36b\pmod{36m}\). Thus each new tail channel is confined to
the even progression \(n=32\pmod{36}\). This retains information outside
the w projection when proving privacy below.

Let \(\mathcal S_k\) consist of P, the four-prefix primes, and the tail
above. Then

\[
|\mathcal S_k|=27+k,\qquad
|\mathcal S_k\setminus P|=7+k,\qquad k\ge2.
\tag{12}
\]

Every new prime beyond the seven active fixed supplementary primes has order
at least 432. Every newly inactive observer prime in R4 has order at most 420;
the remaining fixed R3 primes also have order below 432. Consequently all new
prime choices are coprime to \(S_4\). Every retained fixed prime in (9) has
exactly its historical root residue, including the literal choices in (11).
There is no change to the original 74 observations.

## 4. Private positions in the full integer sequence

Keep the twenty inherited odd private exponents, in the displayed P order,

\[
37,3,89,5,293,117,413,113,41,33,87,233,773,207,237,257,53,593,63,111.
\tag{13}
\]

Every tail channel has even order and even zero phase, and hence misses all
of them. The fixed four-prefix channels retain the old privacy checks.

The four prefix primes keep private exponents

\[
5:6,\qquad13:12,\qquad19:152,\qquad73:20.
\tag{14}
\]

Each is an old hole and belongs to exactly its assigned prefix row. None is
32 modulo 36, so all tail rows miss them. The calculator verifies (13) and
(14) directly against the full old-prime and prefix phases.

The following w values are private for their permanent tail rows whenever
the rows are present:

| Row | Private w | Exponent \(32+36w\) |
|---|---:|---:|
| D1 | 3 | 140 |
| D2 | 30 | 1112 |
| R | 28 | 1040 |
| Q | 68 | 2480 |
| X | 108 | 3920 |
| Tk | 0 | 32 |

All six w values belong to B modulo 35. The D1 and D2 points have valuations
zero and one. The R, Q and X points have valuation two and respective residues
one, two and zero modulo three; their direct residues distinguish all the
fixed classes. Every Dj with j at least four misses these points. The point
zero belongs only to Tk.

For a Dj row with j at least four, choose any nonnegative solution of

\[
w\equiv3\,2^{j-1}\pmod{3\,2^j},\qquad w\equiv0\pmod{35}.
\tag{15}
\]

CRT applies because the two moduli are coprime. The point has exact two-adic
valuation j minus one and is divisible by three. It avoids R and Q, has
valuation greater than that of X's class, and avoids every other dyadic row
and Tk. The resulting exponent lies in (8) and is private for Dj. For shorter
numerical witnesses the checker permits any member of B modulo 35 in (15);
this does not alter the argument.

Thus every \(\mathcal S_k\) has \(27+k\) different full-sequence private
terms. This is only irredundancy so far. The next step proves the global
minimum among all possible prime dictionaries.

## 5. Compatible coprimalization proves both exact minima

Fix k and all its prime choices. Set

\[
K_k=S_4\prod_{q\in\mathcal S_k,\ q\nmid S_4}q.
\]

The R4 constraints and (11) fix a nonempty residue class
\(a\equiv c_k\pmod{K_k}\). For the private indices \(n_i\) above, set

\[
D_k=\mathop{\operatorname{lcm}}_{i<j}
(2^{|n_i-n_j|}-1),\qquad
E_k=D_k\Big/\prod_{p\mid K_k}p^{v_p(D_k)}.
\tag{16}
\]

Then \(\gcd(E_k,K_k)=1\), so

\[
a\equiv c_k\pmod{K_k},\qquad a\equiv0\pmod{E_k}
\tag{17}
\]

has infinitely many positive ordinary integer solutions.

If a prime \(\ell\) divides two different private terms, then
\(\ell\nmid2a\), and cancellation implies
\(\ell\mid2^{|n_i-n_j|}-1\). Thus \(\ell\mid D_k\). If \(\ell\nmid K_k\),
then \(\ell\mid E_k\mid a\), which makes every term equal to minus one
modulo \(\ell\), a contradiction. If \(\ell\mid K_k\), it is either a
selected dictionary prime, an inactive fixed prime, or 2 or 3. The selected
prime hits just its own private term; the inactive fixed prime divides a and
hits none; 2 and 3 hit none. Again simultaneous divisibility is impossible.

The private terms are therefore pairwise coprime. Any complete prime cover
requires at least \(27+k\) primes to meet them, and the \(7+k\) supplementary
private terms avoid P, forcing that many supplementary primes. The constructed
dictionary supplies both upper bounds. For all sufficiently large roots in
(17), all selected factors are proper, and

\[
\boxed{\delta_P(a)=7+k,\qquad\tau(a^2)=27+k.}
\tag{18}
\]

Combining k at least two with (3) proves the exact finite spectrum (4).
Every active fixed R4 prime is selected here. Hence there is no unselected
active observer that could obstruct (17); the formerly problematic fixed
phase at 487824887233 is now permanently included.

## 6. One additional finite observation still supports every sufficiently large cost

For any positive integer N define

\[
B_N=\max\bigl(\{1\}\cup\{\operatorname{ord}_q2:
q\mid N,\ q\text{ odd prime}\}\bigr),
\]

and

\[
L_k=\begin{cases}432,&k=2,\\72\,2^k,&k\ge3,\end{cases}
\qquad j_N=\min\{k\ge2:L_k>B_N\}.
\tag{19}
\]

**Finite-observation theorem on the fixed R4 fiber.** There exists a residue
\(r_N\pmod N\) such that

\[
\boxed{\forall s\ge j_N+7\quad\exists^\infty a\in R_4:
a\equiv r_N\pmod N,\quad
\delta_P(a)=s,\quad\tau(a^2)=20+s.}
\tag{20}
\]

The observation is fixed before s varies. Arbitrarily large but finite prime
powers are allowed in N.

The first transition, from k=2 to k=3, retires T2 of order 432 and introduces
X and T3, both of order 864. For every k at least three, the transition
retires Tk and introduces \(D_{k+1},T_{k+1}\), with changed orders

\[
108\,2^k,\qquad72\,2^k,\qquad216\,2^k.
\tag{21}
\]

Each step increases the supplementary size by one. All retained primes retain
the same literal root exponent in (11). The minimum changed order is exactly
\(L_k\); these thresholds are strictly increasing. Therefore after index
\(j_N\), no added or retired prime divides N.

For each prime power \(q^e\Vert N\), choose the observation lift as follows:

| Coordinate | Chosen root residue modulo \(q^e\) |
|---|---|
| q divides S4 | A4 |
| q is a new member of \(\mathcal S_{j_N}\) | the literal inverse power in (11) |
| all remaining q | 0 |

The first case includes 2 and 3, and all historical fixed coordinates. The
second case is stable for every later k. The third case never becomes a new
dictionary prime at a later k, by (21). These choices define one residue
\(r_N\pmod N\), not merely a selection of zero/nonzero patterns.

Now add \(a\equiv r_N\pmod N\) to (17). At a prime dividing \(K_k\), the
specified lift agrees with the fixed root residue and \(E_k\) has no such
prime factor. At any prime dividing \(E_k\) outside \(K_k\), the observed
lift, if present, is zero, which is compatible with \(E_k\mid a\) at every
relative prime-power precision. Generalized CRT therefore gives an infinite
progression. The coprimalization proof remains unchanged and proves (20).

Thus both the complete root observation and all future residue values are
fixed:

\[
F_n(a)\equiv r_N^2 2^n-1\pmod N\qquad(n\ge0).
\tag{22}
\]

For orientation, \(B_N\le431\) permits all costs from nine; bounds
432 through 575 permit all costs from ten; bounds 576 through 1151 permit all
costs from eleven. These are sufficient construction thresholds, not claimed
optimal thresholds for each particular N.

## 7. A strict increase beyond the complete eight-budget observer

Let \(\Omega_b(R_i)\) denote the least maximum observed prime order among
finite modulus observations deciding \(\delta_P\le b\) throughout the
specified fiber. If \(B_N<L_{b-7}\), then (20) supplies exact-cost-b and
exact-cost-(b+1) roots with identical observations. Hence for R4,

\[
\boxed{\Omega_9(R_4)\ge432,\qquad
\Omega_b(R_4)\ge\frac9{16}\,2^b\quad(b\ge10).}
\tag{23}
\]

Every observation sufficient on R3, R2 or R1 is also sufficient on its
subfamily R4. Thus both inequalities in (23) hold for each of those larger
fibers. Identical root observations in (22) also give the same lower bounds
for observers allowed to read the entire future trajectory.

In particular the previous exact result and the new strict lower bound give

\[
\boxed{\Omega_8(R_3)=420<432\le\Omega_9(R_3).}
\tag{24}
\]

The proof of (24) uses two finite exact costs and the newly compatible chain.
It does not require a complete nine-cover classification. The existing
general finite-budget upper bound remains applicable, but neither equality
in the nine-budget lower bound nor its optimality is asserted.

## 8. Actually evaluated ordinary roots with exact totals 29 and 30

The checker has evaluated (16) and (17) for costs nine and ten, formed all
private integer terms, and tested every pairwise gcd. It saves the complete
roots, progression moduli and E values as hexadecimal integers.

| Supplementary cost | Exact total | Root bits | Private terms | Gcd pairs checked | Scalar period |
|---:|---:|---:|---:|---:|---:|
| 9 | 29 | 128163 | 29 | 406 | 60480 |
| 10 | 30 | 219388 | 30 | 435 | 60480 |

Every gcd is one; both selected covers have zero uncovered positions in their
complete scalar residue periods. Every root satisfies all 74 fixed R4 prime
coordinates. The proof, rather than extrapolation from these finite periods,
establishes the full infinite sequence and the unbounded cost spectrum.

For the cost-ten numerical example, the CRT computation uses C itself as a
modulus at the T3 phase, instead of needing a numerical value for its least
prime factor. This is a stronger congruence than the required one modulo T3.
All prime divisors of C have exact order 864 and the same assigned root phase,
so every one hits at most the T3 private term. Stripping all prime factors
supported on this composite-permitted CRT modulus preserves the same gcd
argument. Selecting any one prime divisor of C supplies the single T3 prime
in the 30-prime upper-bound dictionary. The composite C is never counted as
a prime, and its primality is not an input to any conclusion.

The compact CRT start before coprimalization is also saved, but its displayed
dictionary size is only an upper bound. Exact total minima in the table refer
to the separately saved coprimalized roots.

## 9. Reproduction and boundaries

Run `python verify_nine_spectrum.py` beside this proof. The script uses only
the Python standard library and writes `nine_spectrum_certificate.json`.
It checks the small prime certificates, the two coprime factors in (5), the
order tests and cofactor exclusions, the 74-coordinate fiber, complete
congruence covers and full private-incidence matrices for k=2 through 12,
retained literal phases and changed-order thresholds, and the two evaluated
coprimalized examples. The universal statements are proved above.

The complete cost-eight classification and observer are reused at immutable
science commit `e78c84e2516caff59d206123bdc5e348e9733a6a`, under
`research_notes/portable_direct/riesel_eight_classification_20261124`.
The arbitrary-order existence input is the same credited Bang theorem used
in the preceding consecutive-cover constructions: each new requested order
is greater than six, and only one prime per new order is used.

The companion two-tail classification describes the nine-cover subfamily
required to retain all seven active fixed supplementary primes. Its 24 signed
CRT descriptions on R4 and their least root are conditional-family results.
This note does not promote that minimum to the least cost-nine root on all
of R4, does not classify all cost-nine dictionaries, and does not claim an
exact nine-budget observer modulus. The finite-spectrum theorem and the
lower bounds (23) do not depend on resolving those broader questions.
