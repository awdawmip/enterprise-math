# R749SNI — Exact left transition on the Walsh t=1/2 off-diagonal ray

**2026-11-14**, Researcher `EM-DIRECT-487291`, Activity `RA-2006009B6E0119A16438F27D`. Author proof; NOT_REVIEWED. Frozen science `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Continue R749SNH at PR #2316, scientific snapshot `212c5c3a4ede1897aaac3c586cc35d4f4d09475b`; R749SNG at `74abff6fff03fb6defec95c6c505c69ea5b0832c`.

## Exact new theorem

In the same auxiliary Walsh signed-source model on `G=F_2^4`, retained characters `B={3,5,6,7,9,10,11,12,13,14}`, with `m_3=t=1/2`, `m_12=s`, remaining eight B moments zero, the unrestricted total-variation minimax radius satisfies, for **all real** `s in [1/2,3/5]`,

```
rho(1/2,s) = (13-10*s)/20.
```

Combining with proven R749SNH `rho(1/2,s)=(2-s)/4` for `3/5<=s<=1`, we now have the **entire** free-prediction ray:

```
rho(1/2,s) = (13-10*s)/20, 1/2<=s<=3/5;
rho(1/2,s) = (2-s)/4,    3/5<=s<=1.
```

The sharp first kink is **s=3/5**: the lower certificate switches from an event/positivity combination to a diametral source pair. At `s=1/2`, radius is `2/5`, matching R749SNG; at `s=3/5`, both formulas yield `7/20`. Calibrated prediction on `[1/2,3/5)` is a separate unresolved function; R749SNH already settled `[3/5,1]`.

## Exact source variables and two universal event bounds

Recall `A=chi_3,D=chi_12,P=chi_1,Q=chi_4,AD=chi_15`; all compatible `mu` have inverse Walsh form

```
16mu(x)=1+(1/2)A+sD+hAD+uP+vAP+wQ+zDQ >=0.
```

The shift symmetries flipping P and Q allow a minimax free decoder of form
`16q(x)=1+tau A+sigma D+eta AD >=0`; every such decoder has `1-tau-sigma+eta>=0` (the A=D=-1 block).

Define feasible source laws for `1/2<=s<=3/5`:

```
alpha_s: h=s-1/2, u=v=1-s, w=z=1/2;
beta_s:  h=3/2-s, u=v=w=z=0.
```

Both distributions normalize and have nonnegative atoms throughout the interval: alpha has four base blocks `1+2s,2-2s,1,0` with source magnitudes `2(1-s),0,1,0`, and beta has four base blocks `3,0,2s-1,2-2s`.

Index 16 atoms by `(A,D)=(++),(+-),(-+),(--)`, with `(P,Q)=(++),(+-),(-+),(--)` in each block. For the fixed events
`E_alpha={0,4,5,8,10}` and `E_beta={0,1,2,3,12,13,14,15}`,
the inequalities `TV(q,mu)>=mu(E)-q(E)` give

```
L_alpha=alpha_s(E_alpha)-q(E_alpha)=(11-8s-tau-sigma+3eta)/16
L_beta = beta_s(E_beta)-q(E_beta)=(3-2s-2eta)/4.
```

The positive weights `4/5`, `1/5` yield

```
(4L_alpha+L_beta)/5
 = (13-10s)/20 + (1-tau-sigma+eta)/20
 >= (13-10s)/20.
```

This holds for every symmetric admissible decoder; symmetrization proves the same minimax lower bound for arbitrary 16-atom decoders.

## Explicit legal decoder and complete upper certificate

For `1/2<=s<=3/5`, choose

```
tau=2-2s, sigma=2s-4/5, eta=1/5.
```

The four block numerators are `12/5,18/5-4s,4s-2,0`, all nonnegative throughout the interval.

Set `Uplus=|u+v|,Uminus=|u-v|,Wplus=|w+z|,Wminus=|w-z|`. Source nonnegativity is exactly `U,W>=0` and four constraints `1+A/2+sD+hAD >= U_A+W_D`. The six joint variables `(s,h,Uplus,Uminus,Wplus,Wminus)`, two s endpoint constraints and the eight source constraints form a bounded six-dimensional polytope. Both decoder and target radius are affine in s, so `TV(mu,q_s)-(13-10s)/20` is convex in all six variables. A maximum occurs at a vertex; test every 6-active-facet set among 10, using exact Fraction Gaussian elimination.

```
6-facet subsets: 210
nonsingular: 125
feasible bases: 34
distinct vertices: 22 (10 at s=1/2, 12 at s=3/5)
equality vertices: 6
upper-bound violations: 0
```

The standard-library certificate `R749SNI_LEFT_EXTENSION_EXACT_CHECK.py` uses the adjacent R749SNH verifier's complete rational vertex generator and independently tests all 22 exact vertices. Joint-polytope convexity proves the upper bound for every real s in the claimed interval, and combines with the event lower bounds to establish the theorem.

## Boundary and next scientific problem

This result is an exact auxiliary Walsh source-observation statement, with frozen scientific input retained. It neither changes P000 nor asserts a native signed Port/X6/V29/V39 implementation correspondence; review remains NOT_REVIEWED.

The free ray `t=1/2,s in [1/2,1]` is now closed. A useful next task is to derive the **calibrated radius on `[1/2,3/5]`** with its first sharp transition, and to extend the zero-penalty region around `(1/2,2/3)` to an open two-dimensional chamber.
