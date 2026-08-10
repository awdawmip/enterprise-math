# P025 Supplement 94 — Biaxial Local Updates and Representation Tradeoff

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 92–93  
Hard block: `NONE`

## 1. Equivalent coordinates need not have equivalent update cost

Stage 93 gives three exact representations of the same finite activation state:

1. threshold-centric crossing depths `(j_k)`;
2. orbit-centric node ranks `(r_j)`;
3. a monotone `H/V` Ferrers boundary word.

Because they are bijectively equivalent, they contain the same semantic information. But a precision system does not only read states; it also extends the threshold grid and the orbit horizon.

Stage 94 studies the exact mutation cost of those two extension directions.

## 2. P025-T220 — adding one threshold is local in crossing coordinates

Fix an existing threshold grid and insert one new threshold `T` at its ordered position.

Its first crossing depth is one new scalar

\[
\boxed{j_T\in\{0,\ldots,h,\infty\}.}
\]

All old thresholds retain exactly their old crossing depths. Therefore the crossing representation changes only by inserting the one new coordinate `j_T`.

In dense-coordinate write count:

\[
\boxed{W_{\rm cross}^{(T)}=1.}
\]

## 3. P025-T221 — the same threshold may rewrite a suffix of ranks

For every existing orbit node `j`, the new threshold increases `r_j` by one exactly when

\[
\rho_j\ge T.
\]

If `j_T` is finite, this occurs for the suffix

\[
j_T,j_T+1,\ldots,h.
\]

Hence the exact number of changed old rank coordinates is

\[
\boxed{
W_{\rm rank}^{(T)}
=
\begin{cases}
h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}}
\]

Thus a threshold extension can be globally distributed in the rank representation even though it is one-coordinate-local in the crossing representation.

## 4. P025-T222 — adding one orbit node is local in rank coordinates

Extend the dyadic horizon by one new node `h+1`.

All old node ranks are unchanged. The rank representation simply appends

\[
\boxed{r_{h+1}.}
\]

Therefore

\[
\boxed{W_{\rm rank}^{(j)}=1.}
\]

for every one-node orbit extension.

## 5. P025-T223 — the same orbit node may resolve many infinite crossings

Every threshold already reached before the extension keeps its finite crossing depth.

A threshold previously recorded as

\[
j_k=\infty
\]

changes exactly when the new node first reaches it, in which case

\[
\boxed{j_k=h+1.}
\]

If the old final rank is `r_h` and the new rank is `r_{h+1}`, then precisely

\[
\boxed{r_{h+1}-r_h}
\]

previously infinite crossing coordinates become finite.

Therefore

\[
\boxed{W_{\rm cross}^{(j)}=r_{h+1}-r_h.}
\]

This quantity may be zero, one, or many.

## 6. P025-T224 — Ferrers boundary update is one-symbol local on both axes

The boundary word contains one `V` step per threshold and one `H` step per orbit node.

Adding one threshold changes the boundary by inserting exactly one additional

\[
\boxed{V}
\]

step at its crossing location. Deleting that new `V` recovers the previous boundary word exactly.

Adding one orbit node changes the boundary by inserting exactly one additional

\[
\boxed{H}
\]

step at its rank location. Deleting that new `H` recovers the previous boundary word exactly.

Hence:

\[
\boxed{
\text{threshold extension}=\text{one V insertion},
\qquad
\text{orbit extension}=\text{one H insertion}.
}
\]

The Ferrers boundary is therefore a biaxially local update representation.

## 7. Exact threshold-extension fixture

Start from the Stage-93 state

\[
(j_k)=(0,1,2,\infty),
\qquad
(r_j)=(1,2,3,3),
\]

with boundary word

\[
\texttt{VHVHVHHV}.
\]

Insert threshold

\[
T=10.
\]

For the same arithmetic orbit, it crosses at depth two. The new state is

\[
\boxed{(j_k')=(0,1,2,2,\infty),}
\]

and

\[
\boxed{(r_j')=(1,2,4,4).}
\]

Thus:

- crossing coordinate writes: `1`;
- rank coordinate rewrites: `2`;
- boundary update:
  \[
  \boxed{
  \texttt{VHVHVHHV}
  \to
  \texttt{VHVHVVHHV},
  }
  \]
  exactly one inserted `V`.

## 8. A threshold can rewrite every old rank

On the same four-node orbit, begin with thresholds

\[
\frac12,1,11
\]

and insert

\[
T=\frac1{100}.
\]

The new threshold is already reached at depth zero, so every existing node rank increases.

Hence

\[
\boxed{W_{\rm cross}^{(T)}=1,\qquad W_{\rm rank}^{(T)}=4.}
\]

This shows that the update-cost gap can scale with the orbit horizon.

## 9. Exact orbit-extension fixture

Take

\[
(q,p,m)=(7,17,2).
\]

At exponent two,

\[
\rho_{2,-}=\frac16.
\]

At exponent four, Stage 86 gives

\[
\rho_{4,-}=\frac{13}{6}.
\]

Start at horizon zero with thresholds

\[
\frac12,1,2.
\]

None is initially reached:

\[
(j_k)=(\infty,\infty,\infty),
\qquad
(r_0)=(0).
\]

Appending the exponent-four node reaches all three thresholds at once:

\[
\boxed{(j_k')=(1,1,1),}
\]

and

\[
\boxed{(r_j')=(0,3).}
\]

Thus:

- crossing rewrites: `3`;
- rank writes: `1`;
- boundary word:
  \[
  \boxed{
  \texttt{HVVV}
  \to
  \texttt{HVVVH},
  }
  \]
  exactly one inserted `H`.

This is the exact mirror of the threshold-extension fixture.

## 10. P025-C32 — no crossing/rank coordinate globally dominates updates

Threshold extensions favor crossing coordinates:

\[
W_{\rm cross}^{(T)}=1
\]

while rank rewrites may scale with `h`.

Orbit extensions favor rank coordinates:

\[
W_{\rm rank}^{(j)}=1
\]

while crossing rewrites may scale with `s`.

Therefore neither dual coordinate is globally update-optimal across both extension axes.

This is a negative boundary against choosing one coordinate merely because it is semantically complete.

## 11. Boundary word trades storage for symmetric locality

The three representations have different shapes:

- crossing vector length: `s`;
- rank vector length: `h+1`;
- boundary word length: `s+h+1` symbols.

So the Ferrers path is not automatically the smallest storage representation.

Its advantage is different:

\[
\boxed{
\text{both extension axes become one-symbol local edits}.
}
\]

Thus representation choice lies on a storage/update-locality tradeoff rather than a single total order.

## 12. P025-D39 — axis-relative coordinate policy

For a workload dominated by threshold-grid refinement, crossing coordinates are naturally local.

For a workload dominated by orbit-horizon extension, node ranks are naturally local.

For a workload requiring balanced mutation on both axes, the boundary word offers symmetric one-symbol updates.

This yields the representation policy

\[
\boxed{
\text{choose coordinates relative to the future extension language,}
}
\]

not by a globally fixed representation hierarchy.

## 13. Relation to Stage 90

Stage 90 shows that the future query determines which observables and observation order are sufficient.

Stage 94 adds a second dimension:

> once a sufficient semantic state is chosen, the expected **future extension direction** determines which equivalent coordinate representation is operationally local.

So future-relative precision has at least two layers:

1. which semantic quotient is needed;
2. which coordinate chart best supports the expected future operations on that quotient.

## 14. Prior-art / novelty discipline

Sparse updates, dual coordinates, lattice-path insertion and storage/update tradeoffs are broad prior concepts.

P025 claims none of those notions in isolation.

The project-side result is the exact arithmetic Ferrers-state update law and its concrete use as a pressure test for coordinate-choice semantics. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 15. Executable assets

Added:

- `src/enterprise_math/abc_dyadic_boundary_update.py`;
- `tests/test_abc_dyadic_boundary_update.py`.

The executable layer verifies exact threshold/rank write counts, one-symbol `V/H` insertion, distributed threshold updates, multi-threshold orbit crossings and the symmetric path-update law.

## 16. Next frontier

No hard block exists. Continue with:

1. prove the threshold/orbit extension diamond commutes;
2. show the final boundary is independent of extension order;
3. formulate the three representations as a Pareto family rather than one preferred state;
4. derive a mixed-workload cost model without hard-coding arbitrary costs;
5. then relay the semantic-state/coordinate-chart distinction back to P023/A2.
