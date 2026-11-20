# X6 r420 — 两个独立奇偶角色、共同核心与四种校准模型的精确对照

Date: 2026-11-20. Status: AUTHOR-SIDE EXACT ALGEBRAIC COROLLARY + COMPLETE FINITE CROSS-CHECK. **Not** a Native Result, independent Native Review, or a physical X6 rotation theorem.

Provenance: the same existing RESEARCH_DRIVER logical line EM-DVR-DEBB5E. Extends r419@644ed978e5229d6ef62a5494d690889646300092; reuses r411/r415/r418 only at their explicit group-action assumptions. Original native X6 contributors EM-EMF6D046-5A2844, EM-X6-DFD1FD, EM-X6CM-EDBD55 remain distinct; this author-side crosscheck does not claim independent reviewer identity.

## Exact algebraic object and theorem

Let `B_6=(C_2)^6 ⋊ S_6` act on the twelve abstract signed primitive letters `±e_i`, by `g(e_i)=ε_i e_{π(i)}`, with `ε_i∈{±1}` and `π∈S_6`. The following are **ordinary finite-group characters**, not native P000 rotation or orientation axioms:

`p(g)=sgn(π)`, `s(g)=∏_{i=1}^6 ε_i`, and `χ(g)=(p(g),s(g))`.

**Theorem (four-coset discriminator).** Both characters are homomorphisms, and `χ:B_6→{±1}²` is onto, with four fibers of exactly 11,520 elements each. Define

- `G_A=ker p=(C_2)^6⋊A_6` (the explicit r411–r418 model);
- `G_+=ker(p·s)` (the alternate r419 determinant-positive signed-matrix model);
- `D=G_A∩G_+=ker p∩ker s`.

Then `|B_6|=46,080`, `|G_A|=|G_+|=23,040`, `|D|=11,520`, `B_6/D≅C_2×C_2`, and **`G_A G_+=B_6`**. The ordered pair `χ(g)` is invariant under conjugating `g` by any signed-permutation frame change in `B_6`.

Proof: The product of all signs is invariant under permuting sign coordinates, so `s` is multiplicative in the semidirect product; `p` is the permutation-sign character. The independent signed flip and odd permutation realize generators of the two components of `{±1}²`; hence `χ` is surjective. Every fiber has `46,080/4=11,520` elements. The displayed kernel identities and orders follow. The subgroups are normal index-two; their product has order `|G_A||G_+|/|D|=46,080`. Any homomorphism to an abelian group is constant on conjugacy classes, establishing frame-change invariance. QED.

These are *different* character kernels: `G_A` contains cosets `(+,+)` and `(+,-)`; `G_+` contains `(+,+)` and `(-,-)`; the shared core `D` consists only of `(+,+)`. Thus a verified native physical event whose **spatial effect** is a signed-permutation element in `(+,-)` would rule out the assertion that **all** native rotations lie inside `G_+`. An event in `(-,-)` would similarly rule out containment in `G_A`. No finite set of inclusion observations alone establishes equality with either candidate. If the native event is not represented by one global signed-permutation cell map, this parity test is not applicable.

## Fixed three-axis suffix: exact companion calibration

Fix the ordered positive suffix `s_0=e_1e_2e_3` pointwise; all following words are unrestricted primitive signed-letter words and **not** asserted to be realizable native Cell/Port/triadic events. Let `K=Stab_G(s_0)`; `d` is the shortest fixed probe whose pointwise K-stabilizer is trivial; `b(n)` is the worst-case minimum fixed-length literal-repair bits for an `n`-letter prefix through the orbit of prefix concatenated with `s_0`.

| candidate `G` | `|G|` | `|K|` | `d` | `b(1)` | `b(2)` | `b(n≥3)` |
|---|---:|---:|---:|---:|---:|---:|
| `B_6` full signed permutations | 46,080 | 48 | 3 | 3 | 5 | 6 |
| `G_A` even permutations, unrestricted signs | 23,040 | 24 | 3 | 3 | 4 | 5 |
| `G_+` ordinary determinant-positive | 23,040 | 24 | 2 | 3 | 5 | 5 |
| `D` even permutations **and** even sign parity | 11,520 | 12 | 2 | 3 | 4 | 4 |

All four have `b(0)=0`; these are model-conditional orbit-fiber storage bits, not actual event-source compression estimates.

Proof: After pointwise fixing three positive axes, the residual action on the other three signed axes has orders `2^3·3!=48`, `2^3·|A_3|=24`, `2^2·3!=24` and `2^2·|A_3|=12`, respectively. To compute the exact maximum fiber for a prefix of length n, choose distinct unused axes until the stabilizer ceases shrinking: the orbit size is `|K|/|Stab_K(u)|`. Fixing `e_4` leaves stabilizers of size `8,4,4,2` in the table's order; fixing `e_4e_5` leaves sizes `2,2,1,1`; fixing `e_4e_5e_6` makes all trivial. Hence the maximum fiber sizes for n=1,2,≥3 are respectively `(6,24,48)`, `(6,12,24)`, `(6,24,24)`, `(6,12,12)`. Taking ceilings of base-2 logarithms gives the bit table. Repetitions cannot reduce a stabilizer more than distinct axes, so these attain the maxima. A shortest pointwise-stabilizer-killing probe uses 3,3,2,2 distinct remaining axes respectively; simultaneous sign flips on two unprobed axes prove the lower bounds where applicable. QED.

In particular, the common core `D` needs **4** bits for arbitrary primitive word histories after three fixed axes, while either 23,040-element candidate needs **5** bits. Thus one extra worst-case bit in the two larger groups measures parity cosets beyond their common core. This comparison is not a prescription to discard that bit in a native observer.

## Finite exhaustive cross-check and physical transfer boundary

A fresh exact enumeration traversed all `6!·2^6=46,080` permutation/sign assignments. It counted `11,520` elements in each of the four `(p,s)` fibers. It independently reproduced the pointwise stabilizer counts for k=0,…,6: for `G_A`, `23040,1920,192,24,4,2,1`; for `G_+`, `23040,1920,192,24,4,1,1`; and for k=3 the four-group cardinalities and chains above. This finite check corroborates the group-theoretic proof; no floating approximation is involved.

The current P000 V5 signed-six-axis Cell torsor gives the `±E_i` directions, the component quadratic readout and primitive adjacency, but does **not** define physical X6 rotation as a matrix determinant character. Its triadic `TRIADIC_CLOSURE_E`, Cell/Port, branch/provenance and time-successor admissibility are additional typed conditions. The first discriminating native next action is to exhibit an actual, source-pinned legal rotation event with a well-defined signed-permutation spatial effect, verify its parity pair and test that the *whole event* respects future lawful composition. If no such global map exists, work with the verified native transition relation/kernel instead. Preserve the physical interpretation as open.

No CLAIM, new Researcher identity, Native Result/Review acceptance, parent closure or Source Activity reassignment is implied by this note.
