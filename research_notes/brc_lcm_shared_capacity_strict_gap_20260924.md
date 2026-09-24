# BRC strict shared-LCM capacity gap at p=3181

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the already-published finite LCM-atom quotient theorem at Enterprise Math commit `0e3ba7eea784721d314c0279d5c21957c73e923c`. It does **not** reprove that theorem. It supplies the next nonredundant unit: an explicit exact witness that the earlier one-row-at-a-time clean-atom capacity test is strictly weaker than the global LCM cone. Shared cancellation support can make an otherwise capacity-failing singleton repair feasible.

No D24 owner, Result, review, Working Truth, Foundation status, or LIFT/JT2 status is changed.

## 1. The four relevant branches

Take

`p=3181`, `d=37`, `q1=2221`, `q2=3109`.

All four are primes congruent to `13 mod24`.

For a class-13 prime q write

`ord_q(4)=2s_q`, `c_q=v_q(1+4^{s_q})`.

Exact modular-order certificates give

- `ord_37(4)=18`, so `s_37=9` and `c_37=1`;
- `ord_2221(4)=1110`, so `s_2221=555` and `c_2221=1`;
- `ord_3109(4)=222`, so `s_3109=111` and `c_3109=1`;
- `ord_3181(4)=530`, so `s_3181=265` and `c_3181=1`.

For example, for q=2221 the order candidates are certified by

`4^1110=1 mod2221`

while the prime-divisor tests at exponents `555,370,222,30` give respectively

`2220,543,330,980 mod2221`,

none equal to 1. The other three orders have the analogous exact prime-divisor tests in the paired checker. The q-adic depths are also certified modulo `q^2`; the quotients `(4^{s_q}+1)/q mod q` are nonzero.

## 2. One shared core

Set

`L=555=3*5*37`.

Then

`s_2221=555 | L`

and

`s_3109=111 | L`, with quotient `L/111=5` odd.

Thus the same odd LCM atom cancels both clean rows:

`delta_2221(L)=-1`,

`delta_3109(L)=-1`.

It is target-p neutral because

`s_3181=265` does not divide `555`

and `3181` does not divide `555`; the class-13 endpoint is even whereas L is odd. Hence

`delta_3181(L)=0`.

No target compensation is needed for this witness.

## 3. Exact class-19 neutrality without a statistical scan

For an odd port j, a class-19 branch r can receive positive defect only if

- `r|j`, or
- `h_r=(r-1)/2 | j`.

The prime divisors of L are `3,5,37`, none congruent to `19 mod24`, so the first event is impossible for every class-19 r.

For `r ==19 mod24`, one has

`h_r ==9 mod12`.

The positive divisors of `555` are

`1,3,5,15,37,111,185,555`,

whose residues modulo 12 are respectively

`1,3,5,3,1,3,5,3`.

None is 9 modulo 12. Therefore no class-19 endpoint divides L. Consequently

`delta_r(L)=0`

for every class-19 target `r<3181`.

So the shared atom is exactly class-19-neutral by an elementary finite divisor argument, not by empirical prime sampling.

## 4. The unique positive earlier class-13 coordinate

Because L is odd, no class-13 endpoint occurs. For a class-13 q the singleton defect is therefore

`delta_q(L)=-c_q` when `s_q|L` with the required odd quotient, and otherwise `v_q(L)>=0`.

A positive coordinate can therefore occur only at a class-13 prime dividing L. Among the prime factors `3,5,37`, only 37 is a target class-13 prime. Since

`s_37=9` does not divide `555`,

there is no 37-cancellation, while `v_37(555)=1`. Thus

`delta_37(L)=+1`.

There are no other positive earlier class-13 coordinates.

The exact nonzero signature through p is

`delta_13(L)=-1`,
`delta_37(L)=+1`,
`delta_61(L)=-1`,
`delta_2221(L)=-1`,
`delta_3109(L)=-1`,

with every other earlier class-13 coordinate zero and `delta_3181(L)=0`. The extra negative coordinates are helpful and do not consume capacity.

## 5. Singleton causal repair fails

Consider the residual state b on earlier class-13 rows defined by

`b_2221=+1`,
`b_3109=+1`,
`b_37=-1`,

and all other earlier class-13 coordinates `<=0`; take every earlier class-19 coordinate to be zero and target-p residual to be zero.

The descending singleton clean-row policy first reaches `q2=3109`. Its canonical self atom has core

`s_3109=111=3*37`.

That atom gives

`delta_3109(111)=-1`,
`delta_37(111)=+1`,
`delta_2221(111)=0`.

So it closes q2 and exhausts the sole unit of dirty-37 slack.

The q1 row remains positive and requires its singleton self atom `s_2221=555`, which gives another

`delta_37(555)=+1`.

Hence the two singleton atoms close q1 and q2 but produce

`b'_37=-1+1+1=+1`.

The singleton causal capacity test therefore rejects this residual state.

## 6. One shared LCM atom succeeds

Use instead a single copy of the shared LCM core

`L=lcm(111,555)=555`.

It acts simultaneously on both clean demands:

`b'_2221=1-1=0`,

`b'_3109=1-1=0`,

while the dirty capacity is spent only once:

`b'_37=-1+1=0`.

All other earlier class-13 coordinates stay nonpositive; every earlier class-19 coordinate remains exactly zero; and the target p coordinate remains zero.

Therefore the same residual state is feasible in the exact global LCM cone.

### Theorem 6.1 — strict separation

The descending singleton clean-atom capacity test is not globally complete. There exists an exact residual state for which it fails while the finite LCM-atom cone succeeds.

The explicit witness is

`p=3181`,
`b_2221=b_3109=1`,
`b_37=-1`,

with shared atom `L=555`.

Thus shared-support dirty cost is genuinely subadditive: two singleton repairs charge the dirty row twice, whereas the shared LCM hyperedge cancels both clean rows while charging that same dirty denominator provenance once.

This does not contradict the earlier causal theorem, which explicitly limited minimality to its descending singleton policy. It is a strict witness that the enlargement to the finite LCM cone in commit `0e3ba7ee...` is mathematically necessary, not merely a convenient reformulation.

## 7. BRC meaning

The relevant residual object is a hyperedge, not a list of independent scalar cancellations.

The core `L=555` simultaneously carries

- cancellation provenance for q1=2221;
- cancellation provenance for q2=3109;
- one denominator-capacity charge on dirty d=37;
- no class-19 debt;
- no target-p debt.

If the observer decomposes this hyperedge into independent q1/q2 atoms before accounting for shared support, it duplicates the same dirty denominator event and creates a false infeasibility result.

Therefore the minimal sufficient state for global clean repair must retain shared LCM support together with its denominator vector. Boolean row coverage or additive per-row debt is insufficient.

## 8. Exact checker

Paired checker:

`research_checks/check_brc_lcm_shared_capacity_strict_gap_20260924.py`.

It reconstructs primality, multiplicative orders, q-adic cancellation depths and all relevant branch defects from exact integer arithmetic. It verifies:

- the four order/step values above;
- exact class-19 neutrality of `111` and `555` below 3181;
- `555` has unique positive earlier class-13 coordinate `37:+1`;
- its negative coordinates are exactly `13,61,2221,3109` at depth one;
- target 3181 sees zero defect;
- two singleton atoms leave dirty row 37 at `+1`;
- one shared LCM atom leaves q1, q2 and d all exactly at zero;
- total failures: zero.

The fixed witness is proved structurally in Sections 2–6; the checker is an exact certificate/regression of those calculations.

## 9. Do not repeat / next

Do not use the descending singleton capacity test as a global feasibility criterion after this witness.

Do not expand the arbitrary physical-port search again; the finite LCM theorem already gives the exact global cone.

The next nonredundant auxiliary question, only if formal D24 control remains blocked, is to quotient the finite LCM library by exact dominance: for atoms with the same cancellation-support vector, determine when one denominator vector is coordinatewise dominated by another and derive the smallest antichain/Hilbert-style carrier that preserves integer repair feasibility.

If the canonical lossless staging-disposition/session-rollover operation becomes live, stop auxiliary work and return immediately to the Source-native D24 continuation path.
