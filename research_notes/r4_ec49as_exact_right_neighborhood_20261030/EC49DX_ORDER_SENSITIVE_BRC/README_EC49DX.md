# EC49DX — First-occurrence-order BRC observer: nine historical features and sharp 27-rank criterion

Date: 2026-11-02. Status: AUTHOR_ANALYTIC_PROOF / EXACT_CHECK_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED. Parent: EC49DW, pinned predecessor 5d5aca996e5d880d10377fae31a3ed6077c313c7. Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1@773d538180bfb49e24cffeb35c3ee75eb0628e2e, EnterpriseMath@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Read-only current norms: global main@576eea8c767fc6c5328aac083b07ea4a71330c2c; EM main@d8dad1ccde5229a865dc26cea5dade362284adfd. P000 and ACTIVE worldview unchanged.

## Model and precise new observer

A genuine historical word w is an ordered signed primitive path in all six Enterprise native X6 axes, with even length n and full six-axis displacement D=−2E1. An A event occurs at any adjacent (+E1,+E2); a B event at any adjacent (+E2,+E1). Unlike the old four-flag observer, the new observer retains which event first appeared. Its terminal buckets are N (neither), A (A only), B (B only), AB (both, A first), and BA (both, B first). Simultaneous first A/B occurrence is impossible because an adjacent primitive pair cannot have both orders. Define last port L=1 if last historical primitive +E1, L=2 if +E2, otherwise L=0.

The new nine Boolean historical features in their fixed order are:

    z9(w)=(1[N],1[A],1[B],1[AB],1[BA],
           1[A and L=2],1[B and L=1],1[N and L=1],1[N and L=2]).

For strictly positive real six-vectors x,y, set p_i(w)=the number of positive +Ei primitives, X(w)=product_i x_i^p_i(w), and Y(w)=product_i y_i^p_i(w), with negative-step weight one. The third instrument is path count. The historical 27-column matrix has rows H9(w)=(X(w)z9(w),Y(w)z9(w),z9(w)). Every future operation is a fixed signed native path and future words are open-loop, independent of hidden historical states. Returning future words must have displacement +2E1 in all six native components; their final buckets are separately read with X,Y,count.

The original five operations are a=(−1,−1), b=(−2,−2), c=(1,2,−1,−2), d=(2,1,−2,−1), e=(3,1,1,−3). Here j means +Ej and −j means −Ej. Additional f=(1,−1), g=(2,−2) and h,i with internal events are optional; the main theorem needs only a through e.

## Theorem 1: universal nine-feature transfer, and minimality

For every x,y∈(0,∞)^6, any finite set of genuine historical paths at D=−2E1 and any collection of fixed open-loop future signed-X6 words, every future word/bucket/instrument readout lies in the column span of H9, so rank O(Γ,h)≤rank H9≤27. If Γ contains the original a–e operations, then for EVERY integer h≥2, for every such historical population,

    rank O(Γ,=h)=rank H9,    rank O(Γ,1..h)=rank H9.

Nine Boolean features are necessary on the full native historical domain: nine genuine ten-step paths all with the same positive-step vector p=(2,2,0,0,0,0) form a 9×9 z9 matrix with determinant −1. Equal positive counts make their BRC multipliers equal for arbitrary x,y, so this is also a physical path-count certificate for nine independent historical seam memories.

PROOF OF FACTORIZATION. All new event occurrences in concatenation w·t are internal to the known fixed future t or involve the unique seam (last primitive of w, first primitive of t). In historical N state, seam effects depend only on whether L=1, L=2 or neither; the N-port pair is two added features. In historical A-only state, the only relevant seam discovery is B, requiring L=2; in B-only state, new A requires L=1. AB and BA already lock the first-event order forever, so their last port is observationally irrelevant. Thus the above five buckets and four exceptional port flags determine any future final bucket. Each fixed-future bucket indicator is therefore a linear function of z9. The multiplicative BRC identity X(wt)=X(w)X(t), Y(wt)=Y(w)Y(t) makes each weighted output a linear function of its respective weighted copy of z9, proving the upper factorization. This is scoped to the stated finite open-loop future language and ordered-event bucket observer.

PROOF OF FULL FUTURE SPAN. Under the original alphabet, four returning words ce,ec,de,ed at exact operator horizon 2 generate nine linearly independent ordered-bucket readout columns: a concrete 9×9 integer determinant is +1. At horizon 3, the returning words aee,cce,dce,dde yield another independent 9×9 minor +1. Witness word/bucket column labels, transfer matrices and their exact paths appear in the executed JSON (future_witnesses_a_to_e), reproduced by the saved checker. The composite (ae) has zero full X6 displacement, introduces no A or B adjacency internally or at its boundary with these witnesses, and multiplies future BRC weights by nonzero x3*x1² and y3*y1², respectively. Appending (ae)^k lifts each parity's nine-feature column span to every h≥2. For each weighted instrument the future column multipliers are nonzero, so the three weighted feature families all survive. Combined with the upper factorization, this proves the exact and cumulative rank identities for all positive real x,y. QED.

## Theorem 2: exact necessary and sufficient condition for 27-rank at n=10

Define the explicit 6×3 weight-geometry matrix P with rows P_j=(x_j,y_j,1), 1≤j≤6. For ALL x,y∈(0,∞)^6, historical paths of exact length 10 and D=−2E1 satisfy

    rank H9=27   ⇔   rank P=3.

Equivalently the six weight points (x_j,y_j) are not contained in an affine line. If rank P=3, ten is the earliest even historical length at which the original a–e future observer attains 27 dimensions for every horizon h≥2.

CONSTRUCTIVE SUFFICIENCY. For history length 8 and positive-step count pA=(2,1,0,0,0,0), eight explicit genuinely ordered signed native words have z9 vectors that form a determinant ±1 basis for the 8D subspace EA={z_BA=0}. For pB=(1,2,0,0,0,0), eight other real words analogously span EB={z_AB=0}. Both exact 8×8 minors and all sixteen paths appear in JSON core_path_witnesses. Prefix each of these sixteen words by (+Ej,−Ej) for every j=1..6, obtaining genuine ten-step words with unchanged z9 and D=−2E1 and positive count pA+ej or pB+ej. The associated X/Y/count triples for the A-family are (x1²*x2*xj, y1²*y2*yj, 1); for the B-family they are (x1*x2²*xj, y1*y2²*yj, 1). Positive diagonal row rescaling of P implies each family's instrument triple span has rank rank P. If rank P=3, these two families span EA⊗R³ and EB⊗R³. Since EA+EB=R⁹, their sum equals the entire R²⁷. This explicitly realizes 27 independent columns using real native paths.

NECESSITY. An AB-first history must include the positive subsequence (+E1,+E2,+E1), hence at least positive counts pA=(2,1,0,0,0,0). At n=10 and D=−2E1, exactly four primitives are positive, so every AB-first history has positive count pA+ej for some j. Its three AB-indicator instrument columns (X*1[AB],Y*1[AB],1[AB]) therefore have rank exactly at most rank P, with all other terminal classes zero in these columns. If rank P<3, these three columns are dependent, precluding total rank27. For rank P=2, the disjoint BA block also loses one independent direction, proving the sharper bound rank H9≤25.

MINIMUM LENGTH. At n=8, there are only three positive steps. The AB-first bucket then has only count pA and BA-first only pB. In both buckets the triple X,Y,count is proportional, losing two dimensions apiece and bounding rank H9≤23. Every earlier even admissible length can be embedded in length8 by prefixing fixed neutral pairs (+Ej,−Ej), which act on H9 as invertible instrument-diagonal rescalings. Hence no earlier even history reaches 27. The preceding construction reaches it at n=10 if rankP3. QED.

## Actual execution and scope

The executed Python-standard-library checker decodes from VERIFY_EC49DX.py.gz.b64 (base64 then gzip) and reconstructs real signed native paths, all six displacement coordinates, A/B first appearance, ports and positive count. It exhausts history DP for n=2,4,6,8,10,12, and all returning a–e, a–f and a–g operator words up to h=5 and a–i up to h=4. Exact future transfer ranks: for a–e at h=1,..,5 the ranks are 5,9,9,9,9; adding f/g/h/i retains 9 at h≥2. Independent integer Bareiss determinants are −1 for the nine equal-p witness, −1/+1 for the two eight-history cores, and +1/+1 for horizon-2 and -3 future 9×9 matrices. Modular ranks in primes 1000003 and 1000033 give candidate lower bounds, and maximal selected integer minors plus analytic ceilings give exact ranks where marked.

Named parameter cases:
- x=(2,3,5,7,11,13), y=(17,19,23,29,31,37), rankP3: n8 rank23, n10 rank27, n12 rank27; exact n10 27×27 determinant −2501261740594453078956230833191281217308680047820800.
- x=(2,3,1,2,3,4), y=2x+1, rankP2: n10 rank25 and n12 rank27; integer 25×25 determinant −813156860780612812800000000, combined with upper25.
- x=(2,2,1,2,3,4), y=(3,3,1,3,5,7), rankP2: n10 rank25, n12 rank27; exact n12 27×27 determinant −11979213683847696722023975747584.
- x=(2,3,1,2,3,4), y=2x: n10 rank18; proportional weight ceiling18 with a nonzero integer minor.
- x all 2, y all 3: n10 rank9, all weights uniform at fixed history length.

All selected real-path row certificates, exact maximal minors, scope-tagged modular ranks and transfer column witnesses are in the decoded EC49DX_EXECUTED.json.gz.b64. The checker produces this JSON and deterministic run summary; the full original local proof, script, JSON and hashes also accompany this run's downloadable evidence archive. This document states a model-internal author proof and a finite exact computation, not an independent Driver approval or empirical physical calibration.

## Actual authority and next question

GitHub connector identity: awdawmip, with repository push access. Native gateway 0.6.11 reported research_authority_granted=false; native canonical Owner listing returned CONTROL_QUOTA (5/5), and own RESEARCHER session-start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. Thus no own RA, CLAIM, Result, independent Driver review or Foundation admission was established. This Draft PR source publication is independent of formal machine acceptance. Next EC49DY: classify exact ten-step rank for rank(P)=2 and whether/when twelve steps restores all 27 dimensions for all non-proportional affine families.

