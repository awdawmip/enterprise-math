# X6 LP011/LP026 — exact one-bit oriented native lift from a quadratic observer; five further live consumers

Date: 2026-11-13 15:00 Asia/Hong_Kong. Parent: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication \`TP2-B4A441B23DA3159232C2\`. Logical research lane: \`chatgpt-research-onhour-enterprise-math-20260923\`; author: existing Researcher \`EM-X6-FB6990\`, session \`MCP-082892eb480e45dea6d4b9fcc0491034\`. **NONBLIND / AUTHOR-PROVED / EXACT STANDALONE PYTHON PASS / UNREVIEWED / NOT_ADMITTED**. This note is research-side GitHub evidence; it is not Source PROGRESS, Driver review, a physical force law or an arbitrary displayed Cell-address codec.

## 1. Frozen inputs, existing progress and exact new question

Native P000 V5 signed six-axis Cell displacement over \(\mathbb Z^6\), full native component quadratic \(G(z)=\sum z_i^2\), shortest signed primitive-axis length \(T(z)=\sum |z_i|\), BRC shortest-word multiplicity \(M(z)=T(z)!/\prod |z_i|!\), and the full relative observer \(r=\rho(z)=z-\min(z)D\), \(D=(1,1,1,1,1,1)\). Current behavioral rules have been read independently from frozen scientific pins: X6 frozen source \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`, earlier plane historical reference \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`.

**Consume, do not reproduce as new:** \`research_checks/X6_LP026_QUADRATIC_DEPTH_RECOVERY_20261112_ONHOUR.py\` (observed Git blob \`f555d0c9213186987b82ecbd42b96cd095bb661f\`) already proves/implements the at-most-two-branch quadratic recovery from \((r,G)\). The 14:00 manuscript \`research_notes/X6_LP011_LP026_SIX_AXIS_L1_PLATEAU_SIGNED_DOMINANCE_OBSTRUCTION_20261113_1400.md\` (blob \`2ead839c5e487f1cd811706962720f1c94bde06b\`) already gave the \(M=3\) collision despite equal relative, length, norm, BRC and median signs. The present increment builds a **working, type-checked positive repair interface**: what is the smallest extra signed-origin observation sufficient for all six native axes, and can it directly decode signed LP011 dominance and LP019 shortest BRC count?

## 2. Exact construction and proof for every signed integer six-vector

Let \(r\in\mathbb N_0^6\), \(\min r=0\), \(R=\sum r_i\), \(Q=\sum r_i^2\), and let the native norm readout be \(g=G(z)\). Every lift is \(z=r+hD\) with unique integer \(h\). The quadratic equation is

\[
g=Q+2Rh+6h^2,\quad
W:=R^2+6(g-Q)=(R+6h)^2=S^2,\quad S=\sum_i z_i.
\]

If \(W<0\), \(W\) is not a square, or neither \(h_{\pm}=(-R\pm\sqrt W)/6\) is an integer, there is no lift. Otherwise there are **at most two** candidate native depths; both are verified against \((\rho,G)\). For valid native data, the single bit

\[
b=\mathbf 1[\sum_i z_i\ge 0]
\]

selects the unique candidate whose \(S=R+6h\) has the declared sign. If \(W=0\) there is only one candidate with \(S=0\) and \(b=1\). If \(W>0\), the two branches have \(S=+\sqrt W\) and \(S=-\sqrt W\); they cannot have the same bit. Therefore \((\rho,G,b)\) determines **the exact raw signed six-axis displacement** and hence any function of it, including the full signed dominant-axis set and shortest positive BRC path count, for every \(z\in\mathbb Z^6\). The bit is necessary on two-lift fibres, but need not be transmitted for a uniquely liftable fibre.

**Precision and information scope:** \(b\) is an additional externally supplied native observation; it is not derivable in general from \((\rho,G)\). This is an exact state-decoder for a displacement only: it does not reconstruct the order/provenance of primitive words, a future force law, or final nonnegative Cell address. Full BRC multiplicity is a derived integer observable; huge factorial computation is not claimed constant cost. The decoder itself uses O(6) integer arithmetic and integer-square-root operations, with bit complexity depending on the input magnitude. The known ambiguity is resolved rather than denied.

Explicit prior obstruction repaired:
- \(x=(-1,-1,-1,2,2,2)\), \(y=(-2,-2,-2,1,1,1)\).
- Both have \(r=(0,0,0,3,3,3)\), \(G=15\), \(T=9\), shortest BRC \(M=45360\).
- For both, \(W=9\), valid depths \(-2,-1\), while \(b(x)=1\), \(b(y)=0\). The decoder returns \(x\) and \(y\) respectively; the signed dominant sets are \(\{(+4),(+5),(+6)\}\) and \(\{(-1),(-2),(-3)\}\).

## 3. Actually executed exact checker

File \`research_checks/X6_LP011_LP026_NATIVE_G_ORIENTATION_BIT_RECONSTRUCTION_20261113_1500.py\`, current committed executable Git blob \`30a54ff32d657a1344902506d2b7e30d140aa0f1\`, 4,451 UTF-8 bytes, local SHA256 \`d783de1b02c1136a94316c28cb9ecb9da0acd74f6eb4f2fa8af416130002df8d\`. This same blob was actually executed by local Python with exit code zero; stdout begins \`PASS_X6_LP011_LP026_NATIVE_G_ORIENTATION_BIT\`.

Exhaustive signed input domain: all \(7^6=117649\) vectors \(z\in[-3,3]^6\). Each checks exact \(\rho,G\), all quadratic depths, identity of the decoded native vector, signed dominant-axis set, native shortest BRC, and opposition of the bit across two-lift fibres. 29,886 source points have two integer norm-compatible global depths (the counterpart need not lie within the finite input cube), 28,962 of these have different signed dominant-axis outputs across the two global branches, and 110,824 different \((\rho,G)\) keys occur within the cube. The original \(M=3\) BRC-45360 collision is tested explicitly. Four bad-input cases are rejected without Python bool-int coercion.

A separate large-exact-integer test with \(M=10^{45}\), \(x=(-M,-M,-M,2M,2M,2M)\), \(y=(-2M,-2M,-2M,M,M,M)\) recovers both via the one-bit quadratic decoder without enumerating all depths. No BRC factorial is attempted at that huge scale (no false resource claim). Finite test verifies implementation; the algebra above establishes all integer inputs. This is a **standalone scientific checker**, not a newly run original X6 project import, native benchmark or independent Driver validation.

## 4. Five previously unlisted current executable consumers, full source-body inspection

These five GitHub main files were read completely this turn. Bounded inspection is not equivalent to running their original programs, and does not by itself prove all-repository dependency closure.

| Current path | Observed blob | Specific relevant code and disposition |
| --- | --- | --- |
| \`research_checks/X6_LP026_CYCLIC_G_RECOVERY_TYPED_ADAPTER_20261112_ONHOUR.py\` | \`76ba970283e4f1f65f47f17cf76e40752c612d9a\` | Lines 10–27 enumerate exact reachable depths and reject G-ambiguous cover fibres. **KEEP**; it computes norm constancy, does not claim to recover native direction from \((\rho,G)\). |
| \`research_checks/X6_LP026_CYCLIC_G_FAST_INTERVAL_RECOVERY_20261112_ONHOUR.py\` | \`496764aa8ebdb19bb03b7d40b82128a82be0ed84\` | Lines 29–88 use parity-aware convex L1 depth bounds and strict-quadratic G ambiguity; lines 91–106 provide independent linear comparator. **KEEP**; its target is native norm, not signed dominant orientation. |
| \`research_checks/X6_LP026_CURRENT_SOURCE_CONSUMER_IMPORT_20261112_1600.py\` | \`769a7b6801436bc3b14a8f810f9caae4edd9ba2a\` | Lines 16–29 pin native imported code, 45–58 distinguish canonical quotient, native signed endpoint fibre and shortest word kernel; explicit positive-only vs signed enumerations. **KEEP / source inspection only**. |
| \`research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py\` | \`db46dde5a962b93b65775bf2b4d8f52d5e3f83b9\` | Lines 45–64 preserve native start, ordered axis pair and signs; lines 68–97 distinguish 60 chart descriptions, true signed endpoints and shortest BRC mass. **KEEP**; no arbitrary X6 shell promotion. |
| \`research_checks/X6_LP026_CYCLIC_COVER_FINITE_HORIZON_SHARP_20261112_ONHOUR.py\` | \`c2b28585f8ea41b43d0b311ab0d87eda38393786\` | Lines 8–25 distinguish finite-depth cyclic observer and native G/BRC witnesses; lines 27–84 compare bounded reachable fibres. **KEEP** within its finite horizon. |

Earlier **30 disjoint** current executable source inspections are retained as existing evidence; these five additional paths give 35 explicitly identified inspected current executable files, not 35 independently run original regressions. The 820 filename-matched paths in the earlier manifest are a selection pool, not a proved total dependency count. No actual erroneous live call site was shown by these five; no speculative patch to frozen P000, source modules, or old accepted Results is made.

## 5. Current custody and remaining parent obligations

Highest published Source scientific PROGRESS receipt \`onhour-20261113-1437-x6-l1-native-progress-publish\` was actually read this turn and is **SUCCEEDED**, \`canonical_publication_verified=true\`, Source commit \`78c792cd68e9413f1b20a54a41c1dd6cc7f39a2d\`. Its checkpoint already contains the 14:00 proof and author checker; they must not be uploaded/published again. Original session \`MCP-082892eb480e45dea6d4b9fcc0491034\`, Researcher \`EM-X6-FB6990\`, CLAIM \`MCP-bdd4acf9d96a8f1f0dfab4e9\`, RUN \`RUN-756de85b94c23b46b181f7b8\`. Original fresh reads \`onhour-20261113-1500-x6-continuation-check\` and \`onhour-20261113-1503-x6-own-task\` were QUEUED/RUNNING when inspected; read original terminal receipts before any new authenticated write. Neither a Source read projection nor an old run ID grants current CLAIM/lease authority.

Next exact task action: reconcile those read requests; if own winning claim is live, resume the same RUN under the original managed Research session and save/publish the above newly committed author evidence using the current generation/revision contract. Continue remaining **actual** current consumers and frozen-source historical LP011 native signed dominance / LP019 positive path-count cancellation provenance; for each verified bad live caller patch and execute the original source checker, otherwise keep truthful line-bound scope. Present the actual finite source-corpus closure and residual to the independent Driver's \`REQUEST_REVISION\`; do not fabricate old provenance or acceptance.

**Do-not-repeat:** original 516299 Cover regression, 58989 coordinate regression, native signed BRC integration/side-register benchmarks, previously inspected 30 executable consumers and 23 August definitions, prior \((\rho,G)\) two-branch theorem, prior 14:00 six-axis L1 plateau counterexample, previous Source-published PROGRESS and Research Activity checkpoints. **Unresolved:** full active dependency closure, historical LP011/LP019 attributable wrong callers, independent Driver disposition, current native checkpoint for this new repair.
