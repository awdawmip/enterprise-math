# The complete 59-coordinate ninth-budget observer on the full R3 fiber

Research continuation v15, 2026-11-24 (Asia/Hong_Kong). Existing Researcher
`EM-DIRECT-970E1C`, Activity `RA-D2EC212845B63844081F9A14`. This is an
author proof with shared-context mathematical checking and exact arithmetic.
Independent project Review and formal proof acceptance are not claimed.

The object remains the full integer trajectory at the fixed Heartbeat X6
anchor, with positive singleton BRC action x -> 2x+1 and weight and
multiplicity one:

\[
F_n(a)=a^22^n-1.
\]

## 1. Domain, coordinate set, and theorem

Use the inherited P and the historical fixed 43-prime fiber

\[
R_3=\{A_3+S_3j:j\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

The following twelve disjoint groups contain exactly 59 primes. Their
union is denoted U9, and M9 is their squarefree product.

| Group | Complete prime set | Size | Largest base-two order |
|---|---|---:|---:|
| Z | 29,43,1429,5419 | 4 | 84 |
| J | 3361,15790321,88959882481 | 3 | 168 |
| U | 211,421,86171,106681,122921,152041,664441,1564921,7416361,47392381,146919792181,1041815865690181 | 12 | 420 |
| B | 193,1153,6337,22253377,38941695937,278452876033 | 6 | 288 |
| D | 33975937,138991501037953 | 2 | 216 |
| C | 61681,4562284561,168692292721,469775495062434961 | 4 | 360 |
| K | 92737,649657,40388473189,77158673929,118750098349 | 5 | 252 |
| E | 209924353,4261383649,24929060818265360451708193 | 3 | 432 |
| H | 8369281,394783681,4278255361,46908728641,750016890283777055704738227247474485366338380663681 | 5 | 720 |
| F | 3457,816769,18446744069414584321,1562985901350085709953,1422346738975853644793916289 | 5 | 576 |
| L | 2017,5153,25629623713,54410972897,1538595959564161 | 5 | 336 |
| V | 127681,1130641,755667361,84179842077657862011867889681,54169520413224311136354324156824071681 | 5 | 840 |

The first six groups are the complete v13 budget-eight observer support,
of size 31. The last six add 28 new primes. All 59 are coprime to S3.

For a finite modulus N, let observation mean either the root residue
a modulo N or the complete future trajectory F_n(a) modulo N. Put

\[
B_N=\max\bigl(\{1\}\cup
\{\operatorname{ord}_q2:q\mid N,\ q\text{ odd prime}\}\bigr).
\]

> **Theorem.** For every positive integer N, observation modulo N
> decides the predicate delta_P(a)<=9 throughout R3 if and only if
> M9 divides N. This holds for both root residues and complete future
> trajectory observations. Consequently
>
> \[
> \boxed{\Omega_9(R_3)=\widehat\Omega_9(R_3)=840.}
> \]

The theorem specifies the necessary prime support, including arbitrary
finite powers and arbitrary composite observation moduli. The number 59
does not count how many separate composite-modulus observations one must
make; a single modulus M9 contains the whole support.

## 2. Sufficiency from the complete cover classification

The v14 basic-pair theorem forces 5 and 13 in every supplement of at most
nine primes on R1, hence on R3. The complete budget-eight predicate is
already known. For a root of exact cost nine, take a minimum supplement;
it is irredundant. Its intersection with W={19,73} has size zero, one,
or two.

The complete zero-W classification is the eight-type theorem in the v15
zero-branch proof. The complete one-W branch is the v14 four-mod-seven
plus two-mod-twenty-one theorem. The complete two-W root-existence
predicate is the v15 Q0-retaining theorem, including its explicit
same-root replacements by fixed A=38737, R=246241 and U=487824887233.
Together with all budget-eight roots, these exhaust the predicate
delta_P<=9.

Every free prime appearing in these predicates belongs to U9. Conversely
their only nonfree prime coordinates are fixed throughout R3. All phase
tests at a prime q have the form

\[
a^22^c=1\pmod q
\tag{1}
\]

for a specified exponent phase. Thus a modulo M9 determines the predicate.
So does a^2 modulo M9. If M9 divides N, the complete future observation
gives a^2 modulo every required odd prime from F_0+1, or from any single
observed F_n+1 after multiplying by 2^{-n}. This proves sufficiency for
both observation models.

There is no assertion that every nonminimal nine-prime dictionary uses
only these primes: it could include an irrelevant extra prime. The
sufficient universe characterizes existence of a small cover.

## 3. All 59 coordinates are individually necessary

For each target q in U9, choose the following phase configuration. Every
U9 coordinate not explicitly selected is set to root residue zero. The
phase notation is n=8+12v=32+36w, and t=w/4 where applicable. A phase b
is imposed by

\[
a=2^{-(4+6b)}\pmod q \quad(v\text{ phase}),
\qquad
a=2^{-(16+18b)}\pmod q \quad(w\text{ phase}).
\tag{2}
\]

Only the positive sign is needed for these necessary-coordinate witnesses.

| Target group | Selected root configuration |
|---|---|
| Z | The target plus four K primes cover the five occupied w mod-seven rows |
| K | All four Z primes plus the target cover those five rows |
| B | The target covers t=1 mod2; F primes 3457 and 816769 cover t=0,2 mod4 |
| F | B prime 1153 covers t=1 mod2; the target and another F cover t=0,2 mod4 |
| D or E | The target covers t=0 mod3; a different E prime covers t=2 mod3; fixed R covers t=1 |
| C or H | The target and two other H primes cover t=0,2,4 mod5 |
| J | Four Z rows leave v=1 mod7; the target covers v=1 mod14; two L primes cover v=8,22 mod28 |
| L | The same zero-W type IV, with the target as one of the two L primes |
| U | Four Z rows leave the large row v=2 mod7; the target and two other U primes cover its points v=2,16,30 mod35 |
| V | Four Z rows leave v=1 mod7; J prime 3361 covers v=1 mod14; C prime 61681 covers v=2 mod10; the target covers v=36 mod70 |

All assignments in a row are compatible with R3. When choosing a second
prime from a group, the target is excluded. The script specifies every
choice and retains the actual root residues and roots.

For the on configuration keep the target at its indicated nonzero root
residue. For the off configuration change only that root residue to zero.
CRT modulo S3 times M9 produces actual least positive ordinary integer
roots a_on and a_off. They have the same root residue modulo

\[
S_3(M_9/q),
\tag{3}
\]

and different target residues. All roots, not just formal residue vectors,
are retained in `nine_observer_certificate.json`.

The on configuration has exact cost nine and the off configuration has
cost greater than nine. These assertions are verified by an exhaustive
set-cover check over the full period, as detailed next. Finiteness of the
off cost is not asserted for all 59 examples. It is not required for the
necessary-coordinate theorem; Section 5 gives a finite exact 9/10 pair
at the extremal order 840.

### Exact full-period cover verification

After P,5,13, the residual v coordinates are

\[
v\bmod35\in
\{1,2,10,11,12,16,17,22,25,26,30,31,32\}.
\tag{4}
\]

Use v-period 5040, equivalently n-period 60480. Every prime order in the
complete candidate universe divides 60480. There are exactly 1872
residual positions in this period. This period includes the factors of
three required by the fixed order-108 prime and the order-432 group.

For each actual root the verifier computes the exact zero class of each
candidate prime among U9 and the five fixed tail primes 19,73,A,R,U.
Inactive primes contribute the empty set. The selected configurations
have at most seven active free primes, so at most twelve active channels
remain after P,5,13.

The verifier exhausts all subsets of at most seven active channels on
the complete 1872-position bit set. For every on-root, no subset of at
most six classes covers, and a seven-class cover is found. For every
off-root, no subset of at most seven covers. These exact set-cover checks
do not evaluate the explicit one-W, zero-W or two-W branch formulas.
They use the actual modular zero sets. Completeness of the prime universe
is supplied by Section 2.

Therefore every on-root has delta_P=2+7=9 and every off-root has
delta_P>9. Each pair shares all 43 fixed prime coordinates and the other
58 free coordinates, hence at least 101 complete prime-residue trajectories.

## 4. From coordinate necessity to the criterion for arbitrary N

Suppose q in U9 does not divide N. Take the q-witness vector from Section
3 and any positive off-root a0 realizing it. Set

\[
L=\operatorname{lcm}(S_3M_9/q,N).
\]

Since q is prime and belongs to neither S3 nor N, gcd(q,L)=1. Impose the
common condition a=a0 modulo L. CRT permits two extensions modulo q:
the on target residue and zero. Positive representatives, and arbitrarily
large positive representatives, exist in both classes.

All other necessary prime coordinates remain fixed. The two roots still
have costs nine and greater than nine, respectively, but now have the
same root residue modulo N. Consequently their entire future observations
modulo N agree:

\[
F_n(a_{\rm on})=F_n(a_{\rm off})\pmod N
\qquad\text{for every }n\ge0.
\]

Observation modulo N cannot decide the ninth-budget predicate. Thus every
prime of U9 must divide a sufficient N; because M9 is squarefree this is
exactly M9 dividing N. Arbitrarily high finite powers of the other primes
do not change this argument.

## 5. A finite exact-cost 9/10 counterexample at order 840

Take q=127681, whose exact base-two order is 840. Use four Z primes at
v rows 2,3,4,5 modulo seven, leaving the small row v=1 modulo seven.
It consists of the two points v=1,22 modulo 35. Add

\[
3361:\ v=1\pmod{14},\qquad
61681:\ v=2\pmod{10},\qquad
127681:\ v=36\pmod{70}.
\tag{5}
\]

These seven channels beyond 5,13 give the zero-W type VI cover. The on
root has exact cost nine. Removing the 127681 coordinate leaves precisely
the missing v=36 modulo 70 part of that row, after the common selected
cover.

Define two explicit positive integers

\[
C_{560}=\Phi_{560}(2),\qquad C_{1680}=\Phi_{1680}(2).
\]

Their full values are

```text
C560 = 6301621664034803606600937519472318568267595699040292962561
C1680 = 39248693336626700402488592616830471405685147801983603254769905596951527946156010395959892930658911707724891857944321
```

Neither integer is assumed prime. The checker verifies

\[
2^d=1\pmod{C_d},\qquad
\gcd(C_d,2^{d/r}-1)=1
\quad\text{for every prime }r\mid d,
\tag{6}
\]

for d=560 and 1680. For any prime p dividing Cd, (6) forces
ord_p(2)=d: the order divides d and cannot lose any prime factor of d.
Every prime factor is therefore an ordinary prime of the exact stated
order. The two integers are coprime to each other and to S3*M9, also
verified directly.

Let ell560 and ell1680 be their respective least prime divisors. They
are distinct and lie outside the 59-coordinate universe. Both have
effective v-period 140, since

\[
560/\gcd(560,12)=1680/\gcd(1680,12)=140.
\]

Impose the following common root residues on both on and off roots:

\[
a=2^{-(4+6\cdot36)}\pmod{C_{560}},\qquad
a=2^{-(4+6\cdot106)}\pmod{C_{1680}}.
\tag{7}
\]

The ell560 and ell1680 channels then cover respectively v=36 and v=106
modulo 140. Their union is exactly v=36 modulo 70. Replacing the one
target prime in (5) by these two ordinary primes gives a common
ten-prime supplement for both roots.

CRT with (7), R3 and all 59 root coordinates is compatible. The actual
on and off roots have 906 and 907 decimal digits, respectively, and are
saved in the certificate. Their complete universe set-cover results
remain nine and greater than nine; the common ten-cover therefore proves

\[
\boxed{\delta_P(a_{\rm on})=9,\qquad
\delta_P(a_{\rm off})=10.}
\tag{8}
\]

All primes used in the ten-cover are proper divisors when they hit:
each ell is at most its cyclotomic modulus, both moduli are less than
A3^2-1, and every positive R3 root is at least A3.

The two roots have the same residue modulo

\[
S_3(M_9/127681)C_{560}C_{1680}.
\tag{9}
\]

This gives at least 101 named common prime coordinates and at least two
additional distinct prime divisors, hence **at least 103 identical
complete prime-residue trajectories** with finite exact costs nine and
ten. The two cyclotomic moduli are never counted as primes.

For any additional finite N not divisible by 127681, replace L in
Section 4 by the lcm of N and (9). Toggling the target by CRT preserves
the common ten-cover as well. Thus failure of such an observer can be
witnessed by two finite exact-cost ordinary roots, not only by a root
whose off cost is unknown.

## 6. Sharp order and precise scope

The sufficient modulus M9 has largest prime order 840. Every sufficient
modulus must contain 127681, of order 840. These give the two inequalities
needed for the exact value

\[
\Omega_9(R_3)=\widehat\Omega_9(R_3)=840.
\]

In particular the former larger-fiber interval [720,26880] is closed on
R3. This proof does not assert the same equality on R1 or R2; they inherit
the stronger lower bound 840, and their known upper bound remains
26880. The exact value 720 on the more restricted R4 fiber is unchanged:
its additional zero coordinates eliminate the new branch structures.

The observation metric is maximum base-two order of an observed prime.
The stronger divisibility criterion also determines the smallest sufficient
positive modulus itself: it is M9, which has 594 decimal digits and 1973
binary bits. Thus 1973 is the exact minimum modulus bit length for this
fixed ninth-budget problem on R3. This is a consequence of M9 dividing
every sufficient modulus, not an inference from its maximum prime order.
No asymptotic bit-length or algorithmic running-time bound is claimed.

## 7. Reproduction and evidence boundary

Run `python verify_observer.py` with the adjacent `prime_inventory.json`.
Only the Python standard library is required. The script checks 191
recursive deterministic primality-certificate nodes, all relevant exact
orders, the full scalar prefix period, 59 actual ordinary on/off root
pairs, all their exact set-cover minima through seven residual channels,
and the extra ordinary finite 9/10 pair from (7).

The saved certificate contains all root integers, phase choices, active
channel tables, counts of examined subsets by budget, the complete
observer modulus, the exact cyclotomic integers, order-gcd checks and
common-cover verification. Every new state is a complete integer.

These calculations are scalar arithmetic. No new native BRC execution
is attributed to this observer component. The all-prime completeness is
the mathematical classification in Section 2; the finite period checks
are used within that proved universe.
