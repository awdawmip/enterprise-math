# T6 / maximal p=17 / vertical order 6: split (2,4) and (3,3) exact mixed-congruence exclusion

Date: 2026-11-23 (Asia/Hong_Kong). Role lane: `chatgpt-research-onhour-enterprise-math-20260923`; research actor: existing recorded `EM-X6-FB6990` / public SID `MCP-082892eb480e45dea6d4b9fcc0491034` (this source attribution alone grants no live CLAIM). Scientific evidence: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Global mother objective `T6=2332`: **OPEN**.

## Scope and exact inherited inputs

Frozen task `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md` at commit `d84bd940cfb093cdc60e569f15cad58772a51dca`, blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. Preserve the two exponent-mass budgets `<=2331`, complete named composite denominator `a=e+1`, signs and multiplicities, seven original observations `H0..H6`, and source firewall. Work under current P000; no P000 or frozen-science amendment.

Consume, do not reprove, accepted order-1 through order-4 campaigns and author exact p17 order-5 and order-6 splits (0,6),(1,5), plus the author p17-squared cancellation lemma. These author units are not yet independent Source mathematical admissions.

After cancelling common named atoms, a maximal-p17 valuation-one denominator is `a=17(r+17q)`, `1<=r<=16`, `q>=0`; its mass is `289q+17r-1` and its vertical order is `q`. We leave all p17-free atoms unrestricted. The original six reciprocal-observer equalities imply, for each `j=1,...,6`, the globally necessary mixed congruence:

```
sum_{r=1}^{16} u_r * r^(-j)
 + sum_{q>=1,r=1}^{16} m_{q,r} * (r+17q)^(-j)
 == 0 (mod 17^j).
```

Every inverse is a modular inverse of a unit. `u_r` is the signed multiplicity of the q0 atom `(0,r)`, and `m_{q,r}` is that of each vertical atom. These congruences are valid even when lower-prime denominators provide compensation to the rational H observers.

## Exhaustive finite domain

Generate all integer partitions of vertical order 2, 3, 4 into positive `q`, with sorted multisets of `r=1,...,16` at each repeated q. Discard states exceeding side mass 2331. The complete state counts are:

| Side vertical order | 2 | 3 | 4 |
| --- | ---: | ---: | ---: |
| Admissible named rosters | 152 | 1,088 | 6,460 |

For split (2,4), enumerate all `152*6460=981920` oriented side pairs; 262,720 contain a shared named vertical atom and cancel to a lower vertical order. Exactly **719,200** primitive pairs remain.

For split (3,3), exchange of both sides is overall sign and leaves the equality problem unchanged. Enumerate each unordered pair once, `C(1088,2)=591328`; 171,136 share a named vertical atom. Exactly **420,192** primitive pairs remain. Identical sides cancel entirely.

The q0 alphabet is all 16 residues, with arbitrary signed integer multiplicity and each side bounded by original mass. It is **not** a hand-picked q0 cutoff or a bounded local rational H-moment approximation.

## Saturated affine lattice and exhaustive obstruction

Reuse the complete 16x16 integral row basis `U` of the original p17 q0 kernel from `research_artifacts/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260920_01A079FC/p17_q0_certificate.json` (blob `d9ac014355a6a1058cc8a0cf2141a01082628881`). `|det(U)|=17^21`; combined with the mixed-moduli Vandermonde index, this proves saturation. For each named vertical atom, the six exact successive modular solves furnish an integral particular q0 representative. Every possible compensation is that particular representative plus an integral combination of the rows of U. We use the exact q5 published kernel routine `research_checks/T6_P17_Q5_EXACT_MODULAR_LATTICE_CHECK_20261123.py` (blob `2c1aa73268aa11300a32b9923e3bdbddb6190813`).

Set `W=diag(16,33,...,271)`, and let `c+,c-` be the respective vertical masses. Separate original signed-side budgets imply the necessary inequality

```
||W*u||_2^2 <= (2331-c+)^2 + (2331-c-)^2 = R^2.
```

With the exact rational Gram–Schmidt decomposition of `U W`, the minimum squared orthogonal length is `Dmin ≈ 17,372,418.621726293`. This decimal is display only; all decisions use the exact fraction saved in the certificate and the previously verified q5 source. Maximum possible R² is 4,360,450 for (2,4) and 4,193,408 for (3,3), **strictly below Dmin**. At every reverse Gram–Schmidt coordinate, at most the exact floor and ceiling of the affine center can meet this bound. Recurse through both candidate integers and prune only when an exact rational partial squared norm already exceeds R². This visits every lattice point that could meet the necessary weighted-sphere bound.

The independently chunked local execution produced:

| Split | Raw pairs | Shared-vertical | Primitive pairs | Exact GS nodes | Sphere leaves | Budget-valid completions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| (2,4) | 981,920 | 262,720 | 719,200 | 1,917,830 | **0** | **0** |
| (3,3) | 591,328 | 171,136 | 420,192 | 1,035,941 | **0** | **0** |
| **Total** | **1,573,248** | **433,856** | **1,139,392** | **2,953,771** | **0** | **0** |

Source: exact standalone Python/SymPy execution in five disjoint, complete ranges: (2,4) left-state indices [0,76), [76,152); (3,3) indices [0,300), [300,700), [700,1088). Each chunk wrote a local JSON with its execution statistics and SHA-256, enumerated in the project certificate. The full local program and raw five certificates are preserved in this run's files; the compact published checker composes the already published q5 routine and **has not itself been separately reexecuted**. This is author-run evidence, not independent review.

## Conclusion and next exact frontier

**Author exact finite proposition.** Under the frozen T6 inputs and the previously proved p17 valuation>=2 cancellation, there is no primitive maximal-p17 valuation-one vertical-order-six signed shape of split (2,4) or (3,3) with both original side masses <=2331 and all six globally necessary mixed congruences. Proof: complete finite roster, complete saturated affine parameterization, exhaustive rational sphere enumeration with zero leaves. Shared atoms reduce to earlier lower-order cases.

Together with the already saved (0,6) and (1,5) author units, this **completes the author-level p17 vertical order-six split coverage**, but it is **not** an independent audit or global T6 threshold proof. Continue from the smallest genuinely unresolved p17 order-seven primitive split, recompute exact budget and q0-lattice sphere radius, preserve p17-free completion, and move onward only after checking whether the new exact necessary filter has any survivor. Do not rerun q5, p19 or these four q6 splits. If a survivor occurs, retain full signed names and solve p17-free lower-prime completion rather than claiming a collision.

## Control/identity boundary

At this author research boundary, native T6 Task read `onhour-20261123-0315-t6-current-task-read-v1` remains a waiting read under GitHub primary rate limiting and auto-resumes under its original ID. Prior Source continuation `onhour-20261123-0105-t6-current-source-cont-v1` is SUCCEEDED but is not fresh write authority. No winning T6 CLAIM/RUN, official semantic PROGRESS, Result admission, or nonauthor proof review is asserted; these portable research files are not the protected native return.
