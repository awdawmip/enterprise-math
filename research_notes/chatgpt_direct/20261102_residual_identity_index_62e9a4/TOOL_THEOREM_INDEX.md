# Tool and conditional theorem index — residual identity index

Source conversation: 平方和正交研究. Package event: `EM-20261102-RESIDUAL-IDENTITY-INDEX-62E9A4`.

**Status: AUTHOR_CHECKED / UNREVIEWED / CONDITIONAL.** This is an extraction and preservation index, not independent mathematical acceptance, formalization, deployment, or a new research run. The source package itself records no new formal Research-Activity binding. Its compact project report is separately recorded at commit `b54c03dcbe647dc8ecd7f4f6d544168b07d100cd`, path `research_notes/chatgpt_direct/20261102_residual_identity_index_62e9a4/RESULT.md`; the local detailed `RESULT.md` is a different layout, not asserted byte-identical. Paths below are relative to the preserved package root.

## Reusable tools

| Entry | Actual interface / purpose | Preconditions and limits |
|---|---|---|
| `check_identity_index.py::Compiler` | `run(J, op)` for maintained bind/copy/drop and execute/valid; `dispatch(J, i, mode='exact', delete=True)` reads complete Boolean result registers and selects a fixed current-record port from full key `K=1+tM+c`. | Legal original source/current/reference tables; exact directory equals registered request key; closed-reference condition; stable sequential non-reentrant API or protected interval. An arbitrary stale directory is **not** safe in exact mode. |
| `Compiler.dispatch(..., mode='hint')` | Reads arbitrary hint bits; a 13-instruction PAIR checks both request and current endpoints; zero/out-of-range/mismatch falls back to the original full scan. | Same legal original tables, stable interval and closed-reference conditions; hint does not have to be accurate. Does not repair the hint. Full miss/fallback cost must be included. |
| `check_identity_integration.py::IdentityRing` | Extends inherited `PhaseRing`; keeps directory maintenance, read, endpoint check and commit inside the protected interval; uses real output feedback and private result delivery. | Inherits reliable feedback, cooperative writers, atomic primitives and call-drain contract. Demonstrated repetition/omission scope is three adjacent repeats per position and at most two omissions, not unrestricted fault tolerance. |
| CLI and fixed artifacts | Python 3.11+, standard library, bundled `parent/`; see `README.md`. Index CLI modes: `audit`, `costs`, `hints`, `failures`, `lifecycle`, `workload`, `scaling`, `programs`; integration modes: `ring_costs`, `ring_graph`, `empty_filter`. `PROGRAMS.json` stores six-slot compiled blocks/layout/candidates. | `encode`, `decode`, `expected` and domain enumeration are fixture/validation functions, **not** production lookup oracles. `--slots 2 --canonical` selects 142 renamed representatives, not the entire 1900-state domain. |

All state-changing primitives are inherited from the bundled original triadic kernel. Python address selection is an explicit feedback-control capability; its storage, addressing and physical realization are not free primitive operations. This is not a drop-in production/backend integration.

## Extracted propositions and proof locations

Let `d` be target count, `r` request slots, `M=r+1` local identifiers per target, and `q=ceil(log2(dM+1))`. Targets are finite candidate source triples, current source is a disjoint matching; reserve requires all three members free and release removes the containing event. Identity `(t,c)` is a registered finite reference, not a physical creation timestamp.

| Conditional proposition | Source proof / evidence | Boundary |
|---|---|---|
| Full-key directory invariant is maintained at complete API boundaries; subsequent finite stable/adaptive calls remain correct. | `RESULT.md` §2.1–2.3: bind writes only the unique occupied reference column, copy/drop preserve encoding, other operations preserve the reference key; boundary induction. `Compiler.__init__`, `run`. | Assumes original table/source invariant, uniqueness, cleared workspace and closed-reference registration. |
| Exact lookup costs `8q` empty, `8q+8` nonempty invalid or validity-only, `8q+10` valid execution. Thus this construction's query primitive count is `O(log(dM))`. | `RESULT.md` §3: actual bit reads identify key, current endpoint establishes validity, two-step commit; `Compiler.dispatch`, `costs.json`, `scaling.json`. | Does not make total storage, compilation, maintenance, feedback implementation, time or energy logarithmic. |
| A request-key-only directory, queried with current relations but without revisiting the original request, needs at least `dM+1` distinguishable states, hence at least `q` fixed binary bits. | `RESULT.md` §3.2: any two keys are distinguished by a current background retaining only the first; empty differs likewise. | Interface-specific information lower bound; not a universal lower bound for hinted verification that also reads the original request. |
| Arbitrary hints plus both-endpoint PAIR verification and fallback give the same projected final state as the original scan. | `RESULT.md` §4 and `hints.json`; `failures.json` supplies stale-current-key and wrong-target counterexamples to current-endpoint-only acceptance. | Hint hit `8q+15`; in-range miss `8q+13+parent scan`; zero/out-of-range `8q+parent scan`. Not guaranteed faster. |
| Declared workload can select an optional empty-first filter. | `RESULT.md` §5.1; `check_identity_integration.py::empty_filter`, `empty_filter.json`. Extra average primitive count is `8-8qp`; gain requires empty fraction `p>1/q`. | A conditional cost identity, not an empirically established workload probability. |
| Protected integration preserves full source/request/directory/gate/private-answer/workspace state under the stated cooperative contract. | `RESULT.md` §6; `IdentityRing`; `ring_execute_bind.json`, `ring_execute_restart.json`. | Two demonstrated operation pairs and stated omission/repetition bound. Holder stalls, out-of-call old effects and noncooperative writers retain inherited limits. |

Full costs are in `RESULT.md` §5, `costs.json`, `lifecycle.json`, `workload.json` and `ring_costs.json`: six-slot/three-target full-key inventory is 285 members/1724 candidates; protected two-participant inventory is 322/1752. Bind, copy, drop, migration, empty-query and miss overhead are not omitted. Small configurations can lose to the parent scheme. The report acknowledges LLVM SparseSet as engineering context; general indexing/cache verification is not claimed novel. P000/X6 Cell/field/support correspondence remains a separate bridging question.

## Existing author-test scope (not rerun during extraction)

`SUMMARY.json` records 12 output modes, **251,348** new-layer assertions and **1,427,252** inherited gate assertions, separately counted:

- All 77 one-slot preparations ×21 operations = 1,617 API comparisons; 231 bit readouts.
- 142 consistent-renaming two-slot representatives ×37 operations = 5,254 comparisons; 1,136 bit readouts.
- 142 representatives ×2 requests ×16 hints = 4,544 hint projection checks.
- Eight scale configurations /557 executed preparations; six-slot lifecycle 20 rounds, 322 APIs, 22,524 primitive commands.
- Ten protected cost traces; execute/rebind graph: 27,911 aggregate prefixes/86,412 edges; execute/release-recreate: 28,550/88,102. These are evidence under the stated contract, not independent audits.
- `VALIDATION_ATTEMPTS.json`: the full 1,900 two-slot preparation attempt timed out, **no passed claim**. Interactive-session attempt did not start.
- `CLEAN_RECHECK.json`: same-author clean-dependency rerun of only `costs` and `failures`, matching full JSON; not independent verification and excluded from primary counts.

## Preservation integrity / publication screening

Read-only extraction check, 2026-11-02 UTC: all **62 MANIFEST entries** match declared byte lengths and SHA-256; **63 actual files**, with `MANIFEST.json` the sole unlisted file; no missing entries. Original files were not changed and no research/test program was executed during this extraction.

Bounded plaintext screening across the 63 files found no private-key headers, common GitHub/AWS token forms, bearer literals, quoted credential assignments, email addresses or user-home paths. Reviewed provenance/publication metadata contains repository commits, research event IDs and historical gateway status, not credentials. This pattern/content check is not a guarantee against every possible secret or an expansion of sharing authority; the publishing owner retains the user's permitted destination and final review.

EM-Source-Status: Read=Verified (local package, 62 manifest entries); Write=Written and verified (local draft only); Source=⚠ Not written by this extraction subtask (remote publication assigned to the publishing owner).
