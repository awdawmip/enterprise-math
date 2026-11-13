# R5 — The exact collision-residual equality locus (two-law stopped paths)

Date: 2026-10-30 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_INTEGER_AND_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This auxiliary finite two-law model is not an established X6/Heartbeat physical theorem. Mother problem: equal FULL/seedless-LR *convex hulls* but unequal *actual real behavioral images* (still OPEN).

## Frozen inputs and inheritance

GLOBAL_KNOWLEDGE_V1 canonical main 0429f83eac0a7590d13f1d82002c34554484382f (00_BOOTSTRAP.md, OPERATING_MANUAL.md, ACTIVE worldview and mathematical/BRC/code/research-activity rules). Enterprise Math canonical main f2972ea48c82f39c42fb8e269489d609a36aee4c (AGENTS.md, P000, native X6/time, joint-observer preservation, portable research, current operations). Scientific predecessor is Draft PR #1663 commit 2951a074a6c3e96c27dafc143435542cb184f6de, research_notes/brc_r5_ten_param_interacting_q_no_go_20261030_t0943/RESEARCH.md. Existing historical proofs are author-side input, not independent review or a present Source claim.

## Exact model and BRC carrier

Two strictly positive measures P and Q have natural history masses (360P,360Q):

    t1 A(120,240), B(240,120).
    t2 A0(60,180), A1(60,60); B0(180,60), B1(60,60).
    t3 A00(30,108), A01(30,72), A10(30,45), A11(30,15);
       B00(90,36), B01(90,24), B10(20,40), B11(40,20).

Parent/child mass is conserved under BOTH laws. Stop decisions are optional at t1–t3 and mandatory at t4. A compulsory t4 leaf inherits its natural t3 source mass. The exact path likelihood ratio is L(h)=P(h)/Q(h). Two shared LR keys are A1/B1 at (t2,L=1) and A11/B11 at (t3,L=2). FULL has 14 independent optional-history stop probabilities; **seedless LR** has 12 distinct (time,L) keys, with no persistent correlated seed. A natural path visits any one key at most once.

At a stop at natural history h at time t, define exact legal terminal error probabilities

    p(t,h)=1/5+t/20+(t+1)/(100L(h))
    q(t,h)=2/5−t/30+(t+2)L(h)/200+η c_h.

Here η>0 and only c_A11=a, c_B11=b may be nonzero. All coefficients are real but restricted to the strict probability range 0<p,q<1 for every possible stop, including t4. The explicit η=1/1000, (a,b)=(1,1) and (1,0) examples satisfy this. The BRC information carrier is the exact labelled positive-rational P/Q path-mass family; we do not suppress source labels prior to the declared final observer and do not infer native X6 dynamics.

Let (eP,eQ,TP,TQ) be the original four-observer and set

    R = Σ_optional stopped Q(h)c_h,
    DP = 4−TP = Σ_optional stopped (4−t(h))P(h),
    DQ = 4−TQ = Σ_optional stopped (4−t(h))Q(h).

Because Q(h)L(h)=P(h), for **every real behavioral policy**

    eP = 21/100 + TP/20 + TQ/100,
    eQ = 41/100 + TP/200 − TQ/30 + ηR.

For fixed η>0, the four-observer hull equals an injective affine image of the (R,DP,DQ) hull.

## Theorem — iff equality classification

**For every admissible real (a,b,η), η>0, conv(O_FULL)=conv(O_LR) if and only if a=b.** When a=b≠0, this common four-observer hull has affine dimension exactly THREE; when a=b=0 it has dimension TWO. The theorem concerns convex hulls, not the actual real behavioral images.

### If a≠b: explicit all-real separating support direction

Choose s in {−1,+1} such that H=max(sa,sb)>0; let K=min(sa,sb)<H. Choose d=(H+max(K,0))/2. Thus H/2≤d<H, and d>max(K,0). For the signed linear objective

    Ψ=s(eQ−41/100−TP/200+TQ/30)−ηd(4−TQ),

the normalized reward for stopping at optional h is

    r(h)=sQ(h)c_h−d(4−t(h))Q(h).

All nodes other than A11 and B11 have strictly negative reward. Of the two t3 colliding nodes, the high source yields h=Q_high(H−d)>0, and the low source yields ℓ=Q_low(K−d)<0; the two Q masses are 1/24 and 1/18. FULL continues all other nodes and stops only at the high collision, hence max_FULL Ψ/η=h.

LR must either stop at BOTH t3 collision nodes or at neither. Its sole alternative to eliminate only the low t3 collision while preserving the high one is to stop the low root at t1; this costs 3dQ_low-root≥d. Yet h≤Q_high d≤d/18<d, so source isolation cannot improve the maximum. The t2 common stop would eliminate BOTH t3 rewards and itself costs a strictly negative reward; all other early stops also cost negative rewards. Thus

    max_LR Ψ/η = max(0,h+ℓ),
    max_FULL Ψ−max_LR Ψ = η·min(h,−ℓ) > 0.

This is a **universal signed support obstruction for all unequal real a,b**, not a parameter-grid inference. Each policy objective is multi-affine in its real local stop probabilities, since no natural path repeats any decision key. Its maximum over the full real probability hypercube is consequently at a deterministic mask. The proof covers both policy classes and their convex hulls.

### If a=b: exact complete 3-dimensional polyhedral certificate

First put a=b=1. Scale (R,DP,DQ) by 360, yielding integer (r,x,y). FULL has 16,384 deterministic masks giving 647 distinct observer triples; LR has 4,096 masks giving 272 distinct triples.

FACET_CERT.json lists 24 exact supporting integral halfspaces A·r+B·x+C·y≤D. The dependency-free VERIFY.py checks EACH inequality on EVERY FULL and LR deterministic triple, and checks that each is supported by ≥3 LR triples. Append the universally true box 0≤x,y≤1080, making the resulting 28-halfspace polyhedron H bounded. The verifier enumerates all C(28,3)=3,276 boundary-plane triples, with exact rational 3×3 Cramer's rule. Exactly 3,075 triples have nonzero determinant. Their feasible intersections consist of exactly 31 different vertices, all themselves ACTUAL LR deterministic observations. A compact full-dimensional polyhedron is the convex hull of its vertices, so H=conv(the 31 LR vertices)=conv(O_LR), and since all FULL deterministic observations satisfy H, conv(O_FULL)⊆H. Conversely every LR deterministic policy is a FULL policy. Hence exact hull equality holds in ALL signed directions, without numerical LP, direction sweeps or floating-point geometry. The exact determinant test in VERIFY.py proves affine rank 3.

When a=b=c≠0, simply apply the invertible change (R,DP,DQ)↦(cR,DP,DQ) to the c=1 result, preserving hull equality and rank. When c=0, project out R, retaining the rank-2 (DP,DQ) convex equality. Real behavioral images lie inside the convex hull of deterministic images by multi-affine cube interpolation, and the deterministic images are real policies themselves. Thus equality holds for the convex hulls of **all real policies**, not merely finite rational samples.

This exact facet/vertex-completeness proof is an alternative complete certificate to listing 647 separate primal Carathéodory mixtures; it establishes the same all-signed containment.

## Explicit rational negative witness for the unequal line

For η=1/1000, a=1, b=0, choose s=1,d=1/2. Then high h=1/48, low ℓ=−1/36, so max_LR Ψ=0, max_FULL Ψ=η/48=1/48000. The FULL policy stopping **only A11** has four-observer

    O*=(1069/2400,21433/72000,47/12,95/24).

Every real seedless LR policy and convex mixture satisfies

    48000 eQ − 240 TP + 1624 TQ ≤ 19776,

but O* yields 19777, a strict exact integer violation of 1. This excludes every unequal pair, and supplies one particularly small numerical instance.

## Actual validation and non-claims

Executed local standard-library exact int/Fraction checker returned PASS_EXACT_R5_COLLISION_RESIDUAL_EQUALITY_LOCUS. It checks both collision ratios, positive normalized natural masses and legal terminal rates (including t4), 20,480 deterministic masks for both the equal and unequal examples, 24 facet inequalities, 3,276 exact plane triples / 3,075 nonsingular triples / 31 exact feasible LR vertices, a nonzero rank-3 determinant, and the explicit rational separation. These finite computations prove the finite polytope identity under a complete mask enumeration; the universal a≠b conclusion is analytic and the all-real policy extension uses multi-affinity. No formal theorem prover run, independent Driver review, valid native Source CLAIM/Result or physical X6 correspondence is asserted. BRC reuse: REUSE_APPLIED for labelled two-measure path mass and change-of-measure observer, preserving provenance.

## Smallest continuation

The equal-collision scalar line produces a genuine rank-3 ALL-SIGNED equal-hull model; actual real FULL-vs-LR image equality remains unresolved. First decide real-image equality/nonmembership there using a rigorous semialgebraic or constructive policy argument. Independently add one P-error perturbation with a fourth genuinely independent observation direction and retest ALL-signed rank-4 convex equality with exact rational certificates; any strict Farkas/support gap kills that candidate. Continue on existing R5 Draft PR #1663, without re-testing the excluded fixed-opposite-collision ten-parameter family or altering P000/ACTIVE worldview.