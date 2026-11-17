# X6 Unit87 — direct signed BRC certification beyond the first finite-cover return alias

Date: 2026-11-17. Parent: \`PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905\`; task: \`RS-X6-LEGACY-PLANE-RECONCILIATION\`; publication: \`TP2-B4A441B23DA3159232C2\`.

**Author evidence:** AUTHOR-EXACT / INDEPENDENT INTEGER CONVOLUTION EXECUTED / SOURCE-CONSUMER-INSPECTED / UNREVIEWED / NOT_ADMITTED. No authenticated X6 native semantic PROGRESS or Research Activity claim is made.

## Scope and new conclusion

Continue the frozen signed-native P000 V5 \`Z^6\` Cell displacement model, twelve distinct labeled primitive moves \`+e_i/-e_i\`, min-zero relative observation \`rho\`, and derived finite-depth readout \`C_m(z)=(rho(z), min(z) mod m)\` for integer \`m>=1\`. Set \`A_L(h)\` to the **nonnegative integer** count of length-\`L\` primitive words ending at signed native displacement \`h*(1,1,1,1,1,1)\`. Write \`R_m(L)=sum_{h in m Z} A_L(h)\`; \`R_0(L)=A_L(0)\` denotes exact native Cell return.

Unit86 established the first alias at \`L=6m\`. The next nonzero alias is exactly two native events later:

\`\`\`text
R_m(6m+1)-R_0(6m+1) = 0
R_m(6m+2)-R_0(6m+2) = 12*(6m+2)! / ((m+1)!*(m!)^5)
\`\`\`

At \`6m+2\`, every nonzero diagonal endpoint admitted by \`C_m\` is either \`+m*1\` or \`-m*1\`: the next \`2m\` diagonal requires \`12m > 6m+2\` for \`m>=1\` except \`m=1\`, where \`12>8\` also holds. For each chosen sign and each of six possible axes, a word achieving \`m*1\` uses exactly \`m+1\` moves in the chosen direction and one reverse move on that axis, and \`m\` chosen-direction moves on each other axis. Its labeled multinomial count is \`(6m+2)!/((m+1)!(m!)^5)\`. Six axis choices and two endpoint signs give the formula. Odd-length diagonal returns vanish because total primitive word length has even parity for all multiples of the six-axis diagonal.

The first-two nonzero-alias masses have an exact relative growth factor:

\`\`\`text
[R_m(6m+2)-R_0(6m+2)] / [R_m(6m)-R_0(6m)]
= 6*(6m+2)*(6m+1)/(m+1).
\`\`\`

This identifies the actual **positive BRC mass** folded into cover return at the second viable horizon, not a signed subtraction or a Cell identity.

## Independent executed certificate

The checker \`research_checks/X6_UNIT87_FINITE_COVER_SECOND_ALIAS_CHECK_20261117.py\` computes each \`A_L(h)\` by independent axis-interleaving convolution, recursively combining \`j\` events on one axis and \`L-j\` on the remaining axes with binomial shuffle factor \`C(L,j)\`. It does not call Unit85 or Unit86's dynamic programming, and does not enumerate the full six-dimensional endpoint table. Exact integers only.

The checker executed in ordinary Python, Python \`-O\`, and Python \`-OO\`: identical serialized outputs, \`failures=0\`; 95 pre-alias/odd-horizon equality comparisons, and independently recomputed first and next-even aliases for each \`m=1..5\`.

| Cover modulus | first L | first extra BRC words | next nonzero L | next extra BRC words |
|---:|---:|---:|---:|---:|
| 1 | 6 | 1,440 | 8 | 241,920 |
| 2 | 12 | 14,968,800 | 14 | 5,448,643,200 |
| 3 | 18 | 274,450,176,000 | 20 | 156,436,600,320,000 |
| 4 | 24 | 6,493,341,074,220,000 | 26 | 5,064,806,037,891,600,000 |
| 5 | 30 | 177,665,292,119,576,701,440 | 32 | 176,243,969,782,620,087,828,480 |

Unlike Unit86's earlier formula-only large-horizon values, these cover-return coefficients at lengths 18, 20, 24, 26, 30, and 32 were actually computed by this independent six-axis integer convolution. This is **not** a complete native six-dimensional endpoint-table benchmark.

## Current real consumers and meaning

- \`experiments/x6_native_coordinate_completion_v7_20260905/x6_cover.py\`, Git blob \`171baf1cee7f1aceaf38c73d0c0659a25fd8d7bd\`, lines 41–87: \`CoverState\` exposes \`coordinate_observation\`; \`signed_native_displacement\` rejects all finite moduli. Lines 99–105: \`first_positive_diagonal_return\` counts **macro six-axis loops**, not signed BRC path return mass. No defect in this type boundary was found.
- \`experiments/x6_native_coordinate_completion_v7_20260905/x6_coordinate.py\`, blob \`9738543aace13f8a72af577e9ad8964c5fd40de8\`, lines 136–167: \`brc_endpoint_multiplicity\` handles **positive-only relative words**, not signed native path counts.
- \`experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py\`, pinned blob \`300a96e3dc24bf6fff73743037a0347a8bc83176\`, lines 35–58: \`endpoint_multiplicity\` counts the original signed 12-operation BRC endpoint words, including non-minimal returns.
- \`experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py\`, blob \`5d0f2cb88a0d4e437b5025e9050e3044f7831cd4\`, lines 19–35, 91–105, 137–145: its signed count is a family of **triadic 3-at-once events**, distinct from signed primitive-axis words. These formulas retain positive multiplicities, not erroneous negative cancellation.
- \`src/enterprise_math/p022_geodesic_multiplicity.py\`, blob \`46373050168d2430b6cb3952aa763f3081284632\`, lines 69–84: simple-cubic shortest-path multiplicities are correctly restricted to geodesic words and do not count arbitrary longer signed path returns.

No read current call site establishes an LP011/LP019 historic erroneous path. Forensic attribution remains \`UNRESOLVED_PROVENANCE\`; Driver may consider \`REQUEST_REVISION\` based on original source evidence, not this author's review authority.

## Durable controls and next mother action

Frozen science: P000 \`59538f585d037d09ef687b28715c4bc1a3f9fe03\`; historical corpus \`fd2bcff10ca6e147348b6c1236027fc0d2877df3\`; native signed BRC \`300a96e3dc24bf6fff73743037a0347a8bc83176\`. Unit85–86 main-author results retained as independent predecessor evidence, not recomputed or admitted anew.

Original research lane historical SID \`MCP-082892eb480e45dea6d4b9fcc0491034\`, CLAIM \`MCP-579c8e23625448582b421831\`, RUN \`RUN-fb25028676f9692ab1bacaee\`, Activity \`RA-5E3FE1E761E4963EC461A892\` at last-verified 106 events; no authenticated current writer binding. Original read requests \`#6994\` and \`#6995\` are terminal \`SUCCEEDED\` and unmodified. No task dispatch, new CLAIM/open, review, schedule or native Result mutation.

**Next precise scientific action:** inspect another real unreviewed X6 consumer that uses endpoint return, cover identity or triadic branch counting, record source blob, arguments, observer and expected output algebra; repair only a proven current defect. Deliver LP011/LP019 provenance determination with source:line if found, otherwise retain documented unresolved status for independent Driver. Native R063/Helly benchmarks remain the original object and verification scope.
