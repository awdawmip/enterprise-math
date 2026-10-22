# One-Point Repair and Exact Enumeration for a Four-Coordinate Boolean Sumset
PREFIX-187 · Complete author-side research note · 22 Oct 2026 · Unreviewed.

## Abstract and scope
Let X_j(n) be degree-n nonnegative integer four-vectors with support cardinality j. Given any E⊂X_2(n) with |E|=n−4, set B_E=X_1(n)∪(X_2(n)\E)∪X_4(n). We prove symbolically that for all n≥8, a **single** added q∈X_3(n) suffices to cover every target in X_4(2n). The n=7 exception needing two repair points is sharp. We also count for every n≥8 all E causing exactly 0,1,2,3 missed targets. This concerns an auxiliary, existence-only, 4-coordinate Boolean-BRC model; it does not claim a faithful embedding into native P000 X6 Cells, paths, joint branches, memory or dynamical observations.

## Producer lemma and the prior result
Write m=n−5≥3 and N=n−2=m+3. The author-side PREFIX-186 analytic lemma states that the missing-target set H_E=X_4(2n)\(B_E+B_E) is exactly {y∈M_n:P(y)⊆E}, where M_n has exactly one coordinate equal to 1 and three coordinates in [3,N], and P(y)={r∈X_2(n):y−r∈X_4(n)}.
For y∈M_n with its 1 at index k, write y_i=N−d_i for the other three indices, with d_i≥0 and Σd_i=m. On the support edge {i,j}, if ℓ is the omitted high index, the producers are exactly r_i=t, r_j=n−t and 3+d_j≤t≤m+2−d_i. This integer interval contains d_ℓ points. Thus |P(y)|=m. Two missing targets must satisfy |P(y)∩P(z)|≥m−1 since both P sets lie in E of size m+1.

## Theorem 1: a constructive, all-parameter repair
For all n≥8, all E with |E|=n−4 admit q∈X_3(n) such that X_4(2n)⊆(B_E∪{q})+(B_E∪{q}). The minimum number of new X_3 points is 0 precisely when H_E is empty, otherwise 1.

Proof. First assume every missing y has its unique 1 at the same index k. Producers on distinct edges are disjoint, giving
m−1≤|P(y)∩P(z)|≤Σ min(d_i(y),d_i(z))=m−(1/2)Σ|d_i(y)−d_i(z)|.
Consequently each deficit coordinate differs by at most one from that in any fixed reference missing target. Therefore Σ_i max_y d_i(y)≤m+3. The capacities u_i=min_y(y_i−1)=m+2−max_y d_i(y) are at least 2 and sum to at least 2m+3≥n=m+5. Choose positive integers q_i≤u_i (i≠k) adding to n, with q_k=0. Then q is support three, and for every missing y the residual y−q is support four of degree n, hence belongs to B_E.

Now suppose missing targets have at least two different 1-coordinates a,b, and let c,d be the remaining indices. The P of such two targets can intersect only along support edge {c,d}, and in at least m−1 points. A third different small-coordinate type would force at least 2(m−1) elements of one size-m P on two disjoint edges, contradicting m≥3. Hence all missing targets have their 1 at a or b.

Producer counts along edge {c,d} imply that every target is among
A0=(1,3,N,N), Ac=(1,4,N−1,N), Ad=(1,4,N,N−1),
B0=(3,1,N,N), Bc=(4,1,N−1,N), Bd=(4,1,N,N−1),
with coordinate order (a,b,c,d). P of A0 and B0 occupies all m elements of the interval [3,m+2] on {c,d}; a subscript c removes the upper endpoint, a subscript d removes the lower endpoint. Each subscripted target has exactly one additional producer outside this shared edge. Any c-type and d-type intersect in just m−2 producers; they therefore cannot both be missing. If any subscripted target occurs, all such targets have the same subscript s∈{c,d}, and all missing y satisfy y_t=N at the other high index t.

Define q=e_a+e_b+N e_t. It is degree n and has support three. For an A-type missing y, the residual y−q lies on {b,s} with nonzero values (2,N) or (3,N−1); for a B-type, it lies on {a,s}. Choose any missing A and B. Their P sets jointly contain exactly m+1 points, so their union equals E. Outside {c,d}, that union only contains producers on {a,t} or {b,t}; none of the foregoing residuals belongs to E. All residuals therefore lie in X_2(n)\E⊂B_E, establishing the repair.

If no subscripted target occurs, H_E={A0,B0}. E then contains the entire m-point shared edge and only one additional deletion. Both choices t=c and t=d yield a support-three candidate q as above. The two pairs of residuals occupy four distinct support edges {a,c},{a,d},{b,c},{b,d}; the sole extra deleted point can damage at most one candidate. The other succeeds. QED.

The n=7 example E={(3,0,0,4),(0,3,0,4),(0,0,3,4)} was proved in PREFIX-186 to require exactly two added X_3(7) points. Thus n≥8 is optimal.

## Theorem 2: exact zero/one/two/three-deficit census
Let N_j count E with |E|=n−4 and exactly j missing targets. Set m=n−5≥3 and I=2(m+2)(m+1)(5m+24). Then
N3=24; N2=42m+108; N1=I−84m−288;
N0=C(6(m+4),m+1)−I+42m+156; and Nj=0 for j≥4.
The number of deletion sets needing one repair point is I−42m−156.

Proof. |M_n|=4C(m+2,2)=2(m+2)(m+1), and each P(y) of size m lies in precisely |X_2(n)|−m=5m+24 deletion sets, so N1+2N2+3N3=I.

To count pairs of simultaneously missing targets, note that for a common 1-coordinate, their deficit triples must differ by a unit transfer. The interval endpoints show that a union of size m+1 occurs precisely when the unchanged third deficit is zero; otherwise the shifted interval causes a second replacement, and the union has size at least m+2. The permitted adjacency graph is the perimeter cycle of the triangular lattice d_1+d_2+d_3=m. There are 3m adjacent pairs for each of four positions of the unique 1, hence 12m pairs.
For different 1-coordinates there are 6 unordered pairs of indices; each has exactly one target pair A0,B0 with equal P of size m, and six additional target pairs with |P∪P'|=m+1 (full/endpoint-trimmed or same-endpoint trimmed). Hence the total count of missed-target pairs over all E is
N2+3N3=12m+36+6(5m+24)=42m+180.
Three missing targets cannot have three different unique-1 coordinates by the disjoint-edge bound in Theorem 1. Nor can three share the same 1-coordinate: the eligible perimeter graph is a cycle of length 3m≥9, without a triangle. A three-target deletion set with exactly two 1-coordinate types necessarily contains A0,B0 and one of four near neighbours. Thus N3=6×4=24. Solve the two incidence equations and subtract from total C(6(m+4),m+1) to obtain all formulas. QED.

## Verification, limits, next experiment
A Python exact-integer constructive checker generates every potentially failing E=P(y)∪{e}, builds an explicit q according to these two proof cases, and checks y−q in the surviving X2 or X4. It confirms the formulas and zero failures for n=8 through 20 inclusive and n=24. For n≥9 this is a proof-backed complete **candidate** scan, not brute force over every astronomically many E. Recompiled and reran the independently written prior C++17 direct-sumset solver for all 7,140 deletion configurations at n=7 and 111,930 at n=8. At n=8 the exact histogram is N0=110652,N1=1020,N2=234,N3=24, with zero one-point failures; at n=7 four sets need two points. These computations do not replace the above all-n analytic proof.

No native Researcher/Owner/CLAIM was obtained: session registration returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false, and dispatch returned CONTROL_QUOTA. Mathematical status is author-side proof and finite checking, NOT Driver reviewed or P000 accepted. Next investigate deletion |E|=n−3 and an independent observer-faithful X6 bridge.
Source: GLOBAL_KNOWLEDGE_V1 main@ec44261d822dea70b6ad6dc6c99b15ed5479d9d1; Enterprise Math main@63f87045b456cf573a9eaa7bbc8d4a4673a3e6ea.
