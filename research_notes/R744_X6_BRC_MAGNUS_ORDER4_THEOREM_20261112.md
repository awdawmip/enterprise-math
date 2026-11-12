# R744 — Fourth-order integer BRC word signature restores hidden X6 connector order

Date: 2026-11-12, Asia/Shanghai. Author-side mathematical theorem, exact X6 signed-axis path carrier. Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS (TP2-8B7E13C5904A2D6F1142). Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior result: R743 (PR #2148; commit 2b4a22960e7efab0153ccca0c3f7d569d2d424b6).

## 1. Exact BRC branch population and observation

Choose a chart-relative X6 Cell and a set I of r distinct connector axes disjoint from two loop axes a,b, with 2 <= r <= 4 in native X6. Each connector permutation sigma determines a distinct positively counted, identity-labeled branch

  w_sigma = c_sigma L c_sigma^{-1},
  c_sigma = (+sigma_1,...,+sigma_r),
  L = (+a,+b,-a,-b).

The inverse connector is the reverse word with opposite step signs. All r! branches are rooted closed paths of length 2r+4, have no immediate inverse cancellation, and have the same nonzero signed coordinate edge-current. The square is based at the common connector endpoint, independent of sigma. This reuses the proven R743 path/current carrier. Branch multiplicity is one; counting these branches is an N-BRC-style provenance count, while the signed polynomial observer defined below is distinct from positive BRC mass or any native force law.

The future-operation question is exact recovery of the ordered connector branch from a compact *algebraic observer*, rather than from the erased signed edge-current.

## 2. Finite integral noncommutative observer

Let A = Z< X_0,...,X_5 > / (all words of length >= 5) be the free associative integer algebra truncated after word degree four. Define the multiplicative map Phi on signed native-axis words by

  Phi(+i) = 1+X_i,
  Phi(-i) = 1-X_i+X_i^2-X_i^3+X_i^4.

The last polynomial is the exact multiplicative inverse of 1+X_i in A. Thus Phi(path concatenation)=ordered multiplication, Phi(w^{-1})=Phi(w)^{-1}, and relabeling any of the six axes commutes with Phi. The construction is finite integer word arithmetic, using no continuum trigonometry or classical time propagator. It is an explicitly defined symbolic BRC branch-observer extension, not a native V39 operator.

Define the observable O_d(w) to be the coefficients of Phi(w) in word degrees <= d.

## 3. Main theorem — exact first separation degree

For every 2 <= r <= 4 and every two connector permutations sigma,tau:

(A) O_3(w_sigma) = O_3(w_tau): every connector permutation has the same word coefficients through degree three.

(B) For every two distinct connector axes i,j in I,

  [X_i X_j X_a X_b] Phi(w_sigma) =
      1  if i occurs before j in sigma,
      0  if j occurs before i in sigma.

Here [word] means its exact integer coefficient. Consequently the degree-four signature determines every pairwise precedence relation, hence sigma uniquely. Therefore the minimum degree among this fixed hierarchy of word-signature observers which separates all r! branches is exactly four.

(C) The entire construction is S6-equivariant under axis-label permutations: relabel both the path and formal variables, including the designated loop-axis pair. This provides a natural covariant branch-recovery signature rather than a chosen noncovariant path index.

## 4. Algebraic proof

Write U=X_a, V=X_b and ell = Phi(L). Because Phi(L) is the commutator (1+U)(1+V)(1+U)^{-1}(1+V)^{-1}, its constant term is 1, its degree-one part vanishes, and

  ell = 1+ell_2+ell_3+ell_4,
  ell_2 = UV - VU,

where ell_3,ell_4 use only U,V and are independent of sigma.

Write C_sigma=Phi(c_sigma)=1+c_1+c_{2,sigma}+higher degrees, with

  c_1 = sum_{i in I} X_i,
  c_{2,sigma} = sum_{p<q} X_{sigma_p} X_{sigma_q}.

The linear term c_1 does not depend on sigma. Its inverse has, through degree two,

  C_sigma^{-1} = 1-c_1+(c_1^2-c_{2,sigma})+higher degrees.

Since Phi(w_sigma)=C_sigma ell C_sigma^{-1}, collect homogeneous degrees:

  degree 0 = 1,
  degree 1 = 0,
  degree 2 = ell_2,
  degree 3 = ell_3 + c_1 ell_2 - ell_2 c_1,

so all coefficients through degree three are common to every sigma. At degree four,

  degree 4 = ell_4 + c_1 ell_3 - ell_3 c_1
           + c_{2,sigma} ell_2 - c_1 ell_2 c_1
           + ell_2 c_1^2 - ell_2 c_{2,sigma}.

Only the commutator [c_{2,sigma},ell_2] depends on the connector order. For distinct connector axes i,j and loop axes a,b, a term beginning with X_i X_j and ending with UV can only come from c_{2,sigma} ell_2. Its coefficient is precisely the coefficient of X_iX_j in c_{2,sigma}, which equals the indicator that i precedes j in sigma. This establishes (B).

A total ordering of labeled distinct axes is uniquely determined by all its pairwise precedence relations. Since r>=2 yields at least two different permutations sharing O_3, degree four is both necessary and sufficient within the O_d hierarchy. This proves (A),(B). Formula Phi(+i),Phi(-i) is functorial under substitutions X_i -> X_{pi(i)} for pi in S6, establishing (C).

The proof uses only exact identities in the truncated noncommutative integer algebra; it applies unchanged for any larger signed-axis carrier with at least r+2 distinct axes.

## 5. Exact finite tests / reproducibility

Verifier: research_notes/R744_X6_BRC_MAGNUS_ORDER4_VERIFY.py (Python 3 standard library, integer dictionary-of-words algebra).

For r=1,2,3,4 respectively, it checks all 1,2,6,24 permutations. All signatures have one shared degree-<=3 class, while the degree-<=4 classes number respectively 1,2,6,24. Within each r, signed edge-current has one class. The ordered-pair coefficient formula is checked on 0,4,36,288 ordered pairs (328 total). For r=4 the five adjacent-transposition generators of S6 are checked on all 24 signatures (120 relabeling comparisons). The verifier uses exact integers and explicit word truncation, no floating-point comparisons.

Machine evidence: research_notes/R744_X6_BRC_MAGNUS_ORDER4_RESULTS.json. Test label: R744_X6_BRC_MAGNUS_ORDER4_EXACT_PASS. The general theorem follows from the preceding algebraic proof; exhaustive computations independently verify the stated finite X6 cases.

## 6. New implications and next scientific test

For the R743 r=4 family, six pairwise precedence coefficients recover the 24 connector orders. These six 0/1 coefficients are redundant: their valid patterns are exactly 24 transitive tournaments. After exact decoding, a fixed ranked binary representation needs ceil(log2(24))=5 bits, whereas the raw six coefficients retain the direct S6-covariant meaning. The hierarchy O_3 discards all connector order, while O_4 is lossless on this restricted family.

Next: take one legal frozen TRIADIC_CLOSURE_E Cell/Link/Port event and determine whether its V29 PASS/V39 frame update admits a provenance-preserving map from the above signed-word branch groupoid. Test whether native updates distinguish two connector histories with common (j,h) but different degree-four word coefficients. A negative correspondence test is as valuable as a positive one; this mathematical signature is currently a symbolic coordinate-path observer, not an already established native force-dynamics invariant.

P000 and the frozen scientific pin are unchanged. No formal shared Result, independent review, Working Truth or Foundation promotion is asserted by the author-side proof.