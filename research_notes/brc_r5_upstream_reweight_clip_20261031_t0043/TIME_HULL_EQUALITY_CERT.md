# R5 supplementary theorem: off-diagonal three-class source residual with equal 2D STOP-time convex hulls

**2026-10-31 Asia/Shanghai. Author-side PROVED by exact complete finite facet enumeration; UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Pinned inputs: GLOBAL_KNOWLEDGE_V1 main@7c3130bc1a11f50266cfef83d123c939fdf3917d, Enterprise Math main@d6784e1dad20bf11d02962ba8f199ea95051218a, preceding upstream-reweighted clipping theorem in this research folder. The full current P000, ACTIVE worldview, observer-preservation companion and portable protocol were read and remain unchanged. Native active-owner read returned CONTROL_QUOTA; this paper is portable author-side evidence, not Source CLAIM, Result or review.

## Exact genuine STOP/CONTINUE model

Nature selects X,U in {0,1} and V in {0,1,2}. STOP decisions at times 2,3,4 absorb immediately; time-4 CONTINUE terminates at time 5. FULL observes all history. Seedless LR sees only current time and likelihood ratio P/Q.

Q upstream masses:

    Q(0,0)=49/100; Q(0,1)=1/100;
    Q(1,0)= 1/100; Q(1,1)=49/100.

Time-3 likelihood ratios r0=3/4, r1=5/4; time-4 ratios R=(1/2,1,3/2). Conditional Q transition laws for source x and u:

    K_(x,0)=(1/2+t_x,1/2-2t_x,t_x)
    K_(x,1)=(t_x,1/2-2t_x,1/2+t_x)
    t0=1/16, t1=1/8
    q_xuv=Q(x,u) K_(x,u)(v), p_xuv=R_v q_xuv.

All 12 p and q masses are strictly positive; both measures normalize to 1, with E_Q[R_V|X,U]=r_u. Time-2 source LR classes are 19/25 and 31/25, so LR initially distinguishes X, but loses X within the shared U likelihood-ratio class at time 3. Source-sensitive future kernels differ:

    K_(0,u)-K_(1,u)=(-1/16)(1,-2,1)
    total-variation distance=1/8 > 0.

## Exact theorem

Let T_FULL and T_LR be the sets of all pairs (E_P[tau], E_Q[tau]) induced by REAL behavioral policies in their respective information classes. Then

    conv(T_FULL) = conv(T_LR) = C,

where C is exactly a full-two-dimensional convex polygon with TEN vertices and TEN certified primitive outward facet normals. Consequently, a genuinely non-lumpable positive three-child LR transition can coexist with exact equality of the two-dimensional STOP-time convex hulls. The result is a hull property, not equality of actual time images and NOT yet the desired equality/difference of four-dimensional error-and-time observables.

## Complete exact certificate

Each row states nP*T_P + nQ*T_Q <= beta for every FULL and LR deterministic STOP strategy. LR vertex indices follow CCW cyclic order; the vertex at row j and the next cyclic vertex both saturate row j.

| j | LR vertex (T_P,T_Q) | primitive outward normal (nP,nQ) | beta |
|---:|---|---|---:|
|0|(2,2)|(2074,-2707)|-1266|
|1|(5907/1600,2637/800)|(1,-1)|633/1600|
|2|(6103/1600,547/160)|(22,-19)|474/25|
|3|(3061/800,1373/400)|(1958,-1603)|3979/2|
|4|(309/64,149/32)|(2,-1)|5|
|5|(5,5)|(-2,3)|5|
|6|(287/64,149/32)|(-318,373)|1243/4|
|7|(4937/1600,2771/800)|(-46,53)|1041/25|
|8|(9821/3200,5519/1600)|(-1,1)|1217/3200|
|9|(9233/3200,209/64)|(-4050,2833)|-2434|

### Proof

Each full or LR decision key is visited at most once per path. An expected linear STOP-time payoff is multi-affine in the independent real behavioral control probabilities. Thus every signed support maximum over the relevant policy cube occurs at a deterministic vertex.

FULL has 18 binary controls (2 at stage 2, 4 at stage 3, 12 at stage 4), giving exactly 2^18=262144 deterministic policies. Seedless LR has 7 controls (2,2,3 at corresponding stages), giving 2^7=128 deterministic policies. Unreachable control bits are harmless: both exhaustive domains really include all policies. The verifier builds the 128 exact rational LR time pairs by summing the 12 path masses times the explicitly determined STOP time for each strategy.

The exact Andrew monotone-chain hull algorithm uses rational oriented-area cross products and identifies the ten strictly convex counterclockwise vertices shown. Every adjacent edge produces a primitive integer outward normal and exact support beta. All LR points satisfy all ten halfspaces, and two adjacent LR points exactly saturate each edge, certifying the full 10-facet representation of the LR polygon. Ten noncollinear strictly convex vertices give affine dimension exactly 2.

For every one of the ten facet normals, the analytical Bellman recursion for FULL and LR computes precisely equal support beta, as verified with Fraction arithmetic. Separately from Bellman formulas, the verifier scales all twelve source P/Q masses to one common integer denominator. For all 262144 FULL deterministic policies, it independently constructs the pair of exact integer expected stopping times and checks EVERY one of the ten halfspaces. There are 2,621,440 exact policy-facet checks. Hence all deterministic FULL points lie in the LR polygon. Convex hull of all real FULL behavioral outcomes equals convex hull of deterministic FULL outcomes by multi-affinity; the reverse inclusion follows as LR is a subset of FULL. This proves the equality for every real behavioral policy.

The code VERIFY_TIME_HULL.py is a standalone Python standard-library exact checker. Its captured literal stdout with all ten facet rows and PASS sentinel is EXACT_TIME_HULL_OUTPUT.txt. A finite exhaustive proof applies to this ONE EXACT rational model, not to a continuum of upstream weights. No Monte Carlo, numerical tolerance, abstract hull theorem without checked facets, or presumed independent review is used.

## BRC information/observer scope

The positive-mass source-labeled twelve-branch carrier is preserved until the observer and future operation are declared. The LR projection at time 3 erases X and does not make the next-child kernel constant: the exact source discrepancy is TV=1/8. Yet the two-dimensional *convexified* STOP-time observer is insensitive to that discrepancy for the declared model and STOP horizon. Do not erase X for arbitrary future reward operators or equate a convex-hull result with equality of actual real policy images. This is finite classical probability mathematics reusing BRC provenance-preservation principles, not a native X6/Heartbeat physics claim.

## Next precise independent research unit

Keep the frozen 12 positive source-labeled path masses and true STOP timing. First decide whether the **actual** two-dimensional FULL and seedless LR time-image sets are equal (not just their convex hulls), with a real semialgebraic proof or counterexample. In parallel select source-dependent terminal P/Q error reward kernels and obtain an exact four-dimensional hull equality certificate with affine rank four: every FULL deterministic four-vector as a nonnegative rational combination of at most five LR four-vectors, or a strict rational separator. Only after the 4D hull prerequisite passes prove actual FULL/LR real-image inequality, or else produce an exact LR lift. Keep this 2D hull equality as a consumed verified author-side lemma, not a formally admitted Result.