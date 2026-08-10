# P025 Supplement 151 — The labelled enabled-action frontier is an exact runtime state

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Setup

Let `P_gate` be the helper dependency poset and let

\[
I\in J(P_{gate})
\]

be a legal asynchronous completed-helper ideal.

Define the labelled enabled-action frontier

\[
\operatorname{En}(I)
=
\{h\notin I:\operatorname{Pred}(h)\subseteq I\}.
\]

Stage 146 showed that equal ideal cardinality can have different enabled frontiers.  The stronger result is that the complete labelled enabled frontier determines the ideal exactly.

## 2. Enabled frontier is the minimal complement antichain

Because `I` is an ideal, its complement

\[
U=P_{gate}\setminus I
\]

is an upset.  A helper `h` is enabled exactly when it lies in `U` and has no predecessor still in `U`. Therefore

\[
\boxed{
\operatorname{En}(I)=\operatorname{Min}(U).
}
\]

The enabled action set is automatically an antichain.

## 3. Exact reconstruction

Every finite upset is generated upward by its minimal elements:

\[
U=\uparrow\operatorname{Min}(U).
\]

Hence

\[
\boxed{
I
=
P_{gate}\setminus\uparrow\operatorname{En}(I).
}
\]

Therefore

\[
\boxed{
\operatorname{En}(I)=\operatorname{En}(J)
\iff
I=J.
}
\]

The labelled enabledness signature is injective and preserves the entire exact runtime progress state.

The terminal ideal has empty enabled frontier; it is uniquely reconstructed as the full ideal.

## 4. Dual boundary charts

Every ideal therefore has two exact antichain charts:

1. **completed boundary** — maximal completed helpers `Max(I)`;
2. **enabled boundary** — minimal incomplete helpers `Min(P_gate\I)`.

They are dual descriptions of the same runtime state.

The maximum possible size of either boundary is controlled by

\[
\boxed{\operatorname{width}(P_{gate}).}
\]

For the balanced `k=2^d` compiler this width is `k/2`.

## 5. Sharpening Stage 146

Stage 146's task ladder can now be sharpened.  For all labelled helper actions visible,

\[
\boxed{
\text{enabled-action quotient}
=
\text{exact progress quotient}.
}
\]

Thus the state-class ladder is

\[
\boxed{
1
\quad\to\quad
m+1
\quad\to\quad
|J(P_{gate})|,
}
\]

for endpoint, remaining-work rank, and full labelled action-legality/exact progress respectively.

The third step still has two distinct coordinate charts: completed ideal/antichain and enabled frontier.

## 6. Connection to legality-sensitive future quotients

This is a concrete specialization of the existing P023/Foundation rule that action enabledness is future-observable structure.  Here the complete vector of current labelled enabledness already separates every legal runtime state; no deeper action-word refinement is needed for exact state identity.

This strength depends on observing **all helper action labels**. Stage 152 should study partial action visibility.

## 7. Prior-art boundary

Ideals, upset minimal boundaries and enabled-event frontiers are classical order/event-structure theory. No generic novelty claim is made. P025 provides the exact specialization and the correction of Stage146's previously unresolved intermediate quotient.
