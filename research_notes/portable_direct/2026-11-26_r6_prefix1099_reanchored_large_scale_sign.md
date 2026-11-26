# PREFIX-1099 — Re-anchor the six radial modes to 25 decimals; certified last-negative signs through 10^20

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Same frozen Stage46 double-negative BRC radial observer. Original own session metadata recovered by r6-20261126-0949-own-recovery-v1 (SID MCP-f6d93209fc8e4c5bb2c3b44f69a47174, original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, no own run); EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Owner query r6-20261126-0949-owner-read-v1 SUCCEEDED/error=null, Source b8cc35e065391066f098dc1e1de907a4bcdb0a4a, inventory as_of 2026-11-26T01:50:01.240873Z, LEASED filter empty, completed 01:51:17.899292Z. No new claim, task mutation, result freeze, or mathematical acceptance.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Same original six-axis joint Cell equality, sign, phase, ordered multiplicity and ports as PREFIX-1098. The work bounds its existing exact radial observer; no new native propagation or classical physical comparison. Parent files:
- dc4fcdd14e85a886f07b6484ee67acd260e5081a:research_notes/portable_direct/2026-11-26_r6_prefix1095_frobenius_certificate.py (exact row and basis, grouped BRC occupancy moments)
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md (basis convergence, anchor and lower-band bridge)
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md (entire suffix monotonicity)
- 93558d71777dd7ca3de8e5e238dc3e6e87592a40:research_notes/portable_direct/2026-11-26_r6_prefix1098_beta_sign_oracle.md (normalization, integration, cutoff and sign oracle)
- a89442d139ce2bd37d3b51a1d16bdd153e486c31:research_notes/portable_direct/2026-11-26_r6_prefix1099_reanchor_sign.py (consolidated reproducible companion, verified complete remote readback; local actual tests were equivalent split scripts, not execution of the consolidated remote file).

## 1. Re-anchoring, with explicit fixed-denominator rounding

The 1095 original four y0 anchors used k=(2000,2400,2800,3200), then rounded all six parameters to 10^-15 endpoints. The raw base-mode radius was about 2.87208123e-18. 1098 found that the resulting public intervals dominated the large-scale oracle error. We now use k=(2800,3200,3600,4000), and mixed anchors at k=2800. Retain the same four 201-term Frobenius modes with exponents 0,1/2,1,2, the same two homogeneous mixed modes and the same original BRC occupancy recurrence. The exact mixed moments use shifts (1,1,0,0,0,0) and (2,1,0,0,0,0). No high-m CT enumeration.

Use the parent incomplete Beta integrals J_a(k)=integral_0^1 R^a(1-R/36)^k dR, with the exact two recurrences
J_a(k)=(k J_a(k-1)+(35/36)^k)/(a+k+1);
J_(a+1)(k)=36[(a+1)J_a(k)-(35/36)^(k+1)]/(a+k+2).
All terms are rational for a integer or half-integer. To avoid a giant common denominator, round EACH exact product in each local matrix entry downward on grid H=10^100. For N=200, a matrix entry has N+1 terms, so its extra absolute error is <=(N+1)/H. For a 4-entry row, pay 4(N+1)/H. The exact global y0 observations are also rounded downward on the same grid, paying 1/H. The mixed global observations and homogeneous denominators are kept exact. Sign is respected in rounding.

Let M be this 4x4 rational matrix and o the rounded exact global moments. Let eb=sum four parent basis tail bounds +4(N+1)/H. Let e_i=(35/36)^k_i+1/H. The actual basis matrix and observation satisfy (M+E)c=o+eta with ||E||_infty<=eb and |eta_i|<=e_i. Define c_hat=M^-1 o, kappa=||M^-1||_infty eb, r=max_i sum_j |(M^-1)_ij|e_j. Then, for kappa<1,
||c-c_hat||_infty <= (r+kappa||c_hat||_infty)/(1-kappa)=delta.
Proof: write c-c_hat=M^-1(eta-E c), use ||c||<=||c_hat||+||c-c_hat|| and rearrange. This is the parent's exact perturbation bound, extended to pay the fixed-grid rounding explicitly. No uncontrolled floating point.

For the two mixed rows j=1,2, let rr be the four locally integrated (and grid-rounded) basis contributions and d=J_j(2800)>0. The homogeneous coefficient center is (ob-rr*c_hat)/d. Its radius is bounded by
[TV_j (35/36)^2800 + delta sum_i |rr_i| + (||c_hat||+delta) eb]/d,
where TV_j=6^(j+1)/(j+1), as in 1095. The grid and series error in the mixed row are <=eb. This yields the six new enclosing intervals, integer endpoints divided by 10^25:
c0 [1684139808832244674612244,1684139808832244674612245]
c1/2 [403144180414993614805275,403144180414993614805276]
c1 [-109220034251684978380170,-109220034251684978380169]
c2 [-1,1]
Ch1 [336827961766448934922448,336827961766448934922449]
Ch2 [28068996813870744576870,28068996813870744576871].
Actual base radius 2.839468037584961e-27 (<3e-27 exact check), mixed radii 7.192261898228823e-29 and 9.507677080254694e-28 (display only), inverse infinity norm approx 677316302.0171807. All six outward-rounded intervals are strictly narrower than and contained in the old ones (exact integer comparisons); the width shrinks by 10^10 in each coordinate. The base raw radius shrinks by about 10^9. c2 remains unresolved as an exact zero. We retained independent boxes here, not a claim that correlations were already exploited.

Actual local anchor run rebuilt the zero-shift 7x7 ODE and verified the four matrix norms, eigenbasis, resonance conditions and contraction factor 5025203/5349120. Exact BRC integer moments generated through 4000 for the zero shift and 2800 for each mixed shift, all divisions exact. One initial implementation used 2H-I in place of H-I for the zero-shift block, failed at the eigenvector construction, and was corrected before the successful run. The final local anchor calculation took approximately 12.85 seconds excluding the shared basis build. Exact signs use rational comparisons. There was no external classical input or attribution.

## 2. Adaptive-degree oracle and signed integration

Reuse PREFIX-1098 theorem: for D_m(k)=L[x^m(1-x)^k], B=integral_0^1 x^m(1-x)^k dx>0, K=36/(4*36^8*16^3*4^3)>0,
D_m(k)/(KB) in [V-E,V+E].
Here t=6 sqrt(x), T=13/10, w=T^2/36, s=(1299/1000)^2/36. Reconstruct the 66 signed Laurent terms and the exact 28x7 map (SHA256 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312), preserving all signs and joint observations. In each of six basis polynomials F_j retain n<=cut terms; bound the omitted terms from cut+1..200 by exact coefficient magnitudes and n>200 by 64 T_lambda 2^-n. Multiply by the exact polynomial readout row's absolute bound on [0,T]. Round coefficientwise down on 10^-digits and compute the ACTUAL weighted rounding residual at T, not a guessed generic error. For d=4,16 approximate (1-t^2/d)^-3 by A_d=sum_(n=0..J) binom(n+2,2)(t^2/d)^n; with u=T^2/d, the tail is bounded by eps_d=binom(J+3,2)u^(J+1)/(1-u(J+4)/(J+2)), since the successive ratios decrease. Let M_d=(1-u)^-3 and P_j=t^6 Q_j A_4 A_16. The local uniform error is
E_loc=T^6[(E_series+E_round)M_4 M_16+H_F(eps_4 M_16+M_4 eps_16)],
where H_F=sum_j mag_j sum_l |Q_jl|T^l. This follows by a product telescoping and the triangle inequality; A_d<=M_d. The powers and error weights are those of the existing scalar readout, not native state replacements.

Parameters (cut,J,digits,degree,E_loc displayed):
(50,80,30,450,2.478937338188522e-8)
(60,100,40,550,2.8939936721693415e-12).
Reused exact half-integer Beta moment reduction and the 16th central moment square-root certificate from 1098. The common sqrt error is paid after signed center combination, independent anchor radii after each signed integration. Same global C^3 cutoff and monotone monomial tail estimate; all admissibility tests per observation checked. Upward repeated-squaring lattice increased from 2^-256 to 2^-512, so no large rational powers are built for the sign oracle. Formula:
V=sum_j c_j (A_j+B_j v);
E_int=|sum_j c_j B_j| e + sum_j r_j(|A_j+B_j v|+|B_j|e).
Then E=E_int+E_loc+E_out as in 1098. All endpoints below have strict rational V+E<0 or V-E>0. They use exact parent bridge and monotonicity, not a re-enumeration of the native CT table.

## 3. Actual sign certificates and exact last-negative integers

Since all tested m>=100000 and 5*l>=107m, the 1097 infinite monotonicity applies to the suffix. A strict negative l and strict positive u certify the entire global last-negative integer K_last(m) in [l,u-1]. If u=l+1 this is exact. The following values were obtained by local exact rational computations. V_l,V_u and radii are rounded DISPLAY values; exact sign tests were performed before printing. The 450-degree run:
m,l,u,V_l,E_l,V_u,E_u
1e10,214400367303,214400367304,-.1335717571613112,2.481559930008558e-8,.5789999353886175,2.481559930008492e-8
1e11,2144003672139,2144003672140,-.04313971489923975,2.481559930010122e-8,.02811745442937191,2.4815599300101153e-8
1e12,21440036720503,21440036720504,-.00559364299007127,2.4815599300102757e-8,.001532073943514219,2.481559930010275e-8
1e13,214400367204145,214400367204146,-.000413892412621531,2.481559930010291e-8,.0002986792807442018,2.481559930010291e-8
1e14,2144003672040563,2144003672040564,-3.8431693550277245e-5,2.4815599300102923e-8,3.2825475786368466e-5,2.4815599300102923e-8
1e15,21440036720404743,21440036720404744,-8.856216431717351e-7,2.4815599300102926e-8,6.2400952904935604e-6,2.4815599300102926e-8
1e16,214400367204046538,214400367204046540,-6.938729192940673e-7,2.4815599300102926e-8,7.312704674390065e-7,2.4815599300102926e-8
1e17,2144003672040464497,2144003672040464498,-3.338352287642265e-8,2.4815599300102926e-8,3.7873646460231115e-8,2.4815599300102926e-8
1e18,21440036720404644078,21440036720404644087,-3.146603563764656e-8,2.4815599300102926e-8,3.2665416765341836e-8,2.4815599300102926e-8.

The 550-degree run closed the two remaining earlier brackets and extended the scale:
1e16,214400367204046538,214400367204046539,-6.938732326040196e-7,2.911991188987661e-11,1.8698460762517238e-8,2.911991188987661e-11
1e18,21440036720404644082,21440036720404644083,-2.963481212937367e-9,2.911991188987663e-11,4.16223572072801e-9,2.911991188987663e-11
1e19,214400367204046439931,214400367204046439932,-6.340174089601451e-10,2.911991188987663e-11,7.855428440639255e-11,2.911991188987663e-11
1e20,2144003672040464398426,2144003672040464398428,-4.478518187915413e-11,2.911991188987663e-11,9.772915679415341e-11,2.911991188987663e-11.

Thus all ten power-of-ten rows m=10^10,...,10^19 are now exact; the 10^20 row has two certified candidates [2144003672040464398426,2144003672040464398427]. The 1098 five smaller rows were not recomputed. No claim of coverage of every intermediate integer m. The last negative search uses a secant predictor only to choose probes, then exact sign and suffix monotonicity to certify. In the two ambiguous 450-degree rows, refinement was performed by a more accurate oracle, not by claiming the midpoint sign. The 10^20 bracket is a sufficient certificate; not proven optimal. The final two degree choices use 225 and 275 steps for each integer and half-integer moment array, respectively; no giant normalization factorial. Bit complexity and arbitrary precision preprocessing still need separate analysis.

## 4. Correlation-preserving dual bound (new reusable lemma, not used in the numerical results)

Let A be an invertible rational 6x6 approximate anchor matrix for the four y0 and two mixed equations, let o be the exact/rounded observation vector, and let actual (A+E)theta=o+eta with elementwise |eta_i|<=e_i and |E_ij|<=b_ij. Let theta_hat=A^-1 o and suppose certified |theta_j|<=M_j. For any exact rational target row v, define z=A^-T v. Then
|v^T(theta-theta_hat)| <= sum_i |z_i|(e_i+sum_j b_ij M_j).
Proof: v^T(theta-theta_hat)=z^T(eta-E theta). Pay absolute values only after constructing the signed dual z. For a rectangular anchor system, any rational z with A^T z=v gives the same bound relative to z^T o. If target row itself has a certified error r_j, add sum_j M_j r_j. This preserves correlations induced by shared moment equations; comparison with independent boxes for the actual six-mode coefficients is not yet computed. For a fixed square exact A and independent observation errors, this is the sharp linear-functional support bound (take eta_i signs aligned with z_i); entrywise matrix uncertainty gives a safe larger enclosure. This is a route to avoid expanding all individual coefficient intervals, and may make the next high-m sign test cheaper than increasing every precision parameter.

## 5. Verification boundary and next

Actual local runs: basis rebuild, re-anchoring, complete 66-term symbolic row reconstruction, fixed-degree exact rational oracle (450/550), strict endpoint assertions for all 13 displayed pairs, including repeated 10^16 and 10^18 refinements. The earlier 1098 350-degree radius near 10^12 was about .262618602; new 450-degree radius is 2.48156e-8, and 550-degree radius near 10^20 is 2.91199e-11. These are normalized enclosure radii, not actual native residual magnitudes or measured speed gains. At degree 550 the anchor payment is again the dominant part (~2.62259e-11), so improving only polynomial degree has limited value. The local scripts reanchor.py/oracle.py/extend.py and parameter variants were actually executed; consolidated companion reproduces all exact rows from the immutable parent and was published/read back, not separately run as that consolidated file. Independent mathematical review and Activity observation audit pending.

Next: compute the two remaining 10^20 candidate signs by retaining the unrounded anchor error or using the dual support lemma; increase anchor endpoint precision and fixed-degree local approximation only as needed. Establish precision-versus-scale and cost bounds, and classify the remaining spectrum independently. Mother B_fix,odd(32), global spectral p,d and full sign classification remain open. Do not redo the previously closed rows or infer mother-goal closure. 
