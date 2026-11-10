# BRC-X6 native nine-root D=14 integer saturation and twelve-policy theorem

**2026-11-10 · AUTHOR_PROVED / EXACT_FINITE_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**

Original frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Four source ports `(6,7,28,29)`; signs `(+1,-1,-1,+1)`; six *labeled* actions per source; original nine roots and all 81 signed root/edge/observer channels; 38 lawful deterministic policies. Native six-spatial-axis P000 remains in force. The exact source kernel is unchanged.

## Precise theorem and strengthened denominator bound

Let `C ∈ {0,1}^{24×38}` denote the incidence matrix of the **full set of 38** lawful deterministic four-port policies. Let `W ∈ Z^{81×24}` be the original complete nine-root signed conservation map, without replacing the joint observer by a marginal observer.

For **every** `b ∈ Z_(>0)^24` with source-wise six-action numerator sums equal to **D=14** and `W b=0`, there exists `n ∈ Z_(≥0)^38` satisfying:

```
C n = b;  sum_j n_j = 14;  number of distinct j with n_j>0 <= 12.
```

Combined with the previously proven D=6,...,13 finite ranges under this same frozen scientific model, this gives

```
D_reduced <= 14  =>  minSupport(b/D) <= 12.
minSupport(b/D) = 13  =>  D_reduced >= 15.
```

The earlier constructive 13-minimal instance of reduced denominator 1023 supplies the existing upper bound; the remaining search for a least possible reduced denominator is therefore within 15...1023.

## Exact proof, part 1: eight-unit native integer saturation

The uniform vector `J=(1,...,1) ∈ Z^24` obeys WJ=0 and has source-wise action sum six. For any positive D14 target put `r=b-J`; then `r>=0`, each port's action histogram sums to eight, and `Wr=0`.

A six-action nonnegative histogram of total eight has `binom(13,5)=1,287` possibilities. Exact two-port / two-port meet-in-the-middle on the *original 81 signed labeled channels* enumerates precisely **8,866,429** distinct four-port invariant residual vectors.

Independently enumerate all **215,553,195** multisets of 8 lawful policies, i.e. `binom(45,8)`, add their original 24-dimensional incidence vectors and deduplicate. There are exactly **8,866,429** distinct images. Every image necessarily has source total eight and W-invariance, so the image set is included in the invariant set; the exact equal finite counts prove equality. A separate 11-dimensional integer left-nullspace enumerator tested every conserved residual for membership and found **zero holes**.

Original nine-root W has rank 9. Appending three independent equal-source-mass rows yields rank 11, equal to the orthogonal rank of the native 24×38 matrix C (rank 13), validating the fixed-row-sum equivalence between the two exact enumeration contracts. The direct original 81-channel verifier and the C++ nullspace verifier are independent implementations.

## Exact proof, part 2: at most twelve *distinct* policies

There are precisely **268** legal six-policy complete covers of the uniform vector J. Every one of the 38 lawful policies belongs to at least one of these covers.

Make an undirected 38-vertex graph G: policies i,j are adjacent iff some legal complete six-policy cover contains both. G has 423 edges out of the 703 possible distinct pairs.

Exact bitset Bron-Kerbosch enumeration of all maximal independent sets of G gives 78 sets, with sizes

```
size 3: 36   size 4: 26   size 5: 4   size 8: 12
```

There is no independent set larger than eight, and there are **exactly twelve** independent eight-policy sets. For any eight-policy decomposition of r:

* If a policy appears twice, choose any J perfect cover containing it. The combined 14-term representation has no more than `6+7-1=12` distinct policies.
* If all eight residual policies differ but any two share a J cover, choose that cover. The combined representation has no more than `6+8-2=12` distinct policies.
* Otherwise, the residual eight-policy set is one of the exactly twelve independent sets enumerated above. For **each of those twelve sets**, an explicit alternative 14-unit exact integer representation of `J+r` was found using exactly **10 distinct lawful policies**. The certificate lists each 24-coordinate target and each nonnegative integer coefficient; a standalone Python verifier recomputes every integer equality from the frozen lawful policy tuples, without trusting the numerical MILP discovery process.

These cases exhaust all eight-policy residual representations and establish the theorem.

## Independent verification record

```
D=12 m=6 valid=784536 integer_representable=784536 integer_nonrepresentable=0
D=13 m=7 valid=2804920 integer_representable=2804920 integer_nonrepresentable=0
D=14 m=8 valid=8866429 integer_representable=8866429 integer_nonrepresentable=0
         distinct_multiset_policy_images=8866429
         raw_lawful_eight_policy_multisets=215553195
NATIVE_9ROOT_81CHANNEL_D14_EXACT_COUNT_PASS 8866429 keys 189837 root_count 9
maximal cliques count 78 by length {3: 36, 4: 26, 5: 4, 8: 12} size8 12
D14_EXCEPTION_WITNESSES_PASS 12 each support=10, exact 24-coordinate equality
```

Reproducible **14-file** companion author package, produced with exact C++ and Python and freshly unpacked for rechecking:

```
BRC_X6_D14_NATIVE_12SUPPORT_EXACT_AUTHOR_PORTABLE_20261110.zip
SHA256 = 88a31c60bf0522f705a7bbae814e13ce0976a096c1f94be27019ac79d6b8702d
D14_EXACT_SATURATION_12SUPPORT_CERTIFICATE.json
SHA256 = da5ededeb666416c3b322be758d9e9cc7aa3889fc71209f1bc9cc551ae45d6f2
D14_12_INDEPENDENT8_EXACT_WITNESSES.json
SHA256 = e469142bbe533f8aab58161fe17e8660673377afad378be0b89237dfcd0dd57f
Inherited frozen_native_kernel_prefix577.py
SHA256 = d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0
```

The companion ZIP is an author portable conversation attachment, not a claim that the ZIP bytes have been uploaded to the repository. All evidence statuses here refer to exact finite computation and explicit integer witnesses, not to Source-native mathematical admission.

## Provenance and continuation

This is a new D14 extension of earlier author evidence, not a reproof of D6..13. The immediate predecessor proof is:
`awdawmip/enterprise-math@26a84984d49f317df28d9d4ed8501150c32834ec:research_notes/portable_direct/2026-11-10_prefix577_r6_native_D13_integer_saturation_12support_author_portable.md`.

Next mathematical unit: test D=15 nine-root, full-positive integer invariant fibers with a memory-bounded exact strategy; then determine whether any candidate actually requires 13 policies. The parent D25/LIFT/JT2 still awaits native H0/B0 divided-power and [X]U modulo p² data plus semilinear Frobenius normalization. Own current session/CLAIM is not verified, so neither this note nor a client-scoped checkpoint is represented as Source Result/admission.

UR V2 four-file original bundle recovery remains pending: **94,687 bytes**, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`. Completed UR mathematics is not repeated.
