# PREFIX-1048 — Explicit positive upper spectral band from a Frobenius coefficient majorant

Date: 2026-11-24 Asia/Shanghai. Parent: PREFIX-1047. Status: AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_SYMBOLIC_CROSSCHECK / NOT_REVIEWED.

## Inputs and actual result

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Stage46 W=J12−6I12, incoming −e1, both directions excluded on Link {0,e1}, exactly one outgoing negative step; retain full X6 Cell–terminal-port–grade observer, signs, multiplicities, provenance, branch order and residual. This paper continues only the inherited auxiliary scalar observer, NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new classical reference run or native BRC propagation, no numerical phase or π evaluation. Symbolic ODE identities and rational proof bounds only.

Sources:
- PREFIX-1035 ebccbb436685bafe6d697ace256ad93b39c0c50f:research_notes/portable_direct/2026-11-23_r6_prefix1035_six_phase_picard_fuchs_frobenius.md (fifth-order scalar ODE, contrast identity).
- PREFIX-1044 8d29f3214a82ed34830beb11b8f64478bfccfa2c:research_notes/portable_direct/2026-11-24_r6_prefix1044_exact_edge_density_and_beta_rays.md (unique nondegenerate maximum in the inherited six-phase scalar model, c>0 edge density and Morse chart).
- PREFIX-1047 44d334c43838b26d86919b2022190c3a0b9ec467:research_notes/portable_direct/2026-11-24_r6_prefix1047_beta_variation_diminishing_and_unique_zero_transport.md (latest same-line predecessor; actual sign question).
- PREFIX-1041 7bcaa3dc08c01119b661f0f9ecc31ca7fa7ba806:research_notes/portable_direct/2026-11-23_r6_prefix1041_effective_beta_positive_cones.md (existing global bound, not needed for the new spectral band).

Theorem. With the inherited auxiliary density and contrast, and c the positive upper-edge density coefficient of PREFIX-1044, the following strict, explicitly bounded positivity holds:
\[
\boxed{321/10\le y<36\quad\Longrightarrow\quad
g(y)>1000c(36-y)^{5/2}>0.}
\]
At y=36, g(36)=0. This is a 39/10-wide certified band of the actual auxiliary spectrum; the earlier edge theorem only gave an unspecified positive radius. No numerical integration or unknown truncation constant is involved.

## 1. Frobenius equation in the edge deficit

Put x=36−y, D=x d/dx. Write the inherited spectral ODE as sum a_j(y) rho^(j)=0. Direct expansion of the PREFIX-1035 Euler polynomials gives, after division by y^2, the coefficients from j=0 through 5:
\[
\begin{array}{ll}
a_0/y^2=-(y-6),&
a_1/y^2=-(31y^2-516y+1020),\\
a_2/y^2=-6(15y^3-406y^2+2078y-1152),&
a_3/y^2=-y(65y^3-2408y^2+19836y-27648),\\
a_4/y^2=-5y^2(3y^3-140y^2+1568y-3456),&
a_5/y^2=-y^3(y-36)(y-16)(y-4).
\end{array}
\]
After multiplying by x^4 and changing variables (d/dy)^j=(-1)^j x^{-j}(D)_{\underline j}, this is the polynomial Euler equation
\[
\sum_{k=0}^5 x^k P_k(D)\rho(36-x)=0,
\]
where operators act before multiplication by x^k and
\[
\begin{aligned}
P_0(L)&=-14929920 L(L-3)(L-2)(L-1)(2L-3),\\
P_1(L)&=15552 L(L-2)(L-1)(316L^2-632L+437),\\
P_2(L)&=-432L(L-1)(2L-1)(368L^2-368L+409),\\
P_3(L)&=4L(2536L^4+2903L^2+216),\\
P_4(L)&=-2(2L+1)(40L^4+80L^3+98L^2+58L+15),\\
P_5(L)&=(L+1)^5.
\end{aligned}
\]
These finite algebraic identities can be checked by expanding each a_j and using the falling factorial formula above. The noninteger indicial exponent is 3/2. Thus the normalized formal solution rho(36-x)=c x^{3/2} A(x), A(x)=sum b_n x^n, b_0=1, satisfies
\[
 b_n=-\frac{\sum_{k=1}^{\min(5,n)}P_k(3/2+n-k)b_{n-k}}
 {P_0(3/2+n)}\quad(n\ge1).
\tag{1}
\]
All denominators are nonzero.

## 2. All-index coefficient majorant (not extrapolation from finite coefficients)

Write L=3/2+n-k>=3/2. For k<=n the ratio |P_k(L)/P_0(L+k)| is bounded, respectively for k=1,...,5, by
\[
(R_1,R_2,R_3,R_4,R_5)=(1/6,1/90,1/1000,1/20000,1/1000000).
\tag{2}
\]
To verify: for k=1 cancel L(L-1)(L-2) (none zero on the half-integer lattice). The remaining ratio is (316L^2-632L+437)/(960(L+1)(2L-1))<=158/960<1/6, using L>=3/2. For k=2 cancel L(L-1), then use (2L-1)/(2L+1)<1 and 368L^2-368L+409<=368L^2 to obtain 368/34560<1/90. For k=3 cancel L and bound (L+3)(L+2)(L+1)(2L+3)>=2L^4. The numerator polynomial divided by L^4 is <=2536+2903(4/9)+216(16/81)<4000. Hence the ratio is <8000/14929920<1/1000. For k=4, (2L+1)/(2L+5)<1, the other four denominator factors dominate L^4, and 40+80(2/3)+98(4/9)+58(8/27)+15(16/81)<160. Thus ratio <320/14929920<1/20000. For k=5 every denominator factor dominates L+1 and ratio <1/14929920<1/1000000.

Since sum_{k=1}^5 4^k R_k<1, induction on (1) first gives |b_n|<=4^{-n} for all n>=0. The following exact initial coefficients sharpen this substantially:
| n | b_n |
|---|---|
| 1 | 1/24 |
| 2 | 5/3456 |
| 3 | 751/15676416 |
| 4 | 2887/1839366144 |
| 5 | 1334491/25824700661760 |
| 6 | 19234751/11156270685880320 |
| 7 | 24252679/413796221803560960 |
| 8 | 410875009/201677912411335557120 |
| 9 | 41097540797/566311578051030244392960 |

Each is obtained by (1); for n=5,...,9 directly 4^n |b_n|<1/18000. For n>=10, all predecessor indices in (1) are >=5. Using (2) and the same weighted sum proves the stronger uniform tail
\[
\boxed{|b_n|\le (1/18000)4^{-n}\qquad(n\ge5).}
\tag{3}
\]
This is a bound on all coefficients, not an assumption of their positivity.

## 3. Why this series is the actual inherited density near the edge

The unique nondegenerate maximum of the existing scalar model is established in PREFIX-1044. Its smooth five-dimensional Morse chart gives, by radial integration of the smooth chart Jacobian, a complete expansion of the density in powers x^{3/2+n}. Odd Taylor degrees integrate to zero on the sphere. The expansions can be differentiated any fixed number of times: take a sufficiently high smooth Taylor order before radial integration, also for the required derivatives. The leading coefficient is the inherited c>0. Inserting these expansions in the Euler equation determines their normalized coefficients uniquely by (1). In particular no independent integer-exponent mode may be added without contradicting the all-order Morse expansion.

For completeness this argument need not assume convergence of the smooth chart's Taylor series. The majorant above guarantees convergence of A(x), with termwise derivatives, for |x|<4, and equation (1) verifies that c x^{3/2} A(x) solves the ODE there for x>0. The difference from the actual density has all differentiated asymptotic coefficients zero. The difference's Euler-state vector Z=(r,Dr,...,D^4r) obeys x Z'=M(x)Z with M analytic and bounded near zero, because the leading D^5 coefficient of P_0 is nonzero. If Z were nonzero at small epsilon>0, the elementary linear-system norm estimate would give |Z(epsilon)|<=|Z(x)|(epsilon/x)^C for some finite C and every 0<x<epsilon. Flatness to arbitrary powers forces the right side to zero. Hence the difference is identically zero near the edge. Ordinary ODE uniqueness extends this equality throughout 0<x<4, as the nearest other singularity is x=20. This identifies the actual density, rather than an arbitrary local Frobenius solution.

## 4. Positive band with explicit margins

For 0<=x<=39/10 put t=x/4<=39/40. The tail (3) gives
\[
\left|\sum_{n\ge5}b_n x^n\right|
\le \frac{1}{18000(1-t)}\le1/450,\quad
\left|\sum_{n\ge5}n b_n x^n\right|
\le\frac{t}{18000(1-t)^2}<4/45.
\]
The first four coefficients are positive; bound them above by 1/24, 1/600, 1/20000, 1/600000. Using x<=4 gives
\[
99/100<A(x)<6/5,\qquad |x A'(x)|<1/3.
\tag{4}
\]
Indeed the upper bound for A is 1+1/6+16/600+64/20000+256/600000+1/450<6/5. The derivative bound is 1/6+32/600+192/20000+1024/600000+4/45<1/3. The lower bound follows from positivity of the first four terms and the tail >=−1/450.

Use the exact inherited contrast
5g=4(H rho)'−2P rho+12(11+y)U,
H=y^2(36−y)^2, P=y(y−36)(17y−91), U(y)=int_y^36(6-s)rho(s)ds.
Substitute rho(36−x)=c x^{3/2}A(x) and rescale the U integral. The exact identity is
\[
\begin{aligned}
\frac{5g(36-x)}{c x^{5/2}}={}&
(36-x)(538-12x) A(x)-4(36-x)^2 x A'(x)\\
&-12(47-x)\int_0^1(30-xv)v^{3/2}A(xv)\,dv.
\end{aligned}
\tag{5}
\]
For 0<x<=39/10, apply (4) to x and xv; 36−x>=32, 538−12x>=490. The first term is >32*490*99/100. The derivative term is bounded below by −4*1296/3. The integral contribution is bounded below by −12*47*30*(2/5)*(6/5). Thus the right side of (5) is strictly greater than
\[
32\cdot490\cdot99/100-4\cdot1296/3-12\cdot47\cdot30\cdot(2/5)\cdot(6/5)
=28368/5>5000.
\]
This proves the theorem. In particular the interval [321/10,36) contains no zero, negative region or even-order touch of this inherited scalar contrast. The proof leaves the density coefficient c symbolic (positive by the prior result); no numerical evaluation of it is necessary.

## 5. Exact validation and next problem

Local SymPy symbolic expansion checked all six Euler polynomials from PREFIX-1035, and recurrence (1) generated the nine displayed rational coefficients. Exact integer/Fraction comparisons checked sum 4^k R_k<1, all five tail base cases, the rational inequalities of (4), and final margin 28368/5. Reproduction: expand theta^j using theta(y^m d^m)=m y^m d^m+y^{m+1}d^{m+1}; insert the six a_j in sum (-1)^j (a_j(36−x)/(36−x)^2) x^{4-j}(L)_{\underline j}, expand and collect x; apply (1), then (2)–(5). The induction and ODE uniqueness arguments, not the finite crosscheck, give the infinite-index and interval claims. No new classical model evaluation, Bessel sampling, phase calculation, native BRC experiment or independent review was performed.

Scientific next: extend this certified edge band toward y=16 using a less coarse recurrence majorant or overlapping regular ODE interval enclosures with rigorously propagated rho,...,rho^(4),U. Preserve the actual branch matching and sign margins. Remaining scalar sign problem outside the certified intervals, full native signed BRC observer correspondence and mother B_fix,odd(32) in {19,20} are open.

Control provenance: prior LEASED query r6-20261124-0550-leased-observe-v1 succeeded, fixed snapshot as of 2026-11-23T21:52:04.192737Z, empty filtered tasks, execution_authorized=false. Fresh scoped owner read r6-20261124-0652-leased-observe-v1 was submitted. Original r6-20261123-2358-session-start-own-v1 SUCCEEDED, EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Account-scoped own recovery metadata r6-20261124-0655-own-recovery-read-v1 shows open underlying SID, no runs, no execution authority. Historical registration is preserved, not a fresh logical-conversation authorization. Independent portable scientific note; no CLAIM, formal PROGRESS, Result or Activity mutation. Current norm read snapshots global main@1803152ee2755f51a7633ce62b74ad579ca1af47 and project main@42390b17ba87b11705d2824981d52811e5efc52d; frozen science pin unchanged.
