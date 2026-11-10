# BRC–X6 exact integer saturation for D=16 (frozen native nine-root)

**Date:** 2026-11-10. **Status:** AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED. No native Source CLAIM, Result, reviewer authority or independent admission is asserted.

**Frozen input pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Exact four native ports (6,7,28,29), signs (+,-,-,+), six labeled actions per source, nine frozen roots, **all 81 joint signed original observation channels**, 38 lawful deterministic strategies. P000 Heartbeat World native six-dimensional spatial basis is unchanged.

**Exact theorem.** For every `b∈Z_{>0}^{24}` whose six action counts sum to **16** independently at each port, and which satisfies the full original conservation equations `Wb=0`, where `W∈Z^{81×24}`, there exists `n∈Z_{≥0}^{38}` such that `Cn=b`, `sum_j n_j=16`, where `C∈{0,1}^{24×38}` is the incidence matrix of all lawful native deterministic strategies. This is **integer saturation**, not a claim that the 16-unit decomposition always has at most 12 distinct supports.

**Exact proof.** The all-ones 24-vector `J` has 268 legal complete six-policy covers and `WJ=0`. For every full-positive D16 invariant target put `r=b-J`. Then each source histogram is a nonnegative 6-action multiset summing to 10; exactly `binom(15,5)=3003` possibilities exist per source. The rank of the original full 81-row native W is 9 and the original C has rank 13. We performed full 2+2 meets on all `3003²=9,018,009` source-histogram pairs per side in two exact integer coordinate systems: a rank-9 row basis **derived from all original native W channels**, and the 11-row primitive integer left-nullspace of C (with equal source row sums). Both independently returned:

```
D16_INVARIANT_RESIDUALS 66460433
D16_UNSUPPORTED_CELLS 0
D16_MATCHED_SIGNATURE_GROUPS 12221
```

“Unsupported” tests every invariant four-source residual vector `r` for the existence of one of the 38 lawful original strategy columns `c_j` with `c_j≤r` coordinatewise. **Zero unsupported** was computed over all **66,460,433 distinct** invariant residuals, rather than sampled. Therefore subtract such a `c_j`: `r-c_j≥0`, the new source total is 9, and `W(r-c_j)=0`. Apply the already-established original-source **D15 integer saturation theorem** to write `r-c_j` as nine lawful policies. Thus r is a sum of ten lawful policies, and adding any six-policy J perfect cover yields the claimed sixteen-unit decomposition.

**Exact earlier dependence:** `awdawmip/enterprise-math@59b1c9a6c60ce8d198fba122148fef920501eee4:research_notes/portable_direct/2026-11-10_prefix577_r6_native_D15_12support_saturation_author_portable.md`. That earlier theorem supplies both D15 saturation and the separate **reduced-denominator ≥16** lower bound for any 13-minimal full-positive native rational policy. The present D16 extension establishes one new, narrower integer-saturation result and does not recredit D15.

**Reproduction.** The ten-file author portable ZIP was separately extracted and both complete C++ enumeration programs rerun with the same three exact integer outputs:

```
BRC_X6_NATIVE_D16_INTEGER_SATURATION_AUTHOR_PORTABLE_20261110.zip
SHA256 ad47774b613a0b19bd7ba4bcd5e9f1a34e314bb4d248a8336b7dce5cda9afaf8
D16_EXACT_INTEGER_SATURATION_CERTIFICATE.json
SHA256 980441cbc992ab20301d10d2cbf137442eeb5c9fd28942331c0a328ad3906411
```

The ZIP is a **conversation-local attachment**, not asserted to be uploaded to GitHub. The exact native frozen kernel, two integer relation matrices, two enumeration programs, original reconstructed valid strategy table and certificate are included.

**Next scientific unit:** determine the exact **minimum number of distinct lawful strategies** for full-positive D16 targets, reducing ten-policy residual families through cover/interchange structure or a complete exact certificate. The full `binom(38,10)` family has not been exhausted; no D16 12-support conclusion is claimed. Native D25/LIFT/JT2 remains open pending original-class H0/B0 and [X]U mod p² data, and real issued own session/claim provenance. Original UR V2 four-file package remains unverified (94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`).