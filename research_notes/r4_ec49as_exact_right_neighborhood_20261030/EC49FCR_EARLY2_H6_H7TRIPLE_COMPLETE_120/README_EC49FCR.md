# EC49FCR — exact five-path rigidity for every H6-containing early pair + H7 triple

2026-11-06 · **Author-side finite exhaustive theorem** · Not independently reviewed/admitted.

## Frozen science and exact question

Science pin: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.
Parent: EC49FCQ at Git commit \`e8d311f268cdd416aa61d892ca23a6be5d31f1b9\`, PR #1730.
Frozen candidate model: \`frozen_model.py\` Git Blob \`c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b\` (same exact OPS/T/SIG/STEPS/ENC/REQ/W/candidates/build semantics as the model actually executed from earlier EC49FCN evidence ZIP, with a different docstring).
All 24 original observation slots, their signed ordered native primitive-step prefix expansions, the original nine-state observer signatures, and fixed BRC key multisets \`L=(4,2,1)\` / \`M=(7,3,2)\` are retained. H2/H3 words are fixed.

Take **two** slots from H4/H5/H6 with **at least one H6 slot**, and **three** of the four H7 slots; keep the remaining 19 witness words fixed. For the five selected slots, allow all words in \`frozen_model.candidates(h)[signature]\`, and measure the number of distinct nonempty *ordered, signed primitive-step prefixes* across all 24 words. There are
\`(C(10,2)-C(6,2))*C(4,3)=(45-15)*4=120\`
distinct groups.

**Theorem (finite, frozen candidate language).** The exact minimum is **158 prefix edges for every one of the 120 groups**. Together with EC49FCQ's disjoint 60 groups, the **entire early-two + H7-triple subfamily (180/180 groups)** is now certified at 158 within this fixed model.

## Exact exhaustive argument

For selected group S, let \`F\` be the union of signed primitive-prefix sets of the 19 fixed words. Let \`R_i(w)=P(w)\F\` for a permitted replacement word w in selected slot i. Put \`c=158-|F|\`. Every possible complete solution has cost
\`|F|+|R_1(w_1) union ... union R_5(w_5)|\`.
The original witness satisfies all constraints and gives cost 158. Therefore a strict improvement exists exactly when the union of five selected residual sets has size <c.

For each slot, enumerate its complete frozen candidate pool. Starting from \`A_0={emptyset}\`, form all unions \`a union r\` with \`a in A_{i-1}\`, \`r in R_i\`, discard those with size >=c, and retain only inclusion-minimal sets in \`A_i\`. This is exact: whenever \`a subset b\`, for every subsequent union \`t\` one has \`a union t subset b union t\`. Thus replacing b by a cannot lose any possible strictly-improving completion, and pruning at size >=c is safe by union monotonicity. All finite candidate pools are generated from exact integer multiset and automaton rules; there is no numerical approximation.

The actually executed bitset implementation returned empty final antichains \`A_5\` for **each of indices 0–119**; hence no legal five-slot replacement improves 158. The existing witness gives the matching upper bound. This closes precisely the stated finite subfamily.

## Actual execution / evidence

- Executed source \`VERIFY_EC49FCR_H6_H7_BATCH.py\` saved here **byte-for-byte**; Git Blob SHA1 \`a11b5f9d0101aa3b9f2a5b5427571143af6e9bab\`. The frozen generator used in the runs came from the previous local evidence bundle (Git Blob SHA1 \`7e97065ac9a0ff70435b92ee2f4bd718c9bf1859\`) and shares all mathematical functions/constants with the published \`frozen_model.py\` (Git Blob \`c21336ba1f3719cfa03b07c3a7e9722e4cd1e84b\`).
- Exact runs: indices \`[0,4)\`, \`[4,20)\`, and \`[20,120)\`. **120/120 completed**; bitset strictly improving groups: **0**. Independent literal signed-prefix \`frozenset\` representation verified **6/120** indices (0–5), with identical stage-by-stage antichain sizes, fixed-edge count, and improvement existence. Literal verification is not claimed for the other 114.
- Full 120-group per-index JSON certificate is \`EC49FCR_FULL_120.json.gz.b64\` (base64(gzip(JSON))). Uncompressed UTF-8 JSON bytes SHA256: \`0c53a7301bae354921d4b8785d6c9cd130717d3050a753c5b5a28b3a112c2638\`; compressed-text Git Blob SHA1: \`a51c33d50a4f3fc72096c10e7b22d6e01cb14641\`.
- Each group records ordered slot IDs, full unpruned candidate Cartesian product count, fixed-edge count, strict improvement threshold, every inclusion-minimal stage's state count, the improvement flag and whether an independent literal test was actually performed.
- Sum of unpruned candidate tuple products: **13,756,055,040,000**, *not* the number of actual enumerated tuples. Maximum intermediate bitset antichain size **576**. Total result rows **120**, distinct and exhaustive with index range \`0..119\`.
- To reproduce: \`python VERIFY_EC49FCR_H6_H7_BATCH.py --start 0 --stop 120 --literal 6 --output EC49FCR_CHECK.json\`. To decode: \`base64 -d EC49FCR_FULL_120.json.gz.b64 | gzip -d > EC49FCR_FULL_120.json\` (then SHA256 compare). Runs were split to limit execution time; no runtime/performance improvement claim.

## Scope, limits, and next move

This covers the declared frozen \`OPS\`, nine-state transition/signature table, fixed L/M cache keys, selected witness words, and their signed primitive-step expansions; it is **not** an all-X6 unrestricted optimality result, a global 158-edge lower bound under arbitrary cache-key rearrangement, nor a resolution of the nine-window 93-edge mother goal. Those remain open research routes, not negations of the useful finite certificate.

The predecessor reported 7,812 disjoint author-side five-path groups. Adding these 120 yields **7,932** reported disjoint groups (subject to the preceding distinctness/evidence ledgers), including the newly completed early-two/H7-triple 180 groups.

Current source readings: global canonical main \`d606788d60cb4f4cc1a7fc644ff9256ad5f06ed4\`; Enterprise Math main \`83459850569e002f8e1277bfb91fb309281e08e7\`; artifact source is the independent immutable PR branch commit, preserving the scientific pin above. P000 and protected ACTIVE worldview unchanged. BRC usage: **REUSE_EXECUTED** for exact key multiset/observer constraints and retained signed ordered path provenance, no positive-mass-only quotient.

Real control: GitHub operation actor \`awdawmip\`. New native researcher session request \`ec49fcr-r4-20261106T2130-auth-01\` returned \`FAILED / OSError\`; the current task inventory request \`ec49fcr-r4-20261106T2130-tasks-01\` returned \`WAITING_RESOURCE / EVENT_COLLECTION_IO / OSError\`. No valid current Source Researcher-ID, verified active owner, CLAIM, Result or independent Driver mathematical acceptance was obtained. This is a **portable author research artifact**.

Next scoped scientific work: \`NEXT_EC49FCS.md\`.
