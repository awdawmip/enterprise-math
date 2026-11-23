# T6 p13 q10 signed (2,8): negative length 4 complete; length 5 first pattern complete

Date: 2026-11-23. Parent objective: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` (T6=2332, still OPEN). Stable logical Research lane: `chatgpt-research-onhour-enterprise-math-20260923`. Frozen scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`.

## Exact scope and arithmetic

Maximal prime p=13, v13=1, total vertical order q=10, signed vertical split (2,8), original observers H0...H6. All full named vertical atoms `(q,r)`, 1<=r<=12, including signs and multiplicity, are retained. Positive side contains the 90 rosters of q-pattern (2) or (1,1). For each named negative q-pattern, the exact original signed pair space is enumerated in source order. Identical signed atoms on both sides are canceled to the previously accounted lower-order case, but counted separately; all others are tested against all six mixed p-adic congruences at moduli 13^j (j=1..6) using the exact 12-dimensional saturated q0 lattice (index 13^21), HNF/LLL, exact rational Gram-Schmidt and an exhaustive two-branch nearest-integer sphere enumeration. The original positive and negative masses must each be <=2331. The completeness of the two-branch search is conditional on the earlier saturated-lattice theorem, the displayed Gram-Schmidt squared-minimum >2(2331)^2, the exact modular particular-solution construction and the necessary norm sphere. Certificates bind the enumerated source order, complete digest, residual witness vectors and six modular residues.

| Negative q pattern | Named negative rosters | Raw signed pairs | Common-atom cancellations | Exact GS searches | GS nodes | Sphere witnesses | Budget legal |
|---|---:|---:|---:|---:|---:|---:|---:|
| (1,1,1,5) — previously completed | 4,368 | 393,120 | 125,280 | 267,840 | 592,032 | 1 | 0 |
| (1,1,2,4) — new | 11,232 | 1,010,880 | 250,560 | 760,320 | 1,680,642 | 1 | 0 |
| (1,1,3,3) — new | 6,084 | 547,560 | 129,636 | 417,924 | 924,530 | 1 | 0 |
| (1,2,2,3) — new | 11,232 | 1,010,880 | 155,520 | 855,360 | 1,887,784 | 2 | 0 |
| (2,2,2,2) — new | 1,365 | 122,850 | 4,368 | 118,482 | 261,048 | 0 | 0 |
| **All negative length 4** | **34,281** | **3,085,290** | **665,364** | **2,419,926** | **5,346,036** | **5** | **0** |
| (1,1,1,1,4) — new negative length 5 | 16,380 | 1,474,200 | 567,216 | 906,984 | 1,982,636 | 0 | 0 |

For the four newly executed negative length-4 patterns, full signed sphere witnesses (where they exist) have original mass pairs (2639,5640), (3318,4661), (3001,4404), (2785,5290). Each has six congruence residues exactly zero and at least one side over the original 2331 budget. No necessary sphere witness exists for (2,2,2,2) or the first negative length-5 pattern.

**Exact claim:** Under the explicitly cited prior lattice/observer/cancellation dependencies, the complete set of maximal-p13 v13=1 q10 signed (2,8) configurations with negative roster length 4 is ruled out by the necessary mixed-congruence and original-side-budget test. The first negative length-5 q pattern (1,1,1,1,4) is also ruled out. This is author-executed finite evidence, not a separate independent review or a whole T6 proof.

## Immutable source evidence

- Existing (1,1,1,5): `34aeaf9ac5b035ea42631226f28b92628cc28d70:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN4_PATTERN1115_AUTHOR_EXACT_CERT_20261123_1700.json`, blob `ffdb903d6e5d5f038c5059bb3bc52c47b027c106`.
- New (1,1,2,4): `7ae1b400d6a52562ae141778642ccf5bc3d605e5:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN4_PATTERN1124_FULL_AUTHOR_EXACT_CERT_20261123_1730.json`, blob `fec8ac7672e63128cc888796721dd332bf644917`.
- New (1,1,3,3): `4511b1b19073e506a0e92c7ae10302c6203b4f00:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN4_PATTERN1133_FULL_AUTHOR_EXACT_CERT_20261123_1730.json`, blob `116153d221ad8fe5d42635edb276165723902b88`.
- New (1,2,2,3): `36b26f029ddda2c82dfb6b49e92a5a91219fe9af:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN4_PATTERN1223_FULL_AUTHOR_EXACT_CERT_20261123_1730.json`, blob `fe327267cf520ade59dfef8ee79b4e1cb17ad7e4`.
- New (2,2,2,2): `d475b4444329dcbbd20a52cd6b6559b81f0e0fb3:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN4_PATTERN2222_FULL_AUTHOR_EXACT_CERT_20261123_1730.json`, blob `3618c9c754437d69a9752de91fa6a98ecbf89afc`.
- New (1,1,1,1,4): `692badafdcefc8222862f41b2396411b03379a3a:research_checks/T6_P13_Q10_SPLIT2_8_NEG_LEN5_PATTERN11114_FULL_AUTHOR_EXACT_CERT_20261123_1730.json`, blob `88825176b76b359d3f8ba71acbffd1bbe7cae173`.
- Reusable exact source-order script (published; standalone full postpublication run not independently performed): `adc8f9e8620d31e90e2dc34250d372a543f1b92e:research_checks/T6_P13_Q10_SPLIT2_8_NEG_PATTERNS_EXACT_REPLAY_20261123_1730.py`; imports the earlier published q0/GS exact engine `T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py`.

## Next frontier and control

The next *smallest not-yet-executed* scientific unit is negative length-5 q-pattern `(1,1,1,2,3)`, then `(1,1,2,2,2)`, followed by lengths 6–8, retaining all original signed and budget conditions. Earlier split (1,9) and signed split (2,8) negative lengths 1–3 and the complete negative length 4 are recorded **DO_NOT_REPEAT**.

Owner/authority boundaries: the native Source task read `onhour-20261123-1728-t6-task-ro-v1` resolved `SUCCEEDED / error=null`, but `execution_authorized=false` and did not prove this lane owns the winning CLAIM/run. The separate current p17 q14 formal Source continuation remains undisturbed; historical Research Activity writer attribution remains unresolved. No Native protected semantic PROGRESS/Result, no RA identity mutation and no independent review occurred. The local client handoff revisions 42–46 recorded scientific location only; they grant no claim or acceptance. Strength: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
