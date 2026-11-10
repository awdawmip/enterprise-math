# R5 — Exact physical realization of all 210 minimal invisible Blackwell branch circuits

Date: 2026-11-11 (Asia/Shanghai). Follow-up to RESEARCH.md in this same branch, which proves the six-edge minimum and the 210-circuit classification. This addendum **solves its previously open physical-realizability question** for the frozen seven-ratio P/Q–BRC auxiliary observer, using the original physical parameter map. Scientific source pins remain global \`a01383f825ef9d43b4b754254303298c64041568\` and EM \`86149263e38c22292c9def1e0f69092efa1be77e\`.

## Theorem — an exact physically lawful 15-dimensional transfer fiber

There exists a single **rational** 14-variable physical source/target pair \((x,y)\) satisfying all **five original physical equalities**, all **26 original physical capacity inequalities**, and an exact coupling \(E^0\) with **every one of the original 30 allowed arc masses strictly positive**, satisfying all **21 original Blackwell marginal/martingale equations**.

The exact 14 physical coordinates, 30 coupling masses, and their guaranteed minimum
\[
m=\min_{(i,j)\in D}E^0_{ij}=\boxed{\frac{196521}{33975844}}>0
\]
are fully recorded, in the original \((g,a,b,u,v,w,z)_x,(g,a,b,u,v,w,z)_y\) and frozen ordered-arc convention, in **WITNESS.txt**. The adjacent **VERIFY_ALL_210.py** independently rebuilds the original mass map, two clock readings, 13 capacities per physical state, 21 coupling equations and 30 allowed columns, and exactly checks every stated equality and inequality with rational arithmetic.

Let \(C\) be the original 21-by-30 linear observer and \(q=q(x,y)\). From the companion proof, \(\operatorname{rank}C=15\), so \(\dim\ker C=15\). Because \(E^0\) is strictly positive on **all** arcs,
\[
\boxed{(E^0+\ker C)\cap\mathbb R_{>0}^{30}}
\]
is a nonempty **15-dimensional relatively open** set of fully lawful nonnegative couplings **for this same fixed physical pair** \((x,y)\) and the same 21-dimensional readout \(q\). Indeed for any \(\Delta\in\ker C\) with \(\|\Delta\|_\infty<m\), all \(E^0+\Delta\) arc masses remain positive and \(C(E^0+\Delta)=q\). The original physical constraints remain satisfied because their variables \((x,y)\) are unchanged.

Moreover **all 210 minimal six-arc signed circuits** from the companion exact classification are realized as actual physical coupling freedoms at this one pair. For arbitrary different sources \(j,k\in\{1,2,3,5\}\) and distinct targets \(a,b,c\in\{0,\ldots,6\}\), define the six-nonzero-entry vector
\[
H_{aj}=r_b-r_c,\ H_{bj}=r_c-r_a,\ H_{cj}=r_a-r_b,\quad
H_{ik}=-H_{ij}\quad(i=a,b,c).
\]
Then \(CH=0\), and with the same explicit rational amplitude for every pattern,
\[
\boxed{\epsilon=\frac{m}{4}=\frac{196521}{135903376}},
\qquad
E^\pm=E^0\pm\epsilon H,
\]
both \(E^\pm\) satisfy the original **five+26 physical constraints**, original **21 coupling equations**, and strict positivity on all 30 arcs. The bound follows from
\(\|H\|_\infty\le r_6-r_0=9/5\), so
\(\epsilon\|H\|_\infty\le9m/20<m\). Each pair has **different port-resolved branch masses** but exactly the same physical parameters and observer readout.

Thus the minimum invisible residual support **six** is globally sharp **inside the physical feasible model**, and its entire 210-pattern minimal circuit list is physically realizable on a common interior coupling fiber. At the observer-only level, RESEARCH.md first exhibited a six-arc positive pair; the current witness provides the stronger original-physical realization, with 30 positive base arcs and 15 independent hidden real degrees of freedom.

## Exact verification and discovery provenance

The submitted rational witness arose from a numerical linear-programming search for a common positive margin across the original 30 arcs, followed by an **exact rational reconstruction** of a full-rank active-set linear system. The numerical search is discovery only; the proof rests on the explicit rational witness, the original analytic linear expressions, the previous minimal-circuit lemma, and the exact independent verification. The checker actually executed with Python Fraction and SymPy and produced **EXACT_PHYSICAL_OUTPUT.txt**. It verifies all 210 patterns individually at the same physical pair and exact \(\epsilon\).

This is a theorem in the **frozen P/Q–BRC auxiliary Blackwell operator**. The latent 15-dimensional transfer freedom is a mathematically exact branch-provenance residual of the declared observer. Mapping these freedoms into a native X6 dynamical state would require its own typed embedding/readout/preservation analysis.

## Next scientific unit

Determine the **extreme points and minimal support sizes of this fixed-physical-pair 15-dimensional coupling polytope**, and classify which of its 210 circuits connect adjacent feasible vertices. The exact rational interior witness provides an executable common anchor. This is separate from the global five-arc non-diagonal minimum established in PR #2013.

Formal R5 CLAIM, canonical Source scientific Result admission and independent mathematical review are not asserted by this author-side publication.
