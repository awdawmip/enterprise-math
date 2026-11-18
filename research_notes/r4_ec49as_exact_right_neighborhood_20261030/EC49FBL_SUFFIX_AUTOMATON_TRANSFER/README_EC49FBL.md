# EC49FBL — Exact terminal-prefix suffix-transfer theorem and 124-pair BRC scan

Date: 2026-11-05. Research mode: TASK_RESEARCH / author-side exact enumeration. Scientific input frozen pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Mother problem and local question

The H2–H9 mother problem minimizes the total number of distinct signed native-X6 primitive-prefix edges required for rank-nine observer clauses under a five-complete-positive-BRC-key budget. The earlier author-side mother bounds are `80 <= E* <= 94`. EC49FBK showed that the primitive two-step operation code is prefix-free and exhibited the special f/g observer-stable lift. This unit determines *all* possible complete-terminal prefix pairs for the 124 L/M candidate pairs of EC49FBH, across nine early/late horizon combinations, by a general finite automaton transfer.

This enumeration supplies a precise measure of total-terminal inheritance opportunities, rather than optimizing full prefix-edge cost. Each pair's complete schedule still needs its own global rank feasibility and edge-cost optimization; interior partial-prefix sharing is included in that downstream optimization.

## Definitions and exact input

Primitive signed X6 operation letters, in signed-axis-index notation:
`a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2)`.
Each encoded operation starts with one of six different signed primitive two-step sequences; therefore a complete terminal primitive prefix is equivalent to an operation-word prefix (EC49FBK).

Legal horizon-h operation word w has endpoint D(w)=(2,0,0,0,0,0), complete positive BRC key K(w)=(x,y,z,0,0,0), and nine-state observer terminal state s with accepted signature S(s) in {1,2,4,8,16,32}. The frozen DFA transition table T and S array appear exactly in the executable verifier.

Let `cd = #c+#d`. The endpoint, positive key and length impose exactly

```text
#a=z-1, #e=z, #cd=x+y-h-1, #f=h+1-y-2z, #g=h+1-x.
```

Thus for an early terminal (h,L=(x,y,z)) and late terminal (H,M=(X,Y,Z)), define d=H-h and the **unique required suffix-count vector**:

```text
Delta a = Delta e = Z-z
Delta cd = (X-x)+(Y-y)-d
Delta f = d-(Y-y)-2(Z-z)
Delta g = d-(X-x).
```

Every entry must be a nonnegative integer for terminal prefix inheritance. Together these counts sum to d.

## Theorem — exact automaton suffix-transfer count

Let `C_{h,L}(s)` count legal accepted early words ending in DFA state s. Let `A_D(s,t)` count suffix words with the prescribed vector D, choosing c or d separately at each of the `Delta cd` positions, whose DFA path sends s to t. Then the number of ordered terminal prefix pairs (w,v) from horizon h/key L to horizon H/key M with *both* signatures accepted is **exactly**

```text
P_all(h,L;H,M) =
   sum_{s,t: S(s) != 0, S(t) != 0} C_{h,L}(s) A_D(s,t).
```

If D has a negative count, P_all=0. For the rank-specific clause profile of EC49FBH, restrict S(s) to `R_h` and S(t) to `R_H` to get the exact clause-compatible count P_clause. Here `R4=R5=R7=R8={1,2,4,8}`, `R6=R9={16,32}`.

**Proof.** If a valid late operation word v contains the complete early word w as prefix, the word-count differences force exactly D by subtracting the five integer identities above. The first two native steps of every letter uniquely identify that letter, so the primitive terminal prefix condition gives the same operation suffix v=wt. Conversely any suffix with the D counts has exactly d operations, adds the required positive cache-key coordinate differences, and has zero signed displacement: a contributes -2 on E1, e contributes +2 on E1, while c,d,f,g contribute zero and Delta a=Delta e. Thus wt is a valid late endpoint/key word. Its observer state is exactly the deterministic T transition of the early state through the suffix. Finally the map (early word, suffix word) to (early terminal, late terminal) is bijective. Counting early paths by state and suffix paths by endpoint state proves the formula and the rank-restricted form. QED.

**Exact evaluation.** The program uses a recursive, memoized state-count dynamic program over five nonnegative operation-count classes (a,cd,e,f,g) and nine DFA states; the cd-class branches on c versus d. Every integer is checked against the JavaScript safe-integer bound. All 124 candidate pairs are taken verbatim from the immutable EC49FBH report by filtering non-null `minH2H6`; no extra candidate pair is added.

## Executed results

For 124 feasible EC49FBH pair configurations, all nine pairs `h∈{4,5,6}, H∈{7,8,9}` were counted. Totals across these **124 distinct hypothetical key configurations** are:

| Exact quantity | Count |
| --- | ---: |
| Candidate L/M pairs | 124 |
| With at least one accepted terminal prefix pair | 94 |
| With zero accepted complete-terminal prefix pairs | 30 |
| All accepted complete-terminal prefix pairs (sum over windows/configurations) | 141,920 |
| Clause-compatible complete-terminal prefix pairs | 39,576 |
| Signature-preserving complete-terminal prefix pairs | 129,828 |

Two highest clause-compatible configurations are L=(4,3,1), M=(7,4,2) and L=(5,2,1), M=(8,3,2), each with 1,440 clause-compatible pairs. The EC49FBK control comparisons reproduce exactly: L=(4,3,1),M=(8,2,1) has zero terminal prefix pairs; L=(5,2,1),M=(8,2,1) has 194, all clause-compatible. The detailed JSON records 124×9 exact horizon-pair counts and all four anchor checks.

## Validation, uses and next question

The actual JavaScript 9-state integer DP generated `EXACT_REPORT_EC49FBL.json`. Independently, a locally executed Python standard-library *direct ordered-word enumeration* reconstructed all nine pair counts for four selected configurations, including the zero case, the fff-lift case, the 4,920/1,440 case and the 2,304/1,440 case, and agreed entry-by-entry. The direct cross-check source is `CROSSCHECK_EC49FBL.py`. The mathematical theorem supplies complete finite counting semantics for all 124 pairs, while only four selected pairs received a second implementation's brute-force cross-check.

The next unit is rank-aware joint prefix-edge optimization for the highest clause-compatible L/M pairs, using these exact terminal-prefix matrices to select useful candidates, while allowing interior-prefix sharing and alternative H2/H3 roots. Test a complete legal <=93-edge witness against the true mother constraints. The source report's 124-pair set is an EC49FBH early-feasibility set, not a proof that each fixed L-early/M-late schedule is rank-feasible.

## Provenance and status

- Exact pair source: EC49FBH `26d3b584ca34ff7439ba0c5879f93a1cc40ee29a`, `EXACT_REPORT_EC49FBH.json`.
- Immediate predecessor EC49FBK: `c7c7620c0df7e51e5ca80c58ec966ba74e9a0a20`.
- Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
- Normative read: account global `main@fb2cba977b1467694decb8bb06ceb8802efd3f3b`, Enterprise Math control `main@ace008c3e9694a334dd857a5523dd806f4e6e273`; P000/ACTIVE untouched.
- Result class: AUTHOR_PROOF / EXACT_INTEGER_ENUMERATION / PYTHON_BRUTE_CROSSCHECK_SAMPLE / PORTABLE_DRAFT. Native CLAIM, Result and independent Driver verdict depend on current native execution authorization.
