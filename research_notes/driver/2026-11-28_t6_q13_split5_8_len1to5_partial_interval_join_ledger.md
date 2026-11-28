# T6 q13 split(5,8) lengths 1–5: exact alternate-solver ledger

Informed EM-DVR-DEBB5E, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. Five independently executed alternate-solver slices; all read back. Complete set of 7 partitions of 5 × 18 partitions of 8 of length <=5, exact set equality (126 pairs). Checked 252 raw/domain count fields against the three previously saved author-side coverage/fiber audits, zero differences. Per-row rejection sums and index coverage rechecked. Original author audit explicitly did not replay the lattice solver; this execution adds a distinct algorithm with shared nonblind inputs and Driver authorship of alternate solver, not clean independent review of own method. Relaxed nonsmooth high domain, common atoms retained, mixed congruences and both 2331 budgets. Same saturated lattice and dual coordinate interval uniqueness theorem. Zero valid witnesses. Original author and separate audit contributions retained.

## Executed ledger
```json
{
  "stats": [
    {
      "slice": "len1to3",
      "patterns": 70,
      "raw": 74021688,
      "search": 74021688,
      "index_pass": 21798580,
      "box_survivors": 1257,
      "valid": 0
    },
    {
      "slice": "len4",
      "patterns": 35,
      "raw": 373937148,
      "search": 373937148,
      "index_pass": 104829032,
      "box_survivors": 3790,
      "valid": 0
    },
    {
      "slice": "len5_pos1to3",
      "patterns": 15,
      "raw": 211092336,
      "search": 211092336,
      "index_pass": 60060845,
      "box_survivors": 2141,
      "valid": 0
    },
    {
      "slice": "len5_pos4",
      "patterns": 3,
      "raw": 424517184,
      "search": 424517184,
      "index_pass": 114419459,
      "box_survivors": 2427,
      "valid": 0
    },
    {
      "slice": "len5_pos5",
      "patterns": 3,
      "raw": 424517184,
      "search": 424517184,
      "index_pass": 108817084,
      "box_survivors": 1643,
      "valid": 0
    }
  ],
  "totals": {
    "raw": 1508085540,
    "search": 1508085540,
    "index_pass": 409925000,
    "box_survivors": 11258,
    "valid": 0
  },
  "coverage": {
    "completed": 692,
    "total": 885,
    "split5_completed": 126,
    "split5_total": 154
  },
  "minimum_observed_box_survivor_excess": {
    "pp": [
      1,
      1,
      1,
      2
    ],
    "np": [
      1,
      1,
      2,
      4
    ],
    "pos": [
      6,
      12,
      12,
      12
    ],
    "neg": [
      4,
      9,
      6,
      9
    ],
    "u": [
      "7",
      "-4",
      "-4",
      "2",
      "9",
      "6",
      "-6",
      "1",
      "1",
      "0",
      "0",
      "0"
    ],
    "masses": [
      "2830",
      "2504"
    ],
    "excess": 499
  }
}
```

## Pins
- 66e0eeb08b3e208072ad869080d4ed2131871a47:research_notes/driver/2026-11-28_t6_q13_split5_8_len1to3_modular_interval_join.md blob d2303cfb9bbee070cf08e4ba457a8ba6450259bd
- 1895592d991f3663c82133d82837caaa844bf8aa:research_notes/driver/2026-11-28_t6_q13_split5_8_len4_modular_interval_join.md blob 0a62e52ec10061367b344798cfb2cae876cfc002
- 86e1e42c088dda964308ba7e70115104601f383f:research_notes/driver/2026-11-28_t6_q13_split5_8_len5_pos1to3_modular_interval_join.md blob bb0d490a97b96ad40a6908c9eca76c43a4ae0569
- db3ca2ae6e75bc786019d14b9dea823e17a67c83:research_notes/driver/2026-11-28_t6_q13_split5_8_len5_pos4_modular_interval_join.md blob ff24f64ab82ea8ebb53243f802d5ac0702bd810f
- f5acfbd9481996599feed33fa9bb8e86cac7f5a5:research_notes/driver/2026-11-28_t6_q13_split5_8_len5_pos5_modular_interval_join.md blob 00bf1f250f7c7dc63def60ac3c51eb0766192fcc

Author-side coverage/fiber evidence (no independent search attestation):
- 5eacc4e8e68275f7c923f5e3c3ee9c901103bf11:research_checks/T6_P13_Q13_SPLIT5_8_LEN1_3_COVERAGE_FIBER_AUDIT_20261128.json blob e056c08e5dcca2ecb124b41d81c6ea049d127aed
- c1e94676591d8cc2261fc31b674979f4026ad0c2:research_checks/T6_P13_Q13_SPLIT5_8_LEN4_COVERAGE_FIBER_AUDIT_20261128.json blob 81e455f3aeff2f623037572558486c1f35a382b6
- 5cfd56eee15cf5c93484572962a0ab35701a5f88:research_checks/T6_P13_Q13_SPLIT5_8_LEN5_COVERAGE_FIBER_AUDIT_20261128.json blob 5228bf5ea44ec3d408856ca5f7f1b84adca91bc4

## Remaining
Split(5,8) negative lengths 6–8: 28 patterns; split(6,7): 165 patterns. Independent alternate-solver coverage 692/885. H0, observation-envelope sufficiency, lower-prime completion and global T6=2332 remain open. No Result acceptance or Task/mother closure. No fresh DA assertion for source-note storage.
