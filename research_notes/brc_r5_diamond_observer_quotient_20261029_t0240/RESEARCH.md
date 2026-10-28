# R5 — exact four-observer projection of the rank-two diamond

Research date: 2026-10-29 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. This is author-side portable mathematical research, not a native CLAIM, frozen Result, Driver review, or X6 transfer.

Frozen input: GLOBAL_KNOWLEDGE_V1 main@205ef3f46928d3660ef4246ed8f999743670080c; enterprise-math main@216dccb996235366ed58ef12b534bf64272e9cd6. Read canonical bootstrap/manual, P000, ACTIVE worldview, current portable research protocol, and preceding research_notes/brc_r5_tree_polytope_diamond_20261029_t0140/RESEARCH.md.

## New theorem (all real behavioral strategies)

The previous R5 note exhibits a genuine two-route, two-source likelihood-ratio diamond whose source-resolved continuation-flow set is nonconvex (rank-two incoming source vectors). For the SAME diamond when the common merged time-3 LR=3/2 state continues into a final kernel eta that is independent of the source and incoming path, the actual image of every seedless LR policy in four observables O=(e_P,e_Q,T_P,T_Q) is a **compact convex polytope**. Its survival-flow base has **exactly eight vertices**. For every signed real 4-vector c, the precise support function is the eight-vertex expression below. In particular this diamond cannot realize equal full/LR convex hulls with unequal actual images: whenever the hulls are equal, the actual sets are equal. This conclusion is observer- and tail-kernel-scoped.

## Exact strictly positive two-measure model

Signatures S=(1/2,1,3/2,5/2), parent LR r=3/2. Q origin masses A=B=1/4 at the root time1 and forced terminal Q mass 1/2 at LR=1/2. Thus initial P masses are 3/8,3/8,1/4, both laws sum to 1. At time1 the origin-indexed Q transition kernels are
mu_A=(7/50,11/75,1/2,16/75),
mu_B=(17/200,23/150,3/5,97/600).
Time2 nonterminal children: left at LR=1 and right at LR=3/2, with Q kernels:
nu_A,L=(1/2,1/6,1/4,1/12);
nu_B,L=(5/12,1/3,1/6,1/12);
nu_A,R=(17/100,23/75,1/5,97/300);
nu_B,R=(31/120,5/18,1/15,143/360).
Time3 observed LR=3/2 is one merged nonterminal state; all other time3 outcomes stop. A continuation from the merged state stops at time4 after source-independent Q kernel eta=(1/8,1/4,3/8,1/4). Every listed kernel is strictly positive, sums to 1, and has expected child LR equal to parent LR. Define P(child s | origin, parent r)=s Q(child s | origin,parent r)/r. This normalizes P exactly.

An LR behavioral policy uses one fresh stopping/continuation coin per observable (t,s) state and a terminal declaration coin per observable (t,s) cell; it has no persistent random seed. Full-history policies may condition on source/path. Every following variable and quantifier is real, not finite-grid restricted.

## Exact linearization and constructive proof

Let U be root continuation probability; L and R the unconditional root-to-time2-left/right continuation factors (U times the respective time2 continue probability); M the *aggregate Q mass* continued at the time3 merged state. Two exact incoming coefficients are
C_L = sum_i (1/4)mu_i(1)nu_i,L(3/2) = 7/450,
C_R = sum_i (1/4)mu_i(3/2)nu_i,R(3/2) = 7/200.
The complete seedless LR flow domain is the rational linear polytope

    0 <= U <= 1,  0 <= L,R <= U,  0 <= M <= C_L L+C_R R.          (1)

Necessity: for actual local continuation probabilities alpha0,alphaL,alphaR,gamma, the flows are U=alpha0, L=U alphaL, R=U alphaR, M=gamma(C_L L+C_R R). Sufficiency: for any (U,L,R,M) in (1), choose alpha0=U; alphaL=L/U and alphaR=R/U if U>0, else zero; gamma=M/(C_L L+C_R R) if the denominator is positive, else zero. These are legal seedless behavioral coins and recover exactly the original flows, including boundary cases.

Write W_(t,s) for the aggregate Q terminal mass. With i in {A,B}, a_i=1/4, its fourteen cells are EXACTLY:

    W_(1,1/2) = 1/2, W_(1,3/2) = (1-U)/2;
    W_(2,s) = U sum_i a_i mu_i(s) for s=1/2,5/2;
    W_(2,1) = (U-L) sum_i a_i mu_i(1);
    W_(2,3/2) = (U-R) sum_i a_i mu_i(3/2);
    W_(3,s) = L sum_i a_i mu_i(1)nu_i,L(s)
             +R sum_i a_i mu_i(3/2)nu_i,R(s), for s != 3/2;
    W_(3,3/2) = C_L L+C_R R-M;
    W_(4,s) = M eta(s), for all s in S.                           (2)

All W are affine in the four flows. Mean preservation ensures sum W = sum sW = 1. P terminal mass at each cell is exactly sW. Terminal declaration can be parameterized by joint Q declare-P mass m_(t,s), with 0 <= m_(t,s) <= W_(t,s). Every such m is implemented by a single LR terminal coin theta=m/W when W>0, else zero. The four observables are exactly

    e_P = 1 - sum_(t,s) s m_(t,s), e_Q = sum_(t,s) m_(t,s),
    T_P = sum_(t,s) t s W_(t,s), T_Q = sum_(t,s) t W_(t,s).

Equations (1)-(2) and 0<=m<=W are bounded linear rational constraints; the observer is a linear-affine map. The bidirectional policy construction proves that its projection is EXACTLY the real LR observation image: hence a compact convex polytope, not just its convex hull. The full-history class is a finite tree when full source/path is retained, and its analogous prefix-flow polytope also has convex image. Since O_LR is contained in O_full, conv(O_full)=conv(O_LR) implies O_full=O_LR in this exact diamond. QED.

## Eight vertices and complete signed support

For U>0, normalize (x,y,z)=(L/U,R/U,M/U). The domain is [0,1]^2 with 0<=z<=C_L x+C_R y. It is the convex hull of the four lower square corners and four upper affine corners, with (0,0,0) shared: seven points. Adding the U=0 zero-flow point gives exactly eight flow vertices V8:

    (0,0,0,0), (1,0,0,0),
    (1,1,0,0), (1,1,0,7/450),
    (1,0,1,0), (1,0,1,7/200),
    (1,1,1,0), (1,1,1,91/1800).

For arbitrary real signed c=(c1,c2,c3,c4), the declaration term is (c2-c1 s)m_(t,s), and its maximum is max(0,c2-c1 s)W_(t,s). The remaining objective is affine in the flows. Hence the exact all-signed support is

    h_LR(c) = c1 + max_(v in V8) sum_(t,s) W_(t,s)(v)
                   *[t(c3*s+c4) + max(0,c2-c1*s)].              (3)

The lower support is -h_LR(-c). Thus all signed support directions require only eight finite exact vertex evaluations. This does not infer equality with full-history supports; that is a separate test for the mother question.

## Origin-flow counterexample erased by exact four-observer quotient

The two path-origin Q vectors are v=(11/1200,23/3600) and w=(1/40,1/100), with det(v,w)=-49/720000. The source-flow midpoint of (incoming,continued)=(v,v) and (w,0) would have x=(v+w)/2,y=v/2 and wedge y_A*x_B-y_B*x_A=-49/2880000 !=0, thus cannot be realized as source-resolved outgoing flow by one seedless gamma.

But its *entire 14-cell aggregate terminal distribution* is realized by the real seedless LR continuation probabilities (root,left,right,merged)=(1,1/2,1/2,4/13). The corresponding linear flow midpoint is (U,L,R,M)=(1,1/2,1/2,7/900). With terminal declare-P rule theta_(t,s)=(t+j)/12 for the one-based index j of s in S, the two endpoint observer vectors and the exactly realizable midpoint are:

    O1 = (13513/21600, 523/1800, 1109/600, 2863/1800);
    O2 = (11399/19200, 191/640, 173/80, 71/40);
    Omid = (42139/69120, 16963/57600, 4813/2400, 3029/1800)
         = (O1+O2)/2.

So source-resolved flow nonconvexity DOES NOT imply four-observer nonconvexity. BRC provenance may only be discarded after a proved observer-and-future-operation quotient; this exact proof is one such scoped certificate, not source-state equivalence.

## General tail-response criterion and remaining mathematical gap

Suppose the final Q kernels eta_i can depend on origin. Let v_i and w_i denote pathwise source Q masses, with C_L=sum v_i, C_R=sum w_i. The very same linearization remains valid if for every s

   sum_i(v_i eta_i(s))/C_L = sum_i(w_i eta_i(s))/C_R = bar_eta(s). (4)

Then W_(4,s)=M bar_eta(s). This is a SUFFICIENT condition, not a claim of necessity for convexity. For exactly two sources the cross-multiplied residual equals

   C_R sum_i v_i eta_i(s) - C_L sum_i w_i eta_i(s)
     = det(v,w)*(eta_A(s)-eta_B(s)).

Since det(v,w) is nonzero here, (4) reduces to eta_A=eta_B. Source-heterogeneous tails remain an OPEN case; failure of (4) alone proves neither nonconvexity nor the mother target.

## Evidence, scope, and prior art

VERIFY.py was executed locally using Python Fraction exact rational arithmetic. It checks both-law kernel normalizations, CL/CR, wedge and midpoint, reconstruction of 1,600 rational behavioral-policy mixtures (including exact declaration coins), and the eight-vertex signed upper bound for 800 signed integer directions and 4,000 sampled policies. Actual stdout is EXACT_OUTPUT.txt. The universal real-domain theorem follows from the constructive algebra above; finite tests are regression checks only.

External methodological comparisons (not priority/novelty claims): Laroche & Tachet des Combes (ICML/PMLR 202, 2023), https://proceedings.mlr.press/v202/laroche23a.html ; Piunovskiy & Zhang (SIAM J. Control Optim. 62, 2024), https://doi.org/10.1137/23M1572398 . Their Markov/occupation-measure hypotheses are not automatically valid for hidden-origin LR-only policies. This note proves only the exact finite scoped quotient. BRC resolution: REUSE_APPLIED for positive-rational origin masses, source/path identity, LR P/Q weighting, and future-observer factorization; no typed native Heartbeat/BRC-Shor operation or X6 spatial transfer was executed.

Actual governance boundary: GitHub author-side source preservation is not Source CLAIM/Result/independent Driver acceptance. Native control_tasks returned CONTROL_QUOTA and em_status reported research_authority_granted=false. Active Source Owner is not established by this note. Next exact source-sensitive tail perturbation and proof obligation are in NEXT_TASK.md.
