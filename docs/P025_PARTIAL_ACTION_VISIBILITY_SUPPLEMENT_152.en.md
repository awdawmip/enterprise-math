# P025 Supplement 152 — Partial action visibility requires dependency-closed support

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Partial action language

Let `P_gate` be the helper dependency poset, let

\[
I\in J(P_{gate})
\]

be the exact completed-helper state, and expose only a subset of labelled helper actions

\[
Q\subseteq P_{gate}.
\]

The visible current legality signature is

\[
E_Q(I)=\operatorname{En}_{P_{gate}}(I)\cap Q.
\]

We ask when this signature is a clean observable of the projected visible progress

\[
I_Q=I\cap Q.
\]

## 2. Predecessor-closed sufficient condition

Assume `Q` is an order ideal of `P_gate`: every helper ancestor of a visible helper is also visible.

Then `I_Q` is an ideal of the induced poset on `Q`, and for every visible helper `q`, all of its prerequisites are also visible. Therefore global enabledness of `q` depends only on `I_Q`.

More precisely,

\[
\boxed{
\operatorname{En}_{P_{gate}}(I)\cap Q
=
\operatorname{En}_{Q}(I\cap Q).
}
\]

By Stage 151 applied inside the induced poset `Q`, the right-hand side reconstructs `I\cap Q` exactly. Hence

\[
\boxed{
Q\text{ predecessor-closed}
\Longrightarrow
E_Q\text{ is an exact coordinate of projected progress }I\cap Q.
}
\]

Hidden helpers outside `Q` cannot affect visible action legality.

## 3. Nonclosed action sets can leak hidden dependency state

If `Q` omits helper predecessors, the clean factorization can fail.

In the balanced eight-way compiler, `h5` depends on hidden helpers `h1,h2`. Let

\[
Q=\{h_5\}.
\]

Consider two legal ideals with the same visible projection `empty`:

- no helper completed: `h5` is disabled;
- `h1,h2` completed: `h5` is enabled.

Thus

\[
\boxed{
I\cap Q=J\cap Q
\quad\not\Rightarrow\quad
E_Q(I)=E_Q(J).
}
\]

Visible action legality can reveal hidden predecessor progress not represented in the visible projected state.

## 4. Enabledness can also fail to recover visible progress

The reverse direction can fail too.  With the same `Q={h5}`:

- before hidden predecessors complete, `h5` is disabled and absent;
- after `h5` itself has completed, `h5` is again disabled.

The visible enabled signature is empty in both cases, while the visible progress projections differ (`empty` versus `{h5}`). Hence

\[
\boxed{
E_Q(I)=E_Q(J)
\quad\not\Rightarrow\quad
I\cap Q=J\cap Q.
}
\]

So an arbitrary partial action set does not automatically define a self-contained state subsystem.

## 5. Operation-support closure principle

A robust way to expose a helper action family is therefore to close it under dependency before treating it as an autonomous future language:

\[
Q\leadsto\downarrow Q.
\]

On a predecessor-closed support, current labelled enabledness and projected progress match exactly.  Without closure, one must either retain additional hidden-state information or accept a different/coarser semantics.

This is an operation-language analogue of earlier state-support closure results.

## 6. Architectural consequence

The resources now include not only which actions are declared, but also the **relation support required to interpret those actions**.

A small syntactic action language can have a larger semantic dependency footprint.  Thus

\[
\boxed{
\text{raw action count}
\neq
\text{semantic operation-support size}.
}
\]

## 7. Prior-art boundary

Dependency closure, projected transition systems and hidden-predecessor effects are classical systems/order theory. No generic novelty claim is made. P025 contributes the exact finite action-visibility boundary and its future-precision interpretation.
