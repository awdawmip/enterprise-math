# BRC Phase Quotient/Remainder Transport — Round 13

Status: `PROVED PHASE SECOND-DIFFERENCE BOUND / 1KB RECIPROCAL TABLE / EXACT QUOTIENT-REMAINDER TRANSPORT / LARGE-INTEGER OPTIONAL SPEEDUP`
Date: `2026-09-07`
Parents: `t0.brc_linear_deep_tail`, `t0.brc_square_gap_cascade`

## 1. Question

Round 11 reduced every deep-tail root increment to

`q_h(m)=floor(2h J_m/(4m+h))`, `h in {1,2}`,

and Round 12 made the second gap-isqrt almost disappear with a 3.6KB staged
quadratic-residue cascade.  The remaining conspicuous operation is therefore the
big-integer division in q_h(m).

Can that quotient and its remainder themselves be transported between later
multipliers, with a small table used only for bounded correction?

Yes, exactly.

## 2. Five fixed phases

The exact odd-N representative source residues are

`m mod 8 in {0,1,3,5,7}`.

The outgoing step is fixed by the source residue:

- residues 1,3,5 use h=2;
- residues 7,0 use h=1.

Each phase returns after exactly 8 in m.  For one fixed phase define

`D(m)=4m+h`,
`X(m)=2h J_m`,
`q(m)=floor(X(m)/D(m))`,
`r(m)=X(m)-q(m)D(m)`.

Then

`0<=r(m)<D(m)`

and along that phase

`D(m+8)=D(m)+32`.

## 3. Smooth envelope and exact second-difference bound

Let

`S_h(m)=2h sqrt(mN)/(4m+h)`.

For m in the deep tail, q(m) differs from S_h(m) by less than 2.  Indeed,
replacing sqrt(mN) by J_m loses less than one root unit, hence less than one
quotient unit, and the final floor loses less than another.

Direct differentiation gives

`S_h''(m)`
`= h sqrt(N) (48m^2-24hm-h^2)`
`  / (2 m^(3/2) (4m+h)^3)`.

On the relevant positive-convex range,

`0 <= S_h''(m) <= 3h sqrt(N)/(8m^(5/2))`.

The common order-one tail satisfies

`4m^5>=N`,

so

`sqrt(N)/m^(5/2) <= 2`.

Therefore

`S_h''(m) <= 3h/4`.

For phase spacing 8, the integral form of the second finite difference yields

`0 <= Delta_8^2 S_h(m) <= 64*(3h/4)=48h`.

Thus the smooth bounds are at most 48 for h=1 and 96 for h=2.

Write

`q(m)=S_h(m)-epsilon_m`, `0<=epsilon_m<2`.

Then

`-4 < Delta_8^2 epsilon_m < 4`.

Because the integer second difference of q is integral, the exact bounds are

`-3 <= Delta_8^2 q <= 51` for h=1,

and

`-3 <= Delta_8^2 q <= 99` for h=2.

The universal five-phase correction range is therefore the fixed 103-value set

`{-3,-2,...,99}`.

This bound is independent of N, m, and the final multiplier horizon once the
common deep tail has begun.

## 4. Exact quotient/remainder recurrence

Take three successive visits to the same phase, indexed k-1,k,k+1.  Put

`qhat_(k+1)=2q_k-q_(k-1)`.

The target denominator is 32 larger than at the previous visit.  Using

`X_i=q_i D_i+r_i`

and eliminating the large products q_i D_i gives the exact residual relative to
the linear extrapolation:

`rho_(k+1)`
`= X_(k+1)-qhat_(k+1)D_(k+1)`
`= 2h(J_(k+1)-2J_k+J_(k-1))`
`  +2r_k-r_(k-1)`
`  +64(q_(k-1)-q_k)`.

No product of a full quotient by the large denominator remains.  The expression
uses only additions/subtractions and multiplication by the tiny constants
2h and 64.

The exact correction is

`e_(k+1)=floor(rho_(k+1)/D_(k+1))`.

By the theorem above,

`-3<=e_(k+1)<=99`.

Then

`q_(k+1)=qhat_(k+1)+e_(k+1)`,

`r_(k+1)=rho_(k+1)-e_(k+1)D_(k+1)`.

So each phase needs only two ordinary divmod seeds.  Every later quotient and
remainder is exact state transport.

## 5. Why the correction table can be only 1KB

For rho<0 the theorem leaves only three cases:

`e in {-1,-2,-3}`,

which are distinguished by at most two comparisons with D and 2D.

For rho>=0, normalize the denominator by its top 10 bits.  Write

`D in [u*2^s,(u+1)*2^s)`, `512<=u<=1023`.

Store

`R_u=floor(2^20/(u+1))`.

There are 512 entries, every entry fits in 16 bits, so the logical payload is

`512*2 = 1024 bytes`.

The table estimate is

`e0=floor(rho R_u / 2^(20+s))`.

Because the table uses the upper bucket endpoint u+1, e0 is always a lower
estimate.  For the proved range rho/D<100,

`rho/D - rho R_u/2^(20+s)`

is less than

`100/513 + 100*1024/2^20 < 0.293`.

Hence

`e-1 <= e0 <= e`.

One exact comparison against `(e0+1)D` therefore returns the exact non-negative
correction.

The normalized denominator bucket changes only when the slowly increasing D
crosses a top-10-bit boundary, so long streams reuse the same seed for many
steps.

## 6. Total table budget after Round 12

Round 12 BALANCED square-gap cascade:

`3609 bytes`.

Round 13 normalized quotient correction table:

`1024 bytes`.

Combined logical table budget:

`4633 bytes`.

The two roles are different:

- 3609 bytes remove almost all second gap-isqrt calls;
- 1024 bytes help remove the remaining per-step full quotient division after
  phase warmup.

Neither table grows with N or with the multiplier horizon.

## 7. Validation

Repository regression checks:

- reciprocal table size and 16-bit entry bound;
- declared h=1 and h=2 second-difference bounds;
- exhaustive small odd-N phase triples on the common tail;
- direct-divmod equivalence for random 64..8192-bit N;
- long streams beyond multiplier 100;
- exactly ten seed divmods for a warmed five-phase stream, then recurrence only.

The reference research harness also compared the integrated order-one BRC +
BALANCED square-gap cascade with and without the tracker.

## 8. Finite performance boundary

Committed benchmark parameters:

- 16 deterministic odd N values per bit size;
- 700 retained multiplier transitions each;
- 5 timing repeats;
- identical order-one BRC correction and BALANCED QR cascade in both paths.

Only the quotient backend changes.

Representative current-environment results:

| N bits | direct divmod / phase tracker |
|---:|---:|
| 1024 | 0.58x |
| 2048 | 0.76x |
| 4096 | 1.17x |
| 8192 | 1.37x |

Thus the tracker is **not** a universal replacement for native division.
Python's built-in big-integer division is faster at 1024/2048 bits in this
runtime.  The recurrence becomes useful only once operands are large enough and
the long-stream warmup is amortized.

Decision:

`DIRECT_DIVISION` remains the safe general default.

`PHASE_QR_TABLE` is registered as an exact optional backend for very large
integer long-tail streams.

No architecture-independent crossover is claimed.

## 9. Relation to recursive BRC

This result continues the user's error-recursion program:

- BRC gap correction has constant second difference -2;
- the order-one predictor quotient, sampled by fixed mod-8 phase, has a uniformly
  bounded second difference;
- two quotient/remainder samples therefore form a sufficient local transport
  state, with only a bounded table correction thereafter.

So the long tail now has two nested finite-difference structures:

`root gap: exact quadratic -> linear first difference`,

`increment quotient: near-linear phase sequence -> bounded second difference`.

## 10. Boundary

- This is exact integer arithmetic on the already-certified N^(1/5) tail.
- It does not reduce the multiplier horizon.
- It does not change Lehman/Hart factorization complexity.
- It does not imply RSA practicality.
- The reciprocal table is derived runtime data, not new theorem content.
- Performance is runtime-dependent; small and medium integers should keep native
  division.

## 11. Next

The quotient division itself is now absent after warmup.  Remaining deep-tail
cost is dominated by large integer multiply/add work in the BRC remainder update
and by the few modular reductions that survive the staged filters.

A next attack should therefore look for shared residues / low-word shadow state
that lets the BRC remainder update and the QR cascade reuse arithmetic already
carried by the quotient/remainder phases, rather than adding another independent
approximation layer.
