# Native BRC–X6 D=15 integer saturation and 12-policy theorem

**Date:** 2026-11-10. **Research state:** AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / GITHUB_AUTHOR_EVIDENCE / UNREVIEWED / NOT_ADMITTED. This is an author-side portable result, not a native Source result, independent review, or TASK CLAIM.

**Frozen original scientific pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Full original 4 signed source ports (6,7,28,29), signs (+,-,-,+), six labeled actions at each source, nine roots, 81 signed joint root/edge observation channels and all 38 lawful deterministic policies. The rank-preserving integer observer basis is a computational coordinate change, not a marginalization of the original joint observation. The P000 Heartbeat World 6D native-spatial assumption is preserved.

## Statement

Let `C∈{0,1}^{24×38}` be the incidence matrix of **all** lawful deterministic native policies and `W∈Z^{81×24}` the original joint signed observation matrix. Every `b∈Z_{>0}^{24}` with 6-action row sum 15 at each of the four source ports and `Wb=0` has an integer representation

```
n∈Z_{≥0}^{38},   C n=b,   sum(n_j)=15,   |{j:n_j>0}|≤12.
```

Consequently, together with the predecessor's already verified D=6,…,14 original-model finite saturation/support theorems, any full-positive rational native policy whose minimum support is 13 has **reduced common denominator at least 16**. The historical explicit 13-minimal denominator-1023 example remains a separate upper bound.

## Proof 1. Complete D=15 integer saturation

The all-one 24-coordinate vector `J` satisfies `WJ=0` and admits exactly 268 distinct six-policy perfect covers. For any target set `r=b-J`: it is nonnegative, invariant under W, and every port histogram sums to 9.

The original W matrix has exact rank 9, and C has exact rank 13. All 81 native signed channels were reconstructed from the frozen kernel. A complete 2+2 meet-in-the-middle enumeration using the exact rank-9 row basis of W tested `binom(14,5)^2=2002^2=4,008,004` port-histogram pairs on each side. A separate integer-left-nullspace 11-row calculation obtained the same counts; on the equal-row-sum slice these row-space constraints represent the identical original native conservation system.

Both integer calculations returned:

```
D15_INVARIANT_RESIDUALS 25326678
D15_UNSUPPORTED_CELLS 0
D15_MATCHED_SIGNATURE_GROUPS 8350
```

“Unsupported” means that none of the 38 exact lawful policy columns `c_j` satisfies the coordinatewise test `c_j≤r`. Since all 25,326,678 invariant r have at least one such policy, `r-c_j` is a nonnegative invariant residual of total 8 per source. The predecessor's established D=14 eight-unit integer saturation theorem then writes `r-c_j` as a sum of eight lawful columns, proving full D=15 saturation, not merely saturation on sampled decomposable inputs.

Predecessor immutable source:
`awdawmip/enterprise-math@542b32450b4c24c4940f01abc80ff8db1492f033:research_notes/portable_direct/2026-11-10_prefix577_r6_native_D14_12support_saturation_author_portable.md`.

## Proof 2. Every nine-unit residual gives at most 12 distinct policies after adding J

For a nine-policy multiset `r`:

**Repeated policies.** If the number t of distinct residual policies is at most 7, any J cover containing one residual policy yields `6+t-1≤12`. If t=8 and some two residual policies share a J cover, then `6+8-2=12`. In the remaining case the eight are an independent set in the 38-vertex common-perfect-cover graph; the complete graph enumeration has exactly 12 independent eight-sets. This turn independently regenerated an exact integer replacement with **10** distinct lawful policies for `J+sum(S)` for each of those 12 sets. Adding the ninth repeated policy gives at most 11 distinct policies.

**Nine distinct policies.** If one J cover shares three of them, union support is `6+9-3=12`. The 268 perfect covers forbid 1,756 different triples; from all `binom(38,9)=163,011,640` nine-subsets, exactly **305,327** contain no forbidden triple. Independent C++ cover-count DFS and Python forbidden-triple DFS produced the same 9-mask sequence with SHA256
`e43cc0578085d7557cdeec29e4bb56b6bb1ab5a7f2fcc8b7430dbaa809fa369a`.
Those 305,327 subsets have 181,364 distinct native residual vectors.

**Integer pair swaps.** For every nine-subset, inspect all pairs of selected columns and all pairs of 38 lawful columns with `c_i+c_j=c_k+c_l` (24 exact integer coordinates). A replacement that creates a repeated policy or a J-cover triple invokes the preceding cases. Two separately written complete classifiers—C++ using 24-coordinate pair-signatures and Python using four source action multisets—agree:
```
305327 triple-free nine-subsets
305319 reducible by one exact pair swap
8 remaining masks
```

The eight 38-bit masks are:
`71010648616, 68854779656, 139865424432, 137709555472, 2155999776, 2159936032, 130816, 4067072`.

Each of these eight targets `J+sum_{j∈S}c_j` has an explicit **10-distinct-policy integer decomposition**, verified by checking all 24 coordinates, nonnegative integer coefficients and total weight 15. The twelve independent-eight J-cover witnesses are separately exact integer-verified at total weight 14. Discovery used integer MILP, but the final proof verifier uses **only the frozen original native kernel and integer arithmetic**, not the optimizer or floating-point evidence.

Thus every original native full-positive D=15 target has a 12-distinct-policy (or smaller) exact integer decomposition.

## Reproduction and provenance

The complete 25-file companion author-only ZIP was independently unpacked and verified, with all C++ and independent Python checks passing:
```
BRC_X6_NATIVE_D15_12SUPPORT_SATURATION_AUTHOR_PORTABLE_20261110.zip
SHA256 bf32d595527c6b0259305581e2f8f7fbeddcb8e5a80787344499da9f76dbfdf5
```
The archive is a **conversation-local** reproducibility attachment, not represented as uploaded to this repository. Exact certificates in the archive include `D15_COMPLETE_EXACT_CERTIFICATE.json` (SHA256 `72d91c6620951f6e04e3683a86dcd5bc537cd31a98e54542722997e8365ae3be`), eight D15 integer witnesses and twelve independently regenerated D14 integer witnesses.

This result extends, and does not recredit, the predecessor's D≤14 science. The next exact research unit is D=16: ten-unit residual saturation and full 38-policy support-minimality audit, using the same original scientific pin. The D25/LIFT/JT2 mother task stays OPEN and still requires native H0/B0 divided-power [X]U mod p² data, semilinear Frobenius direction, normalization eta and the kappa/Delta_p−R_p mapping. UR V2 original four-file package remains a byte-level recovery debt (94687 bytes, SHA256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`). No native own session, winning CLAIM, execution checkpoint, Result or review is asserted by this author note.
