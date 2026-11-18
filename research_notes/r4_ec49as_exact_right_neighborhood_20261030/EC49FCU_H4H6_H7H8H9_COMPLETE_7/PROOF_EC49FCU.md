# EC49FCU — seven difficult mixed-late groups closed; H4:1/H6:1 pair's 32-group family complete

Date of computation: 2026-11-07 (Asia/Shanghai).
Classification: AUTHOR_FINITE_EXACT_PROOF / DUAL_REPRESENTATION_EXECUTED / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Parent: EC49FCT, immutable author commit `d2fe52f09e6c4f3c45a44a515d912208ad1dc560`, `PROOF_EC49FCT.md`, covering indices 160 and 168–191.
Source model: predecessor directory `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/frozen_model.py`, Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.
Source exact-bitset executor: `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/VERIFY_EC49FCS_EARLY2_H7H8H9.py`, Git blob `6403b576ea415646d80aa8971d75a7facc20af85`.

## Theorem (finite signed-native prefix language)
In the frozen model with 24 original witness slots, fixed BRC multiset cache keys L=(4,2,1) for H2–H5 and M=(7,3,2) for H6–H9, the nine-state observation automaton and the injective ordered signed-step prefix representation, let the five replaceable slots be `(4:1,6:1,7:1,8:s8,9:s9)` for each `s8 in (1,2,4,8)`, `s9 in (16,32)`. Among all legal simultaneous replacement words for each such selection, with the other 19 witness words unchanged, the minimum number of distinct **nonempty ordered signed primitive-step prefixes** is exactly **158**.

The predecessor EC49FCT certifies `s8=1,s9=16` (index 160) and all H7:2/4/8 cases (indices 168–191). This return directly certifies **indices 161–167**, so all **32/32** selections with early pair H4:1/H6:1 and one H7/H8/H9 slot are covered by the union of disjoint author-side certificates. The new seven indices are the unfiltered global 1,440-group order defined by `tuple(pair)+(h7,h8,h9)` where `pair` ranges over `combinations(early,2)` and `h7,h8,h9` over the corresponding `product(s7,s8,s9)`, using `frozen_model.REQ` insertion order.

## Exact finite reasoning
For word w, P(w) is its set of all nonempty literal **ordered** signed primitive prefixes. For the unchanged 19 words define F as the union of their prefixes. For each replaceable slot i, enumerate all legal words with prescribed multiset, trap-avoiding observer walk and terminal signature using the pinned frozen-model generator. Define R_i(w)=P(w)\\F and strict-improvement cap c=158-|F|. A <158 result exists iff some five options satisfy `|R_1 ∪ ... ∪ R_5| < c`. Original witness words remain valid at exactly 158, giving the upper bound.

The integer-bitset implementation maps each distinct literal signed prefix injectively to one bit and enumerates all candidate residuals. It discards any option with size >=c. Within an option pool or an intermediate stage it retains inclusion-minimal residuals, since A⊆B implies |A∪T|≤|B∪T| for any future T. For later pool j let I_j be the intersection of all residual options in j; every completion contains `M_i=∪_{j>i} I_j`. Thus partial state U can be discarded if `|U∪M_i|≥c`. These operations preserve every possible strict improvement. All seven final strict-improvement antichains are empty.

The independent checker `VERIFY_EC49FCU_LITERAL.py` was executed on **all seven** selections. It independently builds `frozenset[str]` literal signed prefixes, computes its own inclusion-minimal antichains, and **does not use integer bitsets or the mandatory-suffix pruning**. It agrees with integer-bitset results on fixed counts, caps, each slot's minimal-option counts, every stage's antichain size, actual union test count and absence of an improvement.

## Exact per-group computation, actual runs
| Index | H8 | H9 | |F| | c | slot option counts | stage antichain sizes | executed union tests |
|---:|---:|---:|---:|---:|---|---|---:|
|161|1|32|124|34|12,30,540,1890,1680|12,360,436,50,0|1,102,812|
|162|2|16|124|34|12,30,540,3150,1680|12,360,436,52,0|1,655,532|
|163|2|32|124|34|12,30,540,3150,1680|12,360,436,52,0|1,655,532|
|164|4|16|124|34|12,30,540,1890,1680|12,360,436,52,0|1,106,172|
|165|4|32|125|33|12,30,540,1890,1680|12,360,256,50,0|762,612|
|166|8|16|124|34|12,30,540,3150,1680|12,360,436,50,0|1,652,172|
|167|8|32|124|34|12,30,540,3150,1680|12,360,436,50,0|1,652,172|

**New: 7/7 exact; literal independent 7/7; 9,587,004 actual bitset stage unions; 5,966,835,840,000 unpruned Cartesian combinations (a combinatorial figure, not executed checks); peak intermediate antichain 436.** Decoded lossless `EC49FCU_7_EXACT.json.gz.b64` is 3,437 bytes, SHA-256 `5b715ea5dfbd55a109f4fd686df9305890328defbda41dc746daedf54c444127`. Each record preserves all seven keys, full exact counts and independent comparison. `base64.b64decode` then `gzip.decompress` restores JSON.

## Reproduce
From the immutable source directory `EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256`:
```sh
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 161 --stop 162 --literal 0 --output FCU_161.json
python VERIFY_EC49FCS_EARLY2_H7H8H9.py --start 162 --stop 168 --literal 0 --output FCU_162_168.json
PYTHONPATH=. python ../EC49FCU_H4H6_H7H8H9_COMPLETE_7/VERIFY_EC49FCU_LITERAL.py
```
The original integer-bitset executables were run in two bounded batches; group 163–167 were also independently repeated in an overlapping batch and the row records agreed. All seven literal checker rows were executed and checked against the bitset rows. The execution environment used Python's exact integer/set operations; no approximate arithmetic.

## Source and future work
The seven groups are a **finite auxiliary BRC-derived observer/word-language result** at the stated keys and signed-prefix measure, preserving the frozen scientific pin. P000 and ACTIVE X6 worldview unchanged. Previous author report: 8,213 five-path cases; with these 7 disjoint newly verified cases, cumulative **8,220 author-reported cases** (the previous cases retain their own exact historical evidence). The 1,440-case mixed-late family now has 288 directly reported groups (EC49FCS 256 + EC49FCT 25 + EC49FCU 7), with 1,152 not covered by these three certificates.

Source-native session issuance and live dispatch were attempted during this run, returning `FAILED/OSError` and `WAITING_RESOURCE/EVENT_COLLECTION_IO`, respectively. No current active owner or Source CLAIM/Result was confirmed; this is author-side publication pending independent Driver review.

Next: `NEXT_EC49FCV.md`, focusing on a different early pair and on local changes capable of challenging 158. The broader nine-window 93-edge mother problem remains open.
