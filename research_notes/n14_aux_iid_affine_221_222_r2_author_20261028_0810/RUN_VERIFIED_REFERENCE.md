# Byte-identical execution of GitHub portable reference — Stage221–222

Classification: `AUTHOR-SIDE EXACT REPRODUCTION / NOT_ADMITTED`.

The exact 3,801-byte file already stored at immutable GitHub commit `ebc8d53d0849a118c5fcb36566f0b26ca325f5cc`, path `research_notes/n14_aux_iid_affine_221_222_r2_author_20261028_0810/PORTABLE_REPRO_STAGE221_222.py`, was executed locally under Python 3 using exact rational `fractions.Fraction` and integer-mass ordered DFS.

Source Git blob from the local executed bytes: `d531e3911e4bb07134bced126c0db1673e3a7768`; GitHub's actual remote readback blob: `d531e3911e4bb07134bced126c0db1673e3a7768`. **Byte-identical PASS.**
Source SHA256: `1af5a30c0f93fba59e960601b2b6abaa7c0d42a4aa8053d0664183c399f65a0f`.

Actual full stdout:

```text
STAGE221_PORTABLE_EXACT_PASS 46186
STAGE222_PORTABLE_EXACT_PASS 38956
```

Log SHA256: `18cf7f2a3d20338014b0307c74ed4ec2fc3cda5eecb52029c0495f0802126607`.

Checks performed by this exact source: complete 680-state rational Bellman values per stage, 1,238 positive action gaps and minimum gap, two specific tie sets, four deterministic strategy corners by suffix DP vs independent unmerged integer-weight ordered-history DFS, zero mixed coefficient, exact error-balanced coin law, both endpoint values, legal full real randomization, strict P/Q time dominance and supporting-line equality.

This program independently re-runs the primary author's Python calculations; it is **not** a separate human or Driver review, native X6 experiment, Source execution event or mathematical admission. The primary executed programs, complete four-corner certificates and original logs are preserved in the accompanying ChatGPT research archive, SHA256 `06d3e95c107eb0b7aa207390d8eb200a50f1c6c4ecf5b9bdd56653e5ce369f23` (12 files; archive is not a replacement for these GitHub-published runnable sources).
