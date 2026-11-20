# Stage330-B — Global exclusion of the public r₂≤0 chamber in the 3-visit BRC model

Date: 2026-10-31. Status: PORTABLE_AUTHOR_LEMMA / EXACT_INTEGER_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Immutable inputs and exact observer

GLOBAL_KNOWLEDGE_V1 canonical main `a5ce32dac233e1f9b61031f26acc58e391849a57`; Enterprise Math canonical main `6efa6699766c16e524ae429ca3f78b043b928750`; Stage329-B scientific predecessor `f8b73b74eb2baed74f39df71a23055623286a707`. P000 startup projection matches original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`. ACTIVE worldview and portable research protocol were read. This lemma concerns the auxiliary Bernoulli BRC observer, not native X6 dynamics or its 3D slice / time / final Cell address.

For `k=0,1,2,3`, let

```text
B_k(z) = z^k (1-z)^(3-k)
r_k(x,y) = (4/5) B_k(x) + (1/5) B_k(y) - m_k/160
m=(61,21,9,9); w=(1,3,3,1)
b(x,y) = (5/32) sum_{k=0}^3 w_k |r_k(x,y)|
(x,y) in [0,1]^2.
```

All binomial multiplicities and all four public residuals are retained.

## Theorem A — complete real-domain public-sign exclusion

**For every real x,y∈[0,1], b(x,y)≤61/10000 implies r₂(x,y)>0.** This is over the full Bernoulli parameter square; neither the inherited `r₁=0` branch nor any tagged-sign chamber is assumed.

### Finite exact proof certificate

Set `D=65536`, `D3=D**3`, `Q_k(n)=27*n**k*(D-n)**(3-k)`; hence `Q_k(n)=27*D3*B_k(n/D)`. On any dyadic interval `[a,b]/D` the exact minimum of `Q_k` occurs at one of its endpoints. Its maximum is likewise an endpoint unless `k=1` and the interval contains 1/3 or `k=2` and it contains 2/3; at either critical maximum the exact value is `4*D3`. This follows by differentiating `B_k`: `B_0` decreases, `B_3` increases, `B_1,B_2` are unimodal with the stated maxima.

For any closed rectangle `[a,b]/D × [c,d]/D`, write `Xlo_k,Xhi_k` and `Ylo_k,Yhi_k` for these exact interval extrema. Define the integers

```text
L_k = 32*(4*Xlo_k + Ylo_k) - 27*m_k*D3
U_k = 32*(4*Xhi_k + Yhi_k) - 27*m_k*D3.
```

Every point of the rectangle has `L_k/(160*27*D3) ≤ r_k ≤ U_k/(160*27*D3)`. For each `k`, define the integer distance of zero from `[L_k,U_k]` by `d_k=L_k` if `L_k>0`, `d_k=-U_k` if `U_k<0`, and `d_k=0` otherwise. Therefore `A=sum w_k*d_k` satisfies `b≥A/(1024*27*D3)`.

A rectangle is certified by either `L_2>0`, or `10000*A > 61*1024*27*D3` (then `b>61/10000`). Divide any uncertified rectangle dyadically along x when `4*(b-a)≥d-c`, otherwise along y, provided the chosen interval has more than one grid unit; an already-unit x-interval forces a y split. The actual exact-integer verifier terminated over the entire unit square in **103 closed leaf rectangles**: 41 with `L₂>0`, 62 with strict public-cost exclusion, maximum depth 23. Their integer areas sum to `D²=4294967296`; the recursion itself preserves complete coverage and disjoint interiors.

The executed `REPRO_STAGE330B.py` prints all 103 rectangles, their classification and depth; independently reclassifies every leaf from its rational polynomial bounds; checks exact aggregate area; and returns `STAGE330B_GLOBAL_R2_CHAMBER_EXCLUSION_EXACT_PASS`. Manifest SHA256 is `435103e5e63aad8455668ea4ed500715440c7e80190791324a679e9351db301d`. This is a **continuous interval certificate**, not a floating-point grid inference. The contrapositive is immediate: no point with `r₂≤0` can have `b≤61/10000`.

## Corollary B — reduction for both source groups up to the algebraic cusp

Let `beta*` be the **global** minimum of `b` from the inherited Stage307/Stage329 exact inputs and let the inherited cusp budget satisfy `epsilon_dagger<2181407228/10^12`. At the explicit rational point `(2311/10000,1111/2000)`, exact evaluation gives `b=6057273/1600000000<379/100000`. Therefore

```text
beta* + epsilon_dagger
 <= 6057273/1600000000 + epsilon_dagger
 < 6057273/1600000000 + 2181407228/10^12
 < 61/10000.
```

For **any** two groups of Bernoulli rates satisfying `b_1+b_2 ≤ 2*beta*+epsilon_dagger`, individual global minimality `b_i≥beta*` implies `b_i≤beta*+epsilon_dagger<61/10000`. Apply Theorem A to each group: **both have strictly positive r₂**. This rules out the `r₂≤0` public-TV sign chamber throughout the *full* two-group feasible set through the tagged cusp. It does not establish global optimality of the restricted Stage329 allocation, exclude all off-curve competitors, or infer native P000 consequences.

## Proposition C — the r₃ chamber cannot be erased

Two rational points satisfy the same public-budget shell while giving opposite `r₃` signs:

```text
q_plus  = (9/40, 31/50):
b=156957/32000000, r2=43519/10000000>0, r3=5281/10000000>0.
q_minus = (9/40, 3/5):
b=63/12800, r2=63/16000>0, r3=-63/16000<0.
```

The inherited global minimum root lies in `(231/1000,232/1000)×(555/1000,556/1000)`. Endpoint/critical-point rational interval evaluation yields `beta*>23860079/6400000000>3/1000`. Both explicit witnesses satisfy `0≤b(q)-beta*<2181407226/10^12<epsilon_dagger` (the last strict lower bound is inherited from Stage329). Hence the full feasible shell **contains both r₃ signs**; setting a fixed `r₃` sign would erase admissible BRC observer provenance.

## Verification boundary, permission and next exact problem

Verifier: Python stdlib unbounded integers + `Fraction`, two executions yielding byte-identical stdout. The global sign theorem and rational witnesses are checked here; Stage307 global minimality, Stage329 cusp/curvature, and native X6 transfer are cited premises, not re-executed results. As of this run, native `research_authority_granted=false`, active owner enumeration returns `CONTROL_QUOTA`; no native claim, Result or mathematical review is claimed. GitHub storage is an evidence handoff, not acceptance.

Next Stage331-B: classify the remaining `r₀,r₁,r₃` public sign chambers and all 16 tagged Bernoulli comparison signs on the globally feasible region, isolate the `r₃=0` arc, then prove an exact KKT/interval exclusion of off-curve competitors or produce an earlier rational competitor for `1/5000 < E ≤ epsilon_dagger`.
