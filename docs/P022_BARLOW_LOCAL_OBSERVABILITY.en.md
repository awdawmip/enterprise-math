# P022 — Two Consecutive Coordination Shells Recover the Current Hidden Drift State

Status: `ACTIVE RESEARCH NOTE / EXACT TWO-STEP OBSERVABILITY / NOVELTY UNVERIFIED`  
Owner: `program/p022-geometry-v2`  
Depends on: Barlow coordination shell-energy identity  
Cross-route relevance: P018 kernel-time/predictive depth; P023/P024 history-sensitive quotient sufficiency

## 1. From full-history sufficiency to local observability

The coordination-history theorem proves that the complete sequence

\[
(S_0,S_1,\ldots,S_n)
\]

recovers the unordered absolute drift state

\[
P_q=\{|\delta_q|,|\delta_{-q}|\}
\]

at every radius.

That proof reconstructed the state recursively from the root.  It left open a sharper question:

> how many immediately preceding coordination observations are actually required to recover the **current** hidden drift pair?

One shell is not always enough because static sum-of-two-squares ambiguity appears.  This note proves that two consecutive shells always suffice and that the bound is sharp.

## 2. Shell cardinality and quadratic hidden energy

At radius `n`, write

\[
P_n=\{a,b\},
\qquad a,b\ge0,
\]

where

\[
a=|\delta_n|,
\qquad b=|\delta_{-n}|.
\]

The coordination identity is

\[
4S_n=42n^2+8-a^2-b^2.
\]

Hence one shell count is equivalent to the scalar quadratic energy

\[
\boxed{Q_n=a^2+b^2.}
\]

At radius seven,

\[
50=1^2+7^2=5^2+5^2,
\]

so `Q_7` and therefore `S_7` alone cannot recover the hidden pair.

## 3. One-step energy relation

Each one-sided absolute drift changes by one reflected unit from radius `n-1` to `n`.

For one current coordinate `a`, a legal predecessor has magnitude `a-1` or `a+1`, with the usual reflected convention at zero.  Thus its squared-energy difference is

\[
(a\pm1)^2-a^2=1\pm2a.
\]

For the two channels together,

\[
Q_{n-1}-Q_n
=2+2(\epsilon a+\eta b)
\]

for suitable signs

\[
\epsilon,\eta\in\{-1,+1\}.
\]

Define

\[
\boxed{
L=rac{Q_{n-1}-Q_n-2}{2}.
}
\]

Then

\[
\boxed{L=\pm a\pm b.}
\]

This linear shadow is exactly the extra information supplied by the previous shell.

## 4. P022-LO01 — two consecutive energies uniquely recover the current unordered pair

We know

\[
Q=a^2+b^2
\]

and

\[
L=\pm a\pm b.
\]

There are three cases.

### Case A: \(L^2>Q\)

A difference satisfies

\[
(a-b)^2\le a^2+b^2=Q.
\]

So `L` cannot be a signed difference. Therefore

\[
|L|=a+b.
\]

Then

\[
2ab=L^2-Q.
\]

The unordered pair `{a,b}` is the set of integer roots of

\[
x^2-|L|x+\frac{L^2-Q}{2}=0.
\]

### Case B: \(L^2<Q\)

A sum satisfies

\[
(a+b)^2\ge Q.
\]

So `L` must be a signed difference:

\[
|L|=|a-b|.
\]

Then

\[
2ab=Q-L^2
\]

and

\[
(a+b)^2=2Q-L^2.
\]

Again the sum and product recover the unordered integer roots uniquely.

### Case C: \(L^2=Q\)

Then

\[
2ab=0,
\]

so one coordinate is zero and the other is

\[
\sqrt Q.
\]

Thus in every legal case

\[
\boxed{
(Q_{n-1},Q_n)
\Longrightarrow
\{a,b\}.
}
\]

No earlier hidden state is required.

## 5. P022-LO02 — two consecutive shell cardinalities are sufficient

The radius is query context, and each shell cardinality reconstructs its energy exactly.  Therefore

\[
\boxed{
(S_{n-1},S_n)
\Longrightarrow
\{|\delta_n|,|\delta_{-n}|\}.
}
\]

This is a **local** decoder.  Applying it independently for every `n` reconstructs the complete unordered drift trajectory from a sliding observation window of width two.

The reconstruction does not need to remember the previously reconstructed pair in order to decode the next pair.

## 6. P022-LO03 — the uniform current-state observation depth is exactly two

Depth one fails at radius seven because

\[
1^2+7^2=5^2+5^2.
\]

Depth two succeeds for every legal radius by LO01.

Hence the sharp uniform depth for the current hidden two-channel drift state is

\[
\boxed{d_{\mathrm{obs}}=2.}
\]

This is stronger than saying “history helps.”  The exact amount of history required for the **current state** is finite and minimal.

## 7. Why this does not collapse whole-shell future history to two numbers

The radius-`n` total geodesic multiplicity depends on the drift pair at every height

\[
1,2,\ldots,n,
\]

not just the current extreme pair at height `n`.

So

\[
(S_{n-1},S_n)
\]

is sufficient for the current hidden drift state `P_n`, but not generally for the whole-shell future statistic `T_n`.

To compute `T_n` from coordination observations, one still needs the sequence of local decodings across all heights.  Equivalently, one needs the coordination history through `n`, but every hidden coordinate in that history is decoded by a **two-sample local rule**.

Thus two distinct notions must remain separate:

- **state observability depth**: two;
- **future-language horizon** for a shell-wide statistic: potentially all heights through `n`.

## 8. Precision consequence

This gives a concrete finite distinction among three things often collapsed into one word “memory”:

1. terminal observation;
2. local observation depth needed to reconstruct current hidden state;
3. total observation horizon needed by the declared future functional.

In this Barlow system,

\[
\boxed{
1<d_{\mathrm{obs}}=2\ll n
}
\]

can coexist with a shell-wide query that still needs drift information at every height up to `n`.

That is directly relevant to P018/P023/P024: a quotient may be locally state-observable with bounded memory while a richer future query remains long-horizon.

Any upstream abstraction must preserve this distinction.

## 9. Executable verification

Added:

- `src/enterprise_math/p022_barlow_local_observability.py`;
- `tests/test_p022_barlow_local_observability.py`.

The tests exhaust all legal two-channel absolute transitions through radius 24 and all microscopic two-sided windows through length six, comparing the local two-shell decoder with direct hidden drift trajectories and with the earlier recursive history decoder.
