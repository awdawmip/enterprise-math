# EC49FCU — finish seven difficult H4:1/H6:1 mixed-late groups

Predecessor: EC49FCT exact 25-group author-side proof. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, unchanged original signed-prefix encoding, nine-state automaton and fixed BRC cache keys L=(4,2,1), M=(7,3,2). Read `PROOF_EC49FCT.md` and decode the complete 25-group certificate before modifying the verified result.

**Specific first question:** For original unfiltered group indices **161–167**, representing H4:1/H6:1/H7:1 with the seven remaining H8/H9 choices, determine whether any simultaneous replacement has at most 157 distinct native signed ordered prefixes. Either produce explicit five replacement words and recount all 24 slots exactly or certify the 158 minimum with a complete finite-language search.

A previous run with `--start 160 --stop 168 --literal 2` hit a 100-second timeout during the batch, so it did **not** certify index 161. Investigate the expensive literal cross-check and stage ordering separately from the integer-bitset recurrence; preserve the exact same candidate semantics. Useful tests: test `--start 161 --stop 162 --literal 0` with a bounded resource budget, then compare a provably equivalent order `H8/H9/H7/H4/H6` or stronger suffix lower bounds. Do not equate timing out with impossibility. Preserve each successful row and its independent checker coverage.

If the seven groups close, the entire fixed H4:1/H6:1 early pair's 32 mixed-late groups is solved. The mother `early-two + one each H7/H8/H9` family contains 1,440 groups, with 281 currently evidenced by EC49FCS+FCT, so 1,159 groups remain outside the two completed certificates. Keep the original nine-window 93-edge objective and legal cache-key variation as alternative scientific routes.

Source-native active Owner and role remain unverified because of current control I/O errors. Persist author-side results with exact evidence and do not label them Source-admitted until the actual native claim/result and independent review exist.
