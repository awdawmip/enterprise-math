# Stage334-B — five strict low-error BRC public-sign chambers cannot be Pareto optimal

Date: 2026-10-31. Classification: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a fully labelled auxiliary three-visit two-source Bernoulli observer, **not** P000-native X6 physics.

## Source / scope
Frozen GLOBAL_KNOWLEDGE_V1 main@977d83eec352915a0e945218ed279f29f2fc2133, project main@a2f0a44c2a7e0b345e0aadc72c90f0b5866bcf24, Stage332-B immutable scientific predecessor 839f7912cbcd788c5a38b57d812172d8113c4920 (Draft PR #1736). Original project P000 V5 was read; this auxiliary model has no demonstrated lossless X6, time, 3D slice or final Cell bridge. Native owner enumeration returned CONTROL_QUOTA and research authority is not granted; GitHub storage is not a CLAIM/Result/independent review.

## Exact model
For k=0,1,2,3 let B_k(z)=z^k(1-z)^(3-k), multiplicities w=(1,3,3,1), target m=(61,21,9,9).
Let r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160, and
b(x,y)=(5/32) sum_k w_k |r_k(x,y)|.
Retain all four binomial words and source tags. Let D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|, and
c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256.
The inherited two-source objectives are P=b(q1)+b(q2), T=33/1024+c(q1)+c(q2). Exact branch conservation: sum_k w_k B_k(z)=1, sum_k w_k m_k=160, hence sum_k w_k r_k=0.

Conditionally reuse the precise **author-proved but not independently admitted** upstream implications: b<=61/10000 implies R=[21/100,6/25] x [1/2,2/3] (Stage332); r2>0 (Stage330); the only six strict public signs (sgn r0,sgn r1,sgn r3) in the low-error set are ++-, +-+, +--, ---, --+, -+- (Stage331); fifteen source-tag comparisons are strictly fixed on R, and the only tagged switch is y_d=(1+sqrt(13))/8 (Stage332).

## Theorem: five-chamber strict simultaneous domination
At **every** point q=(x,y) with b(q)<=61/10000, with all of r0,r1,r3 nonzero and sign word in {++-,+-+,+--,---,--+}, there exist arbitrarily close valid q' in [0,1]^2 such that **b(q')<b(q) and c(q')<c(q)**. Consequently no exact global two-source Pareto optimizer in a window where the Stage332 per-source low-error envelope applies may use one of these five strict words. The only strict word left by this result is -+-; all public-zero boundaries remain possible.

**Proof.** For strict public word sigma=(e0,e1,e3), set e2=+1 and Q_sigma(z)=sum_k w_k e_k B'_k(z). Differentiation, retaining binomial multiplicities, gives b_x=Q_sigma(x)/8 and b_y=Q_sigma(y)/32. Exact polynomial expansions:

| sigma | Q_sigma(z) | direction decreasing b |
|---|---|---|
| ++- | -6z^2 | increase x |
| +-+ | -6(1-z)(1-3z) | increase x |
| +-- | -6(2z-1)^2 | increase x |
| --- | 6z(2-3z) | decrease y |
| --+ | 12z(1-z) | decrease y |
| -+- | 6(1-2z) | not excluded |

At x in [21/100,6/25] all first three Q(x) are **strictly negative**, so increasing x strictly decreases b. At y in [1/2,2/3] the Q(y) for --- and --+ are positive except Q_---(2/3)=0; Q_--- is positive at all points immediately below that endpoint, so decreasing y still strictly decreases b.

The full 16-term tagged absolute-value derivative, with the 15 strict invariant signs, simplifies to c_x=-(1-x)(189-183x)/256<0, and:
for y<y_d, c_y=3y(1-y)/64>0;
for y>y_d, c_y=3y(18-25y)/256>0.
Both one-sided derivatives at the unique cusp are positive, and c is continuous there. Since 2/3<18/25, c strictly decreases with x and increases with y throughout R, including passage across the cusp. Hence **the same coordinate change** strictly reduces c. Strict residual/tag signs are locally stable; the cusp has the established one-sided slope. R is an enclosure, not a hard wall: all its points lie inside the physical parameter square, so the small coordinate steps remain admissible even from an R endpoint. The two strict inequalities hold simultaneously. For the additive two-source objective, replace just that source to lower both P and T; a Pareto optimizer cannot permit this. QED.

As an extra direct check in --- the mass identity yields b=(3/16)[4B_2(x)+B_2(y)-9/32], strictly increasing in y up to y=2/3 even though its derivative vanishes exactly at the endpoint.

## Exact rational witnesses
The executed Python Fraction verification at the original absolute-value definitions checked five representative exact improvements (the universal proof is **not** inferred from this finite set):

| sign | q=(x,y) | q' | b(q)-b(q') | c(q)-c(q') |
|---|---|---|---|---|
| ++- | (221/1000,13/25) | (2211/10000,13/25) | 14658931/4000000000000 | 11571134791/256000000000000 |
| +-+ | (11/50,621/1000) | (2201/10000,621/1000) | 79519803/4000000000000 | 11600262661/256000000000000 |
| +-- | (11/50,597/1000) | (2201/10000,597/1000) | 23511601/1000000000000 | 11600262661/256000000000000 |
| --- | (23/100,57/100) | (23/100,5699/10000) | 49611297/16000000000000 | 73532099/64000000000000 |
| --+ | (57/250,5/8) | (57/250,6249/10000) | 70316249/8000000000000 | 17820449/10240000000000 |

The exact checker compares all six public derivative polynomials, three full signed tagged derivative polynomials, four-binomial conservation, and five rational witness/budget inequalities; two executions produced byte-identical output ending STAGE334B_FIVE_CHAMBER_STRICT_PARETO_DOMINANCE_EXACT_PASS. Stage330/331/332 global enclosures were *not* reexecuted in this checkpoint. No independent Lean/Driver acceptance.

## Next Stage335-B
Classify r0=0, r1=0, r3=0 boundaries with correct nonsmooth b subgradients, beginning with the r1=0 branch adjacent to --- and -+-; handle their pairwise intersections and the y_d tag cusp. Then apply exact polynomial KKT and boundary one-sided inequalities in surviving -+- to test the genuine first global Pareto allocation transition. The native P000 X6/three-dimensional slice/triadic closure/time/Cell mapping remain separate obligations.
