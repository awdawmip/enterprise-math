# Exact total cover cost and two cofinite families in one old residual class

**Status:** new author derivation with exact finite certificates; not an independent project Review. Researcher `EM-DIRECT-970E1C`, activity `RA-D2EC212845B63844081F9A14`. No new registration or claim is made here.

## 1. Result and precise scope

Write

\[
 F_n(a)=a^2 2^n-1\qquad(n\ge1),
\]

and let \(\tau(a^2)\) be the minimum cardinality of a finite set of primes containing a proper divisor of every \(F_n(a)\). Put \(\tau=\infty\) when no such finite cover exists. For the fixed old dictionary \(P\), put

\[
 \delta_P(a)=\min_C |C\setminus P|,
\]

where \(C\) ranges over all finite proper prime covers of the same sequence. These are different minimizations: \(\delta_P\) counts only newly added primes, while \(\tau\) counts every prime in a cover.

The old root and dictionary are

\[
 a_*=690786768637635218740714348513373826260012289,
\]

\[
\begin{split}
P=\{&7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,\\
&1321,14449,29191,65537,6700417\},
\end{split}
\]

\[
 M=\prod_{p\in P}p
 =1397394912916194098609132326092145093313722687204526281.
\]

**Theorem.** For each \(b\in\{5,11\}\) and each pair of nonnegative integers \(h,j\), there are infinitely many positive odd roots \(a\equiv a_*\pmod{2M}\) such that

\[
 \boxed{\delta_P(a)=b+4h+5j,
 \qquad \tau(a^2)=20+b+4h+5j.}
\]

The \(b=5\) family can additionally satisfy the earlier forcing condition \(T_{3,1}\mid a\). The \(b=11\) family can satisfy \(T_{11,1}\mid a\), including \(3\cdot5\cdot11\mid a\).

Consequently, **every integer \(s\ge13\)** occurs as an exact additional cost, together with exact total cost \(20+s\), infinitely often in this one old residual class. Equivalently, **every total cost \(N\ge33\)** is attained infinitely often with \(a\equiv a_*\pmod{2M}\).

These are sufficient thresholds, not claims of smallest possible thresholds. The argument also explicitly attains additional costs \(5,9,10,11\). It does not decide the attainability or impossibility of additional costs \(6,7,8,12\), or all costs below 5.

Two complete numerical examples are supplied: \((\delta_P,\tau)=(5,25)\) and \((9,29)\). The two general families are proved by induction and primitive prime existence; the finite symbolic skeleton checks do not replace that proof.

## 2. Old residual states and all twenty private odd witnesses

The complete old residue state is fixed, not merely its zero/nonzero indicator. For every \(a\equiv a_*\pmod{2M}\), every \(p\in P\), and every \(n\ge0\),

\[
 [F_n(a)]_p=[F_n(a_*)]_p.
\]

In this class the old dictionary covers all odd indices. Its common exponent period is 6720. The following table gives the exact base-2 order \(o_p\), the unique zero phase \(r_p\), and one odd index at which only \(p\) among the old twenty primes divides the term. The selected indices also avoid \(n\equiv2\pmod9\), which will exclude the only odd-order new channel in the five-prime seed.

| \(p\) | \(o_p\) | \(r_p\) | Number of private odd residues in one 6720 period | Selected private \(n_p\) |
|---:|---:|---:|---:|---:|
| 7 | 3 | 1 | 208 | 37 |
| 17 | 8 | 3 | 272 | 3 |
| 31 | 5 | 4 | 48 | 89 |
| 41 | 20 | 5 | 48 | 5 |
| 71 | 35 | 13 | 16 | 293 |
| 97 | 48 | 21 | 52 | 117 |
| 113 | 28 | 21 | 16 | 413 |
| 127 | 7 | 1 | 16 | 113 |
| 151 | 15 | 11 | 48 | 41 |
| 241 | 24 | 9 | 104 | 33 |
| 257 | 16 | 7 | 136 | 87 |
| 281 | 70 | 23 | 16 | 233 |
| 337 | 21 | 17 | 16 | 773 |
| 641 | 64 | 15 | 34 | 207 |
| 673 | 48 | 45 | 52 | 237 |
| 1321 | 60 | 17 | 48 | 257 |
| 14449 | 84 | 53 | 16 | 53 |
| 29191 | 105 | 68 | 16 | 593 |
| 65537 | 32 | 31 | 68 | 63 |
| 6700417 | 64 | 47 | 34 | 111 |

Every entry is checked directly from \(a_*\) and exact modular orders. In particular, the old cover is irredundant **on odd indices**. Merely having twenty old channels would not imply this; the private witnesses are essential to the new total-cost result.

For even indices write \(n=2u\). The set of old holes is periodic modulo 105:

\[
\begin{split}
H=\{&0,1,3,6,9,10,15,16,21,30,31,33,36,45,48,49,51,54,\\
&55,63,64,66,69,70,75,76,78,79,84,85,90,91,93,96,99,100\}.
\end{split}
\]

Thus no old prime divides \(F_{2u}(a)\) exactly when \(u\bmod105\in H\). The verifier checks this equivalence throughout the full old even-index period 3360, rather than inferring it from 105 sample values.

## 3. A general lemma that upgrades private witnesses to exact total cost

Suppose a finite dictionary \(S=P\sqcup Q\) has prescribed compatible root residues, covers all positive indices, and has a private positive index \(n_q\) for every \(q\in S\). Privacy means

\[
 q\mid F_{n_q}(a),\qquad
 p\nmid F_{n_q}(a)\quad(p\in S\setminus\{q\}).
\]

Assume the \(Q\)-private indices are also old holes, as in the constructions below. Define

\[
 D=\operatorname{lcm}_{q\ne r\in S}
       (2^{|n_q-n_r|}-1),
 \qquad
 E=\frac{D}{\prod_{p\in S}p^{v_p(D)}}.
\]

The indices are distinct: one index cannot be private to two different channels. The integer \(E\) is odd and coprime to every prescribed channel prime. Therefore the CRT can simultaneously impose the old root class, all new channel root residues, and \(a\equiv0\pmod E\).

**Pairwise coprimality.** If a prime \(\ell\) divided both \(F_{n_q}(a)\) and \(F_{n_r}(a)\), then \(\ell\nmid 2a\) and

\[
 \ell\mid 2^{|n_q-n_r|}-1\mid D.
\]

If \(\ell\in S\), the two privacy conditions rule this out. Otherwise \(\ell\mid E\mid a\), which would give \(F_n(a)\equiv-1\pmod\ell\), also impossible. Hence the \(|S|\) private terms are pairwise coprime.

Every prime cover of the whole sequence needs a different prime for each of these \(|S|\) pairwise-coprime terms. The displayed dictionary \(S\) is a cover of that size. Therefore

\[
 \tau(a^2)=|S|=20+|Q|.
\]

Likewise the \(|Q|\) private terms belonging to \(Q\) are pairwise coprime and have no old prime divisor. Every full cover needs at least \(|Q|\) primes outside \(P\). Since \(S\) supplies exactly that many,

\[
 \delta_P(a)=|Q|.
\]

For proper divisors it suffices to choose a positive solution \(a\) large enough that \(2a^2-1>\max S\). All sufficiently large members of the resulting CRT progression meet this condition. Thus the conclusion holds for infinitely many positive odd roots. No claim that an individual old prime must appear in every optimal cover is needed; the lower bound concerns distinct prime divisors of pairwise-coprime witness terms.

## 4. Two private distinct-modulus covers

The following congruence covers each cover all integers \(v\), and each class has a private residue:

| Pattern | Classes \(v\equiv b\pmod m\), written \((m,b)\) | Private residues, in the same order | Count increment on replacement |
|---|---|---|---:|
| Five classes | \((2,0),(3,0),(4,1),(6,5),(12,7)\) | \(2,3,1,11,7\) | 4 |
| Six classes | \((2,0),(3,0),(4,1),(8,3),(12,7),(24,23)\) | \(2,15,1,11,7,23\) | 5 |

These facts are finite equalities checked over periods 12 and 24 respectively. Their moduli are distinct within each pattern. If a parent class is \(u\equiv c\pmod d\), replacing it by

\[
 u\equiv c+db\pmod{dm}
\]

for every \((m,b)\) in a pattern covers exactly the parent class.

For each child take a prime \(q\) satisfying

\[
 \operatorname{ord}_q(2)=2dm,
 \qquad a\equiv 2^{-(c+db)}\pmod q.
\]

Then its even-index zero set is exactly the desired class, because \(\operatorname{ord}_q(4)=dm\). Its zero phase in the full exponent \(n\) is even, so it never divides an odd-index witness.

Existence follows from the classical primitive-prime result: for every integer \(t>6\), a prime of exact base-2 order \(t\) exists. The source used here is Lemma 2 of [the Filaseta et al. paper](https://people.math.sc.edu/filaseta/papers/SierpinskiEtCoPap5.pdf), which cites Bang (1886). All requested orders below exceed 6. The argument only uses that statement; it does not treat symbolic prime labels as numerical primality certificates.

The largest child modulus is \(12d\) or \(24d\). The phase must be carried as \(c+db\), reduced modulo the child modulus. There is **no assumption that \(c=d-2\)** after mixed refinements.

## 5. The five-prime seed and all costs \(5+4h+5j\)

The first seed is:

| \(q\) | \(\operatorname{ord}_q(2)\) | \(d=\operatorname{ord}_q(4)\) | \(c\) in \(u\equiv c\pmod d\) | Private \(u\in H\) |
|---:|---:|---:|---:|---:|
| 5 | 4 | 2 | 1 | 3 |
| 73 | 9 | 9 | 1 | 10 |
| 13 | 12 | 6 | 0 | 6 |
| 19 | 18 | 9 | 4 | 76 |
| 109 | 36 | 18 | 16 | 16 |

It covers every old hole. The common period with \(H\) is 630. The listed private residues show irredundancy in those old holes.

After \(h\) five-class and \(j\) six-class refinements of the current largest class, all extra periods divide

\[
 d=18\cdot12^h24^j,
\]

and the common period with \(H\) is \(L=35d\). Let \(w=c+dv_0\) be a private witness for the parent. Every

\[
 u=w+Lt
\]

remains an old hole and avoids every unaffected extra channel. In parent coordinates it has \(v=v_0+35t\). Since 35 is coprime to both 12 and 24, \(t\) can be chosen to give the private residue of any child pattern. Each child therefore obtains a private old-hole witness. Unchanged channels retain their old witnesses, since those lay outside the parent class.

Fresh primes cause no collision. At the first step the requested orders are either

\[
72,108,144,216,432
\]

or

\[
72,108,144,288,432,864.
\]

Neither list intersects the old orders or the seed orders. After the first step every new order is greater than \(2d\), which bounds every previously used order. Distinct moduli produce distinct orders and thus distinct primes.

The sole extra prime with odd order is 73, whose zero phase is \(n\equiv2\pmod9\). The private odd indices in Section 2 avoid it, and all other extra channels have even zero phase modulo even order. Thus **all twenty old private witnesses survive every refinement**.

The dictionary now has \(5+4h+5j\) extra channels and private witnesses for every old and new channel. Applying Section 3 proves both exact costs for \(b=5\).

## 6. The eleven-prime seed and its initial two-parity lift

The second seed, independently verified in the companion forbidden-small-primes work, is:

| \(q\) | \(\operatorname{ord}_q(2)\) | \(d\) | \(c\) | Private \(u\in H\) |
|---:|---:|---:|---:|---:|
| 13 | 12 | 6 | 0 | 6 |
| 19 | 18 | 9 | 1 | 10 |
| 73 | 9 | 9 | 7 | 16 |
| 37 | 36 | 18 | 3 | 3 |
| 109 | 36 | 18 | 15 | 15 |
| 61 | 60 | 30 | 1 | 31 |
| 433 | 72 | 36 | 9 | 9 |
| 38737 | 72 | 36 | 27 | 63 |
| 631 | 45 | 45 | 4 | 49 |
| 23311 | 45 | 45 | 40 | 85 |
| 181 | 180 | 90 | 76 | 76 |

This seed covers \(H\) with common period 1260 and avoids all primes at most 11. The verifier here checks the table independently from the exact residues and primality of the displayed numbers.

### Old odd private witnesses remain available

The only odd-order new channels have zero phases

\[
73:\ n\equiv5\pmod9;\qquad
631:\ n\equiv8\pmod{45};\qquad
23311:\ n\equiv35\pmod{45}.
\]

Take any old private odd index \(n_0\) and examine the three lifts \(n_0+6720t\), \(t=0,1,2\). They preserve every old state. The 73 condition eliminates at most one lift because \(6720\equiv6\pmod9\). The two order-45 phases are distinct modulo 15, while \(6720\equiv0\pmod{15}\), so at most one of the two order-45 conditions can apply to that fiber. Since \(6720\equiv15\pmod{45}\), that one condition eliminates at most one lift. At least one of the three lifts therefore avoids all three new odd-order channels. The remaining new channels never hit an odd index.

This supplies all twenty old private witnesses for the eleven-prime seed and for every subsequent refinement.

### First refinement: two parent fibers are necessary

The largest parent has \(d=90\), \(c=76\), and the old common period is \(L=1260=14d\). Here 14 is **not** invertible modulo 12 or 24, so the single-fiber argument from Section 5 cannot be copied unchanged.

The parent has, among others, private witnesses

\[
 u=76=76+90\cdot0,\qquad
 u=346=76+90\cdot3.
\]

They supply both parities of the parent coordinate \(v=(u-76)/90\). For a target private residue \(w_i\) of a child pattern, choose \(v_0=0\) when \(w_i\) is even and \(v_0=3\) when it is odd. With \(R=12\) or 24 solve

\[
 14t\equiv w_i-v_0\pmod R,
 \quad\text{equivalently}\quad
 7t\equiv\frac{w_i-v_0}{2}\pmod{R/2}.
\]

This is solvable because 7 is invertible modulo \(R/2\). The lifted \(u=u_0+1260t\) remains an old hole and avoids all unaffected channels, while becoming private to the intended child. Thus both refinement patterns work at the first step.

### Later refinements

After the first step all surviving extra periods, including the old period 36, divide the new maximum

\[
 d=90\cdot12^h24^j\quad(h+j>0).
\]

The common period with \(H\) is now \(L=7d\). Since 7 is coprime to 12 and 24, the ordinary single-fiber lifting argument applies at every later step. The requested first new prime orders are at least 360, greater than every old and seed order, and subsequent orders are likewise fresh.

The channel count is \(11+4h+5j\). All old and new private witnesses exist, so Section 3 gives exact \(\delta_P\) and exact total \(\tau\) for \(b=11\).

## 7. Preserving the earlier finite forcing conditions

Let

\[
 T_1=(2^{210}-1)\Big/\prod_{p\in P}p^{v_p(2^{210}-1)}.
\]

For every channel in either seed, its base-2 order does not divide 210. The same is true of every refined channel: in the five-prime family the new orders are divisible by 4, while 210 is not; in the eleven-prime family they exceed 210. Therefore no extra channel prime divides \(T_1\).

The \(b=5\) family may impose \(T_1\mid a\), retaining \(T_{3,1}\mid a\). The \(b=11\) family may additionally impose \(3\cdot5\cdot11\mid a\), because all its channels exceed 11, including every primitive prime with the requested orders. Thus it retains

\[
 T_{11,1}=\operatorname{lcm}(T_1,165)=5T_1\mid a.
\]

In either case combine the desired forcing integer with \(E\) by their least common multiple. It remains coprime to the old and new prescribed primes and to 2, so the same CRT argument applies. These fixed finite forcing claims do not imply compatibility with arbitrary \(B,m\).

## 8. Why every additional cost at least 13 is attained

The two families supply four consecutive starting values:

| Additional cost \(s\) | Seed \(b\) | Five-class refinements \(h\) | Six-class refinements \(j\) |
|---:|---:|---:|---:|
| 13 | 5 | 2 | 0 |
| 14 | 5 | 1 | 1 |
| 15 | 5 | 0 | 2 |
| 16 | 11 | 0 | 1 |

Adding any number of five-class refinements adds a multiple of 4. Each integer \(s\ge13\) is one of these four starts plus a nonnegative multiple of 4. The resulting exact total cost is always \(20+s\).

Using only the five-prime seed would give the weaker sufficient threshold 17. The eleven-prime seed supplies the missing congruence-class start at 16 and lowers the proved sufficient threshold to 13.

## 9. Numerical certificates and native project verification

`verify_total_cost.py` checks four immutable project source blobs at commit
`b1efc6c805661ed7b476e6e730107da6043176ee` before importing the native BRC implementation:

| Module | Git blob SHA-1 |
|---|---|
| `brc_transport.py` | `be1debe367263931bd5e93fd750be3ed54624fe1` |
| `brc_histogram.py` | `9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1` |
| `brc_rational_holonomy.py` | `2591640fe348da9cd7f293a957bea9ae92c82943` |
| `brc_weighted_recurrent.py` | `4e6b3132580e3cd70a20a0d8bd4d28792b961afb` |

The native singleton positive packet is

\[
 x\longmapsto2x+1,\qquad x_0=a^2-1,
\]

whose second iterate is \(x\mapsto4x+3\). Every selected term is generated by this actual native packet; packet weight and multiplicity remain 1. The fixed X6 anchor is unchanged, the arithmetic index is not physical time, and residue classes are not spatial axes. The number of dictionary primes is a cover statistic, not the number of native branches.

| Numeric family | Root digits | Exact \(\delta_P\) | Exact \(\tau\) | Full exponent period checked | Pairwise gcd checks |
|---|---:|---:|---:|---:|---:|
| Five-prime seed | 9671 | 5 | 25 | 20160 | 300 |
| One five-class refinement | 35169 | 9 | 29 | 60480 | 406 |

For the second row the explicit new primitive primes of orders \(72,108,144,216,432\) are respectively

\[
 433,\quad246241,\quad577,\quad33975937,\quad209924353.
\]

The nine extra private even-index coordinates are

\[
 u=(3,10,6,76,160,70,1114,430,574).
\]

Both complete roots and complete root-progression moduli are saved in `total_cost_certificate.json`; no giant integer must be copied from prose. The certificate also records canonical CRT inputs, witness indices, exact orders, D/E/T sizes and hashes, removed valuations, every pairwise gcd, all witness term hashes, and native-source pin checks. The default run verifies 62 symbolic skeletons, covering both seeds and every pattern word of length 0 through 4. All these private-witness checks pass. The arbitrary-depth assertion rests on Sections 5 and 6.

To reproduce from the project root with the pinned source files available:

```bash
python v6_total_work/verify_total_cost.py
```

The exact numerical roots in this file are **new CRT roots** obtained by strengthening the forcing conditions. This does not claim that the preceding v5 numerical root already had total cost 25, or that the earlier eleven-prime numerical root already had total cost 31 without the expanded coprimalization.

## 10. Interpretation within the residual-observer question

The old complete residual trajectories and the native positive packet are fixed throughout these families. Nevertheless the exact additional cover cost and exact total cover cost attain every integer in the proved cofinite ranges. Therefore those old twenty residual channels alone cannot determine the quantitative finite-cover complexity.

The new structural ingredients are explicit: private witness classes, covers of the old-hole set, compatible prime orders, and CRT coprimalization of all selected terms. They provide a rigorous sufficient construction for this square-root class. The theorem does not establish that every Riesel number has a finite cover, that every Riesel number arises from the same construction, or that one informal notion of residual embedding is a necessary-and-sufficient explanation for all Riesel numbers.
