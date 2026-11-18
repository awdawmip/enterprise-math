# PREFIX-896 — 容量强制碰撞定理及19位模数域的精确去重覆盖
Date: 2026-11-18 (Asia/Shanghai). Lane: 进取数论研究6. Researcher: EM-DIRECT-E370C2; existing SID: MCP-4b417026c0f54b45970c6f223e1833f6. Scientific input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (unchanged).
Predecessors: PREFIX-887, PREFIX-894, PREFIX-895 (not rederived). Status: AUTHOR_PROVED / TWO_EXACT_INDEPENDENT_IMPLEMENTATIONS / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. This is independent BRC observer science, not a shared RS-X6 CLAIM.

## 1. Exact typed population and observation
For p=32, put N=2^32, T=N(p+1)=141733920768 and Q={262145,262147,...,524287}, |Q|=131072. Every directed, named trajectory is precisely one of Z_x=(x,x) or F^i_x=(x,x xor 2^i), 0<=x<N, 0<=i<32. Its observation under two positive odd moduli q1,q2 is Phi_(q1,q2)(u,v)=(u mod q1,v mod q2). All start states, end states, named source indices, directions and transition types remain distinct. The 33N trajectories are distinct as typed objects.

## 2. Theorem 896-A: unconditional capacity collision and multiplicity bound
For any p>=1 and any positive moduli q1,q2, let n=2^p(p+1), m=q1*q2, t=floor(n/m), r=n-t*m. For the full named zero/one-flip population, the number C_p(q1,q2) of unordered pairs of distinct legal trajectories with equal observation satisfies
C_p(q1,q2) >= (m-r)*t*(t-1)/2 + r*t*(t+1)/2.
In particular, q1*q2<2^p(p+1) forces C_p(q1,q2)>=1.

Proof. Each trajectory has a unique source label (Z,x) or (F,i,x), giving exactly n distinct objects. The pair of residues has at most m possible values. For fiber occupancies c_1,...,c_m >=0 with sum n, the collision count is sum_j c_j(c_j-1)/2. Exchanging one unit from occupancy a to b when a>=b+2 strictly reduces the sum; hence a minimum has all occupancies t or t+1, with exactly r of the latter. The displayed bound follows. If n>m then some fiber has >=2 trajectories. This is about the specified finite observer, not an X6 native-coordinate collapse.

## 3. Theorem 896-B: exact strict-19-bit capacity census
Define P={(q1,q2) in Q^2: q1*q2<T}. For any q in Q its number of eligible second ports is
h(q) = max(0, 1+floor((min(524287,floor((T-1)/q))-262145)/2)).
Thus |P|=sum_{q in Q} h(q)=7,364,142,398.
For every q1<=270335 in Q (4096 first-port values), the capacity criterion excludes every q2 in Q. The symmetric column statement follows from the same inequality.

## 4. Theorem 896-C: exactly deduplicated combination with PREFIX-895
Let S be the 16 certified first-port rows from PREFIX-894, A32 the 24 axis moduli from PREFIX-887, and R the two disjoint 256-row strips of PREFIX-895. Put U=S union A32 union R, |U|=552; their exact members and construction are preserved from PREFIX-895. Every pair touching U in either port has a previously certified source collision. The row/column set H=(U x Q) union (Q x U) has |H|=2*552*131072-552^2=144,398,784. Direct exact integer capacity counting gives
sum_{u in U}h(u)=18,312,436, #(P intersect U^2)=11,996.
Consequently #(P intersect H)=2*18,312,436-11,996=36,612,876, #(H without P)=107,785,908, and #(P union H)=7,471,928,306.

PREFIX-894/895 also provides the zero/zero criterion Z={(q1,q2):lcm(q1,q2)<N}, with explicit distinct Z_0,Z_lcm witnesses. To count Z outside P, write q1=g*a, q2=g*b, with g=gcd(q1,q2), a,b odd and gcd(a,b)=1. The inequalities defining Z without P become
262145<=g*a,g*b<=524287; g^2*a*b>=T; g*a*b<N.
Since g=(q1*q2)/lcm(q1,q2) > (q1*q2)/N >=33 and g is odd, necessarily g>=35. Thus the following gcd decomposition is exact and nonoverlapping:
g odd in [35,524287]; a,b odd in [ceil(262145/g),floor(524287/g)], gcd(a,b)=1, g^2ab>=T, gab<N.
An exact ordered-pair census gives |Z without P|=95,365,328. Of these, 1,050,532 have at least one port in U and 94,314,796 have both ports outside U. Therefore the three pairwise disjoint sets P, H\P, Z\(P union H) establish
**|P union H union Z|=7,364,142,398 + 107,785,908 + 94,314,796 = 7,566,243,102**
distinct ordered modulus pairs with certified collisions, leaving 9,613,626,082 not excluded by THIS three-family union out of |Q|^2=17,179,869,184. Relative to PREFIX-895's exact 351,837,696-pair union, this is an additional 7,214,405,406 pairs after explicit deduplication. Earlier unrelated exclusion families have not been globally merged.

## 5. Reproduction and independent checks
- `PREFIX896_R6_CAPACITY_UNION_CENSUS.cpp`: C++17 integer enumeration of capacity, the inherited U row/column coverage, and Z outside P using unique gcd decomposition. The implementation enumerates 117,714,631 restricted (g,a,b) candidate triples and verifies asserted counts. Build: `g++ -O3 -std=c++17 PREFIX896_R6_CAPACITY_UNION_CENSUS.cpp -o p896 && ./p896`.
- `PREFIX896_R6_INDEPENDENT_MOBIUS_CHECK.py`: independent Python exact calculation of coprimality through squarefree-divisor Möbius inclusion/exclusion over each admissible b-interval. It confirms 95,365,328 Z pairs outside capacity and 94,314,796 outside both capacity and U without iterating the same gcd(a,b) pair list. It also explicitly hashes all legal trajectories for 1,287 small p=2..7 capacity-positive modulus inputs; each has a duplicate observed pair.
- `PREFIX896_R6_CAPACITY_UNION_RESULTS.json`: numeric scope, counts and first implementation output. Both programs ran locally with assertions satisfied. All operands are exact integers; there is no floating-point or probabilistic inference.
- Dependencies, not recreated: `2026-11-18_r6_prefix895_two_midstrip_complete_collision_census.md`, `PREFIX895_R6_TWO_STRIP_CERTIFICATE.json`, and PREFIX-894 original ZZ certificate.

## 6. Open frontier
Among the 9,613,626,082 pairs not covered by this particular union, first prioritize q1*q2>=33N, gcd(q1,q2)<35 (or lcm>=N), with both ports outside U. Test existing PREFIX-891 endpoint criterion and PREFIX-895 FF carry search on selected new uniform bands; seek a structural theorem or actual injective witness. The broader fixed odd-observer question B_fix,odd(32) in {19,20} remains open. P000, native six-axis space and separately typed time are retained as project premises; the typed two-port model is an auxiliary representation only.
