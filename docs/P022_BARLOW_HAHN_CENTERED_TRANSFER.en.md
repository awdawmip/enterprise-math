# P022 Barlow — Fixed centered Hahn transfer at the q=18m-1 boundary

Status: **PROVED_WIP / exact matrix reduction / all-m nonvanishing still open**

Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Researcher: `EM-P022OBS-919781`

## 1. Input already accepted upstream

The accepted Hahn-diagonal reduction writes

\[
n=3m,\qquad p=6n-1=18m-1
\]

and identifies the surviving P022 arithmetic obstruction with

\[
H_n:=Q_n(n;-3n,n-1,3n)\equiv0\pmod p.
\]

The admissible P022 twin-boundary gate is

\[
3\mid n,\qquad 6n-1,\ 4n-1,\ 4n+1\ \text{prime}.
\]

This note does not re-prove that reduction. It starts from it and constructs
the matrix/second-order invariant requested by the previous live checkpoint.

For the standard Hahn polynomial the x-difference equation is (DLMF 18.22.10)

\[
A(x)Q(x+1)-(A(x)+C(x))Q(x)+C(x)Q(x-1)
-n(n+\alpha+\beta+1)Q(x)=0,
\]

with

\[
A(x)=(x+\alpha+1)(x-N),\qquad
C(x)=x(x-\beta-N-1).
\]

At

\[
\alpha=-3n,\qquad \beta=n-1,\qquad N=3n
\]

this becomes

\[
A(x)Q(x+1)+\bigl[-A(x)-C(x)+n^2\bigr]Q(x)+C(x)Q(x-1)=0
\]

with

\[
A(x)=(x-3n+1)(x-3n),\qquad C(x)=x(x-4n).
\]

Reference: DLMF §18.22(ii), equations 18.22.10–18.22.11.

## 2. Moving parameters disappear after centering

Put

\[
Y_s:=Q_n(n+s;-3n,n-1,3n).
\]

On the prime boundary `p=6n-1`,

\[
n\equiv\frac16\pmod p.
\]

Substituting `x=n+s` into the exact Hahn difference equation and then reducing
modulo `p` gives

\[
\boxed{A_sY_{s+1}+B_sY_s+C_sY_{s-1}=0}
\]

where

\[
\boxed{
A_s=(s-\tfrac13)(s+\tfrac23),\quad
B_s=\tfrac13-2s^2,\quad
C_s=(s-\tfrac12)(s+\tfrac16).
}
\]

The crucial point is that **no coefficient now depends on `n`**. The
moving-parameter Hahn diagonal has become a fixed rational second-order
difference equation; only the interval length remembers `n`.

Define

\[
V_s=\binom{Y_s}{Y_{s-1}},\qquad V_{s+1}=M_sV_s,
\]

with

\[
\boxed{
M_s=\begin{pmatrix}-B_s/A_s&-C_s/A_s\\1&0\end{pmatrix}.
}
\]

For the relevant steps `1-n <= s <= -1`, the original factors in `A(x)` are
nonzero modulo `p`, so every matrix is defined. Moreover

\[
\boxed{\det M_s=C_s/A_s.}
\]

On the same interval the original factors in `C(x)` are also nonzero modulo
`p`, hence the complete transfer is invertible.

## 3. Exact fixed initial vector

The hypergeometric definition gives `Q_n(0)=1`. At `x=1` the series has only
two terms, so

\[
Q_n(1)=1-\frac{n}{3(3n-1)}=\frac{8n-3}{3(3n-1)}.
\]

Using `n=1/6 (mod p)`,

\[
\boxed{Q_n(1)\equiv10/9\pmod p.}
\]

Let

\[
T_n:=M_{-1}M_{-2}\cdots M_{1-n}.
\]

Then

\[
V_{1-n}=\binom{Q_n(1)}{Q_n(0)}=\frac19\binom{10}{9}
\]

and therefore

\[
\boxed{T_n\binom{10}{9}=9\binom{Q_n(n)}{Q_n(n-1)}\pmod p.}
\]

Consequently the surviving P022 obstruction is exactly

\[
\boxed{Q_n(n)=0\iff e_1^{\mathsf T}T_n\binom{10}{9}=0\pmod p.}
\]

This is the requested genuinely matrix/second-order formulation. It is not a
second copy of the scalar Hasse logarithmic derivative. Because `T_n` is
invertible, a central zero automatically has `Q_n(n-1) != 0`; consecutive
central zeros are impossible.

## 4. Universal local crossing law at a putative zero

Assume `Y_0=Q_n(n)=0`. Evaluate the fixed recurrence at `s=-1,0,1`. One obtains

\[
\boxed{
\frac{Y_{-2}}{Y_{-1}}=\frac43,\qquad
\frac{Y_1}{Y_{-1}}=-\frac38,\qquad
\frac{Y_2}{Y_1}=\frac32\pmod p.
}
\]

Thus every hypothetical boundary zero crosses the center through the **same
projective direction**, independent of `m,n,p`. The unresolved question is no
longer an unspecified moving Hahn zero: it is whether the fixed transfer orbit
issued from `(10:9)` can hit this universal central-zero direction at an
admissible length `n=3m`.

This is the smallest exact exceptional condition obtained in this execution.

## 5. Why the obvious Hasse second-jet Casoratian is not independent

The previous live checkpoint proved the formal-adjoint relation between the
original Hasse period `P` and its conjugate `D`, together with

\[
81\theta^2P+36\theta P+5P=0,\qquad
81\theta^2D+36\theta D+4D=0,
\]

and, on the boundary-zero ordinary locus,

\[
\theta P/P=-5/27,\qquad \theta D/D=-4/27.
\]

Hence

\[
\theta^2P/P=5/243,\qquad \theta^2D/D=4/243.
\]

The first cross determinant is

\[
P\theta D-\theta P D=PD/27,
\]

so it carries no information beyond the scalar first jets. Worse, the
apparently more second-order determinant satisfies

\[
\boxed{\theta P\theta^2D-\theta^2P\theta D=0}
\]

identically on the same obstruction locus. Therefore the naive scalar-Hasse
2x2 Casoratian route is rigorously killed: it is still a scalar adjoint
consequence, not the independent matrix invariant sought by the checkpoint.

The centered Hahn transfer survives this kill because its state space is the
discrete `x`-evolution, not the two adjoint scalar jets at a single `z`-point.

## 6. Direct conductor-18 contact after three-step blocking

The one-step determinant is

\[
\det M_s=\frac{(s-\tfrac12)(s+\tfrac16)}{(s-\tfrac13)(s+\tfrac23)}.
\]

For a three-section step `s=3t+a`, `a in {0,1,2}`,

\[
\det M_{3t+a}=
\frac{(t+\tfrac a3-\tfrac16)(t+\tfrac a3+\tfrac1{18})}
{(t+\tfrac a3-\tfrac19)(t+\tfrac a3+\tfrac29)}.
\]

Thus blocking the fixed Hahn transfer by residue class mod 3 naturally raises
the fractional scale to denominator 18. This is a precise determinant-level
contact with the conductor-18 three-section route frozen in the previous
execution.

This statement is deliberately limited: the rank-two determinant data do not
by themselves identify the full rank-nine conductor-18 Frobenius system. The
next proof-level step, if pursued, is to compute the **full three-step matrix**
(or an equivalent Cartier/Hasse-Witt off-diagonal block), not just its
determinant, and test the fixed central-zero direction against admissible
Frobenius transport.

## 7. Regression and falsification controls

The task-local checker directly compares the hypergeometric Hahn diagonal with
the fixed transfer.

Controls:

- the unrestricted known zero `n=25,p=149` is detected exactly by both
  descriptions;
- all tested prime boundaries `n in {1,2,3,4,5,7,8,9,25}` satisfy the exact
  transfer/Hahn equality;
- among the 13 admissible P022 boundaries with `3|n`, `n<=500`, the equality
  has zero failures and no diagonal zero occurs;
- an additional research-time scan through `n<=5000` found 64 admissible
  boundaries, zero transfer/Hahn mismatches, and zero admissible zeros.

The finite scans are regression/falsification evidence only. They are not an
all-`m` nonvanishing proof.

## 8. Frozen frontier

What is proved:

1. the moving Hahn x-equation collapses at `p=6n-1` to one universal
   second-order recurrence;
2. the P022 obstruction is exactly one entry of a fixed 2x2 transfer product
   applied to the fixed projective seed `(10:9)`;
3. that transfer is invertible on the whole relevant interval;
4. a hypothetical zero has the universal local crossing ratios
   `4/3,-3/8,3/2`;
5. the obvious scalar Hasse second-jet Casoratian is redundant and should not
   be retried;
6. mod-3 blocking of the transfer exposes denominator-18 structure, giving a
   concrete bridge to the conductor-18 route.

What remains open is

\[
e_1^{\mathsf T}T_{3m}\binom{10}{9}\ne0
\]

for every admissible `18m-1, 12m-1, 12m+1` prime.

The recommended continuation is a full three-step transfer/Frobenius matrix
analysis or an equivalent Cartier block determinant. A larger finite census
is not a substitute.
