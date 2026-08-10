# Branching Future Signatures for Relation-Valued Operations

Status: `RESEARCH BRIDGE / NONCANONICAL`

The relation-support stable quotient can be expressed as an ordinary future-signature kernel once the future language is allowed to observe **branching successor behavioural types**, rather than only terminal support unions along literal words.

## 1. Recursive branching signature

Let `O:X->Y` be the current observation and `{R_a}` a finite labelled relation family.

Define

`σ_0(x)=O(x)`.

Recursively define

`σ_(h+1)(x)`

as the current observation together with, for every named action a, the set

`{ σ_h(y) : x R_a y }`.

The empty set is retained exactly.

This is the depth-h labelled branching tree up to equality of repeated successor types; it is support-sensitive, not multiplicity-sensitive.

## 2. Exact equality with relation-support refinement stages

Let `E_h` be equality of `σ_h`.

At h=0, `E_0` is exactly the current observation partition.

Given `E_h`, two states have equal `σ_(h+1)` exactly when:

- they have the same current observation; and
- for every action, they reach the same set of `E_h` successor classes.

Because equality of `σ_h` already implies equality at all earlier depths, this is exactly one support-stability refinement round.

Therefore

`kernel(σ_h) = h-th relation-support refinement partition`.

The executable branch verifies equality of the complete partition sequence with the fixed-point compiler.

## 3. Finite branching depth certifies the infinite quotient

On n finite states with c_0 initial observation blocks, every strict branching refinement adds at least one block.

Hence the stable relation-support quotient is reached after at most

`n-c_0`

strict branching-depth refinements.

If one horizon produces no new partition split, the relation support is already stable and no deeper branching signature can refine it.

Thus the infinite support-bisimulation quotient has a finite exact depth certificate.

## 4. Literal terminal support is a deterministic projection

Given `σ_h(x)` and a word

`w=a_1...a_k`, `k<=h`,

compute terminal observed support recursively:

- empty word -> singleton `{O(x)}`;
- for first action a, recursively evaluate the remainder on every successor signature in the a-support and take their union.

This produces exactly

`{ O(y) : x R_w y }`.

Therefore every word-indexed terminal observed-support signature factors through the branching signature:

`branching signature -> terminal support traces`.

Consequently the branching partition always refines the terminal trace partition at the same horizon.

## 5. Why the projection loses information only under genuine branching

If every action/source has at most one successor, each action support is either

- empty; or
- one child signature.

The terminal word language can then reconstruct recursively whether that one child exists and its complete future trace type.

Thus for deterministic partial relation families:

`branching partition at horizon h`

`=`

`legality/terminal-support word partition through horizon h`.

This recovers total deterministic and FQ-006 behaviour exactly.

The branching/trace distinction begins only when one action can expose several sibling successor types simultaneously.

## 6. Choice-timing witness

For

`p = a.(b+c)`

and

`q = a.b + a.c`,

terminal traces agree but branching signatures do not.

At depth1, p and q remain equivalent because their a-successors are still in one observation class.

Depth1 already separates the intermediate states:

- r supports both b and c;
- s only b;
- t only c.

At depth2:

`σ_2(p)` contains one a-child type `[r]`,

while

`σ_2(q)` contains two a-child types `[s],[t]`.

So branching depth2 detects the timing of nondeterministic choice although no literal terminal word does.

## 7. The information lost by terminal union

Word traces independently ask what can happen after each chosen action sequence.

They do not retain the joint answer to:

> which collection of future behaviours belongs to one and the same successor branch?

Branching signatures retain that correlation by grouping future behaviour **per successor type before unioning**.

This is why branching-time semantics can distinguish processes with the same linear-time traces.

## 8. Still only support precision

The set constructor removes duplicate equal successor signatures.

Thus `σ_h` still forgets:

- how many raw successors have the same behavioural type;
- multiple parallel witnesses to the same state;
- path identity/provenance;
- branch-local history or cost.

A count-sensitive or witness-sensitive future language requires a richer successor aggregator than `set`.

This opens the next precision axis naturally:

`terminal union`

`< set of successor behavioural types`

`< multiset/count of successor behavioural types`

`< explicit witness/provenance state`,

where each strictness depends on the declared future semantics.

## 9. Semantic-preorder interpretation

The same raw A4 relation can therefore support several legitimate precision objects:

- trace quotient, if the future asks only terminal reachable support;
- support-bisimulation quotient, if the relation itself must descend as a set-valued operation on behavioural classes;
- richer witness quotients, if multiplicity/provenance is reactivated.

No scalar “relation precision” orders these without naming the required interface.

## 10. Prior-art boundary

Tree unfoldings, bisimulation approximants, modal transition semantics and trace projections are standard prior mathematics/computer science. A4 retains correspondence/witness ownership; P023/A2 retains future-signature/kernel ownership.

The project value is the explicit factorization:

> **direct multivalued-operation precision is the kernel of a recursive branching future signature, and terminal support traces are a strict coarse projection of that signature in general.**