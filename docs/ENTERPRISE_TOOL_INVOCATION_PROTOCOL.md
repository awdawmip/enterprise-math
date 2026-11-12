# Enterprise Math Tool Invocation Protocol

[中文版本](ENTERPRISE_TOOL_INVOCATION_PROTOCOL.zh-CN.md)

Status: `ACTIVE / AUTONOMOUS METHOD SELECTION PROTOCOL / V2`
Date: `2026-08-28`
Machine policy: `tool_invocation_policy.json`
Tool registry: `enterprise_toolbox_registry.json`
Method inventory: `research_method_inventory.json`
Executable discovery router: `tools/enterprise_toolbox.py`

## 1. Purpose

Enterprise Math has many reusable mathematical mechanisms under route names, theorem names and source-module names. A researcher who does not know that history can accidentally rederive an existing quotient compiler, precision calculus, collision spectrum, certificate system or holonomy diagnostic and call it new machinery.

Reuse is a useful default, not a prerequisite or a prescribed research sequence.
The model chooses, reorders or replaces methods around the objective and evidence.
Existing implementations may be replaced for insight, performance, simplicity or
independent verification without a capability gap or an exception request.
Novelty and shared-tool claims still require relevant, truthful prior-work comparison;
exploration, preserving results and routine continuation do not wait for it.
User assumptions, blind-discovery firewalls and semantic boundaries remain binding. Assistant-proposed taskbook methods are options, not prescribed thinking steps; explicit user experiment conditions remain binding.

## 2. Understand first, lookup second

Do not preload the toolbox before understanding a task. Tool names can anchor problem formulation.

For ordinary `TASK_RESEARCH`, first read the exact task and first necessary dependency. Once the information structure is clear, perform coverage lookup before claiming method novelty or accepting a shared general-purpose method. Unshared exploration, derivation and material preservation may proceed first or in parallel.

Recommended lookup:

`python tools/enterprise_toolbox.py coverage <plain-language need>`

The router searches:

1. curated global tool families;
2. harvested methods/domain facades;
3. AST/docstring/public-API metadata from current `src/enterprise_math/*.py`.

These are available evidence sources, not a mandatory reading order. The source layer discovers executable source but does not execute it.

## 3. Coverage verdict is only the first decision

Coverage resolves to:

- `REUSE_EXISTING_TOOL`;
- `COMPOSE_EXISTING_TOOLS`;
- `EXTEND_EXISTING_TOOL`;
- `CAPABILITY_GAP_CONFIRMED`;
- `ALTERNATIVE_APPROACH_CHOSEN` — choose a useful alternative, including identical input/output, without claiming novelty from that choice;
- `NOT_APPLICABLE`.

A positive match is **not** proof that the tool was actually reused.

Before novelty claims or shared-tool acceptance, relevant matches resolve to one of these states:

- `REUSE_APPLIED` — exact mathematical/tool interface was applied to the current task; no software execution was necessary;
- `REUSE_EXECUTED` — an existing executable implementation was actually run for the claimed computation/certificate;
- `COMPOSE_APPLIED` — concrete existing tools/methods were composed with their hard boundaries preserved;
- `EXTEND_EXISTING_TOOL` — the existing owner is correct but a genuinely missing capability must be added;
- `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE` — an adequate executable exists but cannot be executed in the current environment; do not claim it ran and do not relabel environment unavailability as a mathematical capability gap;
- `CAPABILITY_GAP_CONFIRMED` — exact required input/output capability is absent;
- `ALTERNATIVE_APPROACH_CHOSEN` — choose a useful alternative, including identical input/output, without claiming novelty from that choice;
- `NOT_APPLICABLE`.

Minimum record:

- coverage verdict;
- matched tool/method IDs;
- reuse-resolution state;
- how the tool was applied/executed, or why not;
- hard boundary checked.

## 4. What counts as reuse

For a **mathematical calculus/theorem interface**, exact application of its declared law, hypotheses and hard boundary can be `REUSE_APPLIED`; code execution is not required merely to say the method was reused.

For a claim that depends on a **software computation/certificate**, finding the source module is not enough. Prefer reuse when it serves the objective; an alternative implementation is also permitted without a capability gap. Record which implementation actually ran and distinguish independent validation from novelty.

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

After the candidate/no-go packet is frozen, relevant coverage comparison is required when making method novelty or shared-tool claims, not immediately before any further research.

An ordinary TASK may not self-declare blindness merely to skip reuse.

## 7. Driver decisions

Choose the research and review sequence autonomously. For material novelty or shared-tool decisions, use relevant prior-work evidence and classify the actual contribution. Do not require a capability gap, force reuse, or prescribe an evidence/harvest/lookup sequence. Same-interface alternatives may be valuable; naming alone is not mathematical novelty.

## 8. Steward gate

Before a Steward accepts shared reusable machinery, check the current registry/inventory and require explicit reuse resolution.

A classical/general mechanism packaged for Enterprise semantics may be useful without being novel. Tool acceptance, reuse and novelty are separate facts.

Do not move theorem ownership into the toolbox. The toolbox routes to the exact owner.

## 9. Post-return method harvest

When a return changes shared reusable machinery or its routing, classify the contribution using the relevant category:

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

## 11. Autonomous research, truthful reuse

Research may reuse, compose, extend or replace methods. Preserve useful results and
relevant prior-work links without mandatory repeated lookup or a fixed thinking chain.
Tool acceptance, implementation improvement and mathematical novelty are distinct;
none is inferred merely from a new name or a claimed capability gap.
