# Poincaré / 3-sphere recognition — corrected BRC arithmetic frontier

Status: `CURRENT HANDOFF / CORRECTED PRUNING THEOREMS + OPEN NON-CIRCULAR CLOSURE`
Research provenance: `EM-FREE-P3K7Q2` plus subsequent durable continuation
Prepared for successor researchers: `2026-09-09`

## 1. Current canonical source

Read this exact source before changing theorem strength or claiming novelty:

`awdawmip/chatgpt-global-knowledge@8acfeac504eee85f6fbb66018470ad233ef33ff7:knowledge/projects/enterprise-math/poincare-brc-normal-surface-arithmetic-observer-20260905.md`

It supersedes the *technical frontier* of the earlier handoff while preserving that earlier record as provenance. The current packet does **not** prove the Poincaré conjecture. It provides a corrected arithmetic pruning layer for normal/almost-normal recognition and isolates the remaining non-circular closure gap.

## 2. Mandatory correction: raw standard-coordinate chi=2 is not the useful observer

A closed triangulation has triangle-only vertex-linking normal 2-spheres. They satisfy the standard matching equations, have Euler characteristic 2, and are compatible with every quadrilateral-type branch. Therefore the original relaxed target

`standard matching equations + chi=2`

is algebraically valid for “some chi=2 normal vector exists” but inadequate for the recognition observer “non-trivial normal sphere exists”.

Bare quadrilateral projection removes vertex-link directions, but Euler characteristic does not descend through bare Q-coordinates because adding/removing a vertex link changes chi. A repair state is required.

## 3. Canonical Q repair states

Write standard coordinates as `x=(t,q)` with triangle part `t` and quadrilateral part `q`. For every global triangulation vertex choose one incident triangle coordinate declared zero in a canonical representative. The tuple of these choices is a repair state `tau`.

If several triangle coordinates vanish, one surface can belong to several repair states. Preserve this overlap as provenance. A branch is globally dead only after every possible repair state has been killed.

For one-vertex triangulations there are at most `4n` repair states, so the extra state layer is linear in the tetrahedron count.

## 4. Direct prime-local triangle elimination

Split the standard integer matching matrix as

`A=[T|Q]`

and the standard Euler row as

`e=(e_T,e_Q)`.

For repair state `tau`, let `G_tau` select the declared-zero triangle coordinates and set

`H_tau=[T;G_tau]`.

For an odd prime `p` where `H_tau` has full triangle-column rank over `F_p`, solve

`e_T = alpha T + mu G_tau  (mod p)`

and define

`d_{p,tau}=e_Q-alpha Q`.

Every integral standard matching solution in repair gauge `tau` then obeys

`chi(t,q)=d_{p,tau} q (mod p)`.

No rational section or denominator clearing is needed in this prime-local layer. Rank-dropping primes are simply bad for this interface and must not be used as if the formula were certified.

## 5. Corrected subtree-monotone modular certificate

Let `B` be the Q-matching matrix. At partial quadrilateral branch `beta`, retain the allowed columns `J_beta`, giving `B_beta` and the restricted Euler row `d_{p,tau,beta}`.

A canonical target sphere in repair state `tau` must satisfy the relaxed equations

`B_beta q=0`,

`d_{p,tau,beta} q=2 (mod p)`.

If

`d_{p,tau,beta} in rowspan_Fp(B_beta)`,

then every `q` in the kernel has Euler readout 0, contradicting target 2. Equivalently,

`rank(B_beta)=rank([B_beta;d_{p,tau,beta}])`.

This kills the state `(beta,tau)`.

A descendant only deletes more columns. The same row-dependence witness restricts to every descendant, hence the kill is subtree-monotone.

Maintain

`S_beta={tau : tau not yet killed by a certified observer}`.

Only

`S_beta=empty`

permits pruning the whole quadrilateral branch.

## 6. Exact integer/gcd and p-adic layer

For an exact rational/integer Euler row after a repair gauge, let

`L_beta=ker_Z(B_beta)`

and let `phi(q)` be the Euler-value homomorphism. Its image is

`phi(L_beta)=g_{beta,tau} Z`.

For target Euler value `2D_tau`, a necessary condition is `g != 0` and `g | 2D_tau`. Descendants have smaller integer kernels, so their image subgroup is contained in the parent image; for nonzero generators this gives

`g_parent | g_descendant`,

hence every `v_p(g)` is nondecreasing down the tree.

When `r=rank_Q(B_beta)` and the augmented row raises rank by one,

`g = Delta_{r+1}([B_beta;d_tau]) / Delta_r(B_beta)`

in terms of determinantal divisors. This composes directly with existing Smith/local-support and modular exact-linear-algebra machinery.

## 7. Euler coset code and branch mass

For fixed good `(p,tau)` define

`C_p(T)=rowspan_Fp(B)`

and affine coset

`E_{p,tau}=d_{p,tau}+C_p(T)`.

A residual `r=d-lambda B` is a static branch certificate. If the branch keeps coordinate set `J` and `r|_J=0`, that `(branch,tau)` state is dead.

Group coordinates into tetrahedron blocks of size three. If `z_i(r)` is the number of zero residual entries in block `i`, one residual covers exactly

`W(r)=product_i z_i(r)`

full labeled quadrilateral branches for one repair state.

Different residuals overlap. Their `W(r)` values may not be added unless an exact union representation retains certificate provenance.

## 8. Treewidth and stronger feasibility ladder

Optimizing a general coset representative is hard, but the Q-matching code is tetrahedron-local. For fixed prime `p`, if the triangulation dual graph has treewidth `k`, a factor-graph dynamic program yields a coarse exact bound of the form

`O(n * p^(6(k+1)) * poly(n))`

for the best single residual certificate. This is a fixed-parameter tractability statement in dual-treewidth for fixed `p`, not a global polynomial-time recognition claim.

After modular pruning, use the increasing-strength feasibility ladder:

1. real cone obstruction;
2. integer lattice / gcd / Smith / valuation obstruction;
3. affine-semigroup-hole obstruction.

Do not build the expensive third layer unless empirical survivors show that cone+lattice pruning leaves enough work to justify it.

## 9. Concrete implementation and QO extension

The current packet identifies Regina-compatible primitives: Q and standard matching matrices, the Euler row, existing quadrilateral validity branching, and immediate control triangulations including small `S^3`, Poincaré homology sphere, lens spaces, and hyperbolic examples.

Quadrilateral-octagon coordinates admit the same repair-state / finite-field elimination architecture after fixing the exceptional octagon type/location; the octagon contribution appears as an explicit linear correction. This is the natural almost-normal extension after the normal-sphere / 0-efficiency phase.

## 10. Non-abelian route: useful cross-check, not independent closure

Ordinary homology/SNF cannot distinguish `S^3` from the Poincaré homology sphere. A non-abelian observer remains useful.

However the general Zentner / Heusener–Zentner representation route uses geometrization in its theorem chain. It may serve as an algorithmic cross-check or non-sphericity certificate under those stated dependencies, but it **cannot** be presented as an independent Progress-Number-Theory proof of Poincaré.

## 11. Exact remaining Poincaré gap

Arithmetic observers can accelerate and certify parts of a correct 3-sphere-recognition search. They do not yet prove

`pi_1(M)=1 -> M=S^3`.

A genuinely independent Progress-Number-Theory route still needs a non-circular theorem connecting simple connectivity to existence and termination of the required normal/almost-normal recognition certificate. This bridge is OPEN and is now the highest mathematical-value follow-up.

## 12. Pachner / width boundary

Pachner reversibility still rules out a nonconstant scalar of the bare triangulation that strictly decreases under every nontrivial move. Promising questions are instead:

- how a local bistellar move transforms the Q-row code by extension/puncturing/shortening while retaining provenance;
- whether directed simplification can target lower dual-treewidth or lower arithmetic factor width.

No universal Pachner entropy or topological invariant is currently established.

## 13. Successor task map

- corrected Regina benchmark/integration of repair-state modular + exact gcd observers;
- exact theorem/certificate package and QO almost-normal adapter;
- non-abelian finite-field route strictly as dependent algorithmic cross-check;
- Pachner/Q-code transport and width route;
- highest-value non-circular simple-connectivity-to-recognition closure bridge.

All successors must cite this handoff and the exact canonical Global Knowledge source above. Old publication generations based on the raw-standard-coordinate observer are historical provenance only and must be superseded before execution.
