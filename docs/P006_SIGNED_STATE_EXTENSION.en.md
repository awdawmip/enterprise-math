# P006 — Signed-state extension without conflating order and magnitude

Status: `PROVED DESIGN RESOLUTION`  
Open problem: `P006`  
Scope: integer state space, signed roots, collapse semantics

## 1. Why the signed extension is not unique

Moving from \(\mathbb N\) to \(\mathbb Z\) creates two natural but different notions of discrete root:

1. an **order root**, defined as the greatest integer whose power does not exceed the input;
2. a **signed-magnitude root**, obtained by rooting the absolute value and restoring the sign.

These agree on nonnegative inputs but disagree on negative inputs. Enterprise Math must therefore name them separately rather than pretending that “adding a sign” gives a unique extension.

## 2. Odd-exponent order root on \(\mathbb Z\)

Let \(p\ge1\) be odd. Define

\[
R^{\mathbb Z}_p(n)
=
\max\{k\in\mathbb Z:k^p\le n\}.
\]

Because \(k\mapsto k^p\) is strictly increasing and unbounded in both directions for odd \(p\), this maximum exists for every \(n\in\mathbb Z\).

### P006-T01 — Signed odd-root characterization

Status: `PROVED`

For odd \(p\),

\[
\boxed{
R^{\mathbb Z}_p(n)=k
\iff
k^p\le n<(k+1)^p.
}
\]

Thus the same interval characterization as T001 extends to all integer basin anchors \(k\in\mathbb Z\).

For \(n\ge0\),

\[
R^{\mathbb Z}_p(n)=R_p(n).
\]

For \(n=-m<0\), define the positive integer ceiling root

\[
U_p(m)=\min\{j\in\mathbb N:j^p\ge m\}.
\]

Then

\[
\boxed{R^{\mathbb Z}_p(-m)=-U_p(m).}
\]

So negative inputs naturally use a ceiling magnitude, not the natural-number floor magnitude.

## 3. Order-adjoint structure survives exactly for odd exponents

Let

\[
P_p(k)=k^p.
\]

### P006-T02 — Odd power / signed order-root adjunction

Status: `PROVED`

For odd \(p\),

\[
\boxed{
P_p(k)\le n
\iff
k\le R^{\mathbb Z}_p(n).
}
\]

Hence

\[
P_p\dashv R^{\mathbb Z}_p
\]

on the ordinary integer order.

Moreover,

\[
R^{\mathbb Z}_p(k^p)=k,
\]

so this is a Galois coinsertion exactly analogous to the positive-state root structure.

## 4. Signed order collapse

For odd \(p\), define

\[
C^{\mathbb Z}_p(n)
=
\left(R^{\mathbb Z}_p(n)\right)^p.
\]

### P006-T03 — Integer-order collapse laws

Status: `PROVED`

For odd \(p\):

\[
C^{\mathbb Z}_p(n)\le n,
\]

\[
C^{\mathbb Z}_p(C^{\mathbb Z}_p(n))=C^{\mathbb Z}_p(n),
\]

and

\[
C^{\mathbb Z}_p(n)=n
\iff
n=k^p
\quad\text{for some }k\in\mathbb Z.
\]

The basin of \(k^p\) is

\[
\{n\in\mathbb Z:k^p\le n<(k+1)^p\},
\]

with cardinality

\[
(k+1)^p-k^p.
\]

### Important geometric consequence

For negative inputs, “contractive in the ordinary order” means moving downward, which can increase magnitude.

Example:

\[
R^{\mathbb Z}_3(-2)=-2,
\qquad
C^{\mathbb Z}_3(-2)=-8.
\]

So ordinary-order collapse is not a “move toward zero” rule.

## 5. Signed-magnitude quantization

For any \(p\ge1\), define

\[
S_p(n)=\operatorname{sgn}(n)R_p(|n|),
\]

and define the signed-magnitude collapse

\[
A_p(n)
=
\operatorname{sgn}(n)R_p(|n|)^p.
\]

This is a different construction. It quantizes magnitude while carrying sign as an explicit coordinate.

### P006-T04 — Signed-magnitude collapse laws

Status: `PROVED`

For every \(p\ge1\) and every \(n\in\mathbb Z\):

\[
A_p(-n)=-A_p(n),
\]

\[
|A_p(n)|\le|n|,
\]

\[
A_p(A_p(n))=A_p(n),
\]

and

\[
A_p(n)=n
\iff
|n|=k^p
\quad\text{for some }k\in\mathbb N.
\]

Thus \(A_p\) is total for both odd and even exponents and is contractive in magnitude.

However, for negative \(n\), it is generally **not** contractive in the ordinary integer order. For example,

\[
A_3(-2)=-1>-2.
\]

It is therefore not the same interior operator as \(C^{\mathbb Z}_p\).

## 6. Counterexample: the two signed roots disagree

### P006-C01 — Order root is not sign-restored natural root

Status: `COUNTEREXAMPLE`

Take \(p=3\) and \(n=-2\).

The order root gives

\[
R^{\mathbb Z}_3(-2)=-2
\]

because

\[
(-2)^3=-8\le-2<(-1)^3=-1.
\]

But sign-restored magnitude gives

\[
S_3(-2)=-R_3(2)=-1.
\]

Therefore

\[
\boxed{R^{\mathbb Z}_3(-2)\ne S_3(-2).}
\]

Any signed specification that uses the phrase “integer root” must say which operation it means.

## 7. Even exponents: no ordinary-order signed root adjunction

For even \(p\), the map

\[
k\mapsto k^p
\]

is not monotone on \(\mathbb Z\). For example,

\[
-2<-1
\]

but

\[
(-2)^2=4>1=(-1)^2.
\]

### P006-C02 — Even power has no right adjoint on the ordinary integer order

Status: `COUNTEREXAMPLE / STRUCTURAL OBSTRUCTION`

Any left adjoint between preorders must be monotone. Since even-power formation is not monotone on \(\mathbb Z\), it cannot be the left member of a Galois connection

\[
P_p\dashv R
\]

on the ordinary integer order.

Also, negative integers are not even \(p\)-th powers in \(\mathbb Z\).

Therefore a total signed operation for even \(p\) cannot simultaneously be interpreted as an ordinary-order right adjoint to integer power formation.

## 8. Incompatibility of the two design goals

### P006-T05 — Odd symmetry and ordinary-order adjunction cannot both select the same root rule

Status: `PROVED`

For odd \(p\), the right adjoint to \(k\mapsto k^p\) on the integer order is unique. P006-C01 shows that this unique order root is not the sign-restored magnitude rule.

Hence no single operation can simultaneously be:

1. the ordinary-order right adjoint to odd-power formation; and
2. the signed-magnitude truncation \(\operatorname{sgn}(n)R_p(|n|)\).

The specification must choose which order/geometry it is expressing.

## 9. Minimal signed-state design

P006 is resolved by keeping the integer state domain

\[
\mathbb Z
\]

while refusing to overload one root symbol with incompatible semantics.

The minimal explicit design is:

### A. `orderRootOdd`

For odd \(p\) only:

\[
R^{\mathbb Z}_p(n)=\max\{k\in\mathbb Z:k^p\le n\}.
\]

Use this when the intended structure is ordinary integer order, Galois adjunction, and order-interior collapse.

### B. `magnitudeRoot`

For any \(p\ge1\), apply the existing natural root only to the explicit magnitude

\[
R_p(|n|).
\]

Sign is retained separately.

### C. `signedMagnitudeCollapse`

If a total sign-preserving quantizer is required, use

\[
A_p(n)=\operatorname{sgn}(n)R_p(|n|)^p
\]

and call it a **signed-magnitude collapse**, not an integer \(p\)-th-power collapse when \(p\) is even and the output is negative.

### D. Even roots remain partial as actual integer roots

For even \(p\), an actual \(p\)-th root relation over \(\mathbb Z\) is defined only on nonnegative perfect powers if exact inversion is required, or on nonnegative states if the floor-root operation is intended.

No hidden complex, real, or fractional state is introduced.

## 10. Interpretation boundary

The choice between ordinary-order collapse and magnitude collapse is mathematical structure, not yet physical evidence about how signed physical quantities should behave.

If a later physical model treats sign as orientation and magnitude as resolution, the signed-magnitude construction may be more natural. If it treats the usual integer order as fundamental, the odd order-root construction is the correct adjoint extension.

Enterprise Math should keep both available until a domain-specific axiom chooses between them.

## 11. Prior-art discipline

Integer order, odd/even power monotonicity, floor/ceiling roots, Galois adjunctions, and sign-magnitude decompositions are established mathematics. P006 does not claim historical priority for these ingredients.

The project-specific contribution is the explicit separation of two signed extensions that would otherwise be easy to conflate inside the finite-state semantics. Historical novelty of this packaging remains `NOVELTY_UNVERIFIED`.
