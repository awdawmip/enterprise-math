# E002 — Finite Predictive Quotient Compiler, Supplement 06

Status: `ACTIVE ENGINEERING RESEARCH NOTE`  
Scope: generic finite predictive partition compilation and reconstruction of E002 closed forms  
Parent: `docs/E002_TASK_RELATIVE_OBSERVABLE_SUPPLEMENT_05.en.md`  
Dependency: P023 future-compatible quotient theory  
Prior art: `docs/PRIOR_ART_E002_PREDICTIVE_QUOTIENT.en.md`

## 1. Motivation

Stages 1–5 derived a growing collection of closed integer precision formulas for specific physical actions and future queries. A serious risk is that these formulas are merely hand-selected coincidences rather than instances of one operational state principle.

Stage 6 therefore stops deriving the next special-case formula first. Instead it builds a generic finite compiler:

\[
\boxed{
(\text{fine states},\text{actions},\text{observation},\text{horizon})
\longmapsto
\text{coarsest predictive partition}.
}
\]

The compiler knows none of the E002 gcd, residue, vector-product, binomial, or Boolean formulas. Those formulas count as independently recovered only if the generic compiler produces the same partitions/cardinalities from the underlying finite system.

Finite-state behavioral equivalence and automaton minimization are established prior mathematics. [SRC-MOORE-1956-SEQUENTIAL-MACHINES] [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION] E002 does not claim a new minimization algorithm.

## 2. Finite system

Let

\[
X
\]

be a finite nonempty state set. Let

\[
\mathcal A=\{T_a:X\to X\}
\]

be a finite nonempty family of total deterministic actions, and let

\[
O:X\to Y
\]

be a finite-valued observation map.

For an action word

\[
v=a_1\cdots a_k,
\]

write

\[
T_v=T_{a_k}\circ\cdots\circ T_{a_1},
\]

with the empty word acting as the identity.

No probability, real-valued metric, embedding, or infinite-precision completion is needed.

## 3. Horizon-indexed predictive equivalence

Define equivalence relations recursively.

At horizon zero,

\[
\boxed{x\sim_0y\iff O(x)=O(y).}
\]

For `h>=0`, define

\[
\boxed{
x\sim_{h+1}y
\iff
O(x)=O(y)
\ \text{and}\ 
T_a(x)\sim_hT_a(y)
\text{ for every }a\in\mathcal A.}
\]

This is exactly the partition-refinement recurrence implemented by

- `observation_partition`,
- `refine_predictive_partition`,
- `finite_horizon_partition`.

## 4. E002-T33 — Exact finite-horizon semantics

For every `h>=0`,

\[
\boxed{
x\sim_hy
\iff
O(T_v(x))=O(T_v(y))
\text{ for every action word }v\text{ with }|v|\le h.}
\]

Therefore `~_h` is the coarsest partition of `X` that preserves the complete declared observation future through horizon `h`.

### Proof

By induction on `h`.

For `h=0`, the only word is the empty word, so the statement is the definition of `~_0`.

Assume the result for `h`. By definition,

\[
x\sim_{h+1}y
\]

requires equal current observations and

\[
T_a(x)\sim_hT_a(y)
\]

for every first action `a`. By the induction hypothesis, the latter is equivalent to equal observations after every suffix word of length at most `h` from those successor states. These are exactly all nonempty action words from `x,y` of length at most `h+1`. Together with the empty word/current observation, this gives the claimed language. ∎

### Consequence

Any two states merged by `~_h` are behaviorally interchangeable for the declared finite future language. Any coarser partition would merge some pair distinguished by at least one allowed word/observation and would therefore fail predictive sufficiency.

This makes horizon an explicit precision obligation rather than an informal planning parameter.

## 5. E002-T34 — Monotone finite stabilization and stable congruence

The predictive relations refine monotonically:

\[
\boxed{
\sim_{h+1}\ \subseteq\ \sim_h.
}
\]

Equivalently, block counts are nondecreasing with horizon.

Because `X` is finite, the sequence stabilizes after finitely many strict refinements. If `b_0` is the number of current-observation blocks, then there can be at most

\[
\boxed{|X|-b_0}
\]

strict refinement rounds.

Let the stable relation be

\[
\sim_*.
\]

Then:

1. `~_*` refines current observation equality;
2. `~_*` is an action congruence:
   \[
   x\sim_*y\implies T_a(x)\sim_*T_a(y)
   \quad\forall a\in\mathcal A;
   \]
3. `~_*` preserves observations after **every finite action word**;
4. `~_*` is the coarsest equivalence relation with properties 1–2.

### Proof

T33 immediately implies monotonicity because every horizon-`h+1` future language contains the horizon-`h` language.

Every strict refinement increases the number of nonempty blocks by at least one. A partition of `|X|` states has at most `|X|` blocks, giving the finite bound.

At a fixed point, the recursive definition of `~_(h+1)` equals `~_h`, so equivalent states have equivalent successors under every action: this is congruence. Congruence then propagates equivalence along arbitrary finite action words, while current observation equality gives equal output after every propagated word.

Finally, let `R` be any action congruence that refines observation equality. By induction on `h`, `x R y` implies `x~_h y`: true at `h=0`; if true at `h`, congruence gives `T_a(x) R T_a(y)`, hence successor `~_h` equivalence, proving `~_(h+1)`. Thus `R` is contained in every `~_h`, and hence in `~_*`. Therefore `~_*` identifies at least as many states as every other safe congruence and is the coarsest one. ∎

## 6. Compiler outputs

The executable compiler exposes three useful products.

### Finite-horizon partition

`finite_horizon_partition` returns block labels for `~_h`.

### Stable quotient

`stable_predictive_partition` returns

- the stable partition;
- the first stabilization depth;
- the stable block count.

### Executable quotient machine

For a safe stable partition:

- `quotient_transition_table` constructs the induced deterministic action table;
- `quotient_observation_table` constructs one observation per quotient state.

Both functions reject a proposed partition when it merges states whose future transition/output behavior is not well-defined.

Thus the result is not only a cardinality estimate. It is an executable finite world-state machine.

## 7. Restricted initial fibers

E002 formulas usually count the fine phases inside one declared coarse precision cell rather than all states in a globally closed test system.

The compiler therefore separates:

- the finite closed state set on which actions operate;
- a declared initial subset/fiber whose predictive block count is measured.

`restricted_block_count` counts how many compiled predictive blocks intersect that initial fiber.

This allows a finite closed harness to model a local precision cell without pretending that physical actions stop at its boundary.

## 8. E002-T35 — Generic reconstruction of earlier closed forms

Use a finite countdown system for the diagonal-unit-action experiments:

\[
X=\{0,1,\ldots,w\}^n,
\]

with action

\[
T(x_1,\ldots,x_n)
=(\max(0,x_1-1),\ldots,\max(0,x_n-1)).
\]

Interpret states `1..w` in each coordinate as the original fine phases and state `0` as 'already crossed'.

The compiler is given only this transition and the selected observation map. It is **not** given the hand-derived class formulas.

Then bounded reconstruction verifies:

### Complete vector observation

For

\[
O_{\rm full}(x)=(\mathbf1_{x_1=0},\ldots,\mathbf1_{x_n=0}),
\]

it recovers

\[
\boxed{(h+1)^n}
\]

initial-fiber classes for `h<w`.

### Symmetric sum

For

\[
O_{\rm sum}(x)=\sum_i\mathbf1_{x_i=0},
\]

it recovers

\[
\boxed{\binom{h+n}{n}}.
\]

### Boolean ANY / ALL

For

\[
O_{\rm ANY}=\mathbf1_{\exists i:x_i=0},
\qquad
O_{\rm ALL}=\mathbf1_{\forall i:x_i=0},
\]

it recovers

\[
\boxed{h+1}
\]

independently of dimension.

### Two-coordinate linear observations

For

\[
O_{\alpha,\beta}
=\alpha\mathbf1_{x_1=0}+\beta\mathbf1_{x_2=0},
\]

it independently recovers the complete T29 coefficient classification:

\[
1,\ B,\ B(B+1)/2,\ B(B-1)+1,\ B^2
\]

in the corresponding coefficient cases.

### Boolean equality

For

\[
O_=(x)=
\mathbf1_{(x_1=0)=(x_2=0)},
\]

it recovers

\[
\boxed{1+h(h+1)/2}.
\]

These reconstructions show that the earlier E002 formulas are special closed forms of one generic predictive equivalence compiler on these finite systems.

They do not prove that every future Enterprise Math problem will have a simple closed form.

## 9. What has changed conceptually

The engineering line can now be stated without controller-specific terminology:

\[
\boxed{
\text{fine finite world state}
+\text{allowed actions}
+\text{declared observation}
+\text{future horizon}
\longrightarrow
\text{minimal predictive quotient}.
}
\]

The quotient may coincide with:

- a coarse precision cell;
- a gcd refinement;
- a finite horizon residue rank;
- a product of coordinate ranks;
- a multiset summary;
- a Boolean crossing bucket;
- or an irregular finite partition with no short arithmetic formula.

The arithmetic formulas from Stages 1–5 are useful exactly when they allow the generic quotient to be represented without enumerating all fine states.

## 10. Relation to P023

P023 owns the general principle that future operations must factor through a retained state and that the coarsest safe repair is language-relative.

Stage 6 is an executable finite deterministic specialization:

- T33 gives exact finite-word semantics;
- T34 computes the stable common-compatible congruence by classical finite partition refinement;
- T35 uses that generic oracle to falsify or recover E002 closed forms.

E002 therefore does not promote the compiler algorithm into a new Foundations theorem family. Its role is engineering verification and automatic state synthesis.

## 11. Prior-art boundary

Moore's sequential-machine work is prior art for finite state/output behavioral distinction. [SRC-MOORE-1956-SEQUENTIAL-MACHINES]

Hopcroft's automaton-minimization work is prior art for state minimization and partition refinement. [SRC-HOPCROFT-1971-AUTOMATON-MINIMIZATION]

E002 makes no claim that the recurrence, stable minimization, or finite-state quotient compiler is historically new.

The project-specific experiment is the interpretation and use of that compiler as a finite-precision world-state synthesizer constrained by explicit physical/control action and observation languages.

Historical novelty remains `NOVELTY_UNVERIFIED`.

## 12. Executable audit

Implementation:

- `src/enterprise_math/predictive_quotient.py`

Tests:

- `tests/test_predictive_quotient.py`

The tests check generic finite stabilization, distinguishing horizons, quotient transition/output tables, unsafe-partition rejection, and automatic reconstruction of E002 Stage-4/5 formulas over bounded finite domains.

Independent reconstruction also implemented the recurrence separately and reproduced the full-vector, symmetric-sum, and ANY formulas without using their closed forms inside the refinement algorithm.

## 13. Falsification criteria

Stage 6 fails or must be narrowed if:

1. the recursive partition does not match direct enumeration of observation futures through the same horizon;
2. a stable partition does not define deterministic quotient actions/observations;
3. a strictly coarser action congruence preserving the observation exists than the claimed stable partition;
4. the generic compiler fails to reconstruct an E002 formula on a domain where that formula is claimed exact;
5. finite-state minimization/partition refinement is described as an Enterprise Math invention.

## 14. Next pressure tests

The compiler makes the next questions operational:

1. allow state-dependent/partial action availability and compile controller-policy languages rather than all total actions;
2. compare enumerated quotient size/runtime with closed-form arithmetic specializations to measure when the mathematics buys engineering speed;
3. feed E001 vector collision states and Boolean collision observations into the compiler and search automatically for smaller future-safe collision state;
4. add product controller memory and delayed queues as explicit finite states;
5. search compiled partitions for arithmetic/geometric regularity, then prove closed forms only after the generic oracle exposes a pattern.
