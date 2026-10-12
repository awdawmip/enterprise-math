# Exact coverage argument for the published p17 order1 unit

This argument accompanies only Task RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET. It does not assert a census outcome before actual execution, nor close the original global T6 task.

Let L be the 16-coordinate mixed kernel of sum_s u_s s^(-k)=0 modulo17^k, k=1..6. The frozen integral basis belongs to L and has determinant magnitude17^21. The six-column coefficient matrix is invertible modulo17, hence modulo17^6, so the mixed congruence map is onto the product of groups of orders17,...,17^6. Its kernel index is17^21. Therefore the certified basis spans all of L, including composite-denominator coordinates.

For each admissible r, solve the stronger six-row system modulo17^6 to obtain one representative u0. This construction supplies a point satisfying the original mixed congruences; it does not restrict the full affine coset u0+L to the stronger system. Every complete reconstructed candidate is checked against the original row-specific moduli17^k.

With weights w_s=17s-1, the separate signed budgets imply ||wu||² <= C_r²+2331²=R_r², where C_r=2043-17r. Exact Gram-Schmidt gives ||wu0+sum z_i b_i||²=sum D_i(z_i+c_i)², descending centers c_i=h_i+sum_{j>i}z_j μ_{ji}. Every D_i exceeds the largest R_r². Thus a feasible coordinate can only be floor(-c_i) or ceil(-c_i); at an integer center there is only one choice. Choose the nearer integer as preferred, breaking exact half-integer ties toward the smaller integer.

A nonpreferred choice costs at least D_i/4. Since3 min(D_i)>4 max(R_r²), a feasible path has at most two nonpreferred coordinates. Its index set S must satisfy sum_{i in S}D_i<=4R_r². Given S, descending centers and the fixed tie rule determine a unique path. The complete eligible empty/singleton/pair lists have299 members over the twelve actual-domain classes. Exact partial-norm pruning preserves completeness because all remaining orthogonal contributions are nonnegative. A vanished distinct nonpreferred choice also certifies that the named path cannot be feasible.

Every unpruned complete candidate must satisfy exact weighted reconstruction, the GS/fullnorm identity, all six original congruences and both original weighted side budgets. Certificate or invariant failure aborts the unit and is never recorded as an ordinary rejection or EMPTY. Every locally feasible vector is retained, including vectors rejected by a subsequent named necessary completion cut.

The four r values2,6,12,14 have cofactors19,23,29,31. Their atoms violate maximal-prime17 and receive OUTSIDE_MAXIMAL_P17_DOMAIN. No affine search or relaxed-class EMPTY assertion is made for these rows.

A local survivor has M0=1+sum u_s and Mk=[17(17+r)]^(-k)+sum u_s/(17s)^k. The mixed constraints remove its17-pole. A full collision additionally requires integer multiplicities on17-free denominators with prime factors<=13, all seven moment balances and both residual signed budgets. The displayed completion cuts are necessary only. Higher p17 orders, lower-prime completion and the global threshold remain outside this task.
