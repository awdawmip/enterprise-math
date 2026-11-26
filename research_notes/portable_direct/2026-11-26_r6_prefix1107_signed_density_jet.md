# PREFIX-1107 -- Signed local density jets shrink the effective integer-edge band to C=400000

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Continuation of own R6 Activity RA-0ABD84561C86E53067DB0322, EM-DIRECT-780BBE / TASK_RESEARCH. Original registration r6-20261123-2358-session-start-own-v1 recovered via own metadata receipt; no run, no new CLAIM. Current LEASED query r6-20261126-1755-owner-read-v1 SUCCEEDED / error=null, fixed as-of 2026-11-26T09:56:05.361734Z, source 5fa90d76777a48da4c2fc61d8f7b802602762d88, empty filter. This is independent continuation, not a shared Task state mutation.

Frozen science: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json and joint/time companions. Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. Full six-axis Cell equality, port, sign, phase and ordered branch multiplicity retained by the original BRC joint carrier. Use its exact auxiliary radial observer identity D_m(k)=L[x^m(1-x)^k], no native propagation rerun or external numerical reference.

Immutable sources:
- 7315c3af2b97b872aa2a4ce32142d4446a387f84:research_notes/portable_direct/2026-11-26_r6_prefix1106_scaled_moment_edge_band.md
- 04ca670bf23a2b37e9182921376cb28e87992658:research_notes/portable_direct/2026-11-26_r6_prefix1105_effective_integer_edge_band.md
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md
- 2d373f42f619a15fda899f0d36b62689725b2fed:research_notes/portable_direct/2026-11-26_r6_prefix1096_edge_shift.py
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md
- acd24d8499f11d2b8faa6cd0fd8567735f295333:research_notes/portable_direct/2026-11-26_r6_prefix1104_compressed_exception_sieve.md
- f6903fef5f9c2eae033eb4524c62bc67b437e3d5:research_notes/portable_direct/2026-11-26_r6_prefix1107_signed_density_jet.py (blob 39ef02089396d6e6de7fcb56ef544d4ac29b952b, full readback matched saved bytes).

## 1. Result

In the exact setup of PREFIX-1106 write b for the first spectral zero, rho=1/b-1, f(m)=rho*m+c+d/m, k=f(m)+e, |e|<=2, B=Beta(m+1,k+1), G=g/g'(b). Inherit .044<b<.045, 99<c<100, 9<d<10, g'(b)<0. For every integer m>=10^8 and integer k in that window,

  |D_m(k)/(g'(b)*B)+b^2*e/m| <= 1000*|e|/m^2 + 620/m^3.

Set C=400000. Whenever |e|>=C/m^2 and |e|<=2, sign D_m(k)=sign e, and |D_m(k)/(g'(b)*B)|>2/m^3. For a rigorous rational enclosure [l,u] of f(m) of width <=1/8, L=floor(l-C/m^2), U=ceil(u+C/m^2)-1 satisfy L<=K_last<=U, U-L<=1, using the existing infinite-tail monotonicity theorem. Endpoint signs follow since they have |e|>=C/m^2, |e|<=2 and are within the inherited monotonic cone. At most one native CT sign fallback, including zero. The same comparison K/|g'|<1 as in 1105/1106 shows that if a fast oracle of radius <=S^-3 fails at the queried candidate j, then |j-f(m)|<C/m^2. Thus the compressed exception sieve of PREFIX-1104 applies with A=C+1 and M>=10^8, provided the declared rational coefficient accuracy is actually supplied. The coefficient accuracy supply and real-window execution are not completed here. No new exact integer row, no proof of uniform separation or zero exclusion.

Compared with 1106: edge constant 10^18 -> 400000 (factor 2.5e12); localization activation 10^10 -> 10^8; sufficient sieve scale 2e18 -> 10^8 (factor 2e10). These are sufficient analytic constants, not measured computational speedups.

## 2. Signed reconstruction and derivative bounds

Use the exact nine-state readout of 1095/1096. With t=sqrt(36x), R=t^2, J(t)=t^6/[(16-t^2)^3(4-t^2)^3] and F(t)=N(t^2) dot (Z,h1,h2), the density is a fixed positive constant times J(t) F(t). Reconstruct all 66 signed Laurent terms before taking absolute bounds. The 28x7 elimination hash is 333adb48c52ac3c5530e8d0509a7b45b77db62a99e65557cafbd70ce38bba312; row degrees (9,10,9,9,8,8,7,9,8). Four rational Frobenius series are reconstructed to n=200 with the parent contraction 5025203/5349120<1, resonance equalities, and both mixed homogeneous terms. Reuse the actual six 15-decimal anchor intervals of 1095 and root enclosure t in [6800006737/5368709120,3400003369/2684354560]. No re-anchoring.

Use the degree <=104 signed center polynomial from n<=40. Shift its exact coefficients to t0=127/100 before interval evaluation: P(t)=sum_j p_j(t-t0)^j, p_j=sum_{i>=j} C_i binom(i,j)t0^(i-j). This preserves cancellation in the entire signed readout, instead of separately bounding the original monomials. Parameter errors use the half-width times absolute differentiated basis-polynomial bound on [0,13/10]. For j=0,...,6, the omitted exact terms n=41,...,200 are bounded by absolute coefficients, and the n>=201 basis tail by a geometric series. For each Frobenius exponent lambda and p=2lambda+402, the tail derivative term ratio is at most

  q_j=(13/10)^2/2 * [(p+2-j+1)/(p-j+1)]^j < 1.

The initial term is 64*T_lambda*2^-201*(p)_falling_j*(13/10)^(p-j). Apply Leibniz to the row N(t^2) and multiply by the full coefficient interval magnitudes. Include both homogeneous polynomial terms in parameter payment. All errors are uniform on the full t interval, not sampling errors. Calculated total F derivative error radii (j=0,...,6, display only): 0.08459976265, 0.34256569394, 1.29915298535, 6.27006664024, 132.97315917, 7494.32303554, 464828.61400407.

## 3. Exact chain-rule jet in the auxiliary observer coordinate

Let h denote a formal displacement in x, so R changes to R+36h. At a t interval, form the formal truncated coefficients (through h^6) of u(h)=t[(1+36h/R)^(1/2)-1]. Explicitly u_0=0 and u_i=t binom(1/2,i)(36/R)^i. This is exact differentiation of the algebraic auxiliary radial observer, not a new propagation approximation. Form

  Q(h) = sum_{j=0}^6 [F^(j)(t)/j!] u(h)^j mod h^7,
  J(h) = (R+36h)^3 (16-R-36h)^(-3) (4-R-36h)^(-3) mod h^7.

Use exact polynomial convolutions of interval coefficients. The coefficients of each inverse cubic are binom(i+2,2)*36^i/(d0-R)^(i+3), d0=4,16, with denominators strictly positive. The coefficient of h^i in J(h)Q(h) encloses the i-th derivative of the density divided by i! and by the same fixed positive constant. The calculation uses no interval floating comparisons and no analytic approximation to these finite derivatives. At the actual root F(t)=0 exactly, so the constant coefficient is set to zero there; off the root it is retained.

The exact interval for the first prefactor-free x derivative at the root is strictly negative (display [-13687866.8325555,-13687866.792571843]). Divide each other coefficient by this interval. At the root the resulting a2,a3,a4 intervals are contained in (display rounded) [82.3717214,82.3717222], [2737.3719441,2737.3719845], [50953.0120,50953.0138]. The actual exact comparisons reproduce |a2|<83, |a3|<2738, |a4|<51000 and establish

  |a5|=|g^(5)(b)/(5!g'(b))| < 716000.

On the full t interval [5/4,13/10], cover by ten closed equal rational subintervals. Each is evaluated by the same interval convolution, keeping F0. The maximum of the resulting sixth coefficient magnitudes divided by the root first derivative is approximately 47086212.40790303, and the exact rational comparison establishes

  sup_{t in [5/4,13/10]} |g^(6)(t^2/36)/(6!g'(b))| < 48000000.

The interval covers all x satisfying |x-b|<=1/1000 by exact endpoint comparisons. Therefore Taylor's theorem for G on the real cutoff support yields |G(x)-P5(x)|<=48000000|x-b|^6. At the root the exact computed a5 magnitude upper bound is approximately 715401.606707331. The constant from JF cancels in the ratios; no false sign change is introduced.

## 4. Combine with PREFIX-1106 moments and complement

The signed scaled Beta moments of 1106 give H5(10^-8)<6.355e-6, H6(10^-8)<1.085e-7, and the first-four truncation payment computed using the same exact rational recurrence. The old complement proof applies unchanged: cutoff inner radius 1/2000, outer radius 1/1000, m>=10^8, and the full P5 polynomial is bounded no worse than in 1106 since the new fifth bound is smaller. Its contribution <=m^-3 is already included in the small payment.

Using exact rational (not rounded) moment bounds, the new coefficient payments multiplying m^-3 are:
- first four moments and complement: 609.2321372283689 (display);
- fifth signed moment: 4.549549402131613;
- sixth Taylor remainder: 5.207362724513962;
- total: 618.9890493550145 < 620 (exact assertion).

All first- and second-order cancellations in 1096/1105/1106 are preserved: first-order coefficient -b^2 e; second-order coefficient B2(e) with B2(0)=0 and |B2'(e)|<1000 on [-2,2]. This proves section 1. The exact sign margin (b0^2-1000/10^8)*C-total is about 151.41095064498558 >2, with b0=44/1000. The bound for |e|>=C/m^2, m>=10^8 is consequently strict, including the required magnitude condition.

## 5. Execution and limits

Actual local Python/SymPy/Fraction execution completed all reconstruction assertions, all four 201-coefficient series, exact shifted polynomial and seven derivative error payments, root jet and ten uniform subinterval sixth-jet bounds, and all final rational comparisons. Floating values above are display only. The companion reconstructs the same parent prefix verbatim plus the executed derivative extension, with the same assertions; saved and exact full-file readback verified, not independently rerun as a consolidated file. No new native CT integer table, no rerun of old 18 rows, no external reference, no independent mathematical review. The previous failed streaming execution route was not needed; local Python cells succeeded.

## 6. Next

The low-order moment truncation estimate now dominates (>98% of total). If further tightening matters, directly bound the exact rational scaled moment remainder on real z in [0,10^-8], instead of using the broad Cauchy circle. More valuable immediately: implement adequate precision supply for rho,c,d and apply the compressed exception sieve to actual Stage46 windows with M>=10^8, explicitly paying coefficient uncertainty. The exact-zero question, uniform Diophantine separation, remaining spectral zeros, c2=0, and mother B_fix,odd(32) stay open.
