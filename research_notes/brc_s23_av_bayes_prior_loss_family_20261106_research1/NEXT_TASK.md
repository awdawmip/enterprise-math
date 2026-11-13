# Next discriminating research unit (2026-11-06)

Mother question: determine sharp ten-label S23 behavioral minimax bounds (previous reference `R_beh(k,10) in [1/2,2/3]` for k=4,6). The AV one-source result supplies an exact prior-sensitive obstruction for observer compression.

1. Read the frozen legal ten-label encoder and decoder and source-conditioning rule. Decide whether there exists one lawful policy producing, for fixed common (a,b), both AV full-stop experiment A_c and W=1_{AV:stop3} under both hypotheses. Record full policy, conditional law and a hypothesis-independent forward kernel if it exists.
2. If such a bridge exists, derive the exact transferred binary-risk inequality and check its direction for the mother minimax quantifiers. Compare the resulting inequality to the current [1/2,2/3] bound; calculate any actual improvement.
3. If that bridge is absent under the tested policy class, identify the exact legal constraint and test an alternate source-tagged observer or additional branch coordinate, retaining common b and the six-source positive BRC carrier.
4. Independent proof review: check Theorems 1–3 including breakpoint strict ordering, global-parameter uniqueness, and the stochastic-kernel contradiction. Keep status UNREVIEWED until actual reviewer receipt.

Executable check: run `node VERIFY.js` (modern Node with BigInt); expected output is stored in RUN_EVIDENCE.txt. Proof of all-real statements is in PROOF.md; tests enumerate 24 exact rational parameter pairs and 216 prior checks only.
