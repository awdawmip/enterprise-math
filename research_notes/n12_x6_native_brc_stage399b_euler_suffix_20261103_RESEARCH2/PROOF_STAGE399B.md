# Stage399-B — exact Euler-arborescence transfer for BRC history-memory quotients

Date: 2026-11-03. Research2 author-side proof and exact computation. Parent Stage398-B, immutable commit b2e8eecc4c7f2fe4936e5e67e632737ff45720b1 (PR #1736). Frozen scientific inputs: Enterprise Math 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; GLOBAL_KNOWLEDGE_V1 bf84bd7c61a2444b59b1da96be57df0e9ae47e53; original P000 Git blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. This is UNREVIEWED / NOT_ADMITTED.

## Exact objects and parent

A is the 12 signed directions ±E_i on six X6 axes. A history w is a finite word in A with length m, endpoint z in Z^6 relative to a chosen Cell, and ordered adjacency histogram J_ab=#{i<m:(w_i,w_(i+1))=(a,b)}. Fix the source, the positive rational per-direction BRC weights and independent nonzero rational signed per-letter trace factors. The complete current observer O_J from Stage398-B retains z (all 20 relative triple readouts and common depth), source, m, J, signed product, unweighted and positive-weighted full-length BRC endpoint masses. The last three are determined by m,z,J and the terminal letter t in this per-direction model. Its future language permits arbitrary APPEND(a) and at most C CANCEL operations deleting inverse terminal pairs. Stage398-B's author-side theorem says two words in one O_J fiber are future-equivalent exactly when S_C signatures coincide; S_C depends on at most the last min(m,2C+1) letters.

A fixed J forces sum(J)=m-1 for nonempty histories, so every exact fixed-(m,z,J) fiber is finite. An unbounded research family needs varying m or J. Empty and one-letter words are handled explicitly.

## Theorem 399.1: Euler path count from directed J

Let R be a finite nonnegative integer directed-edge matrix on A. Let E(R;s,t) count *vertex-letter words* whose first letter is s, last letter t and directed edge multiplicities equal R (parallel edges of a fixed ordered type are indistinguishable).

If sum R=0, E=1 for s=t and E=0 otherwise. Otherwise let out(v)=sum_x R_vx, in(v)=sum_x R_xv and V be the edge-support vertices together with s,t. If out(v)-in(v) is not 1_(v=s)-1_(v=t) for some v, E=0. Put L=diag(out)-R on V; let tau_t be the determinant of L with the row and column for root t removed. A zero determinant or a negative factorial argument yields E=0. In all other cases:

E(R;s,t) = tau_t * product_(v in V) (out(v)-1+1_(v=t))! / product_(a,b) R_ab! .     (399.1)

All quantities are integers and (399.1) is a nonnegative integer.

Proof. Temporarily distinguish individual copies of each directed edge. The last exit from each vertex v≠t in a complete walk forms a directed spanning arborescence toward t. Conversely choose that tree, order each v≠t's remaining outgoing edges arbitrarily before its chosen tree edge, and order t's outgoing edges arbitrarily. Following each vertex's next unused edge yields a unique complete Euler walk: an early stuck walk with unused edges would contradict the toward-t last-exit tree. Thus labeled edge walks are counted by tau_t times the displayed factorial product; the directed matrix-tree theorem gives tau_t as the reduced outgoing Laplacian determinant. Each indistinguishable vertex-letter word has exactly product R_ab! labeled lifts. This includes loops and s=t closed walks. QED.

## Theorem 399.2: exact signature distribution without enumerating full histories

Input m,z,J,C with m≥1 and sum J=m-1. Put k=min(m,2C+1). Enumerate possible suffixes u=(u_1,...,u_k) in A^k. For each u:

1. Its terminal letter is t=u_k. Every letter multiplicity is forced by n_a=out_J(a)+1_(a=t). Check z=sum_a n_a e(a) and any independently specified per-letter product.
2. Subtract the k-1 internal edges (u_1→u_2),...,(u_(k-1)→u_k) from J; reject negative remainder.
3. If k=m the suffix is the full word; its contribution is 1 precisely when the remaining edge matrix is zero. Otherwise enumerate the letter b preceding u_1 and subtract the bridge edge b→u_1. For each such residual P and each starting letter s, add E(P;s,b) from (399.1). Call the sum d(u).
4. Accumulate d(u) in the bin indexed by S_C(u), discarding zero bins.

The resulting distribution is exactly
D_C(sigma) = #{w in the declared complete O_J fiber : S_C(w)=sigma}.          (399.2)

Therefore sum_sigma D_C(sigma) is the exact cardinality of the fiber; conditional on the parent Stage398-B signature-characterization theorem, the smallest deterministic extra-memory alphabet size and fixed-bit requirement are
q_C(o)=#{sigma : D_C(sigma)>0},  bits_C(o)=ceil(log_2(q_C(o))).               (399.3)

Proof. Every full word has exactly one length-k suffix. If a prefix exists, it has exactly one boundary predecessor b and one initial letter s. Removing the suffix's internal edges and the boundary edge leaves precisely the prefix Euler histogram P, and (399.1) counts all and only compatible prefix words. Conversely any counted prefix followed by u restores J, z and all stipulated deterministic current readings. Hence no word is missed or counted twice. By induction in the recursive definition, S_C(w) reads no more than the final 2C+1 letters (each recursive level removes at most two, leaving the last letter), so S_C(u)=S_C(w). Binning yields (399.2), and the parent signature/future-equivalence result yields (399.3). QED.

For q-only computation, replace exact E by Euler feasibility (degree balance and weak connectivity of nonzero-degree graph support), and do not calculate factorials. At most 12^min(m,2C+1) suffix candidates and at most 12^2 predecessor/start trials per candidate are needed; each feasibility check operates on 144 binary-encoded nonnegative counters and a 12-vertex graph. For fixed C, q computation is polynomial in the encoded input length even when the fiber has exponentially many paths. Exact multiplicities may need Omega(m) output bits, so factorial/determinant execution is output-size sensitive; no poly(log m) claim is made for full D_C. Building J by a path stream costs O(m) sparse updates, storing its 144 counts costs O(144 log(m+1)) bits, and APPEND or a properly provenance-equipped CANCEL modifies at most three directed counts. This does not give constant-time recomputation of the full BRC endpoint mass.

## Executed exact evidence

The full standalone Python integer verifier implements (399.1) with exact Bareiss determinants, exact factorial division, the suffix transfer, and Stage398-B signatures. A complete comparison across all 21,845 words of lengths 0..7 over {±E1,±E2} gives 11,805 exact (m,z,J) fibers, all with identical signature multiplicities under the Euler transfer and direct enumeration. The Stage398-B *complete* n=8 fiber of six histories returns multiplicities [4,1,1], q=3. A second larger independent verifier (available as conversation research artifact) additionally checked six mixed-six-axis fibers, length 8/9/10 two-direction families, and direct native 12-direction BRC recurrences N_8(6E1)=288 and W_8^p(6E1)=20992 for weights (2,3,1,...,1). All tests used exact integers, never floating point. The full program ran twice with identical output; the shorter repository verifier was also run and produced the attached stdout.

This theorem addresses the path-formal future language, preserving native X6 axes, the source label, full joint J rather than marginalizing it, signed trace separately from positive mass and unchanged P000/frozen science. Its mathematical status is author proof plus finite exact checker, pending independent Driver review and native Source acceptance.

Next Stage400-B: exact coupled-source J_P,J_Q plus an explicit synchronized cross-source histogram, a minimal counterexample to unjustified product factorization (or exact conditions that justify it), and runtime accounting for the coupled suffix transfer.