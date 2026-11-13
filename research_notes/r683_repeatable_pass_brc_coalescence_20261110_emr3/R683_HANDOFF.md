# R683 — repeatable PASS, BRC branching and exact recoalescence
Date: 2026-11-10 Asia/Shanghai. Mother task RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW; publication TP2-47D65B35A7D48082EFBB. Original science frozen R462@18783e01e3646c72b7aab3b16d3f565e83e6446f. Predecessor R681@3b3414dc143583f06e71b8595f67235bf038305a. R682 Draft PR #1928 covers distinct cycle-credit/affine-spectrum work.

Files: R683_PROOF.zh-CN.md contains hypotheses, proofs and scope; R683_VERIFY.py is the independent standard-library exact integer/Fraction checker; R683_EVIDENCE.json gives explicit witness and finite 120×64 result.

Research: Allow the three R681 V29 PASS events to repeat indefinitely. The max(Q_e,w[a]-w[b]) scheduler always chooses a unique PASS because priorities (-2,3,-1) are distinct; it does not always choose a unique V27 activity triad. Explicit initial u=(-2,-4,-3,10), S=024 produces 12-step BABABABABABA and a 13th B event with score 98 attained by both 125 and 234. An exact rational BRC kernel gives each positive branch 1/2; they recombine into the same full (u,M,S) at time 19. Total supported states over all 120 starts at times 0,13,14,18,19,32,64: 120,122,123,123,121,121,121. Each run has exact total positive mass 1 and nonnegative ledger, sum(u) conserved.

Verify: python3 R683_VERIFY.py => final marker R683_REPEAT_PASS_BRC_EXACT_PASS. Interpretation: current-and-future (u,M,S) stochastic observer; retain original path identities separately if later measured. Scope: auxiliary local field scheduler, no claim of full native X6 link-port/V17 h/V39 j physical law.

Control: Artifact is author-side research and independently verifiable. Native session/dispatch requests were queued during this attempt, with no confirmed current CLAIM or Result at handoff creation. The existing owner and formal Driver decisions retain authority.

Next work: constrain repeated PASS with actual native X6 Cell/Link ports and V29 resource legality; add h and j to the state, obtain minimal exact BRC future observer or counterexample. Reuse frozen pin and actual source publication when it becomes available. No credentials in these files.
