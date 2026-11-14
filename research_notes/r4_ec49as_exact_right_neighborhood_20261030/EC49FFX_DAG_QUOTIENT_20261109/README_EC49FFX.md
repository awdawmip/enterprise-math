# EC49FFX — Exact state-quotiented native BRC prefix optimizer

**2026-11-09 | AUTHOR-SIDE EXACT COMPUTATIONAL FINITE RESULT | UNREVIEWED / NOT ADMITTED**

Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Model sources EC49FFT/EC49FFV; preceding EC49FFW at immutable commit aa91c76788d5bc60c41221e9ea8cdb2426add1f2. The exact native operation-prefix counting identity is **prior work EC49FBS (2026-11-05)**; this note adds the **state-quotient theorem and executable finite extension**.

## New finite theorem and algorithm

Fix H2 operation paths ce,de,ec,ed (original signed six-axis BRC codes, low DFA signatures 4,1,8,2). For an integer h>=3 select four length-h operation paths with original nine-state DFA signatures 1,2,4,8, one each, allowing **any number of positive complete BRC cache keys**. Let M(h) be the minimum distinct nonempty native signed-X6 microstep-prefix count for all eight paths.

**Exact computed classification:** M(h)=4h+42 for **each integer h=14,15,...,30**. Newly closed H14=98, H15=102, H16=106, H20=122, H24=138 and H30=162. Combined with previous H10-H13 verified results, the exact finite range is 10<=h<=30. This is an exhaustive finite DP result, not an infinite-h value formula.

**Algorithmic theorem:** for arbitrary input h>=3, a 16-mask dynamic program over at most 9(h+1)^4 quotient states computes M(h) exactly, using O(h^4) arithmetic operations and O(h^4) memory for the fixed four-signature, nine-state model; integer-cost bit complexity is O(h^4 log h). This replaces enumeration of exponentially many operation words.

## Exact native model

Operation alphabet in order a,c,d,e,f,g and full signed-native codewords (axis numbers encode the signed six-axis microsteps):
- a=(-1,-1); c=(1,2,-1,-2); d=(2,1,-2,-1);
- e=(3,1,1,-3); f=(1,-1); g=(2,-2).

For each operation word of length h, counts E=#e, A=#a, F=#f, G=#g must obey E=A+1>=1 and 2E+F<=h. Its complete positive key equals (x,y,z)=(h+1-G,h+1-2E-F,E), and #c+#d=x+y-h-1; all six signed native displacement components sum to (2,0,0,0,0,0). Its original nine-state DFA terminal signature must lie in {1,2,4,8}. These conditions describe the **entire** admissible candidate domain (for unrestricted positive keys).

Define the previously proved EC49FBS native edge cost for a set of outgoing letters S at one operation-prefix:
F(S)=SUM_{u in S} length(code(u)) - 1[c,f subset S] - 1[d,g subset S].

The six codewords have pairwise distinct two-step prefixes; only pairs c/f and d/g share their first step. Distinct operation prefixes contribute disjoint additional native edges after their maximal common operation history. Thus native cost for any finite path family is sum_P F(S(P)). Relative to the fixed baseline W0={ce,de,ec,ed}, baseline outgoing letters B(P) create exact incremental local cost F(S(P) union B(P))-F(B(P)). The original H2 baseline contributes 28 edges. B(P) is nonempty only for the root and operation-prefixes c,d,e (depth <=1).

## Quotient theorem and rigorous optimality argument

Let s=(k,E,A,F,q), with operation depth k and exact nine-state observer q. Future admissible suffix words depend only on s and h. At **every depth k>=2**, B(P)=empty. Therefore if two different full operation prefixes P and Q of depth k reach the same state s, the 16 exact minimum descendant costs for each subset of the four required terminal signatures are equal. The native code is prefix-free, so descendant costs for P and Q have the same internal sharing and do not depend on earlier distinct histories. Memoize this 16-cost row for each s. Retain distinct root and depth-one rows where baseline overlap is nonempty.

Compute each row by combining the four disjoint first-microstep groups {a}, {c,f}, {d,g}, {e}. Allocate disjoint signature masks to selected children, add child costs and exact local F-difference, and perform min-plus mask convolution. The depth-h leaf only supplies the signature actually returned by the DFA. The terminal conditions E=A+1>=1 and 2E+F<=h and the transitions give complete valid-word coverage. Duplicate realizations of a required signature can be deleted without increasing prefix cost. Induction on remaining depth proves the root row for all four signatures is the **global minimum**, with no sampling or numerical approximation.

There are <=9(h+1)^4 state tuples and 16 masks per tuple. Six children and 4 fixed local groups require a bounded number of integer comparisons and additions per state, proving the stated polynomial complexity.

## Reproduced evidence and explicit attaining family

- Actual compiled C++ code VERIFY_EC49FFX_DAG.cpp returned exact minima for all h=3..30. It reproduced all earlier unrestricted H3-H13 values: 36,44,52,59,65,71,77,82,86,90,94. H14-H30 returned 98,102,106,...,162.
- Independent Python direct-score implementation VERIFY_EC49FFX_INDEPENDENT_SHORT.py reproduced H3,H6,H9,H11,H14,H20,H24,H30. An additional independent reconstructed-witness Python solver checked H3,H6,H9,H11,H14,H15,H16,H20,H24,H30 and independently expanded the native signed microsteps.
- VERIFY_EC49FFX_NATIVE_WITNESS.py checked all h=14..30 with exactly two complete keys (3,1,1) for H2, and (4,h-2,1) for Hh. At Hh, paths for sig1/sig2/sig4/sig8 respectively are gfe g^(h-4) d, fe g^(h-3) d, fe g^(h-3) c, gfe g^(h-4) c. Their signed-native prefix-union cost is exactly 4h+42.
- COUNT_EC49FFX_CANDIDATES.py uses a separate arbitrary-precision word-count recurrence: H13=367,524,430 (agrees with old enumeration), H14=1,801,977,660, H20=24,952,444,838,400, H30=205,177,995,658,512,067,620. State-quotient optimization bypasses literal enumeration of these words.
- H30 on the local execution container: 137,348 distinct evaluated DP states and 526,517 cache hits; about 0.05 seconds of inner DP time and 277,632 KiB peak resident memory including dense arrays (one-machine measurement). This is separate from the mathematical big-O bound.

Reproduce: compile C++ with g++ -O3 -std=c++17, run for each h=3..30; run Python independent-short for h=3,6,9,11,14,20,24,30; execute native witness and arbitrary-precision counting scripts. All integer arithmetic is exact.

## Research scope and continuation

The infinite-h equality M(h)=4h+42 for every h>=10 is the next analytic lower-bound / counterexample question. The original frozen mother problem has additional H2/H3 high signatures and its own 24-label, <=5-key, <=93-edge constraints: carry that exact observation distribution before lifting this auxiliary model result to the mother objective.

Actual authority: the old EC49AS exact lookup returned NO_CURRENT_IMMUTABLE_PUBLICATION; an EC49AS-bound session request returned UNKNOWN_CURRENT_TASK. This is an **independent author-side scientific artifact**, not a formal CLAIM/Result or Driver admission; P000 and protected ACTIVE worldview are unchanged.
