# R063 Stage 2 — Unit Quotient and Ordered Component-Root Multiplication

Status: `PROVED WITH ORIENTATION BOUNDARY`

## 1. Unit-orbit root monoid

Let

`U={1,J,-1,-J}`,

`URoot(N)=SRoot(N)/U`.

Define

`[z]_U star_U [w]_U = [zw]_U`.

### Theorem 1.1 — well-definedness

If `z'=uz` and `w'=vw` for units `u,v`, then

`z'w'=(uv)zw`,

so `z'w'` and `zw` lie in the same unit orbit. Therefore `star_U` is independent of representatives.

Associativity and commutativity descend from Gaussian multiplication. The norm-one identity is `[1]_U`, and grading is exact:

`URoot(A) x URoot(B) -> URoot(AB)`.

Thus the disjoint union over supported norms is an exact graded commutative monoid.

Under the frozen Stage 1 normalization, a `URoot(N)` class is equivalently the vector of split-prime allocations `(t_p)`, and

`|URoot(N)| = product_{p == 1 mod 4} (e_p+1)`.

## 2. Closed first quadrant is not globally a section of the unit quotient

Stage 1 returns the **full ordered nonnegative component-root fiber**

`GRoot_E(N)={(a,b) in N_0^2 : a^2+b^2=N}`.

The taskbook asks whether the canonical closed-first-quadrant representative gives a bijection

`URoot(N) <-> GRoot_E(N)`.

The answer is:

- **yes when `N` is supported and nonsquare**;
- **no when `N` is a square**.

### Theorem 2.1 — exact fiber statement

Every non-axial unit orbit meets the closed first quadrant in exactly one point. An axial unit orbit is

`{(r,0),(0,r),(-r,0),(0,-r)}`,

and therefore meets the closed first quadrant twice, at `(r,0)` and `(0,r)`.

An axial root exists exactly when `N=r^2`. There is then exactly one axial unit orbit. Consequently

`|GRoot_E(N)| = |URoot(N)| + 1_{N is a square}`.

The quotient map

`q_N : GRoot_E(N) -> URoot(N)`

has all fibers of size `1`, except for the unique axial fiber of size `2` when `N` is square.

Minimal counterexample to a global bijection:

`N=1`: `GRoot_E(1)={(1,0),(0,1)}` but `|URoot(1)|=1`.

This is a **unit quotient only**. No conjugation or component-swap quotient has been inserted.

## 3. Exact oriented component product

Although `URoot` does not choose between the two axial Stage 1 component representatives, an exact product exists after an ordered sector orientation is explicitly retained.

For

`r=(a,b)`, `s=(c,d)` in the ordered nonnegative component carrier, define the raw Gaussian product

`x=ac-bd`,

`y=ad+bc`.

Since `a,b,c,d>=0`, `y>=0`. Define the `i`-oriented normalization

`r star_i s = (x,y)` if `x>=0`,

`r star_i s = (y,-x)` if `x<0`.

The second case is exactly multiplication of the raw Gaussian product by the unit `-J`; it is not an untyped coordinatewise absolute-value operation.

Then

`r star_i s in GRoot_E(AB)`

whenever `r in GRoot_E(A)` and `s in GRoot_E(B)`, because unit multiplication preserves Gaussian norm.

The quotient compatibility is exact:

`q_AB(r star_i s) = q_A(r) star_U q_B(s)`.

The identity is `(1,0)`, and the operation is commutative.

### Associativity

A short derived-Gaussian proof uses only an auxiliary quarter-turn phase coordinate; it is not promoted to native geometry. Let a nonnegative-quadrant Gaussian number have phase parameter in `[0,H]`, where `H` is one quarter-turn. The normalization above induces

`theta o phi = theta+phi` when `theta+phi<=H`,

`theta o phi = theta+phi-H` when `theta+phi>H`.

For any finite positive total `S`, the iterated value is the unique remainder in `(0,H]` modulo `H`; it is `0` only when every input phase is `0`. Hence the result depends only on the total phase sum, not on parenthesization. Combined with associativity of Gaussian multiplication and multiplicativity of norm, this proves associativity of `star_i`.

Thus `(GRoot_E,star_i)` is an exact orientation-conditioned graded commutative monoid.

## 4. The opposite orientation and the choice boundary

Let

`sigma(a,b)=(b,a)`.

Define the swap-conjugate product

`r star_j s = sigma( sigma(r) star_i sigma(s) )`.

It is equally exact, with identity `(0,1)`.

The products disagree at the mandatory discriminator:

`(1,1) star_i (1,1) = (0,2)`,

`(1,1) star_j (1,1) = (2,0)`.

The two outputs are in the same `URoot(4)` class but are distinct Stage 1 ordered component roots.

Therefore `URoot` multiplication alone does not canonically descend to the **full ordered Stage 1 component-root fiber**. The descent requires an orientation/boundary convention, and that convention must remain typed as additional Stage 2 operational semantics.

A stronger symmetry statement is immediate: because `(1,1)` is fixed by `sigma`, any single-valued component product that both lifts the `URoot` product and is `sigma`-equivariant would have to send `(1,1),(1,1)` to a `sigma`-fixed norm-4 component root. No such ordered nonnegative norm-4 root exists. Hence an orientation-free `sigma`-equivariant lift is impossible.

## 5. Classification

`UNIT_QUOTIENT_ROOT_GRADED_COMMUTATIVE_MONOID = PROVED`.

`CLOSED_FIRST_QUADRANT_URoot_TO_FULL_GRoot_BIJECTION = FALSE_ON_SQUARES`.

`ORIENTED_COMPONENT_ROOT_PRODUCT = EXACT_CONDITIONAL_DERIVED`.

`ORIENTATION_FREE_SWAP_EQUIVARIANT_ORDERED_COMPONENT_PRODUCT = NO_GO`.

`CONJUGATION_OR_SWAP_QUOTIENT = NOT_TAKEN`.
