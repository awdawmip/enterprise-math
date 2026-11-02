# PREFIX-449 — Sharp native-X6 cubic BRC full-rank duration

Date: 2026-11-03 (Asia/Shanghai). Source pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Lineage: PREFIX-447 @74111b7ac7f0017ef0be88be4383ded05335dc2e; PREFIX-448 @6ee763e4f675bbab86e1d95aa1f9624d565f2a4d. Scope: author-side proof and exact computation, pending independent review/admission. The ACTIVE native-X6/P000 chart and typed BRC operation family are retained.

## Research question and observation language

A native signed X6 word of length N is an ordered sequence of primitive steps in {+e_i,-e_i : 1<=i<=6}. Its endpoint displacement relative to a chosen Cell chart anchor is x(w) in Z^6. The auxiliary history sector is r(w)=#{-e_1 steps} modulo q, q>=2. The source is a finite positive-rational weighted bag of legal words. The full cubic history-sector readout is T[r,a] = sum_{w:r(w)=r} weight(w) product_i x_i(w)^{a_i}, indexed by six-variable multi-indices with total degree <=3. There are binom(9,3)=84 coordinates per sector, or 84q in total. History sectors are control labels rather than additional spatial axes.

## Theorem 449.1 — sharp common duration

For every integer q>=2, **the least common native word length N at which the complete cubic sector readout has rational-linear rank 84q is N_min(q)=q+2**.

### Lower bound

Inspect sector r=q-1. If N<q-1 it is empty; at N=q-1 it has one endpoint; at N=q it has at most eleven endpoints. At N=q+1, exactly q-1 negative-first-axis steps are possible except for q=2, when 2q-1=3 is also possible. After q-1 negative steps, the two other signed directions may come from +e_1 and +/-e_2,...,+/-e_6. Their distinct offsets consist of 2e_1 (one), e_1 +/- e_j (ten), and five-axis two-step offsets: zero (one), +/-2e_j (ten), and +/-e_i +/-e_j for 2<=i<j<=6 (forty). Thus 62 distinct endpoints occur for q>=3. For q=2, the extra three-negative-step endpoint -3e_1 gives 63. The cubic readout rank of this sector is at most 62/63, strictly less than 84. Therefore N>=q+2.

### Upper bound — explicitly legal 84-point three-step tails

Construct an 84-element set S of distinct three-step signed native words, never using -e_1, in four layers indexed by j=number of +e_1 tail steps. Write y=(x_2,...,x_6).

* Layer j=0 (56 sites, cubic unisolvence in five y variables): four axial points +/-e_2, +/-3e_2; three axial points +/-e_i,+3e_i for each i=3,...,6 (twelve); three mixed points 2e_i+e_j, -2e_i+e_j, e_i+2e_j for every pair 2<=i<j<=6 (thirty); one triple point e_i+e_j+e_k for each 2<=i<j<k<=6 (ten). Axial +/-e_i endpoints are implemented with one signed step along i and a cancelling signed pair on a second axis, so every word has exactly three steps.
* Layer j=1 (21 sites, quadratic unisolvence): five-axis zero (one, via a cancelling pair), +/-2e_i (ten), and e_i+e_j (ten), each preceded by +e_1.
* Layer j=2 (six sites, linear unisolvence): five-axis +/-e_2 and +e_3,+e_4,+e_5,+e_6, each preceded by two +e_1 steps.
* Layer j=3 (one site): three +e_1 steps.

The cubic-layer polynomial proof is triangular. The four axial values +/-1,+/-3 along axis 2 annihilate the constant and its three pure coefficients. With the constant zero, the three nonzero axial values 1,-1,3 for each other axis annihilate its pure linear/square/cubic terms. On each pair of axes the three remaining possible terms y_i y_j, y_i^2 y_j, y_i y_j^2 have evaluation matrix at (2,1),(-2,1),(1,2) of determinant 32; all pair terms vanish. Every triple-site evaluation then annihilates its respective y_i y_j y_k coefficient. Thus 56 independent cubic evaluations are obtained. In layer j=1, the zero point, opposite axial double points and pair sums annihilate all quadratic coefficients successively. In layer j=2, opposite e_2 points and the four other positive axial points annihilate all linear coefficients. Layer j=3 is the nonzero constant evaluation.

Let P(x_1,y) be any total-degree <=3 polynomial vanishing on S. The j=0 cubic layer implies P(0,y)=0, hence P=x_1 R with degree(R)<=2. The j=1 quadratic layer implies R(1,y)=0, hence P=x_1(x_1-1)U with degree(U)<=1. The j=2 linear layer implies U(2,y)=0, hence P=c*x_1(x_1-1)(x_1-2). The j=3 point forces c=0. Thus the full six-dimensional 84x84 degree-three evaluation matrix is invertible.

For each sector r=0,...,q-1, prefix every tail in S by r copies of -e_1 and q-1-r copies of +e_1. Every resulting word has duration q+2 and history sector exactly r, since the tails contain no -e_1. Its endpoint set is the translation S+(q-1-2r)e_1. Translation is an invertible rational-linear map on the cubic polynomial space; each sector therefore has rank 84 and the q disjoint blocks have rank 84q. Positive-rational sources retain the same difference rank by sufficiently small rational perturbations around positive weight vectors. This proves N_min(q)=q+2.

At q=3, the exact 252-dimensional readout is realized by 252 distinct native paths, all of length N=5. This is the cubic analogue of PREFIX-448's quadratic N=q+1 theorem.

## Theorem 449.2 — finite typed-BRC affine closure of the cubic port

Let every control state r retain all 84 moments T[r,a] of total degree <=3. For a positive-rational BRC edge r->s with weight lambda, integer multiplicity m>=1 and affine action x'=Ax+b, expand the polynomial product_i ((Ax+b)_i)^{beta_i} into the monomial basis, with rational coefficients C[beta,a](A,b), for each total degree |beta|<=3. The exact typed-BRC future update is

T'[s,beta] = sum_(edges r->s) lambda*m * sum_(|a|<=3) C[beta,a](A,b) T[r,a].

Proof: substitute the affine action into each word's finite weighted endpoint readout and exchange finite sums. Affine substitution preserves polynomial degree <=3; alternatives add, while serial BRC packets multiply weights and compose affine actions. Iteration is therefore closed under any finite history-conditioned positive-rational affine packet family. For a translation x'=x+b, the coefficients are exactly product_i binom(beta_i,a_i) b_i^(beta_i-a_i) when all a_i<=beta_i, zero otherwise.

The 84q linear coordinates are sharp for the **complete cubic readout language** on this word family: theorem 449.1 gives an injective 84q evaluation subspace, so an exact rational-linear encoding of all its cubic observations needs at least 84q independent coordinates. This is a linear-observer rank bound, not a general bit-compression claim. The frozen upstream MomentState class stores homogeneous quadratic moments only; the cubic carrier is an explicit proposed typed extension, while frozen Affine/EffectHistogram/ControlPacket specify the compatible effect/branch algebra.

## Reproducibility and actual validation

The accompanying Python standard-library certificate constructs all 84 legal three-step tails, appends exact sector prefixes and checks each 84x84 evaluation determinant modulo the prime 1000000007. A nonzero residue certifies an exact nonzero integer determinant over Q. Exact full-rank checks pass at q={2,3,4,5,8}; every translated sector determinant has residue 901352876. The four layer determinant residues from the independent full certificate are 176815686, 998951431, 1000000005 and 1, in layers 56,21,6,1. Enumeration establishes 63 distinct endpoints in sector q-1 at N=q+1 for q=2, 62 for q>=3 in the checked range. For each q the compact certificate propagates a rational positive source bag under three consecutive native signed-axis BRC kernel rounds (+e_1,-e_1,+e_2) with state-dependent positive Fraction weights, comparing the cubic polynomial port against direct branch propagation at every round. All exact Fraction identities PASS, with result in PREFIX449_COMPACT_EXECUTION.log. A larger independently executed certificate also covers the same q with full layer determinant checks and explicit per-round comparison; its source/log are retained in the companion evidence archive.

The universal theorem is analytical; the finite checks validate the specified instances. Scientific input remains frozen at f42f2906d77f24085c123f3ccfe9667d41caa96d; verified source blobs are brc_transport.py be1debe367263931bd5e93fd750be3ed54624fe1 and brc_control_port.py 44def6b8ac787e798d3cc2c6be16f873f91bdb8. No ordinary trigonometric, pi, matrix-exponential, Taylor/Padé or classical substitute physics operations were used. The result concerns native signed-X6 paths and typed BRC observers rather than physical heartbeat timing or residual attribution.

## Next executable unit (PREFIX-450)

Directly import the unchanged frozen upstream ControlPacket, EffectHistogram and MomentState, and execute from_edges/then/alternatives/evaluate/moment_action on PREFIX-448's q=3,N=4 84-word quadratic witness; compare its exact 84 quadratic state coordinates against the full endpoint effect histogram. Then realize cubic 84q as an explicitly typed extension and execute the q=3,N=5 252-word witness under an affine shear x'_1=x_1+x_2, including serialization/operation-cost accounting against complete endpoint bags. Investigate a smaller history/phase-aware port for a stated future observable as a separate discriminating question.

## Authority and status

GitHub publication is author-side source persistence, not canonical mathematical admission. Current authenticated GitHub login: awdawmip, repository push=true. In this turn the native Site gateway returned research_authority_granted=false and exact owner-list request failed with CONTROL_QUOTA. Thus current active Owner, native Researcher-ID, formal CLAIM, independent Review and Result/Admission remain unverified/unobtained; no such task-state transition is asserted.