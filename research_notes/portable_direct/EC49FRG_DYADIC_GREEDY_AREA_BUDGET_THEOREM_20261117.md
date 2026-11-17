# EC49FRG supplementary theorem — globally optimal dyadic area-refinement allocation

Status: `AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / NOT_REVIEWED`. Date 2026-11-17. Companions: [EC49FRG six-seam proof](EC49FRG_SIX_SEAMS_116_NODE_THEOREMS_20261117.md), [116-node verifier](EC49FRG_116_NODE_EXACT_GEOMETRY.py). Frozen BRC scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Precise model

Fix finitely many already Bellman-certified disjoint price intervals `[a_j,b_j]` in `[1,3]`. Their certified-interval strip-area *upper* enclosure is

```
K(x) = 7557 - 169*x > 0
D = 2185500
U(a,b) = D*(b-a)^2/(K(a)*K(b)).
```

An admissible dyadic refinement step replaces a **current leaf price interval** `[a,b]` by its arithmetic-midpoint children `[a,m],[m,b]`, `m=(a+b)/2`. Starting from the finite initial intervals, perform exactly `M>=0` such steps. Minimize the **sum of U over the resulting leaves**. All endpoints and inserted midpoints are exact rational numbers whenever initial endpoints are rational.

## Theorem

For every finite initial interval family and every nonnegative integer budget M, **splitting the current leaf with largest U at each step is globally optimal** for the final total strip-area enclosure among all M-step dyadic refinement sequences. Equivalently, select at each step the current largest ratio `K(a)/K(b)`. Ties may be resolved arbitrarily. The optimum reduction is the sum of the M largest feasible tree-node split gains, which in this particular model are `U(node)/2`.

### Proof

First, the affine-K midpoint identity from the companion theorem gives

```
U(a,m)+U(m,b) = U(a,b)/2.
```

So splitting `I=[a,b]` decreases the global area enclosure by exactly `U(I)/2`. Write `u=K(a),v=K(b),c=K(m)=(u+v)/2`, with `0<v<c<u`. The child-to-parent ratios are

```
U(a,m)/U(a,b) = v/(4*c) < 1/4,
U(m,b)/U(a,b) = u/(4*c) < 1/2.
```

Thus **every descendant split gain is strictly smaller than every gain on its ancestor chain**.

Imagine the countable binary forest of all potential midpoint splits growing from the original price intervals. A feasible M-step refinement is precisely a set of M forest nodes that is closed under ancestors. The sum of its gains equals its reduction in total enclosure area. Since descendants have strictly smaller gains than their ancestors, an M-element set of globally largest node gains can be chosen ancestor-closed, hence feasible. Equivalently, when an unexposed descendant has a large remaining gain, its unsplit visible ancestor has a strictly larger one; the largest remaining gain is therefore always among currently splittable leaves. The greedy algorithm successively takes it. Induction on M proves global optimality.

Finally, write `r=K(a)/K(b)>1`. Because `K(a)-K(b)=169(b-a)`,

```
U(a,b) = (D/169^2)*(r + 1/r - 2).
```

The derivative of `r+1/r-2` is `1-1/r^2>0` for `r>1`, so maximizing U is exactly equivalent to maximizing the ratio r. QED.

## Application and scope

Applied to EC49FRF's verified 110-node anchor grid and M=6, the largest-ratio recurrence selects, in order,

```
[13/8,53/32]  -> 105/64
[51/32,13/8]  -> 103/64
[25/16,51/32] -> 101/64
[49/32,25/16] -> 99/64
[3/2,49/32]   -> 97/64
[137/48,23/8] -> 275/96.
```

All six inserted price nodes have independent native BRC Bellman certificates and were checked by the separate weighted-subset implementation. The resulting area enclosure is

```
S116 = 353039202146480393615/236644210143071463572064.
```

Therefore this 116-node grid **globally minimizes the sum of strip-area enclosures among all six-step arithmetic-midpoint refinement plans starting from this 110-node grid**, with fixed already-certified initial points.

The optimization domain here is the **fixed midpoint-only dyadic refinement family**. The earlier EC49FRF theorem optimizes arbitrary real insertions and allows re-spacing of nodes to equal-log-K positions; those are separate comparison classes. A minimized *enclosure* is not a proof that the underlying BRC policy is optimal on the remaining strips. This supplementary theorem has an elementary complete proof, but no independent project review/admission.