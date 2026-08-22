# Prime-BRC odd-tail / no-recoalescence / switched-carry checkpoint

Status: `L3 OWNER-LOCAL RESEARCH CHECKPOINT / NOT CANONICAL`
Date: `2026-08-22`
Researcher-ID: `EM-PRIMEBRC-7F3A21`
Owner branch: `research/prime-brc-stage-a`

This checkpoint records only claims already reduced to exact integer identities or elementary inequalities. It does **not** claim Legendre's conjecture, a level of distribution, or a P2 theorem.

## 1. Odd multiplier quotient windows are globally separated

For `k>=1` and an odd integer `1<=a<=k`, define

`W_a(k)=[floor(k^2/a)+1, floor(k(k+2)/a)]`.

If `a<b<=k` are odd, then `b-a>=2` and

`k(b-a)>=2k>=2a`,

hence

`a(k+2)<=bk`.

Therefore

`floor(k(k+2)/b)<=floor(k^2/a)`,

so

`max W_b(k)<min W_a(k)`.

Freeze owner-local theorem:

`ODD_MULTIPLIER_WINDOWS_PAIRWISE_DISJOINT`.

Consequently, if `q>k` is odd and `aq` lies in the open square basin for an odd `a<=k`, then that multiplier `a` is unique.

## 2. Exact odd-sector smooth/tail partition

The open square basin contains exactly `k` odd integers. By canonical P017-L020 smooth-tail semantics, every odd basin state is exactly one of:

1. a prime;
2. `n=a*q` with odd `3<=a<=k` and one prime tail `q>k`;
3. a fully `k`-smooth odd composite.

The odd-window separation above makes `(a,q)` unique in case 2. Hence

`k = PRIME_ODD_COUNT + LARGE_PRIME_TAIL_ODD_COUNT + FULLY_SMOOTH_ODD_COUNT`.

This is an exact partition, not an asymptotic statement. The familiar first-order `log 2` versus `1-log 2` complement is interpretation only and does not by itself yield a strict capacity gap.

## 3. Odd-sector residual no-recoalescence horizon

Suppose two odd basin states admit factorizations

`n1=A1*B`, `n2=A2*B`,

where `A1,A2` are odd positive integers and `B>=k`.

If `A1!=A2`, then `|A1-A2|>=2`, so

`|n1-n2|>=2B>=2k`.

But the maximal distance between two states of the open basin is `2k-1`. Contradiction.

Therefore

`B>=k -> n1=n2`.

Freeze:

`ODD_FACTOR_STRIPPING_INTERSTATE_RECOALESCENCE_REQUIRES_RESIDUAL_LT_K`.

In particular, a large-prime-tail semiprime `p*q` with `q>k` has no inter-state recoalescence at its terminal prime-tail residual. BRC compression in that sector cannot come from merging exact residual identities across distinct basin states.

## 4. Odd hit count is a one-bit dyadic carry refinement

For odd `m`, let `H_m(k)` be the full basin hit count and let `O_m(k)` count odd basin multiples of `m`. Then exactly

`O_m(k)=H_m(k)-H_{2m}(k)`.

Writing `q=floor(k/m)`, the canonical binary-carry law implies

`O_m(k) in {q,q+1}`.

Equivalently

`O_m(k)=floor(k/m)+eta_m(k)`, `eta_m(k) in {0,1}`.

This is the parity-halved exact hit law used below.

## 5. B-type switched divisibility is exactly a dyadic-carry sum

For a B-type largest-prime range `R` (for example the rough-triprime range with `k^(2/3)<r<=k`), quotient windows `W_r(k)` are pairwise disjoint by the stronger all-odd window theorem.

For any odd `d`, the number of odd residual states in the union of these windows that are divisible by `d` is exactly

`A_d = sum_{r in R} O_{r d}(k)`.

Thus the switched sieve data are not a new ad hoc sequence: they are exact sums of P017 dyadic hit/carry objects.

No uniform level-of-distribution claim is frozen here. Finite experiments show small relative errors against an `A_1/d` model on tested ranges, but that remains discovery evidence only.

## 6. Rough triprime outer-product decoder

For an odd rough triprime

`n=p*q*r`, `p<=q<=r`, `n in (k^2,(k+1)^2)`,

one always has `q<=k` and

`D=p*r>k`.

Indeed, if `r<=k`, then `p*r^2>=p*q*r>k^2`, hence `p*r>k^2/r>=k`; if `r>k` the conclusion is immediate.

Since `D` is odd and exceeds `k`, the odd unique-hit law implies that `(p,r)` / `D` uniquely determines the basin state and the middle factor `q`.

Equivalently, stripping the middle prime gives an exact switching representation

`n <-> (q,D)`

with `D in W_q(k)`, `D=p*r` semiprime, `p<=q<=r`.

Different `q` windows are disjoint.

## 7. Scope boundary

These results materially simplify representation and switching multiplicity, but they do not overcome the final parity step.

Current strongest interpretation:

`PRIME_BRC_VALUE = EXACT_COMPRESSION_BOUNDARIES + SQUARE_SPECIFIC_SWITCHING_NORMAL_FORMS`,

not

`PRIME_BRC = PRIME_ORACLE`.

The next load-bearing analytic target is to determine whether the switched sequence `A_d=sum_r O_{rd}(k)` admits a provable distribution estimate strong enough to improve an existing weighted-switching bound. Static support recoalescence and root-only recoalescence have already been classified as insufficient for recursive prime semantics.
