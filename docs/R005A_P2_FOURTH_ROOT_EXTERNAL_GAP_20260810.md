# R005-A — Finite p=2 Fourth-Root Core Certificate from External Prime Gaps

Status: `EXTERNAL-COMPUTATION TRANSFER + PROVED R005 CONSEQUENCE / NOT CANONICAL`  
Date: `2026-08-10`

## 1. Goal

p=2 sits below the Baker–Harman–Pintz 0.525 phase boundary for every finite m-root observation core. So BHP cannot give an asymptotic finite-arity classification by the T-A22 route.

But the large externally computed prime-gap table can still give a strong finite statement. We target the fourth-root core because T-A21 plus the generic residual lower bound gives exact residual arity three whenever that core is forced.

## 2. Square-basin geometry

For `A=k^2`, `U=(k+1)^2-1=k^2+2k`, the screening horizon is exactly `F=k`. Define `C4=floor(U^(1/4))`.

For a prime witness `q<=C4`, put `x=A/q`. If a prime r satisfies `x<r<=x+G` and `G<=(U-A)/q=2k/q`, then `A<q*r<=U`. Also `x>F` throughout the certified range, hence `r>F`, so q*r has q as its only candidate prime divisor and forces q.

It is enough to impose the worst-core inequality

`G*C4<=2k`.

## 3. External computation premise

This checkpoint uses the same explicitly external Oliveira e Silva prime-gap computation premise as the earlier R005 gap transfer:

- selected double-checked cofactor region through `X=4*10^17`;
- finite gap bound `G=1328`;
- operationally, for cofactor x with `x+G<=X`, a next prime is available inside `(x,x+G]`.

Enterprise Math does not reproduce or re-prove that external computation here. The executable verifies only the downstream integer inequalities.

## 4. Exact finite range

The exact first k satisfying `1328*C4<=2k` is

`k=440,232`.

At that endpoint the margin is exactly zero; at `k=440,231` it is -2.

The largest cofactor point in the fourth-root core occurs at q=2. Conservatively requiring

`k^2/2 + 1328 <= 4*10^17`

gives the exact upper endpoint

`k=894,427,190`.

The next k leaves the chosen external finite computation region; it is not a mathematical counterexample.

## 5. Consequence

Throughout

`440,232 <= k <= 894,427,190`,

under the declared external gap premise:

1. every fourth-root-core witness is forced;
2. T-A21 gives residual `Omega<=3`;
3. generic residual structure gives `Omega>=3`.

Hence every square-basin residual in that finite range, if any, has exactly three prime factors counting multiplicity.

This does not say every basin has a residual and does not say every basin lacks a least basis. It is a finite multiplicative-complexity theorem for the unresolved fiber.

## 6. Relation to the exact finite family

The existing 49-basin / 50-residual exact family already exhibits only `Omega=3` residuals and fully forced fourth-root cores. The external-gap transfer shows that the same arity constraint must persist across a vastly larger finite k interval under the declared computation premise, even without enumerating each basin.

Thus both routes support the same precision-layer interpretation:

`fourth-root precision -> three-factor unresolved shell`.

## 7. Next

Inside the certified interval, the open p=2 question is no longer residual arity. It is classification of the exact three-factor shell `q^2 r` and `q r s` together with the non-forcedness conditions on candidate support.

An `Omega>=4` residual inside this interval would contradict the transferred fourth-root-core theorem under its stated external premise.
