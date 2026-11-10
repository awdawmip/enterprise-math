# BRC-X6 原生二策略交换生成整个整数关系核

**2026-11-10** · Frozen science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` · `AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED`.

This proof is a new author-side algebraic science unit continuing the D16 integer saturation theorem (GitHub `252cc9e7386c2e2dfb3c85b2e43fa3d18e1b5b2a`) and the independent eight-perfect-cover theorem (`7b29a40075624d11a2d043832dbc86a07c835ed0`). No Source session/CLAIM/Result or independent review is asserted.

## Model and exact theorem

Use the same original 96 source-action ports, in particular four signed source ports (6,7,28,29), signs (+,-,-,+), six distinct action labels at each source, nine frozen roots, and their **81 raw signed joint-flow conservation channels**. Full native screening of the 1296 ordered four-action choices yields precisely the following **38** legal deterministic policies, indexed by tuple lexicographic order 0..37:

```
0000 0011 0022 0044 0055 0123 0420 0521
1032 1133 1430 1531 2200 2211 2222 2244 2255
3300 3311 3322 3344 3355 4002 4103 4400
4411 4422 4444 4455 4501 5012 5113 5410
5500 5511 5522 5544 5555
```

For each legal policy `j`, let `C_j∈{0,1}^{24}` be its four-source incidence column and let `C=[C_0 ... C_37]∈Z^{24×38}`.

An **exact quadratic exchange** is `e_i+e_j-e_k-e_l∈Z^{38}` with `C_i+C_j=C_k+C_l`; repeated indices are allowed. Then:

```math
\boxed{\ker_{\mathbb Z}(C)
 = \operatorname{span}_{\mathbb Z}\{e_i+e_j-e_k-e_l:
 C_i+C_j=C_k+C_l\}.}
```

**Stronger:** 25 explicitly selected exact quadratic exchanges below form an **integer basis** of this entire lattice, not merely a rational spanning family.

## Complete finite enumeration and explicit unimodular certificate

All unordered pairs with repetition `0<=i<=j<38` total `741`. Group them by their exact 24-coordinate sum `C_i+C_j`. There are `605` distinct sums: `472` singleton classes, `130` double classes, and `3` triple classes. Thus there are `133` nontrivial collision classes and `278` oriented nontrivial exact quadratic replacements.

For each collision class, take its **first** lexicographically enumerated pair as anchor and form one exchange row `e_i+e_j-e_k-e_l` against each other pair in the class. This creates `136` nonzero integer rows `Q_r∈Z^{38}`. Order classes by the first encounter when scanning pair indices `i<=j` lexicographically; within each class order by pair indices.

The original 24×38 integer incidence matrix has exact rational rank **13** (verified with fraction-only Gaussian elimination). Hence `rank_Z(ker_Z C)=25`. Choose the following zero-based row indices of `Q` and zero-based strategy coordinate indices:

```text
R = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,30,31,32,37,40,41,42]
L = [0,1,2,3,4,5,6,8,9,10,12,13,14,15,17,18,19,20,22,23,24,25,26,27,28]
```

Exact **integer Bareiss** elimination on this explicit 25×25 matrix gives

```
det(Q[R,L]) = -1.
```

For additional reconstruction, the selected 25 rows, in the same order, are pair identities (left pair = right pair):

```text
(0,13)=(1,12); (0,14)=(2,12); (0,15)=(3,12);
(0,16)=(4,12); (0,18)=(1,17); (0,19)=(2,17);
(0,20)=(3,17); (0,21)=(4,17); (0,25)=(1,24);
(0,26)=(2,24); (0,26)=(6,22); (0,27)=(3,24);
(0,28)=(4,24); (0,34)=(1,33); (0,35)=(2,33);
(0,36)=(3,33); (0,37)=(4,33); (1,35)=(7,30);
(2,9)=(5,8); (2,10)=(6,8); (2,11)=(7,8);
(2,23)=(5,22); (2,29)=(7,22); (2,31)=(5,30);
(2,32)=(6,30).
```

Every row is in `ker_Z C` by the exact coordinate identities. Their 25-coordinate projection has determinant -1, so they span a saturated direct summand of `Z^{38}` of rank25. That lattice lies in `ker_Z C`, itself of rank25. Saturation plus equal rank implies equality: **these 25 quadratic exchanges are a Z-basis of the full integer relation kernel.**

## Direct D16 application: an exact nonnegative exchange path

Use the previous 10-policy sharp witness `S=(12,13,17,22,24,25,29,30,31,32)`, six-cover `F=(7,9,16,20,24,30)`, and `b=J+sum_{j∈S} C_j`, where `J=(1,...,1)`. The exact four original source action rows are:

```
[1,1,3,2,5,4]
[3,2,3,2,4,2]
[6,6,1,1,1,1]
[5,4,3,2,1,1]
```

The initial `J` cover plus these 10 policies has 16 tokens across **14** distinct legal policies. Just two coordinate-preserving nonnegative 2-for-2 replacements reduce distinct support from **14→12→10**:

```
(12,25) -> (13,24)
(22,32) -> (24,30)
```

An explicit checked **13-step** series of the same original-native quadratic exchanges gives a second **9-distinct** representation (nonnegative integer coefficients):

```
(5:1), (11:1), (13:3), (17:1), (20:1),
(23:1), (24:4), (30:3), (37:1).
```

Their coefficients sum to 16, all 24 integer action coordinates match b and every step preserves all 81 signed joint-flow channels. This is a constructive *nonnegative path for this witness*, not a statement that all nonnegative fibers are connected. The distinct support is **at most 9**, not a claimed optimum.

## Reproducibility, boundaries, next question

The author independently reconstructed the 38 legal native strategies from the nine original roots and raw 81 signed joint keys, checked all 741 unordered policy pairs and group cardinalities, `rank C=13` via exact rational arithmetic, and `det(Q[R,L])=-1` using a standard-library **integer Bareiss** procedure. Another direct standard-library checker verifies all 13 exchange steps including their nonnegativity and the exact 24-coordinate invariants. No floating point or substituted marginal observer was used.

The **12-file conversation-local reproducible ZIP** (original frozen kernel, three original-native integer checkers, exact JSON certificates and both theorem texts) has SHA256 `5753de734621d1bfba346d7203a11b658a8678c65cdbacfffac2735432b3f7b4`. The ZIP is not separately represented as GitHub-published by this note.

Next scientific unit: exploit the *complete integer kernel basis* to search for **nonnegative fiber connectivity / a Markov basis**, and thereby decide the original **D16 uniform distinct-support≤12** question using all 38 legal columns. Neither D16 integer saturation nor integer-kernel spanning alone proves that uniform nonnegative bound. Original-class D25 Frobenius/eta/kappa and UR V2 genuine 94,687-byte original object/provenance still require their own actual native writer/claim; the existing UR mathematics is not rerun.
