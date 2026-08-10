# P025 Supplement 147 — Eventual completion is a scheduler-contract property

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Setup

Use the asynchronous helper-progress ideal system from Stages 144–146. A legal state is an ideal

\[
I\in J(P_{gate})
\]

of a finite helper dependency poset.  Each helper may fire at most once.  A nonterminal ideal always has at least one enabled helper: choose a minimal element of its complement.

We compare three scheduler contracts for the same completion proposition.

## 2. MAY-complete

Ask

> does there exist a legal scheduler execution that completes every helper?

For every ideal `I`, repeatedly choose any enabled helper.  Each firing strictly increases the ideal and the helper set is finite. Therefore a completion execution exists from every state:

\[
\boxed{\operatorname{MAY\_complete}(I)=\mathrm{true}\quad\forall I.}
\]

The MAY-completion future has exactly one state class.

## 3. MUST-complete without fairness

Now let the scheduler be allowed to stutter/no-op indefinitely and impose no fairness requirement.

From every nonterminal ideal, the infinite all-stutter execution is legal and never completes.  The terminal ideal is already complete. Hence

\[
\boxed{
\operatorname{MUST\_complete}_{unrestricted}(I)
\iff
I=P_{gate}.
}
\]

The corresponding future has exactly two classes:

1. terminal;
2. nonterminal.

Thus the same nonterminal state is `MAY=yes` but `MUST=no`.

## 4. Weak fairness is sufficient

Assume **weak fairness**:

> any helper action that becomes enabled and then remains continuously enabled must eventually fire.

Take a nonterminal ideal `I`. Choose a minimal helper `h` outside `I`. All helper predecessors of `h` already lie in `I`, so `h` is enabled. Since completed helpers are monotone and prerequisites are never removed, `h` remains enabled until it fires.

Weak fairness therefore forces `h` to fire eventually. The number of remaining helpers strictly decreases. Induction on the finite remaining count gives eventual completion of every helper.

Therefore

\[
\boxed{
\operatorname{MUST\_complete}_{weak\ fairness}(I)=\mathrm{true}
\quad\forall I.
}
\]

Weak fairness is enough; strong fairness is not required for this monotone finite system.

## 5. Exact quotient flip

For the same legal state space and the same observable proposition `eventually complete`, only the scheduler contract changes:

\[
\boxed{
\begin{array}{c|c}
\text{future contract} & \#\text{truth-value classes}\\
\hline
\text{MAY completion} & 1\\
\text{MUST, unrestricted stutter} & 2\\
\text{MUST, weak fairness} & 1
\end{array}}
\]

The future quotient therefore cannot be specified from state geometry alone.

## 6. Scope correction for Stage 146

Stage 146's endpoint-one-class statement is correct only after declaring a completion/liveness contract such as weak fairness or an explicit `run-to-saturation` operation.

Without such a contract, `eventual saturated endpoint` is not a total deterministic future observable under arbitrary asynchronous scheduling.

## 7. Architectural consequence

A future specification needs at least three logically separate ingredients:

1. state/transition legality;
2. path quantifier (`MAY`, `MUST`, or a selected deterministic scheduler);
3. liveness/fairness assumption on admissible infinite executions.

Changing only items 2–3 can change the coarsest future-safe quotient while all states and transitions remain fixed.

## 8. Prior-art boundary

MAY/MUST path semantics, weak fairness, liveness and finite well-founded progress arguments are classical transition-system/concurrency theory. No generic novelty claim is made. P025 contributes the exact finite pressure-test instance and the scope correction needed by the precision architecture.
