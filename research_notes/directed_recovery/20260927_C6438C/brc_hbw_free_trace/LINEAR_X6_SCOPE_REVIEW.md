# Fixed linear X6 scope: shared-context review

Status: **PURE_SYMBOLIC_REVIEW / NO_SCIENTIFIC_EXECUTION / NOT_ADMISSION**.

The full `LINEAR_X6_ORDER_SCOPE.md`, SHA-256 `ca04beb3a4b807d93337ac598615ebfa2f19e16a4da3f968880252fd7295eee1`, was read. No source was changed and no local-order instance was calculated.

**No substantive defect found.** Invertibility ensures every eigenvalue is nonzero. For each irreducible factor of degree d_i, all its roots lie in F_(p^d_i), so the semisimple block order divides p^d_i-1. A nilpotent Jordan part of size at most s_i is killed by p^e when p^e is at least s_i, by the characteristic-p binomial identity. The common p-power bound and the least common multiple of the prime-to-p bounds therefore give the displayed divisibility. A Jordan-block size of one has no unipotent factor; for p>d a nontrivial block needs exactly the stated possible factor p. The proof does not require constructing the splitting field or knowing p during the algorithm.

The scope distinctions are correct. Similarity cannot change the order. Repeating a fixed, predetermined composition still iterates one matrix. An affine map needs its charged homogeneous dimension increase before applying the theorem. State-dependent selection, nonlinear projective laws, branching observations and a varying curve family are not covered. Nor does the lemma constrain all possible proper-coordinate gcd hits before complete return.

For the regular determinant-one degree-two companion, the stronger p-1/p+1 restriction is correctly separate from degenerate unipotent cases. This helps reject redundant coordinate-search directions without claiming that factoring, BRC or Shor is impossible. It also explains why the proposed elliptic interface changes the geometric group rather than supplying a counterexample to this fixed-linear theorem.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
