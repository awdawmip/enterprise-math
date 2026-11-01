# PREFIX-401 — Four-annulus exact feasibility and variable-I3 branch separation

Date: 2026-11-01 (Asia/Shanghai). Scientific status: AUTHOR_SIDE_EXACT_VERIFIED; UNREVIEWED; NOT_ADMITTED; NATIVE_REGISTER_PENDING. **External auxiliary static complex three-amplitude inverse model only**; neither P000 native X6 nor typed BRC dynamics is proved.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@ae1c9380c450555df6302dfe5ad4d58c053e9196; Enterprise Math main@9412897fb2b8e77bb30ee26391fb65edaba2a8fd. Depends on 2026-11-01 PREFIX-400 exact singular slice, original five-Port A and observer preservation. Actual contributor: connected GitHub login awdawmip. Native service research authority NOT granted (UPSTREAM_CODE_REVIEW_REQUIRED; active jobs 5/5); no current Owner or CLAIM established. This file is portable author-side evidence, not a formal Result.

## Model and exact four-annulus normal form

Original A (rows) is
    (4,4,0), (0,-4,4), (-5+3i,0,-3+i),
    (-2-2i,4+4i,2+2i), (-2,0,5+2i).
The first three rows A3 have det = -32+32i. Fix I1=1, I2=3481/3969 and Cu=14884/3969. Exact triangle-inequality saturation gives the unique global-phase gauge W=A3Y=(1,59/63,c+id); each real (c,d) determines one source Y=A3^{-1}W.

Let N=75154, T=245c-123d, S=123c+245d. Then T²+S²=N(c²+d²), c=(245T+123S)/N and d=(-123T+245S)/N. Direct expansion of the ORIGINAL A yields:
    I3 = (T²+S²)/N,
    I4 = (16/N)*((T+37577/63)²+S²),
    I5 = (53/(8N))*((T+43249/63)²+S²),
    Cv = ((T+245)²+(S+123)²)/N.
Thus the four measured quantities are positive rational multiples of squared distance to the fixed rational centers
    h3=(0,0), h4=(-37577/63,0), h5=(-43249/63,0), hv=(-245,-123).
The constants in all four complete-the-square identities vanish exactly. This avoids division by any singular eliminant.

## Theorem A: complete two-way YES/NO with at most 72 quadratic candidates

For arbitrary FINITE rational closed intervals Lj≤Ij≤Uj for j=3,4,5,v, source existence is equivalent to intersection of four closed annuli (possibly degenerate or empty) in the (T,S)-plane. For a measurement α||x-h||², U<0 means empty; otherwise the outer disk has radius squared U/α, and an inner excluded open disk exists only when L>0, with radius squared L/α. Therefore each of four bands contributes at most two boundary circles; deduplicate identical circles to get n≤8.

Enumerate (i) leftmost/rightmost points of each boundary circle (including radius-zero singleton centers) and (ii) intersections of each pair of distinct-center boundary circles (up to two each). At most 2n+2*C(n,2)=n(n+1)≤72 candidates arise. All their coordinates are of the form (a+b√D,c+d√D) with rational a,b,c,d,D≥0. Test all ORIGINAL four inequalities at each candidate, using only exact comparisons of rational squares to determine the sign of a+b√D. YES returns a reconstructible real source via c,d and A3^-1; NO returns a finite table showing at least one violated inequality at each enumerated candidate.

Completeness proof: if nonempty, the feasible intersection K is compact (the I3 outer disk bounds it). Choose a point x*∈K of maximal T. It cannot satisfy all constraints strictly. If two distinct active boundary circles meet at x*, it is an enumerated intersection. Otherwise exactly one distinct boundary circle is active (coincident circles were deduplicated); all remaining constraints are strict there. If x* is not a left/right extremum of that circle, a short arc inside all remaining strict constraints increases T, contradicting maximality. A radius-zero circle's center is itself enumerated. Therefore every nonempty feasible K contains a candidate; a passing candidate conversely reconstructs an exact source. Two circles subtract to a line and intersect in a quadratic radical, so no higher-degree algebraic representation is required. General validity follows from this argument, NOT from the finite test suite.

## Theorem B: strictly robust separation with nonzero I3 uncertainty

Nominal real source pair: I3=2, T=122, S=±368, J4=550600/3969, J5=4417309/63504. Their Cv values are 5 and 97357/37577, difference d=90528/37577. Permit independent |I3-2|≤δ=1/10, |I4-J4|≤ξ4=1/10, |I5-J5|≤ξ5=1/10. The exact I4 identity gives
    |T-122|≤D_T=(63/16)ξ4+63δ=1071/160.
Consequently
    S²≥N(2-δ)-(122+D_T)²=3231501279/25600>355².
The sign of S is preserved throughout the entire continuous three-dimensional band; both signs are attained by the nominal sources. For either branch,
    ||S|-368| ≤ D_S=(Nδ+(244+D_T)D_T)/(355+368)
                =235353121/18508800.
From Cv=1+I3+(2/N)(245T+123S), each signed-branch true Cv lies within H of its respective nominal value:
    H=δ+(2/N)(245D_T+123D_S)
      =42950935081/231835059200.
Allow independent measured Cv absolute error η≤1. The entire two label-specific observed bands remain strictly disjoint:
    d-2H-2η ≥ d-2H-2
             =4474780119/115917529600 >0.
This is branch-label separation, not pointwise uniqueness inside a band. The extra I5 constraint only narrows the permitted set. In particular, measured Cv at the exact midpoint (5+97357/37577)/2 with η=1 is mathematically impossible for EVERY allowed intensity triple (a continuous-noise NO certificate): midpoint distance from either nominal Cv minus H is >1.

## Theorem C: exact-source injectivity of three observables on this slice

Keep the fixed I1,I2,Cu gauge and suppose I3=k, I4=j4, Cv=q are exact. Any source MUST have
    T=(63/16)*(j4-300616/3969-16k),
    S=(N*(q-1-k)/2-245T)/123,
    c=(245T+123S)/N, d=(-123T+245S)/N,
    Y=A3^{-1}(1,59/63,c+id).
Hence there is at most ONE global-phase-inequivalent source. It exists iff T²+S²=Nk and any other exact I5 equality is satisfied. This is scoped to the fixed-gauge singular slice; it does not imply global injectivity for arbitrary I1,I2,Cu.

## Actual verification / limitations / BRC usage

The standard-library Fraction checker enumerates all candidates exactly and passed eight specified YES/NO cases, including a 64-candidate NO with nonzero I3 uncertainty. An independent SymPy checker re-expands the original complex matrix, verifies the four annulus identities, reconstructs both nominal sources and checks the exact rational gap. Local run output: PASS_PREFIX401_FINITE_72_CANDIDATE_FOUR_ANNULUS_FEASIBILITY_AND_INTERVAL_I3_BRANCH_SEPARATION and PASS_PREFIX401_INDEPENDENT_SYMPY_ORIGINAL_A_AND_BRANCHED_ANNULUS_BOUND. Executed local code and logs belong to the separately packaged complete evidence; GitHub code is also stored here, but byte identity to locally executed code must be checked, not assumed.

BRC REUSE_APPLIED: preserve source identities and the sign(S) provenance fiber; Cv repairs this lost sign in the specified scope. No typed BRC arithmetic was executed and no native heart-world correspondence is established. Logical limits: I1,I2,Cu are EXACT. Allowing these three to vary invalidates the fixed W2=59/63 gauge and the four-annulus reduction. Prior PREFIX-399/400 assumptions remain author-side, not independent admission.

Next PREFIX-402: allow rational positive error on I2 and Cu with I1=1. Find an exact finite-dimensional semialgebraic lift and executable two-way certificate (or a minimal counterexample to four-annulus sufficiency); preserve phase and source labels. Independent review and native registration remain distinct tasks.
