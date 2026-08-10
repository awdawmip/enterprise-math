# P025 Supplement 148 — Bounded progress gives an exact completion deadline

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Quantitative scheduler contract

Stage 147 separated unrestricted scheduling from qualitative weak fairness. To obtain a finite deadline, impose an explicit stronger quantitative contract.

For a positive integer `B`, define the **B-progress contract**:

> while the helper process is nonterminal, every consecutive block of `B` scheduler steps contains at least one actual helper firing.

Scheduler steps may otherwise stutter. Each helper firing completes exactly one previously incomplete helper.

This is a deliberately explicit progress contract, not an attempt to rename every standard bounded-fairness convention.

## 2. Exact upper bound

Let

\[
r(I)=m-|I|
\]

be the number of helpers still incomplete at ideal `I`, where `m` is the total helper count.

Each block of at most `B` scheduler steps completes at least one helper. Hence after at most

\[
Br(I)
\]

steps all remaining helpers have fired:

\[
\boxed{T_{max}(I;B)\le B\,r(I).}
\]

## 3. Sharpness

The bound is attained by the scheduler that, whenever the process is nonterminal,

1. stutters for `B-1` steps;
2. fires exactly one enabled helper on the `B`-th step;
3. repeats.

Stage 147 guarantees every nonterminal ideal has an enabled helper. The schedule therefore remains legal and uses exactly `B` scheduler steps per completed helper.

Thus

\[
\boxed{T_{max}(I;B)=B\,(m-|I|).}
\]

This is the exact worst-case completion time under the declared B-progress contract.

## 4. State quotient versus value precision

For fixed `B`, the deadline depends only on ideal cardinality. Therefore the deadline future has exactly

\[
\boxed{m+1}
\]

state classes, the same quotient as Stage 146's remaining-helper-work future.

Changing `B` changes the numerical guarantee but does **not** refine the state partition:

\[
I\sim J
\iff
|I|=|J|
\]

for every fixed positive `B`.

Hence liveness-contract strength can change **future value precision** without changing **state precision**.

## 5. Qualitative versus quantitative liveness

Weak fairness from Stage 147 guarantees eventual completion but supplies no uniform finite time bound: it permits arbitrarily long finite delays before a continuously enabled action fires.

The B-progress contract adds exactly the missing quantitative resource and converts eventuality into a sharp deadline.

Thus

\[
\boxed{
\text{weak fairness}\Rightarrow\text{eventual completion},
\qquad
B\text{-progress}\Rightarrow\text{finite exact worst-case deadline}.
}
\]

## 6. Architectural consequence

Scheduler contracts have at least two precision axes:

1. **qualitative liveness** — whether completion is guaranteed;
2. **quantitative progress** — how quickly completion is guaranteed.

Two contracts can induce the same state quotient while returning different quantitative guarantees.

## 7. Prior-art boundary

Bounded progress assumptions and worst-case progress-time bounds are classical scheduling/verification ideas. No generic novelty claim is made. P025 contributes the exact finite specialization and the state/value precision separation.
