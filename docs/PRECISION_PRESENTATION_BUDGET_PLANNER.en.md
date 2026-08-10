# Exact Budget Planner for Literal-Macro Presentations

Status: `RESEARCH BRIDGE / NONCANONICAL`

The parent presentation theorem gives the forward map

`macro depth d -> (stored rules, execution blocks)`.

This generation solves the inverse engineering problem: given a latency/depth budget or a storage budget, choose the Pareto-efficient exact presentation inside the same literal macro-table class.

## 1. Forward laws

For k generator actions, macro depth d and declared word horizon h:

`S(k,d)=sum_(i=1)^d k^i`

stored literal transition macros, and

`D(h,d)=ceil(h/d)`

worst-case macro executions.

S is strictly increasing in d; D is nonincreasing and piecewise constant.

## 2. Execution-depth budget -> least storage

Suppose at most R macro executions are allowed.

The exact condition is

`ceil(h/d)<=R`.

Therefore the least feasible macro depth is

`d_min=max(1,ceil(h/R))`.

Because S(k,d) increases strictly with d, this d also gives the least rule storage among all literal presentations satisfying the execution budget.

Hence

`B_rules_min(k,h,R)=S(k,ceil(h/R))`

with the generator-depth1 floor when R>=h.

## 3. Storage budget -> minimum execution depth

Given rule budget B, first find the largest affordable depth

`d_max=max{d<=h:S(k,d)<=B}`.

This determines the best achievable runtime

`R_min=ceil(h/d_max)`.

However d_max need not itself be Pareto-efficient because D can be flat across several d values.

The correct presentation is the **smallest** d attaining R_min:

`d_Pareto=ceil(h/R_min)`.

This minimizes storage among all presentations with the best execution depth affordable under B.

## 4. Sharp dominated-depth example

Take k=2,h=12,B=125.

The budget can afford d=5 because

`S(2,5)=62`.

But

`D(12,5)=3`

and already

`D(12,4)=3`

with only

`S(2,4)=30`

stored rules.

So d=5 is storage-dominated. The planner correctly returns d=4,30 rules,3 execution blocks, leaving95 units of unused rule budget.

This shows why “use the largest affordable macro” is not the correct inverse optimizer.

## 5. Horizon-only Pareto depth theorem

Because S(k,d) is strictly increasing for every k>=1, whether one depth dominates another depends only on D(h,d), not on k.

The complete nondominated depth set is

`D_h={ceil(h/r): r=1,...,h}`.

The action count k changes the storage coordinate attached to each depth but not which depths survive Pareto elimination.

For h=12:

`D_h={1,2,3,4,6,12}`.

This recovers the parent's scanned frontier for every tested action count.

## 6. Frontier size is sublinear in horizon

Since

`ceil(h/r)=floor((h-1)/r)+1`,

the standard distinct-quotient argument gives only O(sqrt(h)) distinct Pareto depths.

A simple bound used by the executable layer is

`|D_h| <= 2 floor(sqrt(h-1)) + 1`

for h>1.

Thus even though there are h candidate macro depths, the exact nondominated resource menu is much smaller.

## 7. Dense scalar-storage budget

For a b-dimensional dense transition state, one macro matrix costs b^2 scalars.

Therefore scalar budget B_s corresponds to rule budget

`floor(B_s/b^2)`.

The same inverse planner then returns the Pareto-optimal macro depth and execution count.

## 8. Same latency: state compression has an exact square storage law

To meet execution budget R, the required macro depth and rule count do not depend on state dimension. Hence

`B_scalar_min = b^2 S(k,ceil(h/R))`.

If an exact representation change reduces state dimension from b to r, the scalar storage needed for the **same latency target** changes by exact ratio

`r^2/b^2`.

This is a direct composition of the state-representation and macro-depth axes.

## 9. Same storage: state compression can buy execution depth

Under one fixed scalar budget, a smaller state dimension increases the affordable rule budget and can cross a macro-depth threshold.

Example k=2,h=12,scalar budget1000:

- dimension4: at most62 rules; Pareto plan d=4,3 execution blocks,480 stored scalars;
- dimension2: at most250 rules; Pareto plan d=6,2 execution blocks,504 stored scalars.

So exact state compression can convert the same memory ceiling into lower runtime depth.

## 10. Weighted-fan consequence

The previous weighted-fan theorem changed an exact terminal-trace representation from11 discrete branching coordinates to2 linear predictive coordinates.

For any fixed literal-macro latency target, dense matrix storage changes by

`2^2/11^2 = 4/121`.

This does not mean the two-dimensional representation is semantically sufficient for the stronger branching interface; it applies only where the terminal-linear predictive state satisfies the declared task.

## 11. Exact optimizer status

The executable layer verifies the inverse planner against brute-force enumeration over small action counts, horizons and frontier-adjacent budgets.

It explicitly uses lexicographic Pareto intent:

1. under a storage budget, minimize execution blocks;
2. among equal-runtime presentations, minimize stored rules.

This prevents hidden dominated points.

## 12. Representation-class boundary

All formulas are exact only inside the literal contiguous-macro table class.

Binary-power macros, addition chains, algebraic normal forms, circuits and shared DAGs can create a different frontier. The next generation deliberately pressure-tests that boundary.

## Owner-local assets

- `presentation_budget_planner.py` / tests;
- `presentation_budget_frontier.py` / tests;
- `PRECISION_PRESENTATION_BUDGET_PLANNER.{en,zh}.md`.

## Prior art / status

Time-memory tradeoffs, inverse resource planning and divisor-quotient frontier compression are standard prior mathematics/CS. The project value is the exact inverse compiler and the coupling to semantic state-representation cost.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.