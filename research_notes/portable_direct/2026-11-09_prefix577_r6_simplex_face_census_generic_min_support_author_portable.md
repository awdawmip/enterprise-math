# BRC-X6 exact simplex-face census and generic minimum-support law (author portable)

**Author-side status:** AUTHOR_PROVED / EXACT_FINITE_ENUMERATION / UNREVIEWED / NOT_ADMITTED. Date 2026-11-09. Frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This source is not an original-task Source checkpoint, native RESULT, CLAIM, independent review or P000 promotion.

## Model and precise claim

In the frozen nine-root, 96-port, six-action BRC-X6 model, retain original source ports `(6,7,28,29)`, signs `(+,-,-,+)`, all 24 individual port/action probabilities and signed one-step atom `(next-port,R1,...,R6,K)`. The lawful pure controls form a set `V` of **38 original 24-coordinate 0/1 vertices** with a 12-dimensional convex hull `P`. The earlier complete 46,204-face lattice is used as a pinned input, and is rederived by intersecting all 24 nonnegative-coordinate zero masks.

Write `s(x)` for the least number of distinct pure lawful policies in a positive convex combination giving `x`. For any nonempty face `F` of affine dimension `d`, the exact exceptional set

`E_F = relint(F) ∩ ⋃_{S⊆V(F), |S|≤d} conv(S)`

is relatively closed, nowhere dense and has zero relative `d`-dimensional Lebesgue measure. **Every `x∈relint(F)\E_F` has `s(x)=d+1`.** In particular generic full-dimensional points have exact support 13; generic relative-interior points of an eight-dimensional face have exact support 9. Previously verified eight-face barycenters with support 7 or 8 lie in this explicitly described exceptional locus.

**Proof.** Since `F` is a face, a convex representation of `x∈F` by vertices of `P` uses only `V(F)`. Affine Carathéodory gives a representation with at most `d+1` vertices. If `s(x)≤d`, then `x` belongs to one of finitely many convex hulls of ≤`d` face vertices, each of affine dimension at most `d-1`. Those hulls are relatively closed, nowhere dense and measure zero. The complement is relatively open dense and full measure, where `s(x)>d`; hence `s(x)=d+1`. For `d=0`, the exceptional union is empty. This is a scoped finite-polytope theorem, not a universal complexity bound.

If `F` is a simplex, every `x∈relint(F)` has a **unique** pure preserving representation on its `d+1` vertices, so `s(x)=d+1` without exceptional points: all representing vertices lie in `F`, and its columns are affinely independent. The exact decomposition can therefore be recovered from the `d+1` original 0/1 columns by rational linear algebra, checking the 24 source/action coordinates.

## Complete census of simplex faces

A face is counted as a `d`-simplex precisely when it has `d+1` distinct original vertices. The exact census of all 46,204 faces (including empty face and `P`) gives:

| Dimension | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9–12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Simplex faces | 38 | 434 | 1,924 | 3,838 | 3,784 | 2,132 | 696 | 120 | 8 | 0 |

Total **12,974 simplex faces**, largest dimension **8** even though `P` has dimension 12. Eight maximal-dimensional simplex-face masks are:

`000001ff00`, `00003e0f00`, `008081f220`, `0080be0220`, `1008108f08`, `1088908228`, `2010210f10`, `2090a10230`.

The finite verifier reconstructed 38 preserving controls under all nine roots, generated the complete face set by 24 zero masks, matched the previous immutable face ledger, and checked full column rank for every one of the 12,974 simplex faces over prime 1,000,000,007. Integer 0/1 minors with `k≤9` satisfy `|det|≤k^(k/2)<1,000,000,007`, making the modular rank an exact rational-rank certificate. The eight 8D centroids were also solved as exact 9-term weight vectors `(1/9,...,1/9)`.

## Reproducibility and preservation

The author-side reproducible seven-source-file plus manifest bundle contains `frozen_native_kernel_prefix577.py`, `FULL_FACE_LATTICE_MASKS.txt`, `exact_min_support.py`, `verify_simplex_face_census.py`, `SIMPLEX_FACE_CENSUS_CERTIFICATE.json`, the full expanded theorem and continuation. An independent zip extraction/re-execution completed successfully using Python 3 standard library.

Evidence SHA-256: kernel `d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0`; prior face ledger `2a4fa0cbebd8828b3f05cae6cbd3804be5bd8b74b808ca96e87a6aa1f4433786`; new JSON certificate `2fd470a8e13a1bead9d0e42e9a9f099fea7b8060452939744a222ad9934cebcb`; verifier `65930305aca2a46d749db6511c06fa4d4371daa28b596e287a15b4a54176261f`; expanded theorem `c67fab31c52ffc934ca0ca8a84fa3c6f434402cc81882d0b0732a4cfd3085fac`; zip `ef358e4ed255969e9d34758a4b79d36eb83ee8714d4d3972f77e26096a132a33`.

Next exact scientific unit: exploit this geometry to prune minimum-support enumeration for general strictly positive rational policies and output exact compact infeasibility witnesses. Original D25 native `H0/B0`, divided-power Frobenius/CM work and original UR V2 four-file 94,687-byte SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` provenance recovery remain separate and unfinished. No predecessor Source `completed_units` or native writer authority is claimed by this portable work.
