# R5: source-sensitive middle STOP errors destroy four-observer hull equality on a time-lumpable tree

2026-10-31 Asia/Shanghai. Author-side \`EM-R5-2BDD96\` (retained local conversation identity only; not a Source-issued researcher identity/CLAIM). Status: AUTHOR_PROVED / EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

## Authority and exact prior frontier

Pinned GLOBAL_KNOWLEDGE_V1 canonical main ffc97b2fc5890fa54226ae4b464d5db401a87470; Enterprise Math canonical main 673a838d7baa33e7427e98aa5b06381a2ada81d4. Read their bootstrap/manual, P000, ACTIVE Heartbeat X6 worldview and joint-observer contract, current portable research/operations/control routes. Scientific predecessor: d3ea995feff73faa65f2a537da9f5feaf2692ff1 (diagonal natural kernel yields equality of **actual** two-dimensional time images). Newer PR #1663 head 31d7a6b703054bb335242312d6bf17f30fbf49e5 independently gave an off-diagonal, upstream-adjusted time-hull-equal, full-rank **time-only early error** no-go. The present proof is distinct: it treats a diagonal, time-Markovizable process with **source-dependent middle STOP errors**, proves an all-real family result, and explicitly obtains four-dimensional affine rank.

## Finite dual-measure genuine stopping model

Nature has twelve strictly positive labeled paths (x,u,v), x,u in {0,1}, v in {0,1,2}. In order (00,01,10,11), Q(x,u)=(3/8,1/8,1/8,3/8). At time 3, likelihood ratios r_0=3/4, r_1=5/4; at time 4, R_v=(1/2,1,3/2). For each real t in (0,1/4), take source-independent kernels

K_(x,0)=(1/2+t,1/2-2t,t),  K_(x,1)=(t,1/2-2t,1/2+t).

Let q_xuv=Q(x,u)K_(x,u)(v), p_xuv=R_v q_xuv. All positive; both measures sum to one; sum_v K_(x,u)(v)R_v=r_u. At time 2 one may STOP or CONTINUE based on x (distinct LR ratios 7/8 and 9/8); at time 3 the LR value r_u merges both x histories; at time 4 LR sees only R_v. STOP always immediately absorbs at times 2, 3, or 4; continuation at 4 is absorbed at 5. FULL sees complete available history; LR sees only (time, P/Q) with independent behavioral randomization and **no persistent seed**.

Observers: (e_P,e_Q,T_P,T_Q), expected terminal binary error probabilities and stopping times under each measure. Use a common conditional error probability eta_xu in (0,1) if STOP at time 3, and 1/2 if absorption at time 2, 4, or 5. The **same** event error probability at a path is used under P and Q.

## All-real source-sensitive u=0 no-go theorem

For every t in (0,1/4), any interior eta with eta_00 != eta_10, and every sufficiently small positive epsilon, define

ell(t)=(5-2t)/(6-4t), d_x=1/2-eta_(x,0), dbar=(3d_0+d_1)/4,
lambda=ell(t)+[3 epsilon dbar]/[4(3/2-t)],
H=T_P-lambda T_Q+epsilon e_P.

Then the support functions of **all real** FULL and LR behavioral strategies satisfy the *exact* positive gap

  sup_FULL H - sup_LR H = 9 epsilon |eta_00 - eta_10| / 128 > 0.

Thus their four-observer convex hulls (and actual images) differ even though their actual two-time-observer images coincide. Arbitrary interior eta_(0,1),eta_(1,1) do not affect the displayed gap for sufficiently small epsilon. This rejects this whole class as a candidate for *four-hull-equal yet real-image-different*; it is not a negative solution for all stop trees.

### Complete analytic proof

1. Each history is visited at most once, and the expected linear payoff is multiaffine in each behavioral policy probability. A maximum over each finite policy cube is attained at deterministic vertices. Thus finite Boolean support optimization gives **all-real** support bounds.
2. At epsilon=0 and lambda=ell(t) in (5/6,9/10), optimal time-4 continuation signs are strict, L_v=[R_v-lambda]_+=(0,1-lambda,3/2-lambda). The time-3 CONTINUE-minus-STOP gain for source x at u=0, per unit Q(x,0), is exactly
   G_x0=(3/2-t)(ell(t)-lambda)+epsilon*(3/4)*(1/2-eta_x0)
       =(3 epsilon/4)(d_x-dbar).
   Hence G_00=3 epsilon(d_0-d_1)/16 and G_10=-9 epsilon(d_0-d_1)/16, with 3G_00/8+G_10/8=0; the two signs are opposite whenever eta_00!=eta_10.
3. At epsilon=0, time-3 continuation for u=1 is strictly optimal: G_x1=5/2-2lambda+t(lambda-1/2)>7/10. Each time-2 source continuation margin is strictly positive: x=0 margin >3/40 and x=1 margin >3/8 (using lambda<9/10, Q weights and G_x1>7/10). The time-4 signs are strict as well. Since there are finitely many actions and the payoffs are continuous in epsilon and lambda, for each t,eta there exists a positive epsilon neighborhood preserving time-2 CONTINUE, u=1 CONTINUE, and time-4 choices. Only the two hidden-history u=0 decisions can differ.
4. FULL independently chooses the better u=0 action on x=0 and x=1; LR must use one shared action. Their exact support discrepancy is
   (3/8)[G_00]_++(1/8)[G_10]_+ - [(3/8)G_00+(1/8)G_10]_+
    = 9 epsilon |d_0-d_1|/128
    = 9 epsilon |eta_00-eta_10|/128.
   This covers all real behavioral strategies, not merely rational grid checks. The equal K kernels imply lumpability of the 2D time observer, so its real images remain equal by the predecessor's seedless occupancy argument. End proof.

## Fully rational full-affine-rank witness and verified evidence

Set t=1/8, eta_00=1/4, eta_10=3/4, eta_01=1/3, eta_11=2/3, epsilon=1/100. All branches and error probabilities are strictly interior. Then

lambda=3803/4400;
sup_FULL H=231019/281600; sup_LR H=5773/7040;
gap=9/25600>0.

An exact maximizing FULL Boolean policy is bitmask 200111 under the attached verifier's encoding, with (eP,eQ,TP,TQ)=(67/128,17/32,597/128,285/64). It is at infinity-norm distance **at least 33/175936** from every real LR four-vector, by the dual norm bound gap/(1+lambda+epsilon).

The 128 LR Boolean observations possess *full affine rank 4*. Relative to LR bitmask 0, the difference rows for bitmasks 1,2,5,6 form

   [-37/384, -11/96, 7/16, 1/2]
   [ 13/128,   3/32, 9/16, 1/2]
   [ -5/192,  -1/48,23/32, 7/8]
   [   5/64,   1/16,21/32, 5/8]

with exact determinant **3/32768**, so the exclusion persists on an open parameter neighborhood by continuity.

The included standard-library Python Fraction/int checker independently enumerates **262144** FULL and **128** LR Boolean strategies (18 and 7 control bits), checks both measure normalizations, all 12 strict positive path masses, the conditional likelihood identities, the full and LR support extrema, a full deterministic witness, the 4D rank determinant and norm bound. The all-real quantifier rests on the analytic proof above. EXACT_OUTPUT.txt contains the literal executed stdout.

## BRC and observer-preservation interpretation

BRC uses twelve positive P/Q-weighted paths with their source labels retained; LR compression erases x at stage 3. Even though future natural transition K is **identical** across x, the terminal STOP error kernel remains source-sensitive, so the quotient is not safe for the enriched future observer. A minimal repair is to retain the source-resolved eta_x0 (or an equivalent sufficient state). This is a finite stochastic observer counterexample, not a phase-cancellation theorem or a physical assertion about the locked native X6 / Heartbeat worldview.

Prior art scope: Puterman, *Markov Decision Processes*, finite-horizon Markov optimality/occupation measures (1994), DOI 10.1002/9780470316887.ch4 is background to the earlier seedless 2D time-Markovization, not a novelty claim for this source-specific proof. No independent review, literature priority, formal proof assistant or external experiment is claimed.

## Actual authority and next scientific unit

In this run native em_status returned research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED. A bounded read of active owners via em_control_tasks was rejected with CONTROL_QUOTA; current Source owner could not be verified. This note's project GitHub storage does not grant a Source session, CLAIM, Result or mathematical admission.

Continue on the *newer off-diagonal, upstream-adjusted but 2D-time-hull-equal* 12-path process cited above, changing genuinely source-sensitive u=1 or time-4 error rewards while preserving 4D rank. First prove four-observer hull equality by rational lifts of FULL vertices into <=5 LR vertices, or exhibit an exact Farkas separator. Only upon hull equality test real-image nonmembership. Do not repeat the diagonal u=0 middle-STOP source-sensitive region now analytically excluded.