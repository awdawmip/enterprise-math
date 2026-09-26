# Shared-context review of the strong compiled-word Shor theorem

Status: AUTHOR SHARED-CONTEXT CROSS-CHECK / UNREVIEWED / NOT_ADMITTED.
Activity: RA-CAAAC604CB513AEA8BBC1DFC.

This is a directed read-and-proof check by the author of the effective compiler
note. It is not an independent reviewer role, a theorem admission, an actual
compiler run, or validation of a complete variable-word factorization driver.

Reviewed `STRONG_SHOR_COMPILATION_THEOREM.md` SHA256
`aad6256b52974a020ce4769584d781daccbe5ba285aade5ae7d2f8db4cb528fa`.
Supporting effective compiler note SHA256
`30c52a650332e4536217e5ed6bd54e1ef8fa790cd16a6da1529f00924af1ae04`.
Also read the fixed-alphabet density proof, the frozen Stage79/80 exact
interfaces, and the success/tree invariants in
`completion/SUCCESS_AND_COMPLETION_THEOREM.md` and
`integration/COMPLETE_FACTORIZATION_PROOF.md`.

## Finding

No substantive overclaim or mathematical defect was found in the reviewed
theorem at its explicitly stated symbolic and conditional scope. The following
links were checked rather than inferred from the small executed examples.

1. **Effective termination.** Density in SO(61) supplies approximations in
   Frobenius norm as well, by equivalence of the finite-dimensional norms. The
   target half-angle branch has convergent rational enclosures from actual
   typed polynomial probes. A strict upper error witness eventually accepts
   any word with a positive error margin. Fairly interleaving finite words and
   observer depths therefore terminates, including when other candidates lie
   exactly on the threshold. A length-only search that endlessly refines one
   such candidate would not have this guarantee; the reviewed theorem does
   not use that incorrect procedure. Symbolic termination is distinct from a
   bounded execution returning CERTIFIED or PARTIAL.

2. **Full columns and retained residuals.** The target is a planar phase
   direct-sum I_59, while every actual candidate is a complete 61-mode word.
   A complete Frobenius certificate bounds operator norm on arbitrary inputs,
   including residual-bearing and reference-entangled states. Agreement only
   on the clean first two input columns would not suffice. The reviewed
   theorem explicitly uses the stronger complete-carrier certificate.

3. **Controlled error.** Controlled letters compose into the controlled word
   because retained control sectors do not mix. Its operator error is the
   error of the active block and is not multiplied by the number of work
   labels or spectators. This conclusion uses operator norm, not an incorrect
   equality of enlarged and base Frobenius norms. The inherited all-column
   source catalog supplies the finite controlled letter operations.

4. **Occurrence budget and terminal TV.** For even t>=2,
   M=t(t-1)/2 is positive and counts all phase occurrences. Choosing each
   strict error below epsilon/M gives a total error at most epsilon; exact
   quarter turns only improve it. Unitary telescoping remains valid after
   earlier words populate residual modes. Vector distance bounds pure-state
   trace distance, and a common measurement or fixed postprocessor contracts
   this distance. The ideal joint law is explicitly that of the augmented
   realified circuit; only its control marginal is identified with ordinary
   Shor. The statement does not misidentify extra internal labels as ordinary
   Shor outputs or claim to have numerically executed the ideal circuit.

5. **Streaming equivalence.** The schedule proof uses complete linear maps
   controlled by retained labels, so it is not specific to a rank-one formula
   or the K33 bank. Classical records can be kept coherently for the error
   proof and then measured; subsequent controlled maps preserve those labels.
   Internal carrier operations remain separate from the shared H4 spectator,
   so the existing even-width return invariant still applies. No intermediate
   conditional-state normalization is needed to establish the TV bound.

6. **Original-CF success.** The existing ideal proof uses Q>=N^2>r^2 and the
   strict CF criterion, keeping the true order denominator within cap N-1.
   Its phi(r)/r>=1/n estimate follows from distinct-prime counting and does
   not require runtime order input. The good-unit proportion and exact gcd
   precheck give the random-base ideal bound 1/(8n) on {2,...,N-2}; deleting
   endpoints 1 and N-1 removes bad bases. The uniform readout TV epsilon=
   1/(16n) therefore leaves actual success at least 1/(16n). This is an
   attempt bound under fresh conditionally uniform randomness, not a claim
   that every fixed base has that factor-success probability.

7. **Retry and full-tree failure allocation.** A block of 16n attempts has
   all-failure probability below one half under the conditional lower bound,
   so 16n*b attempts give at most 2^(-b). The number of stochastic attempt
   nodes, including nodes that exhaust retries, is at most Omega(N)-1 and
   hence at most floor(log2 N)-1. One can see this by extending each unresolved
   composite leaf to a hypothetical full prime-factor tree: it has at least
   two prime factors, so its already attempted split can be assigned an
   internal node of that full tree. Perfect-power compression and deterministic
   preprocessing cannot increase this count. Thus b=s+ceil(log2 n0) and fewer
   than n0 nodes give total retry-failure probability at most 2^(-s), even
   when node values depend on earlier random outcomes. This is conditional
   union accounting, not an unjustified independence assumption across nodes.

8. **Correct outputs and interruption scope.** Exact prime, perfect-power,
   divisibility, multiplicity and product certificates support each reported
   factor independently of probability assumptions. Retry failure never
   proves primality. Compilation caps, missing random bits or explicit base
   lists are separately reported and cannot inherit the uniform retry
   theorem automatically. Rejection sampling is almost-sure finite, not a
   deterministic upper bound on external random bits. The theorem retains
   these distinctions.

9. **No efficiency or transcript overclaim.** A polynomial number of retry
   attempts does not bound the cost of exhaustive word compilation, O(N)
   work labels, exact large integers, or the Wilson baseline by a polynomial
   in log N. Whole-transcript TV needs the separate sum of conditional round
   budgets stated in the theorem. The symbolic all-finite-input construction
   does not establish a single finite bank for all widths, a practical
   all-input run, physical Born sampling, or six-axis hardware realization.

The dependency on the author-level density and effective-compiler proofs is
material and explicit. The independently checkable bounded native reflection
word is useful source binding, but it is not by itself an empirical proof of
density or universal compilation. No new numerical test was performed for this
review. A future implementation still requires its own full native execution
and error-observer receipts under the newly declared algorithm profile.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
