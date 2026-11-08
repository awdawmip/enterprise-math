# PREFIX-592-R6 — The unique cubic BRC observer is one original native phase indicator

Date: 2026-11-08 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_RATIONAL_NATIVE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Scientific freeze: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Native six-action kernel: \`research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py\`, Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.
Direct predecessor: PREFIX-591-R6, immutable source commit \`2ab77962c8d6830a123915364fc8d97aa9e90f73\`.
Researcher provenance: source-issued \`EM-DIRECT-E9247A / TASK_RESEARCH\`, session \`MCP-901bb3e918294503a2dd3167270812a7\`, native activity \`RA-5AD9BBA722554D0755576668\`. A native task CLAIM was not used to obtain this independent scientific result.

## Problem, native scope and exact definitions

The mother question is to preserve complete declared joint BRC observations under the smallest valid all-horizon summary. PREFIX-591 established the graded native rational port-function spaces

\[
\dim W_0=1,\quad \dim W_1=13,\quad \dim W_2=32,\quad \dim W_3=33.
\]

Here the original native model has 48 phases, 96 branch ports \`i=2*phase+bit\`, six original *labeled* actions, the frozen zero root and equal independent action probabilities. Each native edge carries exact original six-axis counts and one gate marker. With cumulative original counts \(R_1,\ldots,R_6,K\), set

\[
T=192K-5R_1+R_2-5R_3+R_4+4R_5+4R_6,\quad
P_0=R_1+R_2,\quad P_1=R_3+R_4.
\]

For every multiindex \(\alpha=(a,b,c)\) with total degree at most three, the observer comprises the initial-port functions \(f_{n,\alpha}(i)=E_i[T_n^aP_{0,n}^bP_{1,n}^c]\) at every integer \(n\ge 0\), and the spaces \(W_d\) are the exact graded weighted-transition-invariant spaces constructed and checked in PREFIX-591. No initial-port distribution or nonzero root is assumed.

## Theorem — explicit phase generator of the entire cubic-only quotient

Let \(s(i)=\lfloor i/2\rfloor\) be the original native phase of port \(i\), and let \(\phi_\star=42\), with exact native phase tuple

\[
\mathrm{PHASES}[42]=(3,-2,4).
\]

Define the original-phase occupancy test

\[
g(i)=\mathbf1_{\{s(i)=42\}}
=\mathbf1_{\{i=84\}}+\mathbf1_{\{i=85\}}.
\]

Then the rational port-observer spaces satisfy the exact direct-sum identity

\[
\boxed{W_3=W_2\oplus\mathbb Q g.}
\]

Consequently the **only additional independent linear statistic of an arbitrary native initial-port law** needed to pass from the complete all-horizon quadratic BRC observer to the complete all-horizon cubic observer is

\[
\boxed{E_\pi[g]=\pi(84)+\pi(85).}
\]

Thus quadratic observations at all lengths require 31 variable linear initial-law coordinates (plus normalization), whereas all cubic-and-below observations require 32 variable coordinates. The old original 96-port dynamics are retained; this is an exact observation-carrier statement.

## Constructive exact proof

Reconstruct the original six-action edge map through the pinned PREFIX-565 kernel and form the 20 exact integer operators \(B_\alpha\) as in PREFIX-591. Its deterministic rational echelon construction gives a 32-dimensional \(W_2\) with pivot ports

\[
(0,2,4,6,7,8,10,12,14,16,18,20,22,24,28,32,34,36,
38,42,46,48,50,52,54,56,60,64,68,72,76,80).
\]

The \(W_3\) construction yields those same 32 pivots together with pivot \(84\), with final normalized new vector exactly \(g\): its 96 entries are zero except for a value of one at each of ports 84 and 85. In particular, \(g\in W_3\). The echelon remainder of \(g\) under the full \(W_2\) basis is \(g\ne0\), proving \(g\notin W_2\).

A native operator witness makes this decomposition directly inspectable. Let \(w_{24}\) be the zero-indexed 25th normalized vector in the deterministic \(W_2\) basis. For \(B_{(0,0,1)}\), which weights each original labeled transition by its first-axis-pair count \(P_1\), exact rational elimination yields

\[
\boxed{\rho_{W_2}\!\left(B_{(0,0,1)}w_{24}\right)=\tfrac34 g.}
\]

Since PREFIX-591 already established exact all-length graded closure and \(\dim W_3=33\), the preceding membership and non-membership establish the theorem for every length and every initial law, not just for sampled depths.

The quotient can also be seen in small unnormalized integer path moments. Let \(m_{n,\alpha}(i)\) be the sum of \(T^aP_0^bP_1^c\) across all \(6^n\) original labeled paths starting at port \(i\) (without the common factor \(6^{-n}\)). For all ten total-degree-three monomials and \(0\le n\le3\), their exact \(W_2\) remainders vanish. At depth four,

\[
\boxed{\begin{aligned}
\rho_{W_2}(m_{4,(2,0,1)})&=-13824g,\\
\rho_{W_2}(m_{4,(2,1,0)})&=\phantom{-}13824g,\\
\rho_{W_2}(m_{4,(3,0,0)})&=\phantom{-}331776g.
\end{aligned}}
\]

All seven other degree-three remainders at depth four are zero. Conditional expectations divide these integer path sums by \(6^4=1296\). This is an exact first-depth witness of the missing cubic direction relative to the already complete *all-horizon* quadratic space.

## Certificate and limits of interpretation

\`PREFIX592_R6_native_cubic_phase_detector_certificate.py\` imports the two published native proofs, reconstructs the rational graded spaces from original BRC actions, checks every vector of the phase indicator, the operator witness, and the complete degree-three finite-depth path recurrence up to depth four. All comparisons are exact integer or rational operations. Independent local reimplementation of the pinned native edge rules and of the PREFIX-591 module returned \`ALL_CHECKS_PASS\`; the deposited certificate uses the published dependencies. Exact result values appear in \`PREFIX592_R6_PHASE_DETECTOR_RESULTS.json\`.

The reduction applies to the declared \((T,P_0,P_1)\) moments through degree three, all lengths, original zero-root kernel and arbitrary initial distributions. It does not replace 96 native ports by 33 physical ports or decide other roots, degree four, or future observables that demand more original information.

Next question: decide whether the phase-indicator generator remains one-dimensional under the eight other frozen roots, and compute the new graded dimension and an explicit native generator, if any, at degree four.
