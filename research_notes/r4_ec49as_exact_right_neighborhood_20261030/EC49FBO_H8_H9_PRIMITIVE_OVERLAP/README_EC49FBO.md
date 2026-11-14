# EC49FBO — H8/H9 sharp primitive-prefix overlap

Date: 2026-11-05. Native signed six-axis X6 / complete positive BRC key / frozen 9-state DFA. Previous source: EC49FBN at immutable `320835bed5a70e312dc19f38efd82dab6fe3aac2`; task scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The 5-key H2–H9 mother problem and original rank clauses are unchanged.

## Theorem (sharp, for each eligible complete H9 cache key)
Let `M=(X,Y,Z,0,0,0)`, `X+Y=10, Z>=1, X>=2Z+1, Y>=1`. Let `A8(M)` denote all *observer-accepted* complete H8 words with M, and `FG9(M)` all complete H9 words of F/G signature 16/32 with M. Expand operations into the exact native signed-axis primitive steps, and let `lcp(u,v)` count common initial primitive steps. Then:
```
  Lambda(M) = max_{u in A8(M), v in FG9(M)} lcp(u,v)
            = 15+2Z    for Z=1,2,3
            = 1        for Z=4 (uniquely M=(9,1,4)).
```
All these H8 and H9 terminal paths have native primitive length `ell(M)=18+2Z`.

## Proof

The frozen key equations require the operation counts:
```
             a     e      f        g       c+d
  H8         Z-1   Z    X-2Z-1    Y-1       1
  H9         Z-1   Z    X-2Z      Y         0
```
The original signed primitive operation codes are:
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.
They are prefix-free. An H9 F/G observer word starts f/g and contains only a,e,f,g. The unique c/d in an H8 word must therefore be where its primitive prefix stops matching a given H9 F/G path, after at most **one** native primitive step inside that c/d. At most seven H8 operations can precede that step, comprising at most Z copies of the four-step e; all other preceding operations have two steps. Hence `lcp<=2*7+2Z+1=15+2Z=ell-3`.

For Z<=3 the seven non-c/d H8 operations include `(X-2Z-1)+(Y-1)=8-2Z>=2` copies of f/g. Put all seven into a word q beginning with f or g; q contains all Z copies of e. Then the H8 word `q c` is observer-accepted and the H9 word `q f g` is observer F or G. Their initial native prefix consists of all `14+2Z` steps in q, plus the common first native step of c/f: equality holds.

For Z=4, eligibility forces (9,1,4). Every H8 word has f=g=0 and therefore begins a,e,c or d, while every H9 F/G word begins f or g. The first primitive code step can agree only for c/f or d/g, with immediate divergence at the next primitive step. Choosing an H8 accepted word beginning with c and an H9 F word beginning with f gives exactly one matching step. Therefore the bound is attained also at Z=4.

## Executed exact verification

`VERIFY_EC49FBO.js` generates **every** complete H8 ordered word (separating c and d), filters by the frozen DFA, inserts each native signed-primitive path into a prefix trie, then compares it to every complete H9 F/G word. The output `EXACT_REPORT_EC49FBO.json` contains all 16 eligible keys, each H8/H9 population, and exact common-prefix histogram. The exact population/maxima also agree with a separately implemented Python standard-library ordered-word enumerator.

| Z | Eligible keys | Sharp longest overlap | Primitive path length |
|---:|---:|---:|---:|
|1|7|17|20|
|2|5|19|22|
|3|3|21|24|
|4|1|1|26|

For the key M=(7,3,2), a sharp witness can be obtained with `q=gaeeffg`, H8 `gaeeffgc`, H9 `gaeeffgfg`. Native length=22 and shared native steps=19. This lemma targets **interior primitive sharing**, which complements the EC49FBN complete-terminal inheritance theorem.

## Research use and next test

Use `Lambda(M)` as a sharp pairwise primitive-overlap bound in the H8/H9 joint edge-union optimizer. Next EC49FBP: calculate the minimum *union* edge cost for the four compulsory H8 signatures 1,2,4,8 plus the two compulsory H9 F/G signatures 16,32, for each of the 16 eligible keys. Feed the resulting exact two-window costs into the 27+28 rank-feasible complete H2–H9 schedules and seek a complete <=93-edge construction or a broader certified lower bound.

Evidence state: author-side analytic proof / exhaustive exact finite enumeration / portable draft / independent Driver acceptance pending; role/claim/Result remain governed by current native Source authority.
