# R34 — Non-stepwise S23/AV startup via Farey regime last-survivor rank/select

Date: 2026-11-10. Deliverable: exact finite-prefix proof and executable integration, author-side research (independent review pending). Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Reference interfaces: R26 Farey successor/Floor Sum (c50ad8594e8840476d10f51d73067ab5ec62a654), R27 last-survivor event theorem (6cfd0bf078b3bd05fbd4c51508a868a4706a5823), R32 direct long-horizon bulk compiler (87fdeff1cba7055f50a5fd8dadaad390476d9da1), and R33 interval-Euclidean stage generator (18d43c744aaed7041e5f7e87f98d278489b6aa57).

## Objective and exact model

R32's trillion-horizon S23/AV compiler generated 298 maximal affine risk runs, but initialized with **261** consecutive full-phase risk evaluations, n=129,...,389. Replace this startup by a source-preserving exact rank/select algorithm, then combine it with R33's 28 quotient decisions and R32's unchanged 148 positive interval blocks.

Fix m=128, irrational theta in

    262204504569236716045286 / 10^24 < theta < 262204504569236716045287 / 10^24.

Let P_n be the circular fractional phases {t theta}, 0<=t<n. The m historical arcs I are the oriented gaps of P_m. Write M_n(I) for the maximum elementary P_n gap within I. The scalar risk is R_n=1-sum_I M_n(I). Source labels and owner arcs are retained until a maximum-gap event has been selected.

## Lemma: exact rank/select startup for a fixed Farey stage

Let a/i<theta<c/j be adjacent Farey neighbors of order n-1, with ic-ja=1 and i,j<n<=i+j. Define u=i theta-a>0, v=c-j theta>0 and w=u+v. R26's exact clockwise successor permutation gives gap-source ranges:

- u: 0<=t<n-i;
- w: n-i<=t<j;
- v: j<=t<n.

For a stage with fixed Farey pair and first n0, adding each cut n>n0 destroys the unique w gap sourced at t=n-i-1, splitting it into u and v inside the same original historical arc. For any historical arc I put

    T_I={t in [n0-i,j): {t theta} is in I}.

If T_I is nonempty, that arc has exactly one positive risk increment during the full stage, when the last w gap disappears:

    n_I=i+max(T_I)+1,
    Delta R_(n_I)=w-max(u,v)=min(u,v).

If T_I is empty, no such event occurs in this stage. Distinct historical arcs give distinct event times. For a truncated stage, retain only events <= its horizon. This applies R27's already proved last-survivor theorem to the former startup prefix.

The source population in any half-open integer interval and any historical arc is obtained via R26's Euclidean Floor Sum identity. A suffix-count binary search selects max(T_I) while preserving its original source and owner. At Farey stage transitions, query exact risk on both sides of the boundary; the boundary increment is not silently presumed to vanish.

## Certified three-stage startup

Uniform exact Farey brackets across the strict frozen parameter interval are:

| n stage | Farey neighbors | Interior last-survivor events | Event amplitude |
|---|---|---|---|
| 128..164 | 27/103 < theta < 16/61 | n=129..164 (36) | 16-61 theta |
| 165..225 | 43/164 < theta < 16/61 | n=166..225 (60) | 164 theta-43 |
| 226..389 | 43/164 < theta < 59/225 | n=227..292 (66), n=329..389 (61) | 164 theta-43 |

The exact risk endpoint queries certify an additional positive increment 164 theta-43 at each transition n=165 and n=226.

Thus all 261 startup updates have exactly four maximal constant-increment segments:

| n updates | steps | exact Delta R |
|---|---:|---|
| 129..164 | 36 | 16-61 theta |
| 165..292 | 128 | 164 theta-43 |
| 293..328 | 36 | 0 |
| 329..389 | 61 | 164 theta-43 |

There are 225 positive increments and 36 zero increments. Since R_128=0, the exact startup endpoint is

    R_389=36(16-61 theta)+189(164 theta-43)
         =-7551+28800 theta.

The prefix compiler performs 6 complete Floor Sum risk-oracle calls (one initial, three stage ends, two transitions), rather than 261 individual reconstructions. It also performs per-arc source rank/select operations, and the present implementation still materializes 225 positive source events. The six-query figure is not a total time or bit-operation count.

## Verification and reproducibility

VERIFY_R34_PREFIX.py constructs the stage sequence, exact arc-source counts, last-survivor rank/select positions and transition risks from m and rational theta bounds. It does not ingest R32 or R27 event/risk tables. Its separate regression checker independently reconstructs all 261 complete circular partitions for 129<=n<=389 with rational arithmetic and checks the exact affine coefficients at every n.

VERIFY_R34_INTEGRATION.py takes unchanged R32 and R33 scripts as input paths. It substitutes only the two stage/prefix generator entrypoints of the R32 integration module at runtime; the existing R32 long-tail block compiler and final run serialization remain unchanged. With R33's 28 certified decisions producing 78 Farey stages, the integrated program produces 148 later positive blocks, 298 final maximal affine runs, and the identical terminal risk

    R_(10^12+128)=-4017401528447+15321634290944 theta.

The generated 298-row TSV is byte-identical to the saved R32 reference TSV with SHA-256:

    2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6

Reproduce locally with both pinned predecessor Python source files (R32 at PR #1929, R33 at PR #1935) and the optional R32 reference TSV:

    python VERIFY_R34_PREFIX.py
    python VERIFY_R34_INTEGRATION.py --r32 /path/to/VERIFY_R32.py --r33 /path/to/VERIFY_R33.py --reference /path/to/AFFINE_RUNS_R32.tsv

The exact 4-row prefix table is in PREFIX_R34.tsv, the 298-row complete table in AFFINE_RUNS_R34.tsv, the selected stage/endpoint checks in CERTIFICATE_R34.json, and actual local outputs in RUN_EVIDENCE.txt.

## Complexity, provenance and scope

For these three initial stages, there are at most m suffix binary selections per stage; each uses logarithmically many Euclidean Floor Sum counts of integer bit lengths depending on frozen parameter precision and stage source bounds. The stage-boundary query cost is fixed in the prefix, and R33's accelerated Farey stage construction plus R32's 148 long-tail blocks retain their own prior costs. This eliminates the specifically identified per-cut startup loop. General m, arbitrary irrational parameter enclosures, and full bit-complexity accounting remain open extensions. The actual cost of source-rank operations, input transform, precision, serialized output and proof checking remains part of any complexity comparison.

BRC reuse: the original historical-arc owner, source number, and gap family are kept until the exact risk-relevant selection is certified. The final risk is sufficient only for this specified scalar observer and declared horizon; this is an auxiliary irrational-circle result, not an assertion about native X6 dynamics. Exact computation and author derivation are completed; independent mathematical review and formal shared-task acceptance are pending.

## Next mathematical unit

Replace the 225 materialized positive events with a direct source-range rank/select that emits the four maximal initial blocks. Then make a portable general-m interface for the R33 jump generator, R34 prefix compiler and R32 long-tail block generator. Verify a second irrational interval and different history length, counting all integer bit operations, and seek independent review under actual project role authority. Preserve the frozen scientific input.
