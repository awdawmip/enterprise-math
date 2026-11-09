# BRC-X6: sharp native 13-minor bound 3 and explicit 25-bit 13-minimal positive witness

**2026-11-09** · AUTHOR_PROVED / EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. Author-portable mathematical evidence only; no native Source CLAIM, run, Result, Driver review or admission. Frozen input `f42f2906d77f24085c123f3ccfe9667d41caa96d`; native 96 ports, six labelled actions, nine signed joint-observer roots, source ports `(6,7,28,29)` with signs `(+,-,-,+)`; original root-legal deterministic strategy list has exactly 38 labelled tuples. Previous 29-bit explicit result: commit `435a172efd2233d5d61768de946b52bfdf067b49`. This note proves a further new bound rather than recrediting earlier strategy discovery.

## Exact theorem

Let `C` be the `24×38` 0/1 native source-action incidence matrix, one chosen labelled action per original source and strategy. Use the faithful exact coordinate chart
```
R=(0,1,2,3,4,5,18,19,20,21,22,6,10)
A=C[R,:].
```
Exact rational row reduction gives `rank(C)=rank(A)=13`. **For every 13 distinct original lawful labelled policy columns S, `|det(A[:,S])| <= 3`. This bound is sharp:** for
```
S3=(23,3,32,17,26,18,8,5,35,13,16,11,15)
```
the exact integer determinant equals `+3`.

**Proof.** The first eleven rows are the reduced incidence of the bipartite multigraph on the six source-0 and six source-3 action labels, with one vertex equation omitted. The last two rows indicate original source-1 actions 0 and 4. A nonzero 13-column determinant requires rank eleven on these incidence rows, hence the 13 projected labelled edges form a connected graph spanning twelve vertices with cycle rank exactly two. Choose an eleven-edge spanning tree and its two chords. Integer elimination along tree edges, with unimodular tree incidence, reduces the determinant (up to sign) to the 2×2 determinant of the oriented fundamental-cycle signatures
```
sigma(gamma)=(sum_i (-1)^i * [native source-1 action of edge_i == 0],
              sum_i (-1)^i * [native source-1 action of edge_i == 4]).
```
Two parallel original policy labels form a valid length-two cycle. Retaining each labelled policy and its nine-root joint observer is essential.

Exact exhaustive simple-cycle enumeration gives 103,653 labelled cycles, grouped by lengths `{2:6,4:310,6:3389,8:20256,10:49596,12:30096}`. In a fixed single-orientation convention there are 16 signatures (19 after allowing reverse orientation), with prior max pair determinant 4. Exactly 11 unordered signature classes give absolute pair determinant four, yielding **34,481,643** pairs of labelled cycles. Of these, **244,047** pairs have a union of at most thirteen labelled edges, and these have **232,371** distinct union edge masks. The exact graph cycle ranks of these 232,371 masks are
```
rank 3: 50199, rank 4: 134382, rank 5: 42300, rank 6: 5490.
rank <= 2: 0.
```
No such union can fit inside a connected 13-edge support with cycle rank two; pairs whose union uses >13 edges cannot fit either. Therefore determinant four is impossible. The previously established max-four upper bound then gives max three. The displayed +3 minor certifies sharpness.

Two genuinely different author-side algorithms verify this exhaustive finite domain: (1) original labelled-edge DFS, numpy uint64 union masks, exact integer cycle-rank tests; and (2) NetworkX elementary simple *vertex* cycles, Cartesian expansion of every labelled parallel-edge alternative, length-two cycles inserted separately, independent union/rank calculations. Both return 103653 / 34481643 / 244047 / 232371 and minimum union cycle rank three. This is author-side exact cross-checking, not an independent Driver review.

## Constructed 25-bit minimal witness

Reuse the predecessor's thirteen lawful native policy IDs
```
IDS=(2,8,15,21,24,28,29,31,37,0,1,3,5).
```
Choose weights `w_j=4^j` for `j=0,...,12`, and `D=sum(w_j)=(4^13-1)/3=22369621` (**25 bits**). The four rows of exact original six-action probability numerators are
```
[22282241,       4,       16,       64,     5376,   81920]
[ 5505029,16793600,       16,       64,     1280,   69632]
[  266496, 1064960, 16777217,        4,  4194320,   66624]
[  262400, 1052672,        5, 16793600,  4194320,   66624]
```
Each row sums to D and all 24 coordinates are positive. All nine *original* root-wise signed joint next-port and seven-observer reward balances verify exactly. The selected chart determinant equals `−1`, so the 13-term convex representation is independent.

If that probability vector had a representation using <=12 lawful policies, extend them to twelve linearly independent lawful columns `T`. Taking determinants against the integer numerator vector yields
```
0 = sum_{j=0}^{12} 4^j d_j,
d_j = det(A[:,T], A[:,IDS[j]]),  |d_j|<=3.
```
The 13 selected columns are independent, so some d_j is nonzero. For its largest nonzero index k, `|4^k d_k| >= 4^k > 3 sum_{j<k}4^j = 4^k-1`, impossible. Thus the strategy has **exact minimum support 13**, with public rational denominator `22369621`. The same argument excludes signed-coefficient 12-column spans, which is stronger than the convex claim.

## Reproducibility, provenance and remaining frontier

Self-contained author bundle `BRC_X6_NATIVE_SHARP_MINOR3_25BIT_AUTHOR_PORTABLE_20261109.zip` has SHA-256 `4b2812f83b7a4e478d40167fbd6d751d7c7fc09b76046d5f1e1a040d9d7429d6`; it includes `full_pair_numpy_extended.py`, `independent_networkx_cycles.py`, `verify_25bit_witness.py`, frozen native kernel, exact JSON enumerations and source-level proof. Verified in a separate local run on 2026-11-09. Git publication of this note is a distinct author-evidence persistence boundary.

The unchanged D25 Source task is `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Its original-class H0/B0, native Frobenius, eta and CM frontiers remain open; this portable BRC-X6 theorem is not a D25 native experiment. Historical UR V2 four-file bundle (expected 94687 bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) remains unlocated. Current own service-issued session and winning claim are unverified: no native checkpoint or Source completion asserted.

**Next exact mathematical unit:** optimize denominator across arbitrary strictly positive 13-policy mixtures using the sharp rank-13 chart and original labelled joint observer; a smaller feasible witness would be independently valuable. No global denominator minimum is claimed.
