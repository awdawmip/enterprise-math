# BRC-X6: shorter exact 9–13-policy optimal-support certificates (169-bit endpoint)

**Date 2026-11-09. Status: AUTHOR_PROVED / EXACT_INTEGER_AND_RATIONAL_VERIFIED / UNREVIEWED / NOT_ADMITTED.** Frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`.

## Precise theorem

Use the original 24 source/action indicator coordinates of the 38-vertex signed policy polytope, with source ports (6,7,28,29), signs (+,-,-,+), six native actions, nine frozen roots and complete one-step (next-port,R1..R6,K) signed atoms. Retain the previously proved linearly independent 13 original lawful 0/1 policy columns, ordered:

```
w0 =(0,0,2,2)   w1 =(1,0,3,2)   w2 =(2,2,4,4)
w3 =(3,3,5,5)   w4 =(4,4,0,0)   w5 =(4,4,5,5)
w6 =(4,5,0,1)   w7 =(5,1,1,3)   w8 =(5,5,5,5)
w9 =(0,0,0,0)   w10=(0,0,1,1)   w11=(0,0,4,4)
w12=(0,1,2,3)
```

Every prefix of lengths k=9,10,11,12,13 is linearly independent and the first nine columns cover every original source/action coordinate. Choose **B=2^14=16,384**, `D_k=Σ_{i<k} B^i`, and `x_k=Σ_{i<k} B^i w_i / D_k`. Then for **every k=9..13**, all 24 original coordinates of x_k are strictly positive and `minSupport(x_k)=k`.

The denominator sizes are now **113, 127, 141, 155, 169 bits** for k=9..13, compared with **201, 226, 251, 276, 301 bits** in the preceding base-2^25 certificate. The k=13 common denominator is **132 bits shorter**, while its original-native mathematical optimality is unchanged.

## Stronger exact determinant argument

For an n×n binary matrix A construct an (n+1)×(n+1) ±1 matrix with first row/column all +1 and lower-right entries 1−2A. Row subtraction shows `|det H|=2^n|det A|`. Hadamard on H gives the sharp-to-this-argument binary bound

`|det A| ≤ (n+1)^((n+1)/2)/2^n`.

For all 1≤n≤13, `|det A| < 12868` (the largest numerical upper bound, n=13, is `14^7/2^13=823543/64≈12867.859375`). As determinants are integers, every such absolute determinant is ≤12,867, and `B−1=16,383>12,867`.

To exclude a representation of x_k by at most k−1 of the 38 lawful pure policies, take an independent basis of its span and extend it to k−1 independent original binary columns (available because the full polytope has linear rank 13). Since w0..w(k−1) have rank k, at least one w_i is not in that span. Choose k original coordinate rows making the k×k determinant of the extended alternative columns and this w_i nonzero. With its last column varied, the resulting integer linear functional L vanishes on the alternative span but the integer coefficients `c_i=L(w_i)` are not all zero and satisfy `|c_i|≤12,867`.

If x_k belonged to the span, then `Σ_{i<k} c_i B^i=0`. At its highest nonzero coefficient j, the leading contribution has absolute value ≥B^j, while the total absolute value of lower powers is ≤`12,867(B^j−1)/(B−1)<B^j`. Contradiction. Hence at least k pure policies are required; the explicit positive k-term mixture achieves equality.

All relevant rows are original 24 native action coordinates, not an averaged or quotient observer. The theorem does not require enumerating all alternative subsets.

## Reproducibility and source status

A pure-Python exact verifier `verify_short_base_14_spectrum.py`, `SHORT_BASE_14_SPECTRUM_CERTIFICATE.json`, and the expanded mathematical proof are in the delivered portable bundle alongside the existing unchanged frozen kernel and `exact_min_support.py`. The verifier checks all 38 lawful pure policies under all nine frozen roots, 24-coordinate strict positivity, exact row sums, five prefix ranks, full original signed atom balances and integer determinant bound, then emits all four-by-six integer numerator matrices.

New proof SHA-256 `b176839c9992e597bfb714d2e3068a9c29e7db3e59015f857d1a2c685b5f41fd`; verifier `5a731ed31aaf4ffcf6f771e166e906dbf103a0ac98ff11f15d90817035a315c3`; exact output certificate `752e9f2c3cb491f4550e01120b60ebcd6a4a5873444d66764859de4cb9777f8b`; original frozen kernel `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`.

This is a **new certificate-size improvement** of an existing exact result, not a new proof that the D25 Source-native H0/B0/CM objective is complete. Source-native writer/provenance/checkpoint remains subject to its own valid session, CLAIM and task authorization.
