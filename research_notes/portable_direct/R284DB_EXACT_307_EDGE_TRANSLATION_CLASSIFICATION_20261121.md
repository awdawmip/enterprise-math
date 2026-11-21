# R284DB — Exact affine translation classification of all 307 Port source-neighbor equality edges

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scope: unchanged R284CO frozen 34-bit Port auxiliary observer and R284CZ one-flip/unequal-swap source-neighbor graph.

## New structural proposition

For a circular arc `(a,w)` on modulus P, choose the relevant unwrapped complement lift `b=a+w+kP`, `e=a+(k+1)P`. On its right-end distance branch the function is `d(x)=x-b` (slope +1); on its left-start branch it is `d(x)=e-x` (slope -1). R284DA proves that the farthest-arc observer `D(x)=max_{i=0}^{63}d_i(x)` can be evaluated exactly by a two-slope event envelope.

**Affine equality lemma.** If the maximizing arcs at sites x and y have the same slope s in {+1,-1}, and their lifted affine intercepts are c_x,c_y, then

```text
D(x)=D(y)   iff   y-x=(c_x-c_y)/s.
```

Equivalently, for the +1 branch the codeword shift equals the difference of the corresponding *lifted right endpoints*, `y-x=b_y-b_x`; for the -1 branch it equals the difference of the *lifted left endpoints*, `y-x=e_y-e_x`. If the winning slopes differ, an equality instead obeys a distinct sum equation, and the same-slope translation implication does not apply.

*Proof.* Substitute `D(x)=s*x+c_x`, `D(y)=s*y+c_y` and solve the exact integer equality. The branch formula is the R284DA half-open complement decomposition; no approximation or division other than by `s=±1` occurs.

## Frozen exact classification

Exhaust the original 1,474,560 undirected lower single-flip and unequal-entry swap edges, retain those satisfying exact `D(x)=D(y)`, and for the distinct endpoints of those edges independently determine the unique winning arc and active slope from integer distances. The resulting **307** equal-distance edges have:

| Invariant | Exact value |
|---|---:|
| Different original source-neighbor edges with equal D | 307 |
| Distinct incident codewords | 612 |
| Same winning slope, +1 at both endpoints | **145** |
| Same winning slope, -1 at both endpoints | **162** |
| Opposite winning slopes | **0** |
| Same winning arc label | **0** |
| Winning endpoint with a branch-midpoint tie | **0** |
| Distinct unordered winning arc-label pairs | **30** |
| Distinct (unordered label-pair, slope) classes | **35** |
| Distinct signed integer source shifts across those classes | **28** |
| Classes containing more than one distinct shift | **0** |

Consequently, every one of the R284CZ 307 equality edges is an **exact lifted endpoint translation**, with the correct sign depending on whether the active distance branch is right-end or left-start. The 35 class-specific translations are in `R284DB_translation_classes_certificate.json`; all class edge counts sum to 307.

Some largest classes (unoriented arc labels, exact original-source orientation `y-x`):

| Arc label pair | Winning slope | Edge count | Exact signed source shift |
|---|---:|---:|---:|
| 49, 57 | +1 | 32 | -3,725,499,553 |
| 48, 56 | +1 | 30 | -3,725,499,553 |
| 7, 15 | -1 | 26 | +9,728,870,037 |
| 0, 8 | -1 | 24 | +13,451,347,648 |
| 1, 9 | -1 | 20 | +13,451,347,648 |
| 18, 19 | +1 | 6 | -6,669,045,998 |
| 21, 37 | -1 | 1 | -4,503,221,351 |

The last two rows contain, respectively, the A-type and B-type exceptional translation mechanisms already identified in R284CX, and the complete 35-class atlas also covers the 303 source-neighbor equalities that are absorbed by other-level forced inclusion.

## Exact reproducibility and limits

The standard-library program `R284DB_translation_classes_checker.py` imports the unmodified R284CO generator and the newly verified R284DA envelope. It generates all 65,536 frozen codewords (SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4`), visits the exact original source-neighbor edges, and derives winning arc labels and slopes for all 612 distinct equality-edge endpoints. It checks each affine shift equation, 35 class memberships, their one-shift property, and the previous R284CZ canonical 307-edge digest:

`251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b`.

The local run passed. This is exhaustive for the frozen 307 equality-edge set, not a theorem about all possible Port site pairs nor about full native X6 dynamics. An independent mathematical review has not occurred. Existing all-level forced-rank conclusions rely on R284CW and are not modified here.

## Research continuation

Next construct candidate source edges by equating source-determinant position changes to the **28 signed lifted endpoint shifts** and checking the 35 arc-label/slope regimes before graph enumeration. Investigate whether this yields an exact constructive generator of all 307 equality edges, with a provable reduction in search cost once determinant evaluation, interval tests and source-index recovery are accounted for. Preserve source-index orientation and the original `tau`-based distinction between four unforced and 303 absorbed edges.

Source persistence is an independent portable research checkpoint; no shared Task CLAIM or new Result/Review authority is asserted. Historical attribution is `EM-DIRECT-20B766`, Activity `RA-617F40704F37299B15489DCA`; the new source-to-Activity semantic association remains a separate authorized write.
