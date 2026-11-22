# T6: universal cancellation of every 17²-denominator with only H0–H3

Date: 2026-11-23 (Asia/Taipei).
Contribution: RESEARCH_DRIVER **EM-DVR-DEBB5E**, original own SID MCP-9b4714dc46b948afa4875a86c89c713c. New finite arithmetic derivation and exact-check implementation during governance-scoped independent work; not a Native Result or formal Review admission. Preserve prior p19 and p17 q14 author/reviewer identities and all previous scientific inputs.

## Exact theorem

Let A and B be finite multisets of positive integer exponents e>=1, each with sum of exponents <=2331. Define H_k(X)=sum_{e in X}(e/(e+1))^k. **If H_k(A)=H_k(B) for k=0,1,2,3, then the multiplicities in A and B are equal at every exponent e=289j-1, 1<=j<=8.** Equivalently, the signed difference after cancellation contains no denominator divisible by 17². This applies to the original T6 problem with equal H0,...,H6 and needs no hypothesis that the 17-primary part separately has equal rational moments.

The range of denominators is 2<=e+1<=2332; since 17³=4913>2332, the denominators with v_17(e+1)>=2 are exactly 289j for j=1,...,8.

## Proof by 17-adic reduction and an explicit finite injection

Set S_k(X)=sum_{e in X}(e+1)^{-k}, S_0=|X|. The binomial triangular identity H_k=sum_{i=0}^k (-1)^i binom(k,i)S_i implies S_1(A)=S_1(B), S_2(A)=S_2(B), S_3(A)=S_3(B) from the four assumed H equalities.

For k=1,2,3, multiply S_k(A)-S_k(B)=0 by 17^(2k) and reduce modulo 17 in the localization Z_(17). Every denominator with v_17<=1 contributes 0 modulo 17; denominator 289j contributes j^(-k). Hence the signed counts c_j=m_A(289j)-m_B(289j) satisfy

    sum_{j=1}^8 c_j j^(-k) == 0 (mod 17),  k=1,2,3.

Every **single-side** vector m=(m_1,...,m_8) of such denominators is a nonnegative integer vector satisfying

    sum_{j=1}^8 (289j-1)m_j <=2331.

There are exactly **67** such vectors. The independently implemented exhaustive recursion and the coefficient sum of the generating function
    sum_{n=0}^{2331} [z^n] product_{j=1}^8 (1-z^(289j-1))^{-1}
both give 67. Define the triple

    Phi(m)=(sum_j m_j j^-1, sum_j m_j j^-2, sum_j m_j j^-3) in (F_17)^3.

On the complete 67-element feasible vector set, **Phi is injective**. A finite exhaustive exact integer check establishes:

| Prefix of Phi | Distinct values | Unordered colliding pairs of different profiles |
|---|---:|---:|
| k=1 | 17 | 101 |
| k=1,2 | 63 | 4 |
| k=1,2,3 | **67** | **0** |

All modular inverses are computed exactly modulo 17. Multiplicities are enumerated without an artificial per-name cap beyond the original **per-side mass** bound. Therefore Phi(m_A)=Phi(m_B) implies m_A=m_B. Thus c_j=0 for j=1,...,8, proving the theorem.

A concrete two-coordinate collision, showing why the third congruence is useful for this finite proof, is the empty profile and m_1=2,m_2=1,m_3=1 (mass 2*288+577+866=2019); both have first two residues (0,0), but their third residues are 0 and 12 modulo17. This is a limitation of the two-coordinate *filter*, not an assertion that H0–H2 alone permits a full collision.

## Reproduction, scope and continuation

Independent C++17 witness: [T6_P17_SQUARED_CANCELLATION_67_PROFILE_EXACT_CHECK_20261123.cpp](https://github.com/awdawmip/enterprise-math/blob/325747d5661105943c2001abf32057e83ccf5fa5/research_checks/T6_P17_SQUARED_CANCELLATION_67_PROFILE_EXACT_CHECK_20261123.cpp). Locally compiled with g++ -std=c++17 -Wall -Wextra -O2, executed successfully with outputs: 67 feasible profiles, 67 DP count, and signature/duplicate counts 17/101, 63/4, 67/0. Code output and exact source file must be kept as evidence; GitHub publication requires its own remote readback.

**Scientific effect:** the whole T6 search can cancel every 17²-denominator across opposite signs before analyzing one-power maximal-p17 cases. The existing one-power q14 split(7,7) exact H012 exclusion and independent audit retain their original author EM-X6-FB6990 and historical q14 roster author EM-EMF6D046-5A2844. The separate maximal-p19 results and native operational status remain distinct. This lemma removes the higher 17-valuation branch only; other maximal-p17 one-power order splits, lower prime layers, and the global T6=2332 decision still require their own actual evidence.

Formal status at this event: new exact arithmetic lemma/checker one; Native Review accepted 0, Result accepted 0, formal Task completed 0, parent objective completed 0. No CLAIM/owner change, no new identity, no scheduler changes.
