# Enterprise Math R112 — high-axis orbit amplification to 20 bits

Date: 2026-10-18. Type: finite combinatorial proof (author-side, unreviewed, not project-admitted). **No native-BRC physical claim.**

## Sources and scope

Verified source pair: GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge@e2c99e7eeea5f67b9014b350fff8f8b35fe38d4c` (P000 ACTIVE_LOCKED, ACTIVE worldview, math/code/BRC research policy), and `awdawmip/enterprise-math@341ea3fb3b06d32b16208d523dd5b7fdf6037f39` (portable-research, ordinary-control, BRC-only arithmetic). Frozen predecessor files: R106 and R107 proofs/verifiers in `EM_X6_R107_CYCL_ONLINE_18BIT_LOWER_20261017.zip`. R105's 31-bit upper bound remains an independent, unreviewed author construction.

The formal alphabet is the twelve signed directions of **six** native spatial axes, `{±1,...,±6}` (not twelve dimensions). A length-22 word belongs to `CYCL22` if (i) each axis has equal plus and minus counts; (ii) sorted plus-counts are `(1,1,1,1,3,4)`; (iii) no pair of cyclically adjacent letters are mutual inverses. The axis with `4/4` occurrences is the unique high axis `h`, and the axis with `3/3` is the unique secondary `l`.

Let `N_(a,b,c,d)(w)` be the number of order-preserving (not necessarily consecutive) four-letter subsequences. The terminal signed **formal integer readout** is

```
Z(w) = N_(h,h,h,l) - N_(h,h,h,-l)
       - 2 N_(-h,-h,-h,l) + 2 N_(-h,-h,-h,-l).
```

An exact deterministic single-pass observer must output `(h,l,Z)` with no external access to forgotten input letters or stored provenance. The adversarial lower-bound prefixes are compared at exactly 16 events; *all* distinguishing suffixes used in this proof yield **valid** CYCL22 words on both compared prefixes, so this is a promised-valid-input lower bound and does not require an observable reject symbol.

## Theorem R112 (20-bit online lower bound)

Every such observer must have at least

```
4 (64,908 + 3,159 + 69,599) = 550,664 > 2^19 = 524,288
```

distinguishable reachable memory states after its 16th input symbol. Thus `B_online >= ceil(log2(550664)) = 20 bits`. Combined *conditionally* with the unreviewed R105 construction: `20 <= B_online <= 31`. This new lower bound does not depend on R105's correctness.

### Proof: within-orbit injectivity

R106 has two constructed classes, sizes 64,908 and 3,159, and R107 adds a disjoint class of 69,599. Let `F` be their union of **137,666 distinct** length-16 legal prefixes. Every `p∈F` has the same twelve-direction occupation: axis 1 has `4+` and `4-`; axes 2, 5, 6 have `1+` and `1-`; axes 3, 4 each have `1+` and `0-`. Every `p` accepts five *common fixed* six-letter suffixes:

```
s2=(-3,+2,+2,-4,-2,-2)
s3=(+3,+3,-4,-3,-3,-3)
s4=(+4,+4,-3,-4,-4,-4)
s5=(-3,+5,+5,-4,-5,-5)
s6=(-3,+6,+6,-4,-6,-6).
```

Each `p s_j` is cyclically freely reduced and has terminal `(h,l)=(1,j)`. Each `p` is indexed by a tuple `(d2,t3,t4,d5,d6)` of integer source levels, with five terminal readouts `(d2,t3+4,t4+4,d5,d6)`. These tuples are injective within both R106 and R107 constructions; in addition, R106 has `t3∈{-4,0,1,2,4}` while R107 has `t3∈{-8,-7,-2}`, so their images are disjoint. Consequently every pair of distinct members of `F` is separated by a suffix that is valid for *both*.

For each `h∈H={1,2,5,6}` let `π_h` exchange absolute axis labels 1 and h while preserving direction signs; `π_1` is the identity. Let `F_h={π_h(p):p∈F}`. Direction-balance, cyclic free-reduction and the ordered-four-subsequence formula are equivariant under any such signed-axis relabeling. For each distinct `π_h(p),π_h(q)∈F_h`, a common probe `π_h(s_j)` gives two valid outputs that differ. Thus **each `F_h` contributes 137,666 pairwise distinguishable states**.

### Proof: cross-orbit separation by a single universally valid suffix

The crucial new lemma is that **the same unpermuted** `s3=(+3,+3,-4,-3,-3,-3)` legally completes **every** word `π_h(p)` for **all** `h∈H` and `p∈F`:

- Axis h has `4/4` counts and the three other axes of H each have `1/1`. Axis 3 has initially `1+/0-`; axis 4 initially `1+/0-`. Suffix s3 changes axis 3 to `3+/3-`, axis 4 to `1+/1-`. Hence the final counts are exactly the required `(4,3,1,1,1,1)`.
- The suffix has no adjacent inverse symbols. Every prefix is internally reduced. The prefix has **no -3**, so the boundary to the suffix's first `+3` is safe. The suffix's last symbol `-3` cannot cancel the prefix first letter, which is `±h` with `h∈H` and hence `h≠3`. The cyclic seam is safe.

Therefore `π_h(p)s3` is always a valid CYCL22 word with terminal `(h,l)=(h,3)`. Any prefixes from `F_h` and `F_k` with `h≠k` are distinguished by that **same valid suffix**, regardless of their `Z` values, because the first terminal output coordinate differs. This proof neither uses an invalid suffix nor relies on whether an invalid completion would emit `⊥`.

All four sets contain prefixes of the same length 16, so knowing the input clock does not circumvent distinguishability. Thus the four families form `550664` mutually distinguishable states. Since `2^19=524288 < 550664 < 2^20`, the theorem follows. □

## Exact verification and reproducibility

A local independent proof package `EM_X6_R112_AXIS_ORBIT_20BIT_20261018.zip` includes `PROOF_R112.md`, `verify_r112.py`, `verify_r112_independent.js`, copies of the original R106/R107 programs, `R112_CERTIFICATE.json`, a seven-file SHA-256 manifest and a README.

- Python reproduced 64,908 + 3,159 + 69,599 unique signatures and checked **all 550,664** transformed prefixes against common s3 for CYCL22 legality, terminal axes and exact Z. Sampled full five-probe outputs were also checked with an unrelated order-four scattered-subsequence DP.
- Independent JavaScript regenerated all base parameter families using *alternative legal source-difference representatives* and confirmed **all 550,664** CYCL22 completions by direct scattered-subsequence DP. Different generated-word hashes are expected because representatives differ.
- All seven artifact files were verified after fresh archive extraction; both verifiers passed from the extracted cold-start tree.
- Python ordered-transformed-prefix SHA-256: `808ef613e7a0d8abe57e1205ba172e12cc45d853c1a89203716230cc1a33184e`. JS alternative-representation digest: `52be6fbba217e2580d4bd0198ef19886ebc6285387ab78d8534a83010e93e3a8`. ZIP SHA-256: `c418d653b1d594688ca686b6caa1793089448b2a61f596f138c2ad153ba3d2de`.

The theorem is proved by the finite construction and equivariance lemmas above; the exhaustive checks verify the construction and its implementations. **No BRC-native provenance acquisition, physical experiment, Lean formalization, independent Driver review or canonical Result admission was done.** Formal signed integer postprocessing is not positive BRC branch mass or native physics.

## Next question (R113)

For a strict **21-bit lower bound**, construct >1,048,576 pairwise distinguishable prefixes of one fixed length, with a shared legal completing suffix for each pair. The present four saturated-high-axis orbits contain 550,664 states; enlarging one fixed fiber's five-readout signature set faces the R108 conditional combinatorial barrier. Explore different prefix occupancies/cuts or a richer set of co-legally-accepted suffixes. Do **not** mistake one-sided acceptance of an invalid completion for a promised-input lower bound. Review R105's 31-bit online code and the missing typed BRC provenance observer separately.

## Control/admission

This branch is author-side working material only. Source task enumeration returned `CONTROL_QUOTA`; Site-scoped connection is `static_machine_readonly`. No verified ACTIVE owner, formal task CLAIM, native Result freeze or independent Driver acceptance. P000/ACTIVE worldview are unchanged.