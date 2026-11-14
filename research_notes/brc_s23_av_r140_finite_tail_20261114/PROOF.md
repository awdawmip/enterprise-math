# R140 — Exact finite-domain eventual saturation, and the length-4 exception

Date: 2026-11-14 (Asia/Shanghai). Status: AUTHOR-SIDE PROOF / EXACT FINITE CERTIFICATE / NOT_REVIEWED.
Scientific input remains frozen at \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Scope: external one-parameter tied-phase S23 observer, not a native X6 update.
Predecessors: R137B Farey-gap language, R138 exact modular predicate, R139 exact per-gap tail cutoff, R139B extremal-word last absence.
This note preserves the original R139B historical text and explicitly repairs its finite-range extrapolation at m=4.

## Definitions

For integers m>=1, K>=2, and real 0<theta<1, put L=K-1 and

\[
S^{(K)}_i(\theta)=\lfloor(L+i+1)\theta\rfloor-\lfloor(L+i)\theta\rfloor,\quad i=0,\ldots,m-1.
\]

Let V(K,m) be its set of length-m binary words, and W_m the full finite Sturmian language. Define the eventual (permanent) complete-language threshold

\[
T(m)=\min\{t\ge2:\ \forall K\in\mathbb Z,\ K\ge t\implies V(K,m)=W_m\}.
\]

For m>=4 define
\[
E(m)=(m-2)\lfloor(m-1)/2\rfloor+1.
\]

## R140.1 — A previously missed exception

The formula T(m)=E(m) **fails at m=4**. In fact T(4)=4, whereas E(4)=3.

At K=3 the word 1000 is absent. If its first bit were 1, then floor(3theta)>floor(2theta). The only possible slope ranges are [1/3,1/2) (where floor(3theta)=1) and [2/3,1) (where floor(3theta)=2). In either interval floor(6theta)>floor(3theta), so at least one of the next three bits is 1. Thus 1000 is impossible at K=3. The complemented word 0111 is also absent.

For m=4,K=4, the complete Farey-gap certificate below finds all F_4=14 words; the same R139 gap-cutoff argument certifies all later K. Hence T(4)=4. Independent exact chronological rational-atom enumeration obtains 12 words at K=3 and 14 at K=4.

This corrects R139B's sentence claiming equality with E(m) for every m=4,...,22. The extremal-word theorem and its lower bound remain intact: E(4)=3 is a valid lower bound, merely not sharp.

## R140.2 — A finite-domain theorem

**Theorem (certified finite interval).** For every integer 5<=m<=64,
\[
\boxed{T(m)=(m-2)\lfloor(m-1)/2\rfloor+1.}
\]
For m=4, \(\boxed{T(4)=4}\).

The statement is a finite-domain exact-arithmetic theorem, conditional only on the stated Farey-gap correspondence and the published R139/R139B predecessor lemmas (all presently author-side/not independently reviewed). The numerical interval is not an asymptotic conjecture.

### Completeness mechanism

Enumerate the neighboring Farey fractions a/b<c/d of order m and each consecutive intercept gap g in that slope cell. Each carries a word W(g), cut metadata (p,j;q,k), and
\[
D_g=jbc-kad+(q-p)bd,\qquad B_g=bd-D_g.
\]
R138 proves that at coefficient K the gap is feasible exactly when
\[
K-1+D_g>d\Bigl(b-(((K-1+k)a)\bmod b)\Bigr).
\]
R139 proves that the **individual** gap is feasible for every K>=
\[
T_g=\max(2,B_g+2).
\]

For each word w set \(U_w=\min_{g:W(g)=w}T_g\), and \(U_{\rm rep}=\max_w U_w\).
For K>=U_rep every word has a permanently feasible selected gap, so V(K,m)=W_m.

For a proposed threshold C(m) define the *critical words*
\[
\mathcal C_m=\{w\in W_m:U_w>C(m)\}.
\]
All noncritical words are already guaranteed at every K>=C(m). Thus the remaining universal tail condition reduces **exactly** to the finite list
\[
\forall w\in\mathcal C_m,\quad
\forall K\in\{C(m),\ldots,U_{\rm rep}(m)-1\},\quad
\exists g:W(g)=w\text{ with the modular predicate true}. \tag{*}
\]
No inference from random sampling is used here: (*) checks *every* word–coefficient pair left after a mathematically justified permanent-gap reduction.

Take C(4)=4, C(m)=E(m) for 5<=m<=64. The exact certificate in check_r140.py verifies (*), with the original integer floor observations rechecked on explicit rational witness points. It independently checks the number of words against
\[
F_m=1+\sum_{q=1}^{m}(m+1-q)\varphi(q).
\]
R139B proves that the extremal word \(10^{m-2}1\) is absent at K=E(m)-1 for all m>=5. The length-4 argument above proves the separate sharp lower bound. Therefore these C(m) are the exact eventual thresholds for every specified m.

### Exact witness reconstruction

For each feasible g and K, let
\[
N=\left\lfloor (L+k)a/b-q\right\rfloor+1.
\]
The strict feasibility inequality gives
\[
(L+k)a/b-q<N<(L+j)c/d-p.
\]
Choose \(\theta\) as the rational midpoint of the nonempty open interval
\[
\left(\max(a/b,(N+p)/(L+j)),\ 
       \min(c/d,(N+q)/(L+k))\right).
\]
This theta produces the stored word under the original floor-difference definition. The program uses Python integers and exact Fraction arithmetic only.

## Exact validation at m=4,...,64

The checked coverage consists of:
- 61 consecutive integer lengths, all m=4,...,64.
- 1,370,516 Farey intercept gap records and 466,488 distinct word records summed over these lengths.
- 20,038 critical-word records (summed over lengths).
- 24,650,158 *every* critical word–coefficient pairs in the required integer intervals.
- 80,132 independently reconstructed exact rational witnesses, checked against the original floor differences.
- 31,716,825 exact modular predicate evaluations, including rational-interval crosschecks.
- Output marker \`R140_FINITE_EVENTUAL_TAIL_PASS\`.

Representative thresholds:
| m | F_m | C(m)=T(m) | U_rep | Critical words |
|---:|---:|---:|---:|---:|
| 4 | 14 | 4 | 5 | 4 |
| 5 | 24 | 7 | 10 | 8 |
| 7 | 54 | 16 | 26 | 8 |
| 10 | 136 | 33 | 65 | 14 |
| 20 | 944 | 163 | 325 | 64 |
| 30 | 3018 | 393 | 785 | 160 |
| 40 | 6980 | 723 | 1445 | 326 |
| 50 | 13454 | 1153 | 2305 | 574 |
| 56 | 18776 | 1459 | 2917 | 806 |
| 64 | 27834 | 1923 | 3845 | 1150 |

The complete 61-row statistics are generated in \`r140_verification_m64.json\`; the executable complete verifier is \`check_r140.py\`. A separate direct rational-atom scan of the raw observer for m=4,K=3 and K=4 confirmed the exception (12 and 14 attainable words).

## Remaining mathematics

1. Decide whether T(m)=E(m) for every m>=5, without an upper bound on m; current author-side proof covers only 5<=m<=64.
2. Explain the strong reduction from all F_m words to the relatively few critical words through intrinsic Sturmian/Farey geometry, and seek a symbolic tail-cover theorem.
3. Investigate whether the observed closed form U_rep(m)=(m-2)^2+1 for m>=4 holds universally; finite evidence is separate.
4. Keep any later native-X6 transfer typed and subject to separate observer-preservation proofs. No native task CLAIM or mathematical acceptance is inferred from this note.
