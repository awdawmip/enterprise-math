# R037 R033/R034 independent replication audit — review return

- Task: `RS-R037-R033-R034-INDEPENDENT-ALGORITHM-DATA-REPLICATION-AUDIT`
- Publication: `TP2-FEE5990D460CCB106345`
- Claim: `CLAIM-R037-20260906T0652Z-CHATGPT-05`
- Researcher-ID: `EM-R037-5F8E99`
- Execution branch base: `main@9bc95577902f14e1539b1849ed9c4e31a155fa54`
- Review target: PR #812, head `87d617a90d81b6197d521699512e1894db4346d8`
- Frozen R033 owner head: `c2aa1758c6cf8f194d8b4493b90c903a2dfcd048`
- Frozen R034 owner head: `674fb8717d753cd36fd83b061c869d79e8875b31`
- Review mode: durable-frontier review only; completed R033/R034 derivations were not replayed.

## Verdict

`PASS_MATHEMATICAL_AUDIT_WITH_PROVENANCE_QUALIFICATION`

I find no theorem-critical mathematical mismatch in the evidence frozen by PR #812. The evidence grades used there are materially appropriate, provided the R034 portion is **not** described as provenance-clean blind replication. The prior partial frozen-script exposure is a process/provenance defect, not a mathematical counterexample; it cannot be retroactively removed from this run.

Driver recommendation:

1. Accept the mathematical replication grades in PR #812 at their stated scopes.
2. Retain the all-radius exposed-face `S^2` statement and the pointwise nonperiodic heat-kernel/local-CLT statement as open/theorem-candidate only.
3. The Barlow return/root-local-spectral gauge statement is reviewable as exact only in the frozen ideal bi-infinite, uniform-nearest-neighbor scope.
4. Do **not** grant the combined R034 run the label `provenance-clean blind independent replication`.
5. If that strict provenance label is an independent acceptance requirement, reissue **only R034** to a fresh zero-exposure executor; R033 does not need reissue on the present evidence.

## 1. R033 evidence-grade review

The principal exact identities are internally consistent. In particular, for FCC

`A_r = 10 r^2 + 2`,

`V_r = (10 r^3 + 15 r^2 + 11 r + 3)/3`,

and direct symbolic differencing gives `V_r - V_{r-1} = A_r`. The intrinsic scalar `A_r^3/V_r^2` has limit `90`. For the even HCP branch, the stated shell/volume leading coefficients give limit `189/2`.

The topology claim is correctly graded as finite evidence: PR #812 certifies the exposed-face complexes through `r=20`, but does not provide an all-radius shelling/induction. Therefore the all-`r` `S^2` statement must remain `THEOREM_CANDIDATE_ONLY`; no promotion is justified from the finite certificate alone.

The Euclidean-form `5/2` and `21/8` quantities are also correctly fenced as calibration-dependent readout constants. They are not classical-pi identities.

## 2. R034 radial-moment review

Let `R=|X|^2`, `a=X·V`, `|V|=1`, with zero conditional drift and `E[a^2|X]=R/3`. Then

`R' = R + 1 + 2a`

implies

`E[(R')^2|X] = R^2 + (10/3)R + 1`,

which yields the frozen common fourth moment

`E|X_n|^4 = (5n^2-2n)/3`.

For sixth order,

`E[(R')^3|X] = R^3 + 7R^2 + 7R + 1 + 8 E[a^3|state,X]`.

Using the frozen independent certificate's HCP signed-cubic transfer `E[C_next]=-1/432`, the per-step HCP/FCC sixth-moment difference is `8(-1/432)=-1/54` after the initial step. Hence

`M6_HCP(n)-M6_FCC(n)=-(n-1)/54`,

and symbolic substitution verifies both closed forms in PR #812 satisfy the corresponding recurrences exactly. This part of the audit is mathematically coherent.

## 3. Barlow gauge upgrade review

The upgrade is logically valid at the stated scope. After basal Fourier transform, legal ideal Barlow stacking changes only the phase of the interlayer hopping while the magnitude is fixed. The layer adjacency graph is the line `Z`, so it has no cycles and therefore no gauge-invariant flux. Fixing the diagonal gauge at the root (`u_0=1`) and recursively removing each edge phase gives a root-preserving unitary equivalence to the same Jacobi fiber

`J_q = alpha(q) I + beta(q)(S+S*)`.

Consequently the root fiber spectral measure, and after basal-momentum integration the all-time root return probabilities/root local spectral measure, are stacking-independent in the ideal bi-infinite uniform-NN model.

This argument does **not** produce a physical-coordinate vertex permutation, because the gauge depends on momentum `q`. Therefore it cannot be widened to pointwise nonperiodic heat-kernel equality, a uniform local CLT, or disappearance of physical angular dispersion. PR #812 states this boundary correctly.

## 4. Provenance review

The R034 run records that a metadata lookup exposed part of the frozen experiment patch before the independent implementation was complete. The frozen script was not executed/imported as the computation engine, and the returned mathematical certificates were regenerated independently, but the preferred zero-exposure ordering was violated.

Accordingly two propositions must remain separate:

- **Mathematical replication status:** supported at the evidence grades frozen in PR #812.
- **Strict blind/provenance-clean status:** failed for the combined R034 run.

A fresh R034-only reissue is necessary only if the second proposition is itself an acceptance gate. It is not necessary merely to preserve the mathematical evidence already obtained.

## 5. CI and artifact consistency

PR #812 head `87d617a90d81b6197d521699512e1894db4346d8` has 19 recorded GitHub check runs. The primary `test`, `check`, and inspected unit shards are completed with `success`; no `failure` or `cancelled` conclusion was found in the check-run payload inspected for this review.

The PR return, machine-readable evidence matrix, spectral/moment derivation certificate, and mismatch/provenance report agree on the same boundaries:

- mathematical mismatches: `0`;
- all-radius boundary `S^2`: not promoted;
- pointwise nonperiodic heat-kernel/local-CLT: not promoted;
- Barlow root-return/local-spectral gauge: exact only in the frozen ideal-NN bi-infinite scope;
- strict R034 blind provenance: `false`.

## 6. Terminal disposition

`SUCCESS / REVIEW_COMPLETE / AWAITING_DRIVER_DECISION`

The durable frontier is now sharper rather than reopened: the Driver can decide the mathematical acceptance and the provenance-label requirement independently. No broader ontology, Working Truth, Foundation consequence, continuum identity, or classical-pi claim is authorized by this review.