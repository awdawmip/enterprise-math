# X6 Unit116 — sharp fixed-positive R063 residue collision and N-BRC information-loss thresholds

**Date:** 2026-11-18. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. **Task:** `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. **Scope:** original R063 fixed-positive ordered two-axis chart, embedded in the selected signed-X6 Cell directions only when the axis/sign/start labels are explicitly retained. **Evidence status:** `AUTHOR-PROVED / EXACT-INTEGER-EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Source and genuinely new mathematical question

The actual frozen historical file `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py` at commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3` has Git blob `643b2bac659a445891dcb5588b647972977104e0`. Lines 77–82 enumerate `sector_ball(R)`; lines 85–98 define `residue(point,m)` and the first collision; lines 101–132 define the original `check_spatial` capacity-based radius `R_cap(m)`, for `m=2,...,20`. The original checker records the earliest radius **forced by its pigeonhole-capacity argument**, not the earliest radius at which its actual ordered sector has a residue collision.

With the original nonnegative two-generator sector
[
P_R=\{(a,b,0):a,b\in\mathbb Z_{\ge0},\ a^2+b^2\le R^2\},
\qquad \rho_m(a,b,0)=(a\bmod m,b\bmod m),
]
and the exact native positive shortest-word multiplicity
[
B(a,b,0)=\binom{a+b}{a},
]
we now determine two distinct *sharp* thresholds.

## Theorem 1: first residue collision is at radius exactly m

For every integer `m>=1`, `rho_m|P_R` is injective for every integer `R<m`, and is noninjective at `R=m`.

**Proof:** For `R<m`, both coordinates are between 0 and `m-1`, so their residues uniquely determine the coordinates. At `R=m`, three pairwise distinct points `(0,0,0)`, `(m,0,0)`, and `(0,m,0)` all have residue `(0,0)`. Moreover, at this radius these are **the only points in any non-singleton residue fiber**: a distinct congruent pair differs by `m` in at least one coordinate; on `P_m` the endpoint with that coordinate `m` must have other coordinate 0, which forces the entire pair into that three-point fiber. Thus exactly three unordered colliding pairs occur. In the original a-major / b-minor iteration, `first_collision(P_m,m)` returns `(0,0,0)`, `(0,m,0)`, residue `(0,0)`. QED.

## Theorem 2: first residue fiber with differing N-BRC is at exactly m+1

For every integer `m>=1`, every residue fiber in `P_R` for integer `R<=m` has constant `B`; at `R=m+1` there is a residue fiber with two different values.

**Proof:** Theorem 1 covers `R<m`. At `R=m` the only non-singleton fiber contains `(0,0,0)`, `(m,0,0)`, `(0,m,0)`; every point has `B=1`. At `R=m+1`, the distinct points
[
x=(0,1,0),\qquad y=(m,1,0)
]
belong to the disk since `m^2+1<=(m+1)^2` and satisfy `rho_m(x)=rho_m(y)=(0,1)`, while
[
B(x)=1,\qquad B(y)=\binom{m+1}{m}=m+1.
]
Hence the first loss of current BRC-count determinability occurs exactly one integer radius after first residue noninjectivity. QED.

**Interpretation:** the original fixed-positive modulo-sector endpoint quotient loses endpoint identity at `R=m`; its fibers remain N-BRC-constant at that exact radius; a concrete N-BRC mismatch first appears at `R=m+1`. This certifies a precise readout-and-operation boundary, not an all-X6 projection. The native signed coordinates and ordered path/source labels remain separate from the chart residue.

## Exact executed validation

An independent checker reproducing the original `sector_ball` enumeration order and modular residue formula was locally executed for all **99 moduli m=2..100**. It exhaustively grouped every point of `P_m` by its residue, verified injectivity on `P_(m-1)`, exactly the three threshold collision pairs and their BRC counts, and checked the `m+1` witness. The checker was executed with CPython standard, `-O`, and `-OO`; every mode produced identical machine JSON, SHA256 `821cf79b9235477e016ed1e57338f769d510678077801c61632978f4ff17e82e`.

For the original checker range `m=2..20`, its pigeonhole guarantee radius `R_cap(m)=min\{R:|P_R|>m^2\}` equals the sharp collision radius for `m=2..5`, and is **later** for every `m=6..20`; at `m=13..20` the delay is two integer radii. Example: `m=20` first collision is at 20, first BRC mismatch at 21, whereas `R_cap(20)=22` and `|P_20|=335`. These statements are exact for the declared finite range and follow from the two global theorems for the sharp thresholds.

- Executed independently checked source: `research_checks/X6_UNIT116_SHARP_SECTOR_RESIDUE_BRC_THRESHOLD_20261118.py` at GitHub commit `84f7131b3c576ccd79a0072fe06c3bf1d7ad7740`, blob `6d3d5a8ef5ecd11ce888e996412e2a138d385594`.
- Full numerical certificate for `m=2..20`, plus total checks `m=2..100`: `research_checks/X6_UNIT116_SHARP_SECTOR_RESIDUE_BRC_THRESHOLD_RESULTS_20261118.json` at commit `2652e1babad0632b0ac662383386a85efc95a8e5`, blob `4397e568fc06e50955e4154ead66eb7640bb161e`.
- The original R063 module source was inspected at its actual immutable Git blob through the authorized GitHub connector, while the local Unit116 checker was an independent implementation. No original C3/C4 benchmark was executed in this Unit116.

## Existing native-benchmark evidence and the remaining scope

The original support issue [#2416](https://github.com/awdawmip/enterprise-math/issues/2416) includes an **2026-11-15T22:43:34Z** comment documenting a 2026-11-16 original six-blob loader execution under the same-object wrapper: exit 0, 17/17 gates, 512/512 radii, 13 output files and pinned digests. Original authored report is `research_notes/X6_R063_ORIGINAL_SIX_BLOB_NATIVE_REPLAY_20261116_0631_REPORT.md` at commit `441042862a2c29496d4e86926c23218a32c015e5`. That author-side original execution evidence is **already saved**; its independent authorized-runner verification, review and Source-admission decisions remain separate open items. The issue header's older 'not executed' status must not be reused without incorporating this later comment.

This unit refines the source-type and observability implications for LP028 and LP019. LP011/LP019 historical wrong-callsite claims remain `UNRESOLVED_PROVENANCE`, and the 28-LP downstream consumer graph remains only partially audited. The original signed-X6/PathSqrt typed consumer at `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` preserves explicit start, axes, signs and roots, rather than treating the two-component residue as a full signed Cell; follow-up should pin other actual callers, not invent an offending native consumer.

**Next exact action:** after confirming original same-run resume receipt and current owner authorization, checkpoint the already GitHub-saved Units114–116, then publish Native semantic PROGRESS once with original request-ID tracking and Source readback. Continue directed source tracing of real `residue/first_collision` consumers, and hand the exact threshold distinction to independent Driver's 28-LP review. Do not repeat C3/C4, change frozen science, or use the maintenance lane's identity.
