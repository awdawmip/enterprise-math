# Enterprise Math Tool Invocation Protocol

Status: `ACTIVE / UNIVERSAL REUSE-BEFORE-INVENTION PROTOCOL / V2`
Date: `2026-08-28`
Machine policy: `tool_invocation_policy.json`
Tool registry: `enterprise_toolbox_registry.json`
Method inventory: `research_method_inventory.json`
Executable discovery router: `tools/enterprise_toolbox.py`

## 1. Purpose

Enterprise Math has many reusable mathematical mechanisms under route names, theorem names and source-module names. A researcher who does not know that history can accidentally rederive an existing quotient compiler, precision calculus, collision spectrum, certificate system or holonomy diagnostic and call it new machinery.

The default flow is:

`QUESTION/TASK`

`-> IDENTIFY INFORMATION STRUCTURE`

`-> TOOL COVERAGE LOOKUP`

`-> REUSE RESOLUTION`

`-> APPLY / EXECUTE / COMPOSE / EXTEND / CONFIRM GAP`

`-> RESEARCH`

`-> METHOD HARVEST AT ACCEPTED RETURN`.

Freeze:

`NEW_MECHANISM_BY_DEFAULT = FORBIDDEN`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

`TOOL_COVERAGE_LOOKUP != TOOL_USE`.

This is reuse discipline, not a theorem premise and not a Foundation change.

## 2. Understand first, lookup second

Do not preload the toolbox before understanding a task. Tool names can anchor problem formulation.

For ordinary `TASK_RESEARCH`, first read the exact task and first necessary dependency. Once the information structure is clear, perform coverage lookup **before constructing a new general-purpose method, helper calculus, quotient, certificate, invariant or search engine**.

Recommended lookup:

`python tools/enterprise_toolbox.py coverage <plain-language need>`

The router searches:

1. curated global tool families;
2. harvested methods/domain facades;
3. AST/docstring/public-API metadata from current `src/enterprise_math/*.py`.

The third layer discovers executable source but does not execute it.

## 3. Coverage verdict is only the first decision

Coverage resolves to:

- `REUSE_EXISTING_TOOL`;
- `COMPOSE_EXISTING_TOOLS`;
- `EXTEND_EXISTING_TOOL`;
- `CAPABILITY_GAP_CONFIRMED`;
- `NOT_APPLICABLE`.

A positive match is **not** proof that the tool was actually reused.

Every relevant match must then resolve to one of the machine-policy reuse states:

- `REUSE_APPLIED` — exact mathematical/tool interface was applied to the current task; no software execution was necessary;
- `REUSE_EXECUTED` — an existing executable implementation was actually run for the claimed computation/certificate;
- `COMPOSE_APPLIED` — concrete existing tools/methods were composed with their hard boundaries preserved;
- `EXTEND_EXISTING_TOOL` — the existing owner is correct but a genuinely missing capability must be added;
- `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE` — an adequate executable exists but cannot be executed in the current environment; do not claim it ran and do not relabel environment unavailability as a mathematical capability gap;
- `CAPABILITY_GAP_CONFIRMED` — exact required input/output capability is absent;
- `NOT_APPLICABLE`.

Minimum record:

- coverage verdict;
- matched tool/method IDs;
- reuse-resolution state;
- how the tool was applied/executed, or why not;
- hard boundary checked.

## 4. What counts as reuse

For a **mathematical calculus/theorem interface**, exact application of its declared law, hypotheses and hard boundary can be `REUSE_APPLIED`; code execution is not required merely to say the method was reused.

For a claim that depends on a **software computation/certificate**, finding the source module is not enough. If the environment can execute the existing implementation, run it and record `REUSE_EXECUTED` rather than silently rewriting a duplicate.

If the current chat/runtime cannot execute the repository implementation, record `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`. The researcher may still use the exact mathematical interface as reasoning input when appropriate, but must not claim executable validation occurred.

## 5. Anti-duplication taxonomy

Do not create a new family when the difference is only:

- historical naming;
- application domain;
- filename/package;
- specialized parameter regime;
- wrapper/facade;
- inability of the current chat environment to execute an otherwise adequate existing implementation;
- a theorem instantiating an existing generic calculus.

Route these as alias, domain facade, specialization/subtool, source reuse, or execution-unavailable state as appropriate.

A strict superset with one genuinely new operation normally extends the existing family.

A new family is reserved for a genuinely different semantic input/output contract or structural law.

## 6. Discovery-firewall timing

The lookup rule has one principled timing exception: a controlling research protocol may explicitly delay current-tool visibility to protect independent discovery.

This covers:

1. FREE Phase A; and
2. a TASK taskbook that explicitly declares a blind-forward/source-whitelist information firewall and freeze point.

Before freeze, do not expose toolbox/current method vocabulary merely to enforce reuse.

For FREE research:

`QUESTION_FIRST -> TOOL_SECOND`.

Immediately **after** the candidate/no-go packet is frozen, normal coverage + reuse-resolution becomes mandatory before method novelty or new-tool claims.

An ordinary TASK may not self-declare blindness merely to skip reuse.

## 7. Driver gate

For every meaningful return:

`EVIDENCE AUDIT -> METHOD HARVEST -> TOOL COVERAGE -> REUSE RESOLUTION -> VERDICT + ROUTE`.

Before opening a new tool/method task, Driver must show why existing matches were applied, composed, rejected on exact semantic grounds, or genuinely insufficient.

A task whose only novelty is rediscovering existing machinery under another name should be redirected/closed rather than promoted as a new family.

## 8. Steward gate

Before a Steward accepts shared reusable machinery, check the current registry/inventory and require explicit reuse resolution.

A classical/general mechanism packaged for Enterprise semantics may be useful without being novel. Tool acceptance, reuse and novelty are separate facts.

Do not move theorem ownership into the toolbox. The toolbox routes to the exact owner.

## 9. Post-return method harvest

Every Driver-accepted or Steward-accepted return receives one classification:

- `GLOBAL_TOOL_FAMILY`;
- `GLOBAL_SUBTOOL`;
- `DOMAIN_FACADE`;
- `DOMAIN_OPERATOR`;
- `RESULT_ONLY`;
- `CANDIDATE_NOT_TOOL`;
- `DUPLICATE_ALIAS`;
- `NO_TOOL_PAYLOAD`.

Update registry/inventory only when future reuse/routing changes. Do not manufacture tool entries for completeness.

## 10. Semantic safety

A tool can only be used at the strength of its declared inputs and hard boundaries.

Examples:

- T4 cannot invent an observation merely to obtain a capacity theorem;
- T6 cannot choose which distinctions are semantically disposable;
- T7 cannot create a canonical choice when declared symmetry has no fixed datum;
- T9 nonzero holonomy diagnoses failure of strict trivialization, not a unique repair.

`TOOL_USE != PREMISE_PROMOTION`.

## 11. Closed-loop invariant

`CURRENT RESEARCH -> HARVEST REUSABLE METHODS -> TOOLBOX`

and

`NEW RESEARCH -> TOOLBOX LOOKUP -> REUSE RESOLUTION -> APPLY/EXECUTE/COMPOSE/EXTEND OR EXPLICIT GAP`.

A method discovered once should become harder, not easier, to rediscover wastefully under another name.
