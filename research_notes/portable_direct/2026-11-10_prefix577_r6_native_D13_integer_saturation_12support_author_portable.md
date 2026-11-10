# BRC-X6: D=13 native integer saturation and twelve-policy support theorem

Date: 2026-11-10. Status: **AUTHOR_PROVED / EXACT_FINITE_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED**.
This is independent author-side portable mathematics, not a Source-native TASK_RESEARCH checkpoint, Result, Driver review, or accepted theorem.

## Frozen semantics and theorem

Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Use the original native 96-port graph, six *labeled* actions per port, four ports `(6,7,28,29)`, signed coefficients `(+1,-1,-1,+1)`, nine frozen roots, 81 root/edge/observer channels, and **all 38 lawful deterministic policies**. The observer retains all signed joint relations; no marginal-only replacement occurs.

Let `W ∈ Z^(81×24)` be that signed joint-conservation matrix, and `C ∈ {0,1}^(24×38)` the lawful-policy incidence matrix. Each column of C chooses exactly one of six actions at each of the four native ports and obeys Wc=0.

**New exact theorem.** For every `b∈Z_(>0)^24` whose six entries at each port sum to **13** and which obeys `Wb=0`, there is `n∈Z_(≥0)^38` with

```
C n = b
sum_j n_j = 13
|{j:n_j>0}| <= 12.
```

Together with the separately established same-frozen-input D=6..12 theorem, this establishes for this precise positive native-policy model

```
(reduced common probability denominator <= 13)  =>  minSupport <= 12
minSupport = 13  =>  reduced common denominator >= 14.
```

The previously proven explicit 13-minimal denominator 1023 instance remains an upper bound for the search, so the next denominator window is `14 <= D_reduced <= 1023`.

## Proof with finite exact certificates

1. Write `J∈Z^24` for the all-one vector. Direct original nine-root channel arithmetic verifies `WJ=0`; every port row of J sums to six. For full-positive b with row sum 13, `r=b-J` has nonnegative integer entries, four row sums seven, and `Wr=0`.
2. Each port's nonnegative 6-component histogram of total seven is one of `binom(12,5)=792` possibilities. Enumerate all four-port r satisfying the original signed 81-channel equations, splitting ports 0,1 and ports 2,3, matching opposite exact integer 81-channel signatures. Count: **2,804,920 distinct four-port histograms**. The separate `verify_d13_independent_nine_root.py` builds the entire signature directly from nine frozen roots (81 keys); no 11-dimensional nullspace is used.
3. Independently enumerate every unordered multiset of seven columns from the 38 lawful policies: exactly `binom(44,7)=38,320,568` seven-policy multisets. Preserve the four ports and action labels, add each multiset's native 24 coordinates, and deduplicate. The distinct image count is **2,804,920**. Every such image is nonnegative, has four row sums seven, and satisfies Wr=0, so the image is contained in the 81-channel conservation set. The equal exact counts give equality. A separate membership check in the 11-dimensional integer-annihilator C++ verifier yields **zero unrepresented conserved targets**.
4. Enumerate all six-lawful-policy complete covers of the 24 actions (each native action occurs exactly once at each port). There are **268 covers**. Each of the 38 lawful policies occurs in at least one such cover (20 to 142 covers per policy), checked via explicit complete-cover witnesses.
5. Choose one of the seven lawful policies appearing in the representation of r, say c_j; choose any complete six-policy cover of J containing c_j. Then `b=J+r` has a 13-term nonnegative *integer* decomposition in which c_j occurs at least twice. Consequently the number of **distinct** policies in the decomposition is at most 12. The coefficient sum is exactly 13.
6. The earlier D=6..12 saturation applies to all those smaller positive integer denominators, so this extends the strict 13-support minimum denominator to at least 14. The reduced denominator itself is a valid integer D for the theorem's integer numerators.

The independent 81-channel signed W has rank 9; adding the three constraints of equal total source mass yields rank 11, equal to the integer left-annihilator dimension of the original rank-13 matrix C. Thus, on the prescribed fixed-row-sum domain, the C++ rank-11 conservation enumeration and direct signed-root enumeration use the same exact constraints.

## Exact verification transcript

```
D=12 m=6 valid=784536 integer_representable=784536 integer_nonrepresentable=0 distinct_multiset_policy_images=784536
D=13 m=7 valid=2804920 integer_representable=2804920 integer_nonrepresentable=0 distinct_multiset_policy_images=2804920
NATIVE_9ROOT_81CHANNEL_D13_EXACT_COUNT_PASS 2804920 keys 94144 root_count 9
PERFECT_COVER_PASS count=268 lawful_covered=38 all_witnesses=38 min_usage=20 max_usage=142
```

Reproducible **11-file author evidence archive**, including frozen kernel, generator, C++ full combination verifier, independent original 81-channel Python verifier, cover verifier, explicit per-policy six-cover witnesses, and full theorem document:

```
BRC_X6_D13_NATIVE_INTEGER_SATURATION_12SUPPORT_AUTHOR_PORTABLE_20261110.zip
SHA256: 32167ebc9befb82ab1e7280bb819b1d5826732acd41e4e842e1837e5c974a0d6
D13_EXACT_SATURATION_12SUPPORT_CERTIFICATE.json
SHA256: 7a7bddce7937901901cde78e138f50b149cb0edc91b2088769e0244c0b3d7e05
frozen_native_kernel_prefix577.py SHA256:
d2b84a22928e8160315e8578ea99a62f91b8688462d2b6451a71eef871df88b0
```

The archive was unpacked afresh and both independent checks re-executed from that extracted directory with matching exact outputs. The ZIP is a separately attached author portable artifact, **not an assertion that the ZIP was uploaded to this GitHub repository**.

## Lineage, obligations and next action

Previous D=6..12 theorem (inherited mathematical dependency, not recredited):
`awdawmip/enterprise-math@9bafbdab52ac89b5328084c3074df10bd8dfd45b:research_notes/portable_direct/2026-11-10_prefix577_r6_native_D6_D12_integer_saturation_author_portable.md`.

This task lane has no newly verified native Source-issued own session/winning CLAIM and has not published a Source-native Result. Author notes and client checkpoint are separate durable surfaces. The primary D25/LIFT/JT2 Source mother objective remains open: its native H0/B0 divided-power [X]U modulo p² and semilinear Frobenius comparison inputs remain missing.

Next precise scientific action: at D=14 test the eight-unit residual invariant fiber and its full lawful-policy image, then test actual minimum support rather than inferring it from a fixed-column representation. Preserve all BRC signed provenance and current P000 assumptions.

UR V2 four-file original remains an unresolved provenance recovery: historical size 94,687 bytes and SHA-256 `4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76`; this theorem does not redo the already completed UR mathematics.
