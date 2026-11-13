# R749SNH — An exact off-diagonal Walsh minimax ray and the calibration transition

**Date:** 2026-11-14. **Status:** author-side theorem and independent exact rational local checker; **scientific review:** NOT_REVIEWED.
**Input:** preserved frozen scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, following R749SNG at `74abff6fff03fb6defec95c6c505c69ea5b0832c` (PR #2309).
**Scope:** an auxiliary finite Walsh signed-source observer model. No native X6/V29/V39 event correspondence is claimed.
**Session:** own native session request `research2-20261114-r749snh-offdiag-session`; identity / RA resolved separately from this scientific statement.

## Exact theorem

Let `G=F_2^4`, `chi_k(x)=(-1)^{popcount(k & x)}`, and `B={3,5,6,7,9,10,11,12,13,14}`. The compatible source fiber `F(t,s)` consists of probability laws with `m_3=t`, `m_12=s`, all other eight moments indexed by `B` equal to zero. Define

```
rho(t,s) = min_{q in Delta(G)} max_{mu in F(t,s)} TV(mu,q)
rho_cal(t,s) = min_{q in F(t,s)} max_{mu in F(t,s)} TV(mu,q).
```

**Theorem (R749SNH).** For **every real** `s in [3/5,1]` on the genuinely off-diagonal line `t=1/2`,

```
rho(1/2,s) = (2-s)/4                                      [3/5, 1]
rho_cal(1/2,s) = (3-2*s)/5                                [3/5,2/3]
rho_cal(1/2,s) = (2-s)/4                                  [2/3,1].
```

In particular, the calibration penalty is `rho_cal-rho=(2-3*s)/20` for `3/5<=s<=2/3`, and zero for `2/3<=s<=1`. This locates an **off-diagonal calibration transition at s=2/3** on the line `t=1/2`.

## Full source fiber and reduction

Set `A=chi_3`, `D=chi_12`, `P=chi_1`, `Q=chi_4`, `AD=chi_15`. The inverse Walsh transform is a bijection between `F(t,s)` and feasible real `(h,u,v,w,z)`:

```
mu(x) = [1+t*A(x)+s*D(x)+h*A(x)*D(x)
          +u*P(x)+v*A(x)*P(x)+w*Q(x)+z*D(x)*Q(x)] / 16 >= 0.
```

The fiber and total variation are invariant under the two shifts that independently flip `P` and `Q`, keeping `A,D` fixed. Symmetrizing any decoder cannot increase its worst-case loss. Thus an optimal free decoder has form

```
q_{tau,sigma,eta}(x)=[1+tau*A(x)+sigma*D(x)+eta*A(x)*D(x)]/16 >= 0.
```

For calibrated decoding `tau=t=1/2` and `sigma=s`. Every compatible source can be represented for evaluating the loss of such a decoder by five nonnegative-or-real parameters `(h,Uplus,Uminus,Wplus,Wminus)`, where

```
U_A = |u+v*A|,    W_D=|w+z*D|,
b_{A,D}=1+(1/2)*A+s*D+h*A*D,
Uplus,Uminus,Wplus,Wminus >= 0,
b_{A,D} >= U_A + W_D  for the four (A,D) in {+1,-1}^2.
```

Any such magnitudes admit actual signed coefficients `u,v,w,z`, and all signs give the same TV against symmetric `q`. For any reduced source candidate `v` and decoder `q`,

```
TV(mu_v,q)=(1/32) * sum_{A,D in {±1}} sum_{P,Q in {±1}}
  abs(b_{A,D}+P*U_A+Q*W_D - (1+tau*A+sigma*D+eta*A*D)).
```

## Universal free lower bound from an explicit pair

For `1/2<=s<=1` define two source laws `mu^+_s,mu^-_s` by

```
h=s-1/2, Uplus= +2(1-s), Uminus=0, Wplus=+1, Wminus=0 (mu+)
h=s-1/2, Uplus= -2(1-s), Uminus=0, Wplus=-1, Wminus=0 (mu-)
```

Here signed `U,W` in these two lines are the actual `P,Q` coefficients in the inverse Walsh expansion, not the nonnegative reduced magnitudes. Equivalently `u=v=±(1-s)`, `w=z=±1/2`. The four base masses before `P,Q` are respectively `1+2s,2-2s,1,0`; the magnitudes `(2-2s,0,1,0)` obey the four exact atom nonnegativity constraints for all `s>=1/2`. Both distributions normalize to one.

Direct summation of their 16 probabilities gives

```
TV(mu^+_s,mu^-_s)=(2-s)/2.
```

The triangle inequality implies `max(TV(q,mu+),TV(q,mu-)) >= (2-s)/4` for **every** decoder `q`.

## Additional calibrated lower bound for s in [3/5,2/3]

Symmetrize a calibrated decoder, so `q=q_{1/2,s,eta}`. Besides `mu^+_s`, use the compatible law `nu_s` with

```
h=3/2-s, Uplus=0, Uminus=0, Wplus=2s-1, Wminus=0.
```

For `s in [3/5,2/3]`, this and `mu^+_s` are probability laws. Enumerate the 16 source atoms in the fixed order `(A,D)=(++),(+-),(-+),(--)`, and within each block `(P,Q)=(++),(+-),(-+),(--)`. Consider events

```
E_a={0,2,4,5,8,10},  E_b={0,1,2,3,12,13,14,15}.
```

For any `eta`, the total-variation event inequalities `TV(q,mu) >= mu(E)-q(E)` give

```
L_a = mu^+_s(E_a)-q(E_a)=(9-6s+2eta)/16,
L_b = nu_s(E_b)-q(E_b)=(3-2s-2eta)/4.
```

The coefficient combination `(4L_a+L_b)/5=(3-2s)/5` eliminates `eta`, proving the calibrated lower bound. The event inequalities hold for any `eta`; no optimizer hypothesis is used.

## Explicit upper-bound decoders

Free prediction on the entire slab `3/5<=s<=1`:

```
tau=(1-s)/2, sigma=1, eta=(1-s)/2.
```

This is a normalized nonnegative law supported on `D=+1`.

Calibrated prediction:

```
tau=1/2, sigma=s,
eta=3/10-s/5  for 3/5<=s<=2/3,
eta=s-1/2    for 2/3<=s<=1.
```

Each decoder has nonnegative 16 atom probabilities over its stated interval.

## Complete rational upper certificate: all real s, not grid sampling

Take the **joint** variables `(s,h,Uplus,Uminus,Wplus,Wminus)`. On either slab `[3/5,2/3]` or `[2/3,1]`, the entire source family is a bounded six-dimensional polytope with four inequalities `b_{A,D}>=U_A+W_D`, four inequalities `U,W>=0`, and two endpoint inequalities `lo<=s<=hi`: precisely ten affine facets (with redundancies at endpoints harmless).

Each candidate decoder is affine in `s`; for the proposed affine radius `R(s)`, `TV(mu_v,q_s)-R(s)` is **convex** in all six variables. Its maximum over the joint polytope therefore occurs at a vertex. Every vertex admits six linearly independent active constraints; test all `C(10,6)=210` combinations with exact `Fraction` Gaussian elimination, discard singular or infeasible candidates, and check every distinct vertex. The supplied Python standard-library script reproduces the complete finite certificate.

| Slab | Active combinations | Non-singular | Feasible bases | Distinct vertices | Free equalities | Calibrated equalities | Violations |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [3/5,2/3] | 210 | 125 | 24 | 24 | 10 | 8 | 0 |
| [2/3,1] | 210 | 125 | 25 | 15 | 8 | 5 | 0 |

The second slab contains an interior joint vertex at `(s,h,Uplus,Uminus,Wplus,Wminus)=(3/4,3/4,0,1/2,0,0)`, which is included in the complete enumeration. The first slab's vertices are all at its endpoints. Exact arithmetic proves all vertex inequalities without rounding. Convexity then yields the universal upper bounds. Combining with the universal lower bounds proves the stated formulas.

## Scientific scope, reproduction, continuation

This is a finite auxiliary Walsh source-observation model. It preserves the previously declared frozen scientific input, does not alter P000, and establishes no native X6/V29/V39 signed-Port correspondence. Independent scientific review: NOT_REVIEWED. This is not a new formal Task Result/Driver decision.

**Artifacts:** `R749SNH_OFFDIAGONAL_HALF_SWEEP_EXACT_CHECK.py` and `R749SNH_OFFDIAGONAL_HALF_SWEEP_RESULTS.json` in this directory. Run the Python 3 standard-library script; the result JSON records finite counts and exact bound comparisons.

**Next independent mathematical problem:** determine the first left transition `s<3/5` on the same `t=1/2` ray, particularly where free radius first meets the diameter lower bound, and extend the observed off-diagonal zero-calibration-penalty region to an exact two-dimensional chamber with dual witnesses. Native-event transport remains a separate task.
