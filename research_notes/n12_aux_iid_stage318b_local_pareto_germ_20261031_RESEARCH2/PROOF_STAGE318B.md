# Stage318-B — exact global near-floor Pareto germ and asymmetric one-block allocation

Classification: **PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Research2 author-side continuation of Stage317-B. No native CLAIM/Result, independent Driver review, or P000/X6 transfer is implied. All continuum claims below are in the explicitly declared external BRC-inspired finite positive-rational source/observer model.

Source snapshot fixed for this turn: GLOBAL_KNOWLEDGE_V1 `main@d310c5f090bd5883e89df4c5827468959073541b`; Enterprise Math `main@e4da8741fc91c6b584de6a61a9c8cd6b7ae1ed66`. P000 V5 source blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`; ACTIVE worldview blob `99238c3466eb0805748bae01fd1a20868a5a351e`. Parent source: Stage317-B `b6ddb02d9c5a66e1e4d673f341841d7a92d459e0`, Stage316-B `ae57c9c8159db7694546e9a35969888ac604715e`, Stage315-B `388bd4f074dfba8a6e8ff9b9d242819822e85bee`, and the Stage307-B.2 unique global algebraic minimum and exterior certificate `128d2ce6aeb0299cdf842d0ad65082a64ba9d475`, all in Research2 Draft PR #1736. The original mathematical premises are reused at the exact observer/horizon scope, not re-promoted.

## Frozen auxiliary model

S is fair in {0,1}; conditioned on S, the private bit J correctly copies S with probability 7/8, public bit W correctly copies S with probability 3/4, and public bit Y has rate p_S where p0=1/4 and p1=3/4. The eight private h=(J,W,Y) source-mass pairs (a_h,b_h)/256, h=000,...,111, are (63,1),(21,3),(21,3),(7,9),(9,7),(3,21),(3,21),(1,63). The representation uses one *deterministic, locked* Bernoulli rate t_h in [0,1] for each h across three future F accesses. A future H access emits an independent fair bit. The public observer sees G=(W,Y) and future actions/outputs; tagged observer sees (S,J,G) and actions/outputs. Every public-history-adaptive H/F transcript is a common postprocessing of the full all-F 3-bit word, so the worst public/tagged total variations P3,T3 equal their all-F values. Randomizing a persistent rate within a private h, changing the true process, adding source access, or changing horizon is outside the claim.

By Stage315-B, at any feasible public budget, every tagged-optimal eight-rate representation fixes central t001=t010=1/4, t101=t110=3/4. By Stage316-B, after identifying (x,y)=(t000,t100) and (x',y')=(1-t111,1-t011), the *exact* complete four-rate objective is P3=b(x,y)+b(x',y'), T3=K+c(x,y)+c(x',y') where K=33/1024 and

- B_k(z)=z^k(1-z)^(3-k), r_k(x,y)=4B_k(x)/5+B_k(y)/5-p_k, p=(61,21,9,9)/160;
- d(x,y)=(1/2) sum_{k=0}^3 binom(3,k)|r_k(x,y)| and b=(5/16)d;
- D3(q,z)=TV(Bern(q)^{⊗3}, Bern(z)^{⊗3}); c=[63D3(p0,x)+D3(p1,x)+9D3(p0,y)+7D3(p1,y)]/256.

Let (x*,y*) be Stage307-B.2's **unique global** minimizer of d; a*=1-x* is the unique root in (7689/10000,769/1000) of (41/16-4a²)^3−(61/32−4a³)^2=0 and y*=1−sqrt(41/16−4a*²). More precise certified brackets: a* in (768916059144478,768916059144479)/10^15 and y* in (555508857277,555508857278)/10^12. There r0=r1=0, r2>0,r3<0. Define β*=b(x*,y*), P_min=2β*≈0.00755826723771693829, and F3(z)=min{T3(t):P3(t)≤z}.

## Theorem (complete eight-real-rate local Pareto germ)

Set **δ=1/100000000**. There is a unique right-moving analytic branch (x_ε,y_ε), 0≤ε≤δ, with (x_0,y_0)=(x*,y*), x_ε≥x*, r1(x_ε,y_ε)=0 and b(x_ε,y_ε)=β*+ε. It lies in R=[231/1000,2312/10000]×[555/1000,556/1000], where r0(x_ε,y_ε)<0 for ε>0, and has unique positive x-displacement for ε>0.

**(1) One-block envelope.** For each 0≤ε≤δ,

C3(β*+ε):=min{c(x,y):b(x,y)≤β*+ε}=c(x_ε,y_ε).

Its minimizer is unique in the entire real square [0,1]^2. For 0<ε≤δ this is an actual change of the lower envelope, not merely a candidate restricted to one sign chamber. C3 is strictly decreasing and twice differentiable on (β*,β*+δ] with **−41<C3''(s)<−38**. At the floor it has the exact right derivative

C3'(β*+) = −κ,  with κ=−[c_x+c_y v]/[(15/16)(r2_x+r2_y v)] evaluated at (x*,y*), v=−r1_x/r1_y,

and the rational enclosure **1197917/10^6<κ<1197919/10^6** (κ≈1.19791766).

**(2) Complete eight-rate Pareto formula and optimizers.** For all 0≤ε≤δ,

**F3(P_min+ε)=K+c(x*,y*)+c(x_ε,y_ε).**

For ε>0 there are exactly TWO full eight-rate minimizers: after the central four MAP resets, one outer block is (x*,y*) and the other is (x_ε,y_ε), in either order under G=00/G=11 complementation. For ε=0 the tagged-optimal full vector is unique, as in Stage317-B. The strict asymmetry is caused by negative envelope curvature, not by a numerical preference or a presupposed symmetric allocation.

## Proof with exact global exclusion and finite rational interval certificate

1. **Global localization is quantitative, including outside the Stage307 box.** Stage307's exact rational exterior cover of [0,1]^2 minus B=[23/100,24/100]×[55/100,56/100] partitions four rectangles into (329,165),(55,28),(27,14),(133,67) (nodes, leaves). Every leaf's explicit rational lower bound on d exceeds the Stage307 rational witness U=d(231083940855/10^12,555508857277/10^12), and the **minimum strict difference exceeds 1/200000**. The current `REPRO_STAGE318B.py` regenerates the entire dyadic recursion and certifies that stronger finite rational gap, preserving exactly the Stage307 split and word extrema rules. Since d(x*,y*)≤U, any (x,y) outside B obeys b−β*≥(5/16)(1/200000)>δ, and cannot appear in C3(β*+ε), ε≤δ. Inside B, Stage307's proved local sharp inequality d−d*≥(|x−x*|+|y−y*|)/120 implies |x−x*|+|y−y*|≤384ε≤3.84×10^-6. The exact root brackets put every feasible point strictly inside R, with a positive margin. Hence no boundary of B, R or the full square can contain a constrained optimum.

2. **Exact signs and constrained stationarity.** Throughout R, rational Bernstein extrema yield r2>0,r3<0, and the binomial sum of all r_k is zero. Thus **d=3r2+[r0]_++3[r1]_+** and b=(5/16)(3r2+[r0]_++3[r1]_+). Throughout R, the four tagged D3 terms have their Stage317 polynomial forms; hence c=[63(1−x)^3+A(x)−2A(y)−1295/64]/256, A(z)=1−3z²+2z³. In each one of the four open sign chambers for (r0,r1), b is a cubic polynomial, with gradient (5/16)(3∇r2+e0∇r0+3e1∇r1), e0,e1∈{0,1}. Exact rational interval evaluation over R certifies each determinant det(∇b,∇c) is strictly nonzero (e0=e1=0 gives positive sign, the other three negative). Also c_x<0,c_y>0 throughout R. Therefore there is no unconstrained interior optimum (∇c≠0) or smooth-chamber active constrained optimum (Lagrange multiplier would require det=0). A constrained optimum must lie on **r0=0 or r1=0**; their only common zero in R is the unique Stage307 minimizer. For ε>0 this common zero is not optimal, since the next paragraph constructs a feasible branch with strictly lower c.

3. **Four kink branches and exact slopes.** Implicit functions r0=0 and r1=0 exist throughout R since r0_y,r1_y are strictly nonzero. Along each, v=−r_i,x/r_i,y and all branch derivatives are rational functions of (x,y) with denominators bounded away from zero. The derivative of the *other* residual has a strict sign throughout R: along r0=0, dr1/dx>0; along r1=0, dr0/dx<0. Thus each zero curve has two oriented sides x>x*, x<x* with fixed residual chamber. Exact interval evaluation yields |v|<12 and |db/dx|>18/100 in every oriented branch, with db/dx>0 on the right and <0 on the left. Since the root brackets lie more than 12×10^-7 from R's y boundaries, each oriented segment of x-length 10^-7 remains inside R and raises b by >1.8×10^-8>δ. By monotonicity, every ε∈(0,δ] has exactly one feasible b=β*+ε point on **each** of the four branches.

  From c_x,c_y and b_x,b_y, interval evaluation of (dc/dx)/(db/dx) on the four branches produces the following uniform, rationally certified ranges (decimals here are strictly rational outer enclosures; the checker uses `Fraction`, not floats for assertions):

  | Zero curve | x direction | dc/db strictly between |
  |---|---|---|
  | r1=0 | right | −1.21 and −1.19 |
  | r0=0 | right | −0.90 and −0.87 |
  | r1=0 | left | 1.70 and 1.90 |
  | r0=0 | left | 3.00 and 3.20 |

  Every branch starts at (β*,c*). Integrating these **strictly separated** slopes over the same positive budget ε proves that the r1=0 right-moving branch has strictly least c of all boundary kink candidates. Moreover, because dc/db<0 there, it strictly improves on the floor point c*. This proves **unique global C3 minimizer** and the expression C3(s)=c(x_s,y_s).

4. **Exact curvature sign.** Along the winning implicit branch r1(x,y(x))=0 put v=y'=−r1_x/r1_y and w=y''=−(r1_xx+r1_yy v²)/r1_y. Set B'=(15/16)(r2_x+r2_y v), B''=(15/16)(r2_xx+r2_yy v²+r2_y w), E'=c_x+c_y v, E''=c_xx+c_yy v²+c_y w. Then C3'(b)=E'/B' and C3''(b)=(E''B'−E'B'')/(B')³. Direct exact interval evaluation over the entire R proves **−41<C3''<−38** and B'>0. Substitution of the precise Stage307 algebraic root enclosures gives **1.197917<κ<1.197919**. Each assertion is in `REPRO_STAGE318B.py` and its executed stdout, with rational interval arithmetic; no pointwise float evaluation is used as a certificate.

5. **Complete Pareto allocation.** The Stage316 exact infimal-convolution theorem gives F3(z)=K+min_{s∈[β*,z−β*]}(C3(s)+C3(z−s)). For z=P_min+ε, ε≤δ, both arguments lie in the just-proved concave/decreasing interval. Since C3 is strictly decreasing, optimal solutions spend the entire feasible public budget; because C3 is strictly concave, the sum is strictly concave on the split interval and so its MINIMUM occurs only at the two endpoints, namely (s,z−s)=(β*,β*+ε) or reversed. Each block has a unique C3 minimizing vector. Stage315 gives central-MAP uniqueness for tagged optimization. This proves the value and exhaustive two-vector classification. At ε=0 both endpoints coalesce; Stage317 uniquely characterizes the tagged-optimal full vector. QED.

## Reproduction, interpretation and remaining obligations

`REPRO_STAGE318B.py` uses standard-library `fractions.Fraction` with an exact closed-interval class (all arithmetic endpoints exact, no floating-point assertions). It generates all four global exterior-cover trees, proves the strict minimum gap, validates the algebraic-root enclosures, 4 chamber determinants, four kink slope intervals, winning-branch strict curvature, and independently enumerates all 128 tagged and 32 public atoms for a rational test of the Stage316 block formula. Actual stdout is stored as `REPRO_STAGE318B_EXECUTED_STDOUT.txt` and ends `STAGE318B_EXPLICIT_LOCAL_PARETO_GERM_EXACT_PASS`. The continuum proof uses the displayed localization, implicit-function, stationarity, branch-comparison and curvature arguments **in addition** to the certified rational bounds; finite checks alone do not prove the theorem.

The full result applies to the explicit finite Bernoulli BRC observer model (positive source joint masses; both public and provenance-tagged future observations), **not** to original P000 dynamics. A genuine native bridge still requires a six-axis X6 Cell-path embedding, a correctly typed 3D slice and third coordinate, triadic force closure, ordered time, registered final Cell address and preservation of future observer relations. No such bridge is asserted. Native owner remained unconfirmed because the actual `em_control_tasks` read returned `CONTROL_QUOTA`; `em_status` reported `research_authority_granted=false`. No native CLAIM or independent admission was attempted or invented.

**Next Stage319-B:** enlarge the rigorous local δ toward the previously exhibited Stage314 algebraic single-fiber competitor and certify the first competing sign chamber or allocation transition. A finite rational chamber CAD/Sturm/interval certificate can compare the four kink costs beyond R and distinguish genuine Pareto bifurcation from breakdown of a coarse localization bound. Do not repeat the already established global floor and exact near-floor germ. Native X6/BRC transfer remains a separate typed proof obligation.
