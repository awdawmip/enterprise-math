# R005-A — Cubic Core Reduction and Finite Oppermann Transport

Status: `PROVED R005 STRUCTURE + EXTERNAL-COMPUTATION TRANSFER / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. Why the p=3 frontier changes again

The previous danger-radius theorem said that for a p-power basin it is sufficient to force every candidate prime witness up to `D=floor(sqrt(U/2))`. For p=3 this is not sharp enough.

The cubic geometry plus the residual-support theorem allow a much smaller sufficient core:

`q <= k`.

This is a structural theorem, not a numerical optimization of the old cutoff.

## 2. T-A18 — cubic core theorem

Let `A=k^3`, `U=(k+1)^3-1`, `F=floor(sqrt(U))`. Assume every candidate prime witness `q<=k` is forced. Then the cubic basin has no residual composite.

Suppose a residual composite n exists. The generic residual theorem gives at least two distinct non-forced candidate prime divisors `q1,q2 | n`. Since all candidate primes up to k are forced, `q1,q2>k`. The generic non-forced bound gives `q1,q2<=sqrt(A)=k^(3/2)`, so `q1*q2<=A=k^3`.

Because `n>A` and `q1*q2|n`, write `n=q1*q2*m` with integer `m>=2`. Take any prime divisor s of m. If `s<=F`, then s is a candidate divisor of residual n and cannot be forced, so `s>k`. If `s>F`, then certainly `s>k`. Thus every prime divisor of m exceeds k, so `m>=k+1`. Also `q1,q2>=k+1`. Hence `n>= (k+1)^3`, contradicting `n<=U=(k+1)^3-1`.

Therefore no residual composite exists. By the generic forced-basis theorem:

> if all candidate primes `q<=k` are forced, the forced core is the unique least safe divisor-witness basis.

This shrinks the p=3 least-basis danger core from order `k^(3/2)` to order k.

## 3. T-A19 — Oppermann first-half forcing for q <= k

Fix a candidate prime q with `q<=k`. Put

`y=sqrt(k^3/q)`, `t=ceil(y)`.

Assume the first half of Oppermann holds at t, i.e. there is a prime r with

`t^2 < r < t(t+1)`.

Then r gives an exclusive collision for q.

Since `t>=y`, `r>t^2>=k^3/q`, hence `q*r>k^3=A`. For `k>=3`, `k^2>F`; because `q<=k`, `k^3/q>=k^2`, so `r>F` and r is not a candidate witness.

For the upper bound, `t<=y+1` and `t+1<=y+2`, so

`q*r < q*t(t+1) <= q(y+1)(y+2) = k^3 + 3*sqrt(k^3*q) + 2q <= k^3 + 3k^2 + 2k < (k+1)^3-1 = U`.

Thus `q*r` lies in the basin and q is its only candidate prime divisor, so q is forced.

## 4. Worst Oppermann index

The required index `t(q)=ceil(sqrt(k^3/q))` is largest at the smallest candidate prime q=2. Therefore

`t_max(k)=ceil(sqrt(k^3/2))`.

This converts any finite verified Oppermann range directly into a finite least-basis theorem for cubic basins.

## 5. Transfer from Sorenson–Webster 2025

Sorenson and Webster report computational verification of Oppermann's conjecture through `N=7.05*10^13`.

Using the exact integer condition

`t_max(k)<=70,500,000,000,000`,

the largest k is

`k=2,150,153,225`.

Exact endpoint values:

- `t_max(2,150,153,225)=70,499,999,996,893`;
- `t_max(2,150,153,226)=70,500,000,046,075`.

Hence, using the published finite Oppermann verification as an external computation premise:

> for every `2<=k<=2,150,153,225`, the cubic-basin divisor-witness language has a unique least safe basis.

This supersedes the earlier p=3 finite least-basis frontier `k<=4,104,076`.

The earlier prime-gap duality remains important as an independent horizontal characterization; the new result wins numerically because the cubic-core theorem reduces the dangerous witness range from order `k^(3/2)` to order k.

## 6. Three p=3 layers remain distinct

- Prime anchor: the 2026 consecutive-cubes computation supplies an actual prime in every tested cube basin up to a much larger finite range.
- Unique least witness basis: the finite Oppermann transport now gives `k<=2,150,153,225`.
- Full forcing saturation: still false in general; p=3 can contain candidate witnesses above k that are not forced.

Thus the result is not “all witnesses are mandatory”. It is that forcing a much smaller core already eliminates every residual composite.

## 7. Status boundary

Internal R005 theorem: cubic core theorem; Oppermann-to-forced-witness transport inequality; exact endpoint conversion.

External premise: finite verification of Oppermann through `7.05*10^13`.

Nonclaims: no proof of Oppermann or Legendre; no claim beyond the external verified index; no full p=3 forcing claim; no Lean-checked status.

Next: formalize the cubic-core theorem after the generic WitnessCover module actually typechecks; ask whether p=3 has an even smaller canonical sufficient core; generalize the factor-count argument to other p and identify the dimension-dependent sufficient forced-core radius.
