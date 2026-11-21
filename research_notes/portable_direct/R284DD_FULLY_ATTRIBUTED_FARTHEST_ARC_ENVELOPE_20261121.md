# R284DD — Exact two-slope farthest-arc envelope with full winning-label provenance

Date: 2026-11-21 (Asia/Shanghai)  
Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**  
Scope: general finite integer circular-arc families; census and implementation verified on frozen R284CO Port observer.

## Question and contribution

R284DA proved that a two-slope event envelope calculates the farthest distance D from an integer site to all 64 frozen labeled residual arcs without computing 64 separate distances. R284DC then recovered the 307 equal-D source-neighbor edges from 420 within-fiber pairs, but looked up 64 arc distances for 612 distinct incident sites to reproduce the exact winner-label provenance.

This result removes that final labeling computation from the **construction algorithm**: the two-slope event envelope can carry the original arc label through the maximization, and thus return `(D(x),argmax_i d_i(x))` exactly for every site in one event-index lookup.

## Theorem — attributed finite circular-arc envelope

Let P be a positive integer, `A_i=[a_i,a_i+w_i]` a finite nonempty family of positively oriented labeled integer arcs with `0<w_i<P` and starts reduced to `0<=a_i<P`. Distance `d_i(x)` is the circular nearest-point distance to arc i at integer site `0<=x<P`, and `D(x)=max_i d_i(x)`.

R284DA associates each arc to at most four clipped half-open affine branch segments on the interval `[0,P)`, using the right-end distance branch `x-b` with key `(+1,-b,i)`, or the left-start distance branch `e-x` with key `(-1,e,i)`; `b=a_i+w_i+kP`, `e=a_i+(k+1)P`, `k∈{-1,0}`, with the integer midpoint split `floor((b+e)/2)`.

On each elementary event slab `[t_j,t_{j+1})`, the active branch-key set is fixed. For each slope s=+1 or -1, select the **maximal intercept** `C_s` among active keys with that slope, together with the complete set `L_s` of arc labels attaining `C_s`. These are independent of the site x within the slab.

For each site x in the slab, calculate

```text
D(x) = max(0, x+C_+ if present, C_- - x if present).
```

If `D(x)>0`, the complete maximizing-arc label set is exactly the union of the labels in `L_+` for which `x+C_+=D(x)`, and the labels in `L_-` for which `C_- - x=D(x)`. If `D(x)=0`, *every* arc has distance zero, so `argmax_i d_i(x)` is all labels.

**Proof.** At site x every positive distance to an arc is represented by its unique active lifted affine branch, with the appropriate arc label, and every absent positive branch corresponds to an arc with distance zero. Within a given slope class, the branch with maximal intercept has maximal value simultaneously for all x in the slab, and exactly the intercept ties attain that slope-class maximum. Taking the maximum across the two slope classes and zero therefore returns the exact distance. Whenever this maximum is positive, all winners must be in maximal-intercept branches of one or both slope classes; equality tests identify them exactly. For maximum zero, every nonnegative arc distance is zero. No label is discarded or inferred from the distance value alone.

The representation stores O(m) branch segments and at most O(m) distinct event slabs for m input arcs; the at-most-O(m) labels in a maximal intercept tie are output-sensitive. A balanced-event preprocessing implementation takes O(m log m) plus any necessary argmax tie output storage, while the supplied simple standard-library reference scans active branches at each event and uses O(m²) preprocessing. For each site, event predecessor lookup takes O(log m); the numerical value requires O(1) arithmetic, with additional time proportional to the returned winner labels. Source words must first be generated from the actual original matrix input; this is not excluded from end-to-end cost.

## Frozen Port exact verification

Using the unchanged frozen `R284CO_spectral_witness_checker.py` and its SHA-256 `b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4` (modulus 17,179,869,143; 65,536 codewords; 64 arcs), the attributed envelope has **194 event positions** and **193 slabs**.

At all 65,536 sites the maximizing arc is unique, and the new algorithm's complete `(D(x), winning arc label)` pair equals an independently evaluated **4,194,304-distance** brute-force baseline. Grouping those 65,536 D values into exact-value fibers produces 420 candidate pairs, from which the original source-adjacency predicate recovers the identical 307 source-mutation equality edges. The complete list, in the original matrix order, including winning arc labels, has SHA-256

```
251a3ca8d2d72cf6f7ca19869f174eb9e370f330533e484faf13dcb2a68dab8b
```

matching independent R284CZ, R284DA, R284DB and R284DC certificates.

**Cost distinction:** Within the new attributed-envelope + fiber-join *construction*, the number of direct `dist(x,A_i)` evaluations for D **and** for winner labels is **zero**. Its separate exhaustive validation program deliberately performs the full 4,194,304 comparisons. Source determinant generation, attributed envelope preprocessing, 65,536 binary event predecessor searches, bucket construction, 420 exact source-adjacency tests and 307-record materialization remain. Therefore the result eliminates a class of operations; no measured universal end-to-end speedup is claimed.

## Program and persistence

Reproduce using `R284DD_attributed_envelope_checker.py`; deterministic summary `R284DD_attributed_envelope_certificate.json`, both in this directory. The checker preserves exact original source-matrix index orientation, follows the frozen numeric source, checks unique winners explicitly and verifies the previous canonical edge digest. No external mathematical library, floating arithmetic or formal proof assistant is used.

Frozen source pin: `awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py`, Git blob `b46e0f682b58e47c27094b4bea6fa4e55119a3ee`. Current project protocol, P000 and ACTIVE world assumptions govern research interpretation; this is a finite Port auxiliary observation result, not an X6 dynamic theorem or mathematical promotion. Independent review remains `NOT_REVIEWED`.

## Next research unit

The remaining dominant construction is the full 65,536-codeword determinant evaluation and event lookup. An intrinsically algebraic next step is to intersect the signed endpoint-translation families of R284DB with the exact determinant update for lower-bit flips and unequal-entry swaps, to generate candidate pairs before evaluating all source codewords. Test total operation counts, including matrix-to-codeword transformation, sorting/preprocessing, candidate verification and original-index/arc provenance. Do not discard residual identity merely because two observations agree.

Source artifacts are independently preserved GitHub research notes. Historical attribution `EM-DIRECT-20B766` / `RA-617F40704F37299B15489DCA` remains unchanged; any new Activity checkpoint must be attached by an actually authenticated original session with Source CAS and scoped observation readbacks. No formal Task CLAIM/Result/Review actions were taken.
