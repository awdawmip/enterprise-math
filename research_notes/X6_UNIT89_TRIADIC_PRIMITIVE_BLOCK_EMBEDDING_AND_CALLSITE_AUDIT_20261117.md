# X6 Unit89 — typed triadic-event / primitive-block bridge and consumer audit

Date: 2026-11-17. Mother: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION; publication TP2-B4A441B23DA3159232C2.

State: AUTHOR-EXACT / FINITE INTEGER EXECUTED / SOURCE-CALL-SITE-INSPECTED / UNREVIEWED / NOT_ADMITTED. Authored portable science only; original X6 Native activity and semantic PROGRESS are pending independent owner authorization.

## Frozen objects and operation types

P000 V5 scientific pin: 59538f585d037d09ef687b28715c4bc1a3f9fe03, native X6 signed integer displacement. History pin: fd2bcff10ca6e147348b6c1236027fc0d2877df3. Frozen primitive signed BRC source: experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py, blob 300a96e3dc24bf6fff73743037a0347a8bc83176.

The current composite source experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py, blob 5d0f2cb88a0d4e437b5025e9050e3044f7831cd4, lines 8-16 and 91-105, uses 20 distinct 3-axis supports times 8 signed assignments, hence 160 labeled *simultaneous triadic events*. These are not automatically 160 primitive physical axes or serial three-tick physical programs.

## Exact theorem and proof (all lengths)

Let the six named Laurent variables be x_i, and y_i=x_i+x_i^(-1). Define P=sum_i y_i (12 primitive signed operations), Q=sum over i<j<k of y_i*y_j*y_k (160 signed triadic event types). For L>=0 and z in Z^6 let T_L(z) be the coefficient of x^z in Q^L, let A_L(z) be the coefficient of x^z in P^(3L), and let D_L(z) count the signed primitive words of length 3L whose *aligned* consecutive triples each contain 3 distinct named axes.

Then D_L(z)=6^L*T_L(z), for **every** z and L. Each signed triadic event has precisely 3!=6 linear orders in its three distinct-axis primitive signed letters. Independently choosing each block order is a bijection with all such constrained primitive words; terminal signed displacement is unchanged. For any terminal-only observation O(z), summing over an O-fiber preserves this identity. With commuting positive rational signed-axis weights factorized across letters, each serialization retains the same product, giving the corresponding weighted identity.

The unrestricted primitive relation is P^3=6Q+H, with H a Laurent polynomial with *nonnegative integer* coefficients: it counts primitive triples containing a repeated axis. Thus A_L(z)>=D_L(z) pointwise. An explicit separating endpoint is z=(3,0,0,0,0,0) at L=1: +e_1 repeated three times is unrestricted but no distinct-axis aligned triad realizes it. For even L>=2 strict separation occurs also at the zero Cell: pair the repeated triple +e_1,+e_1,+e_1 with -e_1,-e_1,-e_1, filling remaining even blocks with cancelling pairs. For odd L both exact-Cell return and any diagonal-cover return vanish by parity, since 3L is odd and a diagonal endpoint has even coordinate sum.

**Scope:** this is a signed chart terminal-displacement/commuting-multiplicity theorem; it does not equate a simultaneous triadic event with any chronological legal native three-microstep realization. Noncommutative operators, intermediate-state observers, operation legality, branch IDs, and event-time observers require a separately justified bridge. No P000 change.

## Executed exact integer evidence

Independent Python generated all 160 signed event vectors and all 160^2=25,600 two-event histories. It generated the 960 signed *ordered* distinct-axis primitive blocks (6 serializations per triad) and enumerated all 960^2=921,600 six-step aligned-block pairs. For all 3,477 resulting terminal signed displacement classes, the blockwise multiplicity agrees exactly with 36 times two-event triadic multiplicity. Separately it computed all 12-direction unrestricted primitive six-step transition multiplicities by sparse integer DP, plus exact four-event and twelve-primitive return coefficients.

| Observer | Two composite triads | Six aligned distinct primitive steps | Six unrestricted primitive steps |
|---|---:|---:|---:|
| Exact Cell return | 160 | 5,760 | 19,920 |
| Relative / mod-1 depth cover | 200 | 7,200 | 21,360 |

The unrestricted-minus-constrained gap is 14,160 for each observer. At four triadic events, native Cell return is 460,320; modulus-2 depth cover return is 464,040, with 1,860 additional event words at each signed diagonal endpoint. Twelve-step constrained primitive Cell return is 596,574,720, compared with unrestricted primitive Cell return 8,175,770,064.

The separately executed checker has SHA256 cf65bfc5c422a4483468293f0c97ba61aeb0c2798eb640cd73d834f8b6a8dcca, and its exact JSON certificate has SHA256 9ab0a08f3adaee005bf94717415ffb827b09f6d1f057174f1e12f9e643151a61; normal Python, -O and -OO executions gave identical output. No original native R063/Helly benchmark was reexecuted.

## Scoped real source-call audit, with exact Git blob and lines

- experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py at d5f6dfcfd0dedbe46feae3bc1b227185af417c2f: lines 10-14 load frozen signed_brc.py; lines 55-56 correctly call shortest_event_count and shortest_path_multiplicity on a two-primitive displacement; lines 133-146 independently count **unsigned** ordered triadic degree decompositions. This is the nearest confirmed actual native primitive/triadic consumer, and no conversion of 160-event return to primitive endpoint_multiplicity occurs.
- experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py at 5d0f2cb88a0d4e437b5025e9050e3044f7831cd4: lines 10-16 and 91-105 define the signed composite event alphabet/counts, without a native signed_brc or cover return coercion.
- experiments/x6_native_event_time_v1_20260906/check_event_time_markov.py at df0df29327fe8c969ad9e4c758d5c7372ecd65cd: lines 37-39 explicitly distinguish its model's two relation ticks and six primitive force occurrences; those are not the untyped 3L serialization clock.
- experiments/x6_native_event_trace_v2_20260906/check_event_trace_partial_order.py at 252c9dcdefe0040afbeef8676384366973a287cb: lines 22-28 concern generic commuting independent events, not permission to serialize these 160 events.
- experiments/x6_triadic_interaction_defect_v18_20260906/check_triadic_interaction_defect.py at dac16eeaf4174fe00e408ff8dc1b73c80c886b7b: lines 12, 60, 133-142 study the unsigned 20-support/15-pair shadow, not signed primitive return.

No current incorrect LP011/LP019 call is established by this bounded audit. Those historical assertions retain UNRESOLVED_PROVENANCE pending original source path/line or independent Driver REQUEST_REVISION. Further 28-LP actual downstream consumers need exact call tracing and selective correction only on proven misuse.

## Original Native identity and admission boundary

Historical X6 author conversation chatgpt-research-onhour-enterprise-math-20260923, SID MCP-082892eb480e45dea6d4b9fcc0491034, claim MCP-579c8e23625448582b421831, run RUN-fb25028676f9692ab1bacaee, activity RA-5E3FE1E761E4963EC461A892 with 106 last verified events. Original bridge #6994 SUCCEEDED but projects D25 SID, and #6995 SUCCEEDED exact X6 continuation read gives execution_authorized=false and a typed-preparation route. No X6 current authenticated writer established; no native PROGRESS/Activity or independent review/admission claimed. New neutral GitHub science retains separate provenance; scheduling and notifications unchanged.
