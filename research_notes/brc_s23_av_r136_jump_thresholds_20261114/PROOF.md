# R136 — Exact jump divisor law, complement symmetry, and saturation thresholds

Date: 2026-11-14 (Asia/Shanghai). Scope: author-side S23 auxiliary mathematics, NOT_REVIEWED. Pinned science: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Predecessor: R135 at 195734abcd97356feb3bc26f9c4a3e0ea5924921. No native X6 event, formal task, CLAIM, or independent review is claimed.

## Definitions and exact floor representation

For integers \(K,m\ge1\), \(0<\theta<1\), and \(0\le i<m\), let

\[
S_i^{(K)}(\theta)=\mathbf1[\{(K+i)\theta\}<\{\theta\}]
=\lfloor(K+i)\theta\rfloor-\lfloor(K+i-1)\theta\rfloor.
\]

Let \(V(K,m)\) be its set of length-\(m\) binary words. Let \(F_m=1+\sum_{q=1}^m(m+1-q)\varphi(q)\) be the classical finite Sturmian-language count. The previously verified R134/R135 identification gives \(V(K,m)\subseteq\) that language and proves all words occur for every \(K\ge B_m\), where \(B_1=2\), \(B_m=m(m-1)+1\) for \(m\ge2\).

Put \(L=K-1\), \(M=\max(1,L)\), \(N=L+m\).

## Theorem R136.1 — Exact chronological event count

For all integers \(K,m\ge1\), the number \(J(K,m)\) of **genuine** jump parameters of the whole vector \(S^{(K)}(\theta)\) on \((0,1)\) is exactly

\[
\boxed{J(K,m)=\sum_{q=2}^{N}\varphi(q)
 \mathbf1\!\left[\left\lfloor\frac Nq\right\rfloor-
                      \left\lfloor\frac{M-1}{q}\right\rfloor\ge1\right].}
\]

At every jump parameter the vector equals its value immediately on the right. Consequently,

\[
|V(K,m)|\le J(K,m)+1
\le1+\sum_{n=M}^{N}(n-1).
\]

**Proof.** For positive \(n\), \(\lfloor n\theta\rfloor\) has its interior jumps precisely at the rationals \(p/n\), \(1\le p<n\); the \(n=0\) term is constant. A reduced \(p/q\in(0,1)\) is a jump of at least one floor in the consecutive index range \(n=L,\dots,L+m\) exactly when \(q\ge2\) divides some positive \(n\in[M,N]\). For each such \(q\) there are \(\varphi(q)\) reduced numerators, giving the displayed count of candidate events.

At \(\theta=p/q\), the right-minus-left floor jump is \(\delta_n=\mathbf1[q\mid n]\) for positive \(n\), \(\delta_0=0\). The jump of word coordinate \(i\) is therefore \(\delta_{L+i+1}-\delta_{L+i}\). Since \(q\ge2\), no two consecutive indices are divisible by \(q\). There is at least one divisible index by the event condition, and because \(m\ge1\) there is at least one nondivisible index. Thus \((\delta_n)_{L\le n\le N}\) is nonconstant, some adjacent difference is nonzero, and every candidate event is a genuine word change.

Every \(\lfloor n\theta\rfloor\) is right-continuous on \((0,1)\); so is the word vector. At each rational event its word is therefore the word of the open interval immediately to the right. There are \(J+1\) chronological intervals and no additional singleton words. Strings may recur, so this is an upper bound on **distinct** words. The final inequality counts individual floor jumps with multiplicity. QED.

## Corollary R136.2 — Stronger necessary bound for saturation

For \(K\ge2\), the sum is

\[
\sum_{n=K-1}^{K+m-1}(n-1)
=(m+1)(K-2)+\frac{m(m+1)}2.
\]

Thus \(|V(K,m)|=F_m\) requires

\[
\boxed{K\ge2+\frac{F_m-1}{m+1}-\frac m2.}
\]

Using the known \(F_m=m^3/\pi^2+O(m^2\log(m+1))\), this entails
\(K\ge m^2/\pi^2-O(m\log(m+1))\).
R135 used \(1+2C\) to accommodate singleton events. Right-continuity rigorously replaces that factor two by one in the same general floor-crossing argument. This is a necessary bound; it does not assert a formula for the exact threshold for arbitrary \(m\).

## Theorem R136.3 — Complement symmetry

For every \(m\ge1\), \(K\ge2\), \(V(K,m)\) is closed under coordinatewise binary complement; in particular its cardinality is even.

**Proof.** If \(\theta\) is irrational, none of \((K+i-1)\theta\) is integral. Thus \(\{(K+i)\theta\}\neq\{\theta\}\). For positive integer \(n\), \(\{n(1-\theta)\}=1-\{n\theta\}\). Each strict comparison reverses, giving \(S_i^{(K)}(1-\theta)=1-S_i^{(K)}(\theta)\) for all \(i\). Every rational-parameter word also occurs at an irrational parameter immediately to its right, by the finite right-continuous event partition established above. Hence the complement pairing covers all words. No positive-length binary word equals its own complement. At \(K=1\) the first coordinate is identically zero, explaining the precise exception. QED.

## R136.4 — Exhaustively certified finite first/eventual thresholds

Define \(K_{\mathrm{first}}(m)\) as the smallest \(K\) with \(|V(K,m)|=F_m\), and \(K_{\mathrm{eventual}}(m)\) as the smallest \(K\) such that all integer \(K'\ge K\) saturate.

For fixed \(m\), R135 guarantees saturation for all \(K\ge B_m\). The companion exact algorithm checks **every** \(1\le K\le B_m\). For each \(K\), it constructs all rational floor cuts \(p/n\) for \(n=M,\dots,N\), \(1\le p<n\), merges equal fractions using exact rational arithmetic, and sweeps all word changes. The initial word immediately right of zero is all zero. At a cut, floor jumps at indices divisible by the reduced denominator \(q\); toggling the associated adjacent difference bits realizes the exact new word. Theorem R136.1 proves there are no additional rational singleton words. Distinct masks are counted and compared to the exact integer \(F_m\). The first saturated index gives \(K_{\mathrm{first}}\), and one plus the largest nonsaturated index below \(B_m\) gives \(K_{\mathrm{eventual}}\). R135 supplies the complete infinite-tail certificate, so these are exact finite determinations.

| m | F_m | first | eventual | B_m |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 4 | 2 | 2 | 3 |
| 3 | 8 | 3 | 3 | 7 |
| 4 | 14 | 4 | 4 | 13 |
| 5 | 24 | 7 | 7 | 21 |
| 6 | 36 | 9 | 9 | 31 |
| 7 | 54 | 11 | 16 | 43 |
| 8 | 76 | 16 | 19 | 57 |
| 9 | 104 | 22 | 29 | 73 |
| 10 | 136 | 25 | 33 | 91 |
| 11 | 178 | 29 | 46 | 111 |
| 12 | 224 | 41 | 51 | 133 |
| 13 | 282 | 46 | 67 | 157 |
| 14 | 346 | 51 | 73 | 183 |
| 15 | 418 | 67 | 92 | 211 |
| 16 | 498 | 73 | 99 | 241 |
| 17 | 594 | 79 | 121 | 273 |
| 18 | 696 | 99 | 129 | 307 |
| 19 | 816 | 106 | 154 | 343 |
| 20 | 944 | 113 | 163 | 381 |

The exact Python Fraction test checked 2,681 pairs \((m,K)\), all \(m=1,\dots,20\), \(K=1,\dots,B_m\). It additionally checked binary-complement closure on all 2,661 pairs with \(K\ge2\), recomputed selected event words independently using direct floors, and performed exhaustive independent event-word recomputation for all \(m\le8\). Result: R136_EXACT_THRESHOLD_SWEEP_PASS. The code and verification summary accompany this proof.

Nonmonotonicity is explicit: for \(m=7\), \(K=11\) is saturated, \(K=15\) is missing two complementary patterns, and every \(K\ge16\) saturates. The verification data preserves reversion indices for all checked \(m\).

## Limits, evidence, next research problem

R136.1–R136.3 are mathematical proofs. R136.4 has an exhaustive, **finite** exact certificate for \(1\le m\le20\), invoking the already proved R135 uniform infinite-tail theorem. The results are for the external one-parameter auxiliary S23 observer under the stated frozen pin and not a native six-dimensional Cell/Link/Port model. Independent mathematical review remains NOT_REVIEWED.

Reproduce with standard Python only: python check_r136.py --limit 20. The verification file includes exact threshold and reversion data.

Next objective: obtain a non-enumerative formula or asymptotic constant for \(K_{\mathrm{first}}(m)\) and \(K_{\mathrm{eventual}}(m)\), using the exact divisor-event count and the complementary pairing to classify missing words in Farey slope/intercept cells. A separate extension could test whether the exact right-continuity jump accounting remains valid for a general signed S23 indicator after its boundary convention is defined.

## Sources

- R135 PROOF.md at immutable commit 195734abcd97356feb3bc26f9c4a3e0ea5924921.
- R134 PROOF.md at immutable commit cf0054d39919605bc026175c9438ff7f6495f600.
- Classical Sturmian factor count: F. Mignosi, *On the Number of Factors of Sturmian Words*, Theoretical Computer Science 82 (1991), 71–84. DOI: 10.1016/0304-3975(91)90172-X. The classical count is not presented as new.