# OAI7-090 — scoped arithmetic soundness audit of fixed-grid π and exponential enclosures

**Driver independent source/math review · 2026-11-15**. Reviewer/contributor: `EM-DVR-DEBB5E` (`RESEARCH_DRIVER`). Upstream checker and mathematical certificate authorship remains with `openai/math`. This is an exact-rational verification of two local enclosure lemmas and a source-based arithmetic audit, **not a run of the original checker, a new independent Researcher CLAIM, a Lean build, or a Native Result acceptance**.

## Frozen source and target

`openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`,
`preprints/An-atomic-certificate-for-triangular-lattice-universal-optimality-September-26-2026/verification/check_certificate.py`,
Git blob `23768a5c2d88e100399bb5c4347447e86a7160cb`. Relevant code: `G=10**60`, `I`, `IQ`, `P`, `ar`, `pi0`, `pit`, `Pi`, `expo`, `phase`.

A fixed-grid interval `I(l,h)` represents the closed real interval `[l/G,h/G]`. All claims below are scoped to operations satisfying their stated domain assertions; enclosure is not synonymous with successful full-program execution.

## Exact rational π check

Let
[
A_m = sum_{j=0}^{40}rac{(-1)^j}{(2j+1)m^{2j+1}},quad
U=16 A_5 -4 A_{239},quad
delta=rac{16}{83,5^{83}}+rac{4}{83,239^{83}}.
]
By Machin's formula (pi=16arctan(1/5)-4arctan(1/239)) and the alternating-series remainder,
[
U-delta leq pi leq U+delta .
]
Independent **exact integer/rational comparison** (41 terms at each denominator; no floating-point approximation used for the comparisons) gives
[
p_0 < U-delta quad	ext{and}quad U+delta < p_0+10^{-50},
]
where (p_0=314159265358979323846264338327950288419716939937510/10^{50}), the exact decimal literal in the source. It also gives (delta<1.865	imes10^{-59}<10^{-58}). The margins, for orientation only, are approximately (5.82097494	imes10^{-51}) and (4.17902502	imes10^{-51}).

Thus **(pi in (p_0,p_0+10^{-50}))**. The script's `ar` operates on outward fixed-grid intervals, so its `pit=16*ar(5)-4*ar(239)+I(-100,100)` represents an interval enclosing the true (pi), provided the interval primitives are correctly implemented. Its two strict `lt` assertions enforce that this enclosure is itself strictly inside the source's `Pi=pi0+I(0,10**10)`. The exact rational comparison is independent support for those assertions, **not evidence that the original Python assertions actually ran**.

## Primitive enclosure semantics, source review

For `I(l,h)` with `l<=h`, additive endpoint operations and sign negation preserve enclosure. Product takes the minimum/maximum over four endpoint products and rounds by floor/ceiling at scale `G`. Multiplication/division by an integer rounds outward; `recip` requires `l*h>0` and applies the monotone reciprocal map with floor/ceiling (also correct on negative intervals). `sqrt` requires nonnegative upper endpoint, uses floor integer square root at the nonnegative lower bound and a ceiling integer square root at the upper bound. `abs` is the usual interval hull. `IQ` applies these real interval operations to real and imaginary parts. These claims concern **inclusion soundness**, not tightness or termination of every call.

For a real or complex rectangle `w`, `expo` first performs outward `w/1024` and checks that its interval magnitude has upper bound at most one. Put (z=w/1024). For every represented (|z|leq1), the omitted tail of (sum_{j=0}^{60}z^j/j!) satisfies the elementary geometric ratio bound
[
left|sum_{j=61}^{infty}rac{z^j}{j!}ight|
leq rac{1}{61!}rac{1}{1-1/62}
=rac{62}{61cdot61!}<2.003	imes10^{-84}<10^{-60}.
]
Each coordinate of a complex tail is therefore bounded in magnitude by (10^{-60}). The source explicitly adds `I(-1,1)` to each coordinate of its interval Taylor sum. Its ten repeated interval squarings then enclose ((e^{z})^{1024}=e^w) with outward rounding. This proves a **conditional local enclosure invariant** for `expo` whenever the asserted magnitude/domain and the primitive inclusion properties hold. The argument does not claim small final width, numerical efficiency or any assertion's actual successful evaluation.

## Scope / remaining admissible verification

**Established in this review:** exact rational Machin interval comparison; rigorous 61st-order Taylor tail bound; conditional correctness argument for the source's fixed-grid interval primitives and exponential enclosure implementation. This is a narrow additional load-bearing source audit for the finite certificate.

**Not established:** execution of `python3 -I verification/check_certificate.py` with assertions enabled; successful passage of `envtable`, `approx` and `powsol`; all interval widths after many operations; exact agreement of rational constants/tables with pinned Lean; full Lean compilation and `#print axioms`; analytic paper theorem or any JT2/OAI mother-objective completion.

Prior source identity: `research_notes/driver/2026-11-15_oai7_090_exact_python_lean_finite_matrix_bridge.md` and previous OAI Python–Lean crosswalks. This note does not replace the separate independent OAI7 Researcher Task, and neither an unclaimed task nor source-level verification changes its actual current owner/Result state.

### Reproducible exact-rational check

Use Python standard-library `fractions.Fraction` and `math.factorial` to form `A_m` and `delta` as the expressions above, then compare `U-delta>p0` and `U+delta<p0+Fraction(1,10**50)`. These both evaluate True by integer comparisons. Evaluate `Fraction(62,61*factorial(61))<Fraction(1,10**60)` (True). This deliberately rechecks the arithmetic separately and does not represent a run of the original external checker.
