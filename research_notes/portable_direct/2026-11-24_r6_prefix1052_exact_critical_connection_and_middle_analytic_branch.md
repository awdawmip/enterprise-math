# PREFIX-1052 — Exact critical connection and analytic middle spectral branch

Date: 2026-11-24 Asia/Shanghai. Parent PREFIX-1051. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_SYMBOLIC_CROSSCHECK / NOT_REVIEWED.

## Scope and immutable inputs

P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json, Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step, full native X6 Cell–terminal-port–grade, branch identity, sign, multiplicity and provenance retained. Only the inherited auxiliary six-phase scalar observer is analyzed. NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native propagation, phase/pi evaluation or classical reference experiment.

Sources (immutable, actual content read):
- PREFIX-1034 cb84ce603586412a1501aad920d9715d3f9c3177:research_notes/portable_direct/2026-11-23_r6_prefix1034_morse_cusps_and_critical_beta_scaling.md (leading one-sided cusp amplitudes and smooth background).
- PREFIX-1035 ebccbb436685bafe6d697ace256ad93b39c0c50f:research_notes/portable_direct/2026-11-23_r6_prefix1035_six_phase_picard_fuchs_frobenius.md (global distributional ODE and contrast identity).
- PREFIX-1044 8d29f3214a82ed34830beb11b8f64478bfccfa2c:research_notes/portable_direct/2026-11-24_r6_prefix1044_exact_edge_density_and_beta_rays.md (positive upper-edge density constant c).
- PREFIX-1051 5df27cada185084996cab98b8736d5864e333d0f:research_notes/portable_direct/2026-11-24_r6_prefix1051_critical_radius_polynomial_tail.md (upper branch and complete upper positivity).

Let rho be the scalar probability density, U'= (y−6)rho, U(36)=0, H=y²(36−y)², P=y(y−36)(17y−91), 5g=4(Hrho)'−2P rho+12(11+y)U.

## 1. Exact local basis, no logarithmic modes

For L=sum a_j(y) d^j/dy^j, expansion of the Euler operator in PREFIX-1035 gives
a0=−y²(y−6);
a1=−y²(31y²−516y+1020);
a2=−6y²(15y³−406y²+2078y−1152);
a3=−y³(65y³−2408y²+19836y−27648);
a4=−5y⁴(3y³−140y²+1568y−3456);
a5=−y⁵(y−36)(y−16)(y−4).

At v=4 or 16 put t=y−v, A_j(t)=a_j(v+t), d=a5'(v). We have A5(0)=0, A4(0)=5d/2, d≠0. Define falling factorial (m)_j=m(m−1)...(m−j+1). The coefficient of t^(m−4) in L(t^m) is d(m)_4(m−3/2); other terms have strictly higher powers. For the analytic series R(t)=sum r_m t^m, r0,r1,r2,r3 are arbitrary, and comparison at t^n for n>=0 solves uniquely for r_(n+4), with nonzero divisor d(n+4)_4(n+5/2). There are no negative powers when applying L to an analytic series. Thus all four resonant integer exponents generate independent analytic solutions, not logarithmic modes.

The fifth solution is t^(3/2) C_v(t), C_v(0)=1. For k>=1 its kth coefficient is determined by
C_k = − sum_{l=0}^{k−1} C_l W(k,l)/W(k,k),
W(k,l)=sum_{j=0}^5 [t^(k−l−4+j)] A_j(t) (l+3/2)_j,
where negative coefficient indices are zero. W(k,k)=d(k+3/2)_4 k≠0. The recurrence has finite width and each ratio of its polynomial coefficient to the divisor is bounded for large k (all degrees <=5, divisor degree 5). The analogous analytic recurrence has the same property. Hence the series converge locally by a geometric majorant; analytic ODE continuation extends them to the nearest other singularity, with C_v single valued after removing the known fractional power. The radii are at least 4 at v=4 and 12 at v=16. The real negative-side mode is (−t)^(3/2) C_v(t) with the same analytic coefficients: this follows by constant-phase continuation of the complex Frobenius solution, without a numerical phase computation.

Four independent analytic solutions plus this nonanalytic solution span the fifth-order equation on either side. In particular the general local solution contains no logarithmic modes. This strengthens the earlier indicial-root calculation, which alone could not rule out logs.

## 2. Distributional matching: analytic backgrounds on the two sides are identical

Write rho(v+t)=R_+(t)+A_+ t^(3/2) C_v(t) for t>0, and R_−(t)+A_− (−t)^(3/2) C_v(t) for t<0, with R_± analytic solutions. Each one-sided cusp is itself a distributional solution across t=0: use the analytic continuation of the homogeneous distributions t_+^lambda and (−t)_+^lambda under differentiation and multiplication by t. All exponents are half-integers, away from the negative-integer poles; differentiating a convergent analytic multiplier and applying the coefficient recurrence gives L(cusp)=0. Equivalently each possible half-integer singular coefficient cancels, with no delta distribution term. To justify using the series in distributions, remove its first five terms; the remainder times t_+^(3/2) has sufficiently many vanishing classical derivatives at zero, and the remaining series differentiates locally with convergence.

Now the inherited GLOBAL distribution identity L rho=0 forces the analytic backgrounds to join. If their first different Taylor jet has index k<=3, let delta_r be the difference of kth derivatives at zero. The jump part has leading term delta_r t_+^k/k!, modulo higher-order jumps. Its D^5 yields delta_r delta^(4−k), its D^4 yields delta_r delta^(3−k). Since t delta^(q)=−q delta^(q−1), the highest point-supported term in L is
delta_r [A4(0)−(4−k)d] delta^(3−k) = delta_r d(k−3/2) delta^(3−k).
No higher-order jump or lower derivative can contribute to that term. Its coefficient is nonzero for k=0,1,2,3. Contradiction. Therefore the first four jets agree, and the analytic recurrence forces every subsequent coefficient to agree. Thus R_+=R_−, an exact analytic connection, not just continuity or first-derivative matching.

PREFIX-1034 identifies the leading cusp coefficients: at 16 only the right side has a cusp, at 4 only the left side has a cusp. In units of the inherited upper-edge coefficient c, the amplitudes are +27/2 at 16 and −135 at 4. These are ratios of the already published symbolic coefficients, no new pi evaluation. The missing-side coefficients are exactly zero, since a nonzero leading 3/2 power cannot be absorbed into the smooth background or its O(|t|^(5/2)) remainder. Consequently:

rho(16+t)=R16(t)+(27/2)c t_+^(3/2) C16(t) for |t|<12 on the physical interval;
rho(4+t)=R4(t)−135c (−t)_+^(3/2) C4(t) for |t|<4.

The same matching holds for U, after integrating the cusp with lower limit t=0, because U is continuous. The contrast identity then reconstructs g exactly from analytic backgrounds plus the explicitly retained cusp contributions. In particular the middle rho,U,g have analytic extensions across BOTH 4 and 16. These extensions are not the physical scalar density on the other side when the cusp there is nonzero.

## 3. Exact recovery of the middle branch from the already certified upper branch

Write F(y) for the analytic continuation of the middle rho, and V(y) for its U. The fifth-order equation has no finite singularities other than 0,4,16,36. On the complex strip 0<Re(y)<36, the only apparent obstructions for this particular middle solution are 4 and 16, both removable by section 2. Analytic continuation along paths in the punctured strip is single valued: its fundamental group is generated by loops around 4 and 16, chosen with stems along the real middle interval, and each fixes this solution because its germ is analytic at that point. Thus F and V extend holomorphically to the whole strip (V'= (y−6)F, with one fixed value). The continued middle contrast G=[4(HF)'−2PF+12(11+y)V]/5 is also holomorphic there.

No singularity of the actual upper branch has to be crossed numerically. At y=20, t=y−16=4 and x=36−y=16 are simultaneously squares. The upper series rho/c=x^(3/2) sum b_n x^n from PREFIX-1051 and its first four derivatives have absolutely convergent rational-term sums at x=16. The cusp basis C16 and its first four derivatives converge at t=4. Let R_j be the four analytic basis solutions at 16 with initial coefficients [t^i]R_j=delta_ij for i,j=0..3. Write F(16+t)/c=sum_j q_j R_j(t). Its four unknown q_j are determined by the five linear equations at y=20:
sum_j q_j R_j^(k)(4) = (rho/c)^(k)(20) − (27/2) (t^(3/2) C16(t))^(k)|_(t=4), k=0..4.
The four columns are independent at this ordinary point by uniqueness of the 5th-order IVP. Appending the cusp column gives an invertible 5x5 matrix; hence one can solve the complete system and check the known cusp coefficient 27/2. Every entry is a convergent rational-term series because both x,t are squares. This is a fully specified connection formula, not a numerically evaluated connection matrix.

For the sixth state,
U(20)/c=integral_0^16 (x−30)x^(3/2) sum b_n x^n dx;
V(20)/c=U(20)/c − (27/2) integral_0^4 (10+s)s^(3/2) C16(s) ds.
Each integral admits rational-term evaluation with the same convergence. The data determine V everywhere in the strip. On (0,4), the actual rho is F(y)−135c(4−y)^(3/2) C4(y−4); actual U is V(y) plus the integral of that difference times (y−6) from 4 to y. This reconstructs the lower branch too, without erasing either cusp.

## 4. Consequence for the remaining sign proof

The middle contrast G is analytic on |y−10|<10, so its Taylor expansion about 10 has a radius at least 10 despite the two physical critical points. The entire remaining middle band [4,16] is contained in |y−10|<=6. For any bound M_R >= max_|z−10|=R |G(z)|, 6<R<10, Cauchy's coefficient estimate gives
sup_[4,16] |G(y)−sum_{j=0}^K G^(j)(10)(y−10)^j/j!|
<= M_R (6/R)^(K+1)/(1−6/R).
For example R=9 gives 3 M_9 (2/3)^(K+1). This removes the endpoint singularity obstruction from the middle polynomial certificate. M_9 and the actual coefficients still require certified evaluation. No claim of new middle positivity is made; upper [16,36) and the tiny known critical neighborhoods remain the verified positive coverage.

## 5. Exact symbolic crosscheck

Executed locally with SymPy; expanded the Euler powers by T(y^j D^j) composition (T=yD), verified A4(0)=5 a5'(v)/2 and the nonzero fractional recurrence denominator, and calculated the first five nonconstant coefficients exactly:
v=4, d=−393216:
C4 = 1 −7t/40 +157t²/4480 −2329t³/322560 +24949t⁴/16220160 −3955073t⁵/11808276480 +...
v=16, d=251658240:
C16 = 1 −t/16 +t²/256 −61t³/258048 +659t⁴/45416448 −42193t⁵/47233105920 +...
These are local ODE algebra checks, not new scalar phase samples or a native model calculation. Reproduction: substitute the six a_j into W(k,l) in section 1 and recursively evaluate k=1..5 in exact rational arithmetic. The all-order no-log and matching proofs are analytic, independent of this finite check.

## 6. Current actual control and next action

Previous original owner read r6-20261124-0950-leased-observe-v1 SUCCEEDED / error=null; fixed as-of 2026-11-24T01:52:02.926810Z, LEASED filter empty. Current r6-20261124-1050-leased-observe-v1 RUNNING / NATIVE_RUNNER at last observation. Original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED, EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Own recovery metadata reports open session and no runs, execution_authorized=false; current logical-session binding not established by metadata. No CLAIM/PROGRESS/Result/Review or protected Activity mutation. Activity association remains pending.

Next: evaluate the connection at y=20 with exact directed rational residual bounds, then Taylor/Bernstein certify the middle contrast on [4,16] or find a negative witness. Do not repeat upper band positivity or local matching. Mother B_fix,odd(32) in {19,20} remains open.