# P025 Supplement 154 — Syntactic action count and semantic dependency support can separate linearly

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-fairness-stage147`

## 1. Operation-support closure

Stage 153 identified predecessor/downward closure as the natural support for an autonomous helper-action subsystem. For a declared action set

\[
Q\subseteq P_{gate},
\]

define its semantic dependency support

\[
\boxed{
D(Q)=\downarrow Q.
}
\]

The raw number of syntactically listed actions is `|Q|`; the support needed to interpret them autonomously is `|D(Q)|`.

## 2. Maximal actions generate the same support

Let `Max(Q)` denote the maximal elements of `Q` under the helper dependency order. Every nonmaximal action lies below some maximal action, so

\[
\boxed{
\downarrow Q
=
\downarrow\operatorname{Max}(Q).
}
\]

Thus the dependency footprint has an exact antichain generator boundary. Listing ancestor actions explicitly does not enlarge the support already forced by a later action.

This is an operation-language analogue of ideal boundary compression.

## 3. One action can force a large support

Consider the perfect balanced compiler with

\[
k=2^d
\]

raw antecedents.  Choose one of the two highest pre-output helper gates. Its dependency subtree contains `k/2` raw leaves and therefore

\[
\boxed{\frac{k}{2}-1}
\]

helper gates including itself.

Hence a syntactic action language containing only this one helper has

\[
\boxed{
|Q|=1,
\qquad
|D(Q)|=\frac{k}{2}-1.
}
\]

Exact values are

\[
1,3,7,15
\]

for `k=4,8,16,32`.

The semantic support blowup is therefore linear in the raw problem size even though the action count remains one.

## 4. Exact eight-way fixture

In the eight-way compiler, upper helper `h5` depends on first-layer helpers `h1,h2`. Thus

\[
D(\{h_5\})=\{h_1,h_2,h_5\}.
\]

Moreover

\[
D(\{h_1,h_2,h_5\})
=
D(\{h_5\}).
\]

So the raw action list with three labels compresses to one maximal support generator, while the autonomous semantic support contains three helper states/actions.

## 5. Three operation-language resources

The action language therefore carries at least three distinct size notions:

1. **raw action count** `|Q|`;
2. **support-generator count** `|Max(Q)|`;
3. **dependency-support size** `|down(Q)|`.

None should be silently called `operation precision` without qualification.

## 6. Relation to state precision

A small declared action family can require a large state/relation footprint to make its legality and transitions self-contained.  Conversely, a large syntactic action list can contain many support-redundant ancestor actions.

Thus future-language complexity and required state support are coupled but not equal.

## 7. Prior-art boundary

Transitive dependency closure and maximal-generator antichains are classical order theory. No generic novelty claim is made. P025 contributes the exact perfect-compiler family and its operation/state precision interpretation.
