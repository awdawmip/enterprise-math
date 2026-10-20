# Precision-State Diagnostic: Five Failure Locations

Status: `RESEARCH BRIDGE / NONCANONICAL`  
Scope: Foundation-facing synthesis from current P023/P024/E001/A4 pressure tests  
Purpose: prevent distinct mathematical failures from being repaired by the wrong kind of state, precision, or policy.

## 1. Core classification

A coarse discrete world can fail at five different locations:

1. **FIBER / hidden detail** — several fine states share one coarse state;
2. **IMAGE / COKERNEL** — a requested target is not in the declared integer image / coordinate representation;
3. **DOMAIN / action language** — an algebraic update exists but a state-dependent action or word is not legally executable;
4. **RELATION / multivalued successor** — the declared law itself has several admissible successors;
5. **LEDGER / transfer allocation** — already-quantized or conserved content is distributed among explicit compartments and policy operations move it between them.

These are failure locations, not five names for “missing precision”.  They require different repairs.

The **declared future language** is the outer selector.  It determines which differences inside these layers are actually future-visible and therefore must be retained now.

## 2. Diagnostic order

When a coarse state or transition appears insufficient, ask:

1. Is the successor functional or relation-valued?
2. Is the requested target in the integer image of the declared map?
3. Which fine states lie in the same coarse fiber, and which fiber differences survive the future language?
4. Which named operations are partial, and which action words are causally legal?
5. Which already-quantized quantities live in different ledger compartments, and which transfers are allowed now or may be allowed later?

Do not repair one layer by silently changing another.  In particular:

- more history does not remove a cokernel obstruction;
- a higher denominator does not select one branch of a relation;
- a scheduler is not a proof that a multivalued response was secretly deterministic;
- a statically feasible batch target is not proof of a legal guarded word;
- a conserved total is not proof that its compartment allocation is future-irrelevant.

## 3. FIBER — what is hidden inside one coarse state?

### 3.1 Finite carry fiber

For one contact channel,

`N=A*j+delta`, `0<=delta<A`.

The delivered integer `j` forgets the subquantum remainder.  Named future raw additions reveal `delta` through carry timing.  With memoryless local carry/body-output futures, the exact contact predictive state is `(B j,delta)` rather than the full delivered allocation.

### 3.2 Finite-memory fiber

For a TTL whole-queue age histogram

`q=(q_0,...,q_(D-1))`,

current total `Q=sum q_a` forgets age.  Pure future aging reveals one oldest bucket per horizon step.  At horizon `h<=D-1`, the exact total-observation key is

`(sum_(a=0)^(D-h-1) q_a, q_(D-h),...,q_(D-1))`.

At horizon `D-1`, the full histogram is recovered from total traces by integer differences only.

### 3.3 Free-lattice / homology fiber

For contact incidence `B`, histories with one body delta differ by

`ker_Z B = H_1(G;Z)`.

An additive witness `Cj` descends through body state iff

`ker_Z B subseteq ker_Z C`.

The hidden witness group is

`C(ker B) ~= ker B/(ker B intersect ker C)`.

A scalar witness that is an integer coboundary `c=B^T phi` telescopes to body state and needs no cycle repair.

### 3.4 Fiber existence is not retained-state necessity

A fiber may exist mathematically while a declared future language kills it completely.  The correct repair is the future-visible quotient of the fiber, not the whole fine state.

## 4. IMAGE / COKERNEL — what cannot be reached or represented?

Zero kernel does not imply full integer reachability.

Examples already appearing in the contact program include:

- path/contact Grams with unique witness but finite congruence cokernel;
- graph critical-group classes forcing a nontrivial potential/cycle representation denominator;
- two-sided action languages with permanent numerical-semigroup gaps versus temporary finite-horizon packing underresolution.

For a graph critical class of order `s`, repeated physical delta `m` times has minimum representation denominator

`s/gcd(s,m)`.

This is a representation/reachability obstruction, not hidden history.  Storing more history does not repair it.

## 5. DOMAIN — what operations are legally executable?

For guarded contact score state `r`, unit action `i` adds `K e_i` only while

`r_i<0`.

A literal word has an exact partial-affine normal form `(Delta,H)`; the prefix requirement `H` is part of the operation.

Consequences:

- algebraically commuting total updates can fail to commute as guarded partial maps;
- a material layer may quantize an exact batch vector `J` while no guarded sequential word realizes all of `J`;
- on Z-coupled systems with nonpositive off-diagonal coupling, enabled-greedy completion is structurally safe whenever any completion exists;
- definedness itself can generate predictive precision from a constant present observation.

This is an action-domain problem, not a target-cokernel problem.

## 6. RELATION — when there is no unique next state to recover

A branching response or guarded terminal family can be genuinely relation-valued.

For finite relation `R` and target observation `O`, the correct one-step observed signature is

`Sigma_(R,O)(x)={O(y):(x,y) in R}`.

The empty set is explicit undefined/no-target behavior.

Raw branching and observable nondeterminism are distinct.  A multivalued raw relation may have a singleton observed target set for one future language without becoming a deterministic world update.

One-step observable determinism is not automatically composition-safe: a later relation can read hidden intermediate branch identity and reactivate branching.  Safe coarse composition requires the later powerset-valued signature itself to descend through the chosen observation quotient.

For reachable-support semantics, A4 relation words can be compiled to deterministic maps on `P(X)`.  That compiler intentionally loses path multiplicity, branch identity, and individual branch death; richer witness futures must remain in A4.

## 7. LEDGER — where conserved/quantized content is allocated

### 7.1 One fixed transfer graph

Let ledger compartments be vertices and an allowed whole-quantum transfer `u->v` change the ledger by

`-d e_u + d e_v`.

The redistribution lattice is the integer incidence image of the transfer graph.  A scalar linear readout is invariant under every allowed transfer iff its weights are constant on each connected component.

Hence one fixed transfer graph has one independent linear invariant per connected component, canonically the component total.

For the applied/queued/expired ledger `(P,Q,X)`:

- application `Q->P` alone preserves `P+Q` and `X`;
- expiry `Q->X` alone preserves `P` and `Q+X`;
- both transfer families connect all three compartments, leaving only total `P+Q+X` as an independent fully policy-invariant linear coordinate.

### 7.2 Several possible future transfer graphs: exact additive state

A first WIP formulation used the common refinement of future connectivity partitions as the minimal additive current state.  That is **false in general**.

The correct object is the joint component-sum matrix.

For each possible future graph `G_i`, add one integer indicator row `1_C` for every connected component `C`.  Stack all rows into

`S : Z^V -> Z^m`.

Then two current additive ledgers are future-indistinguishable exactly when

`S(ell-ell')=0`.

Equivalently,

`ker_Z S = intersection_i im_Z D_i`,

where `D_i` is a transfer-graph incidence matrix.

Therefore:

- hidden free rank = `|V|-rank_Q(S)`;
- the minimum number of independent scalar linear coordinates with the same equality kernel is `rank_Q(S)`;
- the full list of all future component totals may contain linear redundancy.

### 7.3 Crossing-partition counterexample

With four compartments and future partitions

`01|23`,
`02|13`,

the pairwise connectivity-equivalence meet is four singletons.  Nevertheless

`d=(1,-1,-1,1)`

has zero total on every component of both partitions, so `S d=0`.

Thus singleton block totals are safe but overprecise; the exact joint observation rank is only 3.

The connectivity meet remains useful only as:

- an exact test for pairwise **unit-placement** indistinguishability;
- a safe combinatorial block-total upper bound.

It is not the additive minimality theorem.

### 7.4 Injective future totals can still have integer-coordinate torsion

A second issue appears even when `ker S=0`.

For the three pair partitions of four compartments

`01|23`, `02|13`, `03|12`,

the joint component totals uniquely determine the full ledger (`rank_Q(S)=4`), but the row lattice generated by the component indicators has saturation index 2.

So hidden-state ambiguity is gone while the future-total coordinate system is still non-unimodular.  This is an IMAGE/COKERNEL-style coordinate obstruction occurring **inside** the Ledger layer.

This is why the five diagnostic locations are not mutually exclusive ontologies: a ledger problem can itself contain a fiber/kernel question and a separate integer image/torsion question.  The five labels identify where the problem enters the world architecture.

### 7.5 Is today's component-total state safe against future policy change?

Current graph component totals are sufficient for all declared future component-total observations iff no future graph splits one of the current connected components.

Future merging is safe; future splitting can reactivate detail and requires that detail today.

This current-safety criterion is distinct from the globally minimal additive joint signature above.

## 8. Anti-confusion map

| Symptom | Diagnose first as | Do not “fix” it by |
|---|---|---|
| same delivered integer, different next carry time | FIBER | only increasing denominator |
| same body delta, different cycle damage history | FIBER | calling the target unreachable |
| unique rational witness, no integer target solution | IMAGE/COKERNEL | storing more history |
| exact batch target, no legal guarded word | DOMAIN | treating batch feasibility as causal realizability |
| several admissible terminal outcomes | RELATION | silently choosing a representative |
| same quantized total split across applied/queued/expired | LEDGER | deleting compartment identity without transfer/future analysis |
| same queue total, different TTL age histogram | FIBER + future DOMAIN/LEDGER | assuming current total is universal state |
| critical denominator >1 | IMAGE/COKERNEL | calling it hidden cycle history |
| raw relation branches but observed target set is singleton | RELATION + future observation | claiming the underlying law became functional |
| several future transfer policies | LEDGER + joint linear observation | using connectivity-meet blocks as the additive minimum |

## 9. Architecture rule

A precision-first state compiler should keep the questions separate:

```text
STATE/FIBER
    What distinctions lie inside the current coarse fiber?
    Which are reactivated by the declared future language?

TARGET/IMAGE
    Is the requested target reachable / integrally representable?
    Is failure permanent arithmetic obstruction or finite-horizon underresolution?

ACTION/DOMAIN
    Which actions are currently defined?
    Which words are causally realizable?

SUCCESSOR/RELATION
    Is the next-state law functional or relation-valued?
    Which branch differences survive the declared observation?

LEDGER/TRANSFER
    Where is already-quantized/conserved content allocated?
    Which current/future transfers are declared?
    What is the joint future observation kernel?
```

The outer rule is:

> **Retain exactly the distinctions that the declared future operation/observation language can reactivate; never repair one mathematical layer by silently changing another.**

## 10. Evidence status

This document is a noncanonical synthesis.  It consumes canonical and Draft evidence from the finite material impulse lineage, guarded P024 work, contact homology/critical-precision work, causal material queue/history work, A4/P023 relation-observable work, TTL age/loss work, and the corrected material-ledger future-policy lattice.

The mathematics used — quotient/kernel/cokernel theory, finite relations, subset construction, numerical semigroups, graph homology/cohomology, critical groups, queues, graph incidence and integer lattices — is standard prior mathematics.  The project contribution here is architectural separation: these structures occur at different failure locations and must not be conflated when constructing a finite-precision world state.
