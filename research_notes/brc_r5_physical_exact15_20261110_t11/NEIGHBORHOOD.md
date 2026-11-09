# R5 follow-up: positive-width continuum of lawful matched-time g=b pairs requiring 15 Blackwell edges

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.
Depends on RESEARCH.md, VERIFY.py and EXACT_OUTPUT.txt in this same immutable PR branch; scientific pins unchanged.

## Theorem

Keep the exact lawful source X fixed as in RESEARCH.md. Let Y0 and DY be the exact seven-coordinate seedless-F target base and tangent defined there. For every **real**
  t in [1/100000 - 1/10^50, 1/100000 + 1/10^50]
define Y(t)=Y0+t DY, with DY=(0,1,0,-1/4,-1/4,0,1/10).

Then X and Y(t) meet all 13 physical-capacity inequalities, g(X)=b(X), g(Y)=1, z(Y)=a(Y)/10, and the two matched stopping-time equalities
  T(X)=T(Y(t))=(17609/6000,33857/12000).
Moreover there is a strictly positive transport on the same explicit **15-edge support B** from RESEARCH.md for each t, and **no** coupling on 14 or fewer edges. Thus the minimum support is identically **15 throughout this nondegenerate real interval**. This is a continuous physically lawful counterexample family to the uniform-14 hypothesis in the frozen seven-LR auxiliary model.

## Complete proof

The capacity, marginal, stopping-time and fixed-15-edge transport weights depend affinely on t; the verifier checks their nonnegativity and strict positivity at both exact rational endpoints. Thus physical feasibility and existence of the positive 15-edge coupling hold for every real t in between by convexity.

The same ten sparse 21-dimensional dual vectors from VERIFY.py satisfy their 30 edge inequalities independent of t. Their dual lower bounds beta_e(t)=<y_e,h(t)> are affine in t and strictly positive at both endpoints, as checked in NEIGHBORHOOD_VERIFY.py; hence all ten edges F remain mandatory throughout the interval.

At the central t0=1/100000, VERIFY.py proved by complete exact modular rank enumeration that every augmented support S=F union T, |T|=4, is inconsistent with the full 21 Blackwell equations. Here is a quantitative argument that all 4,845 exclusions hold simultaneously for all real t in the displayed interval.

Restrict to the 15 pivot rows I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17), scaling each moment row by 20. This yields an integral matrix C whose entries have modulus at most 38. The restricted right-hand side h_I(t) is affine and at t0 has exact common denominator dividing

  D0 = 1148267016000000.

The maximum absolute derivative component on these scaled rows is precisely

  max_i |h'_I(t)_i| = 23/40.

Fix any of the 4,845 supports S, with rational rank r<=14. Its augmented matrix [C_S | h_I(t0)] has rank strictly greater than r, by the exact modular proof and rank-lift in RESEARCH.md. Thus there exists some (r+1)x(r+1) minor involving the last column h_I(t0) that is nonzero. Because C is integral and D0 h_I(t0) integral, its absolute value is **at least 1/D0**.

Under variation t0+delta, the derivative of that minor is a determinant with only the last column replaced by h'_I(t). Its absolute value is bounded by

  (r+1) * r! * 38^r * (23/40)
  <= 15 * 14! * 38^14 * (23/40).

The exact arithmetic gives

  D0 * [15 * 14! * 38^14 * (23/40)]
    = 11302660903782170368770049792229180335718400000000
    < 10^50.

Consequently, for all real |delta|<=10^-50, the selected minor cannot vanish. This works for every S, using the same bound, regardless of which minor was nonzero. The entire finite family of <=14-support possibilities remains impossible. The explicit positive 15-edge basis remains possible; so the exact minimum stays 15.

This proof uses exact rational/integer finite enumeration only at the central point and a certified analytic determinant bound for the continuum. Checking just two endpoint ranks is not used to infer the continuum.

## Execution and next question

NEIGHBORHOOD_VERIFY.py actually checked D0, the slope bound, all physical and Blackwell equations, strict 15-edge positivity and ten dual forced-positive lower bounds at left endpoint, center and right endpoint. NEIGHBORHOOD_OUTPUT.txt is the actual stdout. The parent VERIFY.py was executed separately and its 4845-case completeness evidence is retained.

Further research: expand this extremely conservative rational interval using sharp support-specific determinant slopes and chart pivots, and seek at least a two-parameter lawful matched-time physical region with exact minimum 15. P000, frozen scientific inputs, ownership, scientific admission and independent review retain their scopes.
