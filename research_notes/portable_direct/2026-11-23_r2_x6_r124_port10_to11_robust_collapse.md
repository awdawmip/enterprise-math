# X6 R124 — Exact eight-to-one Port collapse and a four-weight stability chamber

Date: 2026-11-23 (Asia/Shanghai). Mathematical state: AUTHOR_PROOF / EXACT_INTEGER_REPLAY_PASS / NOT_INDEPENDENTLY_REVIEWED. The theorem concerns the conditional four-positive-weight, six-pair BRC observer, not native P000/X6 time dynamics; the frozen scientific input remains unchanged.

## Definition and new conclusions

For any nonzero integer triple a=(x,y,z) modulo sign only (positive multiples are distinct), let q(a) be the maximum of its positive-coordinate sum and the absolute negative-coordinate sum. Set

\[
h(a)=(0,\ x+3y+6z,\ 3x+12y+30z,\ 7x+39y+126z),\quad
F_w(a)=\max_{0\le i<j\le3}\frac{|h_i(a)-h_j(a)|}{w_i+w_j}.
\]

Here w=(A,B,C,D)>0 consists of four positive real weights. Let eta_p(w) be the least F_w(a) over 0<q(a)<=p, and N_p(w) consist of the sign-unoriented triples in that range satisfying the **strict** inequality F_w(a)<3eta_p(w)/2.

**Theorem A.** At w0=(1,3,4,18), the optimum at Port 10 is 11/19, and its strict-near set consists of exactly eight vectors, modulo sign:

(1,-3,1), (1,0,0), (4,-1,0), (5,-4,1), (5,-1,0), (6,-4,1), (9,-5,1), (9,-2,0).

For **every integer Port p>=11**, the exact optimum is **1/4**, and the complete near set is the **singleton +/- (10,-5,1)**. Thus increasing Port from 10 to 11 causes the count to drop **8 to 1**, and it stays 1 for every larger Port. In the entire nonzero integer lattice, every vector other than +/- (10,-5,1) has score at least 1/2. The second-score bound is sharp at (20,-10,2), of Port 22.

**Theorem B.** The same eight-to-one transition, simultaneously for Port 10 and *all* integer Ports p>=11, holds in the open four-dimensional weight box

\[
|w_i-(w_0)_i|<(w_0)_i/362\quad\text{for all four channels}.
\]

The singleton assertion at all p>=11 separately holds in the larger **closed** box |w_i-(w0)_i| <= (w0)_i/7. These are sufficient stability radii, not claims of optimality.

## Proof of the unbounded integer isolation

At w0, the six pair capacities 01,02,03,12,13,23 are (4,5,19,7,21,22). Suppose a nonzero integer vector a has F_w0(a)<1/2. From pair 01, |h1|<2, so h1=k belongs to {-1,0,1}. From pair 02, |h2|<5/2; because h2=3(x+4y+10z) is divisible by three, h2=0. Solving the two integer equations h1=k, h2=0 yields

\[
x=6z+4k,\qquad y=-4z-k,\qquad h_3=12z-11k.
\]

The 03 bound gives |12z-11k|<19/2, equivalently |12z-11k|<=9. For k=0, only z=0 is possible, hence the zero vector (excluded). For k=1, only z=1 is possible, hence (x,y,z)=(10,-5,1); for k=-1 only z=-1 is possible, hence its negative. The survivor has h=(0,1,0,1), six gaps (1,0,1,1,0,1), score 1/4 and q=11. Twice it has score 1/2 and q=22 by integer homogeneity. Thus the first two lattice scores are 1/4 and 1/2, and the strict near cutoff for all p>=11 is 3/8. This proves the unbounded Port statement without extrapolating finite enumeration.

## Proof of the uniform weight-stability box

For 0<=rho<1, suppose |w_i-(w0)_i|<=rho*(w0)_i. All six positive pair denominators scale between factors 1-rho and 1+rho. Therefore

\[
F_{w_0}(a)/(1+\rho)\le F_w(a)\le F_{w_0}(a)/(1-\rho)
\]

for every integer a, and the same bounds hold for eta_p by taking minima over a Port-independent feasible set.

The complete Port-10 rational enumeration gives eta10(w0)=11/19 and strict cutoff 33/38. The **largest inside** score is 19/22; the **smallest outside** score is 18/19. Every inside vector remains inside when

\[
(19/22)/(1-\rho)<(33/38)/(1+\rho)\iff\rho<1/362,
\]

and every outside vector stays outside when

\[
(18/19)/(1+\rho)\ge(33/38)/(1-\rho)\iff\rho\le1/23.
\]

These both hold for rho<1/362, proving stability at Port 10. At every Port p>=11 the unbounded integer gap implies F_w(a)>= (1/2)/(1+rho) for any competitor a distinct from +/-a0, while F_w(a0)<=(1/4)/(1-rho). The former is >=(3/2) times the latter whenever rho<=1/7. Thus the singleton persists in the larger closed box, and the common open box supports the full transition.

## Finite exact evidence and provenance

The independent local replay (JavaScript BigInt rational cross-products plus Python Fraction crosscheck) reconstructs all six pair gaps over all **1,935**, **2,541**, and **18,997** sign-unoriented integer vectors at Ports 10, 11 and 22, respectively. Minimum scores are 11/19, 1/4, 1/4; complete near counts are 8, 1, 1; the Port-10 maximum near score and minimum outside score are 19/22 and 18/19. The finite run verifies these domains; the preceding elimination certifies the infinite one. Reproducible program and output are companion files named x6_r124_port10_to11_stability_verify.js and x6_r124_port10_to11_stability_results.json.

Frozen exact observer input: [R121](https://github.com/awdawmip/enterprise-math/blob/8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd/research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md). The eight-vector Port-10 witness was already published in [R123](https://github.com/awdawmip/enterprise-math/blob/07a10b16c8ee89ecbb6f2d99c1376be062f2b72b/research_notes/portable_direct/2026-11-23_r2_x6_r123_port2_sharp_port10_eight_witness.md); the independent [all-Port simultaneous-maxima result](https://github.com/awdawmip/chatgpt-global-knowledge/blob/2e6278dc712114e795d216a62b6c71d139701fd5/journal/enterprise-math/2026-11-23/x6-r123-small-port-simultaneous-maximum-results.json) is already complete. R124 adds an explicit **unbounded global isolation proof** and the **four-weight open stability chamber**, not a re-proof of the maxima.

Next question: determine the **sharp** four-weight stability boundary, beyond this sufficient relative box, and investigate globally isolated Port transitions in the other three Port-10 maximizing sets. Native R063 remains separate. This portable note is authored research, not a formal CLAIM/Result/Review or independent review.
