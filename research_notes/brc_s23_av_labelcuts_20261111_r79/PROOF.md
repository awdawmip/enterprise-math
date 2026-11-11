# R79 — Complete latest-source decision with original-label cuts only

Author-side mathematical continuation of R78, 2026-11-11. Original auxiliary circle model with exact rational observer phase `x`, integer source time `t`, branch identity, observation time `j`, integer original labels `a,b`, rational closed query interval `I=[L,U]`. Keep the explicit R77 directed half-open circular arc: from `A={a theta}` to `B={b theta}`, if `A<B` it is `[A,B)`; if `A>B` it is `[A,1) union [0,B)`; if `A=B` it is EMPTY. Latest readout `W(theta)` is the lexicographically greatest qualifying `(t,branch)`, otherwise NONE. The frozen scientific source `43ec6098b1330ae86d0a7863be336c5d97f6ef34` and P000 are unchanged.

## Lemma A: fixed-label wrap and nonwrap share the same lifted inequality

On an open rational interval `J=(u,v)` where floors `k_a=floor(a theta)` and `k_b=floor(b theta)` are constant, and original-label order `A<B` or `A>B` is fixed, set `q=0` if `A<B`, `q=1` if `A>B`. Define

`F_e(theta)=x+(t-j-a)theta+k_a`,
`w(theta)=(b-a)theta+k_a-k_b+q`.

Then on J, `0<w(theta)<1` and original-labelled membership is exactly

`P_e(theta) <=> {F_e(theta)}<w(theta)`.

Proof. The directed positive arc from A to B has circular length `w={B-A}` in `(0,1)`. Subtracting A from the source circle phase rotates the arc to `[0,w)`, so membership is its normalized fractional phase `<w`. The formulas follow by the constant floor identities. This works equally for arcs crossing the zero phase.

## Lemma B: a complete O(1)-arithmetic classification on an OPEN label cell

For source e, write `F_e(theta)=c theta+d` and let `f_-`, `f_+` be the minimum and maximum of its affine *limiting values* at u,v. If a nonconstant F has some integer k in the **strict** open range `(f_-,f_+)`, then it has both an IN and an OUT rational witness in J:

- IN at the unique interior theta solving `F(theta)=k` (fractional part zero, width positive).
- OUT at an interior theta with `F(theta)` strictly below k but sufficiently close to k. Because the interior width at the crossing is `<1` and continuous, fractional parts approaching one are eventually outside. Rational witness calculation may choose `delta>0` smaller than `(1-w(theta_k))/8`, `(k-f_-)/2`, and `(1-w(theta_k))*abs(c)/(8*abs(b-a))` when the last denominator is nonzero; put `F(theta_out)=k-delta`.

If there is **no** integer in the open range `(f_-,f_+)`, the floor `k=floor(F((u+v)/2))` is constant throughout J (including the constant-integer case). Membership is the strict affine inequality

`H(theta)=F_e(theta)-k-w(theta)<0`.

Thus an IN witness exists exactly when this inequality holds at some rational point of the open interval; an OUT witness exists exactly when `H(theta)>=0` at such a point. Since H is affine, its only possible sign division is its rational zero. Split J at that zero if it lies inside J, and check one rational midpoint of each resulting open subinterval. This finds every nonempty sign region and handles equality, half-open boundary logic and the degenerate constant H case. No source phase-wrapping point is enumerated.

Each source is therefore classified on an open label cell as ALWAYS_OUT, ALWAYS_IN, or MIXED using a bounded number of exact rational operations, independently of |t| as a numerical magnitude (integer bit lengths still matter).

## Theorem C: complete latest-source trichotomy on an arbitrary rational interval

For `a!=b`, collect the rational solutions in I of only the three original-label equations

`a theta in Z`, `b theta in Z`, `(a-b)theta in Z`, plus L,U.

Sort distinct cuts `z_0<...<z_m`. Evaluate every singleton cut point using the original R77 arc convention. For each open cell `(z_i,z_{i+1})`, original-boundary floors and the sign of `A-B` are constant. Use Lemma B for sources in decreasing `(t,branch)` order; the first source admitting any IN parameter is the maximum possible winner. If it is ALWAYS_IN on that cell, the latest source is constant and equals this identity; if it is MIXED, two rational witnesses give unequal latest winners. If no source can qualify, latest is NONE there. Compare the winners/witnesses of all singleton and open cells:

- all NONE -> `STABLE_NONE`;
- same identity in every cell -> `STABLE(identity)`;
- otherwise -> `CHANGES(witness_1,witness_2)` with exact rational parameters whose latest outputs differ.

If `a=b`, target arc is empty at every parameter and returns `STABLE_NONE` directly. For a one-point I, only its singleton is evaluated. **The returned trichotomy is exact on all real parameter values of I**, including source wraps, boundary-order changes, label wraps, equal-label singleton contacts and branch ties.

Proof. A label floor can only change where `a theta` or `b theta` is integer, and the order of fractional endpoints can only change where `(a-b)theta` is integer or a floor changes. Thus every open cell has the fixed types of Lemma A. Lemma B certifies precisely whether each source can ever be in/out within that cell. The maximal potential source yields the exact latest-source cell status by the R78 maximality argument, and its rational witness is valid at an actual open parameter. The singleton evaluation supplies exact cutpoint semantics. Finite cells partition I; comparing their constant or varying latest outputs is exhaustive. QED.

## Cost and genuinely new scope

Let `C` be the number of distinct original-label cutpoints. It is bounded by `O(1+(|a|+|b|+|a-b|)*(U-L))` over a fixed rational interval, independent of the source-time magnitudes. With n source identities already available in descending order, at most `O(C n)` source examinations and bounded exact rational arithmetic per examination decide the *three-valued global answer*; the implementation also performs a linear latest-output check at constructed witnesses. This avoids R77's enumeration of `x+(t-j)theta`, `x+(t-j-a)theta` and `x+(t-j-b)theta` integer crossings and proves R78's endpoint mechanism survives both wrapping arcs and boundary-varying intervals. The count C can grow with large original labels; this is a remaining compression direction rather than a no-go for arbitrary encodings. Integer bit complexity, materialized persistent-index updates, memory and a full partition-output complexity are separate measures.

## Executed exact regression

`check_r79.py` uses only Python standard-library Fraction. It performs 400 randomly generated models with both signs of a,b (including a=b), varied rational x and integer source times, and compares the trichotomy to an **independent R77 six-family critical-point reference** evaluating every singleton and open-cell midpoint: 22,464 exact reference strata plus 1,600 direct rational point checks; statuses 101 STABLE_NONE, 25 STABLE and 274 CHANGES. All assertions passed. Additional 403-bit time tests returned CHANGES with only two original-label cuts and directly verified witness differences. Explicit wrapping/equal-label cases and shared-time branch ties were included. `verification_r79.json` captures exact counts and reproducibility parameters.

## Next R80

Implement the original-label-cut-only oracle against R76 persistent AVL maximal-source traversal, count exact big-integer bit work and persistent allocations, and benchmark R75 transient-heap versus R76 maintained-source maximum on identical complete-output workloads. Explore compressed label-cut families when |a|+|b| is itself huge, and observer phase x(theta) that is piecewise affine. The present mathematics is author-side auxiliary-model evidence awaiting independent semantic review.
