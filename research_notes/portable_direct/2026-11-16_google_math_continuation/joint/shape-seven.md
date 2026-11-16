# Removing translation and unknown gain from seven samples

For a window of n consecutive source observations, set k=n−4; k≥1 fourth differences are available. Let G=(20,20,20,−100,140,−100), and Sₐᵏ=(Gₐ,...,Gₐ₊ₖ₋₁) cyclically. The ideal transformed readout has the form z=A Sₐᵏ+B·1 with arbitrary translation B and unknown nonzero constant gain A. This applies in particular to the joint frozen count-error model with E=25920e/r⁶, D=4320d/r⁵ and A=(1+E)/(1+D)². Uniformly for |E|≤L, |D|≤δ<1, and every fixed k, its output is z+O(1/r) coordinatewise.

## How many samples?

For n=7 the six signatures, and their two-component shape keys, are

| phase | Sₐ³ | positive-gain key (subtract first entry and divide by positive gcd, omit initial zero) |
|---:|---|---|
| 0 | (20,20,20) | (0,0) |
| 1 | (20,20,−100) | (0,−1) |
| 2 | (20,−100,140) | (−1,1) |
| 3 | (−100,140,−100) | (1,0) |
| 4 | (140,−100,20) | (−2,−1) |
| 5 | (−100,20,20) | (1,1) |

For arbitrary real observations the same keys mean projective directions: subtract the first value and test positive proportionality to the listed rays (or arbitrary nonzero proportionality if the sign is unknown). Equality of all three coordinates identifies phase 0 exactly in the ideal model. No two of the nonzero keys are opposite or collinear, so identification works even when the sign of A is unknown. With a known positive sign the ordering including equalities alone distinguishes these six triples, e.g. phase 2 has second < first < third, phase 4 has second < third < first. An implementation should not impose exact equality on noisy data.

At n=6, with only two differences, all constant pairs are equivalent under translation (phases 0 and 1), all descending pairs are equivalent with a positive gain (phases 2 and 4) and so are all ascending pairs (phases 3 and 5). n=5 gives only one entry, erased by translation. Thus seven is minimal among consecutive fourth-difference windows for identifying every phase under a positive or a signed, nonzero gain. Eight samples make every ideal signature nonconstant, allowing a continuous direction comparison for every phase.

## Sharp uniform noise tolerance

Suppose candidate gains obey A≥g>0 (positive model) or |A|≥g (sign unknown) and B is unrestricted. Define the shape set for each phase as all A Sₐᵏ+B·1 with these constraints. Use nearest shape set in the infinity norm. For one candidate and one gain, the optimal translation is the midpoint of the largest and smallest coordinates of y−A Sₐᵏ, so its distance is half the range. For phase 0's constant triple, this is exactly (max y−min y)/2. Minimizing over the gain ranges is a one-variable convex piecewise-linear optimization, applied to each sign if needed. All minima exist (for nonconstant templates the objective grows at infinity). The known gain floor forbids arbitrarily small nonzero gains from fitting nearly constant phase-0 data.

The minimum separation of two different phase sets in units g is

| observations n | n≤6 (when n≥5) | 7 | all n≥8 |
|---|---:|---:|---:|
| A≥g | 0 | 60 | 120 |
| abs(A)≥g | 0 | 60 | 60 |

Consequently ε strictly less than half the corresponding separation gives unique decoding for every coordinatewise additive error with maximum absolute value ≤ε. At equality, the midpoint of two closest attainable signals demonstrates ambiguity for every decoder. For n=7,g=1, for instance, (20,20,20) from phase 0 and (80,80,−40) from phase 1 with B=60 give the common noisy reading (50,50,−10) at ε=30. For n≥8, phase 0 and phase 2 with equal positive unit gains give distance 120 on a full period; phase 0 and phase 1 with gains +1 and −1, translation −20 on the second, give distance 60. Their periodic extensions give the same upper bounds at arbitrary window lengths.

**Exact lower bound certificate.** By homogeneity normalize g=1. For each pair of templates U,V, one may anchor one of their absolute gains to 1: divide both gains and their optimizing shifts by the smaller gain if it exceeds 1, decreasing any positive difference. For each ordering and relative sign σ, it remains to minimize range(U−σt V)/2 over t≥1. The range is the maximum of finitely many affine functions

    Uᵢ−Uⱼ+σt(Vⱼ−Vᵢ).

Its minimum is achieved either at t=1 or the intersection of two distinct slopes with t≥1 (a constant segment has such an endpoint, or includes 1). shape-lp.py explicitly evaluates all such rational candidates for all 15 phase pairs, signs and orderings. For k=3 the minimum is 60 with either sign convention. For k=4 it is 120 with positive gain and 60 with unrestricted sign. Dropping coordinates cannot increase the distance between any two fixed signals, so the minima do not decrease with k. The periodic witnesses above show the values already achieved at k=4 remain sharp.

With no gain floor, ideal identification still holds for all nonzero gains, but no strictly positive error radius works uniformly: as A→0 every shape tends to the same constant signal. At A=0 every phase is exactly identical in the limiting model whatever the number of samples.

## Application to source uncertainty

If |D|≤δ<1, |E|≤L, and |1+E|≥η>0, the gain magnitude is ≥g=η/(1+δ)². If 1+E≥η use the positive guarantee. If both signs occur use the two-sided guarantee. Since the joint expansion has O(1/r) remainder uniformly on the compact set, every sufficiently large r in this domain is decoded correctly. In particular for denominator noise alone E=0, all six phases remain identifiable on EVERY compact |D|≤δ<1, including well past the fixed-template negative error threshold δ*=0.18776…. With bounded symmetric raw budgets |e|≤M and |d|≤K the sufficient conditions r⁶≥25920M/(1−η), r⁵≥4320K/δ imply this positive-gain guarantee when 0<η<1. These implications establish neither a specific finite cutoff nor necessity in the original nonlinear count model. At E=−1 the limiting gain is zero and all limiting shapes coincide. The O(1/r) remainder can still contain phase information, and D approaching −1 requires a separate positive-denominator analysis.

With output error specified on the three/four differences, the sharp radii above require no distributional assumptions. If instead per-position errors ≤u are imposed independently on the raw input observations, the crude propagating inequality is ||Δ⁴noise||∞≤16u. Combining this with the proved radii gives sufficient raw bounds u<15g/8 at seven positions, u<15g/4 at eight positions with positive gain. These raw constants are not asserted sharp because adjacent differences share the original source errors.

Scope: finite six-phase signatures, stated error family, author-side derivation. The shape classification uses labeled sampling order.
