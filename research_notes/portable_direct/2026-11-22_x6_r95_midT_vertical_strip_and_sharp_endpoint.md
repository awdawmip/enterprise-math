# X6 R95 — Vertical 1≤T<11 BRC precision strip, exact Port atlas, sharp endpoint

Date: 2026-11-22 (Asia/Shanghai). Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED. Independent portable research; no Task CLAIM, PROGRESS, Result or Review. Frozen scientific source: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`. Builds on R92–R94 and preserves P000's native Cell/Link/Port, triadic-event and temporal-state scope as a separate preservation question.

## Model and theorem

In the conditional positive-count fourth-order BRC star-moment histogram observer with unknown common additive offset, set `w=(1,1,S,T)` for all real `S≥1` and `1≤T<11`. For a nonzero integer difference `a=(x,y,z)`, identify orientations `±a`, let

```
q(a)=max(sum_i max(ai,0),sum_i max(-ai,0)),
u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z,
g=(|u|,|v|,|h|,|v-u|,|h-u|,|h-v|),
F(a;S,T)=max(g12/2,g13/(1+S),g14/(1+T),
             g23/(1+S),g24/(1+T),g34/(S+T)).
η*(p;S,T)=min_{a≠0,q(a)≤p} F(a;S,T).
```

For every integer `p≥11`, the **exact all-integer-lattice optimum** is

```
η*(p;S,T) = 1/2       if p≤26 or S≤11,
             6/(S+1)  if p≥27 and S>11.
```

The complete set of minimizing unoriented integer differences is:

| Port budget | 1≤S<11 | S=11 | S>11 |
|---|---|---|---|
| 11≤p≤15 | {s} | {s} | {s} |
| 16≤p≤26 | {s} | {s,b} | {s,b} |
| p≥27 | {s} | {s,b,c} | {c} |

where `s=(10,-5,1),q=11`, `b=(14,-9,2),q=16`, `c=(24,-14,3),q=27`. Neither the optimal value nor the complete tie atlas depends on T anywhere inside `1≤T<11`.

**Sharp upper endpoint.** At `S=5,T=11,p=11`, the optimum is `1/2` and has precisely three unoriented minimizers `(5,-4,1),(9,-5,1),s`, so the same full tie atlas does **not** extend to `T=11`. This also recovers the R92 sigma-five tie wall.

## Proof covering the entire unbounded integer lattice

Direct substitution gives `F(s)=1/2` for every `S,T` in the theorem domain. Every integer difference has `h-u=6(x+6y+20z)∈6Z`, an exact divisibility constraint of the original integer moment map.

Suppose `F(a)≤1/2`. The 12- and 24-channel gaps imply

```
|u|≤1,     |h-u|≤(1+T)/2<6.
```

Because `h-u∈6Z`, necessarily `h=u`, with `u=-1,0,1`. The further exact integral congruences `v∈3Z` and `h≡u+6v (mod 12)` yield `v=6m`, `m∈Z`. The inverse integral moment map gives

```
a=(10u-24m,-5u+14m,u-3m).
```

**If S≤11**, the 13-gap bound yields `|v|≤(1+S)/2≤6`, so only `m=-1,0,1` survive. Modulo sign, the four candidates are `s,b,c,e=(34,-19,4)` with Port budgets 11,16,27,38. Their score comparisons are

```
F(s)=1/2,
F(b)=max(1/2,6/(S+1),5/(S+T)),
F(c)=6/(S+1),
F(e)≥7/(S+1)>1/2.
```

For `T≥1`, `F(b)≤1/2` precisely when `S≥11`; the same holds for `c`, and there is no candidate with strictly smaller score. Thus `s` alone wins for `S<11` and `s,b,c` tie at `S=11` as permitted by q.

**If S>11 and p≤26**, a strict improvement would satisfy `|u|<1` and `|h-u|<(1+T)/2<6`, hence `u=h=0`. Solving the two moment equations gives `a=kc` for nonzero integer `k`, with `q(a)=27|k|>26`, impossible. Therefore the optimum remains `1/2`. At equality the parameterization above applies; all terms with `|m|≥2` have `|x|≥38`, and for `|m|=1` only b has q≤26. Since `S>11`, b ties when p≥16.

**If S>11 and p≥27**, c is feasible with `F(c)=6/(S+1)<1/2`. Every competitor of score at most `F(c)` has `u=0` and `h-u=0`, hence is an integer multiple of c. Homogeneity makes `±c` the unique minimizing unoriented direction. QED.

**T=11 endpoint witness.** At `(S,T)=(5,11)`, `s` has score 1/2, and direct substitution for `(5,-4,1)`, `(9,-5,1)` also gives exactly 1/2. The previous all-lattice lower bound 1/2 at sigma-five is established in R92, so these are genuine additional minimizers. The exact q≤38 checker below independently confirms the three-way set for p=11.

## Recalculation and next question

`research_notes/portable_direct/x6_r95_midT_strip_verify.py` uses exact Python Fraction inequalities over all 95,133 unoriented q≤38 integer differences. It checks 144 `(p,S,T)` configurations across T=1,3,8,109/10; S=1,5,1099/100,11,1101/100,100; and Port budgets 11,15,16,26,27,38. All 4,250,232 in-budget score comparisons match the theorem, plus the exact T=11 sharp endpoint. `x6_r95_midT_strip_results.json` records the compact certificate. These are author calculations; the proof is the preceding integer divisibility argument, not finite sampling.

Next: classify `T≥11` and the new `h-u=±6` strata, including coexistence with the `S=11` Port wall. Continue separate native P000 operation/future-observation fiber work. Current control task and continuation reads ended `FAILED/SOURCE_TREE_TRUNCATED` under their original IDs; current Task owner and formal authorization are unverified; only portable scientific outputs are published.
