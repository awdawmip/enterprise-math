# R5 independent derivation of the six-cone pole envelope and exact S4 threshold transfer

Date: 2026-11-23 (Asia/Shanghai). Status: AUTHOR_REDERIVED_EXACT_LEMMA / INDEPENDENT_INTEGER_ENUMERATION / NOT_REVIEWED. **This is not an independent Driver review or formal Result.** Frozen scientific inputs are unchanged: awdawmip/enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Scope: five-event *scalar* union observer; no native X6/P000 promotion.

## Scope and new contribution

The previously archived global eight-regime period claim depends on the six-cone root-of-unity pole-degree bound, and the 2026-11-22 S4 derivative audit found an incorrect product-of-(1-q^(mp)) implementation in several older first-jet certificates. This note re-derives the six-cone denominator and its **no-finite-prefix** polynomial degree bound directly from the exact three-overlap incidence, with a separate, small integer-only re-enumeration of all 12 relevant orders. It also supplies an independent rational derivation of the **correct total-item-count S4 transfer**, distinguishing the cases where an S4 price is divisible by the root order and where it is not.

It independently confirms the conditional *degree lemma* used to extend corrected finite jets to all thresholds. It does not recheck all corrected 228 jet vectors, and it does not independently re-prove the 29/32/43 cancellation tables or admit the eight-regime theorem.

## Exact joint-U threshold generating series

Let U={214,...,221}. Shared prices 216,217,218 contribute the load u; put x=a214, y=a215, j=a219+a220+a221. The three event loads are s0=x+y+u, s1=x+u+j, s2=y+u+j, and their minimum is exactly

\[
\min(s_0,s_1,s_2)=u+x+y+j-\max(x,y,j).
\]

For any integer load b≥0, summing the predicate b<m over all positive m gives
\[
\sum_{m\ge1}{\bf1}_{b<m}t^{m-1}=\frac{t^b}{1-t}.
\]
The union numerator of these three events is A_m(q)=D_U(q) times the generating sum with this minimum-load predicate, where \(D_U(q)=\prod_{p=214}^{221}(1-q^p)\). Therefore as a formal rational identity
\[
G_A(t,q):=\sum_{m\ge1}A_m(q)t^{m-1}
=\frac{D_U(q)}{(1-t)\prod_{v=216}^{218}(1-q^vt)}
\sum_{x,y,j\ge0}q^{214x+215y}h_j(q^{219},q^{220},q^{221})
t^{x+y+j-\max(x,y,j)}. \tag{1}
\]
No factorization of the three *events* is used.

For any primitive dth root z with d≥7, the three residues 219,220,221 are distinct. The complete homogeneous polynomial has the exact Lagrange partial fraction
\[
h_j(z^{219},z^{220},z^{221})
=\sum_{r=219}^{221}\beta_r(z)z^{rj},\qquad
\beta_r(q)=\prod_{\substack{r'\in\{219,220,221\}\\r'\ne r}}
(1-q^{r'-r})^{-1}.
\]
All beta denominators are nonzero at z (differences ±1,±2).

Fix r and abbreviate the three weights \(X_i=q^{p_i}\) for \(p_i=(214,215,r)\). Split all nonnegative triples (x,y,j) into six order cones, sorting coordinates by descending *integer value*, and breaking ties by the ascending fixed label order (214,215,r). For a permutation (a,b,c) of these weights, write the ordered coordinates as A≥B≥C. Define δ1=1 if label(a)>label(b), else 0; δ2=1 if label(b)>label(c), else 0. The tie rule is equivalent to the disjoint and exhaustive constraints A−B≥δ1, B−C≥δ2, C≥0. Consequently each cone has the **exact** rational sum
\[
\sum_{\rm cone}a^A b^B c^C\,t^{B+C}
=\frac{a^{\delta_1}(ab\,t)^{\delta_2}}
{(1-a)(1-ab\,t)(1-abc\,t^2)}. \tag{2}
\]
Proof: set A−B=δ1+i, B−C=δ2+j', C=k with i,j',k≥0, then sum three geometric series. The power \(t^{B+C}\) equals \(t^{\delta_2+j'+2k}\). The six cones are disjoint, including ties; their union is all triples.

In (1) the pure q factor \(1-a\) from (2) cancels *algebraically* against its own factor in D_U(q), since the selected largest weight a is always one of q^214,q^215,q^219,q^220,q^221. This must be done **before** q is specialized to z or differentiated. The resulting individual rational term has a numerator of t-degree at most one and t denominator
\[
(1-t)\prod_{v=216}^{218}(1-q^vt)
(1-q^{p_a+p_b}t)(1-q^{214+215+r}t^2). \tag{3}
\]
At q=z it is well-defined; all surviving pure-q denominators beta_r are nonzero. Its denominator has total t-degree seven and numerator degree at most one, so it is strictly proper. Taking the Euler q derivative changes a single t-factor pole order by at most one and preserves strict properness. Thus **no initial-polynomial/finitely-many-exception term** arises in the threshold coefficient sequence.

## Independent root collision count and all-h polynomial consequence

For t=exp(2πij/(2d)), 0≤j<2d, one of the five linear factors of (3), with n in {0,216,217,218,p_a+p_b}, vanishes exactly when
\[
j+2n\equiv0\pmod{2d}.
\]
The quadratic factor vanishes exactly when
\[
j+214+215+r\equiv0\pmod d.
\]
Maximizing the number of simultaneously vanishing denominator factors over j, r∈{219,220,221}, and all six permutations gives the *pole-order upper envelope* μ_d in the following table. This is an upper bound on actual poles; numerator cancellations may reduce the true order.

| d | 7 | 9 | 11 | 13 | 16 | 17 | 19 | 23 | 25 | 27 | 31 | 37 |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| μ_d | 3 | 3 | 3 | 3 | 2 | 2 | 2 | 1 | 2 | 3 | 3 | 2 |

The accompanying Python 3 standard-library program VERIFY_POLE_ENVELOPE.py independently enumerates 18·(2d) candidate cone-root configurations per order (three r choices, six permutations, 2d root indices). It reproduces all 12 μ values, supplies a maximizing witness for each, and checks the three shared-zero factor cases, with no floating point arithmetic.

All poles divide 1−t^(2d), and the rational terms and Euler derivatives are strictly proper. Therefore partial fractions show that for every r0∈{1,...,2d} and **every h≥0**, the threshold sequences A_(r0+2dh)(z) and dot A_(r0+2dh)(z) are polynomials in h of degrees at most μ_d−1 and μ_d respectively. This is an all-h consequence, not extrapolation from a few input points.

For d∈{7,27,31}, the common-U prices 217,216,217 respectively are divisible by d, whereas 214,215,219,220,221 are not. After the algebraic cancellation above, the prefactor D_U/(1-a) still vanishes at z. Hence A_m(z)=0 identically; its Euler derivative comes only from differentiation of the zero prefactor, without a new t denominator. In those three cases dot A_(r0+2dh)(z) has the **sharper** degree bound μ_d−1=2. This verifies the load-bearing degree refinement used for the corrected d31/r59 three-point reconstruction.

## True S4 transfer and its independent phase consequences

Let Z={296,...,312} and D_Z(q)=∏(1−q^p). The exact one-event threshold numerator is
\[
C_m(q)=D_Z(q)\sum_{n=0}^{m-1}h_n((q^p)_{p\in Z}),
\]
not \(\prod_{p\in Z}(1-q^{mp})\). Its threshold series is
\[
G_C(t,q)=\sum_{m\ge1}C_m(q)t^{m-1}
=\frac{D_Z(q)}{(1-t)\prod_{p\in Z}(1-q^p t)}. \tag{4}
\]

For any d≥17, Z has 17 pairwise distinct residues modulo d. At a primitive dth root z let \(E_d=\{p\bmod d:p\in Z\}\) and \(P_d(t)=\prod_{a\in\{0,\ldots,d-1\}\setminus E_d}(1-z^a t)\). Exactly
\[
\prod_{p\in Z}(1-z^p t)^{-1}=\frac{P_d(t)}{1-t^d}. \tag{5}
\]

* If 0∈E_d (exactly one Z-price divisible by d), D_Z(z)=0 and the **true Euler first jet** is
\[
\sum_{m\ge1}\dot C_m(z)t^{m-1}
=\frac{\dot D_Z(z)P_d(t)}{(1-t)(1-t^d)}. \tag{6}
\]
This is strictly proper. On each fixed m mod d, dot C is a polynomial of degree ≤1 in the nonnegative step h, with no finite-head exception. For d=17, E_d is all residues, P_d=1 and (6) gives the exact previously repaired identity \(\dot C_m(z)=-5202\lceil m/17\rceil\).

* If 0∉E_d, D_Z(z)≠0 and P_d(t) contains exactly one factor 1−t. Its cancellation in (4) yields
\[
G_C(t,z)=\frac{D_Z(z)\,P_d(t)/(1-t)}{1-t^d}. \tag{7}
\]
The numerator degree is d−18, so C_m(z) is d-periodic and equals zero whenever m mod d∈{0,d−16,...,d−1}. This directly verifies the S4 tail-zero input to the primitive-29 and primitive-32 cancellation proofs (both have 0∉E_d), *using the actual total-item-count semantics*.

For d<17 with at least two Z-prices divisible by d, D_Z and its Euler first derivative both vanish at z, independently of the finite homogeneous prefix. This covers d=7,11,13 used in the earlier jet witnesses.

## Evidence and exact limitations

The independent integer collision count reproduces all 12 denominator upper envelopes. Equation (2) is an explicit six-cone bijection; equations (4)–(7) are exact rational identities that exclude the previously identified S4 substitution. The re-derivation establishes the pole-degree and S4 phase-transfer lemmas as an author-side alternative proof, not as an independent expert review of the original authors' results.

The global 8-regime least-period formula remains an AUTHOR_CONDITIONAL_COROLLARY / NOT_REVIEWED because its nonzero cyclotomic certificates and the 29/32/43 root-specific cancellation phases are separate dependencies not independently discharged by this note. The corrected 2026-11-22 d31 and d17 evidence remains preserved at the immutable f5ef1521... commit; no old file or attribution is overwritten. Research-Activity and formal CLAIM/RUN/Result/Review are separate.

Next discriminating unit: independent verification of the primitive-29/32 full *joint* phase tables using the exact C transfer (not the incorrect substituted product), followed by direct recomputation of any affected 16/19/25/27/31 jet vectors with a mutually independent implementation.

References (immutable):
- Frozen R5 scope: enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15.
- Original six-cone denominator and μ table: enterprise-math@e0176cd68a434192899a5a1de746c2c66b5946dc, research_notes/portable_direct/r5_q_pole_collision_20261122/RESEARCH.md.
- Exact S4 substitution counterexample and d31/d17 corrections: enterprise-math@f5ef1521521888705104239328bbc1e6c62219db, research_notes/portable_direct/r5_cblock_jet_audit_20261122/.
- 29/32 all-m proof: enterprise-math@74c74c94d7971bdd8594824b734e574f85d43fd2, research_notes/portable_direct/r5_allthreshold_29_32_20261122/.
