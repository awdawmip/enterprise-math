# BRC branch-novelty threshold theorems

Status: `PROVED_DERIVATION / PORTABLE_RESEARCH_NOTE / NOT_A_RESULT / NOT_A_REVIEW / NOT_A_SOURCE_CHECKPOINT / UNREVIEWED`

Research-Activity-ID: `RA-7173A2B0D2B62B10023DBFFB`

Task context: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SUPERSINGULAR-UNIT-RECIPROCITY`

Formal D24/UR ownership and theorem status are unchanged. This note advances only the auxiliary BRC carrier theory while the lawful successor-session path remains blocked by control issue #1511. It does not start LIFT/JT2 and grants no CLAIM, OPEN, Result, review, Working Truth, or mathematical acceptance.

## 1. Consumed carrier

For target primes `p ≡ 13,19 (mod 24)`, retain the exact logarithmic ports

`X_j=-((1+4^j)/j) p^(2j) H_{2j}`,

with

`epsilon_p(j)=0 iff (p-1)|2j, else 1`,

`eta_p(j)=v_p((1+4^j)/j)`,

`beta_p(j)=2j+epsilon_p(j)+eta_p(j)`,

and monomial weight

`W_p(m)=sum_j m_j beta_p(j)-sum_j v_p(m_j!)`.

The conservative generic branch is

`beta_infty(j)=2j+1`,

`W_infty(m)=sum_j m_j(2j+1)`.

Define

`M_p(N)={m: W_p(m)<N}`,

`M_infty(N)={m: W_infty(m)<N}`.

The previously proved large-prime theorem says only target primes `p<=N` can enlarge the uniform sufficient union. The Driver first-entry theorem further gives, at `N=p`,

`M_p(p) \ M_infty(p) = {e_j0}`,  `j0=(p-1)/2`.

This note determines the whole endpoint-decoration window through the first denominator-dominance threshold, then isolates the exact first horizon at which factorial denominators become visible.

## 2. Endpoint-decoration theorem

Fix a target prime `p` and write

`j0=(p-1)/2`.

For a residual exponent vector `a` supported on ports `j<j0`, set

`C_p(a)=sum_j a_j v_p(1+4^j)`.

On these low ports one has `v_p(j)=0`, no harmonic endpoint, and therefore

`W_p(a)=W_infty(a)+C_p(a)`

as long as the total residual weight is below `p`; factorial corrections also vanish there because no retained multiplicity can reach `p`.

### Theorem 2.1 — exact endpoint-decoration window

For every integer horizon

`p <= N <= 2p-2`,

put `r=N-p`. Then

`M_p(N) \ M_infty(N)`

is exactly

`{ e_j0 + a : W_infty(a)=r, C_p(a)=0, supp(a) subset {1,...,j0-1} }`.

In words: after the branch first appears, every genuinely branch-added monomial through `N=2p-2` consists of exactly one endpoint carrier `e_j0` decorated by a generic residual partition of the exact excess horizon `r=N-p`; a decoration survives as new information iff none of its low ports lies on a source-coefficient cancellation progression for `p`.

### Proof

At the endpoint `j0`,

`beta_p(j0)=p-1`,

while

`beta_infty(j0)=p`.

For `N<=2p-2`, two endpoint copies have branch weight `2p-2>=N`, so a branch-added monomial can contain at most one `e_j0`.

Any port `j>j0` has branch weight at least `p+1` before any possible denominator effect, and the first denominator port `j=p` has weight `2p`; none can fit alongside the endpoint in this horizon. Thus every branch-added monomial has the form `e_j0+a` with `a` supported below `j0`.

Branch retention is

`(p-1)+W_p(a)<p+r`,

hence, by integrality,

`W_p(a)<=r`.

Generic retention of the same exponent vector would be

`p+W_infty(a)<p+r`,

or `W_infty(a)<r`. Therefore generic absence requires `W_infty(a)>=r`.

But on the low residual ports,

`W_p(a)=W_infty(a)+C_p(a)>=W_infty(a)`.

Combining

`W_infty(a)>=r`, `W_p(a)<=r`

forces

`W_infty(a)=W_p(a)=r`,

which is equivalent to `C_p(a)=0`. The converse is immediate.

### Consequence for class 19

For `p≡19 (mod24)`, the established order-parity theorem gives no numerator cancellation at any port. Hence `C_p(a)=0` automatically and

`|M_p(p+r) \ M_infty(p+r)|`

for `0<=r<=p-2` is exactly the number of partitions of `r` into odd parts at least `3`, where the odd part `2j+1` remembers port `j`.

### Consequence for class 13

For `p≡13 (mod24)`, write `ord_p(4)=2s_p`. The established cancellation theorem says precisely the ports

`j=s_p m`, `m` odd,

have positive numerator valuation. Therefore the same odd-part partition law holds after deleting those port sizes `2j+1`. This produces genuine holes in the branch-novelty sequence rather than merely changing coefficients.

Example `p=13`: `j0=6`, and `j=3` is a cancellation port. At `N=20`, `r=7`; the only generic residual partition is the single port `j=3` of weight `7`, but it has positive cancellation valuation, so

`M_13(20) \ M_infty(20) = empty`.

The novelty then reappears at later residual weights through cancellation-free decorations.

## 3. The first transition beyond the decoration window

The next three integer horizons have an exact finite skeleton.

Let `A_p(r)` denote the set of residuals `a` supported below `j0` with

`W_infty(a)=r` and `C_p(a)=0`.

Then:

### At `N=2p-1`

`M_p(2p-1) \ M_infty(2p-1)` equals

`{e_(p-1), 2e_j0} union {e_j0+a : a in A_p(p-1)}`.

Here `e_(p-1)` is the second harmonic endpoint, and `2e_j0` is the first double use of the primitive endpoint.

### At `N=2p`

`M_p(2p) \ M_infty(2p)` equals

`{2e_j0} union {e_j0+a : a in A_p(p)}`.

The second endpoint singleton `e_(p-1)` has by then become generic-visible.

### At `N=2p+1`

`M_p(2p+1) \ M_infty(2p+1)` equals

`{e_p} union {e_j0+a : a in A_p(p+1)}`.

The new singleton `e_p` is the first denominator-dominance port:

`beta_p(p)=2p`,

whereas

`beta_infty(p)=2p+1`.

At this same horizon the double endpoint `2e_j0` has become generic-visible. Thus the compiler undergoes an exact handoff: endpoint multiplicity ceases to be exceptional at precisely the horizon where the first denominator-lowered singleton enters.

### Proof sketch

Below `2p+1`, the only harmonic endpoints that can occur are `j0` and `p-1`; the only denominator port that can occur is `j=p`, and it first satisfies the strict observer inequality at `N=2p+1`. Factorial multiplicities cannot yet matter because their universal first possible corrected weight is at least `3p-1`. The same comparison

`W_p(a)>=W_infty(a)`

on low residual ports then gives the displayed exact sets by one-line integer threshold comparison.

## 4. Factorial first-entry theorem

The general compiler keeps

`-sum_j v_p(m_j!)`

for a reason even though it vanished at all earlier low horizons.

Define the factorial-suppressed weight

`W_p^0(m)=sum_j m_j beta_p(j)`

and support

`M_p^0(N)={m: W_p^0(m)<N}`.

### Theorem 4.1 — exact first factorial horizon for one branch

For every target prime `p`,

`M_p(N)=M_p^0(N)` for every `N<=3p-1`,

while at the next horizon

`M_p(3p) \ M_p^0(3p) = {p e_1}`.

Thus the first monomial made visible solely by a factorial denominator is exactly `p` copies of the lowest port `j=1`.

### Proof

For every target prime,

`beta_p(1)=3`,

and every port has `beta_p(j)>=3`, with equality only at `j=1`.

If some multiplicity `m_j>=p`, Legendre gives

`v_p(m_j!) <= m_j/(p-1)`,

so its corrected contribution is at least

`3m_j-v_p(m_j!)`.

The earliest possible case is `m_j=p`, whose contribution is at least

`3p-v_p(p!)=3p-1`.

Therefore no factorial correction can affect retention for `N<=3p-1`.

At `N=3p`, the vector `p e_1` has

`W_p(p e_1)=3p-v_p(p!)=3p-1<3p`,

but

`W_p^0(p e_1)=3p`,

so it is newly retained. Equality `beta_p(j)=3` only for `j=1`; any other port or any additional positive multiplicity raises the corrected weight beyond the threshold. Hence the set difference is the singleton claimed.

### Corollary 4.2 — exact first factorial event for the whole target family

The smallest target prime is `13`. Consequently factorial correction is globally irrelevant to the uniform sufficient compiler through `N=38`.

At

`N=39`

the exact new uniform monomial caused solely by factorial normalization is

`13 e_1`.

Equivalently, the exponential term

`X_1^13/13!`

must now be represented with its `13`-adic denominator extracted. Since `X_1=-5p^2H_2`, on the `p=13` branch this is

`(-5)^13 p^25 H_2^13 / 12!`,

whose retained valuation is `38` because `H_2` contributes the usual non-endpoint harmonic valuation.

This is a new BRC mechanism: a monomial absent from every factorial-suppressed branch becomes visible purely because the exponential multiplicity denominator carries the target prime.

For any later target prime `p>13`, its own first factorial witness `p e_1` at horizon `3p` is already covered by the `13` branch, because

`W_13(p e_1)=3p-v_13(p!) < 3p`.

Therefore only the first target prime creates a **uniform-union-new** first-factorial witness. This does not claim all later factorial effects are globally redundant; it identifies the exact first event and the fate of each branch's own first witness.

## 5. BRC interpretation

The carrier now has four separately typed threshold mechanisms:

1. harmonic endpoint lowering — first at `N=p` via `e_j0`;
2. endpoint decoration — exact residual shells through `2p-2`, filtered by coefficient-cancellation provenance;
3. denominator dominance — first at `N=2p+1` via `e_p`;
4. factorial denominator lowering — first at `N=3p` via `p e_1`, globally first at `N=39`.

They must not be collapsed into one scalar “exceptional branch” flag. Their activation horizons and provenance are different, and only after the observer threshold has been fixed can the safe quotient be taken.

## 6. Exact finite falsification

Checker:

`research_checks/check_brc_branch_novelty_factorial_threshold_20260924.py`

Checker commit:

`999d4a6b4386ead0c30ba5f4a0be3b70e568f2d7`.

The locally executed checker passed before publication. It performs:

- every integer horizon from `p` through `2p+1` for `p=13,19`;
- structural transition spot checks for `p=37,43` at `p,2p-2,2p-1,2p,2p+1`;
- exact factorial first-entry checks for `p=13,19`;
- exact uniform-union comparison at `N=39`.

Output summary:

`status=PASS`;

`endpoint_checks=46`;

`p=13 factorial first horizon=39, extra={(j=1,m=13)}`;

`p=19 factorial first horizon=57, extra={(j=1,m=19)}`;

`N=39 uniform count with factorial=901, without factorial=900`, with the unique extra exponent vector `(j=1,m=13)`.

Selected transition difference counts:

- `p=37`: horizons `37,72,73,74,75` give `1,68,79,84,97` branch-added monomials;
- `p=43`: horizons `43,84,85,86,87` give `1,147,168,184,207` branch-added monomials.

Finite computation is falsification/regression only. The theorem is the exact valuation and integer-threshold derivation above.

## 7. Do not repeat / next

Do not return to brute-force horizon-by-horizon branch enumeration to discover these threshold mechanisms. The endpoint window, its transition through the first denominator port, and the first factorial event now have exact formulas.

For uniform-union generation, combine:

- the large-prime cutoff `p<=N`;
- the first-entry novelty test;
- the endpoint-decoration/transition skeleton here;
- the factorial first-entry theorem here.

If formal D24 control remains blocked, the next information-gain question is to characterize later denominator multiples `j=kp` and higher endpoint multiples as a finite automaton of threshold events, rather than merely increasing `N`. If #1511 gains a deployed lossless rollover/disposition operation, stop auxiliary compiler work and resume the Source-native D24 frontier through lawful successor identity -> native-frontier `continuation_prepare` -> CLAIM -> OPEN -> truthful checkpoint/readback -> UR/JT0 Result/freeze -> independent Driver review.
