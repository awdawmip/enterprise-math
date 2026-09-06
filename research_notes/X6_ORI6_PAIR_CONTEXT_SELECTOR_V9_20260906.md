# X6 rotation V9: symmetry obstruction for odd events and minimal pair-context repair

Status: `FREE_RESEARCH / EXACT EQUIVARIANCE NO-GO + CONDITIONAL EXTENSION / NOT_FOUNDATION`
Date: `2026-09-06`
Researcher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Tasks: `RS-X6-NATIVE-ROTATION-DYNAMICS`, `RS-X6-UPPER-STRUCTURE-INTEGRATION`
Depends on:
- `X6_FULL_INTEGRAL_ISOMETRY_AND_ORI6_GATE_V7_20260906.md`;
- `X6_ORI6_EVENT_CHARGE_AND_OBSERVER_BOUND_V8_20260906.md`;
- `X6_BRANCH_SELECTOR_CONTEXT_NOGO_V3_20260906.md`.
Checker: `experiments/x6_ori6_pair_context_v9_20260906/check_ori6_pair_context.py`.

## 1. Question

V8 shows that current dynamics preserves `Ori_6` and that one new odd-positive-permutation frame event would algebraically connect the full integral isometry group.

That still leaves a symmetry question:

> can a deterministic odd event be selected from a completely axis-symmetric state without adding any relation/context that distinguishes axes?

The answer is no. The first simple axis-subset context that can select an odd event equivariantly is an unordered pair of axes.

## 2. No-context equivariant selector no-go

Let `A6` act on candidate frame updates by conjugation. A state/context carrying no axis distinction is fixed by all `A6` relabelings.

An `A6`-equivariant deterministic event selector from this one-point context would therefore have to output a frame element `g` satisfying

`h g h^-1 = g`

for every `h in A6`.

Thus `g` must lie in the centralizer `C_{S6}(A6)`.

Exact group calculation gives

`C_{S6}(A6)={1}`.

In the signed frame group the centralizer of embedded positive `A6` adds only the global sign inversion `-I`; both central elements have trivial positive-axis permutation and hence `Ori_6=0`.

Therefore no fully `A6`-symmetric deterministic rule can select an `Ori_6=1` frame event without additional symmetry-breaking/context data.

This is an equivariance no-go, not a statement that odd events are impossible once extra context is supplied.

## 3. One distinguished axis is still insufficient

Now let the context distinguish one native positive axis `i` but no other axis.

At a reference axis `i=1`, the stabilizer inside `A6` is an `A5` acting transitively on the other five axes. An equivariant deterministic selector at this context must commute with that stabilizer.

The centralizer in `S6` is again trivial:

`C_{S6}(A5_stab(1))={1}`.

So one distinguished axis does not suffice to select a positive-permutation-odd frame event equivariantly.

In the signed group one can additionally attach sign flips constant on stabilizer orbits, but these do not change positive-axis permutation parity. `Ori_6` still cannot flip.

## 4. An unordered axis pair is sufficient

Let the context distinguish one unordered pair

`P={i,j}`.

The canonical frame update

`F(P)=(i j)`

that transposes the two axes and fixes the other four is odd.

It is `A6`-equivariant:

`F(hP)=h F(P) h^-1`.

At the reference pair `{1,2}`, the `A6` stabilizer has order 24 and its centralizer in `S6` is exactly

`{1,(1 2)}`.

Thus the pair transposition is the unique nontrivial deterministic permutation update compatible with that pair context and the residual symmetry.

Among contexts consisting only of one distinguished **unordered subset of axes**, the minimum subset size supporting such an equivariant odd selector is therefore exactly two:

- size 0: no odd selector;
- size 1: no odd selector;
- size 2: transposition selector exists.

There are `C(6,2)=15` possible pair contexts, forming one `A6` orbit.

## 5. This pair context is not a primitive two-force balance

P000 still states that a primitive nonzero stable force balance has arity three and that a two-force apparent equilibrium is nonprimitive.

The unordered pair `P={i,j}` here is **frame-control/event context** only. It says which two positive-axis labels a hypothetical `Ori_6`-changing frame event would exchange.

It must not be retyped as a stable two-force atom.

The present theorem neither weakens nor derives the P000 force-balance axiom.

## 6. Static pair swap path cost on X6

Let `P_{ij}` swap signed coordinate components `i` and `j` while fixing the rest. For a spatial state `x`,

`P_{ij}x-x = (x_j-x_i)e_i + (x_i-x_j)e_j`.

Write

`d=|x_i-x_j|`.

Then the minimum primitive Cell-transition count between `x` and `P_{ij}x` is

`N_min=2d`,

and the exact shortest-path multiplicity is

`B_min=C(2d,d)`.

Hence even after the odd frame update is selected, a generic moved Cell still has a nontrivial BRC path fiber.

If `x_i=x_j`, the spatial Cell is fixed by the pair swap even though the global frame update has `Ori_6=1`. Therefore spatial displacement/path data alone cannot certify that an odd frame event occurred.

## 7. Binary shared-midpoint criterion is not enough to select a path law

Consider the two unit shell tokens

`e_i -> e_j`

and

`e_j -> e_i`

under the pair swap.

Each path has two shortest realizations:

- INNER via pivot `0`;
- OUTER via `e_i+e_j`.

For the two-token joint event there are four branch combinations. Exactly two have a shared midpoint:

`II` shares the pivot,

`OO` shares the nonzero outer Cell.

Thus the criterion

`BOTH TOKENS MEET AT ONE INTERMEDIATE CELL`

still leaves two branches.

This sharply contrasts with the canonical three-token atomic triadic scatter, where the common-midpoint criterion selects exactly one joint branch `III` out of eight.

The result is a path-level **nonuniqueness of a binary pair-swap event law**, not a proof of the P000 two-force instability axiom.

## 8. Odd frame selection and path selection are two distinct gates

The current `Ori_6` extension problem therefore has at least two independent steps.

### Frame-context gate

Need a relation/context capable of selecting one charge-one static frame element. An unordered axis pair is the smallest native axis-subset context giving a canonical equivariant transposition normal form.

### Path/event-law gate

After the frame element is chosen, one still needs a law selecting/weighting concrete Cell-path realizations. The pair context alone does not choose INNER versus OUTER, even under a shared-midpoint requirement.

Therefore

`ODD FRAME ADMISSIBILITY != ODD EVENT DYNAMICS COMPLETE`.

This mirrors the earlier force-vs-phase branch-selector no-go: event semantics remain necessary above static frame geometry.

## 9. Normal-form significance

V8 proves every odd integral frame isometry lies in one double coset

`R_triad o R_triad`.

Choosing a pair transposition `(i j)` therefore supplies a particularly simple normal-form representative of the entire odd static sector.

If any odd physical event is eventually admitted, pre/post current triadic frame dynamics can algebraically synthesize all other odd static frame maps from one representative class.

Their concrete path costs and internal/event contexts need not be equivalent, so this is only an algebraic normal-form result.

## 10. Current minimal unresolved physical input

The remaining `Ori_6` question is now narrower than “find the missing rotation group”. The static group is closed.

A minimal constructive extension would require:

1. a physical/internal relation that supplies an axis-pair-like symmetry-breaking context (or another context of equivalent strength);
2. a rule admitting the corresponding charge-one frame update;
3. a concrete Path/BRC branch law for the moved Cell population;
4. event-time and internal/channel coupling rules;
5. an observer bridge explaining whether and how the event is detectable.

Without item 1, full `A6` symmetry forbids a deterministic odd selector. With item 1 alone, the path law is still underdetermined.

## 11. Verification

The exact checker verifies:

- `C_{S6}(A6)={1}`;
- one-axis stabilizer `A5` also has trivial centralizer in `S6`;
- an unordered pair stabilizer has centralizer `{1,(ij)}`;
- all 15 pair-transposition assignments are `A6`-equivariant;
- pair-swap X6 path count formula `2d` and shortest multiplicity `C(2d,d)` on exact examples;
- the two-token common-midpoint branch set is exactly `{II,OO}`.

No physical admission of odd events or Foundation promotion is made.
