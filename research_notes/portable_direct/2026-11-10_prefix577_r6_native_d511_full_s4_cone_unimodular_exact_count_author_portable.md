# BRC-X6 native D511 full fixed-S4 cone, integral recognition and exact full-positive counts

Date 2026-11-10 (Asia/Hong_Kong). **AUTHOR_PROVED / EXACT_SYMBOLIC_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**. This is author-portable evidence only; not an authorized native Task checkpoint, claim, Result, review or Foundation promotion.
Frozen scientific SHA256: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Preserve original 96 ports, four source ports `(6,7,28,29)` signed `(+,-,-,+)`, six labeled actions each, and all nine signed seven-variable joint observer roots. No replacement of original X6/Heartbeat basis by the 24-dimensional action readout.

## Inherited native construction (do not recredit)

Lexicographically enumerate all 6^4=1296 original four-source action tuples; exactly 38 pass all signed native roots. Their original 24x38 0/1 action-incidence matrix `C` has rank 13. Reuse 13-column basis `I=(2,8,15,21,24,28,29,31,37,0,1,3,5)`, chart rows `R=(0,1,2,3,4,5,18,19,20,21,22,6,10)`, and fixed 11-policy set `S4=(0,1,3,6,8,12,17,28,29,30,31)` in this order. These are inherited from earlier author evidence, including full signed observer fidelity; the previous 10-dimensional D511 subfamily and its 2,715,533,292,923,099,825 distinct strategies remain credited to that earlier work at commit `89d10d9eb6f0ee50c6810a8993c8c925ccafa477`.

Set `B=C[R,I]` and `J=B^(-1)C[R,S4]`. Exact computation gives `det B=-1`, `rank C=13`, `J` integral of rank 11, and **`C[:,I] J = C[:,S4]` on ALL original 24 coordinates**, before an observer quotient. Previous author notes established this map; the next two classifications and counts are new.

## NEW Theorem A — complete exact recognition of the fixed S4 cone

For arbitrary rational or real 13-chart coordinates `w=(w0,...,w12)`, the original-native action vector `x=C[:,I]w` has a representation by nonnegative weights on this specific 11-policy set S4 if and only if:

```text
E1: w3 - w4 + 2*w8 = 0
E2: w0 - w8 + w12 = 0
v=Lw >= 0  (eleven componentwise inequalities), where:
v0=-w2+w8+w9       v1=-w8+w10       v2=w2+w11
v3=w8              v4=w1            v5=w2
v6=w3              v7=w3+w5+w8      v8=w6+w8
v9=w0              v10=-w0+w7+w8
```

**Exact proof.** On the reused integral chart `J`, verify `E*J=0`, `rank(E)=2`, `L*J=I11`. Since `rank(J)=11`, its image equals `ker(E)`. Thus every `w` satisfying `Ew=0` equals `J L w`, and the unique S4 weights are precisely `Lw`; coordinatewise nonnegativity is necessary and sufficient. A specified 11x11 minor of `J` at zero-based rows `(0,1,2,3,5,6,7,8,9,10,11)` has determinant `+1`, an exact integral-lattice witness. For integer native actions `b=C[:,S4]v`, `v=L B^{-1} b[R]` gives an integer left inverse (because `det B=-1`). Consequently **`gcd(b0,...,b23)=gcd(v0,...,v10)`** for every integer v. These equalities and complete integer matrices are included in the exact certificate and were rerun with exact SymPy arithmetic.

## NEW Theorem B — full-positive cone and denominator enumeration

Within S4, every one of the 24 ORIGINAL source/action cells has strictly positive count if and only if

```text
v2,v3,v4,v5,v6,v7,v8,v10 > 0;    v0,v1,v9 >= 0.
```

Proof: all eight indicated policies possess at least one unique owned source/action cell among the chosen 11 policies; these eight policies together cover every one of the 24 cells. Exhaustively testing all 2^11=2048 S4 support masks gives exactly `(support size 8:1; 9:3; 10:3; 11:1)` all-positive supports, and they are precisely the supersets of the eight mandatory policies. Source and action tags are never merged.

With integer S4 weights v>=0 summing to any D>=1 and all 24 native counts positive, column rank 11 makes each normalized probability vector unique at fixed D. Stars-and-bars gives the **complete S4-cone count**

```text
N(D) = binom(D+2,10)  for D>=8;   N(D)=0 for 1<=D<8.
P(D) = sum_{d|D} mu(d)*N(D/d)  [exact reduced denominator D],
```

where the second identity follows from the integer left inverse, so the gcd of native probability numerators equals gcd of S4 weights. In particular, for `D=511=7*73`:

```text
N(511) = 318476399548643271936
N(73)  = 828931106355
N(7)=N(1)=0
P(511) = 318476398719712165581.
```

Thus **318,476,398,719,712,165,581 distinct strictly full-positive original-native rational strategies have irreducible nine-bit denominator 511 and a legal decomposition using at most 11 deterministic policies on this fixed S4 cone**. The preceding 10-dimensional parameter family is a proper restricted slice of the now-counted full fixed S4 cone. Neither statement decides whether a nine-bit **13-minimal** strategy exists outside this cone.

One exact nine-bit irreducible example: fixed S4 integer weights `v=(503,0,1,1,1,1,1,1,1,0,1)` give the 4x6 ORIGINAL source/action numerator matrix

```text
[505,1,1,1,2,1]
[505,1,1,1,2,1]
[506,1,1,1,1,1]
[506,1,1,1,1,1]
```

Each row sums to 511 and all 24 entries are positive (including 1), so the denominator is irreducible. All nine independent signed joint-root checks returned exact zero.

## Independent reconstruction and provenance

Author portable bundle contains `frozen_native_kernel_prefix577.py`, the **complete executable** `verify_full_s4_cone_20261110.py`, a Chinese theorem/proof, JSON certificate with all E/L/J matrices and coverage witnesses, and README. Fresh extraction, all candidate/root checks, 13D rank, E/L algebra, minor=1, 2048-support enumeration, binomial and independent small-D dynamic programming, and full 24-coordinate example all PASS. No floating point reasoning or assumed target lemma. Six-file portable ZIP SHA256: `47c85a357f133adfd2f5118b323fe40c4410eede234fdab2556057a1395ae8fd`. This hash identifies user-delivered local package, not an assertion of Source-published bundle.

Native D25 LIFT/JT2 remains OPEN: original-class divided-power H0/B0, `[X]U mod p^2`, sigma-semilinear Frobenius and eta/kappa signed Hesse/Green require a legitimate native execution identity/claim and different exact evidence. Original UR V2 four-file bundle has not been recovered; authenticate exactly 94,687 bytes and SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76` before its writer/provenance supplement. Completed UR math is not repeated.

**Next independent scientific unit:** work outside fixed S4 among the remaining 38 legal columns, produce a distinct original-native denominator<=511 candidate and an exact separation or explicit <=12 representation on full 24 tagged actions and all nine signed roots; do not replay Research1 J1/J2 without its own claim. Preserve all previous authors and formal Source boundaries.
