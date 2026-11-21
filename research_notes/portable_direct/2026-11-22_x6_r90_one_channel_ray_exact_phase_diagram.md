# X6 R90 — 单通道精度射线的精确全整数格相图与三重并列壁

Date: 2026-11-22 (Asia/Shanghai).  
Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.  
Mode: independent portable research, no formal CLAIM/PROGRESS/Result.  
Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.  
Antecedents: R86 (nine-core values), R87 (hidden noncore ties), R88 (sharp uniform conditioning), R89 (parity-sum sufficient chamber). This proof is independent of the R86/R72 finite atlas.

## Exact question and result

Use the conditional positive-count degree-four BRC star-histogram observer with an unknown common additive offset, integer differences `a=(x,y,z)≠0` identified modulo sign, and
```text
q(a) = max(x⁺+y⁺+z⁺, (-x)⁺+(-y)⁺+(-z)⁺)
Z(a) = (0,2x+6y+12z,6x+24y+60z,14x+78y+252z)
g_ij(a) = |Z_i-Z_j|/2
F(a;w) = max_{i<j} g_ij(a)/(w_i+w_j)
η*(p,w) = min_{a≠0,q(a)≤p} F(a;w).
```

**Theorem R90 (one-channel exact phase diagram).** For every real `T>0` and **every integer Port budget `p≥11`**, set `w_T=(1,1,1,T)`. Then
```text
η*(p,w_T) = 1/(1+T)       for 0<T≤1,
             1/2          for 1≤T≤23,
             12/(1+T)     for T≥23.
```
The complete set of optimal **unoriented integer difference vectors** is:
- `0<T<23`: exactly `s=(10,-5,1)`, with `q(s)=11`;
- `T=23`: exactly the three vectors `(4,-1,0)`, `(6,-4,1)`, `(10,-5,1)`, with q values `4,7,11`;
- `T>23`: exactly `r=(6,-4,1)`, with `q(r)=7`.

The boundary `T=1` is only an analytical branch switch of the formula, not a change of the unique minimizer. At `T=23`, the optimal value is continuous, and the three-way tie includes `(4,-1,0)` **outside** the R86 nine-value core. This is a complete tie statement about the entire feasible integer lattice.

## Proof without finite atlas or computational assumption

Put `u=x+3y+6z`, `v=3x+12y+30z`, `h=7x+39y+126z`. The six half-gaps in order `12,13,14,23,24,34` are
```text
(|u|, |v|, |h|, |v-u|, |h-u|, |h-v|).
```
For `w_T`, the pair denominators are `(2,2,1+T,2,1+T,1+T)`. The crucial exact integer relations are
```text
v = 3(x+4y+10z),
v=0 ⇒ x=-4y-10z, u=-y-4z, h=-11u+12z,
therefore v=0 ⇒ h≡u (mod 12).
```
Also `u=v=0` iff `a=k(6,-4,1)` for an integer `k`. In particular the moment-map variables do not collapse native P000 state; they are only conditional histogram observables.

Direct substitution gives
```text
F(s;w_T) = max(1/2,1/(1+T)),   q(s)=11,
F(r;w_T) = 12/(1+T),          q(r)=7,
F((4,-1,0);w_T)=max(1/2,12/(1+T)), q=4.
```
We now show these attain the global infimum and exhaust ties.

**Case 0<T<1.** Let `R=1/(1+T)`, achieved by `s`. Any feasible `a` with `F(a;w_T)≤R` has `|u|,|v|,|v-u|≤2R<2`. Since `v` is divisible by 3, `v=0` and `u∈{-1,0,1}`. Moreover `|h|,|h-u|≤(1+T)R=1`. The congruence `h≡u (mod 12)` forces `h=u`; with `u=0` this would give `u=v=h=0` and hence `a=0`, forbidden. For `u=±1`, the two moment solutions are exactly `±s`. Hence `s` is uniquely optimal.

**Case 1≤T<23.** Let `R=1/2`, achieved by `s`. Any `a` with `F≤R` has `|u|,|v|,|v-u|≤1`, so `v=0`, `u∈{-1,0,1}`. Also `|h|,|h-u|≤(1+T)/2<12`. Together with `h≡u (mod 12)`, the only solutions are `(u,h)=(±1,±1)` with the matching sign; `u=h=0` gives zero vector. Thus `±s` are the only minimizers.

**Case T=23.** With `R=1/2`, the previous constraints become `|u|≤1`, `v=0`, `|h|,|h-u|≤12`, `h≡u (mod12)`. Their complete nonzero solution list modulo simultaneous sign is
```text
(u,v,h)=(0,0,12), (1,0,-11), (1,0,1).
```
Using the rationally invertible moment map (or direct substitution), these are precisely `(6,-4,1)`, `(4,-1,0)`, and `(10,-5,1)`. All have `q≤11≤p`, and each has `F=1/2`. No additional integer direction ties.

**Case T>23.** Let `R=12/(1+T)<1/2`, achieved by `r`. Every `a` with `F≤R` has `|u|,|v|≤2R<1`; hence `u=v=0` and `a=kr`. Then `F(kr;w_T)=12|k|/(1+T)`, so the only minimizer is `±r`. This exhausts every nonzero integer difference without a bound on `q`. ∎

## Interpretation, validation, and scope

For the one-channel ray, the R88 uniform `κ<11` condition and the R89 sufficient `K<6d` condition cease to certify uniqueness at `T≥11`, whereas R90 proves `s` stays uniquely optimal until the **exact threshold `T=23`**. The 23-wall has a genuine noncore third tie, illustrating the difference between an optimal-*value* core and an all-ties atlas.

Companion exact Python `Fraction` checker: `research_notes/portable_direct/x6_r90_single_channel_ray_verify.py`. It enumerates all 110,740 nonzero unoriented `q≤40` directions, with `T∈{1/2,1,11,22,23,24,100}`: 775,180 direction-parameter combinations, no below-optimum cases, and exact tie counts `1,1,1,1,3,1,1`. The checker is finite corroboration; the theorem is the integer-congruence proof above. Results: `x6_r90_single_channel_ray_results.json`. Independent peer review: NOT_REVIEWED.

Preserve the P000 V5 6D signed native Cell torsor, 120° native relation and three-force closure, joint/branch provenance, named Ports and heartbeat order. The present degree-four positive star-histogram observer is a conditional readout only; it supplies no native P000 event-operation fidelity certificate. No frozen scientific input was changed.

Next: classify exact boundary multiplicities for two independently varying channel weights and determine whether a finite congruence certificate can characterize all noncore tie walls; independently test a concrete P000 whole-triad, named-Port/time-order observation fiber.
