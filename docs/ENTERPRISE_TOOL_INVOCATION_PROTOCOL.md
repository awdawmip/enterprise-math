# Enterprise Math Tool Invocation Protocol

Status: `ACTIVE / UNIVERSAL REUSE-BEFORE-INVENTION PROTOCOL / V1`
Date: `2026-08-22`
Machine policy: `tool_invocation_policy.json`
Tool registry: `enterprise_toolbox_registry.json`
Method inventory: `research_method_inventory.json`
Executable router: `tools/enterprise_toolbox.py`

## 1. Purpose

Enterprise Math has accumulated many reusable mathematical mechanisms under route names, theorem names and source-module names. A researcher who does not know that history can accidentally rederive a quotient compiler, precision calculus, collision spectrum, Helly certificate or holonomy diagnostic and call it a new tool.

This protocol closes that loop.

The default research flow is now:

`QUESTION/TASK`

`-> IDENTIFY INFORMATION STRUCTURE`

`-> TOOL COVERAGE LOOKUP`

`-> REUSE / COMPOSE / EXTEND / CONFIRM GAP`

`-> RESEARCH`

`-> METHOD HARVEST AT ACCEPTED RETURN`

`-> REGISTRY / INVENTORY UPDATE WHEN ROUTING VALUE CHANGES`.

Freeze:

`NEW_MECHANISM_BY_DEFAULT = FORBIDDEN`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

This is a reuse discipline, not a theorem premise and not a Foundation change.

## 2. The timing rule: understand first, lookup second

Do not preload the whole toolbox before understanding a task. Tool names can anchor the formulation of the problem.

For `TASK_RESEARCH`, first read the exact task and the first necessary dependency. Once the information structure of the problem is clear, perform the tool lookup **before constructing a new general-purpose method, helper calculus, quotient, certificate, invariant or search engine**.

This preserves the hot-start rule while preventing duplicate invention.

Recommended query:

`python tools/enterprise_toolbox.py coverage <plain-language need>`

Examples:

- `coverage "coarsest quotient preserving all future observations"`;
- `coverage "bounded local certificate for global compatibility"`;
- `coverage "path difference cycle provenance"`;
- `coverage "integer precision carry under refinement"`.

The lookup has three layers:

1. curated global tool families;
2. curated harvested methods/domain facades;
3. AST/docstring/public-API search over every current `src/enterprise_math/*.py` module.

The third layer means that a mature executable helper can be discovered even before a Driver has manually classified it.

## 3. Coverage verdicts

Every serious method choice resolves to one of five states.

### `REUSE_EXISTING_TOOL`

The existing tool already has the needed semantic input/output contract. Use it and cite the owner/source.

### `COMPOSE_EXISTING_TOOLS`

No one family solves the problem, but a typed composition does. Record the composition boundary rather than inventing a new family name.

Example pattern:

`T6 operation-safe quotient -> T4 fiber capacity -> T1 scale enumerator`.

### `EXTEND_EXISTING_TOOL`

The old tool is the correct owner but lacks one genuinely new operation/certificate. Extend that owner and preserve backward compatibility and hard boundaries.

### `CAPABILITY_GAP_CONFIRMED`

A new family is justified only when the exact missing input/output capability cannot be represented as reuse, composition, specialization, alias or extension of an existing owner.

The gap record must state:

- tool families checked;
- concrete methods/modules checked;
- exact semantic mismatch;
- missing input/output contract;
- why composition or extension is insufficient.

### `NOT_APPLICABLE`

The task is theorem/object-specific and does not require reusable machinery.

## 4. Anti-duplication taxonomy

Do not create a new family when the difference is only:

- a historical name;
- a new application domain;
- a different filename;
- a specialized parameter regime;
- a wrapper around the same operator;
- a theorem that instantiates an existing generic calculus.

Route these respectively as an alias, domain facade, specialization or subtool.

A strict superset with one new operation normally extends the existing family.

A new family is reserved for a genuinely different semantic input/output contract or structural law.

## 5. FREE researcher firewall

FREE Phase A is the one deliberate exception to pre-invention lookup.

Before candidate freeze:

- do not expose the toolbox registry;
- do not expose the method inventory;
- do not run the coverage router as a discovery prior;
- do not name current tool families in the prompt merely to forbid them.

A FREE researcher may still use generic computation/formalization after its own primitive question has arisen:

`QUESTION_FIRST -> TOOL_SECOND`.

But current project tool availability may not choose the question or candidate.

Immediately **after** the candidate/no-go packet is frozen, Phase B must run the tool coverage lookup before claiming that the candidate also discovers a new method/tool. Existing-tool collision is then a dedup/integration result, not retroactive continuation.

## 6. Driver gate

For every meaningful research return, Driver routing now includes:

`EVIDENCE AUDIT`

`-> METHOD HARVEST`

`-> TOOL COVERAGE / DEDUP`

`-> VERDICT + ROUTE`.

Before opening a new method/tool task, the Driver must resolve:

`REUSE / COMPOSE / EXTEND / GAP_CONFIRMED / NOT_APPLICABLE`.

A task whose only novelty is rediscovering an existing tool under a new route name should be closed or redirected immediately.

## 7. Steward gate

Before a Steward accepts shared reusable machinery, check the current registry/inventory and preserve exact ownership.

A classical/general tool packaged for Enterprise semantics may be valuable without being novel. Tool acceptance and novelty are separate fields.

Do not move theorem ownership into the toolbox. The toolbox routes to the exact owner.

## 8. Post-return method harvest

Every Driver-accepted or Steward-accepted return receives one method classification:

- `GLOBAL_TOOL_FAMILY`;
- `GLOBAL_SUBTOOL`;
- `DOMAIN_FACADE`;
- `DOMAIN_OPERATOR`;
- `RESULT_ONLY`;
- `CANDIDATE_NOT_TOOL`;
- `DUPLICATE_ALIAS`;
- `NO_TOOL_PAYLOAD`.

If the classification changes future routing, update `research_method_inventory.json` and, when a family-level capability changes, `enterprise_toolbox_registry.json`.

If a result has no reusable method, record that fact in the Driver/Steward review and do not manufacture a tool entry merely for completeness.

## 9. Tool-family versus method inventory

The two layers serve different purposes.

**Tool family** answers:

> What mathematical mechanism should own this kind of problem?

**Method inventory** answers:

> Which exact callable implementation, theorem interface, specialization or recent research operator already exists?

The current router searches both, then scans current executable source.

This prevents both kinds of duplication:

- reinventing a whole calculus;
- rewriting a concrete helper that already exists under an unrelated route filename.

## 10. Semantic safety

A tool can only be invoked at the semantic strength of its input.

Examples:

- T4 cannot invent an observation `pi` simply to obtain a capacity theorem;
- T6 cannot decide which distinctions are semantically disposable; the observation/operation language is input;
- T7 cannot create a canonical choice when the declared symmetry has no fixed datum;
- T9 nonzero holonomy proves failure of strict trivialization, not a unique repair;
- T3 cannot import carrier vector dependencies into native incidence;
- T1 growth degree is not native geometric dimension without another theorem.

`TOOL_USE != PREMISE_PROMOTION`.

## 11. Closed-loop invariant

The control-plane invariant is now:

`CURRENT RESEARCH -> HARVEST REUSABLE METHODS -> TOOLBOX`

and

`NEW RESEARCH -> TOOLBOX LOOKUP -> REUSE/COMPOSE/EXTEND OR EXPLICIT GAP`.

Therefore a useful method discovered once should become harder, not easier, to rediscover wastefully under a new name.
