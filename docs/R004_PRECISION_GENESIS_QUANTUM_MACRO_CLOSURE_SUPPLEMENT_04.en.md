# R004 precision genesis — Supplement 04: ordered scale geometry and prime-axis rank

Status: `PROVED_WIP + EXECUTABLE_CHECKED + CANDIDATE_PHYSICAL_INTERPRETATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_03.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

This supplement asks a more specific version of the geometry question:

> can a scalar integer precision hierarchy generate connected finite spatial geometry without first importing a Euclidean continuum or declaring a dimension by hand?

The answer splits into three layers. An integer order plus a boundary bridge law is enough to generate a one-dimensional path exactly. Several independent ordered precision axes generate a finite Cartesian grid. Finally, unique prime factorization gives the scalar scale factor a canonical arithmetic axis rank that can seed such a product construction. Only the first two graph statements are direct finite constructions. Identifying prime-axis rank with physical spatial dimension remains an R004 hypothesis.

## 1. General ordered-boundary path theorem

Let

\[
1=d_0\mid d_1\mid\cdots\mid d_t=L
\]

be any finite divisibility chain. On the finest carrier

\[
X_L=\{0,1,\ldots,L-1\}
\]

use the canonical P005-style projection

\[
\pi_{L\to d}(x)=x//(L/d).
\]

Every projection fiber is therefore a consecutive integer interval.

At every parent scale `d_i`, order its immediate child fibers at scale `d_{i+1}` by their integer leaves. For each adjacent pair of child fibers, add exactly one **boundary witness edge**

\[
\max(\text{left child})
\;--\;
\min(\text{right child}).
\]

### Theorem

The union of all boundary witness edges over every refinement level is exactly

\[
\boxed{
\{\{0,1\},\{1,2\},\ldots,\{L-2,L-1\}\}
}
\]

—the ordinary path graph `P_L`.

### Proof

Take any adjacent fine states `k,k+1`. At scale `d_0=1` they have the same projection, while at the final identity scale `L` they differ. Let `j` be the first level where their projections differ. Then at the previous level they lie in the same parent fiber and at level `j` they lie in two adjacent child fibers, because projection fibers are consecutive intervals and no integer lies between `k` and `k+1`. Consequently `k` is the maximum leaf of the left child and `k+1` the minimum leaf of the right child, so the boundary rule inserts exactly the edge `{k,k+1}`.

The edge cannot be inserted at an earlier level because the two states have not yet separated, and cannot first arise at a later level because once separated they lie in different parent fibers. Thus every adjacent fine edge appears exactly once and no nonadjacent edge is introduced. ∎

This proof works for arbitrary refinement ratios; it is not restricted to powers of two.

## 2. Intrinsic path metric

Since the generated graph is `P_L`, its intrinsic shortest-path distance is

\[
\boxed{d(i,j)=|i-j|.}
\]

This consumes established path-graph/P012 graph-metric mathematics. No real coordinate length is used to define the graph; only the original integer order and the finite quotient-boundary rule are required.

The construction therefore gives a precise positive result:

\[
\boxed{
\text{divisibility hierarchy}
+\text{integer order}
+\text{boundary bridge admissibility}
\Longrightarrow
\text{1D finite path geometry}.
}
\]

But the two added structures matter. Hierarchy alone still does not force the path.

## 3. Independent ordered axes give finite grid geometry

Now take `r>=1` independent ordered precision axes. Axis `i` has its own divisibility chain ending at size `L_i`. By the preceding theorem, each axis generates the path `P_{L_i}`.

Take their Cartesian graph product. The fine states are tuples

\[
(x_1,\ldots,x_r),
\qquad
0\le x_i<L_i,
\]

and primitive edges change exactly one coordinate by one path step.

The number of vertices is

\[
\boxed{|X|=\prod_{i=1}^r L_i.}
\]

The number of primitive edges is

\[
\boxed{
|E|
=\sum_{i=1}^r
(L_i-1)\prod_{j\ne i}L_j.
}
\]

P012's established lattice/path-product argument gives the exact intrinsic distance

\[
\boxed{
d(x,y)=\sum_{i=1}^r|x_i-y_i|.
}
\]

Thus independent ordered precision axes give a finite integer grid without introducing hidden Euclidean distance.

## 4. Scalar capacity does not determine dimension

The product construction immediately produces a negative boundary.

With exactly sixteen fine states one may have:

- one axis of length `16`: dimension `1`, diameter `15`;
- two axes of length `4,4`: dimension `2`, diameter `6`;
- four binary axes: dimension `4`, diameter `4`.

All have the same state capacity `16`.

Therefore

\[
\boxed{
|X|\text{ or scalar precision capacity alone}
\not\Rightarrow
\text{spatial dimension or geometry}.
}
\]

Any physical derivation of three dimensions must identify an additional independent-axis/rank structure.

## 5. Canonical arithmetic rank inside the scale lattice

A positive integer scale already contains one canonical finite rank through unique prime factorization:

\[
\lambda=\prod_{p\mid\lambda}p^{a_p}.
\]

The divisors of `lambda` correspond exactly to exponent vectors

\[
(e_p)_{p\mid\lambda},
\qquad
0\le e_p\le a_p.
\]

Hence the divisor interval below `lambda` is the product of prime-exponent chains. Define the **scale-axis rank**

\[
\boxed{
D_{\mathrm{scale}}(\lambda)
=\omega(\lambda)
=\#\{p:p\mid\lambda\}.
}
\]

This is standard arithmetic structure. In particular

\[
D_{\mathrm{scale}}(1)=0.
\]

If `lambda|mu`, every prime dividing `lambda` also divides `mu`, so

\[
\boxed{
D_{\mathrm{scale}}(\lambda)
\le
D_{\mathrm{scale}}(\mu).
}
\]

Thus scale-axis rank is automatically nondecreasing along compatible refinement.

## 6. Rank opening and later precision growth

The finite chain

\[
1\mid2\mid6\mid30\mid60\mid180\mid900
\]

has exact ranks

\[
\boxed{0,1,2,3,3,3,3.}
\]

The first three nontrivial steps introduce prime supports `2`, then `2,3`, then `2,3,5`. Later refinements increase only existing prime exponents.

This gives a mathematically coherent pattern:

- precision one: zero prime axes;
- early refinement can increase arithmetic rank;
- after prime support stabilizes, precision can continue increasing indefinitely through exponent growth while the rank remains fixed.

That pattern resembles the R004 desired narrative “geometry/rank opens early, precision continues later,” but resemblance is not proof of physical identity.

## 7. Prime-product geometry candidate

For

\[
\lambda=\prod_{i=1}^r p_i^{a_i},
\]

let the `i`-th candidate ordered axis have side length

\[
L_i=p_i^{a_i}
\]

with scale chain

\[
1,p_i,p_i^2,\ldots,p_i^{a_i}.
\]

The side lengths are pairwise coprime and satisfy

\[
\prod_i L_i=\lambda.
\]

Applying the ordered-axis product construction therefore gives a finite grid candidate with

\[
\boxed{
\text{candidate dimension}=\omega(\lambda),
\qquad
|X|=\lambda.
}
\]

For example:

- `lambda=1`: rank `0`, one-state pregeometry;
- `lambda=2`: rank `1`, axis size `(2)`;
- `lambda=6`: rank `2`, axis sizes `(2,3)`;
- `lambda=30`: rank `3`, axis sizes `(2,3,5)`, `30` vertices, diameter `7`;
- `lambda=60`: rank `3`, axis sizes `(4,3,5)`, `60` vertices, diameter `9`;
- `lambda=180`: rank `3`, axis sizes `(4,9,5)`, `180` vertices, diameter `15`.

The geometry continues to refine while candidate dimension remains three once prime support stabilizes.

## 8. The critical no-go: why exactly three primes?

The prime-axis construction removes one arbitrary input—the number of axes can now be read canonically from the arithmetic scale factor—but it creates a sharper physical problem.

Nothing in P005 or unique factorization forces the prime support to stop after exactly three distinct primes. A later refinement could introduce a fourth prime and make

\[
\omega(\lambda)
\]

increase to four.

Therefore a physical identification

\[
\text{spatial dimension}=\omega(\lambda)
\]

requires an additional **prime-support stabilization law**. After the hypothesized three-axis genesis epoch, every later refinement factor would have to use only the already-active prime support.

This is a real model commitment and therefore a useful kill point. The theory must explain why the support stabilizes and why its stable rank is three; merely observing that `30=2*3*5` gives a convenient example is not an explanation.

## 9. Geometry-to-P016 bridge

Supplement 02's threshold-record submodel used an integer alternative separation `delta`. The ordered and product geometries now supply that separation intrinsically:

- on one ordered axis, `delta=d_path(x,y)=|x-y|`;
- on several axes, `delta=d_grid(x,y)=sum_i|x_i-y_i|`.

The record-overlap law becomes

\[
\boxed{
\eta(x,y;d)
=
\frac{\max(d-d_G(x,y),0)}d.
}
\]

So `delta` is no longer an independent fit parameter inside this bridge; geometry determines it.

This creates an immediate combined negative boundary. Three geometries with the same sixteen-state capacity and record resolution `d=10` give different antipodal overlaps:

- `P_16`, diameter `15`: `eta=0`;
- `P_4 square P_4`, diameter `6`: `eta=2/5`;
- four-dimensional binary cube, diameter `4`: `eta=3/5`.

Thus even the P016 toy prediction is sensitive to the internal geometry, not merely the number of states.

The remaining free physical quantity is the record resolution `d` and, more fundamentally, whether the threshold-record law is the correct apparatus interaction at all.

## 10. Revised dimensional frontier

R004 now has a finite constructive ladder:

\[
\text{scale divisibility}
\to
\text{ordered quotient fibers}
\to
\text{path geometry}
\to
\text{independent-axis product grid}
\to
\text{candidate axis rank}.
\]

Unique factorization supplies one canonical arithmetic rank candidate. But the physical program is not closed until one primitive causal law explains all of the following at once:

1. why integer order/boundary bridges are the admissible local relations;
2. why independent scale directions correspond to spatial directions;
3. why prime support stabilizes at exactly three;
4. why the same geometry controls environment-record overlap;
5. how these local/causal rules coexist with the Bell-locality and measurement-independence pressure tests from Supplements 02-03.

This is a much narrower and more falsifiable target than “precision somehow becomes three-dimensional space.”
