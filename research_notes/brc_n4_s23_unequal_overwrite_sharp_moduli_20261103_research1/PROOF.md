# BRC S23: exact two-constant overwrite stability on the full parameter square

2026-11-03, Asia/Shanghai. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**.
Frozen scientific model: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Predecessor: `189bd5e097e8781ad9cfe6ca05b4aa771739f040` (sharp common-beta result).
All statements below are mathematical facts about the frozen six-labeled-source positive-probability branch model and the specified algebraic future observers.

## Observer and all-real scope

For `z=(z0,...,z10) in [0,1]^11`, the six ordered triple indices are

```
A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10)
R(p,q,r)=(p,(1-p)q,(1-p)(1-q)r,(1-p)(1-q)(1-r))
M=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
   (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).
P(z)_i=sum_j M_ij R(z_Aj,z_Bj,z_Cj)/20.
```

A mask is the integer sum of `2^k` over upstream gate indices `k=0,...,4`. Let `U_mask^beta` replace exactly those upstream gate values by a known `beta` and leave downstream values intact. For each of four minimum two-probe families, write `N` for the mask omitting index 2 and `E` for the mask containing index 2:

| Original unordered family | N | E | N contains gate 3 or 4? |
| --- | ---: | ---: | --- |
| (3,31) | 3 | 31 | no |
| (7,27) | 27 | 7 | both |
| (11,23) | 11 | 23 | 3 |
| (15,19) | 19 | 15 | 4 |

Choose independently `beta_N,beta_E in [0,1]`, put `a=1-beta_N`, `b=1-beta_E`, and observe all six labeled four-outcome rows in the baseline `P(z)`, plus `P(U_N^beta_N(z))` and `P(U_E^beta_E(z))`. Let `d(z,w)` be the maximum total variation between corresponding labeled rows in these three views. Define

```
sigma_N,E(beta_N,beta_E)
   = inf_{z != w in [0,1]^11} d(z,w)/||z-w||_infinity.
```

## Theorem — exact sharp modulus for every real unequal overwrite pair

**For all** `beta_N,beta_E in [0,1]`,

```
sigma_(3,31)  = min(a, b^2/21).
sigma_(27,7)  = min(a^2, b^2/21).
sigma_(11,23) = min(a^2, b^2/21).
sigma_(19,15) = min(a^2, b^2/21).
```

The infimum is attained for all choices, including the endpoint cases `a=0` or `b=0`. In particular all four observers are globally injective exactly when `a>0,b>0`.

### Lower bound for the entire continuous eleven-cube

For `d=d(z,w)`, a difference in any one outcome-event probability is at most its four-outcome total variation. Denote observations in the baseline, non-2 and exposing-2 views by `O^0,O^N,O^E`.

**Roots.** All first-outcome probabilities in labeled rows 0,1 equal the root `z0`, while those in rows 3,4 equal `z1`. Thus `|Delta z0|,|Delta z1| <= d` from the baseline.

**Middle gates.** Both raw sources 0,1 use root 0 and middle gate 2. Both have their root overwritten by `N`, while middle gate 2 remains intact. Consequently `O^N_0[1]=a*z2` exactly, so `|Delta z2|<=d/a`. The unmixed source 2 has root 0 and middle 3; unmixed source 5 has root 1 and middle 4. Each of gates 3 and 4 is omitted from precisely one of `N,E` while the relevant root is overwritten. Its second-outcome event is `a*z_k` or `b*z_k`; hence `|Delta z3|,|Delta z4| <=d/min(a,b)`.

**Third gates with mixed rows.** Only `E` overwrites both upstream gates of original sources 0,1,3,4. Their third outcomes become `b^2*z5, b^2*z6, b^2*z8, b^2*z9`, respectively. The precise fixed source mixer has inverse rows

```
raw0=11*O0-10*O1, raw1=10*O1-9*O0,
raw3=(9*O3-5*O4)/4, raw4=(5*O4-O3)/4.
```

Therefore `|Delta z5|<=21d/b^2`, `|Delta z6|<=19d/b^2`, `|Delta z8|<=7d/(2b^2)`, and `|Delta z9|<=3d/(2b^2)`.

**Third gates with unmixed rows.** Source 2 holds `z7` downstream of roots (0,3); source 5 holds `z10` downstream of (1,4). Each pair is overwritten together in exactly one of `N,E`. Since observed rows 2 and 5 are unmixed, `|Delta z7|` and `|Delta z10|` are bounded by `d/a^2` when their exposing mask is N, or `d/b^2` when E. For N=3 neither is exposed by N, so the worst inverse factor is `max(1/a,21/b^2)`. For N=27,11,19 the worst is at most `max(1/a^2,21/b^2)` (because `a,b <=1`).

Thus the claimed `d>=sigma*||z-w||_infinity` holds for **every real state pair** when `a,b>0`. When either vanishes the bound `d>=0` remains true.

### Three explicit sharp witnesses

In all witnesses start with `z0=...=z4=w0=...=w4=1` and all remaining coordinates zero unless specified. They have `||z-w||_infinity=1`.

1. **Exposing-mask mixed witness:** set `z5=1, w5=0, z6=0, w6=19/21`. Baseline and N hide both third gates (middle 2 remains 1). Only E reveals their differences, multiplied by `b^2`. After mixing, labeled rows 0 and 1 have opposite event differences exactly `+b^2/21` and `-b^2/21`, and all other rows match. Thus `d=b^2/21` for all four families.
2. **Non-2 middle witness:** keep downstream coordinates zero and change only `z2=1,w2=0`. Baseline hides middle 2 behind roots 0 and 1; E erases its value. In N, four affected raw sources change their second/fourth outcome probabilities by `+a/-a`; their source mixers preserve the magnitude. Thus `d=a`, in particular for N=3.
3. **Non-2 unmixed downstream witness:** for N containing 3 change only `z7=1,w7=0`; otherwise (N=19, which contains 4) change only `z10=1,w10=0`. Baseline hides the changed third gate; E leaves the relevant original middle gate equal to 1; N exposes both its upstream gates with weight `a^2`. The affected labeled row is unmixed. Thus `d=a^2` for each of N=27,11,19.

The lower bounds and corresponding minimum of these sharp upper witnesses coincide. Endpoints `a=0` and `b=0` are included because these same witnesses yield distinct states with `d=0`. QED.

## Optimal design and measurement accounting

For any of the four optimal mask families the maximal coefficient over independent `beta_N,beta_E in [0,1]` is **1/21**. The full optimizer sets are:

- `(3,31)`: `beta_E=0` and `0<=beta_N<=20/21`.
- `(7,27),(11,23),(15,19)`: `beta_E=0` and `0<=beta_N<=1-1/sqrt(21)`.

Thus common `beta=0` is one optimal design, but different overwrite constants generate an exact plateau of other optimizers. Setting `beta_N=beta_E=beta` recovers the predecessor's `(1-beta)^2/21` for every family.

The present observer uses **three** views (baseline plus two overwrites), each with 6 labeled sources and 4 outcomes: 72 raw displayed probabilities or 54 simplex-independent scalar outcomes. The predecessor single multiplicative-attenuation observation uses **one** 6-by-4 view (24 raw probabilities, 18 simplex-independent). These are measurement-layout counts, not a noise, wall-clock, or bit-complexity equivalence. Its earlier `lambda=1/2` inverse inequality has coefficient `1/84` as a *proved lower bound*, not a demonstrated sharp coefficient.

## Evidence, boundaries and next question

`VERIFY.py` uses Python standard-library exact `Fraction`: for all four families and 36 ordered pairs of overwrite constants in `{0,1/5,1/2,3/4,9/10,1}`, it directly builds the six-source model and checks 396 stated witness identities. On the 100 non-endpoint configurations it also reconstructs 500 deterministic rational state samples exactly and checks 500 exact stability inequalities. These are reproducibility checks; the real-cube theorem is the algebraic proof above.

All original source labels, mixture weights, four outcomes and ordered branch provenance are kept. No signed/phase cancellation or native Heartbeat physical evolution is claimed. This result does not change P000, the original ten-decoder minimax or native Result/Review authority.

**Next:** compute the best *forward* global Lipschitz coefficient for the same three-view operator and compare with the single-attenuation map using a matched probability-measurement cost and noise model. Separately investigate adaptive/unequal per-mask replacement budgets with a fixed number of modified gates.
