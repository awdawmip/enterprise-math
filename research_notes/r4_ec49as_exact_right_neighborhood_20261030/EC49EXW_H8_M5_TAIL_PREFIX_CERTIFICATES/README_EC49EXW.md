# EC49EXW — Signed X6 private-tail separation and exact 399-case H8/M5 exclusion

Research date: 2026-11-04 Asia/Shanghai. Parent: EC49EXV (PR #1730, commit `73a3e1b9cdc577a1e19f7ed266e742d8b794e8b1`).
Status: AUTHOR-SIDE ANALYTIC THEOREM / EXACT FINITE INTEGER COMPUTATION / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pins (UNCHANGED): global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE worldview unchanged. Current behavioral rules separately read at global canonical `e6effa10d84713cdf51b1159084448edaa85213d` and EM canonical `d19932605e091c56d379b1a9461047e229fce62a`.

## Theorem W1 — Observer-preserving signed-native private-tail bound

Fix any legal full-BRC-key schedule `x` in the frozen signed six-axis seven-operation model. The mandatory h8 signature count is `m8` (2 for the cases here). Let `L8=2(u8+v8+w8-1)` be its signed primitive-step length and `L_<8 = max_{2<=h<=7}2(u_h+v_h+w_h-1)`. Let `E7(x)` denote the exact optimal cost of covering all h=2,...,7 mandatory observer signatures using the signed-native prefix trie (with the original 28 prepaid edges), and `E8(x)` analogously cover all h=2,...,8. Then

```
E8(x) >= E7(x) + m8 * max(0, L8 - max(L_<8, L8-3)).
```

*Proof.* All paths assigned to h8 have the identical complete BRC key and signed primitive-step length L8 (EC49EXN conservation). Each distinct required observer signature needs a distinct signed path. EC49EXP/EXQ established that any two distinct legal paths with the same complete BRC key and length L8 have LCP <= L8-3. Hence their edges at depths d > L8-3 are pairwise distinct. Earlier h<=7 paths have length <= L_<8, so no previously paid/selected earlier path can cover an h8 edge at a depth d > L_<8. At every depth d > max(L_<8, L8-3) up to L8, each of m8 mandatory h8 representative paths contributes a distinct new edge. Those edges are not among the 28 prepaid h2 base edges. Taking the union over these depths proves the bound. The statement remains valid when the displayed lower bound is zero. QED.

This is a conditional transfer from the exact already-published signed-native key/word/LCP results, not a claim about arbitrary coarser coordinate observers or external physics.

## Exact census and new certificates

Input: all 946 EC49EXS triple-collision candidate rows in `EC49EXS_TRIPLE_CANDIDATES.tsv`. Reconstructed actual signed-native word totals and the original EC49EXV frontier give exactly **579** unresolved triple arrangements with N>700 (the 367 prior exclusions are retained).

Direct independent TSV reconstruction and `SCREEN_H5_EC49EXJ.words` recensus gives: 284 have zero private-tail gain; 166 have gain 4; 129 have gain 6. Thus 295 positive-gain schedules collapse to **129 distinct, precisely identical h2..7 key/signature schedules with the same cutoff** (74 or 76). For all 129, the original EC49EXJ C++17 exact OR-mask integer solver reported `BOUND_PASS minimum_total_at_least=<74|76>` for all mandatory h2..7 signatures. With W1, these prove **E8>=80** for **all 295** schedules. No solver timeouts or errors in this h7 batch.

For the remaining 284 zero-gain schedules, a bounded full h8 OR-mask integer calculation attempted **154 distinct** cases, returning **104 `BOUND_PASS minimum_total_at_least=80`** and 50 timeouts (cutoffs varied from 1.2 to 2.0 seconds; a timeout is not a certificate). The other 130 zero-gain cases were not attempted in this run. All 104 completed cases have exact input digests, trie node/color counts and original successful output preserved locally; `RESULT_EC49EXW.json` records the exact source catalogue indices of every certificate and every timed-out instance. Source generators and solver are referenced by immutable PR files and reusable replay code is included here.

The new total is **399 disjoint exact exclusions** (295+104). Current unresolved triple **180** (=50 timeout+130 not yet attempted), double **44,234**, combined **44,414**. The already proven global bound stays `63<=E*<=80` because double collisions have not been completely optimized.

Coverage and proof status: W1 is a hand-proved conditional transfer of the published frozen signed-native prefix theorem; integer DP is exact for each fully constructed trie and stated cutoff. The 129 h7 source inputs were verified by the original algorithm. 104 full h8 inputs were verified similarly. The independent TSV-to-word census checked all 946 rows and exactly reproduced the 579/295/284 partition. This is author-side evidence; no formal native CLAIM, Result, Driver review or Foundation admission is claimed.

## Reproduction and boundaries

Same-parent PR sources: `EC49EXS_H8_M5_OBSERVER_SIGNED_MATCH/EC49EXS_TRIPLE_CANDIDATES.tsv`, `EC49EXT_H8_M5_TRIPLE_173_EXACT_DP/VERIFY_EC49EXT.py`, `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/SCREEN_H5_EC49EXJ.py`, `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/EXACT_OR_MASK_DP.cpp`. This folder's `VERIFY_EC49EXW.py` reconstructs input, full schedule, independent W1 partition, h7 groups, and can replay any chosen full h8 case with an explicit timeout. The output manifest separates proof-backed excluded cases from timed-out/untested cases.

The P000 X6 signed-primitive step sequence and complete BRC key are preserved; operator sequences and the nine-history observer map are not replaced by a coarse summary. The computation does not alter the task's scientific pins.

## Next EC49EXX

Process the remaining 180 triple cases, beginning with the 50 timed-out full h8 instances using richer exact DP state dominance or branch/cut, then the other 130. If the 180 are resolved with E>=80, triple-collision entire class is excluded below 80; afterwards handle the 44,234 double-collision candidates. Alternatively, extract a certified <80 signed-native witness from any full-h8 case whose exact DP returns feasible. See `NEXT_EC49EXX.md`.
