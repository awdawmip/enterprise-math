# X6 R150 — complete six-candidate support for strict 3/2-near Port-10 directions

2026-11-23 (Asia/Shanghai). Author analytic + exhaustive finite-integer certificate PASS; independent mathematical review NOT_REVIEWED.

## Frozen input and exact setting

Continue R149 @5a7807ac6dc8fa309049aeadf6514bf20f587d37:research_notes/portable_direct/2026-11-23_r2_x6_r149_global_pareto_and_bridge_six_witness_reduction.md. Preserve frozen R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@0687aa24f5402da3b35f914dd6907967a9805b94. This is the conditional **static three-axis six-pair BRC observer** within native X6/P000 research, not a native time-evolution or physical-residual inference.

Retain all 1,935 unoriented Port-10 integer triples (nonzero multiples distinct) and the R149 six gaps g(a). For B,D>0 take capacities s=(136+B,312,136+D,B+176,B+D,176+D), F=max_j g_j(a)/s_j, eta=min_a F, and strict-near set N={a:F(a)<(3/2)eta}.

## Exact complete near-set theorem

For **every real B>=20 and D>=528**, define
W6={(1,0,0),(4,-1,0),(5,-4,1),(5,-1,0),(6,-4,1),(9,-5,1)} / ±.

Then BOTH the optimizer value and the **complete** strict 3/2-near set obey the finite exact formulae

eta(B,D) = min {F(w;B,D): w in W6},
N(B,D) = {w in W6: F(w;B,D)<(3/2)eta(B,D)}.

All six gap vectors and the exact finite optimizer formula are given in R149. These formulae cover the previously incomplete 20<B<136,528<=D<1872-B real-parameter region as well. Equality is excluded by strictness. A fully simplified chamber-by-chamber atlas is an optional subsequent refinement; membership itself is decided exactly here.

## Proof

(1) R149's 1,935-vector certificate has 1,890 vectors with fixed second gap g1>=6, so F>=6/312=1/52; its witness (1,0,0) yields eta<=3/274 on the entire quadrant. Hence F>=1/52>(3/2)(3/274)>=(3/2)eta, eliminating every high-gap vector from N.

(2) Exactly 45 vectors have g1<=3. Six are W6. Of the remaining 39, the exact integer checker shows that **35** have an element w in W6 with g_j(a)>=(3/2)g_j(w) for every j. Their scores therefore satisfy F(a)>=(3/2)F(w)>=(3/2)eta for ALL positive capacities. With lexicographically first witness, assignment counts are (4,-1,0):23 and (6,-4,1):12. Only four explicit exceptional vectors remain:

u=(1,-3,1) with g=(2,3,16,1,18,19);
r=(3,-1,0) with g=(0,3,18,3,18,15);
t=(7,-4,1) with g=(1,3,19,2,18,16);
v=(9,-2,0) with g=(3,3,15,0,18,18).

(3) For 20<=B<=136, c=(6,-4,1) satisfies F(c)=12/(B+D). All four exceptions have fifth gap g4=18, hence F>=18/(B+D)=(3/2)F(c)>=(3/2)eta.

(4) For B>=136, F(c)=12/(D+136) and F((9,-5,1))=1/104, so eta<=min(F(c),1/104). For r,t, the third gap is >=18, giving F>=(3/2)F(c). For u with D>=584, its sixth gap gives F(u)>=19/(D+176)>=18/(D+136)=(3/2)F(c). For u with 528<=D<=584, its third gap gives F(u)>=16/(D+136)>=16/720>(3/2)/104>=(3/2)eta.

(5) For B>=136, the exact b=(4,-1,0) score is F(b)=max(1/(B+136),11/(D+136),12/(B+D)). The vector v has first, sixth, fifth gaps giving 3/(B+136),18/(D+176),18/(B+D). These are respectively >=(3/2) times the three components of F(b), since the middle inequality requires only D>=304, satisfied by D>=528. Hence F(v)>=(3/2)F(b)>=(3/2)eta. Every outsider is excluded.

The six directions remaining in W6 are then tested by their actual scores against the original strict threshold; this proves exact set equality and does not discard possible ties at the optimizing level.

## Reproduction and next question

Companion standard-library Fraction checker: research_notes/portable_direct/x6_r150_near_six_support_verify.py (imports R149 checker from same folder). Author's local run on 2026-11-23:

R150 FULL STRICT-NEAR SIX-SUPPORT CERTIFICATE PASS
population 1935 high-gap 1890 low-gap 45 scaled-dominance 35 exceptions [(1, -3, 1), (3, -1, 0), (7, -4, 1), (9, -2, 0)]
scaled-dominance assignment [((4, -1, 0), 23), ((6, -4, 1), 12)]
exact_fraction_full_population_crosschecks 99

The parameter crosschecks are exact but the continuum assertion relies on the full integer certificate and displayed analytic inequalities, not sampling extrapolation.

Next: simplify the exact W6 membership equations to an irredundant boundary atlas on 20<B<136,528<=D<1872-B. The frozen inputs, P000 and author/independent-review distinctions are unchanged. Formal CLAIM/Result/Review not implied by this independent Source publication.
