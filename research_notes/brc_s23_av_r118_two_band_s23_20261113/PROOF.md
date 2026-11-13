# R118 — Exact two-band integer oracle for the full S23 six-affine-phase observer

Date 2026-11-13 (Asia/Shanghai). Enterprise Math Research1 author-side mathematical result. Predecessor R117: 4384519a7483ce9931c12f4828aff1b0893150cc. Frozen scientific input remains 43ec6098b1330ae86d0a7863be336c5d97f6ef34. P000 and native X6 semantics are unchanged. This result addresses the full original S23 *auxiliary* phase observer, not a native Cell/Link/Port permission predicate.

## Exact model
Take integers j,a,c,t, rational x, and a rational closed interval I. For theta real, set Y_t=x+(t-j)theta, A=a theta, C=c theta, and frac(z)=z-floor(z). M_t(theta)=1 exactly when frac(Y_t) belongs to the positively directed half-open arc from frac(A) (included) to frac(C) (excluded); coinciding endpoints define the empty arc. Complete source identities (t,b), membership provenance, descending rank, and historical F,G are retained.

For old times T, old rational point/open-gap atoms J are cut at all integer crossings of A,C,A-C,Y_s,Y_s-A,Y_s-C for s in T. Hence every old eligibility bit is constant on each atom. The task: for a new time t of arbitrary signed magnitude, test both M_t bits on every old atom and produce exact rational witnesses *without enumerating t's new integer crossings*.

## R118.1 — Positive-width moving integer-band lemma

Let J=(l,h), rational l<h, and let D(theta), U(theta) be rational-affine and satisfy D(theta)<U(theta) for all theta in J. Put d=min(D(l),D(h)), u=max(U(l),U(h)), and n0=floor(d)+1. Then

EXISTS theta in J, EXISTS integer n: D(theta)<n<=U(theta)

is equivalent to

n0<u OR [U is constant AND n0<=u].

In the feasible case a rational theta can be recovered by solving two one-dimensional affine inequalities and taking the midpoint of the remaining open rational interval.

**Proof.** For each theta, E(theta)=(D(theta),U(theta)] is a nonempty interval. Their union is connected because each E(theta) intersects the continuous midpoint spine (D(theta)+U(theta))/2, whose image over J is an interval. Its infimum is d and its supremum is u. The infimum is excluded by the strict lower bound. If U is nonconstant affine, the supremum over the open J is attained only at an excluded endpoint; if U is constant, its upper boundary is attained in J. Therefore the union is exactly (d,u) or (d,u], respectively. Its smallest possible integer is n0. If U is nonconstant, a feasible n0<u has some theta with strict inequalities D(theta)<n0<U(theta): when the first feasible point sits at U=n0, move slightly inside J toward increasing U while retaining D<n0. If U is constant at n0, retain the included upper equality. All resulting feasible regions have rational interior points. QED.

## R118.2 — Exact full directed-circle oracle

On an old open atom J, integers p=floor(a theta) and q=floor(c theta), and the order of alpha=a theta-p and gamma=c theta-q, are fixed by the old A,C,A-C crossings. Write Y=x+(t-j)theta without reducing mod 1.

Case alpha<gamma (nonwrapping): the directed arc is [alpha,gamma). Membership iff there exists integer n satisfying
  Y-gamma < n <= Y-alpha.
Its affine lower and upper functions are (t-j-c)theta+x+q and (t-j-a)theta+x+p.

Case alpha>gamma (wrapping): the directed arc is [alpha,1) union [0,gamma). Membership iff one of two integer bands is feasible:
  Y-1 < n <= Y-alpha,
  Y-gamma < n <= Y.
The first band has positive width 1-alpha. The second has width gamma>0 whenever gamma is nonzero; if gamma is identically zero on J the second band is empty and is skipped.

Case alpha=gamma throughout J: the directed arc is empty, so M_t=0.

For distinct endpoints, the complement of the half-open directed arc from alpha to gamma is precisely the half-open directed arc from gamma to alpha. Apply the same one- or two-band test with endpoints swapped to decide M_t=0. If endpoints coincide, bit 0 is always attained and bit 1 never attained. On singleton atoms evaluate the original fractional-circle condition exactly.

**Proof.** Fractional membership in any [r,s), 0<=r<s<=1, is equivalent to r<=Y-n<s for an integer n, or Y-s<n<=Y-r. For a wrapping arc this yields precisely the displayed two bands. The endpoints' floors and relative order stay fixed on J. Each nonempty band has positive width and the affine form in R118.1, which supplies the exact existence test and witness. Swapping endpoints handles the exact complement, including start inclusion and end exclusion. The cases exhaust all old open and singleton atoms. QED.

**Important boundary:** the integer-band lower bound is strictly less than n and the upper bound is weak. Changing these changes the directed half-open arc at exact boundary points.

## R118.3 — Exact online new-time signature refinement

For each old atom J_i with old signature s_i, run R118.2 for bits b=0,1; emit (s_i,b) and its exact rational witness iff attainable. Deduplicate only after collecting all old atoms, because one old signature may have disconnected preimages.

The resulting set equals the full attained signatures for T union {t}: every real theta belongs to an old atom and R118.2 captures its new bit; each emitted pair has a witness in that atom. The new bit states may inherit the same old immutable ranked-history root until a new identity (t,branch) is actually inserted. Such an insertion changes only attained states with its new time bit 1, retaining complete branch identity and provenance. This is an auxiliary Boolean-ranked observer operation; no native dynamical action is asserted.

## Cost and scope

For q already available old atoms, at most 2q bit queries and 4q moving-band feasibility checks are needed. Each band uses a constant number of exact integer/rational operations (affine evaluation, floor, comparison, solving inequalities, midpoint). Let B bound input bit lengths (old endpoints and j,a,c,x,t). Total oracle work is O(q poly(B)) bit operations, with log(|t|+2) included in B; no iteration proportional to |t| occurs. Old atom construction, ranked source/history maintenance, signature-root updates and storage are separately charged. The output is the *attained signatures and their witnesses*, not every connected component or every new critical point; explicit full atomization may still require Omega(|t|) output. The theorem handles one new time against an old signature partition, not an arbitrary simultaneously new tuple of times.

## Reproducible exact verification

See check_r118.py (Python 3 standard library, Fraction) and verification_r118.json. Deterministic seed 1182026. Six targeted signed/equal-endpoint/half-open cases plus 500 randomized small integer/rational instances: for each, independent full six-affine-cut atomization is compared against the non-enumerative oracle, and every rational witness is tested against the direct fractional-circle predicate and its old signature. Four additional huge signed new times ±(10^80+7), ±(10^150+19) are checked by direct witness evaluation without forming new cuts.

Executed result: R118_PASS 500 22026 44668 12686 31814 1000.
Counters: 22,026 small old atoms; 44,668 total bit calls including huge cases; 24,163 band checks; 12,686 non-singleton rational witnesses; 31,814 full new-time atoms in small brute comparisons; maximum witness numerator/denominator 1000 bits. Finite checking validates the implementation on those instances. R118.1–3 establish the universal statements.

## Next question R119

Study simultaneous introduction of two or more distinct high-frequency S23 time bits on one old atom. Test exact joint feasibility (not merely per-bit feasibility) using integer-lattice/semilinear certificates; find pairwise feasible but jointly impossible signatures, prove any compact decision bound, and compare output cardinality, bit complexity, historical root sharing and exact rational witnesses. Use small-frequency full six-cut enumeration only for independent validation.

Status: author-side proof and exact finite verification, independent review pending. Formal CLAIM and native research activity are separately determined by their actual control receipts.