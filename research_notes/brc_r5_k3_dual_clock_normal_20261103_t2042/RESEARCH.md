# R5 K3 — a second all-real signed clock-normal family, with an exact witness invisible to the first sweep

Date: 2026-11-03 Asia/Shanghai. Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`.

## Provenance and scientific scope

The mother objective is a finite two-law stopped experiment for which the convex hulls of the FULL and seedless LR four-observer images agree but the real-behaviour images differ. This increment gives a second **necessary hull-equality test** in the already constructed strict *common terminal answer-label* K3 experiment; it does not change the experiment or the observer.

Frozen scientific inputs, carried unchanged from the immediate predecessor: Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate scientific predecessor is `research_notes/brc_r5_k3_common_label_clock_sweep_20261103_t1940/RESEARCH.md` at immutable commit `fccb7c25f9b1da0000e29e833633a7a112c359fc`. Current normative context was separately read on 2026-11-03 from Global Knowledge canonical main `00fc58769029f91313b7a6b61f475af04c67a965` and Enterprise Math main `15c62a5df0972f9d1bb61e684b1890934afb37f3`. P000 is unchanged, and the current ACTIVE worldview continues to govern provenance-sensitive BRC interpretation.

The four source labels remain C,I,BJ,IJ. Define `alpha=(1/2,2/3,1/2,3/4)`, `c=(1/8,1/6,1/16,3/32)`, `w=(1/4,(1-x)/4,y/8,i/8)`. FULL chooses real `0<=x,y<=1`, `0<=i<=1-x`, and real sourcewise `z_s,t_s,u_s in [0,1]`; LR has `i=(1-x)y` and shared `z,t,u`. Set `M_s=w_s alpha_s z_s`, `S_s=(2/3)M_s t_s`, `U_s=S_s u_s`, `d=y/16+3i/32`. Each of `p_s,q_s,r_s,v_s` lies independently in the open interval (0,1). The strict common-label experiment has exactly the previously established four observers:

```
eP=107/128-21x/128+d/4-(sum S)/2+sum_s p_s S_s/8
eQ=13/64+3x/64-d/2+(sum S)/8+sum_s q_s S_s/32
TP=3+sum M+(3/2)sum S+sum_s r_s U_s
TQ=3+(sum M)/2+(3/8)sum S+sum_s v_s U_s/4
```

## Theorem: complementary clock sweep for ALL real parameters

Let `0 < theta <= 96/11`, and define the four-dimensional signed normal and the individual source-time residuals by

```
n_2(theta) = (0,0,4,-theta)
g_s(theta) = 4 r_s - (theta/4) v_s
P_2(theta) = sum_s c_s max(g_s(theta),0)
N_2(theta) = sum_s c_s max(-g_s(theta),0)
B_2(theta) = 3(4-theta) + (8-3 theta/4) sum_s c_s.
```

For every real kernel parameter vector in `(0,1)^16`, and for **all real behavioural policies**, the support functions are exactly

```
h_FULL(n_2(theta)) = B_2(theta) + (2/3) P_2(theta)
h_LR(n_2(theta))   = B_2(theta) + (2/3) max(P_2(theta)-N_2(theta),0)
Delta_2(theta)    = (2/3) min(P_2(theta),N_2(theta)).
```

Consequently strict hull separation occurs whenever the four `g_s(theta)` contain both a positive and a negative entry. Since all `c_s` are positive, a separating `theta` exists **within this family** precisely if the ratios `r_s/v_s` are not all equal and `min_s(r_s/v_s)<6/11`. The time-only formula is independent of all eight answer probabilities `p_s,q_s`.

### Proof

For one unit of source carrier `w_s alpha_s`, maximizing the scalar readout `4 TP-theta TQ` over its three nested controls has four deterministic-stage increments:

```
V0 = 0
V1 = 4-theta/2
V2 = 8-3 theta/4
V3 = 8-3 theta/4 + (2/3)(4 r_s-theta v_s/4).
```

For the entire declared interval, `V2-V1=4-theta/4>0`, and `V2>0`. Moreover `V3 > 8-11 theta/12 >=0`, by `r_s>0,v_s<1`. Thus stages 0 and 1 never improve over stage 2, and all candidate maximizing stages 2 and 3 have nonnegative sourcewise signed increments. The signed constant term is `3(4-theta)`, independent of upstream controls. Every `w_s alpha_s` is componentwise at most `c_s`, with simultaneous equality at the feasible corner `(x,y,i)=(0,1,1)` for FULL and LR. Consequently every maximizing sourcewise stage assignment (FULL) and every maximizing common stage assignment (LR) is globally attained at that corner: increasing any nonnegative carrier cannot reduce the readout. For arbitrary real `z,t,u`, the source contribution is multilinear and admits a convex decomposition into the four deterministic stages; common LR controls generate the same decomposition with one common stage. Therefore no nonvertex behavioural strategy exceeds these deterministic maxima.

At that corner, the FULL source picks the larger of `V2` and `V3`, contributing `(8-3theta/4)+(2/3)(g_s)_+`. LR picks the same stage for all sources, and its optional final stage adds `(2/3)max(sum_s c_s g_s,0)`. This gives the displayed formulas and their difference `min(P_2,N_2)`. The ratio criterion follows because `g_s(theta)` has its unique zero at `theta=16 r_s/v_s`; all residuals start positive as theta tends to 0, and mixed signs occur exactly when one threshold falls below theta and another lies above theta within the specified interval. This completes an all-real proof rather than an interpolation from samples.

## Exact independent witness: previous sweep remains identically zero

Use positive rational probabilities

```
p=(1/4,1/2,3/4,1/2), q=(3/4,1/2,1/4,1/2),
r=(1/5,1/2,1/5,1/2), v=(4/5,9/10,4/5,9/10).
```

In the **first** sweep `n_1(theta)=(0,0,-theta,4)` for `0<theta<=9/8` (immediate predecessor), all residuals stay strictly positive: on `0<theta<=1`, `v_s-theta r_s>=v_s-r_s>0`; on `1<=theta<=9/8`, their minimum is at `9/8`, with values `(31/80,3/20,31/80,3/20)`. Hence `Delta_1(theta)=0` for the **entire continuous first-sweep interval**, not merely for a sampled grid.

For the **second** sweep at theta=8, the source residuals are `(-4/5,1/5,-4/5,1/5)`. Their weighted masses are `P_2=5/96` and `N_2=3/20`, giving

```
n_2(8) = (0,0,4,-8)
h_FULL = -797/72;  h_LR = -533/48
Delta_2(8) = 5/144 > 0.
```

The actual FULL behaviour `(x,y,i)=(0,1,1)` and source stages `(2,3,2,3)`, where stage 2 means `(z,t,u)=(1,1,0)` and stage 3 means `(1,1,1)`, gives the exact four-observer point

```
W = (107/144,257/1536,1147/288,27/8).
```

It satisfies `n_2(8) dot W = -797/72`. Since `||n_2(8)||_1=12`, the support hyperplane certifies

```
distance_inf(W,conv O(LR)) >= (5/144)/12 = 5/1728.
```

The first and second normal families expose distinct information in the same BRC source space. Retaining the four source labels until the extremization is essential: aggregating `g_s` before separate FULL control would erase the positive/negative residual split.

## Actual execution and verification scope

`VERIFY.py` is a standalone standard-library `fractions.Fraction` test. It exhaustively enumerates 6 upstream FULL corners times 4^4 source stages = 1,536 FULL deterministic observations, and 4 LR corners times four common stages = 16 LR deterministic observations, for each of four rational kernels and six rational theta values in `(0,96/11]`. It checks the two exact support functions and their gap at each of the 24 configurations (72 assertions), the explicit support-attaining witness and support values (4 assertions), and the rigorous old-sweep endpoint positivity for each of four sources (8 assertions): **84 exact assertions passed**. `EXACT_OUTPUT.txt` is the observed program output. The arbitrary-real theorem uses the analytical stage and carrier proof above; the computation crosschecks exact rational arithmetic in the stated finite sample.

## Native authority and continuation

The connected GitHub principal was `awdawmip` with admin/push access. At 2026-11-03T12:45:52Z the Enterprise Math Site reported `static_machine_readonly` and `research_authority_granted=false`. A bounded owner query returned `CONTROL_QUOTA`, so no active owner was certified by this run. The source notes are portable author-side material, not a CLAIM, Result or independent Driver acceptance. No changes are made to the immutable scientific pins, protected P000 or ACTIVE worldview.

The mother objective remains open: seek a nontrivial parameter family whose **complete** four-dimensional hulls agree but actual behaviour images differ. The next distinct exact subproblem is specified in `NEXT_TASK.md`.
