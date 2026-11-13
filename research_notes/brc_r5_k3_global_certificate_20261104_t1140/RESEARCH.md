# R5 K3 — complete sixteen-parameter four-observer classification and rational separator

Date: 2026-11-04, Asia/Shanghai. Author-side proof synthesis and exact certificate generation; UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen science: Global Knowledge a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral policy, P000 and ACTIVE worldview read separately; neither foundation was modified.

## Exact four-source object

Sources S=(C,I,BJ,IJ), capacities c=(1/8,1/6,1/16,3/32)>0. All 16 independent parameters r_s,v_s,p_s,q_s lie in (0,1). FULL chooses x,y in [0,1], i in [0,1-x], and sourcewise z_s,t_s,u_s in [0,1]. Seedless LR requires i=(1-x)y and common z,t,u. Put w=(1/8,(1-x)/6,y/16,3i/32), d=w_BJ+w_IJ, M_s=w_s z_s, Z_s=(2/3)M_s t_s, U_s=Z_s u_s. Four observers:

    eP=107/128-21x/128+d/4-sum(Z)/2+sum(p_s Z_s)/8
    eQ=13/64+3x/64-d/2+sum(Z)/8+sum(q_s Z_s)/32
    TP=3+sum(M)+(3/2)sum(Z)+sum(r_s U_s)
    TQ=3+sum(M)/2+(3/8)sum(Z)+sum(v_s U_s)/4.

For each full real behavioral policy, the observer lies in the convex hull of 1536 FULL deterministic observations (6 upstream extreme configurations times 4^4 stages). Likewise LR uses exactly 16 possible deterministic observations (4 upstream corners times 4 stages), by the separate affine decision structure.

## Theorem A — exhaustive classification of K3

For EVERY real sixteen-tuple in (0,1)^16, the following are equivalent:

(i) conv O4(FULL)=conv O4(seedless LR);
(ii) all four r_s equal, all four v_s equal, all four p_s equal, all four q_s equal;
(iii) the actual real behavioral observation sets O4(FULL)=O4(seedless LR).

If (ii) fails then the four-hulls strictly differ.

### Proof of clock necessity (complete boundary partition)

Set mu_s=(9+2v_s)/(8(3+r_s)). Consider the exhaustive cases:

* Different mu values, min(mu)<3/8. Choose tau in (min mu,min(max mu,3/8)) not equal to any mu_s. Stage 3 has positive time score exactly at D={s:tau>mu_s}; stages 1 and 2 have negative score on n0=(0,0,tau,-1). If D is not one of {C},{C,I},{C,BJ}, the positive full score cannot be realized by the four LR source masks plus empty mask, giving a strict clock separator. For those three allowed masks, the LR n0-exposed four-face is respectively one point H. A FULL deterministic W of the same two clocks has eP(W)-eP(H) respectively 13/64,5/128,3/16, so W lies outside the LR four-hull. A small positive eP perturbation separates. This is the all-real exact result at f29e236ed7f32328f3550be31c6c09b5459b4f08.

* All mu equal. The all-real common-mu theorem at 9ec0241798f73019347071cc6b12a67d10b05fb4 proves heterogeneous (r_s,v_s) forces different signed time hulls. It includes v_s=r_s at some sources, mixed v_s-r_s signs and mu=3/8. In the common-mu equation, equal r implies equal v.

* Otherwise min(mu)>=3/8; equivalently v_s>=3r_s/2 for every s. The all-real supercritical theorem at 5895ab8bbbb528c047d7b1822bb7755311fe2295 proves heterogeneous (r_s,v_s) forces different signed time hulls, including the equality boundary.

All possibilities are covered: the second branch is not restricted by min(mu), and the third branch is the exact complement when thresholds are unequal but never below 3/8. Thus four-hull equality forces r_s=r and v_s=v.

### Proof of terminal necessity

For uniform r,v and any heterogeneous terminal p_s or q_s, the two all-real terminal-error theorems supply a strict four-observer separator. The v>r exposed-face theorem is at 5e0ff53bd6b9f573258ce2ad7553721176cf6f0c; the 0<v<=r exact mixed-support theorem is at 025f88eb123b29071922ef3749e37b9e0ea2089b. They cover all r,v in (0,1), including v=r. Hence p_s=p and q_s=q are necessary.

### Proof of actual-image sufficiency

With all parameters source-uniform, each of the four observers depends on policy only through (x,d,M,Z,U) where M=sum M_s, Z=sum Z_s, U=sum U_s. For arbitrary FULL real policy, set W=sum w_s>0, y'=d/(c_BJ+c_IJ(1-x)), i'=(1-x)y', z'=M/W, t'=3Z/(2M) if M>0 else 0, and u'=U/Z if Z>0 else 0. The inequalities 0<=d<=c_BJ+c_IJ(1-x), 0<=M<=W, 0<=Z<=2M/3, 0<=U<=Z prove all derived LR probabilities are admissible. They preserve all five aggregates, so the four observation coordinates coincide exactly. Conversely every LR policy is a FULL policy. Thus O4(FULL)=O4(LR). This direct construction is proved independently at e74cc42ba0d63f674c6ea22db9e1d228654d90c0. QED.

## Theorem B — effective rational decision and distance certificate

For every rational 16-tuple in the open parameter domain, the accompanying Python Fraction procedure halts and returns either an exact real-image equivalence reconstruction for the homogeneous case or a rational separating normal n and exact strict gap h_FULL(n)-h_LR(n)>0, together with a genuine deterministic FULL maximizing vector V. Hence

    dist_infinity(V,conv O4(LR)) >= gap/||n||_1 > 0.

The case selector is constructive:
1. In the mixed-mu, subcritical case select rational tau within the threshold interval avoiding the four mu_s. For a forbidden D use n0 directly; for an allowed D take n=(epsilon,0,tau,-1), epsilon=2^-m, m=1,2,... . Because the LR n0 maximizer is unique and the fixed FULL same-clock eP residual is positive, the support gap is positive for sufficiently large m.
2. At common mu, if all v_s>=r_s use midpoint of unequal nu_s=(3+2v_s)/(4(3+2r_s)); if all v_s<=r_s use midpoint of unequal alpha_s=v_s/(4r_s); otherwise choose tau=1/4. The common-mu mixed-stage proof guarantees strict time separation with n=(0,0,-tau,1).
3. At min mu>=3/8 with unequal clocks, use nu midpoint and n=(0,0,-tau,1) if nu varies; otherwise alpha midpoint and n=(0,0,tau,-1) if alpha varies. Alpha and nu cannot both be constant with unequal clocks in this regime.
4. With uniform clocks and heterogeneous p/q, the v<=r exact normals from the subdiagonal predecessor work with epsilon=1/100. In v>r, take its p/q exposed-face normal and decrease rational epsilon=2^-m until exact support comparison is positive. Convergence follows from strict face exposure and nonzero fiber residual.
Each candidate is checked by exhaustive Fraction support maximization over 1536 FULL and 16 LR vertices. No numerical tolerance or finite sample asserts universal mathematical coverage. The all-real scope comes from the cited full proofs, while the algorithm supplies explicit rational witnesses in every rational instance. QED.

## Executed check and scientific frontier

The companion VERIFY.py was executed locally with only Python standard library Fraction: 15 rational configurations, of which 13 nonhomogeneous cases returned exact positive four-hull support gaps and lower bounds; two homogeneous cases checked every one of their 1536 FULL deterministic observations against the explicit LR reconstruction (3072 equalities). For 13 separated cases the script computed the complete 1536 FULL and 16 LR deterministic four-vectors, totaling 19968 FULL plus 208 LR computations. Tests cover inaccessible and accessible masks, common-mu alpha/nu/cross cases, supercritical alpha/nu cases, the mu=3/8 boundary, the heterogeneous v_s=r_s diagonal, p/q heterogeneity above/below the time diagonal, and homogeneous up/down cases. One initial accessible-mask loop initialized epsilon at zero; corrected to 1/2 before final execution. Final exact stdout is in EXACT_OUTPUT.txt, ending PASS_EXACT_R5_K3_GLOBAL_CLASSIFICATION_DECISION_CERTIFICATES.

Selected exact results: inaccessible BJ mask gap 53/15360; accessible {C,BJ} fiber gap 683/368640; common-mu crossing gap 11/9600; critical mu=3/8 gap 43/22848; heterogeneous diagonal gap 215/77824. L-infinity distance bounds and other cases are recorded verbatim in the output.

This closes the fixed auxiliary K3 parameter classification author-side, NOT the larger R5 target of equal four-hulls but different actual behavioral observer images. Preserve positive source/path/provenance information in the next genuinely reconvergent, source-sensitive topology. No native X6 physical implementation or formal Source admission is claimed. Current native task owner is unconfirmed because owner inventory responds CONTROL_QUOTA; current site is static/read-only. The six inherited component theorems and this synthesis still require independent mathematical review.
