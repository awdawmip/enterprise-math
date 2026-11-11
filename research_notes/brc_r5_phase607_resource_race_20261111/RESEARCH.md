# R5 phase 607: a three-atom compensator race explains the dominant order-count collapse

Date: 2026-11-11 Asia/Shanghai. Status: **exact researcher-side theorem plus executable rational finite certificate**, not a formal Source Result or independent mathematical review. The model is the *frozen P/Q–BRC Blackwell auxiliary transport observer*, not native X6.

## Exact input and provenance

- Global **scientific** pin: `a01383f825ef9d43b4b754254303298c64041568`; EM **scientific** pin: `86149263e38c22292c9def1e0f69092efa1be77e`.
- Original strictly positive state `X`, 15 *labeled* observer-kernel atoms, and maximal endpoint ray: immutable `435e77af0d180eac32bd1f9c4c464bc4010b7551` / Draft PR #2102.
- Complete 1,144 phase-transition census: immutable `666bdb981aa1abaf4643ff7742a48239f4086932` / Draft PR #2105.
- This work holds all 28 dynamic transport masses, labels, observer equations, atomic coefficients, and pins fixed; no task/claim or P000 change.

Write `M_(j,i)` for the 15 labeled atoms, ordered first by compensator `j=1,2,5`, then by `i=1,...,5`. For a subset `S` of these atoms, let `X_S(e)=X+e sum_(a in S) M_a`. A legal permutation is one for which **every** prefix subset has 28 nonnegative masses. Each atom preserves the exact observer.

## Theorem: explicit two-coordinate decomposition of the phase-607 jump

The 607th exact critical parameter is

```
epsilon_607 = 155682221 / 377131868400000000.
```

It lies strictly between the adjacent critical values

```
epsilon_606 = 1401139989 / 3400472346740000000
epsilon_608 = 1401139989 / 3387901284460000000.
```

Exactly **4,114** prefix subsets first reach the nonnegative boundary at `epsilon_607`. Of those, **4,096** are characterized by the single three-atom rule

```
(1,1) in S AND (2,1) in S AND (5,1) not in S.
```

Their *unique* zero coordinate at this critical parameter is `(target=1, source=3)`. The remaining **18** subsets have unique zero coordinate `(target=0, source=3)` and have exact bitmasks

```text
3152 3976 7380 7470 10800 11283 11608 15028 15511
15836 19640 19652 23581 24382 27300 27783 28108 30977
```

under the declared 15-bit atom ordering. None of these 18 belongs to the 4,096-mask three-atom family.

**Proof of the 4,096 pattern.** Let `x=X_(1,3)=155682221/25142124560000000`. The only three atoms affecting `(target=1,source=3)` change its mass by precisely

```
M_(1,1) : -12,     M_(2,1) : -3,     M_(5,1) : +15.
```

Thus `x=15 epsilon_607` and, at a parameter just above the critical value, this coordinate first goes negative exactly for a subset containing both negative atoms and lacking its compensating `+15` atom. The remaining 12 atoms are independent membership choices: `2^12=4096` subsets. The exact full-coordinate scan certifies that each of these subsets has no earlier first failure, and that all remaining first failures at this parameter are precisely the 18 masks given above. It also verifies the *unique* zero coordinate for each of the 4,114 subsets. This completes the classification for the frozen finite input.

A complete schedule therefore cannot place both `(1,1)` and `(2,1)` **before** `(5,1)` once the parameter exceeds `epsilon_607`: the positive compensating atom must arrive before at least one of the two consuming atoms. This is a **local compensator-resource race**, not a new constraint on all BRC systems.

## Exact attribution of the 380,759,849,184 lost legal orders

Let `N_606` count orders just below phase 607; let `N_race` be the count after filtering the new three-atom resource-race condition but **before** applying the 18 additional newly forbidden prefix masks; let `N_607` count orders just above phase 607. All previously forbidden prefixes (phases 1..606) remain forbidden in all three counts.

```
N_606   = 851,207,682,192
N_race  = 471,427,082,208
N_607   = 470,447,833,008

race-induced decrement, filtered first:  379,780,599,984
remaining decrement from 18 masks:          979,249,200
TOTAL phase-607 decrement:               380,759,849,184
```

The race accounts for exactly the rational share `379780599984/380759849184` of the phase loss (approximately 99.743%). This attribution is explicitly **sequential**—first rule out the resource-race prefixes, then the 18 exceptional prefixes—so it does not assign an artificial additive causal weight to overlapping forbidden-prefix events.

**Proof of schedule counts.** For a set `S` of atom labels define `w(S)=0` if `S` is forbidden under the selected cut, else `w(S)=sum_(a in S) w(S minus {a})`, with `w(empty)=1`. This integer Boolean-lattice recurrence counts each legal labeled permutation exactly once by its final atom. Phase 606 excludes precisely the masks whose first-zero rank is at most 606; the race-filtered count further excludes the 4,096 masks in the displayed family; phase 607 further excludes all masks of rank 607. The attached verifier computes all 32,768 subset first-zero ratios using exact rational comparisons, runs this recurrence for each of the three cuts, and **independently** recomputes `N_606` and `N_607` by direct coordinate nonnegativity at rational points on opposite sides of the breakpoint. All identities above pass.

## Reusable method and next scientific question

A high-multiplicity permutation-count transition need not have 4,114 independent algebraic causes: here a *single* three-atom resource race creates 4,096 simultaneous forbidden prefix states. The efficient BRC analysis retains atom labels and prefix order: first identify the coordinate's small set of nonzero contributions, then build the small compensator-race condition, and only then count the truly exceptional cuts using exact subset DP. This compresses the scientific explanation without discarding branch provenance.

Next, test a **general bottleneck-atom compression**: for each of the 1,144 interior R5 phase changes, find the smallest signed atom-support set whose resource inequality explains the new forbidden prefixes, and quantify exact residual exceptions plus order loss. Separately test whether this structure yields smaller order-search certificates for arbitrary strictly positive hidden-fiber endpoints. The model still has no established universal 15-step legal-connectivity theorem.

## Reproducibility and evidence scope

`VERIFY_DOMINANT_PHASE_607.py` is a stand-alone, Python-standard-library `Fraction`/integer checker with the immutable parent `X` and atom coefficients transcribed verbatim. It checks the 15 atom laws, endpoint-ray boundary, entire 32,768-mask rank classification, 4,096+18 split, all 18 mask IDs, three schedule counts and two direct-exact side checks. `LOCAL_EXACT_OUTPUT.txt` captures the executed local run. The program is not a physical native-X6 dynamics simulator, and a researcher-side proof has not yet received independent Source review.


## Theorem 2 — the *entire* 1,144-transition interior spectrum is one-dimensional

The dominance at phase 607 is an instance of a stronger exact finite result for this fixed frozen 15-atom ray.

Let `k=(target=0,source=3)`, let `x=X[k]=155682221/25142124560000000`, and integerize each labeled basic move by `w_a=36 M_a[k]`. In the same fixed 15-atom order as above, the resulting integer vector is

```text
(336,184,18,169,64, 84,299,126,52,16, -420,-483,-144,-221,-80).
```

It sums to zero and has subset-sum support `H={sum_(a in S) w_a : S subset of 15 atom labels}`. Exact finite integer set propagation establishes

```text
min H = -1348,  max H = 1348,  |H| = 2293;
H is symmetric: h in H iff -h in H;
|H intersect negative integers|=1146;
-1 and -2 are in H; |{h in H : h <= -3}| = 1144.
```

The maximal ray endpoint is `epsilon_max=9/115400000`. Since

```
36*x / epsilon_max = 89828641517/31427655700
                    strictly between 2 and 3,
```

the distinct zero-crossing parameters of coordinate `k` *inside the closed ray* are exactly

```
E_k = { -36*x/h : h in H, h <= -3 }.
```

There are exactly **1,144** such parameters and all are strictly interior. The completely independent 28-coordinate, 32,768-mask first-zero census of the frozen PR #2105 verifies

```
{all actual interior first-zero critical parameters} = E_k,
{all actual critical parameters on closed ray} = E_k union {epsilon_max}.
```

Thus **all 1,144 interior phase values can be generated by a one-coordinate integer subset-sum problem**. They do not require the other 27 coordinates for **generating their numerical candidate list** in this particular model. Full nonnegativity and schedule counts still use the original 28-coordinate legality test.

**Exact completeness and coordinate census.** For each of the **25,958** masks with a first-zero value in the ray, the full checker verifies all zero coordinates at its actual minimum ratio. Exactly **25,953** masks have one first-zero coordinate and **5** masks have two tied zero coordinates. The coordinate occurrences (counting both entries on a tie) are:

| First-zero coordinate | Mask occurrences |
|---|---:|
| `(target=0,source=3)` | **14,662** |
| `(target=1,source=3)` | **11,002** |
| `(target=0,source=2)` | **299** |

The last coordinate is responsible solely for the endpoint `epsilon_max`. Every interior phase has at least one mask first reaching zero at `(target=0,source=3)`. The `(target=1,source=3)` constraint contributes additional masks at **exactly three** resonant interior phases: **607, 715, 1039**, coinciding respectively with the three possible negative prefix sums `-15,-12,-3` at that coordinate. At phase 715 there are 4,082 newly failing masks (4,068 first-zero occurrences at target1/source3, 17 at target0/source3 and 3 double ties); at phase 1039 there are 2,856 (2,838 occurrences at target1/source3, 20 at target0/source3 and 2 double ties). Phase 607's 4,114 masks have no tie.

The verified order-count losses at these resonances are respectively

```text
phase 607: 380759849184
phase 715: 139228295864
phase 1039: 12963630596
```

with the three distinct exact phase parameters `x/15`, `x/12`, `x/3`. These are model-specific integer coincidences, and the finite proof consists of the explicit 15 weights, the 1D support propagation and the exact original full-fiber first-zero/chain-DP verification. **The one-dimensional threshold generator is a compression of phase-value discovery**, not a compression of all labeled-prefix feasibility or an arbitrary-input atom-distance solver.

**Reproducibility.** The small self-contained `VERIFY_ONE_DIMENSIONAL_SPECTRUM.py` was actually executed with Python `Fraction` and integer set propagation; `ONE_DIMENSIONAL_EXACT_OUTPUT.txt` captures its output. The enlarged `VERIFY_DOMINANT_PHASE_607.py` also checks equality with the prior exact full-coordinate phase list and all first-zero coordinate occurrences; its import-based published bytes remain pending independent clean-checkout execution. Both methods are provided to separate the cheap one-dimensional generator from the stronger full-fiber exhaustiveness evidence.

## Sharpened next problem

For a general finite BRC atom multiset, determine when the complete *critical-value set* is captured by one exposed coordinate. A discriminating first target is a necessary-and-sufficient condition phrased in terms of the signed subset-sum spectra and the minimum-of-coordinate first-zero operator, then calculate how often that condition occurs in nearby R5 atom decompositions. For order counts, continue preserving every prefix's complete state and branch provenance; evaluate whether one-coordinate generation lowers the cost of full phase enumeration without altering the certified counts.
