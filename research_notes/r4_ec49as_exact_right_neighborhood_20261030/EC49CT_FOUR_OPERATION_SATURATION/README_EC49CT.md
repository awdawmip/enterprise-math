# EC49CT — Exact native X6 BRC saturation at four future operations

Date: 2026-11-01 (Asia/Shanghai). Status: AUTHOR_ANALYTIC_PROOF / EXACT_Q_EXTREME_FIBER_PASS / GENUINE_MODULAR_WITNESS_PASS / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED.

## Source, model and definitions

Verified GLOBAL_KNOWLEDGE_V1 canonical main a1eb5340e1c814b20999bbcb07a6781aca621257 and Enterprise Math main 993a408982a302265cb3c31f93e69e4751299500, prior EC49CS source 8ccf4816303707e0514f2cb61c7b398da9d3de25 in PR #1730. P000 and ACTIVE worldview unchanged.

Primitive ordered signed-X6 alphabet comprises +E_i and -E_i for i=1..6, retaining all six displacement coordinates. Positive BRC channels have plus-step weights w0=(2,3,3,2,1,1), w1=(3,2,3,2,1,1), minus-step weights 1; third channel counts paths. Final four A/B tags are detected with an ordered nine-state automaton recognizing adjacent A=(+E1,+E2) and B=(+E2,+E1). Actual path-channel weights are correlated, not independent. Allowed complete suffix operations are a=(-1,-1), b=(-2,-2), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3). Exact-four language S'^4 contains 625 complete operation words; cumulative S'^{1..4} contains 780. Observer R(s,t,j) sums native positive-BRC weight or count for prefixes whose total signed endpoint after suffix s is zero and whose completed A/B tag is t, channel j=0,1,2. Dimension minimality refers only to rational-linear additive exact observer states for this finite language.

## Main theorem

At genuine ordered signed-X6 prefix length n=14, exact-four observer rank is **365 of 366** and cumulative one-through-four rank is **395 of 396**. At n=16 the respective genuine ranks are **366 of 366** and **396 of 396**. All greater even n attain these ranks. Therefore both languages have exact earliest real-path saturation **n_sat(4)=16**.

### Formal rank upper bounds

EC49CS proved the finite-Q 9-state rowspace recurrence: at h>=2, exact-h rank is 3(11h^2+15h+8)/2 and cumulative one-through-h rank is 18h^2+24h+12. At h=4 these give 366 and 396. The 25 formal target displacement fibers are (2u,2v,0,0,0,0) with v>=0 and |u|+v<=4. Exact-Q recurrence was actually rerun at h=4, obtaining 122 and 132 per formal channel. Correlated genuine BRC path triples may span less than these formal upper bounds.

### Exact obstruction at n=14, the target (-8,0,0,0,0,0)

Only four consecutive e operations (eeee) can cancel prefix displacement -8E1 at horizon four, because e contributes +2E1 and other operations contribute zero or negative E1. Its abstract fiber has 4 joint tags x 3 channel directions = 12 dimensions.

Let p1,p2 count positive E1,E2 steps in an actual 14-step prefix with displacement -8E1. Its signed displacement requires at least 8+2(p1+p2) steps, hence p1+p2<=3. The suffix eeee begins with +E3 and contains no +E2; it cannot create either ordered adjacent pattern A/B internally or across the prefix-to-suffix join. A final tag3 means both A and B were already present in the prefix. Such an ordered prefix must include either the consecutive positive pattern E1,E2,E1 or E2,E1,E2, so p1+p2>=3. Consequently p1+p2=3 and there is no room for any steps on axes E3..E6. Possible positive multiplicities are exactly (p1,p2)=(2,1) or (1,2), yielding genuine positive prefix weight pairs (12,18) or (18,12).

Each e has channel weights (12,27,1), so the suffix eeee contributes fixed weight factors (12^4,27^4,1). At final tag3, each admissible path satisfies the **pathwise exact BRC identity**

    R(eeee,3,count) = R(eeee,3,w0)/622080 + R(eeee,3,w1)/15943230

where 622080=30*12^4 and 15943230=30*27^4, since 12/30+18/30=18/30+12/30=1. It persists under arbitrary additive rational combinations, giving a nonzero row dependence in the 12-dimensional formal fiber and an upper rank of 11. A genuine 11x11 modular minor is **920330 modulo 1000003**, proving rank >=11; exact rational typed-state dynamic programming independently gives rank 11. All 24 other target fibers at n=14 have full-size genuine modular minors. Therefore the two global n=14 ranks are exactly 365 and 395, rather than merely observed lower bounds.

### Full genuine saturation at n=16

At n=16 a genuine 12x12 extreme-target minor has residue **548822 modulo 1000003**. At every other target fiber, prepend the neutral signed-X6 primitive two-step pair (+E3,-E3) to its n=14 full-rank genuine paths. This prefix leaves all six net displacement coordinates and the ordered adjacent A/B progress unchanged, and multiplies the native BRC weighted channels by (3,3) and the count by 1. This invertible diagonal channel action preserves rank. Therefore at n=16 every one of the 25 target fibers is fully spanned, giving 366 and 396 real-path dimensions. Repeat neutral extension for every even n>16. Odd prefix length cannot reach a fully even target signed displacement by parity. If any even n<14 saturated, prepending neutral E3 pairs would imply n=14 saturation, contradicting the strict analytic dependence. Thus **n_sat(4)=16** for both languages. QED.

## Precise executed verification and evidence

The four literal genuine-path JSON certificates (two at n14, two at n16) contain 25 target fibers each, hence 100 fiber minors or exact rank blocks total. Signed six-coordinate native prefix paths, selected complete suffix-word/tag/channel rows and integer minor residues are preserved. Reproduction: decode the UTF-8 payload EC49CT_WITNESS_CERTS.tar.xz.b64 using base64 -d, extract using tar -xJf, and run python EC49CT_RECHECK_INDEPENDENT.py. The stdlib checker has no dependency on the author's prior DP: for every concatenated primitive signed-X6 path it recomputes endpoint, adjacent pair tags, positive BRC product weights and count, and verifies modular determinants for all 100 blocks. The checker actually passed: (n14,exact)=365/366; (n14,cumulative)=395/396; (n16,exact)=366/366; (n16,cumulative)=396/396. The extreme n14 dependent block is checked by an 11x11 nonzero subminor and the pathwise analytic identity above; all other blocks use full nonzero minors. Bundle SHA256: 2ce842c51ae9b0645065e8c6582f11c2aacb8184986af8e156dc8feb1dbebdca.

This is a proof inside the explicitly declared finite signed-native-X6 positive BRC observation model, not a physical propagation theorem, a general h formula for genuine saturation, a signed amplitude-cancellation theorem, a nonlinear-encoder lower bound, or full three-dimensional slice physics.

Native gateway version 0.6.11 returned research_authority_granted=false, executor_binding_configured=false and source_sync.control.state=CODE_REVIEW_REQUIRED. Current Owner inventory returned CONTROL_QUOTA. Hence no native CLAIM, Research Activity registration, formal Result, independent Driver review or admission was established by this portable author publication. No protected-worldview edits.

## Next research unit EC49CU

Test h=5: abstract exact/cumulative formal ranks 537/582, genuine n=16,18 ranks unknown. First prove the positive-letter budget for extreme displacement (-10,0,0,0,0,0), identify any exact BRC/tag row dependence at n=16, then determine all target fibers' earliest full-rank length using exact-Q typed-state DP for upper bounds and genuine literal paths with nonzero integer minors for lower bounds. Do not generalize n_sat(h) from finitely many h.