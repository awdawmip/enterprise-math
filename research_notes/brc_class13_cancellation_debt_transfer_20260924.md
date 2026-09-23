# BRC class-13 cancellation debt transfer to class 19

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / AUXILIARY_ONLY / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`.

Stable logical lane: `chatgpt-research-hourly-enterprise-math-20260923`.

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`.

This note consumes the exact branch-defect cocycle and the same-run large-prime cancellation-signature reduction, but proves a stronger **quantitative** residual law. The earlier binary obstruction said that some class-13 suppressions necessarily wake a class-19 branch. Here the amount of unavoidable class-19 defect is bounded from below by the amount of class-13 suppression demanded.

No D24 owner, Result, review, Working Truth or Foundation status is changed.

## 1. Exact setup

Let `q>13` be a target prime with

`q == 13 (mod24)`.

Write

`ord_q(4)=2s_q`

and

`c_q=v_q(1+4^{s_q})>=1`.

The q-coefficient-cancellation ports are exactly

`C_q={j : s_q|j and j/s_q is odd}`.

For a finite exponent cloud `m=(m_j)`, define its total q-cancellation occupancy

`T_q(m)=sum_{j in C_q} m_j`.

Retain the exact branch defect

`Delta_r(m)=sum_j m_j [E_r(j)+v_r(j)-C_r(j)(v_r(j)+c_r)] + sum_j v_r(m_j!)`

for class-13 branches, and the same formula with `C_r=0` for class-19 branches.

## 2. Every q-cancellation copy can buy at most c_q units of q suppression

On a q-cancellation port `j in C_q`, endpoint and cancellation are disjoint, and the denominator valuation cancels inside the coefficient-cancellation term. Therefore the linear q-defect of one occupied copy is exactly

`-c_q`.

Every non-cancellation port contributes nonnegatively to `Delta_q`, and every factorial term is nonnegative. Hence:

### Lemma 2.1

For every finite cloud m,

`Delta_q(m) >= -c_q T_q(m)`.

Consequently, if

`Delta_q(m) <= -k`

for an integer `k>=1`, then

`T_q(m) >= ceil(k/c_q)`.

This is an exact resource lower bound: q-suppression requires a minimum number of provenance-bearing q-cancellation copies. Factorial credit can only make suppression more expensive.

## 3. Each dirty class-19 branch charges a fixed debt per q-cancellation copy

Let `r<q` be a target prime with

`r == 19 (mod24)`.

Define the q-to-r debt coefficient

`d_{r<-q} = 1_{h_r|s_q} + v_r(s_q)`,
where `h_r=(r-1)/2`.

If `d_{r<-q}>0`, then every q-cancellation port `j=s_q u` with u odd necessarily carries at least that much positive r-defect:

- if `h_r|s_q`, then `h_r|j`, contributing one endpoint unit;
- the denominator contribution is `v_r(j)>=v_r(s_q)`;
- class 19 has no coefficient-cancellation channel;
- factorial and all other occupied ports contribute only nonnegatively.

Therefore:

### Lemma 3.1

For every finite cloud m and every class-19 r<q,

`Delta_r(m) >= d_{r<-q} T_q(m)`.

This lower bound is simultaneous for **every** r with positive debt coefficient.

## 4. Quantitative cancellation-debt theorem

Combining Lemmas 2.1 and 3.1 gives:

### Theorem 4.1 — cancellation debt transfer

If

`Delta_q(m) <= -k`, `k>=1`,

then for every class-19 target prime `r<q` with `d_{r<-q}>0`,

`Delta_r(m) >= d_{r<-q} ceil(k/c_q)`.

Equivalently, a demand for k units of class-13 q suppression creates an unavoidable vector-valued class-19 residual debt

`Debt_19(q,k) = ( d_{r<-q} ceil(k/c_q) )_{r<q, r==19 mod24}`

on every positive debt coordinate.

This is not an average or total-mass statement. Each r-coordinate is retained separately with its endpoint/denominator provenance.

### Corollary 4.2 — binary obstruction recovered

If any `d_{r<-q}>0`, then no cloud can have both

`Delta_q(m)<0`

and

`Delta_r(m)<=0`.

Thus the earlier 19-dirty obstruction is the k=1 shadow of Theorem 4.1.

### Corollary 4.3 — record-budget form

Suppose a target p has defect advantage B over an earlier class-19 branch r, and repairing an earlier q-blocker requires q suppression by at least k. A necessary condition for preserving the strict p record is

`B > d_{r<-q} ceil(k/c_q)`.

When B is one unit and `c_q=1`, any positive debt edge already kills p-neutral strict novelty; a debt coefficient two kills it by two full horizons.

## 5. Structural meaning of the debt coefficient

The two summands of

`d_{r<-q}=1_{h_r|s_q}+v_r(s_q)`

are independent residual sources:

1. **endpoint debt** — the q-cancellation step itself lands on an r endpoint;
2. **denominator debt** — the q-cancellation step itself carries r-adic denominator valuation.

They can occur simultaneously. Therefore a Boolean dirty/clean flag loses scientifically relevant magnitude.

Examples below 5000 include:

- `q=37`, `s_q=9`, `r=19`: endpoint debt only, `d=1`;
- `q=229`, `s_q=19`, `r=19`: denominator debt only, `d=1`;
- `q=2053`, `s_q=513=27*19`, `r=19`: both `h_19=9|513` and `19|513`, so `d=2`;
- `q=3613`, `s_q=903=21*43`, `r=43`: both endpoint and denominator debt, so `d=2`;
- `q=4789`, `s_q=1197=9*133=19*63`, `r=19`: both mechanisms again, `d=2`.

Thus two class-13 suppressions with the same binary “dirty” status can carry different unavoidable class-19 costs.

## 6. Relation to c_q and higher cancellation depth

The source-coefficient depth `c_q` also must remain an integer, not a Boolean flag.

One q-cancellation copy buys exactly `c_q` units of negative linear q-defect before nonnegative factorial/other corrections. Therefore the forced class-19 cost for a requested k-unit suppression scales as

`ceil(k/c_q)`,

not k itself.

A larger `c_q` can make a q suppressor more efficient, but it never removes a positive debt coordinate: if `d_{r<-q}>0`, every cancellation copy still pays that r-debt.

This separates two residual coordinates that a total-only quotient would conflate:

- q-side cancellation efficiency `c_q`;
- r-side irreversible debt vector `d_{r<-q}`.

## 7. Finite falsification/regression

Checker:

`research_checks/check_brc_class13_cancellation_debt_transfer_20260924.py`.

Checker publication commit:

`ba86da4d4f9ca6ddf1da2e6a99fc9c3e57b11543`.

Independent exact-integer regression below 5000 found:

- target primes: `166`;
- higher class-13 q: `82`;
- 19-dirty higher class-13 q: `44`;
- positive q-to-class19 debt edges: `72`;
- maximum debt coefficient observed: `2`;
- coefficient-two examples include `(2053 -> 19)`, `(3613 -> 43)`, `(4789 -> 19)`;
- deterministic multi-port clouds with arbitrary extra positive-channel ports/multiplicities checked: `504`;
- singleton multiplier tests across every dirty edge and odd multipliers `<200`: `0` failures;
- quantitative q-bound, r-bound and combined debt inequality failures: `0`.

Finite computation is falsification/regression only. The proof is Lemmas 2.1 and 3.1.

## 8. BRC interpretation

A q-cancellation event is not a free signed subtraction. It consumes a finite, provenance-bearing cancellation resource, and when `s_q` intersects a class-19 endpoint/denominator fiber, the removed q defect reappears as a one-way positive residual in a branch with no cancellation channel.

For the observer `UNIFORM_EARLIEST_VISIBILITY`, the minimal sufficient repair state therefore includes the vector

`(c_q, T_q, {d_{r<-q}}_r, {Delta_r}_r)`

rather than only the net q defect.

This is a residual-faithful discrete law: a local cancellation can move observational debt between fibers, but cannot erase the branch provenance that makes the transfer irreversible.

## 9. Do not repeat / next

Do not treat all 19-dirty q as a Boolean class. The integer debt coefficients and q cancellation depth now control the exact repair budget.

Do not search arbitrary q-cancellation port indices to estimate class-19 damage. The lower bound depends only on `s_q`, `c_q`, and the affected r coordinates.

If formal D24 control is still blocked, the next nonredundant auxiliary unit is to use the exact debt vectors together with the Driver's finite signature cone to formulate a branch-record repair budget for arbitrary initial defect vectors: which suppressions are feasible before the target p margin is exhausted.

If the lifecycle repair becomes live, stop auxiliary work and return to the Source-native D24 successor chain.
