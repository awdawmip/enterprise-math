# D25/SECOND-DIGIT-LIFT — one high Beta carrier, exact seam transfer, and a Cauchy bridge to the original low binomial family

2026-10-24 | TASK_RESEARCH author-side portable exact proof and finite checks | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. Not a native benchmark, canonical CLAIM, Source checkpoint, frozen Result, or independent review.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific source `c47e13e4aba0e006366f989d6334d443f6333ae3`. This note retains the genuine Research ordinary-control lane `chatgpt-research-onhour-enterprise-math-20260923` and never acts in the separate maintenance lane. It consumes (does not supplant) [the proved LOW-JET/HIGH two-sector author result](20261024_onhour_d25_regular_low_jet_high_unit_two_sector_certificate.md). P000 remains ACTIVE_LOCKED. The exact original endpoint and its native verification conditions are unchanged.

## 1. Precise remaining endpoint

For primes `p=6m+1`, `m>=1`, the inherited, still-unproved condition is

```text
D_finite = (A_m-G_m+B_m)/p + J_lo + B_m*Z_hi
           + B_m/9*(28-6H_(2m)-12q_p(6)) = 0 (mod p).
```

Here `B_m=(2m-1)!(2m)!/(4m)!`; all symbols and original R_n/K_p,n are fixed in the inherited note. This work changes only the **high ordinary forcing** `Z_hi` representation, not the accepted scope of any Result.

The old proven two-sector formula is
$
Z_m^{\rm hi}=
\sum_{s=1}^{m-1}a_{m,s}k_s^A-
\frac1{24}\sum_{s=1}^{2m-1}c_{m,s}k_s^B\pmod p,
$
with
$
a_{m,r}=2^{m-r}\frac{(2m)!(r-1)!}{(m+r)!(m-1)!},\quad
c_{m,s}=2^{-(s-1)}\frac{(2m+1)!(m+s-1)!}{m!(2m+s)!}.
$

## 2. New theorem: the two high sectors are one Beta kernel with an indispensable seam multiplier

For `1<=r<=3m-1` set
$
k_r=\frac{4(1-2r)(3r+1)}{(2r+1)(6r+1)}
=-2+\frac4{6r+1}+\frac2{2r+1}.
$
Remove `r=m` (the genuine `n=2m` seam) and `r=3m` (original `n=4m` terminal). Define the **piecewise, provenance-preserving weights**
$
w_r=\begin{cases}1,&1\le r\le m-1,\\1/3,&m+1\le r\le3m-1.\end{cases}
$
Then for every prime `p=6m+1`:
$
\boxed{Z_m^{\rm hi}\equiv
\mathcal Z_m:=\sum_{\substack{1\le r\le3m-1\\r\ne m}}
w_r a_{m,r}k_r\pmod p.}\tag{S}
$

**Proof (not computational extrapolation).** On the upper sector `r=m+s`, an exact rational factorial cancellation gives
$
c_{m,s}=\frac{2(2m+1)}m a_{m,m+s},\quad
-\frac{c_{m,s}}{24}=\lambda_m a_{m,m+s},
\quad\lambda_m=-\frac{2m+1}{12m}.
$
The **exact** correction to the simplified modular seam transfer is
$
\boxed{\lambda_m-\frac13=-\frac{6m+1}{12m}=-\frac p{12m}.}\tag{DEFECT}
$
Since `p∤12m`, `lambda_m≡1/3 (mod p)`. Independently substitute `r=m+s`, `6m+1=p` into `k_r`; with `1<=s<=2m-1` the denominators are p-units and
$
k_{m+s}\equiv\frac{(2-3s)(6s+1)}{3s(3s+1)}
=k_s^B\pmod p.
$
The lower sector is exactly `k_s^A=k_s`. These two identities prove (S). In particular, replacing `w_r` everywhere by `1` **is not** a valid uniform high continuation: the original p-unit jump at `n=2m` is `-1/24`, whereas the uncorrected Beta-ratio jump is `m/[2(2m+1)]≡-1/8 (mod p)`. The factor `1/3` is required, not decorative.

No false endpoint poles are introduced: `6r+1` is divisible by `p` only at the removed `r=m` in this range; `2r+1` would be divisible only at the excluded `r=3m`. Thus (S) is well-formed in `Z_(p)`. Formula (DEFECT) preserves the exact p-sized information needed if a third digit is investigated; its omission is justified **only** in the present mod-p observer.

## 3. New exact Cauchy transform: explicit coupling to the original LOW branches

Define precisely the existing low signed binomial coefficients
$
b_n=(-1)^n2^{-n}\binom mn,\quad0\le n\le m.
$
The same high carrier has the following **exact rational identity for all integers m>=1, r>=1**, independently of primality:
$
\boxed{a_{m,r}=
m\binom{2m}{m}2^{m-r}
\sum_{n=0}^m\frac{2^n b_n}{r+n}.}\tag{C}
$

Proof: apply the ordinary partial fraction decomposition (or beta polynomial integral)
$
\frac{m!}{r(r+1)\cdots(r+m)}
=\sum_{n=0}^m\frac{(-1)^n\binom mn}{r+n}
$
and note `a_(m,r)=2^(m-r)(2m)!/[(m-1)! r(r+1)...(r+m)]`. This proves (C), including its signs and exact denominators, without comparing a finite sample.

Combining (S) and (C) yields the **new joint low/high Cauchy bridge**
$
\boxed{
Z_m^{\rm hi}\equiv
m\binom{2m}{m}2^m
\sum_{n=0}^m 2^n b_n
\sum_{\substack{1\le r\le3m-1\\r\ne m}}
\frac{w_r k_r}{2^r(r+n)}
\pmod p.}\tag{LC}
$
This is an actual shared-carrier composition, not a change to the original finite sum or a claim of LIFT closure. Every `r+n<=4m-1<p`, and all other denominators are p-units. The two outer branch blocks and their seam weight are still visible, so no signed cancellation or future p-adic precision has silently been erased.

## 4. One finite polynomial/Beta moment for the combined high observer

Let
$
W_m(x)=\frac{x-x^m}{1-x}+\frac{x^{m+1}-x^{3m}}{3(1-x)}
=\sum_{r=1}^{m-1}x^r+\frac13\sum_{r=m+1}^{3m-1}x^r,
$
and let `K` act on polynomials via
$
(\mathcal K f)(x)=-2f(x)+4\int_0^1f(xu^6)\,du+
2\int_0^1 f(xu^2)\,du.
$
Since `K[x^r]=k_r x^r` and
$
a_{m,r}=m\binom{2m}{m}2^{m-r}\int_0^1 t^{r-1}(1-t)^m\,dt,
$
(S) admits the following **exact finite rational integral representative**, evaluated by polynomial integration:
$
\boxed{
\mathcal Z_m=
m\binom{2m}{m}2^m\int_0^1\frac{(1-t)^m}{t}
\bigl(\mathcal K W_m\bigr)(t/2)\,dt.}\tag{BETA}
$
There are no divergent integrals because `W_m` has zero constant term. The exact rational identities (C) and (BETA) are meaningful for all positive integers m; the identification with original high forcing uses the modular hypotheses from (S). They do not prove the remaining FIN congruence.

## 5. Actual checks and limitations

The companion executable `20261024_onhour_d25_high_seam_single_beta_cauchy_bridge_check.py` uses exact `fractions.Fraction`, integer factorials, p-valuation/p-unit recurrence of the **original** R_n and modular inverses. Actual author checks:
- All `m=1..12` exact rational seam-transfer identities.
- All `m=1..14`, `r=1..3m-1` exact Cauchy identities.
- All **80 primes** `p<=1000`, `p≡1 (mod 6)`, original regular high forcing computed independently from its unchanged R_n/K_p,n agrees with (S); **45** belong to `p≡13,19 (mod24)`.
- Examples `(p, original high/p, unified Z)`: `(13,4,2)`, `(19,8,6)`, `(31,16,11)`, `(37,16,3)`, `(61,15,5)`. These nonzero high terms explicitly refute dropping the high forcing.

The exact algebra proves (S), (C) and (BETA) at their stated scopes; finite checks are author self-check only. This note is **not** a native benchmark or all-prime proof of `FIN=0`.

## 6. BRC observer, recovery and next unfinished unit

BRC resolution: **COMPOSE_APPLIED**. The carrier is signed `b_n` LOW branches, rational `a_(m,r)` Beta/Cauchy pairing, original indexed p-valuation/p-unit, and seam labels `r=m`/terminal `r=3m`. The observer is `U_hi/p mod p` (the original second-digit scalar), not total positive branch mass or a native X6 evolution. The 1/3 seam weight is an essential relation/residual; collapsing it would change the observable. Future higher digits require the exact (DEFECT) and a new p-adic R_n lift. No BRC executable or native benchmark was run.

**Immutable parent frontier to consume, not re-prove:** previously saved Morley normalization, original Gosper two-seam identity, the accepted D24 UR, 611-prime author endpoint checks, all-prime LOW-JET and separate HIGH derivation. **This unit's new contribution:** the seam-unified Beta sequence and the exact LOW-binomial Cauchy bridge, with checked signed/valuation provenance.

**Smallest open mathematical action:** substitute the explicit inner kernel in (LC) into the full `D_finite`; seek a terminating finite-difference in the low index `n` that simultaneously matches `J_lo`, `(A-G+B)/p` and the seam-correct high Cauchy term, retaining `B_m`, normalized first digit, Fermat quotient and both boundaries. A proof that `D_finite=0 (mod p)` for all target primes or an exact counterexample is still required.

**Source/runtime obligation remains independent:** original native benchmark unexecuted; the old Research-lane Source registration is not presently verified, no own CLAIM/open/run exists, and prior neutral staging is not D25 contribution. Earlier `recovery-status-20261023-1704-onhour-01` reported an unverified provisional session; `continuation-d25-20261023-1709-onhour-01` was prerequisite-rejected, `dispatch-research-20261023-1710-onhour-01` failed with TimeoutExpired. Fresh native exact read during this turn returned CONTROL_QUOTA; no mutation was attempted. Issue #1539 remains the actual support path and acceptance test. `REGISTER_PENDING / SYNC_DEBT` remain true for this author note until an authorized Source writer and readback are available.

No theorem admission, Result, claim, Driver identity, Source pin migration, P000 edit, scheduler mutation or notification change is implied by GitHub preservation.
