# X6 R92 — Exact sigma-five boundary atlas with 11/13/23 tie thresholds

Date: 2026-11-22 (Asia/Shanghai). Status: SYMBOLIC_AUTHOR_PROOF / EXACT_FRACTION_AUTHOR_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED. Scope: independent portable scientific work; no formal Task CLAIM/PROGRESS/Result/Review.

Frozen scientific foundation: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json⟧. Current behavioral rules read separately. Builds on R91 (`research_notes/portable_direct/2026-11-22_x6_r91_two_parameter_sharp_strip_and_five_tie_wall.md⟧). This is a conditional positive-count degree-four BRC star-histogram observation theorem with an unknown common additive offset, not an operation-preserving quotient of native P000 six-axis Cell/Link/Port/triadic-event/time data.

## Definitions and result

For nonzero `a=(x,y,z) in Z^3⟧, identify `a⟧ with `-a⟧, and define

```
q(a)=max(sum(max(ai,0)),sum(max(-ai,0)))
u=x+3y+6z, v=3x+12y+30z, h=7x+39y+126z
g=(|u|,|v|,|h|,|v-u|,|h-u|,|h-v|)
F_T(a)=max(g12/2,g13/6,g14/(1+T),g23/6,g24/(1+T),g34/(5+T))
eta*(p,T)=min{F_T(a):a!=0,q(a)<=p}.
```

**Theorem R92.** For every integer `p>=11⟧ and every real `T>0⟧ under weights `(1,1,5,T)⟧,

```
eta*(p,T) = 1/(1+T) for 0<T<=1;
            1/2       for 1<=T<=23;
            12/(1+T) for T>=23.
```

Define seven unoriented integer directions:

| Symbol | a | q(a) | First T with F_T(a)<=1/2 |
|---|---|---:|---:|
| a0 | (1,0,0) | 1 | 13 |
| j  | (4,-1,0) | 4 | 23 |
| b  | (5,-4,1) | 6 | 11 |
| r  | (6,-4,1) | 7 | 23 |
| c  | (9,-5,1) | 10 | 11 |
| s  | (10,-5,1) | 11 | 1 |
| d  | (15,-9,2) | 17 | 13 |

The **entire** minimum-attaining direction set, for the indicated Port domain, is:

| T | p=11..16 | p>=17 |
|---|---|---|
| 0<T<11 | {s} | {s} |
| 11<=T<13 | {s,b,c} | {s,b,c} |
| 13<=T<23 | {s,b,c,a0} | {s,b,c,a0,d} |
| T=23 | {s,b,c,a0,j,r} | {s,b,c,a0,j,r,d} |
| T>23 | {r} | {r} |

Thus the level `S=5⟧ of the former R91 interior `(1,1,S,T)⟧ strip has new flat walls at `T=11⟧ and `T=13⟧, with 3/4/5-fold ties, and a 6/7-fold vertex at `T=23⟧ depending on Port. At `T=13⟧, the R91 reported four/five ties are recovered exactly.

## Proof

The inverse integral moment map is

```
x=(19u-8v+h)/2,
y=(-14u+7v-h)/3,
z=(11u-6v+h)/12.
```

In particular `v in 3Z⟧, `h ≡ u+6v (mod 12)⟧ and `h ≡ u (mod 2)⟧. The kernel `u=v=0⟧ is exactly `Z r⟧, where `r=(6,-4,1)⟧ and `F_T(k r)=|k|*12/(1+T)⟧.

**Range `0<T<1⟧.** Since `F_T(s)=1/(1+T)⟧, suppose `F_T(a)<=F_T(s)⟧. Then `|u|<=2/(1+T)<2⟧ and `|h|,|h-u|<=1⟧. The congruence `h≡u (mod 2)⟧ forces `h=u in {-1,0,1}⟧. Moreover `h≡u+6v (mod12)⟧ gives `v⟧ even; together with `v in 3Z⟧, we have `v in 6Z⟧. If `v!=0⟧ then `|h-v|>=5⟧, whereas `|h-v|<=(5+T)/(1+T)<5⟧, contradiction. Hence `v=0⟧ and nonzero solutions are precisely `±s⟧. At `T=1⟧ the below-zero obstruction and the finite box below give the same unique direction.

**Range `1<=T<=23⟧.** Here `F_T(s)=1/2⟧. Any competitor `F_T(a)<=1/2⟧ also satisfies `F_23(a)<=1/2⟧, because the three T-dependent denominators are increasing. At `T=23⟧ the six inequalities imply the *complete* integer moment box

```
|u|<=1; |v|<=3; |v-u|<=3;
|h|<=12; |h-u|<=12; |h-v|<=14.
```

Since `v⟧ is a multiple of 3, we need only `u in {-1,0,1}⟧, `v in {-3,0,3}⟧, and integer `h in [-12,12]⟧. Impose the displayed inequalities and the three divisibilities `2|(19u-8v+h)⟧, `3|(-14u+7v-h)⟧, `12|(11u-6v+h)⟧. Substituting the inverse map, identifying `±⟧, and excluding zero leaves **exactly seven** entries `a0,j,b,r,c,s,d⟧ in the table. This is a complete *unbounded integer-lattice* certificate: every possible competing difference is in the box, regardless of q.

Each of these seven has `F_T>=1/2⟧ for `1<=T<=23⟧: all except `r⟧ have a fixed gap `|u|/2=1/2⟧ or `|v|/6=1/2⟧; `r⟧ has `F_T(r)=12/(1+T)>=1/2⟧. Therefore `eta*=1/2⟧ throughout this range. For a candidate in the box, its T-dependent inequalities are equivalent to

```
T >= max( 2 max(|h|,|h-u|)-1, 2|h-v|-5 ),
```

besides the fixed gap conditions. Evaluating these thresholds yields exactly `1,11,13,23⟧ as shown. Filtering by `q<=p⟧ yields the entire tie table.

**Range `T>23⟧.** Since `F_T(r)=12/(1+T)<1/2⟧, any `F_T(a)<=F_T(r)⟧ has `|u|<1⟧ and `|v|<=6*12/(1+T)<3⟧. Thus `u=v=0⟧ and `a=k r⟧. The unique nonzero minimum up to sign is `r⟧. The values and all ties are proved for every real T and every integer p>=11.

## Recalculation, validation and open boundary

The companion executable `x6_r92_sigma5_exact_verify.py⟧ computes the complete T=23 moment box by exact integrality, verifies all seven activation thresholds, and performs independent exhaustive `q<=30⟧ Fraction checks at ten rational T values and Port budgets 11,16,17,30. The machine JSON is `x6_r92_sigma5_results.json⟧. All these tests are author checks; the universal claim follows from the symbolic proof and finite moment-box completeness, not interpolation from samples.

Next question: classify the full two-parameter arrangement for `S>5⟧, especially the transition from the new `S=5⟧ tie strata to strict winner regions and Port-dependent noncore directions. Native P000 observation fibers and joint triadic time evolution remain a separate exact preservation target. Original continuation request `r2-20261122-0310-x6-r92-cont-observe-v1⟧ ended `FAILED / SOURCE_TREE_TRUNCATED⟧: owner and execution authorization not refreshed; no CLAIM/PROGRESS attempted.
