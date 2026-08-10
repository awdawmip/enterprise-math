# P025 Supplement 74 — Small-Radical Compression on the P018/P025 Centered Overlap

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-paired-square-tail-stage61`  
Depends on: P025 Supplement 73; canonical P018 centered-prime size range; external de Bruijn radical counting  
Hard block: `NONE`

## 1. Add the canonical P018 size hypothesis

Use the Stage-73 centered coordinates

\[
q=B-A,
\qquad
p=B+A,
\]

for distinct odd primes `p>q`, and suppose the pair also lies in the P018 centered theorem range

\[
\boxed{q=B-A>A^2.}
\]

Then in particular

\[
\boxed{A^2<B.}
\]

Assume the P025 `(2,2)` difference atom crosses threshold `T>=1`. Stage 73 gives

\[
\boxed{m(A)\ge T\operatorname{rad}(B).}
\]

## 2. P025-T143 — compile the overlap to one small-radical integer

Since `A,B` are coprime,

\[
\operatorname{rad}(AB)
=
\operatorname{rad}(A)\operatorname{rad}(B).
\]

The projective threshold is

\[
\frac{A}{\operatorname{rad}(A)}
\ge
T\operatorname{rad}(B),
\]

hence

\[
\boxed{
T\operatorname{rad}(AB)\le A.
}
\]

Define

\[
\boxed{n=AB.}
\]

The P018 size range now gives two exact integer inequalities:

\[
\boxed{n^2=A^2B^2<B^3,}
\]

and

\[
\boxed{
T^2\operatorname{rad}(n)^2
\le A^2<B.
}
\]

Thus a state involving two centered primes and a prime-square abc relation collapses to **one integer `n=AB`** with an unusually small radical.

## 3. Center-height formulation

Restrict to

\[
B\le X.
\]

P025-T143 becomes

\[
\boxed{
n<X^{3/2},
\qquad
\operatorname{rad}(n)<\frac{X^{1/2}}T.
}
\]

This is the theorem-native input form for the same de Bruijn radical-counting tool used by Stage 62/64.

The centered-prime conditions `B-A` and `B+A` prime are no longer needed by the counting theorem after the compilation; they can only reduce the candidate set further.

## 4. P025-C18 — de Bruijn overlap scale

Import the classical de Bruijn radical-counting estimate in the same two-parameter form used by Stage 64.

The integer `n` has height `X^(3/2)` while its radical has height only `X^(1/2)/T`, corresponding to one-third of the product-height exponent.

After the standard divisor-bound reconstruction of `(A,B)` from `n=AB`, the overlap slice obeys the formal scale

\[
\boxed{
N_X^{\rm overlap}(T)
\ll_\varepsilon
\frac{X^{1/2+\varepsilon}}T.
}
\]

Here `X` is **center height**, not the original abc `c=p^2` height.

This is much smaller than the trivial `O(X^(3/2))` number of integer pairs with `B<=X` and `A^2<B`.

The analytic count is external-prior-art dependent; the new internal theorem is the exact compression P025-T143.

## 5. Why the exponent improves on the overlap

Stage 64's generic projective compiler sends a height-`X` additive state to a pair product of size roughly `X^2`.

On the P018 centered overlap, the canonical size hypothesis forces

\[
A<\sqrt B,
\]

so the theorem-native product has only

\[
AB<B^{3/2}.
\]

The same projective threshold controls its radical at scale `B^(1/2)/T`.

Thus the cross-route theorem removes half a dimension from the height of the object that de Bruijn must count.

This gain is unavailable from either route alone:

- P025 supplies the radical inequality;
- P018 supplies the radius-square size restriction.

## 6. Exact examples

### `(q,p)=(73,89)`

\[
(B,A)=(81,8),
\qquad
73>8^2.
\]

The P025 threshold-one state has

\[
n=81\cdot8=648,
\qquad
\operatorname{rad}(n)=6.
\]

Indeed

\[
6\le8
\]

and

\[
648^2<81^3.
\]

### `(q,p)=(503,521)`

\[
(B,A)=(512,9),
\]

with

\[
n=4608,
\qquad
\operatorname{rad}(n)=6.
\]

Again threshold one holds.

### `(q,p)=(997,1051)`

\[
(B,A)=(1024,27),
\]

and the projective value is `9/2`. At threshold four,

\[
4\operatorname{rad}(AB)=24\le27.
\]

This gives a higher-threshold overlap sample inside the P018 size range.

## 7. A pointwise squarefree guard in centered coordinates

Stage 73's exact formula

\[
\rho=\frac{m(A)}{\operatorname{rad}(B)}
\]

immediately implies

\[
\boxed{
\rho\ge1
\Longrightarrow
A\text{ and }B\text{ are both nonsquarefree}.
}
\]

Indeed:

- if `A` is squarefree, then `m(A)=1<rad(B)`;
- if `B` is squarefree, then `rad(B)=B>A>=m(A)`.

So before invoking any counting theorem, either squarefreeness bit already certifies a subunit P025 state on this shell.

This is the centered-coordinate analogue of Stage 69's coarse safe basin.

## 8. Cross-route precision interpretation

The full overlap pipeline is now

\[
\boxed{
(p,q)
\to
(B,A)
\to
[\text{P018 size guard }A^2<B]
+
[\text{P025 ratio }m(A)/rad(B)]
\to
n=AB
\to
\text{small-radical external count}.
}
\]

Different routes contribute independent coordinates, and their join creates a theorem-native state strictly cheaper than retaining the original prime pair.

This is a concrete example of composable precision rather than one branch subsuming another.

## 9. Prior-art / ownership boundary

The P018 size theorem is canonical Enterprise Math work in its stated scope. De Bruijn radical counting and divisor bounds are external prior mathematics. The algebraic conversion to `n=AB` is elementary.

The P025 contribution is the exact cross-route composition of those inputs. Historical novelty remains `NOVELTY_UNVERIFIED`.

No claim is made that P025 proves new prime-pair density results independently of the imported radical count.

## 10. Executable assets

Added:

- `src/enterprise_math/abc_p018_centered_overlap.py`;
- `tests/test_abc_p018_centered_overlap.py`.

The code stores only exact finite inequalities and the formal height powers. It does not implement the external asymptotic theorem.

## 11. Next frontier

No hard block exists. Continue with:

1. Relay P025-T142/T143 to P018 as a composable centered-coordinate consumer;
2. compare the overlap sparse compiler with P018's existing factor-proof horizon rather than duplicating prime-pair counting machinery;
3. search for analogous cross-route size gains in `(3,3)` and `(4,4)` shells;
4. use this example in Foundation backflow for `independent route coordinates -> cheaper joined theorem-native state`.
