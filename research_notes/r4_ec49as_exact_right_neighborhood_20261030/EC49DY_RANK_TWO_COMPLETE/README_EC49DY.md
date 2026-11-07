# EC49DY — Exact rank-two stratification of ordered-first-event BRC

Date: 2026-11-02. Parent: EC49DX at 650987da04efc054584ac331a1a927b1bdee26fe in Draft PR #1730. Author status: ANALYTIC_PROOF / EXECUTED_EXACT_NATIVE_CERTIFICATES / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 773d538180bfb49e24cffeb35c3ee75eb0628e2e; Enterprise Math fc0f038e7bfd12c886b4d37f900bfb770c0f61ab (inherited from EC49DX). Current behavioral context independently read from global canonical main 2b7a21fa874d733dee3883a027fd39f5ef3e4a3a and Enterprise Math canonical main 32b1f6f0c3387bb68919f66b340aae13a1248284. P000 and ACTIVE worldview unchanged.

## Precise model

Genuine ordered signed primitive paths use **all six native X6 axes**, fixed exact displacement D=(-2,0,0,0,0,0), even length n and positive-step counts p_i; sum_i p_i=(n-2)/2=m. Negative counts are (p_1+2,p_2,...,p_6). For arbitrary strictly positive real x,y in R^6, the two positive BRC instruments are X(w)=product_i x_i^{p_i(w)} and Y(w)=product_i y_i^{p_i(w)}; the third instrument counts paths. The adjacent events are A=(+E1,+E2) and B=(+E2,+E1). First-occurrence-order terminal buckets are N,A-only,B-only,AB(A first),BA(B first). Last-port L is +E1,+E2,other. EC49DX's nine Boolean features, in order, are z=(1[N],1[A],1[B],1[AB],1[BA],1[A and L=2],1[B and L=1],1[N and L=1],1[N and L=2]). The history row is H9(w)=(X(w)z(w),Y(w)z(w),z(w)), with 27 columns. All ranks are over R, and refer to **all genuine length-n paths**. The 6x3 weight matrix P has row (x_i,y_i,1).

## Theorem: COMPLETE rank(P)<=2 parameter classification

For all strictly positive real x,y, with rank(P)=2:
- **Oblique affine nonuniform:** x not constant, y_i=a*x_i+b for all six axes, with a!=0 and b!=0 (and y_i>0). Then rank H9 at n=10 is exactly **25**, and at EVERY even n>=12 exactly **27**. The first possible full-rank length is **12**.
- **Proportional or one-uniform:** y=a*x for some a>0 with x nonconstant, OR exactly one channel is constant across all six axes. Then rank H9 is exactly **18** at every even n>=10, and cannot reach 27 at any even n.
For rank(P)=1, both weight channels are constant over all axes, and rank H9 is exactly **9** for every even n>=10. Together with the previously proved EC49DX rank(P)=3 criterion, the complete n=10 rank set is **9/18/25/27**. All quantifiers are for fixed-length genuine X6 histories, not arbitrary replacement graphs or time-evolution histories.

### Proof 1: universal upper rank 25 for rank(P)=2 at n=10

There are exactly four positive steps. Every AB-first word requires at least positive subsequence E1,E2,E1, so its positive counts have form p_A+e_j for p_A=(2,1,0,0,0,0). The three AB-coordinate instrument columns have rank at most rank(P)=2 because their nonzero triples are (x1^2*x2*x_j,y1^2*y2*y_j,1), an invertible diagonal transform of P's rows. Likewise every BA-first word has counts p_B+e_j, p_B=(1,2,0,0,0,0), with at most two BA instrument dimensions. The other seven feature coordinates contribute at most three each. Hence rank(H9)<=2+2+7*3=25.

### Proof 2: oblique affine line with x1!=x2 attains 25

EC49DX provides eight genuine length-8 words with positive counts p_A that span E_A={z_BA=0} of dimension 8; eight words with p_B span E_B={z_AB=0} of dimension 8. Both explicit core witnesses are reproduced/reconstructed by the checker accompanying this work, with exact 8x8 integer determinant +/-1. Their intersection has dimension 7 and their sum is R^9.

Prefix every core word with the neutral primitive pair (+Ej,-Ej), j=1..6. This preserves displacement, bucket and last port, while multiplying X,Y by x_j,y_j. These length-10 A/B rows span E_A tensor W_A and E_B tensor W_B, where
W_A=span_j (x1^2*x2*x_j, y1^2*y2*y_j,1),
W_B=span_j (x1*x2^2*x_j, y1*y2^2*y_j,1).
Both W are 2-planes since rank(P)=2. The relation y_j=a*x_j+b gives normal vectors (a/(x1^2*x2),-1/(y1^2*y2),b) and (a/(x1*x2^2),-1/(y1*y2^2),b). If a*b!=0, equality of planes forces x1^2*x2=x1*x2^2 and hence x1=x2. Thus for x1!=x2 the planes have a one-dimensional intersection. The tensor-intersection dimension is 7*1=7, so the two families already span 8*2+8*2-7=25. Combine with upper bound.

### Proof 3: oblique affine line with x1=x2 also attains 25

Write u=x1=x2, U=y1=y2=a*u+b. As x is nonconstant, choose an axis j in {3,4,5,6} with v=x_j!=u, V=y_j=a*v+b. Restrict to genuine 10-step histories with positive steps only along 1,2,j, and group by k=p_j. Exactly the following coordinate-feature subspaces are spanned:
k=0: {0,1,2,3,4,5,6,7,8};
k=1: {0,1,2,3,4,5,6,7,8};
k=2: {0,1,2,5,6,7,8};
k=3: {0,7,8};
k=4: {0}.
The upper inclusions follow from the minimum number of E1/E2-positive steps needed for both events (three), one event (two), and a final +E1/+E2 port (one). The lower equality is certified by **29 actual full signed X6 paths**, grouped as 9,9,7,3,1; each group's selected feature-column square determinant is exactly +/-1. The encoded JSON contains every path, exact positive counts, terminal event/port and features. The independent executable reconstructs all paths and Bareiss determinants. A change of the inert index j among axes3–6 does not change the A/B transition.

At fixed k all such histories share the instrument triple w_k=(u^{4-k} v^k, U^{4-k} V^k,1). Set r=v/u, s=V/U. Because a*b*(v-u)!=0 and y>0, r!=1, s!=1, r!=s, so det(w_0,w_1,w_2)=u^4*U^4*(r-1)*(s-1)*(s-r)!=0. The nested coordinate subspaces therefore split the rank into the nine coordinate directions: N has five k choices and instrument rank3; A,B,A-tail,B-tail each have three k choices and contribute 4*3; the two N-tail features each have four and contribute 2*3; AB and BA each have two and contribute 2*2. Total 3+12+6+4=25.

### Proof 4: exact rank 18 or 9 for globally dependent instruments

For proportional weights y=c*x, fixed m gives Y(w)=c^m X(w), hence two of three instrument groups are linearly dependent. If x is uniform, X(w) is constant at fixed n and is a constant multiple of count; similarly for uniform y. All give rank<=18 for every even n. In each rank-two nonuniform case, the two eight-path core families with neutral-pair prefixes span a common two-dimensional instrument plane (because at least one channel varies across axes), while E_A+E_B=R^9. This supplies 9*2=18 independent rows at n=10. Both-channel uniform has rank<=9 at all lengths; nine genuine n=10 words with identical p=(2,2,0,0,0,0) already span all nine features, proving rank9. Neutral prefix insertion preserves these lower ranks at all later even lengths.

### Proof 5: sharp recovery in exactly twelve steps for oblique rank two

Choose two axes i,j with distinct first-channel weights s=x_i!=t=x_j; write u=y_i=a*s+b and v=y_j=a*t+b. Prefix every eight-core A/B word by TWO neutral native pairs, with index choices (i,i),(i,j),(j,j). This preserves exact D and ordered-event state, and gives multiplicative instrument rows (s²,u²,1), (st,uv,1), (t²,v²,1). Their exact 3x3 determinant is
**(s-t)(u-v)(s*v-t*u) = a*b*(s-t)^3 != 0**.
Hence the three prefixes give the full R^3 instrument space for each core feature vector; all A words span E_A tensor R^3 and B words span E_B tensor R^3. Since E_A+E_B=R^9, they span R^27. The 10-step upper bound is 25, and shorter admissible even lengths embed via neutral prefixes with invertible instrument scaling, so 12 is first. Further neutral prefixes preserve full rank for all later even lengths. QED.

## Actual executed verification and proof boundary

The standalone Python standard-library checker is stored losslessly as VERIFY_EC49DY.py.gz.b64, and its actual output as EC49DY_EXECUTED.json.gz.b64. Decode with base64 -d | gzip -d. The executable rebuilds exact signed six-axis words, end displacement and first-event order, checks the 29 native k-basis words and two eight-path cores, verifies a 48-word two-neutral-pair 27-dimensional tensor construction, and calculates integer determinants via fraction-free Bareiss. It performs 16 reference rank computations (eight strictly positive parameter sets at each of n=10,12) over both primes 1000003 and 1000033, with expected ranks 25/27, 18/18 or 9/9. For oblique example x=(2,2,2,2,2,3), y=(5,5,5,5,5,7), genuine-history exact integer maximal minors include a nonzero 25x25 determinant **-248935680000000000000000** at n=10 and 27x27 determinant **1793420802776171520000000000000000** at n=12. All actual word witnesses, chosen columns, modular outcomes and exact minors are in the encoded JSON.

The theorem is a real-parameter analytic proof supported by finite **combinatorial** certificates; the eight samples do not substitute for the algebraic argument. Corresponding future operator observation ranks for h>=2 use EC49DX's inherited author-side future-transfer lemma; no new independent audit of that lemma is claimed. No physical calibration, formal prover, Source-native Result or independent Driver decision is claimed.

## Authority, preservation and successor

Current authenticated GitHub login is awdawmip with repository write access. The native Enterprise Math gateway is static-machine-readonly, has research_authority_granted=false; owner list returned CONTROL_QUOTA; own researcher session request returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. No verified active owner, current CLAIM, frozen Result, independent review or Foundation admission is inferred from this Draft PR source publication.

Next: **EC49DZ** independently audits EC49DX's nine-feature future transfer, including the exact seam-first-event transition and both BRC multipliers for returning a–e language at h=2,3, then analytically checks the (ae)^k promotion to all finite future horizons. Test restricted operation subsets for loss of feature observability. This work preserves frozen scientific inputs and original P000/ACTIVE world premises.
