# P025 Supplement 149 — Weak fairness equals completion on finite monotone helper runs

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Scope

This supplement is deliberately restricted to the finite one-shot helper process from Stages 144–148:

- legal states are ideals of a finite dependency poset;
- completed helpers never become incomplete;
- each helper fires at most once;
- a helper, once enabled, remains enabled until it fires;
- terminal executions are extended infinitely by terminal stuttering when applying standard infinite-run fairness language.

The statement below is not a generic theorem about arbitrary transition systems.

## 2. Completion implies weak fairness

Suppose an execution eventually completes every helper.

Then every helper fires at some finite point. In particular, any helper that is continuously enabled from some time onward eventually fires.

Hence every completing execution is weakly fair:

\[
\boxed{\text{completion}\Rightarrow\text{weak fairness}.}
\]

## 3. Weak fairness implies completion

Take a weakly fair execution and suppose its current ideal is nonterminal. A minimal helper in the complement has all predecessors completed, so it is enabled. Because completed helpers and prerequisites are monotone, this helper remains continuously enabled until firing.

Weak fairness forces it to fire eventually. The finite number of unfinished helpers decreases by one. Induction gives eventual completion of all helpers.

Therefore

\[
\boxed{\text{weak fairness}\Rightarrow\text{completion}.}
\]

## 4. Exact execution-class equality

Combining both directions,

\[
\boxed{
\{\text{weakly fair executions}\}
=
\{\text{eventually completing executions}\}.
}
\]

So, for this special monotone process, weak fairness is neither an extra hidden trace refinement beyond completion nor a weaker surrogate: it selects exactly the completing executions.

## 5. Why this matters for future precision

Stage 147 showed that adding weak fairness changes MUST-completion from false on every nonterminal state to true everywhere. Stage 149 explains the mechanism more sharply: the fairness restriction is exactly a restriction of the admissible execution family to completing runs.

Thus liveness assumptions can be understood as part of the **future-path domain**, analogously to Stage 138/142 hidden-state legality domains.

## 6. Boundary

The equivalence relies on finiteness, monotone one-shot actions and persistence of enabledness. It need not survive systems with resets, reversible actions, recurring events, or enabledness that can disappear before firing.

## 7. Prior-art boundary

Weak fairness and finite progress arguments are standard concurrency theory. No generic novelty claim is made. P025 contributes only the exact scoped identification inside the current precision testbed.
