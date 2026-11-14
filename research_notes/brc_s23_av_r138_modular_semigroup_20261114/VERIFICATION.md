# R138 exact verification record

Local validation on 2026-11-14 with Python 3, standard-library Fraction and integer arithmetic. Command from this directory:

    python check_r138.py

Observed marker: **R138_MODULAR_SEMIGROUP_PASS**.

| Distinct check class | Executed checks |
|---|---:|
| Modular feasibility vs original exact rational interval | 6,560 |
| Exact rational witnesses against floor and strict fractional-part definitions | 1,282 |
| Local +b/+d interval feasibility implications | 39,944 |
| Global coefficient inclusion using P_(m-1) | 290 |
| Denominator-offset inequality D >= min(b,d) | 15,312 |
| Sharp all-gap boundary tests (m=2..20) | 19 |
| Exact individual-gap eventual cutoffs | 1,172 |

Feasibility comparison covers m=1..9, K=2,3,4,7,11,17,29,10^60+137. Local +b/+d implications and P_(m-1) inclusion cover m=1..10, K=2..30. The exhaustive word threshold reconstruction covers m=1..20 and K=2..m(m-1)+1 (m=1 uses K=2). Its completeness for later coefficients uses the separately proved R135 saturation tail.

| m | F_m | First full K | Eventual full K | R135 upper bound |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 4 | 2 | 2 | 3 |
| 3 | 8 | 3 | 3 | 7 |
| 4 | 14 | 4 | 4 | 13 |
| 5 | 24 | 7 | 7 | 21 |
| 6 | 36 | 9 | 9 | 31 |
| 7 | 54 | 11 | 16 | 43 |
| 8 | 76 | 16 | 19 | 57 |
| 9 | 104 | 22 | 29 | 73 |
| 10 | 136 | 25 | 33 | 91 |
| 11 | 178 | 29 | 46 | 111 |
| 12 | 224 | 41 | 51 | 133 |
| 13 | 282 | 46 | 67 | 157 |
| 14 | 346 | 51 | 73 | 183 |
| 15 | 418 | 67 | 92 | 211 |
| 16 | 498 | 73 | 99 | 241 |
| 17 | 594 | 79 | 121 | 273 |
| 18 | 696 | 99 | 129 | 307 |
| 19 | 816 | 106 | 154 | 343 |
| 20 | 944 | 113 | 163 | 381 |

The R138.3 all-gap cutoff is exactly U_gap=(m-1)^2+2; this is *not* the word-level eventual threshold shown in the table. The program verified the universal all-gap inequality and the immediately preceding missing-gap witness for each m=2..20. The algebraic proof works for all m.

Algorithmic cost: the Farey-gap inventory has O(m^3) entries; modular feasibility per gap is one remainder/comparison with polynomial bit length. Finite first/eventual word threshold reconstruction up to the R135 bound uses O(m^5) feasibility evaluations (plus inventory, word label construction, memory and set operations). A huge K does not force chronological enumeration of K-dependent event fractions. No empirical performance speedup claim is made.

Review status: **NOT_REVIEWED**; no external independent mathematical or formal checker acceptance asserted. Predecessor inputs: R137 immutable commit ab486d53fad5fdeb15b6c8647b6778b8b1e1b093; frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

Next discriminating question: union the separate modular feasibility classes of all Farey gaps representing one word, determine the exact last missing K of that word without an all-K sweep, then maximize over words.
