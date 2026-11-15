# PREFIX-812 — Residual reachability is invariant throughout a fixed bounded named-source fiber

**Date:** 2026-11-15 (Asia/Shanghai). **Role/scope:** research6 independent auxiliary BRC named-source calculation; preserved scientific input pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`. **Predecessor:** PREFIX-809 cycle connectivity and PREFIX-811 residual-SCC observer-difference lattice. This note does not assert a new native X6 event or shared-task CLAIM.

## 1. Objects and exact statement

Let `G=(U,V,E)` be a finite bipartite **named multigraph**. Parallel edges retain their separate names and integer capacities `K_e >= 0`. Fix an integral row/column margin vector `b`, and let

```
F(b,K) = {x in Z^E : Bx=b, 0<=x_e<=K_e for every named edge}.
```

Assume `F(b,K)` is nonempty. For each `x in F(b,K)`, make its directed residual graph `D_x`: edge `e=(u,v)` contributes `u->v` if `x_e<K_e` and `v->u` if `x_e>0`. Both arcs may be present; retain parallel-arc identities. Write `u =>_x v` for the reachability relation, including length-zero paths.

**Theorem 812.1 (whole-relation invariance).** For **any** `x,y in F(b,K)` and **all** vertices `u,v in U union V`,

```
u =>_x v  iff  u =>_y v.
```

Consequently every feasible table has the same residual SCC partition and the same SCC condensation DAG (including its named inter-SCC arcs). In addition, if the endpoints of a named edge lie in different residual SCCs at one feasible table, then its integer count `x_e` is **constant on the whole fiber**.

### Proof

Fix `x,y` and write `d=y-x`. For each edge with `d_e>0`, take `d_e` copies of the forward residual arc `u->v` in `D_x`. For each edge with `d_e<0`, take `-d_e` copies of the reverse residual arc `v->u` in `D_x`. These arcs exist by the capacity inequalities. Because `Bd=0`, these copies form a nonnegative **integral directed circulation**. Decompose it into directed cycles, respecting named arcs, including 2-cycles from parallel edges if present.

Consider a residual arc `a:p->q` present at `x` but absent at `y`. If `a` is forward, then `x_e<K_e=y_e`, so `d_e>0`; if `a` is reverse, then `x_e>0=y_e`, so `d_e<0`. In either case a copy of `a` belongs to one of the difference-circulation cycles `C`.

Every used arc of `C` has its **oppositely directed named residual arc** present at `y`: for `d_e>0`, `y_e>0`; for `d_e<0`, `y_e<K_e`. Therefore, omitting the reverse of `a` and following the reverse of the *rest* of the cycle yields a directed path `p =>_y q`. This is valid also for a 2-cycle. All `D_x` arcs retained at `y` are already valid steps, so replacing each lost arc in a `D_x` path by its alternate `D_y` path proves `u =>_x v` implies `u =>_y v`. Interchange `x,y` for the reverse implication.

The mutual reachability relation is therefore invariant, hence so is the SCC partition. If `x_e\ne y_e`, the corresponding oriented arc was used in the difference circulation and lies on a directed cycle in `D_x`. Thus its endpoints lie in the **same** SCC. Contraposition proves inter-SCC edge counts are fixed. Since their residual forward/backward arc presence depends only on these fixed counts and capacities, their exact named inter-SCC arcs and the condensation DAG are invariant. QED.

**Corollary 812.2 (zero-rebuild observer-lattice maintenance).** Fix also an integer observer matrix `A`. For one fixed `(G,K,b,A)`, PREFIX-811's residual-SCC observer-difference subgroup and its congruence certificate can be computed **once** from one feasible seed and reused for every feasible table visited by any admissible cycle updates. No SCC reconstruction or lattice recomputation is required between these states. If an algorithm additionally tracks the current observer output `Ax`, a unit cycle update changes it by the exact signed column sum of that cycle, using `O(k|C|)` integer additions for `k` observers and a cycle of length `|C|`. The statement concerns cache maintenance after initial construction, not the cost of finding the seed or of optimizing an observer.

## 2. Boundary when the fiber itself changes

Fixing a *new* named edge, changing any capacity or changing the margins defines a **different** fiber, so its residual relation may change. Exact 2x2 witness: with four unit-capacity edges and row/column margins `(1,1)`, both feasible tables are

```
x=(1,0,0,1),  y=(0,1,1,0)
```

(row-major named order). Their full residual graph has one SCC containing all four vertices. If edge `(0,0)` is newly pinned to value 1 and removed from the movable graph, only `x` remains feasible; the residual graph on the other three edges has four singleton SCCs. Thus a pin event requires applying the theorem to the **new** fiber (or an independently justified dynamic-deletion scheme).

For the scalar observer `W(z)=z_{00}+z_{11}`, the two full-fiber values are `2,0`, illustrating that SCC invariance certifies a fixed **difference lattice**, not a constant observer value.

## 3. Executed exhaustive integer regression

The attached JavaScript checker enumerates every capacity vector in each declared finite suite, every integer named-source table `0<=x_e<=K_e`, and every realized margin fiber. For each fiber it compares each table's complete directed reachability Boolean matrix against the first table's, and checks that every cross-SCC named edge retains its integer value. This is an exact full enumeration **within these suites**. No floating-point arithmetic, random sampling or external libraries are used.

| Named graph / capacities | Capacity patterns | Realized margin fibers | Tables | Beyond-first comparisons | Reachability-bit equalities | Cross-SCC value checks |
|---|---:|---:|---:|---:|---:|---:|
| Complete 2x2; each capacity 0,1,2 | 81 | 1,215 | 1,296 | 81 | 1,296 | 0 |
| Complete 2x3; each capacity 0,1 | 64 | 704 | 729 | 25 | 625 | 42 |
| Complete 3x3; each capacity 0,1 | 512 | 17,840 | 19,683 | 1,843 | 66,348 | 6,885 |
| 2x2 with two distinct parallel (0,0) edges; each capacity 0,1 | 32 | 212 | 243 | 31 | 496 | 75 |
| **Total** | **689** | **19,971** | **21,951** | **1,980** | **68,765** | **7,002** |

There are 1,589 multi-table fibers. The checker also confirms the 2x2 cycle-flip reachability and the pinning witness (SCC count changes from 1 to 4). Output: `ALL_EXACT_ASSERTIONS_PASSED`. General validity follows from Theorem 812.1's proof; the regression independently checks enumerated domains.

Files: `PREFIX812_R6_RESIDUAL_REACHABILITY_CHECK.js` and `PREFIX812_R6_RESIDUAL_REACHABILITY_RESULTS.json`.

## 4. Provenance, scope and next problem

Mathematical sources: this note's constructive difference-circulation proof; previously published PREFIX-809 and PREFIX-811. No external literature priority claim is made. This is a theorem about finite named-source integer transportation fibers, an auxiliary BRC source model. P000's six native spatial axes, independent time dimension, three-dimensional research slice and provenance-preservation requirements are unchanged; the native Cell/Link/Port event interpretation remains a separate typed mapping problem.

**Next experiment:** analyze a single new named-edge pin, capacity decrease or margin change: compare dynamically updating affected SCCs and observer-difference congruence generators with full recomputation; identify explicit instances where a pin splits one SCC into several, and measure full input-conversion, certificate and update costs. Test whether a declared observer family is preserved by a specified native X6 sequence of typed events before using this auxiliary invariant as an event-level statement.

**Evidence status:** `AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`. This standalone research material does not claim a shared Task/CLAIM/Result/Review.
