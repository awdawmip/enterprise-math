# BRC N=4 / S23: exact K=17 phase classification for 1/4 ≤ s ≤ 1/3

Date: 2026-11-05 (Asia/Shanghai). Author-side analytic proof and executed exact rational certificate. Scientific source remains frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This continues the verified author-side frontier `89acac9cbdefbc6283a98f894c0589177ade295e` in PR #1765. Independent review and native Result admission are pending.

## Original typed experiment

Let a=11/21, b=10/21. Source T is the ternary pair P=(as,1-s,bs), Q=(bs,1-s,as); its cost is 2-s. B is the specified Bernoulli projection with P=(as,1-as), Q=(bs,1-bs), cost 1. Define
`fT(t;s)=-log(1-s+s(a^t b^(1-t)+b^t a^(1-t)))`,
`fB(t;s)=-log(s a^t b^(1-t)+(1-as)^t(1-bs)^(1-t))`,
`F(m,n;s)=max_{t in [0,1]} [m fT(t;s)+n fB(t;s)]`,
`CT=F(1,0)`, `CB=F(0,1)`, and `H=fB(1/2;s)`.
The common t is essential in mixed designs. Optimize F over nonnegative integer pairs satisfying `(2-s)m+n ≤ 17`. For each feasible m, positive information implies the maximal n equals `n_m=17-2m+floor(ms)`.

## Theorem: three continuous switches, three internal feasibility activations

There are exactly three roots α,β,γ, defined respectively by
`F(8,3;α)=17CB(α)`, `F(7,5;β)=17CB(β)`, and `10CT(γ)=17CB(γ)`,
with
`1/4 < α < 251/1000 < 2/7 < β < 287/1000 < 3/10 < γ < 301/1000 < 1/3`.

The complete classification is:

| Exact parameter set | Unique global maximizer, except at ties |
|---|---|
| [1/4, α) | (8,3) |
| {α} | exactly (8,3) and (0,17) |
| (α, 2/7) | (0,17) |
| [2/7, β) | (7,5) |
| {β} | exactly (7,5) and (0,17) |
| (β, 3/10) | (0,17) |
| [3/10, γ) | (10,0) |
| {γ} | exactly (10,0) and (0,17) |
| (γ, 1/3) | (0,17) |
| {1/3} | (9,2) |

Thus the new integer-budget activations at s=2/7, 3/10, 1/3 are genuine global optimizer jumps. α, β, γ are continuous equal-information transitions on their respective open feasibility cells.

## Complete feasible-set reduction

For 1/4≤s<1/3, maximal n are: m=0,1,2,3: `17-2m`; m=4,5,6: `18-2m`; m=7: 4 until s<2/7, then 5; m=8: 3; m=9: 1; m=10: feasible only from s=3/10, with n=0. At s=1/3, m=3,6,9 newly gain one B, yielding (3,12), (6,7), (9,2).

Use the prior proved strict `CT<2CB` for 0<s<1. New exact certificates establish all inequalities in their closed domains:
`D16=16CB-9CT>0` on [1/4,1/3],
`D7=7CB-4CT>0` on [2/7,1/3],
and `D12=12CB-7CT>0` on [3/10,1/3].
Every one follows from a positive left-endpoint interval and a positive global lower derivative bound on the listed rational subdivisions.

On [1/4,2/7), m=1..3 lose to (0,17) by CT<2CB; m=9 loses by D16. For m=4..7 the points lie at or strictly below the line segment from (0,17) to (8,3): at m=4 the point is its midpoint (4,10), and at m=5,6,7 its n is strictly below the interpolated n. Because F is convex and strictly increasing in n, these are dominated by the greater of the endpoint designs. Hence only (0,17) and (8,3) can win.

On [2/7,3/10), all competitors except (0,17),(7,5) lose to (0,17): m=1..3 by CT<2CB; m=4,5,6,8 by D7; m=9 by D16. On [3/10,1/3), D12 also excludes (7,5), leaving only (0,17) and (10,0). At s=1/3 the three new designs (3,12),(6,7),(9,2) are collinear with (0,17), and strict convexity on their interpolation (proved below) makes (9,2) the only possible new winner. The other previous designs have already been strictly excluded by D7/D12/D16 or their earlier endpoint comparison.

To see strictness on the linear interpolation, T has its unique maximizing Chernoff t=1/2, while B's unique maximizing t differs from 1/2 whenever 0<s<1. Indeed for p=as>q=bs, writing `psi(u)=sqrt(u)*log(u)/(u-1)` on u>1 gives `qB'(1/2)=(p-q)[psi(p/q)-psi((1-q)/(1-p))]<0` for the B Chernoff coefficient `qB`, because psi is strictly decreasing and `p/q>(1-q)/(1-p)` when s<1. Thus B and every mixed design with positive T weight do not share the same maximizing t. Equality in a convex interpolation of their optimized F-values is impossible. This removes interior co-maximizers at α and at the boundary s=1/3.

## Unique roots from rational convex-secant certificates

For each fixed t the functions fT(t;s), fB(t;s) are convex in s, so every F(m,n;s), CT, CB is convex. For δ=1/10000 and a closed subinterval [l,r], set
`L_l=[CB(l)-CB(l-δ)]/δ`,
`U_{m,n,r}=[mCT(r+δ)+nCB(r+δ)-mCT(r)-nH(r)]/δ`.
By convexity and `mCT+nH ≤ F(m,n) ≤ mCT+nCB`,
`[F(m,n;y)-F(m,n;x)]/(y-x) ≤ U_{m,n,r}`,
`[CB(y)-CB(x)]/(y-x) ≥ L_l`
for all l≤x<y≤r. Hence `17L_l-U_{m,n,r}>0` proves strict decrease of `F(m,n)-17CB` throughout the subinterval. The attached exact program checks all 8 rational subdivisions of each of [1/4,2/7] for (8,3), [2/7,3/10] for (7,5), and [3/10,1/3] for (10,0), with strictly positive lower margins.

For `D=kCB-jCT`, the same convexity gives lower slope `k[CB(l)-CB(l-δ)]/δ - j[CT(r+δ)-CT(r)]/δ`. The exact program verifies positive starting value and positive lower slope for D16 on the three major cells, D7 on the last two, D12 on the last cell.

The exact source inequalities establish the signs:
`8CT(1/4)+3H(1/4)>17CB(1/4)`, `8CT(251/1000)+3CB(251/1000)<17CB(251/1000)`;
`7CT(2/7)+5H(2/7)>17CB(2/7)`, `7CT(287/1000)+5CB(287/1000)<17CB(287/1000)`;
`10CT(3/10)>17CB(3/10)`, `10CT(301/1000)<17CB(301/1000)`.
Continuous functions plus the strictly decreasing difference give one and only one crossing in each cell.

At s=1/3 the exact bound `9CT+2H>17CB` proves (9,2) beats (0,17). Strict convex interpolation excludes (3,12),(6,7); all previously feasible alternatives are below (0,17). QED.

## Verification status and next mother-objective connection

`VERIFY.py` uses only Python standard-library `Fraction`, `isqrt`, rigorous 10^-48 sqrt brackets and 34-term logarithm series with a geometric-tail enclosure. Every printed `GT num/10000000000000` is a proven strict lower bound. All 43 assertions completed and the final PASS marker was produced on actual local execution; see `RUN_EVIDENCE.txt`. Exact paper proof is author-side; independent review is pending.

This is the exact finite-budget, typed statistical sampling subproblem. The mother ten-label S23 minimax objective retains its previously recorded open bounds [1/2,2/3]. The next executable subproblem is the cell `1/3≤s<2/5`, where the (9,2) boundary design first wins, and new cost-residue activations may occur.
