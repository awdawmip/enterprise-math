# Stage152 — exact all-real optimal affine segment (N=14 auxiliary iid model)

**Evidence status:** AUTHOR-side exact rational computation-assisted proof, not independently Driver-reviewed, not a native TASK CLAIM/Result, and not a P000/X6/Heartbeat theorem. Consumes Stage151 author result in research_notes/n14_aux_iid_affine_151_20261026/PROOF_STAGE151.md and NEXT_TASK_PACKET_152.md.

## Statement

The finite ternary iid test has horizon 14, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), and permits policies randomized at complete ordered histories. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P[tau], tQ=E_Q[tau]. Define V14(alpha)=min max(tP,tQ) with both errors <=alpha.

Set

    alpha151 = 18373001785623238325/52808422392537808896
    V151     = 318746112099955105013/26404211196268904448
    eta152   = 6360587975/206282899970850816
    alpha152 = 18373003413933759925/52808422392537808896
    V152     = 318745538371909741813/26404211196268904448

**Theorem:** for every REAL 0 <= delta <= eta152,

    V14(alpha151+delta) = V151 - (25612859168/36346217)*delta.

The Bellman affine support is a global lower bound for all alpha and is strictly below V14(alpha) for every alpha > alpha152 (right-sharp).

## Exact Bellman bound on every ordered-history policy

Take K=12844717560/36346217, L=12768141608/36346217. For count state s=(n,a,b), the ratio Q(prefix)/P(prefix)=2^(a+b)/3^a. Recursively set

    H(s) = min( K*2^(a+b)/3^a, L, 1+sum_i P_i*H(child_i(s)) )

with continuation omitted at depth 14. The first action is decide P, second decide Q. Conditioning at each fully ordered prefix proves that the finite iid suffix conditional expectation only depends on s, and yields universally

    H(root) <= tP + L*eP + K*eQ <= max(tP,tQ)+(K+L)*alpha.

Exact rational recursion evaluates all binom(17,3)=680 count states and yields

    H(root) = 341463027624594134301829727/1327376472826305935572992.

The ONLY action ties are B=(11,0,1), Q/continue, and W=(8,3,3), Q/continue. All 1238 other nonminimal action gaps are positive (minimum 204027667/1130512733568), and no negative gap exists.

## Literal ordered-prefix carriers and observer derivatives

Let b,w in [0,1] denote probabilities to stop and decide Q at B,W; all other states take the strict Bellman minimizer.

Under the strict actions, independent literal-prefix enumeration stopped on first hit yields:

    B: 11 histories, P-mass=107421875/1451188224, Q-mass=107421875/725594112
    W: 224 histories, P-mass=175/7962624, Q-mass=175/3359232.

A count a can only increase. W has a=3 at depth 8, B has a=0 at depth 11. Hence W can never reach B, while B cannot reach W by depth. Thus there is no simultaneous-influence path and the four-observer vector M=(eP,eQ,tP,tQ) is affine in (b,w).

Exact rational backward observer recursion, cross-checked by literal ordered-prefix integer-weight DFS on the four deterministic corners, gives

    M(b,w) = M00 + b*dB + w*dW

    M00=(1212592135672539235/3505953353861431296,
         224492569856365/641959232274432,
         5330367237943930717/438244169232678912,
         70007401392629/5944066965504)

    dB=(4619140625/2229025112064,
        -751953125/417942208512,
        -25673828125/278628139008,
        -17939453125/104485552128)

    dW=(16372475/56358560858112,
        -1952125/10030613004288,
        -78138725/2348273369088,
        -19052425/278628139008).

The mixed four-vector M11-M10-M01+M00=(0,0,0,0) EXACTLY. Literal DFS node visits for (b,w)=(0,0),(0,1),(1,0),(1,1) respectively: 496174, 475342, 496042, 475210. Signed observer increments are differences of positive rational branch masses, not signed-cancellation BRC primitives.

## Real-parameter primal attainment

Solving eP=eQ yields the unique compensation

    b(w) = 8061971501813291/8143872000000000 - (797257531/6362400000000)*w.

For every real 0<=w<=1, b(w) is strictly between 0 and 1, from b(0)=8061971501813291/8143872000000000 to b(1)=2686983670724537/2714624000000000. Substitution gives

    eP=eQ=alpha151 + eta152*w,
    tP=V151-(140070323575/6446340624089088)*w.

The affine time gap tP-tQ is positive at both endpoints and therefore throughout:

    gap(0)=36759675262851533665/79212633588806713344 > 0
    gap(1)=12253888791127786955/26404211196268904448 > 0.

At w=0 and w=1 the exact identity tP+L*eP+K*eQ=H(root) holds; by affinity it holds for every real w in [0,1]. Thus the legal policies attain the universal Bellman bound throughout the real interval; eta152 is positive, so they attain every alpha from alpha151 to alpha152. Their slope K+L=25612859168/36346217 and upper endpoint V152 above follow.

## Sharp right endpoint

The behavioral policy space over finitely many full ordered histories is compact and observer outputs are continuous; the optimum is attained. If some alpha>alpha152 attained the SAME Bellman support, positivity K,L>0 would force both errors equal alpha, tP=max(tP,tQ), and a dual-minimizing action at every reached prefix. Strict states have a unique action. At each tie, the likelihood ratio and suffix laws agree across all ordered prefixes sharing the count state, hence arbitrary history-dependent coins can be P-mass averaged into a single effective b or w preserving both error and both sample-time observers. The first-hit path cones are disjoint, so the resulting observer lies in the affine square M(b,w). Equality eP=eQ forces b=b(w); for 0<=w<=1 the equal error is <=alpha152. Contradiction. The same support is therefore strict beyond alpha152; no next-stage theorem is claimed.

## Reproduction and restrictions

Original local Python 3 stdlib verifier uses exact Fraction Bellman recursion and complete count-state gaps, followed by exact corner observer recursion and separate literal ordered-prefix DFS with integer likelihood weights. The first-hit histories are enumerated before any count quotient. Its run log, JSON certificate, and source are in the complete local evidence package; numerical assertions above are the actual output. These are two AUTHOR arithmetic cross-check paths, not independent Driver review or proof-assistant verification.

BRC resolution: positive-rational ordered branch mass/provenance is retained until the count-suffix observer sufficiency argument; this is a real use of the BRC interface, not a native Cell-model theorem. No X6 slice embedding or Heartbeat transport has been established. The current user-locked P000 axioms remain unchanged.

GLOBAL_KNOWLEDGE_V1 pinned this run to main@43639a1bd021e9c6e90e699fbb7b5021855fbef7; Enterprise Math initial main@b3d16cec31ce33651cf8702e2e00847b9e3da3ca. GitHub authenticated principal awdawmip has repository push permission. Native task listing returned CONTROL_QUOTA, and own session_start was rejected STATIC_READONLY_SCOPE_DENIED with operation_sent=false. No native owner, CLAIM, Result or independent Driver success is asserted. Publication here is a source-only AUTHOR checkpoint.

**Next unit (Stage153):** With W Q-stop saturated at 1 and B still mixed, scan an exact new positive dual ray maintaining B's Q/continue tie, locate the next closing gap; then calculate first-hit cones and primal coin feasibility before any optimal-interval claim.
