# R149C — Complement-pair parity and a totient endpoint-flow congruence

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Status: author-side proof, exact finite crosscheck; `NOT_REVIEWED`.
Dependencies: R149.1 exact complement fiber duality and R145/R146C total-mass formulas (their exact original scopes).

**Theorem (all integers m>=1 and K>=2).** Let `W_m` be the complete family of distinct finite Sturmian binary words of length m, `C_w(K)` the R146 integer phase-index multiplicity, and `V(K,m)={w in W_m:C_w(K)>0}`. Then:

1. Every multiplicity class `{w in W_m:C_w(K)=n}` has an **even** number of elements, for each nonnegative integer n.
2. In particular, both `|V(K,m)|` and `S_m(K-1)=sum_{w in W_m}C_w(K)` are even.
3. For any two coefficients `K_1,K_2>=2`, each set of words with any specified ordered pair of multiplicities `(C_w(K_1),C_w(K_2))` has even size. Hence the number of newly appearing words, disappearing words and persistently present words (within a comparison of two K) is even.
4. The R146C exact total-mass increment `m+1+D_m(L)-D_m(L+m+1)` is even for every `L>=1`. Here `D_m(n)=sum_{2<=q<=m,q|n}phi(q)`; an empty sum is zero.

**Proof.** A nonempty binary word has a distinct bitwise complement. The finite Sturmian family is closed under complement by the exact reflected slope support. R149.1 establishes `C_w(K)=C_bar(w)(K)` for every integer K. Thus the complement involution has no fixed point and preserves each single-K multiplicity stratum, as well as every joint multiplicity stratum for several K. All such strata partition into 2-element complement pairs; the claims about cardinalities and sums follow. The increment of the always-even total mass is even, and the R146C identity proves statement 4. QED.

**Independent arithmetic consistency check with R145's totient expression.** R145 states, in the same domain, `S_m(L)=1+sum_{q=2}^{L+m}phi(q)*1_{floor((L+m)/q)-floor((L-1)/q)>=1}`. Every `phi(q)` for `q>2` is even. The block of consecutive integers `[L,L+m]` has at least two elements, hence includes a multiple of 2; the q=2 indicator is 1 and `phi(2)=1`. Consequently `S_m(L)≡1+1≡0 mod 2`. This second deduction does not assume complement pairing, and crosschecks the two antecedent formulas.

**Verification.** Exact enumeration of all `2^m` candidate binary strings for each `m=1,...,12`, filtering by rational slope support, and every `K=2,...,35`: 408 (m,K) cases, both realized-pattern count and total phase mass even, `R149C_COMPLEMENT_PARITY_PASS`.

**Use.** Any candidate one-step disappearance argument must include the complement partner: an odd loss count signals an incorrect count or a changed word universe. The complement pairing reduces independent pattern checks by a factor of two for the same declared observer.

**Next.** For arbitrary m, determine whether the additional, finite-observed endpoint congruence `a+c≡0 (mod gcd(b,d))` is universal. Its proof would turn R149's autocorrelation and reversal results into unconditional theorems.
