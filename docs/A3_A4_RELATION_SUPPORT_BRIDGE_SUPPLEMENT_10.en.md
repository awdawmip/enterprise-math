# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 10

Status: `ACTIVE RESEARCH NOTE`  
Scope: arbitrary-depth witness-count tensors, coefficient convolution, and the exact projection to existence frontiers

## 1. From two-stage histograms to arbitrary depth

Stage 09 identified the two-stage witness-cost histogram as the count-complete state for all budgeted common-target counts. The same construction extends to every finite stage depth.

Fix `k>=1`, endpoints `x,z`, and integer metric `rho` on the A3 zero-relation quotient.

For a represented chain

\[
x=x_0,x_1,\ldots,x_k=z,
\]

define its exact cost vector

\[
\mathbf a=(\rho(x_0,x_1),\ldots,\rho(x_{k-1},x_k))\in\mathbb N^k.
\]

## 2. B36 — multistage witness-count tensor

Define

\[
\boxed{
H^{(k)}_{xz}(\mathbf a)
=
\#\{\text{represented k-stage chains from x to z with exact cost }\mathbf a\}.
}
\]

This is a finite-support function from `N^k` to `N`.

For budget vector `r`, define the number of admissible represented chains

\[
\boxed{
N^{(k)}_{xz}(\mathbf r)
=
\sum_{\mathbf a\preceq\mathbf r}H^{(k)}_{xz}(\mathbf a).
}
\]

Thus the complete multistage count language is the `k`-dimensional prefix-sum transform of the exact cost tensor.

## 3. B37 — product-poset Möbius inversion

Extend `N^(k)` by zero outside `N^k`. Repeated finite differences recover every exact coefficient:

\[
\boxed{
H^{(k)}(\mathbf a)
=
\sum_{\varepsilon\in\{0,1\}^k}
(-1)^{|\varepsilon|}
N^{(k)}(\mathbf a-\varepsilon).
}
\]

Therefore the all-budget path-count function and the exact cost tensor are information-equivalent using integer arithmetic.

Up to re-encoding, `H^(k)` is the P023 task-minimal coordinate for the full `k`-stage witness-count language.

## 4. B38 — coefficient convolution

Let `H^(p)` and `H^(q)` be exact prefix/suffix count tensors. For vectors `u in N^p`, `v in N^q`, let `u||v` denote concatenation.

Then

\[
\boxed{
H^{(p+q)}_{xz}(u\Vert v)
=
\sum_y
H^{(p)}_{xy}(u)
H^{(q)}_{yz}(v).
}
\]

### Proof

Every `(p+q)`-stage path has a unique state `y` at the stage-`p` split. For fixed `y`, every prefix path of exact cost `u` can be concatenated with every suffix path of exact cost `v`, giving the product of their counts. Summing over all split states counts each represented full path exactly once.

This is an associative matrix convolution over non-negative integer coefficients.

Starting from the one-stage coefficient

\[
H^{(1)}_{xy}(a)=1[a=\rho(x,y)],
\]

all finite-depth count tensors are generated recursively.

## 5. Generating-function form

Introduce stage-labeled commuting variables `t_1,...,t_k` and define

\[
\boxed{
P^{(k)}_{xz}(t_1,\ldots,t_k)
=
\sum_{\mathbf a}
H^{(k)}_{xz}(\mathbf a)
\prod_{j=1}^k t_j^{a_j}.
}
\]

Then coefficient convolution is ordinary matrix multiplication with polynomial entries after keeping prefix and suffix variable blocks distinct.

This gives a compact algebraic view of the count-complete future state. It does not require probability or real-valued weights.

## 6. B39 — existence antichain is an idempotent shadow of the count tensor

Take the positive support

\[
S^{(k)}_{xz}=\{\mathbf a:H^{(k)}_{xz}(\mathbf a)>0\}.
\]

Then the Stage-06 existence frontier is exactly

\[
\boxed{
F^{(k)}_{xz}
=\operatorname{ParetoMin}(S^{(k)}_{xz}).
}
\]

So the information projection is

\[
H^{(k)}
\longrightarrow
1[H^{(k)}>0]
\longrightarrow
F^{(k)}.
\]

Coefficient magnitude is discarded first; dominated positive-support costs are discarded second.

The antichain convolution of Stage 08 is therefore the existence/idempotent shadow of the richer natural-number coefficient convolution.

## 7. B40 — geodesic existence collapse does not collapse witness counts

The Stage-06 geodesic theorem says that existence semantics at every finite depth reduces to endpoint `rho` and total budget. That compression is **not** valid for witness-count semantics.

Consider endpoints at normalized positions `0` and `1.5`, so direct integer relation distance is `rho=2`.

### System A

Equal capacities `20`, totals

\[
(0,15,30)
\]

represent positions `0,0.75,1.5`. The exact `(1,1)` split has one internal witness.

### System B

Equal capacities `20`, totals

\[
(0,12,18,30)
\]

represent positions `0,0.6,0.9,1.5`. The exact `(1,1)` split has two internal witnesses.

Both systems are geodesic for the endpoint pair and have the same existence frontier

\[
\{(0,2),(1,1),(2,0)\}.
\]

But their coefficient at `(1,1)` differs.

Therefore

\[
\boxed{
\text{geodesic future-depth collapse is valid for existence,
not automatically for multiplicity.}
}
\]

A count-sensitive future language must retain richer coefficient state even when `Gamma=0`.

## 8. Connection to P011 and A4/E001

### P011

P011 already shows that integer multiplicity structure can be captured by coefficient spectra/polynomials and recovered by integer inversion. Stage 10 uses the same broad coefficient-first methodology on path-cost multiplicities rather than fiber-size multiplicities.

The lines should share algebraic tooling where appropriate but remain semantically distinct.

### A4/E001

A4 relation truth is the positive-support shadow of count matrices; E001 materialized common-target memberships live naturally at the coefficient layer. Engineering may choose which layer to compute depending on whether the requested output is existence, count, or labeled witness identity.

## 9. Future-state ladder

For staged support we now have a strict semantic ladder:

\[
\boxed{
\text{labeled paths}
\Rightarrow
H^{(k)}/P^{(k)}
\Rightarrow
F^{(k)}
\Rightarrow
\text{selected truth bits}
}
\]

Each descent is legal only for future languages that ignore the discarded information.

This ladder is one of the clearest current examples of the Enterprise Math principle:

> state size should be determined by proven future distinguishability, not by an assumption that maximum detail is always required.

## 10. Prior-art discipline

Path-count generating functions, multidimensional prefix sums, product-poset Möbius inversion and polynomial matrix products are established mathematics. The project-specific contribution under test is the exact integration of those tools with the A3-generated support metric, A4 witness semantics and P023 task-relative collapse hierarchy.

## 11. Executable reference

The reference layer adds:

- arbitrary-depth exact cost-count histograms;
- budgeted path counts;
- recursive coefficient convolution;
- projection from coefficient support to Pareto existence frontiers;
- the geodesic-same/existence-different-count regression example.
