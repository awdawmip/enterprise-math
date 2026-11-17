# X6 Unit83 — exact signed/positive BRC quotient-fiber discrimination at a real consumer seam

Date: 2026-11-17. Parent \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`, Task \`RS-X6-LEGACY-PLANE-RECONCILIATION\`, publication \`TP2-B4A441B23DA3159232C2\`.
Classification: **AUTHOR-EXACT / FINITE-EXECUTED / SOURCE-CALL-SITE-INSPECTED / UNREVIEWED / NOT_ADMITTED**. This is an independently preserved scientific/source-evidence note, **not** an authenticated X6 Activity or Native Source progress, and not a fresh accusation that a historical caller is erroneous.

## Actual unresolved mother-task question

The legacy LP019 ledger labels a supposed illegal signed cancellation of natural positive BRC counts but has no source line identifying that operation. LP011 similarly lacks a verified historical *native signed* dominant-axis caller. Unit82 audited 47 dated historical documents and seven other executable sources without finding those callers. This Unit83 inspects a **different** frozen executable seam: the true signed 12-direction BRC kernel versus the correct 6-direction positive/min-zero quotient kernel, and a current direct native consumer.

Frozen scientific source commit: \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`. The P000 V5 six-axis signed Cell domain is retained; the positive paths are a separately typed carrier. Only a chosen Cell-relative displacement is modeled, not a global geometric origin, a final Cell address, or an additional spatial axis.

## Exact result and proof

In \(\mathbb Z^6\), let \(\rho(z)=z-\min_i(z_i)\mathbf1\) and, for each three-element index set \(I\subset\{1,\ldots,6\}\), define
\[
r_I(i)=\begin{cases}0&i\in I,\\1&i\notin I.\end{cases}
\]
There are \(\binom63=20\) distinct observers \(r_I\). Use the genuine **signed** primitive vocabulary \(\{\pm e_1,\ldots,\pm e_6\}\) at exact path length \(L=3\). The complete endpoint fiber at that length consists of exactly
\[
z_-=r_I-\mathbf1\quad\text{and}\quad z_+=r_I.
\]
To prove completeness, any endpoint in the fiber is \(r_I+h\mathbf1\), \(h\in\mathbb Z\). Its minimal signed step length is
\[
T(r_I+h\mathbf1)=3|h|+3|1+h|.
\]
A length-three word can reach it only if \(T\le 3\); the only integer solutions are \(h=-1,0\), and both endpoints have exactly three nonzero unit displacement coordinates. Their shortest-path natural BRC counts are \(3!=6\) each. Hence the signed pushforward at the specified observer is
\[
\boxed{\rho_*N_{3}^{\mathrm{signed}}(r_I)=6+6=12.}
\]

Now change the **path language**, not merely the observer: use only the six positive primitive directions \(+e_i\), at the same length \(L=3\). Every endpoint \(n\in\mathbb N^6\) satisfies \(\sum_i n_i=3\). If \(\rho(n)=r_I\), then \(n=r_I+h\mathbf1\), so \(3+6h=3\), giving the unique depth \(h=0\). This valid positive caller has exactly one endpoint with mass \(3!=6\):
\[
\boxed{N_{3}^{\mathrm{positive-relative}}(r_I)=6.}
\]
**Consequently, directly substituting the positive six-step quotient multiplicity for the signed twelve-step quotient pushforward undercounts by a factor of two on each of these twenty observer fibers.** This is a **cross-carrier typing counterexample**, not negative signed cancellation. Both source kernels below are correct within their separate declared domains.

General algebraic family (not a P000 dimension change): in \(2m\) signed integer coordinates, taking \(m\) zero and \(m\) one entries at length \(m\) yields signed fiber mass \(2m!\) versus positive fiber mass \(m!\), by the same \(m(|h|+|h+1|)\) argument.

## Actual source lines and consumer types

| Exact frozen/current path | Blob SHA-1 | Inspected source lines | Typed operation |
|---|---|---|---|
| Frozen \`experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py\` | \`300a96e3dc24bf6fff73743037a0347a8bc83176\` | 20–32, 42–54, 56–76 | Signed 12-step shortest, all-length and positive-rational weighted count; signed endpoint \(\mathbb Z^6\) |
| Frozen \`experiments/x6_signed_native_spatial_v16_20260905/x6_signed.py\` | \`ac32f6d82a91db99297e587cf63b0df95cece514\` | 26–31, 140–158 | Exact positive six-step path words and relative \(\rho\) with **length determining common depth** |
| Frozen \`experiments/x6_signed_native_spatial_v16_20260905/check_signed_brc.py\` | \`eadc2640e190165020a60a707ac5a14c497036a0\` | 23–32, 44–46, 55–61 | Actually invokes signed 12-step kernel, retains positive integer multiplicity, no signed subtraction |
| Frozen \`experiments/x6_signed_native_spatial_v16_20260905/check_x6_signed.py\` | \`275f327b603a9b07f8f6c0948347e75028d3a38a\` | 103–121 | Actually invokes six-positive-step multiplicity and the relative quotient at **fixed positive length**, valid in its domain |
| Current \`experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_rebase.py\` | \`406b1eea574ac3235c490dc362ce76d4b072458e\` | 24–26, 53–54, 103–123 | Explicitly loads \`signed_brc.py\` and uses \`shortest_path_multiplicity\` on **signed three-axis embeddings**; yields signed \(G=25\) count 846, not quotient-positive substitution |
| Current \`experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_crossfile.py\` | \`25f520df1e29bdd466fe76c6c00e3789c5606e27\` | 15–30, 32–43 | Tests that min-zero relative observer is not a native identity and preserves separate signed native BRC facts |

The two current consumers were read at main on 2026-11-17; frozen sources retain their immutable historical pin. The direct, inspected consumers **do not** contain an instance of the forbidden positive-for-signed substitution. The hypothetical invalid call has now been made numerically precise; attribution to an actual historical LP019 wrong caller **remains UNRESOLVED_PROVENANCE**. LP011 alleged historical argmax caller remains unresolved too. Do not rewrite a correct current consumer or promote an unlocated old allegation into a confirmed code defect.

## Reproducible finite execution and limits

Portable independent checker: \`research_checks/X6_UNIT83_QUOTIENT_SIGNED_POSITIVE_DISCRIMINATOR_20261117.py\`. Machine-readable certificate: \`research_checks/X6_UNIT83_SIGNED_POSITIVE_QUOTIENT_RESULTS_20261117.json\`. A fresh local Python run executed the full two language recurrences through length 3, checked all 20 index sets and 102 explicit conditions, with zero failures. Original totals: signed \(12^3=1728\) labeled words and positive \(6^3=216\). The counts of observer signatures across all length-three words are respectively 284 and 56. Normal Python, \`-O\` and \`-OO\` produce identical certificate SHA256 \`d5ba0b430650e82353ef2f2ca8c4322e008827cffbdd89addc29bf3209018ffe\`. The checker uses explicit exceptions for its verification conditions; \`-O\` does not disable them.

The proof is universal for the declared 20 fibers and general \(2m\) construction; the 1728/216-word check is an independent finite verification, not proof of a stronger all-length native experiment. Neither the original R063 nor Helly native benchmark was re-run. No claims about other programs or historical repositories beyond inspected paths follow from this bounded source trace.

## Next exact mother-task action

Trace real current argument flow beyond the inspected direct \`signed_brc\` consumer: identify a call site that passes a min-zero/positive quotient value into a downstream **signed-native** output (if any), with exact path/line, input domain, observer, operation and a reproducible failing witness. Audit the remaining frozen historical \`research/\`, \`src/\` and downstream pathways without redoing Unit82's 54 blobs. If no actual wrong caller is found after agreed bounded scope, provide this evidence to independent Driver for \`REQUEST_REVISION\` of LP011/LP019's unsupported attribution, preserving valid lower-layer mathematics.

Control identity/source continuity: original X6 author SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`, claim \`MCP-579c8e23625448582b421831\`, run \`RUN-fb25028676f9692ab1bacaee\` are historical references **without current writing authority**. The bridge recovery request \`onhour-20261117-1100-x6-own-recovery-status-v1\` (#6994) projected another D25 session; exact X6 continuation \`onhour-20261117-1103-x6-exact-task-continuation-v1\` (#6995) was read-only, \`execution_authorized=false\`. Original Research Activity \`RA-5E3FE1E761E4963EC461A892\` remains unchanged at 106 entries. No CLAIM, native PROGRESS, Driver review or Result is asserted.
