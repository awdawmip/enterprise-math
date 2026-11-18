# EC49FFW addendum — closed forms for every native nine-state BRC low-signature candidate count

**2026-11-09 · AUTHOR_ANALYTIC_ALL_H_FORMULAE / FINITE_INDEPENDENT_AUDIT / UNREVIEWED.**
Same frozen EC49FFV scientific model and inputs as README_EC49FFW.md; this addendum strengthens its global counting theorem.

## Four-region theorem of the actual nine-state observer

Read the original EC49FFV DFA with operation order (a,c,d,e,f,g) and terminal signatures (0,0,4,1,16,32,8,2,0). The nine states partition into
```
L = {0,1,4,5}      (no c/d seen)
C = {2,6}          (c seen, d absent)
D = {3,7}          (d seen, c absent)
X = {8}            (both seen; absorbing)
```
From L, operations a/e/f/g remain in L, c enters C and d enters D. From C, all operators except d remain in C, while d moves to X; from D all except c remain in D, while c moves to X. X is absorbing. All and only states in C union D have a low terminal signature in {1,2,4,8}. This checks directly from the finite transition table, hence holds for words of **every** length by induction.

**Exact language characterization:** an operation word ends in a low signature iff it contains at least one c and no d, or at least one d and no c. When the complete-key balance n_e=n_a+1 also holds, positivity of the key follows automatically from c+d>0, by Theorem 1 of README_EC49FFW.

## Closed binomial-coefficient formulas

Define for nonnegative integer h, integer r>=0, and nonnegative integer m:
```
B_h(r;m) = [t^r] (m+t+t^-1)^h
         = sum_{k=0}^{floor((h-r)/2)}
           h!/(k! (k+r)! (h-2k-r)!) m^(h-2k-r).
```
Set B_h(r;m)=0 when h<r. All values are exact integers; t is a formal balance marker for e minus a, not a physical phase or continuous variable.

Let A_h(s) count positive-complete-key legal operation words with low terminal signature s. Let N_h count all positive-complete-key legal operation words, irrespective of terminal signature. Then **for every h>=1**:
```
N_h = B_h(1;4) - B_h(1;1)
A_h(1) = A_h(4) = 2*B_(h-1)(1;3) - B_(h-1)(1;2)
A_h(2) = A_h(8) = B_h(1;3) - B_h(1;2)
                    - 2*B_(h-1)(1;3) + B_(h-1)(1;2)
sum_{s in {1,2,4,8}} A_h(s)
       = 2*( B_h(1;3) - B_h(1;2) ).
```
These are all-h exact theorems and replace exponential word enumeration for **candidate counts**.

Proof of total: all words with n_e-n_a=1 have four neutral operation choices c,d,f,g, so the first coefficient is B_h(1;4). Words with c=d=g=0 are formed using a,e,f, giving B_h(1;1); subtract to require positive y.

Proof of low total: a low word has exactly one of c or d represented and at least one occurrence of that chosen letter. With c chosen, the neutral choices are c,f,g, giving B_h(1;3), minus words without c, giving B_h(1;2). The d-only case is disjoint and symmetric.

Proof of the split: for a c-only low word, its final state is signature 4 exactly when the **first operation of the complete word** is c or f. If the first operation is c, the unrestricted remaining suffix over a,c,e,f,g contributes B_(h-1)(1;3); if the first operation is f, at least one c must occur later, contributing B_(h-1)(1;3)-B_(h-1)(1;2). This yields A_h(4). The DFA involution (c d)(f g) yields A_h(1)=A_h(4). Subtract from the c-only total to obtain A_h(8), and use the involution to obtain A_h(2)=A_h(8). Thus the exact per-signature counts follow without further conjectures.

## Finite verification and scope

Independent brute DFA classification tested **335,923 raw words** of lengths 0 through 7 and verified both the C/D/X criterion and first-letter signature rule for every word. The closed-form counts were independently checked against the forward nine-state integer-DFA transfer at each h=1,...,32, including all four individual signatures. The all-h statements are proved by finite transition case inspection and combinatorial coefficient identities; the finite tests are a check, not the extrapolation basis.

At H11 the total low candidate count is 15,233,900, split exactly as
```
A_11(1)=A_11(4)=3,259,420
A_11(2)=A_11(8)=4,357,530.
```
At H14 these counts are 377,182,130; 523,806,700; 377,182,130; 523,806,700 respectively.

**Implementation impact:** candidate-list cardinality and per-signature coverage can be computed exactly by finite sums without enumerating keys or operation words. This does **not** solve the ordered signed X6 prefix-union optimization: distinct words and signatures still need their actual native microstep paths for a cost lower bound/witness.

Next: use the closed form as a strict completeness invariant for EC49FFV/FFW suffix-pruned trie construction, benchmark an H11 instance and investigate an 86-edge exact optimum against the proven upper construction. Preserve the original 22-demand target independently.

## Theorem: exact complete-key-resolved formulas (stronger than global generating functions)

Fix h and a positive legal complete BRC key K=(x,y,z). Write
```
a=z-1, e=z, m=x+y-h-1, f=h+1-y-2z, g=h+1-x,
```
where a,e,m,f,g are all nonnegative integers and a+e+m+f+g=h.
If m=0, the key has **no** low-signature words because every word lacks both c and d.
If m>=1, exactly **two** c/d quota splits can yield a low signature:
```
(c,d)=(m,0) or (0,m).
```
Any split with both c and d positive necessarily ends in the absorbing DFA state 8; this follows directly from the four-region theorem above. Each viable split has
```
P = h!/(a! e! m! f! g!)
```
words, and every word in either split has a low terminal signature. The exact **per-key signature counts** are
```
A_{h,K}(1) = P*(m+g)/h;
A_{h,K}(2) = P*(a+e+f)/h;
A_{h,K}(4) = P*(m+f)/h;
A_{h,K}(8) = P*(a+e+g)/h.
```
The four counts are integers and sum to 2P. Proof: the first-letter signature rule in the previous section partitions the c-only words into first letter c/f versus a/e/g, and the d-only words into d/g versus a/e/f. Among all permutations with fixed quotas, exactly `n_j/h` start with letter j. Summing those exact multinomial counts yields the four expressions. The BRC word-to-key bijection ensures they are counts at the **specified** key, not summed across keys.

Furthermore the number of positive admissible keys, and the number of keys supporting any low signature, are respectively:
```
K_pos(h) = sum_{z=1}^{floor((h+1)/2)} ( binom(h-2z+3,2) - 1 )
K_low(h) = sum_{z=1}^{floor(h/2)} binom(h-2z+2,2).
```
Proof: the equation `m+f+g=h-2z+1`, with m,f,g>=0 and m+g>=1, counts all legal positive keys. For keys with m>=1, put `m'=m-1` and count nonnegative triples `m'+f+g=h-2z`. Distinct triples give distinct keys by the recovery formula.

Independent exact finite verification: for every positive legal key at h=3,...,14, the above four per-key formulas agree with the original DFA's **quota-aware backward suffix DP**, rather than only matching totals. At H10, 120 positive keys contain 415 c/d quota splits, but exactly 95 keys with 190 viable low splits; at H11, 155 keys contain 575 splits, with 125 keys and 250 viable splits; at H14, 301 keys contain 1,337 splits, with 252 keys and 504 viable splits. No DFA search or word permutation enumeration is required to evaluate the closed-form per-key **counts**. Finding minimum signed six-axis prefix cost still requires the original path data and cost algorithm.
