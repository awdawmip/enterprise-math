# S23/AV capacity plateaux 401–410 and global two-candidate staircase inversion

Date: 2026-11-09 (Asia/Shanghai). Status: **AUTHOR_SIDE_EXACT_FINITE_CERTIFICATE + PROVED_CANDIDATE_INDEX_LEMMA**; independent review pending. Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

## Model, definitions and result

In the frozen two-point iid S23/AV auxiliary experiment, one-step laws on labels (1,3,4) are `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)`. Preserve joint counts for labels 1,4 and allow neutral label-3 padding. The thresholds are `T_h={10^j/7^s: 0<=j<=s<=h}`; `N(h)` denotes the least common padded prefix length with an attainable likelihood score strictly in every threshold open cell including exterior cells.

Put

```
r=ln(7)/ln(10/7); epsilon=79*r-431; d=2074774-380295*r;
alpha=d/epsilon; a_i=floor(i*alpha); a_0=0;
V_i=380295*i+79*a_i; K_i=2074774*i+431*a_i;
H_i=V_i+510; M_i=K_i+V_i-V_(i-1)-1.
```

**Finite theorem (with inherited checker-soundness and global lower-bound lemmas):** for each integer `401<=i<=410` and every integer `V_(i-1)+511<=h<=V_i+510`, the exact capacity satisfies `N(h)=M_i`. The ten adjacent integer horizons cover **152136997 through 155940420**, or **3,803,424** values. At the last endpoint,

```
H_410 = 155940420, N(H_410) = 851141153.
```

## Finite certificate proof

1. The immutable all-index scaled-gap first-entry theorem, `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at `85b53d06d6ba775e516c566c1d79828b6ca9bb1f`, gives `N(V_(i-1)+511)>=M_i`.
2. The complete finite critical-cell reduction and all open cells/exteriors are justified in `research_notes/brc_s23_av_plateau20_20261108_r1/PLATEAUX20_200.md` (blob `e2fa7d4584cf4af475decc4b2bdffe9431a03192`). Its checker `VERIFY_PLATEAUX20_200.py`, blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`, was recovered byte-identically in a local execution environment before running. All decisions use integer arithmetic or strict `Fraction` logarithm intervals.
3. Complete `check(i)` returns were obtained for each of 401–410, with 798,271 feasible critical cells across the ten independent endpoint checks and at most 126 narrow displacement classes at an endpoint. The script returns only after checking every feasible cell, top 510 rows and both exterior cells, and returns `None` on an uncovered cell or mixed-sign blocker. Exact rows are preserved in `RUN_EVIDENCE.csv`.
4. Execution was segmented. One process completed 401 with `PASS_S23_AV_ANALYTIC_PLATEAU_401`; the 402–410 process emitted complete success rows for 402–409 before the process time limit, so **no combined pass from that interrupted process is claimed**; 410 was executed alone and emitted `PASS_SEGMENT_410_410`. The row-producing complete calls are sufficient for the ten finite certificates.
5. `VERIFY_AUDIT.py` independently recomputes `a_i,H_i,M_i` and adjacent endpoints from strict rational alpha brackets, and verifies exactly the predecessor endpoint 400 and the final endpoint 410; execution emitted `PASS_10_EXACT_FLOOR_ENDPOINT_CONTIGUITY`.
6. Hence `N(H_i)<=M_i` at each endpoint. Monotonicity of `N(h)` and the all-index lower bound in (1) yield equality on each entire interval. Intervals join since their first integer is the preceding `H_i+1`.

This is an author-side exact finite certificate conditional on the stated previously published checker-soundness and lower-bound theorems. It is not an independent review or native X6 six-source/ten-label transfer.

## New all-index exact lemma: only two endpoint candidates for random access

Let `Gamma=380295+79*alpha` with `0<alpha<1`. For all `i>=0`, setting `H_0=510`,

```
H_i = Gamma*i + 510 - 79*{i*alpha}.
```

For any integer horizon `h>=511`, set `k=ceil((h-510)/Gamma)`. Then the **unique** candidate-plateau index `I(h)=min{i>=1:H_i>=h}` is

```
I(h) = k       if H_k>=h,
       k+1     if H_k<h.
```

**Proof.** Since `k-1 < (h-510)/Gamma <= k`, one has `H_(k-1)<=Gamma*(k-1)+510<h`. Also `H_(k+1)>Gamma*(k+1)+431>=h+(Gamma-79)>h`, because `Gamma>380295>79`. The sequence `H_i` is strictly increasing (increments 380295 or 380374), so only `k` and `k+1` remain. The single exact comparison with `H_k` selects the true candidate index. QED.

This gives a constant number of alpha-floor evaluations in the candidate staircase, rather than scanning its indices. For a requested `h`, the initial `k` can be certified by strict rational enclosures `alpha_-<alpha<alpha_+`. Let `Gamma_-=380295+79*alpha_-`, `Gamma_+=380295+79*alpha_+`. If

```
ceil((h-510)/Gamma_+) == ceil((h-510)/Gamma_-),
```

their common integer equals `k`; otherwise refine the exact log enclosure. For indices `i<=411`, the published 26-digit enclosures already give identical `floor(i*Gamma_-)` and `floor(i*Gamma_+)`. This finite rational check proves their adequacy to select `k` for all integer `511<=h<=H_410`, without enumerating those horizons. For a certificate-dependent actual `N(h)` claim, use the finite `N(h)=M_i` equality already proved for that particular `i`.

`VERIFY_INVERSE.py` checks the rational bracket and 411 uniform gamma floors, checks 10,000 small integer horizons, plateau boundary tests through index 410, 2,000 seeded random horizons, and exhibits nontrivial instances requiring the second candidate. The all-index two-candidate lemma is algebraic; these tests check the implementation.

## BRC, scope and next direction

The relevant BRC interface retains joint label-1/label-4 provenance for the frozen likelihood-score observer; neutral label-3 padding is justified for this specified observer and future likelihood-cell operation. Native P000 X6 foundations and the lawful six-source/ten-label transfer remain unchanged.

Next: independently check index 411; test whether critical-cell witness coverage admits a uniform translated-witness invariant, including a first uncovered exact cell if a candidate fails. Apply the two-candidate inverse to a certified random-access capacity oracle only within the actual proven-capacity range; refine rational enclosures adaptively for arbitrary large horizons.