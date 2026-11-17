# EC49FRU — Four independent original-BRC named-observer prices: global phase theorem and staircase anchor lemma

**Date:** 2026-11-17. **Status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_TWO_RAW_RECONSTRUCTIONS / NOT_REVIEWED. **Scientific pin (unchanged):** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. **Direct predecessor:** EC49FRS–FRT, [PR #2648](https://github.com/awdawmip/enterprise-math/pull/2648), immutable commit 4f745adfb05c8dea4e4436cc24ecc4832870aeaf.

## Exact model

Retain BRC original class 16943, its 310 original configurations, all 141 distinct complete **named** response profiles and all 228 original named physical observations (144 terminal, 84 root). Do not collapse any observer, joint relation, response provenance or original index. Fix x=root/terminal base price=1, lambda=0 (uniform over 141 named profiles), and base observation price t>0. Only physical terminal observers q32,q34,q140,q142 are repriced to (1+a)t,(1+b)t,(1+c)t,(1+d)t, respectively, for arbitrary **real** a,b,c,d>=0.

For any legal complete adaptive identifying tree Q, U(Q) is the total original observation-use count over the 141 distinct named-state paths and n_j(Q) is the use count of the exact named observer qj along those paths. Then

$$
\frac{141 C_Q(a,b,c,d)}t=U(Q)+a n_{32}(Q)+b n_{34}(Q)+c n_{140}(Q)+d n_{142}(Q).
$$

## Theorem 1. Complete unrestricted four-dimensional phase diagram

For **all real** a,b,c,d>=0,

$$
\boxed{\frac{141 V(a,b,c,d)}t
=\min\{296+141a,\ 296+141b,\ 298+141c,\ 298+141d,\ 299\}.}
$$

All five branches are realized by complete original physical-query-labeled adaptive trees. Each is uniquely optimal on a nonempty open price chamber, so exactly **five distinct affine price-incidence types** are needed in a universal fixed-tree menu. The constant plateau can be realized with either original first query q46 or q93.

The six original complete named-state tree witnesses, reconstructed under the NEW exact mixed-price anchor, have these values (U; n32,n34,n140,n142; worst path depth):

| First original q | U | n32,n34,n140,n142 | Depth |
| --- | ---: | --- | ---: |
| 32 | 296 | 141,0,0,0 | 3 |
| 34 | 296 | 0,141,0,0 | 3 |
| 140 | 298 | 0,0,141,0 | 3 |
| 142 | 298 | 0,0,0,141 | 3 |
| 46 | 299 | 0,0,0,0 | 3 |
| 93 | 299 | 0,0,0,0 | 3 |

These are not hypothetical cost vectors: the verifier emits their full original physical-observer-labelled child maps and replays every tree on every one of the 141 named BRC response states. They all have exactly the displayed incidence counts.

## Theorem 2. Staircase-anchor lifting lemma (general finite observation systems)

Let F(y) be the unrestricted optimum of a finite collection of complete identifying strategies, each having an affine, coordinatewise nondecreasing cost in independently nonnegative price perturbations y=(y1,...,yk). Thus F is coordinatewise nondecreasing and concave. Fix baseline u, offsets 0<=b_i<=B, at least one b_i=0, and define z_i(m)=max(0,m-b_i), 0<=m<=B.

Assume the exact unrestricted anchor values satisfy F(z(m))=u+m for **every distinct breakpoint** m among 0,b1,...,bk,B. Assume also that every i has a legal complete witness tree of exact cost u+b_i+y_i for every y>=0, and a legal plateau tree of exact constant cost u+B.

Then for all real y>=0:

$$
\boxed{F(y)=u+\min\{B,b_1+y_1,\ldots,b_k+y_k\}.}
$$

**Proof.** Set m=min(B,min_i(b_i+y_i)). Each z_i(m) lies between 0 and y_i. Hence monotonicity gives F(y)>=F(z(m)). The staircase z(m) is affine on each closed interval between consecutive breakpoints. Concavity of F and the exact anchor equalities imply F(z(m))>=u+m on each such interval, including endpoints. Conversely the individual witness costs and plateau witness give F(y)<=min_i(u+b_i+y_i,u+B)=u+m. Equality follows. QED.

No finite price grid, interpolation heuristic or unproved global Pareto truncation is used in the real-continuum inference. It is a general reusable exact certificate principle with explicit assumptions.

## Application: exactly one new load-bearing native Bellman anchor

Put u=296, b=(0,0,2,2), B=3 and **integer price coordinates** y=(141a,141b,141c,141d). The required staircase is z(m)=(m,m,max(0,m-2),max(0,m-2)); its only distinct breakpoints are 0,2,3:

| m | y32,y34,y140,y142 | Exact Bellman total U-equivalent | Source |
| --: | --- | --: | --- |
| 0 | (0,0,0,0) | 296 | Inherited native base-cost certificate |
| 2 | (2,2,0,0) | 298 | Inherited original full-228 two-surcharge certificate, EC49FRR/FRS |
| **3** | **(3,3,1,1)** | **299** | **New EC49FRU all-228 exact Bellman certificate** |

At the new anchor, the independent raw-source reconstruction routes and integer dynamic programs both return the full-state sum **42159 = 141*299**. Each checks all 228 named observation vectors (with exact original root-key index bijection) and reaches 13,063 dynamic submasks. **All** optimal first original observations are precisely {32,34,46,93,140,142}.

For a non-singleton mask S of named states, each program uses the complete recurrence:

$$
B(S)=\min_{q:\#\Pi_q(S)\ge2}\left[p_q|S|+\sum_{T\in\Pi_q(S)}B(T)\right],\qquad B(\{s\})=0,
$$

with p_q=141+delta_q and delta_32=delta_34=3, delta_140=delta_142=1, all other delta zero. Positive observation prices make uninformative queries strictly dispensable. There are no floating-point coefficients in the Bellman calculation.

The six explicit native trees attain all five affine witnesses. Lemma 2 and the inherited m=0 and m=2 anchors therefore prove Theorem 1 across the entire real nonnegative four-dimensional orthant.

## Theorem 3. Exact complete set of optimal FIRST original physical observations

Define five expressions L32=296+141a, L34=296+141b, L140=298+141c, L142=298+141d, Lflat=299, and Lmin=min of all five.

The complete optimal first-action set is exactly:
- q32 iff L32=Lmin;
- q34 iff L34=Lmin;
- q140 iff L140=Lmin;
- q142 iff L142=Lmin;
- q46 **and** q93 iff Lflat=Lmin.

**Proof of necessity.** With m and z(m) as in Lemma 2, any tree Q optimal at y is also optimal at z(m), because monotonicity of its own affine cost and equality F(y)=F(z(m))=u+m imply every additional price-incidence contribution vanishes. At 0<=m<2, EC49FRS's original Bellman first actions are {32,34}; at m=2 they are {32,34,140,142}. At 2<m<3, any optimal tree must be optimal at both endpoint anchors m=2 and m=3: its endpoint Bellman gaps are nonnegative and its cost is affine along the segment, so a zero interior gap forces both to vanish. Therefore its first action lies in the intersection, {32,34,140,142}. At m=3, the NEW complete first-action certificate is {32,34,46,93,140,142}. The first query occurs along all 141 named-state paths, so any q with a surcharge increased strictly beyond its staircase value is excluded. This yields exactly the five branch-equality conditions above. **Sufficiency** follows from the replayed six exact witness trees. QED.

**Minimality of five.** The five affine branches have distinct four-coordinate gradients and each strictly wins on some open region of the nonnegative orthant. A fixed tree that is optimal throughout a nonempty open chamber has an affine cost identically matching that chamber's affine branch, hence its gradient must equal that branch. Therefore at least five different affine incidence types are necessary. The five exhibited witness trees attain the bound.

## Evidence, limits and continuation

- Pinned frozen original master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
- Pinned frozen original profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.
- New executable verifier: EC49FRU_EXACT_FOUR_PRICE_BELLMAN_VERIFY.py, in the code/ directory of the preceding self-contained evidence archive with the exact original source/ files.
- New full evidence JSON: EC49FRU_FOUR_DIMENSIONAL_NATIVE_BRC_ANCHOR_CERTIFICATE.json, including all six complete decision trees, 141-state replay incidences, two source-response reconstructions and DP subset totals.
- The inherited two-price theorem is an author-proved, exactly finite-checked source dependency, pending independent mathematical admission. This paper is also **NOT_REVIEWED**. These statements hold within the frozen BRC observation/price model, not as general physical calibration claims.

**Next:** (i) overlapping priced observer groups / exact staircase failure boundaries; (ii) nonuniform original configuration weights or x!=1, with exact changed-phase tests; (iii) strictly positive prices under negative surcharges (-1<a,b,c,d<0). Preserve original 228 named observers, the frozen source pin and P000.

**Control provenance:** historical author EM-DIRECT-8454C6 / RA-ED136F89271FD89288F3E58D. Exact Source lookup at 2026-11-17T14:29:15.985546Z returned RS-EC49AS: NO_CANONICAL_PUBLICATION_DIRECTORY; it did not evaluate active operational owner and grants no formal Task execution. This is independent portable research, not a new authenticated CLAIM, Result, Review, Activity checkpoint or canonical-main merge.
