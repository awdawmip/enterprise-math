# P019 Supplement 03 — Spherical Excavation, Directional Boundary, and Cross-Dimensional Identity

Status: `RESEARCH WIP / PROVED COMBINATORIALLY`  
Scope: `A_p` primitive graph balls, discrete cavities, directional cut boundaries, dimension recursion  
Discipline: this note does not claim that physical space is `A_p`, nor that a graph ball is a Euclidean sphere.

## 1. Excavation setup

For

\[
A_p=\{x\in\mathbb Z^{p+1}:\sum_i x_i=0\},
\]

use the primitive-root graph distance

\[
d_G(0,x)=\sum_{x_i>0}x_i=\frac12\sum_i|x_i|
\]

and define

\[
B_p(r)=\{x\in A_p:d_G(0,x)\le r\},
\qquad V_p(r)=|B_p(r)|.
\]

Existing `A_p` growth gives

\[
V_p(r)=\sum_{j=0}^{\min(p,r)}\binom pj^2\binom{r-j+p}{p}.
\]

The outer vertex shell is

\[
S_p(r)=V_p(r)-V_p(r-1)=\nabla V_p(r).
\]

Thus `p`-dimensional excavated volume is a degree-`p` integer-valued polynomial and its first discrete boundary is degree `p-1`.

## 2. X01 — Dimension from finite-difference depth

The ball generating function is

\[
\sum_{r\ge0}V_p(r)t^r
=\frac{H_p(t)}{(1-t)^{p+1}},
\qquad H_p(t)=\sum_{j=0}^p\binom pj^2t^j.
\]

By Vandermonde,

\[
H_p(1)=\binom{2p}{p}.
\]

Hence the leading coefficient of `V_p` is `binom(2p,p)/p!`, so

\[
\boxed{\nabla^pV_p(r)=\binom{2p}{p},\qquad \nabla^{p+1}V_p(r)=0.}
\]

This yields an intrinsic growth dimension: the last nonzero finite-difference order of the ball-volume sequence. For `A_p`, it equals `p`.

## 3. Primitive relation cut boundary

Let

\[
\Phi_p=\{e_i-e_j:i\ne j\},\qquad |\Phi_p|=p(p+1).
\]

After removing `B_p(r)`, define the directed cut boundary

\[
\partial_EB_p(r)=\{(x,\alpha):x\in B_p(r),\alpha\in\Phi_p,x+\alpha\notin B_p(r)\}.
\]

Let `E_p(r)` be its cardinality.

## 4. X02 — One directional cut is exactly a lower-dimensional ball

Fix an oriented primitive root

\[
\alpha=e_i-e_j.
\]

Let

\[
C_{p,\alpha}(r)=\{x\in B_p(r):x+\alpha\notin B_p(r)\}.
\]

Then

\[
\boxed{|C_{p,\alpha}(r)|=V_{p-1}(r).}
\]

### Bijection proof

Write `f(x)=sum_(x_k>0) x_k`. Adding `e_i-e_j` raises `f` by one exactly when

\[
x_i\ge0,\qquad x_j\le0.
\]

Therefore a crossing edge has

\[
f(x)=r,\qquad x_i\ge0,\qquad x_j\le0.
\]

Merge coordinates `i,j` into

\[
y_*=x_i+x_j
\]

and keep all other coordinates. The resulting `p` coordinates still sum to zero, so `y\in A_{p-1}`.

If `a=x_i>=0` and `b=-x_j>=0`, then

\[
d_G(0,y)=r-\min(a,b)\le r,
\]

hence `y\in B_{p-1}(r)`.

Conversely, given `y\in B_{p-1}(r)`, set

\[
t=r-d_G(0,y),\qquad c=y_*.
\]

The unique split

\[
x_i=\max(c,0)+t,
\qquad x_j=\min(c,0)-t
\]

recovers a crossing point. Thus the map is bijective. ∎

## 5. X03 — Exact cross-dimensional cavity-boundary identity

Every primitive direction contributes the same number of cut edges, therefore

\[
\boxed{E_p(r)=p(p+1)V_{p-1}(r).}
\]

In particular,

\[
\boxed{E_3(r)=12V_2(r)=12(3r^2+3r+1).}
\]

So in the `A_3/FCC` working model, each primitive direction sees exactly one complete two-dimensional `A_2` ball of the same radius across the cavity boundary. This is exact, not asymptotic.

Low-dimensional examples are

\[
E_1(r)=2,
\quad E_2(r)=6(2r+1),
\quad E_3(r)=12(3r^2+3r+1),
\]

and

\[
E_4(r)=20\frac{(2r+1)(5r^2+5r+3)}3.
\]

Direct integer enumeration checked the identity through `p=5` for several radii.

## 6. Repeated contraction as a second dimension detector

The coordinate merge associated with a primitive direction maps

\[
B_p(r)\to B_{p-1}(r).
\]

Repeating compatible contractions gives

\[
B_p(r)\to B_{p-1}(r)\to\cdots\to B_1(r)\to B_0(r),
\qquad V_0(r)=1.
\]

Define `dim_contract` as the number of such dimension-lowering contractions needed to reach one point. Then

\[
\boxed{dim_{growth}=dim_{contract}=p.}
\]

Dimension is therefore recoverable from two independent discrete operations rather than merely declared by coordinate count.

## 7. Pressure test against the finite-precision radial ball

For

\[
q_p(x)=\frac12\sum_i x_i^2,
\qquad D_p(x)=R_2(q_p(x)),
\]

a primitive step satisfies

\[
q_p(x+e_i-e_j)-q_p(x)=x_i-x_j+1.
\]

The crossing cost is position-dependent. Consequently the simple identity

\[
E_p(r)=p(p+1)V_{p-1}(r)
\]

does not hold for the collapsed-radial cavity; direct integer enumeration confirms this failure.

This exposes a real structural tension:

1. graph balls have exact cross-dimensional relation recursion but a finite-direction growth form;
2. collapsed-radial balls improve radial balance but acquire arithmetic shell oscillation and position-dependent cut costs;
3. P019 should therefore seek an interface between `relation structure` and `radial precision` rather than assume either one alone carries the full physical meaning.

## 8. Next work

- formalize the fixed-root bijection in Lean;
- implement cut-boundary reference operations and enumerate through higher `p`;
- study whether repeated contractions generate a natural face/incidence complex;
- derive a direction-dependent radial-boundary kernel from `K_m(s,E)`;
- compare graph-cavity and radial-cavity finite-precision isotropy;
- map edge-isoperimetric, root-polytope projection, and root-lattice growth prior art before any novelty claim.
