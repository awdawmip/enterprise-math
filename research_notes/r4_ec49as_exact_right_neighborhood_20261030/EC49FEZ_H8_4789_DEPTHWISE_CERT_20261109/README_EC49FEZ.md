# EC49FEZ — H8-mixed 4789: exact 94-edge native-prefix obstruction

Date: 2026-11-09 (Asia/Shanghai). Scientific input frozen at \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Status: **author-side finite exact proof**, independent Driver acceptance pending. Applies the existing P000 native signed X6 and positive complete forward BRC key semantics. Earlier frontier: EC49FEU H8 census and EC49FEV–FEY pooled-key method on PR #1730.

## Mathematical statement

Among exactly 23 operation words with H2 low labels (1,2,4,8), H3 high labels (16,32), H4 high labels (16,32), H5 low quartet, H6 low quartet, H7 high pair, **H8 mixed type B (1,8,16)**, and H9 high pair, each word has horizon h, original nine-state observer label, native signed X6 endpoint (+2,0,0,0,0,0), and a positive **complete** BRC key (x,y,z). At most five distinct complete keys may be used, and labels of the same horizon may choose different keys. Let C_native count distinct nonempty **ordered signed microstep prefixes** in the union of these 23 words.

**Theorem:** Every such legal system has **C_native >= 94**. In EC49FEU's original five-key census for the late-high set {4,7,8,9}, there are 4,608 typed-B candidate inventories, **2,508** signature-feasible and 2,100 signature-infeasible. The exact prefix lower bound eliminates all 2,508 signature-feasible inventories from the <=93-edge target. The original operation/key involution I=(c d)(f g), J(x,y,z)=(y+2z,x-2z,z) supplies the same result for the corresponding type-C mixed support (2,4,32), also 2,508 signature-feasible typed configurations. Typed B/C counts are not a count of distinct untyped key sets.

## Why pooling is sound

For any legal word with high observation label 16 or 32, the original grammar forces #c+#d=0, so the complete BRC key obeys x+y=h+1. Five high-bearing horizons 3,4,7,8,9 consequently require distinct complete keys with sums 4,5,8,9,10. The high pair at H3 has the unique key (3,1,1). For each ordinary high-bearing h=4,7,9 allow *all* positive complete keys that admit both labels 16 and 32, and for mixed H8 allow all keys that admit label 16. Let K_pool be their union with (3,1,1). The exact enumeration gives **44 pooled complete keys**. Every original five-key inventory lies in this pool; allowing every word to use any pooled key is a relaxation. Thus a prefix lower bound in this larger universe is valid for every original inventory.

## A compact independent-of-solver certificate

Enumerate every original operation word for each of the 23 required (h,label) groups using the 44 pooled keys; the full domain contains **54,423** group-word instances. The six letters are a,c,d,e,f,g with signed native axis microsteps a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). Apply the original nine-state observer, not a coordinate-only projection.

Index groups g from 0 to 22, in ascending horizon and within horizon ascending required label:
0..3 = H2 labels 1,2,4,8;
4..5 = H3 labels 16,32;
6..7 = H4 labels 16,32;
8..11 = H5 labels 1,2,4,8;
12..15 = H6 labels 1,2,4,8;
16..17 = H7 labels 16,32;
18..20 = H8 labels 1,8,16;
21..22 = H9 labels 16,32.

For each signed microstep depth d, the attached certificate provides a chosen subset D_d of groups. Exact exhaustive checking establishes (i) every pooled word of every group in D_d has at least d microsteps and (ii) **no two distinct groups in D_d can have the same signed prefix of length d**, even if they choose different keys. Therefore each legal collection must contain at least |D_d| distinct prefixes at depth d. Prefixes of different lengths are distinct, whence

\[
C_{\mathrm{native}}\ge \sum_{d=1}^{20}|D_d|
=3+5+5+5+6+6+6+6+3+5+6+6+6+6+6+6+2+2+2+2
=\boxed{94}.
\]

The full 20-layer witness D_d is in \`EXACT_DISJOINT_H8_4789.json\`. There are **no floating-point weights or optimizer results in the load-bearing proof**. The independent Python-standard-library verification regenerates all pooled keys, original words, nine-state labels, six-axis endpoints and signed prefix sets, and checks every layer/group pair for collisions. Local result: \`EXACT_INTEGER_PASS\`, 23 groups, 20 layers, 54,423 endpoint/label checks, 72,070 group-word-depth checks and 50,113 distinct checked prefixes summed over layers. The exploratory \`depthwise.py\` (SciPy-based search) is available with the local evidence but is not needed to verify the certificate.

## Reproduction and limits

Run \`python3 VERIFY_EC49FEZ.py EXACT_DISJOINT_H8_4789.json\` with Python 3 standard library; it must print \`EXACT_INTEGER_PASS\` and the integer lower bound 94. Original counts and full pairwise-disjointness are recomputed, not trusted from the JSON.

This one H8/4789 structure is now fully excluded from the <=93 cost target. The other H8 structures and EC49FEY's open H7/5789,6789 structures remain concrete continuation units. In the H8 placement, the other tested depthwise-only lower bounds were 88 (4589), 72 (4689), 78 (5689), 82 (5789), and 90 (6789); those weaker bounds are exploratory sieve outputs, **not** exact optima. Next try improved group-prefix dual or coupled optimization on these survivors. The mother target remains <=5 complete BRC keys and C_native<=93; the existing 94-edge 22-word construction remains the best previously recorded mother-family witness.

## Identity, authorization, evidence

GitHub author-side contribution to the existing PR #1730 branch. Do not infer Source task CLAIM/Result or independent mathematical admission from this material. Native TASK_RESEARCH identity/owner must be determined from current service records. Complete standalone certificate and verifier are kept here for lossless reproduction. P000 and ACTIVE worldview are not modified.
