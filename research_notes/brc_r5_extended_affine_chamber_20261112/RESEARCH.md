# R5 — sharp signed affine-prefix chambers and 12 exact phase-collision parameters

Date: 2026-11-12 (Asia/Shanghai). **Evidence:** researcher-side exact rational finite theorem, reproduced against locally transcribed frozen inputs; native Source Result and independent mathematical review pending. This is the external P/Q–BRC Blackwell auxiliary observer, not a native X6 dynamics claim.

## Scientific pins and unchanged model

Global frozen science `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math frozen science `86149263e38c22292c9def1e0f69092efa1be77e`. The rational 28-component strictly positive `X`, 15 labeled elementary observer-kernel moves `M_a`, operator `A`, and full-ray endpoint were fixed in [R5 PR #2102, commit 435e77a](https://github.com/awdawmip/enterprise-math/commit/435e77af0d180eac32bd1f9c4c464bc4010b7551). [PR #2120, commit b61c394](https://github.com/awdawmip/enterprise-math/commit/b61c394ef2844899eb7bd3279442b12d4c80efa2) proves a two-sided uniform result for `|eta| <= x/100000`.

Let `R=(2,10,15,20,25,30,38)`, `x=155682221/25142124560000000` and `epsilon_max=9/115400000`. Keep `H` equal to the six-arc residual with source 3 changes `(-23,+28,-5)` at targets `(1,2,6)`, opposite changes at source 1, and zero elsewhere. Thus `AH=0`. Consider `X(eta)=X+eta H` for rational `eta`.

For each nonempty subset `S` of the 15 labeled moves, put `P_S=36 sum_(a in S) M_a` (integer), and its first-zero time
```
tau_S(eta)=min_(k:P_S[k]<0) 36*(X[k]+eta*H[k])/(-P_S[k]).
```
Let `E(eta)` be the **distinct** subset first-zero times in `(0,epsilon_max]`. As previously proved, the fixed-coordinate support is `N={n>=3: n=-sum_(a in S) w_a for some S}`, `|N|=1144`, with
```
w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80).
```

## Theorem A: exact maximal one-sided affine-prefix minimizer domains

For **every rational**
```
-x/4945 <= eta <= x/2507,
```
the complete first-zero spectrum is
```
E(eta) = {36*x/n : n in N} union {epsilon_max}
         union {(x-23*eta)/q : q in {3,12,15}},
```
where the right side is an ordinary set (coincident values counted once). For eta=0 it has 1145 distinct values, consistent with [R5 PR #2120](https://github.com/awdawmip/enterprise-math/pull/2120). For sufficiently small nonzero eta without collisions it has 1148 values (1147 interior plus the endpoint). The initial state is strictly positive throughout this closed interval, `A X(eta)=A X`, and `epsilon_max` remains the exact terminal feasible-ray endpoint. Its unique zero mass at the endpoint is `(target=0, source=2)`.

For each nonempty subset, choose the active minimum affine function at eta=0, breaking an initial tie by **smallest slope** for eta positive and **largest slope** for eta negative. Every such selected affine function continues to attain the prefix minimum throughout `[0,x/2507]` or `[-x/4945,0]`, respectively. These two bounds are *sharp for this specified fixed-affine-minimizer representation*: beyond either endpoint, a competing coordinate becomes strictly smaller. Witnesses (15-bit labeled atom mask, active coordinate before the switch, new competing coordinate) are
```
positive: eta=x/2507,  mask=11236,  (0,3) -> (1,3)
negative: eta=-x/4945, mask=14357,  (1,3) -> (0,3).
```
Here coordinate order is `(target,source)`.

This extends the previous rigorously certified perturbation magnitude `x/100000` to two different sharp affine-prefix bounds. The set identity can be used even at phase collisions because a set union incorporates coincidences exactly.

## Theorem B: complete phase collisions inside the affine-prefix domains

Each moving threshold `(x-23 eta)/q` coincides with a fixed threshold `36x/n` precisely at
```
eta/x=(n-36q)/(23n),  q in {3,12,15}, n in N.
```
There are exactly **eight distinct positive collision parameters** at or below `x/2507`, and **four distinct negative collision parameters** at or above `-x/4945`.

| sign | signed eta / x | coincident (q,n) pairs |
|---|---|---|
| + | 1/12443 | (15,541) |
| + | 1/9959 | (12,433) |
| + | 1/6233 | (15,542) |
| + | 1/4991 | (12,434) |
| + | 1/4163 | (15,543) |
| + | 1/3335 | (12,435) |
| + | 1/3128 | (15,544) |
| + | 1/2507 | (3,109), (12,436), (15,545) |
| − | -1/12397 | (15,539) |
| − | -1/9913 | (12,431) |
| − | -1/6187 | (15,538) |
| − | -1/4945 | (12,430) |

The three moving functions do not intersect one another in this parameter interval: equality between distinct denominators would require `x-23 eta=0`, outside it. They do not hit `epsilon_max` in this range. Thus the table is complete, not a sampled set of collisions.

In particular, the **maximal one-sided open perturbation intervals next to 0 on which all 1147 interior values are distinct and keep the same relative order** are
```
 -x/12397 < eta < 0,       0 < eta < x/12443.
```
Within these intervals the exact previous per-phase lost-schedule counts of PR #2120 remain applicable, since the 15-bit first-zero affine winners and relative order of their thresholds stay unchanged. At the first positive or negative endpoint, the appropriate moving/fixed pair coincides; the ordered simple-phase chamber therefore genuinely ends. The total first-zero spectrum remains covered by Theorem A beyond this first collision until the sharper prefix-minimizer bound.

## Proof and exact certificate

With `P_S` integral, each candidate `T_(S,k)(eta)=a_(S,k)+b_(S,k) eta` is a rational affine function. At zero, select a tied minimizer with the sign-appropriate extremal slope. If another candidate has a more competitive slope, their first possible crossing is
```
eta=(a_competitor-a_selected)/(b_selected-b_competitor).
```
Exhaustive scanning of the **32,767 nonempty subsets** finds **303,057 negative-coordinate candidates** and **five** subsets with multiple minimizers at zero. The smallest strictly positive crossing across all selected-vs-competitor comparisons is `x/2507`, attained by mask 11236; the smallest negative absolute crossing is `x/4945`, attained by mask 14357. Every difference is affine, so checking all potential crossings proves the full closed intervals, including all rational interior parameters. No selected threshold crosses `epsilon_max` before these limits.

For the state itself, `X(eta)` and each full-ray endpoint `X(eta)+epsilon_max sum M_a` depend affinely on eta. Exact checks at `eta=-x/4945,0,x/2507` establish initial strict positivity, full-ray terminal nonnegativity and the sole terminal zero `(0,2)`; interpolation gives the whole interval. The endpoint zero and negative full-ray velocity at that same coordinate establish the exact maximal endpoint.

The complete **sign-dependent affine-form sets** for all subset minima equal
```
{(36x/n,0):n in N}
 union {(x/q,-23/q): q=3,12,15}
 union {(epsilon_max,0)}.
```
There are exactly 1148 distinct affine forms for either sign; direct rational-set comparisons prove equality, not just numerical agreement at sample values.

Enumerating the collision equation over the exact integer support `N` proves the table. All listed `n` occur in `N`; all other integers either lie outside the sharp affine-prefix bounds or are absent from `N`. This verifies the first ordered-phase boundaries and the 12 distinct signed parameter values.

## Reproduction and evidence status

- `VERIFY_EXTENDED_CHAMBER.py.gz.b64`: lossless gzip/base64 of Python-stdlib `Fraction` verifier. Decode with `base64 -d VERIFY_EXTENDED_CHAMBER.py.gz.b64 | gzip -d > VERIFY_EXTENDED_CHAMBER.py`. Run it from any directory; it imports the exact prior `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py` on the same stacked PR branch and independently checks the current theorem.
- Decoded script SHA-256: `a1073f29bcabef769960ad3ce85f83edc48d6865d1f20b7ce886e7a4938e57cc`.
- `EXACT_OUTPUT.txt`: actual successful execution of the **same verifier algorithm** using `--local-fixture`, which supplies the original rational X and 15 atom coefficients transcribed in a local independently maintained fixture. The remote published script's ordinary parent-import route has not yet been independently rerun from a clean checkout. Every reported comparison and count uses exact integers/rational numbers.

This publication is a new finite-structure theorem on the existing external auxiliary observer. It does not change P000, task ownership, or the claimed status of native X6 mathematics.

## Next discriminating problem

Within `-x/4945 <= eta <= x/2507`, compute the exact legal-permutation count drop across the first **ten interior collision parameters**, including which former fixed-vs-moving losses exchange magnitude. Separately determine the next affine-minimizer regimes beyond the sharp witness boundaries; use the same prefix finite-affine envelope algorithm rather than rerunning an unstructured 15! enumeration.
