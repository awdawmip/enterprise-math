# R284AX — One exact scalar reading from simultaneous star Port edits

Date: 2026-11-19. Scientific status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Lineage: R284AT → R284AU-PACK → R284AW. Frozen input pin from R284AT: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. This is an auxiliary independently named Port determinant observer, not a new native X6 dynamics assertion.

## Model and theorem

Let n≥2, H≥1 be known, and let the unknown C=(c_ij) belong to {1,...,H}^{n×n}. **In one observation**, the instrument can choose an integer diagonal D and simultaneously modify all n−1 ordered entries in row 0, with independently prescribed nonnegative integer strengths z_v. It reads the exact integer

    y = det(D − C − Σ_{v=1}^{n−1} z_v E_{0v}).

**AX1.** There exist deterministically computable D,z_1,...,z_{n−1} depending only on n,H such that this *single scalar reading* uniquely identifies C. Settings, response, arithmetic, and reconstruction use polynomial bit complexity in n and log(H+1).

**Instrument distinction:** Simultaneous star edits are allowed in this theorem. R284AW's n−1 optimal scalar readings concerned *at most one* edited entry per reading; its lower bound remains valid in that instrument model.

## Algebraic proof

Define F(d)=det(diag(d)−C), and G_v(d)=det(diag(d)−C−E_{0v})−F(d). Every permutation determinant term chooses exactly one entry from row 0. Hence, as an identity of polynomials in all d_i,z_v,

    det(diag(d)−C−Σ_v z_v E_{0v}) = F(d) + Σ_v z_v G_v(d).                 (1)

In particular, all possible quadratic cross terms in the z_v vanish.

Use the previously proved R284AU-PACK §AU2 polynomial-height 3-separating weights w_0,...,w_{n−1}: distinct k-subsets have distinct weight sums for k=1,2,3, and w_i=O(n^6). Put

    W=1+Σ_i w_i,
    e(S)=|S|W+Σ_{i∈S}w_i,
    E=e({0,...,n−1}), R=E+1,
    A=2^n n! H^n,
    B=2^b for an integer b with B>2A,
    d_i=B^(W+w_i), z_v=B^(v R).

Both F and G_v are multiaffine polynomials in d. Their coefficients are signed minors/cofactors, each of magnitude ≤n!H^n. When evaluated at the specified D, at most 2^n such terms collide at a single exponent, so the aggregated coefficient has magnitude at most A<B/2. Equation (1) expresses y as a signed base-B expansion whose entire F(D) lies in exponents 0,...,E and whose G_v(D) lies in vR,...,vR+E. These n blocks are pairwise disjoint. The *balanced* base-B digits therefore recover all n substituted-polynomial blocks without cancellation or carries between them.

Within a block, the coefficient of ∏_{j∉T}d_j for each |T|≤3 is at the unique exponent e([n]\T), by the 3-separating weights. Let f_T denote this exact signed coefficient of F, and g_{v,T} that of G_v. The following exact minor/cofactor identities give the entries:

    a_i := c_ii = −f_{ {i} },
    p_ij := c_ij*c_ji = a_i*a_j − f_{ {i,j} }    (i<j),
    c_{v0}=−g_{v,{0,v}},
    c_{0v}=p_{0v}/c_{v0}                         (v≥1),
    c_{ij}=(a_j*c_{i0}−g_{i,{0,i,j}})/c_{j0},
    c_{ji}=p_ij/c_{ij}                          (1≤i<j<n).

All denominators are positive under the hypothesis. These are the directed pair and named 3-Port path relations already established in R284AT/AU. Thus every C entry is uniquely reconstructed from the one observed integer y. QED.

## Precision and cost

The greedy weights give W=O(n^7), E=O(n^8); log₂ B=O(n(log n+log(H+1))). Each diagonal input has O(n^9(log n+log(H+1))) bits, and each star strength and the resulting scalar have O(n^10(log n+log(H+1))) bits (conservative bounds). Signed-radix extraction, Bareiss determinant calculation and entrywise integer divisions are polynomial-bit operations. The theorem exchanges independent read count for large instrument dynamic range.

A real approximation of the integer reading with absolute error strictly below 1/2 is sufficient: rounding first restores the exact y. No guarantee is asserted for fixed relative error or bounded-range hardware.

## AX2: exact number of reads and information capacity

For H≥2, **one** simultaneous-edit scalar read is optimal because zero reads cannot distinguish H^(n²) matrices. For H=1, C is known and zero reads suffice.

Any injective integer response over the same class must attain absolute value at least (H^(n²)−1)/2 for some matrix: 2M+1 integers is the maximum cardinality of an integer response alphabet inside [−M,M]. Thus the worst-case output bit length is Ω(n² log₂ H). More generally, when each scalar read has at most 2^b possible output symbols, any deterministic adaptive q-read protocol satisfies qb≥n² log₂ H by decision-tree leaf counting. This cardinality bound applies to the declared finite class, independent of the star-edit construction.

## Exact reproducibility and evidence

Companion files:
- R284AX_simultaneous_star_single_read_checker.py
- R284AX_simultaneous_star_single_read_verification.json

Python standard library only. Deterministic seed 2842824. Exactly 606 complete one-reading matrix reconstructions: 64 seeded instances n=2..6; all 512 binary positive 3×3 matrices; 30 additional ternary 3×3 cases. Additionally 64 independent small-integer comparisons of equation (1), including signed strengths, passed. Maximum observed response bit length 38,978; maximum diagonal input 1,393; maximum star strength 34,511. The general theorem is supported by the displayed proof, with finite computations as implementation checks; no independent mathematical review has occurred.

## BRC, residuals, and scope

This is a specified-observer exact compression certificate: for fixed n,H and the programmable simultaneous star intervention, the response has singleton fibers over the declared matrix class. Exact recovery retains directed Port identities and signed 2-/3-body relations; it does not replace signed cancellation with positive mass. It does not authorize deleting provenance or additional BRC interaction carriers under other future operations. P000 and ACTIVE Heartbeat-world native X6 semantics remain unchanged.

## Further questions

1. Under a fixed maximum input magnitude and b-bit noisy response, establish the exact scalar-reading/precision Pareto frontier, including adaptive designs.
2. Reduce the current very large input/output bit bounds toward the Ω(n² log H) capacity limit.
3. Quantify the cost of independently controlling n−1 simultaneous star edits; distinguish one determinant evaluation from one actuator action.
4. Resolve R284AW's adaptive single-entry lower-bound cases H=2,3, which are separate from the present simultaneous-edit theorem.

Provenance: independent portable scientific note. Formal Task CLAIM, PROGRESS, Result and Review are not asserted.