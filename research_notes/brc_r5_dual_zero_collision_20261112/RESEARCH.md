# R5 — Exact dual-zero ordered witness classification at all fixed/moving collision pairs

Date: 2026-11-12 (Asia/Shanghai). Classification: original author-side, finite exact theorem in the frozen **external** 28-coordinate P/Q–BRC Blackwell auxiliary transport model. This is a new candidate scientific increment, not an independent mathematical review or formal Source Result.

## Input provenance and scope

Reuse the immutable 15-operation fixture at Enterprise Math commit \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`, file \`research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py\`. The frozen science pins remain Global \`a01383f825ef9d43b4b754254303298c64041568\`, Enterprise Math \`86149263e38c22292c9def1e0f69092efa1be77e\`. The previous all-parameter first-zero result is Draft PR #2139; the 3,432 crossing-pair event inventory is Draft PR #2143; the uniformly ordered *fixed* witnesses and the exact 28-coordinate fixture reassembly are Draft PR #2146 (immutable commit \`65bd36974843c20a603a8615fb1efa4aa1448aeb\`).

Let \`X\` be the 28-component source state and \`M_1,...,M_15\` the labeled BRC operations. Define the integral sum \`P_S=36 sum_{a in S} M_a\`. Let \`k0=(target0,source3)\`, \`k1=(target1,source3)\`, and

\[
 x=X_{k0}=X_{k1}=\frac{155682221}{25142124560000000},
 \quad X(r)=X+x rH,\quad H_{k0}=0,\ H_{k1}=-23.
\]

The permitted hidden-state interval and operation-ray endpoint are

\[
 I=[L,U]=\left[-\frac{427508577031693280}{628800490619},\frac1{23}\right],
 \qquad E=\frac9{115400000}.
\]

The fixed coordinate weights are

\[
(P_{\{a\},k0})_{a=1}^{15}=
(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80).
\]

There are 1,144 values \`n=-P_{S,k0}>=3\`, defining fixed thresholds \`t_n=36x/n\`. The second coordinate has only three nonzero atom weights:

\[
 (P_{\{1\},k1},P_{\{6\},k1},P_{\{11\},k1})=(-432,-108,+540);
\]
all other 12 atom contributions to \`k1\` are zero. The moving families are \`u_q(r)=x(1-23r)/q\`, \`q in {15,12,3}\`. Each of the 3,432 labeled crossing pairs \`(q,n)\` satisfies

\[
 r_{q,n}=\frac{1-36q/n}{23},\qquad t_n=u_q(r_{q,n}).
\]

## New theorem — shared dual-coordinate zero certificates

At a fixed/moving collision pair \`(q,n)\`, call a subset \`S\` a **dual-zero ordered witness** when a single ordering of \`S\` has all its intermediate 28-coordinate masses nonnegative at \`(r_{q,n},t_n)\`, and its final state vanishes at **both** \`k0\` and \`k1\`.

**Theorem (exact finite census for the frozen 15-atom fixture).** Exactly **1,065** of the 3,432 crossing pairs have a dual-zero ordered witness. Their decomposition is:

| Moving label q | Pair events admitting a dual-zero ordered witness | Distinct labeled masks realizing such events | Largest possible n |
|---:|---:|---:|---:|
| 15 | 229 | 504 | 508 |
| 12 | 298 | 749 | 592 |
| 3 | 538 | 1,682 | 844 |
| **Total** | **1,065** | **2,935** | — |

For all **2,935** masks satisfying the two algebraic zero conditions in one of these event pairs, the full 28-coordinate final state is nonnegative **and** there exists a legal ordering of that mask at the collision. The remaining **2,367** crossing pairs admit no single-subset dual-zero witness, already at the integral-subset-sum level. A pair collision still has the previously established separate fixed and moving capacity evidence; this classification asks whether the **same** operation prefix witnesses both zeros.

### Algebraic reduction

A subset can simultaneously have the two desired zeros exactly when

\[
 P_{S,k0}=-n,\qquad P_{S,k1}=-36q.
\]

Because \`k1\` depends only on atoms 1, 6, and 11, the three possibilities are:

| q | Must include | Must exclude | k0 weight from forced atoms |
|---:|---|---|---:|
| 15 | 1 and 6 | 11 | 420 |
| 12 | 1 | 6 and 11 | 336 |
| 3 | 6 | 1 and 11 | 84 |

The remaining 12 atoms have minimum total \`k0\` weight \`-928\`. Hence the largest possible \`n\` in the three cases is respectively \`508,592,844\`. The exact 12-atom subset sums yield **229, 298, 538** distinct \`n\` values and **504, 749, 1,682** masks respectively. Together this classifies the possible simultaneous-zero pairs before checking legality.

### Exact intermediate-state proof

For each candidate mask \`S\`, its collision parameter \`r_{q,n}\` and ray value \`t_n\` are forced. For every prefix mask \`A\`, legality reduces to the 28 exact rational tests

\[
 F_{A,k}(q,n)=X_k+x r_{q,n}H_k+\frac{x}{n}P_{A,k}\geq0.
\]

A complete subset predecessor recursion on the labeled operations determines whether an admissible order exists:

\[
 D(\varnothing)=\mathrm{true},\qquad
 D(A)=\Big(\forall k,\ F_{A,k}(q,n)\geq0\Big)
       \land\Big(\exists a\in A:\ D(A\setminus\{a\})\Big).
\]

This recurrence is necessary and sufficient by the last-operation decomposition. The attached standalone verifier enumerates all \`2^15=32,768\` masks, computes each forced pair exactly, reconstructs an ordering for **every** one of the 2,935 candidate masks, and separately checks every reconstructed prefix in all 28 coordinates. It proves the 2,935-for-2,935 legality assertion for the declared finite model.

Minimum ordered witness length across the distinct pair events:

| q | Counts by minimum step length |
|---:|---|
| 15 | 3:1, 4:6, 5:23, 6:53, 7:69, 8:50, 9:22, 10:5 |
| 12 | 2:1, 3:9, 4:35, 5:72, 6:87, 7:63, 8:26, 9:5 |
| 3 | 2:3, 3:22, 4:75, 5:149, 6:149, 7:95, 8:38, 9:7 |

### Concrete distinction at r=0

At \`r=0\`, three pairs collide at *distinct capacity values*: \`(15,540)\`, \`(12,432)\`, \`(3,108)\`.

* \`(15,540)\` admits no dual-zero mask: forced atoms 1 and 6 contribute \`+420\` to \`k0\`, while the remaining available negative atoms sum to only \`-928\`; hence the smallest total \`k0\` weight is \`-508 > -540\`.
* \`(12,432)\` admits the five-step witness \`(15,14,10,1,12)\` (1-based labels).
* \`(3,108)\` admits the six-step witness \`(15,6,4,3,2,12)\`.

The two explicit words are checked prefix-by-prefix using exact rational arithmetic.

### Structural separation of uniform and collision-specific witnesses

Any word that is legal for **all** \`r in I\` at a fixed positive \`eps\` must have \`P_{A,k1}>=0\` at every prefix \`A\`: at \`r=U=1/23\`, the initial mass \`X(U)_{k1}=0\`, and the \`k1\` prefix mass is \`eps P_{A,k1}/36\`. A dual-zero witness at an interior moving collision instead requires \`P_{S,k1}=-36q<0\`. Therefore an all-\`I\) uniform fixed witness cannot also be a collision-specific dual-zero word. This is a rigorous reason to carry **separate** witness types in the event-sweep data structure.

## Reproduction, scope and next science

Run \`python3 research_notes/brc_r5_dual_zero_collision_20261112/VERIFY_DUAL_ZERO_COLLISIONS.py\` from any directory with Python 3 standard library. All arithmetic is integral or \`fractions.Fraction\`; no floating rounding. The verifier embeds the full frozen 28-coordinate fixture instead of importing current mutable project state.

This result classifies a declared finite auxiliary model with its 15 labeled BRC residual operations, preserving all source/target ports and intermediate nonnegativity. A transition to native X6 or the three-dimensional research slice would require an explicit embedding/readout and relation-preservation proof; the existing P000 axioms are untouched.

**Next exact question.** For each of the 2,935 dual-zero witnesses, compute the maximal real-\`r\` interval on which its same ordered word remains legal when evaluated at the moving time \`u_q(r)\`. The prefix constraints are affine in \`r\`:

\[
 X_k+x rH_k+\frac{x(1-23r)}{36q}P_{A,k}\geq0.
\]

Each word's validity range is therefore a rational closed interval, obtainable from its finite list of prefix inequalities. Test whether those intervals can be attached to the existing 3,432-swap event stream as a compact piecewise-valid certificate, while retaining the independently proven 1,144 full-interval fixed witnesses. Formal Source Result acceptance and independent review remain with their existing authorities.
