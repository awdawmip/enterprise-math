# PREFIX-587-R2 — Combinatorial native BRC inverse and the exact 96-ray positive boundary cone

Date: 2026-11-08 Asia/Shanghai. Status: AUTHOR-SIDE PROVED / EXACT INTEGER EXECUTED / UNREVIEWED / NOT ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Parent frontier: PREFIX-585 immutable branch commit 5ec3c4c3787fb1e98cc9d8f288cf0d2f28f2efd7; PREFIX-586 exact inverse and endpoint repair, same PR #1797.
Original native model preserved: 4 STARs, 48 phases, 96 branch ports, 144 directed phase edges, 576 labelled actions, all six source-axis rewards and the fixed original gate target. The theorem is about the exact weighted BRC observer and does not alter P000 or assert physical dynamics.

## Selected question

PREFIX-586 computed a sparse integer inverse T=3S^-1 through exact 48-state rational elimination and characterized positive endpoint transport through 96 inequalities. Can both be derived directly from the native phase incidence, and can the positive cone be characterized by its complete irredundant linear geometry?

Answer: YES. The native successor matrix decomposes into twelve four-phase signed-axis blocks at the Gram level. Its inverse has a direct source/preceding-axis formula, and each of the 24 original (signed-axis,branch-bit) endpoint cones is simplicial with four extreme rays.

## Exact native definitions

The original STARs are (1,3,6), (1,4,5), (2,3,5), (2,4,6). Original phase i=(a,p,c), where a is the STAR, p the signed previous axis, c the signed current axis; |p|≠|c|, both contained in STAR a, and their signs obey the original near(a,c) relation.

Write S_ij=1 exactly for the original directed transition i->j. Each phase has three successors. They all have previous-axis field p_j=c_i. Define the phase reversal permutation

    rev(a,p,c)=(a,c,p),   R_{j,i}=1{ i=rev(j) }.

The original phase set is invariant under rev; R^2=I. For each signed current axis c∈{±1,...,±6}, let G_c={i: c_i=c}. Each G_c contains four phases: two in each of the two STARs containing |c|, with distinct preceding-axis labels. These 12 groups partition the 48 native phases.

## THEOREM 587.1 — Exact combinatorial inverse with no elimination

The following are integer-matrix identities of the ORIGINAL phase adjacency:

    S S^T = direct_sum_{c∈{±1,...,±6}} (I_4 + 2 J_4),
    S R   = direct_sum_{c∈{±1,...,±6}} (J_4 - I_4),

where J_4 is the 4-by-4 all-ones matrix and direct_sum is in signed-current-axis order. Consequently

    S (S^T - 2R) = 3 I_48

and, because S is square,

    S^-1=(S^T-2R)/3,
    (S^T-2R) S=3 I_48.

In particular the integer matrix T=3S^-1 is the *direct local native formula* T=S^T-2R. Each row of T has one entry -2 at rev(j), three entries +1 at the other original predecessors of j and zero elsewhere. Thus its support and coefficient signs need no Gaussian elimination.

**Proof of the two block formulas.** For two phases i,k with distinct signed current axes c_i≠c_k, every successor of i has p=c_i whereas every successor of k has p=c_k. They share no successor.

For the same signed c, both i,k belong to the same four-phase G_c. When i=k they have exactly three successors. When i≠k they share exactly two: if their STARs are equal, the two successors in the other STAR are common and the single within-STAR successor differs; if their STARs differ, they share one within each STAR (the one available after excluding their respective previous axes). This establishes the block formula for S S^T with diagonal 3 and off-diagonal 2.

Now S R[i,k]=S[i,rev(k)]. The phase rev(k) has previous-axis field c_k. It is an allowed successor of i precisely when c_k=c_i and i≠k: between different STARs both possible other-STAR transitions are allowed; within one STAR the transition to rev(k) is the single nonbacktracking successor exactly when k's preceding axis differs from i's. Thus S R is the off-diagonal all-ones matrix on each G_c. Subtracting twice yields 3I. A square matrix with a right inverse is invertible, so the inverse and reverse product follow. QED.

**Spectral and conditioning corollary.** Each block I_4+2J_4 has eigenvalues 9 once and 1 three times. Hence all singular values of the original integer S are exactly 3 (multiplicity 12) and 1 (multiplicity 36), and its Euclidean 2-norm condition number is exactly 3. The absolute determinant is 3^12; the signed determinant +3^12 was already obtained by exact arithmetic in PREFIX-586. These statements apply to the finite 48-phase original matrix, with no continuum approximation.

## THEOREM 587.2 — 24 simplicial positive endpoint blocks; exactly 96 extreme rays

Retain PREFIX-585's full 96-port U=H B^T and PREFIX-586's U^-T endpoint transform. Assume x_a>0 for all six axes, while the gate parameter z remains arbitrary. Fix one signed current axis c and one original branch bit u∈{0,1}. Let

    r=(r_(i,u))_{i∈G_c} ∈ R^4,
    t=SUM_{i∈G_c} r_(i,u),
    lambda_i=t/3-r_(i,u).

The combinatorial inverse T=S^T-2R gives the exact transformed endpoint coordinate at the position H(rev(i),u):

    (U^-T r)_{H(rev(i),u)}=lambda_i/x_|c|.

Therefore, the full transformed endpoint U^-T r is nonnegative if and only if every lambda_i>=0 across the twelve signed c and two branch bits. For each individual 4-coordinate block,

    r_i = SUM_{k∈G_c, k≠i} lambda_k.

Indeed, SUM_i lambda_i=t/3, hence r_i=SUM lambda-lambda_i. Thus each block is exactly the image of R_+^4 under the invertible integer 4-by-4 map J_4-I_4 (determinant -3). It is a 4-dimensional simplicial polyhedral cone, with EXACTLY four extreme rays

    (0,1,1,1), (1,0,1,1), (1,1,0,1), (1,1,1,0)

in the order of the four original phase identities within G_c. This also proves nonnegative transformed endpoints already imply r>=0, because every r_i is a sum of nonnegative lambda's.

The full native endpoint cone is a direct product of 12*2=24 such 4-dimensional cones. Consequently it is a full-dimensional simplicial cone in R^96 with exactly 96 extreme rays, one ray supported in each of the 24 disjoint four-port blocks.

Its **96 original linear facet inequalities** are exactly

    3 r_(i,u) <= SUM_{k∈G_c} r_(k,u)

for every i∈G_c, every signed c and both u. Each is irredundant as a linear facet: to violate only the condition indexed by i within that block take r_i=4 and the other three original values equal to 1, while choosing uniform positive vectors on all other blocks. Thus the 96 inequalities cannot be replaced by fewer distinct linear facet inequalities of the same ambient cone. They may be evaluated more compactly using per-block sums and maximum coordinates.

**Uniform endpoints.** The all-ones original endpoint has t=4, lambda_i=1/3 on every block. Its image U^-T 1 therefore has strictly positive coordinates 1/(3x_|c|), recovering PREFIX-586's all-length positive open-path transport without a numerical rank or inverse calculation.

## BRC observation and exact implementation

The 4-source incidences and predecessor exclusions are part of the original provenance-preserving 48-phase source representation, not a loss of the original 96-port branch identity. The branch bit u is retained throughout. The cone is defined for the explicit exact U endpoint map, with all six axis weights positive and all path lengths: the analysis does not assert a general cone-invariant 96-port native automorphism.

A self-contained Python standard-library program supplied with this proof reconstructs all 48 original phases, 144 directed phase edges, the reversal R and S; checks all 2304 entries of both ST=3I and TS=3I with T=S^T-2R; checks all 2304 row-pair overlap identities and all 2304 entries of S R; verifies all twelve original four-phase groups and 24 (group,bit) cone constructions; checks all 96 facet-irredundancy witnesses and all 96 proposed extreme rays. It returned ALL_ASSERTIONS_PASS_AUTHOR_SIDE_UNREVIEWED with only exact integers and rational fractions.

BRC reuse: COMPOSE_APPLIED / EXTEND_EXISTING_TOOL, predecessor PREFIX-585 and PREFIX-586. No change to frozen science inputs or source-sensitive observations. This is a directly usable integer arithmetic algorithm and theorem candidate; independent Driver review and official Result remain pending.

## Next discriminating unit

Investigate whether the 24 block-positive cones form an invariant family under **composition** of axis exchange alpha=(1 3)(2 4), native swap (5 6), and the full original weighted transfer A(x,z). An explicit 96-port cone-preserving or cone-leaking witness (with retained labelled source and branch bits) would determine how much endpoint repair is needed over repeated updates, rather than only fixed all-length transport by similarity.
