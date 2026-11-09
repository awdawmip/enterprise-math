# Addendum: exact 200,000-horizon risk / 82-block finite theorem

Date: 2026-11-09. Researcher-ID: EM-DIRECT-120F35; activity RA-E390CFB268A3F2894652D1DA.
Frozen S23/AV scientific source: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Status: author-side exact finite integer certificate, independent mathematical review pending.

## Theorem

Retain the definitions, strict rational log enclosure of theta, Bayes-risk observer model, and exact update proof in PROOF.md. With history length m=128 and every integer 1<=L<=200000, the first difference
    D_L = R(128,L)-R(128,L-1)
has the exact 82-block decomposition printed in RUN_EVIDENCE_200000.txt. Each row 'BLOCK first last A B' certifies the SAME exact affine formula D_L=A+B*theta for all integer L in that inclusive block. The 82 disjoint blocks exhaust L=1..200000.

In particular the previously unresolved first positive increment beyond L=100000 occurs at
    L=110836, with D_L = -3749+14298*theta.
The preceding flat interval L=96702..110835 has D_L=0.
A new best-return increment class appears at
    L=168028..168094, D_L=40385-154021*theta,
and reappears at L=168131..168191.
Then D_L=0 for L=168192..200000.

The new endpoint risk is exactly
    R(128,200000) = 479873 - 1830144*theta
                  ≈ 0.999189638839550016098816.

## Evidence and proof scope

VERIFY_ONLINE_RISK.py is the pure-stdlib verifier: running
    python VERIFY_ONLINE_RISK.py 200000
reconstructs all 200128 phase cuts, checks the strict theta interval with 160-term rational logs, certifies one common circular sort at both endpoints, performs all 200000 ordered Fenwick / dual-heap gap insertions, verifies all individual symbolic risk increments, and checks the cumulative 82-block sum. It separately rebuilds complete partitions for L=1142, 10000 and 100000 and compares exactly. These are integer comparisons, not float-tolerance checks.

Source file Git blob for the executed 200000-capable verifier:
    25ecda35f3ea5b7d5482b1ccfeabe649a8b25d16.
Source file Git blob for its complete actual 200000-step output:
    1d715b45969e551ab0d5f19319ca3153697f6104.

The general risk insertion lemma and O(N log N) arithmetic-comparison algorithm are established in PROOF.md. This addendum claims a precisely finite 200000-horizon certificate, not a closed-form general interval law for unbounded L. Circle-statistical scope does not automatically transfer to native X6 geometry.

## Next

Find a continued-fraction/three-gap generator that predicts exact interval endpoints and D_L values without prior global sorting, and use it to predict the first nonzero increment beyond L=200000. Independently continue geometric capacity plateau 413 with its own certified critical-region checker.
