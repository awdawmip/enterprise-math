# R713: Exact BRC source-query complexity for triad-to-pair shadow

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen scientific inputs: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Prior author work R711/R712, PR #2057. Mathematical evidence level: two general combinatorial proofs, complete six-axis Boolean census and independent integer inclusion-exclusion. Native X6 Cell/Link/Port + V29/V39 applicability remains to be tested.

## Typed BRC carrier and observer

Fix a finite labeled vertex set V. Source coordinates are the distinct triples T=choose(V,3), with a Boolean licensed-state H subset of T. The pair-shadow G=partial_2(H) records all unordered pairs contained in at least one licensed triple. The observer G is given exactly before a query phase; an addressed direct query Ask(t) returns whether one specific t is in H. The algorithm may adaptively select queries and must reconstruct every H in F(G)={H: partial_2(H)=G}. An arbitrary parity/rank/aggregate query is not a free direct read under this interface.

Let T(G) be the graph triangles of G and d_G(e) the number of such triangles containing edge e. A graph G is a feasible shadow iff d_G(e)>=1 for each edge. Define Forced(G) as the triangles t containing an edge e with d_G(e)=1, and Optional(G)=T(G) minus Forced(G).

## Theorem R713.1: exact worst-case addressed query complexity

For every finite feasible G, the minimum worst-case number of direct yes/no triad-membership queries needed to recover H, even with deterministic adaptive queries, equals

    Q_direct(G)=|Optional(G)| 
       = #{t in T(G): d_G(e)>=2 for all three edges e in t}.

Proof. All legal H contain only triangles of G. Every triangle in Forced(G) is present in every H: it is the sole possible cover of some edge of G. Hence query each optional triangle, infer all forced triangles present and all nontriangles absent; this reconstructs H.

Conversely the legal H_full=T(G) responds 1 to every addressed query. Suppose an exact decision tree halts on that branch without querying an optional t. The distinct state H_minus=T(G) minus {t} has the same pair shadow: each edge of t is still covered by some other graph triangle, while other edges retain their coverage. Every query on the branch receives the same answer in these two states. This contradicts exact reconstruction. Thus every optional coordinate must be queried on the all-ones branch. QED.

This is an exact source-address query bound. If only pair-shadow questions can occur, the shadow alone answers the declared output.

## Theorem R713.2: second largest shadow fiber, arbitrary n>=5

Let f(G)=|F(G)|. Among all proper pair-shadows G other than K_n, maximum f(G) is achieved exactly by the graphs K_n with one edge removed.

Proof. Given proper G choose any absent edge e and set K=K_n minus e. Then G is a subgraph of K. Let A=T(K) minus T(G), and map H in F(G) to H union A. This has shadow K: H covers G, while each new edge in K not in G is covered by a triangle of K necessarily in A. Intersection with T(G) recovers H, so the map is injective.

For strictness if G is a proper subgraph of K, some triangle t of K contains an edge of K missing G, hence t in A. Each edge of K is contained in at least n-3>=2 graph triangles, so T(K) minus {t} still has shadow K. It cannot belong to the image, all of whose members contain t. Thus f(G)<f(K) unless G=K. All K_n minus e are isomorphic. QED.

This general theorem extends R712's largest-fiber uniqueness to the next-ranked shadow, without changing its exact previously computed six-axis counts.

## Exact six-axis outcomes

Each of the 2^20=1,048,576 labeled triadic Boolean H states is assigned a 15-bit exact pair shadow. There are 6,115 feasible graphs. The inclusion-exclusion formula over required pair edges, independently evaluated for K6 (2^15 subsets) and K6 minus one edge (2^14 subsets), agrees with direct enumeration.

| Shadow | Fiber f(G) | Minimal arbitrary fixed-length auxiliary code | Minimal direct addressed queries |
| --- | ---: | ---: | ---: |
| K6 | 477965 | 19 bits | 20 |
| K6 minus one edge (15 labeled cases) | 21450 | 15 bits | 16 |
| K5 plus one isolated vertex | 125 | 7 bits | 10 |

Histogram of direct query cost Q: 0:2713, 1:480, 2:180, 4:1515, 7:780, 8:60, 10:266, 12:45, 13:60, 16:15, 20:1.
Histogram of excess Q-ceil(log2 f): 0:3373, 1:2137, 2:585, 3:20.

The check tests the removal witness for every optional/forced triangle on every feasible G. Executed standard-library Python verdict:

    R713_BRC_TRIAD_QUERY_EXACT_PASS 6115 477965 21450 20 16

Accompanying executable code and JSON contain complete verification and histogram evidence.

## Scientific bridge and next research unit

Theorem domain is a conditional candidate triad-licensing Boolean carrier. P000 fixes six X6 axes, primitive balance arity three and typed TRIADIC_CLOSURE_E, and does not assert that all these hypergraph H can arise at a native Cell/time/port state. The source/address interface distinguishes exact information content from allowed physical observer operations. Positive BRC support is not a signed force cancellation model.

Next: using the frozen X6 Cell/Link/Port, V29 PASS/TRANSFER and V39 loop-flow j rules, construct one *admissible common state* with actual source gate vector H; classify its Forced(G)/Optional(G), inspect a real native update for triad-identity reads, check conservation and S6 axis-renaming covariance. Apply this query bound only to the verified admissible family. Reuse classification: COMPOSE_APPLIED (R711/R712). This author-side result awaits any independent Driver mathematical review.
