# EC49FJD — all released-key six-word B=11 neighborhoods have exact cost 94 (2026-11-11)

## Finite theorem
Freeze the nine-state ordered/signed native X6 BRC input at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` and take either EC49FGJ original seven-key, 24-label, 94-prefix witness A or B. For every six-position replacement set Q, fix the original words outside Q and let F(Q) be their native signed-prefix union. Among Q with **|F(Q)|=82** and at least one of the original seven cache keys released by the fixed words, the minimum total native prefix cost of any legal completion using at most seven complete raw keys is **94**. There are exactly **3,918** such Q for A and **3,918** for B, **7,836** in total.

## Exact proof and numerical certificate
The frozen legal-word generator enumerates 178,850 (label,word) pairs and 94 complete raw keys; the two original witnesses check at 94 unique ordered signed microstep prefixes. For a 93-edge completion with |F|=82, the budget of new edges is 11.

Key-cover lemma: the unchanged 18 words occupy K_F keys; at most 7-|K_F| additional keys are possible. Exact Boolean cover DP on all 94 raw keys checks, for each released original key r, whether every missing observation can be covered while forbidding r. If each such prohibition prevents coverage, all released original keys are compulsory, and the original seven keys exhaust capacity. This holds for 3,912 cases per witness. Six per witness remain unrestricted in this sense.

Prefix-union lemma: for any selected missing labels, enumerate every legal word w with |P(w)\F|<=11 and form D_F(w)=P(w)\F, preserving all ordered signed native six-axis microstep prefixes. The DP carries prefix unions, extending U to U∪D_F(w) for each word. Keep only inclusion-minimal U with |U|<=11: if U1⊆U2 then U1∪S⊆U2∪S for every later S. An empty final antichain certifies infeasibility for that label subset. For forced-seven-key cases use all and only the original seven keys; for the other six cases use **all 94 keys**, giving a stronger key-unrestricted obstruction.

Per witness, 2,880 cases are excluded using only changed labels at windows 8–9; 1,032 need one lower-window label added. Among the six alternate-key-cover cases, 1 is excluded using high labels only, 4 need one lower-window label, and 1 needs all six labels. These five classes total 3,918 per witness. The unmodified six words always realize 94, establishing the exact optimum.

## Reproduce and audit
All four portable source inputs are copied into this directory: `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` (exact labeled demand triples from EC49FGW), `ec49fjd_shared.py`, and `VERIFY_EC49FJD.py`. Run `python VERIFY_EC49FJD.py` in the directory. It exhaustively checks each of the 134,596 six-position choices for each witness, emits all 7,836 per-case certificates to `EXACT_LEDGER_EC49FJD.json.gz`, and writes `EXACT_SUMMARY_EC49FJD.json`. The author-executed local run returned `EC49FJD_ALL_7836_PASS`, ledger uncompressed SHA256 `c72c3dc439e3b1393f38ef388696853970a67dc3327a46d2b1f0e06559964acd`, uncompressed length 1,794,423 bytes. The complete original local ledger is also preserved in the conversation evidence package; it is regenerated losslessly by the checked-in verifier.

## Scope and next
Native BRC finite-combinatorial source only; observer is the complete signed ordered X6 prefix set plus raw key identity. This is author-side finite exact computation pending independent Driver review and formal Result. No CLAIM/owner reassignment is asserted. Next test released-key B=15,17,18,23 and the remaining fixed-key neighborhoods; the global seven-key minimum C_min(7) remains open. The frozen scientific pin and P000 remain unchanged.
