# P022 Observation-History Arithmetic Core Return — 2026-08-27

Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-DE338F269CA11E9BC01B`  
Researcher: `EM-P022OH-540040`  
Claim: `chatgpt-p022oh-20260827-1639`

## Terminal verdict

`EXACT_REDUCTION_COMPLETE / HARD_TARGET_MET_VIA_EXACT_REDUCTION`

The frozen P022 first-reentry program is not closed by a new universal nonvanishing theorem in this replay. It is, however, reduced exactly to one fixed-parameter terminating finite-field hypergeometric cancellation problem, with the elementary valuation and standard terminating-transformation routes exhausted and with no counterexample found in the deterministic boundary census below `q<50000`.

This meets the taskbook's allowed exact-reduction terminal condition. It does **not** establish that the remaining kernel is nonzero for every admissible prime, and it grants no Working Truth, Foundation status, or canonical promotion.

## 1. Frozen P022 boundary

The replay starts from `program/p022-geometry-v2@c07ca4c719117829fe2c6919bbe635a1e97a8c4b`.

The frozen owner lineage already proves:

- `F_n = sum_k binom(n,k)^3` is the Franel convention used by P022;
- a primitive Franel prime at rank `r` obeys the p-Lucas/reflection constraints recorded in the owner helpers;
- a nontrivial twin center has both `2r-1` and `2r+1` prime;
- inside the strict reflection-safe window `q<3r-1`, the terminal defect pivot cannot cancel;
- the first genuinely dangerous endpoint is therefore `q=3r-1`;
- at that endpoint, the frozen midpoint-zero obstruction eliminates `q=5,7 (mod 8)`, so a *complete* boundary escape can survive only in the classes `q=17,35 (mod 72)`.

The question left by the old HANDOFF is whether the dangerous boundary can actually satisfy `q | F_r`.

## 2. Exact normalization: `r=6m`, `q=18m-1`

At a nontrivial twin center, `2r-1` and `2r+1` are odd primes. Modulo three, one of the three consecutive odd numbers

`2r-1, 2r, 2r+1`

is divisible by three. For `r>2`, neither boundary prime can equal three, hence `3 | 2r`, so `3 | r`.

At the dangerous boundary `q=3r-1`, primality of `q>2` forces `r` even. Therefore

`r = 6m`,

and consequently

`q = 18m-1`,

while the twin boundaries are

`12m-1` and `12m+1`.

Thus the remaining arithmetic gate is a one-parameter family indexed by `m`.

## 3. MacMahon reduction to a terminating `3F2(1)`

Use the exact MacMahon expansion

`F_r = sum_{k=0}^{floor(r/2)} 2^(r-2k) (r+k)! / ((r-2k)! (k!)^3)`.

For `r=6m`, let

`A_k = 2^(6m-2k) (6m+k)! / ((6m-2k)! (k!)^3)`.

Then

`A_{k+1}/A_k = (6m+k+1)(6m-2k)(6m-2k-1) / (4(k+1)^3)`.

Modulo `q=18m-1`, one has `18m=1`, hence `6m=1/3`. Therefore

`A_{k+1}/A_k = ((k-1/6)(k+1/3)(k+4/3))/(k+1)^3  (mod q)`.

Normalizing by the unit `2^(6m)` gives the exact congruence

`2^(-6m) F_(6m)`

`= sum_{k=0}^{3m} [(-1/6)_k (1/3)_k (4/3)_k / (k!)^3]   (mod q)`.

At the same modulus,

`-1/6 = -3m`, `1/3 = 6m`, `4/3 = 6m+1`.

Hence

`2^(-6m) F_(6m)`

`= _3F_2(-3m, 6m, 6m+1; 1,1; 1)  (mod q)`.

The parameter `-3m` makes the series terminate *exactly* at `k=3m`. Writing the summands integrally yields

`S_m = sum_{k=0}^{3m} (-1)^k binom(3m,k) binom(6m+k-1,k) binom(6m+k,k)`.

Because `2` is a `q`-unit,

**Exact boundary equivalence**

`q | F_(6m)  <=>  S_m = 0 (mod q)`, where `q=18m-1`.

This is the first main output of the replay.

## 4. Every summand is a `q`-adic unit

For every `0 <= k <= 3m`, none of the rising-factorial factors in

`(-3m)_k (6m)_k (6m+1)_k / (k!)^3`

contains a multiple of `q=18m-1`:

- the nonzero factors of `(-3m)_k` have absolute value at most `3m<q`;
- `(6m)_k` ends at `9m-1<q`;
- `(6m+1)_k` ends at `9m<q`;
- `k!` ends at `3m<q`.

Therefore every individual term of `S_m` is a `q`-adic unit.

So the remaining obstruction is **not** a valuation-support problem. There is no zero term, no unique minimal-valuation term, and no whole tail removable by a positive valuation. Any proof of nonvanishing must control genuine finite-field cancellation.

This closes the elementary valuation route exactly rather than empirically.

## 5. Reversal gives a fixed rational-parameter kernel

For a terminating series

`_3F_2(-n,a,b;1,1;1)`, reverse `k=n-j`. Direct factorial/Pochhammer algebra gives

`_3F_2(-n,a,b;1,1;1)`

`= (-1)^n (a)_n (b)_n/(n!)^2`

`  * sum_{j=0}^n [(-n)_j^3 / ((1-a-n)_j (1-b-n)_j j!)]`.

Set `n=3m`, `a=6m`, `b=6m+1`. The prefactor is a `q`-unit by the same range check. Modulo `q=18m-1`,

`-3m = -1/6`,

`1-9m = 1/2`,

`-9m = -1/2`.

Thus the dangerous boundary zero is equivalently the vanishing of the fixed-parameter truncated kernel

`R_m(q) = sum_{j=0}^{3m} [(-1/6)_j^3 / ((1/2)_j (-1/2)_j j!)]   (mod q)`.

So a particularly compact exact residual statement is:

`q | F_(6m)`

`<=> R_m(q)=0`,

subject to `q=18m-1` prime (and, for the actual P022 escape constellation, `12m-1` and `12m+1` prime plus the frozen surviving mod-72 condition).

All rational denominators in this truncated range are invertible modulo `q`.

This fixed `(-1/6; 1/2,-1/2)` kernel is the smallest explicit residual identity isolated in this replay.

## 6. Standard terminating transformation audit

I audited the exact parameter orbit generated by numerator/denominator permutations together with the standard terminating Weber–Erdelyi transformation

`_3F_2(A,B,-N;D,E;1)`

`= (D-A)_N/(D)_N`

`  * _3F_2(A,E-B,-N; 1+A-D-N, E; 1)`.

For the specialized start

`(-3m,6m,6m+1;1,1)`,

the canonical affine-parameter orbit contains **12** distinct parameter types.

Within this orbit:

- direct numerator/denominator cancellation types: **0**;
- Saalschutz-balanced types: **0**.

Therefore the routine terminating-transform path does not reduce this family to an immediate factorial quotient or a standard balanced `3F2(1)` evaluation.

This is deliberately narrow: it does not claim that every deeper hypergeometric, finite-field, modular, or geometric transformation is impossible.

## 7. Exact deterministic pressure test

The checker enumerates the actual twin-boundary constellation below `q<50000`:

- `q = 18m-1` prime;
- `12m-1` prime;
- `12m+1` prime.

It then computes `F_(6m) mod q` exactly and cross-checks the hypergeometric kernel.

Results:

- total boundary candidates: **90**;
- residue counts modulo 72:
  - `17`: **22**;
  - `35`: **25**;
  - `53`: **28**;
  - `71`: **15**;
- exact zeros `F_(6m)=0 (mod q)`: **0**;
- candidates in the frozen complete-escape survivor classes `17` or `35 mod 72`: **47**;
- zeros among those 47 survivors: **0**.

The original frozen examples are included and are nonzero:

- `(r,q)=(6,17)`: `F_r mod q = 3`;
- `(36,107)`: `77`;
- `(156,467)`: `411`;
- `(174,521)`: `377`.

This finite evidence is **not** an infinite proof.

### Control that kills an invalid broadening

The checker also verifies

`149 | F_50`,

while `149 = 2 (mod 3)` and `50=(149+1)/3`.

Thus the tempting broader claim

`q=2 (mod 3) => q does not divide F_((q+1)/3)`

is false. Any final proof for P022 must use more of the twin-boundary structure and/or the surviving mod-8/mod-72 information; mod 3 alone is insufficient.

## 8. Exact remaining frontier

After this replay, the old P022 boundary question is reduced to:

> For `m>=1` such that `q=18m-1`, `12m-1`, and `12m+1` satisfy the frozen prime-boundary conditions, and in particular for the complete-escape survivor classes `q=17,35 (mod 72)`, prove or refute
>
> `S_m != 0 (mod q)`,
>
> where
>
> `S_m = sum_{k=0}^{3m} (-1)^k C(3m,k) C(6m+k-1,k) C(6m+k,k)`.

Equivalently prove or refute nonvanishing of the fixed truncated finite-field kernel

`sum_{j=0}^{3m} (-1/6)_j^3 / ((1/2)_j(-1/2)_j j!)`.

The elementary valuation route is closed; the standard terminating transformation orbit does not evaluate it. The next technically honest methods are therefore finite-field hypergeometric/Jacobi-sum methods, or a modular/Cartier interpretation specialized to this one kernel. Merely extending the census is not a meaningful successor.

## 9. Artifacts

- deterministic checker: `scripts/check_p022_observation_history_arithmetic_core.py`;
- full boundary certificate: `research_artifacts/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE/boundary_census_q_lt_50000.json`;
- this return: `research_returns/P022_OBSERVATION_HISTORY_ARITHMETIC_CORE_RETURN_20260827.md`.

The checker records the exact 90-candidate census, validates the unit lemma, reproduces the 12-element specialized terminating-transformation orbit, checks the `q=149` control counterexample, and asserts all published finite counts.

## 10. Prior-art touchpoint and status boundary

The MacMahon Franel expansion and Jarvis--Verrill-style Franel congruence machinery are prior art; a convenient audited source is Victor J. W. Guo, *Proof of two conjectures of Z.-W. Sun on congruences for Franel numbers*, arXiv:1201.0617. The contribution frozen here is the specialization to the P022 `q=3r-1` twin-boundary geometry, the exact `r=6m`, `q=18m-1` normalization, the terminating kernel reduction, the unit obstruction, the specialized transformation audit, and the task-local falsification certificate.

No all-`m` nonvanishing theorem is claimed. No Foundation file was modified. No canonical theorem status is implied. Driver review is required before any integration or promotion decision.
