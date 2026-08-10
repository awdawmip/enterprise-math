# P025 Supplement 134 — Exact storage/depth endpoints for chain implication laws

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Chain closure

Fix labels

\[
x_0,x_1,\ldots,x_n
\]

with semantic closure law

\[
x_0\Rightarrow x_1\Rightarrow\cdots\Rightarrow x_n.
\]

Equivalently,

\[
cl(\{x_i\})=\{x_i,x_{i+1},\ldots,x_n\}.
\]

The exact closed states are the empty state and all suffixes.

## 2. Minimum-rule lower bound

Any sound complete single-head implication basis requires at least

\[
\boxed{n}
\]

rules.

Indeed, for every `j=1,...,n`, seed `{x_{j-1}}` must eventually acquire the missing label `x_j`. Since only a rule whose head/root is `x_j` can add that label, at least one distinct rule rooted at each `x_j` is necessary.

The adjacent basis

\[
x_{j-1}\Rightarrow x_j,
\qquad 1\le j\le n,
\]

has exactly `n` rules, so the bound is sharp.

## 3. Uniqueness of the minimum-rule basis

Suppose a complete basis has exactly `n` rules. Then it has exactly one rule rooted at each `x_j`, `j>=1`.

We show by descending induction that this unique rule must be

\[
\boxed{x_{j-1}\Rightarrow x_j.}
\]

For `j=n`, start from seed `{x_{n-1}}`. Before `x_n` appears there is no other later label available. The unique rule rooted at `x_n` must therefore have premise contained in `{x_{n-1}}`. The empty premise is unsound because `x_n` is not mandatory, so its premise is exactly `{x_{n-1}}`.

Assume the statement has been proved for roots `x_{j+1},...,x_n`. Their unique rules form the adjacent tail and cannot fire from seed `{x_{j-1}}` before `x_j` appears. Hence, before `x_j` is first generated, the only available label remains `x_{j-1}`. The unique rule rooted at `x_j` must again be exactly `{x_{j-1}} -> x_j`.

Thus the adjacent/Hasse basis is the **unique minimum-rule single-head basis**.

## 4. Forced derivation depth at minimum storage

From seed `{x_0}`, the unique minimum basis adds precisely one new chain level per parallel round. Therefore

\[
\boxed{d_{\min\text{-storage}}=n.}
\]

Minimum rule count and minimum derivation depth are not simultaneously attainable on this family.

## 5. One-round endpoint

By Stage 133, every one-round complete basis must contain every rooted circuit. For this chain, every pair `i<j` gives circuit

\[
x_i\Rightarrow x_j.
\]

Therefore the unique inclusion-minimal one-round representation has

\[
\boxed{\binom{n+1}{2}}
\]

rules and depth one.

Hence the two exact resource endpoints are

\[
\boxed{
(\#\text{rules},d)
=
(n,n)
\quad\text{and}\quad
\left(\binom{n+1}{2},1\right).
}
\]

For `n=3`, Stage 131 also supplies the intermediate complete point `(4,2)` between `(3,3)` and `(6,1)`.

## 6. Unbounded separation

As `n` grows,

\[
\frac{\binom{n+1}{2}}{n}=\frac{n+1}{2}
\]

and the minimum-storage basis has depth `n` instead of one.

Thus both the storage overhead required for direct closure and the computation depth required for minimum storage can grow without bound.

## 7. Architectural consequence

Even after semantic closure and rule formalism are fixed, relation-law precision still has a genuine storage/execution frontier.  A compact law representation may be semantically exact but computationally deeper; a direct representation may be computationally shallow but much larger.

This is not state precision and not query-generator precision.  It is a separate **law-representation/runtime** resource pair.

## 8. Prior-art boundary

Transitive closure/reduction of chains and shortcut-depth tradeoffs are classical. The project makes no generic novelty claim. The exact family is used only to prove that no single scalar `relation precision` can represent both stored law size and allowed future derivation depth.
