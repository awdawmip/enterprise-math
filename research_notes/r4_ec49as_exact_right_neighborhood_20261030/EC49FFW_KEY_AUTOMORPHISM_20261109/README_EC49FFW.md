# EC49FFW — BRC complete-key bijection, signed-observer involution and exact suffix feasibility

**2026-11-09 · AUTHOR_ANALYTIC_PROOF / EXECUTED_EXACT_INTEGER_COUNTS / NOT_REVIEWED / NOT_ADMITTED.**
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Immediate model provenance: EC49FFV, immutable commit `de8f6306e63828368b972509a78ceea0b358401d`, source `exact_multikey.cpp`, blob `3acb8d2b5b212e86e20d3fe9dd9e547e631d5442`.
Research scope: native BRC nine-state *word/observer/combinatorial counting* model only. A word-count identity is not a native six-axis prefix-cost identity.

## Theorem 1. Eliminate the complete-key enumeration without losing legal words

Let a word w of length h use the six native BRC operation letters a,c,d,e,f,g, and let n_j be the corresponding nonnegative counts. The EC49FFV legal complete-key quotas are:
```
n_a=z-1, n_e=z, n_c+n_d=x+y-h-1,
n_f=h+1-y-2z, n_g=h+1-x,
```
with positive integer key K=(x,y,z). There exists a legal positive complete key for w **if and only if**
```
n_e=n_a+1,  and  n_c+n_d+n_g >= 1.
```
In that case the key is **unique** and is recovered without a search:
```
z=n_e,    x=h+1-n_g,    y=n_c+n_d+n_g.
```
Proof: substitute the quota relations and use h=sum_j n_j. Conversely n_e=n_a+1 implies n_e>=1; x>=1 because n_g<=h; y>=1 by the second condition. Substitution into all five quota equalities gives the original counts exactly. Thus the two predicates are jointly necessary and sufficient; no keys are lost.

Let N_h be the total number of legal raw operation words (before selecting a terminal observation signature). Then
```
N_h = [t^1] ((4+t+t^{-1})^h - (1+t+t^{-1})^h).
```
Explanation: t counts an e, t^{-1} an a, 4 counts unrestricted c/d/f/g; subtract the words containing no c/d/g, whose third category is f alone. All operations in this formula are exact formal integer-coefficient operations; there is no continuous or classical propagator. Equivalently,
```
N_h = sum_{k=0}^{floor((h-1)/2)}
  h!/(k! (k+1)! (h-2k-1)!) * (4^(h-2k-1)-1).
```

## Theorem 2. Exact involution between terminal BRC signature classes

Use the original nine-state DFA transition T with operation order (a,c,d,e,f,g), initial state q=0, and terminal signature table
`S=(0,0,4,1,16,32,8,2,0)`.
Let the operation involution sigma exchange c<->d, f<->g while fixing a,e, and let the DFA-state involution pi exchange (2,3), (4,5), (6,7), fixing 0,1,8.

The 54 exact transition identities
```
T[pi(q)][sigma(j)] = pi(T[q][j])
```
hold, as independently checked in `VERIFY_EC49FFW.py`; also pi(0)=0. Consequently every operation word w and sigma(w) have conjugate terminal DFA states. Their letter counts n_a,n_e are unchanged, so the difference n_e-n_a=1 is preserved. Any word ending with signature 1,2,4,8 necessarily contains c or d (directly from the DFA); hence both words satisfy the positive-key requirement regardless of f/g exchange. Therefore sigma is a fixed-length bijection of **all** legal low-signature candidates that swaps 1<->4 and 2<->8.

**For every integer h>=1**, letting A_h(s) be the number of all complete-key-legal h-letter words ending with signature s,
```
A_h(1)=A_h(4),    A_h(2)=A_h(8).
```
This is an exact all-h theorem, not a finite numerical extrapolation. The involution need not preserve an individual complete key: in general it changes x,y. Nor does it preserve the original ordered signed X6 microstep-prefix union, so no prefix-cost equality follows.

## Theorem 3. Exact suffix-language pruning for a fixed quota

For any nonnegative six-operation remaining quota vector n and current DFA state q, define F(n,q) to be the set of low signatures reachable by exact completion. Its finite recursion is
```
F(0,q) = {S(q)} intersect {1,2,4,8}
F(n,q) = union_{j:n_j>0} F(n-e_j,T[q][j]).
```
A quota-feasible partial word can be pruned **if and only if** F(n,q) is empty; the proof is induction on sum(n). This preserves every possible native low-terminal operation word. The memo table has at most 9*product_j(n_j+1) states per fixed quota, each taking at most six transitions. When used inside enumeration it avoids expanding dead suffixes before building the signed X6 prefix trie. It does not itself establish a lower native prefix-edge optimum.

## Actually executed finite checks and scope

Two independently organized exact integer counters were executed locally:
1. fixed-key/split backward suffix DP counting all words, accepted words and the number of per-split **operation-prefix visits** retained by feasibility; and
2. a forward transfer recurrence on (nine-state DFA state, n_e-n_a, seen(c/d/g)). They agree exactly for h=3,...,14, including each low signature. The independent forward recurrence extends to h=32. H9=625,050 and H10=3,091,460 accepted candidates reproduce the prior EC49FFV exact trie report.

Selected exact counts (all legal / four low terminal classes combined):
```
H9   1,961,955 / 625,050
H10  11,365,650 / 3,091,460
H11  65,942,250 / 15,233,900
H12  383,219,928 / 74,884,944
H13  2,230,675,785 / 367,524,430
H14  13,004,452,230 / 1,801,977,660
H20  524,194,075,207,440 / 24,952,444,838,400
H32  927,724,183,306,025,493,349,536 / 4,981,943,563,654,708,671,936
```
Per-split operation-prefix visit totals before/after feasibility filtering (same initial split repeated as one visit; **not** unique signed-prefix-trie nodes):
```
H10: 33,702,386 -> 9,312,276 (72.37% filtered)
H11: 195,620,911 -> 45,944,720 (76.51% filtered)
H14: 38,613,203,623 -> 5,448,780,918 (85.89% filtered)
```
These are exact virtual node-visit counts, **not measured runtime, RAM, or full-prefix edge savings**. The large h counts are exact combinatorial computations, not an exhaustive physical traversal of all words.

## Reuse and next discriminating research action

Use the key-bijection to enumerate legal BRC words by a single balance predicate, the involution to validate candidate coverage, and F(n,q) to pre-prune dead suffixes. Next: incorporate this filter into the existing EC49FFV C++ signed-X6 cost DP and test H11 for a <86-edge witness or an exact >=86 lower certificate. Preserve h=11 scientific input and H2 baseline (28 signed microstep prefixes). The known analytic upper bound is 4h+42=86 at h=11; **this note does not claim an H11 optimum**. Reuse BRC-native path and observer semantics; do not convert abstract-word counting into a statement about physical X6 evolution or original 22-demand target without the exact interface.
