# Free Research — One-Variance Readout for the Stopped/Beta Block Defect

Status: `FREE_RESEARCH_FRONTIER / EXACT DEPTH-D TWO-MEASURE FOLD / SINGLE MIXTURE VARIANCE / FACTORIAL MASS BALANCE / DEPTH-FOUR SIX-CONTEXT COMPRESSION / VALUE-SENSITIVE COUPLING OPEN / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-05`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_FOUR_LEVEL_NORMAL_ORDERING_V18_20260905.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. Executive advance

The six contexts in the explicit formula for `L_4` need not be estimated separately. Their sum is, by definition, the difference between two positive endpoint measures:

\[
L_d f
=\ell U^df-d!\,\ell J^df.
\]

Here `U=I-S+J` is the positive stopped-history Markov operator, while `J^d` is the subprobability law of `d` successive valid quotient moves. In the ideal logarithmic Volterra model,

\[
\ell U^d=d!\ell J^d
\]

exactly, and both sides are the same Beta `(1,d)` endpoint probability.

At finite arithmetic cutoff, the entire depth-`d` defect is controlled by one positive variance on the sum of these two endpoint measures, plus their scalar mass imbalance. For `d=4`, this replaces six unrelated triangle estimates by a single four-history fold variance.

---

## 2. Positive endpoint measures

Fix a top cutoff `N`, normalized operators

\[
(S_Nf)(n)=A(n)f(n)/A(N),
\]

\[
(J_Nf)(n)=A(N)^{-1}
\sum_{a\le n}u_af(q_a(n)),
\]

and

\[
U_N=I-S_N+J_N.
\]

The operator `U_N` is Markov: at state `n`, it stays put with mass

\[
1-A(n)/A(N)
\]

and performs one valid quotient move with total mass

\[
A(n)/A(N).
\]

Let `ell_N` denote evaluation at the top state. Define endpoint measures by

\[
\int f\,d\mu_{N,d}:=(\ell_NU_N^d)f,
\tag{2.1}
\]

and

\[
\int f\,d\nu_{N,d}:=d!(\ell_NJ_N^d)f.
\tag{2.2}
\]

Then

\[
\boxed{L_{N,d}f=\int f\,d\mu_{N,d}-\int f\,d\nu_{N,d}.}
\tag{2.3}
\]

The first measure has exact mass

\[
\boxed{|\mu_{N,d}|=1.}
\tag{2.4}
\]

The second has mass

\[
\boxed{
|\nu_{N,d}|
=d!\frac{C_d(N)}{A(N)^d},
}
\tag{2.5}
\]

where

\[
C_d(N)=
\sum_{a_1\cdots a_d\le N}
\prod_{j=1}^d u_{a_j}.
\]

---

## SBV-T01 — Exact one-variance fold inequality

Put

\[
\sigma_{N,d}:=\mu_{N,d}+\nu_{N,d},
\qquad
m_{N,d}:=|\nu_{N,d}|.
\]

For every field bounded by `|f|<=B`, the general two-positive-measure inequality gives

\[
\boxed{
|L_{N,d}f|
\le
B|1-m_{N,d}|
+
\sqrt{
(1+m_{N,d})
\mathscr V_{\sigma_{N,d}}(f)
}.
}
\tag{3.1}
\]

No estimate has been placed on an individual normal-ordering term. Every cross covariance among the transported commutator contexts is retained automatically inside the single mixture variance.

---

## SBV-T02 — Fixed-depth factorial mass balance

The first-mass law

\[
A(x)=\log x+O(1)
\]

implies, for every fixed `d`,

\[
C_d(N)
=
\frac{(\log N)^d}{d!}
+O_d((\log N)^{d-1}).
\]

Therefore

\[
\boxed{
m_{N,d}=1+O_d(1/\log N).}
\tag{4.1}
\]

Combining with (3.1),

\[
\boxed{
|L_{N,d}f|
\le
O_d(B/\log N)
+
\sqrt{
\left(2+O_d(1/\log N)\right)
\mathscr V_{\sigma_{N,d}}(f)
}.
}
\tag{4.2}
\]

For depth four,

\[
\boxed{
L_{N,4}
=\ell_NU_N^4-24\ell_NJ_N^4,
}
\tag{4.3}
\]

and the six-context formula from the normal-ordering theorem is merely an expanded representation of this one signed measure.

---

## 5. Ideal Beta endpoint identity

In the continuum model

\[
(Sf)(t)=tf(t),
\qquad
(Jf)(t)=\int_0^tf(u)du,
\qquad
U=I-S+J,
\]

top evaluation satisfies

\[
(U^df)(1)=d!J^df(1).
\]

Both endpoint measures therefore have probability density

\[
\boxed{
d(1-t)^{d-1}\,dt,
\qquad0<t<1.}
\tag{5.1}
\]

For `d=4`, the common density is

\[
\boxed{4(1-t)^3dt.}
\tag{5.2}
\]

The finite arithmetic block defect is consequently a value-sensitive discrepancy between two realizations of one and the same ideal endpoint geometry.

---

## 6. Canonical four-action coupling

Both measures admit a common product-action realization on four independent top actions:

1. `mu_(N,4)` applies each action sequentially, retaining the current state whenever an action exceeds it;
2. `nu_(N,4)` restricts to the chamber in which all four actions are valid and gives that chamber multiplicity `24`.

On the all-valid chamber, both endpoint maps are

\[
q_{a_1a_2a_3a_4}(N),
\]

although their coefficients differ. The mixed stopping chambers supply the compensating mass in the ideal Volterra identity.

This common action lift is the correct carrier for the `S_4` Hoeffding/Gram calculation. It preserves every path label until after the fold variance is formed.

---

## 7. Relation to the six-context Gram theorem

The single variance (3.1) and the six-edge Gram theorem are complementary:

- the stopped/Beta formulation keeps exact cancellation among all six contexts;
- the `S_4` Gram formulation decomposes the remaining centered mixture variance into constant, additive and genuinely bi-centered relation sectors.

A coefficient-safe proof should first use (3.1), then apply the Gram decomposition to the common four-action lift. Reversing the order and applying six absolute-value estimates loses all useful cancellation.

---

## 8. Exact remaining target

Construct a chamberwise coupling or disintegration of `sigma_(N,4)` such that

\[
\mathscr V_{\sigma_{N,4}}(r)
\]

is bounded by:

1. the `S_4` bi-centered interaction energy with coefficient `13/64`;
2. the additive boundary sector with coefficient at most `293/576`;
3. fixed-order mass discrepancy `O(1/log N)`;
4. transported full residual energy `O(1/(log N)^2)`;
5. strict lower-scale moving-tail energy.

This is now the exact value-sensitive core of the four-level theorem.

---

## 9. Classification

Closed exactly or at fixed-depth asymptotic strength:

1. positive stopped endpoint measure;
2. positive factorial valid-history endpoint measure;
3. depth-`d` defect as their difference;
4. one-variance scalar inequality;
5. factorial mass balance;
6. ideal common Beta endpoint law;
7. compression of all six normal-ordering contexts to one signed fold.

Open:

1. arithmetic common-action disintegration of the mixture variance;
2. chamberwise S4 Hoeffding control;
3. additive boundary descent;
4. composition with the `567/625` Mellin block;
5. a promoted native logarithmic prime remainder.
