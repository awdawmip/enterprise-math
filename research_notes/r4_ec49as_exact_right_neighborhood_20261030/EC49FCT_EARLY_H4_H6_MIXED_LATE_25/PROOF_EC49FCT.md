# EC49FCT — exact 25-group H4/H6 + H7/H8/H9 signed-prefix rigidity

Date: 2026-11-06. Classification: **AUTHOR_FINITE_EXACT_PROOF / DUAL_REPRESENTATION_EXECUTED / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED**.

## Frozen problem and result

Scientific input is frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This manuscript consumes the EC49FCS predecessor at immutable author commit `9033460324dff0d3f2778ad5a2f3104bfcaca7c8`. The model has 24 original witness slots, the nine-state observation automaton, the ordered signed-native primitive-step encoding, key multisets `L=(4,2,1)` for H2–H5 and `M=(7,3,2)` for H6–H9. The frozen witness has **158 distinct nonempty signed primitive prefixes**.

Let the original full 1,440-group order be
`[tuple(pair)+(h7,h8,h9) for pair in combinations(early,2) for h7,h8,h9 in product(s7,s8,s9)]`, where `early` lists H4,H5,H6 keys in `frozen_model.REQ` insertion order, and `s7,s8,s9` list H7,H8,H9 keys likewise. The completed indices are exactly **160 and 168 through 191 inclusive** (25 distinct groups). Every group replaces the H4:1 and H6:1 slots and one slot each of H7, H8 and H9, leaving 19 original witness slots fixed. Index 160 selects `(4:1,6:1,7:1,8:1,9:16)`; indices 168–191 select all H7:2, H7:4 and H7:8 signatures, all H8 signatures, and both H9 signatures.

**Theorem (frozen finite candidate language).** For every one of those 25 groups, the minimum number of distinct nonempty ordered signed primitive prefixes among all legal simultaneous replacements is **exactly 158**. The exhaustive search found no legal choice with 157 or fewer prefixes.

This proves 25 of the 32 groups for the fixed H4:1/H6:1 early pair. Seven indices 161–167 remain unresolved by this return. Together with the prior disjoint 256 H4/H5-mixed groups, the current `early-two + one-each-H7/H8/H9` family has **281 of 1,440** groups covered by these two results.

## Exact search proof

For any group of five selected keys `S`, let `P(w)` denote all nonempty signed *ordered* primitive-step prefixes of a word `w`. Let `F` be the union of `P(w)` over the other 19 fixed original words. The strict-improvement budget is `c=158-|F|`. For selected slot `i` and candidate `w`, use residual `R_i(w)=P(w)\\F`; strict improvement is equivalent to some five-way union of residuals having cardinality `<c`.

The frozen `frozen_model.candidates(h)` exhaustively enumerates each permitted finite multiset word by a decrement-and-restore recursion, omitting paths that enter the absorbing observer trap state 8, then partitions by exactly the prescribed terminal signature. Its bitset representation encodes distinct literal signed prefixes injectively. Candidate pools therefore cover the entire explicitly frozen legal word language for each key/signature.

Delete residual options with cardinality at least `c`. Keep only inclusion-minimal surviving residual masks: if `A⊆B`, then `A∪T⊆B∪T` for every later union `T`, so replacing `B` with `A` cannot destroy a strict improvement. For suffix slots `j>i` define `I_j` as the intersection of all their retained residual masks, and let `M_i=∪_{j>i} I_j`. Every completion contains `M_i`; a partial union `U` with `|U∪M_i|≥c` can be pruned. Exact antichain dynamic programming then advances through all five slots. Each of the 25 terminal strict-improvement antichains is empty. The unchanged original witness is a legal 158-prefix construction, establishing equality.

## Executed certificates and reproducibility

Exact integer-bitset search executed on all 25 groups. A second implementation directly on literal signed prefix `frozenset[str]`, **without suffix mandatory-intersection pruning**, independently checked **25/25** groups; fixed counts, strict caps, every stage antichain size and final no-improvement result agreed. No floating-point calculation is involved in these set decisions.

- Index 160: `|F|=125`, `c=33`, option antichain sizes `(12,30,540,1890,1680)`, stage antichain sizes `(12,360,256,50,0)`, 762,612 actual stage-union tests, independently matched.
- Indices 168–191: all 24 passed literal checks; 298,500 actual stage-union tests and maximum stage antichain 43.
- Combined: **25 exact optima**, **25 literal checks**, **1,061,112 actual stage-union tests**, max intermediate state count 360. The unpruned Cartesian-product total is **24,758,939,520,000**, a *combinatorial candidate count, not an execution count*.
- Frozen source model: `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/frozen_model.py` at the predecessor commit, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. This same byte content was actually executed; it constructs 16,156 distinct words and 109,972 distinct signed prefixes and asserts the original witness cost of 158.
- Reused verified executable source: `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/VERIFY_EC49FCS_EARLY2_H7H8H9.py` at the same commit, Git blob `6403b576ea415646d80aa8971d75a7facc20af85`, actual local SHA-256 `687895e8b3c9a13baee8727a51af53b11d8d71d320198d27b95369f66a8c0d8a`.

From the predecessor directory run the unchanged executable:

```sh
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 160 --stop 161 --literal 1 --output FCT_160.json
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 168 --stop 192 --literal 24 --output FCT_168_192.json
```

Both commands actually completed locally (approx. 12.7 and 6.5 seconds, respectively, as observed in this execution environment). The latter command and literal witness use the same frozen candidate alphabet and signatures. The two output JSON SHA-256 values, as generated by the program, are `d311835e347b59c5249aaefc913fd56f72d3be1408c3c2e8f0b0b556af722aef` and `1da4954c4b0ec9c19dcc3afd5711af74443cd34ca53d8811087a185d2b97caeb`.

All 25 raw group records are preserved losslessly in `EC49FCT_25_EXACT.json.gz.b64`: `base64(gzip(UTF-8 JSON))`, deterministic gzip `mtime=0`. Decoded JSON is 7,050 bytes with SHA-256 **`cb2fdbe27d695b2949e12b8482f729ba523bf9478970c495741812a1e987dc41`**. Each row carries the original index, all five signatures, exhaustive raw product count, fixed prefix count, strict cap, five candidate antichain sizes, five stage antichain sizes, actual union tests, no-improvement verdict and independent literal-check PASS. To inspect, decode with `base64 -d EC49FCT_25_EXACT.json.gz.b64 | gzip -d` (or Python's `base64` + `gzip`).

## Boundaries, provenance, and continuation

This is a completed **finite local-exchange** result within the stated original cache keys and frozen observer/word language, not a proof of the unrestricted nine-window 93-edge objective. It adds 25 disjoint groups to the previously reported 8,188 author-side five-path cases, giving **8,213 reported cases subject to the earlier certificates**; this return itself establishes only the new 25. A larger experimental range attempted in the same turn hit a bounded runtime timeout; no conclusion is claimed for omitted indices or other cache-key arrangements.

Source-native `session_start` returned `FAILED/OSError`, while canonical Owner inventory returned `WAITING_RESOURCE/EVENT_COLLECTION_IO/OSError`. GitHub author identity is `awdawmip`. There was no verified live Owner, formal CLAIM, native Result, or independent Driver admission. P000 and ACTIVE worldview are unchanged; the six-axis source uses the signed ordered word encoding of the frozen *auxiliary* model and does not assert a full native-X6 optimum.

Next scoped unit: `NEXT_EC49FCU.md`. Preserve the frozen scientific input separately from current normative rules.
