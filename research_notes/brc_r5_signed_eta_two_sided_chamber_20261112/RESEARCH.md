# R5 — Two-sided exact resonance-splitting chamber

Date: 2026-11-12 (Asia/Shanghai). **Researcher-side exact finite proof and executed rational computation.** Domain: the frozen *external* 28-mass P/Q–BRC Blackwell auxiliary observer, not native X6 dynamics. P000 and the ACTIVE worldview remain unchanged.

## Frozen provenance and problem

Scientific inputs stay pinned to GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. The rational positive 28-vector X, 15 labeled elementary observer-kernel moves M_a, and maximal ray endpoint eps_max=9/115400000 are reproduced from immutable source `435e77af0d180eac32bd1f9c4c464bc4010b7551` (R5 PR #2102); original 1,144 phase spectrum from `343ef84562909be87f520049893320d204fa9c4b`; single positive perturbation from `f545f3882b16c1b9d5bab60b5c6eb832b2debe36`.

With R=(2,10,15,20,25,30,38), fix H with components on source 3 at targets 1,2,6 equal to (-23,+28,-5), and opposite components on compensating source 1. The exact identities -23+28-5=0 and 10(-23)+15(28)+38(-5)=0 prove AH=0. Set

```
x = X[(0,3)] = X[(1,3)] = 155682221/25142124560000000
X(eta) = X + eta H
X_S(eta,eps) = X(eta) + eps * sum_{a in S} M_a
```

An order of all 15 labeled moves is legal when all its prefix states X_S are nonnegative in each of 28 coordinates. A *first-zero phase* is a distinct parameter eps in (0,eps_max] where at least one prefix first hits nonnegativity boundary; a *true order-count phase* decreases the number of complete legal orders across the parameter.

## Main exact theorem

Define the asymmetric rational interval

```
eta_left  = -x/(23*539) = -155682221/311686918170320000000
eta_right =  x/(23*541) =  155682221/312843455900080000000
```

**For every real eta in (eta_left,eta_right), X(eta) remains strictly positive, has unchanged complete observation AX(eta)=AX, and the positive-ray maximal nonnegative endpoint remains eps_max.** Define the integer subset-sum spectrum

```
w=(336,184,18,169,64,84,299,126,52,16,-420,-483,-144,-221,-80)
K = {-sum_{a in S} w_a: S subset of 15 labels, sum_{a in S} w_a <= -3}
E0 = {36*x/k: k in K},  |K|=1144.
```

The **complete** distinct first-zero phase set (including endpoint) is

```
E(eta) = E0 union {eps_max} union {(x-23*eta)/15,(x-23*eta)/12,(x-23*eta)/3}.
```

At eta=0, the three movable thresholds coincide with fixed E0 values for k=540,432,108; there are 1,144 distinct interior phases. For **every nonzero** eta in this entire open interval, the three movable phases are mutually distinct and distinct from E0: there are **1,147 distinct interior phases**. All three extra values are genuine drops in legal permutation counts. The count losses are constant in each of the two sign chambers, but **different between positive and negative eta**.

Thus the one-coordinate complete phase-value generator is an exact central-resonance feature, and both signs of an observer-invisible perturbation split it.

## Proof of uniform chamber, not just a numerical sample

1. H preserves all 15 observation rows; its perturbation does not change the 15 labeled M_a. Strict positivity of all 28 X(eta) and preservation of the maximal endpoint follow from exact coordinate inequalities. The least absolute admissible radius from initial/endpoint positivity in the H-affected coordinates is `155682221/578268864880000000`, larger than both interval endpoints. The unchanged zero endpoint coordinate (target 0, source 2) still enforces eps_max.

2. For each one of the **32,768** labeled subsets S, a negative-coordinate prefix direction has exact affine first-zero line
   `t_{S,k}(eta)=-(X_k+eta H_k)/(sum_{a in S} M_{a,k})`.
   The subset threshold is the minimum over these finitely many affine lines. All lines were constructed from the original 28 rational masses and 15 moves. Comparing each central minimizing line with every strictly nonminimizing line for every subset, the nearest nonzero minimizer switch has parameter `-155682221/124327805949200000000` (mask 14357, coordinates 15 and 14). Its absolute value exceeds both chamber endpoints. Ties at eta=0 are resolved by the sign of eta. All initial and endpoint sign changes are farther out; the fixed endpoint zeros are H-unaffected. Thus throughout this open chamber the 28-coordinate minimum classification changes only at the central ties, with no other active-coordinate invasion.

3. The target-0/source-3 coordinate is unaffected by H; its signed contributions, multiplied by 36, are precisely w. Exhaustive exact integer subset-sum propagation yields |K|=1144, and each E0 value has an active target-0 first-zero witness throughout the chamber. The only additionally active interior coordinate is target-1/source-3: its three possible negative prefix losses are -15,-12,-3, so it supplies exactly the displayed three affine phase values. Their actual attaining prefix subsets are certified by the full finite census. Endpoint source-2/target-0 remains constant.

4. The nearest K-neighbors of k0=36q for q=15,12,3 are (539,541), (431,433), (107,109) respectively. Solving `(x-23eta)/q=36x/k` gives `eta=(x/23)(1-36q/k)`. The closest negative and positive collisions are exactly eta_left and eta_right (both for q=15). Therefore no other coincidence occurs for a nonzero eta in the interval.

5. For every eps the exact number of complete labeled orders is obtained from `ways(empty)=1`, `ways(S)=0` when S is infeasible, otherwise `ways(S)=sum_{a in S}ways(S\{a})`. With all first-zero lines and their order fixed within each sign chamber, the forbidden-prefix families immediately before and after each of the three movable thresholds are constant throughout that chamber. One exact rational sample of each sign, together with the finite chamber proof, therefore proves each **real-parameter** order-count loss, not merely the sampled values.

## Exhaustive exact results

Executable source: `VERIFY_R5_SIGNED_ETA.py.gz.b64` (lossless gzip/base64, decoded Python SHA-256 `2124ad7535e7c741b1b738b8dbeedb7742191b6565a46fcc8e7b46442930c063`); actual captured run: `EXACT_OUTPUT.txt`. Reconstruct with `base64 -d VERIFY_R5_SIGNED_ETA.py.gz.b64 | gzip -d > VERIFY_R5_SIGNED_ETA.py` then `python3 VERIFY_R5_SIGNED_ETA.py`. Python 3 standard-library `Fraction` and exact integer Boolean-lattice DP only. No floating-point tolerance.

Representative exact points `eta=+x/1000000` and `eta=-x/1000000`, both strictly inside the proven interval:

| eta sign | denominator q | newly failing prefix subsets | complete legal orders before | after | drop |
|---|---:|---:|---:|---:|---:|
| positive | 15 | 4096 | 851207682192 | 471427082208 | **379780599984** |
| positive | 12 | 4068 | 345707752456 | 207182288396 | **138525464060** |
| positive | 3 | 2838 | 24238509972 | 11322118044 | **12916391928** |
| negative | 15 | 4096 | 850075412400 | 470447833008 | **379627579392** |
| negative | 12 | 4065 | 344940950320 | 206479456592 | **138461493728** |
| negative | 3 | 2836 | 24166351272 | 11274879376 | **12891471896** |

The negative-eta rows and exact two-sided interval are the new science in this unit. Positive numbers reproduce the prior author-side result. Local output contains exact thresholds, neighbor collision fractions, minimizer-switch bound, and all counts. The remote published source has not yet been independently executed by a separate environment.

**Scope:** complete finite certificate for the frozen auxiliary observer and its 15 labeled moves; researcher-side mathematical proof, not independent review, native X6 transfer, Source Result admission, or a uniform 15-step connectivity theorem.

**Next discriminating unit:** at each boundary eta_left and eta_right, decide whether its newly coincident phase values merely merge as numbers or also merge/lift full-prefix feasibility/order-count jumps. Continue the affine line and Boolean-lattice analysis beyond the first collision without repinning frozen science.