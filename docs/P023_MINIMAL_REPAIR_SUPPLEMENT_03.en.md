# P023 — Minimal Arithmetic Repair, Supplement 03

Status: `ACTIVE RESEARCH NOTE`  
Scope: canonical one-bit repair for an unsafe `Q_r` precision quotient under same-space multiple collapse `D_d`

## 1. Setup

Fix positive integers `r,d`.

The coarse precision state is

\[
q=Q_r(n)=n//r,
\qquad
n=qr+t,
\qquad
0\le t<r.
\]

The future coarse observable is

\[
h(n)=Q_r(D_d(n)).
\]

P023-T09 classifies when `h` already descends through `q`. This supplement asks for the **coarsest repair when it does not**.

## 2. Boundary phase of a precision fiber

Define

\[
\boxed{
b_q=(qr)\bmod d.
}
\]

If `b_q=0`, the left endpoint of the `q`-th `r`-fiber is itself a `d`-multiple.

If `b_q>0`, the next `d`-multiple after `qr` occurs at offset

\[
\boxed{
\tau_q=d-b_q.
}
\]

inside or beyond the fiber.

The fiber splits exactly when

\[
0<\tau_q<r.
\]

## 3. P023-T15 — One-bit coarsest repair

Define the boundary-crossing bit

\[
\beta_{r,d}(n)=
\begin{cases}
1,&0<\tau_q<r\text{ and }t\ge\tau_q,\\
0,&\text{otherwise},
\end{cases}
\]

where `q=n//r` and `t=n-qr`.

Then

\[
\boxed{
\widetilde q(n)=\bigl(q,\beta_{r,d}(n)\bigr)
}
\]

is exactly the coarsest one-step repair of `Q_r` for the observable `Q_rD_d`.

Equivalently, for states `x,y` in the same `Q_r` fiber,

\[
\boxed{
\beta_{r,d}(x)=\beta_{r,d}(y)
\iff
Q_r(D_d(x))=Q_r(D_d(y)).
}
\]

### Proof

Inside one interval

\[
[qr,(q+1)r-1],
\]

`D_d(n)` changes only when a `d`-multiple is crossed.

If `d<r`, several `d`-multiples may lie in the fiber, but `D_d(n)` differs from `n` by less than `d<r`; therefore its `Q_r` image can only be `q-1` or `q`. The first `d`-multiple at or above `qr` is the unique threshold at which the coarse outcome changes from `q-1` to `q`.

If `d>r`, an `r`-fiber contains at most one interior `d`-multiple, so again there are at most two coarse outcomes, separated by the same threshold `\tau_q`.

If `d=r`, or more generally if the fiber does not contain an interior boundary, the outcome is constant and the canonical bit is zero.

Thus `(q,\beta)` and `(q,h)` induce the same partition. P023-T02 then proves coarsestness.

### Consequence

Full Euclidean remainder `t in {0,...,r-1}` is generally **more detail than needed** for this one-step repair. A single bounded bit is sufficient and minimal on every splitting fiber.

## 4. P023-T16 — Period and exact split-fiber count

Let

\[
g=\gcd(r,d).
\]

The phase sequence

\[
b_q=(qr)\bmod d
\]

has period

\[
\boxed{
P=\frac d g.
}
\]

Over one period it visits every multiple of `g` in

\[
\{0,g,2g,\ldots,d-g\}
\]

exactly once.

A coarse fiber splits exactly when

\[
0<d-b_q<r.
\]

Counting such phases gives

\[
\boxed{
S(r,d)
=
\frac{\min(r,d)}{\gcd(r,d)}-1.
}
\]

Therefore:

\[
S(r,d)=0
\iff
\min(r,d)=\gcd(r,d)
\iff
r\mid d\text{ or }d\mid r.
\]

So P023-T09 is recovered as the zero-splitting case of the stronger periodic repair theorem.

## 5. Proof of the count

The map

\[
q\mapsto qr\pmod d
\]

on `q mod d/g` visits each multiple of `g` once because `r/g` is invertible modulo `d/g`.

### If `d<r`

Every nonzero phase splits, so the count is

\[
\frac d g-1.
\]

### If `d>r`

Write `r=gR`, `d=gD`. A phase `kg` splits exactly when

\[
kg>d-r=g(D-R),
\]

with `1<=k<=D-1`. Hence `k=D-R+1,...,D-1`, giving exactly

\[
R-1=\frac r g-1
\]

splitting residues.

Both cases equal `min(r,d)/g-1`.

## 6. Precision-calculus interpretation

This is the first P023 example where the minimal repair detail is not an arbitrary partition label but a canonical bounded integer coordinate derived from an existing P018-style remainder geometry.

The hierarchy is:

\[
\text{coarse quotient }q
\quad+\quad
\text{one boundary bit }\beta
\]

rather than

\[
\text{coarse quotient }q
\quad+\quad
\text{full remainder }t.
\]

Thus P023 begins to quantify **how much** precision detail is actually required by a future operation.

## 7. Executable audit

- `src/enterprise_math/p023_minimal_repair.py`
- `tests/test_p023_minimal_repair.py`

Independent exhaustive checking over all positive `r,d<50` verified the split-count formula and the exact equivalence between the repair bit partition and the projected `D_d` output partition over repeated phase periods. This bounded check is supporting evidence, not a substitute for the proof above.
