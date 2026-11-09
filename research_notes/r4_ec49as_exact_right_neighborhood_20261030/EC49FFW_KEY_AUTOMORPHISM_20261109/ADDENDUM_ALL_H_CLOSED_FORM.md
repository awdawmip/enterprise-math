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
