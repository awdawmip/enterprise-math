# P023 — Reductive Borrow, Supplement 04

Status: `ACTIVE RESEARCH NOTE`  
Scope: universal coarse-precision borrow formula for arbitrary reductive integer operations

## 1. Setup

Let

\[
T:\mathbb N\to\mathbb N
\]

be any operation satisfying

\[
T(n)\le n.
\]

Fix a positive precision ratio `r` and write

\[
n=qr+t,
\qquad
q=Q_r(n),
\qquad
0\le t<r.
\]

Define the reductive gap

\[
\boxed{
G_T(n)=n-T(n).
}
\]

No monotonicity, idempotence, or special arithmetic form of `T` is required for the identity below; reductivity alone is enough.

## 2. P023-T17 — Universal reductive precision-borrow identity

Define

\[
\boxed{
B_{T,r}(n)
=
\left(G_T(n)-t+r-1\right)//r.
}
\]

Then

\[
\boxed{
Q_r(T(n))=Q_r(n)-B_{T,r}(n).
}
\]

Equivalently,

\[
\boxed{
B_{T,r}(n)=Q_r(n)-Q_r(T(n)).
}
\]

Thus `B_(T,r)` is exactly the number of coarse `r`-fibers lost by the reductive operation.

### Proof

Since

\[
T(n)=n-G_T(n)=qr+t-G_T(n),
\]

we have

\[
Q_r(T(n))
=
q+\left(t-G_T(n)\right)//r.
\]

Because `0<=t<r` and `G_T(n)>=0`, the integer

\[
-\left(t-G_T(n)\right)//r
\]

is the ceiling of `(G_T(n)-t)/r`, represented without true division by

\[
\left(G_T(n)-t+r-1\right)//r.
\]

Hence the claimed identity follows.

## 3. P023-T18 — Gap-borrow state is the coarsest one-step repair

For the future coarse observable

\[
h(n)=Q_r(T(n)),
\]

consider the repaired state

\[
\boxed{
\widetilde q_T(n)=\left(Q_r(n),B_{T,r}(n)\right).
}
\]

Since

\[
h(n)=Q_r(n)-B_{T,r}(n),
\]

and conversely

\[
B_{T,r}(n)=Q_r(n)-h(n),
\]

the pair `(Q_r,B_(T,r))` induces exactly the same partition as `(Q_r,h)`.

By P023-T02,

\[
\boxed{
\widetilde q_T
\text{ is the coarsest refinement of }Q_r
\text{ through which }Q_rT\text{ descends.}
}
\]

This is a general canonical repair coordinate, not an arbitrary class label.

## 4. Relation to P018 subtraction borrow

P018-T05 proves the one-layer subtraction borrow for

\[
x-y.
\]

P023-T17 is a different, more general statement: any reductive transformation has an exact **coarse-fiber borrow count**, which may be larger than one.

The P018 subtraction bit is recovered in the special case where the fine subtraction can cross at most one current precision boundary.

Thus carry/borrow is not limited to elementary `+/-` arithmetic. It is a general language for how a reductive operation moves between finite precision fibers.

## 5. P007 multiple-collapse instance

For

\[
T=D_d,
\qquad
G_T(n)=n-D_d(n)=n\bmod d,
\]

we get

\[
\boxed{
B_{D_d,r}(n)
=
\bigl((n\bmod d)-(n\bmod r)+r-1\bigr)//r.
}
\]

Supplement 03 proves that, within each fixed `Q_r` fiber, this borrow count has at most two possible values and therefore the coarsest repair can be compressed further to one boundary-crossing bit.

## 6. P002 perfect-power collapse instance

For

\[
T=C_p,
\]

let the P002 collapse gap be

\[
G_p(n)=n-C_p(n).
\]

Then

\[
\boxed{
B_{p,r}(n)
=
\bigl(G_p(n)-(n\bmod r)+r-1\bigr)//r,
}
\]

and

\[
\boxed{
Q_r(C_p(n))=Q_r(n)-B_{p,r}(n).
}
\]

So the P002 basin gap acquires an exact P023/P018 interpretation:

> after subtracting the already-available within-fiber detail `n mod r`, the remaining gap tells exactly how many coarse precision fibers the perfect-power collapse crosses.

This does not replace the P002 gap; it transports that gap into precision dynamics.

## 7. Why this matters

Before P023, a large collapse gap and a precision borrow were separate-looking objects.

T17 shows that for every reductive integer operation they are linked by one exact decomposition:

\[
\boxed{
\text{reductive gap}
=
\text{within-fiber detail consumption}
+
\text{coarse-fiber borrow contribution}
}
\]

with the coarse contribution measured by `B_(T,r)`.

This gives P023 a direct arithmetic bridge into the existing P002/P007/P018 core and provides a reusable candidate for future collision/collapse dynamics.

## 8. Executable audit

- `src/enterprise_math/p023_reductive_borrow.py`
- `tests/test_p023_reductive_borrow.py`

The bounded reference tests check the identity for every pair `0<=T(n)<=n<120` across positive ratios below 15, plus explicit P007 multiple-collapse and perfect-power-collapse instances.
