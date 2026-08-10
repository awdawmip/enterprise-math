# P025 Supplement 119 — Antichain Normal Form for Joint Queries

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplements 113–118  
Hard block: `NONE`

## 1. Raw query arity is not semantic arity

Supplement 118 measures bounded joint-MAY futures by raw set size \(|S|\). But ideal semantics contains order redundancy: if one required label lies below another, requiring both is no stronger than requiring the larger one.

Stage 119 quotients the **query language itself** before asking how much state precision is needed.

## 2. P025-D44 — maximal-antichain query normal form

For a finite required label set

\[
S\subseteq P,
\]

define

\[
\boxed{
\alpha(S):=\operatorname{Max}_P(S).
}
\]

Because every exact state \(I\) is an order ideal,

\[
\boxed{
S\subseteq I
\iff
\downarrow S\subseteq I
\iff
\alpha(S)\subseteq I.
}
\]

Thus every joint membership query is semantically equivalent to the antichain of its maximal required labels.

## 3. P025-T264 — exact operation quotient

For joint MAY or joint MUST membership semantics, two raw required sets are operation-equivalent iff

\[
\boxed{
S\sim T
\iff
\alpha(S)=\alpha(T).
}
\]

Equivalently,

\[
\downarrow S=\downarrow T.
\]

So the coarsest natural query representation is not a raw subset or raw list of labels. It is a labelled antichain normal form.

This is a direct operation-language quotient: the exact state representation need not change.

## 4. P025-D45 — essential arity

Define the semantic or essential arity

\[
\boxed{
e(S):=|\alpha(S)|.}
\]

Then

\[
\boxed{
e(S)\le\operatorname{width}(P).}
\]

If a declared future allows raw queries of size at most \(k\), the worst-case essential arity is exactly

\[
\boxed{
\min\{k,\operatorname{width}(P)\}.
}
\]

The upper bound follows because \(\alpha(S)\) is an antichain and \(|\alpha(S)|\le|S|\). Tightness follows by choosing an antichain of size \(\min(k,w(P))\).

## 5. Exact extremes

### Chain

If \(P\) is a chain, every nonempty joint query collapses to its single largest label:

\[
\boxed{e(S)=1.}
\]

Arbitrarily long raw conjunctions therefore have one-label semantic arity.

### Antichain

If \(P\) itself is an antichain, then

\[
\alpha(S)=S
\]

and no arity compression occurs.

These are the two extremal geometries.

## 6. Query-class count

Among raw queries of size at most \(k\), the semantic equivalence classes are in bijection with antichains of \(P\) of size at most \(k\).

Hence the operation-language state count is

\[
\boxed{
N_{\rm query}(k)
=
\#\{A\subseteq P:A\text{ antichain},\ |A|\le k\}.
}
\]

This can be much smaller than

\[
\sum_{j=0}^{k}\binom{|P|}{j}.
\]

For a chain it is only \(1+|P|\) for every \(k\ge1\); for an antichain there is no reduction.

## 7. Relation to Stage 106

Stage 106 showed that enriching future semantics can refine the **operation quotient** without refining the state quotient.

Stage 119 gives a complementary direction: before refining state at all, relation geometry can make the raw operation language itself overprecise. Comparable required labels collapse under the ideal law.

Thus future precision has at least two independent reductions:

\[
\boxed{
\text{state quotient}
\quad\text{and}\quad
\text{operation/query quotient}.
}
\]

Neither should be inferred from raw syntax alone.

## 8. Relation to A4

A4 owns witness/correspondence semantics. Stage 119 does not replace A4 witness spectra. It says that when witnesses are ideals of a declared poset, joint-query syntax should first be normalized to an antichain before querying any MAY/MUST support object.

This can reduce the effective witness arity seen by A4 from \(k\) to at most \(\min(k,w(P))\).

## 9. Prior-art discipline

Down-closures, maximal antichains and redundancy of dominated constraints are classical poset facts. No generic novelty claim is made.

The project-side result is the exact operation-language precision reading and its integration with the P025/A2/A4 future-quotient hierarchy. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 10. Executable assets

Added:

- `src/enterprise_math/poset_joint_query_normal.py`;
- `tests/test_poset_joint_query_normal.py`.

The executable layer verifies chain collapse, antichain non-collapse, exact future equivalence of dominated raw queries, ideal-membership reconstruction, and the worst-case essential-arity law.

## 11. Next frontier

The next step is to combine Stage 118 and Stage 119: bounded raw arity \(k\) should really induce a witness skeleton indexed by antichain query classes, not arbitrary subsets. The relevant precision resource should depend jointly on query cap \(k\), poset width, and the realized antichain spectrum of the admissible family.
