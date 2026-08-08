# P012 — Intrinsic discrete geometry without hidden Euclidean distance

Status: `PROVED FIRST-STAGE RESOLUTION`  
Open problem: `P012`  
Scope: intrinsic integer distance from primitive state transitions

## 1. Design requirement

P012 asks for an integer-valued distance or relation compatible with finite-resolution state semantics, and asks which metric axioms survive.

The first construction should not begin with a real Euclidean distance and then round it. That would leave the continuum as the hidden geometry and make the integer value only a lossy report about it.

Instead, take **primitive adjacency / one-step reachability** as geometric data.

Let

\[
G=(V,E)
\]

be a connected undirected simple graph. Its vertices are explicit states. An edge means that one primitive geometric step is allowed.

Define

\[
d_G(u,v)
=
\min\{\ell:\text{there is an }E\text{-walk of length }\ell\text{ from }u\text{ to }v\}.
\]

The value is a natural number because a walk length is a natural number. No real coordinate or hidden straight-line length appears in the definition.

This is established graph-metric mathematics. Mathlib's `Mathlib.Combinatorics.SimpleGraph.Metric` defines graph distance exactly through shortest walk length and proves the corresponding metric laws. Enterprise Math does not claim invention of graph distance. The project-specific choice is to treat primitive adjacency as candidate foundational geometric data rather than as an approximation to a previously existing Euclidean metric.

A stable `SRC-*` registry entry for the mathlib graph-metric source must be added before this note is promoted from draft/research state to canonical review-ready material.

## 2. P012-T01 — Shortest-step distance is an integer metric

Status: `PROVED`

On every connected undirected simple graph,

\[
d_G:V\times V\to\mathbb N
\]

satisfies:

### Identity

\[
d_G(u,v)=0\iff u=v.
\]

A zero-length walk has no edge steps and therefore begins and ends at the same vertex. Conversely, every vertex has the zero-length walk to itself.

### Positivity

If \(u\ne v\), then

\[
d_G(u,v)\ge1.
\]

### Symmetry

\[
d_G(u,v)=d_G(v,u).
\]

Reverse any shortest walk.

### Triangle inequality

\[
\boxed{d_G(u,w)\le d_G(u,v)+d_G(v,w).}
\]

Concatenate a shortest walk from \(u\) to \(v\) with a shortest walk from \(v\) to \(w\). The shortest \(u\)-to-\(w\) walk cannot be longer than this explicit concatenated walk.

Thus all ordinary metric axioms survive exactly, with no real-valued intermediate quantity.

## 3. Disconnected spaces

If \(G\) is not connected, forcing one natural-number distance for all pairs requires an arbitrary junk value for unreachable pairs.

The intrinsic alternatives are:

1. use the ordinary metric separately on each connected component; or
2. use an extended integer distance

\[
\bar d_G(u,v)\in\mathbb N\cup\{\infty\},
\]

with \(\infty\) for unreachable states.

Mathlib uses this same distinction through `SimpleGraph.edist` and `SimpleGraph.dist`.

Enterprise Math should prefer explicit `∞` / component separation over pretending disconnected states have distance zero.

## 4. P012-T02 — Adjacency is exactly distance one

Status: `PROVED`

For distinct states,

\[
\boxed{u\sim v\iff d_G(u,v)=1.}
\]

Therefore the metric retains the primitive graph relation completely: the original adjacency graph can be recovered from the distance function by selecting pairs at distance one.

This is important for the foundational interpretation. Passing from adjacency to shortest-path distance does not erase the primitive one-step geometry.

## 5. P012-T03 — Geometric symmetries are graph automorphisms

Status: `PROVED`

Let

\[
f:V\to V
\]

be a graph automorphism: a bijection satisfying

\[
u\sim v\iff f(u)\sim f(v).
\]

Then

\[
\boxed{d_G(f(u),f(v))=d_G(u,v).}
\]

### Proof

Map every edge of a shortest \(u\)-to-\(v\) walk through \(f\). This gives an \(f(u)\)-to-\(f(v)\) walk of the same length, hence

\[
d_G(f(u),f(v))\le d_G(u,v).
\]

Apply the same argument to \(f^{-1}\) for the reverse inequality. ∎

This gives an intrinsic replacement for the phrase “rotation preserves distance”:

> an exact discrete rotation/symmetry is an automorphism of the primitive adjacency structure.

An arbitrary real-angle rotation need not map allowed states to allowed states and is therefore not automatically a symmetry of a discrete state geometry.

## 6. Standard integer lattice as an example, not a hidden substrate

Let the state space be

\[
\mathbb Z^d.
\]

Choose the primitive adjacency relation

\[
x\sim y
\iff
x-y\in\{\pm e_1,\ldots,\pm e_d\},
\]

where \(e_i\) are the coordinate unit steps.

This choice defines a graph directly on integer states.

## 7. P012-T04 — Standard lattice graph distance is \(L^1\)

Status: `PROVED`

For the standard-axis adjacency above,

\[
\boxed{
d(x,y)=\sum_{i=1}^d|x_i-y_i|.
}
\]

### Upper bound

Change each coordinate one integer step at a time. This constructs a walk with exactly

\[
\sum_i|x_i-y_i|
\]

steps.

### Lower bound

Each primitive step changes exactly one coordinate by exactly one. Therefore every walk from \(x\) to \(y\) must contain at least \(|x_i-y_i|\) net steps affecting coordinate \(i\). Summing over coordinates gives the same lower bound.

Hence equality holds.

The formula is therefore derived from the primitive step set. It is not obtained by replacing a Euclidean square root with an approximation.

Different primitive generator sets give different exact integer geometries. This is a feature, not an inconsistency: geometry is determined by the allowed state relations.

## 8. Exact discrete rotations of the square lattice

On \(\mathbb Z^2\) with standard-axis adjacency, the quarter-turn

\[
\rho(x,y)=(-y,x)
\]

maps every primitive axis step to another primitive axis step. It is a graph automorphism and therefore, by P012-T03,

\[
d(\rho(u),\rho(v))=d(u,v).
\]

Likewise reflections and coordinate sign changes are exact symmetries.

By contrast, a generic real angle such as \(22.5^\circ\) does not map \(\mathbb Z^2\) to itself. It is not an exact symmetry of this particular lattice geometry unless the state space or adjacency structure is enlarged.

This does not say that \(22.5^\circ\) is physically impossible. It says that exact geometric symmetry is a property of the chosen discrete state structure and must be proved there rather than imported from \(SO(2)\).

## 9. Integer spheres, balls, area and volume

For a center \(o\), define the exact integer sphere and closed ball

\[
S_r(o)=\{v:d_G(o,v)=r\},
\]

\[
B_r(o)=\{v:d_G(o,v)\le r\}.
\]

A first intrinsic notion of shell size / volume is simply cardinality:

\[
|S_r(o)|,
\qquad
|B_r(o)|.
\]

No Euclidean area element is required.

## 10. P012-T05 — Exact sphere and ball counts on \(\mathbb Z^2\)

Status: `PROVED`

For the standard-axis lattice and \(r\ge1\),

\[
\boxed{|S_r(0)|=4r.}
\]

Indeed, the equation

\[
|x|+|y|=r
\]

has exactly \(4r\) integer solutions.

The closed ball therefore has

\[
|B_r(0)|
=1+\sum_{j=1}^r4j
=1+2r(r+1).
\]

Hence

\[
\boxed{|B_r(0)|=2r^2+2r+1.}
\]

These are exact integer area/volume-growth observables for this geometry.

The corresponding “circle” is a diamond in ordinary coordinate plotting, but that visual statement is secondary. Intrinsically it is simply the distance shell \(S_r\).

## 11. P012-T06 — Locally finite primitive geometry has finite finite-radius balls

Status: `PROVED`

Suppose every vertex has finitely many primitive neighbors. Then for every vertex \(o\) and every finite \(r\),

\[
B_r(o)
\]

is finite.

### Proof

Induct on \(r\). The radius-zero ball is \(\{o\}\). If \(B_r(o)\) is finite, then the next ball is contained in the union of \(B_r(o)\) and the finite neighbor sets of its finitely many vertices. A finite union of finite sets is finite. ∎

Thus local finite resolution automatically implies finite information inside every finite graph radius, without requiring the entire universe/state graph to be finite.

## 12. P012-T07 — Positive-integer weighted edges give an integer metric

Status: `PROVED`

The unit-step assumption can be generalized. Give each undirected primitive edge a symmetric positive integer cost

\[
w(e)\in\mathbb N_{>0}.
\]

Define distance as minimum total edge cost over walks.

On a connected graph this again satisfies identity, symmetry and triangle inequality and remains integer-valued.

This allows nonuniform local resolution while keeping the geometry fully discrete.

Zero edge costs would destroy identity of indiscernibles; asymmetric/directed costs generally produce a directed quasi-metric rather than an ordinary metric. These are structural choices and should be named explicitly.

## 13. Counterexample: squared Euclidean distance is integer but not a metric

### P012-C01

Status: `COUNTEREXAMPLE`

One might try to avoid irrational square roots by using squared Euclidean distance

\[
d_2^2(x,y)=\sum_i(x_i-y_i)^2.
\]

It is integer-valued on \(\mathbb Z^d\), but it fails the triangle inequality.

Already on the integer line, take

\[
x=0,
\qquad y=1,
\qquad z=2.
\]

Then

\[
d_2^2(0,2)=4,
\]

while

\[
d_2^2(0,1)+d_2^2(1,2)=1+1=2.
\]

Thus

\[
4\nleq2.
\]

Being integer-valued is not sufficient to define a metric.

## 14. Counterexample: flooring Euclidean distance also breaks the metric

### P012-C02

Status: `COUNTEREXAMPLE`

Another tempting construction is

\[
d_{\lfloor E\rfloor}(x,y)
=
\left\lfloor\sqrt{\sum_i(x_i-y_i)^2}\right\rfloor.
\]

Even restricted to integer lattice points, the triangle inequality can fail.

Take

\[
a=(0,0),
\qquad b=(1,1),
\qquad c=(3,3).
\]

Then

\[
d_{\lfloor E\rfloor}(a,b)=\lfloor\sqrt2\rfloor=1,
\]

\[
d_{\lfloor E\rfloor}(b,c)=\lfloor\sqrt8\rfloor=2,
\]

but

\[
d_{\lfloor E\rfloor}(a,c)=\lfloor\sqrt{18}\rfloor=4.
\]

Therefore

\[
\boxed{4>1+2.}
\]

So “compute hidden Euclidean distance and floor it” is not only philosophically non-primitive; it can fail mathematically as a metric.

## 15. What P012 resolves and what it does not

P012 asked for an integer-valued distance/relation compatible with finite-resolution semantics and for a proof of which metric axioms survive.

At this level it is resolved:

- primitive adjacency is taken as the geometric relation;
- shortest primitive-step distance is an intrinsic integer metric on connected components;
- all ordinary metric axioms survive;
- adjacency is recoverable from distance one;
- exact geometric symmetries are graph automorphisms/isometries;
- finite-radius balls are finite under local finiteness;
- shell/ball cardinality provides an intrinsic first volume notion.

This does **not** settle all future discrete geometry.

Open extensions include:

- which primitive state graphs should model physical space;
- discrete curvature notions;
- scale-to-scale geometry and renormalization;
- causal/directed geometry;
- discrete analogues of Pythagorean structure;
- rotational-isotropy constraints at large scale;
- physical falsification of any chosen adjacency model.

These should be separate research problems rather than hidden inside the definition of distance.

## 16. Prior-art discipline

Shortest-path graph metrics, word metrics, lattice \(L^1\) distance, graph automorphisms, locally finite graphs and weighted shortest-path metrics are established mathematics.

Mathlib already formalizes shortest-walk graph distance and its core metric laws. Enterprise Math does not claim these results as inventions.

The project-specific research choice is to elevate an explicit primitive state relation to foundational geometry and to refuse the default assumption that the integer geometry must be obtained by rounding a hidden Euclidean continuum. Historical novelty of that foundational packaging remains `NOVELTY_UNVERIFIED`.
