# EC49BO — Exact subgroup residual lattice and ensemble aggregation in signed X6 BRC

Date: 2026-10-30. Research status: AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_FINITE_CHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. This is an author-side mathematical manuscript, NOT a native Source Result, a canonical task publication, or an independent Driver review.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main 51309f36bdcd96b26f08d9a10153cfca1142ecda; Enterprise Math main dcde68d8979770a9aa5d29ef7a0591a98b9913de; predecessor author draft PR #1730 HEAD 8ee3cc4031a63b75f954fe8630c8be97b2a8912c. Native kernel: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, Git blob 300a96e3dc24bf6fff73743037a0347a8bc83176. P000 remains the six independent native spatial axes, one distinct time dimension, and joint-observer-residual preservation; this paper addresses static path words, not time dynamics, a full three-dimensional slice, complex amplitude, or a physical BRC universe.

## Model and exact observer

An ordered path word t is a finite sequence of signed X6 primitive steps ±E_i, i=1,...,6, from a chosen Cell source (an affine chart-relative anchor, not a global origin). Denote its length by n and signed displacement by d in Z^6. Choose twelve strictly positive rational direction weights w_i^+,w_i^- and q_i=w_i^+w_i^-. The weight of a single witnessed path is chi_w(t)=product over its steps of the corresponding direction weights. This term is extracted from the actual native BRC endpoint_weight(n,d,w+,w-), which SUMS the weights of ALL compatible paths. There is no claim that the current native function accepts a selected path multiset or a filter.

The counts of ±E_i in a word of given n,d are a_i+k_i and b_i+k_i, where a_i=max(d_i,0), b_i=max(-d_i,0), k_i>=0 and sum k_i=K=(n-||d||_1)/2. Consequently

chi_w(t)=B_w(d) product_i q_i^{k_i},   B_w(d)=product_i (w_i^+)^{a_i}(w_i^-)^{b_i}.

Fix the source, n, d, ordered first r and last r labels. The declared one-hole future contexts are concatenation with known paths, algebraic word reversal (negate signs and reverse order), and a finite subgroup H<=S_6 acting by axis relabeling with the positive rational weight INSTRUMENT held fixed. The final observer reports the basic source/length/displacement/boundary registers plus this single-path product. These are mathematical path operations, not an asserted physical heartbeat evolution.

## Theorem A — exact all-H kernel and Smith-normal-form classification

Let P be the primes occurring in numerator/denominator of any q_i; v_p is the integer p-adic valuation of a positive rational. Set W={z in Z^6: sum_i z_i=0} and

C_{H,q}={z in W: sum_i z_i v_p(q_{sigma(i)})=0 for every sigma in H and every p in P}.

For any two legal words in the same fixed basic observer fiber, all the declared future observations agree **if and only if** their loop-count difference k-k' lies in C_{H,q}. Therefore, the set of reachable cosets k+C_{H,q} (along with the fixed basic registers) is the EXACT minimal future-sufficient state classification for this declared observation language. This is not a fixed information-bit count, since actual reachability and encoding are additional questions.

Compute it with integer exact arithmetic. The vectors b_j=e_j-e_6 for j=1,...,5 form a Z-basis of W. Define a matrix M indexed by (sigma,p) in H×P and j in 1,...,5:

M_{(sigma,p),j}=v_p(q_{sigma(j)})-v_p(q_{sigma(6)}).

Then C_{H,q} is the lift of ker_Z M. If integer-unimodular U,V satisfy UMV=diag(s_1,...,s_rho,0,...), the condition Mz=0 is equivalent to the first rho coordinates of V^{-1}z being zero (all s_i nonzero). Thus rho=rank_Q M is the number of independent additive residual coordinates on W; W/C_{H,q}=im_Z M is torsion-free. In particular, the nonunit Smith invariants must NOT be misconstrued as modulo-s_i periodic residuals. A finite n,d path fiber may realize fewer residual classes.

Proof: Given common d, the factors B_w(d) cancel in the ratio between two path products, and every fixed-table sigma sends it to product_i q_{sigma(i)}^{k_i-k'_i}. Unique factorization of positive rationals says this ratio is 1 exactly when all prime valuations vanish, which gives the rows of M. A one-hole concatenation multiplies the products of both compared paths by the same scalar. Inversion swaps plus/minus occurrence counts, and with their common d the extra ratio depends only on d and the instrument, hence also cancels. Composing those operations produces a known scalar times one of the finitely many sigma-orbit weight products. The first/last r registers also compose correctly under these operations, using the stored ends; no hidden path interior is needed for that portion. These observations prove sufficiency by induction on context construction. For necessity, each sigma alone is an allowed future operation, so each ratio must equal 1. Finally b_j is an integral basis of W, the valuation equations are Mz=0, and the unimodular Smith transformations preserve the integer lattice. If diag(s_i) times a vector vanishes with each s_i≠0, every such coordinate is exactly zero. QED.

## Theorem B — strict intermediate state for H=< (1 2) >

Take H={identity,(1 2)}, w+=(2,3,3,2,1,1), w-=(1,1,1,1,1,1), q=(2,3,3,2,1,1) and P={2,3}. The exact four-row, five-column valuation matrix is

M = [[1,0,0,1,0],
     [0,1,1,0,0],
     [0,1,0,1,0],
     [1,0,1,0,0]].

Its Smith diagonal is (1,1,1,0), rank 3, and C_{H,q} has the exact Z-basis
 (1,1,-1,-1,0,0) and (0,0,0,0,1,-1).
This is a genuine rank-two kernel strictly between W (rank five) and the zero subgroup: a three-coordinate residual is necessary on unbounded unconstrained differences but six full loop counters are not necessary for this observation scope. The first relation has q_1 q_2=q_3 q_4=6; the second has q_5=q_6=1. Both also survive the allowed swap.

For a test of whether current weight alone is sufficient, choose legal closed length-six words with the SAME source, displacement d=0, first +E_5 and last -E_5:
 U=(+5,+1,-1,+3,-3,-5),
 V=(+5,+2,-2,+4,-4,-5).
Both have current product chi(U)=chi(V)=6, but after swapping axes 1 and 2, products are respectively 9 and 4. Hence a current single number is not a sufficient representation for the specified future subgroup.

The companion exact verifier exhaustively enumerates all n=6,d=0 signed path words (there are 19,920), compares fixed first/last r=1, and obtains:
 boundary-only 144 classes;
 boundary plus current weight 468 classes;
 boundary plus both H-orbit weights 828 classes;
 boundary plus full six-axis loop histogram 1,044 classes.
It independently checks all 56 nonnegative six-part compositions of K=3 and all 1,596 unordered pairs against the exact lattice basis. Native endpoint_multiplicity=19,920 and native endpoint_weight=152,640, which agrees with explicit sum of all 19,920 per-word products. This finite census is an exact audit of its stated finite domain, not the logical basis for the all-n theorem.

## Theorem C — selected-ensemble aggregate state and lawful filtering counterexample

The native endpoint_weight sums every compatible word; here we explicitly introduce a DIFFERENT auxiliary interface that accepts a *selected finite multiset* of such path witnesses with nonnegative integer multiplicities, all having the same n,d,source and first/last r. Define the H-orbit aggregate vector

A_H(S) = ( sum_{t in S} m_t chi_w(sigma t) )_{sigma in H}.

Assume the only permitted futures apply the SAME one-hole context and the SAME H action uniformly to every multiset element; the final observer returns the unchanged basic registers, total witness count, and sum of resulting rational products, without any path-specific filter or selection. Then two selected ensembles are indistinguishable under ALL these futures exactly when they have equal total count and equal A_H. This is a strictly coarser exact equivalence than preserving each witness's separate orbit signature.

Proof: On the fixed (n,d) fiber, each allowed one-hole context has per-word weight c*chi_w(tau t) for a common positive rational scalar c and a group element tau in H. Hence the ensemble's resulting total is c times component tau of A_H. Equal vectors and counts imply equality for every allowed future. Conversely, choose as future operation each tau in H separately to expose every vector component and use the identity context to observe count. Thus no two unequal vectors can be merged for this observer family. QED.

Explicit failure when the future operation language is enlarged: with the same q,H, take four closed n=6 paths sharing first +E_5 and last -E_5:
 A1=(+5,+1,-1,+1,-1,-5),   A2=(+5,+2,-2,+2,-2,-5);
 B1=(+5,+3,-3,+3,-3,-5),   B2=(+5,+4,-4,+4,-4,-5).
Set S={A1,A2}, T={B1,B2}. Their per-witness H-orbit signatures are respectively {(4,9),(9,4)} and {(9,9),(4,4)}, which are unequal as multisets. But their groupwise SUMS are identical: A_H(S)=A_H(T)=(13,13) and both have exactly two witnesses. Theorem C therefore declares them equivalent under every UNIFORM future. If the future additionally permits the filter 'retain only words containing axis 1 with either sign, then sum', S has weight 4 while T has weight 0. Consequently minimal memory depends on the explicitly typed future operation language, and a stronger observer requires more history.

The selected-ensemble and filter operations above are NOT current native endpoint_weight API parameters. This is an algebraically valid extension of its per-word BRC summands, not an API claim, a signed/complex BRC result, or a physical statement. In particular, a nonzero weighted mass is not a phase cancellation.

## Validation, source and continuation

The source-pinned native signed_brc.py Git blob was imported and its two actual aggregate entrypoints called in an exact Fraction/SymPy verifier. The exact verifier was run twice with byte-identical JSON output; source digest, 56 compositions, 1,596 pairs, all 19,920 words, class counts, native aggregate and all witness values are recorded in accompanying VERIFY_EC49BO.py and EXACT_REPORT_EC49BO.json. Only finite enumeration is computationally verified; the universal statements above are author analytical proofs pending independent review. No formal claim, Source-native Result, or Driver acceptance is inferred from GitHub storage.

Next EC49BP: define an explicitly typed finite algebra of path-dependent filters and its action on selected path ensembles, determine the minimal future-sufficient vector of filtered H-orbit aggregate sums, construct a complete small native-X6 finite audit, and identify rigorous conditions under which the selected-ensemble observation reduces to the existing native all-path endpoint_weight. Secondary work: independently verify integer Smith transformations and actual finite fiber reachability. Preserve P000, provenance, observer typing, and all existing source/permission boundaries.
