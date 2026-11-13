# R626｜独立未知增益下的 signed BRC 方向可辨识性与精确修复

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED.
Parent: R625, source PR #1708. Scientific pin: R462 immutable commit 18783e01e3646c72b7aab3b16d3f565e83e6446f, signed-K source blob 7fa7a762f758b30c6090468ac43487daa34abad8, θ=0. Current behavioral rules read separately.
Mathematical scope: frozen auxiliary signed K response with a declared X6 positive-axis label bridge, not a native heartbeat field or physical time update.

## Model and exact input

Let P_j(t)=K_(2j−1)(t) in Z[t], j=1,...,6. Original frozen K recurrence yields

- valuation e_j=ν_t(P_j)=2(j−1), so e=(0,2,4,6,8,10);
- nonzero initial signed coefficient c=(2,−8,6,106,83,9).

Assign each basic index j to one of six labeled signed X6 positive directions through a permutation π. On a spatial axis x, let j=π⁻¹(x) and suppose one pure packet is Y_x(t)=A_x(t)P_j(t). Each A_x is an independent, unknown, nonzero element of Z[[t]] and may vary with the explanatory configuration. The d-jet observer returns (Y_x mod t^(d+1)) at each of the six separately addressable spatial axes. Let r_x=ν_t(A_x)≥0.

**Identifiability meaning:** if two parameter pairs (π,A) and (π′,A′) deliver the same labeled packet, must π=π′? The unknown gains are nuisance variables, so allowing them to differ between explanations is essential. Equal gains held fixed would give a different question.

## Theorem A: sharp gain-valuation-band dichotomy

Suppose an observer knows 0≤a≤r_x≤b for all six axes, while the integer leading coefficients of A_x remain arbitrary and nonzero.

**If b−a≤1, orientation is identifiable uniformly from the complete six-output d-jets if and only if d≥b+8.**

Proof of sufficiency: every visible Y_x has ν_t(Y_x)=r_x+2(j−1), hence its valuation lies in I_j=[a+2(j−1),b+2(j−1)]. For b−a≤1 the six integer intervals I_j are pairwise disjoint. At d=b+8 all branches j≤5 necessarily have a visible nonzero leading term, so we identify those five axes uniquely and infer the remaining sixth by exclusion. The argument is independent of signed leading coefficients, higher gain coefficients and the orientation.

Proof of necessity: at any d≤b+7 choose all gains A_x=t^b, and compare two orientations differing only by swapping j=5 and j=6. Their responses at those two axes both vanish modulo t^(d+1); all other axes agree exactly. Hence no uniform decoder at smaller depth. QED.

**If b−a≥2, even observing the full six formal series cannot identify every orientation when the gains are independent and unknown.** Take P_1=H_1 and P_2=t²H_2 with H_1,H_2∈Z[t] having nonzero constant terms. For two labeled axes, in the first explanation assign j=1 with gain t^(a+2)H_2 and j=2 with gain t^a H_1. Both outputs are exactly t^(a+2)H_1H_2. In the second explanation swap j=1 and j=2, and swap the respective gain formulas. Both observed outputs remain identical; every gain valuation belongs to [a,b]. All other axes and their gains can remain unchanged. Thus two distinct orientations give identical full infinite-series observations. QED.

The construction is integral and signed: no positive-mass substitution or classical continuous-phase operation is used. The a=0 witness from the actual frozen K is A_for_K1=(-8t²−8t³+4t⁴+3t⁵), A_for_K3=(2+3t), with common response −16t²−40t³−16t⁴+18t⁵+9t⁶.

## Theorem B: complete gauge ambiguity without gain constraints

Put B=∏_(j=1)^6 P_j ∈Z[t], B≠0. For **every** π∈S₆ and every spatial axis x of basic type j=π⁻¹(x), choose A_x=B/P_j=∏_(k≠j)P_k. Then Y_x=B for all x, independently of π. Each A_x is a nonzero polynomial. Thus a single complete six-axis packet has all 720 orientation explanations. This is an exact full-polynomial family, stronger than a bounded jet collision, and exhibits the unknown independent-gain ambiguity rather than any failure of the signed-K branch formula. QED.

## Theorem C: signed leading-unit gain repair

Assume instead that every gain A_x=t^(r_x)u_x(t) has leading coefficient u_x(0)=+1 or −1, with 0≤r_x≤R (R≥0); the six gains and their r_x may differ.

The lowest nonzero coefficient of Y_x has absolute value |c_j|. Because |c|=(2,8,6,106,83,9) are pairwise distinct, the first visible nonzero coefficient identifies j without knowing any gain. At d=R+8 all first five basic labels must be visible, so π is fully recoverable. This uniform bound is sharp: at d≤R+7, setting all gains to t^R and swapping basic axes 5 and 6 gives identical truncated outputs. QED.

If a native contract can instead **calibrate** each gain by an additional channel Z_x=A_x on the same packet, then the difference of finite visible valuations ν(Y_x)−ν(Z_x)=e_j identifies the branch for every axis with visible Y. For bounded r_x≤R the same d=R+8 bound is sufficient and sharp. This is a conditional observer design, not evidence such a channel already exists.

## Precision, update and native interpretation

These are input-output identifiability statements for six parallel *pure positive-branch* packet probes. They do not silently turn an orientation decoder into a certified quotient of an evolving joint state. Future operation safety requires the relevant source, grade, internal fields, branch order and time-typed rules; preserving decoded π is sufficient for this component only if the actual update map factors through it.

Native X6: six signed spatial coordinates with twelve directions; time is separately typed. Source definition definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json currently has fixed_heartbeat_program=null. The six pure independently-addressable outputs Y_x=A_xP_j and their gain constraints are candidate interface contracts requiring an actual native operator/readout witness. The exact no-identification theorem concerns the unconstrained independent-gain carrier; a gain normalization, narrow valuation band or calibrated channel provides three explicit repairs.

## Reproduction and checks

R626_VERIFY.js directly reconstructs all twelve frozen signed K polynomials from exact integer binomials and uses BigInt integer polynomial arithmetic. The executed checks are:
- 2,880 complete-orientation decodes over four narrow valuation bands;
- 4 sharp lower-depth swap witnesses;
- 4 arbitrary-coefficient width-two infinite-series swap witnesses;
- 4,320 exact full-polynomial factorization equalities for 720 orientations;
- 720 leading-unit orientation decodes and one sharp lower-depth witness.

All checks passed, marker R626_GAIN_BAND_IDENTIFIABILITY_EXACT_PASS. The full quantified theorems rest on the algebraic constructions and proofs above; the executable evidence cross-checks the frozen input and declared representative families.

## Next

Read the actual registered native X6 joint-field update/readout, identify whether A_x valuations are equal, belong to an adjacent band, are signed leading-unit normalized, or have a separately observable calibration. Extract one real operator whose input and readout match one of these conditions, and establish an exact operation-level descent certificate. If no registered output satisfies them, preserve this result as an auxiliary BRC observer theorem and test a concrete sum-of-histories counterexample next. Native Owner/RA/CLAIM and independent Driver admission are separately governed.
