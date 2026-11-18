# X6 Unit145 — historical FCC/HCP carrier dual-incidence optimized-guard boundary

Date: 2026-11-19. Task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`. Original onhour author: `EM-X6-FB6990` (SID `MCP-082892eb480e45dea6d4b9fcc0491034`).

**Status:** AUTHOR-SOURCE-VERIFIED / SOURCE-EXACT-GUARD-REPLICA-EXECUTED / UNREVIEWED / NOT_ADMITTED. This unit does not alter the frozen P000 six-axis signed-Cell model, the old FCC/HCP carrier definitions, or native historical R063 benchmark.

## Exact source

Current and frozen `scripts/check_p000_first_shell_polyhedron_classification.py`, Git blob `e58b287ae65eaadd8a805b5ebac84535b2cb5211`, unchanged on the frozen pre-rebase commit `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Source lines 61–67 define `dual_edges(Fc,E)` by collecting all facets incident to each carrier edge `e`, checking `assert len(inc)==2`, and returning a tuple of the facet indices. The same kind of assert appears in `analyze` at line 99. Its original accepted 12-site models have their own exact carrier polyhedral results; this audit makes no claim that those historical inputs violate incidence.

## Precise type and obstruction

For a pair `e={u,v}` and a list of carrier facets `Fc`, define the **incidence degree**

`deg_Fc(e)=|{k : e subseteq Fc[k]}|`.

The intended closed two-manifold dual-edge construction on each carrier edge requires `deg_Fc(e)=2`. This is a topological incidence contract for the 3-coordinate **carrier dual graph**, not six-dimensional native X6 primitive adjacency. The function relies only on an `assert` to enforce this contract.

Because CPython with `-O` and `-OO` removes `assert` bytecode, the same source function returns a non-edge tuple of length `deg_Fc(e)` when that degree is 0, 1, or 3. In ordinary execution, all three malformed inputs raise `AssertionError`.

Exact bounded witnesses, with the common queried edge `e=(0,1)`:

| Facets indexed from 0 | deg(e) | Normal | `-O` / `-OO` |
|---|---:|---|---|
| `{012},{013}` | 2 | `(0,1)` | `(0,1)` |
| `{012}` | 1 | rejected | `(0,)` |
| `{012},{013},{014}` | 3 | rejected | `(0,1,2)` |
| `{234}` | 0 | rejected | `()` |

**Theorem (source-exact scope).** For any finite facet list and any specified edge, the literal `dual_edges` implementation can only emit a 2-vertex dual edge for that edge when its facet-incidence degree is 2. Under optimized execution it never checks that premise, and for all non-2 degrees it emits a malformed tuple rather than rejecting it. Thus an optimized-mode success of this function is not by itself a certificate of carrier dual-incidence validity. The proof is directly by the function's list construction, assertion removal and tuple construction.

## Independently executed regression

Checker: `research_checks/X6_UNIT145_CARRIER_DUAL_EDGES_OPTIMIZED_GUARD_CHECK_20261119.py` at GitHub commit `90a4062ae0393c89f650bb07de3463766893ee5d`. Results: `research_checks/X6_UNIT145_CARRIER_DUAL_EDGES_OPTIMIZED_GUARD_RESULTS_20261119.json` at `1bef369cf40b78eb4f99604e16366a689bf76b1d`. The checker replicates **only** the source-exact 7-line function, uses unconditional `require` for its own test assertions, and executes the four input cases in normal, `-O` and `-OO` Python modes. All exit codes were 0; the mode-distinguished inner SHA256 hashes are:
- Normal: `caa700df12fdbbc869eb89d6ec16f20eb27d9968c369902cdae8f84c1a977f40`.
- `-O` and `-OO`: `c6662d6ed8253bbc378229aa8f10e7f51104c09c17e9b37eca87f32ab38e6837`.

Original historical program and original R063 benchmark were **not** executed. No unverified claim about the accepted FCC/HCP model output is made.

## Minimal consumer remedy and outstanding parent scope

A production or independent verification caller that must reject malformed dual incidence should use a non-optimized-away runtime guard (`if len(inc)!=2: raise ...`) before constructing the tuple. Do not patch a frozen historical file blindly. Verify the exact current caller/acceptance scope before modifying production code, and retain the old source as evidence.

This source-specific guard loss is distinct from prior R063 and triadic optimization checks; it does not prove the old LP011 signed-native argmax or LP019 positive N-BRC subtraction allegation. Those original caller locations, full 28-LP consumer coverage, and independent Driver review stay unresolved. Author Unit144 and Activity158 are retained; Unit145 is author evidence only, not an admitted or Source-native semantic checkpoint.
