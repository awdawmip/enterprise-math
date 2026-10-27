# R5 — Exact two-law terminal zonotope repair via finite hinge coordinates

2026-10-27 Asia/Shanghai. Portable author EM-R5-LOCAL-HINGE-2146; activity RA-R5-20261027-HINGE-ZONOTOPE-2146-A7D1. Status AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED. External two-measure observer mathematics, not an admitted P000 dynamics theorem or native Task/CLAIM/Result.

Authority pins: GLOBAL_KNOWLEDGE_V1 main@ba55fc1478539fb270388d003f1b01d7de36b026 (bootstrap, operating manual, ACTIVE worldview, research/BRC/code policies). Project research inputs main@ce460bfe4854bac10d712b39b833bee2455260f5 (P000, project definition, autonomous and portable research protocols). Scientific predecessor: exact K*=1/48 terminal-three-port theorem at 9ebb8b033fb76a93c094233cb363fbe14d665092, research_notes/brc_n3_zonotope_exact_global_minimax_1over48_20261027_r1t11/PROOF.md. This is a general multiple-terminal-port extension, not a repeat of that minimax proof.

## 1. General theorem with full real quantifiers

Take any finite strictly increasing positive likelihood-ratio support 0<r_1<...<r_N, and nonnegative Q terminal arrival masses m=(m_i) and b=(b_i) satisfying the **two** equality constraints

    sum m_i = sum b_i,     sum r_i m_i = sum r_i b_i.

P-arrival mass at port i is r_i times its Q-arrival mass. Keep labeled positive BRC ports; the signed residual d_i=m_i-b_i is an observer error, not a positive probability.

For any terminal independent decision-Q probabilities 0<=x_i<=1 define the two-law terminal decision-mass vector

    z_w(x) = (sum_i w_i x_i, sum_i r_i w_i x_i),
    Z(w) = {z_w(x):x in [0,1]^N}.

For each k set H_k=sum_i d_i max(r_i-r_k,0). Both endpoint values H_1=H_N=0 by the mass and first-moment equalities. The sharp worst-case **directed** repair radius is

    E(m -> b) := sup_{z in Z(m)} inf_{z' in Z(b)} ||z-z'||_infty
              = max(0, max_{2<=k<=N-1} H_k/(1+r_k)).                 (1)

The maximum over an empty set is 0. Consequently

    Z(m) subset Z(b)  iff H_k<=0 at every internal port;
    Z(b) subset Z(m)  iff H_k>=0 at every internal port;            (2)

and the symmetric L-infinity Hausdorff distance is

    d_H(Z(m),Z(b))=max_{2<=k<=N-1}|H_k|/(1+r_k).                    (3)

All assertions cover every real terminal randomization, not merely rational or sampled policies. For rational weights/ratios all sharp values and certificates are rational.

**Proof.** The support function of the compact convex zonotope is h_w(u,v)=sum_i w_i max(u+v r_i,0). A compact convex set A lies in B+epsilon[-1,1]^2 exactly when h_A(u,v)-h_B(u,v)<=epsilon(|u|+|v|) for all real (u,v). Therefore the least epsilon equals max(0,sup_(u,v)!=0 (h_m-h_b)/(abs(u)+abs(v))). For v=0 the numerator is zero. For v>0 let t=-u/v and define C(t)=sum_i d_i max(r_i-t,0); numerator v C(t). For v<0 set t=u/(-v); numerator (-v)sum_i d_i max(t-r_i,0). But max(t-r,0)-max(r-t,0)=t-r, so both constraints imply the latter sum equals C(t). Thus the normalized ratio is precisely C(t)/(1+abs(t)), for either sign of v. At t<=r_1 and t>=r_N the call defect vanishes by the same moment constraints. Between successive positive r_k values the function C(t) is affine, say A+Bt, and (A+Bt)/(1+t) has derivative (B-A)/(1+t)^2 with constant sign. Hence its maximum is attained at an internal knot r_k (or is 0 outside support). This proves (1). Swap the masses to negate H for the reverse direction; zero directed radius characterizes containment, proving (2)-(3). QED.

**Exact reconstruction / multiple collisions.** For k=2,...,N put S_k=sum_(i=k)^N d_i. Direct finite differences give

    S_k = (H_(k-1)-H_k)/(r_k-r_(k-1));
    d_1=-S_2,  d_k=S_k-S_(k+1) (2<=k<=N-1),  d_N=S_N.            (4)

Thus the N-2 interior hinge coordinates are a lossless linear observer for *every* signed terminal mass defect with both moments zero. If multiple colliding hidden histories create separate signed defects, first add their hinge vectors H_total=sum_j H_j, then apply (1). Taking separate positive parts and summing generally overestimates repair error. This is exact signed-observer residual algebra, while original Q/P weights remain nonnegative BRC branch mass.

## 2. Four terminal ratios are the first possible incomparability

With N<=2, two moment equations force m=b. With N=3, only one H_2 exists, and (2) shows the two zonotopes must be nested in one direction. Four distinct positive likelihood ratios are necessary for crossing, and the following rational strictly positive example proves they suffice.

    r = (1/4,3/4,5/4,7/4)
    m = (9,5,11,7)/32
    b = (8,8,8,8)/32.

Under either m or b, total Q mass and ratio-weighted total P mass equal 1. Hence both define strictly positive normalized P/Q terminal distributions. Their signed difference d=(1,-3,3,-1)/32 has hinges

    (H_1,H_2,H_3,H_4)=(0,1/64,-1/64,0).

Both orientations are strictly non-repairable without error, with exact directed values

    E(m -> b)=1/112;   E(b -> m)=1/144;   d_H=1/112.

Old witness terminal Q-declaration decisions x=(0,0,1,1) give (Q,P)=(9/16,13/16). New decisions x'=(0,2/7,1,1) give (4/7,45/56), coordinate errors (-1/112,+1/112). Dual normal (-3/4,1) yields support gap 1/64 and L1 norm 7/4, proving optimality. In reverse, new x=(0,0,0,1) gives (1/4,7/16), old repair x'=(0,0,1/9,1) gives (37/144,31/72), errors (-1/144,+1/144). Dual normal (-5/4,1) has support gap 1/64 and L1 norm 9/4. Both primal and dual certificates are exact rationals.

## 3. Causal eight-leaf N=3 realization inside one tree

The four-port crossing above also has a **causally realizable** instance in a single strictly positive dual-law N=3 observation tree. At t=0 take root o. At t=1 observe A or B, each having Q=P mass 1/2 and ratio 1. At t=2 each has a deterministic single child A1 or B1 with the same ratio and mass. At t=3 each produces one of four terminal outcomes with conditional Q kernels m from A1 and b from B1 above; P_i=r_i Q_i. All eight leaf P/Q masses are positive, both measures normalize, and all earlier prefix likelihood ratios are 1.

To type external path provenance within P000 X6 without falsely claiming a native evolution law, choose a Cell anchor o: first primitive step is +e1 or +e2 for A/B; second +e3 or +e4; third one of +e5,-e5,+e6,-e6. All terminal Cell tags are distinct. Time t is independently typed. These static tags do not turn the external probabilities into native heartbeat dynamics.

Fix full-history policy pi: continue through t=1; at t=2 continue only A1 and stop B1 declaring P; at t=3 after A1 declare Q only for ports 3,4. Canonical Q-arrival-mass occupancy averaging to seedless LR at (t=2,R=1) continues with probability 1/2 from **both** A1 and B1 and, if stopping, declares P. Both earlier (T,D) laws agree exactly under P and Q: t=2 stopped/declared-P mass is 1/2 and no earlier stopping occurs.

At t=3 the Q-arrival port vectors of full pi and its early occupancy averaged seedless policy are

    M=(1/2)m=(18,10,22,14)/128,
    B=(1/4)(m+b)=(17,13,19,15)/128.

Each has terminal total P=Q=1/2. The signed defect is (1,-3,3,-1)/128 with hinges (0,1/256,-1/256,0). Theorem (1) proves the sharp **uniform terminal repair bound for this fixed early occupancy**

    E(M -> B)=1/448,   E(B -> M)=1/576.

The chosen full terminal Q-decision vector is (Q,P)=(9/32,13/32); a seedless terminal probability vector (0,16/91,1,1) gives (127/448,181/448), hence signed coordinate discrepancies (-1/448,+1/448). The normal (-3/4,1) gives support gap 1/256 and norm 7/4, matching 1/448 exactly. Since each law's terminal total mass is matched, its full (T,D) total variation error under this matched occupancy is the magnitude of that law's coordinate discrepancy, 1/448 each.

The sharp 1/448 claim is **conditional on matching the earlier stopped joint law / occupancy projection**. A globally optimized seedless strategy could trade a small earlier-time discrepancy for a different terminal mismatch. No global minimum or full-policy-vs-LR hull separation is inferred from this local result. The stronger mother question remains equal support hull but unequal seedless real-policy image.

## 4. Evidence and next question

The actually executed Fraction checker, VERIFY.py, verifies both normalized terminal kernels; zero-/first-moment hinge reconstruction; 1/112 and 1/144 primal-dual witnesses; the eight-leaf single-tree normalization, exactly matched t=2 (T,D) mass, causal 1/448/1/576 hinge radii, explicit 16/91 terminal witness; and exact two-sided zonotope vertex-distance checks for 9 positive rational four-port pairs and 27 five-port pairs. It checks 2016 deterministic vertices and the exact facet-normal certificates. EXACT_OUTPUT.txt records the local stdout. The universal all-real theorem rests on the displayed support-function proof, not the finite tests.

Provenance/status: GitHub write identity awdawmip; the native Enterprise Math gateway reported read-only authenticated subject, research_authority_granted=false and saturated new-job quota. This portable research session uses its own declared LOCAL identity, and has no Source CLAIM, current owner validation, native Result or independent Driver admission. The work is not an X6 physical law and has not been Lean formalized.

Next scientific unit: compute the full four-observer deterministic hulls for the causal eight-leaf N=3 tree, **allowing every earlier stopping action**, and issue rational membership or separating certificates. Only after both hulls agree pursue all-real seedless image nonattainability. Do not recycle the completed three-terminal 1/48 minimax computation.
