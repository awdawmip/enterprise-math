# R734 — Signed native X6 triadic-source loop carrier, sharp BRC branch symmetry
Date: 2026-11-12 (Asia/Shanghai). Parent: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`.
Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Actual P000 V5 dependencies: `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`, and mandatory `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`.
Scientific classification: explicit native-coordinate/N-BRC carrier theorem and exact finite verification; NOT a physical `TRIADIC_CLOSURE_E` event certificate, Task Result, or independent review.

## Exact question and typed objects

Can an actual three-source native balance be encoded as a three-step return of X6 signed unit Cell moves? If not, construct the shortest honest three-axis spatial return carrier that **preserves** the three signed source directions and branch orders, and determine the minimum S6-equivariant BRC branch multiplicity from an **unordered** signed source triad.

Choose a Cell `c` as an affine chart anchor, not a global ontic origin. P000 gives twelve signed spatial adjacency actions `c → c ± e_i` in its six-dimensional Cell torsor. A **candidate equal-quantum source triad** for this construction is an unordered set `Q={σ_i e_i, σ_j e_j, σ_k e_k}` on three *distinct* axes; its signed source identity is retained. The P000 `TRIADIC_CLOSURE_E` predicate, actual Cell/Link/Port force incidence, event timing and V29/V39 scheduler are **additional typed fields**, not decisions made by spatial endpoint arithmetic.

A spatial carrier word is an **ordered** list of six primitive axis moves that contains `+e_a` and `-e_a` exactly once for each of the three axes in `Q`. It is automatically a closed coordinate walk. Define the source-sign observer of this word by the **first occurrence** of each of its three axes. This extra convention is a declared encoding, not a physical law. Call the word NB if adjacent moves are never exact opposites.

## Theorem 1 — No odd native coordinate loop; sharp six-step three-axis return

Let `w=(ε_1 e_{i_1},…,ε_L e_{i_L})` be a native signed unit-step path, with endpoint displacement `d=Σ ε_t e_{i_t}`. Modulo 2, `Σ_a d_a ≡ L (mod 2)`; every step changes this parity. Thus **no odd-length path returns to its starting Cell**, in particular no three-step closed coordinate path can represent primitive triadic force closure.

More generally, any closed native path using `k` distinct axes must contain a positive and a negative move on each used axis, hence has length at least `2k`. The bound is sharp: for any signed triple `Q=(q_1,q_2,q_3)` on distinct axes, the six-step ordered carrier `(q_1,q_2,q_3,-q_1,-q_2,-q_3)` returns to the starting Cell and has no premature return or immediate reverse. This is a **coordinate carrier**; P000 triadic **force** closure remains the independent `TRIADIC_CLOSURE_E` relation. Replacing force closure by coordinate return would therefore be a type error, not a derivation from P000.

## Theorem 2 — Exact N-BRC census at the minimal length

Fix one unordered set of three native axes. The family of all length-six words using each of their six signed directions once has `6! = 720` source-distinct ordered members. Its first-return distribution is exactly:

| First return to anchor | Word count |
|---|---:|
| 2 steps | 144 |
| 4 steps | 96 |
| 6 steps | 480 |

Proof: First return at 2 is `3·2·4! = 144`. First return at 4 chooses its two axes in 3 ways; their four-step prefix has `4! - 2·2·2! = 16` first-return-four words, followed by the two orders of the last axis pair, giving `3·16·2=96`. The rest `720-144-96=480` first return at six.

The immediate-reversal-free subfamily has, by inclusion-exclusion on the three forbidden adjacent inverse pairs,
`6! - C(3,1)2·5! + C(3,2)2²·4! - C(3,3)2³·3! = 240` words.
Every such word has first return exactly at six: an earlier first return at two creates an adjacent reverse at positions 1–2; an earlier first return at four forces the final inverse pair at 5–6.

Flipping the positive/negative labels simultaneously for either member of any axis pair acts freely on the eight **first-occurrence sign patterns** and preserves first-return status and nonbacktracking. Hence each of the eight unordered signed source triads `Q` has exactly **60 first-return-six words** and **30 NB words** in this declared first-occurrence lift. There are `C(6,3)=20` axis triples, hence **160** signed source triads, **14,400** total six-step carrier words, **9,600** first-return-six words, and **4,800** NB words. These are positive integer *N-BRC branch multiplicities*, not signed force amplitudes.

## Theorem 3 — Sharp S6-equivariant non-deterministic branch cost

The P000 finite axis-permutation rotation skeleton `S6` acts by relabeling axes, carrying each signed source triad `Q` and its 30-word NB carrier fiber `W(Q)` to the corresponding fiber `W(gQ)`. Thus `Q↦W(Q)` is a faithful set-valued S6-equivariant carrier.

Let `k` be the number of positive directions in `Q` (`0≤k≤3`). The stabilizer of the **unordered** signed source triad acts on its three used axes as `S_k × S_(3-k)` and on the three unused axes as `S3`. Unused-axis permutations fix every carrier word. The effective used-axis action is **free** on each NB word, because every one of the three used axes occurs in the ordered word. Its orbits therefore all have exactly `k!(3-k)!` elements.

Any nonempty S6-equivariant selected subfamily `F(Q) ⊆ W(Q)` must be invariant under that stabilizer, hence a union of these free orbits. The smallest possible branch multiplicity is consequently

`m_min(Q)=k!(3-k)! = 6` for `k=0,3`, and `=2` for `k=1,2`.

The bound is **attained** by choosing one six-step NB word in an orbit for each signed-signature S6 class, then transporting its complete stabilizer orbit equivariantly. In particular, there is **no one-word deterministic strict S6-equivariant carrier selector from an unordered signed triad**, although a deterministic selection is possible after the ordering of three distinct force-source identities is explicitly supplied and retained.

This is a precise cost of missing order/source-frame information in a proposed local `TRIADIC_CLOSURE_E` → spatial BRC carrier. It does not require every physical three-force event to realize all thirty candidate loops; a native dynamical rule may select a genuine invariant subfamily, for which this orbit arithmetic immediately applies.

## Typed bridge proposal for a future actual event

Required native event input record (not invented here):
- `cell`: actual X6 Cell identity and chosen chart anchor;
- `signed_forces`: three distinct source IDs with signed native axis direction and nonzero equal quantum;
- `closure_certificate`: genuine predicate/reference for `TRIADIC_CLOSURE_E`;
- `links_ports`: actual native Link/Port incidence, not merely `±e_i` coordinate adjacency;
- `scheduler`: legal event ordering/time state, and explicitly authorized V29 PASS and V39 flow updates.

Conditional on a valid native event record of this type, `Q↦W(Q)` is a type-preserving **spatial readout carrier**, provided `closure_certificate`, source IDs and schedule remain attached to its branches; it is not a physical event simulator. An ordered source frame selects the explicit NB loop `q_1 q_2 q_3 q_1^{-1} q_2^{-1} q_3^{-1}`. Dropping that frame and choosing one sequence without the orbit repair breaks S6 covariance; retaining all 30 words or an invariant minimal orbit repairs the symmetry at the level proven here.

## Verification and precise status

The standalone `R734_X6_TRIADIC_LOOP_VERIFY.js` enumerates all 720 permutations of the six distinct signed moves on one three-axis set, computes first return and NB constraints, partitions by each of eight signed first-occurrence signatures, and enumerates the corresponding free stabilizer orbits. Each integer result is asserted; sibling JSON records the exact certificate. Python independently enumerated the same 720 local words with the same counts (first return 2/4/6 = 144/96/480, NB = 240).

These are exact, finite combinatorial statements plus general parity/support and group-action proofs. The next required scientific input is an **actual frozen legal Cell/Link/Port triadic-closure event with signed source IDs** and its genuine V29/V39 event update contract. Only then can the 30-to-one spatial carrier be tested for event-level provenance and flow fidelity. P000 and all frozen input pins are unchanged.
