# R5 — Six-port source-conditioned ingress fiber: exact rank-five obstruction

Date: 2026-11-01 (Asia/Shanghai). Author status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is a finite auxiliary two-measure stopping model; it does not imply a native X6 or Heartbeat World theorem.

## Source and role

Frozen GLOBAL_KNOWLEDGE_V1 canonical GitHub main: 1a1e0968079c9ab3e91279990e164d38f31838a5. Read 00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE 我眼中的世界.md, mathematical/code/BRC policies, and research activity guidance.
Frozen Enterprise Math canonical main: f8cc8141ca4c92b793ec694de7bfff9ad5e3bba6. Read AGENTS.md, p000_reality_foundation.json, joint relation observer preservation, native X6 time, active autonomous research protocol and PORTABLE_RESEARCH_PROTOCOL.md.
Exact predecessor: research_notes/brc_r5_ingress_qr_full_linear_span_20261101_t0340 at immutable author commit 51458753d000d0d67e3ebb030de1547a5ef6530f, Draft PR #1663.
Native gateway at observation: research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED, quota 5/5; bounded owner request returned CONTROL_QUOTA. Neither the active owner nor a native session/CLAIM/Result/independent Driver admission was established. P000 and protected worldview were not edited.

BRC reuse: REUSE_APPLIED to exact positive rational P/Q source-and-route-labelled carrier, retaining source identity, all six ingress ports, branch alternatives, likelihood ratios, terminal times, and conditional observer fibers. Future information-preservation beyond the finite scope is not claimed.

## Fixed carrier

There are two origins i=0,1 with P=Q initial mass 1/2 each, alpha=(1/4,1/5), kappa=(3/4,1/6). Both satisfy (1+kappa_i(1-2alpha_i))/alpha_i=11/2. A stop is at time 1; continuing A branches to D,Y,C with Q probabilities alpha_i,alpha_i,1-2alpha_i. D may stop at time 2, or continue to DH with conditional mass 2/3 and to L from D with 1/3. Y may stop at time 2, or continue to YH with 1/2 and to L from Y with 1/2. C stops at time 2 with conditional mass 1-kappa_i or enters L with kappa_i. At L one may stop at time 3 or continue to time 4. FULL has 12 source-specific binary decisions (A,D,Y,LD,LY,LC for each source), yielding 4096 corners; seedless LR has four common keys (A,D,Y,L), yielding 16 corners.

The labelled Q terminal carrier has 24 coordinates Q(i,ell), for ell in (A,D,Y,C,DH,YH,LD,LY,LC,L4D,L4Y,L4C). The respective P/Q ratios are (1,1/2,3/2,1,1/4,2,1,1,1,1,1,1) and times (1,2,2,2,3,3,3,3,3,4,4,4). Thus the two measures are reconstructed without discarding source or ingress provenance.

Let x=Q(DH), u=Q(YH), and t=T_Q. Their simultaneous maxima are x*=3/20 and u*=9/80. Positivity forces all A,D,Y upstream decisions to continue on this maximal face; FULL then has 2^6=64 L-continue choices. The six positive ingress Q masses in order (0,D),(0,Y),(0,C),(1,D),(1,Y),(1,C) are

w=(1/24,1/16,3/16,1/30,1/20,1/20); W=sum w=17/40.

Only LR deterministic corners 14 and 15 reach both maxima. Their time coordinates are t0=43/16 and t1=249/80; t1-t0=W. Every other LR corner has D=(x*-x)+(u*-u)>=9/80.

## Theorem 1 — full maximal-face fiber criterion (all real coefficients)

Take any finite expectation terminal observer z=sum_{i,ell} c_{i,ell} Q(i,ell), with arbitrary real coefficients c. For the six ingress ports j=(i,r), r=D,Y,C, put delta_j=c_{i,L4r}-c_{i,Lr}.

Every FULL deterministic point on the maximal (x,u) face agrees in (t,z) with its unique time-matched LR-edge mixture **if and only if** all six delta_j coincide.

Proof: All non-L leaf contributions to z are constant across this face. Write s_j in {0,1} for the FULL continue choice at ingress j and denote by z0 the all-stop LR value. Then
 t=t0+sum_j w_j s_j,
 z=z0+sum_j w_j s_j delta_j.
The LR corner pair 14/15 is the entire exposed face, so a FULL point with the same x,u,t can only be represented by the LR mixture with lambda=(t-t0)/W. Its z coordinate must be
 g(t)=z0+lambda sum_j w_j delta_j.
Writing bar_delta=(sum_j w_j delta_j)/W gives the exact discrepancy
 z-g(t)=sum_j w_j s_j(delta_j-bar_delta).
If this vanishes for all six single-port choices, positivity of every w_j gives delta_j=bar_delta for all j. The converse follows directly. All quantifiers are over actual real coefficients; no sampling inference is used. QED.

## Theorem 2 — source-flow residual rank five

Each single-port FULL corner has a residual vector in the retained 24-dimensional Q carrier relative to its forced LR-edge time mixture. The six single-port residuals sum to zero; all 64 maximal-face residuals are sums of these six. Thus rank<=5. Their first five rows restricted to the first five source-and-route L4 coordinates have the determinant

 det_5 = (w_1*w_2*w_3*w_4*w_5)*w_6/W = 1/10444800 != 0.

The exact residual rank is therefore **5**. In the space of all 24 terminal observer coefficients, equality of the six L stop/continue contrasts describes a codimension-5 subspace. This is an observer-fiber certificate for this exposed face only; it is not a proof of safe source quotient for arbitrary future operations.

## Theorem 3 — all-real Farkas separation for unequal contrasts

Assume the six delta_j are not equal. Choose j with rho_j=w_j(delta_j-bar_delta) != 0; the FULL policy with only port j continuing has residual rho_j from the LR forced edge. Define sigma=sign(rho_j), g(t)=z0+(t-t0)(z1-z0)/W, and D=(x*-x)+(u*-u). For each nonedge LR corner k, D_k>0. Set
 M=1+max_{k=0,...,15, k not in {14,15}} |z(LR_k)-g(t(LR_k))| / D_k.
This is an explicit finite real number (rational when c is rational). The affine support functional
 H(x,u,t,z)=sigma*(z-g(t))-M*D
vanishes on LR endpoints 14/15 and is strictly negative at all other LR corners. By the multilinear deterministic-corner reduction it is <=0 on all real seedless-LR behavioral observations. The selected FULL deterministic observation has score |rho_j|>0. Thus for **every** real source-conditioned 24-leaf observer whose six ingress contrasts are not all identical, conv V(FULL) != conv V(LR). This theorem does not claim rank four for arbitrary coefficients.

## Explicit four-rank source-conditioned witness

Take z=Q(origin 0,L4D), the bounded Q event statistic detecting origin 0 reaching time 4 via D. Its six contrasts are (1,0,0,0,0,0). FULL deterministic index 3896 (lexicographic 12-bit order) continues all upstream actions, and continues at L only from origin-0 D. It yields
 V_FULL=(x,u,t,z)=(3/20,9/80,131/48,1/24).
For all LR deterministic corners,
 H=z-(5/51)*(t-43/16)+3*(x+u-21/80) <= 0.
Indeed LR endpoints 14 and 15 give equality. For any other LR corner D>=9/80, 0<=z<=1/24, 1<=t<=4, and |(t-43/16)/(17/40)|<4. Consequently |z-(5/51)*(t-43/16)|<5/24<27/80<=3D, proving H<0 without relying on enumeration. The FULL witness gives
 H(V_FULL)=1/24-(5/51)*(1/24)=23/612>0.

The LR four-observer affine rank is exactly **4**: the difference determinant of vertices (0,8,10,12,13) equals -891/1024000 != 0. The L1 norm of the support normal (3,3,-5/51,1) is 362/51. Hence the FULL witness has L-infinity distance >=(23/612)/(362/51)=23/4344 from the LR convex hull and every real seedless-LR behavioral observer set.

This is an exact obstruction, **not** the original mother target (which also requires equality of the complete four-observer convex hulls and inequality of the actual real policy images).

## Verification and scope

The attached standalone Python standard-library Fraction checker evaluated all 4096 FULL and 16 LR deterministic strategies with exact P/Q normalization, all 64 maximal-face residuals, six-port weights, two LR endpoints and all other deficits, a directly computed exact 5x5 determinant, a signed six-contrast regression, the source-conditioned support witness and LR four-rank minor. Its actually executed stdout is in EXACT_OUTPUT.txt. Exact finite checks supplement the analytic all-real proofs. No formal Lean checker, native X6 embedding, independent review or Source mathematical admission is claimed.

Next: Restrict to the ingress-neutral codimension-five coefficient space delta_1=...=delta_6. Use other exact faces of conv(x,u,T_Q) and their 24-leaf residuals to decide whether any remaining z has LR rank four and complete FULL/LR hull equality. Require explicit rational <=5 LR-vertex convex certificates for any successful candidate or an exact signed Farkas separator for any failure. Preserve the source-conditioned early leaf data while testing further fiber constraints.
