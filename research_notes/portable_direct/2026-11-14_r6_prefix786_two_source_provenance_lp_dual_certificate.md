# PREFIX-786 — Exact dual certificates for a correlated two-source observer

Date: 2026-11-14. Status: AUTHOR_PROVED / EXACT_RATIONAL_COMPUTATION / UNREVIEWED / NOT_ADMITTED.
Scientific input pin (preserved, not recalculated): \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Prior provenance: PREFIX-784/785 and Researcher-ID \`EM-DIRECT-E77192\`; Activity \`RA-66BBE259AEE1AD543D9454A3\`.
Mathematical object: an **external scalar affine BRC–Gamma observer model**, not an asserted native X6 Cell/Link/Port map.

## 1. New question

PREFIX-785 proved the sharp \(2/3\) uniform two-sign margin for one shared source \(t\). Here we allow several *correlated provenance-labeled signed sources* while preserving their joint incidence map. Does a finite exact certificate compute the minimum uniform margin, and how does it differ from independent coordinate-error budgets?

For rational \(A,B\in\mathbb Q^n\), \(C\in\mathbb Q^{n\times d}\), \(q>0\) and \(z\in[-1,1]^d\), set
\[
f(q,z)=A-qB+Cz,\qquad
a(q,z)=(f_1,\ldots,f_n,-f_1,\ldots,-f_n).
\]
The two-sign margin is
\[
M(q,z)=\min(\max_j a_j,-\min_j a_j)=\|f(q,z)\|_\infty.
\]
The same \(z\) drives all observation coordinates. The common-source law is part of the model and is not replaced with independent corner bounds.

## 2. General exact primal/dual theorem

**Theorem 786.1.** For any rational data above, the sharp uniform margin
\[
\gamma=\inf_{q>0,z\in[-1,1]^d}\|A-qB+Cz\|_\infty
\]
equals the optimal value of the finite rational linear program
\[
\min r\quad\text{subject to}\quad
q\ge0,\ -1\le z_j\le1,\ 
-r\le A_i-qB_i+(Cz)_i\le r\quad(1\le i\le n).
\]
It also has the exact dual representation
\[
\boxed{\gamma=
\max_{\substack{\lambda\in\mathbb R^n,\ \|\lambda\|_1\le1\\
\lambda^\top B\le0}}
\left(\lambda^\top A-\|C^\top\lambda\|_1\right).}
\]

**Proof.** The objective is continuous in \(q\). Any feasible \(q=0\) can be approached by \(q\downarrow0\), so using \(q\ge0\) does not change the infimum. Introducing the epigraph variable \(r\) gives the displayed rational LP; it is feasible and bounded below by zero, and it has an attained optimal value. Rational linear-programming duality provides a rational optimum for rational input.

For completeness, \(\|v\|_\infty=\max_{\|\lambda\|_1\le1}\lambda^\top v\). The dual ball is convex compact and the primal set \([0,\infty)\times[-1,1]^d\) convex. The minimax theorem for continuous bilinear forms, equivalently LP strong duality, permits interchanging infimum and maximum. For a fixed \(\lambda\),
\[
\inf_{q\ge0}-q\lambda^\top B
=\begin{cases}0,&\lambda^\top B\le0,\\-\infty,&\lambda^\top B>0,\end{cases}
\quad
\min_{z\in[-1,1]^d}\lambda^\top Cz=-\|C^\top\lambda\|_1.
\]
This yields the dual formula. Thus a rational primal point and feasible rational dual \(\lambda\) of equal value give a finite exact optimality certificate. QED.

## 3. New rank-two shared-source exact witness

Choose two genuinely distinct sources \(s,t\in[-1,1]\), and
\[
A=(0,3,1),\quad B=(1,2,3),\quad
C=\begin{pmatrix}1&1\\1&-1\\-1&1\end{pmatrix}.
\]
Hence
\[
f_1=-q+s+t,\quad
f_2=3-2q+s-t,\quad
f_3=1-3q-s+t.
\]

**Theorem 786.2 (sharp two-source margin).** For every \(q>0\) and \(s,t\in[-1,1]\),
\[
\boxed{\max(|f_1|,|f_2|,|f_3|)\ge1/10.}
\]
The lower bound is best possible and has a unique attaining triple
\[
(q,s,t)=(4/5,-3/10,1),
\qquad
f=(-1/10,\ 1/10,\ -1/10).
\]

**Certificate.** Take
\[
\lambda=(-1/2,\,2/5,\,-1/10).
\]
It satisfies \(\|\lambda\|_1=1\), \(\lambda^\top B=0\) and
\[
C^\top\lambda=(0,-1),\qquad
\lambda^\top f(q,s,t)=11/10-t\ge1/10.
\]
By Hölder's inequality, \(\|f\|_\infty\ge\lambda^\top f\ge1/10\), for every admissible real parameter. The proposed triple attains equality. For uniqueness, equality requires \(t=1\) and, since all three \(\lambda_i\ne0\), the three coordinates of \(f\) have signs \((-,+,-)\) and absolute value \(1/10\). Solving \(f_1=-1/10,\ f_2=1/10,\ t=1\) gives precisely \(q=4/5,s=-3/10\), with \(f_3=-1/10\). QED.

This explicit dual cancellation eliminates the two freely varying directions \(q\) and \(s\), while retaining the source bound \(t\le1\). It is a provenance-sensitive invariant rather than a coordinatewise error estimate.

## 4. Exact difference from the independent-box relaxation

Each row of \(Cz\), considered alone, lies in \([-2,2]\). If the three coordinates are allowed independent errors \(e_i\in[-2,2]\), then at \(q=1\)
\[
A-qB=(-1,1,-2),\qquad e=(1,-1,2)
\]
gives \(A-qB+e=0\). Thus the independent coordinate-box observer has **zero** possible uniform two-sign margin, whereas the joint two-source observer has the positive sharp margin \(1/10\). The loss comes from discarding the shared incidence matrix \(C\), not from reducing the magnitude of any individual bound.

**Corollary 786.3 (sharp tolerance for additional measurement error).** Form all six reflected observations \((f_1,f_2,f_3,-f_1,-f_2,-f_3)\) and allow an independent additive measurement error of magnitude at most \(\varepsilon\) on *each of the six readouts*, without changing the underlying shared-source model. For all real \(q>0,s,t\in[-1,1]\) and all such measurement errors, both positive and negative observations exist whenever \(\varepsilon<1/10\), each with magnitude at least \(1/10-\varepsilon\). The strict threshold is sharp: at \(\varepsilon=1/10\), choose the optimizer and cancel all six values exactly. QED, from the largest absolute \(f_i\) and its opposite paired readout.

## 5. Exact verification and scope

Companion \`PREFIX786_R6_TWO_SOURCE_EXACT_LP_CHECK.py\` uses only \`fractions.Fraction\`; it constructs all 11 rational linear inequalities in the four LP variables \((q,s,t,r)\), enumerates all \({11\choose4}=330\) active four-constraint combinations, solves each nonsingular system exactly, and checks global feasibility. There are 19 feasible basic-solution occurrences and the minimum is \(r=1/10\). It also checks the exact primal and dual vectors, the independent-box zero witness, and rational tolerance cases. Output: \`PREFIX786_R6_TWO_SOURCE_EXACT_LP_RESULTS.json\`; validation string \`ALL_CHECKS_PASS PREFIX786 TWO_SOURCE_SHARP_LP_CERTIFICATE\`.

The universal statements follow from the mathematical primal/dual argument and explicit certificates, not from finite tests. No floating-point approximation enters validation. The chosen coefficients are a new illustrative **external scalar** incidence model, not the pinned 189-layer stop-model coefficients. The exact link from native X6 Cell/Link/Port, branch, signed-source and event-time data to any such \(A,B,C\) remains to be established. The original native comparator exclusions remain unchanged. No independent review or Working Truth/Foundation promotion has been performed.

## 6. Next discriminating mathematical unit

Extract a genuine typed native BRC/X6 source-to-corner incidence map (retaining branch identity, sign, timing and admissible joint source constraints), compute its attainable polytope, and run the rational primal/dual certificate *on that verified map*. If its source set is a rational polytope \(P\) rather than a box, replace \(-\|C^\top\lambda\|_1\) with \(\min_{z\in P}\lambda^\top Cz\) and compare the exact joint margin with the independent interval hull. Test whether source-aware observer compression preserves the sufficient joint structure under the intended future operations.