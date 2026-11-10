# R35 — Exact fibre-extinction interval-output theorem

Date: 2026-11-10. Status: author derivation plus exact finite verification, independent review pending.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: R34 PR #1942, commit `f326670b828dd19bd66a44f0564e9e7932c683cd`.

## Question and mathematical setting

R34 computed the 261-update S23/AV prefix using 225 separate source-labelled last-survivor events. R35 replaces that intermediate enumeration by **directly certified maximal constant-increment intervals**. This mathematical observer is the declared auxiliary irrational circle rotation, not a complete native-X6 physical evolution.

Fix `m` original historical rotation phases `{tθ}:0≤t<m`, and denote their oriented partition arcs by `I`. For `n≥m`, `R_n=1-Σ_I M_n(I)`, where `M_n(I)` is the largest elementary gap currently remaining in historical arc `I`.

In a fixed Farey stage, let `a/i<θ<c/j` with `ic-ja=1`, `n₀≤n≤i+j`; write `u=iθ-a>0`, `v=c-jθ>0`, `w=u+v`. By the previously verified Farey successor partition, the `w` gap sources are precisely `[n-i,j)∩Z`. For each historical arc retain its own full source-count function

`C_I(n)= #{t∈[n-i,j) : {tθ}∈I}`.

Define the **extinct-fibre rank**

`F(n)= #{I : C_I(n)=0}`.

## Theorem (exact interval-output certificate)

For each `n` strictly inside this Farey stage,

`F(n+1)-F(n)∈{0,1}`,

and for all `n₀≤a≤b≤i+j`,

`R_b-R_a=(F(b)-F(a))*min(u,v)`.

**Proof.** The next rotation insertion deletes exactly one `w`-gap source `t=n-i`, splitting the same source-owned gap into the two lengths `u,v`. Its unique historical owner is the only fibre whose `C_I` can decrease, and the decrease is exactly one. Hence `F` increases by one if and only if this was the arc's last `w` source. While a `w` gap survives in that arc its maximum is `w`; after the last `w` is removed the maximum is `max(u,v)`. Thus this event lowers that maximum by `w-max(u,v)=min(u,v)`. Summing over historical arcs proves both identities. □

For an interval of updates `(a,b]`, set `d=F(b)-F(a)`, `L=b-a`. The one-step difference bound proves: if `d=0`, every increment is zero; if `d=L`, every increment equals `min(u,v)`; otherwise recursively split the interval at its midpoint and evaluate `F` there. Merge equal adjacent certified intervals to get the maximal constant-increment decomposition. Every certificate is obtained from **endpoint fibre-existence counts**, rather than the enumeration of positive events.

Compute each `C_I` by the exact Euclidean floor-sum owner identity of R26/R29. The algorithm retains history-owner and source membership until forming the chosen scalar risk. At Farey-stage transitions it separately computes the full exact risk at the boundary. Within a stage with `K` output blocks and width `W`, recursive queries number `O(K log(W+1))`, each requiring `m` Euclidean floor-sum ownership tests. This counts exact arithmetic operations, not their bit-complexity or stage discovery cost.

## Frozen S23 application

Use `m=128`, `262204504569236716045286/10^24 < θ < 262204504569236716045287/10^24`, `n≤389`. Integer floor comparisons `floor(dL)=floor(dU)` for every `1≤d≤389`, Farey bounds and strict gap winners certify a common phase ordering throughout the open enclosure.

The **four** maximal update segments are:
- `129..164`: 36 updates, `ΔR=16-61θ`;
- `165..292`: 128 updates, `ΔR=164θ-43`;
- `293..328`: 36 updates, `ΔR=0`;
- `329..389`: 61 updates, `ΔR=164θ-43`.

Consequently `R_389=-7551+28800θ`. Production generation used **three Farey stages, 19 F endpoint queries, 4,736 owner-count calls and six whole-risk queries**, materializing zero individual event records. The separate geometry checker verified all 261 risk values exactly.

## Independent family and trillion-horizon composition

For `θ=√2-1` enclosed by adjacent denominator-`10^25` rationals computed from integer square root, with `m=16, n≤96`, the standalone compiler produced **seven** maximal update intervals, final `R_96=106-254θ`. The checker separately rebuilt all 80 phase partitions. This used five Farey stages, 23 F queries, 848 source-owner count operations and ten whole-risk queries.

The unchanged R33 jump generator and R32 long-horizon compiler then consumed the four new S23 intervals. The complete computation generated 78 Farey stages, 148 long-tail positive blocks and 298 maximal affine runs up to `10^12+128`, with
`R_(10^12+128)=-4017401528447+15321634290944θ`.
The complete R35 TSV is **byte-identical** to independently archived R32 results, SHA256 `2573a84999d53dfd1cce772c45a41abaff251da735171efe904c860f2b2294f6`.

## Evidence and next theorem

`VERIFY_R35_COMPACT.py` executes the exact S23 interval certificate using R34's pinned rank/count implementation. The expanded standalone generator, second-family regression, integration checker, exact certificate, full 298-run data and execution logs are included in the R35 research bundle retained in this session; the relevant condensed checked evidence is below in `RUN_EVIDENCE.md`.

The general mathematical theorem is conditional on the declared Farey stage and exact source-count interface. Independent review and complete bit-complexity accounting remain open. Next: batch multiple ownership counts at a single endpoint; prove output-sensitive bit complexity; test larger `m` and alternate irrational enclosures while preserving the source/observer relation. No mathematical acceptance or shared Task CLAIM is asserted.
