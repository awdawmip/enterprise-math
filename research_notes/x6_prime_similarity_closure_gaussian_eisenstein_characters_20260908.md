# X6 prime similarity closure periods, Gaussian triple charts, and the Eisenstein character bridge

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / natural-number geometry / Nollm cross-observer arithmetic`
Parents:
- `research_notes/x6_minimal_two_defect_frame_triadic_closure_20260908.md`
- `research_notes/nollm_hecke_radix_multiplicative_field_sync_20260908.md`
- `research_notes/nollm_hecke_tree_zeta2_thickness_bridge_20260908.md`
EM source snapshot before write: `awdawmip/enterprise-math@85be5544200d86075069442727fa2adc2df05d29`

## 0. Question and strength

The binary case proved that three pair-supported determinant-2 events can close at index 8 to exact X6 isotropy and that their centered strain defects form a 120-degree zero-sum triad.

This continuation asks the next exact question:

> For an arbitrary prime p, at what smallest power `p^k` can an integer X6 transport become strictly isotropic, and when does the binary three-pair mechanism generalize?

The answer gives a sharp arithmetic split.

Define the **strict X6 prime similarity closure exponent**

`tau_X6(p)`

as the least positive k for which there exists an integer full-rank matrix A with

`|det A|=p^k`

and

`A^T A = q I_6`

for some positive integer q.

Then:

`tau_X6(2)=3`,

and for odd primes

`boxed: tau_X6(p)=3 if p == 1 (mod 4),`

`boxed: tau_X6(p)=6 if p == 3 (mod 4).`

Thus the mod-4 quadratic character is exactly recoverable from the first strict-isotropy closure period in this model.

This is an exact arithmetic/geometry theorem under the declared X6 integer-quadratic transport model. It is not a claim that strict isotropic similarity is the unique physical selection rule.

## 1. Determinant gate: only multiples of three can close

Suppose

`A^T A=q I_6`

and

`|det A|=p^k`.

Taking determinants gives

`p^(2k)=q^6`,

or equivalently

`p^k=q^3`.

Since q is a positive integer,

`3 | k`

and

`q=p^(k/3)`.

Therefore the first possible exponents are

`k=3,6,9,...`.

This cube gate is independent of the prime class.

## 2. Exact closure at p^3 is equivalent to A^T A=p I_6

For k=3 the determinant relation forces

`q=p`.

Hence p^3 closes strictly isotropically iff there exists

`A in M_6(Z)`

with

`A^T A=p I_6`.

For p=2, the parent note gives the explicit block construction

`diag(C2,C2,C2)`,

where

`C2=[[1,-1],[1,1]]`

and

`C2^T C2=2 I_2`.

The odd-prime classification is next.

## 3. Sufficiency for p == 1 mod 4: three Gaussian pair planes

If an odd prime satisfies

`p == 1 (mod 4)`,

Fermat's two-square theorem gives integers a,b with

`p=a^2+b^2`.

Define the 2x2 Gaussian multiplication block

`B_p=[[a,-b],[b,a]]`.

Then exactly

`B_p^T B_p=p I_2`,

`det B_p=p`.

On any perfect matching of the six native axes, put one such block on each of the three disjoint pair planes. The resulting 6x6 integer matrix A satisfies

`A^T A=p I_6`,

`|det A|=p^3`.

Therefore

`p == 1 (mod 4) -> tau_X6(p)=3`.

The same centered-strain directions as in the p=2 case occur; only their amplitude changes from `ln 2` to `ln p`.

Thus all Gaussian-split primes share the same exact 15-direction pair-support / 120-degree defect geometry at the Gram/strain observer.

## 4. Necessity for odd p: a three-dimensional totally isotropic space mod p

Assume now that an odd prime p admits

`A^T A=p I_6`.

First determine the rank of A modulo p.

From

`A^T A=p I_6`

we have

`A^{-1}=A^T/p`.

Hence `p A^{-1}` is integral. In Smith normal form every invariant factor of A therefore divides p.

But

`|det A|=p^3`.

So the six Smith factors consist of exactly three 1's and three p's.

Consequently

`rank_Fp(A mod p)=3`.

Let W be the three-dimensional column space of `A mod p` in `F_p^6`.

Reducing

`A^T A=pI`

modulo p gives

`A^T A=0`.

Therefore every pair of vectors in W is orthogonal for the standard six-square bilinear form, including each vector with itself. Thus W is a three-dimensional totally isotropic subspace.

So the standard nondegenerate quadratic space

`q_6=x_1^2+...+x_6^2`

over `F_p` must have Witt index 3, i.e. it must be split hyperbolic of dimension 6.

## 5. The Witt/discriminant obstruction is exactly -1 being a square

A split six-dimensional quadratic space is a sum of three hyperbolic planes. Its determinant square class is

`(-1)^3 = -1`.

The standard six-square form has determinant square class 1.

Therefore it is split iff

`-1`

is a square in `F_p`.

For odd primes this is equivalent to

`p == 1 (mod 4)`.

Hence

`A^T A=pI_6 -> p == 1 (mod 4)`.

Combining with the explicit Gaussian construction:

`boxed: for odd prime p, A^T A=pI_6 has an integral solution iff p == 1 (mod 4).`

This rules out every p^3 strict-isotropy closure for primes `p==3 mod4`, including any hypothetical indecomposable six-dimensional construction; the obstruction is not merely failure of a chosen 2x2 factorization.

## 6. Inert primes first close at p^6

If

`p == 3 (mod 4)`,

k=3 is impossible by the theorem above.

The next determinant-allowed exponent is k=6.

It is always realized trivially by

`A=p I_6`.

Then

`A^T A=p^2 I_6`,

`|det A|=p^6`.

Therefore

`boxed: tau_X6(p)=6 for p == 3 (mod 4).`

No exponent between 3 and 6 is possible because strict-isotropy exponents must be multiples of three.

Thus the period dichotomy is exact and minimal.

## 7. Closure-period character

For odd primes define the usual quadratic character

`chi_-4(p)=+1 if p==1 mod4`,

`chi_-4(p)=-1 if p==3 mod4`.

Then the X6 strict-isotropy closure exponent is exactly

`tau_X6(p)=3` when `chi_-4(p)=+1`,

`tau_X6(p)=6` when `chi_-4(p)=-1`.

Equivalently

`tau_X6(p)/3 = 2^((1-chi_-4(p))/2)`.

So within this geometric observer, the Dirichlet character mod 4 is not inserted as a label: it is read out from the first possible exact similarity closure period.

Strength boundary: this is a representation of `chi_-4` by the declared X6 similarity dynamics, not a new theorem about Dirichlet L-functions.

## 8. Exact support-rank explanation of the 3-versus-6 split

There is a second local derivation.

Suppose a determinant-p event is identity outside a k-dimensional coordinate support and is strictly isotropic on that support:

`B^T B=q I_k`,

`|det B|=p`.

Then

`p^2=q^k`.

Because p is prime and q is an integer, k must divide 2. Thus only

`k=1` or `k=2`

are possible.

- `k=1`: `B=[p]`, always available, but it loads only one axis and requires six disjoint axis events to cover X6 isotropically; total index `p^6`.
- `k=2`: `q=p`, requiring an integral 2x2 matrix with `B^T B=pI_2`, equivalently p is a sum of two squares; for odd primes this is exactly `p==1 mod4`. Three disjoint pair events cover X6; total index `p^3`.

Hence the split/inert closure arity can be read as

`GAUSSIAN-SPLIT PRIME -> EXACT RANK-2 EVENT -> 3-EVENT X6 CLOSURE`,

`GAUSSIAN-INERT PRIME -> NO EXACT RANK-2 EVENT -> RANK-1 FALLBACK -> 6-EVENT CLOSURE`.

The global Witt theorem shows that an inert prime cannot evade this by an indecomposable p^3 six-dimensional similarity.

## 9. Pair-plane branches for split primes have a two-point phase fiber

Fix `p==1 mod4` and choose a square root

`r in F_p`, `r^2=-1`.

On an ordered native axis pair `(i,j)`, define the index-p branch

`L_(i,j;r)={x in Z^6 : x_i + r x_j ==0 (mod p)}`.

A Gaussian multiplication block of norm p has exactly such a projective left-kernel condition modulo p.

Reversing the pair orientation changes r to

`r^(-1)=-r`.

Thus on one unordered support pair `{i,j}` there are two conjugate projective branches, corresponding to the two roots `+r,-r` of -1.

Consequently a Gaussian-split odd prime has

`15 * 2 = 30`

pair-supported exact conformal index-p branches.

Under S6 the two signs are exchanged by swapping the two axes, so the 30 branches form one S6 orbit when pair orientation is included.

At the Gram/centered-strain observer the two phase branches collapse to the same defect direction. Their phase/conjugation identity must be retained if future transport composition can see it.

For p=2 the two roots coincide modulo 2, so the sublattice branch fiber collapses, although orientation/transport representatives can still remain distinct above that observer.

## 10. Fifteen Gaussian triple charts on X6

A perfect matching

`M={{i1,j1},{i2,j2},{i3,j3}}`

partitions the six signed coordinate axes into three 2-coordinate blocks.

After choosing an orientation in each pair, the underlying abelian coordinate lattice can be written as

`Z^6 ~= Z[i]^3`

by

`(x_i1,x_j1,...)->(x_i1+i x_j1, x_i2+i x_j2, x_i3+i x_j3)`.

This is a computational/metric chart induced by the admitted sum-of-six-squares component norm. It does **not** redefine P000's native right angle as a classical 90-degree angle.

There are 15 perfect matchings, hence 15 such unordered Gaussian triple charts related by S6.

Inside one chart, a Gaussian-split prime event is multiplication by a norm-p Gaussian integer on one component. Applying norm-p multiplication on all three components gives the p^3 isotropic closure.

The three centered component-scale defects live in the two-dimensional zero-sum plane

`{(t1,t2,t3):t1+t2+t3=0}`

and are proportional to

`(2,-1,-1)`, `(-1,2,-1)`, `(-1,-1,2)`.

They are equal norm, pairwise 120 degrees, and sum to zero.

So one X6 perfect-matching chart has a nested structure:

`THREE GAUSSIAN PAIR PLANES -> A2-LIKE 120-DEGREE CENTERED STRAIN PLANE`.

This is an observer hierarchy, not an identification of Gaussian and Eisenstein coordinate rings.

## 11. Ordered oriented matchings form an S6 torsor

Define a **full pair frame** to be an ordered list of three ordered pairs

`((i1,j1),(i2,j2),(i3,j3))`

using every axis label exactly once.

Such a frame is exactly the same data as a permutation

`(i1,j1,i2,j2,i3,j3)`

of the six axes.

Hence there are

`6! = 720`

full pair frames, and S6 acts freely and transitively on them.

Therefore the set of oriented/ordered pair frames is an S6 torsor: there is no distinguished canonical frame, but carrying one frame as state preserves covariance under relabeling.

For a split odd prime:

- orientation within each pair chooses one of the two conjugate `sqrt(-1)` branch phases;
- ordering of the three pairs specifies event time order;
- forgetting orientation/order gives the underlying one of 15 perfect matchings.

Thus the full finite ambiguity can be retained as state rather than resolved by an impossible S6-equivariant canonical selector.

This is a concrete repair to the no-selector theorem in the binary note.

## 12. Exact BRC multiplicity at split-prime p^3 closure

For a split odd prime, at the pair-supported branch level:

- 15 choices of perfect matching;
- 2 choices of conjugate branch on each of three pair planes;
- 3! temporal orders.

Hence

`15 * 2^3 * 3! = 720`

ordered oriented three-event closure histories.

Equivalently these are the 720 full pair frames above.

For disjoint pair-supported transports, temporal permutation recoalesces at the final product when the chosen pair blocks commute. Thus a coarser observer sees fewer states:

`720 ordered/oriented histories`

`-> 120 matching+phase closure transports`

`-> 1 Gram state p I_6`

`-> 1 arithmetic index p^3`.

The exact intermediate count depends on which unit/phase transport distinctions the observer retains, but the path-level 720 frame count is canonical for the oriented-pair schedule carrier.

For p=2 the branch phase collapses modulo 2, so the sublattice-level multiplicity is the smaller 90 count from the parent note; transport-level orientation can still restore a richer frame fiber.

## 13. Cross-observer character bridge with the 2D Nollm Eisenstein field

The current Nollm 2D hex/Eisenstein research uses exact conformality governed by the Eisenstein norm

`a^2+a b+b^2`.

For primes `p>3`, its split/inert distinction is controlled by

`chi_-3(p)`:

- `chi_-3(p)=+1` iff `p==1 mod3`;
- `chi_-3(p)=-1` iff `p==2 mod3`.

The present X6 Gaussian-pair strict closure is controlled independently by

`chi_-4(p)`:

- `+1` iff `p==1 mod4`;
- `-1` iff `p==3 mod4`.

These are different observers on different carriers and must not be collapsed.

For primes `p>3`, however, the joint pair

`(chi_-4(p),chi_-3(p))`

recovers the four prime residue classes modulo 12:

| p mod 12 | chi_-4 | chi_-3 | X6 p^3 closure | Nollm/Eisenstein one-step conformal class |
| --- | --- | --- | --- | --- |
| 1 | +1 | +1 | yes | split |
| 5 | +1 | -1 | yes | inert |
| 7 | -1 | +1 | no; first strict X6 closure p^6 | split |
| 11 | -1 | -1 | no; first strict X6 closure p^6 | inert |

Concrete examples:

- `p=5`: X6 Gaussian-pair easy / Nollm Eisenstein hard;
- `p=7`: X6 Gaussian-pair hard / Nollm Eisenstein easy;
- `p=11`: hard in both observers;
- `p=13`: split in both observers.

This is an exact demonstration of the Joint Relation Observer Preservation principle: one prime can carry genuinely different geometric character data in different observer layers, and the joint observer restores finer arithmetic phase information.

No unified Gaussian-Eisenstein physical field is asserted yet.

## 14. Interpretation for natural-number geometry

The binary result suggested that arithmetic 2 should be represented as an exact count/index plus a geometric relation/fiber rather than one point.

The prime classification strengthens that picture.

A prime p has at least the following distinct typed geometric data:

1. arithmetic identity p;
2. determinant-forced volume scale `p^(1/6)` per one index-p event;
3. full index-p sublattice correspondence in `P^5(F_p)`;
4. strict similarity closure exponent `tau_X6(p)`;
5. when `p==1 mod4`, a 30-branch pair-supported Gaussian phase orbit with the universal 15 strain directions;
6. a separate 2D Nollm/Eisenstein character/defect state;
7. joint mod-12 phase when both geometric observers are retained.

Thus prime factorization alone does not exhaust the geometric observer content of p.

## 15. BRC and tool audit

`T0_BRC`: `REUSE_APPLIED`.

- arithmetic p, branch phase, support pair, ordered pair frame, final transport and Gram are distinguished.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

- collapse from the two conjugate branch phases to one strain direction is explicitly scoped to the Gram/strain observer.

`T7_FINITE_SYMMETRY_EQUIVARIANCE`: `REUSE_APPLIED`.

- the 30 split-prime pair branches and 720 oriented pair frames are treated as S6 orbits/torsors rather than canonically selected points.

`T8_RELATION_OBSERVABLE_SPECTRUM`: `COMPOSE_APPLIED`.

- the full index-p family remains a relation; pair-supported conformal branches are only a declared subrelation.

`T9_HOLONOMY_COCOYCLE_GLUING`: `NOT YET EXECUTED` for prime-dependent phase transport beyond one closure cycle. The current note does not claim a global phase-holonomy theorem.

No new top-level tool family is proposed.

## 16. Status ledger

Exact proved under the declared model:

- strict-isotropy power exponent k must be divisible by 3;
- p^3 closure is equivalent to `A^T A=pI_6`;
- for odd prime p, such an integer A exists iff `p==1 mod4`;
- for `p==3 mod4`, first strict-isotropy closure is p^6;
- `tau_X6(p)` exactly reads the mod-4 quadratic character for odd primes;
- a strict determinant-p conformal support block can only have support rank 1 or 2;
- rank 2 exists exactly for p=2 or odd `p==1 mod4`;
- split-prime pair-supported branches have a two-point `sqrt(-1)` phase fiber per axis pair;
- there are 30 such branches for odd split p and 720 ordered oriented three-pair closure histories;
- ordered oriented perfect matchings form an S6 torsor;
- the X6 `chi_-4` and Nollm/Eisenstein `chi_-3` joint observer recovers p mod12 for p>3.

Still open:

- exact global minimum of `Delta_6(A)` for determinant p beyond p=2;
- whether the minimum-defect determinant-p branch orbit coincides with the pair-conformal suborbit for split primes;
- best low-defect one-step geometry for inert primes;
- whether inert-prime six-event closure has a nontrivial lower-defect factorization than six one-axis scalings;
- phase/holonomy law across consecutive prime closures and changing perfect-matching charts;
- a lossless bridge between the Gaussian X6 chart atlas and the Eisenstein Nollm physical field.

## 17. Smallest next research unit

The next exact bottleneck is now narrower than “general prime”.

**Prime-p one-step anisotropy minimization.** For each prime p, classify

`min_{A in M_6(Z), |det A|=p} Delta_6(A)`

and the S6/projective branch orbits attaining it.

Priority subquestions:

1. prove or refute that Gaussian-split pair-conformal blocks are globally minimum-defect for any infinite prime class;
2. derive a lower bound for inert primes that retains branch/phase information rather than only determinant;
3. determine whether the minimizer spectrum itself detects additional Dirichlet characters beyond `chi_-4`;
4. compare exact X6 minimizer phases with the independently retained Eisenstein defect spectrum only after both carriers are frozen.
