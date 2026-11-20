# Stage439-B — Exact minimal repair after the protected-overlap condition fails

Parent Stage438-B: `research_notes/n12_x6_native_brc_stage438b_protected_overlap_minimal_20261105_RESEARCH2/PROOF_STAGE438B.md`, executable JS checker and executed JSON. Frozen science: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Refresh behavioral rules separately; parent Stage437-B sufficient corridor at commit `e098cfb9417d3df15c89da6843dd4d110917d67a`.

## Mathematical question

Stage438-B proves exact joint future equivalence in the protected-overlap regime `m-p_P >= n+r_Q`, where the P original prefix remains intact at all possible Q indices. Extend to `m-p_P < n+r_Q` with both sources having POP and APPEND budgets. Determine whether one can split the overlap into protected, mutable-original, and appended regions with a minimal explicit relation-carrier; test whether simply combining two protected keys fails.

## Specific first experiment

Enumerate pairs over `A=+E1,B=-E1,C=+E2`, for `(m,n)=(4,4),(5,4),(5,5)`, budgets `(p_P,r_P,p_Q,r_Q)=(1,1,1,1)` and `(2,1,1,1)`, all 12 signed APPEND actions and every legal interleaving; compare exact full observer traces `O=(m,n,V_P,V_Q,J_P,J_Q,K)`. Group by present O, then exact future signature. For every proposed key collision, give a specific operation word distinguishing it; for every proposed merging, prove or exhaustively check the complete declared finite domain. Keep integer class populations and bit lengths. Formalize one bounded generalization only if its proof can be completed.

## Cost and return

Report input conversion O(m+n), key/rank/unrank and codebook cost, per-operation update bit complexity, and original-history recovery cost. Publish proof or a strict finite counterexample, runnable checker with actual executed evidence, and the next exact mathematical question to the existing Draft PR research branch; maintain native owner/CLAIM and independent acceptance boundaries. No claim of physical heartbeat or full BRC signed-amplitude reduction follows from the X6 positive-unit observer.
