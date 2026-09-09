# Native X6 density ports: an autonomous candidate with unbounded defect amplification and bounded channel occupations

Progress-Event-ID: `NS-NATIVE-DENSITY-PORT-20260909-D5C00D-10`
Researcher-ID: `EM-DIRECT-D5C00D`
Research-Activity-ID: `RA-D5C00DF7D77F4AA2ACE0`
Session: `local-chat-ns-openai-audit-d5c00df7d77f4aa2ace0` (retained locally assigned key, not an authenticated platform identifier).
Status: **EXPLICIT CONSTITUTIVE CANDIDATE / ORDINARY PROOFS / EXECUTED INTEGER CHECKS / NOT INDEPENDENTLY REVIEWED**.

## 1. Scope and recovered frontier

The user's active objective is autonomous self-state research consistent with discreteness and Enterprise coordinates, without choosing forcing from a desired answer. The previous checkpoint, at `0327a493fda41377bfed7b320722cd48ed3b7e8c`, classified bare ternary unit-channel states, proved a four-way selector obstruction, and supplied six-step spatial lifts. Those results are consumed, not restarted.

This checkpoint constructs and studies one explicitly declared candidate law. It does **not** assert that P000 uniquely selects this law, that channel packets are primitive force quanta, or that this collision gate realizes `TRIADIC_CLOSURE_E`. Autonomous count dynamics is not automatically the classical condition f=0. No Navier--Stokes, viscosity, primitive-force, or physical calibration theorem is claimed.

Current source snapshot: `awdawmip/enterprise-math@562df4628f1896bd0faca3706efbacdb78f189d0`.
Current global-entry snapshot: `awdawmip/chatgpt-global-knowledge@202e522ea31357275ece35d7ddb9d9ffe3e1d99c`.

Relevant exact interfaces:
- `p000_reality_foundation.json`, blob `dc84bdae6595b5e237a2ad50d8b21916adb2e447`;
- `definitions/00_CURRENT_NATIVE_FOUNDATION.md`, blob `997f8b4a1d27bc7645959967b217972aa2454ef4`;
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, blob `3923890d77a02d84b772f789e6912dd14f220d14`;
- `src/enterprise_math/equivariant_section.py`, blob `0257fb7eaa95b2f88e772636d3ae2068d9ce42c0`;
- `experiments/ns_native_ternary_coherence_d5c00d.py`, blob `5dd5e0bce49c5d37360d34e0f9013830f7600357`.

The last file is imported unchanged by the new checker: its signed-coordinate helpers, ternary configuration constructor, and moment-fiber decomposition are actually reused. T7's stabilizer-fixed-lift criterion is applied as a theorem interface below; its executable section enumerator is not claimed to have been run. A scoped repository search returned no matches; this is not evidence that the repository has no other related dynamics. No new general toolbox family or shared Foundation definition is introduced.

Mathematical axes in this note are **1-based**, E_1 through E_6. Python axes are 0-based. Zero is an ordinary chosen Cell anchor. S6 relabels coordinates and channels jointly; no Euclidean 90-degree metric replaces Enterprise orthogonality.

## 2. A history cannot create an invariant selector from nothing

Let a group G act on a full state space X and let F:X->X be deterministic and G-equivariant. For any x,

    G_x is a subgroup of G_{F(x)}.                              (S1)

Indeed, gx=x implies gF(x)=F(gx)=F(x). Induction gives the same statement for F^t(x). A deterministically generated equivariant history also stays fixed under G_x, because every entry is fixed. Consequently an axis-selector q from such state/history must return an axis fixed by G_x.

Apply the existing T7 fixed-lift criterion to the four unused axes in the prior bare state C_l(j,sigma), j!=l. Their S4 action has no fixed axis. Neither waiting nor generating a deterministic symmetric history supplies the missing selector. Extra distinguishing information must already occur in the full state, its environment, or a separately declared input. Random or relation-valued updates have different contracts.

This is not a ban on nontrivial equivariant dynamics. A spatial distribution can contain local distinctions while the entire configuration remains symmetric. The construction below uses exactly that possibility.

## 3. Freeze one autonomous constitutive candidate: X6-DENSITY-PORT-1

The state is a field of nonnegative integer channel counts

    n_v(z),  z in Z^6, v in {+/-E_1,...,+/-E_6}.

It is an explicitly typed count-observer model, not a claim that this field is the complete native microstate. Put N(z)=sum_v n_v(z).

### 3.1 Collision gate

Use the previously classified configuration

    C_l(j,sigma) = {sigma E_j, +E_l, -E_l}.

A Cell is eligible only when its actual local multiset is exactly C_l(j,sigma) with j!=l. All other local populations are left unchanged. For each of the four candidate axes m outside {j,l}, read the old-state integer score

    A_m(z) = N(z+E_m) + N(z-E_m).                         (C1)

If exactly one candidate m maximizes A_m, replace the neutral pair on l by the pair on m:

    C_l(j,sigma) -> C_m(j,sigma).                         (C2)

If the maximum is tied, do nothing. No axis-label ordering breaks a tie. This wait-on-tie convention is a **constitutive choice**, not a consequence forced by P000 and not an assertion that tied alternatives are physically redundant.

All Cells read the same old field n. Let C(n) denote the simultaneously updated field. A computation's traversal order does not change C(n).

### 3.2 Primitive streaming

After collision each channel moves one actual signed-axis step:

    F(n)_v(z) = C(n)_v(z-v).                             (C3)

Time is the integer iteration count of this declared collision/streaming update. No time-dependent controller, forcing array, singular profile, continuous limit, or post-hoc residual is an input. The score is recomputed from the evolving field, not frozen as an external background potential.

The rule was recorded in `law_frozen.json` before numerical execution. That local freeze is provenance, not independent validation or a claim that the law was uniquely derived. Its choices are: count-three eligibility, neighboring-total score, unique-maximum routing, waiting on ties, and collision before streaming.

## 4. Exact structural properties of the declared law

**Well-definedness and positivity.** Eligibility supplies both old-pair packets. Collision removes one of each and adds one of each on a distinct axis. Nonnegative integer counts remain nonnegative integers. Streaming is a permutation of spatial-channel slots.

**Count and additive moment.** At each collision the total count is unchanged and

    P(z)=sum_i (n_{+E_i}(z)-n_{-E_i}(z)) E_i

is unchanged. Streaming preserves the global sums for finite particle populations. For finite deviations from a constant field it preserves their finite relative sums. These P components are declared algebraic observables, not an established physical momentum bridge.

The unit-channel squared-speed sum equals total count. Its conservation is therefore not an independent energy law or evidence of a viscosity mechanism.

**Coordinate covariance.** S6 maps eligible triples to eligible triples, candidate sets to candidate sets, and score lists by the same relabeling. A unique maximizer maps to the unique maximizer; a tie remains a tie. Translations preserve the relative neighbor positions. Equation (C3) also commutes with these actions. Hence F is S6-equivariant and translation-equivariant for all states and all iterates, not only the numerically tested examples.

**Finite dependency.** Collision at z reads counts within native graph distance one. A streamed output at z reads a collision at z-v, hence input distance at most two. By induction, t iterates at z depend only on the input ball of graph radius 2t. This is a dependency bound, not a claim that a packet traverses two primitive edges in one streaming step.

**Uniform channel bound.** Every changed local output has exactly three distinct occupied channels, each of count one. Unchanged outputs retain their old counts. Streaming preserves the maximum over slots. Therefore, for any initial global channel bound Q>=1,

    0 <= n_v(z,0) <= Q  =>  0 <= n_v(z,t) <= Q            (B1)

for every integer t. No continuous regularity is used.

## 5. A stationary count background and a mass-neutral seed

Let b be the constant field C_2(1,+). Every Cell has one +E_1 packet and a neutral pair on axis 2. All scores equal 6, so collision waits. Streaming preserves a constant field. Thus F(b)=b.

This background has internal traffic even though its count readout is stationary. Calling it stationary does not certify primitive force equilibrium.

Move **one** +E_1 packet from E_1 to 0:

    n(0)=b + delta_{(0,+E_1)} - delta_{(E_1,+E_1)}.       (I1)

The initial count and additive-moment differences are zero. Define

    D_t = sum_{z,v} |F^t(n(0))_v(z)-b_v|.                (I2)

For every finite t this is a finite integer sum, by the dependency bound. D_0=2.

At t=0 the excess Cell has total 4 and the depleted Cell total 2; neither is collision-eligible. At each of the eight Cells +/-E_m, m=3,4,5,6, the score in direction m is 7, and the other three eligible scores are 6. These eight Cells route their neutral pairs to axis m. Near the depleted Cell a single candidate score may be 5, leaving at least three tied maxima of 6; no collision is triggered there.

After streaming the eight pair changes contribute 32 units of count difference, and the excess/depletion contribute another 2:

    D_1=34, with exactly eight collisions.               (I3)

The full input remains symmetric under permutations of axes 3 through 6. All four transverse axes participate symmetrically. No global preferred unused axis has been selected; the relative position of each receiving Cell distinguishes its local port. This is compatible with (S1).

## 6. The all-time result is an induction, not an extrapolated fit

### Lemma 6.1: normal layers decouple

Suppose a layer z_1=k has exactly one +E_1 packet per Cell and no -E_1 packets. Any eligible ternary configuration in it must have j=1: with one +E_1 already present, an exactly cancelling pair can only lie on another axis. The gate therefore never changes an axis-1 channel, and its score reads only neighbors in that same layer. All changed channels stream transversely.

In a fresh layer containing a single extra +E_1 packet, its center has two +E_1 packets and cannot be eligible: with total three, one remaining channel cannot cancel them to give the required one-unit moment. In a fresh layer with one missing +E_1 packet, the center has only the neutral pair and cannot be eligible. Its neighboring score deficit does not create a unique maximum. The missing packet therefore propagates freely and leaves no transverse disturbance.

In (I1) the hole is always one layer ahead of the excess. The hole visits a pristine layer, leaves it pristine, and the excess visits it one tick later. The excess travels along +E_1, seeds the same transverse disturbance in each newly visited layer, and never encounters an old disturbance. The remaining layers evolve independently by the normal-layer rule.

### Lemma 6.2: define the wake once

The excess's eight first collisions create the finite deviation W_0 supported at +/-E_m, m=3,...,6, with a removal of one packet in each axis-2 channel and an addition of one in each axis-m channel. After one transverse streaming step call this wake w_1. Define w_{a+1}=F(b+w_a)-b. All w_a stay in the layer z_1=0, carry no axis-1 deviation, and have total relative count and relative additive moment zero.

For each m=3,...,6 and epsilon,sigma in {+1,-1}, w_1 contains a missing sigma E_2 packet at

    epsilon E_m + sigma E_2.

There are sixteen distinct such missing channel slots.

### Lemma 6.3: sixteen frontier holes cannot be refilled

For every a>=1:

1. w_a vanishes when |z_2|>a.
2. At z_2=a its only possible deviation is a missing +E_2 packet; at z_2=-a its only possible deviation is a missing -E_2 packet.
3. Each distinguished slot

       (epsilon E_m + sigma a E_2, sigma E_2)            (H1)

   remains missing.

**Proof.** The a=1 statement follows by directly streaming W_0. Suppose it holds at a. Outside |z_2|<=a the state is b, with pair axis 2. Its eligible score axes are 3 through 6 and sample that same z_2 level, so all scores still tie. Collision cannot create a change outside the slab.

At the upper boundary z_2=a, a missing +E_2 packet makes the local total two; the Cell cannot collide and so cannot refill that hole. A boundary Cell without a hole has local state b: any eligible collision can only remove its axis-2 pair, never add a +E_2 packet above baseline there. Streaming moves any upper-boundary +E_2 change one step forward. No other channel can reach the new upper boundary carrying a deviation, because it starts outside the old slab or has no positive axis-2 streaming component. The lower boundary is identical with signs reversed. The missing slot (H1) simply advances by sigma E_2. This proves all three assertions by integer induction. QED.

Since w_a has zero relative count, its positive and negative deviations have equal total multiplicity. Sixteen surviving negative units imply

    ||w_a||_1 >= 32, for every a>=1.                     (H2)

This lower bound does not assume that all earlier changes are monotone or that the complete wake norm is monotone. Other packets may interact freely behind the protected fronts.

### Theorem 6.4: unbounded defect amplification

At time t the exact configuration consists of an excess +E_1 at tE_1, a missing +E_1 at (t+1)E_1, and independent wakes w_a in layers z_1=t-a, a=1,...,t. Lemma 6.1 proves this decomposition inductively. The spatial layers and the two longitudinal defects are disjoint. Hence

    D_t = 2 + sum_{a=1}^t ||w_a||_1 >= 32t+2.            (T1)

In particular,

    D_t/D_0 >= 16t+1.

At the same time (B1) gives n_v(z,t)<=2 for all z,v,t. Thus **unbounded total defect amplification and uniformly bounded individual channel occupations coexist** in this specific autonomous candidate.

No desired growth factor occurs in the update law. The inequality is deduced from separately stated rules, conserved finite relative count, layer decoupling, and protected holes. It is not obtained by defining a residual forcing from the desired trajectory.

## 7. Remove the infinite-background dependency at every finite horizon

The infinite constant background in Section 6 is a convenient proof device, not a finite-energy NS datum. A distinct quantified conclusion can be proved with finite particle populations.

For any integer T>=1 put R=3T+3. Define b^(T) to equal b on the finite cube [-R,R]^6 and to vanish elsewhere. Define n^(T) by the same single-packet move (I1). Evolve **both** by the identical law F on Z^6, including the cube's free boundary; do not pin or replenish boundary counts.

The sixteen protected missing slots in each visited layer at time T have every coordinate of magnitude at most T. The longitudinal hole at (T+1)E_1 has maximum coordinate T+1. Their input dependency balls have radius at most 2T, so they lie inside the initial cube: T+1+2T<=R. Both finite evolutions match their infinite-background counterparts at every one of these witness slots.

Their global finite particle counts are equal and remain equal. The T layers and the longitudinal hole therefore give at least 16T+1 negative difference units, and equality of finite counts gives the same number of positive units. Consequently

    ||F^T(n^(T))-F^T(b^(T))||_1 >= 32T+2,
    ||n^(T)-b^(T)||_1 = 2.                              (T2)

Each system has exactly 3(2R+1)^6 packets, finite at its chosen horizon, with channel occupations bounded by two at every subsequent time as well. This proves that there is no uniform constant C, independent of the finite population/system and time, bounding all such perturbation gains by C.

The quantifiers are **for every T, there exists a finite initial pair**. They are not a claim that one fixed finite-particle system has unbounded L1 difference for all time: that is impossible when both populations have M particles, since their difference is at most 2M. No limit of continuous solutions or limiting smoothness is used in (T2).

The cube radius is a safe sufficient radius, not claimed optimal. The numerical finite-population check separately uses radius 2 for one tick; it is not a numerical enumeration of every cube in (T2).

## 8. Stability terminology, controls, and remaining physics

In a fixed integer-valued L1 state space, distinct states have a positive minimum separation. A sufficiently small metric ball contains only the given state. Therefore an epsilon/delta Lyapunov statement in that isolated-point metric would not express the intended physical question. This note claims the exact defect-gain property (T1), and its finite-population, no-uniform-Lipschitz-bound consequence (T2); it does not relabel them as fixed-finite-state Lyapunov instability.

The stream-only law S is a control: for all finite differences, ||S^t(n)-S^t(m)||_1=||n-m||_1. It satisfies count conservation, primitive streaming, and coordinate covariance but never amplifies the defect norm. Thus those structural properties alone do not select amplification, and the successful example cannot be promoted into a claim that P000 itself forces every self-state to be unstable.

This candidate has a real third-packet gate: removing the spectator from an otherwise eligible neutral pair disables that local collision. However the gate also reads a spatial neighborhood. Neither the word "ternary" nor conservation of P proves that the event is an admissible primitive three-force balance. The previous six-step lift remains an available relation/path descriptor for (j,l,m), but has not been shown to be the executed force mechanism of this update. Merely attaching its label would not close that obligation.

The unresolved physical bridge is now sharper: construct a legally typed `TRIADIC_CLOSURE_E` incidence and exchange ledger whose own evolution produces or constrains (C1)-(C3), or show that this candidate must be rejected as a physical realization. It must also distinguish information spread from velocity/stress growth and specify any dissipative observable. The present count rule is not a viscosity model.

## 9. BRC/observer preservation audit

Population: full signed-channel count fields on X6, with finite deviations or explicitly finite particle data. A selected port is derived from the old neighboring occupation field. It is not an independent external input. All score candidates are evaluated; labels remain visible in event output; ties are not secretly assigned probabilities.

The six scalar scores are **not** treated as a replacement for the full field. Equal neighboring totals do not in general determine future scores after channel-dependent streaming. Directional counts are retained. The prior test-model projection to bare local counts fails to determine the port when environments differ, as required by its fiber-obstruction theorem.

Finite score-only compression is used solely for the single collision's selection decision. Counts and the spatial-channel field remain the input to all future iterations. No individual particle trajectory, multiplicity of labeled microscopic histories, or physical force interpretation is reconstructed from these counts by assertion. Such observers would need a richer, provenance-preserving state and a separate descent proof. The candidate count dynamics is defined directly, not passed off as a proved quotient of all native microphysics.

Reuse resolution: `REUSE_EXECUTED` for the unchanged parent configuration/coordinate functions; `REUSE_APPLIED` for T7 stabilizer-fixed lifting and BRC fiber-constancy boundaries; `EXTEND_EXISTING_TOOL` only in the sense of an application-specific research checker, not a new admitted toolbox family.

## 10. Executed checks and exact values

Command:

    python experiments/ns_native_density_port_d5c00d.py --max-age 7 --full-steps 5 --output results.json

The executable imports the unchanged parent file next to it. The sparse background is a representation of omitted, unchanged Cells, not a periodic quotient or an omitted spatial dimension. The whole six-axis update is computed independently of the layer decomposition for the first five ticks, then compared exactly against that decomposition.

- 364 inherited ternary configurations times 64 binary score patterns = 23,296 exact local cases; 960 trigger a nonidentity collision. These finite patterns are tests, not an exhaustion of all integer neighborhoods; the structural proof handles those.
- 720 first-step S6 covariance comparisons and three translation comparisons.
- Seven single-wake ages and 112 distinguished-hole checks, including all slab/frontier predicates.
- Full-system D_t for t=0,...,5: **2, 34, 322, 1794, 7458, 24770**.
- Wake norms at ages 1,...,7: **32, 288, 1472, 5664, 17312, 44224, 108384**.
- A finite radius-two cube has 15,625 initially occupied Cells and 46,875 particles in each run. The identical zero-background law gives one-tick difference 2 -> 34, preserving both finite counts and additive moments. Its boundary is evolved, not clamped.
- An additional finite four-packet run preserves count and additive moment for eight ticks; the stream-only control keeps D=2 for seven ticks.

The numerical values are exact integer outputs. Their fast early growth is **not** an asserted asymptotic exponent or exponential growth theorem. The all-time result is the more conservative inequality (T1), proved in Section 6.

No Lean build, independent review, literature-priority assessment, Foundation promotion, README change, P000 change, or reassignment of another researcher was performed.
