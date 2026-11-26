# PREFIX-1100 — Centered Beta moment denominator and correlated anchor support; exact last-negative integers through 10^22

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Original own researcher EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322. Original registration r6-20261123-2358-session-start-own-v1 read back SUCCEEDED, execution_authorized=false; fresh LEASED owner read r6-20261126-1050-owner-read-v1 SUCCEEDED/error=null, Source d8c6de1f1cc5212fbd0cdc030120753ca64c5964, inventory as_of 2026-11-26T02:51:28.011235Z, tasks=[], next_cursor=null. Independent continuation of existing directed frontier, no new CLAIM, shared task mutation, Result freeze, or acceptance.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and its joint-observer/time companion. Same Stage46 X6 chart O, incoming -e1, signed reversal -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations Link {O,e1} blocked without renormalization, exactly two negative steps. Preserve the original six-axis joint Cell equality, signed Laurent terms, phase, ordered multiplicity and ports; bound only the exact radial observation D_m(k)=L[x^m(1-x)^k]. No new native propagation or classical physical reference. Parent source pins:
- 3dbbec783d4eb0f6ae1ca4909f7b535c6f0e8cf5:research_notes/portable_direct/2026-11-26_r6_prefix1099_reanchored_large_scale_sign.md
- a89442d139ce2bd37d3b51a1d16bdd153e486c31:research_notes/portable_direct/2026-11-26_r6_prefix1099_reanchor_sign.py
- dc4fcdd14e85a886f07b6484ee67acd260e5081a:research_notes/portable_direct/2026-11-26_r6_prefix1095_frobenius_certificate.py
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md
- 93558d71777dd7ca3de8e5e238dc3e6e87592a40:research_notes/portable_direct/2026-11-26_r6_prefix1098_beta_sign_oracle.md
- New replay companion 74b507708fa98cca4031924c9344e663f217ac0f:research_notes/portable_direct/2026-11-26_r6_prefix1100_centered_beta_dual.py, blob 1d6c34d1f5858368f291ef95ef8ff6a0f9591463, complete connector readback matched; assembled from the pinned parent and the equivalent local implementation.

## 1. Pay denominator approximation after the Beta observation

The parent represented g(x)/K=R^3 F(sqrt R) phi_4(R) phi_16(R) on 0<R<4, R=36x, K=36/(4*36^8*16^3*4^3)>0, phi_d=(1-R/d)^(-3). F is the signed combination of six Frobenius bases. Parent 1099 expanded each phi_d about R=0 through order 100 for degree 550. Its uniform remainder ignores concentration of the actual Beta weight near the first root. The new construction does not change the density or observed quantity.

Let X have the normalized positive density x^m(1-x)^k/B(m+1,k+1); take T=13/10, w=T^2/36, s=(1299/1000)^2/36. Choose rational R0 with 0<R0<T^2 and q_d=max(R0,T^2-R0)/(d-R0)<1 for d=4,16. For an odd positive J with r_d=q_d*(J+4)/(J+2)<1 define
A_d(R)=(1-R0/d)^(-3) sum_(n=0..J) binom(n+2,2) ((R-R0)/(d-R0))^n.
M_d=(1-R0/d)^(-3)(1-q_d)^(-3),
C_d=(1-R0/d)^(-3) binom(J+3,2)/[(d-R0)^(J+1)(1-r_d)].

For 0<=R<=T^2, |A_d(R)| and |phi_d(R)| <= M_d; |phi_d(R)-A_d(R)|<= C_d |R-R0|^(J+1).
Proof: exact binomial series for (1-z)^(-3), z=(R-R0)/(d-R0), converges absolutely here. Absolute successive term ratios after first omitted n=J+1 are <=r_d since (n+3)/(n+1) decreases. Factor out |R-R0|^(J+1), sum remaining geometric majorant. Both magnitude bounds follow from the full positive series at |z|<=q_d.

Let Q_i(t) be six truncated and grid-rounded numerator basis polynomials, c_i,r_i enclosing actual coefficients theta_i, H_F=sum_i (|c_i|+r_i) sum_j |Q_ij| T^j. Let E_F be parent certified numerator series+rounding uniform error on [0,T]. Define P_i(t)=t^6 Q_i(t) A_4(t^2) A_16(t^2). Multiplying by t^6 and telescoping the two denominator factors gives
|g(R/36)/K - sum_i theta_i P_i(sqrt R)| <= L + G |R-R0|^(J+1),
L=T^6 E_F M_4 M_16,
G=T^6 H_F(C_4 M_16+M_4 C_16).

Multiply by the parent's C^3 cutoff 0<=chi<=1, supported on [0,w], equal to 1 on [0,s]. Integrate against normalized Beta density. Because J+1 is even, the new local error is bounded by L+G M_(J+1), where
M_(J+1)=E[(36X-R0)^(J+1)] = sum_(i=0..J+1) binom(J+1,i)(-R0)^(J+1-i) 36^i (m+1)_i/(m+k+2)_i >=0.
No absolute-value relaxation of individual binomial terms: compute the whole rational sum. This is a different placement of error payment, not a Taylor replacement of the native propagation. The same parent upper-tail C^3 observation norm and absolute polynomial monomial tail estimate apply because the approximating P_i remain polynomials in sqrt R. In particular the per-input monotonicity inequalities and upward lattice powers (now 2^-768) are checked. All contributions outside the supported region are paid as in 1098/1099. The true signed D_m(k) itself is unaltered.

With degree parameter cut, polynomial degree bound is 2(cut+12)+4J+6, rather than requiring two long zero-centered geometric sums. With cut=80, J=7, degree 218; integer/half-integer moment recurrence lengths are 109 each. The error G M_8 becomes extremely small in the large-scale localized regime; for fixed center not exactly equal to limiting R it need not tend to zero as m grows. In particular it is not a uniform all-scale arbitrarily precise oracle. This explicit centered moment is useful for choosing J and R0 from the declared target.

## 2. Actual correlated anchor calculation

Use the 1099 exact BRC grouped occupancy and incomplete Beta recurrences, with all six equations at once. Four y0 rows and two mixed rows give (A+E)theta=o+eta. A and o are exact rational values after downward rounding each product on H=10^100. In addition to the earlier 4(N+1)/H, pay 1/H for rounding the mixed homogeneous diagonal term. Row-sum matrix error <= e_b=sum of the four parent basis tail bounds + [4(N+1)+1]/H. The four observation errors are (35/36)^k_i+1/H, the mixed rows are 6^(j+1)/(j+1)*(35/36)^k_1+1/H. Old 25-digit boxes imply |theta_i|<1; thus |eta_i-(E theta)_i|<=eps_i=observation_error_i+e_b.

Let c*=A^-1 o, round each c*_i downward to 10^-50 to obtain c, dr_i=|c*_i-c_i|. For every exact target vector v define
S(v)=sum_j |sum_i v_i (A^-1)_ij| eps_j + sum_i |v_i| dr_i.
The exact linear-functional identity from 1099 yields |v^T(theta-c)|<=S(v). Coordinate radii r_i=S(e_i); verify all six resulting boxes lie inside the prior public 25-digit boxes. The old signed half-integer Beta integration gives v=a+b*s_hat, with |E sqrt X-s_hat|<=e_s using the 16th centered moment. Then
|theta^T E[P]-c^T v|<=S(v)+(|c^T b|+S(b))e_s.
This pays the shared sqrt uncertainty and joint anchor uncertainty after signed combination. For comparison independent coordinate payment sum r_i(|v_i|+|b_i|e_s) was also computed. Whole normalized certificate:
D_m(k)/(KB) in [V-E_total,V+E_total], V=c^T v,
E_total=S(v)+(|c^T b|+S(b))e_s+L+G M_(J+1)+E_out.
All signs are exact rational comparisons. No giant factorial for B is evaluated.

Actual first anchor k=(2800,3200,3600,4000) coordinate radii (rounded display):
[1.726431889409088e-30,5.187102538527914e-29,3.439151879461e-28,2.839468037584961e-27,6.385194023910965e-30,9.40442346481771e-28].
Refined k=(3200,3600,4000,4400), mixed at 3200:
[3.6954058127208133e-35,1.1706091630744562e-33,8.184589401908806e-33,7.519917489126037e-32,1.0812249948858252e-34,1.7923020325861407e-32].
All contained in the old boxes exactly. The original six-state correlation reduces actual anchor error at the large-scale edge from about 6.85374e-13 (raw independent coordinate boxes) to 6.59315e-13 (dual support), about 3.8%; the much larger reduction relative to 1099's 25-digit rounded boxes is primarily from retaining raw unrounded information. For the refined anchor the corresponding values are 1.81027e-17 and 1.74825e-17. Do not attribute all improvement to the dual.

## 3. Exact execution evidence

Local Python 3 + SymPy 1.14.0. Reconstructed the parent's original 66 signed Laurent terms; exact 28x7 rational elimination digest 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312 matched; four 201-term bases, resonances, contraction factor 5025203/5349120 and matrix norms checked. Native BRC grouped integer moments through 4000 and then 4400, mixed through 2800 and 3200, all divisions exact. No high-m CT enumeration. First run used (cut,J,digits,R0)=(80,15,55,8/5), degree 250, L approx 1.5897166254108988e-18. At m=10^20 it certified negative l=2144003672040464398426 and positive l+1, E_total approximately 6.593161429794825e-13. The narrower centered choice (80,7,55,160427545/10^8), degree 218, L approx 1.6450964920974603e-18, G approx 4104696982693.0483, gave the following actual local exact comparisons (centers and radii shown as rounded display, not the rational certificate itself):

m,l,u,V_l,V_u,E_l,E_u
1e5,2144102,2144103,-57936.145020184435,13313.044496936642,.0002152665852444919,.00021512751635970956
1e9,21440036819,21440036820,-3.888178972774791,3.2375378802922388,6.593162099110117e-13,6.593162097410991e-13
1e20,2144003672040464398426,2144003672040464398427,-4.418290971067415e-11,2.7074259625979617e-11,6.593161983593491e-13,6.593161983593491e-13
1e21,21440036720404643983373,21440036720404643983375,-6.636837803571182e-12,7.614596063759573e-12,6.593161983593491e-13,6.593161983593491e-13
1e22,214400367204046439832846,214400367204046439832848,-7.445155327612714e-13,6.80627853971804e-13,6.593161983593491e-13,6.593161983593491e-13.

The intermediate k at 1e21 and 1e22 remained undecided under this first anchor. Secant interpolation merely selected probes; it never certified signs. At 1e20 the new centered geometric error G M_8 was approximately 1.53069e-62, compared to uniform L 1.64510e-18 and anchor 6.59315e-13. At 1e5 the geometric error was about 1.57560e-4 and outside error about 5.77065e-5, both explicitly paid. Therefore the improvement is concentrated where the Beta mass is local, not claimed uniformly for every input.

Refined anchors without increasing the 218 degree:
1e21,21440036720404643983373,21440036720404643983374,-6.637907832856747e-12,4.878091008086301e-13,1.9127615888091676e-17,1.9127615888091676e-17
1e22,214400367204046439832847,214400367204046439832848,-3.301386868029895e-14,6.795578246862388e-13,1.9127615888091676e-17,1.9127615888091676e-17.
Both exact sign comparisons and E_out<10^-100 assertions passed, with 5*l>=107*m and m>=100000. The local refine tool reached its time limit after printing BOTH EXACT results (including the assertions immediately before each print); process exit itself not verified. The two earlier local executions returned results normally. The published companion incorporates the equivalent local method and all displayed endpoint checks; it was read back in full, not separately run as that combined remote file. No floating sign decisions. Displayed zeros for E_out are float underflow, not a proof of exactly zero.

By PREFIX-1097 strict normalized suffix monotonicity, any strict negative l and positive u in the certified suffix imply global K_last(m) in [l,u-1]. Adjacent l,u give exact last-negative integer. Thus the three newly closed rows are
K_last(10^20)=2144003672040464398426,
K_last(10^21)=21440036720404643983373,
K_last(10^22)=214400367204046439832847.
Together with the prior 15 rows, 18 power-of-ten scales 10^5 through 10^22 are certified, not all intervening m. From 550 to 218 degree and 275 to 109 each moment recurrence is a reduction of about 60.4% in these counts, not measured runtime or bit complexity. The 1099 large-scale radius 2.91199e-11 vs the refined new 1.91276e-17 illustrates the joint effect of raw anchor, refined anchors and observation-aware denominator payment.

## 4. Next useful research question

Do not rerun the closed rows merely to extend the decimal list. Develop a precision-versus-scale certificate based on a genuinely shrinking center choice and even moments, rather than fixing R0: separate anchor accuracy, numerator series convergence, geometric remainder, and integer boundary separation. The simple root provides asymptotically adjacent normalized gaps of order 1/m, but an arbitrarily near-integer critical point may require additional precision or a zero decision; no universal bit-cost bound follows yet. Also pursue full spectrum sign classification and c2=0 as separate questions. Mother B_fix,odd(32) and global p,d remain open. Independent mathematical review and Activity observation audit remain pending; this is an author-reproduced conditional analytic/finite rational increment.
