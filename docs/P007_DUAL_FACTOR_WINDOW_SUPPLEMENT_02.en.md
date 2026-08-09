# P007 — Dual Factor-Window Transport, Supplement 02

Status: `PROVED RESEARCH NOTE`  
Owner: A0 / P007 discrete division  
Pressure source: P017 high-band root precision  
Discipline: Euclidean division and interval projection are established mathematics. The project contribution is the reusable finite-state transport interface and its downstream use.

## 1. Setup

Let

\[
0\le A<B
\]

and consider the multiplication incidence

\[
\boxed{A<dq\le B}
\]

for positive integers `d,q`.

P007 Supplement 01 fixes `d` and projects this incidence to the quotient coordinate:

\[
W_d(A,B)
=
\{q:A<dq\le B\}
=
\left[
\left\lfloor\frac A d\right\rfloor+1,
\left\lfloor\frac B d\right\rfloor
\right].
\]

The present supplement fixes a quotient bucket and projects the same incidence in the opposite direction.

## 2. P007-S2-T01 — Dual factor-window theorem

Status: `PROVED`.

Fix a positive integer quotient bucket

\[
J=[L,U],
\qquad
1\le L\le U.
\]

Define

\[
D_J(A,B)
=
\{d\ge1:W_d(A,B)\cap J\ne\varnothing\}.
\]

Then

\[
\boxed{
D_J(A,B)
=
\left[
\left\lfloor\frac A U\right\rfloor+1,
\left\lfloor\frac B L\right\rfloor
\right]
}
\]

when the displayed interval is nonempty, and is empty otherwise.

### Proof

The intersection is nonempty exactly when there exists `q` with

\[
L\le q\le U,
\qquad
A<dq\le B.
\]

Because multiplication by positive `d` is monotone in `q`, such a `q` exists exactly when the two endpoint conditions hold:

\[
A<dU,
\qquad
dL\le B.
\]

For integer `d`, these are equivalent to

\[
d\ge\left\lfloor\frac A U\right\rfloor+1,
\qquad
d\le\left\lfloor\frac B L\right\rfloor.
\]

This is the claimed closed integer window. ∎

## 3. P007-S2-T02 — Exact candidate cardinality

Status: `PROVED`.

If the dual window is nonempty, then

\[
\boxed{
|D_J(A,B)|
=
\left\lfloor\frac B L\right\rfloor
-
\left\lfloor\frac A U\right\rfloor.
}
\]

### Proof

The lower endpoint is `floor(A/U)+1` and the upper endpoint is `floor(B/L)`. The cardinality of a closed integer interval is upper minus lower plus one. ∎

This count is an exact **integer candidate resource**. If a later theorem requires `d` to be prime, rough, coprime, or otherwise admissible, those predicates must be imposed after the dual transport rather than silently built into the interval.

## 4. P007-S2-T03 — Root-basin factor window

Status: `PROVED`.

For the square-basin source interval

\[
(k^2,k(k+2)]
\]

and retained square-root index `s`, the quotient bucket is

\[
J_s=[s^2,(s+1)^2-1]=[s^2,s(s+2)].
\]

Therefore the positive factors whose raw quotient windows can hit root `s` are exactly

\[
\boxed{
D_{k,s}
=
\left[
\left\lfloor\frac{k^2}{s(s+2)}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{s^2}\right\rfloor
\right].
}
\]

This is the arithmetic source of the P017 high-band root-label window.

## 5. Incidence duality, not inverse reconstruction

The two P007 windows

\[
d\mapsto W_d(A,B)
\]

and

\[
J\mapsto D_J(A,B)
\]

are two projections of the same finite relation

\[
\mathcal R_{A,B}
=
\{(d,q):A<dq\le B\}.
\]

This does **not** say that quotienting is invertible. It says that once a quotient bucket is declared, the compatible factor labels can be transported exactly without enumerating the full source interval.

This distinction matters for future-safe precision: a retained quotient/root bucket induces a finite exact candidate set of hidden factor labels, while a separate admissibility predicate determines which candidates are physically or number-theoretically realized.

## 6. Research-tool interpretation

The theorem gives a reusable two-stage compiler:

1. **transport the envelope exactly** by the dual factor window;
2. **apply realizability/admissibility filters** only afterward.

Hence

\[
\boxed{
\text{exact envelope}
\neq
\text{realized state set in general}.
}
\]

Disjoint dual windows certify disjoint realized labels, but overlap of dual windows alone does not certify a realized collision.

## 7. Executable specification

- `src/enterprise_math/quotient_window.py`
- `tests/test_p007_dual_factor_window.py`

The tests exhaustively reconstruct the theorem on small integer intervals and verify that the factor-side and quotient-side views give the same incidence relation.

## 8. Prior-art discipline

The proof is elementary Euclidean-division interval arithmetic and is not claimed as new general mathematics. Enterprise Math uses it as a canonical finite transport primitive linking quotient precision, factor precision, root buckets, and later repair counting.
