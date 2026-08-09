# P007 — Exact Quotient-Window Transport, Supplement 01

Status: `PROVED`  
Owner: A0 / P007 discrete-division core  
Pressure source: P017 L054 first-factor cofactor windows  
Discipline: only Euclidean integer division and integer inequalities are used; there is no novelty claim for floor division or interval arithmetic.

## 1. Why this moves from P017 back into P007

P017 repeatedly uses the consecutive-square cofactor window

\[
W_p(k)=\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L054 proves that these windows are strictly separated across distinct least-prime shells once `k>=4`.

The mechanism, however, does not require primes or squares. It is first an exact theorem about how an open-closed integer interval is transported into a quotient coordinate. That theorem belongs to P007/A0; L054 is a specialization.

## 2. Setup

Fix integers

\[
0\le A<B,
\qquad d\ge1.
\]

Let the source interval be

\[
I=(A,B]\cap\mathbb N_0
\]

and let

\[
M_d(q)=dq.
\]

P007 already provides the right adjoint

\[
M_d\dashv Q_d,
\qquad
Q_d(n)=n//d.
\]

Define the exact quotient window for factor `d` by

\[
\boxed{
W_d(A,B)=\{q\in\mathbb N_0:A<dq\le B\}.
}
\]

## 3. P007-S1-T09 — Exact quotient-window transport

Status: `PROVED`.

\[
\boxed{
W_d(A,B)
=
\left[
Q_d(A)+1,
Q_d(B)
\right]\cap\mathbb N_0.
}
\]

The window is empty when the left endpoint exceeds the right endpoint.

### Proof

For an integer `q`,

\[
A<dq
\iff
Q_d(A)<q,
\]

because `Q_d(A)` is the greatest integer `t` satisfying `dt<=A`.

On the other side, P007-T02 gives

\[
dq\le B
\iff
q\le Q_d(B).
\]

Hence

\[
A<dq\le B
\iff
Q_d(A)+1\le q\le Q_d(B).
\]

∎

### Interpretation

This is not a real interval `(A/d,B/d]` followed by an approximate rounding step. It is the exact inverse image of the discrete source interval under the multiplication coordinate `M_d`.

Factor stripping, cofactor windows, and quotient shells should therefore be normalized to this form before looser estimates are introduced.

## 4. P007-S1-T10 — Exact separation criterion for two quotient windows

Status: `PROVED`.

Let

\[
1\le d<e.
\]

When both windows are nonempty, the following are equivalent:

1. every state of `W_e(A,B)` is strictly below every state of `W_d(A,B)`;
2.
   \[
   \boxed{Q_e(B)\le Q_d(A).}
   \]

### Proof

By T09,

\[
\max W_e=Q_e(B),
\qquad
\min W_d=Q_d(A)+1.
\]

Strict separation is therefore

\[
Q_e(B)<Q_d(A)+1,
\]

which, for integers, is exactly `Q_e(B)<=Q_d(A)`. ∎

Thus shell separation can be compiled into a comparison of two integer endpoint states without enumerating either window.

## 5. P007-S1-T11 — Pure-integer cross-product sufficient condition

Status: `PROVED`.

If

\[
\boxed{dB\le eA,}
\]

then

\[
Q_e(B)\le Q_d(A),
\]

so the two windows are strictly separated.

### Proof

Take any integer `q` satisfying `eq<=B`. From `dB<=eA`,

\[
de q\le dB\le eA,
\]

and therefore `dq<=A`. Hence every integer admitted by `Q_e(B)` is also at most `Q_d(A)`. Taking `q=Q_e(B)` gives the result. ∎

No rational state needs to be introduced.

## 6. P007-S1-T12 — Exact gap resource

Status: `PROVED`.

When two nonempty windows are strictly separated, define the number of quotient states used by neither window between them by

\[
G_{d,e}(A,B)
=
\min W_d-\max W_e-1.
\]

Then

\[
\boxed{
G_{d,e}(A,B)
=Q_d(A)-Q_e(B)\ge0.
}
\]

Separation therefore carries an integer margin, not only a Boolean fact. That margin can be consumed by later packing or resource arguments.

## 7. Uniform specialization to the consecutive-square basin

Take

\[
A=k^2,
\qquad
B=k(k+2),
\qquad
1\le d<e\le k.
\]

The T11 cross-product condition becomes

\[
dk(k+2)\le ek^2,
\]

or equivalently

\[
\boxed{k(e-d)\ge2d.}
\]

### P007-S1-C01 — Spacing at least two automatically separates

If

\[
e-d\ge2,
\qquad d\le k,
\]

then

\[
k(e-d)\ge2k\ge2d,
\]

and therefore

\[
\boxed{W_e(k^2,k(k+2))<W_d(k^2,k(k+2)).}
\]

No primality hypothesis is used here.

## 8. P017 L054 is an immediate corollary

Let `p<r<=k` be primes and `k>=4`.

- if `p>=3`, both primes are odd and `r-p>=2`, so C01 applies;
- if `p=2` and `r>=5`, again the gap is at least two;
- the only adjacent-prime case is `(p,r)=(2,3)`, for which the condition is exactly `k>=4`.

Thus the P017 L054 threshold is recovered directly.

This shows that very little of L054 is specifically prime arithmetic. Apart from the `(2,3)` exception, prime spacing supplies the generic factor spacing required by the A0 quotient-window theorem.

## 9. Feedback into number-theory research practice

When an integer interval is split into candidate-factor shells, the default should not be to retain a two-dimensional label `(d,q)` or immediately replace exact windows by density bounds. A stronger order of operations is:

1. compile the exact quotient window by T09;
2. test cross-shell separation by T10/T11;
3. retain the integer separation margin from T12;
4. introduce a shell label, CRT residue, or other repair coordinate only where windows still collide.

This changes the research default from “count first” to “remove unnecessary state dimensions first.”

## 10. Relation to P024

The P007 adjunction `M_d ⊣ Q_d` is already an instance of the P008/P024 order-adjoint structure. This supplement uses a two-boundary interval query rather than one principal threshold; its two endpoints are transported exactly by integer quotient arithmetic.

T09 can therefore be read as:

> pull back the two boundaries exactly, then take the discrete atom between them.

P024 owns the general future boundary-pullback calculus; P007 keeps the concrete integer-division closed form.

## 11. Executable audit

- `src/enterprise_math/quotient_window.py`
- `tests/test_p007_quotient_window_transport.py`

The tests exhaust small integer intervals for T09, compare T10 against realized endpoints, verify that T11 never produces false separation, and pin the sharp P017 raw-window overlap at `k=3` and first uniform separation at `k=4`.

## 12. Prior-art and novelty discipline

Euclidean/floor division, integer interval endpoint arithmetic, and Galois adjunctions are mature mathematics. No novelty is claimed for those facts.

The project-specific contribution is to package them as a reusable **number-theoretic shell-window compiler** and to prove that P017 L054 is a specialization of this A0 tool rather than maintain it as an isolated Legendre-line argument.
