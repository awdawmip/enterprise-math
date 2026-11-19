# R284AI — One-SCC exact cycle-cover cancellation by rank-one Port coupling

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.  
**Scientific frozen pin:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34.  
**Source lineage:** R284AH cycle packing and cancellation gap; R284AG principal-minor expansion; R284AB auxiliary gated bidirectional-feedback Port complement.  
**Scope:** positive rational zero-diagonal *auxiliary observer matrices*; these are named Port channel indices, not native X6 spatial axes. P000/X6 and the ACTIVE residual-preservation worldview remain unmodified.

## 1. Exact theorem: unbounded cancellation inside ONE strongly connected component

For every integer m >= 2 and every two strictly positive rational vectors a,b in Q^m, let

    N_m(a,b) = [ 0_m      I_m  ]
               [ a b^T    0_m  ]

with vertices A_1,...,A_m,B_1,...,B_m. Introduce 2m independently named diagonal edits u_i on A_i and v_i on B_i. Define x_i=u_i v_i and

    P_m(u,v)=det(N_m+diag(u_1,...,u_m,v_1,...,v_m)).

**Theorem AI1 (closed formula).** For every such m,a,b,

    P_m(u,v)=prod_{i=1}^m x_i
             -sum_{i=1}^m a_i b_i prod_{j!=i} x_j.                 (1)

In particular, the least nonzero total degree of P_m is

    nu(N_m) = 2(m-1),            for every m>=2.                  (2)

The support digraph of N_m is strongly connected and contains a vertex-disjoint cycle cover of all 2m vertices. Thus p(G)=2m and the R284AH support bound equals zero, while the actual cancellation gap is

    Delta_m = nu(N_m) - (2m-p(G)) = 2m-2.                         (3)

This gap is unbounded **within a single SCC**, strengthening R284AH's previous b-fold direct-sum construction. The m=2 example, in the reordered basis (A1,B1,A2,B2) with a=b=(1,1), is exactly R284AH's matrix N_0.

**Proof.** For generic nonzero u_i, Schur complement along D_u gives
det([D_u,I; ab^T,D_v])=det(D_u)det(D_v-ab^T D_u^{-1}).
Since D_u is diagonal, this is det(diag(u_i v_i)-ab^T).
The rank-one determinant identity gives the right side of (1).
Both sides are polynomials, so equality extends to all edits, including zero.
Every coefficient of a degree 2m-2 monomial missing one named pair is -a_i b_i, which is strictly nonzero; no smaller-degree monomial appears. This proves (2).
Each A_i→B_i exists; each B_i→A_j exists. Hence any vertices are mutually reachable and the graph is one SCC. All pairs A_i↔B_i form a disjoint cycle cover, giving p(G)=2m. QED.

**Theorem AI2 (compact sign-reversing involution certificate).** For every principal vertex set T of N_m:
- If T contains a different number of A and B vertices, its principal determinant vanishes.
- If those numbers agree but the selected A and B index sets differ, the principal determinant vanishes.
- If both index sets equal I, of size k, then

    det N_m[T,T] = (-1)^k det(a_I b_I^T).

It is therefore -a_i b_i for k=1, one for T empty, and zero for every k>=2.

**Proof.** Every top row has a single nonzero edge to its same-index bottom vertex. A nonzero permutation in a principal determinant must match all selected top vertices to their same-index bottom vertices, forcing equality of the two selected index sets. For k>=2, the remaining bottom-to-top matching is a permutation pi of I, of weight prod_{i in I}a_i times prod_{j in I}b_j, independent of pi. Pair pi with (i0 i1)∘pi for any two fixed distinct indices i0,i1 in I. This is a fixed-point-free, sign-reversing, weight-preserving involution. The paired terms cancel exactly. For k=1 the two-vertex cycle has determinant -a_i b_i. QED.

Consequently ALL maximum-cardinality minors, and in fact all principal minors larger than order two, vanish by a single local involution rule, **without enumerating their permutations or their principal subsets**. The certificate consists of the explicit block pattern and the rank-one factorization (a,b). These are structural witnesses and can be checked by exact multiplication.

**Theorem AI3 (rank, absence of a fixed kernel, and extremality).**

    rank N_m = m+1,  corank N_m = m-1,  nu(N_m)=2 corank N_m.

The whole edited pencil has no nonzero vector in the intersection of all its right kernels, nor in the intersection of all left kernels. Among zero-diagonal supports on q vertices that contain a directed 2-cycle and have p(G)=q, the gap obeys Delta <= q-2, and our family (q=2m) attains equality.

**Proof.** The two off-diagonal blocks have ranks m and 1, so rank N_m=m+1. If h is killed by every N_m+diag(t), comparing t with t+z e_i forces h_i=0 for each independent edit; the left-kernel argument is identical. A directed 2-cycle i↔j has principal minor -N_ij N_ji !=0, so the coefficient of prod_{k notin {i,j}}t_k in the diagonal determinant is nonzero. Hence nu<=q-2. When p(G)=q, Delta=nu, and (3) reaches q-2. QED.

## 2. Transfer to a strictly positive stable internal Port observer

Put q=2m, K=q+1, choose

    c=1/[16(K+m+1)],   delta=1/(256 K),   g=1/16.
    C(t)=c J_K + c blockdiag(N_m,0) + diag(t_1,...,t_q,0)

for rational edits 0<=t_i<=c, where J_K is the all-ones matrix. Every C entry is positive. Each row sum is bounded by c(K+m+1)=1/16. Let the 3K×3K *auxiliary Port complement* be

    A_Port(t) = [ I-delta J    -C(t)        0   ]
                [ -delta J     I-delta J   -gI  ]
                [ -gI         0            0   ].

Eliminating its terminal blocks gives the exact identity

    det A_Port(t) = (-1)^K g^(2K) det C(t).

Subtracting the final row of C from all preceding rows gives

    det C(t) = c det(c N_m + diag(t))
             = c [prod_i(t_i t_{m+i}) -
                  c^2 sum_i a_i b_i prod_{j!=i}(t_j t_{m+j})].   (4)

The two transient internal-layer nonnegative feedback blocks have strictly positive entries on their allowed support; their row sums are bounded by delta*K+1/16 and 2 delta*K+g, both less than one. The internal graph is strongly connected. The terminal block is an algebraic observer, not an independent claim of global stochastic stability.

Thus the one-SCC unbounded cancellation family survives as a strictly positive core, internally stable, feedback-rich Port observer. The formula preserves all 2m individually named edit coordinates and their possible future joint observation; compression to a scalar cannot be presumed observationally lossless.

## 3. Verification and evidence

Source checker: research_notes/portable_direct/R284AI_rank_one_scc_cancellation_checker.py (Python 3 standard library, Fraction exact elimination). Run: python R284AI_rank_one_scc_cancellation_checker.py. Result: research_notes/portable_direct/R284AI_exact_verification.json.

Author-run PASS: 2,170 full exact rational pencil determinants; 336 all-principal-subset determinants; 152 weight-preserving transposition tests; four exact rank tests; six 15×15/21×21 Port/core determinant comparisons. Rational test parameters a_i=(i+1)/(i+2), b_i=(i+2)/(i+3), m=2,...,5, with Boolean edit grid and m=2,3 also ternary edit grid. These are finite cross-checks; equations (1)–(4), the unbounded result and the involution are supported by the proofs above.

**Research status:** original author proof and exact finite checker, independent review NOT_REVIEWED. Formal Task CLAIM, Result, activity/event association and Working Truth admission are separate records.

## 4. Next problem

Classify which sparse irreducible two-layer factors B,C admit a **polynomial-time checkable weighted permutation involution** preserving all selected higher principal minors, without requiring rank(C)=1. Compare structured cancellation certificates with R284Y minor enumeration and R284AE graded Schur recursion using exact operation/bit counts. Determine whether the one-SCC gap construction persists under strictly positive off-diagonal entries of the complete N matrix, rather than merely the strictly positive Port core.
