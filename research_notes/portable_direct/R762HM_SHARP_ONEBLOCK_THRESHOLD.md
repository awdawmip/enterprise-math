# R762HM — Sharp 14-event threshold for one-block signed Port repair

Status: **AUTHOR-PROVED (finite-exhaustive certificate and symbolic reduction) / EXACT INTEGER CHECK / NOT_REVIEWED**. Scientific scope: composite signed Port candidate, **not** admitted primitive TRIADIC_CLOSURE_E.

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS; immutable publication TP2-8B7E13C5904A2D6F1142. Historical original researcher EM-X6-3050F6, own Task session MCP-4b2d70a97f594366a7c94a0f8b45df38. Frozen scientific input: enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000, signed X6 torsor, triadic balance and joint preservation). Reused author results: R762HG@f19346110bdca4c9aa237ed766fedc612210293c (complete half-path parity/signability census through 12), R762HJ@2cc5ef6fb10f1d30d70738e9b6ddb9c563e3aa23 (one-block prefix criterion), R762HK@0778045cdbe977bf86e1d3f7557162e1ed6b33d8 (14-event obstruction), R762HL@93f9d22b00d463537f3bb38af5ea697db8ddbe76 (seam invariance).

## Exact problem

Fix X={0,1,2,3,4,5}, the 15 two-axis named Ports, and initial Port P*={0,1}. A Port step P→Q is admissible when |P∩Q|=1, with labeled three-axis support S=P∪Q and h_S=sum_{i∈S} e_i in Z^6. These are **composite candidate updates**, not primitive one-axis steps and not native-force permission. A closed unsigned history of length m has P_m=P_0=P*. Its parity residual is xor_t S_t, and its signed zero-Cell completions are epsilon_t∈{+1,-1} satisfying sum_t epsilon_t h_(S_t)=0.

For even m define alpha_t=(-1)^t and alternating residual V=sum_t alpha_t h_(S_t). A signing formed by reversing the alternating signs on at most one nonempty contiguous linear interval [a,b) is a one-block repair. Zero-block repair means the original alternating signing already closes. All counts retain distinct ordered named Port histories and positive source multiplicity; no signed mass cancellation is used to count BRC sources.

## HM1. Sharp finite threshold

**Theorem.** Every parity-even closed named Port history of positive length m≤12 admits a zero-Cell signing requiring at most one contiguous flip-block relative to alternating signs. For each m∈{2,4,6,8,10,12}, the minimum flip-block count is zero exactly when V=0, and one otherwise. No positive odd m is parity-even: the sum of all six support incidences is 3m, which is odd for odd m.

Conversely, the previously published 14-event closed Port witness in R762HK is parity-even and admits exactly 104 signed zero-Cell completions, but its minimum linear and cyclic flip-block count is two. Therefore **14 is the first possible event length at which the parity-even closed-Port one-block sufficiency property fails**, with the same threshold for the cycle-seam-independent minimum by R762HL.

This is a **finite theorem about the candidate event language** and does not assert all-length parity sufficiency or P000-native triadic permission.

## Algebraic reduction and exhaustive proof certificate

Let W_0=0 and W_j=sum_{t<j} alpha_t h_(S_t). A single interval flip changes signed displacement from V to V-2(W_b-W_a). Thus one-block repair exists iff some 0≤a<b≤m obeys

    2(W_b-W_a)=V.

Zero-block repair is equivalent to V=0. The condition can be tested with exact integer prefix sums; the independent verifier uses a six-integer coordinate-by-coordinate test.

For m=2n≤12, split a closed Port walk into two length-n halves. Reverse the second half. The resulting ordered pair (u,v) consists of two independent length-n walks beginning at P*, ending at exactly the same intermediate Port p. Their six-bit xor support masks must coincide for parity-even return. Conversely every ordered pair in the same (p,parity-mask) bucket yields precisely one parity-even closed Port history, and all such histories arise uniquely this way. For each n all 8^n half histories are enumerated with all 15 named Port endpoints, all 64 xor masks, and all 8 transitions per Port. For every ordered same-bucket pair, rebuild the 2n supports and test the exact prefix criterion. The complete enumerator has **zero failing pairs**, and verifies the independently established H_(2n) bucket-square counts.

| n | m | Half histories 8^n | Parity-even closed histories H_m | Zero-block minimum | Exactly one-block minimum | Prefix test failures |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 8 | 8 | 8 | 0 | 0 |
| 2 | 4 | 64 | 168 | 168 | 0 | 0 |
| 3 | 6 | 512 | 4,960 | 4,960 | 0 | 0 |
| 4 | 8 | 4,096 | 177,536 | 176,264 | 1,272 | 0 |
| 5 | 10 | 32,768 | 7,289,184 | **6,978,624** | **310,560** | **0** |
| 6 | 12 | 262,144 | 333,869,824 | **295,483,696** | **38,386,128** | **0** |

The m=8 zero-block count matches R762HJ's independently reported alternating-sign count of 176,264. m=10/12 zero/one minimum distributions are new exact author-side results.

The source program R762HM_CHECK.cpp uses six byte-separated integer lanes for the bounded exact prefix values (each coordinate lies between -12 and +12, stored with byte bias 64; there is no inter-lane carry or floating-point arithmetic), exhausts all same-bucket ordered pairs, and independently checks the positive-existence/zero result using six ordinary signed integer coordinates for deterministic actual-path samples. Samples: m=2,4,6,8,10,12 respectively 8,32,32,34,143,5126; independent comparisons passed. Its outputs are captured in R762HM_EVIDENCE.json. The author executed with g++ -O3 -std=c++17 -Wall -Wextra -pedantic; all six exhaustive passes ended PASS, including 333,869,824 parity-even named histories at m=12.

These finite exact computations are author-side verification with reproducible complete traversal, not an independent review or a formal prover certificate. Earlier R762HK is reused at its existing verified scope; there is no need to redo its 16,384-word signing check.

## Interpretation and next question

For all parity-even named closed Port candidate histories through 12 events, the full six-axis signed Cell return can be repaired with an alternating signing and at most one contiguous reversal. At 14 events, that statement fails even though the witness remains signable; a two-block obstruction is **not** an unsignable path.

Next scientific directions: determine the all-length parity-even signability criterion using the exact half-path set-intersection/factor test; establish growth or bounds for the minimum cyclic flip-block number beyond 14; and separately construct actual P000-native TRIADIC_CLOSURE_E primitive-force incidence and its Cell, Link, Port, time and rotation permissions. Preserve P000's six native spatial axes, independent time, three-force minimal stable arity, 120-degree PERP_E, and ordered positive BRC source/provenance. The current candidate Port transition permission may be narrowed when native legality becomes available.

## Reproduction and provenance

    g++ -O3 -std=c++17 -Wall -Wextra -pedantic R762HM_CHECK.cpp -o r762hm
    ./r762hm

Companion files: R762HM_CHECK.cpp; R762HM_EVIDENCE.json. Scientific result status: NOT_REVIEWED. No claimed Result, Review, Foundation or native physics promotion.