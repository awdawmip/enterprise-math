# BRC-X6 full-support pure-policy minimum-support spectrum: exact 10–13-term witnesses

**AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.** Extends immutable author result `1b3c0cb723f3fcf95a17dee32a763c843f520052:research_notes/portable_direct/2026-11-09_prefix577_r6_nine_term_exact_minimal_support_author_portable.md`, without changing earlier Source frozen science `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native 96 ports, 576 labeled actions, complete `(next_port,R1,...,R6,K)` signed observation, all 9 frozen roots. Four source ports (6,7,28,29), signed (+,-,-,+). Each preserving deterministic policy is a four-action tuple. All 38 admissible tuples are regenerated from original frozen kernel SHA-256 `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`.

## Exact construction

Take the first nine preserving vertices from the parent author note, in this exact order:

```
w0=(0,0,2,2) w1=(1,0,3,2) w2=(2,2,4,4)
w3=(3,3,5,5) w4=(4,4,0,0) w5=(4,4,5,5)
w6=(4,5,0,1) w7=(5,1,1,3) w8=(5,5,5,5)
```

Append four further preserving vertices:
```
w9=(0,0,0,0)
w10=(0,0,1,1)
w11=(0,0,4,4)
w12=(0,1,2,3)
```

Let `B=2^25=33,554,432`. For each `k=9,10,11,12,13`, define `D_k=sum_{i=0}^{k-1}B^i` and the original 4x6 policy `X_k=(sum_{i=0}^{k-1} B^i w_i)/D_k`, where each four-action tuple denotes its 24-dimensional one-hot source-labeled vector.

**Theorem:** For every integer k in {9,10,11,12,13}, the 24 action probabilities of X_k are strictly positive, each row sums to 1, all 9 roots preserve the entire signed native output distribution, and **minSupport(X_k)=k**.

The first nine vertices already cover every one of the 24 original source-action coordinates; adding further vertices preserves full support.

## Complete exact affine independence certificates

Augment the 24-row binary vertex-coordinate matrix with a top row of 1s, indexed row 0. For each k the indicated k rows and the first k columns have determinant ±1:

| k | Rows (zero-based including augmentation) | Determinant | D_k bit length |
|---|---|---:|---:|
| 9 | 0,1,2,3,4,5,8,11,13 | -1 | 201 |
| 10 | 0,1,2,3,4,5,8,11,13,15 | +1 | 226 |
| 11 | 0,1,2,3,4,5,8,11,13,14,15 | -1 | 251 |
| 12 | 0,1,2,3,4,5,8,11,13,14,15,17 | -1 | 276 |
| 13 | 0,1,2,3,4,5,7,8,11,13,14,15,17 | +1 | 301 |

**Rigorous minimality lemma.** In any finite collection of 0/1 vertices with binary augmented columns, suppose k chosen augmented columns are linearly independent. Any at-most-(k-1)-vertex alternative representation lies in an augmented column span of rank r<=k-1. Some selected column lies outside that span, hence a suitable (r+1)x(r+1) minor defines an integer linear functional L annihilating the alternative span but not all selected columns. On any binary column `|L| <= (r+1)^((r+1)/2) <= k^(k/2) <= 13^(13/2) < 17,403,308`. Because `B-1=33,554,431`, a nonzero integer polynomial `sum_{i<k} L(w_i) B^i` has a highest nonzero term strictly larger in absolute value than all smaller terms combined; it cannot vanish. Therefore X_k does not belong to the affine span, and hence not the convex hull, of any k-1 vertices. The displayed positive k-term combination gives the opposite bound. This proves exact equality for every k, without probabilistic or floating-point inference.

All 5 certificates are full native, not passive averages or quotients. Native computations enumerate 9x1296 source four-action candidates, verify the common 38 preserving vertices, and check exact joint-atom balances for every selected constructed policy. Integer Bareiss and independent reconstructed kernel/SymPy checks agree. The full author's portable certificate `NINE_SIMPLEX_FACE_CERTIFICATE.json` includes every 24-coordinate positive integer numerator and exact denominator for k=9..13, plus minor rows and signs. The accompanying local research package has both verifiers and frozen kernel.

Earlier author results established strict-positive minSupport 6,7,8. Combining those existing instances with the five present explicit instances, **each integer minimum support 6 through 13 occurs for some strict-positive native preserving policy**. In particular, this 13-term witness has 301-bit denominator and directly uses 13 preserving actions; the earlier base-`2^26` 38-vertex construction's denominator has roughly 963 bits.

These are author-side exact mathematical witnesses; no live Source execution authorization or independent review is asserted. D25 native H0/B0, Frobenius/CM and UR V2 original four-file provenance remain separate unfinished work. Next: an exact minimum-support solver for arbitrary rational 24-coordinate policies, with verifiable infeasibility certificates.
