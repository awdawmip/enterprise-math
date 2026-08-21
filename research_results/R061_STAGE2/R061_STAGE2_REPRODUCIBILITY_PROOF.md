# R061 Stage 2 — Reproducibility Proof

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`  
Taskbook source: `8b197776249e0b18850cee8375488de9aa57cbb4`  
Owner branch: `research/r061-stage2-arbitrary-point-line-gluing`  
Researcher-ID: `EM-R061S2-3CE600`

## Executable checker

Command:

```text
python3 scripts/r061_stage2_validate_arbitrary_point_line_gluing.py --out research_results/R061_STAGE2
```

Exit status: `0`.

The checker uses no floating-point decision for sector typing, decomposition, path validity, reversal, axis gluing, or triangle inequality. It does not read Stage 1/1R result artifacts.

## Stage 1R frozen regression

The checker independently regenerated and matched all frozen Stage 1R hash targets:

- Stage 0 coordinate fiber SHA256: `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`;
- explicit shuffle SHA256: `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`;
- explicit shuffle words: `8,388,607`;
- compressed Pascal SHA256: `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`;
- native Stage 1 replay SHA256: `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`;
- native trace pairs: `190`;
- formal linearizations: `524,287`;
- three-sector native paths: `1,572,861`;
- compressed trace SHA256: `aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`;
- Stage 1 structural replay mismatches: `0`.

`ORIGIN_FORMULA_REGRESSION_PASS = true`.

## Translated atlas / decomposition

On the `81`-vertex patch `-4<=p,q<=4`:

- translated anchor checks: `243`, mismatch `0`;
- directed point pairs: `6,561`;
- zero: `81`;
- axis: `852`;
- open sector: `5,628`;
- every nonzero pair classified into exactly one open translated sector or one translated axis class;
- uniqueness modulo two-chart axis glue: pass;
- all six carrier direction classes: pass without native negative axes.

## Translated path fiber

For all translated trace pairs `a+b<=12`, over seven starts and all three sectors:

- translated trace cases: `1,911`;
- explicit native path representatives: `172,011`;
- center transitions checked: `1,892,394`;
- binomial cardinality mismatches: `0`;
- endpoint/incidence mismatches: `0`;
- translated affine-chart prefix mismatches: `0`;
- within-trace trajectory collisions: `0`.

## Translation / axis gluing / third direction

- translation covariance cases: `12,005`, mismatch `0`;
- global translated axis identities tested: `273`;
- adjacent chart presentations: `546`;
- erroneous physical trajectory deduplication: `0`;
- zero trace has three distinct incidence support branches: true;
- translated third-direction nondegenerate branches tested: `1,386`, mismatch `0`;
- classification remains `CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.

## Reversal classification

The checker proves on the patch that the reverse native displacement is always

`D_rev = M(1,1,1)-D`, `M=max(D)`,

so reversal can always be retyped using positive axes only.

However native length symmetry fails.

Smallest canonical obstruction up to translation/cyclic relabeling:

- forward `E1` one tick: squared length `1`;
- reverse translated `S23(1,1)`: squared length `2`.

Patch symmetry failures: `5,616` of the tested nonzero directed pairs.

This is a classified mathematical negative result, not a checker mismatch.

## Triangle inequality

The checker uses the exact radical comparator

`sqrt(A)<=sqrt(B)+sqrt(C)` iff `A<=B+C` or `(A-B-C)^2<=4BC`.

It exhaustively tested `531,441` ordered triples on the bounded patch and found:

`triangle_failure_count = 0`.

The companion metric audit supplies the global algebraic proof of subadditivity.

## Final classification

Unexpected mismatch count:

`0`.

Hard target:

`ARBITRARY_POINT_TO_POINT_NATIVE_LINE_TRACE_AND_CROSS_SECTOR_GLUING_DERIVED = true`

in the exact **directed line-length** sense.

Metric classification:

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`

because reversal symmetry fails, despite the triangle inequality passing.

The surviving point-to-point object is

`DIRECTED_NATIVE_LINE_GAUGE`.

`CI_NOT_REQUIRED_FOR_RESEARCH`.

Stop after Stage 2 for Driver review.
