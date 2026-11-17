# R5 — Compensated answer/time fibers: exact exposed-face theorem and mixed-facet obstruction

Date: 2026-11-02 Asia/Shanghai. Evidence: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Auxiliary finite two-law stopping graph, not a native X6 realization.

Frozen scientific sources: Global Knowledge main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Direct predecessor: enterprise-math@c06f1123e2ae91d1c07490eb812fea979ed98ba3, research_notes/brc_r5_eight_delay_complete_classification_20261102_t1242/RESEARCH.md. Current behavioral norms read separately at canonical main. P000 and ACTIVE worldview unchanged.

## Exact BRC source-labelled model

Under EACH of P and Q, initial masses 1/2, 1/4 and 1/4 reach decision I (time 1), J via B (time 2) and K via C (time 3). Stopping at I,J,K answers P immediately. Continuing I branches equally to J via I or K via I. Continuing J branches equally to a terminal at time 3 (P(answer P)=3/5, Q(answer P)=2/5) and K via BJ or IJ. At K, continuing from source s in S={C,I,BJ,IJ} answers P with probability a_s under BOTH laws, and ends at time 5 with conditional probability p_s under P and q_s under Q (otherwise time 4). Take the answer and delay events conditionally independent for a concrete all-positive joint terminal kernel. All parameters lie strictly in (0,1) in our examples. No signed probability masses, false cancellation, or loss of source labels. Both measures reach every nonterminal decision key with the same flow, so (time,likelihood ratio) equals (1,1),(2,1),(3,1), respectively.

FULL stop probabilities are (x,jB,jI,kC,kI,kBJ,kIJ) in [0,1]^7. LR uses (x,y,z) with jB=jI=y and k_s=z. Observable O=(eP,eQ,TP,TQ) where eP=P(answer P), eQ=Q(answer Q), and T are expected terminal times. Since each decision point is visited at most once, the map is multi-affine: the 128 deterministic FULL and eight deterministic LR vectors generate the respective convex hulls exactly.

## Theorem A — complete upper exposed-face compensation criterion

For any real 0<a_s,p_s,q_s<1, the FULL/LR answer-sum maximum is eP+eQ=21/20 and its exposed policies have x=jB=jI=0. Its LR observation face is the segment joining U0=O_LR(0,0,0) and U1=O_LR(0,0,1). The complete FULL upper exposed face coincides with this LR segment **if and only if** BOTH sourcewise ratios are constant:

(1+p_s)/(1-a_s) = rho_P for every s; (1+q_s)/(1-a_s) = rho_Q for every s.

Proof: only the J direct terminal contributes excess answer-sum above 1, of 1/5 times its mass. Consequently eP+eQ=1+[(1-jB)+(1-x)(1-jI)]/40, maximized exactly at the stated J/I actions. At the upper face the four K source masses under each law are m=(1/4,1/4,1/8,1/8). Changing single-source s from K continuation to K stop adds D_s=m_s(1-a_s,-(1-a_s),-(1+p_s),-(1+q_s)) to U0. The LR upper segment direction is D=sum_s D_s, with strictly positive first coordinate G=sum_s m_s(1-a_s). If FULL face is contained in LR face, U0+D_s=U0+alpha_s D, and its first coordinate forces alpha_s=m_s(1-a_s)/G. Comparing third and fourth coordinates gives the two ratios. Conversely the ratios imply D_s=[m_s(1-a_s)/G]D for every s, so any real FULL K policy k maps to LR z=sum_s k_s m_s(1-a_s)/G in [0,1], reproducing its entire four-observer vector. This also proves equality of the actual exposed images, not merely their convex hulls. QED.

These conditions are necessary for the FULL/LR GLOBAL convex hulls to coincide, but they do not imply global equality.

## Theorem B — explicit strictly-positive compensated candidate, still strictly separated elsewhere

Order sources (C,I,BJ,IJ) and set:
 a = (1/2, 9/16, 3/5, 7/12),
 p = (1/2, 5/16, 1/5, 1/4),
 q = (3/4, 17/32, 2/5, 11/24).

All source answer/time probabilities are strictly between 0 and 1, and (1+p_s)/(1-a_s)=3, (1+q_s)/(1-a_s)=7/2 for every s. By theorem A, all FULL/LR observations on the formerly obstructing upper face coincide, despite genuinely heterogeneous source kernels.

Nevertheless in signed direction N=(-823,-823,-823,822), exact corner maximization gives:
 h_LR(N)=-5839/8,
 h_FULL(N)=-14589/20,
 h_FULL(N)-h_LR(N)=17/40.

FULL action (x,jB,jI,kC,kI,kBJ,kIJ)=(0,1,0,0,0,0,0) attains the FULL maximum, with W=(637/960,347/960,231/64,1441/384). The exact signed gap separates W from EVERY real LR behavior, including randomized strategies, because their four-vector convex hull equals the hull of the eight LR corners. Since ||N||_1=3291, dist_infinity(W,conv O(LR)) >= 17/131640. The compensating source-fiber equations eliminate one exact exposed-face obstruction but a mixed time/answer support facet still distinguishes FULL.

## Theorem C — complete all-real one-source answer-kernel perturbation

Fix p_s=1/2 and q_s=1/3 for all sources; a_C=1/2+delta and other a_s=1/2. For every real delta in [-1/4,1/4], the convex hulls coincide **if and only if** delta=0. For delta != 0 set sigma=-sign(delta) and N_delta=(400+sigma*9/(3-2delta),400,sigma,0). Then the exact all-real signed support difference is

 h_FULL(N_delta)-h_LR(N_delta) = (3/2)|delta|/(3-2delta) > 0.

Proof: the LR upper edge has answer-P increment G=(3-2delta)/8 and P-time decrement 9/8, so N_delta ties its endpoints. Any other deterministic FULL or LR upstream policy has eP+eQ<=41/40 and loses at least 400/40=10 in the answer-sum score. The residual r eP+sigma TP has variation <=|r|+4<=3.6+4<10 for 0<=eP<=1 and 1<=TP<=5, so all support maxima belong to the upper face. The single source C stop has strictly positive score increment, while each other source K stop has strictly negative score increment, yielding the displayed exact support gap. At delta=0, all source K kernels agree and real FULL behavior can be exactly aggregated to LR at J and K by simultaneous P/Q mass-weighted stop fractions; actual observation images coincide. QED.

## Validation scope / evidence

VERIFY.py is actually executed Python standard-library Fraction code. It checks the 16 FULL upper-face deterministic vertices, all 128 FULL/eight LR corners for the compensated candidate, the exact integer signed separator and witness, plus six rational delta samples including zero, both signs and endpoints. Captured result ends with PASS_EXACT_R5_COMPENSATED_UPPER_FIBER_AND_MIXED_FACET, 341 exact assertions. The full-real theorems are algebraic as proved above; testing finitely many delta values alone does NOT extend them to all real delta.

No formal native owner, CLAIM, Result, independent Driver review or Foundation admission is asserted. Previous canonical owner lookup returned CONTROL_QUOTA; authenticated native service reports research_authority_granted=false. GitHub persistence is author-side, not native task authorization.

Next: allow the K answer kernel to differ between P and Q so the formerly protected answer-sum upper face changes; preserve strict positive labelled paths and exact LR collisions. For small rational candidates test all 128 FULL vectors for rational LR convex decompositions of at most five corners, or produce exact Farkas separators. Only after all-signed hull equality attempt full-rank FULL real-image/nonmembership certificates. Mother objective remains open.
