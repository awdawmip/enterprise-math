# X6 Unit155 — frozen Newton fiber signed-coefficient observer vs native N-BRC path counts

Date: 2026-11-19. Mother objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Research author provenance: EM-X6-FB6990, original on-hour Research lane. Status: AUTHOR_PROVED / INDEPENDENT_EXACT_FINITE_EXECUTED / SOURCE-TYPED / UNREVIEWED / NOT_ADMITTED.

## Source-exact input and new actual consumer edge

Frozen historical comparison commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, distinct from unchanged scientific-task pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

- `src/enterprise_math/brc_newton_fiber_quotient.py`, Git blob `f9db29609e74b8f2a7202a1f626a138eb716fa29`: coordinates and fiber grouping lines 24–115, signed rational coefficient summation lines 118–134, edge restriction lines 149–161, transfer difference lines 164–187.
- `tests/test_brc_newton_fiber_quotient_foundation.py`, Git blob `2fc8a1dcee7710d3f3f2654a1cd9e19d51ea9cc1`: six original labeled positions at lines 23–33, four fibers and two transfer generators at 35–39, actual rational signed transfer at 41–51, weak edge observer at 62–71, signed coefficient label splitting at 73–82.
- Source dependency `src/enterprise_math/brc_newton_recursion.py` provides `RationalValuationScale` (original module read). The example fixes theta=1/2 and multiplicity=2. It is a Newton/Taylor-coefficient consumer, **not a six-axis signed native Cell path counter**.

## Exact theorem

The six frozen labeled positions A1,A2,B1,B2,C,D have full observer coordinates (residual scale, Taylor degree) A1=A2=(1,1), B1=B2=(1,0), C=(1/2,0), D=(1/2,1). Thus for the coefficient column `x in Q^6` the actual full fiber sum and weak edge observation are, in that order,

```text
S(x) = (x0+x1, x2+x3, x4, x5)
E(x) = (x0+x1, x2+x3).
```

The full fiber map `S:Q^6 -> Q^4` has rank four, with kernel exactly `span_Q(e0-e1,e2-e3)`; the edge-only map `E:Q^6 -> Q^2` has rank two, with kernel exactly `span_Q(e0-e1,e2-e3,e4,e5)`. For any fixed finite partition into fibers, the same proof gives `ker S=direct_sum_F {x in Q^F:sum_F x_i=0}`, dimension `n-number_of_fibers`. This is a full algebraic proof, not a finite-range extrapolation.

For **nonnegative natural coefficient counts**, `S(x)=0` implies `x=0`, but `S` is still noninjective on `N^6`: the two distinct labeled positive states `e0` and `e1` both map to `(1,0,0,0)`. Under the actual **signed rational** coefficient contract, `e0-e1 != 0` maps to zero; this is a lawful Taylor coefficient cancellation, not cancellation of positive natural native shortest-path realizations. Moreover `E(e4)=E(0)=0` even on `N^6`, because the edge observer drops residual scale 1/2. These are three distinct semantic phenomena: label coalescence, signed coefficient cancellation and scale-filtered observation.

Within additive linear repairs over `Q`, the full observer requires at least two independent additional scalar readings to reconstruct all six labeled coefficients, and the edge-only observer at least four. The lower bounds are rank-nullity. They are attained by `(S(x),x0,x2)` and `(E(x),x0,x2,x4,x5)`, respectively. This is a minimality statement about *linear* readings of the same labeled coefficient vector, not the absolute bit complexity of arbitrary encodings.

## Independent exact finite certificate

A standalone exact integer/Fraction checker enumerated all 729 states of each cube `{0,1,2}^6` and `{-1,0,1}^6`. For either cube, there are 225 distinct full signatures and 25 distinct edge signatures; ordered equal-signature pair counts are exactly 3,249 and 29,241 respectively. It performed 1,458 additional exact rational transfers `(2/3)(e_moved-e_anchor)` in the two original nonsingleton fibers; every transfer preserves both observers. Three Python execution modes normal/-O/-OO return exit 0 and identical output SHA256 `62c270b79d58eefddfef10aa74f5fd69acc149bd20174222c4928d2effe08445`. Host emitted an unrelated spreadsheet-runtime warmup traceback on stderr, while the checker process itself exited 0; no original frozen module test or R063 benchmark was executed.

Independent enumeration verifies this **literal six-position frozen test fixture**; the structural theorem follows from the displayed fiber-map linear algebra. The portable checker reconstructs the frozen fixture's exact map, rather than importing its historical Python module.

## 28-LP source disposition and next frontier

This is a newly inspected frozen historical source-to-test import edge after Unit153's selected 15-file audit and Unit154's partial-operation audit. LP019: source supports a **signed rational Newton/Taylor coefficient sum**, and thus supplies an exact false-positive exclusion for any proposed "positive native N-BRC subtraction" attribution. LP011: this code has no signed-native spatial axis argmax. Neither hypothetical historical faulty native caller has acquired a verified `commit:path:line` witness; retain both as UNRESOLVED_PROVENANCE. Preserve original R063 same-six-file Unit50 execution (17/17 gates, 512/512 rows, SHA `51891fbf...`), current P000, signed Cell path semantics and separate independent Driver review.

No new claim of mathematical admission, native PROGRESS, full 28-LP coverage, original historical test execution or production-code patch is made by this author evidence. Genuine next work: investigate remaining source-exact LP011/LP019 callers and other uncovered 28-LP source edges; consume the original Source write requests for Units149–152 and record newly authorized Native semantic association without repeating FAILED/UNKNOWN writes.
