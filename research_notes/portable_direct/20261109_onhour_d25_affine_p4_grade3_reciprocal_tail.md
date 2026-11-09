# D25 AF4: exact grade-three reciprocal-tail certificate

2026-11-09 (Asia/Hong_Kong). TASK_RESEARCH / AUTHOR_SIDE_EXACT_DERIVATION_AND_COMPUTATION / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.
Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`; frozen scientific input `c47e13e4aba0e006366f989d6334d443f6333ae3`. Research logical lane `chatgpt-research-onhour-enterprise-math-20260923`. This is a portable author-side continuation of the complete-cutoff AF4 *conjecture*, not the H0/B0 native experiment.

## Exact original observers
For any prime p>3 and 0<=n<p, put
```
A_n=(2n)!(3n)!/((n!)^5 216^n)
C_n=(4n)!/((n!)^4 2304^n)
W_p=sum_{n=0}^{p-1}(6n+1)A_n
V_p=sum_{n=0}^{p-1}(8n+1)C_n
chi_p=(-3/p).
```
All are p-integral rational numbers. Each coefficient has a typed p-adic valuation, respectively
`v_p(A_n)=floor(2n/p)+floor(3n/p)` and `v_p(C_n)=floor(4n/p)`.
The grade-three portions, retained at modulus p^4 but absent at modulus p^3, are
`W_{3,p}=sum_{2p/3<n<p}(6n+1)A_n` and `V_{3,p}=sum_{3p/4<n<p}(8n+1)C_n`.

## Proposition: reciprocal low-grade representation (all p>3)
For integer j with 1<=j<p/3,
\[
 A_{p-j}/p^3\equiv -1/(18j^3 A_j)\pmod p.
\]
For 1<=j<p/4,
\[
 C_{p-j}/p^3\equiv -1/(96j^3 C_j)\pmod p.
\]
Thus the full signed grade-three AF4 channel is the **finite low-index reciprocal sum**
\[
 L_p:=(W_{3,p}-2V_{3,p})/p^3\equiv
 -\sum_{1\le j<p/3}\frac{1-6j}{18j^3 A_j}
 +\sum_{1\le j<p/4}\frac{1-8j}{48j^3 C_j}\pmod p.\tag{G3}
\]
All denominators here are units. Both formulas are specialized consequences of the already proved complementary cubic-product kernel (2026-11-09), now explicitly applied to the **fourth-digit, weighted, complete-cutoff AF4 observer**; the earlier kernel is not claimed as a new theorem.

### Direct proof / sign audit
For k<p^2, let h=floor(k/p), r=k-hp. The elementary factorial block identity is `k!/p^h=(-1)^h h! r! (mod p)` when h<p. Wilson reflection gives `(p-j)!=(-1)^j/(j-1)! (mod p)`. For n=p-j, j<p/3, the factorial valuations of (2n)! and (3n)! are respectively 1 and 2. Their unit parts and Wilson reflection give
\[
 A_{p-j}/p^3\equiv -2\cdot216^{j-1}\frac{(j-1)!^5}{(2j-1)!(3j-1)!}
 =-\frac1{18j^3A_j}\pmod p.
\]
Likewise, j<p/4 makes the numerator (4n)! have valuation three:
\[
 C_{p-j}/p^3\equiv -6\cdot2304^{j-1}\frac{(j-1)!^4}{(4j-1)!}
 =-\frac1{96j^3C_j}\pmod p.
\]
Finally n=p-j changes the **original weights** to 1-6j and 1-8j mod p; replacing high indices by low reciprocals gives (G3), with coefficient +1/48 for the -2V contribution. This explicitly retains the source index, weight, valuation and sign observer.

## Fourth-digit splitting certificate
Let `W_{<=2,p}=W_p-W_{3,p}`, `V_{<=2,p}=V_p-V_{3,p}` as exact rational partial sums, and `E_{<=2,p}=W_{<=2,p}-2V_{<=2,p}+chi_p p`. The equality
\[
 W_p-2V_p+\chi_pp=E_{<=2,p}+p^3L_p\pmod{p^4}
\]
is exact for every prime p>3. Whenever `E_{<=2,p}` is divisible by p^3, the fourth-digit AF4 conjecture is equivalent to the explicit single-field check
\[
 E_{<=2,p}/p^3+L_p\equiv0\pmod p.\tag{AF4-G3}
\]
The divisibility condition is verified separately by full original-binomial arithmetic in the recorded witnesses; it is not assumed globally.

| p | W3/p^3 mod p | V3/p^3 mod p | Lp mod p | E<=2/p^3 mod p | sum mod p |
|---:|---:|---:|---:|---:|---:|
|13|5|6|6|7|0|
|19|4|16|10|9|0|
|37|26|0|26|11|0|
|43|30|21|31|12|0|
|73|10|17|49|24|0|
|109|80|29|22|87|0|
|373|278|119|40|333|0|

At p=373: p^3=51,895,117 and p^4=19,356,878,641. Direct **original full-cutoff** arithmetic yields `W3=14,426,842,526`, `V3=6,175,518,923` mod p^4; hence `(W3-2V3)/p^3=40 mod373`. The low-grade affine residue is `E<=2=17,281,073,961=333 p^3` modulo p^4, and `333+40=373`. For p=13,19: `7+6=13`, `9+10=19`. These witnesses show grade-three tails carry nonzero information for the new p^4 claim, and cannot be discarded using the earlier p^3 grade truncation.

## Scope, provenance and next experiment
This proves the **general p>3 grade-three reflection and finite-field reduction**, and supplies finite exact certificates for the listed primes. It does not prove AF4 universally or substitute for original-class H0/B0 `[X]U mod139129` (#1559).

First discriminating next step: derive and test an *independent* finite-field expression for the lower-grade quotient `E<=2,p/p^3` in the same low-index reciprocal coordinate (G3), preserving the first two p-adic jets, and attempt to prove its equality to `-L_p` in both frozen residue classes. Retain the original complete cutoff and unreviewed status.

Reproducible check: `research_notes/portable_direct/d25_WV_affine_grade3_reciprocal_tail_20261109.py`.
