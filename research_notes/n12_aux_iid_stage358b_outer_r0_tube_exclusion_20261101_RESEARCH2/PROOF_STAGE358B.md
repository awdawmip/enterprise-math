# Stage358-B — Exact Pareto exclusion of an open off-boundary residual tube

Date: 2026-11-01 (Asia/Shanghai). Status: **PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Contributor: Research2 portable-author continuation; it is neither a native CLAIM/Source Result nor an independent review.

## A. Precise model and theorem

Let `w=(1,3,3,1)`, `m=(61,21,9,9)`, `B_k(z)=z^k(1-z)^(3-k)`, for `k=0,1,2,3`. For real `x,y in [0,1]`, define

```
r_k(x,y) = (4 B_k(x)+B_k(y))/5 - m_k/160
b(x,y)   = (5/32) sum_{k=0}^3 w_k |r_k(x,y)|
D_3(a,z) = (1/2) sum_{k=0}^3 w_k |B_k(a)-B_k(z)|
c(x,y)   = (63 D_3(1/4,x) + D_3(3/4,x)
            + 9 D_3(1/4,y) + 7 D_3(3/4,y))/256.
```

The weights encode all 16 source-labeled subset outcomes (four distinct count classes with their original multiplicities), while the four terms in `c` retain four provenance-distinct audit channels. In particular, `r_0=(4(1-x)^3+(1-y)^3)/5 -61/160`.

**Theorem (two-dimensional nonzero-residual tube exclusion).** For every real `(x,y)∈[0,1]^2` satisfying

```
(x <= 229/1000 or x >= 233/1000)
abs(r_0(x,y)) <= 1/20000
b(x,y) <= 299/50000,
```

there exists a rational `(u,v)∈[0,1]^2` such that

```
b(u,v) < b(x,y)   AND   c(u,v) < c(x,y).
```

Hence no such source point can participate in a globally cost-minimal additive two-source solution with an upper error budget, at any budget for which the additive model and pointwise replacement remain valid. This proves dominance on a **nonzero-width two-dimensional region**, not just Stage357-B's one-dimensional `r_0=0` curve. It does not classify the whole off-boundary feasible domain or prove post-cusp global optimality.

## B. Interval certificate: proof over all real parameters

Write `X=[L,H]` for one closed rational `x` cell and `t=1-y`. The residual tube is exactly

```
-1/20000 <= (4(1-x)^3+t^3)/5-61/160 <= 1/20000.
```

Consequently, for every point in this cell satisfying the tube,

```
61/32 - 4(1-L)^3 - 5/20000 <= t^3
 t^3 <= 61/32 - 4(1-H)^3 + 5/20000.
```

If the resulting upper bound is `<0` or its lower bound is `>1`, there is no tube point above `X`. Otherwise intersect the cube interval with `[0,1]` and enclose both cube roots outward on the rational lattice `(1/10^10) Z` using *exact integer bisection*; the resulting rational rectangle `X × Y` contains all real tube points above `X`. Closed-endpoint treatment is conservative and covers dyadic partition interfaces.

For every interval `I=[a,b]`, standard rational interval operations include the exact-value set; `|z|>=max(0,a,-b)` for all `z∈I`. Apply them to `B_k`, all four `r_k`, all original-label multiplicities and four audit distances. Obtain rational lower bounds `b_lo(X)<=b(x,y)` and `c_lo(X)<=c(x,y)` for every such tube point. Each leaf is certified by one of:

* `NO_TUBE`: the derived cube interval lies strictly outside `[0,1]`.
* `B_EXCLUDED`: `b_lo(X)>299/50000`.
* `DOMINATED`: one recorded rational witness `Q` has `b(Q)<b_lo(X)` and `c(Q)<c_lo(X)`.

These are **strict inequalities checked as exact `Fraction` objects**, not decimal rounding or random sampling. The rational witnesses are selected from the 31 distinct explicit witness coordinates in Stage357-B's 71-leaf certificate. The checker independently verifies the Stage357-B input partition and rational comparisons against the exact same model before reusing those witness coordinates. A witness need not lie on a residual-zero curve; its role is a genuine original-space two-objective competitor.

The adaptive exact dyadic refinement terminates with **109 leaves**: 6 `NO_TUBE`, 23 `B_EXCLUDED` and 80 `DOMINATED`, depth at most 15. The cells have pairwise disjoint interiors, cover the closed outer domains, and their widths sum exactly to `996/1000`. The newly generated `CERTIFICATE_STAGE358B_R0_TUBE.csv` contains every endpoint, class, chosen rational witness, both interval lower bounds, and depth. Recomputing every inequality yields the same decision; the CSV is a convenient public audit trace, not an axiom.

The executed checker certifies uniform strict margins over the relevant leaf classes:

```
min_DOMINATED(b_lo-b(Q)) > 3/10000000
min_DOMINATED(c_lo-c(Q)) > 2/1000000
min_B_EXCLUDED(b_lo-299/50000) > 6/1000000.
```

These coarse printed bounds are strictly weaker than the exact minima reported by the executable, and are themselves checked by comparing those exact minima to these rational constants. (The actual minima are about 3.0629e-7, 2.9435e-6 and 6.3700e-6, respectively.) The first inequality is nontrivial: `3/10000000 = 3e-7`.

**Optimization consequence:** If a feasible two-source configuration contains a point in the excluded region, replacing that source by its rational witness strictly decreases the sum of b-values and the sum of c-values, so the original configuration is not cost minimizing. This is independent of the unreviewed Stage346 global-error minimum and Stage356 central-slab arguments. The source cost has the constant term `33/1024`, which cancels in this replacement comparison.

## C. Reproduction and provenance

Run in the research branch checkout:

```
python research_notes/n12_aux_iid_stage357b_outer_r0_pareto_exclusion_20261101_RESEARCH2/REPRO_STAGE357B.py
python research_notes/n12_aux_iid_stage358b_outer_r0_tube_exclusion_20261101_RESEARCH2/REPRO_STAGE358B.py
```

The Stage358 program also generates the parent CSV itself from its published Stage357 checker if the parent CSV is missing. Two actual runs of Stage358's checker produced identical stdout; resulting deterministic CSV has 109 rows plus header, 22,914 bytes and SHA256 `e37ec2aecea24717d646f191f8ff71315a6a1fca513c503dc108829bd73fa021`. It is regenerable from the branch's checked-in exact scripts; all mathematical inequalities are computed without floating point. The output is stored as `REPRO_STAGE358B_EXECUTED_STDOUT.txt` and the CSV as `CERTIFICATE_STAGE358B_R0_TUBE.csv` in the local artifact set. The program's dependency is specifically the Stage357-B author proof/code at PR #1736 commit `5e0dac3d0d8acc60d1302bddfa92b0f6a16ce407` (not a canonically admitted result).

Frozen global authority: `awdawmip/chatgpt-global-knowledge` `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, including `00_BOOTSTRAP`, `OPERATING_MANUAL`, P000 V4 (original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, startup projection matches), ACTIVE world, math/BRC/code rules, task role packet. Frozen EM control reference: `awdawmip/enterprise-math main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419` and its current portable-research operations. Parent author frontier PR #1736@`5e0dac3d0d8acc60d1302bddfa92b0f6a16ce407`.

Native authority: `em_context_manifest` reports `authority_granted=false`, and the current bounded owner query `em_control_tasks` returned `CONTROL_QUOTA`. Consequently current formal owner and CLAIM cannot be verified and no Source Result, Driver admission or promoted theorem is asserted. This is an **author-side exact rational certificate**; independent audit is pending.

BRC reuse is *typed observer/provenance reuse*: distinguish 16 labeled binomial outcomes and four audit channels, retain exact positive-rational lower bounds and strict Pareto witnesses. This auxiliary Bernoulli observer is not a native Heartbeat/BRC–Shor physical computation. There is not yet a typed transfer to P000 native X6, the third coordinate in a native three-dimensional slice, triadic closure, independent time, or Cell-address codec. No native residual attribution is inferred.

## D. Next discriminating mathematical unit

**Stage359-B**: for the remaining central band `229/1000 < x < 233/1000`, classify feasible points with `r0 != 0`, while protecting `q*` and the right `r1=0` candidate curve from unjustified dominance claims. Use exact sign-chamber gradient cones or rational interval certificates to (i) produce explicit strict dominators in candidate off-curve cells, or (ii) isolate rational Pareto witnesses outside the current arc. A second independent direction is extending the present outer tube beyond `1/20000` by searching additional rational witness configurations; failure at one thickness is a local certificate limit, not a global nonexistence result. Verify Stage356 independently before combining its central theorem with this tube.
