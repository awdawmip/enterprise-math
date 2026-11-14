# EC49FCO — Early-three plus H8-pair five-path rigidity

Status: **AUTHOR-SIDE FINITE EXHAUSTIVE PROOF / TWO EXACT IMPLEMENTATIONS EXECUTED / DRIVER REVIEW PENDING**. Scientific input is the unchanged frozen pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This continues EC49FCN at parent Git commit `1aa3cc7189750d03a79ca8dc9e88c8ae6ede0955`, reusing its `frozen_model.py` verbatim by import.

## Exact finite theorem

Under the original 24 slots, fixed H2/H3 roots, nine-state observer, ordered signed native primitive expansions and BRC key multisets `L=(4,2,1)`, `M=(7,3,2)`, replace any three of the ten H4–H6 observation slots and any two of the four H8 slots with legal words having the same window, key multiset and observation signature. For **every one of C(10,3)×C(4,2)=720 choices**, the minimum size of the distinct nonempty signed ordered prefix union is **exactly 158**.

Let `F` be the union of fixed slots' prefix sets, and `R_i(w)=prefixes(w)\F` for each selected slot. Then the exact cost is `|F|+|R_1∪...∪R_5|`. As the frozen original words form a valid 158-edge witness, a strict improvement exists precisely when a legal five-tuple has residual union size `< K=158-|F|`.

The frozen `candidates(h)` enumerates every multiset-permitted operator word and all nine-state signatures, excluding the absorbing reject state; `primpref` preserves sign and native primitive-step order. `VERIFY_EC49FCO_DIRECT.py` enumerates all legal early-three residual unions of size `<K`, followed by all legal candidates for the two H8 slots. It removes only candidate residuals or partial unions of cardinality `>=K` and exact duplicate residual unions. Union cardinality is monotone, so every removed partial branch is incapable of a strict improvement. Every surviving five-tuple is examined. No strict improvement exists in any of 720 cases. Hence the original valid 158 upper bound equals each optimum.

**Actually executed:** three disjoint exhaustive ranges `[0,240)`, `[240,480)`, `[480,720)` using an exact integer-bitset encoding of the finite universe of literal signed ordered prefixes; independent `VERIFY_EC49FCO_LITERAL.py` uses string `frozenset` prefixes and checks all 720 groups without bitsets. Every group's slot keys, fixed-prefix size and minimum 158 agree. Summed raw candidate Cartesian products: **29,494,686,816,000** (a theoretical product count, not actual operations). Executed final-stage union tests: **823,684**; fixed set sizes 141–149; largest qualifying early-three residual family 75. Full original row report SHA256: `518a30092029b2d15448c62cc7dbcb782f7cb3acaf102a4f6c169912c7aa76eb`. Literal independent report SHA256: `4240af7b5689e9380eec4878b0acd66b69566ab068af910493f8f12b0d78871c`. The compact certificate records every indexed group's fixed size and optimum; full raw evidence, logs, and executed code also exist in the author-side `EC49FCO_720_exact_evidence.zip` bundle.

Run from this directory with the predecessor frozen model on your import path:
```sh
PYTHONPATH="../EC49FCN_EARLY3_H7PAIR_COMPLETE_720" python VERIFY_EC49FCO_DIRECT.py --start 0 --stop 240 --output 0_240.json
PYTHONPATH="../EC49FCN_EARLY3_H7PAIR_COMPLETE_720" python VERIFY_EC49FCO_DIRECT.py --start 240 --stop 480 --output 240_480.json
PYTHONPATH="../EC49FCN_EARLY3_H7PAIR_COMPLETE_720" python VERIFY_EC49FCO_DIRECT.py --start 480 --stop 720 --output 480_720.json
PYTHONPATH="../EC49FCN_EARLY3_H7PAIR_COMPLETE_720" python VERIFY_EC49FCO_LITERAL.py
```

This is finite rigidity for this frozen BRC-key assignment, not a global 93-edge theorem. It does not change P000, the ACTIVE native-X6 worldview or source admission. **Next EC49FCP:** test early-three plus both H9 slots (120 groups), then compare early-two plus late-three, six-slot coordination and admissible changed BRC-key assignments. Native CLAIM/Result and independent Driver mathematical review remain separate.
