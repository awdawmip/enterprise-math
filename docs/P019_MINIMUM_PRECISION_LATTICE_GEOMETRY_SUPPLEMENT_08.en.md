# P019 Supplement 08 — Future-Composition Equivalence and Safe Trace Erasure

Status: `RESEARCH WIP / ABSTRACT FINITE THEOREMS PROVED`

## 1. Why there is no unconditional smallest trace

Supplement 07 shows that:

- minimum values can be strongly compressed;
- minimum provenance can also be compressed associatively;
- a one-step full fiber relation can be compressed to `[L,U]`;
- a selected multi-step boundary witness can remain sensitive to the oriented contraction history.

Therefore the question "how much history must be retained?" has no task-independent answer.

The correct question is:

> Given the future operations that are allowed and the observations that may be read, can two fine states ever be distinguished in the future?

Only states that can never be distinguished by that declared future language may be safely merged.

## 2. Future program family

Let `X` be a finite fine-state space.

Let

\[
\mathcal A=\{T_a:X\to X\}_{a\in A}
\]

be a finite family of deterministic discrete operations, and let

\[
O:X\to Z
\]

be the currently allowed observation.

For a finite operation word

\[
w=a_1a_2\cdots a_k
\]

write

\[
T_w=T_{a_k}\circ\cdots\circ T_{a_1}.
\]

The empty word denotes the identity.

## 3. P019-X13 — Future-composition equivalence

Define

\[
\boxed{x\equiv_{\mathcal A,O}y}
\]

if and only if, for every finite operation word `w`,

\[
\boxed{
O(T_w(x))=O(T_w(y)).
}
\]

This is an equivalence relation.

It does not assert that `x` and `y` are ontologically identical. It states only that no finite future program expressible in the declared operation/observation language can distinguish them.

## 4. P019-X14 — Coarsest safe quotient

Let a candidate summary/collapse be

\[
q:X\to Y.
\]

Call `q` **future-safe** for `(A,O)` when

\[
q(x)=q(y)
\Longrightarrow
x\equiv_{\mathcal A,O}y.
\]

Thus every coarse fiber contains only states with identical future behavior in the declared language.

Let

\[
\pi_*:X\to X/{\equiv_{\mathcal A,O}}
\]

be the canonical behavioral quotient. Then

\[
\boxed{
\pi_*\text{ is the coarsest future-safe quotient.}
}
\]

More precisely, if `q` is future-safe, there is a unique well-defined map

\[
h:q(X)\to X/{\equiv}
\]

such that

\[
\boxed{
\pi_*=h\circ q.
}
\]

Proof: if `q(x)=q(y)`, future safety implies `x equiv y`; hence mapping `q(x)` to `[x]` is independent of representative. ∎

This turns "minimum sufficient trace" into a quotient universal property rather than a storage heuristic.

## 5. Finite future horizon

Often exact composability is required only for the next `L` steps.

Define

\[
x\equiv_L y
\]

when

\[
O(T_w(x))=O(T_w(y))
\]

for every word with `|w|<=L`.

Then

\[
\equiv_0
\supseteq
\equiv_1
\supseteq
\equiv_2
\supseteq\cdots.
\]

Longer lookahead can only refine the partition.

Define the integer future-resolution count

\[
Q_L=|X/{\equiv_L}|.
\]

Then

\[
\boxed{Q_{L+1}\ge Q_L.}
\]

For one state define residual ambiguity multiplicity

\[
A_L(x)=|[x]_L|.
\]

Then

\[
\boxed{A_{L+1}(x)\le A_L(x).}
\]

No logarithm or entropy primitive is required; future resolution is an integer partition refinement.

## 6. P019-X15 — Once finite refinement stops, it stays stopped

If for some `L`

\[
\equiv_{L+1}=\equiv_L,
\]

then

\[
\boxed{
\equiv_k=\equiv_L
\quad\forall k\ge L.
}
\]

Proof: if `x equiv_L y`, equality with `equiv_(L+1)` implies that for every generator `T_a` and every word `v` of length at most `L`,

\[
O(T_v(T_a(x)))=O(T_v(T_a(y))),
\]

because the composite word has length at most `L+1`. Thus

\[
T_a(x)\equiv_L T_a(y).
\]

So `equiv_L` is stable under every generator; induction gives all future lengths. ∎

If `X` is finite, every strict refinement increases the number of classes by at least one and the count cannot exceed `|X|`; hence refinement terminates finitely.

Define the first stable level as the **composition horizon**

\[
\boxed{H_{comp}}.
\]

Beyond this horizon, looking further into the future does not force additional state distinctions.

## 7. Direct relation to P018

P018 promotes precision refinement itself to a mathematical operation.

Here we obtain another finite partition refinement:

\[
\text{longer future obligation}
\Rightarrow
\text{finer state distinction}.
\]

Trace precision can therefore be viewed as

`precision required by current observations + precision required by future composability`.

This is not extra digits around a hidden real value; it is additional distinguishability in a finite state partition.

## 8. Dual direction relative to P010/P011

In P010 forward many-to-one evolution, history-fiber multiplicity can grow:

\[
M_{t+1}(x)\ge M_t(x).
\]

Under future-lookahead refinement here, ambiguity fibers can only shrink:

\[
A_{L+1}(x)\le A_L(x).
\]

Thus there is a structural duality:

- **actual forward collapse** merges history classes;
- **increasing future obligations** force summary classes to split.

These are not the same notion of information.

## 9. Concrete contraction-trace classification

### 9.1 Minimum energy / ball membership only

If all future operations depend only on

\[
E_{\mathbf m}^{(s)}(c),
\]

then

`visible totals + block sizes + power`

is already future-safe.

The full contraction history is unnecessary.

### 9.2 Minimum-witness multiplicity only

For `s>1`, the binomial remainder profile / provenance polynomial is reconstructible from the current tagged state.

History can again be erased.

### 9.3 One-step full fiber relation

`[L,U]` is the local candidate minimum summary; it determines both endpoints and multiplicity.

### 9.4 Selected multi-step boundary witness

The Supplement 06/07 counterexamples show that the final partition is not future-safe.

The complete oriented contraction flag is currently a sufficient summary.

### 9.5 Exact historical identity

If the observation language itself contains fine-witness identity, then on the observed component

\[
x\equiv y\iff x=y.
\]

No nontrivial history collapse is future-safe in that language.

## 10. Full relation versus selected representative

A key correction follows.

If a future query asks only

> Which fine witnesses remain possible from the present coarse state?

then the actual contraction tree need not be preserved. The full relation can be defined directly as the complete feasible preimage of the present coarse fiber under the current threshold/cost law.

Non-associativity of the selected right-boundary representative comes from performing a canonical endpoint selection at each level, not from a failure of relational composition itself.

This matches P021:

- witness relation is the composition-complete primitive;
- cardinality or one selected representative is a shadow;
- witness identity may be deleted only after proving that the shadow is safe for the future query.

## 11. Automorphism-safe quotient

P012/P019 use graph-automorphism orbits as an intrinsic relation/direction language.

If the future operation family is equivariant under a group `G` and all observations are `G`-invariant, then a `G`-orbit is a candidate merge class.

But the orbit quotient is usable only after future safety is verified for the full declared language.

A single orbit still does not prove physical isotropy; this section concerns only operational indistinguishability.

## 12. Prior-art boundary

Future behavioral equivalence, automata state minimization, bisimulation/coarsest relational partitions, and partition-refinement algorithms are established subjects.

P019 does not claim these general tools. The research target is their integration with:

1. finite-precision collapse/fibers/block-size tags;
2. an exact criterion for when contraction history may be erased;
3. P010/P011/P018/P021 history, collision, precision, and witness composition.

Formal source/lineage registration is required before promotion.

## 13. Next step

Priorities:

1. implement a finite partition-refinement reference algorithm for contraction toy systems;
2. measure `Q_L`, `A_L`, and `H_comp`;
3. determine which portions of a P019 boundary trace first lose future distinguishability;
4. test whether exact relations can be compressed by interval/multiplicity/provenance-polynomial combinations instead of full witness trees;
5. unify the result with P021 witness join as one shared safe-collapse criterion.
