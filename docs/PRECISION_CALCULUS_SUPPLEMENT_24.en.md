# P018 — Finite-Precision Proof Calculus: Supplement 24

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact one-step transport branching, minimum deterministic correction-token alphabet, integer bit cost, operation-tree composition, and the sharp remainder/carry separation for radix arithmetic  
Depends on: P018-T169–T181, T183–T194, T197  
Prior-art boundary: communication complexity and coding for computing are established fields. The minimum-token statement below is an elementary finite deterministic specialization and is not claimed as a new communication-complexity theorem. See `docs/PRIOR_ART_P018_TRANSPORT_COMPLEXITY.*`. [SRC-YAO-1979-DISTRIBUTIVE] [SRC-ORLITSKY-ROCHE-2001-CODING]

---

## 1. State sufficiency and transport sufficiency are different questions

Supplement 19 answered the finite state question:

> what state distinctions must persist so that every declared operation is exact?

Its answer is the contextual/syntactic congruence closure.

But an implementation may already know the coarse input classes and only need enough extra information to determine the **coarse output of one operation call**. That is a different information problem.

For a finite state set `X`, observation equivalence

\[
E=\ker(O),
\]

and a `k`-ary operation

\[
\mu:X^k\to X,
\]

fix one coarse input cell

\[
C=(y_1,\ldots,y_k)\in O(X)^k.
\]

Define its realizable coarse output set

\[
\operatorname{Out}_E(\mu;C)
=
\{O(\mu(x_1,\ldots,x_k)):O(x_i)=y_i\ \forall i\}.
\]

---

## 2. P018-T198 — Transport branching capacity

Status: `PROVED / EXECUTABLE`

Define

\[
\boxed{
B_E(\mu)
=
\max_C
|\operatorname{Out}_E(\mu;C)|.
}
\]

This is the worst-case number of distinct coarse outputs that remain possible **after the complete coarse input tuple is already known**.

It is an integer satisfying

\[
1\le B_E(\mu)\le |X|.
\]

More sharply, if every raw observation fiber contains at most `M` fine states, then

\[
B_E(\mu)\le M^k,
\]

because one coarse input cell contains at most `M^k` fine tuples.

---

## 3. P018-T199 — Congruence is exactly zero transport ambiguity

Status: `PROVED / EXECUTABLE`

The following are equivalent:

1. `E` is compatible with `mu`;
2. `mu` descends exactly to the coarse quotient;
3. every coarse input cell has exactly one realizable coarse output;
4.

\[
\boxed{B_E(\mu)=1.}
\]

Thus transport branching measures the one-step failure of the raw precision to be operation-congruent.

This is compatible with T169 but answers a quantitative rather than merely Boolean question.

---

## 4. P018-T200 — Exact minimum deterministic correction-token alphabet

Status: `PROVED / EXECUTABLE / ELEMENTARY COUNTING`

Consider the following exact one-message protocol for one operation call.

The decoder already knows the coarse input tuple `C`. An encoder that sees the fine tuple sends one token

\[
c\in\mathcal C.
\]

The decoder must recover the exact coarse output

\[
O(\mu(x_1,\ldots,x_k))
\]

from `(C,c)`.

Then

\[
\boxed{|\mathcal C|_{\min}=B_E(\mu).}
\]

### Lower bound

Choose a coarse input cell attaining `B_E(mu)`. Its `B_E(mu)` different realizable coarse outputs must receive pairwise distinguishable token values; otherwise two different outputs would decode from the same `(C,c)`.

Therefore

\[
|\mathcal C|\ge B_E(\mu).
\]

### Upper bound

Inside each coarse input cell, enumerate its realizable coarse outputs by local indices

\[
0,\ldots,|\operatorname{Out}_E(\mu;C)|-1.
\]

The same token labels may be reused in different cells because the decoder already knows `C`. Since no cell has more than `B_E(mu)` outputs, a global token alphabet of exactly that size suffices.

The reference implementation constructs this codebook explicitly.

This theorem is deliberately restricted to deterministic zero-error one-message cardinality. It does not address probabilistic average rates, interactive protocols, variable-length coding, or asymptotic block coding.

---

## 5. P018-T201 — Exact fixed-length integer bit cost

Status: `PROVED / EXECUTABLE`

For a token alphabet of size `B>=1`, the exact minimum fixed-length binary word size is

\[
\boxed{
L(B)=\operatorname{bitlen}(B-1)
=\lceil\log_2 B\rceil,
}
\]

with `L(1)=0`.

Define

\[
\boxed{L_E(\mu)=L(B_E(\mu)).}
\]

The implementation uses only integer `bit_length`; no floating logarithm is needed.

---

## 6. P018-T202 — Operation-tree transport branching is submultiplicative

Status: `PROVED / EXECUTABLE`

Let an outer `k`-ary operation `mu` receive the outputs of disjoint-input suboperations

\[
\nu_1,\ldots,\nu_k.
\]

Let the composite operation be

\[
\Phi=\mu\circ(\nu_1,\ldots,\nu_k).
\]

For a fixed coarse leaf-input cell, each `nu_i` can produce at most

\[
B_E(\nu_i)
\]

coarse intermediate outputs. Therefore there are at most

\[
\prod_i B_E(\nu_i)
\]

possible coarse intermediate tuples.

For each such tuple, the outer operation has at most `B_E(mu)` possible coarse outputs. Hence

\[
\boxed{
B_E(\Phi)
\le
B_E(\mu)\prod_iB_E(\nu_i).
}
\]

Consequently fixed-length bit costs satisfy the generic additive upper bound

\[
\boxed{
L_E(\Phi)
\le
L_E(\mu)+\sum_iL_E(\nu_i).
}
\]

This is a universal product protocol, not necessarily optimal. Strict inequality measures transport fusion/cancellation that a more structured protocol may exploit.

---

## 7. P018-T203 — Persistent contextual detail bounds transport branching

Status: `PROVED / EXECUTABLE`

Let `R_*` be the contextual closure for an operation language containing `mu`.

For each raw observation value `y`, let

\[
m_y
=
\#\{R_*\text{-blocks contained in }O^{-1}(y)\}.
\]

T176 showed that

\[
D=\max_y m_y
\]

is the minimum reusable persistent detail alphabet for a state representation `(O(x),D(x))`.

Now fix a coarse input cell

\[
C=(y_1,\ldots,y_k).
\]

Each operand can occupy only `m_(y_i)` exact contextual-state blocks inside its raw fiber. Since `R_*` is a congruence, an input tuple of contextual blocks determines the output contextual block and hence the raw coarse output.

Therefore

\[
\boxed{
|\operatorname{Out}_E(\mu;C)|
\le
\prod_i m_{y_i}.
}
\]

Globally,

\[
\boxed{B_E(\mu)\le D^k.}
\]

This makes the distinction precise:

- `D` = persistent per-operand exact state complexity;
- `B_E(mu)` = operation-specific one-step correction complexity given raw coarse inputs.

They can be radically different.

---

## 8. P018-T204 — Radix quotient addition has exactly binary transport branching

Status: `PROVED / EXECUTABLE`

Let

\[
Q_r(n)=\left\lfloor\frac nr\right\rfloor,
\qquad r\ge2.
\]

Write

\[
x=ra+u,
\qquad y=rb+v,
\qquad 0\le u,v<r.
\]

Then

\[
Q_r(x+y)
=
a+b+\left\lfloor\frac{u+v}{r}\right\rfloor.
\]

The final term is always `0` or `1`. Both values occur in every ordinary coarse input cell: use `(u,v)=(0,0)` for `0` and `(r-1,1)` for `1`.

Therefore

\[
\boxed{B_{Q_r}(+)=2.}
\]

By T200,

\[
\boxed{|\mathcal C|_{\min}=2,\qquad L_{Q_r}(+)=1.}
\]

The canonical token is precisely the carry

\[
\kappa_r(u,v)=\left\lfloor\frac{u+v}{r}\right\rfloor.
\]

Combining with T178:

\[
\boxed{
\text{remainder: }r\text{-state minimum persistent operand detail},
\qquad
\text{carry: }2\text{-symbol minimum one-step transport token}.
}
\]

This is the sharpest current separation between state complexity and transport complexity in P018.

---

## 9. P018-T205 — Radix quotient multiplication has maximal residue-pair branching

Status: `PROVED / EXECUTABLE`

The same quotient precision behaves very differently for multiplication.

Write

\[
x=r a+u,
\qquad y=r b+v.
\]

Then

\[
Q_r(xy)
=
r a b+a v+b u+\left\lfloor\frac{uv}{r}\right\rfloor.
\]

Every coarse input cell contains exactly `r^2` fine residue pairs, so automatically

\[
B_{Q_r}(\times)\le r^2.
\]

This bound is attained.

Choose coarse inputs

\[
a=1,
\qquad b=2r.
\]

Ignoring the common constant `2r^2`, the variable coarse output is

\[
F(u,v)=2ru+v+\left\lfloor\frac{uv}{r}\right\rfloor.
\]

For fixed `u`, `F(u,v)` is strictly increasing in `v`. Its largest value is at most

\[
2ru+2r-3,
\]

while the next `u+1` block begins at

\[
2r(u+1)=2ru+2r.
\]

Therefore the `r` value ranges for different `u` are disjoint, and all `r^2` residue pairs produce distinct coarse outputs.

Hence

\[
\boxed{B_{Q_r}(\times)=r^2.}
\]

So the minimum deterministic one-step token alphabet in the worst multiplication cell has size `r^2`:

\[
\boxed{L_{Q_r}(\times)=\lceil 2\log_2 r\rceil.}
\]

In cardinality terms, the worst multiplication transport must retain the entire joint residue-pair distinction. Addition's one-bit carry is therefore highly operation-specific, not a generic consequence of quotient precision.

---

## 10. P018-C22 — Small carry-like transport is not generic

Status: `COUNTERWEIGHT / DESIGN BOUNDARY`

For the same radix quotient state:

\[
B_{Q_r}(+)=2,
\qquad
B_{Q_r}(\times)=r^2.
\]

Thus there is no general theorem of the form

> coarse quotient arithmetic always needs only a small bounded carry token.

The carry cocycle is a strong special structure of addition. Other operations can require transport branching as large as the full fine-input multiplicity of a coarse cell.

Consequently P018 must keep separate:

1. congruence/state closure;
2. exact transport cardinality;
3. additional algebraic structure that may compress or compose the token elegantly.

Only the third layer is appropriately called carry/cocycle-like when its laws actually justify that language.

---

## 11. P018-T206 — Q119 is resolved at the unstructured one-step cardinality layer

Status: `PARTIALLY RESOLVED / EXACT CARDINALITY LAYER`

For a finite state set, finite operation, and raw precision equivalence, the exact deterministic one-message correction alphabet required to recover one coarse output from known coarse inputs is completely characterized by

\[
\boxed{B_E(\mu).}
\]

The layer now has:

- an exact minimum alphabet cardinality;
- an exact integer fixed-length bit cost;
- a generic operation-tree composition bound;
- a direct upper bound from persistent contextual state detail;
- sharp arithmetic examples separating addition from multiplication.

This **does not fully resolve Q119** as originally posed.

The remaining stronger question is:

> characterize when minimal or near-minimal transport tokens admit a structured, representation-stable, composable algebraic law across operation trees, and quantify the gap between generic product composition and optimal fused transport.

That problem remains open.

---

## 12. Executable pressure tests

Added:

- `src/enterprise_math/transport_branching.py`
- `tests/test_transport_branching.py`

Tests include:

1. exhaustive two-state binary operations and observations verifying `B=1` exactly matches operation congruence;
2. explicit minimum-size cell-local codebooks and exact encode/decode round trips;
3. exact integer fixed-length bit costs;
4. exhaustive two-state outer-binary / inner-unary composition tests for T202;
5. contextual-detail product bounds;
6. exhaustive two-state local detail bounds;
7. radix addition `B=2` for radices 2 through 64;
8. radix multiplication `B=r^2` for radices 2 through 39;
9. direct comparison showing multiplication transport can be arbitrarily larger than the binary addition carry.

---

## 13. Current foundational feedback

The finite precision stack now separates four distinct questions:

\[
\boxed{
\begin{aligned}
&\text{static observation}\\
&\downarrow\\
&\text{contextual closure: minimum persistent exact state}\\
&\downarrow\\
&\text{transport branching }B_E(\mu):\text{ minimum one-step token}\\
&\downarrow\\
&\text{structured transport law: carry/cocycle/fusion when actually present}.
\end{aligned}
}
\]

This separation prevents two recurring mistakes:

- treating every missing state distinction as if it were merely a carry bit;
- treating every compact transport correction as if it eliminated the need for persistent exact operand detail.

The next research target should therefore study **transport fusion and representation stability**, not invent another state quotient.
