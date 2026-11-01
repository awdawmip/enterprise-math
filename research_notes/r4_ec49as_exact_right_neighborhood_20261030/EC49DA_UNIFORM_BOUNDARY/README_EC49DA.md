# EC49DA — uniform all-h boundary-fiber saturation for signed-X6 positive BRC

Date: 2026-11-01 (Asia/Shanghai). **AUTHOR_ANALYTIC_PROOF / PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED**.

## Frozen sources, exact observer

Global canonical `main@ba9440e1981ad1bd8092bb02224f83b0f338f07e`; Enterprise Math canonical `main@ce7279d4cafc8d7ddb4a65d75c33e8c40849428c`; predecessor PR #1730 `6ba15e0235eaf75ba3f73568c51b9adb7066b54e` (EC49CZ). Read global startup/manual, current P000, ACTIVE worldview, native X6, joint-observer, native positive BRC constraint and portable research protocol. Neither protected foundation nor worldview was changed.

Input prefixes are **ordered words on the twelve signed primitive X6 axis directions**, with all six endpoint coordinates retained. A chart zero is a chosen Cell, not a global origin. Time is independently typed and not used in this static combinatorial theorem. Ordered adjacent tags are A=(+E1,+E2), B=(+E2,+E1); final tags 0=neither, 1=B only, 2=A only, 3=both. The predecessor's full nine-state DFA retains possible half-matches for future operations; the constructions here evaluate the *literal concatenated words*, not a lossy four-tag state transition.

Two exact positive BRC branch product channels have positive-step weights W0=(2,3,3,2,1,1), W1=(3,2,3,2,1,1), and all negative-step weights 1. A separate count channel is 1. Future operations are a=(-E1,-E1), b=(-E2,-E2), c=(+E1,+E2,-E1,-E2), d=(+E2,+E1,-E2,-E1), e=(+E3,+E1,+E1,-E3). The observer records for every positive-depth <=h suffix returning to the same chosen relative Cell the four final A/B tags and all three exact additive channels. The theorem concerns this finite observer, not signed amplitudes or physical propagation.

## Theorem — every extremal displacement fiber is saturated for every h

For each integer **h>=1**, put

[
B_h=\{(2s,2v,0,0,0,0): s,v\in\mathbb Z,\ v\ge0,\ |s|+v=h\}.
]

There are exactly 2h+1 such endpoint fibers. For **every** D in B_h, the Q-rank of the exact-depth-h **and** cumulative-depth-(1..h) observer on length n=2h+8 native ordered signed-X6 prefixes with endpoint D is **12**. The positive mixed edge s>0,v>0 reuses the explicit EC49CZ all-h theorem; the new independent proofs below cover **the entire s<=0 edge** and the positive E1 corner (s=h,v=0). All h are quantified analytically; no induction from finite observed windows is used.

### 1. Negative edge: upper bound

Write D=(-2u,2v,0,0,0,0), u,v>=0, u+v=h. A return suffix needs displacement (+2u,-2v). Only operation b changes net E2, by -2, hence exactly v copies of b occur. Only e has +2 E1 displacement; the remaining u operations must all be e. Thus **all** returning complete suffixes are permutations of exactly u e's and v b's, and no positive-depth shorter suffix returns.

The operation e contains positive E3,E1,E1 and b contains only negative E2; neither has positive E2. Every such suffix begins either +E3 or -E2, so it cannot create the adjacent A/B pair at the prefix boundary or internally. The final four tags are precisely the prefix tags; each future word multiplies the two positive BRC prefix weights by (12^u,27^u), with count weight 1. All observation rows therefore lie in the four-tag × three-channel span, of rank at most 12.

For the positive E1 corner D=(2h,0,0,0,0,0), the only returning suffix is a^h, containing negative E1 only and weight (1,1,1); the same upper bound holds. On the positive mixed edge EC49CZ established the analogous a^u b^v-only negative suffix classification.

### 2. Negative edge: 12 literal paths with a uniform nonzero determinant

For each of the four tags take **three** positive four-letter gadgets g, where '1','2','3' stand for +E1,+E2,+E3. Let -g be the four negative axis steps in the same order, with **no** cancellation of path provenance. Set

[
P_{u,v,g}=(-E_1)^{2u}\Vert g\Vert(-g)\Vert(+E_2)^{2v}.
]

These are 12 genuine words of length 2h+8 and endpoint D. A/B pairs occur only inside g, since all transitions into and out of g pass a negative step.

| final tag | gadget 1 | gadget 2 | gadget 3 | exact 3x3 column determinant |
|---|---|---|---|---:|
| neither (0) | 1111 | 3111 | 2311 | -216 |
| B only (1) | 3211 | 2111 | 3221 | +216 |
| A only (2) | 1112 | 1122 | 3112 | +216 |
| both (3) | 1211 | 2121 | 3121 | +216 |

The 3x3 matrix columns are precisely (W0(g),W1(g),1)^T. For tag0 these columns are (16,81,1), (24,81,1), (36,54,1), and their determinant is -216; the other three determinants are +216, by exact integer arithmetic.

For any matching suffix, each column in each tag block is transformed by the same diagonal matrix diag(F0,F1,1), with F0=3^(2v)12^u and F1=2^(2v)27^u. Organizing 12 output rows by (tag,channel) and 12 prefixes by (tag,gadget) yields a block-diagonal 12x12 integer observer minor with exact determinant

[
\Delta_-(u,v)=-(216^4)(F_0F_1)^4
             =-(216^4)(6^{2v}324^u)^4\ne0.
]

Consequently **all h+1 negative-edge fibers have rank exactly 12 for every h>=1**, including the formerly finite-only D=(-2h,0) extreme fiber.

### 3. Positive E1 corner

Use the same twelve gadgets and
[
Q_{h,g}=g\Vert(-g)\Vert(+E_1)^{2h}.
]
The unique return suffix a^h creates no new A/B adjacency. The common positive BRC channel factors are (2^(2h),3^(2h),1), giving the 12x12 exact determinant

[
\Delta_+(h,0)=-(216^4)6^{8h}\ne0.
]

### 4. Closing the whole boundary, and the remaining interior

The EC49CZ author-side construction proves the positive mixed edge D=(2u,2v) for u,v>=1 and u+v=h by using four tag-controlled positive runs and three tag-safe neutral-pair weight variants. Each 3x3 channel determinant is XY/9 != 0; the EC49CZ source includes the exact path template. Combining that lemma with Steps 2–3 covers both sloping extremal edges B_h. The upper bound in Step 1 proves **equality** of all 2h+1 boundary ranks to 12.

The actual native geometry remains full signed six-axis X6. Only the constructed *endpoints* happen to have zero last four coordinates; neither a 2D native plane nor a three-dimensional physical slice is inferred.

## Validation and reproducibility

File `VERIFY_EC49DA_GITHUB.py` is an independently executable Python 3 standard-library literal-path checker. It constructs all 2h+1 boundary fibers for **every h=1..30**, computes real endpoints, ordered final tags and two exact native positive BRC channel products, then validates **960 nonzero 12x12 integer minors modulo 1,000,003**. It also exhaustively iterates **6,120 literal prefix/suffix pairs** across every e/b ordering on the negative edge for h<=8 to verify suffix-invariant tags and weight factors.

Actual output:

```json
{"all_suffix_permutation_path_checks_h_le_8":6120,"boundary_fibers":960,"h_range":"1..30","max_mod":999947,"min_mod":945,"nonzero_12x12_mod_1000003":960,"status":"PASS"}
```

An additional author-side full checker `VERIFY_EC49DA_ALL_BOUNDARY.py` was run locally and returned PASS for the same 960 boundary fibers. The earlier native kernel `native_signed_brc.py` from the EC49CZ evidence archive was crosschecked against literal branch summation of all 1, 12, 144, 1,728 and 20,736 signed-X6 words of lengths 0..4 respectively; all exact channel sums matched `endpoint_weight`. The *universal theorem* is supplied by the explicit exact determinants above; the finite checkers cover their stated finite input families only.

## Authority and next problem (EC49DB)

The native Sites gateway returned `research_authority_granted=false`; this run's `em_control_tasks` returned `CONTROL_QUOTA`, leaving active owner/claim unverified. This publication is `PORTABLE_DRAFT / REGISTER_PENDING / UNREVIEWED / NOT_ADMITTED`, **not** a source-native CLAIM, activity registration, Result, Driver review or Working Truth.

**EC49DB:** For every h>=4 and every interior endpoint D=(2s,2v,0^4) with |s|+v<h, construct a uniform **18-column** native-path minor at length 2h+8 or a counterexample. The inherited full nine-state A/B automaton has six independent observer rows in each interior fiber; three BRC channels per row require 18, not merely four final tags ×3. Produce six explicit path-history residual classes and three channel-independent witnesses per class, with an exact nonzero determinant. Do not conflate 4 final tags with the six internal future-distinguishable states.

References: prior EC49CZ signed-X6 positive-boundary proof and independently replayable h=12 certificate at PR #1730 head `6ba15e0235eaf75ba3f73568c51b9adb7066b54e`; `docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` and `research_constraints/heartbeat_brc_only.json` at Enterprise Math main; P000 and ACTIVE worldview are unchanged.