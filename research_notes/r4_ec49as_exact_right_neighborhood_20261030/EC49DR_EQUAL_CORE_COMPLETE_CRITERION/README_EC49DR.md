# EC49DR — Complete ten-step history-feature rank criterion for equal first-two-axis BRC weights

2026-11-01 · AUTHOR PROOF / EXECUTED EXACT CHECKS · PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED

## Provenance and native model

Scientific inputs remain frozen at GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e and Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, inherited from EC49DP. Verified predecessor EC49DQ: research branch commit 05303e06e0db54fdd35026d0164b480037562e2c. Current behavioral rules were read separately at GLOBAL main 3a35cfb4518f82e06019cd17582f03406f38396c and Enterprise Math main a5902327c911630a2c6a387fbbc4822232edaebd, including normative entry, P000, ACTIVE worldview, portable research and BRC method; no protected input is changed.

Histories are length 10 ordered signed words in the six native spatial directions ±Ej. Signed chart displacement is D=(-2,0,0,0,0,0). At this endpoint a word has four positive steps and six negative steps. Positive +Ej multiplies two independent strictly positive BRC instruments by xj,yj; negative steps carry factor 1. The third instrument counts unweighted paths. A=adjacent (+E1,+E2), B=adjacent (+E2,+E1), with joint occurrence and terminal positive ports; preserve ordered paths and provenance. These are raw chart displacements, not final Cell addresses.

For a word w let pj count its positive +Ej steps, X(w)=product xj^pj and Y(w)=product yj^pj. Using the six upstream EC49DQ history label/port features z(w), its 18-column feature row is M(w)=(X(w)z(w),Y(w)z(w),z(w)). Features in order: z0=no A,no B; z1=no A,yes B; z2=yes A,no B; z3=yes A,yes B; z4=no A and terminal positive port E1; z5=no B and terminal positive port E2. The first four are mutually exclusive, while port features can overlap. This theorem concerns the real row span of M(w).

## Theorem EC49DR-A (proved over all strictly positive real weights in the stated subfamily)

Assume x1=x2=u>0 and y1=y2=U>0. Let P0=(u,U) and Pj=(xj,yj), j=3,4,5,6. The span of all genuine length-10 histories with endpoint D=-2E1 has feature rank 18 IF AND ONLY IF these five points are not all affine-collinear. Equivalently some three-row determinant det[(xa,ya,1),(xb,yb,1),(xc,yc,1)] is nonzero, where a,b,c range over {0,3,4,5,6} and x0=u,y0=U.

More precisely, the instrument coefficient subspace belonging to the simultaneous A=B=1 feature has dimension equal to rank of the five 3-vectors (u,U,1),(xj,yj,1), j=3..6.

### Proof: necessity

An ordered signed path with both adjacent 12 and 21 requires at least three positive core steps from axes 1 and 2. A length-10 history with this endpoint has exactly four positive steps. Hence its positive-step weights at A=B=1 are either (u^4,U^4,1) or (u^3*xj,U^3*yj,1) for some j=3..6. All five possible triples actually occur in valid signed native paths; the z3 paths in the constructive templates and the verifier exhibit them. Multiplication by the invertible diagonal diag(u^-3,U^-3,1) identifies their rank with the five augmented points. Every non-AB historical feature contributes at most three instrument directions; the AB coefficient rank is at most two if all five points are collinear. Consequently rank M <=5*3+2=17, proving the necessary condition, scoped to this 10-step representation.

### Proof: sufficiency

Case 1: Three off-core points Pp,Pq,Pr (p,q,r in {3,4,5,6}) are noncollinear. Use the already verified EC49DQ type-II witness with six independent history feature groups, each populated by the three positive count choices (2E1+E2+Ej) for j=p,q,r. The 3-instrument determinant is u^3 U^3 times the nonzero affine 3-point determinant; hence the 18x18 witness is nonsingular.

Case 2: All four off-core points are collinear but the five-point set is not. Then P0 is off their affine line, so choose two distinct off-core points Pp,Pq such that det[(u,U,1),(xp,yp,1),(xq,yq,1)] !=0. In each of six independent history feature groups take three genuine paths with positive counts (3E1+E2), (2E1+E2+Ep), (2E1+E2+Eq). Their instrument matrix G has rows (u^4,U^4,1),(u^3*xp,U^3*yp,1),(u^3*xq,U^3*yq,1). Thus det G = u^3 U^3 det[(u,U,1),(xp,yp,1),(xq,yq,1)] != 0.

Six feature basis rows are z0=e0, z1=e1, z2=e2, z3=e3, z4=e1+e4, z5=e2+e5, with determinant ±1. The full signed 18x18 matrix therefore has determinant ±(det G)^6 !=0. All eighteen paths exist: the verifier deterministically constructs the complete ordered signed path with each specified positive count vector and each z, checking its length, exact six-component endpoint, A/B occurrence and port. For any off-core j, the six explicit templates from EC49DQ are z0=(1,1,-1,-1,-1,-1,2,-2,j,-j), z1=(1,-1,-1,-1,-1,2,1,-2,j,-j), z2=(1,1,2,-1,-1,-1,-1,-2,j,-j), z3=(-1,-1,-1,-1,-2,j,-j,1,2,1), z4=(1,-1,-1,-1,-1,-2,j,-j,2,1), z5=(1,-1,-1,-1,-1,-2,j,-j,1,2). The same six z occur for the all-core count 3E1+E2 by the explicit generator. This proves sufficiency.

## New double-zero counterexample: both EC49DQ sufficient gates vanish

Take x=(2,2,1,2,3,4), y=(3,3,2,4,6,8). First-two-axis type-I gate (u-v)(U-V)(uV-vU) is zero. All four off-core points lie on y=2x, so every type-II triple determinant is also zero. Yet P0=(2,3) lies off y=2x. For p=3 and q=5 the three-instrument determinant is exactly -432. The generated 18x18 signed native history-feature determinant is -6499837226778624, nonzero, hence the feature rank is 18.

## Executed exact checks

The actual Python standard-library program VERIFY_EC49DR.py returned PASS. It generated and checked 18 genuine signed native histories, computed G and the 18x18 determinant by exact integer Bareiss, and checked ranks over primes 1000003 and 1000033. Direct returning future operations a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3) were expanded with exact six-axis return, joint A/B boundary observation, and both multiplicative BRC channels. Returning-future ranks for h=2,3,4,5 were 15,18,15,18, and for cumulative h=1..2 rank 18. Counts of allowed future words were 4,15,56,210,5 respectively.

A second independent exact finite dynamic-programming checker enumerated all 126 nonnegative 6-component positive-count vectors summing to 4 and all 333 reachable (count vector,z) pairs at length 10 and D=-2E1. Two-prime feature ranks: double-zero example 18 (AB feature dimension 3); all-five-collinear sample x=(2,2,1,2,3,4),y=(5,5,3,5,7,9) rank 17 (AB dimension 2); all equal weights xj=2,yj=3 rank 6 (AB dimension 1). For the rank-17 case the analytic theorem supplies the rational upper bound; modular rank 17 supplies a rational lower bound. The exact signed-path nonzero integer determinant independently establishes the rank-18 example over Q and R.

The all-positive-real-parameter iff statement is analytic. Finite computation verifies the stated integer instances and native implementation. Application to every future horizon h>=2 and claimed first joint-saturation length n=10 still depends on the author-side EC49DO six-/five-feature actual-future factorization lemma, which requires independent proof review; the history-feature theorem is separately proved here. No theorem admission, authenticated RA, CLAIM, Result or Driver review is asserted.

## Ownership and continuation

Current site-side service scopes were static_machine_readonly with research_authority_granted=false. A native session registration request was rejected before dispatch with STATIC_READONLY_SCOPE_DENIED; owner listing returned CONTROL_QUOTA. This is author-side portable Source research in existing draft PR #1730, preserving the frozen task and prior owner attribution. Next EC49DS: remove first-two-axis equal-weight restriction, calculate full ten-step rank-defect algebraic locus from 333 (positive-count,feature) reachability rows, test its determinantal ideal on the strictly positive orthant, and independently audit EC49DO's actual-future feature factorization.