# EC49FWO supplement — Sharp fixed local-probe complexity for blind CRT mass resolution

**Date:** 2026-11-22 (Asia/Shanghai). **Scientific pin:** BRC16943; auxiliary static CRT product model. Depends on the companion EC49FWO mass-inverse theorem. **Status:** AUTHOR_PROVED / EXACT_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Theorem

Let n>=1 and q>=3 be coprime positive integers with q odd. Let the unknown support W=U×V⊆(Z/n)×(Z/q), where U,V are **nonempty Boolean subsets**. Observe the entire **indexed** reflection-defect array Δ_W(a,b). In addition, one may select in advance a fixed set Q of physical Boolean membership probes W(a,b). The objective is to recover the total mass N=|W| and hence (by the companion EC49FWO theorem) both factor sizes, the full odd-factor support V, its hole count and hole positions, and K_U, for **every** such product.

The exact minimum number of fixed position probes is

r(n,q) = 1 when n is odd; and r(n,q) = n/2 when n is even.

For odd n, *any* single position suffices. For even n=2m, choose any b0∈Z/q and one a-coordinate from each antipodal pair {i,i+m} in Z/n. The m positions (a,b0) suffice. No smaller fixed set of physical positions works uniformly.

This concerns the recovery of N,V,K_U, not necessarily original signed membership of U. All indexed defects are retained; a local-probe count is not a replacement for their measurement cost.

## Proof

Write M=nq and K_W(c)=|W∩(c−W)|. If W and W' have identical Δ, then Σ_c Δ=2N(M−N) gives N'=N or N'=M−N. In the same-mass case, the companion exact inverse theorem already shows they yield equal V and K_U. We therefore only need to distinguish the different-mass case.

**Case 1: n odd.** Since M is odd, if N'≠N then K_W'(c)−K_W(c)=N'−N=M−2N is odd for every center c. For any subset S of an odd-order cyclic group, ordered off-diagonal pair sums cancel modulo two, and K_S(2x) mod 2=1_S(x). Thus W'(x)=1−W(x) at every physical location. Any one probe distinguishes the candidate masses. At least one is necessary because when U=Z/n and V is a nonempty proper subset of odd Z/q, W and its complement are distinct nonempty CRT products with identical Δ and different N.

**Case 2: n=2m even, upper bound.** Let K_W(a,b)=K_U(a)K_V(b). If W,W' have the same Δ but N'≠N, then

K_U'(a)K_V'(b) = K_U(a)K_V(b) + d, with d=N'−N≠0.

Both matrices have rank one. Every 2×2 minor of the right side equals, up to row/column ordering, d·(K_U(a1)−K_U(a2))·(K_V(b1)−K_V(b2)). Hence either K_U is constant or K_V is constant. For any nonempty Boolean subset S of a finite cyclic group, K_S constant forces S to be the entire group: all nontrivial Fourier coefficients of 1_S have square zero, so 1_S is constant.

If U is full, K_W is constant in a. So K_W' and K_U' are likewise constant in a; U' is full. The n-factor is identical in both products, and Δ_V'=Δ_V. As |V'|=q−|V|, we have K_V'(b)−K_V(b)=q−2|V|, an odd constant. The odd-group diagonal parity rule yields V'=V^c. Thus the two products differ at every (a,b), including at any probe in Q.

If V is full, then V' is also full and Δ_U'=Δ_U with |U'|=n−|U|. At each antipodal pair {x,x+m}, the parity identity is

K_U(2x) mod 2 = 1_U(x) ⊕ 1_U(x+m),

and similarly for U'. Since K_U'(c)−K_U(c)=n−2|U| is even, the antipodal XOR is the same for U,U'. If U and U' agreed on one representative from each antipodal pair, this XOR would force them to agree on both positions of every pair, contradicting the different masses. At least one of the m chosen (a,b0) therefore differs; here V=V'=full, so it is directly observed.

**Even-n lower bound, n>=4.** Let n=2m with m>=2, and suppose Q contains fewer than m physical positions. One antipodal first-coordinate pair P={i,i+m} is unprobed. Choose U with exactly one representative from each of the other m−1 antipodal pairs and neither point of P. Let E=P and T=U∪E. Define e=1_E and u=1_U. Then u(x)+u(x+m)=1−e(x), and for each z,

(u*e)(z)=u(z−i)+u(z−i−m)=1−e(z−i), while (e*e)(z)=2e(z−i).

Consequently K_T−K_U=2u*e+e*e=2 at every reflection center, while |T|−|U|=2, hence Δ_T=Δ_U. Choose V=Z/q. Both products U×V and T×V are nonempty, have equal indexed Δ_W (indeed Δ_W=qΔ_U) and different masses by 2q. They differ only where the first coordinate belongs to P, none of which Q measures. Therefore every fixed Q of fewer than m probes fails.

**Even-n lower bound, n=2.** At least one is needed by the same nonempty complement-product construction as in the odd case. The upper bound is one. QED.

## Exact checks

A separate integer-only verifier exhaustively constructs all nonempty CRT products and all shorter fixed-probe sets for n,q=(4,5), (6,5), (8,3), (10,3). Counts of products: 465, 1,953, 1,785, 7,161. All tests pass, with exact minimum probes 2,3,4,5. Additional odd-n checks (n,q)=(1,5), (3,5), (5,3) confirm a single probe. The (10,11) lower-bound witness has masses 44 and 66 and differs only at antipodal first coordinates {0,5}. The proof covers all stated moduli.

## Information boundary and next problem

The proven minimum is for **fixed membership probes in addition to a complete indexed static reflection-defect array** on unrestricted nonempty Boolean CRT product supports. The frozen P10 support family is smaller, and its own exact probe minimum may improve; determine that separately from its actual frozen input. For native moving-Farey dynamics, a future-operation observer-safety certificate is still needed before treating any such projection as a sufficient evolving state.
