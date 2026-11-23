# Complete classification of five-prime supplements of the old holes

## Result and scope

Fix the old root class

\[
a\equiv a_*\pmod{2M},\qquad 3\mid a,\qquad a>0,
\]

where

\[
a_*=690786768637635218740714348513373826260012289,
\]

\[
M=1397394912916194098609132326092145093313722687204526281,
\]

and the old prime dictionary is

\[
P=\{7,17,31,41,71,97,113,127,151,241,257,281,337,641,
673,1321,14449,29191,65537,6700417\}.
\]

Consider \(F_n(a)=a^2 2^n-1\), for positive exponent indices n. A **complete supplement** is a set of distinct primes outside P whose divisibility channels cover every term not already covered by P. The classification below imposes no prime-size or order cutoff.

**Theorem.** Every complete supplement with at most five primes has exactly five active primes. It contains 5 and 13; their even-index channels have opposite u parity, where \(n=2u\). Put \(\varepsilon\in\{0,1\}\) for the parity covered by 13, and put \(t=c_{13}\bmod3\), where \(c_q\) denotes a channel's u phase. Then \(t\in\{0,1\}\), and precisely the following three types occur.

| Type | Phase of 13 modulo 3 | Remaining old-hole fiber | Other three primes and their coverage | Number of phase dictionaries |
|---|---:|---|---|---:|
| U/H1 | 0 | \(u\equiv\varepsilon\pmod2,\ u\equiv1\pmod3\) | Exactly \(\{11,61,331\}\), assigned to the mod-5 categories 0, 1, 4, one each | 12 |
| W/H1 | 0 | \(u\equiv\varepsilon\pmod2,\ u\equiv1\pmod3\) | Any three distinct primes from \(\{19,37,73,109\}\), assigned to the three effective mod-3 phases, one each | 48 |
| W/H0 | 1 | \(u\equiv\varepsilon\pmod2,\ u\equiv0\pmod3\) | Any three distinct primes from \(\{19,37,73,109\}\), assigned to the three effective mod-3 phases, one each | 48 |

Thus there are exactly **108 phase dictionaries**. These are dictionaries, not disjoint root classes. A fixed root can support more than one dictionary. Each dictionary is realized by infinitely many positive roots in the stated branch. For every such root the minimum number of supplementary primes is exactly five.

The proof uses the established old-hole calculation and the universal four-prime gap from the round-eight staircase theorem, published in science commit
`a2ae4d93398425e67dacbb4c99b7f3a6755e5771`,
`research_notes/portable_direct/riesel_observers_20261122/staircase/proof.md`.
The new all-prime exclusions and complete five-prime classification are proved below. The accompanying `verify_global.py` checks the exact arithmetic inputs and every phase system remaining after those exclusions; `global_certificate.json` records its result. This is an author proof with reproducible exact arithmetic, not a claim of independent review.

## 1. Old holes and the incidence formula

All odd n are covered by P. On even indices, write \(n=2u\). The uncovered u residues modulo 105 are

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}.
\end{split}
\]

There are 36 residues, of full-exponent density \(36/210=6/35\). The classes
\(H_r=\{h\in H:h\equiv r\pmod3\}\) have sizes

\[
|H_0|=23,\qquad |H_1|=13,\qquad H_2=\varnothing.
\]

Their incidences in the five u categories modulo 5 are

| Set | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| \(H_0\) | 6 | 6 | 0 | 6 | 5 |
| \(H_1\) | 5 | 5 | 0 | 0 | 3 |

The maximum mod-7 incidences are respectively 4 and 3. The final category of \(H_1\) is

\[
\{h\in H_1:h\equiv4\pmod5\}=\{49,64,79\},                 \tag{1}
\]

whose mod-7 residues are 0, 1, 2, all distinct.

An active odd prime q has a single even-index divisibility class

\[
u\equiv c_q\pmod{d_q},\qquad d_q=\operatorname{ord}_q4.    \tag{2}
\]

Indeed, \(q\mid F_{2u}(a)\) means \(a^24^u\equiv1\pmod q\); if there is one solution, every solution differs by a multiple of \(d_q\). Prime 2 cannot divide a term, and prime 3 is inactive because \(3\mid a\). A prime dividing a is also inactive.

For a periodic set \(A\subset\mathbb Z/L\mathbb Z\) of size K and one class \(v\equiv c\pmod d\), let

\[
g=\gcd(d,L),\quad e=d/g,\quad
K_g(c)=|\{h\in A:h\equiv c\pmod g\}|.
\]

Its relative density inside A is exactly

\[
\frac{K_g(c)}{Ke}.                                      \tag{3}
\]

To prove this, use the common period \(\operatorname{lcm}(L,d)=Le\). There are Ke positions in A in that period. Each compatible residue h contributes one intersection by CRT. In particular, at fixed g, the maximum in (3) decreases when d increases. For a union of channels, the sum of their relative densities is an upper bound; no independence assumption is made.

For H the complete maximum-incidence table is

| g | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\max_c K_g(c)\) | 36 | 23 | 11 | 7 | 6 | 4 | 2 | 1 |

The parity fibers of H have equal relative density 1/2, because 105 is odd. The affine changes of coordinates used below are invertible on the remaining period, so they preserve these incidence maxima.

The established four-channel theorem leaves full-exponent density at least

\[
D_4=1/140>0.                                            \tag{4}
\]

Consequently a complete supplement with at most five primes uses exactly five active, nonredundant channels. As a useful derived finiteness statement, deleting any one channel from a complete five-channel cover leaves density at least \(1/140\). Its unique contribution is no larger than its entire even phase, of density \(1/(2d_q)\). Thus \(d_q\le70\). The proof below is stronger: it avoids factoring all the periods up to 70 by excluding whole order ranges analytically.

## 2. All-prime bounds away from 5 and 13

### 2.1 A global bound of 1/9 outside five exceptional channels

Remove the old primes and the exceptional primes

\[
E=\{3,5,11,13,19,43,73,331\}.
\]

Every prime factor of \(4^d-1\), for

\[
d\in\{1,2,3,4,5,6,7,8,9,10,12,15\},                    \tag{5}
\]

belongs to \(P\cup E\). Complete small factorizations supporting this assertion are recorded in Section 6 and checked by the calculator. For any other prime, the smallest possible d in the eight gcd columns and the resulting bounds from (3) are

| \(g=\gcd(d,105)\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lower bound on d | 11 | 18 | 20 | 14 | 30 | 21 | 35 | 105 |
| Coverage bound in H | \(1/11\) | \(23/216\) | \(11/144\) | \(7/72\) | \(1/12\) | \(1/9\) | \(1/18\) | \(1/36\) |

All these bounds are at most 1/9. The exceptional active primes other than 5 and 13 have the following exact maxima:

| q | \(d_q\) | Maximum relative coverage in H |
|---:|---:|---:|
| 11 | 5 | \(33/108=11/36\) |
| 19 | 9 | \(23/108\) |
| 73 | 9 | \(23/108\) |
| 43 | 7 | \(21/108=7/36\) |
| 331 | 15 | \(18/108=1/6\) |

These are bounds over every phase, including the phases determined by any particular root.

### 2.2 Five channels cannot avoid both 5 and 13

Suppose a complete five-channel supplement contains neither 5 nor 13. If it also omitted 11, its five largest possible contributions would sum to at most

\[
\frac{23+23+21+18+12}{108}=\frac{97}{108}<1.
\]

If it omitted 19, even allowing 11, its maximum sum would be

\[
\frac{33+23+21+18+12}{108}=\frac{107}{108}<1.
\]

The same argument applies to omission of 73. Hence 11, 19 and 73 are forced.

For each of 19 and 73, its phase modulo 3 is 0 or 1: a phase of 2 hits no old hole and would be redundant. A phase of 0 has maximum relative contribution \(23/108\), while a phase of 1 contributes \(13/108\).

If both phases are 1, the sum of all five contributions is at most

\[
\frac{33+13+13+21+18}{108}=\frac{98}{108}<1.
\]

If one phase is 0 and the other is 1, the upper bound is exactly

\[
\frac{33+23+13+21+18}{108}=1.                             \tag{6}
\]

Equality forces the last two primes to be 43 and 331, with every channel attaining its maximum. To attain \(18/108=6/36\), prime 331 must have its phase in \(H_0\): a single compatible mod-15 class contains at most five elements of \(H_1\). Thus only the phase-1 prime among 19 and 73, prime 11, and prime 43 can cover \(H_1\). Their total contribution to \(H_1\), measured relative to H, is at most

\[
\frac{13}{108}+\frac{5}{36}+\frac{3}{36}
=\frac{37}{108}<\frac{39}{108}=\frac{|H_1|}{|H|},          \tag{7}
\]

a contradiction.

It remains that both 19 and 73 have phase 0 modulo 3. They then leave \(H_1\) untouched, so 11 and the two remaining primes must cover all of \(H_1\).

To analyze this last case, parameterize \(u=1+3v\). The set \(H_1\) becomes a 13-element set modulo 35. A prime channel, if compatible, has effective period

\[
e_q=\operatorname{ord}_q(4^3)=\operatorname{ord}_q64.
\]

For an unused prime outside \(P\cup\{3,5,13,19,73\}\), periods 1, 2, 3 and 4 are excluded by the complete factors of \(2^{6e}-1\). Period 5 permits exactly the primes 11 and 331; period 7 permits exactly 43 and 5419. Excluding 11 and 331, formula (3) gives the following bounds over \(g=\gcd(e,35)\):

| g | 1 | 5 | 7 | 35 |
|---|---:|---:|---:|---:|
| Lower bound on e | 6 | 10 | 7 | 35 |
| Coverage bound in \(H_1\) | \(1/6\) | \(5/26\) | \(3/13\) | \(1/13\) |

Thus only 11 and 331 can attain \(5/13\); all other primes cover at most \(3/13\), and equality in that latter bound requires 43 or 5419.

Since 11 is already one of the three channels, the other two must be 331 and one of 43, 5419: without 331 the sum is at most \((5+3+3)/13<1\). With 331 the maximal sum is \((5+5+3)/13=1\), so each maximum must be attained and the intersections must be disjoint. The 11 and 331 channels must therefore cover the two mod-5 categories 0 and 1. By (1), the remaining three positions occupy three distinct mod-7 classes. Neither 43 nor 5419, which gives only one effective mod-7 class, can cover them. This final contradiction proves that a complete five-channel cover cannot omit both 5 and 13.

### 2.3 Five channels cannot contain exactly one of 5 and 13

A channel for 5 lies in one u parity, as does a channel for 13. On the parity missed by the sole prime among \(\{5,13\}\), write \(u=\varepsilon+2v\). The old holes form an affine copy of H modulo 105, and a compatible new prime has effective period

\[
e_q=\operatorname{ord}_q16.
\]

Outside \(P\cup\{3,5,11,13\}\), none of the periods 1 through 6 is possible: every prime factor of \(16^e-1\) for those e lies in this excluded set. This includes the useful exclusion of period 4, since

\[
2^{16}-1=3\cdot5\cdot17\cdot257.
\]

For the eight gcd columns of H the resulting bounds are

| \(g=\gcd(e,105)\) | 1 | 3 | 5 | 7 | 15 | 21 | 35 | 105 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lower bound on e | 8 | 9 | 10 | 7 | 15 | 21 | 35 | 105 |
| Coverage bound in the parity fiber | \(1/8\) | \(23/108\) | \(11/72\) | \(7/36\) | \(1/6\) | \(1/9\) | \(1/18\) | \(1/36\) |

Every entry is at most \(23/108\). Prime 11 has effective period 5 and covers at most \(11/36\). Therefore the four remaining distinct channels cover at most

\[
\frac{11}{36}+3\frac{23}{108}=\frac{17}{18}<1              \tag{8}
\]

of the missed parity fiber. This excludes exactly one of 5 and 13.

### 2.4 The two forced channels have opposite parity

We have proved that both 5 and 13 occur. If their u parities agreed, the 13 channel would be entirely covered by the 5 channel on the old holes. It could be deleted, contradicting (4). Thus they have opposite parity.

Let \(\varepsilon\) be the parity covered by 13. Then

\[
c_5=1-\varepsilon\pmod2.
\]

If \(c_{13}\equiv2\pmod3\), the 13 channel hits no old hole and is again redundant. Thus \(t=c_{13}\bmod3\) is 0 or 1. Inside the parity \(\varepsilon\), prime 13 covers every old hole with \(u\equiv t\pmod3\). The only remaining fiber has \(u\equiv1-t\pmod3\).

## 3. Complete classification on the remaining fiber

Choose the unique \(u_0\in\{0,1,\ldots,5\}\) satisfying

\[
u_0\equiv\varepsilon\pmod2,\qquad
u_0\equiv1-t\pmod3,
\]

and write \(u=u_0+6v\). The remaining holes form a set A modulo 35 of size 13 if \(t=0\), or 23 if \(t=1\). The effective period of a compatible prime is

\[
f_q=\operatorname{ord}_q(4^6)=\operatorname{ord}_q(2^{12}). \tag{9}
\]

For \(q\notin P\cup\{3,5,13\}\), periods 1 and 2 are impossible because all factors of \(2^{24}-1\) are excluded. Hence \(f_q\ge3\).

### 3.1 The 13-position fiber: U or W, with no mixed family

For the 13-position fiber, formula (3) gives

| \(g=\gcd(f,35)\) | 1 | 5 | 7 | 35 |
|---|---:|---:|---:|---:|
| Coverage bound | \(1/3\) | \(5/13\) | \(3/13\) | \(1/13\) |

Thus each of the three channels covers at most \(5/13\). For their union to be the whole fiber, each channel must contribute at least \(1-2(5/13)=3/13\). Applying (3) in each gcd column forces

\[
f\in\{3,4,5,7\}.                                       \tag{10}
\]

The complete factorizations of \(2^{12f}-1\), followed by exact order checks, give

| f | Eligible primes with this effective period |
|---:|---|
| 3 | \(W=\{19,37,73,109\}\) |
| 4 | None |
| 5 | \(U=\{11,61,331\}\) |
| 7 | \(Z=\{29,43,1429,5419\}\) |

In particular, the absence of period 4 is complete: all factors of \(2^{48}-1\) belong to \(P\cup\{3,5,13\}\).

Suppose a period-3 channel and a period-5 or period-7 channel both occur. There are at most two channels of period 5 or 7. Their union covers at most \(10/13<1\), so choose a residue of A modulo 35 that they miss. Its three lifts modulo 105 run through all three classes modulo 3. At most two period-3 channels cannot cover all three lifts. Thus a mixed family is impossible. If period 3 occurs at all, all three periods are 3, and the three phases must be distinct. This is exactly the W/H1 type.

Now suppose no period-3 channel occurs. If at most one period-5 channel occurs, the three contributions sum to at most \((5+3+3)/13<1\). If exactly two period-5 channels occur, the only possible sum is \((5+5+3)/13=1\), requiring the two largest mod-5 categories 0 and 1 and one mod-7 channel for their complement. The complement (1) has three distinct mod-7 residues, so this is impossible. The affine map from v to u is invertible modulo 7, so this obstruction is unchanged in the v coordinate.

All three periods must therefore be 5. The three eligible primes are exactly U, and the only nonempty mod-5 categories of \(H_1\) are 0, 1, 4. Each must be covered by one channel. This is exactly the U/H1 type.

### 3.2 The 23-position fiber: only W

For the 23-position fiber the corresponding bounds are

| \(g=\gcd(f,35)\) | 1 | 5 | 7 | 35 |
|---|---:|---:|---:|---:|
| Coverage bound | \(1/3\) | \(6/23\) | \(4/23\) | \(1/23\) |

Every entry except the first is strictly smaller than \(1/3\). Three channels can cover the whole fiber only if all three attain \(1/3\), forcing \(f=3\) for all of them. Hence the primes are three distinct members of W and their three effective phases are distinct. This is exactly the W/H0 type.

These arguments classify every remaining prime and phase, without presuming any upper bound on the original prime magnitudes.

## 4. Explicit phases, counting, and realization

The relevant u periods are

| q | 5 | 13 | 11 | 61 | 331 | 19 | 37 | 73 | 109 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d_q=\operatorname{ord}_q4\) | 2 | 6 | 5 | 30 | 15 | 9 | 18 | 9 | 18 |

For every type, choose \(\varepsilon\in\{0,1\}\) and use

\[
c_5=1-\varepsilon,\qquad
c_{13}=(3\varepsilon+4t)\bmod6.                          \tag{11}
\]

For U/H1 take \(t=0\). Assign the categories \(r=0,1,4\) bijectively to the three primes U. The assigned phase is the unique solution of

\[
\begin{array}{c|l}
q&\text{phase conditions}\\\hline
11&c_{11}\equiv r\pmod5,\\
331&c_{331}\equiv1\pmod3,\quad c_{331}\equiv r\pmod5,\\
61&c_{61}\equiv\varepsilon\pmod2,\quad c_{61}\equiv1\pmod3,
\quad c_{61}\equiv r\pmod5.
\end{array}                                             \tag{12}
\]

There are \(2\cdot3!=12\) distinct phase dictionaries.

For either W type, choose any three distinct members of W and assign them bijectively to \(j=0,1,2\). With \(u_0\) as in Section 3, use

\[
c_q=(u_0+6j)\bmod d_q.                                 \tag{13}
\]

For each t there are \(2\binom43 3!=48\) dictionaries, giving 96 across the two W types and 108 in total.

As an explicit W/H0 example, take

\[
(q,c_q)=(5,1),(13,4),(19,0),(73,3),(109,6).              \tag{14}
\]

Prime 5 covers odd u. Prime 13 covers even u with \(u\equiv1\pmod3\). On the remaining \(u\equiv0\pmod6\), the last three channels cover the three classes of \(v=u/6\pmod3\). This demonstrates why a five-prime complete cover need not use the mod-3 phase of 13 that optimizes the two-prime density reduction. Completeness at budget five and optimal intermediate residual density are different optimization questions.

For any phase c modulo \(d_q\), the corresponding root residues are exactly

\[
a\equiv \pm2^{-c}\pmod q.                              \tag{15}
\]

All listed new primes are distinct from 3 and from P. Consequently the old congruence modulo \(2M\), the branch condition modulo 3, and independently chosen signs in (15) are compatible by CRT. Each dictionary therefore gives 32 sign choices modulo its own product of five primes, and each choice extends to infinitely many positive roots in the old branch. These 32 choices per dictionary are not being summed as disjoint root classes across different dictionaries.

The old root representative satisfies \(0<a_*<2M\) and \(a_*>6700417\). Every positive old-class root is therefore at least \(a_*\). All primes in the old dictionary and all primes in the final classified supplements (whose largest member is 331) are proper divisors whenever they divide a term. Together with the old P channels, each classified supplement proves compositeness for every positive exponent index. The already established four-channel gap then gives the exact supplementary complexity

\[
\delta_P(a)=5
\]

for roots realizing any classified dictionary. Write \(\tau(a^2)\) for the minimum total number of covering primes for the coefficient \(a^2\). This is not a proof that this unrestricted total complexity is exactly 25; the immediate bound is only \(\tau(a^2)\le |P|+5=25\).

## 5. Exact verification and its logical role

Run

```bash
python verify_global.py
```

The verifier uses integer trial division, exact multiplicative orders, rational arithmetic, and explicit residue sets. It checks:

- the old-hole incidences, all complete small factorizations, and the rational exclusion bounds used in Sections 1–3;
- the eligible prime sets for each surviving effective period;
- all **40,026** phase assignments on distinct prime triples left by the analytic reduction, obtaining exactly the 108 dictionaries in the theorem;
- every dictionary over its complete old-hole period in u, which is 210 for U/H1 and 630 for the W types;
- a private old-hole witness for each of the five channels in every dictionary, and the two root residues for every channel.

The calculation reports `PASS` with type counts 12, 48, 48. The common-period checks are complete periodic checks, not initial-segment tests. The finite phase enumeration confirms the closed-form classification; the all-prime completeness rests on the analytical order and incidence exclusions above. No empirical bound on prime magnitude or sampled exponent length is used.

The output is `global_certificate.json`. Its full list of 108 dictionaries is provided for reuse by root observers; the proof itself does not depend on accepting an opaque enumeration.

## 6. Complete factorization inputs

All entries below are complete factorizations of \(2^N-1\); the calculator checks both the product and the primality of every listed factor by exact trial division. The omitted smaller powers needed in (5) divide listed powers, or are checked directly by the calculator.

| N | Complete factorization of \(2^N-1\) |
|---:|---|
| 6 | \(3^2\cdot7\) |
| 12 | \(3^2\cdot5\cdot7\cdot13\) |
| 14 | \(3\cdot43\cdot127\) |
| 16 | \(3\cdot5\cdot17\cdot257\) |
| 18 | \(3^3\cdot7\cdot19\cdot73\) |
| 20 | \(3\cdot5^2\cdot11\cdot31\cdot41\) |
| 24 | \(3^2\cdot5\cdot7\cdot13\cdot17\cdot241\) |
| 30 | \(3^2\cdot7\cdot11\cdot31\cdot151\cdot331\) |
| 36 | \(3^3\cdot5\cdot7\cdot13\cdot19\cdot37\cdot73\cdot109\) |
| 42 | \(3^2\cdot7^2\cdot43\cdot127\cdot337\cdot5419\) |
| 48 | \(3^2\cdot5\cdot7\cdot13\cdot17\cdot97\cdot241\cdot257\cdot673\) |
| 60 | \(3^2\cdot5^2\cdot7\cdot11\cdot13\cdot31\cdot41\cdot61\cdot151\cdot331\cdot1321\) |
| 84 | \(3^2\cdot5\cdot7^2\cdot13\cdot29\cdot43\cdot113\cdot127\cdot337\cdot1429\cdot5419\cdot14449\) |

The factor 1321 in the N=60 row is included; it is an old prime and does not add a new period-5 candidate.

## 7. Native interpretation and limits

The native framework and fixed X6 anchor are inherited from the existing research: the integer register, positive singleton weight and multiplicity one, and the updates \(x\mapsto2x+1\), or \(x\mapsto4x+3\) on the even subsequence, are unchanged. Exponent index is an arithmetic index, not an assertion about physical time. Prime divisibility and the phase dictionaries are observations of that state, not new axes replacing it.

The new theorem gives a complete finite phase classification for this particular old dictionary, root class, branch condition and supplementary budget. It does not identify residual-phase observations with the full integer state, nor does it discard cofactors or joint-gcd information in other questions. It does not classify all Riesel numbers or all finite covering systems. No new native execution, formal task claim, or independent review is asserted in this file; the existing native execution and published old-hole/four-channel results are reused with the stated scope.
