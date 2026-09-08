# #1162 — exact weighted-cycle roughness defect for the finite Basel readout

Status: RESEARCH_NOTE / EXACT FINITE ROUGHNESS DECOMPOSITION / NOT_PROMOTED
Researcher-ID: EM-DIRECT-B62D
Research-Mode: TASK_RESEARCH
Progress-Event-ID: 1162-exact-weighted-cycle-roughness-defect-20260908-b62d
Date: 2026-09-08

## 1. Motivation

The previous structural-roughness note bounded weighted-cycle inverse-spectrum readouts under small relative conductance perturbations. The user's correction calls for a stronger treatment when possible: retain the rough microstructure as an explicit repair coordinate rather than hide it inside a generic small-error term.

For the Basel/m=1 cycle readout this can be done exactly for arbitrary positive edge weights.

## 2. Weighted cycle and scale-free readout

Let a cycle have N vertices and positive edge resistances

`r_0,...,r_(N-1)>0`,

with total resistance

`S=sum_i r_i`.

Let `L(r)` be the corresponding weighted Laplacian with edge conductances `1/r_i`.

Define the scale-free finite inverse-spectrum readout

`beta_N(r)= 2 Tr(L(r)^+) / (N S)`.

If every resistance is multiplied by the same positive constant, `L^+` and S both scale by that constant, so `beta_N` is unchanged. Thus global edge-scale gauge is removed before measuring roughness.

## 3. Exact effective-resistance formula

For vertices separated clockwise by k edges from i, let

`a_(i,k)=r_i+r_(i+1)+...+r_(i+k-1)`

(indices modulo N).

The two complementary arcs have resistances `a_(i,k)` and `S-a_(i,k)` in parallel, hence the effective resistance is exactly

`R_(i,i+k)=a_(i,k)(S-a_(i,k))/S`.

For any connected weighted graph, the Kirchhoff index satisfies

`Kf=N Tr(L^+)`.

Summing over ordered pairs therefore gives

`beta_N(r)
 = (1/N^2) sum_i sum_(k=1)^(N-1) s_(i,k)(1-s_(i,k))`,

where

`s_(i,k)=a_(i,k)/S`.

No eigenvalue differentiation or continuum geometry is used.

## 4. Exact sum-of-squares roughness defect

Put normalized edge gaps

`g_i=r_i/S`,  `sum_i g_i=1`.

For each k define

`d_(i,k)=s_(i,k)-k/N`.

For fixed k,

`sum_i d_(i,k)=0`,

because every normalized edge gap appears in exactly k of the N cyclic k-edge arcs.

Since `phi(x)=x(1-x)` is quadratic,

`phi(k/N+d)=phi(k/N)+(1-2k/N)d-d^2`.

The linear terms cancel after summing over i. Hence exactly

`beta_N(r)=beta_N(uniform)-D_N(r)`,

with

`D_N(r)= (1/N^2) sum_i sum_(k=1)^(N-1) d_(i,k)^2 >=0`.

For the uniform cycle `g_i=1/N`,

`beta_N(uniform)=(N^2-1)/(6N^2)`.

Therefore

`beta_N(r)
 = (N^2-1)/(6N^2)
 - (1/N^2) sum_i sum_(k=1)^(N-1)
   [ (r_i+...+r_(i+k-1))/S - k/N ]^2`.

Equality with the uniform value holds iff `D_N=0`; the k=1 terms then force every `g_i=1/N`. Thus the uniform cycle is the unique maximizer of the scale-free inverse-trace readout among all positive weighted cycles with N vertices.

## 5. BRC meaning: explicit repair coordinate

The observer that keeps only `(N,S,beta_N)` loses the distribution of edge resistance. The exact defect `D_N` is a sufficient repair coordinate for the Basel/m=1 readout:

`beta_N + D_N = (N^2-1)/(6N^2)`.

This is a concrete instance of the account BRC rule that a coarse quotient must retain a repair coordinate when fiber constancy fails. Here the repair coordinate is positive and finite, but it was derived before any positive-mass collapse.

The theorem is much stronger than a small-eta perturbation estimate: edge roughness may be arbitrarily large as long as all resistances remain positive.

## 6. Exact interaction with integer refinement extraction

For any weighted cycles supplied at resolutions N and qN, define their exact defects `D_N` and `D_(qN)` as above. The standard two-scale Basel extractor applied to the rough readouts gives

`C_rough(N,q)
 = [q^2 beta_(qN)-beta_N]/(q^2-1)`.

Substituting the exact defect formula yields

`C_rough(N,q)
 = 1/6 - [q^2 D_(qN)-D_N]/(q^2-1)`.

Thus the failure of the finite Basel fixed point under rough refinement is not an unspecified error: it is exactly the transported roughness defect.

In particular the fixed coefficient `1/6` survives a rough refinement family iff

`q^2 D_(qN)=D_N`

for the compared scales. This is a finite checkable condition, not an infinitesimal smoothness assumption.

## 7. Concavity proof of uniform optimality

There is also a short finite convexity proof. `D_N>=0` already proves the claim, but conceptually define `B(g)=beta_N(g)` on the probability simplex of normalized gaps. Each summand `s(1-s)` is concave in the linear partial-sum variable s, so B is concave. B is invariant under cyclic rotation of g. Averaging all N cyclic rotations of any g gives the uniform vector. Jensen therefore gives

`B(uniform)>=B(g)`.

The explicit square formula identifies the exact gap to equality.

## 8. Relation to the unweighted finite Basel coefficient

For the uniform cycle `D_N=0`, so

`beta_N=(N^2-1)/(6N^2)`.

The derivative-free refinement projector then extracts `1/6` exactly. The current theorem says what happens when uniformity is relaxed: the same coefficient remains the uniform upper envelope, while every finite roughness contribution is retained in `D_N`.

The later classical angular calibration that turns `1/6` into `zeta(2)/pi^2` remains separately typed.

## 9. Next

1. Study how `D_N` transforms under declared integer subdivision rules for rough edges; do not assume it scales homogeneously.
2. Diagonalize the finite quadratic form `D_N` only as an optional compatibility readout and identify which coarse gap observables suffice to bound it.
3. Look for higher-m analogues: whether inverse-moment roughness admits finite positive repair tensors rather than unstable microscopic derivatives.
