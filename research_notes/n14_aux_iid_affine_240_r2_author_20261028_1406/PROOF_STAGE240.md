# Stage240: tenth-tie complete finite-face certificate and all-real IID minimax theorem

2026-10-28 · External finite IID only · `PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED`.

## Inputs and exact theorem

N=14, `P=(3,1,20)/24`, `Q=(2,2,20)/24`, arbitrary full ordered-history randomized stopping and P/Q decisions. Define `eP=Pr_P(decide Q)`, `eQ=Pr_Q(decide P)`, `tP=E_P T`, `tQ=E_Q T`, `V14(alpha)=inf_{eP,eQ<=alpha}max(tP,tQ)`. Source Stage239 right endpoint, [immutable prior proof](../n14_aux_iid_affine_236_239_r2_author_20261028_1406/PROOF_STAGE236_239.md), equals

`alpha239=1446305583005/3900793946112`, `V239=10912825831109/1462797729792`.

For **all real** `0<=delta<=4129859375/3900793946112`, including irrational delta, the exact value is

`V14(alpha239+delta) = V239 - (156399672/1321555)*delta`.

The new right endpoint is

`alpha240=362608860595/975198486528`, `V240=2682386241371/365699432448`.

## Universal lower support: no Markov-only restriction

Use rational penalties `lambdaP=75778104/1321555`, `lambdaQ=80621568/1321555`. At count state `s=(n,a,b)`, `Q(h)/P(h)=2^(a+b)/3^a=:r(s)` on **every** specific ordered history h, and define backwards

`B(s)=min{lambdaQ*r(s) [stop P], lambdaP [stop Q], 1+sum_{j=0}^2 P_j B(next_j(s)) [continue, n<14]}`.

Terminal n=14 has only the first two choices. Full-history backward conditional induction proves for every randomized policy, not merely a Markov policy,

`tP+lambdaP eP+lambdaQ eQ >= H = B(0,0,0) = 835979987271629/16283420264448`.

Consequently `V14(alpha)>=H-(lambdaP+lambdaQ)alpha`. The rational sum equals `156399672/1321555`.

## Complete tight policy face; balanced endpoint construction

For every n≤14, all histories at state s have equal likelihood ratio r(s). Conditioning on surviving state s gives identical action conditional distribution under P and Q. Forward induction therefore gives a count-Markovized policy with the same exact four observers `(eP,eQ,tP,tQ)`. This is an observer/future-transition scoped statement, not an X6-native state quotient, and does not assume zero interaction between ancestor-related ties.

The Bellman optimal action set has **exactly ten binary ties**:
`(5,1,0)` P/C; `(6,1,0)` P/C; `(6,1,1)` Q/C; `(7,1,0)`, `(8,1,0)`, `(9,1,0)`, `(10,1,0)`, `(11,1,0)`, `(12,1,0)`, `(13,1,0)` each P/C.
All remaining choices have a **strict positive gap**; 680 count states exhaustively checked, 1,230 positive gaps, smallest `15625/9515196`.

In a finite acyclic MDP, all tight randomized count-occupancy measures form the convex hull of the `2^10=1024` deterministic tie-bit occupancy measures. Full ordered-history tight policies have the same observable four-vectors as this face by the Markovization lemma. Intersect the four-observer convex hull with `eP=eQ`; its extreme points are either balanced corners or intersections of opposite-sign error-difference corners. For corners v,w with `d_v=eP(v)-eQ(v)` and `d_w=eP(w)-eQ(w)` of opposite sign, the unique balancing weight on v is `u=-d_w/(d_v-d_w)`. Exhausting **all** opposite-sign pairs is a finite superset of all hull edges and therefore captures the min and max equal error.

Exact enumeration returned **125,244** balanced vertices, with **79,914** distinct rational errors, and an independent program recomputed them. Every one of the 1,024 corners satisfies `tP>tQ` and `tP+lambdaP*eP+lambdaQ*eQ=H`, so all balanced mixtures satisfy `tP>tQ`. Thus on the balanced face `max(tP,tQ)=tP=H-(lambdaP+lambdaQ)alpha`, exactly attaining the universal lower bound.

Left endpoint witness, tie-bits `1010000000` and `1011111111`, weights `8922452221/232396850000` and `223474397779/232396850000`; equal error alpha239, value V239, strict margin `tP-tQ=1629030615503/2925595459584`.

Right endpoint witness, tie-bits `0000000000` and `0101111111`, weights `1952662899/80656555000` and `78703892101/80656555000`; equal error alpha240, value V240, strict margin `tP-tQ=398392604657/731398864896`.

Both witness weights are in [0,1] and each pair sums exactly to 1. Any real alpha between endpoints is realized by root-mixing these two balanced tight policies with the real interpolation weight. Thus the entire claimed all-real interval follows. Beyond alpha240 the same fixed support cannot be exact, since no balanced tight-face policy has larger common error (finite-polytope upper endpoint). This does not rule out a new support to the right.

## Exact computational evidence

`PORTABLE_REPRO_STAGE240.py`: Fraction Bellman suffix DP checks 680 states, enumerates all 1,024 deterministic tight policies, and cross-checks each **four-observer** vector against an independent full ordered-history DFS with separate positive integer P/Q branch masses; the DFS total is **864,238 visited nodes**. It writes `PORTABLE_EXACT_CERT_STAGE240.json` containing all four-vectors, P/Q path visit counts, exact balanced intersection certificate and endpoint weights. Observed stdout: `STAGE240_PORTABLE_EXACT_PASS 864238`.

`INDEPENDENT_CERT_AUDIT_240.py`: actually executed separately, not importing the generator. It recomputes exact Bellman costs, ties, all positive gaps, 1,024 dual/contact/time checks, 125,244 balanced face intersections, exact witness reconstruction, and Stage239 continuity, returning `STAGE240_INDEPENDENT_AUDIT_PASS 864238`. Full generated certificate is reproducible by the GitHub program; its complete author-side 210KB JSON is retained in the attached portable research archive, **not falsely claimed to be one of this Git text commit's files**.

The earlier Stage240 *dual-only* packet has now been discharged by this Stage240 author-side primal theorem. The next Stage241 dual-only scan is a separate candidate, not a proved primal interval. See `NEXT_TASK_PACKET_241.md`.

**Provenance/boundaries:** Global current read pin `main@4faffbe68584637f37d630e345543a8f7300f394`, EM current control `main@f01fb212f8d640ebced88b2dc836b52f4d933596`, P000 protected blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. BRC-compatible positive P/Q branch mass composition was used at the auxiliary model's exact observer level; no heartbeat-native BRC Shor calculation was claimed. No native-X6 embedding, original project physical correspondence, Lean proof, native CLAIM/Source Result, authoritative owner confirmation, or independent Driver mathematical admission. The native service stated `research_authority_granted=false` and owner query returned `CONTROL_QUOTA`.
