# R5 — Genuine joint-load root phases at 23 and 25 (precision O_m(N²))

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_EXACT_DERIVATION / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED. Independent portable scientific note; no new CLAIM/RUN, official Result or Review.

## Theorem A — exact all-threshold root classification

Use the **frozen R5 scalar observer**, with prices 214,...,314 and original failure supports
S0={214,215,216,217,218},
S1={214,216,217,218,219,220,221},
S2={215,216,217,218,219,220,221},
S3={223,...,290},
S4={296,...,312}.
For threshold m>=1, event Ei means its **own** total multiplicity on Si is strictly below m. All selected event inequalities are jointly retained in an intersection.

Let F_m(q)=R_m(q)/D(q) be the original inclusion-exclusion failure-count generating function, with D(q)=product_{p=214}^{314}(1-q^p). For any primitive roots ζ23 and ζ25, the following statements are **exact for all m>=1**:

\[
R_{m+46}(\zeta_{23})=R_m(\zeta_{23}),\quad
R_m(\zeta_{23})=0\iff m\bmod46\in\{0,42,43,44,45\}.
\]

\[
R_{m+50}(\zeta_{25})=R_m(\zeta_{25}),\quad
R_m(\zeta_{25})=0\iff m\bmod50\in\{0,46,47,48,49\}.
\]

The 23rd-root sequence has 41 nonzero phases out of 46; the 25th-root sequence has 45 nonzero phases out of 50. In the 5 exceptional phases for either root, the entire integer cyclic coefficient vector vanishes, not merely an approximate evaluation.

**Corollary B — conditional exact O_m(N²) period.** Assume the preceding not-yet-independently-reviewed all-threshold author theorem
\[
M_m(O_m(N^3))=L_3=232\,792\,560\qquad(m\ge1).
\]
Then, for *every* m>=1,
\[
\boxed{M_m(O_m(N^2))=L_3\,23^{e_{23}(m)}\,5^{e_{25}(m)}}
\]
where e23 is 0 on the above five residue classes mod 46 and 1 elsewhere, and e25 is 0 on the above five residue classes mod 50 and 1 elsewhere. The classification repeats modulo lcm(46,50)=1150.

| Extra factors above L3 | Period (conditional) | Classes / 1150 |
|---|---:|---:|
| Neither | 232,792,560 | 13 |
| 23 only | 5,354,228,880 | 102 |
| 5 only | 1,163,962,800 | 112 |
| 23 and 5 | 26,771,144,400 | 923 |

In particular m=46 gives M_46(O(N²))=232,792,560 conditional on the preceding L3 theorem, whereas m=1 gives 26,771,144,400 conditional on the same theorem. The root zeros at m=46 are **unconditional results within the frozen finite model**, independent of L3.

## Genuine load reduction

At the two primitive roots, S3 and S4 each contain a multiple of the corresponding order: for 23 these include 230 and 299, and for 25 they include 225 and 300. Hence every original 31-mask inclusion-exclusion term involving either of those events vanishes because its numerator prefactor contains (1-q^p) for a multiple of d. This exact root-observer-specific reduction leaves the seven nonempty masks of S0,S1,S2; it does **not** replace joint event inequalities by a union inequality.

Let x=a_214, y=a_215, u=a_216+a_217+a_218 and j=a_219+a_220+a_221. The three event loads are exactly
\[
L_0=x+y+u,\qquad L_1=x+j+u,\qquad L_2=y+j+u.
\]
For a nonempty I subset of {0,1,2}, let P_{I,m}(q) sum the finite q-weights of assignments subject to **each** original bound Li<m for i in I; put C_I(q)=product_{p in union_{i in I}Si}(1-q^p). Then
\[
R_m(q)=\sum_{I\ne\emptyset}(-1)^{|I|+1}C_I(q)P_{I,m}(q)
\quad(q=\zeta_{23},\zeta_{25}).
\]

## Exact rational threshold generating function

Write a=q^214, b=q^215, U(t)=product_{p=216}^{218}(1-q^p t)^{-1}, J(t)=product_{p=219}^{221}(1-q^p t)^{-1}, and w_i=q^{218+i} (i=1,2,3). Define
\[
C(s,w;t)=\frac{1-swt^2}{(1-st)(1-wt)(1-swt)},\qquad
\gamma_i=\prod_{\ell\ne i}(1-w_\ell/w_i)^{-1},
\]
so J(t)=sum_i γ_i/(1-w_i t) at either primitive root. These coefficients are well-defined because the w_i are distinct. Let B_I(t) sum over the x,y,j variables present in selected event unions, weighting by t to the maximum selected load **after removing the common u**. Exact cone partitioning gives

\[
\begin{aligned}
B_0&=\frac1{(1-at)(1-bt)},&
B_1&=\frac{J(t)}{1-at},&
B_2&=\frac{J(t)}{1-bt},\\
B_{01}&=\frac1{1-at}\sum_i\gamma_i C(b,w_i;t),&
B_{02}&=\frac1{1-bt}\sum_i\gamma_i C(a,w_i;t),&
B_{12}&=J(t)C(a,b;t),\\
B_{012}&=\sum_i\frac{\gamma_i}{1-abw_i t^2}
\left[
\frac1{(1-bt)(1-w_i t)}
+\frac{at}{(1-at)(1-w_i t)}
+\frac{ab t^2}{(1-at)(1-bt)}
\right].
\end{aligned}
\]

For B012, max(x+y,x+j,y+j)=x+y+j-min(x,y,j). Its three terms correspond to the tie-disjoint regions x<=y,j; y<x,y<=j; and j<x,j<y. The two-variable identity C partitions a pair by which is larger. This proves the identity without discarding intersection provenance.

Summing the common u-series and the threshold tail m>max Li yields
\[
\boxed{\sum_{m\ge1}R_m(q)t^{m-1}=
\frac{U(t)}{1-t}\sum_{\emptyset\ne I\subseteq\{0,1,2\}}
(-1)^{|I|+1}C_I(q)B_I(t).}
\]

Each rational denominator factor is (1-q^p t), (1-q^v t²), or (1-t). Therefore all poles are 2d-th roots of unity. A full modular root-overlap audit of the decomposed terms proves that for d=23 every pole is simple. For d=25, the sole candidate repeated pole is t=1 in the w=q^221 triple-intersection component: q^(214+215+221)=q^650=1. Its bracket has common numerator
\[
(1-at)+at(1-bt)+ab t^2(1-wt)=1-abw t^3=1-t^3.
\]
This cancels the factor (1-t) from the quadratic denominator (1-t²), removing that would-be double pole before multiplication by the external 1/(1-t). Thus the full rational series is proper and every pole is simple at a 46th root (d=23) or a 50th root (d=25). Partial fractions establish **both periodic identities for all thresholds**, without assuming finite tests imply infinite conclusions.

## Exact phase certificates, verification and implications

The complete exact integer cyclic-ring computation covers m=1,...,92 for d=23 and m=1,...,100 for d=25; two consecutive blocks of length 46 and 50 agree, even as full cyclic vectors. The first blocks give the exact 5 exceptional phases above. At a primitive 23rd root, the integer residue vector v of length 23 vanishes exactly when all coordinates are equal, by Φ23(q)=1+...+q^22. At a primitive 25th root, v vanishes exactly when each of the five modulo-5 coordinate classes has equal entries, by Φ25(q)=1+q^5+q^10+q^15+q^20. Every remaining phase has an explicit nonzero integer normal-form coordinate. The original m=1 witnesses (c0,c1)=(1,6) at 23 and (c0,c5)=(4,-3) at 25 are reproduced.

The independent direct checker iterates the **original selected event inequalities**, not the cone generating formula, and matches full vectors at d=23: m=1,2,3,23,42,46 and d=25: m=1,2,3,25,46,50. It confirms zero vectors, including m=46 for both orders. All calculations use exact integer arithmetic; for m<=100, the absolute combinatorial bound 7*2^8*binom(2m+8,8)<1.36e17 is below signed 64-bit capacity.

Both d=23 and d=25 have exactly four vanishing denominator factors in D(q), so a nonzero numerator creates an order-4 pole, necessary for the N^3 coefficient period; a zero numerator removes that order at all primitive roots in its phase. All other possible order-4 contributors are already divisors of L3, except d=27,31 whose removal was proved independently in the predecessor. This and the inherited all-m O(N³) equality yield Corollary B. The corollary retains its **explicit dependence** on prior author-side work that has not undergone independent Review.

Source pins: enterprise-math@02ecdefc1118a25e4ca9038059810e6c472e7c10 (previous O(N²) m=1 proof); enterprise-math@2c995f1106ecd67a5896a9d1aad257fbd485d116 (all-m L3 author theorem); genuine-event correction @75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Science inputs stay frozen. P000 and ACTIVE worldview are unaffected; the finite scalar observer is not asserted to be a complete native X6 Cell model. No formal shared Task completion or mathematical acceptance has occurred.

**Next research unit:** independently audit the inherited O(N³) all-m theorem and the current rational pole/cyclotomic normal-form proof, then study residual transitions at the 13 simultaneous missing-factor phases.