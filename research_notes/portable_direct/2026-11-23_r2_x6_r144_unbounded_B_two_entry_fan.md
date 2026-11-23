# X6 R144 — exact two-entry fan on an unbounded positive-weight half-strip

Date: 2026-11-23 (Asia/Shanghai). Status: author exact integer/rational proof and verifier PASS; independent mathematical review pending.

## Frozen scientific input and scope

This continues the R143 scientific frontier. Retain P000 V5, ACTIVE Heartbeat X6, all six pairwise BRC observations, and the immutable R121/R122 scientific pins:
- `awdawmip/enterprise-math@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd:research_notes/portable_direct/2026-11-23_r2_x6_r121_small_port_exact_optimizer.md`
- `awdawmip/enterprise-math@0687aa24f5402da3b35f914dd6907967a9805b94:research_notes/portable_direct/x6_r122_small_port_near_exclusion_certificate.json`

Source predecessor: `research_notes/portable_direct/2026-11-23_r2_x6_r143_closed_upper_endpoint_and_boundary_layer.md` at GitHub commit `aaaef7809a05edab42704faae2efe9ffdc341a6d`.

Use integer Port 10, `q(a)=max(sum positive components,sum absolute negative components)<=10`, `a=(x,y,z) !=0` modulo reversal `±` only (positive multiples remain distinct). There are exactly 1,935 such unoriented integer directions. Define heights `h=(0,x+3y+6z,3x+12y+30z,7x+39y+126z)`, six gaps `g_ij=|h_j-h_i|` in lexicographic pair order, and positive capacities `s=(136+B,312,136+D,B+176,B+D,176+D)`. Let `F(a;B,D)=max_ij g_ij/s_ij`, `eta(B,D)=min_a F(a;B,D)`, and `N(B,D)={a/±: 2F(a;B,D)<3eta(B,D)}`.

This is an exact observer theorem on a declared centered-three-axis slice of the native X6 world. The conclusion concerns the six retained readouts; no native time-dynamics reduction or future-operation redundancy claim is made.

## Theorem — complete two-entrant fan

For **every pair of real numbers**

```
B >= 136,       528 <= D <= 1008,
```

the exact Port-10 optimizer is constant:

```
eta(B,D) = 1/104.
```

Write

```
C = {(1,0,0), (5,-4,1), (5,-1,0), (9,-5,1)}/±,
b = (4,-1,0)/±,     c = (6,-4,1)/±.
```

Then the **complete** strict-near set is

```
N(B,D) = C
       ∪ ({b} if D > max(1880/3, 832-B) else ∅)
       ∪ ({c} if D > 696 else ∅).
```

At equality on either wall, the corresponding entrant is excluded. No other Port-10 direction enters anywhere in the stated infinite-`B` strip. In particular the count takes exactly 4, 5, or 6. The first upper change from the four-direction core occurs at

```
D_*(B) = { 832-B,    136 <= B <= 616/3;
           1880/3,  B >= 616/3. }
```

For `136<B<616/3` the first b-entry wall has slope -1; for `B>616/3` it is horizontal. The second entrant c arrives across `D=696`. At `B=136`, both b and c first enter immediately above `D=696` (the equality point itself still has four directions). The break `(B,D)=(616/3,1880/3)` is the meeting of two active pair constraints for b.

## Proof by a finite exact integer certificate and monotonicity

Let `J={1,2,5}`, the three B-independent pair indices, with denominators `s_1=312, s_2=136+D, s_5=176+D`. All denominators are positive and nondecreasing in B or D.

**(1) Global optimizer lower bound.** The companion checker enumerates the complete 1,935-direction population. At the largest allowed D=1008, **every direction** possesses a `j in J` with

```
104*g_j(a) >= s_j(136,1008).
```

Selection counts are `j=1: 1920` and `j=2: 15`. Each selected j is independent of B; decreasing D only strengthens the inequality. Thus `F(a;B,D)>=1/104` for all directions throughout the entire half-strip. Conversely, `a=(9,-5,1)` has `g_1=3` and `s_1=312`, and at the lowest corner `F(a;136,528)=1/104`. Since increasing either B or D can only decrease its remaining five pair ratios, the constant pair guarantees `F(a;B,D)=1/104` everywhere. Hence `eta=1/104`.

**(2) Four permanent insiders.** At the smallest-denominator corner `(136,528)`, the exact scores of the four C members, in the order above, are `7/664, 1/88, 7/704, 1/104`, all strictly below `3/208=3eta/2`. Increasing B,D weakly decreases each score. Thus all four remain strict insiders.

**(3) Permanent outsiders.** Exclude the four C directions and the two separately classified candidates b,c, leaving **1,929** directions. For every one, the exact checker finds an index `j in J` satisfying

```
208*g_j(a) >= 3*s_j(136,1008).
```

The selected pair counts are `j=1: 1890`, `j=2: 37`, `j=5: 2`. As in (1), these B-independent inequalities remain valid throughout the entire continuous half-strip. Therefore these 1,929 directions satisfy `F>=3eta/2` everywhere and are never in the strict-near set.

**(4) Complete status of b and c.** Their six gap vectors are exactly

```
g(b)=(1,0,11,1,12,11),
g(c)=(0,0,12,0,12,12).
```

For b, the pair scores with gap 1 are already below `3/208` when `B>=136`; pair 1 is zero. The three remaining nonzero gap restrictions are

```
11/(136+D)<3/208  iff D>1880/3,
12/(B+D)<3/208    iff D>832-B,
11/(176+D)<3/208  iff D>1760/3.
```

The third is implied by the first. Therefore b enters exactly when `D>max(1880/3,832-B)`. For c, the three nonzero ratios require `D>696, D>832-B, D>656`, respectively. Because `B>=136`, the first implies the other two. Therefore c enters exactly when `D>696`.

Steps (1)–(4) prove the formula over all real parameters, using finite exact integer enumeration only to certify permanent direction classes, not to extrapolate from sampled parameters.

## Reproducibility and limitations

The standalone `research_notes/portable_direct/x6_r144_unbounded_B_two_entry_fan_verify.py` regenerates all 1,935 integer directions using the original Port and ± convention; checks all 1,935 optimizer inequalities and 1,929 permanent outsider certificates at D=1008; verifies all four corner-insider inequalities, both entrant gap vectors and **96** full-population exact rational replays including equality and neighboring cases. It uses Python standard library `fractions.Fraction` only.

Actual local execution: `R144 UNBOUNDED-B TWO-ENTRY EXACT FAN CERTIFICATE PASS`, 1,935 optimizer certificates, 1,929 outsider certificates, 96 exact replays. Source checker SHA-256 of the locally executed bytes: `971136747267814a5969a5d163e8ff92b5e12a52430065d877b750f26859591c`.

Proof status: author mathematical derivation and exact finite certificate; independent review remains `NOT_REVIEWED`. The Source document, own Activity, native CLAIM/RUN, formally accepted Result and Review are separate operations.

## Next research

Continue below `B=136`, especially `20<B<136`, where `eta` changes optimizer witness before the next strict-near wall; identify the first upper membership wall across all B>20. Separately extend the present large-B fan beyond `D=1008` to locate the first optimizer branch change and distinguish it from the near-member changes. Preserve all six original pair observations and immutable scientific pins.
