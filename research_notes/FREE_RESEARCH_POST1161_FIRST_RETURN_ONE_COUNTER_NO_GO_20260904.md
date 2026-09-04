# Post-#1161 free research — one-counter minimal predictive quotient and fixed-finite G0 no-go

Status: `FREE_RESEARCH_SUCCESSOR_RESULT / MINIMAL PREDICTIVE COUNTER + G0 COLLISION NO-GO / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-G61R8`
Predecessor: `research_notes/FREE_RESEARCH_POST1161_FIRST_BALANCE_RETURN_G0_BOUNDARY_20260904.md`

## 0. Question

The first-balance-return reconstruction of the AGM shape/geometric channel is exact at the history level. The remaining question is whether the required history can be compressed into a fixed finite local state, ideally the current instantaneous native cell state, while preserving every future first-return mass.

The answer again splits cleanly:

\[
\boxed{\text{fixed finite exact predictive state} = \text{NO}}
\]

but

\[
\boxed{\text{one }\mathbb N_0\text{-valued counter is exact and minimal}.}
\]

For a finite future horizon `h`, the exact predictive quotient has only

\[
\boxed{h+2}
\]

classes.

## 1. Alive branch histories and imbalance

Fix the unlabeled two-element commuting-diamond witness fiber `D`. For a finite word `w` in `D`, let

\[
\mu_w:D\to\mathbb N_0
\]

be the multiplicity function. Before the first balanced prefix occurs, define the absolute imbalance

\[
\boxed{
d(w)=|\mu_w(d_1)-\mu_w(d_2)|
}
\]

for either ordering `{d_1,d_2}=D`.

Because of the absolute value, `d(w)` is invariant under the full branch relabeling `Sym(D)=S_2`; no preferred witness is selected.

A balanced return is exactly the event `d=0`.

For an alive state `d>0`, one additional branch witness changes the imbalance by one:

\[
\boxed{d\longrightarrow d-1\ \text{or}\ d+1,}
\]

one branch choice for each transition. State `d=0` is terminal for the first-return observer.

Thus the full path history admits an exact one-counter Markovization.

## 2. Exact first-hitting count

Let `N_m(d)` be the number of `m`-letter continuations from an alive imbalance `d>0` that hit zero for the **first** time exactly at the final step `m`.

The reflection/ballot count is

\[
\boxed{
N_m(d)
=
\frac d m
\binom{m}{(m-d)/2}
}
\]

when

- `m>=d`, and
- `m-d` is even,

and `N_m(d)=0` otherwise.

For the terminal state, define `N_0(0)=1` and `N_m(0)=0` for `m>0`.

The all-future return signature is therefore

\[
\boxed{
\Sigma(d)=(N_0(d),N_1(d),N_2(d),\ldots).
}
\]

This signature depends only on `d`; hence the integer imbalance is sufficient for all future first-return counts and therefore for every first-return mass used by the AGM successor RG.

## 3. Minimality of the counter

Distinct positive counter values have distinct predictive signatures.

Indeed, from state `d>0`, the earliest possible first return is exactly time `d`, and

\[
N_d(d)=1.
\]

If `e>d`, then

\[
N_d(e)=0.
\]

Therefore

\[
\boxed{d\ne e\Longrightarrow\Sigma(d)\ne\Sigma(e).}
\]

So any exact all-horizon quotient preserving first-return counts must distinguish every nonnegative integer imbalance.

Consequently the one-counter quotient is not merely sufficient; it is the coarsest exact predictive quotient at this observer strength.

## 4. Fixed-finite-state no-go

Because the signatures

\[
\Sigma(0),\Sigma(1),\Sigma(2),\ldots
\]

are pairwise distinct, there are infinitely many predictive equivalence classes.

Hence no deterministic state machine with a fixed finite state set can exactly preserve the all-horizon first-return language or its length-resolved masses:

\[
\boxed{
\text{FIXED FINITE CARDINALITY FIRST-RETURN PREDICTIVE STATE}
=\text{IMPOSSIBLE}.}
\]

This is a Myhill-Nerode/predictive-quotient obstruction, not a numerical limitation.

It is fully compatible with the project commitment that finite resolution is endogenous: at every finite time the counter value is a finite integer, even though the set of possible exact states is unbounded across all times.

## 5. Finite-horizon quotient: exactly `h+2` classes

For a declared future horizon `h`, retain only

\[
\Sigma_h(d)=(N_0(d),\ldots,N_h(d)).
\]

Then:

1. states `d=0,1,\ldots,h` are pairwise distinct because state `d` has its first nonzero future return at time `d`;
2. every state `d>h` has the all-zero signature through horizon `h`.

Therefore the exact horizon-`h` predictive quotient is

\[
\boxed{
\{0\},\{1\},\ldots,\{h\},\{d:d>h\},
}
\]

with

\[
\boxed{h+2\text{ classes}.}
\]

This gives an explicit finite precision law for the memory required by a bounded future language.

## 6. Direct current-G0 collision witness

The repeated commuting-diamond construction recoalesces each local diamond to its common terminal cell. Therefore different branch histories of the same block length may share the same current cell and the same block-time index.

Consider four consecutive diamond blocks and the two still-alive histories

\[
w_1=AAAA,
\qquad
w_2=AAAB.
\]

Neither has an earlier balanced prefix. At the end of block four:

- they have the same recoalesced current terminal cell;
- they have the same time/block index `4`;
- the local current incidence type is the same;
- but
  \[
  d(w_1)=4,
  \qquad
  d(w_2)=2.
  \]

From `w_2`, two opposite-branch choices give a first return at future time `2`. From `w_1`, no two-step continuation can return; its earliest return is time `4`.

Thus

\[
\boxed{
(\text{current cell},\text{time index},\text{current local incidence})
\not\Rightarrow
\text{future first-return signature}.}
\]

This is a concrete same-G0-observation / different-future witness.

It also proves that the counter is not merely a renamed time coordinate: two states at the same time have different counter values and different futures.

## 7. Minimal Markov augmentation

At the successor's declared observer strength, the smallest exact Markov state is therefore

\[
\boxed{(\text{current native placement/type as required},\ d)}
\]

with `d in N_0`, rather than the full branch word.

For the repeated translated identical-diamond experiment itself, the current cell recoalesces and carries no additional first-return information, so the effective predictive state reduces further to just

\[
\boxed{d\in\mathbb N_0.}
\]

This is an exact compression of an exponentially growing path-history set to one integer coordinate.

However, `d` is an additional history-derived N1 memory coordinate under the current native-semantics stratification. The collision witness above shows that it is not reconstructible from the existing instantaneous G0 cell plus time index.

Therefore:

- `ONE_COUNTER_MARKOVIZATION = EXACT`;
- `ONE_COUNTER_IS_COARSEST_ALL-HORIZON FIRST-RETURN PREDICTIVE QUOTIENT = PROVED`;
- `FIXED_FINITE_STATE EXACT MARKOVIZATION = NO-GO`;
- `CURRENT G0 CELL + TIME DEFINES COUNTER = FALSE` by explicit collision;
- `PROMOTE COUNTER AS NEW N0 PRIMITIVE = NOT AUTHORIZED / NOT DERIVED`.

## 8. Relation to the AGM first-return RG

The predecessor identifies the first-return generating mass

\[
F(s)=\sum_{n\ge1}f_ns^{2n}
\]

with twice the AGM chord loss,

\[
F=2\ell,
\]

and gives

\[
s^+=\frac{F}{2-F}.
\]

The coefficients `f_n` are precisely the first-return probabilities generated by the counter starting from zero after choosing the first branch step. Hence the entire scalar first-return RG is the generating-function readout of the minimal counter process.

This supplies a sharper architecture:

\[
\boxed{
\text{native two-witness diamond}
\to
\text{N1 minimal imbalance counter }d
\to
\text{N2 first-return mass }F
\to
\text{AGM chord/shape RG}.}
\]

The exponentially large path history is not fundamental at the predictive level; one integer counter is sufficient.

## 9. Executable verification

Committed checker:

`scripts/check_free_research_agm_first_return_predictive_counter.py`

It uses only integer combinatorics and verifies:

- the first-return/Catalan shell formula for `n=1..64`;
- finite horizons `h=0..32` have exactly `h+2` predictive classes;
- all distances `d>h` collapse to one horizon-`h` far class;
- `d=0..h` remain pairwise distinct;
- the first `64` positive counter states are pairwise distinguishable by finite future signatures;
- the explicit `AAAA` versus `AAAB` current-G0 collision.

The checker was fetched back from `main` after commit and independently replayed successfully.

## 10. Tool reuse and novelty boundary

The predictive-equivalence logic is standard Myhill-Nerode/Moore-machine mathematics. Enterprise Math already has predictive-quotient / operation-safe quotient machinery, so this is not proposed as a new general tool family.

The task-specific result is the exact identification of the post-#1161 first-return observer with the minimal absolute branch-imbalance counter and the explicit current-G0 collision witness.

No historical priority claim is made for ballot/reflection counts, Catalan first returns, or one-counter languages.

## 11. Native-semantics verdict

The strongest valid typing is:

\[
\boxed{
\text{G0 native diamond skeleton}
\to
\text{N1 one-counter memory}
\to
\text{N2 AGM return-mass readout}.}
\]

The counter is choice-independent under branch swap and is a canonical quotient of the relevant history language, but that alone does not promote it to current N0/G0: semantic-strength matching requires reconstruction from instantaneous native data, which the collision witness disproves for the current cell+time carrier.

Verdict:

- history compression: `EXACT_RECOVERY`;
- all-horizon predictive quotient: `CONDITIONAL_DERIVED`, countably infinite;
- finite-horizon quotient: exact finite `h+2` classes;
- current instantaneous G0 promotion: `SEMANTIC_MISMATCH / NO-GO AT CURRENT CARRIER STRENGTH`.

## 12. Next smallest question

The current G0 carrier cannot absorb the counter without added state. The next genuinely discriminating question is therefore no longer whether a finite predictive quotient exists; that is settled.

It is:

> Is there an independently motivated existing N0 relational coordinate in the full P000 six-dimensional cell state whose restriction to the repeated-diamond slice realizes this imbalance counter, or does any such realization necessarily introduce a new memory primitive?

A positive result would be a six-dimensional lift of the counter. A negative result would establish that AGM's exact Markovization requires an N1 memory degree of freedom not present in current spatial G0 state.
