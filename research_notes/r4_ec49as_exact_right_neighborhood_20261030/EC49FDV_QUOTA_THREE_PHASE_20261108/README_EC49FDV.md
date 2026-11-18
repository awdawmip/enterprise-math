# EC49FDV — Exact quota refinement of three-phase BRC key schedules

**Research date:** 2026-11-08 (Asia/Shanghai). **Immutable scientific input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Author-side parent:** EC49FDU, commit `73c954d996082450c632f7150688ec1de0473375`. Mathematical acceptance and native Source Result require separate review.

## Complete finite theorem

Use the original ordered signed native-X6 operations `a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`, with complete positive BRC key `(x,y,z)`, terminal displacement `+2E1`, the six allowed nine-history observer signatures, exact rational observer rank nine and all nonempty signed primitive prefixes counted once. At horizons H4,…,H9 require exactly `(2,4,2,4,4,2)` distinct accepted complete operation words. In this theorem **each horizon uses a single complete late key** and exactly three distinct late keys occupy three nonempty contiguous horizon blocks.

Among EC49FDU's 6734 genuinely-three-key rank-feasible triples, **exactly 64 distinct triples support the exact word quotas and rank nine via such a three-block schedule**. Each has precisely one viable three-block schedule. Both switchpoints are forced: after H4 and H6. The complete result is the Cartesian product A×B×C with

```
A (H4)       = {(3,2,1),(4,1,1)}
B (H5,H6)    = {(3,4,1),(5,2,2),(6,1,1),(6,1,2)}
C (H7,H8,H9) = {(4,6,1),(5,5,1),(6,4,2),(7,3,1),
               (7,3,2),(8,2,1),(8,2,2),(8,2,3)}
```

Hence `2×4×8=64`, and 6666 of the 6730 previously found one-key-per-window rank-only triples fail an exact quota. The four additional EC49FDU H4-mixed exceptions are outside this one-key-per-horizon theorem.

**Proof.** The exact six-operator-count and nine-state integer DP exhaustively enumerates every `(h, complete BRC key, six-bit observer signature)` accepted-word multiplicity. The original rational-rank-nine criterion on a signature union is the four-clause mask condition `18,20,33,40`. With two words, the two distinct signatures `16` and `32` are both necessary and sufficient. With four words, an admissible rank-nine subset of size at most four can be padded to four distinct accepted words whenever at least four are available. The numbers of rank-nine singleton-key choices at H4,…,H9 are `9,17,28,43,62,86`; with required quotas they become `2,17,6,43,62,16`. Valid X6 operation counts satisfy `a=z-1, e=z, c+d=x+y-h-1, f=h+1-y-2z, g=h+1-x`, hence `x+y≥h+1`. The only two H4 quota keys both have `x+y=5`, forcing a switch at H4. All six H6 quota keys have `x+y=7`, forcing a switch at H6. Exhaustive DP intersections `Q4`, `Q5∩Q6`, `Q7∩Q8∩Q9` yield exactly A, B and C. All 64 resulting triples satisfy every required rank and quota. This is complete for the declared family.

## Explicit full-system witnesses and independent verification

For each of the 64 late schedules, a deterministic literal signed-X6 word generator constructed two full H2–H9 witnesses extending the two early 2-key seeds `(ce,ed,ge | feg,gef)` and `(de,ec,fe | feg,gef)`; an added H2 word uses the same two early keys. The 128 full witnesses each contain **24 complete words** with horizon quotas `(4,2,2,4,2,4,4,2)`, exactly five distinct positive BRC keys, all six global signatures, exact displacement `+2E1`, and exact nine-history rational rank nine at each horizon. An independently implemented `Fraction` Gaussian eliminator validated **128/128 witnesses and 1024/1024 horizon ranks**. Signed native-prefix costs of these deterministic, not optimized constructions are **126–221**, minimum 126. The independent previously known 94-edge system remains the mother-problem upper bound; the `≤93` target is still open.

## Complete executable evidence (four-part lossless archive)

**All proof exposition, exact DP Python, literal generator, independent verifier, 64-schedule JSON, 128 complete 24-word witness JSON, validation receipts, source pin, SHA256 manifest and unchanged EC49FDU checker are in the four adjacent `EC49FDV_full_sources.tar.xz.b64.part0{1..4}` Git files.** Each file is UTF-8 Base64 text; concatenate in part-number order and decode. The original XZ tar archive SHA256 is:

```
e122ef832f709d9b7428411d4bebab247eb8c37d59e1a5eebac27d03dd469b17
```

```sh
cat EC49FDV_full_sources.tar.xz.b64.part0* | tr -d '\n' | base64 -d > EC49FDV_full_sources.tar.xz
sha256sum EC49FDV_full_sources.tar.xz
tar xJf EC49FDV_full_sources.tar.xz
python EC49FDV_QUOTA_CENSUS.py
python EC49FDV_NATIVE_WITNESSES.py
python VERIFY_EC49FDV_INDEPENDENT.py
```

All calculation code uses the Python standard library. Existing published EC49FDU signed-X6 and observer semantics are retained, with the science pin unchanged. No P000/ACTIVE-worldview or Source Result/Review changes are asserted.

**Next EC49FDW:** optimize signed primitive-prefix sharing over these 64 exact-quota late schedules; vary the early four-word seed and intra-window key mixing; compare directly against the 94-edge systems, and independently validate any `≤93` witness.
