# R636 — Rank-two BRC calibration research handoff

Date: 2026-11-08. Author side, no formal CLAIM. Researcher-ID EM-DIRECT-63422E, Research Activity RA-3A1E595AD88BF40AD7FE160B registered in the Source; no Driver review/acceptance. Direct continuation of R635 (86d36d60dcf43bd633592b7ca093c09bba3c137a). Frozen R462=18783e01e3646c72b7aab3b16d3f565e83e6446f, generator blob=7fa7a762f758b30c6090468ac43487daa34abad8.

Question: In a model with known coefficients c=(0,5,1,2,3,4), six axis nuisance backgrounds H_x=H0+c_x H1, and independent ± signed BRC gains satisfying nu5(A+)=a>=1, nu5(A-)>=a-1, how many matched backgrounds must be measured to recover S6 orientation?

Proved: any TWO distinct background references reconstruct H0 and H1; pure positive BRC valuation signals then distinguish all 720 orientations by d=a+8, with a strict cutoff lower bound. Any SINGLE reference at axis r has a FULL integer-polynomial collision between two different permutations. Witness: W=12 product U_j V_j, C_j=t^(a+2j-2)W, p<q last two non-reference labels; H'_x=(c_x-c_r)(C_p-C_q)/(c_p-c_r), swap p<->q, factor compensated probe outputs using W/(h U_k) and W/(h V_k).

The full proof with hypotheses and integer divisibility is R636_PROOF.zh-CN.md. R636_VERIFY.py is locally executed reproducible code with marker R636_COMPACT_REPRODUCE_PASS (32616 exact checked cases). R636_EVIDENCE.json records the second extended local integer check (33105 grouped checks) and all six witness locations. Full-size extended local artifacts may be retained separately as an attachment.

Current native Source task RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW publication TP2-47D65B35A7D48082EFBB was READY / NEEDS_DISPATCH with owner taskbook/unassigned at snapshot baff709f80f9fa5ed3790e0da90808835e35426f. The author-side result is not a native task Result or evidence of active CLAIM.

Next work: inspect actually registered Source X6 triadic/PF10/network operators for a genuine six-axis low-rank additive field and matched reference operation. If one is found, check gain invariance, provenance, source ordering, and future operation descent. If not, preserve the mismatch as a concrete residual coordinate and test its observable rank.
