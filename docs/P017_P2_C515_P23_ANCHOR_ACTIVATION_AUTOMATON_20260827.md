# P017 — c=103/20 P(23) Anchor Activation Automaton

Status: `PROVED_WIP EXACT 256-STATE THRESHOLD AUTOMATON / SHALLOW ANCHOR MULTIPLICITY COLLAPSE / NOT FULL j=1 / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_p23_anchor_activation_automaton_20260827.py`

Depends on:

- `docs/P017_P2_C515_T12_P23_ANCHOR_AFTER_SUFFIX_FACTORIZATION_20260827.md`;
- the beta-2 upper Rosser support conditions.

Purpose: replace the coarse statement “there are at most 256 P(23) anchor divisors” by the exact finite activation law seen by a fixed P(23)-stripped hard modulus.

---

## 1. Exact reduction to parity and one scalar level ratio

Let

\[
b=q_1\cdots q_s
\]

be a fixed P(23)-stripped squarefree hard Rosser modulus, with all `q_i>=29`, and put

\[
T=\frac Qb.
\]

Write an anchor divisor in descending order

\[
e=a_1\cdots a_k,
\qquad
a_i\in\{23,19,17,13,11,7,5,3\}.
\]

Because every hard prime is larger than every anchor prime, the anchor primes occupy the global Rosser positions

\[
s+1,s+2,\ldots,s+k.
\]

The full level condition is

\[
e<T.
\]

At an anchor position `ell` for which `s+ell` is odd, the beta-2 Rosser condition becomes, after cancelling the fixed hard product `b`,

\[
\boxed{
a_1\cdots a_{\ell-1}a_\ell^3<T.}
\tag{AA1}

Thus anchor support depends on the hard modulus only through

\[
\boxed{s\bmod2}
\]

and the scalar `T`.

---

## 2. Activation threshold

For an anchor subset `e=a_1...a_k` define

\[
\boxed{
T_{\rm crit}^{(s)}(e)
=
\max\left(
 e,
 \max_{\substack{1\le\ell\le k\\s+\ell\text{ odd}}}
 a_1\cdots a_{\ell-1}a_\ell^3
\right).
}
\tag{AA2}

Then exactly

\[
\boxed{
e\text{ is supported}\iff T_{\rm crit}^{(s)}(e)<T.}
\tag{AA3}

The companion checker enumerates all `2^8=256` subsets for both parities using integer arithmetic only.

---

## 3. First thresholds

If the hard depth `s` is even, the first anchor prime occupies an odd global Rosser position. Therefore the first nontrivial activation is

\[
oxed{T_{\rm crit}^{(0)}(3)=3^3=27.}
\tag{AA4}

So

\[
\boxed{s\text{ even and }T\le27\Longrightarrow e=1.}
\tag{AA5}

If `s` is odd, the first anchor position is even, so a single anchor prime is constrained only by the full level. The first activations are

\[
3,5,7,11,13,17,19,23.
\]

However the first two-prime anchor is delayed until

\[
\boxed{T>135.}
\tag{AA6}

Thus for `T<=27`, odd hard depth has at most the identity plus the eight single anchor primes.

---

## 4. Consequence for c515 ratio-6/5 blocks

On geometric blocks

\[
\frac{B}{\rho^{i+1}}<m\le\frac{B}{\rho^i},
\qquad
\frac{N_0}{\rho^{j+1}}<n\le\frac{N_0}{\rho^j},
\qquad
\rho=\frac65,
\]

we have `BN0=D`, hence

\[
T=\frac D{mn}<\rho^{i+j+2}.
\tag{AA7}

Exact comparison of the integer thresholds with powers `(6/5)^n` gives:

1. for
   \[
   \boxed{i+j\le4,}
   \]
   both hard parities force
   \[
   \boxed{e=1;}
   \]
2. for
   \[
   \boxed{i+j\le16,}
   \]
   every even hard-depth state still forces
   \[
   \boxed{e=1;}
   \]
3. on those same diagonals, odd hard depth has at most nine anchor labels total, and no two-prime anchor has activated.

This is substantially stronger than charging the full 256-anchor family uniformly.

---

## 5. Boundary

The activation automaton is a support theorem. It does not by itself make all lower `j=1` blocks small enough for absolute summation: the long/short support mass grows relative to the remaining finite budget before the anchor family becomes large.

Its role is therefore to reduce the prefactor in the forthcoming lower-block `j=1` Cauchy/reciprocal analysis, not to replace that analysis wholesale.

No finite P2 theorem or all-K claim is made.
