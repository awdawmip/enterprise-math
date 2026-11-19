# PREFIX-942 — Exact CRT/floor-sum count of named XOR collisions, and the complete W13 census

Date: 2026-11-19. Lane: Enterprise Math / R6 direct auxiliary research. Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`, unchanged. Dependencies: PREFIX-940 (odd-core W11; \`997f12987c154983381d77c6fc66684b5eda6111\`) and PREFIX-941 (quotient-first XOR inverse; \`285e59534f93b1182b677c7093d02587e8272391\`). Classification: AUTHOR-PROVED / FULL-FINITE-EXACT-COMPUTED / INDEPENDENT-CODE-AGREEMENT / NOT-INDEPENDENTLY-MATHEMATICALLY-REVIEWED / NOT-ADMITTED.

## 1. The exact finite question

Let \`L=262145\`, \`U=524287\`, \`Q={L,L+2,...,U}\` (131,072 strictly 19-bit odd integers), \`N=2^32\`, \`0<=i,j<=18\`, and odd positive \`k\`. A named trajectory is \`F_x^j=(x,x XOR 2^j)\`; it is interpreted in the auxiliary two-port observation \`Phi_(a,b)(u,v)=(u mod a,v mod b)\` for \`a,b in Q\`. For \`k\` in {11,13,15,17}, both relevant trace endpoints are in [0,N). Count all distinct **parameter witnesses** \`(a,b,i,j,t)\`, \`t>=1\`, solving

\`\`\`
D_k(a,i,j) = (k*a XOR 2^j) - 2^i = t*b .                 (1)
\`\`\`

Each such witness gives different legal histories \`F_0^i\` and \`F_(k*a)^j\` with equal observation. Parameter-witness totals are not distinct-pair counts; deduplicate independently when that question is asked.

## 2. The exact CRT/floor-sum theorem

**Theorem.** For an odd positive core k, fixed positive quotient t and source bits i,j, the number of (a,b) in Q^2 satisfying (1) is exactly computable using at most two gcd/CRT arithmetic progressions and two floor sums per surviving progression, without enumerating a or b.

Set \`H=2^j\`. For each signed candidate \`sigma in {+1,-1}\` put

\`\`\`
c_sigma = 2^i + sigma * H,
Y = t*b + 2^i,
k*a = Y + sigma * H.                                   (2)
\`\`\`

When \`sigma=+1\`, require bit_j(Y)=0 (setting the j-th bit); when \`sigma=-1\`, require bit_j(Y)=1 (clearing the bit). Thus (2) is equivalent to (1) exactly on its indicated bit branch.

Let \`d=gcd(k,t)\`. A branch is empty unless \`d | c_sigma\`. If nonempty, put \`m=k/d\`, \`t'=t/d\`, \`c'=c_sigma/d\`. For m>1 the linear congruence in (2) has exactly one residue

\`\`\`
b = r_sigma (mod m), r_sigma = -c' * inverse_mod(t',m) (mod m).   (3)
\`\`\`

For m=1 use residue zero. Since k (and m) are odd and b must be odd, (3) together with b odd is a single progression modulo \`2*m\`. In particular, no enumeration of residue classes modulo \`2^(j+1)\` is necessary.

The allowed a interval requires

\`\`\`
b_lo = max(L, ceil((k*L-c_sigma)/t)),
b_hi = min(U, floor((k*U-c_sigma)/t)).                   (4)
\`\`\`

For odd k,b, a will be odd if and only if the quotient parity satisfies

\`\`\`
t odd <=> ((i==0) == (j==0)).                          (5)
\`\`\`

Reject branches violating (5). In each remaining interval (4) the odd congruence solutions form \`b_q=B+2*m*q\` for q=0,...,n-1, where B is the first allowed value; an empty progression contributes zero. Define

\`\`\`
A=2*m*t; Y_q=t*B+2^i + A*q;
F(n,h,A,C) = sum_{q=0}^{n-1} floor((A*q+C)/h).
ones = F(n,H,A,t*B+2^i) - 2*F(n,2*H,A,t*B+2^i).       (6)
\`\`\`

Because \`bit_j(Y_q)=floor(Y_q/H)-2 floor(Y_q/(2H))\` for every nonnegative integer Y_q, \`ones\` counts exactly those q with bit_j(Y_q)=1. The \`sigma=+1\` branch contributes \`n-ones\`; the \`sigma=-1\` branch contributes \`ones\`. All branches are disjoint because the actual bit_j(Y) determines sigma uniquely. Summing over t,i,j proves the theorem. Both floor sums in (6) are exactly evaluated by Euclidean recursion in logarithmic arithmetic operations. This is a count of all witness tuples, not a bound or a sample.

The complete positive-quotient window is

\`\`\`
1 <= t <= floor((k*U + 2^18 - 1)/L),                  (7)
\`\`\`

since XOR adds at most \`2^18\` and \`2^i>=1\`. The full 19x19 source-bit range and every admissible quotient are included.

## 3. Exact full-domain counts

Two independent implementations were actually run: (a) Python arbitrary-precision CRT and exact floor-sum method (6), (b) C++17 direct enumeration over all a,i,j, computing D exactly and testing every integer t between ceil(D/U) and floor(D/L), collecting pair identifiers for k=11 and k=13 and sorting for exact deduplication. Their raw parameter-witness counts and all per-quotient counts agree for all k below.

| odd k | exact parameter witnesses \`(a,b,i,j,t)\` |
| --- | ---: |
| 11 | 16,974,425 |
| 13 | 16,796,156 |
| 15 | 20,708,178 |
| 17 | 19,318,164 |

For k=11, the raw count agrees with the independently committed PREFIX-940 value. For k=13, C++17 additionally reports:

| Set of ordered modulus pairs | Exact size |
| --- | ---: |
| W11 | 13,144,330 |
| W13 | 12,993,739 |
| W11 intersection W13 | 134,197 |
| W13 minus W11 | 12,859,542 |

The last row is **only relative to W11**, not a net addition to the full previously recorded B/Z/S/U/V/W2/.../W11 union. This run did not re-evaluate those other intersections; the previously published global union of 7,558,699,988 remains unchanged.

A concrete member of W13 outside W11 is \`a=262145, b=262775, i=1, j=13, t=13\`. Here \`13a=3,407,885\`, \`13a XOR 8192=3,416,077\`, and \`3,416,077-2=3,416,075=13*262775\`. Thus the two legitimate traces \`(0,2)\` and \`(3,407,885,3,416,077)\` have exactly the same two-port reading. Non-membership in W11 is established by the complete sorted-pair merge, not by the single displayed witness.

The Python program also compared the CRT/floor-sum method with direct brute enumeration on the independent small domain: odd a,b from 5 to 63, 0<=i,j<=5, k in {1,3,5,7,9,11,13}; for each k the exact counts match 1156,1611,1544,1516,1680,1552,1487. Its exact floor_sum kernel passed 300 fixed-seed randomized checks against direct summation.

## 4. Verification boundary and reproducibility

- Input: frozen scientific pin \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`; current behavioral rules read separately. Auxiliary typed observer is exactly as specified above; no native X6 projection, BRC evaluation or six-dimensional theorem is asserted.
- Exact arithmetic throughout: arbitrary-precision Python and C++17 64-bit integers (the maximum intermediate in this declared range is much smaller than 2^63). No floating point.
- C++17 directly enumerates 131,072 first moduli x 361 source-bit combinations for each k, and checks all possible divisors in a proven interval; the CRT algorithm enumerates quotient/source/sign cells and sums entire arithmetic progressions exactly.
- Sorted pair IDs are \`((a-L)/2)*131072+(b-L)/2\`, unique uint64 IDs. C++17 sorts and unique-ifies W11 and W13 then computes their exact intersection.
- The actual executed scripts and complete machine-readable per-quotient totals are in the same \`research_notes/portable_direct/\` directory as this paper. No mathematical independent review or formal admission has yet occurred.

## 5. Research frontier and attribution

This replaces a first-modulus loop for exact **raw-witness counting**. The next discriminating task is to count *distinct (a,b) pairs* under multiple (i,j,t) without constructing all pair IDs and to subtract W13 from the **entire frozen previous union**. Only the latter establishes the actual new noninjectivity coverage from k=13.

Original R6 attribution: Researcher \`EM-DIRECT-58C410\`, SID \`MCP-31edc522830749ad8775ca012e02ef30\`, Activity \`RA-25432C4AAE9BF66A907F5115\`. Portable Activity/Source association follows its own real permission/CAS and readback; a GitHub paper itself is not an authenticated CLAΙM or mathematically accepted Result. Shared X6 has an independent current owner; no shared mutation was attempted. Parent question \`B_fix,odd(32) in {19,20}\` remains open.
