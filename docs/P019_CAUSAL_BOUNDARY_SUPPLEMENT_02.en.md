# P019 — Causal Boundary, Supplement 02: From Radial Formulae to Primitive Graph Cuts

Status: `ACTIVE RESEARCH NOTE`  
Depends on: P012 primitive graph geometry, P018 finite precision, P019 Schwarzschild/RN stages  
Scope: finite-graph horizon skeleton without a radial coordinate  
Discipline: this supplement abstracts the boundary structure; it does not yet derive the expansion field from Einstein dynamics.

## 1. The input no longer contains radius

Let

\[
G=(V,E)
\]

be a finite primitive undirected graph. Its edges are basic adjacency relations, not products of a hidden Euclidean metric.

Give the graph an integer-valued outgoing-expansion field

\[
\boxed{\xi:V\to\mathbb Z.}
\]

Retain only its phase

\[
\phi(v)=\operatorname{sgn}(\xi(v))\in\{-1,0,+1\}.
\]

At the interpretation layer one may read:

- `+1` as outgoing expansion;
- `0` as marginal/zero expansion;
- `-1` as outgoing contraction.

The theorems below depend only on the integer sign structure, not on that physical interpretation.

## 2. Definition: causal boundary complex

Define the zero-vertex set

\[
\boxed{V_0=\{v\in V:\xi(v)=0\}.}
\]

Define the sign-crossing edge set

\[
\boxed{
E_{\pm}
=
\{\{u,v\}\in E:\xi(u)\xi(v)<0\}.
}
\]

Call

\[
\boxed{\partial_\xi G=(V_0,E_{\pm})}
\]

the **causal boundary complex** of `xi`.

It deliberately retains two discrete horizon representations:

1. a **primal boundary** at zero-expansion vertices;
2. a **dual boundary** on crossing edges between opposite phases.

This is the minimum unified object forced by the RN pressure test.

## 3. P019-G-T01 — Discrete causal intermediate-value theorem

Status: `PROVED`

Let

\[
v_0,v_1,\ldots,v_m
\]

be a graph path whose endpoints have opposite nonzero phase:

\[
\xi(v_0)\xi(v_m)<0.
\]

Then at least one of the following holds:

1. some `i` has

\[
\xi(v_i)=0;
\]

2. some adjacent `i,i+1` has

\[
\xi(v_i)\xi(v_{i+1})<0.
\]

Equivalently,

\[
\boxed{
\text{every path from an expansion region to a contraction region intersects }\partial_\xi G.
}
\]

### Proof

If the path already contains a zero vertex, the result is immediate.

Otherwise every value is strictly positive or negative. Since the first and last values have different signs, a first sign change must occur along the finite sequence. The corresponding adjacent pair has negative product and is therefore an edge in `E_pm`. ∎

This is a fully finite discrete intermediate-value statement; it requires no continuous function, real interval, or limit.

## 4. P019-G-T02 — Removing the boundary leaves phase-homogeneous connected components

Status: `PROVED`

From `G`, delete:

- every vertex in `V_0`;
- every crossing edge in `E_pm`.

Call the remaining graph `G\partial`.

Every connected component of `G\partial` has a single phase.

Otherwise one component would contain both a positive and a negative vertex, joined by a path entirely inside the remaining graph. T01 says that path must contain a deleted zero vertex or crossing edge, a contradiction. ∎

Thus `partial_xi G` genuinely separates the positive and negative causal phases instead of merely marking local anomalies.

## 5. P019-G-T03 — Extremal boundaries show why crossing edges alone are insufficient

Status: `PROVED BY EXAMPLE / STRUCTURAL NECESSITY`

Consider the path

\[
+\;--\;0\;--\;+.
\]

No adjacent pair has negative product, so

\[
E_{\pm}=\varnothing.
\]

Yet the central vertex belongs to

\[
V_0.
\]

This is exactly the structural pattern of RN extremality at `Delta=0`: a zero-expansion boundary exists without a sign reversal across it.

Any discrete definition using only

\[
\text{horizon}=\text{positive/negative sign-change cut}
\]

would therefore miss extremal boundaries.

The minimum unified object must keep

\[
\boxed{V_0+E_{\pm}.}
\]

## 6. P019-G-T04 — The boundary construction is equivariant under primitive graph automorphisms

Status: `PROVED`

Let

\[
\alpha:V\to V
\]

be a graph automorphism and transport the expansion field by

\[
\xi'(\alpha(v))=\xi(v).
\]

Then

\[
\boxed{
\partial_{\xi'}G
=
\alpha(\partial_\xi G).
}
\]

Indeed:

- `xi(v)=0` iff `xi'(alpha(v))=0`;
- `xi(u)xi(v)<0` iff `xi'(alpha(u))xi'(alpha(v))<0`;
- the automorphism preserves primitive adjacency exactly.

The boundary therefore does not depend on vertex names or an external coordinate label.

This is closer to the intrinsic-geometry requirement of P012 than the radial equation `n=h`.

It proves only intrinsic behavior relative to the already chosen primitive graph and expansion field; it does not identify the physical graph or the correct physical `xi`.

## 7. P019-G-T05 — Schwarzschild and RN are one-dimensional specializations

Status: `PROVED BY SPECIALIZATION`

Take the radial line graph

\[
0-1-2-3-\cdots
\]

and define

\[
\xi(n)=P(n)=n^2-an+b.
\]

Then `partial_xi G` is exactly the vertex-edge boundary complex of RN Supplement 01:

- `P(n)=0` produces zero vertices;
- `P(n)P(n+1)<0` produces non-grid-aligned crossing edges.

Further setting `b=0,a=h` gives

\[
P(n)=n(n-h),
\]

whose positive-radius boundary recovers the Schwarzschild horizon `h`.

The three stages therefore form a strict nesting:

\[
\boxed{
\text{Schwarzschild}
\subset
\text{quadratic charged radial model}
\subset
\text{coordinate-free graph-boundary skeleton}.
}
\]

## 8. P019-G-T06 — Precision refinement makes causal-phase ambiguity nonincreasing

Status: `PROVED FROM P018`

Fix a finite terminal vertex set `V` and a precision observation

\[
O_\lambda:V\to Y_\lambda.
\]

For the observation fiber

\[
[v]_\lambda
=
\{u:O_\lambda(u)=O_\lambda(v)\},
\]

define the still-compatible phase set

\[
\boxed{
\Phi_\lambda(v)
=
\{\phi(u):u\in[v]_\lambda\}.
}
\]

and phase ambiguity

\[
\boxed{
A^\phi_\lambda(v)=|\Phi_\lambda(v)|
\in\{1,2,3\}.
}
\]

If `mu` refines `lambda` in the P018 sense, then

\[
[v]_\mu\subseteq[v]_\lambda,
\]

so

\[
\Phi_\mu(v)\subseteq\Phi_\lambda(v)
\]

and hence

\[
\boxed{
A^\phi_\mu(v)
\le
A^\phi_\lambda(v).
}
\]

This gives P019 a more direct candidate than radial-position ambiguity: as precision increases, the number of causal phases still compatible with an observation can only decrease.

It remains precision ambiguity, not thermodynamic entropy.

## 9. P019-G-T07 — Boundary certificates can complete before full state recovery

Status: `DIRECT P018 CONSEQUENCE`

To decide that a state lies in the positive or negative phase, the terminal vertex need not be reconstructed uniquely.

If `phi` is already constantly `+1` on the entire observation fiber, there is a stable OUTSIDE/EXPANDING certificate. If it is constantly `-1`, there is a stable INSIDE/CONTRACTING certificate.

P018 predicate-certificate persistence guarantees that further refinement cannot overturn a phase certificate once it is constant on the coarse fiber.

Horizon detection is therefore naturally a **predicate-complete precision** problem rather than a state-complete precision problem.

This aligns directly with the P018 program: a finite natural question often requires only enough finite precision to decide the target structure, not infinite-precision reconstruction of the whole state.

## 10. Current coordinate-free core

At this point P019 no longer needs

\[
r=r_s
\]

as its definition of a horizon.

The current minimal mathematical candidate is

\[
\boxed{
\text{primitive graph}
+
\text{integer outgoing-expansion field}
+
\text{zero vertices / crossing edges}
+
\text{finite precision fibers}.
}
\]

with

\[
\boxed{\partial_\xi G=(V_0,E_{\pm}).}
\]

Four advantages are already proved:

1. no radial coordinate is required;
2. no hidden Euclidean distance is required;
3. ordinary and extremal boundaries are both represented;
4. the boundary transports naturally under primitive graph automorphisms.

## 11. What remains unsolved

This abstraction moves the problem to its genuinely difficult point; it does not complete a black-hole theory.

### 11.1 Where does `xi` come from?

The integer outgoing-expansion field is currently input data. A physical theory must generate it from local state, matter/energy content, and an evolution law rather than label it by hand.

### 11.2 Directed causality

P012's first metric stage uses undirected primitive adjacency. Physical causal structure is more naturally a directed graph/relation. P019 must next study a directed refinement rather than treat the undirected skeleton as final ontology.

### 11.3 Locality

How large a neighborhood is allowed to determine `xi(v)`? If its computation requires a full-graph scan, the field loses local physical meaning.

### 11.4 Dynamics

A static boundary is only a slice. Formation, evaporation, and merger require

\[
G_t,\xi_t,\partial_{\xi_t}G_t
\]

to evolve with time.

### 11.5 Invariant comparison with continuum GR

Trapped surfaces, null expansion, event horizons, apparent horizons, and related external notions must be compared separately. They cannot all be collapsed into one undifferentiated word “horizon.”

## 12. Stage ledger

- `P019-G-T01`: discrete causal intermediate-value theorem — `PROVED`
- `P019-G-T02`: boundary removal makes each connected component phase-homogeneous — `PROVED`
- `P019-G-T03`: zero vertices are necessary for extremal boundaries — `PROVED STRUCTURAL NECESSITY`
- `P019-G-T04`: graph-automorphism equivariance — `PROVED`
- `P019-G-T05`: RN/Schwarzschild specialization — `PROVED`
- `P019-G-T06`: phase ambiguity is nonincreasing under P018 refinement — `PROVED`
- `P019-G-T07`: phase predicate completeness can precede state completeness — `P018 CONSEQUENCE`

Executable checks:

- `src/enterprise_math/causal_boundary.py`
- `tests/test_causal_boundary.py`

## 13. Next stage

1. upgrade `G` to a directed primitive causal graph;
2. derive an integer expansion candidate from one-step future reachability rather than providing it manually;
3. study compatibility of that expansion under graph refinement / scale projection;
4. classify integer boundary creation/merge/split events for dynamic `G_t`;
5. then use Kerr as the rotation pressure test and determine whether the boundary complex must extend from vertices/edges to higher cells.
