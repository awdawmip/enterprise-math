# Prior Art Note — P023 Composition-Safe Collapse

Status: `RESEARCH PROVENANCE NOTE`  
Scope: quotient factorization, future distinguishability, and partition refinement relevant to P023

## 1. Conservative novelty position

P023 must not present the following general ideas as Enterprise Math inventions:

- a map descends through a quotient exactly when it is constant on quotient fibers;
- congruence-compatible quotients support induced dynamics;
- future distinguishability can define a canonical refinement of finite-state classes;
- repeated partition refinement can compute a coarsest stable partition;
- automata minimization / Myhill–Nerode style equivalence and bisimulation provide mature neighboring theories.

P023 uses these established structures as mathematical infrastructure.

## 2. Paige–Tarjan partition refinement

Robert Paige and Robert E. Tarjan, “Three Partition Refinement Algorithms,” *SIAM Journal on Computing* 16(6), 973–989 (1987), DOI `10.1137/0216062`, develops efficient partition-refinement algorithms including a coarsest-partition problem.

P023's current executable reference implementation is intentionally simple and finite; it does not claim Paige–Tarjan algorithmic novelty or complexity.

## 3. Myhill–Nerode / finite-state distinguishability

The idea that states should remain distinct exactly when some future input/continuation can distinguish their observable behavior is classical in automata theory. P023's operation-word signatures are structurally in this family.

The Enterprise Math interpretation is narrower and project-specific: the resulting future-compatible quotient is treated as a **proof obligation for legal information loss / legal precision collapse** in a system whose coarse states are intended to be primary rather than approximations to a hidden continuum.

## 4. Relation to P023 claims

Accordingly:

- P023-T01/T02 are elementary quotient/factorization statements and are not priority claims;
- P023-T03–T07 are finite partition-refinement/congruence results and are not priority claims;
- the research question is whether integrating these tools with P010/P011 irreversible-history observables, P018 finite-precision state decomposition, and P021 witness transport yields useful new arithmetic classifications and a coherent precision-loss calculus.

## 5. Source registration gate

Before P023 is promoted from Draft research to canonical main, the repository `sources.json` / `lineage.json` should receive stable source IDs for the partition-refinement and automata/congruence lineage used by the final prose. This note records the attribution target but does not bypass the machine-readable provenance gate.
