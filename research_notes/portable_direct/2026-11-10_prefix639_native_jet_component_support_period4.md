# PREFIX-639 — Exact eventual four-periodicity of six-component native BRC jet support

**Date:** 2026-11-10. **Status:** author-side finite-state theorem and executed exact certificate; independent mathematical review pending. **Frozen science:** `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Lineage:** PREFIX-635–638, especially the original 48-phase, 96-port, 576-labelled-action native BRC enumerator and seven-state Aho–Corasick monitor for `P0=(485,316,52,174)`, `P1=(52,174)`.

## Precise statement

For each nonnegative-rational gate sequence `(g1,...,gk)`, let `T_k` be the corresponding `672 × 672` native transfer, with coefficients in the six-coordinate second-order exponential jet `J=(Z,U0,U1,V00,V01,V11)` of nonnegative rational numbers. Every entry is a sum of weights of original labelled paths conditioned on its **joint port and automaton endpoints**; first and second raw occurrence-count moments remain distinguished. Define `sigma(T)` as the matrix of six-bit masks of coordinatewise strict positivity. Let `C_k` denote this exact mask for all-one gate sequences of length `k`.

**Theorem (within this frozen positive-weight native observer).**

1. The entrywise **six-component masks** satisfy `C_10 = C_14`. Thus for every integer `k >= 10`, `C_(k+4) = C_k`. For every `1 <= k <= 9`, `C_(k+4) != C_k`; ten is the first exact four-periodic point.
2. For `k >= 10`, every nonzero transfer entry has mask either binary `000001` (mass alone) or `111111` (all six components). For even `k` there are 3,024 mass-only entries and 1,260 all-six entries; for odd `k` there are 2,128 mass-only entries and 1,260 all-six entries.
3. For **all** lengths `k >= 1` and **all nonnegative rational gates**, there are at most 4,284 matrix positions with positive mass, at most 1,260 positive positions in **each** of the five higher moments, and at most **10,584 positive scalar coordinates** across the whole transfer. Each bound is attained by an all-one positive-gate sequence (possibly at different lengths). The scalar-coordinate bound is sharp at every even `k >= 10`.
4. At every `k >= 10` with all gates positive, for each fixed pair of original joint source/target states, existence of a nonzero-weight labelled path with a `P1` match is equivalent to existence of a (possibly different) nonzero-weight labelled path with a `P0` match. This is a **fixed-endpoint existential statement**: occurrence counts and weighted values are not asserted equal, and the two witnesses need not be the same path.

**Storage consequence.** If a transfer is stored coefficientwise rather than as six slots for every nonzero entry, the fixed observer needs at most 10,584 nonzero scalar values, instead of `6 × 4,284 = 25,704` slots in a fully populated six-tuple representation of the maximal positive-support matrix. The reduction concerns the number of stored coefficient *slots*, not the exact integer bit complexity or Python object overhead.

## Proof

The one-step original 576-action enumerator assigns nonnegative rational weight to each tagged action. For every original action and every automaton state, advancing the Aho–Corasick state has a deterministic hit mask `h=(h0,h1) in {0,1}²`. The edge jet is `w × (1,h0,h1,h0²,h0 h1,h1²)`. Jet multiplication is induced by addition of occurrence counts along concatenated original labelled paths:

```
Z''   = Z Z'
U0''  = U0 Z' + Z U0'
U1''  = U1 Z' + Z U1'
V00'' = V00 Z' + 2 U0 U0' + Z V00'
V01'' = V01 Z' + U0 U1' + U1 U0' + Z V01'
V11'' = V11 Z' + 2 U1 U1' + Z V11'
```

Every coefficient and structure constant is nonnegative. Coordinatewise positivity is therefore preserved exactly by taking Boolean OR for sum, AND for product; the `2` in the diagonal second-moment terms remains positive and does not alter support. In particular the map from positive jets to six-bit positivity masks is a semiring homomorphism on this nonnegative cone, including zero gates.

Build `A=C_1` from the *original* enumerated actions and AC transitions. Let `⊙` be semiring matrix multiplication in the six-bit mask semiring. Then `C_k=A^{⊙k}`. A complete finite calculation computes all 672 input rows and target masks of `C_1,...,C_14`, and finds `C_10 == C_14` entry by entry. Multiplication on the right by `A^{⊙r}` proves `C_(10+r)=C_(14+r)` for all `r>=0`. Checks `C_k != C_(k+4)` for `1<=k<=9` establish the earliest four-periodic point.

The reported component counts and bit-mask histograms are finite exact counts, checked for the initial 14 classes. Their maxima therefore apply at arbitrary length. A gate set containing zeros can only delete paths; a positive gate changes a path's positive weight but preserves which paths exist. Consequently every nonnegative-gate six-coordinate support is a subset of `C_k`, and all-one gates attain the stated maxima. For every fixed start/end joint state and `k>=10`, positive `U1` and `U0` have exactly the same mask support. As their respective coordinates sum nonnegative masses multiplied by occurrence counts, positivity is equivalent to an existential path with the corresponding occurrence. This proves the final statement.

## Executed certificate and coverage

The executable `PREFIX639_jet_component_support.py` verifies the original enumerator code SHA256 `48d6521bab630f7f2d9de8ac7158ff074ff448267c1893a0dd064e4335c264f1` (the exact previously published PREFIX-638 checker); the same binary data are shipped as `PREFIX639_PINNED_PREFIX638_native_jet_support.py.gz.b64`. It uses only native labelled-action semiring composition and exact `Fraction` cross-checks, without external continuous-angle operators.

`C_1` through `C_14` were constructed exactly. Verified essential counts:

| k | Positive matrix positions | U0 positions | U1 positions | V00 positions | V01 positions | V11 positions | Total positive coordinates |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 8 | 4,284 | 974 | 1,260 | 974 | 974 | 1,260 | 9,726 |
| 9 | 3,388 | 1,225 | 1,260 | 1,225 | 1,225 | 1,260 | 9,583 |
| 10 | 4,284 | 1,260 | 1,260 | 1,260 | 1,260 | 1,260 | 10,584 |
| 11 | 3,388 | 1,260 | 1,260 | 1,260 | 1,260 | 1,260 | 9,688 |
| 14 | 4,284 | 1,260 | 1,260 | 1,260 | 1,260 | 1,260 | 10,584 |

The program also checks all six masks against the **actual exact rational six-tuples** at all-one gate for lengths 1 through 6, and conducts 21 additional matrix-coordinate checks (7 prefix lengths each for all-positive rational, periodic zero, and all-zero gate sequences). All assertions passed. These exact checks support the finite semiring certificate, while independent mathematical review remains pending. The 14-step semiring computation itself is exhaustive over all 672 joint source states and all 672 possible target states, with zero entries implicit.

**Reproduction (Python 3 standard library):** place the four published files in one directory and execute `python PREFIX639_jet_component_support.py`; it emits `PREFIX639_jet_component_support_results.json`. Compare that JSON with the published certificate. No GitHub authentication or external mathematical library is required at runtime.

## Next discriminating unit

Compile masks by the stabilized `k mod 4` transfer class, store only its nonzero coordinate slots, and compare **real** memory, `Fraction` allocations and wall time with PREFIX-637's dictionary-based jet product and PREFIX-635 original-action DP. For an extension to 3+ patterns, recompute the AC state graph and test a new eventual-period/cap certificate; the constants 1,260, 4,284 and 10,584 belong to the present two-pattern observer.

**Authority:** author-side research note, not a claimed task Result, independent Driver review, or Foundation promotion. Exact source and verification scope preserved.
