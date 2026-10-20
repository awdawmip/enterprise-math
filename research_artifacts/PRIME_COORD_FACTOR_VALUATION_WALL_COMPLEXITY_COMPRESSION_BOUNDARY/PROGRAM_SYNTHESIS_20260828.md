# Prime Coordinate Factor — Valuation-Wall Program Synthesis

Status: `SUPPLEMENTAL_RESEARCH_SYNTHESIS / NON-AUTHORITY / FOR DRIVER REVIEW`

Date: `2026-08-28`

Program: `PRIME_COORD_FACTOR_EXTRACTION_PROGRAM_20260827`

Current task: `RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION-BOUNDARY`

Publication: `TP2-25876E1168D68965C9E4`

Researcher: `EM-PCF5-8A41D7`

Result under review: `RR-83D5F9A0C24617B4E8A1`

This note is supplemental. It does not replace the frozen research return, result record, execution record, or Driver disposition.

## 1. Program transition

The program has crossed two distinct thresholds.

First, the original PCF4 fixed-public-prefix route was closed at the strongest exact restricted theorem: any fixed finite N-independent family of public-prefix probes reduces to a finite family of precommitted integer gcd probes and therefore has finite prime support. This is a scoped no-go, not a program-wide impossibility theorem.

Second, the independent N-dependent successor PCF4R closed positively: for every distinct odd semiprime

\[
N=pq,\qquad 3<p<q,
\]

there is an exact factor-blind N-only gcd extractor based on

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}.
\]

The load-bearing local identity is

\[
v_r(A_s)=\left\lfloor\frac{2s}{r}\right\rfloor+\left\lfloor\frac{3s}{r}\right\rfloor,
\qquad r>3,\ 0\le s<r.
\]

Hence the first local divisibility wall occurs at

\[
s=\left\lceil\frac r3\right\rceil.
\]

This solves the former missing interface

\[
N\text{-only hidden-factor asymmetry}
\longrightarrow
G_N
\longrightarrow
1<\gcd(G_N,N)<N
\]

at exact extractor-existence level.

## 2. Exact N-only splitter structure

The accepted parent splitter uses only public N-dependent indices.

A dyadic schedule probes

\[
s=1,2,4,\ldots
\]

until the first nonunit gcd. If the first nonunit is already the smaller factor, extraction is complete. If the first dyadic nonunit synchronizes both hidden primes and returns N, the exact wall inequalities force

\[
q<2p.
\]

With

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor,
\]

the public fallback at `t` or `t+1` yields the smaller factor. No hidden factor, factor-labelled coordinate, CRT idempotent, factor-derived phase, or prime-labelled constructor parameter is used.

This is an exact factorization mechanism on the stated semiprime domain, but extractor existence alone says nothing about asymptotic speedup.

## 3. Complexity compression result

The parent implementation reaches an index s by the recurrence

\[
A_s=A_{s-1}\frac{6(2s-1)(3s-2)(3s-1)}{s^3},
\]

so sequential access to the first factor-bearing wall costs

\[
\Theta(p)
\]

updates in the balanced case.

PCF5 replaces this sequential access with exact random-index factorial evaluation. For public k, let

\[
m=\lceil\sqrt{k}\rceil,
\qquad
Q(X)=\prod_{j=1}^{m}(X+j).
\]

Fast product-tree construction and multipoint evaluation of `Q` at arithmetic-progression block starts reconstructs `k! mod N` in

\[
\widetilde O(\sqrt{k})
\]

ring operations. Because

\[
A_s=(2s)!(3s)!(s!)^{-5},
\]

an isolated public `A_s mod N` is available from three factorial residues plus an explicit gcd/unit check in

\[
\widetilde O(\sqrt{s})
\]

ring operations.

The geometric dyadic schedule satisfies

\[
\sum_j\sqrt{2^j}=O(\sqrt p),
\]

and the synchronized fallback adds only constant-many evaluations at scale `Theta(p)`. Therefore the complete N-only splitter has

\[
\boxed{\widetilde O(\sqrt p)}
\]

ring-operation complexity, or conservatively

\[
O\!\left(p^{1/2}\operatorname{poly}(\log N)\right).
\]

For balanced semiprimes `p=Theta(sqrt(N))`, this is

\[
\boxed{N^{1/4+o(1)}}.
\]

## 4. Classification: genuine compression, no novel exponent

The compression is genuine relative to the accepted sequential valuation-wall recurrence:

\[
\Theta(p)\longrightarrow\widetilde O(\sqrt p).
\]

However, the mechanism is structurally the classical Strassen/Pollard-Strassen factorial layer: block products, product trees, and fast multipoint evaluation provide square-root-scale factorial access. The valuation-wall theorem gives a new exact N-only interpretation of which public residues separate the hidden factors, but the first asymptotic acceleration lands on the already-known deterministic `N^{1/4+o(1)}` factorial-factorization layer.

Freeze the distinction:

- `EXACT_N_ONLY_GCD_EXTRACTOR = TRUE` at the accepted PCF4R scope.
- `VALUATION_WALL_RELATIVE_COMPRESSION = TRUE` for the PCF5 construction under review.
- `CLASSICAL_FACTORIAL_METHOD_EQUIVALENCE = TRUE` for the PCF5 construction under review.
- `NOVEL_DETERMINISTIC_FACTORING_EXPONENT = NOT ESTABLISHED`.
- `POLYNOMIAL_TIME_FACTORING = NOT ESTABLISHED`.

No Foundation, Working Truth, or toolbox promotion follows from this synthesis.

## 5. Exact-checker evidence

The frozen PCF5 checker reports:

- factorial residue checks: `1452`;
- sampled `A_s` residue checks: `582`;
- valuation-wall checks: `4222`;
- complete semiprime splitter checks: `946 / 946`;
- evaluator calls: `5236`;
- denominator-nonunit events: `0`.

These are regression/evidence checks. The asymptotic complexity claim is theorem-side and is not inferred from timings or finite scans.

## 6. Relation to parallel PCF3 work

Parallel PCF3 returns independently recover the same factorial valuation geometry in a three-wall form and classify synchronization more finely. In particular, they identify same-index separation by the middle wall for one straddle class and a public square-root-scale seed for the remaining synchronization cases.

Those results are currently separate research returns awaiting Driver disposition. They are corroborative for the program architecture but must not be silently merged into PCF5 authority before their own source-result reviews are terminally accepted.

## 7. Current frontier after PCF5

The scientifically meaningful question is no longer whether an N-only factor-bearing observable exists. It does.

The question is whether the special valuation-wall structure provides leverage *beyond* the classical factorial layer.

A valid successor should therefore not repeat larger semiprime scans or merely repackage the same product tree. It should discriminate among at least these outcomes:

1. **Post-Strassen composition succeeds.** The valuation-wall structure couples to a genuinely faster exact evaluator and yields an asymptotic exponent below `1/4` on the stated semiprime domain.
2. **Classical-equivalence persists.** Every admissible exploitation of the present observable reduces to known deterministic factorial/falling-factorial machinery with no new exponent.
3. **Scoped barrier.** A precisely stated evaluator/observable model admits a rigorous lower bound or information-access obstruction that explains why the wall cannot be accessed faster in that model.

Any future claim must remain N-only and factor-blind on the constructor side. Hidden factors may appear only in proofs.

## 8. Recommended next research lane

If Driver accepts `RR-83D5F9A0C24617B4E8A1`, the preferred next task is a separate post-Strassen lane, conceptually:

`VALUATION_WALL_POST_STRASSEN_COMPOSITION_OR_BARRIER`.

Its target should be explicitly narrower than a general factoring breakthrough:

> Determine whether the accepted valuation-wall observable admits an exact N-only evaluator/composition beating the classical `N^(1/4+o(1))` factorial layer on a stated infinite semiprime family, or freeze the strongest exact classical-equivalence/scoped-barrier theorem supported by the admissible model.

Candidate avenues include fast consecutive-product evaluation, baby-step/giant-step variants adapted to the wall threshold, arithmetic-progression product compression, and careful comparison against exponent-one-fifth deterministic factoring methods. None of these are claimed solved here.

## 9. Control-plane freeze

Current research return under review:

`RR-83D5F9A0C24617B4E8A1`.

Current PR:

`#759`.

This synthesis is intentionally non-authoritative and must travel with the frozen result rather than supersede it.
