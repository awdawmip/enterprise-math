# BRC-X6: uniform twelve-policy compression of a full-positive nine-bit family

Date: 2026-11-10 (Asia/Hong_Kong). Evidence level: `AUTHOR_PROVED / EXACT_SYMBOLIC_VERIFIED / UNREVIEWED / NOT_ADMITTED`. This is an author-portable mathematical result, not a native Source checkpoint, Result, independent Driver review or admission. Researcher Source identity and winning CLAIM are not verified for this conversation.

## Native model and frozen input

Preserve scientific pin SHA-256 `f42f2906d77f24085c123f3ccfe9667d41caa96d`, the 96 original ports, six labeled actions, nine original signed seven-variable next-port/reward joint roots, source ports `(6,7,28,29)` and signs `(+,-,-,+)`. Enumeration of the original 1296 four-source action tuples yields 38 legal deterministic policies, indexed 0..37 lexicographically. Let `C` be their 24-by-38 source/action incidence matrix.

## Exact parametric theorem

For any **real** `a` with `0 <= a <= 64`, let the original 13-policy chart be

```
I = (2,8,15,21,24,28,29,31,37,0,1,3,5)
w(a) = (1,2,4,8,16,32,64,128,128,a,a,64-a,64-a).
```

Its common normalization is 511. All 24 coordinates of `X(a)=C[:,I]w(a)/511` are strictly positive even at both endpoints. Written by source port, the numerator matrix is

```
[129,     2,       4,      8,       112,   256]
[a+67,    192-a,   4,      8,        48,   192]
[a+80,    a+128,   65-a,   2,       68-a,  168]
[a+16,    a+64,    3,      192-a,   68-a,  168]
```

A **single fixed 12-policy set** represents the entire family:

```
S = (1,5,8,12,21,23,28,30,31,33,36,37)
v(a) = (a+64, 65-a, 2, 4, 8, 64, 48, 1, 63, a+12, 68-a, 112).
```

The two exact symbolic identities are `sum(w(a))=sum(v(a))=511` and

```
               C[:,I] * w(a) == C[:,S] * v(a)   (all real a).
```

Every component of `v(a)` is strictly positive for `0 <= a <= 64`. Therefore

```
minSupport(X(a)) <= 12 for every real a in [0,64].
```

For each integer `a=1,...,63`, all 13 original-chart weights are strictly positive integers summing to `511=2^9-1`; hence **all 63 members of this declared nine-bit family** have the explicit native 12-policy compression. For noninteger a, 511 denotes a normalization, not necessarily an integer common denominator. The theorem is a family-specific reduction, not a global nine-bit impossibility theorem.

## Proof / native observer and exact checks

The 12 IDs in S are among the 38 policies that separately satisfy the *complete signed native joint balance* for all nine original roots. Symbolically subtract the two 24-vectors: all 24 affine polynomials vanish coefficientwise. The displayed endpoint values make the alternative weights and marginal numerators strictly positive across the whole interval. Each source-port row sums exactly to 511. Since each original policy is valid for each root and signed joint observations are linear under mixtures, the alternative mixture preserves the original complete nine-root observation. No scalar-only, unlabeled, independently resampled or four-way-product replacement is made.

An author-side reproducibility package contains the complete theorem, independent exact SymPy verifier, exact certificate JSON, and the previously frozen native kernel. Local checker output: `PASS: 38 legal original native policies, 9 joint roots, exact 24-coordinate affine identity; PASS: full interval positivity and D=511`. Exact JSON certificate SHA-256: `851678129f0f636c0424ef82ba7cc0660f97049fbe053c5eb8a003a6a1916856`.

## Context, provenance, next scientific unit

This reuses the known 13-policy chart from the prior author 10-bit D=1023 minimum-support-13 witness (commit `c7710f3a7fe4b6ddd7ce66af6df02ca95a275888`) without recrediting the earlier construction or determinant-bound proof. Comparison against the available earlier 199-case D=511 certificate found no duplicate 13-weight vector in this family. The historical 64-case set has not been fully compared. The new mathematical contribution is the **single explicit affine twelve-policy lift for a continuous parameter interval**, which subsumes all declared 63 integer cases.

Next: select a genuinely different 13-policy chart or weight direction outside this fixed twelve-policy cone and test a full-positive D<=511 candidate with exact original-native infeasibility evidence. Keep UR V2 source recovery and legal native writer/provenance debt separate; the historical 94,687-byte object with target SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` was not recovered in this proof turn.

Native Source checkpoint/write: **NOT WRITTEN** (this conversation has no verified service-issued research session/CLAIM). Author-level evidence: **PROVED AND LOCALLY VERIFIED; NOT ADMITTED**.
