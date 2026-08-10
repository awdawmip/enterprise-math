# P025 Supplement 102 — Exact Second-Order Closure for Finite Action Histories

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-history-closure-stage101`  
Depends on: P025 Supplement 101  
Hard block: `NONE`

## 1. From failure to closure

Stage 101 proves that a one-step response signature is not automatically closed under two-step histories. The missing information is structured: mixed threshold/node histories need a corner bit, while repeated node histories need later node ranks.

Stage 102 asks whether this repair hierarchy continues indefinitely.

For finite threshold/node extension envelopes, it does **not**. The scalar activation-area future closes exactly at interaction order two.

## 2. Finite extension envelope

Let the current state consist of ordered thresholds

\[
T_1<\cdots<T_s
\]

and a nondecreasing orbit prefix

\[
\rho_0\le\cdots\le\rho_h.
\]

Let candidate new threshold rows be

\[
U_1<\cdots<U_a
\]

and let a precomputed future node prefix be

\[
v_1\le\cdots\le v_b,
\qquad v_1\ge\rho_h.
\]

An executable history may insert any subset of candidate thresholds in any order and append a prefix `v_1,...,v_t` of the future nodes.

Define the current area

\[
A:=\#\{(k,j):\rho_j\ge T_k\}.
\]

For each candidate threshold define its old-block span

\[
L_i:=\#\{0\le j\le h:\rho_j\ge U_i\}.
\]

For each future node define its old-threshold rank

\[
R_j:=\#\{1\le k\le s:v_j\ge T_k\}.
\]

Finally define the prospective mixed corner block

\[
\boxed{C_{ij}:=\mathbf1_{\{v_j\ge U_i\}}.}
\]

## 3. P025-T231 — exact finite-history area formula

For any selected threshold subset `I subset {1,...,a}` and any future prefix length `0<=t<=b`, the final activation area is

\[
\boxed{
A(I,t)
=
A
+\sum_{i\in I}L_i
+\sum_{j=1}^{t}R_j
+\sum_{i\in I}\sum_{j=1}^{t}C_{ij}.
}
\]

### Proof

The final activation cells split into four disjoint blocks:

1. old thresholds x old nodes — contributes `A`;
2. selected new thresholds x old nodes — contributes `sum L_i`;
3. old thresholds x new node prefix — contributes `sum R_j`;
4. selected new thresholds x new node prefix — contributes `sum C_ij`.

These blocks are disjoint and exhaust the final matrix. No correction term remains.

Therefore the formula is exact for every allowed history and is independent of the interleaving order used to reach the final row set and node prefix.

## 4. P025-D45 — second-order history signature

Define

\[
\boxed{
\Sigma^{(2)}
=
\left(
A;
(L_i)_{i=1}^{a};
(R_j)_{j=1}^{b};
(C_{ij})_{1\le i\le a,1\le j\le b}
\right).
}
\]

P025-T231 shows that `Sigma^(2)` is sufficient for **every finite area history inside the declared extension envelope**.

Thus Stage 101's pairwise repairs do not proliferate to an unbounded tower.

## 5. P025-T232 — the response coordinates are recoverable

The signature is not merely a convenient sufficient cache. Its coordinates can be read back from the future response language.

For a threshold row `U_i`,

\[
\boxed{L_i=A(\{i\},0)-A.}
\]

For the `j`-th future node increment,

\[
\boxed{R_j=A(\varnothing,j)-A(\varnothing,j-1).}
\]

For the mixed corner,

\[
\boxed{
C_{ij}
=
\big(A(\{i\},j)-A(\{i\},j-1)\big)
-
\big(A(\varnothing,j)-A(\varnothing,j-1)\big).
}
\]

Hence the declared history-area responses determine every coordinate of `Sigma^(2)`.

At the level of this future language, `Sigma^(2)` is therefore an exact response coordinate system, not hidden surplus structure.

## 6. P025-T233 — degree-two multilinear envelope

Introduce independent Boolean row/column selection variables

\[
x_i,y_j\in\{0,1\}.
\]

The algebraic extension of the area response is

\[
\boxed{
A(x,y)
=
A
+\sum_iL_ix_i
+\sum_jR_jy_j
+\sum_{i,j}C_{ij}x_iy_j.
}
\]

This polynomial has degree at most two.

Therefore every irreducible Boolean interaction coefficient of order three or higher is identically zero.

Physical node histories are the prefix-restricted subfamily of this algebraic envelope, so the same second-order data suffice there as well.

## 7. What Stage102 does and does not say

It **does** say:

\[
\boxed{
\text{finite row/column area history}
\Longrightarrow
\text{exact second-order closure}.
}
\]

It does **not** say that every dynamical system has second-order history closure. The result depends on the incidence-area observable being an additive count of cells created by row and column extension.

It also does not claim that the raw `a x b` corner matrix is already the minimal storage representation. Monotonicity imposes additional structure on that block; Stage 103 will compress it.

## 8. Arithmetic realization

The executable tests instantiate the theorem with the `(q,p)=(3,41)` dyadic pressure orbit, using an old orbit prefix and later exact dyadic nodes as the future prefix. Exhaustive enumeration over every candidate-threshold subset and every physically valid future-node prefix agrees with the second-order formula.

This keeps the architecture theorem generic while retaining a concrete P025 arithmetic pressure test.

## 9. Architectural consequence

Stage 102 gives a sharp hierarchy:

- one-step language -> first-order response coordinates;
- two-step counterexample -> mixed interaction is genuinely necessary;
- full finite extension-history language -> first + second order is sufficient;
- no third-order repair is required for this observable.

This is a much stronger notion than storing the whole action history. The correct state is a finite response jet whose required order is fixed by the observable's extension algebra.

## 10. Prior-art / novelty boundary

Bilinear incidence counts, Boolean multilinear polynomials, finite differences and interaction decompositions are classical/general ideas. P025 claims none individually.

The project-side contribution is the exact pressure-test route from one-step quotient failure to a proved finite-history closure order, with arithmetic counterexamples and executable recovery formulas. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_finite_history_closure.py`;
- `tests/test_abc_finite_history_closure.py`.

## 12. Next frontier

The mixed corner block `C` is not arbitrary. Because candidate thresholds increase and future node values increase, it is itself a Ferrers matrix. Stage 103 will compress the `a*b` raw bits into a monotone boundary and quantify the exact interaction-state count.