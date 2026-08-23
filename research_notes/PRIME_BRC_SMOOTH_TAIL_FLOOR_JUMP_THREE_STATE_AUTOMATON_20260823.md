# Prime-BRC Smooth-Tail / Floor-Jump Three-State Automaton

Status: `L3 OWNER-LOCAL / PROVED BRIDGE / NOT LEGENDRE`
Date: `2026-08-23`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

## 1. Two previously separate descriptions

For an odd state

\[
K^2<n<(K+1)^2,
\]

canonical P017-L020 writes

\[
n=S_K(n)Q_K(n),
\]

where `Q_K(n)=1` or `Q_K(n)` is one prime `>K`; moreover `n` is prime iff `S_K(n)=1`.

Independently, define the floor-prime set

\[
\mathcal G(x)=
\left\{\left\lfloor\frac{x}{j}\right\rfloor:1\le j\le x\right\}\cap\mathbb P,
\qquad
G(x)=|\mathcal G(x)|.
\]

The owner-local odd jump theorem proves

\[
G(n)-G(n-1)
=\mathbf1_{\{P^+(n)^2\ge n\}}
\]

for odd `n>=5`, where `P^+(n)` is the largest prime factor.

Because the open square basin contains no squares,

\[
P^+(n)^2\ge n
\iff
P^+(n)>\sqrt n>K.
\]

## 2. Exact first-bit identification

Therefore

\[
\boxed{
G(n)-G(n-1)=1
\iff
Q_K(n)>1.
}
\]

Equivalently,

\[
\boxed{
\Delta G(n)=0
\iff
n\text{ is fully }K\text{-smooth composite},
}
\]

and

\[
\boxed{
\Delta G(n)=1
\iff
n\text{ is prime or a large-prime-tail composite}.
}
\]

Thus the canonical P017 smooth-tail dichotomy is exactly the current floor-prime branch-entry bit.

## 3. Successor persistence is the missing bit

Assume `Delta G(n)=1`. Let `q=P^+(n)>K` be the unique entering large prime branch and write

\[
n=a q,
\qquad a=S_K(n)<q.
\]

The branch-lifetime theorem gives

\[
\operatorname{life}(q)=a.
\]

Define the one-step persistence bit

\[
P(n)=\mathbf1_{\{q\in\mathcal G(n+1)\}}.
\]

Then

\[
P(n)=0\iff a=1,
\]

and

\[
P(n)=1\iff a>1.
\]

Hence the exact reachable state table is

\[
\boxed{
\begin{array}{c|c|c}
\Delta G(n)&P(n)&\text{arithmetic class}\\ \hline
0&0&\text{fully }K\text{-smooth composite}\\
1&0&\text{prime}\\
1&1&\text{large-prime-tail composite}.
\end{array}}
\]

The fourth Boolean pair `(0,1)` is unreachable by definition because no branch can persist if no new large-prime branch entered.

## 4. Minimality / no-resurrection boundary

The current bit `Delta G` alone is insufficient: it deliberately identifies

\[
\text{prime}\sim\text{large-tail composite}.
\]

The one-step persistence bit separates them exactly.

Therefore, for the declared three-way target, the reachable runtime has exactly three states. Any exact classifier for all three classes needs at least three distinguishable values; the pair `(Delta G,P)` attains this bound with one current bit plus one successor-support bit.

This is a concrete specialization of the canonical R023 one-step repair principle:

```text
current coarse observation
+ minimum successor information
-> exact future-relevant class.
```

## 5. Density interpretation and the log(2) barrier

At scale `x~K^2`, the event

\[
\Delta G=0
\]

is the classical `K`-smooth / `sqrt(x)`-smooth sector. Its first-order density is the Dickman value

\[
\rho(2)=1-\log2.
\]

The complementary branch-entry sector has first-order density

\[
\log2.
\]

Thus the familiar first-order identity

\[
(1-\log2)+\log2=1
\]

is exactly the density decomposition of the **first BRC state bit**.

The unresolved Legendre-level difficulty lies entirely inside the `Delta G=1` sector: one must force at least one entering branch with lifetime `1` rather than lifetime `>1`.

## 6. Structural consequence

Prime-BRC has therefore isolated the parity hard core as

\[
\boxed{
\text{branch enters}
\quad\text{versus}\quad
\text{branch enters and persists one more step}.
}
\]

The first distinction is classical smoothness / large-prime-tail structure. The second is a genuinely future-sensitive P1/P2 discriminator.

This does not prove a prime must occur in every square basin. It specifies exactly which one-step future event remains to be forced.

Freeze:

`P017_SMOOTH_TAIL_BIT_EQUALS_ODD_FLOOR_PRIME_JUMP_BIT = true`.

`PRIME_BRC_THREE_STATE_RUNTIME = {(0,0),(1,0),(1,1)}`.

`PRIME_STATE = ENTRY_WITH_NO_ONE_STEP_PERSISTENCE`.

`LEGENDRE_REMAINS_A_POSITIVITY_PROBLEM_FOR_THE_LIFETIME_ONE_SUBSTATE = true`.
