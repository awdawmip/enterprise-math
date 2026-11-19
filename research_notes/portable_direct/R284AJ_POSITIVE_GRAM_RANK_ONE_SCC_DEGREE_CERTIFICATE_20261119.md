# R284AJ — Positive Gram-rank certificate for exact one-SCC Port activation order

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.  
**Predecessor:** R284AI one-SCC rank-one cancellation, extending R284AH. **Frozen scientific input:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34.  
**Scientific scope:** auxiliary nonnegative Port channel pencils with individually named diagonal edits, not native X6 spatial dimension reduction; P000 and the ACTIVE worldview unchanged.

## 1. A two-layer principal-minor transport identity

For arbitrary m×m C over a characteristic-zero field, let

    N_C = [0_m I_m; C 0_m],    D(u,v)=diag(u_1,...,u_m,v_1,...,v_m),
    x_i=u_i v_i.

**Theorem AJ1 (exact coefficient oracle):**

    det(N_C+D(u,v))
       = det(diag(x_1,...,x_m)-C)
       = sum_{I subset [m]} (-1)^|I| det(C[I,I]) prod_{j notin I} x_j.     (1)

Proof. Over the rational function field where all u_i are invertible, take the Schur complement of D_u. Its determinant is det(D_u) det(D_v-C D_u^{-1}), which equals det((D_v-C D_u^{-1}) D_u)=det(D_vD_u-C). Extend the polynomial identity to every point, including zero edits. Expand determinant by diagonal-selected rows to obtain the sum of complementary principal minors. QED.

Define the **principal nonsingular order** d(C) as the largest size of a principal submatrix with nonzero determinant (empty set has size 0). Then (1) gives the exact total-degree formula

    nu(N_C)=2(m-d(C)).                                               (2)

Indeed distinct I yield distinct monomials in separately named coordinates, so their nonzero coefficients do not cancel across I.

## 2. Strictly positive rank-r Gram certificate

Fix integers m>=2 and 1<=r<m. Let U be any m×r rational matrix of column rank r and **strictly positive entries**. Set C=UU^T. Then C has strictly positive entries and exact rank r.

**Theorem AJ2 (rank-only exact degree).** For this family,

    d(C)=r,
    rank(N_C)=m+r,
    nu(N_C)=2(m-r).                                                   (3)

Its support graph is ONE strongly connected component, p(G)=2m, and hence the exact R284AH cycle-cover cancellation gap is 2(m-r).

Proof. C is a positive semidefinite Gram matrix. For any principal index subset I, C[I,I]=U_I U_I^T, so Cauchy–Binet yields

    det C[I,I] = sum_{J subset [r], |J|=|I|} det(U[I,J])^2.            (4)

The sum is nonnegative, and is zero whenever |I|>r. Since U has rank r, some r rows form a nonsingular r×r U_I, so the r-principal minor of C is positive. Thus d(C)=r. In N_C, the top-right identity has rank m and the bottom-left C has rank r, giving rank m+r. Since every entry C_ij>0, each B_i connects to all A_j and each A_i connects to B_i: the directed support is strongly connected and contains the complete packing of m two-cycles. Apply (2). QED.

**Theorem AJ3 (small certificate for high-order cancellation).** Given an exact claimed factor U satisfying C=UU^T, verify the equality by rational multiplication, check U's column rank r using exact elimination, and check positivity of its entries. This certifies simultaneously that all principal minors of C of order exceeding r vanish, that at least one r-minor is nonzero, and that the first nonzero multi-edit response order is exactly 2(m-r). It avoids enumerating the 2^m principal subsets and all signed cycle covers. Matrix equality and rank checks require polynomially many exact arithmetic operations; bit complexity depends on rational numerator/denominator growth and is not claimed independent of coefficient heights.

This includes R284AI's rank-one C=ab^T only when a=b up to positive symmetrizing scalings. More generally a nonsymmetric positive rank-one C has the direct weighted involution certificate of R284AI.

For an explicit dense rational test family take U_{ij}= i^(j-1)/m^(r-1), i=1,...,m and j=1,...,r (Vandermonde row vectors). Every entry is strictly positive; r distinct rows yield nonzero determinant, so (3) gives every even degree 2,4,...,2(m-1) within one strongly connected positive-support family.

**Observer note.** All 2m edit names u_i,v_i are retained. This algebraic certificate concerns the first nonzero total-degree coefficient of a scalar determinant observer, not a claim that a scalar observation preserves all latent paths or all future operations. The pencil has no nonzero fixed common right or left kernel under arbitrary independent diagonal edits, by varying one edit coordinate at a time.

## 3. Stable internal Port embedding

For q=2m, K=q+1, set c sufficiently small, for instance

    c=1/[16(K+max_i(row_sum(N_C)_i)+1)].

Then the K×K core

    H(t) = c J_K + c blockdiag(N_C,0) + diag(t_1,...,t_q,0)

has strictly positive entries and row sums <1 for every t_i in [0,c]. Subtracting the last row gives

    det H(t) = c det(c N_C+diag(t))
             = c det(diag(t_i t_{m+i})-c^2 C).                       (5)

Using R284AB's auxiliary gated feedback complement, with delta=1/(256K) and g=1/16,

    A_Port = [ I-delta J  -H(t)       0;
               -delta J   I-delta J -g I;
               -g I       0          0 ],

yields det A_Port=(-1)^K g^(2K) det H(t). Its internal two-layer feedback matrices are nonnegative and have row sums <1; their support is strongly connected. The terminal layer remains an auxiliary Port observation, with no extra physical dynamics inferred.

Hence the entire even activation spectrum (3) admits positive-core, internally stable feedback Port realizations. The analysis is exact rational linear algebra; no unexecuted native BRC–Shor arithmetic is claimed.

## 4. Author verification

Checker: research_notes/portable_direct/R284AJ_gram_scc_checker.py, importing exact Fraction determinant/rank functions from R284AI_rank_one_scc_cancellation_checker.py in the same directory. Evidence: research_notes/portable_direct/R284AJ_exact_verification.json.

Actual author run: 100 principal-minor checks (all signs and the rank cutoff), 1,936 full Boolean-grid 2m×2m determinant comparisons with (1), 14 rank checks, and five exact complete Port/core determinant crosschecks. Families: m=2,3,4 and all 1<=r<m, plus m=5,r=3. All PASS. Universal statements rely on (1)–(5) and their algebraic proofs; these finite checks establish finite test coverage only. Independent Review=NOT_REVIEWED.

## 5. Next problem

Extend polynomial-time certificates beyond a supplied PSD Gram factor: symmetrizable nonnegative matrices, bounded-rank but non-symmetric factorizations C=UV^T with varying signs of principal minors, and low-treewidth supports. Determine whether exact first-degree detection for arbitrary sparse C admits a substantially cheaper certificate than principal-minor enumeration; retain all named edits and BRC/Port observer typing.
