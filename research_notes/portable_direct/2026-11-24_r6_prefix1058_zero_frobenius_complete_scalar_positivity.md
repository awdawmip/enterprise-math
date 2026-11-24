# PREFIX-1058 — Zero-endpoint Frobenius bridge and full auxiliary scalar spectral positivity

Date: 2026-11-24 Asia/Shanghai. Parent PREFIX-1057. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and dependencies

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Retain Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step, full native X6 Cell–terminal-port–grade, branch, signs, multiplicity and provenance. Analyze ONLY the already-derived auxiliary scalar observer; NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native propagation, classical phase evaluation or pi computation. Mother B_fix,odd(32) in {19,20} remains open.

Read immutable sources:
- PREFIX-1035 ebccbb436685bafe6d697ace256ad93b39c0c50f:research_notes/portable_direct/2026-11-23_r6_prefix1035_six_phase_picard_fuchs_frobenius.md (ODE).
- PREFIX-1044 8d29f3214a82ed34830beb11b8f64478bfccfa2c:research_notes/portable_direct/2026-11-24_r6_prefix1044_exact_edge_density_and_beta_rays.md (bounded rho at zero, exact integral identity, positive c, continuous g, Hausdorff/Beta identity).
- PREFIX-1045 9567f20ca52f44f4b33adc2535ca26a2985d193e:research_notes/portable_direct/2026-11-24_r6_prefix1045_uniform_boundary_cones_and_negative_density.md (global alternative).
- PREFIX-1052 de0250c78a0952c5b282623dacedce81c47bad90:research_notes/portable_direct/2026-11-24_r6_prefix1052_exact_critical_connection_and_middle_analytic_branch.md (four analytic modes plus signed cusp at 4).
- PREFIX-1057 1253ec572d43e8c3afbddb1c3df0badf21561f82:research_notes/portable_direct/2026-11-24_r6_prefix1057_recentered_lower_spectral_bridge.md, checker 45b5c2473ea65a63239d2f9c00ced6a3d7a1f0c8:research_notes/portable_direct/PREFIX1057_R6_RECENTERED_LOWER_CHECK.py (all-band coverage [1/240,36), inherited PREFIX-1054 connection boxes and PREFIX-1056 uniform tail). The inherited certificates are dependencies, not independently replayed here. In particular use the loose bound |(5/2)^n b_n|<10^−18 for n>100 in each 4-side mode from PREFIX-1057. Recompute the first 101 terms for each mode at a different connection point.

## Theorem

Let c>0 be the inherited upper-edge density coefficient, u=rho/c, v=U/c. Then

5g(y)/(cy)>13,000,000 for 0<y<=1/240.

Together with PREFIX-1057, g(y)>0 for every 0<y<36. Continuity and the inherited endpoint expansions give g(0)=g(36)=0. Hence the auxiliary scalar spectral contrast is nonnegative on its entire support, strictly positive on the interior. For every pair of nonnegative integers m,k, the inherited integer-scaled Hausdorff difference E_{m,k}=integral_0^36 y^m(36−y)^k g(y)dy is strictly positive, as is D_{m,k} in PREFIX-1045. The signed native correspondence remains a separate open question.

## 1. Exact endpoint primitive constraint eliminates a false independent residual

From PREFIX-1044, E[Y]=6 and U(y)=integral_y^36(6−t)rho(t)dt=integral_0^y(t−6)rho(t)dt. Thus v(0)=0 EXACTLY. This removes the independently rounded primitive constant at the singular endpoint, by an identity about the auxiliary observer rather than a fitted cancellation. Keep all density modes, including the signed sqrt and log branches. Let theta=y d/dy, H=y²(36−y)², P=y(y−36)(17y−91). The inherited contrast 5g/c=4(Hu)'−2Pu+12(11+y)v implies

5g/(cy)=C(y)u+4(36−y)² theta u+12(11+y) integral_0^1(yt−6)u(yt)dt,
C(y)=(36−y)(106+18y)=3816+542y−18y².

In particular, writing A=u(0), the contribution of the constant A is exactly A K(y) with K(y)=3024+536y−12y². If |u−A|<=E0 and |theta u|<=E1 throughout 0<y<=d=1/240, the last display gives the uniform lower bound

5g/(cy) >= 3024 A − (3816+542d+72(11+d))E0 − 5184 E1.

This bound is uniform down to arbitrarily small positive y, unlike independent boxes on v and g. No approximation of the zero endpoint or unbounded iteration is needed.

## 2. Frobenius basis at the singular endpoint, including the resonant logarithm

Write the PREFIX-1035 ODE as sum_(l=0)^3 y^l Q_l(theta)u=0, where

Q0(t)=1152 t²(t−1)²(2t−1);
Q1(t)=−4t³(196t²+59);
Q2(t)=2(2t+1)(14t⁴+28t³+28t²+14t+3);
Q3(t)=−(t+1)^5.

Set R=12/5. Use scaled coefficient series f_alpha(y)=y^alpha sum_(n>=0)b_n(alpha)(y/R)^n, b_0=1, with
Q0(n+alpha)b_n=−sum_(l=1)^min(3,n) R^l Q_l(n+alpha−l)b_(n−l).
At alpha=0 choose b_1=0: the resonant equation has zero right-hand side because Q1(0)=0. For alpha=1/2 or 1 all n>=1 have nonzero denominator.

For a double root alpha=1 introduce e_n=b'_n(1), e_0=0, by differentiating the recurrence. The associated solution is f_L(y)=f_1(y) log(y/Y)+y sum e_n(y/R)^n. The constant Y will be the matching point. This is exact: for parameter alpha near 1 the recurrence gives L f_alpha=Q0(alpha)y^alpha, and both Q0(1),Q0'(1) vanish. Differentiation therefore yields a solution, and subtracting log(Y) f_1 normalizes the logarithm. The differentiated recurrence is
Q0(n+1)e_n=−Q0'(n+1)b_n−sum_l R^l [Q_l'(n+1−l)b_(n−l)+Q_l(n+1−l)e_(n−l)].

The other double root alpha=0 similarly supplies one logarithm with leading log y: the only apparent singularity of the parameter recurrence near alpha=0 is b_1=−R Q1(alpha)/Q0(alpha+1), which has a removable zero because Q1 has a cubic zero and Q0(alpha+1) a double zero. All higher denominators are nonzero in a sufficiently small parameter neighborhood. The recurrence ratios are uniformly bounded there, so the series and its alpha derivative converge locally (a geometric majorant on a small complex alpha circle suffices). Hence the five independent local solutions have successive leading behaviors log y, 1, sqrt(y), y log y, y. Linear independence follows by extracting these orders successively; f_0−1=O(y²), f_half−sqrt(y)=O(y^(3/2)), f_1−y=O(y²), f_L−y log(y/Y)=O(y² |log y|+y²). They span the fifth-order equation on the ordinary positive interval. The inherited boundedness of u at zero rules out only the leading log y solution. The physical branch is therefore exactly

u=A f_0+B f_half+C f_1+D f_L.

This retains the bounded logarithmic mode; dropping it based only on the indicial roots would not be justified.

## 3. All-order rational series and differentiated-tail certificate

For each alpha in {0,1/2,1} compare polynomial coefficients after shifting n=N+z, N=120, z>=0. Put d(z)=Q0(N+alpha+z), p_l(z)=R^l Q_l(N+alpha+z−l). The checker verifies each coefficient d_k>0 and beta=max_k sum_l |p_(l,k)|/d_k<1. Similarly define gamma=max_k (|d'_k|+sum_l |p'_(l,k)|)/d_k, with primes denoting derivatives of the polynomials. Thus the recurrence homogeneous row absolute sum is at most beta for ALL n>=120, and its differentiated inhomogeneous row has sum at most gamma. Exact induction yields |b_n|<=M=max_(N−3<=i<N)|b_i| and, for the alpha=1 derivative, |e_n|<=M_e=max(max_(N−3<=i<N)|e_i|,gamma M/(1−beta)) for n>=N. All three displayed beta diagnostics are 0.9626666666666667. M diagnostics are 3.8518e−33, 3.1301e−32, 1.2060e−31 for alpha=0,1/2,1; M_e is 2.6465e−31 approximately. The bounds used in the checker are exact fractions.

For q=y/R<1 the absolute tail for theta^j of a power mode is bounded by

y^alpha M q^N (N+2)^j j!/(1−q)^(j+1),

because (N+alpha+k)^j<=(N+2)^j(k+1)^j and sum_(k>=0)(k+1)^j q^k<=j!/(1−q)^(j+1). Use M_e for the derivative series. The logarithmic product is differentiated by the Leibniz rule, preserving the additional theta derivative terms. This certifies evaluation over the needed interval without extrapolation from finite sampled signs.

## 4. Rational connection point and interval inverse

Choose Y=1600/841=(40/29)^2, X=4−Y=1764/841=(42/29)^2. Thus both square-root prefactors are exact rational, and log(y/Y)=0 at y=Y. All five theta-jet entries of each of the four zero-side modes are rational-term sums with explicit tails. At Y, theta^k of f_1 log(y/Y) equals k theta^(k−1) f_1, for k>=1; for k=0 it vanishes. This avoids evaluating any logarithm numerically at connection.

The inherited 4-side representation is u=sum_(j=0)^3 Q_j R_j(y−4)−135(4−y)^(3/2) C_4(y−4); use its weights [2356.98,2357.02], [−440.62,−440.59], [68.45,68.48], [−12.44,−12.42], −135. Recompute coefficients through index 100 exactly and apply the PREFIX-1057 inherited uniform tail at X/(5/2)<1 for the first four derivatives. Convert ordinary derivatives to the theta-jet by the exact operator identity. The fifth (k=4) jet is used as a consistency check only.

Let M be the interval matrix of the first four theta-jet rows at Y, columns f_0,f_half,f_1,f_L; w the corresponding observed interval vector. The exact inverse C0 of the rational midpoint matrix is used only as a preconditioner. With beta0=||I−C0 M||_infty<1 verified by outward interval arithmetic, every actual solution x=(A,B,C,D) satisfies x=C0 w+(I−C0 M)x, so
||x−C0 w||_infty<=beta0 ||C0 w||_infty/(1−beta0).
All arithmetic is exact rational or outward-rounded on the grid 10^−30. The actual beta0 upper bound displays as 1.75e−28. The first four rows suffice for uniqueness; fifth row enclosure intersection is checked, not asserted as independent reconstruction of the physical identity.

Outward rounded display enclosures of coefficients (not used as the underlying exact endpoints):
A in [4494.07,4523.87], B in [−1105.30,−1043.00], C in [86.64,116.88], D in [−3.42,5.00].
Exact assertions include 4494<A<4524. Note that the broad inherited connection boxes already suffice, with no tightening of their correlations.

## 5. Uniform lower-end proof and global conclusion

For 0<y<=d=1/240, use sqrt(y)<=1/15 and y log(Y/y)<=7d. The latter follows from Y/d>3>e, monotonicity of y log(Y/y) on (0,d], and Y/d<e^7, with the last comparison certified by the finite Taylor lower bound sum_(j=0)^10 7^j/j!. This is an analytic bound on the auxiliary logarithm, not numerical phase evaluation. At q=d/R define absolute moments of the scaled coefficient series using finite coefficient absolute sums and the proven tails. For f_0−1 omit n=0. For the sqrt, linear and log modes include n=0, and multiply by sqrt bound, d and 7d as appropriate. In the theta derivative of the logarithmic term additionally include f_1. Multiplying by the verified coefficient boxes yields uniform E0<75, E1<38, with tighter diagnostic bounds 74.33218984014184 and 37.51635643211275. Substitution of the exact interval endpoints and exact moment bounds into section 1 gives the exact asserted lower bound >13,000,000, displayed as 13052871.999300368. Thus the whole interval (0,1/240] is certified. No finite grid near zero is used.

The previous certified band [1/240,36) and inherited endpoint values now complete the auxiliary scalar sign theorem. Since y^m(36−y)^k>0 on the interior for every m,k>=0, every E_{m,k}>0 and every D_{m,k}>0 by the inherited Beta identity. No negative interval or negative integer difference exists for this auxiliary model under the inherited identities.

## 6. Executed evidence and continuation

Exact Python/SymPy/Fraction checker actually executed and terminal assertions passed:
    tail 0 beta 0.9626666666666667 B 3.851773771980281e-33 E 0.0
    tail 1 beta 0.9626666666666667 B 1.2059533552134983e-31 E 2.6464015083169135e-31
    tail 1/2 beta 0.9626666666666667 B 3.130098499947106e-32 E 0.0
    inverse residual 1.75e-28 coeff [(4494.070664135854, 4523.8636210181585), (-1105.2984334981008, -1043.0011250734856), (86.64780679976089, 116.87119379696085), (-3.4112515142941264, 4.993144779496707)]
    E0 E1 lower 74.33218984014184 37.51635643211275 13052871.999300368
    PREFIX1058_ZERO_FROBENIUS_BRIDGE_CERTIFICATE_PASSED

Checker: fad76a38601d303d973238cdc46cfb14061f505f:research_notes/portable_direct/PREFIX1058_R6_ZERO_FROBENIUS_BRIDGE_CHECK.py, Git blob 04ece947959945cb5c9cff9ea10c251ec0467600 matches local executed Git object; full remote readback matched. Local SHA256 a1067e4e285b6e04c1d6bba05eb1419668f8ce936a11275d9431c7a5eff67fb9; stdout SHA256 90927d7ee0f9097d21a78b7d4c471df005cf196bd0118ca5207295bf195c6b0b. The Euler/ordinary ODE polynomial identity was independently checked within the script; all tail comparisons, inverse residual, uniform bounds and final positivity assertions used exact rational arithmetic. Floating numbers in logs are diagnostics. No independent review and no formal result admission. The fifth matching row was checked for intersection, not a separate proof of source identity.

Next scientific question: stop extending auxiliary spectral bands (complete conditional proof). Review the chain of inherited scalar identities and all band certificates; extract the endpoint primitive constraint plus resonant-mode certificate as reusable scoped methods. Then investigate the exact signed native BRC/X6 observer correspondence under its BRC-only operation contract; retain joint Cell, terminal port, grade, signed branch, multiplicity and provenance. Determine whether the auxiliary all-order Hausdorff positivity can be transferred and what this would say about B_fix,odd(32), without assuming transfer. No new native computation in this note.

Control: original registration r6-20261123-2358-session-start-own-v1 re-read SUCCEEDED; historical EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322, original activity receipt empty, execution_authorized=false. Current scoped LEASED query r6-20261124-1650-sites-leased-observe-v1 last observed RUNNING/NATIVE_RUNNER, error=null. No current CLAIM or protected task write, no Activity association asserted. Independent auxiliary work preserved without claiming an unrelated task.
