# BRC-X6 D16: sharp eight-cover transversal and exact recombination

**2026-11-10** · Frozen native science pin `f42f2906d77f24085c123f3ccfe9667d41caa96d` · **AUTHOR_PROVED / EXACT_FINITE_VERIFIED / UNREVIEWED / NOT_ADMITTED**.

This author-side portable research result continues but does not recredit the D16 integer saturation theorem at `awdawmip/enterprise-math@252cc9e7386c2e2dfb3c85b2e43fa3d18e1b5b2a`. It addresses the **still-open distinct support <=12** issue for D16. The native model retains source ports (6,7,28,29), signs (+,-,-,+), six separately labelled actions each, all nine original frozen roots and 81 signed joint-flow keys. Its exactly enumerated legal deterministic policies are the 38 lexicographically ordered four-action tuples indexed 0...37.

Define `C_j` as the 24-coordinate incidence vector of legal policy j, and `J=(1,...,1)`. A **J-six-cover** is any set F of six distinct policy IDs with `sum(j in F) C_j=J`. The native 81-flow checker and complete first-source canonical backtrack find exactly **268** such covers.

## Theorem A: exactly eight J-six-covers are necessary and sufficient to cover all 38 policies

The eight explicit covers below are individually exact six-covers and their union is `{0,...,37}`:

```text
[5,11,32,22,16,20]
[8,31,7,16,17,27]
[9,3,13,33,26,21]
[9,36,12,2,18,28]
[9,14,4,20,34,24]
[9,15,21,6,29,30]
[9,16,20,0,25,35]
[10,23,15,37,19,1]
```

**Lower-bound proof:** precisely eight lawful policies, IDs `22,23,24,25,26,27,28,29`, have label 4 at the first source port. Any J-six-cover has *one* policy with first-source label 4; thus at least eight covers are necessary. The displayed eight achieve this bound:

`minimum J-six-cover family covering all 38 = 8`.

## Theorem B: sharp two-policy overlap with every 10-policy support

For every ten-element subset `S` of the 38 lawful policy IDs, at least one J-six-cover `F` satisfies `|F ∩ S| >= 2`: assign each of ten elements to one of the eight displayed covering sets containing it, then apply the pigeonhole principle.

The bound **2 is sharp even when optimizing over all 268 six-covers**. An explicit ten-element witness is

```text
S = [12,13,17,22,24,25,29,30,31,32].
```

Exact enumeration of all 268 covers by intersection with S yields
`|F∩S|=0: 48; =1: 120; =2: 100; >=3: 0`.

## D16 exact witness: merely swapping the six-cover is insufficient

Define `b=J+sum(j in S) C_j`. Its 24 original integer action counts in four ordered source rows are

```text
[1,1,3,2,5,4]
[3,2,3,2,4,2]
[6,6,1,1,1,1]
[5,4,3,2,1,1]
```

All 24 entries are strictly positive, each row sums to 16 and all original 81 signed joint-flow equations vanish. The decomposition into any exact J-six-cover plus the **unchanged** ten residual policies in S has at least `6+10-2=14` distinct policy IDs.

Nevertheless, the following *different* exact integer decomposition exists:

```text
b = 1*C_5 + 1*C_9 + 3*C_12 + 1*C_20 + 1*C_21
  + 1*C_22 + 4*C_25 + 2*C_30 + 2*C_33.
```

The coefficients sum to 16, and the full 24-coordinate equality is exact, giving **minSupport(b/16) <= 9**. No equality to 9 is claimed. The witness shows why simply optimizing the J-cover's overlap with one fixed ten-policy residual is not a sufficient route to a general D16 12-support theorem; a cross-residual policy recombination is materially useful.

## Exact finite validation and continuity

The independent author-side Python-standard-library checker reconstructed 38 legal policy tuples by screening all `6^4=1296` choices against the original 81 joint signed-flow keys (nine roots); exhaustively constructed 268 covers via the unique first-source label ordering; verified the displayed eight covers, the lower-bound pigeonhole, the exact intersection histogram, all 81 joint-flow equations for b, and the nine-policy identity. No floating-point inference is used.

Portable archive created in this author's conversation: `BRC_X6_D16_EIGHT_COVER_NATIVE_AUTHOR_PORTABLE_20261110.zip` with generator, executable checker, exact JSON certificate, full Chinese proof, README and manifest; archive SHA-256 `e4632dafc589d82700328f0eed079685c29a80fd40b1faaec0dacecb3a697cc6`. This **archive is conversation-local**, not claimed as uploaded to GitHub by this Markdown publication.

**Next mathematical unit:** replace the overlap-only argument with exact small cross-residual swaps or a full 38-column separation certificate. D16 universal support<=12 remains open. Source-native D25/LIFT/JT2, true UR V2 object recovery (94,687 bytes; required SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`) and execution writer/provenance remain separate. No researcher session, winning CLAIM, Source checkpoint, Result, independent review or admission is asserted by this author note.
