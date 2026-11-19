# R284AM — Exterior-tensor span DP: deterministic principal rank without enumerating all principal subsets

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Predecessors: R284AL (AL1–AL4), R284AK (AK1–AK5), R284AJ (AJ1), R284AE. Frozen scientific input remains 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Scope: auxiliary rational, independently named Port-edit observations. P000, ACTIVE Heartbeat X6, joint observer and provenance constraints remain unchanged. No native time dynamics, physical claim or future-operation-safe state compression asserted.

## Theorem AM1

Let U,V be arbitrary rational m-by-r matrices (m,r>=1), C=UV^T, and d(C)=max{|S|: det(C[S,S]) != 0}, with d=0 if every nonempty principal minor vanishes. There is a **deterministic exact** algorithm computing d(C), a real nonzero principal-minor witness when d>0, and a spanning certificate proving all larger principal minors vanish. Its conservative arithmetic-operation bound is

D = Σ_{j=0}^r binom(r,j)^2 = binom(2r,r) <= 4^r,
O(m poly(r) D^3).

Thus principal-rank detection for a supplied rational factorization is fixed-parameter tractable (FPT) in factor width r, with polynomial rational bit complexity as a function of m, D, r and input bit length. No random weights or enumeration of all binom(m,r) principal subsets is needed. The result holds for signed, nonsymmetric and rank-deficient factors.

## Proof: paired exterior reachability

For each input row i let u_i,v_i in Q^r. For 0<=j<=r let

W_j = (wedge^j Q^r) tensor (wedge^j Q^r),  dim W_j = D_j = binom(r,j)^2.

For an increasing named subset S={i_1<...<i_j}, define the genuine subset state

z_S = (u_(i_1) wedge ... wedge u_(i_j)) tensor (v_(i_1) wedge ... wedge v_(i_j)).

In standard wedge bases indexed by j-element column sets J, the two coordinates are det(U[S,J]) and det(V[S,J]). Define the linear contraction ell_j(x tensor y) = Σ_{|J|=j} x_J y_J. Cauchy–Binet gives

ell_j(z_S) = Σ_{|J|=j} det(U[S,J])det(V[S,J]) = det(C[S,S]).     (AM1a)

Let L_j(i) be the linear span of all z_S with |S|=j and S subset of {1,...,i}. Let E_i:W_(j-1)->W_j append u_i in the first exterior factor and v_i in the second, in that order. Because the same insertion order is used in both wedge factors, no sign reversal arises. Splitting subsets according to whether index i is present proves the **exact recurrence**

L_j(i) = L_j(i-1) + E_i L_(j-1)(i-1),                    (AM1b)

with L_0(i) spanned by 1⊗1 and L_j(0)=0 for j>0.

Store at each grade a row-echelon basis consisting **only of original subset states** z_S and their full named index sets S. For each new i, process grades in descending order and insert E_i images of the previous grade's stored basis, keeping only independent candidates. By linearity of E_i and (AM1b), every omitted dependent state has all future images represented by the retained span. Induction on i proves that the maintained basis spans precisely L_j(i).

At i=m,

some S of size j has det(C[S,S]) != 0  iff  ell_j restricted to L_j(m) is not zero.   (AM1c)

Test ell_j on the stored basis vectors. A nonzero contraction gives an actual S and exact determinant witness. If every basis contraction is zero, linearity certifies that **every** j-principal minor is zero, including those not enumerated. The largest nonzero grade is exactly d(C). This proof preserves paired signed Plücker data and does not replace them by positive mass or scalar support.

## Costs and negative-certificate verification

The sum of all basis sizes is bounded by D, independent of m. At most mD candidate subset states are examined; each vector is assembled from exact j-minors of the factor rows, then reduced against a D_j-dimensional rational echelon basis. A conservative total arithmetic bound is O(m poly(r) D^3), with O(D^2+rD) working field words plus the input. The factor-rank dependence is exponential; this is not a uniform polynomial-in-r algorithm or a general black-box PIT derandomization.

For rational factor entries of at most B bits, common-denominator scaling, wedge determinant formation and exact echelon elimination have standard polynomial integer-height/minor bounds in m,D,r,B. A fraction-free implementation provides polynomial total bit complexity in these quantities. The supplied reproducible checker uses Python Fraction arithmetic and is not a fraction-free performance benchmark.

A negative certificate consists of each grade's original subset-state basis, its zero contractions at grades above d, and a verifiable recurrence/closure transcript (or exact rerun of (AM1b) from the stated U,V). Only the final vanishing contractions, without proving spanning, are insufficient.

For the earlier independently named two-layer Port pencil M_C(u,v)=[[diag(u),I_m],[C,diag(v)]], the proved identity det M_C=det(diag(u_i v_i)-C) entails

first_nonzero_total_degree(det M_C) = 2(m-d(C)).

AM1 therefore supplies a deterministic exact degree detector for this auxiliary Port family, with no stochastic misdetection.

## Reproducible exact validation

Companion script: R284AM_exterior_span_principal_rank_checker.py. Companion output: R284AM_exact_verification.json.

- 150 seeded strictly positive integer-factor pairs, 2<=m<=8 and 1<=r<=min(m,4), compared against complete independent principal-minor enumeration.
- 4,692 explicit true-subset membership checks against the computed grade spans.
- 105 further signed integer-factor pairs checked against full principal-minor enumeration, including a nilpotent rank-one example with d(C)=0.
- R284AL cancellation example: d=2, witness S={1,2}, principal determinant +1.
- R284AK strict-positive nonsymmetric rank-gap constructions k=2,3,4: d=2, witnesses with exact determinants -2,-3,-4 respectively, and every higher grade has zero reachable span.
- Separate m=64,r=3 strictly positive-factor instance: d=3, witness determinant -8605076592, 1,136 candidate states, total ambient span bound 20. This last case has no exhaustive subset enumeration.

All completed local exact tests PASS. Finite computation validates implementation and selected examples; the general theorem follows from (AM1a)–(AM1c). Independent mathematical review: NOT_REVIEWED.

## Scientific interpretation and next work

This gives a deterministic upper/lower *principal-rank certificate* in the sign-cancellation regime left open by R284AL. It is an **observation diagnostic**, not permission to eliminate named paths, joint branches or future Port operations. R284AK and R284AL are directly reused; no claim of global literature novelty is made, nor any formal CLAIM, Result, Review or P000 modification.

Next: implement fraction-free incremental basis with an auditable compact closure transcript; benchmark total input factorization, exact bit growth, reductions and witness extraction against naive principal-minor enumeration and AL2/AL3 weighted probes as m,r and input bits vary. Investigate whether a smaller invariant quotient preserves the declared Port observer and its permitted future edits exactly.
