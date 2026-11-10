# BRC-X6 original-native D511: second independent 11-policy cone and exact S4∪S5 counts

Date: 2026-11-10 Asia/Hong_Kong. Status **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**; author-portable evidence, not native Source Claim/Result/review. Frozen scientific SHA256 `f42f2906d77f24085c123f3ccfe9667d41caa96d`, preserving the original 96 ports, source ports `(6,7,28,29)` signs `(+,-,-,+)`, six labeled actions, and all nine seven-variable signed joint-root observers. No synthetic or substitute native experiment.

## Reused exact S4 theorem

Original `6^4=1296` action-tuples yield exactly 38 lawful deterministic original-native policies, in lexicographic order. Their full 24x38 integer indicator matrix `C` has rank 13. Prior author note at commit `cb7c65bf9b51f2658984952d96562ef5e3950d93` classified the exact complete fixed 11-policy S4 cone:

```text
S4 = (0,1,3,6,8,12,17,28,29,30,31)
N4(D) = binom(D+2,10) if D>=8 else 0
N4(511) = 318476399548643271936
P4(511) = 318476398719712165581   [true irreducible denominator]
```

That theorem and the preceding 10-dimensional parameter slice retain their original authorship. This report studies a **different** source-respecting 11-policy cone and counts the overlap without double-crediting points.

## NEW independent native S5 cone

Replace the S4 policy with original index 0 by a different lawful policy at index 7:

```text
S5 = (1,3,6,8,12,17,28,29,30,31,7)
R5 = (0,1,2,3,4,5,6,7,10,12,13)  # original native 24-coordinate row indices
```

Direct exact integer matrix checks give `rank C[:,S5]=11` and `det C[R5,S5]=+1`. Thus this S5 support has an integral left inverse on the **original 24 source/action coordinates**, and for integer nonnegative weight vector v, `gcd(C[:,S5] v) = gcd(v)` exactly. Furthermore `rank C[:,S4∪S5]=12`, so the S5 cone introduces a genuine new legal native observation direction outside the fixed S4 vector span.

Full enumeration of all 2048 subsets of the eleven S5 policies, retaining every source and action label, gives the exact number of supports covering **all 24** native cells:

```text
support size: 7   8   9  10  11
count:        1   5   8   5   1
```

Since the 11 S5 columns are independent, integer weights are unique at fixed displayed denominator D. Positive integer compositions on each full-cover support give the universal exact formula

```text
N5(D)=binom(D-1,6)+5*binom(D-1,7)+8*binom(D-1,8)
      +5*binom(D-1,9)+binom(D-1,10).
```

Take binom(n,k)=0 for k>n, so the minimum D with strictly positive original 24 coordinates is 7. Applying exact native gcd/divisor Möbius inversion to D511=7*73 yields:

```text
N5(511) = 331003492680429922496
N5(73)  = 1065050876044
N5(7)   = 1
N5(1)   = 0
P5(511) = N5(511)-N5(73)-N5(7)+N5(1)
        = 331003491615379046451.
```

The `N5(7)=1` term is essential: an exploratory calculation omitted this divisor and was **corrected before publication** by the full exact checker.

One explicit native example uses S5 weights `(0,505,0,1,1,1,1,0,0,1,1)`, yielding the four-source by six-action numerator matrix:

```text
[506,1,1,1,1,1]
[506,1,1,1,1,1]
[2,1,1,1,505,1]
[2,1,1,1,505,1]
```

Every row sums to 511, every original action probability is positive, the denominator truly is irreducible 511, and the original signed joint observer on all nine frozen roots is identically zero. Every point in this S5 nonnegative cone uses at most 11 native policies.

## NEW union theorem, with complete overlap elimination

Ten native policies are common to both supports:

`K=(1,3,6,8,12,17,28,29,30,31)`.

The 10 shared columns have rank 10 and all **12** columns of S4∪S5 are independent. If a native vector belongs to both cones, subtracting its two expansions and using rank 12 forces the S4-only policy-0 and the S5-only policy-7 coefficients to vanish and every shared coefficient to agree. Therefore the exact cone intersection is precisely the common 10-policy nonnegative cone. Since full positivity in this common cone requires 8 mandatory positive weights plus 2 optional,

```text
NI(D) = binom(D+1,9)  if D>=8, else 0
NI(511) = 6208116950265950720
PI(511) = 6208116839741803206.
```

The distinct native original-action probabilities in the **two-cone union** (not a sum with duplicates) are therefore:

```text
NU(511) = N4(511)+N5(511)-NI(511)
        = 643271775278807243712.
PU(511) = P4(511)+P5(511)-PI(511)
        = 643271773495349408826  # true exact irreducible denominator
```

This is a proved union of **two concrete** 11-policy cones inside the original 38-policy model. Each represented point satisfies `minSupport<=11`; no global absence of 9-bit 13-minimal points is asserted.

## Exact computation and original-input provenance

Original-native verifier reconstructs 38 lawful policies from the 1296 tuples, tests all nine signed roots, integral S5 minor +1, S4/S5 union rank12, exactly enumerates 2048 S5 supports, applies exact integer binomial formulas and native gcd, and **independently enumerates actual original 24-coordinate probability vectors for D=7,8,9** to check all S4/S5/intersection/union cardinalities. Zero floating point and no assumed target lemma. The complete Chinese proof and both standalone reproduction scripts, frozen native kernel, exact JSON certificates and manifest were clean-unzipped and all tests PASS. Ten-file author portable package SHA256 `0c6ffbed3ca77f639256221a100e790d9d1acc6040ac1005ce6079df5651297d` (conversation delivery, not claimed as Source-published bundle).

Source D25 LIFT/JT2 original-class divided-power module, H0/B0, [X]U mod p^2, source Frobenius/eta/kappa and native reviewer remain separate and await genuine authorized original-class execution; no new native session/CLAIM/Result is asserted. Earlier completed UR math not repeated. Original four-file UR V2 bundle remains unverified: exactly 94687 bytes and SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` are required before its provenance/writer supplement.

Next discriminating science action: test larger original-native rank-12 and rank-13 support arrangements at D<=511, preserving all signed roots and joint interactions, and produce complete exact minSupport<=12 primal representation or rigorous 13-minimal separation; avoid unclaimed Research1 J1/J2 drafts. This two-cone theorem is author-only evidence, UNREVIEWED / NOT_ADMITTED.
