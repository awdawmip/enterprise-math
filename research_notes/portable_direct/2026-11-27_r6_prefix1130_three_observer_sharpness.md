# PREFIX-1130 — Coupled rho,c,d jet feasibility at the minimal line

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / COMPACT_ANCHOR_THREE_JET_RELAXATION / NOT_REVIEWED.

Continue PREFIX-1129 at e993cc8e5084aacea730192791e5919c26cdc55c:research_notes/portable_direct/2026-11-27_r6_prefix1129_robust_inner_anchor_feasibility.md. The inherited Researcher/Activity is EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 / TASK_RESEARCH; original registration r6-20261123-2358-session-start-own-v1 read back SUCCEEDED. Fresh owner observation r6-20261127-1654-leased-observe SUCCEEDED with error=null, LEASED tasks=[], next_cursor=null, fixed as_of 2026-11-27T08:55:09.926898Z, control Source a6e5f8aa371f9b02a97f5e6ac19a97700383032e. No CLAIM or shared Task mutation. Current account entry snapshot 6c8be6f6aac62ff2597803a242ef333fc39f9abb; frozen P000 V5 and companion source f42f2906d77f24085c123f3ccfe9667d41caa96d. Retain signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. All coordinates of the observer below are auxiliary algebraic readouts of the inherited signed X6 carrier, not native spatial axes or time. No new native arithmetic or moment anchor; inherited Stage46 correspondence, analytic boundary, root isolation and earlier 8400/8800 command-exit uncertainty remain conditions.

## 1. Three linear observations on one coefficient vector

Let Acal=a0+W[-1,1]^6+diag(dr)[-1,1]^6 be the frozen 9600 compact anchor. Write F_a(t)=sum a_i P_i(t), b=t^2/36, v=b(1-b), ell=1-2b and A=1-b(c+2). Reuse the density jet of the frozen root_8800.py in the PREFIX-1122 execution package. For fixed t put R=t^2 and introduce an auxiliary variable x; D_j is j! times the coefficient of x^j in

  (R+36x)^3 / ((4-R-36x)^3 (16-R-36x)^3) * F_a(sqrt(R+36x)).

Only j=1,2,3,4 is required; on F_a(t)=0 the j=0 contribution of F to each D_j can be omitted. Thus these are linear observations of a, computable by exact formal truncated coefficient composition from the signed Frobenius jet. D_1<0 is checked throughout Acal and the t interval. The inherited r_j=D_j/D_1, A=-v*r_2/2 and c=(1-A)/b-2 give

  d=-(c+2)A+r_2/2*(A*ell-(c+3)*v+A^2)+r_3/6*v*(2*ell+3*A)+r_4/8*v^2.

For fixed t,c,d define
  B=-(c+2)A-A/v*(A*ell-(c+3)*v+A^2),
  C3=v*(2*ell+3*A)/6, C4=v^2/8.

Then imposing the three linear observations
  H_1=F_a(t),
  H_2=v D_2+2 A D_1,
  H_3=(B-d)D_1+C3 D_3+C4 D_4
simultaneously equal to zero is equivalent (where 0<b<1 and D_1!=0) to the root and the inherited c,d jet relations. Indeed H_2 sets r_2=-2A/v, and substitution in the inherited d expression gives exactly H_3/D_1=0. This eliminates the apparent nonlinear dependence on coefficients without discarding the shared coefficient directions. The formula is a root-fiber identity, not a generic off-root equality.

## 2. Robust interior certificate in three observation coordinates

For each parameter point write H(Acal)=m+sum [-1,1] v_j (12 shared columns). Enclose all centers and columns on a parameter rectangle, choose rational midpoints m0,w_j and let e_i bound |m_i-m0_i|+sum |v_ji-w_ji| uniformly. Assume the w_j span R^3. For each nonzero cross product n=w_i cross w_j, check

  sum |n dot w_k|-|n dot m0|-sum |n_i| e_i >0.

It suffices to check these directions because every facet of a full dimensional zonotope is exposed by a direction orthogonal to a spanning pair of its generating segments: the face dimension equals the rank of the perpendicular generators. The two signs are checked by |n dot m0|. The nominal zonotope therefore contains the error box [-e,e] strictly in its interior. For every real direction n the actual support is at least the nominal support minus sum |n_i|e_i, hence nonnegative; separation gives 0 in the actual zonotope. This holds for each exact parameter pair and each enclosed realization, with one common a for all three equations. Strict margins also imply interior membership. Cross products here are an external algebraic operation on observer rows, not a new native cross product.

## 3. Actual computation and scope

Select the minimal q among the 115 frozen lines from PREFIX-1128 (not a new enumeration claim). q=704830121671781357562188570181003663463817577529892083528277, p=15111583690290265361910097499591303255690478646004698769663152, h=69877570449453801340258215642018962660689140809934967422785021. For L0=10^114 and inherited d interval [dl,du], evaluate the complete rectangle rho in [p/q,p/q+du/L0^2], c in [h/q-2du/L0,h/q]. Use rho=36/t^2-1 and outward integer sqrt grid 10^180, verify t enclosure inside parent. The shared Frobenius evaluator uses exact outward integer Horner, derivative 0..4 with existing product-rule tail bounds, and the compact anchor's 12 shared directions. A nominal interior point of the first two observations is found by the radial boundary construction: for target -m0 use the least positive ratio of facet support to absolute target projection, then choose endpoint signs on nonperpendicular generators and distribute the remaining parallel-edge coordinate. Scaling back from the boundary gives |z_j|<1; verify the nominal two equations exactly. Choose rational d by evaluating the third/fourth jet ratios at that nominal coefficient vector, rounded down to 10^-150. This is only a choice of test parameter; the subsequent three-row certificate, not the nominal solution, proves existence.

Actual d (exact in compact certificate) lies strictly inside the inherited d interval. The 3D rank and all nonzero cross-product normals checked exactly, infinity normalized. Minimum paid support margin 2.0357638737176927e-92 > 2e-92, density D_1 upper endpoint approximately -13687866.81290847. Thus for EVERY parameter pair in the above rectangle there exists ONE coefficient vector of Acal satisfying the three exact jet equations with this fixed d. At the earlier L0=10^100 the same strategy had negative certified margin -3.564596283747011e-92; that attempt proves neither infeasibility nor feasibility there. Only the minimal line was checked in this round; the other 114 triple-jet tests are open.

The 10^125 compact certificate rounds each center and each of 12 generators down, adds 13 grid units to each coordinate error. Exact verifier confirms the uncompressed margin and D_1 sign, rank, positive compact margin, frozen list minimum, d interval membership, and the two witnesses below. All current selected calculations completed; no fresh anchor.

## 4. Consequences: previous sharp windows survive with d coupled

For each integer L>=L0, take z as largest integer <2L satisfying pz+h=0 mod q, a=z-q. Then q<L/3, L<=a<z<2L. Let rho'=p/q+d/(az), c'=h/q-d(1/a+1/z); the pair lies in the certified rectangle, and f(m)=rho'm+c'+d/m agrees exactly with the integer (pm+h)/q at both points. The three-row certificate supplies a common coefficient vector realizing rho',c',d (the vector may depend on L).

For the first previously unexcluded dyadic triple window L3=first 10^8*2^k > dl*q^2/(4E), E=400000, use a=z-2q,b=a+q and lambda=d q^2/(2abz); add lambda to c'. The three signed residuals are +lambda,-lambda,+lambda. Exact verifier confirms rectangle containment, integer observations and individual budgets, maximum fraction 0.8199604454512887 <1. L3 approximately 3.669597785584114e114. At L2=first 10^8*2^k>=q^2, approximately 9.619630419041621e119, the pair has exact zero residual and q<=sqrt(L2). Therefore both previously sharp first-window boundaries survive the FULL rho,c,d shared compact jet relaxation, and q_min remains attainable for every L>=10^114 in this model. This is a stronger obstruction than PREFIX-1129's d-independent relaxation. It does not assert that the alternative coefficients obey the exact original moment equations or that the true fixed BRC coefficients have an anomaly.

## 5. Reproduction and next question

Readback-confirmed source:
- ef3a5c982642ad351c4536d24fe4f52983467eb9:research_notes/portable_direct/2026-11-27_r6_prefix1130_three_observer_compact.json (Git blob 5b7afeb7c30519ebfea246cde04309190fa0978e; SHA256 f6d305f9bc8918f85476215636abb41386f68289926e3dbfc11635d30f8fa30b).
- db609aaeae6c1d6c1b30aabea8affedfd9da5601:research_notes/portable_direct/2026-11-27_r6_prefix1130_three_observer.py (Git blob 83c08fb8a1a0bafaedfb3bb34fd30ebe96426b39; SHA256 75f7681eb687230e01d6d98b144bafbaaad569cd6cc9e9e876d2af4214d48c8f).
- 97ba7930f301d8d5704e537f4d4b7c6fd8fd6137:research_notes/portable_direct/2026-11-27_r6_prefix1130_verify_three.py (Git blob c1cb80acc39e034817e9439cff80c509d0a86ab0; SHA256 b75c62d64038a523ef1106a447c1d4a134d32d924d0e32c2f574167154838504).
Frozen input and exact raw output in local execution package: root_joint_compact.py, replay_9600_n300_gmp.py, anchor_compact.json, root_8800_result.json, root_9200_only.json, joint_result.json, prefix1128_result.json. Run python three_observer.py 1 then python verify_three.py. Raw result SHA256 fb7ac25cec2f37254ee4f4041e34297a31ca653acc267aadfe5a9388681a4e10. No additional BRC anchor. Prior 10^100 negative certificate preserved separately. Independent review pending.

The minimal line survives the strongest tested compact shared jet model; repeating the same three observations at larger scales cannot resolve it within this box. The next discriminating step is to evaluate one additional independent original moment direction on the same coefficient fiber, or tighten the shared anchor (not just marginal rho,c,d). The continuous integer endpoint 4.724775756597e43 and one pending candidate remain; true fixed-spectrum anomaly separation and B_fix,odd(32) remain open.
