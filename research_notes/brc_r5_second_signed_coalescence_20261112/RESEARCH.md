# R5 — Exact second signed resonance coalescence and asymmetric legal-order loss

**Date:** 2026-11-12 Asia/Shanghai. **Research mode:** independent author-side exact finite calculation; frozen external P/Q–BRC Blackwell auxiliary model, not native X6. Independent review and canonical Source Result pending.

## Provenance and frozen inputs

Original 28 rational masses `X`, fifteen labeled six-arc BRC moves `M_a` and ray direction `D` are unchanged from immutable [R5 PR #2102](https://github.com/awdawmip/enterprise-math/pull/2102), commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`. The immediately preceding bilateral phase classification is [PR #2116](https://github.com/awdawmip/enterprise-math/pull/2116), commit `616296146a0d48966bcf6021a52692e10242aad2`; its two first collision endpoints were also studied in [PR #2114](https://github.com/awdawmip/enterprise-math/pull/2114). Preserve frozen science pins: Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.

Take `R=(2,10,15,20,25,30,38)`, source ports `(1,2,3,5)`, `x=X_(0,3)=X_(1,3)=155682221/25142124560000000`. The observer-kernel `H` changes masses on source 3 at targets 1,2,6 by `(-23,28,-5)`, and changes source 1 by the opposite vector. It satisfies `AH=0`, by both zero sum and R-weighted zero sum. Set `X(eta)=X+eta H` and keep `epsilon_max=9/115400000`.

The 1,144 fixed original interior phase values are `E0={36*x/k:k in K}`, where `K={-sum_{a in S}w_a:sum_{a in S}w_a <= -3}` for 15 integer weights

```
w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
```

The three moving resource thresholds are `t_q(eta)=(x-23eta)/q`, for `q in {15,12,3}`. All phase values are thresholds of first nonnegative-constraint zero along a **fixed labeled-prefix state**, not automatically changes in the number of complete legal orders.

## Theorem — second collision on both sides

After the known first collisions `eta_1^+=x/(23*541)` and `eta_1^-=-x/(23*539)`, the **next** collision between one moving `t_q` and a fixed element of `E0` occurs at the following exact parameters:

| Sign | Second collision eta | Equal phase epsilon | Coincident lines |
|---|---|---|---|
| positive | `eta_2^+=x/(23*433)=155682221/250390418493040000000` | `1401139989/2721634983620000000` | `t_12(eta_2^+)=36x/433` |
| negative | `eta_2^-=-x/(23*431)=-155682221/249233880763280000000` | `1401139989/2709063921340000000` | `t_12(eta_2^-)=36x/431` |

At **each** second-collision point the complete frozen 28-coordinate/15-atom model has exactly **1,146 distinct interior first-zero phase values**. In each open interval strictly between the first and second collisions on the corresponding side, the complete count is **1,147**. Both endpoint states are strictly positive and in the same observer fiber; the maximal nonnegative epsilon endpoint is still `9/115400000`.

At the newly merged phase, exact counts of labeled legal full permutations are:

| eta boundary | Newly zero prefix masks | Before | After | Lost |
|---|---:|---:|---:|---:|
| `eta_2^+` | **4,090** | 346,345,839,600 | 207,182,288,396 | **139,163,551,204** |
| `eta_2^-` | **4,092** | 344,940,950,320 | 205,570,222,828 | **139,370,727,492** |

The collision merges two neighboring order-count cuts, but the losses are different on the positive and negative sides. Using a rational parameter strictly before the second edge, the corresponding cuts decompose exactly as follows:

- **Positive:** the fixed `k=433` phase contributes **22** newly failing masks and **638,087,144** lost orders, followed by the moving `q=12` phase with **4,068** masks and **138,525,464,060** lost orders. The sum is 4,090 masks and 139,163,551,204 orders.
- **Negative:** the moving `q=12` phase comes first, contributing **4,065** masks and **138,461,493,728** lost orders; fixed `k=431` follows, with **27** masks and **909,233,764** lost orders. The sum is 4,092 masks and 139,370,727,492 orders.

The decomposition is **ordered** along these two-cut paths, not an assertion of independent causal additivity for arbitrary rearrangements.

## Proof of the second-collision ordering

Any equality `t_q(eta)=36x/k` solves to

```
eta = (x/23)*(1-36*q/k).
```

Enumerate the precise finite integer set `K` from the displayed fifteen integer weights. The two smallest positive collision ratios `eta/x`, among all `q in {15,12,3}` and all `k in K`, are `1/12443` (q=15,k=541) and `1/9959` (q=12,k=433). The two smallest negative absolute ratios are `1/12397` (q=15,k=539) and `1/9913` (q=12,k=431). In particular the second edge is mathematically different from the first.

The preceding exact finite minimizer-switch bound from [PR #2114](https://github.com/awdawmip/enterprise-math/pull/2114) is `|eta|=x/4945`, beyond both second edges. Hence the original affine first-zero-coordinate classification remains stable until the second edges; only the phase-value coincidences change. Direct complete 28-coordinate rational enumeration at each boundary and representative positions on both sides confirms the exact union `E0 ∪ {epsilon_max} ∪ {t_15,t_12,t_3}`, with 1,146 interior distinct values at each second edge and 1,147 between edges.

For the order counts, each labeled subset `S⊆{1,...,15}` determines a unique intermediate transfer `X(eta)+epsilon sum_(a in S)M_a`. Exact rational coordinate tests determine feasible subsets. The integer Boolean-lattice recurrence `ways(empty)=1`, `ways(S)=1_feasible(S)*sum_(a∈S)ways(S\\{a})` counts complete full schedules. At each phase the program selects an exact rational epsilon midpoint between neighboring phase values, giving the displayed before/after counts. Its finite domain is all 32,768 masks, all 28 masses and all 15 labeled operations, without floating-point approximations.

## Reproduction and next unit

Run `python3 VERIFY_SECOND_COLLISION.py` (standalone Python 3 standard library). It embeds the exact immutable original 28 rational masses and labeled move coefficients. Actual executed outputs are in `EXACT_OUTPUT.txt`. A separate locally executed same-input comparison `SIGNED_DECOMPOSITION_OUTPUT.txt` gives the neighboring-cut decomposition.

This is researcher-side exact finite evidence; formal task CLAIM, canonical Source Result, independent review and native-X6 transfer are separate. **Next:** classify the third signed collision `eta_3^+=2x/(23*542)=x/6233`, `eta_3^-=-2x/(23*538)=-x/6187`, and investigate whether the nearby affine minimizer switch at `|eta|=x/4945` introduces genuinely new first-zero coordinate families.
