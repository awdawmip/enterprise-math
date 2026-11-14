# X6 LP019 — Exact signed native versus diagonal-observer BRC return fibres

Date: 2026-11-14 08:00 Asia/Hong_Kong. Parent task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Author-side result only: **UNREVIEWED / NOT_ADMITTED**, not a Source semantic PROGRESS, Result or Driver acceptance.

## Frozen semantics and actual source

This analysis uses the task's immutable native foundation `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03` (P000 V5, six signed primitive spatial axes, affine Cell torsor over `Z^6`, no ontically distinguished global origin). Historical comparison pin remains `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. The explicit current kernel examined is `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`, Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`, whose `endpoint_multiplicity(length,z)` counts signed primitive-axis words of exactly that length and native displacement. This is **not** the three-at-once triadic-force-event alphabet and is not an R062 positive-only benchmark.

Fix one chosen native Cell as the chart anchor for displacement calculations, not as a global origin. Write `e_i` for each of the six independent native directions. Let `W_n` be the `12^n` signed primitive words `(±e_i)` of length `n`; let `\Delta(w)` be their complete signed displacement. The full diagonal relative observer is `\rho(z)=z-\min_i z_i\,\mathbf{1}`, where `\mathbf{1}=(1,1,1,1,1,1)`. Its zero fibre is exactly `\{k\mathbf{1}:k\in\mathbb Z\}`; this **does not** identify those distinct native Cell endpoints.

## All-length exact theorem

Define `C_n(z)=#\{w\in W_n:\Delta(w)=z\}`, the native return mass `N_n=C_n(0)`, and the relative-zero mass `Q_n=\sum_{\rho(z)=0}C_n(z)`. Then for every integer `n≥0`,

```math
Q_n=N_n+2\sum_{k=1}^{\lfloor n/6\rfloor}C_n(k\mathbf{1}).
```

For nonnegative `k`, the exact coefficient is zero unless `n≥6k` and `n-6k` is even. In the remaining case, put `t=(n-6k)/2`; then

```math
C_n(k\mathbf{1})=n!\sum_{u_1+\cdots+u_6=t\atop u_i\ge0}\prod_{i=1}^6 \frac{1}{(k+u_i)!\,u_i!}.
```

The same coefficient holds for `-k\mathbf{1}` by simultaneous reversal of every primitive letter.

**Proof.** Each signed primitive word has well-defined counts `p_i,q_i≥0` of `+e_i,-e_i`. Displacement `k\mathbf{1}` requires `p_i-q_i=k` for each `i`. For `k≥0`, write `p_i=k+u_i, q_i=u_i`; total length is `n=6k+2\sum u_i`. Conversely every such nonnegative six-tuple generates exactly `n!/\prod_i[(k+u_i)!u_i!]` distinct words by multinomial shuffling. Sum disjoint count tuples. The observer equation `\rho(z)=0\iff z=k\mathbf{1}` partitions the relative-zero fibre; the `k=0` term is exactly native return, and `±k` pair. This proves the identities without signed-amplitude subtraction or cancellation. The shortest non-native diagonal endpoint has `L_1=6`, hence **`Q_n=N_n` for every `n<6`**, while `Q_6-N_6=2\cdot6!=1440`; for odd `n` both counts vanish.

This is an exact BRC pushforward/counting theorem under the declared native alphabet. It is *not* a theorem that quotient endpoints preserve full path identity, future legal compositions, time-ordered provenance or physical dynamics. In particular the surplus counts positive-length paths to different native Cells, not genuine native loops, nor a negative mass to be cancelled. The 20-chart/selected-three-axis carrier return `111\mapsto0` at length 3 is a **different restricted observer**; the full six-axis diagonal threshold here is 6.

## Actual exact integer computation: independent DP and coefficient sum

Executable: `research_checks/X6_LP019_SIGNED_NATIVE_DIAGONAL_OBSERVER_RETURN_FIBERS_20261114_0800.py` at commit `8ce5e70d6373561d22644edeb380493972b4cea7`, Git blob `8c1fa14e9b52b83b78179ba2c5302dc9ef8f337e`, local SHA256 `2bea9eebf624a189c440605342bbb52c58dedf0dfe53fc61f115bb906bcb7899`. The published bytes were fetched back and **match the executed local Git blob exactly**. Python standard library only, integer arithmetic and assertions enabled; `exit_code=0`, `PASS_X6_SIGNED_BRC_DIAGONAL_FIBER_EXACT`. Two independent calculations were compared: (i) exact native-endpoint dynamic programming from the 12 distinct signed generators, and (ii) the separate factorial/composition formula above. Every length `0…10` was exhaustively covered by DP; the polynomial identity itself does not rest on finite enumeration.

| n | native endpoint states | native zero N_n | relative zero Q_n | excess Q_n−N_n |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 |
| 1 | 12 | 0 | 0 | 0 |
| 2 | 73 | 12 | 12 | 0 |
| 3 | 304 | 0 | 0 | 0 |
| 4 | 985 | 396 | 396 | 0 |
| 5 | 2668 | 0 | 0 | 0 |
| 6 | 6321 | 19920 | 21360 | 1440 |
| 7 | 13504 | 0 | 0 | 0 |
| 8 | 26577 | 1281420 | 1523340 | 241920 |
| 9 | 48940 | 0 | 0 | 0 |
| 10 | 85305 | 96807312 | 127652112 | 30844800 |

No claim of original `check_signed_brc.py` execution is made by this new checker; its native endpoint formula is consumed at source-theorem level. This newly executed checker is not the R061/R062 original native benchmark.

## Concrete LP action and continuation

Add `LP019_SIGNED_X6_RELATIVE_ZERO_FIBRE` to the bounded consumer ledger as `KEEP_NATIVE_BRC_WITH_EXPLICIT_OBSERVER_FIBRE`; keep original current `signed_brc.py` native return semantics unchanged. Any future caller deriving native zero-loop counts from `\rho\)-zero counts at length ≥6 must be repaired only after an **actual** offending consumer is identified. The alleged pre-rebase LP019 signed-cancellation wrong caller and LP011 signed-dominance wrong caller are still `UNRESOLVED_PROVENANCE`; finite-source search does not invent an offender. Preserve historical 72, signed three-axis N25 30/846, local three-axis 111/6, R062 accepted positive-sector certificate, all prior exact regression proofs, and independent Driver's `REQUEST_REVISION`.

Original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, last recorded own CLAIM `MCP-899eb9f77ad9eebb90eb5f73`, run `RUN-87968b801c1dacea28269652`. Original semantic publish request `onhour-20261114-0710-x6-chart-event-progress-v1` has **FAILED / INVALID_UPLOAD_SET** (do not replay). New exact read `onhour-20261114-0805-x6-exact-current-continuation-v1` was **QUEUED / WAIT_ORIGINAL** when this note was prepared; it is a read projection and not current write authority. Before native publication, finish that original receipt and fresh claim/resume check, follow current `em_execution_publish` upload schema with actual complete own-session upload and current generation. New report/code persisted through GitHub as author-side Source research, not Native semantic PROGRESS.

Next smallest research action: inspect actual current downstream invocation sites of `signed_brc.endpoint_multiplicity` and relative/diagonal group quotient, identifying which (if any) projects native loop predicates through `\rho\). Record caller/function/line and type each consumer as KEEP/RETYPE/REVISE. Continue original 28-row dependency coverage without redoing settled positive-sector tests.


## Bounded current consumer trace and novelty boundary (08:12+08)

The following **complete current-main source bodies** were read with the connector and typed. Exact Git blob observations: `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` `300a96e3dc24bf6fff73743037a0347a8bc83176`; `src/enterprise_math/diagonal_quotient.py` `a527e347e33d0a0039258a9b25f48b1f1466d149`; `scripts/diagonal_quotient_normalization_check.py` `095d37643b2a8aa134ed5cd91926040b90bd123a`; `research_checks/X6_LP026_SIGNED_RELATIVE_C6_PARITY_BRC_20261112_ONHOUR.py` `08d0cd5c2720410d9a938c49df830d90573b408f`; `research_checks/X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_20261113_ONHOUR.py` `a82b8cfb6039531aec2266e283a5277ab20f7c4c`; `research_checks/X6_LP019_TRIADIC_EVENT_NATIVE_VS_RELATIVE_RETURN_20261113_1000.py` `3db88a103a02e7aca6bec96a513b65939a8553b4`. This is a six-file complete-body **source audit**, not six original-executable runs or repository-wide usage enumeration.

- Native signed BRC `signed_brc.py`, lines 38–52, `endpoint_multiplicity(n,z)`: **KEEP_NATIVE**. It uses all six raw signed coordinates and retains exact endpoint length counts. Its `return_multiplicity(n)` (lines 72–73) calls native zero `z=0` only; it does *not* treat an observer-zero fibre as a native zero loop. No patch.
- Three-axis derived quotient module `diagonal_quotient.py`, lines 1–15, 44–88: **KEEP_TYPED_REPRESENTATION**. It explicitly rejects interpreting its `Z^3/Z111` quotient as native Cell identity. It is not even the six-axis `Z^6/Z111111` observer of the all-length theorem. Original checker `diagonal_quotient_normalization_check.py`, lines 2–6, 54–88 tests only derived representation laws. No patch.
- Existing author-side signed-relative checker `X6_LP026_SIGNED_RELATIVE_C6_PARITY_BRC_20261112_ONHOUR.py`, lines 34–51 and 67–85: **KEEP_TYPED_RELATIVE_NBRC**. It already contains a general formula summing native endpoint histograms over hidden diagonal lifts `h`; in particular it **already recorded the n=6 relative-zero count 21,360**. The present work is a direct all-length *closed diagonal-zero-fibre specialization* of that known construction, with the exact first-native/observer discrepancy criterion, explicit positive excess and independent lengths 0…10 DP. Do **not** claim novelty of a generic signed-relative endpoint formula or the n=6 numeric count.
- `X6_LP019_FCC_SIGNED_BRC_PUSHFORWARD_20261113_ONHOUR.py`, lines 35–77: **KEEP_TYPED_FCC_PUSHFORWARD**. It maintains separate native `Z^6` and 3D FCC carrier distributions, verifies the pushforward rather than identifying native Cell endpoints. Its FCC carrier quotient is **not** the full 6D common-diagonal observer in this theorem.
- `X6_LP019_TRIADIC_EVENT_NATIVE_VS_RELATIVE_RETURN_20261113_1000.py`, lines 1–6, 20–48: **KEEP_TYPED_TRIADIC_EVENT**. The 160-vs-200 two-**triadic-event** zero-count contrast uses a separate 160-letter event alphabet and discloses that it is not the signed primitive-axis BRC. It cannot be substituted for `Q_2=N_2=12` in the primitive 12-letter model.
- None of the inspected six real current files uses a positive N-BRC multiplicity as a signed *amplitude* or cancels opposite positive path counts to infer native non-reachability. No actual LP019 historical wrong caller is established by these exact reads. The null conclusion is bounded to these six named bodies and their inspected interfaces.

Readback/source authority: GitHub connector `fetch_file` on current `main`; historical scientific baseline unchanged. Independent Driver `REQUEST_REVISION` and the broader 28-LP consumers remain open. The new computed exact fibre formula is **AUTHOR-PROVED / EXACT-INTEGER-CHECK PASS**, not independently reviewed or Native-admitted.

