# PREFIX-1098 -- Fixed-degree rational sign oracle and certified trillion-scale last-negative brackets

2026-11-26. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / FINITE_EXACT_RATIONAL_CERTIFICATE / NOT_REVIEWED. Continuation of PREFIX-1097 on the same frozen Stage46 double-negative BRC observer. Own recovered metadata EM-DIRECT-780BBE / TASK_RESEARCH, RA-0ABD84561C86E53067DB0322, original registration r6-20261123-2358-session-start-own-v1; own recovery r6-20261126-0852-own-recovery confirms existing SID and no run. Owner read r6-20261126-0852-owner-read-v1 SUCCEEDED/error=null; Source e5df6b9d494cc6df2efb185cc5ced97e9587a845, as_of 2026-11-26T00:53:19.021263Z, LEASED filter empty. No new CLAIM or shared Task mutation.

Frozen scientific input: P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; Stage46 X6 chart O, incoming -e1, reversal signed -5 (phase cover 5q), all other weights 1, next incoming -d, both orientations of Link {O,e1} blocked without renormalization, exactly two negative steps. All native joint Cell equality, sign, phase, port and ordered multiplicity remain in the parent BRC CT carrier. This is a rigorously bounded evaluation of its existing exact radial observer, not a new native propagation or external numerical reference.

Parents:
- 8d25f98107e9602c08ad92e01254d808955431f4:research_notes/portable_direct/2026-11-26_r6_prefix1092_two_anchor_effective_positive_tail.md (weighted distribution norm and C^3 cutoff).
- 08f0330096daa21d866aef04ea1db0c6d4f24384:research_notes/portable_direct/2026-11-26_r6_prefix1095_certified_lower_edge.md (exact density representation, six anchor intervals, Frobenius tail bound).
- 0919218e87c1f6a094123bb19ff315c17846b778:research_notes/portable_direct/2026-11-26_r6_prefix1096_second_order_last_negative_edge.md and 2d373f42f619a15fda899f0d36b62689725b2fed:research_notes/portable_direct/2026-11-26_r6_prefix1096_edge_shift.py (basis/readout construction and predictor).
- 53d572769fe8745d7c60d93b92b28b182dabfa00:research_notes/portable_direct/2026-11-26_r6_prefix1097_effective_monotone_last_negative.md (infinite monotonic cone m>=100000, k>=ceil(107m/5)).
- e7bf78edbfa8bd116ab101ffc0a999b5d21682f0:research_notes/portable_direct/2026-11-26_r6_prefix1098_beta_sign_oracle.py (new standalone reproduction with exact pinned parent dependency, complete readback; integrated remote script not yet independently executed).

## 1. Result and scope

Write D_m(k)=L(x^m(1-x)^k) as in 1097, B=integral_0^1 x^m(1-x)^k dx>0, K=36/(4*36^8*16^3*4^3)>0. The new oracle bounds D_m(k)/(K B) using six fixed degree-350 rational polynomials of t=6 sqrt(x), a single certified square-root beta moment, and a cutoff error. This avoids constructing the high-degree CT integer table or even the enormous normalization factorials. It returns an exact sign when the resulting rational interval excludes zero, otherwise UNKNOWN. A sign interval is not a new claim that the full native state is reconstructible from a scalar.

The sign certificates and 1097's infinite normalized monotonicity imply the following exact integer results (all eight rows satisfy m>=100000 and 5a>=107m):
m             negative a             positive b             inclusive K_last interval
100000        2144102                2144103                [2144102,2144102]
1000000       21440135               21440136               [21440135,21440135]
10000000      214400466              214400467              [214400466,214400466]
100000000     2144003771             2144003772             [2144003771,2144003771]
1000000000    21440036819            21440036820            [21440036819,21440036819]
10000000000   214400367302           214400367304           [214400367302,214400367303]
100000000000  2144003672135          2144003672144          [2144003672135,2144003672143]
1000000000000 21440036720467         21440036720542         [21440036720467,21440036720541]

Proof of bracket: D_m(a)<0, D_m(b)>0; normalization by (1-b_edge)^k preserves signs and is strictly increasing on the entire suffix by 1097. Hence no negative integer at or after b, and a itself is negative. Adjacent endpoints give the exact global K_last without an explicit asymptotic remainder constant. This is finite exact certification of eight rows, not coverage of all intervening m. No direct CT integer table at these scales was constructed.

## 2. Fixed-degree approximation of the exact BRC radial density

Let T=13/10, w=T^2/36, s=(1299/1000)^2/36. Parent 1095 gives on 0<x<=w

    g(x)/K = t^6 F(t) (1-t^2/4)^(-3)(1-t^2/16)^(-3), t=6 sqrt(x).

F is the signed readout of six basis modes. Write F=sum_j theta_j F_j, where theta_j belongs to the parent rational intervals with midpoints c_j and radii r_j; mag_j=|c_j|+r_j. All six independent coefficient enclosures are retained. Reconstruct the degree<=104 basis polynomials F_j,40 from the parent 1096 exact code. For the four nonhomogeneous modes, n=41..200 tails are bounded by absolute coefficients; n>200 by the parent Frobenius 64 T_lambda 2^(-n) bound. In detail, if a=2lambda, rowabs=sum_i,k |N_ik| T^(2k), q=T^2/2, then the mode readout error is bounded by

    E_j = rowabs * [sum_(n=41..200) ||(Z_n,h1_n,h2_n)||_inf T^(a+2n)
                    +64 T_lambda T^a q^201/(1-q)].

The two homogeneous modes have no series tail. Actual rational reconstruction and comparison gives sum mag_j E_j < 1/100000 (about 6.662218714e-6). Each basis polynomial is rounded coefficientwise downward with denominator 10^20, giving rational Q_j; the local error is <1/1000000 per basis since the exact absolute-coefficient error sum at T is below that value. The aggregate absolute basis bound H_F=sum mag_j sum_i |Q_ji|T^i is about 4.087223352626e11, verified <10^14.

For d=4,16 let A_d(t)=sum_(n=0..60) binom(n+2,2) (t^2/d)^n. Put u=T^2/d, J=61. Its uniform positive remainder is bounded by

    eps_d = binom(J+2,2) u^J / (1-u*(J+3)/(J+1)),
    M_d=(1-u)^(-3).

Indeed the successive term ratio from J onward decreases and is at most u*(J+3)/(J+1)<1. Define P_j(t)=t^6 Q_j(t) A_4(t) A_16(t) of degree<=350. Then on [0,w], with the exact unknown coefficients theta_j, the density differs from sum theta_j P_j by at most

    E_loc=T^6[(1/100000+sum mag_j/1000000) M_4 M_16
                      +H_F(eps_4 M_16+M_4 eps_16)].

This is an error bound for g/K. Actual E_loc approx 0.00035941981944738385, verified <1/1000. Retaining the six coefficient uncertainties separately is essential: the earlier single midpoint polynomial paid about 2.9776198 for uniform local error, whereas now the dominant uncertainty can be paid after integration using signed cancellations within each basis. Parent coefficient intervals are not changed or re-anchored.

## 3. Exact beta moment reduction to one square-root observation

Let X have density x^m(1-x)^k/B on [0,1]. With alpha=m+1, S=m+k+2, define rising factorial (a)_j. Integration by parts, also valid for positive half-integer exponents, proves

    E[X^j]=(alpha)_j/(S)_j,
    E[X^(j+1/2)]=E[sqrt(X)] (alpha+1/2)_j/(S+1/2)_j.

Thus E[P_j(6sqrt X)] = A_j+B_j E[sqrt X] with rational A_j,B_j determined by two arrays of consecutive rational ratios, at most 175 steps each. No gamma values, pi, classical trigonometric calculation, or external physical approximation are used. This is an auxiliary integration identity on the existing BRC radial observer.

A universal finite rational bound for the sole unknown moment follows from a binomial polynomial. Set r0=19/90, x0=r0^2, u=(X-x0)/x0 >= -1. For any odd positive integer l, define T_l(u)=sum_(j=0..l) binom(1/2,j)u^j. Then for every u>=-1,

    |sqrt(1+u)-T_l(u)| <= |u|^(l+1).

For -1<=u<=0, every nonconstant binomial-series term has nonpositive sign, and the sum of the absolute coefficients is 1 (by the binomial identity and monotone limit at -1), so the tail is bounded by |u|^(l+1). For u>=0 Taylor's integral remainder is bounded by |binom(1/2,l+1)|u^(l+1)<=u^(l+1), because the magnitude of the relevant derivative decreases along [0,u]. At -1 continuity gives the same bound. With l odd, the error expectation is the exact nonnegative even moment, not a heuristic absolute-moment estimate. With l=15,

    v=r0 sum_(j=0..15) binom(1/2,j) E[u^j],
    e=r0 E[u^16],
    E[sqrt X] in [v-e,v+e].

Every E[u^j]=sum_(i=0..j) binom(j,i)(-1)^(j-i) E[X^i]/x0^i is rational. Consequently set V_j=A_j+B_j v. The integral of the approximating density has center V=sum c_j V_j and radius

    E_int=|sum c_j B_j| e + sum r_j (|V_j|+|B_j|e).

The common square-root error is charged once after combining signed center coefficients. Anchor uncertainty is evaluated on each signed integral, not on the sum of absolute polynomial coefficients. This is a strict enclosure even when all six uncertainties are correlated; it simply contains their entire box.

## 4. Global complement payment without giant powers

Use the inherited C^3 cutoff chi_(s,w), equal to one below s and zero above w. The weighted observer norm with C=(114025897/629856,118208/2187,1637/324,4/27) and cutoff derivative constants R=(1,7,42,420) gives the 1097 bound

    |L((1-chi) f)| <= J(C,s,w) (1+m+k)^3 f(s)/(1-s)^3,
    J=sum_j C_j sum_(i=0..j) binom(j,i) R_i/(w-s)^i,

provided k>=3 and (m+6)/(m+6+k-3)<=s, where f=x^m(1-x)^k. This pays any higher-band distribution, not just a regular-density extrapolation. The cutoff at zero is legitimate by the parent 1075/1092 boundary estimates. Subtract the polynomial integral outside the same cutoff. Each monomial t^j f(x) is decreasing on [s,1] when (2m+350)/(2m+350+2k)<=s, so the absolute polynomial complement is bounded by P_s f(s), where P_s=sum mag_j sum_i |P_ji| (1299/1000)^i. Domain length is <=1. The local difference contributes <=K E_loc B because the cutoff is between zero and one.

To bound f(s)/B without building large factorials, choose rational witness endpoints a=m/(m+k)-1/m, z=m/(m+k)+1/m, check 0<a<z<s. Log concavity of f implies B>=(z-a)min(f(a),f(z)). Hence

    f(s)/B <= (z-a)^(-1) max_(u=a,z) (s/u)^m ((1-s)/(1-u))^k.

Write k=qm+n, 0<=n<m; check p=(s/u)((1-s)/(1-u))^q<=1 and v0=(1-s)/(1-u)<=1. The ratio is p^m v0^n. The actual code computes an upward bound by repeated squaring on the lattice 2^(-256): round the base up, every multiply/square up, then divide by 2^256. Because nonnegative multiplication is monotone, induction proves this bound for arbitrary nonnegative integer exponents; it never uses enormous rational numerator/denominator powers. All admissibility checks are performed for each queried pair; out-of-domain inputs require another certificate rather than an unverified sign.

With U an upper bound for f(s)/B just computed, set

    E_out=U [J(C,s,w)(1+m+k)^3/(K(1-s)^3)+P_s].
    D_m(k)/(K B) in [V-E,V+E], E=E_int+E_loc+E_out.

This completes the new conditional proof of the oracle under the inherited exact observer and density certificates. It keeps both signs of the original residual and explicitly pays the unresolved high-band contribution. The only approximation is the certified scalar observer evaluation, not a replacement of native path information.

## 5. Actual exact calculations

Local independent reconstruction: symbolic 28x7 elimination SHA256 matched the 1095/1096 parent; all 66 Laurent terms and readout degrees reconstructed, all encountered resonant divisions checked, four 201-term rational basis tables generated. Computed series-only error <1e-5, all six basis rounding errors <1e-6. First midpoint-only experiment had local error 2.9776198018622533 and certified 5 adjacent pairs through m=10^9; it was inconclusive at the initial 10^10 probes. Separate coefficient treatment reduced the total normalized radius from about 2.978 to about 0.262619, dominated by the existing anchors. Initial exploratory assertion H_F<4e11 failed; actual H_F=4.087223352626e11, and corrected bound <1e14 was used. Actual degree 350, E_loc=0.00035941981944738385, exact rational calculations. No failed assertion was used as evidence.

For the final eight bracket rows, displayed normalized centers and conservative radii (display rounding only; decisions on exact fractions):
m         center(a)             radius(a)          center(b)             radius(b)
1e5       -57936.14779628348      .262659376414      13313.041720842524      .262658576659
1e6       -6138.203420074148      .262616911880      987.4338525920203       .262616845848
1e7       -245.88095356488094     .262618429575      466.68992786852704      .262618422971
1e8       -12.934164882951459     .262618584647      58.322996285844944      .262618583986
1e9       -3.890955290949988      .262618600286      3.2347615621175345      .262618600220
1e10      -.8489197679356895     .262618601830      .5762236171939299       .262618601817
1e11      -.33094471041341195    .262618601983      .3103698135441374       .262618601977
1e12      -.26489577079807997    .262618601998      .26953299922064616      .262618601993

For m=10^5 through 10^9 both adjacent signs certified at the initial 1096 predictor pair. For m>=10^10 the initial predictor is shifted by accumulated rho uncertainty; a local secant estimate selected new probes, with exact sign comparisons establishing the final brackets. The uncertain position 214400367303 at 10^10 has center approximately -.136348075356, radius .262618601823, so the two-candidate result is genuine. For m=10^11 and 10^12 the final bracket widths 9 and 75 are sufficient certificates, not a claim of optimal information-theoretic width. At 10^12 the ratio outside payment is approximately 6.615e-72; at 10^5 it is about 5.77e-5. Dominant remaining error is anchor uncertainty, not the beta sqrt moment or global complement.

The locally executed oracle used a separate exact reconstruction script and JSON of six rounded bases. The published integrated script reconstructs the same bases directly from the immutable parent 1096 file, checks its SHA256, repeats the tail/rounding checks and verifies all eight pairs. The integrated remote copy was read back byte-for-byte but not itself rerun this turn. Local pair timings after preprocessing approximately .039-.099 seconds for the tested inputs (exploratory timing, no controlled comparison to native CT). No high-m CT table, independent mathematical review, or physical attribution was performed.

## 6. Cost and next

After fixed preprocessing, for bounded k/m the two 175-step moment arrays and six fixed polynomial contractions have fixed arithmetic operation count; the two 256-bit upward exponentiations require O(log(m+k)) multiplications. Rational input/output bit lengths of fixed-degree moments grow O(log(m+k)) plus fixed coefficient lengths (ordinary rational sum/product complexity must still be charged; this is not constant bit time). The normalization B is never evaluated. Precision and degree are fixed here; for larger scales or near-integer roots the error may exceed the sign, so a general uniform exact-sign complexity bound is open. The existing monotonicity suffices to turn any certified opposite-sign pair into a global integer bracket.

Next: sharpen the six anchor coefficients with the original exact moment system, including correlated rather than independent coefficient errors; increase fixed-point exponent precision only when its contribution matters. Then repeat the three unresolved high-m brackets and investigate a precision-versus-scale bound for the oracle. The smaller-m activation threshold, full lower-band sign classification, independent review of parent certificates, and mother B_fix,odd(32), p,d remain open. Do not regenerate high-order CT tables for the five closed rows or redo the 1095 root isolation without new precision evidence. No Result freeze, review, Working Truth or task closure asserted.
