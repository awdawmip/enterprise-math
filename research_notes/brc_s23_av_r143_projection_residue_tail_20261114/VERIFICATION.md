# R143 reproducibility and evidence scope

Date: 2026-11-14. Exact Python Fraction arithmetic; no floats, random samples, or assumed formal solver. Run \`python check_r143.py 20\`.

## Finite independent checks

- **310** (m,K) pairs with m=1,...,10 and K=2,...,32: exact original parameter-event enumeration versus new support-endpoint interval criterion. Event generator explicitly includes **K-1** (initial floor), in addition to K,...,K+m-1, so no left-prefix discontinuity is omitted. All matched.
- **5,452** word-threshold computations: m=2,...,20, with all Sturmian words produced by an independent Farey slope/intercept generator. Every residue-class final failure and its next progression step were checked, and each computed T_w was checked to be present, with T_w-1 absent when T_w>2.
- **5,452** additional rational witness reconstructions at K=T_w: reconstruct an exact phase theta via the strict interval and independently evaluate all original floor differences, with 5,452/5,452 matches.
- The global maxima for m=2,...,20 were exactly:
  \`(2,2), (3,3), (4,4), (5,7), (6,9), (7,16), (8,19), (9,29), (10,33), (11,46), (12,51), (13,67), (14,73), (15,92), (16,99), (17,121), (18,129), (19,154), (20,163)\`.
- For m=5,...,20, all computed maxima equal \`E(m)=(m-2)*floor((m-1)/2)+1\` and have two complementary extremal maximizers.

Checker terminal marker: \`R143_PROJECTION_RESIDUE_PASS 310 5452\`.

The new exact membership and per-word tail formulas are all-m mathematical results proved in PROOF.md; the computed values are finite checks and are not used as a universal proof of \`T(m)=E(m)\`.

## Unresolved next lemma

For \`L=E(m)-1\`, put \`D_w(L)=L*(beta_w-alpha_w)+u_w(alpha_w)-ell_w(beta_w)\`. A useful candidate is \`D_w(L)>1\` for every \`w in W_m\` other than \`10^(m-2)1\` and its complement, for all m>=5. Tested on m=5,7,10,12,16,20; it remains unproved for all m. If verified, R139B's explicit extremal word criterion combines with R143.1 to settle the proposed permanent saturation formula for every m>=5.

Source status: author-side, independent review NOT_REVIEWED. External fixed-phase S23 model, not a native X6 result. Scientific pin \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
