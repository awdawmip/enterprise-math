# R77 — Complete exact critical-cell partition through original-label crossings

Date: 2026-11-11. Author-side research, auxiliary rational circular-source model. Predecessor R76 immutable scientific report: `352abbd17c31f146e08a77d0caa8afeb74797389`. Frozen S23/AV scientific input remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (not rebased). Retain source time, branch, original label and observer phase. No formal CLAIM, Result, independent review, native X6/BRC transfer or P000 change is claimed.

## Domain and declared arc convention

Let `E` be a finite set of distinct source identities `(t,branch)`, with integer times and totally ordered integer branch IDs. Take rational `x,L,U` with `L<=U`, integer observation time `j`, and integer original labels `a,b`. For real `theta` in `I=[L,U]`, define

`A(theta)={a theta}`, `B(theta)={b theta}`, `s_t(theta)={x+(t-j)theta}`,

where braces mean fractional part in `[0,1)`. A *directed, positively oriented, half-open circular arc* from A to B is specified as follows:

* if `A<B`: `A<=s_t<B`;
* if `A>B`: `s_t>=A or s_t<B`;
* if `A=B`: the arc is **empty** (not the full circle).

This is a declared extension of the R76 stable nonwrapping arc semantics and is not silently ascribed to an original research task. Define the latest-source readout `W(theta)` to be the lexicographic maximum `(t,branch)` qualifying at theta, or `NONE` if none qualifies. Branch-tie policy is therefore fixed and explicit. R76 latest-*time* semantics are recovered by projecting `W` to its first coordinate.

## Theorem R77-A (finite complete stratification)

For every source time t occurring in E, collect all theta in I solving an integer equality among

`a theta ∈ Z; b theta ∈ Z; (a-b)theta ∈ Z;`
`x+(t-j)theta ∈ Z; x+(t-j-a)theta ∈ Z; x+(t-j-b)theta ∈ Z.`

Also include L and U. When a coefficient is zero, the corresponding equality is either constantly true or never true, so it does not create isolated cutpoints. Every nonconstant equation has a finite set of rational solutions in the compact rational interval I. Let the sorted distinct rational cuts be `z_0<...<z_m`. Partition I into singleton cells `{z_i}` and nonempty open cells `(z_i,z_(i+1))`.

**Claim:** Each original-labelled membership Boolean of every source identity, and consequently W(theta), is constant on each open cell. Therefore testing one rational midpoint of each open cell and each singleton gives the exact complete latest-source partition for **all real theta in I**.

**Proof.** For any real affine function `v theta+c`, its fractional part is continuous and affine on an interval avoiding solutions of `v theta+c ∈ Z`; its floor is constant there. On an open cell, `{a theta}`, `{b theta}` and `{x+(t-j)theta}` are therefore affine continuous functions. Their ordering changes only if `(a-b)theta`, `x+(t-j-a)theta`, or `x+(t-j-b)theta` is an integer, all of which are included as cuts. Hence each of the three arc cases and each source membership Boolean remains fixed on the open cell. Taking the maximum over the finite, totally ordered identities leaves W constant. The original membership inequalities are evaluated directly at every singleton cut, including integer phase wraps, equal boundaries, lower-included and upper-excluded contacts. Every open rational interval has a rational midpoint; so the decision is exact over all its real points. QED.

**Degenerate domain:** If L=U, the algorithm makes exactly one singleton cell. Empty E returns NONE everywhere. If a=b or label phases coincide identically, the declared arc is empty and W=NONE. A source pair at a shared time preserves distinct branch IDs, so a fixed branch-tie rule does not erase identities.

## Theorem R77-B (linear-output oscillation family)

Take a single identity at time `t=12m`, `x=j=0`, `a=1,b=2`, `I=[1/4,1/3]` and m a positive integer. There are exactly m full source periods `[k/t,(k+1)/t]` wholly within I, indexed by integers `k=t/4,...,t/3-1`. In each such period consider

`theta_yes=(k+2/5)/t`, `theta_no=(k+9/10)/t`.

They lie strictly inside that period in increasing order. Their source fractional phases are respectively `2/5` and `9/10`. For every theta in I, `1/4<=theta<=1/3` and `1/2<=2theta<=2/3`, so `2/5` belongs to `[theta,2theta)`, whereas `9/10` does not. The ordered pair of witnesses shows at least one true-to-false transition in each full period; between the false witness for period k and the true witness for period k+1 is another transition. Consequently the latest-source function has at least `2m` adjacent-cell changes on I (including boundary transitions), as exact execution also confirms for m=2,4,8,16,32. Any **explicit complete constant-membership cell list** for this family has `Omega(t)` output size, while t occupies only `O(log t)` binary input bits.

This output-size lower bound applies to explicit cell enumeration, **not** to all possible compressed symbolic representations or arbitrary query models. It motivates a periodic or lazy certificate representation rather than an unrestricted complexity no-go.

## Executed exact evidence

`check_r77.py`, Python standard-library `fractions.Fraction`, seed 771126, executed locally without floating-point comparisons. On 160 random finite exact models, each singleton cut and three interior rational points of each open cell were checked against direct pointwise latest-source evaluation: **18,464 comparisons**, all passed. 126 random models contained at least two different latest-source values across the parameter interval; the maximum random partition had 487 cells. On the explicit period family t=24,48,96,192,384, the complete cell lists contained 13,25,49,97,193 cells respectively, and reported 4,8,16,32,64 adjacent-cell changes. These checks test the independent cell-invariance prediction at rational points; the universal all-real claim is supplied by the proof, not sampling.

## Cost and continuation

If `M` denotes the number of distinct nontrivial rational cuts, the displayed implementation sorts cutpoints and evaluates all n sources in each of at most `2M-1` strata. It is an explicit complete algorithm, **not** a demonstrated R76 time improvement. The number of cuts may scale with the magnitude of source times and label coefficients, not just their bitlength. The computation budget does not include an optimized bit-operation scheduler or memory-persistent winner structure.

**R78:** develop a lazy event/cell oracle that avoids producing all output cells when only `STABLE_NONE/STABLE(t)/CHANGES(witnesses)` is needed. Compare R75 heapification versus R76 maintained winners on matched complete outputs under update/query-heavy workloads, counting tree allocations, historical version bytes and exact arithmetic. Prove any shortcut under a stated observer and original-label convention, preserving the frozen S23 pin and source identities.
