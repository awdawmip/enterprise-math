# BRC-X6 original-native: a signed integer residual and exact D511 rank13-to-12 reduction

Date: **2026-11-10 Asia/Hong_Kong**. **AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. Author-portable independent math evidence; **NOT** native Source Claim/Result/review. Scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Original 96 ports, four source labels `(6,7,28,29)` with signs `(+,-,-,+)`, six distinct labeled actions per source, and all nine seven-variable signed joint-root observers retained.

## Reused previously verified structure and precise new question

Enumerate the 1296 four-source action tuples against all nine signed roots, obtaining exactly **38** legal native deterministic policies, ordered lexicographically; their **24×38** integer labeled-action incidence matrix `C` has rank **13**. Previously author-proved and published, the fixed eleven-policy sets `S4=(0,1,3,6,8,12,17,28,29,30,31)` and `S5=(1,3,6,8,12,17,28,29,30,31,7)` have rank 11. Their union

`U=(0,1,3,6,7,8,12,17,28,29,30,31)`

has rank 12 and original native row minor `det(C[R12,U])=-1` for `R12=(0,1,2,3,4,5,6,7,10,12,13,16)`. Reused prior author evidence: GitHub commits `cb7c65bf9b51f2658984952d96562ef5e3950d93` and `92ecb0ae95558047b93d624c367207385ed35d63`, and immediate preceding rank12 cone theorem `b9504c1d23f792e393f6f4503554672d1c274045`. None is recredited as discovered here.

## NEW Theorem 1 — exact rank-13 signed original-native residual

On the **original complete 24 labeled integer action coordinates** define

`g(b)=-b[0]-b[1]-b[5]+b[6]+b[7]+b[14]`.

Exact signed root–preserving column evaluation on all 38 native policies gives:

```
g(C_j)=+1: j = (2,5,14,19,22,23,26)             # 7
g(C_j)=-1: j = (10,11,32,33,34,36,37)          # 7
g(C_j)= 0: j = (0,1,3,4,6,7,8,9,12,13,15,16,17,18,20,21,24,25,27,28,29,30,31,35) # 24
```

Every U column lies in `ker(g)`. Since `rank(C_U)=12`, `rank(C)=13`, and `g(C_2)=1`,

`span_Q(C_U) = span_Q(C) ∩ ker(g)`.

This equality is **only of linear spans**: it does not identify the nonnegative U cone with all native legal distributions on the g=0 hyperplane. In particular nonzero g rules out U-only representations but does **not** establish 13-minimal support in the full 38-policy model.

## NEW Theorem 2 — all 14 signed residual extensions are unimodular

Extend the original native row order by index14: `R13=R12+(14,)`. Direct exact integer determinant for **each** of the 14 legal policies with `g(C_j)=±1` gives

`det C[R13,U+(j,)]=-g(C_j)=±1`.

So each extension is a 13×13 unimodular integral readout basis, retaining all labels and nine source-signed joint observers. Every other legal column outside U has g0 and does not lift the rank. This supplies an exact type-preserving integer residual coordinate useful for candidate generation and fast separation, without a claim about global cone-minimality.

For integer numerator b at displayed denominator D, gcd(D,b_0,...,b_23) divides g(b). Thus g(b)=±1 implies the denominator D is truly irreducible; general nonzero g requires direct gcd verification.

## NEW Theorem 3 — a nonzero-residual D511 13-term candidate has an exact 12-term primal reduction

Let `D=511=2^9-1`. An explicit **13-policy** original legal representation `ids13=U+(2,)`, with weights

`w13=(36,26,28,11,14,15,17,32,37,24,14,12,245)`

sums to 511 and generates this full-positive **native four-source by six-action numerator** matrix:

```
[360, 15,  17,  32, 61, 26]
[364, 12,  17,  32, 48, 38]
[109, 52, 270,  15, 28, 37]
[ 96, 64, 274,  12, 28, 37]
```

Each row sums to 511, every coordinate is positive, all nine signed roots vanish, `g(b)=245 ≠0`, and `gcd(511,b_0,...,b_23)=1`. Thus this genuine reduced 9-bit native distribution lies outside the U rank-12 *linear span* and admits the explicit rank13 13-term presentation.

**Nevertheless**, the following **different 12-policy** legal native support and strictly positive integer weights generate the same exact **24** coordinates:

`ids12=(0,1,2,4,6,8,15,19,23,27,29,32)`
`w12=(59,26,227,37,11,15,17,32,12,11,38,26)`.

Direct exact matrix multiplication gives `C[:,ids13] w13 = C[:,ids12] w12 = b`, both sums=511. Therefore this candidate satisfies **minSupport(b/511)≤12**, despite its nonzero rank13 residual and 13-term positive representation. We do **not** assert equality 12, nor the nonexistence of other D≤511 13-minimal strategies. This example identifies a concrete failure mode of using linear rank or nonzero residual as an incorrect global lower-bound certificate.

## Exact verification, true scopes and next step

A standalone 8-file author-side package `BRC_X6_NATIVE_RANK13_SIGNED_RESIDUAL_9BIT_REDUCTION_20261110.zip`, SHA256 `12514f61b714ca3e3adf527812e27f121d03a644b61d59eaa8506231635d8779`, was clean-extracted and verified. Script `verify_rank13_residual_reduction.py` rebuilds all 38 legal policies from original nine roots, verifies 24×38 rank13, U minor -1, exact 24/7/7 g partition, all 14 ±1 13×13 minors, and exact full-positive nine-root 13-to-12 rational-primal equality at D511. The independent `verify_native_residual.py` also rebuilds the frozen kernel and checks g, legal columns and ±1 witnesses. Both PASS, zero floating point; original integer assignments and observer data are preserved. The archive itself is a **conversation artifact**, not represented as Source-published.

Canonical D25/LIFT/JT2 source requires real native H0/B0, [X]U mod p², Frobenius eta/kappa, current winning claim, publication and independent review; this portable proof does not replace the native experiment. Original UR four-file V2 bundle exact 94687 bytes / SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` is still not verified; do not restage a synthetic substitute.

**Next discriminating science**: augment original U with signed residual ±1 columns, use the unimodular 13-row decomposition to isolate genuinely different native D≤511 candidates, then for each prove a ≤12-term exact primal decomposition or an exact *full 38-policy* 12-term infeasibility separator. Preserve signed source/action labels, all nine native roots and project frozen science. Status **UNREVIEWED / NOT_ADMITTED**.
