# PREFIX-461 — Exact all-degree X6 BRC last-sector generator and polynomial moment recurrence

Date: 2026-11-03 (Asia/Shanghai). Status: AUTHOR_PROVED / INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Source and model

Continuation of PREFIX-460 (commit 28933bcf5fab061599dd19dad28d7e6e5d69c27c), using frozen scientific input f42f2906d77f24085c123f3ccfe9667d41caa96d. Current normative context was read at global-knowledge main@8e7e25eb258da27bd34d5397afe62c268ca9851b and Enterprise Math main@50c6e6bc55cd3e5778cfb400ee09b0c40e71138e: global bootstrap/manual, P000 projection verified against canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, ACTIVE native-X6/residual worldview, TASK bootstrap, current normative continuation, portable research and current research_method.json.

The mother question is exact polynomial-observer rank and resource-efficient carriers for native six-axis paths. The arbitrary-degree exact rank equality remains open. This note gives two complete, independent all-degree structural results that are directly usable as exact regression and algorithmic tools.

We use raw signed X6 displacements (not final nonnegative Cell addresses). Full paths are length N ordered words over the twelve native directions ±e1,...,±e6. Each ordered path has positive integer BRC mass one. History records the number of -e1 letters modulo q. Let m>=0, q>=m+1 and N=q+m-1. We examine residue q-1. Moment observers are endpoint monomials of any declared total degree.

## Theorem A: exact last-sector support

There are exactly q-1 occurrences of -e1 in this residue sector. Indeed the next possible number 2q-1 exceeds N<=2q-2. Removing those q-1 occurrences leaves an ordered m-word on eleven letters D={+e1, ±e2,...,±e6}; every such word has precisely binom(q+m-1,q-1) insertions of the indistinguishable -e1 letters into the full N-word.

Let s>=0 be its number of +e1 letters, and y=(y2,...,y6) its signed remaining displacements. Its support is exactly

W_m = {(s,y) in Z_nonnegative x Z^5 : s+sum_i |yi|<=m, and m-s-sum_i |yi| is even}.

The original endpoint is (s-(q-1),y). The complete exact support enumerator is

sum_{m>=0} |W_m| z^m = (1+z)^4/(1-z)^7,

and hence (with binom(n,6)=0 for n<6)

|W_m| = sum_{j=0}^4 binom(4,j) binom(m-j+6,6).

In particular |W_m| = m^6/45 + O(m^5), and the ratio of support locations to the nominal number binom(m+7,6) of all degree<=m+1 six-variable monomials tends to 16. This is a support-count statement, not a rank assertion.

Proof: the least number of signed steps realizing y is sum |yi|, and extra positive/negative inverse-step pairs consume two letters each. Conversely each nonnegative even slack is achievable by adding such a pair, so the displayed support is exhaustive. The univariate ordinary generating function for s is (1-z)^(-1); for each signed yi it is (1+z)/(1-z); and for even slack it is (1-z^2)^(-1). Multiplication gives (1+z)^4/(1-z)^7. Expanding its numerator yields the binomial expression, with leading coefficient 16/6!=1/45. QED.

## Theorem B: exact Laurent mass and all-degree integer moment engine

With formal commuting invertible u1,...,u6, the joint endpoint multiplicity Laurent polynomial in the residue-(q-1) sector equals

F_{q,m}(u) = binom(q+m-1,q-1) * u1^(-(q-1)) *
              (u1 + sum_{i=2}^6(ui+ui^(-1)))^m.

All Laurent coefficients are nonnegative integers and exactly count ordered native paths. Total sector mass is T=binom(q+m-1,q-1)*11^m.

For a multi-index alpha=(a1,...,a6), write A_alpha(m) for the unshifted positive integer raw moment sum of all eleven-letter m-words; x^alpha means prod x_i^a_i, including 0^0=1. Initial values: A_0(0)=1, and A_alpha(0)=0 if alpha is nonzero. For every alpha and m,

A_alpha(m+1) =
  11 A_alpha(m)
  + sum_{k=1}^{a1} binom(a1,k) A_(alpha-k e1)(m)
  + 2 sum_{i=2}^6 sum_{j>=1,2j<=ai} binom(ai,2j) A_(alpha-2j ei)(m).

The original sector's raw monomial endpoint mass B_alpha(q,m) is

B_alpha(q,m)=binom(q+m-1,q-1)
  * sum_{k=0}^{a1} binom(a1,k) (-(q-1))^(a1-k)
                        A_(k,a2,...,a6)(m).

These formulas give ALL moments to any fixed degree d in at most
O(m*d*binom(d+6,6)) integer arithmetic operations and
O(binom(d+6,6)) stored integer coordinates, with no 11^m-word or
|W_m|-endpoint enumeration. Actual bit cost also depends on integer
magnitudes and q.

Proof: select the q-1 indistinguishable negative-first-axis slots, then expand the eleven-letter residual word's formal Laurent polynomial. Append one of eleven legal letters to each length-m word. Binomial expansion of the shifted endpoint monomial yields 11 copies of the old moment, the positive-e1 correction and the even-power corrections for the pairs ±ei; the odd-power terms cancel algebraically in the observer sum. The final negative-first-axis shift is a binomial expansion in x1. Each update uses lower-degree moments and can be computed in integer arithmetic. QED.

Normalized uniform-sector first/second moments give another exact benchmark:
E[X1]=m/11-(q-1); E[Xi]=0 for i=2..6;
Var(X1)=10m/121; Var(Xi)=2m/11 for i=2..6;
Cov(Xi,Xj)=0 for i≠j.
These follow from the eleven equiprobable residual step types and the deterministic full-path insertion multiplier.

## Actual executable verification and use scope

The accompanying stdlib-only Python certificate computes the independent eleven-direction endpoint DP and the moments recursion, comparing exact integers. ALL degree<=m+1 monomials were checked for m=0..4 (respectively 7, 28, 84, 210, 462); deterministic coverage at m=5 and m=6 was 395 and 602 monomials. Support and total mass were exhaustively checked for m=0..6. The support closed form was checked through m=13, reproducing |W13|=212681. Shifted full-path moments through degree three were additionally checked for (q,m)=(12,4),(20,5),(100,2), with 84 coordinates per case. Every comparison passed with integer arithmetic.

The analytic proofs cover all q>=m+1, m>=0 and any polynomial degree. The numerical checks are focused regression evidence for the implementation. BRC reuse: this is the positive branch-count carrier with exact sector history and endpoint observer; the Laurent generator sums positive multiplicities, not amplitudes. Compression/aggregation is scoped to the declared uniform path source and endpoint polynomial observer; complete ordered-path provenance is not reconstructed.

## Next research unit: PREFIX-462

Investigate the all-m exact sign-character kernel formula from PREFIX-460:
dim_Q ker A_(m,t) = max(0, floor((m-t+3)/2)), t=0,...,5.
Seek a parity-simplex Newton/border interpolation basis, or a concrete violating support/degree pair; cross-check with the exact W_m count and the all-degree moment engine above. Also benchmark higher-degree uniform BRC moment propagation against explicitly enumerating the support, including integer coefficient bit lengths.

Actual GitHub authentication: awdawmip, admin permission. On 2026-11-03, the native task listing returned CONTROL_QUOTA; session registration returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Active owner, native Researcher-ID and formal CLAIM remain unconfirmed. This author-side publication is not an independent Review/Admission.
