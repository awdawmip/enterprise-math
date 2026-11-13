# Stage282-B — Exact causal-prefix simplex and non-IID two-fiber BRC counterexample

Status: PORTABLE_AUTHOR_PROOF / FINITE_EXACT_REPLAY / UNREVIEWED / NOT_ADMITTED. Researcher-side external ordered-history finite BRC mathematics, not native X6 dynamics or a claim about physical reality.

Source pin: GLOBAL_KNOWLEDGE_V1 main@7165476d23554f44cde0da96a8724449801d1bf7; Enterprise Math canonical main@64f29780c682ae896aff65d617e314c85ece6b96. P000 original Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc; ACTIVE worldview and portable research protocol read, unmodified. Scientific parent: Stage281-B at research PR #1571, commit dd7da1c80b70536b9acb2939d965eb51d650e597, with Stage282-B packet in the same commit.

## Theorem 1: exact serial two-coin convexification

Consider a finite ordered-history decision tree and finitely many source laws with source-dependent fixed, possibly non-IID transition kernels. A source-blind first coin x in [0,1] chooses whether to continue; a second source-blind coin y is encountered on any path at most once and only after the first coin continued. Coins are constant across their own depth-homogeneous fibers; no path sees the same gate twice. Let F_i be any fixed [0,1]-valued terminal observer of complete ordered path, actions and ports under source i.

Every terminal path mass equals a constant times one of (1-x), x, x(1-y) or xy (including exogenous path weights). Consequently for each source there exist fixed c_i,d_i,e_i such that

    E_i^{rho(x,y)} F_i = c_i + d_i*x + e_i*x*y.

With z=xy, the exact feasible image is Delta={(x,z): 0<=z<=x<=1}. Conversely any point of Delta is implemented by y=z/x for x>0 and arbitrary y when x=z=0.

For an original full-history policy pi, global minimax observer compression thus equals the *exact* linear program

    min t
    0<=z<=x<=1, t>=0,
    -t <= E_i^pi F_i - c_i - d_i*x - e_i*z <= t for each i.

For rational laws, original policies and rewards the LP has rational coefficients and a rational optimizer/certificate: restrict t<=1 (the observers are [0,1]-valued), obtain a compact rational polytope, and choose an optimal rational vertex. This theorem does NOT cover overlapping/revisited gates or arbitrary state quotients.

More generally in a strictly serial m-coin continue chain let u_0=1, u_j=product_{k=1}^j x_k. The exact domain is 1=u_0>=u_1>=...>=u_m>=0. Stopping at stage j has factor u_{j-1}-u_j, continuing through all m has factor u_m, so every fixed terminal expectation is affine in the u_j. Reconstruction is x_j=u_j/u_{j-1} whenever u_{j-1}>0; after zero prefix mass later coins are irrelevant. This is a sufficient positive-mass serial-gating BRC rule, not a general graph theorem.

## Non-IID, strictly positive depth-3 ordered model

Sources P and Q generate potential observations H1,H2,H3 in {0,1}. Under P, Pr(H1=0)=3/4, under Q it is 1/4. Under both sources Pr(H2=0|H1)=1/2. The conditional Pr(H3=0|H1H2) values are:

| source | 00 | 01 | 10 | 11 |
|---|---:|---:|---:|---:|
| P | 1/4 | 1/2 | 1/2 | 3/4 |
| Q | 3/4 | 1/2 | 1/2 | 1/4 |

All eight complete ordered words have strictly positive rational mass under each source; this is not an IID process. The first decision fiber C1={0,1} chooses stop (A1=0) or continue (A1=1) to H2. If H2=1 stop. If H2=0, second fiber C2={00,10} chooses stop (A2=0) or continue (A2=1) to H3 and stop.

Original complete-history policy pi chooses A1=1 only if H1=0, and A2=1 only for history 00; the action at unreachable 10 is nevertheless specified to be 0. Source-indexed [0,1] terminal observers are:

- F_P=1 iff history 00 reaches C2 and A2=1.
- F_Q=1 iff either (H1=0 and A1=0), or (history 10 reaches C2 and A2=1). Those events are disjoint.

Under pi, E_P F_P=3/8 and E_Q F_Q=0. Under the compressed source/history-blind coins (x,y), direct ordered-tree enumeration gives

    E_P^{rho} F_P = 3xy/8,
    E_Q^{rho} F_Q = (1-x)/4 + 3xy/8.

Write z=xy and the two nonnegative source observer distortions

    A=3(1-z)/8;  B=(1-x)/4 + 3z/8.

## Theorem 2: exact global certificate and local failures

Over all legal x,y in [0,1], the exact minimax distortion is 3/16, achieved uniquely at x=1,y=1/2. Indeed,

    R(x,y)=max(A,B) >= (A+B)/2
           =3/16 + (1-x)/8 >=3/16.

At (1,1/2), A=B=3/16. Equality requires x=1 (from the last inequality), and then z=1/2 (from A=B), hence y=1/2: global optimality and uniqueness follow for the entire *continuous* coin square, not just a grid.

Compare two precisely defined, source-faithful but locally optimized schemes.

**Stage279-type local action mass:** minimize local source action-mass error at each fiber using pi's ORIGINAL reaching masses. At C1 the original P/Q action1 masses are 3/4 and 1/4 (both total mass 1), giving x_A=1/2. At C2 only 00 is reached (P mass 3/8, Q mass 1/8) with original A2=1; thus y_A=1. The resulting true global observer risk R(1/2,1)=5/16, exceeding the global optimum by 1/8.

**Stage281-style frozen-occupancy downstream-first observer procedure:** fix the ORIGINAL first-stage pi occupancy and optimize the downstream observer coin y. On reachable original C2 paths only 00 is present and P's observer requires A2=1, so the downstream local minimizer is y=1. With y frozen, optimize x using the FULL actual two-source observer expressions. This gives

    R(x,1)=max(3(1-x)/8, 1/4+x/8).

The lines cross at x=1/4, achieving constrained risk 9/32, still 3/32 above global 3/16. This is a strict counterexample to the precisely defined two-pass procedure; it is NOT a claim that all observer-aware algorithms, Stage281's one-fiber theorem, or full dynamic programming are invalid.

The causal reason is the mixed mass z=xy: the globally optimal first-stage x=1 makes source-Q history 10 newly reachable, which was invisible under original-pi downstream occupancy. At this new reachability the y=1 local choice is too costly; the optimal pair is (1,1/2). Full branch identity, source, action, temporal order and port provenance were retained until the declared observer was evaluated.

## Verification and limits

REPRO_STAGE282B.py is an executed standard-library Fraction verifier using independent full ordered terminal-leaf enumeration including H3 under each source. It checks source terminal mass 1, exact original expectations, 17x17=289 source-by-source rational compressed-policy comparisons to the derived symbolic formula and the rational lower-bound inequality, all three exact policies, gaps and causal-simplex coefficients. Observed stdout in REPRO_STAGE282B_EXECUTED_STDOUT.txt ends STAGE282B_CAUSAL_SIMPLEX_EXACT_PASS. The universal two-coin and chain statements rely on the algebraic proofs above; finite grid checks do not prove them. No independent replication, Lean proof or native result/review acceptance is claimed.

Actual BRC reuse: source-indexed positive rational ordered histories and terminal-port action masses; composition of stagewise reachability; quotient by prefix masses ONLY for declared serial-gated observers. Other future observations may depend on omitted ordered residuals.

The native P000 Heartbeat-world X6 bridge is NOT supplied: before transfer require a fully specified time-stamped six-coordinate Cell and registered lossless six-nonnegative-field address codec, a selected three-dimensional slice with explicitly defined third component, ordered axis-step and port identities, the declared future operation/observer scope, and a proof native transitions preserve the required source and prefix masses. Never call this external binary decision tree a native 2D plane. P000 and ACTIVE records remain locked.

## Native role/owner boundary and next question

The dedicated Site reports research_authority_granted=false; em_session_start rejected STATIC_READONLY_SCOPE_DENIED (operation_sent=false), and the active-owner list returned CONTROL_QUOTA. No authorized CLAIM, Source Result, formal activity binding or Driver admission was obtained. This PR content is only a portable unreviewed author-side proof, not a substitute for the native writer.

Stage283-B: break serial gating by revisiting a coin or introducing overlapping routes; prove by a concrete positive-rational DAG that lifting only (x,z=xy) loses exactness, determine a new minimal provenance/port coordinate and give a strict relaxation-gap certificate. Stage278-A's N=12 Bellman next-face question remains independently open.
