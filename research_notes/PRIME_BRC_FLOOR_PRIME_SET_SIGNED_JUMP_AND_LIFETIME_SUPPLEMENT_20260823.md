# Prime-BRC Floor-Prime-Set Signed Jump and Branch Lifetime Supplement

Status: `L3 OWNER-LOCAL / PROVED ELEMENTARY THEOREM / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

Depends on owner-local note:

`research_notes/PRIME_BRC_FLOOR_PRIME_SET_ODD_JUMP_THEOREM_20260823.md`.

## 1. Setup

For `x>=1`, define

\[
\mathcal G(x)=\left\{\left\lfloor\frac{x}{n}\right\rfloor:1\le n\le x\right\},
\qquad
G(x)=|\mathcal G(x)\cap\mathbb P|.
\]

For `m>=1`, define the exact membership multiplicity

\[
J_x(m)=
\left\lfloor\frac{x}{m}\right\rfloor
-
\left\lfloor\frac{x}{m+1}\right\rfloor.
\]

Then

\[
m\in\mathcal G(x)\iff J_x(m)>0.
\]

The one-step signed carry law is

\[
\boxed{
J_x(m)-J_{x-1}(m)
=
\mathbf1_{m\mid x}-\mathbf1_{m+1\mid x}.
}
\]

## 2. Exact prime-entry criterion

Let `p` be prime.

A new prime value `p` enters `\mathcal G(x)` at the step `x-1 -> x` iff

\[
\boxed{
p\mid x,\qquad \frac{x}{p}\le p.}
\]

Equivalently,

\[
\boxed{p\mid x,\qquad p^2\ge x.}
\]

### Proof

Write `x=ap`. Then

\[
J_{x-1}(p)
=a-1-
\left\lfloor\frac{ap-1}{p+1}\right\rfloor.
\]

Since `(ap-1)/(p+1)<a`, this is zero iff

\[
(a-1)(p+1)\le ap-1,
\]

which reduces exactly to `a<=p`.

In this range `p+1` cannot also divide `x`, so the signed carry is `+1` and `J_x(p)=1`.

## 3. Exact prime-loss criterion

A prime value `p` leaves `\mathcal G(x)` at the step `x-1 -> x` iff

\[
\boxed{
p+1\mid x,\qquad \frac{x}{p+1}<p.}
\]

### Proof

Write

\[
x=a(p+1).
\]

Then

\[
J_x(p)
=\left\lfloor\frac{a(p+1)}p\right\rfloor-a
=\left\lfloor\frac ap\right\rfloor.
\]

Thus `J_x(p)=0` iff `a<p`. In that range `p` cannot divide `x`, so the signed carry is `-1`, hence `J_{x-1}(p)=1`.

## 4. Exact all-integer jump theorem

Define

\[
E(x)=
\#\left\{p\in\mathbb P:p\mid x,\ \frac{x}{p}\le p\right\},
\]

\[
L(x)=
\#\left\{p\in\mathbb P:p+1\mid x,\ \frac{x}{p+1}<p\right\}.
\]

Then for every integer `x>=2`,

\[
\boxed{
G(x)-G(x-1)=E(x)-L(x).
}
\]

The entry and loss criteria above are disjoint for a fixed prime `p`, and every change of prime membership is accounted for by the signed carry law.

This strictly strengthens the odd-only jump theorem: for odd `x>=5`, every odd-prime loss is parity-forbidden; the only even prime `2` never actually leaves once `x>=5`. Hence `L(x)=0` at the membership level and the prior odd theorem follows.

## 5. Entry-exit pairing and finite branch lifetime

Let `p` be prime and let

\[
x_0=ap,
\qquad 1\le a<p.
\]

Then `p` enters at `x_0` and remains present for exactly `a` consecutive values:

\[
\boxed{
p\in\mathcal G(ap+t)\quad(0\le t<a),}
\]

while

\[
\boxed{p\notin\mathcal G(a(p+1)).}
\]

Thus the branch interval is

\[
\boxed{[ap,\ a(p+1)-1]}
\]

and its exact lifetime is

\[
\boxed{\operatorname{life}(p;a)=a.}
\]

For `0<=t<a`, the witness denominator `a` gives

\[
\left\lfloor\frac{ap+t}{a}\right\rfloor=p.
\]

At `a(p+1)`, the loss criterion applies because `a<p`.

### Square-boundary exception

If `a=p`, so `x_0=p^2`, the prime `p` enters at the exact square-root boundary but does **not** have the finite lifetime law above. In fact the zero-membership intervals for `p` occur only for quotient index `<p`; after `x>=p^2`, `p` never leaves `\mathcal G(x)`.

This distinction is essential when translating the theorem back to open consecutive-square basins, which contain no perfect squares.

## 6. Consecutive-square specialization

Let

\[
K^2<n<(K+1)^2,
\]

with `n` odd. Since `n` is not a square, any prime divisor `q` with

\[
q^2\ge n
\]

actually satisfies `q>\sqrt n>K`.

Write

\[
n=a q,
\qquad a<q.
\]

Then the new large prime branch `q` has exact lifetime

\[
\boxed{\operatorname{life}(q)=a=n/q.}
\]

Using the canonical P017 smooth-tail decomposition `n=S_K(n)Q_K(n)`:

- if `n` is prime, then `Q_K(n)=n`, `S_K(n)=1`, and the new branch has lifetime `1`;
- if `n` is a large-prime-tail composite, then `Q_K(n)=q>K`, `S_K(n)=a>1`, and the branch lifetime is exactly the smooth core `S_K(n)`;
- if `n` is fully `K`-smooth, no prime divisor lies above the square-root frontier and no new large-prime branch enters at `n`.

Therefore, on odd non-square states in the square basin, one-step future persistence yields the exact three-way classification

\[
\boxed{
\begin{array}{c|c}
\text{new large-prime branch at }n? & \text{persists to }n+1?\\ \hline
0&0\quad\text{fully }K\text{-smooth composite}\\
1&0\quad\text{prime}\\
1&1\quad\text{large-prime-tail composite}.
\end{array}}
\]

Thus the current entry bit alone merges prime and large-tail composite, while one successor-persistence bit repairs the ambiguity exactly.

## 7. BRC interpretation

This is a concrete R023-style one-step repair example.

The coarse current observable is

\[
E_n=\mathbf1\{\text{a new prime-valued floor branch enters at }n\}.
\]

It is insufficient because `E_n=1` for both prime states and large-prime-tail composites.

The successor-support bit

\[
P_n=\mathbf1\{\text{that entering branch survives at }n+1\}
\]

is sufficient on odd open-square-basin states. The pair `(E_n,P_n)` is exactly the minimal three-state runtime described above.

This does **not** give a cheap primality algorithm: the observable is itself prime-filtered. Its value is structural. It proves that a genuine future signature, not another static divisor-incidence feature, separates the P1/P2 hard-core ambiguity.

## 8. Validation and scope

The all-integer jump identity was independently brute-force checked for every `2<=x<3000` with zero mismatches. The general proof is the integer argument above; the bounded check is falsification support only.

Freeze owner-local results:

`FLOOR_PRIME_SET_SIGNED_ENTRY_EXIT_LAW = true`.

`FINITE_BRANCH_LIFETIME_FOR_x_equals_a_p_with_a_less_than_p = a`.

`SQUARE_BASIN_LARGE_TAIL_LIFETIME_EQUALS_SMOOTH_CORE = true`.

`ONE_SUCCESSOR_PERSISTENCE_BIT_REPAIRS_PRIME_VS_LARGE_TAIL_AMBIGUITY = true`.

`THIS_IS_NOT_A_LEGENDRE_PROOF = true`.
