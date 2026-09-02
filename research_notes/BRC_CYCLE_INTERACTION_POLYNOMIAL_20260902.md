# BRC determinant cycle-interaction polynomial: finite exclusion certificate versus infinite loop closure

Status: `RESEARCH CANDIDATE / EXACT FINITE POLYNOMIAL DUAL OF LOOP-ZETA`
Date: `2026-09-02`
Research mode: `TASK_RESEARCH continuation`
Foundation baseline: `main@3a6bb471a10fd8673483ea5163687ce850bba9bb`
Parent research: recurrent logdet, loop response, prime-valuation holonomy, parity/thickness

## 0. Setup

Let `G=(V,E)` be a finite directed multigraph with one formal variable `x_e` for every explicit branch edge. Define the branch-resolved total-mass matrix

\[
W(x)_{ij}=\sum_{e:i\to j}x_e.
\]

Define the finite determinant polynomial

\[
\boxed{P_G(x):=\det(I-W(x)).}
\]

For a stable positive rational specialization `x_e=q_e`, the preceding research gives

\[
Z_{\rm loop}(q)=P_G(q)^{-1},
\qquad
\Gamma(q)=-\ln P_G(q).
\]

The determinant/cycle-system expansion and graph-zeta inverse are classical. No generic novelty claim is made. The project-specific objective is to make the finite/infinite BRC roles and their exact response consequences explicit.

## 1. Explicit-edge cycle-system expansion

A **cycle system** `F` is a finite set of pairwise vertex-disjoint directed simple cycles, with each transition choosing one explicit branch edge. The empty system is allowed.

Write

\[
w(F)=\prod_{e\in F}x_e,
\qquad
c(F)=\text{number of directed cycles in }F.
\]

Then the Leibniz determinant expansion gives

\[
\boxed{
P_G(x)
=\sum_F(-1)^{c(F)}w(F).
}
\]

Proof sketch: choose from each diagonal entry either the identity `1` or a self-loop term `-x_e`, and from each non-diagonal selected permutation edge a term `-x_e`. The moved vertices form the cycle decomposition of a partial permutation. A permutation cycle contributes one overall minus sign, so a collection of `c` disjoint cycles contributes `(-1)^c`.

This is the standard determinant cycle-system formula.

Candidate typed name:

`BRC_DETERMINANT_EXPLICIT_CYCLE_SYSTEM_EXPANSION`.

## 2. Multiaffinity and coefficient rigidity

Because the cycle systems are vertex-disjoint and every directed simple cycle uses each explicit edge at most once, every variable `x_e` appears with exponent at most one.

Thus

\[
\boxed{P_G\text{ is multiaffine in the explicit branch variables}.}
\]

Moreover an explicit selected edge set that satisfies the cycle-system condition has a unique cycle decomposition. Hence no two distinct cycle systems produce the same explicit-edge monomial.

Therefore every nonzero coefficient of the **fully branch-resolved** polynomial is exactly

\[
\boxed{+1\text{ or }-1.}
\]

After tree-gauge substitution or aggregation of branch variables, distinct monomials may collapse and integer coefficients of larger magnitude may appear. The `±1` statement belongs to the explicit-edge polynomial only.

## 3. Formal acyclic criterion

If the support graph has no directed cycle, the only cycle system is empty, so

\[
P_G(x)=1.
\]

Conversely, if a directed cycle `C` exists, its explicit edge monomial occurs with coefficient `-1` and cannot cancel with another explicit cycle system.

Hence

\[
\boxed{
P_G(x)\equiv1
\iff
G\text{ is directed-acyclic}.
}
\]

This is a formal polynomial statement, stronger than evaluating one numerical weight assignment.

Candidate typed name:

`BRC_CYCLE_INTERACTION_POLYNOMIAL_ONE_IFF_DAG`.

## 4. Gauge invariance term by term

Under a positive vertex gauge

\[
x'_e=x_e\frac{h_{t(e)}}{h_{s(e)}},
\]

every directed cycle product telescopes. Therefore every cycle-system monomial is individually gauge invariant:

\[
w'(F)=w(F).
\]

Thus the determinant gauge invariance

\[
P_G(x')=P_G(x)
\]

is already visible term by term in the finite cycle-system expansion; no determinant cancellation is needed to establish it.

This sharply separates the positive multiplicative gauge content from the alternating inclusion-exclusion sign used to compress disjoint cycle systems.

## 5. Determinant signs are not signed BRC amplitudes

The coefficient

\[
(-1)^{c(F)}
\]

is an inclusion-exclusion/permutation sign in a finite algebraic certificate.

It is **not** a signed/amplitude branch weight in the positive Weighted-BRC carrier.

The positive recurrent semantic object remains

\[
Z_{\rm loop}=1/P_G>0
\]

and its log expansion

\[
\Gamma
=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k
\]

with non-negative closed-walk masses.

Freeze:

```text
DETERMINANT_ALTERNATING_COEFFICIENT != SIGNED_BRC_BRANCH
FINITE_INCLUSION_EXCLUSION_CERTIFICATE -> POSITIVE_INFINITE_LOOP_CLOSURE
```

## 6. Vertex-disjoint hard-core exclusion

Two directed cycles that share a vertex can never occur in the same determinant cycle system.

Example: vertices `0,1` with

- self-loop at `0` of weight `a`;
- 2-cycle `0->1->0` with edge-product `bc`.

Then

\[
\boxed{P=1-a-bc.}
\]

There is no `abc` term because the self-loop and 2-cycle overlap at vertex `0`.

By contrast,

\[
\Gamma=-\ln(1-a-bc)
\]

contains mixed higher powers after expansion. Thus inversion/log closure turns finite hard-core exclusion into an infinite interacting loop family.

If two self-loops lie in distinct one-vertex SCCs,

\[
P=(1-a)(1-b)=1-a-b+ab,
\]

and

\[
\Gamma=-\ln(1-a)-\ln(1-b),
\]

so genuinely independent recurrent components factor/add exactly.

## 7. Spanning-tree gauge interaction polynomial

For a connected rationally weighted graph, choose root/spanning tree `T` and pass to the unique tree gauge in which every tree edge has weight `1`.

Let the `beta_1` non-tree fundamental rational holonomies be

\[
z_1,\ldots,z_{\beta_1}.
\]

Substitute tree variables `1` and non-tree variables `z_j` into `P_G`:

\[
\boxed{
P_{G,T}(z_1,\ldots,z_{\beta_1}).
}
\]

This is a finite multiaffine polynomial with **integer** coefficients. Coefficients need not remain `±1` because distinct explicit cycle-system monomials can collapse after tree variables are set to `1`.

For every rational weight system `q`,

\[
\boxed{
\det(I-W(q))=P_{G,T}(\widehat q_1,\ldots,\widehat q_{\beta_1}).
}
\]

Thus the stable loop-zeta denominator can be evaluated entirely from the complete rational gauge coordinates.

Changing the spanning tree changes the coordinate polynomial by the induced integral/Laurent change of cycle coordinates but not its value on a gauge class.

Candidate typed name:

`BRC_TREE_GAUGE_CYCLE_INTERACTION_POLYNOMIAL`.

## 8. Prime-valuation and parity/thickness substitution

Each tree-normal coordinate has the exact prime-valuation form

\[
z_j=\prod_pp^{\nu_{p,j}},
\]

or for the parity/thickness split,

\[
z_j=s_jr_j^2.
\]

Hence

\[
\boxed{
P_{G,T}(z)
=P_{G,T}(s_1r_1^2,\ldots,s_{\beta_1}r_{\beta_1}^2).
}
\]

For a fixed squarefree/C2 skeleton `(s_j)`, the rational thickness variables `(r_j)` move inside a single parity stratum while changing the exact determinant, stability potential, loop-zeta and response geometry.

The one-state case is

\[
\boxed{P=1-sr^2.}
\]

Thus the earlier counterexample `q=1/2` versus `q=2` is simply motion within the fixed skeleton `s=2` across the finite-polynomial critical boundary

\[
1-2r^2=0.
\]

This gives a finite algebraic mechanism for the statement that C2 parity alone does not determine positive recurrent phase.

## 9. Edge derivative as finite numerator of infinite response

Let `P=P_G(q)>0` at a stable positive rational specialization. The previous response theorem gives

\[
R_e=q_eS_{t(e),s(e)}.
\]

Jacobi differentiation of `P` gives

\[
\boxed{
R_e
=-\frac{q_e\,\partial_eP}{P}.
}
\]

Thus the infinite positive edge-loop occupancy is a rational function whose numerator and denominator come from the finite cycle-interaction polynomial.

Since `R_e>=0`,

\[
\boxed{\partial_eP\le0}
\]

throughout the stable positive domain, with strict inequality exactly when edge `e` lies on a directed cycle.

Formally,

\[
\partial_eP\equiv0
\iff
e\text{ lies on no directed cycle},
\]

because the explicit cycle-system derivative contains a monomial iff a cycle system containing `e` exists.

Candidate typed name:

`BRC_FINITE_POLYNOMIAL_EDGE_RESPONSE_NUMERATOR`.

## 10. Multiaffine self-curvature identity

Because `P` is multiaffine in each explicit branch variable,

\[
\partial_e^2P=0.
\]

Let

\[
H_{ee}
=\frac{\partial^2\Gamma}{\partial(\ln q_e)^2}.
\]

From

\[
R_e=-q_eP_e/P
\]

and `P_{ee}=0`,

\[
\boxed{
H_{ee}=R_e+R_e^2=R_e(1+R_e).
}
\]

Thus the diagonal loop-response curvature of an explicit branch edge is determined completely by its first-order edge-loop occupancy.

Candidate typed name:

`BRC_MULTIAFFINE_EDGE_SELF_RESPONSE_IDENTITY`.

## 11. Pair response and stable polynomial inequality

For distinct explicit edges `e!=f`,

\[
\boxed{
H_{ef}
=\frac{q_eq_f}{P^2}
\left(P_eP_f-PP_{ef}\right).
}
\]

The exact response theorem also gives

\[
H_{ef}=q_eq_fS_{t(e),s(f)}S_{t(f),s(e)}\ge0.
\]

Therefore every stable positive specialization satisfies

\[
\boxed{
P_eP_f\ge PP_{ef}.
}
\]

This is a finite-polynomial inequality induced by the positive recurrent BRC closure.

Equality holds exactly when the corresponding two-edge loop-response channel vanishes.

This inequality is not promoted as a generic new determinant inequality; it is a typed consequence of the established positive inverse formula.

## 12. Finite versus infinite recurrent representations

The recurrent BRC now has two exact representations:

### Finite exclusion certificate

\[
P_G
=\sum_{\text{vertex-disjoint cycle systems }F}
(-1)^{c(F)}w(F).
\]

### Infinite positive closure

\[
P_G^{-1}
=Z_{\rm loop},
\]

\[
-\ln P_G
=\Gamma
=\sum_{k\ge1}\frac{\operatorname{tr}(W^k)}k
=\sum_{[p]\ primitive}-\ln(1-w(p)).
\]

The finite side enforces vertex-disjointness by alternating inclusion-exclusion. The infinite side exposes repeated and interacting recurrent branch families with positive mass.

Candidate synthesis name:

`BRC_FINITE_CYCLE_CERTIFICATE_INFINITE_LOOP_CLOSURE_DUALITY`.

## 13. Prior-art boundary

Classical ingredients include:

- determinant expansion over permutations/cycle systems;
- `det(I-A)` as an alternating sum over vertex-disjoint directed cycles;
- Bowen-Lanford / weighted directed graph zeta determinant identities;
- Jacobi determinant differentiation.

No generic novelty claim is made. The known combinatorial determinant literature explicitly interprets `det(I-A)` as a signed sum over disjoint cycle systems.

The project-specific synthesis under test is its typed integration with:

- explicit positive BRC branch variables;
- rational tree-gauge holonomy normal coordinates;
- prime-valuation and parity/thickness decomposition;
- exact recurrent edge response/Hessian;
- the strict boundary between determinant signs and signed/amplitude BRC semantics.

## 14. Hard boundaries

This candidate does not claim:

- determinant signs are physical/signed branch weights;
- the finite polynomial alone is a complete state outside its declared graph/gauge coordinates;
- a basis-free tree-normal polynomial;
- generic novelty of cycle-cover determinant formulas;
- that C2 parity alone determines the sign/value of the interaction polynomial;
- extension to signed/amplitude or complex-weight recurrence.
