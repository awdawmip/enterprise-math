# EC49FGH — A six-complete-key, 100-native-prefix construction for frozen 24 BRC demands

2026-11-10. Author-side research note, exact constructive result, independent Driver admission pending.

## Fixed scientific object and theorem

Preserve original frozen science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; original nine-state DFA, native X6 signed microsteps, operation words and raw complete key definitions from frozen model Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`. H2/H3/H5/H9 each require signatures {16,32}; H4/H6/H7/H8 each require {1,2,4,8}. All 24 words have window length, literal DFA signature, signed X6 endpoint (+2,0,0,0,0,0), and their positive-axis counts determine the raw three-part complete key (zeros distinguished).

**Proposition (explicit certificate).** A family of 24 legal words exists with exactly **6 distinct raw complete keys** and exactly **100 distinct nonempty ordered signed-X6 microstep prefixes**. In particular,

```
C_min(k<=6) <= 100.
```

The predecessor EC49FGG showed the global **5-key** minimum is exactly 112, by an integer branch/dual certificate. The sixth key therefore supports a concrete **12-edge reduction**, 112→100, without changing demands or observation. This proposition **does not** claim 100 is globally minimum for 6 keys.

## Construction

Start with the exact 112-edge EC49FGG witness. Keep the 18 unchanged original paths, and change six words as follows:

| Demand | New operation word | Complete raw key |
| --- | --- | --- |
| H6, signature 1 | `gefddg` | (5,4,1) |
| H6, signature 2 | `fegddg` | (5,4,1) |
| H6, signature 4 | `fegccg` | (5,4,1) |
| H6, signature 8 | `gefccg` | (5,4,1) |
| H7, signature 4 | `fegccgf` | (6,4,1) |
| H7, signature 8 | `gefccgf` | (6,4,1) |

The added raw key is **(5,4,1)**; the prior five raw keys remain in use:

```
{(3,0,1),(2,1,1),(3,1,1),(4,2,1),(5,4,1),(6,4,1)}.
```

The exact union prefix costs during a reproducible six-step local replacement sequence were 112, 109, 106, 105, 103, 102, 100. Different replacement order is immaterial to the final certificate.

## Independent exact verification

`SIX_KEY_WITNESS_EC49FGH.json` stores all 24 words and complete keys. `VERIFY_EC49FGH_WITNESS.py` uses explicit original DFA and signed-native microstep declarations and independently checks every word's signature, X6 endpoint, exact key, demand coverage and the union of unique **ordered** nonempty X6 prefixes. Its integer/dictionary calculation returns 24 demands, 6 keys and 100 edges. `REPORT_EC49FGH.json` stores the resulting scope and status.

This is an exact construction (not a global 6-key optimality proof, not an unreviewed physical prediction, and not formal Result admission). It reuses the EC49FGG five-key theorem, with no repinning of P000 or changes to frozen scientific requirements.

## Next scientific step

Explore the six-key minimum with an exact lower bound or smaller witness and the seven-key construction/optimality; compare with the previously constructed eight-key 93-edge witness. Keep key count conventions, typed observers and terminal signature set fixed. The original 5-key/93-edge joint target remains impossible **in this precise frozen model**, but the nearby key-cost frontier remains mathematically informative.

Author: `EM-DIRECT-5B6A8E`, activity `RA-41A7671EB26332A671ABB5D7` (registered Source); no current immutable EC49AS publication or formal CLAIM/Result, independent review pending.
