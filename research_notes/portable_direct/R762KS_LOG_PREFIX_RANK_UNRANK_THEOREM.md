# R762KS — Exact logarithmic lexicographic selection for M3 provenance fibers

Date: 2026-11-24 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_PYTHON_CHECKED / NOT_REVIEWED.

## Scientific inheritance and scope

Continues **R762KR** at immutable commit \`4ac774f52110c91bdb1db9b968319704e0ef475b\`, with earlier R762KN@2ca3fe1f and frozen scientific input \`a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`. The mathematical object is the same unsigned auxiliary composite Port–Euler M3 model: inactive Ports 01,23,45; 12 active Port parity bits; 8 supports s∈{0,1}^3; a positive integer multiplicity m_s at each support; and a typed, **unordered** source triple (x_s,y_s,z_s) of edge counts AB, AC, BC with x_s+y_s+z_s=m_s.

The existing 5-state suffix dynamic program D_i(r,q) of R762KR and its conditional fiber cardinality Q_m(b)=D_0(b,EMPTY) are reused unchanged. This note improves the lexicographic *selection* of those source triples, which R762KR carried out by scanning O(m_s²) local triples. The observer retains multiplicities, exact 12-bit forced boundary b∈F and quotient connectivity; the code's output is the exact tuple of 8 auxiliary source triples. It makes no statement about native signed time-ordered BRC updates.

## Theorem KS.1 — Closed prefix sums on local parity/support classes

At a fixed support s and multiplicity m, partition all triples (x,y,z) into disjoint classes C=(U,p), where U⊆{x,y,z} is the set of strictly positive coordinates and p gives the parity of each positive coordinate. For a∈U put ℓ_a=1 if p_a=1 and ℓ_a=2 if p_a=0; for a∉U put ℓ_a=0 and fix its count to zero. Let h=|U| and T=(m−Σ_a ℓ_a)/2. A class is feasible precisely when T is a nonnegative integer. Writing each positive coordinate as ℓ_a+2t_a turns the class into a nonnegative h-part composition of T.

Define H(T,h)=binom(T+h−1,h−1) for h≥1,T≥0, with H(0,0)=1 and H(T,h)=0 for T<0 or h=0,T≠0.

For integer threshold X, let N_C^x(X) count triples in C satisfying x<X.

* If x∉U, N_C^x(X)=1_{X>0} H(T,h).
* If x∈U, set k_x=max(0,ceil((X−ℓ_x)/2)). Then

\[
\boxed{N_C^x(X)=H(T,h)-H(T-k_x,h).}
\]

For a *fixed* x=x_0, the residual class exists if x∉U and x_0=0, or x∈U and t_x=(x_0−ℓ_x)/2 is a nonnegative integer not exceeding T. In the latter case replace (T,h) with (T−t_x,h−1), deleting x. For integer Y, the number N_C^{xy}(x_0,Y) of triples with this fixed x and y<Y is then given by the same two formulas on the remaining y coordinate.

**Proof.** A parity/support class has exactly H(T,h) compositions. For x∈U, the inequality x≥X is equivalent to t_x≥k_x. Shifting t_x by k_x leaves H(T−k_x,h) compositions; subtraction yields the first formula. For x∉U, x is identically zero. Fixing x removes precisely one composition variable when x∈U, which proves the second formula. The h=0 convention covers a singleton nonzero edge family without case omissions. ∎

For any fixed m, each h-subset U permits at most 2^(h−1) parities consistent with m. Hence the number of feasible local classes is at most 3+6+4=**13**, independent of the magnitude of m.

## Theorem KS.2 — Exact rank and unrank with logarithmic local search

For current support i, boundary remainder r and connectivity state q, let

\[
w_C=D_{i+1}(r\oplus e_C,\,q\star \operatorname{color}(C)),
\]

where e_C is the support-dependent XOR of odd typed edge boundaries. All triples of C have this same suffix weight. Define

\[
P_x(X)=\sum_C w_C N_C^x(X),\qquad
P_{xy}(x,Y)=\sum_C w_C N_C^{xy}(x,Y).
\]

These are exact nondecreasing integer prefix counts for the lexicographic source order (x,y,z).

To unrank an integer 0≤k<D_i(r,q): use binary search for the least x∈[0,m] with P_x(x+1)>k; subtract P_x(x). Next, search the least y∈[0,m−x] with P_{xy}(x,y+1)>k; subtract P_{xy}(x,y), set z=m−x−y, and advance r and q by that exact triple. Repeat for the eight supports. Rank traverses the given source and adds P_x(x)+P_{xy}(x,y) at each support.

**Proof.** The classes partition all local triples, and the previous theorem calculates each class's exact restricted count. For a class, its boundary and connectivity output depend only on support presence and parity, so the suffix count w_C is constant. Therefore P_x and P_{xy} equal the actual numbers of valid global completions in the indicated lexicographic prefixes. Every rank k in a positive fiber belongs to exactly one local block, found by the least-prefix criterion. Subtracting its predecessors and continuing recursively gives the inverse map. Induction on the remaining eight supports gives rank(unrank(k))=k and unrank(rank(v))=v. ∎

**Arithmetic-operation complexity.** After obtaining the inherited suffix DP, at each support computing a prefix requires at most 13 constant-degree binomial evaluations and exact-integer multiplications/additions. Binary search takes O(log(m_i+1)) prefixes for x and y. Thus the *selection* phase uses O(Σ_i 13 log(m_i+1)) such arithmetic operations per unrank, and O(8·13) for rank. This replaces the former O(Σ_i m_i²) candidate scan. All integer bit complexities, suffix-DP construction and output-bit lengths remain separately charged; this is not a uniform constant-time algorithm in the binary input length.

The conditional fixed-width source annotation remains optimal at ceil(log2 Q_m(b)) bits when Q_m(b)>0, by the R762KR pigeonhole lower bound and this explicit invertible enumerative construction.

## Exact validation

A fresh Python standard-library implementation of this closed-prefix selector was locally executed. It compared **every** forced-boundary fiber count against the independent GF(2) group-algebra recurrence for seven multiplicity vectors, each over all 512 boundaries (3,584 exact count equalities). For every nonempty fiber it tested 0, floor(Q/2), Q−1, plus all indices if Q≤12, comparing **both fast and slow rank/unrank**. Each assertion passed.

| Multiplicity vector | Q_m(0) | Total over F | fast/slow sampled rank tests |
|---|---:|---:|---:|
| (1)^8 | 6 | 1,638 | 1,638 |
| (2)^8 | 7,197 | 420,093 | 1,536 |
| (3)^8 | 71,197 | 25,000,189 | 1,536 |
| (4)^8 | 2,788,422 | 640,727,574 | 1,536 |
| (1,2,3,4,1,2,3,4) | 5,984 | 1,822,605 | 1,536 |
| (2,1,1,1,1,1,1,2) | 18 | 6,561 | 3,024 |
| (2,5,3,1,4,2,6,3) | 47,574 | 23,814,429 | 1,536 |

With m_s=10^6 and 10^12 uniformly, seven explicitly listed boundaries (0,3,18,51,204,3840,4095) were independently count-checked and three ranks per nonempty fiber round-tripped. The zero-boundary fiber requires respectively 300 and 619 bits; the tested code handles these without scanning m² triples. The fixed witness m=2,b=0,k=3598 reproduces R762KR's eight exact triples.

Single-process warm-DP illustrative timings at m=800, uniform stock, b=0, k=floor(Q/2): fast unrank 0.00072 s versus prior scan 0.83749 s, fast rank of that source 0.00010 s. These measurements are informational only; machine/runtime variance is not a complexity proof.

## Provenance, limits, next problem

Author status: exact algebraic proof and locally executed Python checks; independent review NOT_REVIEWED. No P000/ACTIVE worldview change, no replacement of any prior task science pin, no formal task Result/CLAIM/PROGRESS or native signed BRC equivalence claimed. Preserve original R762KR and its author/Activity association; this is an algorithmic extension.

Next: separate suffix-DP precomputation from one-query selection performance; explore a typed *ordered signed* lift with explicit time and third slice coordinate, and test a future BRC observer on a pair of auxiliary-source triples that the current coarse boundary fails to distinguish. Prove any claimed quotient safety at that future observation horizon, not merely at static GF(2) parity.