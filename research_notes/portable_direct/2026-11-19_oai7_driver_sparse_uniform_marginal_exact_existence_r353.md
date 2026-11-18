# OAI7 r353 — Exact existence of a sparse fully uniform-marginal minimax sampler

Date: 2026-11-19. Author-side finite mathematical theorem, logically proved using a nonempty rational polytope and an extreme-point support bound. Extends pinned r347–r352; shares their Driver scientific context and retains all original OAI7 contributor provenance. This is not a Native Result review or Task admission.

## Theorem: ≤490 rows, exact coverage optimum and exactly uniform position marginals

Set \(G=\mathbb F_{29}\). For an ordered random five-tuple \(H=(H_1,\ldots,H_5)\) with distinct components, let \(C=\{H_1,\ldots,H_5\}\) and the fixed-test failure probability be
\[
q(H)=\max_{K\subset G,\ |K|=4}
\Pr\{|K-C|\le16\}.
\]
The known exact unrestricted minimax is \(v=2024467747/3324255613\). There exists an **exactly specified finite rational probability distribution** (a vertex of the explicit rational feasibility polytope below) such that:
\[
\boxed{q(H)=v},\qquad
\boxed{\Pr\{H_\ell=a\}=1/29\quad(\ell=1,\ldots,5;\ a\in G)},
\]
\[
\boxed{350\le |\operatorname{supp}(H)|\le490},\qquad
\boxed{H(H)\le\log_2 490
=8.936637939002571\ldots\ {\rm bits}.}
\]
The distribution needs no independent random ordering variable: every sampled row is deterministically assigned an ordered tuple. The exact minimax and all five uniform-position marginals hold simultaneously. Relative to r352's explicit translation-invariant realization (entropy 12.727726619437224 bits), this establishes that an admissible, generally non-translation-invariant exact realization exists with entropy at most **8.936638 bits**, saving at least **3.79108868 bits**. It lies within at most **1.066892315 bits** of r351's unconditional set-entropy lower bound 7.869745624309653 bits.

## Rational polytope and proof

Let \(x=1,\ldots,350\) index r350's unique loss-profile representative five-sets \(W_x\). Their **exact rational** masses \(p_x>0\) are fixed by r351; they sum to 1. Choose once and for all any deterministic ordering \((w_{x,1},\ldots,w_{x,5})\) of each \(W_x\). These 350 sets are pairwise translation-inequivalent.

For each \(x\) and \(t\in G\), introduce \(z_{x,t}\ge0\) subject to the **495 explicit rational equations**
\[
\sum_{t\in G} z_{x,t}=p_x
\qquad(x=1,\ldots,350),                                      \tag{1}
\]
\[
\sum_{x=1}^{350}\ \sum_{t:\,w_{x,\ell}+t=a}z_{x,t}
=\frac1{29}
\qquad(\ell=1,\ldots,5,\ a\in G).                            \tag{2}
\]
There are 350·29=10,150 variables. The polytope is **nonempty**: \(z_{x,t}=p_x/29\) is the exact feasible r352 uniformly translated law. It is bounded, since (1) fixes every row-profile mass. Every coefficient of its constraint matrix is an integer 0 or 1, and every right-hand side is rational.

For each position \(\ell\), summing its 29 equations (2) reproduces \(\sum_xp_x=1\), already implied by (1). Hence the matrix rank is at most \(350+5(29-1)=490\). Any bounded nonempty polytope in the standard form \(Az=b,z\ge0\) has a vertex whose number of positive variables is at most \(\operatorname{rank}(A)\le490\): otherwise the corresponding columns are dependent, and one can perturb in both signs while retaining feasibility, contradicting extremality. Because \(A,b\) are rational, such a vertex can be chosen rational.

Sample a positive pair \((x,t)\) with probability \(z_{x,t}\) at that vertex, then output the deterministic tuple \(H_\ell=w_{x,\ell}+t\). Equations (2) prove exact uniformity. Equations (1) preserve all loss-profile masses; the indicator \(\mathbf1\{|K-(W_x+t)|\le16\}\) is independent of \(t\), so the entire fixed-test failure vector equals r350's exact-optimal one. Distinct \((x,t)\) give distinct underlying sets because the \(W_x\) are pairwise translation-inequivalent with orbit size 29. Therefore the number of positive variables equals the support size of \(H\). All \(p_x>0\) force at least one pair for every profile, giving support≥350. The entropy of a probability distribution supported on at most 490 outcomes is at most \(\log_2 490\). QED.

The construction is **exact finite existence**, not an assertion that a particular floating-point LP output is already a certified rational vertex. An explicit vertex can be recovered by rational simplex/pivoting on the displayed nonempty rational polytope.

## Reproducible numerical exploration (not used as proof)

Using the pinned r350 set/profile enumerator, sorted order for each \(W_x\), and the 495-by-10,150 sparse 0/1 matrix of (1)–(2), a SciPy/HiGHS run with a seeded generic linear objective found an approximate basic feasible solution with **490 positive variables**, estimated joint entropy **8.320216738434128 bits**, and maximum equality residual **7.91×10^-16**. These are numerical exploration facts; the exact certified theorem above is \(H\le\log_2 490\). Extracting the candidate's rational basic solution with an exact nonnegativity/equality certificate would sharpen the upper bound.

## Evidence scope and contribution attribution

This is an **external finite \(\mathbb F_{29}\) model**. The full loss-profile distribution is fixed by r351; the new polytope changes the chosen translation conditionally on the profile to attain marginal uniformity at low support. Its quotient identifies states only for the exact declared finite test indicators and does not erase native signed/path/provenance structures or certify an X6 Link/Port transfer.

Pinned parents: r347@12bd331ea2aef70cc844682db432a623b235e726, r350@2737a8ea300816066714ef0ff8d72b62c6df2e46, r351@10ac54cc216860ddfd0ce62fe82b229318482573, r352@b9890c5cccd0a2e0176a19759b850bf997ecd8b3; also r348/r349 and original OAI7 research by EM-EMF6D046-5A2844. Task RS-OAI7-028-C-20261007-6F2A81; immutable TP2-96FAC49786245691AE19. No Native Review, Source/Activity event, Task completion or mother-objective closure has occurred as a result of this note.