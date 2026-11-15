# R192 — Affine query minimality and unrestricted two-source rigidity

Date: 2026-11-16 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Mode: independently saved portable research; no formal CLAIM, Result, Review or P000 promotion.
Frozen science input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

## Exact sources and research object

R182 last-occurrence quotient: enterprise-math@83824bda8cb4ca4d9db71d660165f00fd92326ef.
R183 quadratic-dimensional coordinatewise reset upper bound: enterprise-math@5557fb3748bbe9e831e2f35716607dacffc0c6d4.
R191 dyadic history-sensitive lift and bit-optimal quotient codec: enterprise-math@cce5ae839dcc7719c1e30f179a3181d74136ceee.

Fix k>=1 selected source IDs T={0,...,k-1}. Histories consist of complete BRC/X6 atoms whose selected-source last-occurrence observer is considered; unselected atoms are invisible to this *specific observer* and remain in the richer original carrier. The quotient S_k is the set of partial permutations of T, ordered from oldest to newest final occurrence. Its chronological product is

    s ⋆ t = (entries of s absent from support(t), in old order) followed by t.

It is the finite right-regular band from R182; source letters satisfy aa=a, aba=ba. The observer q_U(s) is the last-occurring member in subset U, or NONE. The native X6 six axes, separate time, paths, branch identities, weights and multiplicities are not modified by these auxiliary metadata coordinates.

Let C_k contain every singleton {i} and pair {i,j}, i<j. Define f_U(s)=0 if no U-member appears, otherwise f_U(s)=i+1 where i is its last-occurring U-member. The values are distinct, and these functions separate S_k. Put d_k=k+binom(k,2).

## R192A. Exact minimum dimension with affine-linear specified query readouts

**Theorem.** Suppose there are rational affine generator actions on Q^d with arbitrary cross-coordinate coupling, a common initial point x_0, and affine-linear functionals L_U for each U in C_k, satisfying

    L_U(A_s(x_0)) = f_U(s)

for every s in S_k, with A_(s⋆t)=A_t o A_s. Then d>=d_k. The R183 affine reset maps attain this bound, so the minimum in this *affine-readout model* is exactly k(k+1)/2, regardless of whether the transition maps themselves are restricted to diagonal resets.

**Proof.** Regard functions on S_k as vectors in Q^(S_k). The set of 1+d_k functions {1} together with all singleton f_{i} and pair f_{ij} is linearly independent.

Assume a relation

    c_0 + sum_i a_i f_{i}(s) + sum_(i<j) b_ij f_{ij}(s) = 0

holds for every s. Evaluating at the empty word gives c_0=0. For fixed i<j, subtract the equation at state (j,i) from that at (i,j). Both states have equal support; all singleton functions agree. Every pair function other than f_{ij} also agrees, since such a pair contains at most one of i and j, and no other source appears. But f_{ij}((i,j))=j+1 and f_{ij}((j,i))=i+1. Their difference is nonzero, forcing b_ij=0. Repeating this for all pairs eliminates all pair coefficients. At singleton state (i), f_i=1 and every other singleton f_j=0, implying a_i=0 for every i. Hence all 1+d_k functions are independent.

Every one of these functions, however, is a pullback along s↦A_s(x_0) of an affine-linear function on Q^d. The latter vector space has dimension d+1. Therefore d+1>=1+d_k and d>=d_k. R183 constructs an action on Q^d_k by overwriting coordinate U with i+1 whenever i∈U and leaving it unchanged otherwise. Each coordinate then gives the corresponding f_U by direct affine-linear projection from the zero initial state. The representation respects ⋆ and is faithful. Equality follows. QED.

The same argument holds for any rational numeric encoding in which each singleton distinguishes present from absent and each pair assigns different values to its two target answers, using any fixed absent value. The pair antisymmetry argument first eliminates pair coefficients, then singleton contrasts eliminate the rest.

**Scope.** This theorem is unconditional with respect to affine *update coupling* but assumes affine-linear numerical query readout from one common state. With nonlinear query decoding or abstract map-only faithful actions, the general minimal dimension is a different problem.

## R192B. Full unrestricted minimum for the five-element band S_2

**Theorem.** Over Q, the minimum dimension of any faithful rational affine action of the five-element band S_2={ε,a,b,ab,ba} is exactly 3. No linear query readouts are assumed for this result. The same proof works over any infinite field.

**Upper bound.** The R183 construction, on coordinates (x_a,x_b,x_ab), is

    A(x_a,x_b,x_ab) = (1,x_b,1),
    B(x_a,x_b,x_ab) = (x_a,1,2).

These affine maps satisfy A²=A, B²=B, A o B o A=A o B, B o A o B=B o A. On x_0=(0,0,0), the five words ε,a,b,ab,ba yield respectively (0,0,0), (1,0,1), (0,1,2), (1,1,2), (1,1,1), so all five actions are distinct.

**Lower bound.** Suppose these five transformations had a faithful affine representation on Q². Because the five affine transformations are distinct and Q is infinite, we may choose a rational initial point x_0 at which their five evaluations are distinct. Indeed, each pairwise coincidence set is a proper affine subspace and a finite union of proper affine subspaces cannot cover Q². Let the corresponding distinct points be p_ε,p_a,p_b,p_ab,p_ba.

Chronological append-a is an affine map A. The band law aba=ba gives

    A(p_b) = A(p_ab) = A(p_ba) = p_ba,
    A(p_a) = p_a ≠ p_ba.

Thus A is nonconstant, and p_b,p_ab,p_ba must be collinear: an affine map on the plane that sends three noncollinear points to one point is constant everywhere.

Similarly append-b is an affine map B with

    B(p_a) = B(p_ab) = B(p_ba) = p_ab,
    B(p_b) = p_b ≠ p_ab.

Hence p_a,p_ab,p_ba are collinear. The two lines contain the same two distinct points p_ab,p_ba, so they coincide. All four nonempty-state orbit points lie on one line ℓ. Since A sends the distinct points p_b,p_ab on ℓ to p_ba, its restriction to ℓ is constant at p_ba; hence A(p_a)=p_ba, contradicting A(p_a)=p_a. No faithful affine action in dimension 2 exists. Dimension ≤1 would embed into dimension 2 by adjoining inert coordinates, so it is excluded as well. Thus d>=3, and the upper bound is sharp. QED.

**Corollary.** S_1 has minimum affine dimension 1. Any S_k for k>=2 contains a two-source subband, so its unrestricted minimum is at least 3. The unrestricted minimum for k>=3 is still unresolved (R183 supplies the upper bound k(k+1)/2).

## Exact verification

The companion R192_affine_query_minimality_check.py executes only exact Python integer arithmetic. It exhaustively checks all S_k state pairs and their affine action products for 1<=k<=5 (4+25+256+4225+106276=110786 comparisons), along with action injectivity. It constructs a rank witness matrix with one empty row, k singleton rows and binom(k,2) antisymmetric pair-difference rows, verifying rank 1+d_k for 1<=k<=10. In k=2, it additionally checks the 3D orbit rank and both band relations. R192_verification.json records the actual finite results.

The all-k claims follow from the proofs above, not from enumeration. No native BRC physical evolution, native Affine/EffectHistogram integration, π/trigonometric computation, or physical residual attribution was performed.

## Scientific continuation

R192A extends R183's restricted reset-coordinate dimension lower bound to all affine transition dynamics when the declared source-query responses are affine-linear probes. R192B resolves the first nontrivial unrestricted faithful affine dimension, k=2. R191's lower-dimensional dyadic free-word lift does not descend to the finite quotient; that history-sensitive construction uses an additional nonlinear maximum/threshold observer.

Next: determine whether S_3 has a faithful affine quotient action in dimension 3, 4 or 5, or prove a dimension-6 lower bound. Preserve the exact frozen science pin. Separately integrate the specified source-only observer action with pinned enterprise_math.brc_transport.Affine and EffectHistogram and validate exact positive weights, multiplicity, identity and serial composition while retaining full branch/path provenance.

Current work is author-proved and finite-checked, not independently reviewed or canonically admitted. Any Activity linkage and shared Task ownership require separate current authenticated controls.
