# P018 — Finite-Precision Proof Calculus

Status: `ACTIVE RESEARCH NOTE`  
Issue: `P018 / #34`  
Scope: finite precision as a first-class mathematical coordinate  
Discipline: **precision is not treated here as an error bar around a hidden real number.**

## 1. Research thesis

Enterprise Math starts from finite numerical states.  A state at one precision can be projected to a coarser precision, but that projection is many-to-one.  Refinement therefore does not mean recovering a unique hidden value.  It means exposing additional finite state information.

P018 studies the algebra and proof theory of that information change.

The central pattern is

\[
\boxed{
\text{fine state}
=
\text{transported coarse state}
+
\text{bounded precision detail}.
}
\]

The project then asks:

- when can a proposition be proved at a low precision and remain permanently proved at all later refinements?
- when low-precision parts agree, can they be cancelled so that only the new precision shell remains?
- how do carries and borrows transmit information between precision layers?
- which operations commute with precision projection, and when they do not, is the defect itself an exact finite state?

No limit `d -> infinity` is part of the core construction.

## 2. Precision scale

Use positive integer precision factors ordered by divisibility:

\[
d\preceq e
\iff
d\mid e.
\]

When `d|e`, write

\[
r=e/d.
\]

The canonical projection of a fine integer state `x` to precision `d` is

\[
\pi_{e\to d}(x)=x\operatorname{//}r.
\]

Define its **precision detail** by

\[
\delta_{e:d}(x)=x\bmod r.
\]

This is Euclidean division used as a state decomposition, not as an approximation theorem.

## 3. P018-T01 — Precision fiber decomposition

Status: `PROVED`

For every `d|e` and `x in N`,

\[
\boxed{
x
=r\pi_{e\to d}(x)+\delta_{e:d}(x),
\qquad
0\le\delta_{e:d}(x)<r.
}
\]

The pair

\[
\bigl(\pi_{e\to d}(x),\delta_{e:d}(x)\bigr)
\]

is unique.

Thus the fiber over a coarse state `a` is exactly

\[
\{ra,ra+1,\ldots,ra+r-1\}.
\]

The detail is not postulated to survive a physical collapse.  It is a relation between two explicit precision states when both are under consideration.

## 4. P018-T02 — Nested detail composition

Status: `PROVED`

Let

\[
d\mid e\mid f,
\qquad
r=e/d,
\qquad
s=f/e.
\]

For a state `x` at precision `f`, let

\[
u=\delta_{e:d}(\pi_{f\to e}(x)),
\qquad
v=\delta_{f:e}(x).
\]

Then

\[
\boxed{
\delta_{f:d}(x)=s u+v.
}
\]

Proof: write

\[
\pi_{f\to e}(x)=ra+u,
\qquad
x=s(ra+u)+v.
\]

Therefore

\[
x=rs a+(su+v),
\]

and `0<=su+v<rs`. ∎

This is the first exact form of **nested precision detail**: old detail is transported upward and the next layer contributes only its new bounded remainder.

## 5. P018-T03 — Coarse-order proof stability

Status: `PROVED`

Let `d|e` and let `x,y` be explicit states at precision `e`.

If

\[
\pi_{e\to d}(x)<\pi_{e\to d}(y),
\]

then

\[
\boxed{x<y.}
\]

Indeed, if `a<b`, then

\[
ra+u\le ra+r-1<r(a+1)\le rb\le rb+v.
\]

Hence a strict order certificate obtained at a coarse precision cannot be overturned by resolving finer detail inside the two already separated fibers.

If instead

\[
\pi_{e\to d}(x)=\pi_{e\to d}(y),
\]

then the common transported coarse term cancels exactly and

\[
\boxed{
x<y
\iff
\delta_{e:d}(x)<\delta_{e:d}(y).
}
\]

So order proof has a finite refinement rule:

1. compare the coarse fibers;
2. stop permanently if they separate;
3. otherwise cancel the common coarse state and pass the proof obligation to the detail layer.

This is the first precise meaning of **proof by increasing precision** in P018.

## 6. P018-T04 — Addition carry across precision

Status: `PROVED`

Write

\[
x=ra+u,
\qquad
y=rb+v,
\qquad0\le u,v<r.
\]

Define

\[
c=(u+v)\operatorname{//}r,
\qquad
t=(u+v)\bmod r.
\]

Because `u+v<2r`,

\[
c\in\{0,1\}.
\]

Then

\[
\boxed{
x+y=r(a+b+c)+t.}
\]

Equivalently,

\[
\boxed{
\pi(x+y)=\pi(x)+\pi(y)+c.
}
\]

The inter-level carry `c` is not numerical error.  It is the exact event by which two fine details change the coarse arithmetic result.

## 7. P018-T05 — Subtraction borrow across precision

Status: `PROVED`

For `x>=y`, with the same decompositions above, define

\[
b=\mathbf 1_{u<v}.
\]

Then

\[
\boxed{
x-y=r(a-b'-b)+(u-v+br),}
\]

where `b'` denotes the coarse state of `y` (that is, use `a` and the coarse quotient of `y` in the obvious notation).

More transparently, if `A=pi(x)` and `B=pi(y)`,

\[
\boxed{
\pi(x-y)=A-B-b,
}
\]

and

\[
\delta(x-y)=u-v+br.
\]

Thus borrow is the subtraction-dual of precision carry.

## 8. P018-T06 — Precision-chain telescoping

Status: `PROVED`

Let

\[
d_0\mid d_1\mid\cdots\mid d_m
\]

and let `x_i` be the projection of one final state `x_m` to precision `d_i`.

Write

\[
x_i=(d_i/d_{i-1})x_{i-1}+\delta_i.
\]

Then

\[
\boxed{
x_m
=\frac{d_m}{d_0}x_0
+\sum_{i=1}^{m}\frac{d_m}{d_i}\delta_i.}
\]

Every term is an integer.

This is a finite mixed-radix / telescoping proof decomposition.  If two expressions have equal transported contributions through some level, those common layers cancel and only the first unequal detail layer remains relevant to their order.

## 9. Precision is a lattice, not only a chain

P005 independently identifies positive scale factors with the divisibility lattice:

- `gcd(d,e)` is the greatest common coarsening;
- `lcm(d,e)` is the least common refinement;
- canonical projections commute along divisibility paths.

P018 therefore needs a shell calculus that works on the whole divisor lattice, not only on one chosen chain.

## 10. P018-T07 — Transported Möbius precision shell

Status: `PROVED`

Let `A(d)` be an integer-valued quantity attached to every divisor scale of `d` and suppose it has scale degree one, so a value at scale `c|d` is transported to scale `d` by multiplication by `d/c`.

Define the **transported precision shell**

\[
\boxed{
\widehat A(d)
=
\sum_{c\mid d}
\mu(d/c)\frac{d}{c}A(c).
}
\]

Then exact divisor-poset Möbius inversion gives

\[
\boxed{
A(d)
=
\sum_{c\mid d}
\frac{d}{c}\widehat A(c).
}
\]

Proof:

\[
\sum_{c\mid d}\frac dc\widehat A(c)
=
\sum_{a\mid d}A(a)\frac da
\sum_{b\mid d/a}\mu(b),
\]

and the inner Möbius sum is zero unless `a=d`. ∎

Unlike adjacent-chain details, lattice shells are signed.  Their purpose is cancellation across overlapping precision paths.

## 11. P018-T08 — Scale-linear bulk annihilation

Status: `PROVED`

If

\[
A(c)=cA(1)
\]

for all `c|d`, then for every `d>1`,

\[
\boxed{\widehat A(d)=0.}
\]

Indeed,

\[
\widehat A(d)
=dA(1)\sum_{c\mid d}\mu(d/c)=0.
\]

This gives a precise algebraic version of **high/low precision cancellation**:

> anything that merely scales linearly with precision disappears from every nontrivial precision shell; the shell records only genuine precision-dependent deviation.

This is standard Möbius inversion applied with an Enterprise Math transport rule, not a claim that Möbius inversion itself is new.

## 12. Root precision states

Define, independently of any hidden real root,

\[
S_{p,d}(n)=R_p(nd^p).
\]

This is the same scale-factor root construction studied in P005.

## 13. P018-T09 — Root precision detail

Status: `PROVED`

For `d|e`, `r=e/d`,

\[
\boxed{
S_{p,e}(n)=rS_{p,d}(n)+\eta_{e:d}^{(p)}(n),
\qquad
0\le\eta_{e:d}^{(p)}(n)<r.
}
\]

Proof: let `k=S_(p,d)(n)`. Then

\[
k^p\le nd^p<(k+1)^p.
\]

Multiplying by `r^p` gives

\[
(rk)^p\le ne^p<(r(k+1))^p.
\]

Therefore

\[
rk\le S_{p,e}(n)<r(k+1),
\]

which is exactly the claimed fiber decomposition. ∎

The root detail inherits T02's nested composition law.

## 14. P018-T10 — Root precision shell isolates only refinement detail

Status: `PROVED`

Let

\[
k=S_{p,1}(n)
\]

and define the base-relative detail

\[
\eta_d=S_{p,d}(n)-dk.
\]

Then for every `d>1`,

\[
\boxed{
\widehat S_p(d)
=
\sum_{c\mid d}\mu(d/c)\frac dc\eta_c.
}
\]

The transported coarse root bulk `ck` disappears by T08.

Thus the nontrivial precision shell of an integer-root family contains **only information created by refinement**.

The shell need not be nonnegative.  For example, for `n=2`, `p=2`, the shell at scale `12` is

\[
\widehat S_2(12)=-3.
\]

Signed shell values are therefore genuine cancellation observables, not counts of newly created states.

## 15. Collapse at a precision

Define

\[
C_{p,d}(n)=S_{p,d}(n)^p.
\]

For `d|e`, `r=e/d`, define the **fine-collapse recovery projected to d** by

\[
\mathcal R_{p;e\to d}(n)
=
C_{p,e}(n)\operatorname{//}r^p.
\]

This compares two different orders of operations:

\[
\text{coarse then collapse}
\qquad\text{versus}\qquad
\text{refine, collapse, project back}.
\]

They do not generally commute.

## 16. P018-T11 — Collapse/refinement defect is a basin coordinate

Status: `PROVED`

Let

\[
k=S_{p,d}(n).
\]

Then

\[
\boxed{
C_{p,d}(n)
\le
\mathcal R_{p;e\to d}(n)
\le
(k+1)^p-1.
}
\]

Hence the commutation defect

\[
\chi_{p;e:d}(n)
=
\mathcal R_{p;e\to d}(n)-C_{p,d}(n)
\]

satisfies

\[
\boxed{
0\le\chi_{p;e:d}(n)
\le
(k+1)^p-k^p-1.
}
\]

Proof: T09 writes

\[
S_{p,e}(n)=rk+\eta,
\qquad0\le\eta<r.
\]

Therefore

\[
r^pk^p
\le
S_{p,e}(n)^p
<
r^p(k+1)^p.
\]

Integer division by `r^p` gives the result. ∎

The upper bound is exactly the sharp coarse-basin gap bound studied in P002.

So failure of collapse/refinement commutation is not an uncontrolled approximation error.  It is an exact state coordinate inside the original coarse collapse basin.

### Explicit noncommutation

For `n=3`, `p=2`, `d=1`, `e=10`,

\[
C_{2,1}(3)=1,
\]

but

\[
S_{2,10}(3)=17,
\qquad
17^2\operatorname{//}100=2.
\]

Thus

\[
\chi_{2;10:1}(3)=1.
\]

## 17. P018-T12 — Refinement recovery is monotone

Status: `PROVED`

Let

\[
d\mid e\mid f.
\]

Then

\[
\boxed{
\mathcal R_{p;e\to d}(n)
\le
\mathcal R_{p;f\to d}(n).
}
\]

Proof: write `s=f/e`. Root scale compatibility gives

\[
S_{p,f}(n)=sS_{p,e}(n)+\zeta,
\qquad\zeta\ge0.
\]

Hence

\[
S_{p,f}(n)^p\ge s^pS_{p,e}(n)^p.
\]

Projecting degree-`p` states from `f` to `d` proves the inequality. ∎

Therefore, along every finite refinement chain,

\[
C_{p,d}(n)
=
\mathcal R_{p;d\to d}(n)
\le
\mathcal R_{p;e_1\to d}(n)
\le\cdots.
\]

The increments

\[
\Delta_i
=
\mathcal R_{p;e_i\to d}(n)
-
\mathcal R_{p;e_{i-1}\to d}(n)
\]

are nonnegative integers and telescope exactly:

\[
\sum_i\Delta_i
=
\mathcal R_{p;e_m\to d}(n)-C_{p,d}(n).
\]

This is a second, operation-specific meaning of precision shells: higher precision can recover additional coarse-basin state without erasing already recovered state.

## 18. What P018 does not say

### CE01 — coarse projection has no state-only inverse

P005 already gives a direct counterexample: the same coarse root state may correspond to different finer root states.  Refinement therefore requires either the retained source state or genuinely new information.

### CE02 — refine/collapse/project is not coarse collapse

The `n=3`, square-root, scale-10 example above disproves exact commutation.

### CE03 — lattice precision shells are not nonnegative

`n=2`, `p=2`, `d=12` gives shell `-3`.

### CE04 — local detail does not have to increase

For `n=2`, `p=2` along

\[
1\mid2\mid4\mid8\mid16,
\]

the successive local root details are

\[
0,1,1,0.
\]

The cumulative recovery observable of T12 is monotone; individual local digits/details are not.

This distinction is essential.  “More precision” is not the statement that every local remainder numerically grows.

## 19. Relation to P017

P017 repeatedly produced the pattern

\[
\text{bulk}
+
\text{carry/shell residual}.
\]

Examples include:

- Euclidean basin descent: deterministic quotient bulk plus a bounded local carry;
- Möbius carry identity: the bulk sum collapses and only signed carries remain;
- cutoff pairing: interior terms cancel and only cutoff-crossing shell edges remain;
- Alexander descent: a large threshold problem is transferred to a smaller precision/scale region.

P018 does **not** yet prove that P017 is literally an instance of one universal precision functor.  But T07–T12 provide a concrete language in which that claim can now be tested rather than asserted metaphorically.

A major next target is therefore:

> rewrite one nontrivial P017 identity entirely as a transported precision-shell identity and identify exactly which term is the precision-changing defect.

## 20. Prior-art boundary

Several mature theories are close to parts of P018:

- Euclidean quotient/remainder and Galois/right-adjoint floor projection are classical;
- filtered objects and associated graded constructions are established algebraic language for separating successive layers;
- multiresolution analysis explicitly studies information added between resolution levels;
- interval arithmetic proves statements using finite enclosures and can refine those enclosures;
- p-adic computation has sophisticated precision propagation, including lattice-valued precision;
- Möbius inversion on divisor posets is classical.

P018 therefore makes no priority claim for any of those ingredients.

The project-specific research question is whether the following finite-only package is useful as one coherent proof calculus:

\[
\boxed{
\text{divisibility precision lattice}
+
\text{many-to-one projection}
+
\text{bounded detail/carry}
+
\text{proof stability}
+
\text{transported signed shells}
+
\text{collapse/refinement recovery}.
}
\]

No historical-novelty claim is made.  Status remains `NOVELTY_UNVERIFIED` pending a dedicated source registration and comparison pass.

## 21. Stage-1 status

- P018-T01 precision fiber decomposition: `PROVED`
- P018-T02 nested detail composition: `PROVED`
- P018-T03 coarse-order proof stability: `PROVED`
- P018-T04 addition carry: `PROVED`
- P018-T05 subtraction borrow: `PROVED`
- P018-T06 chain telescoping: `PROVED`
- P018-T07 transported precision-shell inversion: `PROVED`
- P018-T08 scale-linear bulk annihilation: `PROVED`
- P018-T09 root precision detail: `PROVED`
- P018-T10 root shell isolates refinement detail: `PROVED`
- P018-T11 collapse/refinement defect lies in the coarse basin: `PROVED`
- P018-T12 refinement recovery monotonicity: `PROVED`
- universal proof calculus for arbitrary predicates/operations: `OPEN`
- exact equivalence with the P017 shell machinery: `OPEN`
- historical novelty of the integrated package: `NOVELTY_UNVERIFIED`

Executable integer-only checks live in `src/enterprise_math/precision.py` and `tests/test_precision.py`.
