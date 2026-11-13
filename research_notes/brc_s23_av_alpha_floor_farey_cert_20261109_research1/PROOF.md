# Sharp uniform floor-certification horizon of the frozen S23/AV alpha interval

Date: 2026-11-09 Asia/Shanghai. Status: **AUTHOR_SIDE EXACT NUMBER-THEORETIC PROOF**, contingent only on the previously published rigorous alpha interval. Independent review pending. Frozen scientific input remains `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Question

The S23/AV capacity machinery uses the irrational slope `alpha=(2074774-380295*r)/(79*r-431)` where `r=ln(7)/ln(10/7)`. Its published 45-term rational logarithm bounds certify
`0<DL/EU<alpha<DU/EL<1`, with

```
DL=153966341169532252075
DU=153966341169532632370
EL=262921775619052595806
EU=262921775619052595885
```

Write `l=DL/EU` and `u=DU/EL`. The previously published `get_witnesses(n)` uses `floor(i*l)` as a candidate for `a_i=floor(i*alpha)`, with per-index strict rational checks. Find the **largest uniform initial index range** on which the *existing fixed-width enclosure alone* proves all floors and the first index where this interval cannot distinguish them.

## Theorem (sharp fixed-enclosure floor horizon)

For **every integer** `1<=i<=36,493,922`,
`floor(i*l)=floor(i*u)=floor(i*alpha)`.

At the **first index** `q=36,493,923`, the two rational bounds satisfy

```
floor(q*l)=21,370,750
floor(q*u)=21,370,751.
```

Consequently this specific fixed rational interval does **not** certify `floor(q*alpha)`; either of the adjacent integers is consistent with the interval. This is a statement about the first ambiguity of the *specified enclosure*, not the actual unknown floor at q or a mathematical failure of the S23/AV capacity theorem.

## Exact Farey certificate and proof

Define the two bounding reduced fractions

```
L=8,236,616 / 14,065,319
R=13,134,135 / 22,428,604 .
```

The exact integer identities and comparisons are

```
13,134,135*14,065,319 - 8,236,616*22,428,604 = 1,
L < l < (8,236,616+13,134,135)/(14,065,319+22,428,604) < u < R.
```

The middle mediant is `p/q=21,370,751/36,493,923`. The comparisons are performed by integer cross multiplication in `VERIFY_FAREY.py` with no floating point.

**Farey denominator lemma.** If `a/b<c/d` with `bc-ad=1`, any rational `m/n` strictly between them, written with positive integer denominator, satisfies `n>=b+d`. Indeed `bm-an` and `cn-dm` are positive integers, and

```
n=d*(bm-an)+b*(cn-dm)>=d+b.
```

Apply the lemma to `L,R`, where `b+d=q=36,493,923`. For `1<=i<q`, if `floor(i*l)<floor(i*u)`, there would be an integer `m` with `i*l<m<=i*u`; then `m/i` lies strictly between `L,R` and has a denominator `i<q`, contradiction. Thus `floor(i*l)=floor(i*u)`. Since `l<alpha<u`, the exact same integer is necessarily `floor(i*alpha)`.

At `i=q`, `l<p/q<u`, so `q*l<p<q*u`. The additional exact inequality `q*(u-l)<1`, together with the verified cross products, gives `floor(q*l)=p-1` and `floor(q*u)=p`. Their disagreement proves the *sharpness* of the uniform certification horizon from this fixed enclosure.

No large scan is used. The Farey denominator lemma is a universal exact proof for all 36,493,922 indices in the claim. The checker additionally verifies sample indices and all load-bearing cross products.

## Use and limits

This supplies a reusable uniform preflight for the previously published `get_witnesses(n)` alpha-floor step, covering all indices before 36,493,923 from one finite rational certificate. It does **not** replace the other critical-cell coverage predicates and does **not** establish `N(H_i)=M_i` beyond the separately checked finite endpoints. Beyond q, tighten the rational logarithm enclosure or use a certified per-index test before computing `a_i`; one should not infer an actual wrong result from the coarse interval alone.

BRC reuse: the exact integer residual `p-q*alpha` is retained as an unresolved bounded-sign observation at q. No joint-count observer, branch provenance or native X6 information is discarded by this arithmetic preflight. P000/worldview and the six-source/ten-label mapping obligation remain unchanged.

Sources: original interval and checker in `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py` (Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`); prior exact Sturmian skeleton `research_notes/brc_s23_av_plateaux201_220_20261108_research1/STURMIAN_SKELETON.md` at `696f253de86bf781dda922080a65f49076d2018b`. Scientific pin unchanged. Independent mathematical review and project admission pending.
