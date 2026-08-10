# P025 Supplement 146 — Task-relative quotients of asynchronous helper progress

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Setup and fairness boundary

Fix the asynchronous helper-progress system from Stage 144 with all raw antecedents present and output `z` not yet fired.  A legal pre-output runtime state is an ideal

\[
I\in J(P_{gate})
\]

of the helper dependency poset.

This supplement compares different declared futures on the **same** ideal state space.

Whenever we speak about the eventual saturated raw endpoint, we assume the scheduler is eventually completing/fair enough that every enabled helper required for saturation is eventually fired.  Without such a liveness condition, an asynchronous scheduler may stutter forever and the phrase `eventual saturated endpoint` is not a total future observable.  Stage 147 should isolate that liveness contract explicitly.

## 2. Endpoint-only future

Under eventual completion, every pre-output ideal reaches the same saturated helper state and then the same raw output `z`.

Therefore, for the future language

> return only the final saturated raw endpoint,

all pre-output helper ideals are equivalent:

\[
\boxed{N_{endpoint}=1.}
\]

The enormous ideal lattice from Stages 144–145 contributes zero additional state precision to this endpoint-only query.

## 3. Remaining-helper-work future

If the future asks only

> how many helper firings remain before all helpers are complete?,

then every helper can fire at most once and each asynchronous action completes exactly one helper.  With `m` helpers,

\[
\boxed{R(I)=m-|I|.}
\]

Thus ideal cardinality is sufficient and exact. Every cardinality `0,...,m` occurs along any linear extension, so the quotient has exactly

\[
\boxed{m+1}
\]

classes.

This is a scalar rank quotient of the ideal lattice.

## 4. Enabled-action future breaks rank

Now strengthen the future to ask

> which labelled helper actions are enabled next?

For ideal `I`,

\[
\operatorname{En}(I)
=
\{h\notin I:\operatorname{Pred}(h)\subseteq I\}.
\]

Equal cardinality does not determine this labelled enabled set.

In the four-way balanced compiler the two first-layer helpers are incomparable. The ideals

\[
I_1=\{h_1\},
\qquad
I_2=\{h_2\}
\]

both have size one and therefore the same remaining-work count, but

\[
\operatorname{En}(I_1)=\{h_2\},
\qquad
\operatorname{En}(I_2)=\{h_1\}.
\]

Hence

\[
\boxed{|I|\text{ is not sufficient for labelled next-action semantics}.}
\]

The scheduler-facing future reintroduces labelled support geometry.

## 5. Exact-progress future

If the future asks for exact completed-helper identity, exact internal trace continuation, or any language that distinguishes all ideals, then the full ideal state is retained.  The state count is

\[
\boxed{|J(P_{gate})|},
\]

with the antichain-boundary compression of Stage 144 available as a coordinate chart.

## 6. Precision ladder

For the same raw state, compiler and asynchronous legal state space, the declared future yields the exact ladder

\[
\boxed{
1
\quad\to\quad
m+1
\quad\to\quad
\text{enabled-action quotient}
\quad\to\quad
|J(P_{gate})|.
}
\]

The first two levels are endpoint and remaining-work semantics.  The third depends on labelled action support and can be strictly finer than rank.  The fourth is exact progress identity.

Thus the existence of many legal runtime states does not by itself require equally fine observation precision.

## 7. Architectural consequence

Stage 144 showed that scheduler freedom generates an ideal lattice. Stage 146 shows that the future language decides how much of that lattice must remain visible.

The same runtime therefore admits:

- total collapse for endpoint-only semantics;
- scalar rank for amount-of-work semantics;
- labelled relation/support state for action legality;
- full ideal/antichain state for exact progress.

This is a direct concurrency specialization of A2/P023/P024 future-relative precision.

## 8. Prior-art boundary

Order-ideal rank, enabled-event sets and asynchronous configurations are classical concurrency/order theory.  No generic novelty claim is made. P025 contributes the exact task ladder and the fairness/liveness scope warning.
