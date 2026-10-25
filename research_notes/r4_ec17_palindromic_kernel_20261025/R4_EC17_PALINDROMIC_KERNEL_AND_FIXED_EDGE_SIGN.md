# R4-EC17 — Palindromic BRC grade kernel and exact finite-grade sign classification

**2026-10-25 — AUTHOR-SIDE PROOF, exact integer/symbolic verification, NOT native mathematical admission.**
Researcher label EMR4-LOCAL-20261025-EC17 is an explicitly local writer label, not a service-issued identity.

## 0. Scope, frozen inputs, native authority

GLOBAL_KNOWLEDGE_V1 main@7120aa3053ac490626bfc808810021701308a0c3, project Source main@865b82764a5f85d946cd674a0c2ca8f9d9f1d51e. Read both global entry documents, project bootstrap, P000 ACTIVE_LOCKED, ACTIVE worldview, current portable-research protocol, BRC/mathematical research policy, Heartbeat native X6 basis, and applicable Source control authority. Direct mathematical antecedent: R4-EC16 research_notes/r4_ec16_complementary_edge_20261025/R4_EC16_COMPLEMENTARY_EDGE_ASYMMETRY.md at immutable 1b08f7c22f3355092ae27c7f5d28d7e63f08764b.

Actual GitHub account is awdawmip. Native control task read was refused CONTROL_QUOTA; native session_start was refused STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The active owner, formal CLAIM, and service-issued Researcher session are NOT verified. This is an author-side independent unit, not a takeover or an independent Driver review.

The object is an auxiliary positive-weight ordered binary affine BRC, **not** P000 native six-spatial-axis Cell dynamics or heartbeat-time/triadic physics. The observer retains grade, depth, and the predicate that the word avoids literal 00; it discards full affine effect and future-word response. Results are true only for the declared observer and model, subject to inherited EC16 exact input.

## 1. Exact binary BRC and inherited generating function

There are three control states q=0,1,2 and orientation e in {-1,+1}. Each input a in {0,1} has transition (q',eta,b):

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

Here e'=eta*e and signed grade increment is e'*b=e*(1-2a). Start from q=0,e=+1, grade 0. Let j=(n-t)/2 and C[n,j] count length-n paths of grade j without the substring 00; out-of-range entries vanish. R4-EC13–EC16 established the formal rational identity

\[
F(x,u)=\sum_{n,j}C[n,j]x^n u^j
=\frac{(1-ux^2)(1-ux^3)}{\Delta(x,u)},\qquad
\Delta=1-(1+u)x+2u^2x^4-u^3x^6. \tag{1}
\]

Let D[n,k]=C[n,n-k]-C[n,k]. R4-EC16 derived

\[
D(x,u)=\sum_{n,k}D[n,k]x^nu^k
=\frac{u(1-u)x^3(1-ux^2)}{\Delta(x,u)}. \tag{2}
\]

We do not upgrade EC16's author-side truth/admission category.

## 2. Theorem A: positive palindromic kernel; reflection is its first difference

Define

\[
E(x,u)=\frac{1-ux^2}{\Delta(x,u)}
=\sum_{n,j}E[n,j]x^nu^j. \tag{3}
\]

Then for every finite n,j,k:

(a) E[n,j] is a nonnegative integer;

(b) E[n,j]=E[n,n-j] (including extension by zero outside [0,n]);

(c) D[n,k]=E[n-3,k-1]-E[n-3,k-2], with E[m,*]=0 for m<0.

**Proof.** Equation (1) implies E=F/(1-ux^3)=F sum_{h>=0}u^h x^{3h}; F has nonnegative integer path counts, hence so does E. Direct substitution gives Delta(ux,u^{-1})=Delta(x,u) and 1-u^{-1}(ux)^2=1-ux^2. Thus E(ux,u^{-1})=E(x,u), which proves coefficientwise palindromicity. Finally equation (2) is D=ux^3(1-u)E; take coefficients to get (c). All manipulations occur in integer formal power series, not by finite numerical approximation. QED.

**Exact reduction of the open sign problem.** For a fixed n>=3, all noncentral left-half D[n,k]>=0, 1<=k<n/2, if and only if the palindromic row E[n-3,0],...,E[n-3,floor((n-3)/2)] is nondecreasing. Strict positivity corresponds to strict increases. Thus eventual high-grade dominance is equivalent to an ordinary symmetric polynomial unimodality question; it is not established merely by symmetry.

## 3. Theorem B: uniform exact polynomial formula starting at n=2k+1

For every k>=1 there is an explicitly computable polynomial Q_k(n) of exact degree k-1 and leading coefficient 1/(k-1)! such that

\[
\boxed{D[n,k]=Q_k(n)\quad\text{for every integer }n\ge 2k+1.} \tag{4}
\]

This improves R4-EC16's fixed-k eventual polynomial theorem by an exact threshold adjacent to the diagonal.

**Constructive proof.** Set A_j(x)=[u^j]Delta^{-1}=B_j(x)/(1-x)^{j+1}, B_0=1 and B_j=0 for j<0. Coefficient extraction from Delta*sum A_j u^j=1 gives the finite polynomial recurrence

\[
B_j=xB_{j-1}-2x^4(1-x)B_{j-2}+x^6(1-x)^2B_{j-3}. \tag{5}
\]

Inductively deg B_j<=3j: the three terms have degree at most 3j-2, 3j-1, 3j-1, with absent terms omitted. Substitution x=1 gives B_j(1)=1 for all j>=0. From (2),

\[
[u^k]D(x,u)=P_k(x)/(1-x)^k,\quad
P_k=x^3[B_{k-1}-(1+x^2)(1-x)B_{k-2}+x^2(1-x)^2B_{k-3}]. \tag{6}
\]

Thus deg P_k<=3k and P_k(1)=1. Write P_k(x)=sum_{d=0}^{3k}p_{k,d}x^d. When n>=2k+1, n-d+k-1>=0 for all d<=3k. Consequently the **actual** formal coefficient equals

\[
\boxed{Q_k(n)=\sum_{d=0}^{3k}p_{k,d}\binom{n-d+k-1}{k-1}}, \tag{7}
\]

where the ordinary binomial coefficient vanishes when 0<=upper<lower. Each term is a polynomial of degree <=k-1 in n. The leading coefficient is P_k(1)/(k-1)!=1/(k-1)!, so the exact degree is k-1. This argument proves equality for **every** n in the displayed range and never substitutes a forbidden negative upper binomial index. QED.

## 4. Theorem C: exact k=4 and k=5 defect and sign pattern

The constructive recursion yields two explicit polynomial numerator certificates:

\[
\begin{aligned}
P_4(x)&=x^5(3x^6-6x^5+9x^4-6x^3-x^2+3x-1),\\
P_5(x)&=x^6(x^8+x^7+4x^6-18x^5+25x^4-15x^3+x^2+3x-1).
\end{aligned} \tag{8}
\]

Applying (7) gives, **for every integer n in the stated range**,

\[
\boxed{D[n,4]=\frac{(n-13)(n-9)(n-8)}6,\quad n\ge9}, \tag{9}
\]

\[
\boxed{D[n,5]=\frac{(n-15)(n-10)(n^2-25n+148)}{24},\quad n\ge11}. \tag{10}
\]

The formulas provide full sign classifications on the noncentral half-shell. At k=4, D[9,4]=0, D[10,4], D[11,4], D[12,4] are negative, D[13,4]=0 and D[n,4]>0 for all n>=14. At k=5, D[n,5]>0 for n=11,12,13,14; D[15,5]=0; D[n,5]>0 for all n>=16. The quadratic in (10) has roots (25±sqrt(33))/2 in (9,10) and (15,16), establishing its sign without extrapolation. The central equality D[2k,k]=0 is tautological and outside the asserted noncentral half. These exact grades supplement EC16's previously proved k<=3.

## 5. Evidence, explicit limits and next test

The accompanying actually executed R4_EC17_verify.py performs all-integer checks: 8191 raw input words of lengths 0..12; an independent eight-fine-state BRC path-count DP through n=256; separate exact E coefficient recurrence through n=256; checks E symmetry and D=discrete difference for every grade; constructs (5)–(7) for k<=12 and compares all 2k+1<=n<=256. An independent SymPy program R4_EC17_symbolic.py checks E(ux,1/u)=E(x,u), D=ux^3(1-u)E, and the exact k4/k5 polynomials. Both programs passed a clean ZIP-extract run.

In the **finite** region n<=256, 1<=k<n/2, the complete negative cells observed are (7,3,-1), (8,3,-1), (10,4,-1), (11,4,-2), (12,4,-2); the complete zero cells observed are (5,2), (9,3), (9,4), (13,4), (15,5). This is an exhaustive finite statement only. E_m has nondecreasing lower half for 10<=m<=256, but a universal unimodality theorem is **not** proved. In particular we DO NOT infer there are no new exceptional n beyond 256.

No formal Task, CLAIM, independent mathematical review, proof assistant, native X6 evolution or Foundation promotion was performed.

**Next EC18:** Prove universal palindromic unimodality of E_m for all m>=10 via a positivity-preserving graded transducer or a finite invariant cone, or find a certified counterexample. If proved, this would yield D[n,k]>=0 for n>=13 and every noncentral half-grade. Preserve the full provenance/observer distinction; grade-only formulas do not imply original full-affine-effect future-word equivalence.

**BRC-use statement:** REUSE_APPLIED to exact EC16 positive branch counts and eight-state clean-path automaton, not to unexecuted P000-native BRC-Shor dynamics.
