# BRC-X6: all 268 optimal decompositions of the uniform native first-step policy

**Date**: 2026-11-09 Asia/Hong_Kong. **Research role**: TASK_RESEARCH, author-only portable incremental result; **UNREVIEWED / NOT_ADMITTED**, no native Source claim, Result or independent review. **Frozen science pin**: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 96 ports, six labeled actions, complete seven-component step rewards `R1,...,R6,K` and the next native port; nine frozen roots `0, ±e1, ±e2, ±e3, ±e4`.

## New exact finite classification theorem

Preserve the four native source ports `P=(6,7,28,29)` with signs `(+,-,-,+)`. A deterministic preserving controller is a four-tuple of actions in `{0,...,5}^4` whose signed dictionary of original output atoms `(next port,R1,...,R6,K)` cancels *termwise*. Previous author-side exact work established there are 38 such pure controllers for each of the nine roots, the same 38 across all roots, and proved that the uniform policy `u[p,a]=1/6` requires **exactly six** preserving pure controllers.

**New result**: The uniform policy has **exactly 268 distinct unordered convex decompositions of minimal length six**. Each of the six coefficients is necessarily `1/6`. Classifying each selected controller as *nondiagonal* when `a_6 != a_7` or `a_28 != a_29`, the 268 optimal decompositions have exactly `0,2,3,4` nondiagonal controllers with counts respectively `120,90,40,18`; all other counts vanish. All 38 pure controllers occur in at least one optimal decomposition. Their participation-frequency histogram is `{20:6,30:6,42:21,71:4,142:1}`, totaling `6*268=1608` vertex occurrences.

## Proof and reproducible exact certificate

A pure controller has exactly four nonzero original action coordinates, one for each source port; uniform `u` has all 24 original coordinates positive. Exactly six pure controllers offer exactly 24 coordinate-coverage positions. Therefore every source action at every port occurs exactly once, and its unique controller weight must equal `1/6`. Conversely, any six preserving pure controllers whose actions are a permutation of `0,...,5` at **each** of the four source ports constitute an optimal decomposition. Ordering these six by first-source action `a_6=0,...,5` canonically removes the `6!` permutation ambiguity.

From the frozen native transition/reward function `edge(p,(slot,newbit),root)`, evaluate all `6^4=1296` candidate four-tuples, and retain exactly the 38 whose signed exact output-atom counts cancel. Verify the 38-element set is identical at all nine frozen roots. Let `V_i` consist of preserving four-tuples whose first action is `i`. For the remaining three ports use six-bit occupied-action masks `m1,m2,m3`. The integer recurrence

```
C(i,m1,m2,m3) =
    sum(C(i+1,m1|1<<v[1],m2|1<<v[2],m3|1<<v[3])
        for v in V_i
        if all((m[j] & (1<<v[j+1])) == 0 for j in range(3)))
C(6,63,63,63) = 1
C(6,anything_else) = 0
```

visits exactly **89 memoized states** and returns `C(0,0,0,0)=268`. Its branches are in bijection with all unordered optimal decompositions via the canonical first-action order, proving completeness and nonduplication. A separately implemented exhaustive set-cover backtracker reconstructs the native four-tuples from the frozen `edge` function without consulting the DP; it independently recovers all 268 decompositions and verifies equality of the complete six-tuple collection and the distribution. No floats, sampling, or approximate tolerances are involved.

For the 120 purely diagonal decompositions there is also an analytic count: the sole all-diagonal controller with first action 1 is `(1,1,3,3)`; first actions `0,2,3,4,5` match their second actions, and the common third/fourth actions freely permute `{0,1,2,4,5}`. Hence `5!=120). The other `148=90+40+18` optimal decompositions involve nondiagonal controllers and are certified by exhaustive exact native enumeration.

**Source-side reproducible package** (author-only): `frozen_native_kernel_prefix577.py`, `native_edge_snapshot.csv`, `verify_uniform_optimal_268.py` (integer DP plus independent enumeration), `independent_verify_uniform_268.py` (separate native exact-cover enumeration), `UNIFORM_OPTIMAL_268_CERTIFICATE.json` (entire explicit set of 268 six-tuples), this theorem, and `UNIFORM_OPTIMAL_268_MANIFEST.json`. Both programs passed fresh-directory rerun and file-hash verification. SHA-256 of the compact canonical matching array: `5cd0bcd92b514bf3685c3888c3a626e3a899d53eb5b03898ef6f654783e4b5c3`; exact JSON certificate SHA-256: `57d8d80680b14ef4c6061ca81ee2fe470f3412962156d860fa4e9cf65d5f9055`. Package SHA-256: `83e525ef121bd9b6ec50ca6ff08d8f8d196d69b696d1eea376df9fb28df4c4ef`.

**Novelty scope**: An exhaustive exact classification of *all* uniform-minimal mixtures, refining the prior theorem that the uniform point needs six and the full rational polytope has a sharp 13-term upper bound. No claim of arbitrary-network complexity or native D25 completion. Next portable scientific unit: exact minimum-support certificates for a supplied nonuniform rational policy; original D25 native H0/B0, Frobenius, kappa, CM and byte-exact UR-V2 writer/provenance remain distinct outstanding fronts.
