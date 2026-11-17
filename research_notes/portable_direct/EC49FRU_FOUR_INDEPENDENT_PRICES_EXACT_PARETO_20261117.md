# EC49FRU — Exact four-independent-price BRC Pareto theorem

Date: 2026-11-17. Original frozen BRC scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Scientific predecessor: PR #2648 at 4f745adfb05c8dea4e4436cc24ecc4832870aeaf. Frozen class 16943: 310 original configurations, 141 full named states and 228 physical queries (144 terminal + 84 root). The native response maps, provenance, labels and full decision-tree legality are unchanged.

**Claim scope.** Let the terminal/root baseline query cost be t>0, root-to-terminal ratio x=1, and use the uniform prior on all 141 complete named states (lambda=0). Give the four original physical queries 32,34,140,142 independent additional nonnegative real costs at,bt,ct,dt. All other 224 queries cost t. For any legal complete adaptive native identification tree Q, let U(Q) be the sum of all query uses over the 141 original named state paths, and n_j(Q) the corresponding uses of original physical query j. Its expected cost is

\[
C_Q(a,b,c,d)/t=\frac{U(Q)+a n_{32}(Q)+b n_{34}(Q)+c n_{140}(Q)+d n_{142}(Q)}{141}.
\]

## Theorem 1 — all-real, unrestricted global Bellman value

For **every** real a,b,c,d >= 0, taking the infimum over **all** admissible complete native adaptive decision trees using all 228 original physical observations,

\[
\boxed{\frac{V(a,b,c,d)}{t}=
\min\left\{\frac{296}{141}+a,\frac{296}{141}+b,
\frac{298}{141}+c,\frac{298}{141}+d,\frac{299}{141}\right\}.}
\]

Five fully re-played legal original trees attain these five affine pieces respectively. The native first physical queries may be chosen as 32,34,140,142,46. Their exact (U;n32,n34,n140,n142) incidence vectors are

| Native first query | Total uses U | Selected-query incidence |
|---|---:|---|
| 32 | 296 | (141,0,0,0) |
| 34 | 296 | (0,141,0,0) |
| 140 | 298 | (0,0,141,0) |
| 142 | 298 | (0,0,0,141) |
| 46 | 299 | (0,0,0,0) |

Original query 93 is another full native witness for the last row. Every witness identifies all 141 states, has worst-case depth 3, and its path-cost vector is checked exactly. Complete tree JSON is preserved in the independently downloadable self-contained evidence package.

## Proof: three exact anchors suffice

First set the surcharges of queries 32 and 34 equal to u, and those of 140 and 142 equal to v. Define W(u,v)=V(u,u,v,v). Its value is an infimum of cost expressions affine in (u,v) with nonnegative slopes, so W is jointly concave and separately nondecreasing.

Two independent reconstructions of the frozen original 94-family response data, followed by full integer Bellman enumeration retaining all 228 physical queries, give exactly

\[
W(0,0)=296/141,\quad
W(2/141,0)=298/141,\quad
W(3/141,1/141)=299/141.
\]

The integer DP objectives with every unit t represented by cost 141 are, in order, 41736, 42018 and 42159. Each run visits 13,063 subproblem masks; the full tied native first-query sets are respectively {32,34}, {32,34,140,142}, {32,34,46,93,140,142}. The independent native-index DP agrees exactly at all three anchors.

The explicit native trees rooted at 32,140,46 yield the global upper bound

\[
W(u,v)\le g(u,v):=\min\{296/141+u,\ 298/141+v,\ 299/141\}.
\]

We now establish the reverse inequality over the entire unbounded real quadrant.

**A region.** If 0<=u<=2/141, concavity on the segment from (0,0) to (2/141,0) implies W(u,0)>=296/141+u. Monotonicity in v extends this to v>=0. For 2/141<=u<=3/141, concavity from (2/141,0) to (3/141,1/141) implies W(u,u-2/141)>=296/141+u. Monotonicity in v extends it to v>=u-2/141. Together these cover exactly the chamber where the first piece of g is active (including ties).

**B region.** For 0<=v<=1/141, the same second segment gives W(2/141+v,v)>=298/141+v. Monotonicity in u extends the lower bound to every u>=2/141+v. This is the chamber where the second piece is active.

**Plateau.** For u>=3/141 and v>=1/141, monotonicity from the third exact anchor gives W(u,v)>=299/141, the third piece.

These chambers cover every nonnegative (u,v). Therefore W=g identically for all real u,v>=0, with no inference from a finite sampling grid.

For independent (a,b,c,d) set u=min(a,b),v=min(c,d). Since every query-use incidence is nonnegative, monotonicity of the unrestricted value gives V(a,b,c,d)>=W(u,v). Choose the cheaper of the two one-query-incidence witnesses rooted at 32/34, choose the cheaper of 140/142, or use the q46 avoiding witness. One of these has cost exactly g(u,v)=W(u,v), giving the reverse inequality and the stated four-real-variable formula. QED.

## Theorem 2 — minimal five-tree universal fixed menu

The five exhibited incidence types form a fixed deterministic policy menu attaining V at every real nonnegative (a,b,c,d). Five is optimal: each of the five affine pieces has a nonempty *strict* optimality chamber in the positive orthant. Their slopes are respectively e1,e2,e3,e4 and 0, all distinct. A fixed legal tree has one affine cost gradient, and cannot coincide with two distinct affine functions on two nonempty open sets. Thus no menu of four or fewer fixed complete deterministic trees is universally sufficient. There may be additional tied optimal trees on transition boundaries; this theorem concerns the minimal universal menu size, not exhaustive boundary-tree enumeration.

## Reproducible evidence

Frozen raw master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Original profile CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

The two original native response constructors agree after exact typed root-key reindexing for all 228 original physical observations, with 141 named states and total original multiplicity 310. Two distinct Bellman implementations reproduce the three load-bearing rational anchors and all optimal first native queries. Twelve rational four-price regression cases (including those three anchors and five strict-menu chambers) each traverse 13,063 reachable Bellman subset states. Exact full native witness trees rooted at 32,34,140,142,46,93 were extracted and re-played through all 141 states, with checked incidence vectors, path costs and maximum depth. These are finite model certificates; the monotone-concave argument proves the all-real conclusion.

**Status:** AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CHECKED / NOT_REVIEWED. GitHub publication is portable research evidence, not a formal Task Result, independent Review or P000 modification.

**Next mathematical problem:** independently price an additional original query such as 46, search for the first genuinely new affine incidence vertex, and determine finite-anchor certificates for larger native observer-price portfolios without discarding joint response or provenance.
