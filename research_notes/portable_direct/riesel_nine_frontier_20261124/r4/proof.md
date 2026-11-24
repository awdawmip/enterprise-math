# The complete cost-nine class, exact observer and minimum on R4

Research continuation, 2026-11-24, Asia/Hong_Kong. Researcher `EM-DIRECT-970E1C / TASK_RESEARCH`; Activity `RA-D2EC212845B63844081F9A14`. This is an author proof with shared-context collaborative checking and exact executed arithmetic. Independent project Review and formal proof acceptance are not claimed.

## 1. Fixed integer object and a completely specified new fiber

The object is the full typed integer register at the fixed Heartbeat X6 anchor, with positive singleton BRC update

\[
x\mapsto2x+1,\qquad x_0=a^2-1,\qquad F_n(a)=a^2 2^n-1.
\]

Prime residues and exponent progressions are observations of this integer. The full integer, its cofactors and its joint common-divisor relations remain part of every argument.

Let P be the old twenty-prime dictionary. The supplementary minimum is \(\delta_P(a)\), and the unrestricted total covering-prime minimum is \(\tau(a^2)\). Every covering factor is required to be a proper prime divisor.

The historical R3 progression is

\[
R_3=\{A_3+S_3k:k\ge0\},
\]

```text
A3 = 191972202303719298729928918311723396431844443114656289541489997722900148740095048143165366560585581706728525286370671799498153425353200109163
S3 = 398569978187125493241348981737346491702787412670647652655838012662365320990659421311257378134104419105098635600781280382381386713746554859390
```

Let T8 be the product of the following 31 primes, the complete free budget-eight observer of the preceding paper:

```text
193,1153,6337,22253377,38941695937,278452876033,
33975937,138991501037953,
61681,4562284561,168692292721,469775495062434961,
29,43,1429,5419,3361,15790321,88959882481,
211,421,86171,106681,122921,152041,664441,1564921,
7416361,47392381,146919792181,1041815865690181.
```

Define

\[
R_4=\{a\in R_3:a\equiv0\pmod{T_8}\}
=\{A_4+S_4j:j\ge0\},
\]

where

\[
S_4=S_3T_8,\qquad
A_4=A_3+S_3((-A_3)S_3^{-1}\bmod T_8).
\tag{1}
\]

The inverse exists and \(0<A_4<S_4\). Both integers have 354 decimal digits. The certificate retains their complete values. The family fixes 43 historical prime residues and 31 further zero root residues, hence 74 complete prime trajectories. The preceding complete eight-budget theorem gives

\[
\delta_P(a)\ge9\quad\text{for every }a\in R_4.
\tag{2}
\]

The immutable dependency is `awdawmip/enterprise-math@e78c84e2516caff59d206123bdc5e348e9733a6a:research_notes/portable_direct/riesel_eight_classification_20261124/observer/proof.md`, with its companion prefix and tail proofs.

## 2. Complete classification and the role of joint phases

Put

\[
Q_0=\{5,13,19,73\},\qquad
A=38737,\ R=246241,\ U=487824887233.
\]

The companion `observer_proof.md`, section 2, proves that every complete supplement of size at most nine on R4 contains Q0. Its argument uses the new whole-R1 basic-pair theorem, the complete one-W classification, and a two-fiber mass obstruction for the zero-W branch.

After P and Q0, the holes are exactly

\[
n=32+36w,\qquad w\bmod35\in
B=\{0,3,5,8,10,15,21,23,26,28,30,31,33\}.
\tag{3}
\]

The fixed tails A,R,U cover \(w\equiv1\pmod2\), \(w\equiv1\pmod3\), and \(w\equiv2\pmod4\), respectively. Three complete free-prime inventories remain:

| Group | Primes | Base-two orders |
|---|---|---|
| \(\mathcal G\) | 92737, 649657, 40388473189, 77158673929, 118750098349 | 63, 63, 252, 126, 252 |
| \(\mathcal R\) | 209924353, 4261383649, 24929060818265360451708193 | 432, 432, 432 |
| \(\mathcal H\) | 8369281, 394783681, 4278255361, 46908728641, 750016890283777055704738227247474485366338380663681 | 720, 240, 80, 240, 720 |

The complete nine-prime supplements are precisely Q0 plus one of the following five-tail types:

| Type | Fixed tails retained | Free primes and their w phases | Phase dictionaries | Signed CRT descriptions |
|---|---|---|---:|---:|
| G | none | all five \(\mathcal G\), bijectively assigned to 0,1,2,3,5 modulo 7 | 120 | 3,840 |
| RR | A,R,U | two distinct \(\mathcal R\), assigned to 0,8 modulo 12 | 6 | 24 |
| RRR | A,U | all three \(\mathcal R\), assigned to 0,4,8 modulo 12 | 6 | 48 |
| HHH | A,U | three distinct \(\mathcal H\), assigned to 0,8,16 modulo 20 | 60 | 480 |
| Total | — | — | **192** | **4,392** |

The full all-prime proof is `tail_proof.md`. It first bounds the mass of an arbitrary-order channel, excludes all other structural cases, and only then resolves the finite surviving order inventories. The exact remaining-row cases are separately checked in `verify_no_h2_mass.py`. No bound on prime magnitude substitutes for this reduction.

For a free prime q at w phase b, the literal root condition is

\[
a\equiv\pm2^{-(16+18b)}\pmod q.
\tag{4}
\]

All assigned free primes are coprime to S4. CRT therefore gives every listed signed progression, and all positive roots on it have exact cost nine by (2). Their full dictionaries are automatically inclusion-minimal.

There are four dictionary types but only three root predicates. The RRR root set is contained in RR: the channel at w=4 modulo twelve may be replaced by the already fixed R, leaving the other two assigned free primes. The canonical root descriptions therefore number \(3840+24+480=4344\). These descriptions still have possible intersections; they are not disjoint root residue classes.

## 3. Complete new prime inventory

The new effective period-five inventory after w=4t is determined by

\[
\operatorname{ord}_q(2^{144})=5.
\]

Writing \(d=\operatorname{ord}_q2\), the equation is \(d/\gcd(d,144)=5\), so \(d=5g\) with \(g\mid144\). The old cases are old dictionary primes or inactive R4 coordinates. The surviving orders are 80,240,720, and the complete products are

\[
\begin{aligned}
\Phi_{80}(2)&=4278255361,\\
\Phi_{240}(2)&=394783681\cdot46908728641,\\
\Phi_{720}(2)&=8369281\cdot750016890283777055704738227247474485366338380663681.
\end{aligned}
\tag{5}
\]

The calculator verifies each product by the defining cyclotomic recursion, every factor's exact multiplicative order, and deterministic primality via complete recursive n-minus-one certificates. The 51-digit factor in the last line is fully certified; it is not an assumed probable prime. The new five-factor inventory needs 36 recursive certificate nodes; the merged inventory for all selected mathematical dependencies verifies 88 distinct prime nodes.

The \(\mathcal G\) inventory is inherited from the complete orders 63,126,252 in the current prefix proof. The \(\mathcal R\) inventory is inherited from the complete order-432 factorization in the current two-tail proof. The merged standard-library checker verifies the relevant primality certificates anew at this combined inventory boundary and records their source paths.

## 4. Exact observer and the meaning of order 720

Let

\[
M_9=\prod_{q\in\mathcal G\cup\mathcal R\cup\mathcal H}q.
\]

For every positive integer N,

\[
\boxed{[a]_N\text{ decides }\delta_P(a)\le9\text{ throughout }R_4
\iff M_9\mid N.}
\tag{6}
\]

Exactly the same equivalence holds if the observer receives the complete future sequence \(([F_n(a)]_N)_{n\ge1}\).

Sufficiency follows from the three complete root predicates. Necessity is proved separately for every one of the thirteen free coordinates. The certificate constructs thirteen pairs of positive ordinary roots, one with exact cost nine and the other with exact cost ten. A pair differs only in its target coordinate among all 87 fixed-plus-essential prime coordinates. A common order-864 refinement supplies a ten-prime cover to both roots, proving that the negative example has finite exact cost ten.

More precisely, the pairs also retain the residue at X=68016300334849 and modulo the explicit integer C satisfying

\[
X C=2^{288}-2^{144}+1,
\]

where every prime divisor of C has order 864. Thus they have the same full trajectories at 87 explicitly named primes besides the changed target, and also at every prime divisor of C. In particular at least 88 prime trajectories are identical. C itself is not counted as a prime. The complete C value and the proof avoiding any primality assumption on C are in `../spectrum/proof.md` and the certificate.

For an arbitrary N missing a target q, the common CRT conditions extend to \(\operatorname{lcm}(S_4,N,M_9/q,X,C)\), which is coprime to q. This gives the same counterexample inside one residue class modulo N, including arbitrary finite prime powers. The detailed proof is `observer_proof.md`.

Consequently

\[
\boxed{\Omega_9(R_4)=\widehat\Omega_9(R_4)=720.}
\tag{7}
\]

The metric is the maximum base-two multiplicative order of an observed odd prime. There are exactly thirteen necessary additional prime coordinates; their product is one sufficient composite modulus. Increasing powers of the other primes cannot replace a missing essential coordinate.

Because \(R_4\subset R_3\subset R_2\subset R_1\), this gives the lower bound 720 on each larger family's budget-nine observer. Only R4 receives equality in (7).

## 5. The global minimum of the complete R4 cost-nine class

For every one of the 4,392 signed CRT descriptions, the checker computes its least positive root. The full four-family enumeration gives:

| Family | CRT starts compared | Digits of family minimum |
|---|---:|---:|
| G | 3,840 | 394 |
| RR | 24 | **371** |
| RRR | 48 | 395 |
| HHH | 480 | 378 |

Possible overlaps do not affect a minimum. The complete classification proves that every cost-nine root in R4 belongs to this union, so comparing all least starts proves the global minimum on that precise domain. The result is

\[
\boxed{a_{9,\min}^{R_4}=A_4+75240521932528635\,S_4.}
\tag{8}
\]

Its full decimal value is

```text
41827204235278113102728963989385111219996616875810967006685409379631973239368404676825708932524338584566302489346933611334268092964973257823581835136481095570798758906669004270819218885649203203304534183167368156237584516628895469357035618923674786027207678768467525149076136384266734275127645336612154683885541594283259752136216244695264672084525880943271789328244084723
```

Put \(Q_7=Q_0\cup\{A,R,U\}=\{5,13,19,73,38737,246241,487824887233\}\). Its supplement is

\[
Q_7\cup\{4261383649,209924353\},
\]

with the two free primes at w=0 and w=8 modulo twelve, respectively, both with the positive sign in (4).

The checker also finds and verifies twenty-nine pairwise-coprime private integer terms, all at indices at most 1,472. All 406 pairwise gcds equal one. The general finite-witness lemma in `../totals/proof.md` therefore strengthens the minimum's costs to

\[
\boxed{\delta_P(a_{9,\min}^{R_4})=9,
\qquad\tau((a_{9,\min}^{R_4})^2)=29.}
\tag{9}
\]

The exact (selected prime, witness index) pairs are

```text
(5,6),(7,16),(13,12),(17,3),(19,152),(31,89),(41,5),(71,293),
(73,20),(97,213),(113,413),(127,113),(151,41),(241,33),(257,87),
(281,233),(337,773),(641,207),(673,237),(1321,257),(14449,53),
(29191,593),(38737,140),(65537,63),(246241,1472),(6700417,111),
(209924353,320),(4261383649,32),(487824887233,968).
```

This minimum is over all R4 roots of cost nine, not just the RR type. It is not claimed to minimize over the larger R3 or R1 families.

## 6. Exact natural frequency, with all overlaps counted

For a finite prime set S and k required phase colors, each giving two distinct root residues at every prime, define

\[
C_k(S)=\sum_{j=0}^k(-1)^j\binom{k}{j}\prod_{q\in S}(q-2j).
\tag{10}
\]

This is inclusion-exclusion on missing colors. The checker also obtains the same integer by a weighted subset-mask count, independently of this formula.

Put

\[
g=\frac{3840}{\prod\mathcal G},\qquad
r=\frac{C_2(\mathcal R)}{\prod\mathcal R},\qquad
h=\frac{C_3(\mathcal H)}{\prod\mathcal H}.
\]

The three prime groups are disjoint and are coprime to S4, so CRT makes their coordinates independent when counting residues along R4. The exact relative natural density is therefore

\[
\boxed{\rho_9(R_4)=1-(1-g)(1-r)(1-h).}
\tag{11}
\]

Numerically it is

\[
8.9428657228405933706561002742181955773152113864121274594365701290997188271059893
\times10^{-18}.
\]

The complete integer numerator and denominator, before and after reduction, are retained in the certificate. The frequency is relative to the R4 progression, and follows from exact periodicity modulo M9. It is not a statement about random uniform integers outside this family.

## 7. A further bound on the original R1 observation question

The new basic-pair theorem applies throughout R1 at budget nine. Consequently a minimum complete supplement of at most nine primes has at most seven primes remaining after 5 and 13. The residual set after those two is the union of thirteen progressions

\[
n=8+12r+420t,\qquad r\in\{1,2,10,11,12,16,17,22,25,26,30,31,32\}.
\]

Every indispensable remaining prime has a private position on at least one such progression. If s is the number of remaining primes and

\[
e_q=\operatorname{ord}_q(2^{420})>2^{s-1},
\]

the next \(2^{s-1}\) positions after its private one receive no hit from q. They must be covered by at most s-1 other congruence classes. The Crittenden–Vanden Eynden interval theorem then makes those classes cover the whole progression, contradicting privacy. Thus

\[
e_q\le2^{s-1}\le64,
\qquad \operatorname{ord}_q2=e_q\gcd(\operatorname{ord}_q2,420)\le26880.
\]

Only finitely many primes have \(\operatorname{ord}_q(2^{420})\le64\): each divides one of \(2^{420j}-1\), \(1\le j\le64\). Observing their root residues therefore decides the original budget-nine predicate. Together with the R4 lower bound,

\[
\boxed{720\le\Omega_9(R_i)\le26880\quad(i=1,2,3),}
\tag{12}
\]

with the same bounds for full-future observers. In particular the original \(\Omega_9\), whose domain is R1, has this interval, while (7) remains an exact statement only on R4.

The external theorem used in this paragraph is Theorem 1 of P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe and M. Tiba, *Covering intervals with arithmetic progressions*, Acta Mathematica Hungarica 161 (2020), 197–200, DOI [10.1007/s10474-019-00980-z](https://doi.org/10.1007/s10474-019-00980-z), [author manuscript](https://par.nsf.gov/servlets/purl/10165575). It states that k arithmetic progressions covering \(2^k\) consecutive integers cover all integers. The order bound and the R1 application above are the present deduction.

## 8. Actual execution and reproduction

Run

```sh
python verify_r4_nine.py
```

for the self-contained standard-library arithmetic, or add `--source-dir /path/to/src` to execute the frozen native BRC package at commit `b1efc6c805661ed7b476e6e730107da6043176ee`. The saved certificate was produced with native execution enabled and reports `PASS`.

The arithmetic covers all 192 phase dictionaries and all 4,392 signed CRT starts, verifies the complete new inventories with deterministic prime certificates, computes the exact Boolean union density, constructs all thirteen essential-coordinate pairs, checks the minimum's full 60,480-position phase cover, and computes all 406 gcds of its 29 witnesses.

The native run produces the 371-digit minimum's full states through index 1,472. At each index it reads all 87 fixed-plus-essential prime channels, compares the 74 fixed observations with A4, and recomposes the full integer from a joint mixed-radix readout. The actual new counts are 1,472 one-step updates, 736 two-step composed evaluations, 128,064 prime readouts, 1,472 joint readouts/recompositions, and 108,928 fixed-coordinate comparisons. All 29 full native witness integers equal the arithmetic terms used for the unrestricted lower bound.

The native interval is a witness interval. The complete 60,480-phase upper-cover check is separate. Every full integer witness, its proper prime cofactor, the final full native state, the thirteen counterfactual root pairs, the exact density, and each family's minimum are retained in `r4_nine_certificate.json`. The complete CRT stream is represented by its deterministic enumeration algorithm, counts and per-family digest; replay does not require a multi-megabyte list of every start.
