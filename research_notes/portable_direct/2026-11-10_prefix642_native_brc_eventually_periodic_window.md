# PREFIX-642 — Exact eventually-periodic rolling BRC moment queries across a finite transient

**Date:** 2026-11-10 (Asia/Shanghai). **Status:** AUTHOR_SIDE / algebraically proved + 180 original-action exact checks / UNREVIEWED.
**Frozen observer science:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
**Related:** PREFIX-640 integer six-jet transfer, PREFIX-641 periodic transfer (Draft PR #1948), general-gate end-to-end predecessor (Draft PR #1944).
**Native target:** original 48 STAR phases / 96 labelled ports / 576 original weighted BRC actions, 7-state Aho–Corasick automaton over original action IDs, motifs `(485,316,52,174)` and `(52,174)`, and six original-path moment coordinates `(Z,U0,U1,V00,V01,V11)`.

## Theorem — eventually-periodic six-jet rolling query

Let the native BRC gate sequence be arbitrary nonnegative rationals up to a finite startup length `h>=0`, followed by an exactly `p>=1` periodic tail. Thus `g_(h+j+p)=g_(h+j)`. Let `L>=1` be a fixed window length, and `W>=1` the number of successive window queries at times `0,...,W-1`. Associate each original labelled-action BRC/AC gate step with its exact chronological six-jet transfer `T_i`. With `M(t,L)=T_t ⋆...⋆T_(t+L-1)` and the exact time-`t` 96-port source vector, all six rational moment outputs for every window can be calculated in

`O(h + p^2 + p log(1+L) + W)`

**six-jet matrix compositions**, plus `O(W)` original BRC source updates and a constant number of vector/operator contractions per query. This count assumes access to the compact preperiod plus one period and fixed original frozen 672-state automaton. The original exact rational output is calculated with integer numerator jets and one final denominator normalization. The theorem includes zero gates and overlapping motif matches.

For the frozen two-pattern observer, previous exact finite support certificates bound each full transfer by 4,284 nonzero matrix positions and each pairwise composition by 10,500 candidate pair joins. Integer numerator/denominator bit length is charged separately and grows with input gate sizes, source time and query length. A raw noncompressed gate stream requires scanning to certify the period promise. No physical-timing or general native spatial-rotation inference is asserted by this observer calculation.

## Constructive proof

Write the transient transfers as `U=(T_0,...,T_(h-1))`, followed by periodic transfers `S_j=T_(h+j)`, with `S_(j+p)=S_j`. They are full BRC/AC six-jet transfers, preserving the action ID and AC state through all chronological compositions.

**Pre-boundary windows (`t+L<=h`).** Maintain a chronological two-stack matrix-product queue over transient steps in the window. Its two ordered aggregate products represent the same native path transfer as explicitly concatenating all original actions. Across at most `h` transient steps, each is pushed or popped a bounded number of times, so all such queue updates together require `O(h)` compositions.

**Boundary-crossing windows (`t<h<t+L`).** The transient queue holds precisely the time interval `[t,h)`; define `k=t+L-h>0` and `V_k=S_0 ⋆ ... ⋆ S_(k-1)`. The full chronological window transfer is queue product followed by `V_k`. Initialize `V_k` from the exact period block-power theorem `(S_0 ⋆ ... ⋆ S_(p-1))^floor(k/p)` times the first `k mod p` steps, using `O(p+log(1+k))` compositions. On each successive crossing window, increment `k` by one and use the exact update `V_(k+1)=V_k ⋆ S_k`. Pop one transient queue step whenever the left boundary advances. For each query, apply the AC-root-embedded source vector first through the queue's one or two aggregate blocks and then through `V_k`; this uses at most three sparse vector contractions and avoids an additional costly full boundary matrix-matrix product. Every labelled BRC path and match crossing the boundary is preserved because the intermediate AC state is retained.

**Post-boundary windows (`t>=h`).** Let `r=(t-h) mod p`, `q=floor(L/p)`, `s=L mod p`. Define full rotated period `Q_r=S_r ⋆ ... ⋆ S_(r+p-1)` and remainder `R_(r,s)=S_r ⋆ ... ⋆ S_(r+s-1)`, periodic indexes mod `p`. Then `M(t,L)=Q_r^q ⋆ R_(r,s)`. Memoize at most `p` phase-class transfers; each phase requires at most `O(p+log(1+L))` matrix compositions, totalling `O(p^2+p log(1+L))`. Apply each resulting operator to the actual advanced native source vector, with AC matching reset to root at the beginning of the queried window.

The BRC six-jet multiplication is associative: concatenation of two labelled path families has exactly the summed zero/first/second raw moments of their concatenated motif counts, including shared motif prefixes across the join. By original-action BRC definition, every complete path belongs to exactly one such concatenation, with correct positive weight multiplication. The integer numerator/common denominator representation is an exact rescaling of this semigroup. These identities prove all moment outputs and the composition bound. QED.

## Executed exact original-action certificate

Program `PREFIX642_eventually_periodic_window.py`, with `PREFIX641_native_rolling_end_to_end.py`, `PREFIX640_fraction_free_rolling_jet.py` and original typed `PREFIX638/PREFIX638_native_jet_support.py`, executed in Python with exact integers and fractions. Every strategy window is independently compared to `native.oracle`, which evaluates **original BRC actions** in chronological order and returns the full six-field exact rational tuple.

The completed run reports **15 workloads and 180 exact six-field comparisons, all assertions passing**. It tested period 1/all-ones, period 3/positive rational values `(1,2/3,5/4)`, period 4/zero-containing `(1,0,3/2,5/3)`, and transient lengths 0,3,8,12 relative to L=8, plus longer L=32. Cases span preperiod, boundary and wholly periodic windows. There were no trigonometric, π, Taylor or ordinary matrix-exponential reference computations.

Single-run example, with preprocessing + native source updates + query contractions included (times seconds):

| Gate family | h | L | W | Matrix compositions | New method | Original native BRC DP |
|---|---:|---:|---:|---:|---:|---:|
| all-one (p=1) | 0 | 8 | 10 | 3 | 0.135223 | 0.263333 |
| all-one (p=1) | 3 | 32 | 16 | 19 | 0.326601 | 3.070105 |
| rational (p=3) | 3 | 32 | 16 | 39 | 0.624581 | 1.282896 |
| contains zero (p=4) | 3 | 32 | 16 | 39 | 0.446357 | 1.190765 |
| all-one (p=1) | 8 | 8 | 11 | 24 | 0.713969 | 0.281846 |

The strategy duration is the measured whole-case time minus separately instrumented original-action DP oracle duration, both running serially in the same process and excluding the same shared four-step native source initialization. Timings are observations of one runtime, not statistics or universal machine-bit speedups. Direct DP is faster for some short/transient-heavy workloads.

The accompanying `PREFIX642_evidence.tar.gz.b64` is an ASCII-base64 lossless archive of this paper, executable source, the full 15-case original JSON, run log, dependent exact native source code, and SHA256 manifest; decoding is `base64 -d PREFIX642_evidence.tar.gz.b64 | tar xzf -`. Exact raw JSON SHA256: `b3525f487c2d4fdb447c11622b8443d1895f2d57f282e3069babb46f916d8814`. Repeat the full script to obtain `ALL_ASSERTIONS_PASS`. No credentials are part of these research materials.

## Research significance and open unit

The result proves a complete special-family operator law for the **original positive-weight, labelled-path BRC/AC moment observer**. Distinct path identities are retained by the original transfer during evaluation; the six returned moments intentionally aggregate only the declared observer, and arbitrary path enumeration remains on the provenance-preserving DAG. The formal mother task remains signed arbitrary-triad C6 and actual Cell-path physical rotation dynamics: author-side observer work supplies no formal CLAIM or Foundation theorem admission.

**Next discriminating experiment:** replace the transient two-stack full 672-product-state matrices by a *reachable-row factored BRC representation* for this frozen four-point probe, prove six-moment equivalence under queue/period joins, and measure integer bit operations, memory, and crossover as `h,L,W` grow.
