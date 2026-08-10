# R004 precision genesis — Supplement 31: typed coupling-liveness gates

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + JOINT-COUPLING DEMOTION SPECIALIZATION`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_30.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 30 established the joint weighted coupling as the canonical strong certificate before marginal erasure. This supplement asks when a remaining coupled query can nevertheless be answered exactly from marginals, so the joint coupling may be retired.

The answer is semantic-type dependent. MAY, COUNT and LABEL-SET have different exact gates.

## 1. MAY cylinder-forcing gate

Let the retained marginal supports be nonempty finite sets `S_i` and let

`Y=product_i S_i`.

A coupled MAY predicate is a subset `P subseteq Y`. After the joint relation has been erased, the only known fact is that the unknown coupling J has coordinate projections exactly `S_i`.

### Forced false

`MAY(P)` is false for every compatible J iff

`P cap Y=empty`.

### Forced true

`MAY(P)` is true for every compatible J iff the complement

`Y\P`

fails to project onto at least one full marginal S_i.

Equivalently, there exists coordinate i and value v in S_i such that the full cylinder

`{y in Y : y_i=v}`

is contained in P.

Proof. A coupling avoiding P exists exactly when the complement itself contains a relation with all required projections. The complement has such a relation iff every coordinate projection is full; the complement itself is then one. If some marginal value disappears from the complement, every compatible relation must hit P to realize that value.

Every other predicate is coupling-sensitive.

## 2. COUNT coupled-query gate

Now let N(y) be a joint nonnegative integer count tensor and retain all one-dimensional count marginals

`m_i(v)=sum_{y:y_i=v}N(y)`.

For an integer coefficient tensor c, consider

`Q_c(N)=sum_y c(y)N(y)`.

Then Q_c is determined by the one-dimensional marginals for **every** joint count tensor iff

`c(y_1,...,y_m)=alpha+sum_i f_i(y_i)`

for integer one-coordinate potentials f_i.

### Sufficiency

If the representation holds,

`Q_c=alpha*N_total+sum_i sum_v f_i(v)m_i(v)`.

### Necessity

A function on a Cartesian product is of this additive form iff all mixed 2x2 rectangle differences vanish. If a mixed difference

`c(a,b)+c(a',b')-c(a,b')-c(a',b)`

is nonzero with the remaining coordinates fixed, use the standard signed 2x2 cycle (+1,+1,-1,-1). It has zero one-dimensional marginals. Adding a unit baseline on those four cells gives two nonnegative integer joint tables with identical marginals but different Q_c.

Thus any non-additive coupled count query proves that joint count coupling remains live.

## 3. Boolean predicate COUNT is stricter than MAY

If c is the Boolean indicator of a predicate P, additive separability implies that P depends on at most one nontrivial coordinate (including empty/full cases).

Indeed, if two coordinate potentials were both nonconstant, choosing two values in each coordinate would produce four Boolean values of the form

`z, z+a, z+b, z+a+b`

with nonzero integer a,b; no such four values all lie in `{0,1}`.

Therefore

`COUNT(P) from one-way marginals`

is possible exactly when P is essentially a marginal/single-coordinate query.

This is strictly stronger than MAY. A predicate may contain a full cylinder and hence have MAY forced true while its exact count remains coupling-sensitive.

## 4. COUNT gate is another Structural Target Compiler instance

Flatten N into a vector indexed by the joint cells Y. One-way marginalization is an integer incidence matrix

`A_marg N`.

A family of coupled linear count queries is a target matrix

`B N`.

Then the exact condition is simply

`ker A_marg subseteq ker B`,

which is Supplement 20's Structural Target criterion applied recursively to the **coupling certificate state**.

For one row c, the additive-potential condition above is exactly

`c in Row(A_marg)`.

So COUNT coupling liveness requires no new mother theory.

## 5. Full joint COUNT coupling dimension

Suppose target coordinate i has n_i values. The joint count tensor has

`Ncells=product_i n_i`

coordinates.

The one-way marginal incidence matrix has rank

`r_marg=sum_i n_i-(m-1)`.

Proof. A linear relation among its rows is a family of one-coordinate functions g_i satisfying

`sum_i g_i(y_i)=0`

for every joint tuple. Varying one coordinate at a time forces every g_i to be constant; the constants have one equation, so the row-relation space has dimension m-1.

Moreover an integer full-rank minor with determinant ±1 is obtained by choosing one base cell plus cells that change exactly one coordinate from a base value. Hence all nonzero Smith invariants are 1.

Therefore the exact p-adic coupling defect between the full joint count tensor and its one-way marginals is a free module

`(Z/p^K)^(d_coup)`

with

`d_coup=product_i n_i-sum_i n_i+(m-1)`.

For a 2-way r x c table this is `(r-1)(c-1)`.

## 6. LABEL-SET gate decomposes labelwise

Finite label sets under union are a product of Boolean OR channels, one for each label.

For each live label lambda, consider the Boolean joint support of tuples carrying lambda and its marginal supports. The label belongs to the coupled predicate's union iff the corresponding MAY query is true.

Therefore marginal LABEL-SET certificates determine a coupled label-union query iff the MAY cylinder gate is decisive for every live label separately.

If any label remains coupling-sensitive, the joint label coupling remains live.

## 7. Generic monoid fallback

No universal closed form is claimed for every commutative monoid or every query language.

When no typed factorization theorem applies, keep the joint coupling table as certificate state and use Supplement 24/P023 suffix compilation. The compiler must fail closed rather than infer independence from marginal summaries.

## 8. Validation

### MAY

All nonempty Boolean relations on shapes `2x2`, `2x3`, `2x2x2`, and `2x2x3` were grouped by marginal supports. Across **120** distinct marginal profiles, the forced-true/forced-false/ambiguous gate had zero violations; 35 profiles admitted multiple couplings.

### COUNT

All joint count tables with cell entries in `{0,1,2}` were enumerated for shapes:

- `2x2`: 81 tables / 65 margin profiles;
- `2x3`: 729 tables / 425 margin profiles;
- `2x2x2`: 6,561 tables / 1,537 margin profiles.

For every Boolean predicate coefficient tensor (16, 64 and 256 queries respectively), "constant on every fixed-marginal fiber" exactly matched the additive-potential gate.

Additionally all coefficient tensors in `{-1,0,1}` were checked for shapes `2x2` and `2x3` (81 and 729 query tensors); again the gate was exact.

### Smith/rank formula

For every shape of 2, 3 or 4 target coordinates with each size in `{1,2,3}` — **117 shapes** — the one-way marginal incidence matrix had rank `sum n_i-(m-1)` and every nonzero integer Smith invariant equal to 1.

## 9. Architecture consequence

"Coupled query" is not a sufficient compiler type. The semantic layer matters:

- MAY can sometimes be decided by cylinder forcing;
- exact COUNT requires additive marginal factorization;
- LABEL-SET decomposes into per-label MAY gates;
- generic witness semantics fall back to the joint coupling certificate.

The same syntactic predicate may therefore require different representation precision under different declared semantics.

## 10. Next frontier

The next useful problem is **coupling obstruction cuts for a family of live queries**. For COUNT, the Structural Target reduction suggests a linear query-defect module. For MAY, the cylinder gate suggests a hypergraph of coupling-sensitive predicates. The goal is to compute the smallest extra coupling certificate beyond marginals, not merely decide whether full joint state is necessary.
