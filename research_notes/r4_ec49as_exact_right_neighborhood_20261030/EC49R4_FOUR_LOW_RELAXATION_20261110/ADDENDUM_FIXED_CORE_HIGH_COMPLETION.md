# EC49R4 addendum — Exact 22-edge high-signature completion of a fixed 64-edge core

Date: 2026-11-10 Asia/Shanghai. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Same signed-X6 codes, original nine-state DFA and 24-label pattern as `README_EC49R4.md`. Author-side exact finite computational result; no formal CLAIM/Result/independent Driver review.

## Conditional finite theorem

Fix **exactly** the original H2/H3 high seed and the 16 H4/H6/H7/H8 low operation words in README_EC49R4.md. Their ordered signed-native prefix union contains **64 edges**. Now freely select H5 and H9 high outputs 16 and 32, one word per required output per horizon, allowing every positive complete-key word (without the original five-key cap). Minimize additional distinct native prefixes.

**Exact result:**

```
min additional(H5:16, H5:32, H9:16, H9:32 | fixed specified 20 paths) = 22 edges.
min full 24 paths with this fixed 20-word core = 86 edges.
```

Exhaustive enumerator under the original DFA, endpoint and positive full-key conditions finds exactly **96** legal high-label operation words at H5 and **21,864** at H9. Their literal signed-X6 microstep-prefix trie contains **121,187 nodes** (including root). A four-bit integer trie dynamic program, zero-charging every existing one of the 64 fixed prefixes and charging each new signed-native prefix once, evaluates **290,428 exact mask merges** and returns **22 fresh edges**. The leaf-mask recurrence and induction are identical to the 16-mask complete proof in README_EC49R4.md.

An attaining addition uses:

```text
H5: 16=feggg,       32=gefgg    (key (3,3,1))
H9: 16=feggggggg,   32=gefgggggg (key (3,7,1))
```

The total 24-path family has **86 literal ordered signed-native prefix edges** and signed endpoint (+2,0,0,0,0,0) for each path. Independent original nine-history bucket-transformation rank calculation modulo **1,000,003** yields rank **9 at each of H2,H3,H4,H5,H6,H7,H8,H9**, so its rational observation rank is exactly nine. Its set of terminal signatures is precisely {1,2,4,8,16,32}.

## Crucial quota distinction

The low 16 paths require seven positive BRC keys; adding H5 and H9 makes **nine distinct positive full keys** overall. H6,H7,H8 each contain two different keys in the same horizon. Therefore the **86-edge 24-label family is a valid relaxed witness, not an original mother-model solution**: the original requires one complete key per horizon and at most five globally. The source H2/H3 high seed's special key interpretation is not silently reclassified.

This quantified gap is useful: it isolates **key unification and prefix cost together** as the next constructive problem. Can a different set of words make the six-horizon key scheme feasible under five distinct keys while limiting any cost increase relative to this 86-edge relaxed construction to at most seven edges? Existing 94-edge five-key witnesses demonstrate a feasible comparison point, so search should try changes in both the 64-edge core and H5/H9 high suffix, not merely alter existing key annotations.

## Reproduction and status

The author's runnable `HIGH_EXTENSION_OPT.py` and `VERIFY_86_RANK.py` are published beside this note, with exact output and independent rank record in `HIGH_EXTENSION_RUN.log` and `VERIFY_86_RANK.log`. The high-extension optimizer ranges over **all admissible high candidate words for the fixed core**; this is an exact conditional optimum, not the global unrestricted 24-label optimum. Source prior frozen model: `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py` Git Blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`.
