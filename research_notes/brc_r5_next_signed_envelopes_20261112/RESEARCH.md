# R5 — next two signed affine envelopes and ten new collision transfers

Date: 2026-11-12 (Asia/Shanghai). Status: researcher-side exact rational finite theorem, pending formal Source Result and independent review. Frozen *external P/Q–BRC Blackwell auxiliary observer*, not native X6 dynamics.

## Exact provenance

Continuation of Draft PR #2123 (head `45ee355d94cf3bf40b4a179420fec13ad12a119e`) and the uniform signed affine-prefix theorem in Draft PR #2122. Immutable scientific sources: global pin `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math pin `86149263e38c22292c9def1e0f69092efa1be77e`; original 28-rational state `X`, 15 labeled residual moves `M_1,...,M_15`, observation matrix and terminal ray epsilon from commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`, file `research_notes/brc_r5_sharp_nonlocal_fifteen_ray_20261111/VERIFY_R5_SHARP_RAY.py`. The perturbation `H` has source-3 target (1,2,6) components (-23,+28,-5), opposite at source 1. All claims preserve frozen inputs, original observer, P000 and all current task owners.

Put `x=155682221/25142124560000000`, `r=eta/x`, `X(r)=X+x*r*H`, and `epsilon_max=9/115400000`. For nonempty mask S of 15 atoms define `P_S=36 sum_(a in S) M_a` (integral 28-vector), and
`tau_S(r)=min_(k:P_S[k]<0) 36*(X[k]+x*r*H[k])/(-P_S[k])`.

## Theorem 1: the next prefix-minimizer chambers are exact

The previous exact global minimizer chambers ended at `r+=1/2507` and `r-=-1/4945`. Immediately beyond those boundaries, precisely two mask minimizers exchange at each boundary:

- at `r+=1/2507`, masks **11236, 29474**, from target0/source3 to target1/source3 on the increasing-r side;
- at `r-=-1/4945`, masks **14357, 26629**, from target1/source3 to target0/source3 on the decreasing-r side.

After these endpoint changes, there is **no further coordinate minimizer switch** for any of the 32,767 nonempty masks throughout the open intervals

`1/2507 < r < 1/1265`, and `-1/2461 < r < -1/4945`.

Their *sharp next* endpoint changes are:

- at **r=1/1265**, masks **6516, 6714, 18788, 18986, 23214, 28732, 30846** exchange from target0/source3 to target1/source3;
- at **r=-1/2461**, masks **10926, 28966** exchange from target1/source3 to target0/source3.

The affine winning values at the endpoints agree exactly, and the competing slopes differ, so no slightly larger two-sided minimizer chamber exists.

**Finite proof.** For every S, enumerate all negative P_S coordinates. Each candidate is an exact affine function `a_(S,k)+r*b_(S,k)`. At the starting boundary select the tied minimizer of least slope for increasing r (greatest slope for decreasing r). For each competitor with more favorable eventual slope, solve the unique exact equality `(a_w-a_k)/(b_k-b_w)`. All competitors with less favorable slopes never overtake after that boundary. Exact enumeration of all 32,767 masks gives the first global positive crossing `1/1265` and first negative crossing `-1/2461`, with the exact masks listed. Affine comparisons at both interval endpoints then prove the claim uniformly, not merely for sampled values.

Both the initial vector and the full 15-atom endpoint remain nonnegative throughout each *closed* extended interval (the initial 28 entries are all strictly positive). Their initial and terminal coordinate expressions are affine in r, so verification at two endpoints suffices. The ray terminal time remains exactly `epsilon_max`: its existing target0/source2 zero coordinate is untouched, and no other terminal coordinate becomes negative.

## Theorem 2: seven positive and three negative interior collision transfers

Inside each extended open minimizer chamber, the 32,767 subset first-zero time forms consist of the **same 1144 fixed forms** `F_n=36*x/n`, the **same three moving forms** `Q_q=x*(1-23r)/q` for `q in {3,12,15}`, the endpoint, and the beyond-endpoint class. For generic r there are 1147 distinct interior phase times; when a fixed and moving form coincide this number falls.

The exact new crossing parameters `r=(n-36q)/(23n)` and the redistribution of *complete legal labeled atom permutations* are as follows. The transfer is `Q-loss-after minus Q-loss-before`, with “before/after” in the direction of motion away from r=0. The fixed phase changes by the opposite amount.

| Direction | Crossing r | Q q | F n | Exact loss transfer to Q |
|---|---|---:|---:|---:|
| positive | 1/2093 | 15 | 546 | +27,345,600 |
| positive | 5/10051 | 12 | 437 | +817,628,752 |
| positive | 7/12581 | 15 | 547 | +1,336,050,192 |
| positive | 1/1679 | 12 | 438 | +44,684,640 |
| positive | 2/3151 | 15 | 548 | +333,390,528 |
| positive | 7/10097 | 12 | 439 | +135,540,768 |
| positive | 1/1403 | 15 | 549 | +337,459,680 |
| negative | -1/4117 | 15 | 537 | -88,495,488 |
| negative | -1/3289 | 12 | 429 | -344,005,152 |
| negative | -1/3082 | 15 | 536 | -266,265,216 |

All ten collisions are in the *open* extended minimizer chambers, separate from their endpoints. At the positive endpoint `1/1265`, Q3 meets F110; at the negative endpoint `-1/2461`, Q3 meets F107. Thus the next minimizer change and a phase-time coincidence happen at the same exact parameter, but “coordinate minimizer change”, “collision of phase values”, and “legal order-count drop” are distinct mathematical notions.

**Exact combinatorial proof.** The tags `F_n/Q_q/E/O` attached to each subset are fixed within each open minimizer chamber. To calculate permutation counts at phase time theta, use Boolean-lattice DP `ways(empty)=1` and `ways(S)=0` if its first-zero time is below theta (strict variant: at-or-below theta), otherwise `sum_(a in S) ways(S\\{a})`. The difference of inclusive and strict full-mask counts is the exact loss at theta. For each crossing, use exact rational midpoints on either side of adjacent crossings, count F and Q phase losses separately, and verify their pairwise sum stays constant. All 10 integer transfers above are obtained this way.

On both new open minimizer chambers, the exact terminal number of valid 15-label orders at `epsilon_max` is **3,514,190,816**, unchanged from the prior ray. This is an actual fixed-atom statement, not a uniform bound for arbitrary hidden-fiber endpoints.

## Reproduction, scope and unresolved work

The accompanying `VERIFY_NEXT_SIGNED_ENVELOPES.py` runs the immutable parent R5 verifier in the same checkout, enumerates all 32,767 masks, derives every affine candidate with `Fraction`, proves both sharp next boundaries by exact crossing search, classifies phase forms, checks initial/terminal nonnegativity, and recomputes all ten labeled-order loss transfers by integer DP. `EXACT_OUTPUT.txt` records an independently executed equivalent locally transcribed exact algorithm; the published wrapper has not yet been rerun from its remote GitHub bytes in an independent environment.

Next: cross `r=1/1265` and `r=-1/2461` to derive the subsequent envelope cells and determine whether the set of 1144 fixed forms changes after the new endpoint swaps. Distinguish form disappearance, new threshold activation and actual schedule-count changes. Preserve the same scientific pins, P000 and current owner scope. No CLAIM or Source Result is inferred from this Draft PR.
