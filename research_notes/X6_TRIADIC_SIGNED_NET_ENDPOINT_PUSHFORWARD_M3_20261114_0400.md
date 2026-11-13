# X6 signed triadic incidence → six-axis net endpoint: all-m criterion and exact m=3 census

Date: 2026-11-14. Parent objective: `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Scientific status: **AUTHOR-PROVED (finite labelled-incidence model) / INDEPENDENT EXACT-INTEGER CHECK PASS / UNREVIEWED / NOT_ADMITTED**.

This unit follows the verified prior note `research_notes/X6_TRIADIC_BRC_ALL_M_FEASIBILITY_SIGN_MULTIPLICITY_20261114.md` (Git blob `6216c7db82e62e354a7d2279b9acece77ff7b693`); the original checker is `experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py` (Git blob `5d0f2cb88a0d4e437b5025e9050e3044f7831cd4`). Frozen Task inputs: Source P000 V5 / centered signed X6 at `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparator `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Global worldview P000 V4 remains a separately scoped account-level statement.

## Mathematical object and observer typing

One *labelled triadic incidence event* chooses a 3-element subset of the six native axis labels and independently assigns a sign ±1 to each selected axis. Repeated event types are allowed; **this combinatorial event alphabet is not asserted to exhaust admissible P000 native force-closure or temporal Cell transitions**. An ordered length-`m` word retains the full sequence of signed axis triples, producing:

- a 12-slot nonnegative signed-incidence vector `d=(d_(i,+),d_(i,-))`, with `sum d=3m`;
- a six-slot signed net displacement `z_i=d_(i,+)-d_(i,-)`, in the affine `Z^6` coordinate difference domain;
- the *word multiplicity* `T_m(z)` in this specific labelled-event algebra.

Neither `d` nor `z` is a complete ordered history or native physical state. The map to `z` is a declared many-to-one endpoint observer; retain exact `d`, event order, branch/source IDs, and later-observer requirements when applicable.

## Theorem A: exact feasibility of any net endpoint

For every integer `m>=0` and `z in Z^6`, put `a_i=|z_i|`, `A=sum_i a_i`. The following are **necessary and sufficient** for some ordered `m`-event labelled signed-triad word to end at `z`:

1. `a_i <= m` for each of the six axes;
2. `3m-A` is a nonnegative even integer;
3. `K=(3m-A)/2 <= sum_i floor((m-a_i)/2)`.

**Proof.** For any word let `D_i=d_(i,+)+d_(i,-)`; then `D_i=a_i+2k_i` with integers `k_i>=0`, `D_i<=m` and `sum_i D_i=3m`. Thus `sum_i k_i=K` and `k_i<=floor((m-a_i)/2)`, establishing necessity. Conversely, if these inequalities hold, choose `k_i` within the individual integer intervals with prescribed sum `K` (the Minkowski sum of integer intervals is the full integer interval). Then `D_i=a_i+2k_i` satisfies `sum_i D_i=3m` and `max_i D_i<=m`. The already-proved all-`m` unsigned triadic decomposition theorem supplies an ordered triple-incidence sequence. Assign `d_(i,+)=(D_i+z_i)/2` positions of each axis positive, and the remaining positions negative. This yields precisely `z`. Boundary case `m=0` gives the unique endpoint `z=0`. QED.

## Theorem B: exact typed pushforward multiplicity

Let `U(D)` denote the number of ordered *unsigned* 3-axis-incidence words with axis degrees `D` (with `U(0)=1` and the original triad-removal recurrence). Define `k` over the integer solutions in Theorem A. Then for all `m>=0` and `z in Z^6`,

```
T_m(z) =
  sum_{k_i>=0, sum_i k_i=(3m-sum_i|z_i|)/2, |z_i|+2k_i<=m}
    U((|z_i|+2k_i)_i)
    * product_i binom(|z_i|+2k_i, (|z_i|+2k_i+z_i)/2).
```

The sum is zero when Theorem A's conditions fail. Each term counts first an exact unsigned incidence history and then its independent per-axis sign choices, and distinct `k` yield disjoint exact 12-slot signed-degree fibres. This is the pushforward of the prior exact `N_signed(d)` count under `d → z`. Equivalently, with commuting Laurent variables `X_i`,

```
T_m(z)=[X^z] (sum_{S subset {0,...,5}, |S|=3} product_{i in S}(X_i+X_i^{-1}))^m.
```

This is **not** the free signed *primitive single-axis* BRC length-`3m` count; the three-axis grouping and event order are part of its type. It is also not an unrestricted native triadic force-closure count.

## Executed exact integer census and independent check

Companion code: `research_checks/X6_TRIADIC_SIGNED_NET_ENDPOINT_PUSHFORWARD_M3_20261114_0400.py` at Git blob `3d36776f7087e39f81cd503003b3d6c06711d113`, main creation commit `fca66554de5ab55b623097d84710081e50cb33e3`. Exact bytes matched the locally executed Python program (local `git hash-object` equals remote Git blob); run exited code 0.

```text
PASS_X6_TRIADIC_12_TO_6_ENDPOINT_PUSHFORWARD_M3
endpoint_count_by_m / total_words / maximal_fibre: [(1, 160, 160, 1), (2, 3477, 25600, 160), (3, 26440, 4096000, 4320)]
m2_origin_two_event_loops: 160
m3_origin_three_event_loops: 0
m3_maximal_fibres: 12 at signed unit endpoints
m3_L1_bands (norm, endpoints, words): ((1, 12, 51840), (3, 292, 656160), (5, 2232, 1683360), (7, 8064, 1369440), (9, 15840, 335200))
validation: exact integer DP vs independent 12-slot incidence summation
```

The independent methods were: (1) repeated convolution by all 160 distinct signed event vectors, which records the **six-slot net endpoint** directly, and (2) the independent signed-degree fibre formula using `U(D)`, exact binomial coefficients and bounded nonnegative `k`. They agree at each of all `160+3477+26440=30077` reachable endpoint states across `m=1,2,3`, and the feasibility test agrees with the complete `[-m,m]^6` candidate grid for each such `m`.

For exactly three events, the distinct net endpoint count is **26,440**, total ordered histories **4,096,000**, and the largest fibre size **4,320**, attained at exactly the 12 signed unit-axis endpoints. The complete census by `L1(z)` is:

| `L1(z)` | Distinct net endpoints | Ordered event words |
|---:|---:|---:|
| 1 | 12 | 51,840 |
| 3 | 292 | 656,160 |
| 5 | 2,232 | 1,683,360 |
| 7 | 8,064 | 1,369,440 |
| 9 | 15,840 | 335,200 |
| **Total** | **26,440** | **4,096,000** |

A minimal observer-loss witness is `m=2,z=0`: there are **160** distinct ordered signed event histories, arising from the first signed triad and its opposite; their 12-slot incidence vectors range over **20** different supports, each with count **8**. Thus using only net displacement as the *history* would erase branch, signed degree, intermediate trace and multiplicity information. For `m=3`, `z=0` is forbidden by the exact parity condition, not a numerical accident.

## Additional frozen source-consumer inspection (bounded)

At exact pre-rebase `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, inspected actual implementation lines, without rerunning these four historical checks:

- `experiments/brc_dominant_degeneracy_quotient_check.py` blob `33740d338fdc0459bb5ef07a9afc01892fae4752`, lines 20–66 and 168–204: `max` is over positive rational histogram weights; ties aggregate path multiplicities. **KEEP / PRESERVE_PATH_BRC** at inspected sites; not a native signed-axis `argmax` coercion.
- `experiments/brc_weighted_multiplicity_tower_check.py` blob `28618135c77939cfd90cbcc84a44a3de75767393`, lines 90–158: nonnegative rational path statistics and positive edge supports. **KEEP / PRESERVE_PATH_BRC** in the inspected graph model.
- `experiments/brc_moment_length_safe_port_transfer_check.py` blob `6367f1eccb7e32a3b6af708056f84dd901cae346`, lines 112–171: formal moment matrices and Schur boundary reduction; subtraction belongs to rational matrix algebra. **KEEP / PRESERVE_PATH_BRC** within that typed linear-algebra model.
- `experiments/brc_newton_fiber_sum_operation_safe_quotient_check.py` blob `16b0e572f4d1263f709fd85c584b415c2c35ae91`, lines 34–64 and 146–177: signed **Fraction coefficient** cancellations inside explicitly defined residual coordinate fibres, not cancellation of positive Native BRC multiplicity. **KEEP / PRESERVE_OBSERVER** for inspected operation-safe Newton quotient.

These are exact *site-scoped* provenance findings. They do **not** close the unresolved historical wrong-call claims `LP011` native signed-axis dominance or `LP019` positive path counts used as signed cancellations, nor the complete 28-LP source/consumer closure.

## Continuation state and verification boundary

- Owner/source bridge `onhour-20261114-03-x6-read-continuation-v1` returned **SUCCEEDED**, `phase=TYPED_FRONTIER_REQUIRED`, `execution_authorized=false`; no new CLAIM/open was made.
- Historical Researcher `EM-X6-FB6990` and SID `MCP-082892eb480e45dea6d4b9fcc0491034` remain **source provenance only** for this invocation. Native own-session recovery is a read-only projection and grants no current ownership. No old session key is adopted; no Activity, Native semantic PROGRESS, Result/freeze or Driver review is asserted.
- Parent inputs P000 V5 and Source `59538f...` baseline, old `fd2bcff1...` comparator, and already accepted R062/R063 scientific evidence remain frozen.
- **Completed this invocation:** code-level two-route exact check and all-`m` endpoint criteria; five-band m3 census; four bounded frozen-source classifications; code and note GitHub publication/readback.
- **Unfinished exact unit:** locate the *actual* path from legacy LP011/LP019 caller arguments to any signed native endpoint or Cell consumer, and establish `KEEP/RETYPE/REVISE` with source-line witness. Then close the actual 28-LP dependency ledger and pass complete evidence to independent Driver `REQUEST_REVISION`.
- **No-repeat set:** original signed X6 / coordinate / cover complete regressions, G25/PathSqrt certificate, accepted R062 Stage0 and related historical numerical returns, original all-`m` signed degree theorem; do not repeat this m3 exhaustive census.
- **Native action when lawful:** first resolve true logical-conversation identity and the current task authority via canonical continuation/dispatch; check ownership before preparation/CLAIM/open. Until then this report is **GitHub-persisted author-side portable evidence**, with `REGISTER_PENDING / SYNC_DEBT` for the present real invocation. Do not use the maintenance `chatgpt-hourly-enterprise-math-20260921` lane or take another owner's SID/CLAIM.

The original hourly automation schedule and notification settings were not edited.
