# PREFIX-941: Exact modular-lattice floor-sum census for named XOR collision witnesses

Date: 2026-11-19. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Parent: PREFIX-940, awdawmip/enterprise-math@997f12987c154983381d77c6fc66684b5eda6111.
Status: AUTHOR_PROVED / EXACT_FINITE_COMPUTED / TWO_INDEPENDENT_ALGORITHMS_MATCH / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.
Scope: auxiliary named XOR two-port observer; no native six-dimensional X6 transfer is claimed.

## Theorem: exact census with no scan of a or b

Fix odd L,U and Q={L,L+2,...,U}; fix odd k>0, source indices 0<=i,j<=J, and positive t. Count the witnesses (a,i,j,t) with a,b in Q and

    ((k*a) XOR 2^j)-2^i = t*b.                      (1)

Require 0<=k*a<2^32 and 0<=(k*a XOR 2^j)<2^32 for the specified legal trajectory model. The next formula exactly counts witnesses of (1), in arithmetic complexity logarithmic in the bit modulus and **without looping over Q**.

For each sign s in {+1,-1}, put C=s*2^j-2^i, g=gcd(k,2*t) and d=2*t/g. Since b must be odd,

    k*a+C = t (mod 2*t).                           (2)

If g does not divide t-C, the sign cell is empty. Otherwise gcd(k/g,d)=1 and there is exactly one residue a0 in [0,d) satisfying

    (k/g)*a0 = (t-C)/g (mod d).

Because k and g are odd, d is even. An even a0 gives an empty cell (a in Q must be odd). The two box bounds a,b in [L,U] are equivalent to

    lo=max(L,ceil((t*L-C)/k)),
    hi=min(U,floor((t*U-C)/k)).

Let h0=ceil((lo-a0)/d), h1=floor((hi-a0)/d), and return zero when h1<h0. Otherwise set n=h1-h0+1, A=k*d, B=k*(a0+d*h0), M=2^(j+1), P=2^j. Define the exact integer floor-sum S(n,M,A,B)=sum_{x=0}^{n-1} floor((A*x+B)/M) and H=S(n,M,A,B+M-P)-S(n,M,A,B). The number of witnesses with sign -1 is H; with sign +1 it is n-H.

**Proof.** Exactly one sign applies to every XOR flip: (x XOR 2^j)=x+s*2^j with s=+1 if bit j of x is zero and s=-1 otherwise. Condition (2) is equivalent to b=(k*a+C)/t being odd integral. The linear-congruence theorem gives precisely the progression a=a0+d*h; the interval ensures both a and b lie in Q. For a in that progression, x=k*a=A*z+B. Its bit j is 1 precisely when (x mod M)>=P. For any integer z the indicator of (z mod M)>=P equals floor((z+M-P)/M)-floor(z/M). Summing gives H. The sign+1 cell is its complement. Both signs exhaust and partition the witnesses. QED.

Normalizing signed coefficients and applying the Euclidean floor-sum algorithm evaluates each S in O(log M) integer arithmetic steps; modular inversion costs O(log(2*t)). A complete census over source bits and t<=T uses O((J+1)^2*T*log(max(2^(J+1),T))) arithmetic operations and O(T) output counters, independent of |Q| at the loop level. This is an arithmetic-operation bound, not a constant-bit-cost guarantee. A safe complete quotient bound is

    T=floor((k*U+2^J-1)/L).

## Full-domain exact evidence

Domain: L=262145, U=524287 (131072 odd moduli), J=18. An independently written C++17 program directly visits every a and all 361 (i,j) combinations, checking every feasible quotient. Its full per-t vectors agree with the Python modular-lattice algorithm.

| k | Complete quotient scan | Raw witness tuples | Comparison |
|---:|---:|---:|---|
| 11 | t=1..22 | 16,974,425 | Matches independently enumerated PREFIX-940 by-t record |
| 13 | t=1..26 | 16,796,156 | Full independent C++17 by-t equality |
| 15 | t=1..30 | 20,708,178 | Full independent C++17 by-t equality |

By-t vectors (the first entry corresponds to t=1):

    k=11 [0,0,0,0,4766,75469,1720886,271076,3059619,388451,4266964,355465,2648020,243410,1778629,159369,1113784,93991,588875,41707,163944,0]
    k=13 [0,0,0,0,0,0,520071,138631,1860756,256049,2714012,334399,3503663,309679,2378264,225604,1713475,160187,1188106,107924,762609,65074,411643,29409,116601,0]
    k=15 [0,0,0,0,0,0,2497,41502,1466057,214385,1835786,373919,2427372,293355,5319496,274167,2153128,304872,1627616,194278,1797572,113588,850698,113969,692941,47686,454373,21841,87080,0]

The Python source also directly enumerated 16 smaller parameter combinations (odd k in {1,3,5,11}, J in {0,1,2,4}, odd Q=3..31) and all matched. This is auxiliary software testing; the three full direct C++ checks provide the full-domain independent finite comparisons.

**Scope distinction.** These counts represent *parameter witnesses*, not deduplicated ordered pairs (a,b); a pair can have many witnesses. The established distinct-pair union of 7,558,699,988 from PREFIX-940 remains unchanged. The complement is not proved injective.

## Reproduction and next question

Exact originally executed programs: PREFIX941_R6_EXACT_FLOOR_SUM_SIEVE.py (integer Euclidean floor sums) and PREFIX941_R6_DIRECT_FULL_CENSUS.cpp (exhaustive direct scan). Complete local source, raw results, SHA-256 manifest and tests are in the accompanying PREFIX941_R6_REPRODUCTION_BUNDLE.zip; they are distinct from this publication. No floating arithmetic, sampling in the three full censuses, independent project mathematical review, formal Source Result, or X6 CLAIM is asserted.

Next question: derive a **distinct ordered-pair union/old-family-overlap** counter from these modular cells, or certified bounds avoiding explicit enumeration of every pair. Retain source-bit identity and immutable historical evidence. Mother problem B_fix,odd(32) in {19,20} remains OPEN.
