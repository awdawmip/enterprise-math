# R5 | Primitive seventh-root cost residual and sharp first 420-phase transition

Date: 2026-11-21. Status: AUTHOR_EXACT_PROOF / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: independent portable work continuing R5's frozen scalar nonadaptive failure-count model; no formal CLAIM/RUN/Result or independent Review asserted.

## Frozen model and provenance

Queries have integer prices \(P=\{214,\dots,314\}\); the 256 labeled hypotheses and their 32,640-pair separation certificate are inherited without recomputation from EXACT_R5_ALL_101_BUDGETS.json, SHA-256 \`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b\`.

The five minimal separating price sets are
\[
S_0=\{214,\dots,218\},\quad S_1=\{214,216,217,218,219,220,221\},\quad
S_2=\{215,\dots,221\},\quad S_3=\{223,\dots,290\},\quad S_4=\{296,\dots,312\}.
\]
For \(m\ge1\), \(F_m(N)\) counts nonnegative price-multiplicity vectors of total weighted cost \(N\) with at least one \(S_j\) having multiplicity sum \(<m\). All estimates below hold for integer \(N\to\infty\), at fixed \(m=1\). The scalar generating function is the exact 31-term inclusion-exclusion rational function.

Verified predecessor (sixth-root result, distinct research branch):
https://github.com/awdawmip/enterprise-math/blob/960c36250c189b416ff9d7daf120cd0c825ce9f3/research_notes/portable_direct/r5_primitive_sixth_exception_20261121/RESEARCH.md

## Theorem — nonzero primitive seventh-root contribution at m=1

Write \(\zeta=e^{2\pi i/7}\) and
\[
P_7=\prod_{j=0}^{12}(224+7j),\qquad A_7=\frac1{7^{14}P_7}.
\]
The sum of the six primitive seventh-root partial-fraction contributions to \(F_1(N)\) has exact leading term
\[
\boxed{\ F_1^{(7)}(N)=\frac{A_7 N^{12}}{12!}
\,(-7,14,7,0,7,-14,-7)_{N\bmod7}+O(N^{11}).\ }
\]
In particular this harmonic is nonzero, and its primitive seventh-root poles have order exactly 13.

### Proof

For \(m=1\), every selected failure event requires all multiplicities on its union \(U_I\) to vanish, so each local polynomial \(H_{I,1}(\zeta)=1\). Across all 31 nonempty subsets \(I\subseteq\{0,\dots,4\}\), precisely the seven nonempty \(I\subseteq\{0,1,2\}\) leave all 13 multiples of 7 among the free prices, namely \(224,231,\dots,308\). Every other intersection has at most 12 such free prices (indeed at most 12, checked by exhaustive set enumeration), so it cannot affect pole order 13.

For \(E_0=P\setminus S_0=\{219,\dots,314\}\), the 13 complete 7-residue blocks and the remaining residues \(2,3,4,5,6\) imply
\[
\prod_{\substack{p\in E_0\\7\nmid p}}(1-\zeta^p)
=7^{13}\prod_{r=2}^6(1-\zeta^r)=\frac{7^{14}}{1-\zeta}.
\]
For \(I\subseteq\{0,1,2\}\), let
\[
R_I(\zeta)=
\frac{\prod_{p\in U_I\setminus S_0}(1-\zeta^p)}
{\prod_{p\in S_0\setminus U_I}(1-\zeta^p)}.
\]
The remaining free multiples of 7 have common leading factor \(P_7^{-1}(1-x/\zeta)^{-13}\).
Exact reduction in \(\mathbb Q[z]/\Phi_7(z)\), \(\Phi_7=1+z+\cdots+z^6\), yields
\[
\sum_{\varnothing\ne I\subseteq\{0,1,2\}}
(-1)^{|I|+1}R_I(z)
=(z+1)(z^2+1)(z^2+2z-1).
\]
The normalized seventh-root numerator, after multiplying the common \(1-z\) factor, is
\[
T(z)=(1-z)\sum_I(-1)^{|I|+1}R_I(z)
=-z^5+2z^4+z^3+2z^2+3z\quad\bmod\Phi_7(z).
\]
This has degree at most 5 and is not identically zero, so it is nonzero at every primitive seventh root. Finally,
\[
\sum_{a=1}^6(\zeta^a)^{j-N}
=\begin{cases}6&j\equiv N\pmod7,\\-1&j\not\equiv N\pmod7,\end{cases}
\]
gives the stated seven-residue trace vector. A pole of order 13 contributes \(N^{12}/12!\) at leading order. This proves the theorem.

## Corollary — sharp precision-dependent minimal cost modulus

There exists a period-60 quasi-polynomial \(Q_{1,60}\) with
\[
F_1(N)=Q_{1,60}(N)+O(N^{12}),
\]
and **60 is the least possible positive period** for such an approximation. There exists a period-420 quasi-polynomial \(Q_{1,420}\) with
\[
\boxed{F_1(N)=Q_{1,420}(N)+O(N^{11}),}
\]
and **420 is the least possible positive period** at this stronger error level.

Indeed exhaustive divisor counting over all 31 event intersections and all \(8\le d\le314\) gives at most 12 free prices divisible by \(d\); orders \(d>314\) supply no pole. Hence all primitive roots of order at least 8 contribute \(O(N^{11})\). The seventh-root term is \(N^{12}\), so it may be absorbed by an \(O(N^{12})\) remainder but not by \(O(N^{11})\). Previously verified nonzero primitive 2-, 3-, 4-, 5-root components at \(m=1\) force their lcm 60 at both levels. The nonzero primitive 7-root Fourier coefficient forces the additional factor 7, giving lcm \((2,3,4,5,7)=420\). Fourier uniqueness of quasi-polynomials rules out a smaller period; collecting the corresponding finite pole principal parts supplies the asserted approximants.

**Precision boundary:** a degree-12 periodic term is allowed in \(O(N^{12})\), and must be retained for error \(O(N^{11})\). This distinction is essential.

## Verification, scientific limits and continuation

Run \`python VERIFY_SEVENTH.py\` (Python 3 + SymPy). Exact integer-modular polynomial reduction computes the seven leading contributions and verifies the closed form. An independently structured local-multiplicity DP evaluates the seven overlap events for each \(m=1,\dots,12\); it finds nonzero primitive-7 leading coefficient in all 12 tested cases. Exhaustive 31-subset, \(8\le d\le314\) pole-count checking gives the bound 12. The script produces \`RESULT_SEVENTH.json\`; all these computations use exact arithmetic.

The all-\(m\) nonvanishing of the seventh-root coefficient remains open; these finite checks do not establish it. The minimum modulus 420 theorem is proved for \(m=1\), not all thresholds. The calculation is an observer-specific scalar rational-counting result and does not assert a native X6 or BRC phase realization; P000 and the ACTIVE residual-fidelity worldview remain unchanged.

**Next question:** derive the all-\(m\) primitive-seventh-root threshold generating function (using the three-event overlap observer), determine its exact zeros, and classify when the 420-period transition occurs. Preserve the existing 60-period and sixth-root results and the frozen R5 input pins. New result: NOT_REVIEWED pending independent mathematical review.
