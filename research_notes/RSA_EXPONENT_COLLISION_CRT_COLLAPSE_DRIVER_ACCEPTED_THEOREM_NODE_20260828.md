# RSA Exponent-Collision CRT Collapse — Driver-Accepted Theorem Node

Status: `DRIVER_ACCEPTED / RESULT_ONLY / NO_TOOL_PROMOTION / NO_SPEEDUP_CLAIM`

Date: `2026-08-28`

Node:

`RSA_EXPONENT_COLLISION_CRT_COLLAPSE_THEOREM`

Authority:

- result `RR-2D43CCB30B906AFB6E20`;
- Driver review `DR-2F834647FD94CAF46D05`;
- human review `driver_reviews/RSA_EXPONENT_COLLISION_CRT_COLLAPSE_DRIVER_REVIEW_20260828.md`.

## 1. Fixed-unit exponent kernel

Let `n=pq` with distinct odd primes and let `x` be a unit modulo `n`. The exponent map

`e -> x^e`

has kernel

`ord_n(x) Z`.

Hence a local exponent collision

`x^e = x^e' (mod n)`

is exactly equivalent to

`ord_n(x) | (e-e')`.

For a finite family `{x_i}`, the common exponent kernel is

`lcm_i ord_n(x_i) Z`,

the exponent of the generated subgroup.

## 2. Exact 2-adic CRT split criterion

Given only a valid certificate

`x^Delta = 1 (mod n)`, `Delta>0`,

write

`Delta=2^s u`, with `u` odd,

and proof-side local orders

`ord_p(x)=2^a m_p`, `ord_q(x)=2^b m_q`,

with `m_p,m_q` odd.

Along the extractor-visible chain

`z_j=x^(u 2^j) (mod n)`,

the first global pre-`1` state is a nontrivial CRT square root of one if and only if

`a != b`.

Therefore

`2-adic collision collapse splits n <=> v2(ord_p(x)) != v2(ord_q(x))`.

No hidden factor, Carmichael value, or local order is consumed by the extractor; these appear only in the proof.

## 3. Exact random-unit probability

Let

`A=v2(p-1)`, `B=v2(q-1)`, `m=min(A,B)`.

For a uniform unit, the local 2-depth distribution is

`Pr(a=0)=2^-A`,

`Pr(a=t)=2^(t-1-A)` for `1<=t<=A`,

independently at `q`. Since failure is exactly `a=b`,

`P_fail=(4^m+2)/(3*2^(A+B))`,

and

`P_split=1-P_fail >= 1/2`.

The lower bound is sharp at `A=B=1`.

## 4. Global exponent-map collision

Two exponents induce the same power map on every unit exactly when their difference is a multiple of

`lambda(n)=lcm(p-1,q-1)`.

Thus a nonzero global fake-exponent difference exposes a known annihilating exponent. The resulting random-base factor extraction is classical Miller/Rabin-style order-to-factor mathematics and is not claimed as a new RSA attack.

## 5. Multi-certificate aggregation theorem

For valid local certificates `(x_i,Delta_i)`, let

`L=lcm_i Delta_i`.

Then `L` annihilates the subgroup `H=<x_i>`, so every combination in `H` can be fed to the same 2-adic collapse.

The exact all-combination failure barrier is:

`every h in H fails the 2-adic split`

if and only if

`H_2` is the graph of an isomorphism between its two cyclic local 2-primary projections.

Equivalently, both local projections are injective on `H_2` and preserve element orders.

This explains strict aggregation gains: individually failing generators can combine to a nontrivial CRT square root.

## 6. Scope boundary

Accepted:

- local exponent-kernel characterization;
- exact single-certificate iff split criterion;
- exact random-unit probability;
- safe lcm subgroup aggregation;
- diagonal-graph failure barrier.

Not accepted:

- efficient collision generation from `n` alone;
- a factoring complexity improvement;
- external novelty for the local or multi-certificate formulations;
- Working Truth, Foundation, or toolbox promotion.

Method harvest classification remains `RESULT_ONLY`.