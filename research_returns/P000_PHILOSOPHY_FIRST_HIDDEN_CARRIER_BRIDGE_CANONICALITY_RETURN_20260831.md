# P000 Philosophy-First Q18 — Hidden–Carrier Bridge Canonicality Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000Q18C1-5E9A2D`  
Task-ID: `RS-P000-PHILOSOPHY-FIRST-HIDDEN-CARRIER-BRIDGE-CANONICALITY`  
Publication-ID: `TP2-50935B60B03C7F3C3C29`  
Claim-ID: `chatgpt-p000q18c1-20260831-0000-5e9a2d`  
Execution-Record-ID: `ER-733709A5E73155CCAC78`  
Execution branch: `research/p000-phil-q18-hidden-carrier-bridge-canonicality-em-p000q18c1-5e9a2d`  
Execution base: `7a6b80db39529874edc913253cff151948d91607`

Hard target: `P000_HIDDEN_CARRIER_BRIDGE_CANONICALITY_AND_INFORMATION_COST_CLASSIFIED`

Terminal class: `NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE`

## 1. Result

Q15's `HiddenAxisInc` is **not canonically derivable** from the bridge-free primitive hidden structure and the Q10 carrier-star structure.

The bridge-free Q15 hidden relation internally derives four fibres by the codegree-zero rule. Its primitive automorphism group has order `48`; on those four fibres its image is all `S4`, with kernel the already-derived simultaneous two-point flip `{1,z}` of order `2`. Independently, the Q10 four carrier stars carry their full `S4` action.

Therefore, before a bridge is chosen, the symmetry acting on fibre-to-star identifications is

`Aut(HiddenBalance3) × Aut(carrier stars)`

with quotient action `S4_H × S4_C` on the two four-object sets.

There are exactly `4! = 24` bijections from the hidden fibres to the carrier stars. Under the bridge-free product action

`(g,h)·f = h ∘ f ∘ rho_H(g)^(-1)`

all 24 bijections lie in **one orbit**, and there is **no fixed bijection**. Postcomposition by `S4_C` is free and transitive, so the 24 bridges form a torsor of relative frames.

Choosing one bridge has stabilizer order `48`, carrier projection order `24`, and kernel order `2`; this is exactly the Q15 coupled automorphism signature. The deterministic checker independently re-runs Q15's 24 quotient `(3,2,4)` generating pairs and all 96 lifted pairs and again obtains

`(AB)^4 = z != 1`

for every lift, so the chosen-frame stabilizer is the same nonsplit extension rather than a new presentation artifact.

Hence Q15's success should be read as:

`HIDDEN INTERNAL STRUCTURE + ONE INDEPENDENT RELATIVE FRAME CHOICE -> NONSPLIT COUPLING`

not as:

`HIDDEN INTERNAL STRUCTURE -> CANONICAL CARRIER BRIDGE`.

## 2. Bridge-free derivation

The certificate uses the same eight opaque Q15 hidden points and eight `HiddenBalance3` triples already accepted by the Driver. The point names `u±,v±,p±,q±` remain checker labels only.

For every unordered hidden pair, compute its codegree in `HiddenBalance3`. Exactly four pairs have codegree zero and the remaining 24 pairs have codegree one. The four zero-codegree pairs are disjoint and cover all eight hidden points, hence they are definable from the primitive ternary relation alone and supply the hidden fibre set `F_H`.

Exhausting all `8!` hidden permutations gives exactly 48 primitive automorphisms. Their induced action on `F_H` is all 24 permutations. The fibre-action kernel has order two; its nonidentity element swaps the two points inside every fibre simultaneously.

On the carrier side no A/B/C/D naming is used. The four Q10 `CarrierStar3` neighbourhoods are treated as the derived four-object set `F_C`; their primitive carrier relabeling action is the full 24-element `S4_C`.

No bridge, projective coordinate, chosen bijection, or relative frame is used in either derivation.

## 3. Exact naturality obstruction

Let `B = Bij(F_H,F_C)`. Then `|B|=24`.

Because both quotient actions are surjective, for any two bridges `f_1,f_2` there is a carrier relabeling `h=f_2 f_1^(-1)` with

`(1,h)·f_1=f_2`.

Thus the product action on `B` is transitive. It is already enough to use the pure carrier subgroup to see that no `f` is fixed by the full bridge-free symmetry: if `h != 1`, then `h∘f != f`.

The stabilizer of any selected `f` consists exactly of pairs satisfying

`h = f rho_H(g) f^(-1)`.

It therefore has 48 elements, projects onto all carrier `S4`, and has kernel precisely the two hidden automorphisms acting trivially on fibres. This is the finite relative-frame form of Q15's coupling.

So there is no parameter-free natural bridge. Any concrete bridge breaks the independent `S4_H × S4_C` symmetry to a diagonal graph determined by one relative frame.

## 4. Information cost

There are exactly 24 admissible relative frames and no invariant distinguished one.

The exact finite choice cost is therefore:

- cardinality of the choice torsor: `24`;
- Shannon description cost under a uniform prior: `log2(24) = 4.584962500721...` bits;
- any fixed-length binary code requires at least `5` bits.

This is **not** 24 different unlabeled hidden theories. All choices are in one isomorphism orbit. The invariant content is that an independent relative frame must be supplied; the presentation label of the selected frame is gauge-like bookkeeping.

Accordingly, the information lower bound is a finite relational-choice cost, not a promotion of `S4`, `GL(2,3)`, `C2`, projective coordinates, or the certificate labels to bare P000 ontology.

## 5. Exhaustive binary cross-sort relation census

To test whether a weaker binary relation could retain the full Q15 readout without encoding a bijection, the checker exhausts all

`2^(4×4) = 65,536`

relations `R subset F_H × F_C` under independent `S4_H × S4_C` relabeling.

There are exactly `317` independent-relabeling orbits.

Only **four** orbits have automorphism projections equal to the full 24-element permutation group on both sides:

1. empty relation, edge count `0`;
2. a perfect matching, edge count `4`;
3. the complement of a perfect matching, edge count `12`;
4. full relation, edge count `16`.

The empty and full relations leave the two sides completely decoupled and therefore restore the split product.

The perfect matching is exactly a full fibre-to-star bridge.

The complement of a perfect matching has the same 24-element diagonal stabilizer, but it is not a weaker structural repair: the unique missing star in every row recovers the matching, and complementing recovers it definitionally. It therefore carries the same 24-choice relative-frame information and is rejected by the task's anti-repackaging kill condition.

Thus, within the complete binary cross-sort grammar:

`FULL S4 ON BOTH SIDES + NONTRIVIAL COUPLING`

forces matching-level relative-frame information.

## 6. Two genuinely weaker bridge tests

### Candidate A — one-incidence relation

Select only one fibre-star incidence.

Its quotient stabilizer has order `36`; its hidden and carrier projections each have order `6`, not `24`. Pulling the relation back through the hidden `48 -> 24` fibre action gives a 72-element hidden/carrier stabilizer, but the carrier image remains only order `6`.

Verdict:

`FAILS_FULL_S4_READOUT`.

It supplies less information than a full bridge, but does so by marking a preferred fibre/star pair and destroying most carrier symmetry.

### Candidate B — two-block `2+2` relation

Partition the four hidden fibres into two unordered pairs, partition the four carrier stars into two unordered pairs, and relate corresponding blocks completely.

The quotient stabilizer has order `32`; both side projections have order `8`, and the quotient kernel to either side has order `4`. After pullback through the hidden twofold fibre kernel, the coupled group has order `64` and carrier kernel order `8`, while the carrier image is still only `8`.

Verdict:

`FAILS_FULL_S4_READOUT`.

This candidate is genuinely coarser than a bijection, but it replaces the required four-star action by a block-preserving subgroup and enlarges the hidden kernel.

### Anti-matching control

The 12-edge complement of a matching does preserve the full order-24 carrier image and order-2 pulled-back hidden kernel. However it is definitionally equivalent to the missing matching itself.

Verdict:

`REJECT_REPACKAGED_FULL_BIJECTION`.

So neither tested genuine weakening recovers Q15, while the only binary apparent success simply re-encodes the full bridge.

## 7. Abstract exact-signature lower bound

The binary census can be strengthened at the automorphism-group level.

Suppose a cross-sort enrichment—of any relational arity—retains the **exact** Q15 symmetry signature: its coupled automorphism group `A` projects onto the full carrier `S4_C`, onto the full hidden fibre `S4_H`, and its kernel to the carrier is exactly the already-derived order-two hidden kernel `K={1,z}`.

Modulo `K`, the image `A/K` is a subgroup of

`S4_H × S4_C`

whose two projections are surjective and whose projection kernels are trivial. Hence `A/K` is the graph of an isomorphism

`phi:S4_H -> S4_C`.

For the natural four-point permutation group, every automorphism of `S4` is inner. One elementary certificate is that automorphisms preserve the six transpositions and their commuting/noncommuting incidence; the four maximal three-transposition stars reconstruct the four underlying points. Therefore `phi` is induced by a fibre-to-star bijection. The centralizer of the full natural `S4` action is trivial, so that relative frame is unique.

Consequently, any cross-sort relation that preserves the exact Q15 `C2 -> A -> S4` signature must contain **matching-level relative-frame information at the automorphism level**, even if the relation encodes that frame indirectly.

This is task-local finite structure only. It is not a universal definability theorem for arbitrary P000 models.

## 8. Deletion/minimality audit

- Delete the relative frame entirely: the automorphism group returns to the bridge-free product of order `48×24=1152`, with a pure-carrier section. Nonsplit coupling disappears.
- Replace it by one incidence: carrier image drops to `6`.
- Replace it by a `2+2` block bridge: carrier image drops to `8` and carrier kernel enlarges after pullback.
- Replace it by anti-matching: exact Q15 symmetry is recovered, but the full matching is definitionally recoverable, so no information is saved.
- Keep a full matching: stabilizer order `48`, carrier image `24`, kernel `2`, and all 96 Q15 lift checks satisfy `(AB)^4=z`.

Within the declared bridge-free structures and exact Q15 symmetry target, one full relative-frame choice is therefore information-minimal.

No absolute minimum-symbol or minimum-arity theorem is claimed against arbitrary encodings.

## 9. Tool reuse and deterministic checker

Reuse resolution:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE` -> `REUSE_EXECUTED`;
- `T2_BLOCK_FINITE_CERTIFICATE` -> `REUSE_EXECUTED`;
- no new global tool family is proposed.

Checker:

`research_checks/P000_PHILOSOPHY_FIRST_HIDDEN_CARRIER_BRIDGE_CANONICALITY_CHECK_20260831.py`

Certificate:

`research_artifacts/P000_PHILOSOPHY_FIRST_HIDDEN_CARRIER_BRIDGE_CANONICALITY/P000_Q18_HIDDEN_CARRIER_BRIDGE_CANONICALITY_CERTIFICATE_V1.json`

Deterministic local verdict:

`PASS / NO_NATURAL_HIDDEN_CARRIER_BRIDGE_WITH_EXACT_TORSOR_CERTIFICATE`

Verified counts:

- hidden primitive automorphisms: `48`;
- hidden fibre quotient image: `24`;
- hidden fibre kernel: `2`;
- bridges: `24`;
- bridge orbit size: `24`;
- fixed natural bridges: `0`;
- chosen-bridge stabilizer: `48`;
- quotient `(3,2,4)` generator pairs: `24`;
- lifted nonsplit checks: `96`;
- binary relations: `65,536`;
- independent-relabeling binary relation orbits: `317`;
- full-both-side-projection binary orbits: `4`, with edge counts `0,4,12,16`.

## 10. Driver recommendation and boundary

Recommended exact conclusion:

`P000_Q15_NONSPLIT_COUPLING_REQUIRES_AN_INDEPENDENT_24_CHOICE_HIDDEN_CARRIER_RELATIVE_FRAME;_NO_NATURAL_BRIDGE_EXISTS_IN_THE_BRIDGE_FREE_SIGNATURE`.

The strongest safe task-local lower bound is:

`EXACT_Q15_C2_TO_S4_SYMMETRY -> MATCHING_LEVEL_RELATIVE_FRAME_INFORMATION`.

Do not promote the certificate group names, point labels, or this finite witness to bare P000 ontology. Do not infer Foundation or Working Truth status. Driver review is required.
