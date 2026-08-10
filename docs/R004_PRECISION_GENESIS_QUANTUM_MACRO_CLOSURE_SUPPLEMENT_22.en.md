# R004 precision genesis — Supplement 22: nonlinear defect bundle and A4 escalation gate

Status: `PROVED_WIP + EXECUTABLE_REFERENCE + A4_ESCALATION_BRIDGE`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_21.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplements 20–21 found a strong structured defect object for linear targets: a finite p-group missing-target module. This supplement closes the boundary for arbitrary nonlinear targets. The correct fallback is not another invented scalar or module. It is the existing A4-style support correspondence.

## 1. Canonical nonlinear target correspondence

Let `q:X->Q` be any finite collapse and `t:X->T` any deterministic target. Define

`R_(q,t) subseteq Q x T`

by

`a R_(q,t) y  iff  exists x: q(x)=a and t(x)=y`.

Equivalently,

`R_(q,t)(a)=t(q^{-1}(a))`.

This is the exact target-uncertainty bundle seen from the coarse world.

The target descends to a coarse function iff every fiber support is a singleton.

## 2. Composition law

For any post-relation `S subseteq T x U`, the exact coarse support after the future step S is

`R_(q,t) ; S`.

This is just ordinary relational composition. Therefore arbitrary nonlinear target support already belongs to the A4 correspondence/composition layer.

If the future language asks only MAY support, `R_(q,t)` is sufficient. If it asks witness multiplicity, labels, or witness identity, Boolean support is insufficient and the typed monoid/weighted relation compiler from Supplement 13 must be used instead.

## 3. Group-valued target and derivative gate

Now assume X and T are finite abelian groups and q is the quotient by subgroup K. For `k in K` define the discrete target derivative

`partial_k t(x)=t(x+k)-t(x)`.

Suppose, for every k, `partial_k t(x)` is independent of x. Define

`phi(k)=partial_k t(x)`.

Then phi is automatically a group homomorphism:

`phi(k+l)=phi(k)+phi(l)`.

For every coarse fiber,

`t(x+K)=t(x)+im(phi)`.

Thus the nonlinear support correspondence compresses to

`coarse base value in T/im(phi) + uniform defect subgroup im(phi)`.

This is the exact gate behind the linear-module case. If q and t are homomorphisms, `phi=t|_K` and Supplement 20's missing-target module is the finite dual representation of this kernel-image defect.

## 4. State-dependent defect bundle: cubic mod 8

Let

`X=Z/8`, `q(x)=x mod 4`, `t(x)=x^3 mod 8`.

The kernel translation is `+4`, but target variation depends on the coarse state:

- coarse 0: target support `{0}`;
- coarse 1: target support `{1,5}`;
- coarse 2: target support `{0}`;
- coarse 3: target support `{3,7}`.

So no single global defect subgroup can represent all fibers. The correct object is the state-dependent A4 correspondence.

This illustrates the real nonlinear boundary: nonlinearity matters when fiber behavior depends on the coarse base state, not merely because the fine formula contains powers/products.

## 5. Common coset support is weaker than action semantics

Even if every fiber support is a coset of the same subgroup, a uniform action defect need not exist.

Take

`X=Z/6`, `K={0,2,4}`, `Q=Z/2`, `T=Z/3`.

Define target values so that along the even coarse fiber the kernel translation `+2` acts as `+1` in T, while along the odd coarse fiber it acts as `-1`.

Both coarse fibers have the same MAY support: all of `Z/3`. Thus support-level compression sees the same subgroup H=T in both fibers.

But

`partial_2 t(x)`

is `+1` for even x and `-1` for odd x. It is not basepoint-independent, so there is no single homomorphism `phi:K->T` encoding target transport.

Therefore

`common support coset !=> action/witness homogeneity`.

A MAY-only task may use the compressed support. A task that must execute kernel actions or preserve witness transport must fail the derivative gate and retain richer typed semantics.

## 6. Defect representation ladder

The compiler now has a fail-closed nonlinear target ladder.

1. **Linear / translation-homogeneous target**: use a uniform group/module defect; in the p-adic linear case use the Structural Target missing-module and Smith profile.
2. **Support-coset target**: if only MAY semantics is required, a coarse-state coset bundle may compress the A4 correspondence.
3. **Arbitrary deterministic target, MAY semantics**: use the full A4 support correspondence `R_(q,t)`.
4. **COUNT/LABEL/witness semantics**: use typed monoid/weighted relation state.

State type is selected by the declared future semantics and the strongest proved structure gate, never by formula shape alone.

## 7. Ownership boundary

Generic relations/correspondences and their composition belong to A4; generic future-safe quotient minimality belongs to P023. R004's addition is only the reduction/fail-closed dispatch rule showing when its structured linear defect can be used and when the compiler must escalate back to A4.

This supplement deliberately avoids a new mother abstraction named "nonlinear defect algebra". The canonical nonlinear object was already present in the project as a relation/correspondence.

## 8. Next frontier

The remaining hard problem is **typed defect composition across representation changes**. Given successive collapses and targets,

`X -> Q -> R`,

when can a structured defect certificate be transported/composed without reopening fine state? Linear module defects, A4 correspondences and typed weighted relations each have composition laws, but a mixed certificate calculus must preserve which semantic layer each certificate belongs to.
