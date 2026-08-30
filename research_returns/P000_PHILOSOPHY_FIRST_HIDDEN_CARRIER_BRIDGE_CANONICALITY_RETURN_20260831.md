# P000 Philosophy-First Q18 — Hidden–Carrier Bridge Canonicality and Information Cost Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000Q18C1-5E7A92`  
Task-ID: `RS-P000-PHILOSOPHY-FIRST-HIDDEN-CARRIER-BRIDGE-CANONICALITY`  
Publication-ID: `TP2-50935B60B03C7F3C3C29`  
Claim-ID: `chatgpt-p000q18c1-20260831-0002-5e7a92`  
Execution-Record-ID: `ER-1234952091FA71FB31C6`  
Execution branch: `research/p000-phil-q18-hidden-carrier-bridge-canonicality-em-p000q18c1-5e7a92`  
Execution base: `7a6b80db39529874edc913253cff151948d91607`

Hard target:

`P000_HIDDEN_CARRIER_BRIDGE_CANONICALITY_AND_INFORMATION_COST_CLASSIFIED`

Primary terminal class:

`WEAKER_CROSS_SORT_RELATION_SUFFICES_FOR_NONSPLIT_INTERNALIZATION`

Secondary exact boundary:

`NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE`

## 1. Executive result

Q18 has a mixed but sharp exact answer.

First, the Q15 full `HiddenAxisInc` bridge is **not canonical**. Removing that bridge leaves two independently symmetric derived four-object systems:

- four hidden fibres derived internally from `HiddenBalance3`;
- four Q10 carrier stars derived internally from `CarrierStar3`.

The bridge-free primitive automorphism group is the direct product of an order-48 hidden automorphism group and the order-24 carrier-star automorphism group. On the 24 fibre-to-star bijections this product acts transitively. Every bridge has stabilizer order 48, so the 24 choices form one relative-frame torsor and there is no automorphism-fixed bridge. Q7 naturality therefore forbids any claim that Q15's chosen bridge is derivable from the bridge-free primitives.

Second, straightforward **forgetful weakenings** of the full bridge do not preserve the Q15 nonsplit mechanism:

- matching only the three `2+2` partition objects costs 6 choices but the resulting order-192 joint automorphism group splits over carrier `S4`;
- matching only the two orientation classes costs 2 choices and the resulting order-576 joint automorphism group also splits.

Thus the exact Q15 central-`C2` extension is not robust under these proper quotient forgettings.

Third, there is nevertheless a genuinely lower-information **alternative** cross-sort primitive that does not encode any fibre-to-star bijection and still yields a full-carrier nonsplit readout. Define `BlockOrientationBridge` as follows:

1. choose one unordered `2+2` partition `P={B0,B1}` of the four hidden fibres;
2. take the two block-orderings `(B0,B1)` and `(B1,B0)`;
3. take the two orientation classes of the four carrier stars;
4. pair those two hidden block-orderings bijectively with the two carrier orientations.

There are exactly `3*2=6` such relation states. The stabilizer has order 192, carrier image order 24, and carrier kernel order 8. It has **no homomorphic section**. The obstruction is elementary and exact: every hidden automorphism that swaps the two chosen blocks has order 4 or 8 (four of each), while a section must lift an odd carrier transposition of order 2 to an element whose hidden component has order dividing 2. No such lift exists.

So a weaker alternative relation does suffice for nonsplit internalization, but it yields a **different** nonsplit extension with a larger derived kernel. It does not recover the exact Q15 central-`C2` extension.

Finally, exhaustive subgroup analysis of the exact bridge-free order-1152 symmetry proves an information lower bound: **no full-carrier nonsplit coupling can have a relation-state orbit of size below 6**. `BlockOrientationBridge` attains 6. Hence 6 is the exact minimum finite choice-orbit cost for a nonsplit full-carrier coupling in this finite witness, while the specific full `HiddenAxisInc` matching costs 24 choices.

The cardinality alone is not enough: the 6-choice `PairPartitionBridge` splits, while the 6-choice `BlockOrientationBridge` does not.

## 2. Frozen bridge-free structures

### 2.1 Hidden side from `HiddenBalance3`

The Q15 eight-point ternary relation is retained exactly, but its certificate coordinates are not primitive.

For distinct hidden points, pair codegree in `HiddenBalance3` is:

`24 x 1 + 4 x 0`.

Therefore the four codegree-zero pairs are definable internally. Call their set

`F = {F0,F1,F2,F3}`.

Exact `8!` enumeration gives:

`|Aut(HiddenBalance3)| = 48`.

Its action on `F` is onto all 24 permutations, with kernel order 2. Thus the four fibres and their full permutation action are derived before any cross-sort bridge is added.

### 2.2 Carrier side from Q10

From the six `AxisType` elements and the four K4-star triples, derive

`S = Star(CarrierStar3)`,

with `|S|=4`.

Independent `6!` enumeration of the star hypergraph gives:

`|Aut(AxisType,CarrierStar3)| = 24`,

and its induced action on the four stars is the full four-object permutation group.

No A/B/C/D constants are used in the object language. Numerical labels occur only in the certificate.

### 2.3 Bridge-free product

Without any hidden–carrier relation,

`Aut_0 = Aut(HiddenBalance3) x Aut(CarrierStar3)`

has order

`48 * 24 = 1152`.

The pure carrier factor is present, so the carrier readout splits immediately in the bridge-free reduct.

## 3. Full bridge canonicality: exact 24-choice torsor

Let

`B = Bij(F,S)`.

Then `|B|=4!=24`.

For `(h,c) in Aut_0`, write `bar(h)` for the induced permutation of hidden fibres. The natural action on bridges is

`b -> c o b o bar(h)^(-1)`.

Exact enumeration proves:

- the orbit of every bridge is all 24 elements of `B`;
- every stabilizer has order 48;
- no bridge is fixed by all bridge-free primitive automorphisms.

Equivalently, after choosing one presentation bridge, the other bridges are obtained freely and transitively by relative carrier permutations. The invariant content is the **single 24-element orbit**, not any named matching.

Hence:

`CANONICAL_BRIDGE_DERIVED_FROM_EXISTING_RELATIONS = FALSE`.

The exact finite choice cost of the full bridge is:

- 24 equipotent states;
- Hartley information `log2(24) ~= 4.58496`;
- minimum fixed-length binary encoding: 5 bits.

This is an invariant symmetry index, not a claim that the primitive relation literally contains five Boolean fields.

The Q15 identity-matching stabilizer is the accepted order-48 nonsplit extension with kernel order 2. The checker independently reproduces the Q15 census:

- 24 carrier `(3,2,4)` generating pairs;
- 96 lifted pairs;
- `(AB)^4=z` for all 96;
- no section.

Thus the old nonsplit result is preserved exactly when a full matching is supplied.

## 4. Two proper forgetful weakenings both split

The first question is whether the full 24-way relative frame can simply be forgotten to a coarser quotient while retaining nonsplitting.

### 4.1 `PairPartitionBridge`: 6 choices, but split

For any four-set `X`, derive the three unordered `2+2` partitions of `X`. A full bridge `F->S` induces a bijection between:

`Part_2+2(F)` and `Part_2+2(S)`.

There are `3!=6` such quotient bridges; every one forgets four of the original 24 full matchings.

Fix one such partition bridge. Exact enumeration gives:

`|Aut| = 192`,  
`|carrier image| = 24`,  
`|kernel| = 8`.

But a homomorphic section exists. The checker finds a six-element hidden subgroup whose action on the three hidden partitions is the full three-object permutation group; composing the carrier action on pair partitions with this subgroup gives an explicit section.

Therefore:

`PAIR_PARTITION_FORGETTING => SPLIT`.

The exact Q15 central-`C2` obstruction does not survive this proper quotient.

### 4.2 `OrientationBridge`: 2 choices, but split

For a four-set, derive its two orientation classes (orderings modulo even permutation). A full bridge induces one of two orientation alignments.

Fix one orientation alignment. Exact enumeration gives:

`|Aut| = 576`,  
`|carrier image| = 24`,  
`|kernel| = 24`.

This extension splits: the hidden witness contains an order-2 automorphism inducing an odd fibre permutation. Composing carrier parity with this involution gives a section.

Therefore:

`ORIENTATION_FORGETTING => SPLIT`.

These two negative controls show that “coarser bridge” is not automatically enough.

## 5. A 6-choice alternative that is nonsplit

### 5.1 Definition without fibre-to-star matching

Let `P={B0,B1}` be one unordered partition of the four hidden fibres into two 2-element blocks.

The two block-orderings are:

`beta+=(B0,B1)`,  
`beta-=(B1,B0)`.

Let the carrier four-set have its two derived orientation classes:

`omega+`, `omega-`.

A `BlockOrientationBridge` is the two-tuple cross-sort relation

`{(beta+,omega+),(beta-,omega-)}`

or its reversed alignment.

Because there are three choices of `P` and two alignments, there are exactly six relation states.

This relation never names a carrier star adjacent to a hidden fibre. It does not define a function `F->S`. Indeed, after fixing one `BlockOrientationBridge`, its full automorphism stabilizer still acts transitively on **all 24** fibre-to-star bijections. Therefore no full bridge is hidden inside the candidate by definability.

### 5.2 Exact automorphism census

A hidden fibre permutation preserves the chosen unordered partition iff it lies in the order-8 setwise stabilizer of that partition. Such a permutation either preserves the two blocks individually or swaps them.

The joint relation is preserved exactly when:

`hidden_block_swap_bit = carrier_orientation_flip_bit`.

Lifting from fibre permutations to the exact eight-point hidden automorphisms gives:

`|Aut(BlockOrientationBridge model)| = 192`,  
`|carrier image| = 24`,  
`|kernel| = 8`.

So the carrier readout remains surjective.

### 5.3 Exact nonsplitting obstruction

Consider any odd carrier transposition `tau`. It has order 2.

A homomorphic section would have to send `tau` to a joint automorphism `(h,tau)` whose order divides 2, hence in particular `h^2=1`.

But compatibility with `BlockOrientationBridge` forces `h` into the hidden block-swapping coset. Exact enumeration of that coset gives:

- four elements of order 4;
- four elements of order 8;
- zero elements of order 1 or 2.

Therefore no lift of an odd transposition can be the image of a homomorphic section.

Hence:

`SECTION_EXISTS = FALSE`.

This is a new nonsplit finite extension, not the Q15 central-`C2` extension. Its derived kernel has order 8.

## 6. Deletion and minimality audit for the successful weaker relation

Three exact regressions isolate what is doing the work.

### 6.1 Delete the cross-sort relation entirely

Return to the direct product:

`|Aut|=1152`,  
`|carrier image|=24`.

The pure carrier factor supplies a section.

Result: `SPLIT`.

### 6.2 Keep the hidden `2+2` partition but forget orientation pairing

Allow both carrier orientations independently of hidden block ordering. Then:

`|Aut|=384`,  
`|carrier image|=24`.

Again the pure carrier action survives, so a section exists.

Result: `SPLIT`.

Thus selecting a hidden partition alone is insufficient; the cross-sort parity correlation is necessary.

### 6.3 Delete one of the two paired tuples

Keep only one pair, for example `(beta+,omega+)`.

Then hidden automorphisms must preserve the ordered bipartition and carrier automorphisms must preserve one orientation. Exact enumeration gives:

`|Aut|=96`,  
`|carrier image|=12`.

Full carrier surjectivity is lost.

Thus both paired tuples are required for the full `S4` readout.

This establishes deletion minimality of the two-tuple `BlockOrientationBridge` packet for this exact construction. No claim of globally minimum arity or one-symbol definability is made.

## 7. Exact lower bound: six relation states are necessary

This bound is stronger than testing a few hand-picked candidates.

Let `A` be the stabilizer, inside the bridge-free product

`Aut_0 = H x C`

with `|H|=48` and `|C|=24`, of any added finite relation state on this same witness. Assume the carrier projection

`A -> C`

is surjective.

Let

`K = ker(A -> C)`.

Then:

`|A| = 24 |K|`

and the orbit size of that relation state under the bridge-free symmetry is

`m = 1152/|A| = 48/|K|`.

Goursat reduction says that with `L=pr_H(A)`, the quotient `L/K` must match a quotient of carrier `S4` by one of its normal subgroups. The possible nontrivial quotient sizes are 2, 6, and 24.

The checker exhaustively enumerates all 55 subgroups of the exact hidden order-48 automorphism group and all relevant normal pairs.

For index-two hidden quotients `L/K ~= C2`, the nonsplit pairs occur exactly at:

- `( |L|,|K| )=(4,2)`: 3 cases;
- `(8,4)`: 6 cases;
- `(16,8)`: 3 cases.

There is **no nonsplit index-two pair with `|K|>8`**.

The quotient-to-three-partition `S3` cases all split; the full `S4` quotient is the Q15 order-48 / kernel-2 nonsplit case.

Therefore a full-carrier nonsplit coupling cannot have:

`m < 6`.

At `m=6`, the order-16 / kernel-8 nonsplit hidden quotient exists, and `BlockOrientationBridge` realizes it concretely.

Hence the exact finite lower bound is:

`MIN_FULL_CARRIER_NONSPLIT_CHOICE_ORBIT = 6`.

This is an orbit/information-cost theorem on the frozen finite witness. It is not a universal theorem about all hidden structures or all P000 models.

## 8. What this says about Q15

Q15's bridge has two logically distinct properties that should no longer be conflated:

1. **Canonical derivability:** false. The 24 full matchings form a single fixed-point-free torsor.
2. **Necessity of exactly that much cross-sort information for any nonsplit readout:** also false. A different six-choice primitive gives a nonsplit full-carrier extension.

But a third statement is true:

3. **Necessity of the full matching for the exact Q15 central-`C2` mechanism under the tested natural quotient forgettings:** supported exactly. The 6-choice pair-partition quotient and 2-choice orientation quotient both split.

So the correct interpretation of Q15 is not “the hidden relation naturally discovers the carrier,” and not even “24-way matching is the minimum cost of nonsplitting.” It is:

`HiddenBalance3 + one chosen full relative matching`

realizes one especially small-kernel nonsplit extension, while another form of cross-sort organization can realize nonsplitting more cheaply in finite choice cardinality.

## 9. Information cost versus structural form

The exact comparison is:

| Coupling | Choice states | Joint Aut | Kernel | Carrier image | Section |
|---|---:|---:|---:|---:|---|
| none | 1 | 1152 | 48 | 24 | yes |
| orientation alignment | 2 | 576 | 24 | 24 | yes |
| pair-partition alignment | 6 | 192 | 8 | 24 | yes |
| `BlockOrientationBridge` | 6 | 192 | 8 | 24 | **no** |
| full fibre-star matching | 24 | 48 | 2 | 24 | **no** |

The two six-choice rows are the key warning: **raw information cardinality does not determine splitness**. The placement of that information inside the automorphism structure matters.

## 10. Deterministic checker and certificate

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_HIDDEN_CARRIER_BRIDGE_CANONICALITY_CHECK_20260831.py`

Certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_HIDDEN_CARRIER_BRIDGE_CANONICALITY/P000_Q18_HIDDEN_CARRIER_BRIDGE_CANONICALITY_CERTIFICATE_V1.json`

The checker uses only the Python standard library and verifies:

- Q15 eight-point `HiddenBalance3`;
- `24x1 + 4x0` pair-codegree census;
- four internally derived hidden fibres;
- exact hidden automorphism order 48 and fibre image order 24;
- Q10 six-axis/four-star carrier hypergraph automorphism order 24;
- bridge-free product order 1152;
- all 24 full bridges form one orbit with stabilizer 48 and no fixed bridge;
- all 96 Q15 lifted generator pairs retain `(AB)^4=z`;
- 6-choice pair-partition bridge: order 192, kernel 8, explicit section;
- 2-choice orientation bridge: order 576, kernel 24, explicit section;
- 6-choice `BlockOrientationBridge`: order 192, kernel 8, full image 24, no section;
- block-swapping hidden coset order distribution `4^4 + 8^4`;
- candidate stabilizer acts transitively on all 24 full bridges;
- deletion regressions `1152 / 384 / 96` with split or image-loss outcomes;
- all 55 hidden subgroups;
- exact nonsplit index-two pair census;
- lower bound `m>=6`;
- attainment at `m=6`.

Local execution:

`PASS / WEAKER_CROSS_SORT_RELATION_SUFFICES_FOR_NONSPLIT_INTERNALIZATION`.

## 11. Method reuse and ontology boundary

Reused project methods:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE`;
- `T2_BLOCK_FINITE_CERTIFICATE`;
- the Q15 exact `HiddenBalance3` automorphism census.

No new global tool family is proposed.

Classical labels such as `S4`, `C2`, `S3`, dihedral groups, Goursat decomposition, orientations and subgroup indices are certificate-level finite mathematics. They are not promoted to bare P000 ontology.

In particular this return does **not** claim:

- that `BlockOrientationBridge` is canonical;
- that its order-8 kernel is a universal P000 kernel;
- that six choices are globally minimal across all P000 models;
- that the candidate has minimum primitive arity;
- that Q15's `F3^2` certificate coordinates are primitive;
- any Foundation, Working Truth, L4, or canonical-ontology promotion.

## 12. Driver recommendation

Recommended exact finite acceptance:

`Q15_FULL_BRIDGE_IS_A_NONCANONICAL_24_STATE_RELATIVE_FRAME; PROPER_NORMAL_QUOTIENT_FORGETTINGS_SPLIT; A_DIFFERENT_6_STATE_BLOCK_ORIENTATION_COUPLING_IS_INFORMATION_MINIMAL_FOR_FULL_CARRIER_NONSPLITTING_IN_THE_FROZEN_FINITE_WITNESS`.

Driver should preserve two boundaries simultaneously:

1. do not reinterpret Q15's arbitrary matching as canonically derived;
2. do not reinterpret the new six-state alternative as a proof that the exact Q15 central-`C2` extension can be obtained from only six states.

The new result changes the ontology-cost conclusion, not the certificate-level identity of Q15's extension.

Driver review is required.
