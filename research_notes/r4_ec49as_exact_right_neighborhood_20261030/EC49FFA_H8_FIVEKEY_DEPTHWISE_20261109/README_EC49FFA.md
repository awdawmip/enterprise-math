# EC49FFA — all remaining H8 mixed 23-word five-key structures have native signed-prefix cost at least 96

Date: 2026-11-09 (Asia/Shanghai). Status: **author-side finite exact result, not independently Driver-admitted**. Scientific input remains frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Native P000 signed X6, the exact original nine-state observer, full positive forward BRC keys and at most five distinct complete keys are unchanged.

## New finite theorem

In the previously unresolved H8 mixed type B `(1,8,16)` 23-word schemes, H2 is the low quartet `(1,2,4,8)`, H3 is the high pair `(16,32)`, H9 is high, and precisely three of H4–H9 are ordinary additional high-pair windows (counting H8 as a high-bearing mixed window). Words of one observation horizon may use **different** keys from the common five-key inventory. Cost is the number of distinct **nonempty ordered signed six-axis microstep prefixes** of all 23 original words.

| late high-bearing horizons, including mixed H8 | five-key inventories meeting all signature demands | verified universal lower bound on C_native |
|---|---:|---:|
| 5689 | 5,472 | **98** |
| 5789 | 9,216 | **96** |
| **newly classified** | **14,688** | **96** |

The original exhaustive signature-feasibility census is reproduced by the new exhaustive integer enumeration: 5689 has 5,472 feasible and 672 signature-infeasible inventories; 5789 has 9,216 feasible and none signature-infeasible. In 5689 the generated certified lower bounds range from 98 to 172; in 5789 they range from 96 to 185. These are **valid lower bounds**, not claims of sharp per-inventory optima.

Together with EC49FEZ's previously documented, separately checked H8 schemes 4589 (bound 110), 4689 (98), 4789 (111), and 6789 (105), all **26,652 original signature-feasible type-B H8 inventories** now have a certified native prefix cost **at least 96**. The original complete-key and operation-letter involution `I=(c d)(f g)`, `J(x,y,z)=(y+2z,x-2z,z)` transfers the statement to the typed-C mirror `(2,4,32)` in the scope previously established. Typed counts do not represent distinct untyped systems.

## Proof and exact certificate

For each five-key inventory K and required observation group g=(h,s), let W_g(K) be **all** original legal h-letter words using any key of K, with the required nine-state signature s and native six-axis endpoint (+2,0,0,0,0,0). Let P_d(w) be the first d *signed microsteps* of a word, a tuple retaining sign and order. All words of fixed (h,key=(x,y,z)) have the same microstep length

```
L(h,key) = 2*h + 2*(x+y-h-1+z)
```

because a, f and g expand to two signed microsteps, while c, d and e expand to four. Therefore the minimum length L_g(K) over the complete permitted word set is exact.

A certificate chooses, for each depth d=1,...,20, a subset D_d(K) of the 23 groups such that (i) every possible word of each selected group has at least d microsteps, and (ii) their **complete** possible signed depth-d prefix sets are pairwise disjoint across different selected groups. For any lawful one-word-per-group collection, each selected group contributes a different prefix at d; different d give different prefixes. Hence:

```
C_native >= sum(d=1..20) |D_d(K)|.
```

This is a direct finite integer proof. The constructive greedy independent-set search is used only to **find** valid D_d; it is not assumed optimal. A separate auditor reads each complete K,D certificate, reenumerates original words, recomputes endpoints/labels and signed prefixes, and checks every length and pairwise-disjointness condition and complete census coverage. The two full verifier runs returned `EXACT_INTEGER_PASS`, respectively **5,472 / 5,472** and **9,216 / 9,216**; 68,369 and 54,223 original group-key word instances also passed signed six-axis endpoint and DFA label checks.

The full per-inventory exact witness set consists of JSONL records `{keys,lower_bound,D}` (5,472 + 9,216 rows), with 20 depth-indexed selected group sets in each row. Local evidence SHA-256 for compressed bundle: `537c03824e44785ba3b0c3ba4dfc7abcb04d592b78b9486ecf7c30d127efbfcf` (159,008 bytes). The full archive was delivered as a conversation artifact alongside this research note. The primary GitHub package contains the mathematical statement and reproduce/audit code; the full raw JSONL witness archive is presently a conversation attachment, not claimed as a GitHub blob.

## Reproduce / audit

Use the Python standard library. Run `python3 h8_key_depth_sieve.py 5689 --limit 0` and `python3 h8_key_depth_sieve.py 5789 --limit 0`. The generator names these outputs `WITNESSES_5689_0_0.jsonl` and `WITNESSES_5789_0_0.jsonl`. Run `python3 VERIFY_H8_DUAL_DEPTH.py 5689 WITNESSES_5689_0_0.jsonl` and analogously for 5789. For bounded-memory repeated runs, use `--start / --limit` and concatenate disjoint consecutive ranges in inventory enumeration order; a `--limit` bound is exclusive. No LP, floating-point search, numeric tolerance, or third-party optimizer is used in the proof or validation.

The generator/validator reproduce the exact immutable source oracle `VERIFY_EC49FEZ.py` from the previous EC49FEZ research note; frozen source commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` is the unchanged science pin. The certificate proof checks complete BRC keys rather than a pooled-key relaxation, preserving possible mixed keys within every window.

## Continuation

H8 mixed 23-word types B/C are fully excluded under the <=93 edge target. Next address H7's two open configurations (5789 and 6789) and/or new permitted path counts/signature allocations. Existing 94-edge 22-word valid construction remains the recorded mother-family upper bound. This is an author-side exact finite classification, awaiting independent Driver review and any native Source Result authority.
