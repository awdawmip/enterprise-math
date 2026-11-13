# R5: exact full-rank hull equality with a real-image gap from forgotten nonterminal routing

Date: 2026-10-30 Asia/Shanghai. Scope: auxiliary finite two-law LR behavioral model with a **nonterminal binary routing action**. Status: AUTHOR_PROVED / EXACT_BIGINT_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Inputs, BRC and material scope distinction

Frozen GLOBAL_KNOWLEDGE_V1 canonical main@63f701b793312d4d7997eb893a218f9c29c070fb; Enterprise Math main@f05844fa7a1ed5fa3e75fc98eecd757949bcb3f2. Predecessor: PR #1663 @ eb7afd8f238c7b4bfbcaffebb9eb0db1485fc9d9, which proves actual image equality for the earlier 14-history strict stop/continue-only model and an obstruction for its fifth source-sensitive observer. Current canonical account bootstrap/manual, P000, ACTIVE worldview, project bootstrap, joint relation observer contract and portable research protocol were consulted.

This theorem CHANGES the model: at time 1 a policy action chooses between two routes, BOTH of which survive until time 3. It is not a stop/continue-only action. Consequently it is a genuine auxiliary positive construction but **does NOT close the strict original stopping-only mother problem** unless its action alphabet is independently authorized or a faithful reduction back to strict stopping is proved. No native X6 physical realization is asserted; P000/worldview unchanged.

Applied BRC: exactly retained source-labelled positive rational branch carrier (X,U,Y), separate P and Q masses, collision-key quotient only for the seedless LR decision rule and no unjustified compression of route provenance. The current source interface is definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at Enterprise Math main@f05844fa...; positive weighted mass does not prove signed observer completeness. Reuse resolution: REUSE_APPLIED (typed positive branch mass and provenance, observer-specific quotient), no new general BRC tool family.

## Finite model with positive conditional kernels

At t=1 choose nonterminal X in {0,1} with common behavior Pr(X=1)=x in [0,1] under both P and Q. Nature samples U independently conditional on X with

    Q(U=0)=1/2, Q(U=1)=1/2;
    P(U=0)=1/4, P(U=1)=3/4.

At t=3 choose Y in {0,1}: Y=1 stops at t=3; Y=0 continues and is forced to stop at t=4. FULL may choose y_{x,u}; seedless LR sees only (time,P/Q likelihood ratio) and chooses y_u, independent of X. Each U outcome induces a true LR collision between histories X=0 and X=1 at t=3; ratios are r0=1/2 and r1=3/2. All exogenous kernels are strictly positive. No LR persistent random seed is allowed.

The same terminal error-probability kernel is used by the two laws:

    k(X,Y,U)=1/4+X/8+XY/8.

Its only values are 1/4,3/8,1/2 (strictly between zero and one). Observe the standard four quantities

    O=(eP,eQ,TP,TQ),
    eL=E_L[k(X,Y,U)],    TL=4-E_L[Y],    L=P,Q.

The P/Q-labelled path carrier is NOT identified merely because the terminal observer is four-dimensional. Future operations outside these four observers remain out of scope.

## Theorem A: ALL signed convex hulls equal and have full affine rank 4

    conv(O_FULL)=conv(O_LR);  affdim(conv(O_LR))=4.

Proof. The FULL observation is multi-affine in its five independent real parameters x,y00,y01,y10,y11. Its Bernstein representation is a convex combination of its 32 Boolean images. At a Boolean route policy x=0 or x=1, only y_{x,0},y_{x,1} are reachable, and a Boolean LR policy using the same x and those two choices produces exactly the same observation. Therefore the FULL Boolean image is included in the eight LR Boolean observations. Their convex hulls are equal because every LR behavior is also a FULL behavior. This is all-signed support equality by exact convex-hull identity; no finite directional sampling is used.

For LR Boolean x,y0,y1 in {0,1}, the integer-scaled observer is

    v=(32eP,32eQ,4TP,4TQ)
     =(8+4x+x(y0+3y1), 8+4x+2x(y0+y1),
       16-(y0+3y1), 16-2(y0+y1)).

The eight distinct v sorted lexicographically have 4D difference determinant -16 for indices (0,1,2,4,5), where 0 is the base vector. Undoing the diagonal rescaling gives the original observation affine determinant -1/1024, nonzero. QED.

## Theorem B: explicit FULL real observation outside seedless LR

Under LR, X is chosen before the independent U draw and Y depends only on U. Thus for each L in {P,Q},

    E_L[XY]=x E_L[Y],

hence for EVERY real LR behavioral policy,

    eP-eQ = (x/8)(E_P[Y]-E_Q[Y])
           = (x/8)(TQ-TP),   x in [0,1],

which implies the exact nonlinear LR invariant

    |eP-eQ| <= |TP-TQ|/8.                       (1)

Choose the legal FULL policy x=1/2, with Y=X for U=0 and Y=1-X for U=1. In order (X0U0,X0U1,X1U0,X1U1), its P branch masses are (2,6,2,6)/16 and Q masses (4,4,4,4)/16, all positive. Exact expectations are

    E_P[X]=E_Q[X]=1/2;
    E_P[Y]=E_Q[Y]=1/2;
    E_P[XY]=1/8; E_Q[XY]=1/4.

So the FULL observer is

    O*=(21/64, 11/32, 7/2, 7/2).

It has TP=TQ while eP differs from eQ by 1/64, contradicting (1). Therefore O* belongs to the FULL actual real image but not the LR actual real image, although the entire four-dimensional convex hulls agree. QED.

For the raw four-coordinate L-infinity norm, let epsilon be the distance between O* and a seedless LR observation O'. We have |eP'-eQ'| >= 1/64-2epsilon and |TP'-TQ'|<=2epsilon. By (1), 1/64-2epsilon<=epsilon/4. Hence

    dist_infty(O*,O_LR) >= 1/144.

This is a valid lower bound, NOT claimed optimal. It is a real-strategy universal result by the exact invariant, not a grid search.

## Exact verification and next scientific boundary

The standalone standard Node.js VERIFY.js executed under v22.16.0. It checks all eight Boolean LR and 32 Boolean FULL policies, exact inclusion of every FULL Boolean observer in the LR Boolean set, BigInt signed determinant -16, exact normalized positive branch masses, witness values and LR Boolean identity. EXACT_OUTPUT.txt is the original executed output, ending PASS_EXACT_R5_ROUTING_MEMORY_FULLRANK_HULL_EQUAL_REAL_IMAGE_GAP. Universal claims rely on the multi-affine and conditional-independence proofs above; computation checks the finite hypotheses.

The stop/continue-only mother problem remains OPEN. If first-stage nonterminal route actions are allowed by the exact Task contract, this example is a candidate pending independent review; if not, use its latent-action-memory mechanism as a discriminator for searching an allowed topology or proving a stop-only obstruction. Do not promote an auxiliary model, GitHub commit or author's proof into native Source admission.

Authority observed: native research_authority_granted=false; bounded active owner read CONTROL_QUOTA; own em_session_start explicitly STATIC_READONLY_SCOPE_DENIED and operation_sent=false. No Source CLAIM/Result/Driver review, and no Google Drive fallback to bypass this denial.