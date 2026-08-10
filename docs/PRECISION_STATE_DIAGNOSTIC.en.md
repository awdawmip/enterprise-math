# Precision-State Diagnostic: Fiber, Image, Domain, Relation, and Ledger

Status: `RESEARCH BRIDGE / NONCANONICAL`  
Scope: Foundation-facing diagnostic extracted from current P023/P024/E001/A4 pressure tests  
Purpose: prevent mathematically different failures from being repaired with the wrong kind of state, precision, or policy.

## 1. Why this diagnostic exists

Recent precision-first research repeatedly produced states that looked similar at a coarse interface but failed for fundamentally different reasons. Calling all of them “missing precision”, “hidden history”, “underresolution”, or “nondeterminism” is too coarse.

Five mathematically distinct failure locations now recur:

1. **FIBER / HIDDEN DETAIL** — several fine states share one coarse state;
2. **IMAGE / COKERNEL OBSTRUCTION** — a requested coarse target is not in the integer image / chosen representation;
3. **DOMAIN / ACTION-LANGUAGE DEFECT** — an update formula exists but a state-dependent action may be disabled, and word order can matter;
4. **RELATION / MULTIVALUED SUCCESSOR** — the declared law itself has several admissible next states or terminal outcomes;
5. **LEDGER / TRANSFER ALLOCATION** — a conserved or quantized quantity is distributed among explicit compartments and policy moves redistribute it.

These are not five names for the same phenomenon. They require different repairs.

The **declared future language** is not a sixth failure type. It is the outer selector that determines which distinctions inside each layer are actually future-visible and therefore must be retained.

---

## 2. Diagnostic question order

When a coarse state or world transition appears insufficient, ask the questions in this order.

### Q1 — Is the declared successor single-valued?

If not, the first object is a **relation**, not a hidden deterministic state.

Do not repair a multivalued relation by silently choosing a scheduler, minimum-norm witness, contact ID, symmetric representative, or optimizer. A selector is an additional world law unless future-observable equivalence proves all branches interchangeable.

### Q2 — Is the desired target in the integer image of the declared update/representation map?

If not, this is an **image/cokernel obstruction**.

Adding hidden history cannot make an unreachable target reachable. Typical repairs are a different target, a larger allowed operation language, a compatible refinement denominator, or an explicit UNDERRESOLVED/IMPOSSIBLE result depending on which obstruction is present.

### Q3 — For reachable/single-valued coarse behavior, do several fine states map to one coarse state?

If yes, inspect the **fiber**.

Do not retain the whole fine state automatically. Retain only the quotient repair read by the declared future language. The hidden fiber may be finite, free-lattice, finite-memory, or otherwise structured.

### Q4 — Are future operations partial/state-dependent?

If yes, include **action domain / definedness** in the future signature.

Algebraically commuting total updates need not commute as guarded partial operations. A final target can be statically feasible yet have no legal causal action word.

### Q5 — Is an already-quantized/conserved quantity split among compartments?

If yes, identify the **ledger and allowed transfer graph**.

Applied, queued, expired, recovered, delayed, damaged, quarantined, or other compartments are not interchangeable unless the declared transfer operations and future observables make them so. Compute the transfer-difference lattice / component totals before deleting compartment identity.

---

## 3. Layer A — FIBER / hidden detail

A coarse map `q:X->Y` creates fibers

`q^{-1}(y)`.

The first question is not “how large is the fiber?” but:

> Which differences inside a fiber can a declared future operation/observation still read?

### 3.1 Contact-local subquantum remainder

For one contact channel,

`N=A*j+delta`, `0<=delta<A`.

Current delivered impulse `j` forgets the finite remainder fiber. Named future raw additions reveal `delta` through the first carry time. With all contacts independently addressable, the memoryless contact predictive state becomes `(B j, delta)`, not full delivered allocation `j`.

This is a **finite fiber/carry repair**.

### 3.2 TTL queue age histogram

For age buckets

`q=(q_0,...,q_(D-1))`,

current total `Q=sum q_a` forgets age distribution. Pure TTL aging reveals one oldest bucket per future step. At horizon `h<=D-1`, the exact key is

`(sum_(a=0)^(D-h-1) q_a, q_(D-h),...,q_(D-1))`.

The hidden age state is fully reconstructed at horizon `D-1` from total traces using integer differences only.

This is a **finite-memory / passive-observability fiber**.

### 3.3 Contact cycle history

For incidence `B`, histories with one body delta differ by

`ker_Z B = H_1(G;Z)`.

A linear witness `Cj` descends through body state iff

`ker_Z B subseteq ker_Z C`.

The exact hidden witness group is

`C(ker B) ~= ker B / (ker B intersect ker C)`.

This is a **free-lattice / homology fiber**.

### 3.4 Fiber repair is task-relative

A fiber may exist mathematically while requiring no stored repair for a particular future language.

Examples:

- cycle allocation is invisible to the pure local carry/body-output language, so `(B j,delta)` is exact even on cyclic graphs;
- a scalar cycle witness that is an integer coboundary `c=B^T phi` telescopes to body state and requires no cycle repair;
- modular observation can reduce an infinite scalar hidden subgroup `gZ` to only `M/gcd(M,g)` phases.

Therefore:

**fiber existence != required retained state.**

---

## 4. Layer B — IMAGE / COKERNEL obstruction

A map may have no hidden ambiguity and still fail to reach every integer target.

This is not a fiber problem.

### 4.1 Path/contact target congruence

For the uniform path contact Gram, `ker K=0` but

`coker(K) ~= Z/nZ`.

A target can have a unique rational witness and still fail integer reachability. Nullity zero does not remove torsion.

### 4.2 Graph critical-group denominator

For body delta `b=Bj` and graph Laplacian `L=B B^T`, representing an integer edge history as rational potential/cut plus cycle can require a denominator.

The minimum denominator is the order of `[b]` in

`im_Z(B) / im_Z(L)`.

For a cycle `C_n` and one edge impulse, the denominator is exactly `n`.

This is a **representation/reachability obstruction**, not hidden history.

### 4.3 Repetition phase

If a critical class has order `s`, repeating the same physical delta `m` times changes the minimum denominator to

`s_m=s/gcd(s,m)`.

This can be nonmonotone in ordinary integer `m` while decreasing along true divisibility refinement.

### 4.4 Diagnostic rule

If the failure is in the image/cokernel:

- more history does not repair it;
- choosing another relation branch does not repair it unless that branch changes the target;
- increasing numerical denominator can repair a representation obstruction only when the refinement is compatible with the relevant torsion/order;
- distinguish permanent arithmetic impossibility from finite-horizon/packing underresolution.

---

## 5. Layer C — DOMAIN / action-language defect

A formula may be perfectly defined algebraically while the world operation is only partially legal.

### 5.1 Guarded contact actions

For contact scores `r` and coupling `K`, unit action `i` adds `K e_i` only while

`r_i<0`.

An arbitrary word compiles to an exact partial affine operation `(Delta,H)`, where `H` records the maximum prefix requirement at each used contact.

Thus:

`algebraic update equality != causal operation equality`.

### 5.2 Batched target vs causal realizability

A material layer can quantize a delivered vector `J` exactly. Batched network application is always the additive update by `KJ`.

A guarded sequential world instead asks whether a legal unit-action word with count vector `J` exists.

For a q=1 positive-coupled three-leaf star, batch `J=(1,1,1)` is algebraically valid but no guarded sequential word consumes all three units.

This is a **domain/word-language failure**, not an arithmetic image failure.

### 5.3 Z-coupled greedy structure

If all off-diagonal couplings are nonpositive, any currently enabled remaining action can be moved to the front of an existing completion. Hence any enabled-greedy scheduler succeeds iff any guarded completion exists.

This is a domain theorem. It does not imply that the full guarded operation algebra globally commutes.

### 5.4 Partial-action precision genesis

Definedness itself can generate predictive precision even when present observation is constant. Therefore current state precision must be computed relative to the declared future action domains, not only current value observation.

---

## 6. Layer D — RELATION / multivalued successor

Sometimes there is no single fine successor waiting to be discovered. The declared law itself returns a set/relation.

### 6.1 Static response relation

A branching contact network can have several incomparable minimum-total responses. Keeping the whole first feasible layer is different from choosing one response.

### 6.2 Scheduler terminal relation

A prequantized target `J` under guarded consume-until-stuck semantics can have several terminal applied-count vectors `n`.

The exact queue `Q'=J-n` is therefore relation-valued whenever terminal count is not unique.

### 6.3 Observable determinism of a relation

For finite relation `R` and target observation `O`, use the powerset-valued signature

`Sigma_(R,O)(x)={O(y):(x,y) in R}`.

Raw relation branching can be hidden by a declared observation without turning the underlying relation into a deterministic state update.

A source quotient is safe iff `Sigma_(R,O)` is constant on its fibers, including the empty/no-target outcome.

### 6.4 Composition warning

One-step observable determinism is not automatically composition-safe. A later relation can read hidden intermediate branch identity and reactivate branching.

Safe coarse composition requires the later powerset-valued signature itself to descend through the chosen observation quotient.

### 6.5 Powerset compiler boundary

A4 support dynamics can be compiled to deterministic maps on `P(X)` for reachable-support semantics. This loses witness multiplicity, path identity, and individually dead branches. If the future reads those, powerset support is too coarse.

---

## 7. Layer E — LEDGER / transfer allocation

A conserved or already-quantized quantity may be known in total while its compartment allocation remains future-relevant.

### 7.1 Applied / queued / expired

For whole-contact material quanta:

`H=P+Q+X`.

Policy moves redistribute this total:

- application moves `Q->P`;
- expiry moves `Q->X`.

For scalar readout `uP+vQ+wX`:

- application/scheduler invariant iff `u=v`;
- expiry invariant iff `v=w`;
- invariant under both iff `u=v=w`.

This explains structurally why applied, live-committed, and ever-quantized histories have different determinism properties.

### 7.2 General transfer graph

For arbitrary compartments and allowed transfer edges, a scalar linear observable is invariant under all allowed transfers iff its weights are constant on each connected component of the transfer graph.

Hence:

`rank(independent linear transfer invariants) = number of transfer components`.

Canonical coordinates are component totals.

### 7.3 Future policy meet

If future transfer graphs may change, today's component totals are not necessarily future-safe.

Two compartments may be merged today only if they remain in the same connected component in **every** declared future transfer graph.

The minimal current additive ledger state is one total per block of the common refinement/meet of all future connectivity partitions.

Future merging is safe; future splitting can reactivate detail and therefore requires that detail now.

---

## 8. Cross-layer anti-confusion table

| Symptom | Correct layer | Wrong repair to avoid |
|---|---|---|
| Same coarse state, different next carry time | FIBER | raising denominator without retaining future-visible remainder |
| Same body delta, different cycle damage history | FIBER | declaring target unreachable |
| Unique witness over Q but no integer target solution | IMAGE/COKERNEL | storing more history |
| Exact batch vector but no legal guarded word | DOMAIN | treating batch feasibility as causal realizability |
| Several admissible terminal outcomes | RELATION | silently selecting one scheduler/representative |
| Same quantized total split across applied/queued/expired | LEDGER | collapsing compartments without checking transfer/future invariance |
| TTL queue count equal now, different age histogram | FIBER + DOMAIN/LEDGER future | assuming present scalar total is universally sufficient |
| Critical-group denominator >1 | IMAGE/COKERNEL | calling it hidden cycle history |
| Raw relation branches but all branches have same observed target | RELATION + future observation | claiming underlying relation became single-valued |

---

## 9. Unified diagnostic output

A future precision/state compiler should not return one undifferentiated label such as `UNDERRESOLVED` whenever possible. It should classify the missing structure along these axes:

```text
STATE/FIBER:
    what distinctions exist inside the current coarse fiber?
    which of them survive the declared future language?

TARGET/IMAGE:
    is the desired target reachable/representable in the declared integer structure?
    if not, is the defect permanent arithmetic torsion/gap or finite-horizon underresolution?

ACTION/DOMAIN:
    which named operations are currently defined?
    which words are causally realizable?
    does order change legality?

SUCCESSOR/RELATION:
    is the next-state law functional or relation-valued?
    which branch differences survive the declared observation?

LEDGER/TRANSFER:
    where is already-quantized/conserved content allocated?
    which transfers are allowed now and in declared future policies?
    which component totals are therefore future-safe?
```

The outer rule is always:

> **retain exactly the distinctions that the declared future operation/observation language can reactivate; do not repair one mathematical layer by silently changing another.**

---

## 10. Current evidence map

This note is a synthesis of current canonical and Draft research evidence, not a canonical Foundation theorem. Relevant research surfaces include:

- canonical finite material impulse/remainder telescope from the #194 lineage;
- P024 guarded-action and two-sided action-language work, including #310/#315;
- contact guarded/homology/critical-precision Draft bridge #342;
- contact-local predictive reservoir Draft #357;
- causal whole-quantum material tick Draft #360;
- history/scheduler ambiguity Draft #365;
- generic A4/P023 relation-observable Draft #368;
- finite TTL queue-age Draft #370;
- TTL loss/order/history Draft #371;
- material-ledger transfer/future-policy precision Draft #372.

Prior mathematics used throughout includes quotient/fiber/kernel/cokernel theory, finite relations, automata/subset construction, numerical semigroups, graph homology/cohomology, critical groups, finite queues, graph connectivity and integer conservation ledgers.

No claim is made that every diagnostic layer is a new mathematical object. The project value is the precision-first architecture: these standard structures occur at different failure locations and must not be conflated when constructing a discrete world state.
