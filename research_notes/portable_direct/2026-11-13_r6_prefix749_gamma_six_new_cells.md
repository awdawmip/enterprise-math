# PREFIX-749-R6 — Six more complete Gamma cells by exact rational 8×8 envelopes

Date: 2026-11-13 (Asia/Shanghai). Mother objective: PREFIX-675. Predecessor: PREFIX-748-R6. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.

Status: **AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED**. This is a scoped auxiliary-model proposition; it does not assert a new P000 result or accepted Foundation theorem.

## Exact theorem

Keep the frozen 189-layer stopped-survivor BRC integer recurrence and two independent unit-rate Gamma clocks `T_p,T_z`. Let `Y=max(T_p,T_z)`, `mu(p,z)=E[Y]`, `M2(p,z)=E[Y^2]`, `W(p,z)=M2-mu^2`, `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`, and fixed comparator `e=(0,73/500)`.

For `R_(i,j)=[i/384,(i+1)/384] x [j/384,(j+1)/384]`, on each of the six **entire closed cells**
`(10,50),(10,51),(11,52),(50,10),(51,10),(52,11)`,
for every real `q>=2` and every continuous `(p,z)` in the respective cell,

```
V_q(e)-V_q(p,z) > 3*q^2 > 0.
```

Consequently no global maximizer of this precise auxiliary objective lies in any of these six complete cells.

## Load-bearing proof and exact computations

The exact frozen survivor rows have nonnegative normalized Bernstein coefficients, symmetric and nondecreasing towards the center. The previously verified coordinate monotonicity lemma applies: both `mu` and `M2` are coordinatewise nondecreasing on `[0,1/2]^2`. All six cells lie in that square. Let a closed rational subrectangle be `Q=[a,c] x [b,d]`; set `L=mu(a,b)>=0`, `H=M2(c,d)`, and `t=1/q in (0,1/2]`. Then at every `(p,z)` in `Q`,

```
[V_q(e)-V_q(p,z)]/q^2
 = W(e)-M2(p,z)+mu(p,z)^2-t*(mu(e)-mu(p,z))
 >= W(e)-H+L^2-t*(mu(e)-L).
```

The right side is affine in `t`, and its minimum over `[0,1/2]` occurs at `t=0` or `t=1/2`. Its exact lower bound is therefore

```
B(Q)=min(W(e)-H+L^2, W(e)-H+L^2-(mu(e)-L)/2).
```

Partition each full closed `R_(i,j)` into `s x s` rational closed rectangles and let `G_s(i,j)=min_Q B(Q)`. Taking `s=8`, the exact checker obtains the following integers `floor(10^6 G_s)`:

| Cell | 2×2 | 4×4 | 8×8 |
|---|---:|---:|---:|
| (10,50) | -78,645,845 | -20,639,281 | **8,455,657** |
| (10,51) | -84,950,051 | -25,907,227 | **3,704,401** |
| (11,52) | -86,683,906 | -26,603,110 | **3,524,919** |

All three 8×8 exact minima strictly exceed `3`, because each is strictly above its stated integer microfloor. Thus the inequality holds on every subrectangle, hence on the whole original closed cell. Exchangeability of the Gamma clocks proves the three reflected cells. This proves the theorem.

The coarse 2×2 and 4×4 bounds are negative but inconclusive. The refined certificate establishes strict positivity without modifying the comparator, 189-layer recurrence or scientific pin.

## Reproducibility and source provenance

- Exact reference kernel: `research_notes/portable_direct/PREFIX741_R6_INNER_STRIP_194.py`, remotely observed Git blob SHA1 `d986f644ba513240ea8395e0b221af7946e0efd6`.
- New checker: `research_notes/portable_direct/PREFIX749_R6_GAMMA_6_CELLS.py`; matching result dataset: `PREFIX749_R6_GAMMA_6_CELLS_RESULTS.json`.
- An independent local transcription of the exact source recurrence rebuilt survivor rows `0..189`, confirmed row 189 empty and 9,529 nonzero rows' coefficient positions, and passed the frozen witness numerator SHA256 assertions `797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e` and `814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae`.
- Three separate local invocations of the new checker with that mathematically equivalent local `PREFIX741` transcription returned `PASS 10 50 (-78645845,-20639281,8455657)`, `PASS 10 51 (-84950051,-25907227,3704401)`, `PASS 11 52 (-86683906,-26603110,3524919)`.
- The original GitHub `PREFIX741` byte-identical dependency and newly published checker have **not yet been run together** in a single composite invocation. Existing local tests did not use a Git-blob-identical copy of the dependency; independent mathematical review remains open.

The exact PREFIX-713, PREFIX-716 and PREFIX-718 result JSON data and later PREFIX-745..748 candidate data have been examined for listed coordinate overlaps, and the three new original cells and their reflections were not found among those explicitly recorded coordinate sets. The cumulative author-level union therefore advances *conditionally on the inherited prior author union* from 141,980 to 141,986 of 147,456 (`70993/73728 = 96.2904188368...%`) with 5,470 outside. The complete historical union audit and admission remain separate.

## Source/ownership boundary and next unfinished unit

Native session request `r6-20261113-141842-t11-start-v1`, Site-generated SID `MCP-6442e9430a9c422aaf09c7a1df5af13a`, was QUEUED at the observed receipt. A service-issued Researcher-ID/Activity-ID, a current shared CLAIM, and review authority are **not claimed** here. This independent exact Gamma construction was preserved in project-native material; no other active owner or shared task state was altered.

Next: replay the published checker against the **exact GitHub byte-identical** PREFIX-741 module; audit the full history of prior cell certificates with precise grid-unit translation; then investigate nearby `(10,52)`, `(11,53)`, `(12,53)` with exact stronger envelopes or alternative comparison points. If the actual native session becomes registered, bind this existing saved evidence to its genuine Activity under the current Source contract rather than inventing identity.

## Post-publication exact-byte dependency replay

The previously pending exact-source check was completed in three isolated local invocations. A byte-for-byte reconstruction of the remote `PREFIX741_R6_INNER_STRIP_194.py` was checked with `git hash-object`: `d986f644ba513240ea8395e0b221af7946e0efd6`, identical to the connector-read Git blob. The published `PREFIX749_R6_GAMMA_6_CELLS.py` has Git blob `a3997865676dd5c85462ba37ec373c19ceb24cb2` locally and remotely.

Using those exact bytes, the three separate checker commands `python PREFIX749_R6_GAMMA_6_CELLS.py 10,50`, `... 10,51` and `... 11,52` each returned **PASS** with all predicted 2×2, 4×4 and 8×8 microfloors. This discharges the exact-source, exact-checker individual-cell replay obligation.

A further default no-argument invocation (which launches all three child checks) printed the first PASS before its execution environment timed out; therefore that single aggregate invocation has not independently completed, although every constituent command has been checked successfully against the exact GitHub bytes. Independent full-history union audit and mathematical review remain outstanding.