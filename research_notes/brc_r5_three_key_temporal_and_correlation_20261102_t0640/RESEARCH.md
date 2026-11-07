# R5: Three causally coupled stopping keys and a conditional-correlation benchmark

Research date: 2026-11-02 (Asia/Shanghai). Author-side result: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

Frozen scientific input: GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Separate current-rule reads: global main@aa5e3ee8aa3481ececba9181847bb7b28a9ba41f; EM main@89453173bf0e78d01726362d8f8d79c115235346. Global P000 startup projection matches original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview read and not edited. Predecessor: 2c75fef0e35b7b9c80f4c7443331afc04e4e68b5, causal-diamond proof. The statements below concern a precisely defined auxiliary two-law finite stopping DAG and a separately identified abstract BRC benchmark; no native X6 transfer is claimed.

## A. Actual two-law finite stopping DAG with three interacting keys

Observation: O=(eP,eQ,TP,TQ). Stopping at integer time t answers P and yields S_t=(1,0,t,t); a terminal natural answer at t with answer-P probability p under law P and q under law Q yields A_t(p,q)=(p,1-q,t,t).

The natural root branches with identical P/Q probabilities: 1/2 to I=(1,LR=1), 1/4 to J=(2,LR=1) by the B route, 1/4 directly to K=(3,LR=1) by the C route. At I, stop at time1 or continue; on continuation, natural probability 1/2 reaches J from I and 1/2 reaches K directly from I. At J, stop at time2 or continue; on continuation, natural probability 1/2 reaches K (marked BJ or IJ) and 1/2 terminates at time3. J-B natural final answer uses (p,q)=(2/5,3/5), while J-I uses (p,q)=(3/5,2/5).

At K, stop at time3 or continue. On continuation, the terminal natural answer occurs at time5 with conditional probabilities dP under P and dQ under Q, and at time4 otherwise. Its answer-P probabilities under P/Q are (p,q), independent of which time4/time5 final branch occurred. The K source-conditioned kernels are:

| Source | p | q | dP | dQ |
|---|---:|---:|---:|---:|
| C (root→K) | 3/4 | 1/4 | 1/4 | 3/4 |
| I (I→K) | 1/4 | 3/4 | 3/4 | 1/4 |
| BJ (B→J→K) | 2/3 | 1/3 | 1/3 | 2/3 |
| IJ (I→J→K) | 1/3 | 2/3 | 2/3 | 1/3 |

All natural branches and terminal Bernoulli probabilities are strictly between 0 and 1 under both laws, including complements. Every path before its last decision has identical P/Q probability; therefore all arrivals at each named decision key have its declared exact time and likelihood ratio 1. No decision follows K's source-dependent natural kernel. The positive BRC source carriers are retained separately; signed temporal differences below are observer readouts and not signed probabilities.

FULL may use seven independent behavioral stop probabilities (x,jB,jI,kC,kI,kBJ,kIJ), each in [0,1]. LR is seedless, sharing jB=jI=y and kC=kI=kBJ=kIJ=z, with (x,y,z)∈[0,1]^3. The mixed term (1-x)(1-jI)(1-kIJ) makes the upper I and J controls jointly affect the provenance arriving at K, rather than adding independent diamonds. The observation map is multi-affine in each behavioral parameter, so deterministic binary choices suffice for support maximization. There are 128 FULL and 8 LR binary policies.

### Exact temporal separator

Consider the signed linear observation n=(0,0,1,-1), i.e. D=TP-TQ. Only K continuation contributes to this difference. The four source masses entering K, multiplied by their respective dP-dQ, yield for every real behavioral FULL policy:

    D_FULL = -(1-kC)/8
             +(1-x)(1-kI)/8
             -(1-jB)(1-kBJ)/24
             +(1-x)(1-jI)(1-kIJ)/24.

Each of the positive contributions is at most 1/8 and 1/24, and both negative ones are nonpositive. All maxima can be attained simultaneously by the deterministic FULL policy (x,jB,jI,kC,kI,kBJ,kIJ)=(0,1,0,1,0,1,0). Hence max_FULL D=1/6. Independently summing all P/Q physical terminal flows gives that policy's complete four-observer vector

    W=(163/240,43/240,163/48,155/48),

so D(W)=1/6. In LR, substitution of the shared y,z variables collapses the expression exactly to

    D_LR(x,y,z)= -x(1-z)(4-y)/24 <= 0

for every x,y,z in [0,1]; equality holds at x=0. Therefore h_FULL(n)=1/6, h_LR(n)=0, and the exact signed support gap is 1/6. By L1/L∞ duality and ||n||_1=2,

    dist_infty(W,conv(LR real image)) >= 1/12.

This phenomenon is not caused by a low-rank LR hull. The LR deterministic vectors indexed (x,y,z)=(0,0,0),(0,0,1),(0,1,0),(1,0,0),(1,0,1), using the first as the origin and the remaining as columns, have four-dimensional determinant exactly 1/5120. Hence the LR four-observer convex hull is full dimensional.

## B. Finite-hull plus Jacobian-rank theorem

Let L:[0,1]^k→R^d and F:[0,1]^m→R^d be multi-affine, with k<d≤m, and L(image) included in F(image). Assume every FULL binary vertex F(e) lies in the convex hull of the LR binary vertices L(v). Then the two entire real-image convex hulls are equal. If DF has rank d at an interior point, their **actual real images differ strictly**.

Proof: multi-affine interpolation writes each F output as a convex combination of its binary outputs, yielding containment in the LR vertex hull; reverse inclusion follows from assumed image inclusion. L is Lipschitz on a compact k-cube. A grid of O(h^(-k)) domain cubes of side h maps into d-dimensional boxes with volume O(h^d), giving image d-volume O(h^(d-k))→0. Fixing m-d coordinates at a full-rank interior DF minor and applying the inverse function theorem to the other d coordinates yields a nonempty d-dimensional open set in F(image). This open set cannot be inside L's measure-zero image. This supplies an exact search certificate: finite FULL-vertex LR convex decompositions plus a single nonzero FULL rank minor, without first eliminating a specific real point. Physical realization of the model and equal decision-key semantics remain separate requirements.

## C. Exact source-conditional correlation benchmark (abstract, not yet a stopping DAG)

Let X be a binary first source label with marginal P(X=1)=x. Conditional second choices are u=P(Y=1|X=0) and v=P(Y=1|X=1). The BRC joint carrier has nonnegative masses

    p00=(1-x)(1-u), p01=(1-x)u,
    p10=x(1-v),     p11=xv,

which sum to one. Read out (x,y,z,t) where y=p01+p11, t=p11, z is an independent [0,1] control. FULL source-aware and common-parameter LR maps are

    F(x,u,v,z)=(x,(1-x)u+xv,z,xv)
    L(x,y,z)=(x,y,z,xy), a restriction u=v=y.

At each binary FULL corner x=0 or x=1, its unreachable conditional choice disappears; the FULL and LR binary corner images are exactly the same eight vertices. Thus BOTH convex hulls are the four-dimensional McCormick polytope

    0<=x,y,z<=1,  max(0,x+y-1)<=t<=min(x,y).

The LR vertices (0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(1,1,0,1) have affine determinant 1. The FULL Jacobian in parameters (x,u,v,z) has determinant -x(1-x), so the rank theorem applies for 0<x<1.

An explicit point is F(1/2,0,1,1/2)=W0=(1/2,1/2,1/2,1/2), which equals [L(0,0,1/2)+L(1,1,1/2)]/2 and hence lies inside the LR convex hull. But an LR point with the same first two coordinates must have t=xy=1/4 instead of 1/2, proving actual-image nonmembership. Moreover,

    dist_infty(W0,LR real image) = (sqrt(5)-2)/2.

Proof: if an LR point is within ε of W0, its x,y are <=1/2+ε but xy>=1/2-ε. Hence ε²+2ε-1/4>=0, giving ε>=(sqrt(5)-2)/2. Equality holds for x=y=(sqrt(5)-1)/2 and z=1/2. The source-correlation residual t-xy survives the four-coordinate observer although it leaves the convex hull unchanged. This benchmark proves the desired geometric mechanism in a conditional-live-source model. Its first binary control leaves BOTH outcomes live; in an actual stopping tree the stopped branch terminates. A physical stopping realization is therefore the concrete next open step, not claimed by this abstract construction.

## D. Evidence, authority, and next unit

The attached VERIFY.py ran using only Python standard-library Fraction and exact integer arithmetic. Its captured EXACT_OUTPUT.txt ends in PASS_EXACT_R5_TWO_MEASURE_THREE_KEY_AND_CORRELATION_BENCHMARK. It checks 2,477 exact assertions, 128 physical FULL / 8 LR deterministic vertices, noncorner behavioral formula identities, positive terminal kernels, both exact witnesses, LR rank determinant, 16/8 abstract binary corners and the algebraic distance polynomial. The all-real temporal inequality and general Jacobian/rank theorem are proved algebraically above; finite regression is independent arithmetic corroboration, not an extrapolated real-domain proof.

Native Sites credential read on 2026-11-02 was static read-only: research_authority_granted=false; write_relay_enabled=false; scopes em:access,source:read,control:read. A bounded native owner inventory query returned CONTROL_QUOTA, so no authenticated current task owner, CLAIM, native Result or Driver review was obtained. Connected GitHub author-side PR publication is distinct from native research admission.

Next: modify the interacting I→J→K source pathways/kernels so the currently exact temporal gap vanishes. Then **for every FULL deterministic four-observer vertex**, obtain a rational LR convex decomposition or an exact rational Farkas separator. Only after all vertices pass, compute an interior 4×4 Jacobian minor with at most three LR controls; the finite-hull/rank theorem would then establish actual real-image inequality. Preserve all natural positive P/Q branches, time–likelihood-ratio key identity, frozen P000 and source provenance. See NEXT_TASK.md.