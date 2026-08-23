# Enterprise Math Tool Invocation Protocol

Status: `ACTIVE / UNIVERSAL REUSE-BEFORE-INVENTION PROTOCOL / V2`
Date: `2026-08-23`
Machine policy: `tool_invocation_policy.json`
Tool registry: `enterprise_toolbox_registry.json`
Base method inventory: `research_method_inventory.json`
Method addenda: `research_method_inventory_addenda/*.json`
Executable router: `tools/enterprise_toolbox.py`
Logic-closure checker: `tools/check_toolbox_logic_closure.py`

## 1. Purpose

Enterprise Math has accumulated reusable mechanisms under route names, theorem
names, report names and source-module names. A researcher who does not know
that history can accidentally rederive a quotient compiler, precision calculus,
collision spectrum, finite certificate, holonomy diagnostic, toppling
stabilizer, Morse reducer or path-closure engine and call it new.

The closed research flow is:

`QUESTION/TASK`

`-> IDENTIFY INFORMATION STRUCTURE`

`-> TOOL COVERAGE LOOKUP`

`-> REUSE / COMPOSE / EXTEND / CONFIRM GAP`

`-> RESEARCH`

`-> METHOD HARVEST AT ACCEPTED RETURN`

`-> REGISTRY + INVENTORY/ADDENDUM UPDATE`

`-> EXECUTABLE INTEGRATION WHEN CALLABILITY IS CLAIMED`

`-> ROUTER + REGRESSION + HUMAN INDEX`.

Freeze:

`NEW_MECHANISM_BY_DEFAULT = FORBIDDEN`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

`ACCEPTED TOOL -> ROUTABLE -> CALLABLE`, unless it is explicitly classified
`INTERFACE_ONLY` and never advertised as production-callable.

This protocol changes routing, not theorem ownership and not Foundation.

## 2. Understand first, lookup second

Do not preload the whole toolbox before understanding a task. Tool names can
anchor the problem formulation.

For ordinary `TASK_RESEARCH`, first read the exact task and the first necessary
dependency. Once the information structure is clear, perform the lookup before
constructing a new general-purpose method, helper calculus, quotient,
certificate, invariant or search engine.

Recommended command:

```bash
python tools/enterprise_toolbox.py coverage <plain-language need>
```

The router searches four layers:

1. curated global families in `enterprise_toolbox_registry.json`;
2. the backward-compatible base inventory `research_method_inventory.json`;
3. every dated shard matching
   `research_method_inventory_addenda/*.json`;
4. every current `src/enterprise_math/*.py` module by
   AST/docstring/public API, without importing it.

Duplicate `method_id` values across the base and addenda are rejected. A method
does not become invisible merely because it was harvested after the base
inventory was created.

## 3. Coverage verdicts

Every serious method choice resolves to one of:

### `REUSE_EXISTING_TOOL`

The existing tool already has the required typed input/output contract. Use it
and cite its owner/source.

### `COMPOSE_EXISTING_TOOLS`

No one family solves the problem, but a typed composition does. Preserve the
composition boundary rather than minting another family name.

### `EXTEND_EXISTING_TOOL`

The old owner is correct but lacks one genuinely new operation or certificate.
Extend it without discarding its existing hard boundaries.

### `CAPABILITY_GAP_CONFIRMED`

A new family is justified only when the missing capability cannot be represented
as reuse, composition, specialization, alias or extension.

The gap record must state:

- families checked;
- base/addendum methods checked;
- executable modules checked;
- exact semantic mismatch;
- missing input/output contract;
- why composition or extension is insufficient.

### `NOT_APPLICABLE`

The task is object/theorem-specific and does not require reusable machinery.

## 4. Anti-duplication taxonomy

Do not create a new family when the difference is only:

- a historical name;
- a new application domain;
- a different filename;
- a specialized parameter regime;
- a wrapper around the same operator;
- a theorem instantiating an existing calculus.

Use alias, domain facade, specialization or subtool. A strict superset normally
extends the current owner. A new family is reserved for a genuinely different
semantic input/output contract or structural law.

## 5. Discovery-firewall timing

The reuse rule has one principled timing exception: a controlling role/task
protocol may delay current-tool visibility to protect independent discovery.

This covers:

1. FREE Phase A; and
2. a TASK taskbook that explicitly declares a blind-forward/source-whitelist
   firewall and names its raw candidate/no-go freeze point.

Before the declared freeze:

- do not expose the registry;
- do not expose the base inventory or addenda;
- do not run the router as a discovery prior;
- do not name current families merely to forbid them;
- obey the exact task-local source whitelist.

Immediately after freeze, the same execution must run current-tool dedup before
claiming method novelty or opening a tool continuation. Existing-tool collision
does not rewrite the frozen Phase-A packet; it determines Phase-B routing.

An ordinary task cannot self-declare blindness to skip reuse.

## 6. TASKBOOK-ONLY LAST MILE

A strict taskbook-only packet may not have read `AGENTS.md` or this protocol.
Therefore every newly authored or re-reviewed dispatchable taskbook carries:

`tool_invocation_policy = INHERIT_GLOBAL`.

This compact field means:

- ordinary TASK work performs lookup after understanding task semantics and
  before inventing general machinery;
- a taskbook-declared discovery firewall keeps the catalog hidden until its
  named freeze, then makes dedup mandatory;
- the field does not preload tool names into blind discovery;
- the taskbook body does not copy the entire repository policy.

`tools/research_taskbook.py new` writes the field.
`review` repairs it.
`audit --dispatch` rejects a missing or altered value.

This is the same kind of last-mile closure used for the mandatory final-response
identity footer: inherited policy must remain visible even when the execution
packet says “只读取任务书”.

## 7. Driver and Steward gates

For every meaningful return, Driver intake includes:

`EVIDENCE AUDIT -> METHOD HARVEST -> TOOL DEDUP -> VERDICT + ROUTE`.

Before opening a new method/tool task, the Driver resolves:

`REUSE / COMPOSE / EXTEND / GAP_CONFIRMED / NOT_APPLICABLE`.

Before a Steward accepts shared machinery, the Steward checks the current
registry, base inventory, dated addenda and executable source and preserves exact
theorem/tool ownership.

A classical tool packaged for Enterprise semantics may be valuable without
being new mathematics.

## 8. Post-return harvest

Every Driver-accepted or Steward-accepted return receives one classification:

- `GLOBAL_TOOL_FAMILY`;
- `GLOBAL_SUBTOOL`;
- `DOMAIN_FACADE`;
- `DOMAIN_OPERATOR`;
- `RESULT_ONLY`;
- `CANDIDATE_NOT_TOOL`;
- `DUPLICATE_ALIAS`;
- `NO_TOOL_PAYLOAD`.

When routing changes, update the family registry and either the base inventory
or a dated addendum. The base inventory remains backward-compatible; new
harvests should normally use dated addenda to avoid one permanent merge hotspot.

If a result has no reusable method, persist that fact and do not create a
ceremonial family.

## 9. Tool-family, method and executable layers

The family registry answers:

> Which mathematical mechanism owns this problem shape?

The base inventory plus dated addenda answer:

> Which exact callable method, specialization, recent operator or negative
> boundary already exists?

The executable scan answers:

> Which current module can actually be called, even if curation lagged?

All three layers are required. Documentation alone is not callability.

## 10. Production callability gate

A production-callable accepted tool requires:

1. family registry entry;
2. base/addendum method record;
3. production source module;
4. executable-router discoverability;
5. deterministic regression;
6. human registry visibility;
7. semantic hard boundary.

An explicitly interface-only result may omit a production module, but then:

- its status must say interface-only;
- an exact checker/formal certificate must remain;
- no role may describe it as production-callable.

A downgraded result that is likely to be rediscovered—such as a domain
specialization or exact no-go—still enters the method inventory, but receives no
new global family number.

The machine gate is:

```bash
python tools/check_toolbox_logic_closure.py
```

## 11. Current T10–T12 closure

The 23 August tool-discovery intake is fully routed as:

- T10 — local redistribution/toppling/potential:
  `src/enterprise_math/discrete_laplacian_chip_firing.py`;
- T11 — discrete Morse/acyclic matching:
  `src/enterprise_math/discrete_morse_collapse.py`;
- T12 — idempotent path closure/Bellman:
  `src/enterprise_math/idempotent_path_closure.py`.

Weighted incidence energy is a T10 variational specialization, not another
family. Carrier Voronoi/Delaunay remains a domain operator. Current discrete
conformal/circle-pattern work remains an admissibility/no-go result pending
extra structure.

## 12. Semantic safety

A tool is invoked only at the strength of its declared input.

Examples:

- T4 cannot invent an observation map;
- T6 cannot decide what information should be forgotten;
- T7 cannot invent symmetry breaking;
- T9 holonomy does not select a unique repair;
- T3 cannot import carrier dependencies into native incidence;
- T10 potential is not automatically geometry or energy;
- T11 homology equivalence is not operation safety;
- T12 weights must be explicit and a path envelope is not automatically a
  metric.

`TOOL_USE != PREMISE_PROMOTION`.

## 13. Closed-loop invariant

The control-plane invariant is:

`CURRENT RESEARCH -> HARVEST -> TOOLBOX/INVENTORY/EXECUTABLE`

and

`NEW RESEARCH -> ROLE-TIMED TOOL LOOKUP -> REUSE/COMPOSE/EXTEND OR EXACT GAP`.

A useful method discovered once must become harder—not easier—to rediscover
wastefully under another name.
