# RH Riesz factor-port depth: single-output versus Pair-BRC collision

Status: `RESEARCH FRONTIER / POSITIVE CAPACITY + MATCHING-EXPONENT CONSTRUCTION / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Riesz / Pair-BRC / Alladi ordered-factor port / collision preservation / provenance depth`

## 0. Typing guard

This note concerns a **factor-only observer**. The correct Enterprise architecture continues to retain integer Cell identity as a separate provenance fiber. When integer Cell identity is retained, equality collision `m=n` is directly observable and the factor-only depth requirement below does not apply to equality detection.

Freeze distinction:

`FACTOR_ONLY_COLLISION_PORT != INTEGER_CELL_IDENTITY_AWARE_PORT`.

---

## 1. Riesz scale

Write the Riesz parameter as `x=N^2` and define

`W_N(n)=mu(n)^2 n^-2 exp(-N^2/n^2)`.

The positive first mass has scale

`A_N=sum_n W_N(n) ~ const * N^-1`.

The positive diagonal/collision mass has scale

`V_N=sum_n W_N(n)^2 ~ const * N^-3`.

The RH signed output scale is `N^-3/2+o(1)`.

---

## 2. High-factor-count tail at growing depth

Let

`K=c log N/loglog N`, `0<c<1` fixed,

and define the positive omitted mass

`R_K(N)=sum_{omega(n)>K} W_N(n)`.

On the dominant dyadic shell `n~N`, the uniform Hardy--Ramanujan large-deviation estimate gives

`#{n~N:omega(n)>K} <= N^(1-c+o(1))`.

Multiplying by the shell weight `~N^-2` gives

`R_K(N) <= N^(-1-c+o(1))`.

Smaller shells are exponentially suppressed by `exp(-N^2/n^2)`; larger polynomial shells give smaller weighted contributions. Hence

`R_K(N) <= N^(-1-c+o(1))`.

---

## 3. Matching exponent construction on selected dyadic scales

The exponent `1-c` cannot generally be improved by a purely positive factor-count argument.

Let `L=log N` and

`k=floor(c L/log L)`.

Choose a prime scale

`y=exp(L/k)=L^(1/c+o(1))`.

The fixed relative interval `[y,2y]` contains

`M=y^(1+o(1))=L^(1/c+o(1))`

primes, while `k=L^(1+o(1))`; because `c<1`, `M/k -> infinity`.

There are

`C(M,k)=exp((1-c+o(1))L)=N^(1-c+o(1))`

k-element prime subsets.

Their products range from `N` to `N 2^k`, a log-range of length `O(k)=o(L)`. Partition this range into dyadic bins. There are only `N^o(1)` bins, so one bin `[X,2X]`, with `log X=(1+o(1))L`, contains

`X^(1-c+o(1))`

such squarefree products, each with exactly k distinct prime factors.

Taking the Riesz scale to be this `X` gives a positive omitted mass

`R_k(X) >= X^(-1-c+o(1))`

along such selected scales.

Thus the exponent `-1-c` is a genuine positive-capacity barrier for a factor-only truncation.

---

## 4. Single-output-safe depth

To make the omitted positive mass no larger than the RH signed-output scale,

`R_K(N) <= N^-3/2+o(1)`,

it is enough to take

`c>=1/2`.

Thus the familiar single-output critical depth is

`K_single ~ (1/2) log N/loglog N`.

This is the same half-depth previously found from:

- Hildebrand/Dickman critical scaling,
- factorial Taylor tails,
- ordered-factor primitive selection.

---

## 5. Factor-only Pair-BRC collision-safe depth

Suppose now that a pair/collision observer attempts to reconstruct the RH pair object from the truncated factor port alone, and treats the omitted single-state mass as uncontrolled.

One bad endpoint and one arbitrary endpoint contribute an absolute pair mass bounded at the scale

`A_N R_K(N) <= N^(-2-c+o(1))`.

The true diagonal collision scale is

`V_N ~ N^-3`.

Therefore absolute collision-scale safety requires

`2+c >= 3`, i.e.

`c>=1`.

Hence

`K_collision,factor-only ~ log N/loglog N`.

This is asymptotically the maximal distinct-prime-factor depth possible for integers of scale N (primorial law).

Freeze:

`HALF_DEPTH_ALLADI_FACTOR_PORT_ALONE DOES NOT PRESERVE PAIR_COLLISION_SCALE`.

At collision resolution, a factor-only observer must be essentially complete, unless it retains another exact identity carrier.

---

## 6. Why this does not contradict the correct Enterprise architecture

The correct RH architecture already retained

`Arithmetic Cell identity -> X6 local port tensor prime/integer provenance fiber`.

If integer Cell identity is retained, the collision observer `H_x(0)` is simply `m=n` and is exact independently of the number of revealed prime factors.

Therefore the depth-doubling law is **not** a requirement to expose all prime factors in the correct architecture. It is an observer-preservation no-go against replacing integer Cell identity by a half-depth factor prefix.

This is a direct instance of the existing T4 finite-fiber/collision rule:

`COLLISION IS MORE INFORMATION-SENSITIVE THAN SINGLE OUTPUT`.

---

## 7. Consequence for the Alladi--Pair--BRC Gram bridge

The first

`K~(1/2)log N/loglog N`

Alladi ordered-factor coordinates are sufficient to approximate a single primitive-source readout to RH signed scale, but are insufficient by themselves to reconstruct the positive pair collision scale.

Thus any RH use of the Alladi--Pair--BRC Gram kernel must be tensored with integer Cell identity (or an equally fine exact collision carrier).

Freeze architecture:

`ALLADI GROWING FACTOR DEPTH + INTEGER CELL IDENTITY`,

not

`ALLADI HALF-DEPTH FACTOR PREFIX AS COMPLETE RH STATE`.

---

## 8. Current frontier

The representation problem is now largely closed:

- integer identity preserves exact collision;
- growing Alladi/BRC depth preserves ordered prime provenance;
- full Alladi jets are lossless and their finite truncation error is understood positively;
- prime-adapted connection is pure gauge.

The remaining RH problem is therefore a genuinely global signed estimate on the retained arithmetic state, not a missing local representation or compression mechanism.
