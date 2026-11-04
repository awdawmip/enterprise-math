# PREFIX-479 — arbitrary-word weighted BRC gate renewal, special-count law, and KMP suffix factorization

Date: 2026-11-04 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Sources and fixed model

Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`; P000/ACTIVE X6 and joint-observer preservation have been checked at that pin. Project continuity: PREFIX-478 `eb7bbb3c07223a788fe6947e2bf2f3ea3437127d`. Current behavior/rules: canonical GLOBAL_KNOWLEDGE_V1 read from `main@da094238f4383e6f5d58c8f52311c1ea3a9b8399`, plus current Enterprise Math continuation, portable and method protocols.

This is the native-six-axis **restricted positive BRC path-support model** of PREFIX-478. The ordinary directions are ten signed X6 directions `aAbBcCdDeE` on E2..E6. The distinguished special native direction `x=+E1` is allowed as the first step, or immediately after a prescribed ordinary word `w` of length `k>=1`. Every ordinary step is legal. At each x, reset the KMP prefix-suffix state q to 0. Otherwise q records the longest suffix of ordinary steps since the last x equal to a prefix of w; q ranges from 0 to k. The native positive-step weights are (6,1,12,1,18,1,24,1,36,1) on these ordinary directions and chi=1 on x. Separate counting weights set every step weight to 1.

For general **commuting formal nonnegative weights**, let `t_c` be the ordinary direction weights, `A=sum_c t_c`, `chi` the x weight, and `Q=product_{i=1}^k t_(w_i)`. Variables z and u mark path length and the number s of special x steps. The additive BRC observer, ordered-path multiplicity, positive mass and retained KMP suffix are distinct carriers. This proof concerns the precise ordered-path counting/mass carrier and its q refinement; the final native BRC support observer can still be calculated separately.

## Theorem 1 — arbitrary-word exact bivariate renewal law

For **every** ordinary gate word w, including repeated letters, opposite signs and self-overlap, the weighted ordered-language generating function is

```
L_w(z,u) = sum_(n,s>=0) M_w(n,s) z^n u^s
         = (1+u*chi*z)/(1-A*z-u*chi*Q*z^(k+1)).
```

Consequently **the ordered path total and its full special-step-count distribution depend only on k and Q**, independent of the word's letter order and KMP overlap. In particular anagrams have equal bivariate series. For unweighted counting A=10, chi=Q=1; for the native positive weights A=101, chi=1, Q is the directional-weight product.

**Proof.** Split each ordered legal path at every occurrence of x. A path with no x is an arbitrary ordinary word, with generating function `1/(1-Az)`. The ordinary block immediately preceding any noninitial x must end in w and uniquely decomposes as arbitrary ordinary prefix v followed by w, with generating function `Q z^k/(1-Az)`. This decomposition is unique even if w overlaps itself: it selects the *last* k ordinary steps before that x. Each inter-x block contributes `u chi Q z^(k+1)/(1-Az)`. The block before the first x is either empty (initial x) or an arbitrary prefix followed by w. The tail after the last x is arbitrary ordinary. Summing the geometric series for inter-x blocks and adding the no-x case simplifies exactly to the displayed formula. This argument uses only the declared legality rule and retains each ordered word as one branch. QED.

## Theorem 2 — exact coefficient for each number of special steps

Define `C(m,r)=0` unless integers satisfy `m>=r>=0`. For `s=0`, `M_w(n,0)=A^n`. For all integers n>=0 and s>=1, put `d=n-(k+1)s` and `e=n-1-(k+1)(s-1)`. Terms with negative d or e equal zero. Then

```
M_w(n,s) = chi^s * (
    [d>=0] Q^s A^d C(d+s,s)
  + [e>=0] Q^(s-1) A^e C(e+s-1,s-1) ).
```

**Proof.** Extract u^s from `(1+u chi z) sum_(j>=0) (u chi Q z^(k+1))^j/(1-Az)^(j+1)`. The numerator's 1 term gives the first summand at j=s; its u chi z term gives the second at j=s-1. Apply the formal binomial identity `[z^m](1-Az)^(-h)=A^m C(m+h-1,h-1)` for m>=0. This covers all n,s, including boundaries. QED.

Example (k=3, n=8, counting weights): s=0 gives 100000000 paths, s=1 gives 10050000, s=2 gives 4001, s>=3 gives 0, total **110054001**. Thus the ordered-path count in PREFIX-470 is recovered without enumerating X6 histories.

## Theorem 3 — exact factorization retaining every KMP history state

Let M_w be the (k+1)-state ordinary-letter KMP transition matrix with entry `(M_w)_(ij)=sum_(c:delta(i,c)=j) t_c`. Set

```
R_q(z) = [(I-z*M_w)^(-1)]_(0,q),
H_w(z,u) = (1+u*chi*z)*(1-A*z)/(1-A*z-u*chi*Q*z^(k+1)).
```

For every q=0..k, the weighted generating function of legal paths ending with KMP suffix q is

```
L_(w,q)(z,u) = H_w(z,u) * R_q(z).
```

**Proof.** Partition each legal path uniquely at its last x (or at the start for a no-x path). All ordinary characters after that cut form an unrestricted ordinary suffix, processed by the KMP automaton from q=0, hence R_q. The generating series of the empty-or-last-x-ended prefix is L_w(z,u)*(1-Az): appending an arbitrary ordinary tail to such a prefix partitions every path uniquely. By Theorem 1 this equals H_w. The multiplication is a bijective decomposition preserving length, the complete x-count, ordered multiplicity and exact step weight. The KMP transfer matrix and its formal inverse exist because its constant term is the identity. QED.

For **any fixed w**, coefficient extraction uses exact (k+1)-state ordinary automaton DP and the scalar renewal recurrence, with O(N*k*10) additions/multiplications to obtain the length prefix through N (at the stated arbitrary-integer arithmetic granularity). No full path dictionary is required to recover path-number / positive-mass suffix totals. The BRC-observation fiber itself is not quotiented by this factorization.

## Discriminating anagram witness (X6 carrier)

The two words `aab` and `aba` have the same k=3 and Q=6*6*12=432; hence their total count and total native positive mass agree at every n and s by Theorem 1. At n=8 both have 110054001 unweighted legal ordered paths and native positive mass 10936007142504414. Their unweighted KMP q=0,1,2,3 path totals are respectively

```
aab: 98939680,  9903980, 1100320, 110021
aba: 97949381, 10894279, 1100320, 110021
```

Thus the same total/Parikh-level gate weight fails to preserve declared future-observable suffix histories. Independent finite X6 Parikh/KMP compression (n=6) gives identical base BRC support size 6824 but different tagged-state supports: **10711** for aab and **10713** for aba, as independently checked in the local companion Python evidence. This is an explicit BRC information-loss witness for the total-only observer; it does not discard the retained history.

## Executed finite certificate and scope

The accompanying **actually executed** JavaScript BigInt certificate tests 8 gate words `aab, aba, aAa, ababa, abab, aa, aA, abbb`, each with count and native positive weights. For each word/weight pair it tests every 0<=n<=16, every possible 0<=s<=n, and every KMP q against three independently implemented expressions: direct path-suffix DP, bivariate binomial formula, and KMP ordinary-tail convolution; independently enumerates every ordered path at n=0..4; checks the anagram invariance and suffix contrast. It completes with `ALL_CHECKS_PASS`. Mathematical statements for all n,k arise from the explicit formal-language decomposition, not extrapolation from that finite test. A separate Python evidence program additionally verifies native X6 BRC state support for aab and aba to n=6, and performs the same arithmetic checks to n=16.

External method lineage (checked 2026-11-04): L.J. Guibas and A.M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, JCTA 30 (1981), 183–208, DOI 10.1016/0097-3165(81)90005-4; Anthony Widjaja To, *Parikh Images of Regular Languages: Complexity and Applications*, arXiv:1002.1464 (2010). The formula here specializes to the above gated X6 BRC path model and is not a general pattern-avoidance claim.

## Authority and next unit

This is an author-side proof and executed numerical certificate, not a native Result, independent Review or Admission. Current Sites identity is static read-only with research_authority_granted=false; bounded native inventory returned CONTROL_QUOTA. These facts do not change the frozen P000, worldview or project role state.

**PREFIX-480 candidate:** refactor the full BRC observation (s,y2..y6,V,W) into a weight-refined fiber generating polynomial P_(n,f,q)(t), and prove/measure whether the suffix factorization can be lifted through the observable without loss. Start with aab versus aba, n<=6, comparing exact labeled fiber multiplicities and a low-order moment readout before proposing a compression lease.
