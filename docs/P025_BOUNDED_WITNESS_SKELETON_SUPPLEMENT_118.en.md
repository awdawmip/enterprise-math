# P025 Supplement 118 — Bounded-Arity Witness Skeleton

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-poset-observable-stage113`  
Depends on: P025 Supplement 117; canonical A4 witness-spectrum boundary  
Hard block: `NONE`

## 1. Full joint-MAY can still be overprecise

Supplement 117 shows that all existential joint-MAY queries are encoded by the joint-MAY complex

\[
\mathcal K_{\mathcal F}
\]

or, equivalently, by its maximal faces.

But a declared future language may ask joint witnesses only up to some bounded arity

\[
1\le k\le |P|.
\]

Then retaining full high-arity witness faces is unnecessary.

## 2. P025-D43 — truncated witness complex

Define the arity-\(k\) truncation

\[
\boxed{
\mathcal K_{\mathcal F}^{(\le k)}
:=
\{S\in\mathcal K_{\mathcal F}:|S|\le k\}.
}
\]

For the declared future consisting of all joint-MAY queries with at most \(k\) labels,

\[
S\text{ jointly MAY?},
\qquad |S|\le k,
\]

this truncated complex is the exact semantic signature.

## 3. P025-T263 — maximal truncated faces are exact generators

Let

\[
\boxed{
H_k
:=
\operatorname{Max}_{\subseteq}
\mathcal K_{\mathcal F}^{(\le k)}.
}
\]

Then

\[
\boxed{
\mathcal K_{\mathcal F}^{(\le k)}
=
\bigcup_{F\in H_k}2^F.
}
\]

Thus \(H_k\) is an exact finite generator for every joint-MAY query of arity at most \(k\).

## 4. Exact arity ladder

The construction interpolates continuously between pointwise support and the full joint complex.

### `k=1`

\[
H_1
\]

is just the collection of singleton MAY labels, equivalent to the ordinary MAY support \(U\).

### `k=2`

\[
H_2
\]

is the maximal edge/vertex data of the pairwise co-activation graph. It can distinguish states with identical pointwise support but different pairwise coexistence.

### general `k`

\[
H_k
\]

is a bounded-rank witness hypergraph/simplicial skeleton.

### full arity

For

\[
k=|P|,
\]

we recover

\[
\boxed{
H_{|P|}=\operatorname{Max}_{\subseteq}(\mathcal F).
}
\]

## 5. Strict arity separation

On the three-element antichain \(\{a,b,c\}\), let

\[
\mathcal F
=
\{\{a,b\},\{a,c\},\{b,c\}\}.
\]

Every singleton is MAY and every pair is jointly MAY. Therefore the entire `k=2` future reports no missing pair.

But

\[
\{a,b,c\}
\]

is not jointly MAY. Hence the `k=3` language is strictly finer than the `k=2` language.

So there is no general collapse from pairwise witness information to arbitrary joint witness information.

## 6. Worst-case state count boundary

If the ambient poset is an \(n\)-element antichain, every subset is an ideal and arbitrary simplicial witness complexes can occur. Therefore the number of maximal truncated faces can attain the standard Sperner-layer scale

\[
\boxed{
\binom{n}{\min(k,\lfloor n/2\rfloor)}
}
\]

in the worst case.

This is prior combinatorics, not a new P025 theorem. Its architectural meaning is that bounded witness arity is a real precision resource: increasing \(k\) can sharply increase the required correlation state even while the underlying label universe is unchanged.

## 7. Relation to A4

A4 already owns generic witness spectra and multivalued correspondence. Stage 118 should be treated as a specialization / pressure test:

\[
\boxed{
\text{declared witness arity}
\Longrightarrow
\text{required hypergraph skeleton depth}.
}
\]

It gives an exact example where future-language complexity changes the **arity of relation state** rather than merely refining a scalar observation.

## 8. Prior-art discipline

Simplicial complexes, hypergraph skeletons, maximal faces and Sperner bounds are classical. No generic novelty claim is made.

The project-side result is the exact future-relative witness-arity compiler inside the P025/A4 pressure test. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/poset_bounded_witness_skeleton.py`;
- `tests/test_poset_bounded_witness_skeleton.py`.

The executable layer verifies the `k=1` MAY-support reduction, pairwise correlation, full-arity recovery, maximal-face regeneration, and a strict `k=2` versus `k=3` separation.

## 10. Next frontier

The next question is whether the poset order itself reduces witness arity. A required label set \(S\) and its down-closure \(\downarrow S\) have the same joint-MAY truth against ideal states. Therefore many labels dominated by others are semantically redundant. The correct local joint-query complexity may be controlled by the antichain width of the required set rather than raw arity \(|S|\). Stage 119 should derive that antichain reduction exactly.
