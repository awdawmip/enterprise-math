# Profinite Local-Global Precision

Status: `FOUNDATION-FACING RESEARCH BRIDGE / NONCANONICAL`

This note does not introduce a new Foundation Question. It compresses the current integer IMAGE/FIBER research into one precision architecture using the congruence/profinite topology on finitely generated integer lattices.

## 1. Modular precision is a topology of congruence neighborhoods

On `Z^n`, the subgroups

`M Z^n`, `M=1,2,...`

form the standard congruence neighborhood system around zero.

Passing from exact integer data to mod-M data means replacing one exact point or subgroup by its coset/thickening at that neighborhood scale.

Increasing arithmetic precision is therefore not merely increasing a scalar number. It means moving through a divisibility-refined family of congruence neighborhoods.

## 2. Closed means asymptotically identifiable

Let `H<=Z^n` be a finitely generated subgroup. Standard subgroup separability gives

`H = intersection_(M>=1) (H + M Z^n)`.

So every integer lattice subgroup is closed in the profinite/congruence topology.

Precision interpretation:

> If an exact state lies outside H, some finite modular precision will eventually separate it from H.

This is the topological form of the integer local-global principle.

Closedness does **not** say that one preselected finite modulus works uniformly for every outside state.

## 3. Open means finitely and uniformly certifiable

H is open iff it contains some congruence neighborhood:

`M Z^n subseteq H`

for some finite M.

Equivalently, H has finite index in the ambient integer lattice.

Precision interpretation:

> An exact membership property has one finite uniform modular cutoff precisely when the defining subgroup is open.

Thus:

`closed -> every individual false state has some finite separating precision`,

while

`open -> one finite precision works for the entire unrestricted state family`.

## 4. IMAGE can be nontrivially clopen

For

`A:Z^n -> Z^m`,

let

`L=im_Z(A)`.

Exact target reachability is membership in L.

L is always closed. It is open iff

`rank_Q(A)=m`,

that is, iff the cokernel has no free part.

When open, let

`E=exp(coker(A))`

be the largest Smith factor. Then E is the unique least modulus with

`E Z^m subseteq L`.

Hence:

- full row rank -> IMAGE is clopen and one finite exact precision E exists;
- rank deficient -> IMAGE is closed but not open; each bad target has a finite separator, but no one finite modulus decides all unrestricted targets.

This is the topological meaning of the affine local-global hierarchy.

## 5. Rational-image promises change the ambient precision space

For rank-deficient A, define the saturation

`S = span_Q(L) intersect Z^m`.

If a target is independently known to lie in S, the free cokernel coordinate is already removed. Inside this smaller ambient lattice, L has finite index.

Therefore L becomes open in the induced profinite topology on S, and the same finite torsion exponent E becomes the least uniform exact certificate.

So a prior structural promise can turn a closed/non-open problem into an open one by changing the admissible world rather than by increasing the modulus.

## 6. FIBER has a different topology

For integer observation

`O:Z^n -> Z^m`,

let

`K=ker_Z(O)`.

K is saturated because the codomain is torsion-free. Hence

`Z^n/K ~= im(O)`

is free abelian.

Therefore:

- K is always closed;
- K is open iff `im(O)=0`, i.e. iff O is the zero observation.

So every proper exact observation fiber is closed but not open.

Precision consequence:

> For any nonzero integer observation, no fixed finite modular family uniformly certifies exact state-output equality over all unbounded integer states.

Yet any state difference outside K is eventually separated by sufficiently refined modular precision.

This is a genuine IMAGE/FIBER asymmetry: a nontrivial IMAGE subgroup can be clopen; a proper kernel into free integer observations cannot.

## 7. Independent bounds finite-ize closed non-open questions

Closed-but-not-open does not mean finite precision can never be decisive. It means no uniform cutoff exists over an unbounded admissible family.

If an independent height bound restricts the allowed lifts, a finite cutoff returns.

### IMAGE

Let integer left-null rows Q span the rational obstruction directions. If

`||Qb||_infinity <= B`,

then any modulus D satisfying

`D>B` and `E|D`

makes mod-D solvability equivalent to exact reachability on that bounded target family.

### FIBER

If

`|x_i|,|y_i|<=H`,

then

`|O_j(x-y)| <= 2H ||O_j||_1`.

Any modulus strictly larger than the largest possible output difference makes modular output equality identical to exact output equality on the whole bounded state box.

Common principle:

> **closed exact property + independent finite lift-height bound -> finite exact precision certificate.**

The bound is part of the declared world, not information manufactured by the modulus.

## 8. Supernatural precision describes arbitrary infinite experiment families

For a finite or infinite modulus family, define its supernatural lcm

`Q_* = product_p p^(q_p)`,

`q_p=sup_M v_p(M)`.

For

`coker(A) ~= Z^f direct_sum T`,

with torsion exponent

`E=product_p p^(a_p)`,

the family is uniformly complete for exact IMAGE reachability iff

- `f=0` or `Q_*` is infinite supernatural; and
- `q_p>=a_p` for every torsion prime.

Thus arbitrary modular experiments have two exact resources:

1. **free separation** — enough unbounded supernatural extent to force a free integer coordinate to zero;
2. **prime depth** — enough p-adic depth to eliminate each finite torsion component.

Finite families, all-prime breadth, and one tailored power ladder are merely different ways of supplying these coordinates.

## 9. Least precision undergoes a structural phase change

If the cokernel is finite, complete supernatural profiles form the principal up-set

`{Q : E divides Q}`

with one unique least element E.

If a free cokernel remains, completeness additionally requires Q to be infinite supernatural. The complete profiles still form an up-set, but there is no least element.

Their minimal elements are

`E*p^infinity`, one for each prime p,

meaning: keep every finite torsion depth exactly at its required value and choose one arbitrary prime direction to extend without bound.

Hence:

`finite cokernel -> unique least exact precision`,

`free cokernel -> no least exact precision, but infinitely many incomparable minimal unbounded directions`.

For a nonzero FIBER observation, E=1 and the minimal exact precision directions are simply `p^infinity`.

## 10. Precision requirements compose by join, not by addition

One integer IMAGE task contributes a requirement

`(free-separation flag ; required p-depths)`.

Several tasks sharing one experiment language combine by coordinatewise join:

- free flag -> logical OR;
- p-depth -> maximum.

If no joined free direction remains, the least common finite modulus is the ordinary lcm of the individual torsion exponents.

If a free direction remains, the joined finite torsion requirement E still combines by lcm, while one arbitrary infinite prime direction can serve the entire joined free-separation need.

So precision resources combine by lattice join rather than scalar addition.

## 11. Foundation routing consequence

The current precision architecture can now distinguish four questions that should not be collapsed:

1. **Does an exact object exist?** — IMAGE/COKERNEL.
2. **If it exists, how large is its state fiber?** — FIBER/KERNEL.
3. **Will some finite refinement eventually distinguish a false state?** — closedness.
4. **Is there one finite uniform cutoff for the whole admissible world?** — openness, possibly after adding an independent bound or changing the admissible ambient space.

This provides a precise meaning for several earlier project intuitions about finite precision:

- “not yet distinguished” is not the same as “identical”;
- “distinguishable at some finite precision” is not the same as “there is one universal finite precision”;
- an unbounded precision requirement need not have one canonical direction.

Profinite topology, subgroup separability, finite-index lattices, Smith normal form and supernatural numbers are standard prior mathematics. The Enterprise Math contribution here is the routing and precision interpretation, not the underlying generic algebra.