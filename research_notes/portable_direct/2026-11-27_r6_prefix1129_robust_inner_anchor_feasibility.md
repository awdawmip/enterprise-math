# PREFIX-1129 — Robust inner feasibility of the shared-anchor rho,c relaxation

2026-11-27. AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_AUXILIARY_COMPUTATION / COMPACT_ANCHOR_RHO_C_RELAXATION / NOT_REVIEWED.

Researcher EM-DIRECT-780BBE / TASK_RESEARCH; original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, Activity RA-0ABD84561C86E53067DB0322. Owner query r6-20261127-1550-leased-observe SUCCEEDED, error=null, LEASED tasks=[], next_cursor=null, as_of 2026-11-27T07:51:29.624465Z, Source d1b6a136f642e5e588242ac319d0525410520d45. No CLAIM or shared Task mutation.

## Inputs and scope

Continue PREFIX-1128 at 3f5d43256df6712da2675f91f517be87521971ac:research_notes/portable_direct/2026-11-27_r6_prefix1128_affine_strip_scale_localization.md. Use its exact 115 primitive lines in the tail L0=10^100, q<=3*10^60, not a new model or new task. Frozen P000 V5 and joint observer, X6 time, residual fidelity companions at f42f2906d77f24085c123f3ccfe9667d41caa96d; current global entries at 88ea110857f791249f9717cb0fe00fa3c4a95a7e. Retain signed reversal -5, 5q cover, chart O incoming -e1, next incoming -d, both orientations Link{O,e1} blocked without renormalization, exactly two negatives. The two observation coordinates below are auxiliary algebraic readouts of the inherited signed X6 carrier, not native spatial axes or time. Reuse PREFIX-1126 compact shared anchor and its signed Frobenius evaluator; no new moment anchor, native CT enumeration, or classical replacement of native arithmetic. Inherited carrier correspondence, root isolation, analytic boundary and 8400/8800 command-exit uncertainty remain conditions.

Important distinction: the compact coefficient set encloses the true coefficients, but can contain additional vectors. The theorem below imposes the common root and c-jet relations on this entire shared-column set; d remains independently retained, not linked to the same coefficient vector. We do not claim that alternative vectors satisfy the exact original moments, actual fixed BRC coefficients, or the remaining d-jet constraint.

## 1. Robust inner zonotope theorem

Let the compact coefficient set be A=a0+W[-1,1]^6+diag(dr)[-1,1]^6, using all 12 columns, including rounding directions. For any t,c, use the linear observation map H(a)=(F_a(t), beta(t)F_a''(t)+(alpha(t)-c)F_a'(t)), where F_a=sum a_i P_i and

    alpha=36/t^2-2+(1-t^2/36)/2*(198/t^2+216/(4-t^2)+216/(16-t^2)),
    beta=9/t-t/4.

Write its actual image as Z=m+sum_j[-1,1]v_j. Suppose interval evaluation encloses each coordinate of m and each v_j on a parameter rectangle, and choose rational center m0 and rational generators v0_j. Let e_i bound |m_i-m0_i|+sum_j|v_ji-v0_ji| uniformly there. Set Z0=m0+sum_j[-1,1]v0_j, assume rank of the rounded generators is two. For every normal n perpendicular to a nonzero generator, require

    S(n)=sum_j|n dot v0_j|-|n dot m0|-sum_i|n_i|e_i > 0.

Then for every parameter in the rectangle and every exact basis realization enclosed by the intervals, 0 belongs to the actual image Z.

Proof: The centered zonotope in two observation coordinates has all its facet normals perpendicular to generators: in any support direction, every generator not perpendicular to the direction contributes a single endpoint, and a positive-dimensional exposed face requires a perpendicular nonzero generator. The displayed conditions check both orientations of each facet. Thus the rectangle [-e,e] is contained strictly inside Z0 by its facet halfspaces. Consequently for all directions n, h_Z0(n)>=sum_i|n_i|e_i. Triangle inequalities give h_Z(n)>=h_Z0(n)-sum_i|n_i|e_i>=0 for every n. A compact convex set containing no origin has a strictly separating support direction, a contradiction. Therefore 0 is in Z. This proof uses a single common coefficient vector for both observations; it does not infer common feasibility from independent intervals. It remains valid when the exact basis values vary jointly anywhere inside the interval enclosures. Axis normals may also be checked redundantly.

If additionally F_a'(t)<0 throughout A and the t interval, an attained zero of H gives a root at t with the specified c relation without division by zero. Put rho=36/t^2-1. Thus each parameter pair in the checked rectangle is attained by some coefficient vector of A. The vector can depend on the parameter pair.

## 2. Direct BRC evaluation on all 115 candidate rectangles

For each primitive relation (q,p,h) retained by PREFIX-1128 let d0 be the midpoint of the inherited d interval. Test the entire rectangle

    rho in [p/q, p/q+d0/L0^2], c in [h/q-2*d0/L0,h/q].

Convert rho to an outward rational t enclosure by integer square roots of 36/(1+rho), using grid 10^180. Evaluate the frozen six signed Frobenius basis polynomials and derivatives 0,1,2 with outward integer Horner and the existing product-rule tail bounds. Form centers and all twelve shared observation columns directly with interval arithmetic. Pay the sum of their coordinate radii, not merely the center uncertainty. Normalize each facet normal by its infinity norm. Independently enclose F_a' over the full coefficient set by center plus/minus coefficient radii times basis bounds.

Actual execution direct_all.py produced 115 rows, all with strictly positive S and strictly negative F_a' upper endpoint. The independent Fraction verifier prefix1129_verify.py reconstructs the complete earlier finite lattice box (620 integer points, 115 primitive candidates), checks equality and order of the candidate list, every rectangle's inclusion in inherited rho,c,t boxes, every square-root inequality, generator rank, exact margins and derivative sign, and the two witnesses below. This is an auxiliary arithmetic verification, not a new native BRC anchor.

Results: minimum normalized S = 9.671944802156032e-86 (row 36); minimum-q row 3.915903050553181e-85. Every margin strictly exceeds 9.671e-86. The maximum F_a' upper endpoint is about -9.569233600936583e9. Hence every one of the 115 entire rectangles is feasible in this common compact-coefficient relaxation, uniformly in the evaluated t,c ranges. There is no new exclusion of these lines at this relaxation level.

## 3. Exact pair family and sharp-window witnesses

The smallest q of these lines is

    704830121671781357562188570181003663463817577529892083528277.

For any of the 115 lines and any integer L>=L0, q<L/3. Choose z as the largest integer below 2L satisfying p*z+h=0 mod q, and a=z-q. Then L<=a<z<2L and j_m=(p*m+h)/q is integral at both points. Set

    rho'=p/q+d0/(a*z),
    c'=h/q-d0*(1/a+1/z).

These parameters lie in the checked rectangle. Direct substitution in f(m)=rho'*m+c'+d0/m yields f(a)=j_a and f(z)=j_z exactly. The theorem supplies a common compact coefficient vector for rho',c'. Therefore every line has a pair witness for every integer L>=L0 in the d-independent compact relaxation (the vector may vary with L). In conjunction with the inherited lower bound, q_min is sharp at this relaxation level.

For the first previously unexcluded dyadic triple window L3 (the first dyadic 10^8*2^k>d_l*q_min^2/(4E)), choose z as above, a=z-2q, b=a+q and lambda=d0*q^2/(2*a*b*z). Set rho'=p/q+d0/(a*z), c'=h/q-d0*(1/a+1/z)+lambda. The exact residuals at a,b,z are +lambda,-lambda,+lambda. The same rectangle containment and the individual budgets |residual|*m^2/E<=1 were verified using exact fractions with E=400000. Maximum budget fraction 0.8199604454512887, strictly <1. Thus at L3 approximately 3.669597785584114e114 the triple is attainable in the d-independent compact relaxation.

For the first previously unexcluded dyadic square-root gap window L2 (first dyadic >=q_min^2), the pair construction gives gap=q_min<=sqrt(L2) and both residuals exactly zero. L2 approximately 9.619630419041621e119. Exact L3,L2 and all witness coordinates, residual parameters and budgets are in prefix1129_witnesses.json and prefix1129_verify.log. These constructions prove the information obstruction of the specified relaxation, not a true anomaly of the fixed Stage46 model.

## 4. Compact certificate and evidence

Downward-quantize every center and every generator on grid 10^100. All 115 rows have exactly the same twelve quantized generators. Increase the outward coordinate error by thirteen grid units (one center plus twelve columns) and take the maximum across all rows. The resulting integer error vector is [14,718627856610] on that grid. The exact compact certificate is 6504 bytes versus detailed raw 1308338 bytes (about 99.50% smaller). Minimum exact support margin still >9.671e-86, displayed 9.671944802155936e-86; first-row margin 3.9159030505531707e-85. Standalone compact verifier checks all 115 rows; with original raw file present it also checks every rounding payment and raw SHA256. This is a proof certificate for the declared two-observer scope, not permission to discard the full shared coefficient carrier.

Published and byte-readback verified:
- compact certificate fbdcf0f5a185dcc9d6cc6c1438bc571064134fd8:research_notes/portable_direct/2026-11-27_r6_prefix1129_compact_inner_certificate.json (SHA256 147cab7eb0d98230e19aa2353c5b5754114ff4315e6878b9dc3716bc07feef74)
- direct generator f18e8cf25d6a03afa522127e167d5d2d6fc95989:research_notes/portable_direct/2026-11-27_r6_prefix1129_direct_all.py (SHA256 833944350faae893045ce1bd92002a2c2a2f08c0f55b018fc773984e4f151246)
- verifier d771bc2fe1fc970ee36161783eaf67a15cb934ae:research_notes/portable_direct/2026-11-27_r6_prefix1129_verify.py (SHA256 c3ac908d571340891384a2a83f919631e9e9291f52aa18c9eabbf25b6e6ddc73)
- compact verifier 42ef7926d84dbaf9f68f8b9feb016fa10ce33348:research_notes/portable_direct/2026-11-27_r6_prefix1129_compact_verify.py (SHA256 a474c5f118e67e913f91009b99927490b08f64b957ee70b969c87c31d89f9b1a).

Frozen local inputs: root_joint_compact.py, replay_9600_n300_gmp.py, anchor_compact.json, root_8800_result.json, root_9200_only.json, joint_result.json, prefix1128_verify.py, prefix1127_verify.py, prefix1128_result.json. Exact file identities in SHA256SUMS in execution package. The raw direct_all.jsonl SHA256 is 9cc65e3e30d00765d738502705e6c82a2a5601520eabe16354fe26baddfe7824; witness JSON SHA256 c7fc43c8ef6500eccf498a6fee74ac7a170d42b35e9f63345f4bcb1479ee351d. All three executed programs exited 0. In the package directory run python direct_all.py, python prefix1129_verify.py, python prefix1129_compact_verify.py (Python with existing SymPy dependency for Frobenius generator, standalone compact arithmetic uses standard library). Full raw outputs, logs and frozen inputs are retained locally; independent mathematical review and Activity observation audit pending.

## 5. Next scientific question

The two-observer compact shared-anchor relaxation with independently retained d has reached the exact first unexcluded windows: the previous finite bounds remain unchanged, including continuous integer endpoint 4.724775756597e43 and its one pending candidate m=47247757565973207955345875119021762026915609. The next discriminating step is to impose the exact d-jet equation on the same coefficient vector (requiring an additional signed derivative observation), testing whether this removes q_min or other lines. If all remain feasible, sharpen original moment constraints or make targeted new anchor observations. Do not redo 9600 anchoring merely to repeat the existing two-observer result. Unbounded single anomaly separation, exact zero and B_fix,odd(32) remain open.
