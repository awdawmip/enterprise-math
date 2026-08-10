# R004 precision genesis — Supplement 25: temporal primitive-instruction retirement

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + RESOURCE-POLICY SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_24.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 24 computes the weakest live certificate quotient at every point of a staged program. This supplement applies the obstruction-cut view to the primitive instruction set carried through time.

The key new distinction is operational: may a primitive instruction that was discarded earlier be reacquired later? That capability changes the minimization problem and therefore belongs in the typed future language rather than being an unstated implementation assumption.

## 1. Weakening suffixes enlarge the adequate-set family

Fix one primitive generator catalog G. At program point i let

`Phi_i(S)=1`

mean that retained generator set S is adequate for the remaining suffix.

If point j is later than i and carries the same catalog semantics, every set able to execute the longer suffix is able to execute the tail:

`Phi_i(S)=1 => Phi_j(S)=1`.

Let `C_i` and `C_j` be the inclusion-minimal deletion-cut clutters for the two predicates.

Every later cut contains an earlier cut:

`forall H_j in C_j, exists H_i in C_i with H_i subseteq H_j`.

Proof. A later bad deletion set is also bad for the stronger earlier requirement. Since the earlier bad family is upward closed, it contains an earlier minimal bad subset.

Hence future weakening pushes obstruction cuts outward in the generator subset lattice.

## 2. Minimum instruction count cannot increase

Any retained set that hits every earlier cut also hits every later cut: for every later H_j choose an earlier H_i subset H_j and hit H_i.

Therefore

`tau(C_j) <= tau(C_i)`.

The minimum number of primitive instructions needed for the remaining suffix is nonincreasing as future requirements disappear.

This is a cardinality law only. It does not imply that a later minimum basis is contained in an earlier minimum basis.

## 3. Minimal local bases need not nest

Take generators `{a,b,c}`.

Early clutter:

`C_0={{a},{b}}`.

The unique minimum basis is

`{a,b}`.

Later clutter:

`C_1={{a,c},{b,c}}`.

The unique minimum basis is

`{c}`.

The future became weaker: every later cut contains an earlier singleton cut. The minimum cardinality dropped from 2 to 1. Yet

`{c} not subseteq {a,b}`.

Thus a stagewise optimizer that permanently deletes every currently redundant generator can destroy the best future basis.

A generator can be **currently redundant but globally valuable**.

## 4. Reacquisition allowed versus no reacquisition

### Global primitive library

If discarded instructions can be loaded again at zero/declared cost, stages may optimize independently. The minimum basis at each point can be chosen from scratch.

### Carried instruction set

If no new primitive instruction may appear without an explicit acquisition operation, retained sets must be nested:

`S_(i+1) subseteq S_i`.

This turns local basis minimization into a temporal optimization problem.

The no-upward-lift rule from Supplement 23 makes this distinction semantic rather than cosmetic: reacquiring an instruction is a real future capability and must be declared if it exists.

## 5. Temporal cut-cover formulation

Introduce binary variables

`x_(g,i) in {0,1}`

meaning generator g is retained at stage i.

No reacquisition gives

`x_(g,i+1) <= x_(g,i)`.

Adequacy at every stage gives one constraint per cut:

`sum_(g in H) x_(g,i) >= 1` for every `H in C_i`.

For nonnegative holding costs `w_(g,i)`, minimize

`sum_(i,g) w_(g,i) x_(g,i)`.

Equivalently each primitive instruction chooses a retirement time `tau_g`; g is present exactly before that time.

This is a pure integer formulation. Generic hitting-set / dynamic-programming complexity is prior mathematics; R004 uses it only as the resource semantics of its compiled instruction cuts.

## 6. Anticipatory redundancy example

Use the three-generator clutters above. Let the later clutter persist for h stages and use unit holding cost.

Myopic early minimum:

- stage 0 retains `{a,b}`;
- because c has already been deleted and reacquisition is forbidden, every later stage must keep `{a,b}`.

Total cost:

`2+2h`.

Anticipatory schedule:

- stage 0 retains currently redundant c as `{a,b,c}`;
- after the early requirement expires, retire a,b and keep only `{c}`.

Total cost:

`3+h`.

For `h>=2`, anticipatory redundancy is strictly cheaper.

Thus "remove every currently redundant primitive" is not a valid temporal optimization rule.

## 7. Exhaustive cut-clutter pressure test

All antichain cut clutters on four generators were enumerated, excluding the impossible empty deletion cut. Among all **7,413** ordered clutter pairs whose bad families satisfy the required future-weakening inclusion:

- every later minimal cut contained an earlier minimal cut;
- minimum transversal cardinality never increased;
- but **346** pairs had no later cardinality-minimum transversal contained in any earlier cardinality-minimum transversal.

So the nonnested-basis phenomenon is common even on four generators, not a hand-selected anomaly.

## 8. Architecture consequence

Primitive instruction minimization has two distinct modes:

1. **static library optimization** — reacquisition permitted, optimize each suffix independently;
2. **persistent-machine optimization** — no reacquisition, choose a globally nested retirement schedule.

The compiler must not silently choose between them. `ACQUIRE(generator)` itself is part of the future operation language when allowed.

This is another instance of the project rule:

> future capabilities determine the mathematically correct representation problem.

## 9. Next frontier

The remaining opportunity is to exploit algebraic cut backends inside the temporal problem. For Arithmetic Cut, Module Cut and Structural Target families, can retirement schedules be computed from dependency geometry directly rather than from generic hypergraph cuts? In particular, matroid-basis exchange suggests a sharp difference between "temporarily add then drop" and strict no-reacquisition, while p-adic target cuts may carry extension-depth costs rather than unit instruction counts.
