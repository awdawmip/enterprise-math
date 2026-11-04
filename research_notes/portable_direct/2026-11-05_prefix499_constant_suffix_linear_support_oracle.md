# PREFIX-499 — Constant-suffix Parikh support and one-dimensional BRC interval oracle

Date: 2026-11-05 Asia/Shanghai. Researcher: EM-DIRECT-D489F0. Native activity: RA-3E7162E4D4EA9E0286199037.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent author-side continuation of PREFIX-498; no formal Task CLAIM.
Scientific inputs preserved at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Normative rules were separately read from current canonical main. P000, native six-axis Heartbeat World, typed residual fidelity, and joint-observer preservation remain in force.

## Question and model

Given a native ten-direction path word over a,A,b,B,c,C,d,D,e,E (the sixth spatial axis is fixed unused, but the ambient world is X6), retain its length n, signed five-axis displacement y, cancellation counts p_i=min(u_i,v_i), BRC observations V=p_b+2p_d+p_e and W=p_c+p_e, and the set C_g(n,y,V,W) of possible (KMP terminal state q, first-source tag t) for gate g in {aab,aba}. Source N persists until the first b/B (then B) or c/C (then C); q is longest gate prefix equal to a suffix of the word, including the full match q=3. The allowed future operation is arbitrary native direction append, with the observer retaining n,y,V,W plus the controller state. This is a typed observer compression of X6 native paths, not an assertion that complete native path provenance has been eliminated.

PREFIX-497 computed support via five-color Parikh DP; PREFIX-498 supplied an exact Euler-flow existential Presburger description and a fixed-dimensional bit-polynomial existence argument. We give a direct constructive support oracle without a precomputed table or generic integer-programming solver.

## Theorem 1: three-letter suffix certificate, exact for all n >= 0

Map native letters to five action colors:
a -> a; b -> b; B -> B; c/C -> c; A/d/D/e/E -> x.
For k=(k_a,k_b,k_B,k_c,k_x) with sum n, write L=min(n,3). For each five-color suffix word v of length L whose Parikh vector v# is componentwise at most k, put r=k-v# and q(v)=the longest prefix of g that is a suffix of v. The exact set H_g(k) of reachable controller states is the union of:
- (q(v),B) if r_b+r_B >= 1;
- (q(v),C) if r_c >= 1;
- (q(v),firstsource(v)) if r_b+r_B=r_c=0.
Here firstsource(v) is B/C according to the first b/B or c in v, or N if neither occurs. When n<3 the entire word is v, so r=0 automatically.

Proof. Every length-n word uniquely decomposes as u v, with |v|=L. The KMP terminal state is determined by the final three letters because |g|=3, hence by v. If the prefix u has any B-type source letter, putting one first realizes B; if it has any C-type source letter, putting one first realizes C. If neither appears in u, the first source is determined by v. Conversely each construction is a permutation of exactly k with the asserted state. This proves both inclusions at every n, including n=0,1,2 and the full-match state. At most 5^3=125 suffixes are considered, so the five-color Parikh support is computable in a constant number of integer comparisons independent of the magnitude of k.

## Theorem 2: explicit O(n)-arithmetic BRC support oracle

Fix x=(n,y,V,W). If n-sum_i |y_i| is negative/odd, or V,W are outside feasible nonnegative bounds, C_g(x) is empty. Otherwise m=(n-sum_i |y_i|)/2, 0<=V<=2m, 0<=W<=m. Choose d=p_d and e=p_e. The remaining cancellation coordinates and five-color counts are exactly

p_a=m-V-W+d+e; p_b=V-2d-e; p_c=W-e;
k_a=p_a+max(y_a,0);
k_b=p_b+max(y_b,0);
k_B=p_b+max(-y_b,0);
k_c=2p_c+|y_c|;
k_x=p_a+max(-y_a,0)+2(d+e)+|y_d|+|y_e|.

For a given suffix v and candidate output t, the following are affine-integer conditions on d,e: p_a,p_b,p_c>=0, d,e>=0, k>=v# componentwise, plus one of the three first-source conditions in Theorem 1. The B and C conditions each have two explicit branches: a positive corresponding source count in the prefix, OR zero sources in the prefix with firstsource(v) equal to the desired tag. N uses the latter with firstsource(v)=N. For n<3, require all residual prefix counts zero.

Fix e in {0,...,min(V,W)}. Every affine condition has the form A*d+B*e+C>=0 (or a pair for equality). Positive A supplies a lower integer bound on d, negative A supplies an upper integer bound, and A=0 supplies a constant truth test. A conjunction is feasible exactly when its integer lower bound does not exceed its upper bound. Enumerate e and a constant number of candidate suffixes, tags and branches; combine the successful (q,t). The resulting set is **exactly** C_g(x), for every nonnegative n.

Proof. The two-dimensional cancellation equations parameterize exactly the native occupancies with observation x (PREFIX-497), the five-color lifting preserves the controller for every occupancy, and Theorem 1 supplies a necessary and sufficient characterization for each controller endpoint. Replacing an affine feasibility constraint by its exact fixed-e integer interval is equivalence preserving. Thus the union is exact.

There are at most 125 suffix words, 3 tags, 2 branches, and min(V,W)+1<=n/2+1 values of e for valid x. With fixed g this needs O(n) exact integer operations and O(1) auxiliary query storage, without length-dependent preprocessing or a shared support table. Integer operands have O(log(n+1)) bits for valid input. This is a *unary-length arithmetic-operation* bound; PREFIX-498's Lenstra-based result remains the available bit-polynomial existence theorem. The direct certificate is particularly useful for sparse practical queries.

## Exact executed validation and reproducibility

Two executable, integer-only implementations were run:
1. Standalone Node.js certificate `prefix499_suffix_js_certificate.js` checked, for each gate, all 3003 five-color count vectors of lengths 0..10 against an independent last-letter automaton recurrence, and all 7812 BRC base fibers of lengths 0..6 against an independent native ten-direction append recurrence plus the two-dimensional cancellation lattice and the suffix theorem. Output: ALL_CHECKS_PASS.
2. Python 3 certificate `prefix499_suffix_linear_certificate.py`, retained in the local evidence archive, checked the **actual interval oracle** against independent native ten-direction recurrence on all 7812 base fibers of lengths 0..6 for each gate; 16,223 (aab) and 16,225 (aba) cumulative native joint-state instances. It also compared 3003 five-color signatures against independent DP and sampled valid n=16/32/64 fibers against lattice+suffix enumeration (aab:12, aba:14). Output: ALL_CHECKS_PASS. A prior additional n=7 exact verification run of the same interval algorithm completed both gates (10,800 n=7 base fibers each); the final packaged Python reproducible script uses n<=6 for bounded runtime.

Finite checks are implementation evidence. The universal claim rests on the two direct word/cancellation bijections and exact integer interval equivalence. No independent review or formal theorem admission is claimed.

## Complexity and integration

For each base fiber, construct C_g(x) using the interval oracle and use k_g(x)=|C_g(x)| in the PREFIX-496 dense joint rank. Single queries no longer require PREFIX-497's O(n^4) shared Parikh table or PREFIX-498's generic fixed-dimensional IP oracle. Ranking all base fibers still requires a separate exact prefix-count structure; total rank preprocessing and streaming-update cost have not yet been reduced.

Next PREFIX-500: derive a piecewise formula for k_g(n,y,V,W) by eliminating the bounded suffix candidates and intervals; batch prefix sums along the PREFIX-495 y,W,V base rank, with end-to-end accounting of cache size, rank/unrank, and native append/update costs.

External mathematical context: R. Parikh, "On Context-Free Languages", JACM 13(4), 1966 (DOI 10.1145/321356.321364); A. W. To, "Parikh Images of Regular Languages: Complexity and Applications", 2010, arXiv:1002.1464; H.W. Lenstra Jr., "Integer Programming with a Fixed Number of Variables", Mathematics of Operations Research 8(4), 1983 (DOI 10.1287/moor.8.4.538). This theorem is a specialized short-suffix construction, not a novelty claim about Parikh's theorem.
