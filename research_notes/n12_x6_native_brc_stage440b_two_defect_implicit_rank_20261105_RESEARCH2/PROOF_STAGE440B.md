# Stage440-B — exact implicit class ranking for two moving one-defect X6 sources

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF, exact finite computation, UNREVIEWED, NOT_ADMITTED.
Parent: Stage439-B (commit 7f9456031a9fdfdf12836116f178a17bf50be965), Draft PR #1736.
Frozen scientific sources: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488.
Current behavioral rules read independently. Model: original signed X6 (12 directions), static ordered words, exact positive-unit match observer. These statements concern this finite-operation observer and no physical evolution or signed cancellation.

## The precise complete fiber

Let A=+E1 and B=-E1, regarded as two of all twelve native signed X6 steps.
For integer L>=a+4 and 1<=b<=a, define P_x=A^(x-1) B A^(L-x), Q_y=A^(y-1) B A^(L-y), x,y in {2,...,L-1}.
Fix the present complete observation O: lengths both L, endpoints (L-2)E1 for each word; directed J for each source has one A->B edge, one B->A edge and L-3 A->A edges; K=L-2.
Exactly all pairs x!=y constitute the full O fiber: J and endpoints restrict each path to exactly the one-internal-B form, and with equal lengths K=L iff the defects coincide, L-2 otherwise. Thus |F|=(L-2)(L-3).
Future operations: P may POP at most a times and APPEND at most once; Q may POP at most b times and APPEND at most once; operations can be arbitrarily interleaved, and APPEND uses any of the twelve signed X6 directions. Every legal operation prefix is observed, including length, both six-component endpoints, full directed J and K.

## Theorem 440.1 — exact classes and populations

Set s=max(b,a-1), d=a-s (therefore d is 0 or 1), h=L-a-2>=2.
Define categorical defect coordinates
  i=0 if x<L-a, otherwise i=x-(L-a)+1, so i in {0,...,a};
  j=0 if y<L-s, otherwise j=y-(L-s)+1, so j in {0,...,s}.
The set of possible categorical pairs consists of all (i,j) except i>d, j=i-d.
Two histories in F have the same complete observed future for every labelled budget-respecting operation word if and only if their categorical pairs agree.

Consequently the class count is
  q_F=(d+1)(s+1)+s^2.
For b=a, this is a^2+a+1. For 1<=b<a, it is a^2+1.
The class population M(i,j) (original ordered history pairs) is
  M(0,0)=h(h+d-1);
  M(0,j)=h for j>=1;
  M(i,0)=h+d-[i<=d] for i>=1;
  M(i,j)=1 for i,j>=1 and the pair is allowed.
Each mass is a positive integer and the sum is (L-2)(L-3). In particular the exact future-sufficient category label requires ceil(log2(q_F)) fixed bits on this known O fiber.

### Proof

The own-source POP suffix in Stage439 Theorem 439.1 exposes x>=L-a and y>=L-b. Because P can POP from length L to any of L-a,...,L-1 and then APPEND one arbitrary direction, the crossed observer K identifies Q's original letter separately at any one index in [L-a+1,L]. Hence y>=L-a+1 is also visible. Symmetrically Q's APPEND reveals P's original directions in [L-b+1,L], already contained in P's POP-exposed x range as b<=a. The remaining Stage439 mutable original-overlap match bits refer to positions [L-a+1,L], already determined by these visible defect coordinates, since current K=L-2 forces x!=y. The repair key therefore factors exactly through (i,j). Conversely the individually exposed positions distinguish each nonzero i or j; zero signifies the remaining invisible interval. Stage439's sufficiency and necessity for all legal future traces establishes the exact classification under its stated premises. This theorem is an author-side consequence of the earlier author-side Stage439 theorem, not an independently admitted result.

Count: the P hidden interval {2,...,L-a-1} has h sites. Q's hidden interval {2,...,L-s-1} has h+d sites; it contains the P hidden interval and possibly one more site (d=1). Both defect sites must differ. This gives M(0,0)=h(h+d-1). A visible Q site lies outside the P hidden interval, yielding h choices for P. For a visible P site, Q hidden offers h+d choices, minus one if i<=d (the P site also lies in the Q hidden interval). When both sites are visible there is one original pair, except their common-site diagonal i>d,j=i-d. All masses and q follow by elementary sums; the total equals |F|.

## Theorem 440.2 — codebook-free exact rank and reconstruction

Order admissible category pairs lexicographically by i then j; omit the forbidden diagonal. The rows i=0,...,d have s+1 entries; rows i=d+1,...,a each have s entries.
For a pair (i,j), let
  base=i(s+1) if i<=d; otherwise base=(d+1)(s+1)+(i-d-1)s;
  local=j if i<=d; otherwise local=j-[j>i-d].
Then rank=base+local in {0,...,q_F-1}. Inverse: ranks below B0=(d+1)(s+1) use i=floor(rank/(s+1)), j=rank mod (s+1). Above B0 use i=d+1+floor((rank-B0)/s), t=(rank-B0) mod s, j=t+[t>=i-d]. This is a bijection; it uses constant-many integer arithmetic operations and NO explicit class table.

For recovering a particular original history choose a within-class index z in {0,...,M(i,j)-1}. For (0,0), write z=x0*(h+d-1)+t, then y0=t+[t>=x0], and x=2+x0,y=2+y0. For (0,j>0) use x=2+z, y=L-s+j-1. For (i>0,0), x=L-a+i-1, select y as the z-th position in Q's hidden interval skipping x only if i<=d. For (i,j>0), use the two fixed visible positions. This gives a bijection between (rank,z) and F, with exact integer class populations.

Computing the present O and class label from raw words takes O(L) primitive operations/characters; the formulas for q, M, rank and unrank use O(1) arithmetic operations on O(log L)-bit integers (not O(1) bit cost). Reconstituting full ordered paths takes Theta(L) output steps, and separate within-class index information is necessary to recover the exact original history. The class index itself plus initial O and operation budget is sufficient for the specified future observer by the Stage439 repair construction; an initial representative can be built in O(L) time. No class table with q entries is required. For this one-defect family the computation is polynomial and explicit; this does not assert a comparable bound for arbitrary many defects, arbitrary J, or signed amplitude BRC.

## Reproduction and limits

Run `node REPRO_STAGE440B.js` and compare its single JSON line with `REPRO_STAGE440B_EXECUTED.json`. Direct combinatorial count, rank, inverse and within-class reconstruction are exhaustively checked on all 1<=b<=a<=L-4, 6<=L<=16. Four specified smaller fibers additionally compare every complete observation at every legal POP/APPEND prefix, with all 12 native future APPEND labels. Within each claimed class, every member is checked against a representative; between distinct classes, every pair of representatives yields a distinguishing future trace. Equivalence is transitive, so these comparisons establish the predicted partition of each tested fiber. Arbitrary L/a/b results rely on the written proof; no formal checker or independent Driver has admitted them.

## Next

Stage441-B: extend to unequal initial lengths or two defects in each source, retaining exact directed J and K. Test a transfer-matrix state with crossed exposure, defect exclusion and class population; derive implicit rank/unrank or provide a strict missing-state witness. Explicitly account for class indexing and original-history recovery costs.
