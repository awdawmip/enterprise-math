# EC49FFL (partial) — Exact H10 classification for full BRC keys with z=1

Date: 2026-11-09. Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The completed subdomain is **h=10, z=1**, one complete BRC key and four signatures 1,2,4,8, measuring distinct nonempty ordered signed-native-X6 prefixes. Parent target: <=5 full keys, <=93 edges.

The original ordered operation/9-state DFA and proved 16-mask exact trie recurrence are inherited unchanged from [EC49FFJ](../EC49FFJ_NATIVE_PREFIX_TRIE_20261109/README_EC49FFJ.md). The complete key constraint is
`#a=z-1=0; #e=1; #c+#d=x+y-11>=1; #f=11-y-2>=0; #g=11-x>=0`.
Enumerating every nonnegative integer solution for the full-key counts with z=1 yields **45 keys**. Each key was exhaustively solved by the existing original native-BRC exact trie solver, checking all four signed-X6 witness paths. The completed rows span **383420 retained operation words** and **3317389 signed-prefix trie nodes**.

**Exact scoped optimum:** `min_{legal K=(x,y,1)} C_native(H10,K)=56`. Exactly seven complete keys attain it: `K=(x,12-x,1)`, `x=4,5,6,7,8,9,10`. The entire 45-key cost classification is saved in `EXACT_REPORT_EC49FFL_H10_Z1.json`. The analytic h>=4 family from EC49FFK supplies these seven achieving witnesses.

**Coverage boundary:** A subsequent attempt at the unrestricted H10 search was interrupted after these 45 complete z=1 key results and eight z=2 keys; no global H10 minimum is claimed, and no z>=2 exclusion is inferred. This note publishes the completed, independently checkable z=1 subdomain rather than waiting for the larger enumeration. Formal independent Driver review is still pending.

Reproduce with `VERIFY_EC49FFL_Z1.py` (same exact BRC/X6 solver; keeps z fixed to 1). Next research: split z>=2 by key-size and prefix-cost lower certificates, complete H10 or prove an analytic lower bound, then turn back to five-key/multiwindow quota patterns. No P000/worldview changes.
