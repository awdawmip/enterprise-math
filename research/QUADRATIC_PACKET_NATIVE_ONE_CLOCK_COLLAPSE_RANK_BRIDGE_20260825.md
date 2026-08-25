# Quadratic Packet — Native One-Clock Collapse Rank Bridge

Status: `FROZEN RESEARCH THEOREM / SAME-CONTEXT DERIVATION / NOT FOUNDATION PROMOTION`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-5K7N2Q`

Route: `QUADRATIC-PACKET-GROTHENDIECK-ARITHMETIC-FRONTIER`

## 0. Question

Explain, without assuming the algebraic QP-R2 hypotheses back into the native substrate, why a **primitive one-clock downward precision-collapse sector** should have the three local linear shadows

1. `dim coker(E)=1`;
2. `rank(E^2)<rank(E)`;
3. `rank(E^2) in {0,rank(E)}` under typed self-composition.

The proof below is relation-first. Linear algebra is introduced only as a canonical readout after the native collapse object has been specified.

## 1. N0-alone no-go

The current packet/path N0 language contains discrete packet units, adjacency/transition/path/count and optional refinement/channel relations. It does not contain a vector space, a phase endomorphism, a module quotient, nilpotent multiplication or an algebraic self-composition law.

Therefore the three rank conditions cannot be consequences of bare PF-N0 without an explicit definability bridge.

A direct semantic independence witness is enough. Fix any admissible PF-N0 reduct `M`. Extend it by an otherwise independent finite-dimensional linear readout `(V,E)` in four ways:

- `E=J_2`: corank one, strict rank drop and the zero branch of the rank dichotomy all hold;
- `E=J_3`: corank one and strict rank drop hold, but `rank(E)=2`, `rank(E^2)=1`, so the rank dichotomy fails;
- `E=diag(1,1,0)` on a 3-space: corank one and `rank(E^2)=rank(E)` hold, but strict rank drop fails;
- `E=J_2 direct-sum 0` on a 3-space: strict rank drop and `E^2=0` hold, but corank is two.

All four expansions have exactly the same PF-N0 reduct. Hence no theorem stated solely in the current PF-N0 language can force any one of the three linear conditions unless the additional linear object is first defined from N0/N1 structure at the same semantic strength.

This is not a failure of the quadratic theorem. It identifies the necessary bridge layer.

## 2. Native relational object

Let

`C=(X,0,c)`

be a finite pointed deterministic collapse system.

- `X` is a finite set of distinguishable states at one declared precision sector;
- `0` is the no-residual-phase/coarse state;
- `c:X->X` is one application of the selected downward precision-collapse operation;
- `c(0)=0`.

Write

`X^*=X\{0}`

and, for `j>=1`,

`R_j = c^j(X^*) intersect X^*`.

Thus `R_j` is the nonzero residual phase information still present after `j` applications.

The following three requirements contain no rank, matrix, nilpotent algebra or quadratic law.

### NC1 — one-clock / unique unresolved source

`|X^* \ R_1| = 1`.

Equivalently, exactly one nonzero phase state is not itself the image of a finer nonzero phase state.

This is the relation-level statement that the selected primitive sector has one unresolved phase/refinement source rather than several independent clocks/channels.

### NC2 — genuine downward finite collapse

`c` is nontrivial on `X^*`, and every `x in X^*` reaches `0` after finitely many iterations.

Because `X` is finite, there is one common `N` such that

`c^N(X^*)={0}`.

A recurrent cycle is therefore typed as transport/persistent memory, not as downward precision collapse.

### NC3 — primitive typed self-composition / no hidden residual type

After one collapse, a second application is required to stay inside the already-declared primitive residual type or erase it completely. Formally,

`R_2 = empty`

or

`R_2 ~= R_1`

by an allowed type-preserving native relabeling.

A proper nonempty residual `R_2` of a genuinely new type is forbidden **only in this primitive one-clock sector**: it would mean either

- an additional observable residual-depth/precision type exists, so the sector was not one-clock/primitive; or
- the additional depth is hidden, in which case the declared one-clock state is not sufficient to predict its own future self-composition.

Thus NC3 is the operational closure form of `primitive + no hidden precision`, not a disguised rank condition.

## 3. Canonical linearization

Let `k` be any field; for QP-R2 comparison one may take `k=F_ell`.

Define the reduced free linearization

`V_k = k[X^*]`.

For each basis vector `[x]`, define

`E[x] = [c(x)]` if `c(x)!=0`,

and

`E[x]=0` if `c(x)=0`.

This construction is canonical up to relabeling of the native state set. No basis geometry is introduced: the basis is just the finite state set itself.

For every `j>=1`,

`im(E^j)=span_k{[y]: y in R_j}`,

so

`rank(E^j)=|R_j|`.

This identity is immediate because a deterministic set map sends every basis state to another basis state or to zero, and the distinct nonzero images are precisely `R_j`.

## 4. Derivation of the three rank structures

### Theorem 4.1 — one-clock gives corank one

By the rank/image formula,

`rank(E)=|R_1|`.

Hence

`dim coker(E)`
`= |X^*|-|R_1|`
`= |X^*\R_1|`
`=1`

by NC1.

Therefore

`ONE_CLOCK -> CORANK_ONE`.

No cyclic abelian quotient was assumed. The cyclic/one-chain quotient appearing in QP-R2 is one integral realization of this relation-level fact.

### Theorem 4.2 — downward finite collapse gives strict rank drop

NC2 implies `E^N=0`, so `E` is nilpotent. It is nonzero by the nontriviality clause.

Suppose `rank(E^2)=rank(E)`. Then

`E:im(E)->im(E)`

is surjective; in finite dimension it is therefore invertible on the nonzero space `im(E)`. But nilpotence of `E` would then make an invertible endomorphism nilpotent on `im(E)`, impossible.

Thus

`rank(E^2)<rank(E)`.

Therefore

`GENUINE_FINITE_DOWNWARD_COLLAPSE -> STRICT_RANK_DROP`.

This is the precise distinction between a collapse and an idempotent/permutation-like transport shadow.

### Theorem 4.3 — primitive typed self-composition gives rank dichotomy

If `R_2=empty`, then

`rank(E^2)=0`.

If `R_2 ~= R_1` by a type-preserving relabeling, then the finite typed sets have equal cardinality, hence

`rank(E^2)=|R_2|=|R_1|=rank(E)`.

Therefore

`rank(E^2) in {0,rank(E)}`.

If the type equivalence is linearized explicitly, the nonzero branch is represented by an invertible relabeling `U` (and, if the clock admits a nonzero scalar phase gauge, by `c U`), giving the QP-R2-style form

`E^2 = c U E`

at the corresponding readout strength.

Thus

`PRIMITIVE_TYPED_SELF_CLOSURE -> SELF_COMPOSITION_RANK_DICHOTOMY`.

## 5. Quadratic rank is now forced before any dual-number assumption

NC2 gives the strict inequality

`rank(E^2)<rank(E)`.

NC3 gives the dichotomy

`rank(E^2)=0` or `rank(E^2)=rank(E)`.

The second branch is impossible. Therefore

`E^2=0`.

Let

`n=dim(V_k)=|X^*|`.

From NC1,

`rank(E)=n-1`

and therefore

`dim ker(E)=1`.

Since `E^2=0`,

`im(E) subset ker(E)`.

Thus

`n-1 = rank(E) <= dim ker(E)=1`.

So `n<=2`.

Because NC2 requires `E!=0`, we have `n>=2`.

Hence

`n=2`.

Therefore the three local rank conditions are not independent algebraic decorations. They are the exact linear shadows of

`ONE CLOCK + DOWNWARD FINITE COLLAPSE + PRIMITIVE TYPED SELF-CLOSURE`.

## 6. Universal one-chain envelope and the appearance of dual numbers

NC1 and NC2 alone imply that the nonzero states form one unbranched chain.

Indeed, start from the unique state not in `R_1`. Its forward `c`-orbit reaches `0`. If any other nonzero state were not on this orbit, following predecessors upward in the finite acyclic collapse graph would produce another nonzero state outside `R_1`, contradicting NC1.

Hence, before imposing NC3, there are labels

`x_(n-1) -> x_(n-2) -> ... -> x_1 -> x_0 -> 0`.

On the integral free module

`V_Z=Z[X^*]`,

the operator `E` is the single nilpotent shift. Taking `x_(n-1)` as cyclic generator gives

`V_Z ~= Z[t]/(t^n)`

as a `Z[t]`-module with `t` acting as `E`.

Equivalently, the algebra generated by the identity and this one primitive phase shift is the truncated polynomial algebra

`Z[epsilon]/(epsilon^n)`.

This is a universal linear envelope of the one-chain relation; it is not inserted into N0.

NC3 then forces `n=2`, so the universal envelope collapses to

`Z[epsilon]/(epsilon^2)`.

Thus the dual-number carrier is recovered as the minimal composition-closed linear envelope of a primitive one-clock downward collapse, rather than assumed as the starting ontology.

## 7. Higher-jet regression

For `n=3`, the chain is

`x_2 -> x_1 -> x_0 -> 0`.

Its linearization is `J_3`:

- corank one holds;
- strict rank drop holds: `2 -> 1`;
- the self-composition rank is the forbidden intermediate value `1`.

Relation-level, `R_1={x_1,x_0}` while `R_2={x_0}`: a proper nonempty residual type appears.

This is exactly the abstract version of the previously proved higher-jet phenomenon:

- `m>2` has genuine intermediate contact strata;
- hidden arithmetic lifts occur above one coarse cyclic phase;
- one-clock multiplicative closure fails.

For `n=2`,

`R_1={x_0}`, `R_2=empty`,

so no hidden residual-depth type exists and the dual-number one-clock family is closed.

## 8. Why this is the strongest legitimate native claim

The current PF-N0 foundation does **not** globally assert NC1-NC3 for every collapse. In particular, canonical Boolean BRC is a different support-level quotient semantics and must not be forced into this precision-nilpotent template.

The proved statement is task-local and typed:

> whenever the project declares a sector to be a **primitive one-clock downward precision collapse with no hidden residual type**, its canonical finite-state linear shadow necessarily has corank one, strict rank drop, self-composition rank dichotomy, and therefore rank two.

This is a definability bridge from relation/operation semantics to the QP-R2 local algebra, not a retroactive mutation of N0.

The native justification of the three words is:

1. **one-clock** — more than one unresolved source is literally more than one independent clock/channel;
2. **downward collapse** — a nonzero recurrent orbit is transport/persistent state, not loss of precision;
3. **primitive + closed** — a proper nonzero second residual either introduces a new declared precision type or is hidden state; both contradict a complete primitive one-clock descriptor.

These are falsifiable semantic type distinctions and do not mention rank two.

## 9. Relation to independently verified QP-R2

The independent QP-R2 audit proved the local algebraic lemma from exactly

- corank one;
- strict rank drop;
- self-composition rank control.

The present theorem supplies a relation-first source for those three conditions in the intended primitive one-clock precision sector.

The two results therefore compose as

`primitive one-clock downward collapse`
`-> [NC1,NC2,NC3]`
`-> [corank one, strict rank drop, rank dichotomy]`
`-> rank two`
`-> dual-number universal envelope`.

The set-theoretic proof already reaches rank two directly; QP-R2 remains useful because it proves the same rigidity in a much broader finite-free algebraic realization class.

## 10. Foundation/admissibility ledger

- declared N0 substrate used: finite discrete packet/state identity, transition/refinement relations;
- task-local N1 operation: deterministic downward precision collapse and its self-composition;
- task-local semantic typing: one-clock, primitive/no-hidden-residual closure;
- N2 readout: free linearization, rank/cokernel, universal generated algebra;
- imported effective target in premises: none;
- quadratic rank or dual numbers in premises: none;
- target leakage: none detected;
- N0-alone implication: refuted by conservative-expansion countermodels;
- bridge theorem status: `PROVED_AT_RELATION_TO_LINEAR_READOUT_STRENGTH`;
- global Foundation promotion: `NOT AUTOMATIC / REQUIRES EXPLICIT INTAKE OF NC1-NC3 AS A DECLARED PRECISION-COLLAPSE SECTOR`.

## 11. Final theorem package

`NATIVE_ONE_CLOCK_COLLAPSE_RANK_BRIDGE`:

For every finite primitive one-clock downward precision-collapse system satisfying NC1-NC3, the canonical reduced free linearization over any field satisfies

`dim coker(E)=1`,

`rank(E^2)<rank(E)`,

`rank(E^2) in {0,rank(E)}`,

hence

`E^2=0`, `dim(V)=2`.

The integral universal envelope is

`Z[epsilon]/(epsilon^2)`.

This proves why the three QP-R2 local structures belong to the **primitive one-clock precision-collapse sector** without treating them as N0 axioms.