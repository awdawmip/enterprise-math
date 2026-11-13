# R749SND: the exact 7/23 Walsh diagonal transition and calibrated continuation

Date: 2026-11-13 (Asia/Shanghai). Status: author-side exact proof and complete rational vertex certificate; independent scientific review pending.

Lineage: R749SMX through R749SNC. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is the auxiliary Walsh signed-source observation model, not an asserted native X6/V29/V39 event realization.

## Setup and theorem

Let G=F_2^4, chi_m(x)=(-1)^(popcount(m AND x)), and B={3,5,6,7,9,10,11,12,13,14}. Set retained Walsh moments m_3=m_12=p and the other eight B moments to zero. Let A=chi_3, D=chi_12, P=chi_1 and Q=chi_4. The entire compatible source fibre is

\[
\mu_{p,h,u,v,w,z}(A,D,P,Q)
=\frac{1+p(A+D)+hAD+uP+vAP+wQ+zDQ}{16}\ge0.
\]

For total-variation distance TV define the unrestricted and calibrated minimax radii respectively by

\[
\rho(p)=\min_{q\in\Delta(G)}\max_{\mu\in F_p}TV(q,\mu),\qquad
\rho^{cal}(p)=\min_{q\in F_p}\max_{\mu\in F_p}TV(q,\mu).
\]

**Exact theorem.** For every real p in [3/10,1/3],

\[
\boxed{\rho(p)=
\begin{cases}2/5,&3/10\le p\le7/23,\\
23(1+p)/75,&7/23\le p\le1/3,
\end{cases}
\quad \rho^{cal}(p)=\frac{1+p}{3}.}
\]

Explicit minimax predictors on the two unrestricted pieces are

\[
q^I_p=\frac{1+(3p-2/5)(A+D)+(1/5)AD}{16}
\quad (3/10\le p\le7/23),
\]

\[
q^{II}_p=\frac{1+[(4+29p)/25](A+D)+[(29-46p)/75]AD}{16}
\quad (7/23\le p\le1/3).
\]

The calibrated minimax predictor throughout [3/10,1/3] is

\[
q^{cal}_p=\frac{1+p(A+D)+[(1-2p)/3]AD}{16}.
\]

At p=7/23, 23(1+p)/75=2/5. At p=1/3, 23(1+p)/75=92/225, recovering the R749SMY exact point. R749SNC had proved a particular predictor through p=3/10; its loss of optimality there does **not** end the minimax plateau. The plateau continues to the *new* exact transition 7/23.

## Proof: symmetrization and lower bounds

The source fibre is invariant under independent flips P↦-P, Q↦-Q and interchange (A,P)↔(D,Q). Averaging any prediction distribution over these transformations cannot increase worst-case TV. Hence an unrestricted minimax center can be chosen as

\[
q_{\tau,\eta}=\frac{1+\tau(A+D)+\eta AD}{16}.
\]

A calibrated center imposes tau=p. All displayed lower bounds therefore apply to the original optimization, not merely a restricted candidate.

Define compatible source laws

\[
\mu_{AD}=\frac{1+p(A+D)+AD}{16},
\quad
\mu_E=\frac{1+p(A+D)-pAD-2pQ+(p-1)DQ}{16},
\]

\[
\mu_C=\frac{1+p(A+D)+[(1-2p)/3]AD
-[(1+p)/3](P+AP+Q+DQ)}{16}.
\]

Their atom masses are affine in p. The exact attached checker verifies each is normalized and nonnegative at p=3/10, 7/23, and 1/3; endpoint affinity proves feasibility throughout both respective intervals. For p≤1/3, mu_AD is supported on AD=1 and mu_E on the event {DQ=-1} union {A=1,D=-1}. They give for any tau,eta

\[
TV(q_{\tau,\eta},\mu_{AD})\ge\frac{1-\eta}{2},\qquad
TV(q_{\tau,\eta},\mu_E)\ge\frac{3+\eta}{8}.
\]

Their maximum is always ≥2/5. This proves the first piece's lower bound.

For the *second* piece, identify x as the standard integer 0,...,15 in F_2^4. Use fixed witness events

\[
T_{AD}=\{1,2,4,7,8,11,13,14\},
\quad T_E=\{0,1,2,3,5,6,9,10\},
\quad T_C=\{0,1,2,3,4,8,12\}.
\]

The signed event inequalities TV(q,mu)≥q(T)-mu(T) give the following affine expressions exactly, for every feasible tau,eta:

\[
\begin{aligned}
L_{AD}&=(1-\eta)/2,\\
L_E&=(1+3p-\tau+\eta)/4,\\
L_C&=(13-8p+18\tau-3\eta)/48.
\end{aligned}
\]

The nonnegative weights 1/5, 12/25, 8/25 sum to one and eliminate tau and eta:

\[
\boxed{\tfrac15 L_{AD}+\tfrac{12}{25}L_E+\tfrac8{25}L_C
=\tfrac{23(1+p)}{75}.}
\]

Thus the second-piece lower bound holds for every real p in [7/23,1/3].

For calibrated q, the events AD=1 and
H={D=1,Q=-1} union {A=1,D=-1}
give (1-eta)/2 and (1+2p+eta)/4. The maximum of these affine lower bounds is at least (1+p)/3, with equality at eta=(1-2p)/3. This holds throughout [3/10,1/3].

## Exact upper certificate: all real parameters

For each interval [a,b], form the six-dimensional bounded full-dimensional polytope in (p,h,u,v,w,z) defined by all sixteen numerator inequalities for mu≥0 and a≤p≤b. It is bounded because each Walsh coefficient is a moment of a probability law. It has a strictly feasible point with p interior and h=u=v=w=z=0.

Every vertex has six independent active facets, hence appears among all C(18,6)=18,564 six-facet subsets. The companion Python program uses exact integer Bareiss elimination and Fraction back-substitution to enumerate all such subsets, test every candidate against all 18 inequalities, deduplicate vertices and evaluate all 16 coordinates of each source and candidate predictor in exact arithmetic.

| p interval | Nonsingular bases | Feasible bases | Unique vertices | Vertices at endpoints | Unrestricted / calibrated violations |
|---|---:|---:|---:|---|---:|
| [3/10,7/23] | 10,848 | 384 | 106 | 53 + 53 | 0 / 0 |
| [7/23,1/3] | 10,848 | 552 | 90 | 53 + 37 | 0 / 0 |

For each proposed affine center and affine bound, TV(mu,q_p)-bound(p) is convex in the six joint variables. Its maximum on a bounded polytope occurs at a vertex. The exhaustive exact nonnegative slacks at all vertices establish the upper bounds for every real p in both intervals, completing the proof.

## Research frontier

Combining R749SNB and R749SNC gives the complete diagonal unrestricted radius from p=0 through p=1/3, with actual transitions 1/5 and 7/23. The calibrated radius equals (1-p)/2 up to p=1/5 and (1+p)/3 from p=1/5 through p=1/3.

Next: determine the first exact unrestricted segment above p=1/3, then compare off-diagonal fibres t≠s and test future-observer composition. The frozen scientific scope and the absence of native X6/V29/V39 correspondence are preserved.

Files: R749SND_DIAGONAL_SECOND_PLATEAU_EXACT_CHECK.py and R749SND_DIAGONAL_SECOND_PLATEAU_RESULTS.json.