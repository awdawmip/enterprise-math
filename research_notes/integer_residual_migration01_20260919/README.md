# Integer-residual migration 01: angular histogram diagnostics

Status: locally validated source-slice candidate; NOT merged to production main.

## Actual consumer change

`tools/nollm_visual_toolkit/nollm_visual_toolkit/multiplication_lab.py::diagnostics`
now always emits `angular_cv_squared_exact`, produced by `AngularDispersion`.
For ordered counts c, B bins and T=sum(c)>0, the exact scalar is the unreduced
pair N=B*sum(c*c)-T*T, D=T*T. Compare with integer cross-products; no root or
approximate equality is needed. Keep original ordered counts: equal scalars
never identify histograms, native states or paths.

`diagnostics(phi, exact_scale=10**12)` additionally materializes S*N=D*q+r
through the existing `enterprise_math.exact_arithmetic.brc_scaled_evaluate`.
All exact-record integers are decimal strings, including the full BRC trace.
This is the residual of CV SQUARED, not of CV or of any geometric coordinate.

The toolkit remains standalone for symbolic source creation/comparison. BRC
readout is explicit and requires Enterprise Math; missing BRC raises rather
than silently using float. Original `angular_cv` remains a labeled legacy
float display, and the polar quantizer/collision metrics are not migrated.
This is a dual-readout first slice, not elimination of all floating consumers.

## Validation and limits

18 new tests and 16 unchanged upstream arithmetic/data tests pass. All old
fields match exactly in 27 real-consumer differential cases. 1,356 histograms,
4,068 scaled readouts and 676 comparison pairs are checked. The separate prior
31-test prototype suite was rerun unchanged, not counted as new migration work.

The original exact-arithmetic gate passes the new exact module. The historical
mixed module still FAILS that whole-file gate; its 36 legacy numerical AST
nodes are unchanged. No waiver or whole-repository pass is claimed.

Validation used authentic file fixtures (blob IDs in validation.json), not a
complete checkout. Full production package initializers, two HTML-generation
tests, browser JavaScript, full-repository regression and independent review
remain unexecuted. No initializer or existing primitive module is changed.
No hosted Actions/workflow execution was requested.

## Recovery

Do not replay the prior scalar kernel work. Next isolate actual ranking and
threshold consumers of angular_cv and switch their decision inputs to the
exact squared statistic. Separately plan polar-cell boundary certificates.
Preserve A2/declared polar observer versus native X6 typing throughout.

Researcher: EM-DIRECT-4A5102; activity RA-1094DE57986E6E3FDCEA65DA.
