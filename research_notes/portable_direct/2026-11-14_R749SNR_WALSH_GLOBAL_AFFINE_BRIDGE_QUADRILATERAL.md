# R749SNR — Enlarged two-parameter Walsh zero-calibration quadrilateral via one affine residual bridge

Date: 2026-11-14. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. Scope: frozen auxiliary 16-state Walsh source observer, scientific input awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This result is not a native X6, signed-Port, V29, or V39 future-observer mapping. It does not modify P000.

## Precise model and theorem

Let G=F_2^4 and chi_m(x)=(-1)^popcount(m & x). Retain ten Walsh moments at masks B={3,5,6,7,9,10,11,12,13,14}, fix m_3=t and m_12=s, and fix the other eight retained moments at zero. The compatible probability fiber F(t,s) consists of all 16-point laws with these moments. Put TV(mu,q)=sum_x |mu(x)-q(x)|/2, rho(t,s)=min_{q probability}max_{mu in F(t,s)} TV(mu,q), and rho_cal(t,s)=min_{q in F(t,s)}max_{mu in F(t,s)}TV(mu,q).

Let the new bridge triangle be

N=conv{ B=(7/10,3/20), E=(1/2,3/10), F=(1,0) }
 ={(t,s): 30t+40s>=27, 3t+5s<=3, t+2s>=1}.

**Theorem.** For every real (t,s) in N,

rho(t,s) = rho_cal(t,s) = (3+t-s)/8.

The explicit *calibrated* minimax center is

q_{t,s}(x)=[1+t chi_3(x)+s chi_12(x)+eta(t,s) chi_15(x)]/16,
eta(t,s)=(3t+5s-3)/2.

The bridge has area 3/400. Combine it with the previously certified R749SNO triangle

T=conv{E=(1/2,3/10), C=(3/5,2/5), F=(1,0)}.

Their common side is EF, i.e. 3t+5s=3, on which eta=0. Their union is the convex quadrilateral

Q=conv{(7/10,3/20),(1/2,3/10),(3/5,2/5),(1,0)},

whose area is 19/400 (previous T area: 1/25=16/400). Thus zero calibrated-minimax penalty holds throughout Q for all real parameters. A single continuous piecewise-affine center suffices: choose eta(t,s)=(3t+5s-3)/2 on N, and eta(t,s)=0 on T.

R749SNQ, PR #2341, separately established a smaller bridge triangle conv{(7/10,3/20),(7/10,1/5),(4/5,1/5)}. All three of its vertices belong to Q, so this result contains and extends that certified region; its distinct new content is the much larger triangle N and the global quadrilateral Q. The former R749SNP one-dimensional repaired segment is not claimed to be contained in Q in its entirety.

## Seven-coefficient source parameterization

Put A=chi_3, D=chi_12, H=chi_15=AD, U=chi_1, AU=chi_2, V=chi_4 and DV=chi_8. Each compatible source has the unique inverse-Walsh expression

mu(x)=[1+t A(x)+s D(x)+h H(x)+u U(x)+v AU(x)+w V(x)+z DV(x)]/16,

with (h,u,v,w,z) satisfying the 16 atom nonnegativity inequalities. The chosen center sets (h,u,v,w,z)=(eta(t,s),0,0,0,0), so it automatically satisfies all ten prescribed moments. At the three parameter vertices of N it is nonnegative (at B it agrees with the R749SNP repaired center; at E and F it agrees with the R749SNO center). Because it is affine in (t,s), nonnegativity and total probability one hold everywhere in N. This certifies q_{t,s} in F(t,s).

## Lower bound for all unrestricted prediction centers

Xor translations by masks 3 and 12 preserve F(t,s). The average of any prediction law q under the four translations is a probability law supported on the character span {1,A,D,H}; the convex, translation-invariant worst-case TV risk cannot increase under averaging. Hence the unrestricted minimax can be represented by an invariant center.

For each (t,s) in N construct the explicit compatible source W(t,s) having free coefficients

(h,u,v,w,z)=(0,s-1,-t,-s,-s).

W is affine and has nonnegative atoms at the three vertices B,E,F (directly tested with exact fractions in the companion checker); hence W is feasible for every real (t,s) in N.

For the fixed event S={3,5,7,9,11,13,14,15}, the Walsh sums of A,D,H over S all vanish. Thus any invariant probability center q has q(S)=1/2, while exact summation shows W(t,s)(S)-1/2=(3+t-s)/8. The variational TV event inequality proves

rho(t,s) >= (3+t-s)/8,

and the calibrated radius has the same lower bound. This lower bound does not presume that q lies in the source fiber.

## Exact upper certificate for all real parameters

Let y=20(t,s,h,u,v,w,z). The joint source-and-parameter polytope in seven coordinates is defined by the 16 atom inequalities

(A,D,H,U,AU,V,DV) dot y >= -20

and three exact parameter inequalities

(30,40,0,0,0,0,0) dot y >= 540,
(-3,-5,0,0,0,0,0) dot y >= -60,
(1,2,0,0,0,0,0) dot y >= 20.

The polytope is bounded and has full seven-dimensional interior; every vertex is the intersection of seven independent active constraints. The companion standard-library Python program exhausts all choose(19,7)=50,388 possible seven-facet combinations, performs exact integer Bareiss elimination, reconstructs Fraction solutions, tests all 19 inequalities exactly, and deduplicates the feasible vertices.

Exact output: 29,584 nonsingular bases, 4,812 feasible bases, 86 distinct rational vertices. At each such vertex it evaluates

Delta=TV(mu_{t,s,h,u,v,w,z},q_{t,s})-(3+t-s)/8.

Precisely 28 vertices attain equality and zero violate the upper bound. The exact maximum excess is 0. Because Delta is convex in the entire joint seven-coordinate vector (TV of the difference between two *affine* laws, minus an affine target), it attains its maximum on the compact polytope at a vertex. Thus Delta<=0 for every real admissible parameter and every compatible source in N.

Together with the unrestricted lower witness this proves the stated exact equality of both minimax radii throughout N. On T use the separate existing R749SNO exact theorem and q0 certificate; the centers coincide on the shared EF edge, giving the quadrilateral corollary without assuming that arbitrary unions of minimax fibers convexify.

## Adjacent exact obstruction for *this affine decoder*, not for zero calibration

The affine formula eta(t,s)=(3t+5s-3)/2 cannot be extrapolated without a new certificate. At the exterior point (t,s)=(7/10,1/10) it gives eta=-1/5. The explicit feasible source with free coefficients (h,u,v,w,z)=(0,9/10,7/10,1/10,1/10) has

TV(mu,q_eta)=37/80 > (3+t-s)/8 = 9/20,

an exact excess 1/80. The companion script verifies this in rational arithmetic. This is a counterexample to the *specific extrapolated affine center*, not to the minimax theorem: the earlier R749SNP result has already proved rho=rho_cal=9/20 at that same point with a different center. Thus the obstruction identifies a genuine center-selection boundary but does not assert a positive calibration gap.

## Reproduction, provenance, limits, next question

Run: python research_notes/portable_direct/R749SNR_WALSH_GLOBAL_AFFINE_BRIDGE_EXACT_CHECK.py

The companion results JSON records PASS, the frozen scientific input pin, all 50,388 combination counts and witnesses; the code uses integer arithmetic and Python Fraction only. No floating-point enumeration is used in the published certificate. Preliminary numerical exploration is not used as proof.

Independent author contributions: R749SNO (PR #2339) for T, R749SNP (PR #2339) for repaired line, and R749SNQ (PR #2341) for an independently saved smaller bridge. This research is a stronger new *auxiliary-model* theorem; it is neither a native X6 task CLAIM nor a scientific review or Foundation promotion.

Next: attempt an exact upper-envelope characterization of the zero-calibration boundary outside Q and the original R749SNP line, specifically the domain adjacent to segment B->E where a single affine residual center fails. Construct either a new polyhedral chamber with its own exact dual/vertex certificate or a genuine positive calibration gap with an explicit optimum on both prediction classes.
