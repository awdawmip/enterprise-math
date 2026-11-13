# BRC N=4 S23 — sixth-order Chernoff sign and local critical shift

Date: 2026-11-03. **AUTHOR_ANALYTIC_PROOF / EXACT_SYMPY_EXECUTED / UNREVIEWED / NOT_ADMITTED**. The proof addresses a prescribed paired-state statistical experiment; it is neither an authenticated native Result nor a new P000 axiom.

## Frozen model and question

Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct predecessor: PR #1765, immutable commit b6d1b1eb9673cc3b8e0d4fdc5479b8e74b698d20, research_notes/brc_n4_s23_fisher_equal_chernoff_phase_reversal_20261103_research1/PROOF.md. Keep scheme (3,31), deleted source 0, the lawful S23 extremal two-state witness, source/branch labels and independent trials, equal prior hypotheses, nonadaptive sampling and specified abstract prices. Fix real \(0<h\le 1/42\), \(s=(1-\beta_E)^2\in(0,1]\), \(\beta_N=0\). Write \(p=1/2+h\) and \(q=1/2-h\).

Full-source trial \(T\) has law \((sp,1-s,sq)\) versus \((sq,1-s,sp)\); the repaired single-event Bernoulli trial \(B\) has success probabilities \(sp\) versus \(sq\). Their stipulated costs are \(c_T=2-s\) and \(c_B=1\), which equalizes local Fisher information per cost at \(h=0\). The Chernoff information for experiment \(X\) is \(C_X=-\log(\min_{0\le t\le 1}\sum_i P_{X,+}(i)^tP_{X,-}(i)^{1-t})\). Define \(F(s,h)=C_T(s,h)/(2-s)-C_B(s,h)\), so that \(F>0\) favors T and \(F<0\) favors B.

## Theorem: sixth-order sign and analytic displacement

Let
\[
A(s)=-\frac{2s(1-s)(9s^2-40s+4)}{9(2-s)^3},\quad
P(s)=270s^5-1485s^4+728s^3+4296s^2-8448s+1264,
\]
\[
B_6(s)=-\frac{4s(1-s)P(s)}{405(2-s)^5},\qquad
s_*=\frac{20-2\sqrt{91}}9.
\]
For every fixed \(s\in(0,1)\), using the *true optimized Chernoff parameter* of B,
\[
\boxed{F(s,h)=A(s)h^4+B_6(s)h^6+O_s(h^8).}
\]
At the previously unresolved fourth-order threshold,
\[
\boxed{B_6(s_*)=\frac{22963736-2413784\sqrt{91}}{3796875}<0.}
\]
Thus for \(s=s_*\), every sufficiently small positive lawful contrast \(h\) favors the Bernoulli repair observer B over T by Chernoff information per stipulated cost.

There exists a neighborhood of \((s_*,0)\) on which the nontrivial equation \(F(s,h)=0\), \(h\ne0\), has exactly one local real-analytic even crossing \(s=s_c(h)\), with
\[
\boxed{s_c(h)=s_*+\kappa h^2+O(h^4),\quad
\kappa=\frac{1946672-162368\sqrt{91}}{2764125}>0.}
\]
For sufficiently small positive \(h\), F is negative immediately below the local crossing and positive immediately above it. This is *local uniqueness near* \(s_*\), not a uniqueness statement across \(s\in(0,1)\) at arbitrary finite h.

## Proof

Put \(u=s/2\), \(v=1-s/2\), \(d=sh\) and \(\delta=2t-1\). For B the exact Chernoff coefficient becomes
\[
Z_B(\delta)=X e^{\delta\alpha}+Y e^{-\delta\gamma},\qquad
X=\sqrt{u^2-d^2},\quad Y=\sqrt{v^2-d^2},
\]
\[
\alpha=\operatorname{atanh}(d/u),\qquad
\gamma=\operatorname{atanh}(d/v).
\]
The unique unconstrained minimum follows from \(Z_B'(\delta)=0\):
\[
\delta_*(s,h)=\frac{\log(Y\gamma/(X\alpha))}{\alpha+\gamma}.
\]
For each fixed \(s\in(0,1)\), \(\delta_*\to0\) as \(h\to0\); hence it is an interior minimizer \(-1<\delta_*<1\) in the required asymptotic neighborhood. It is odd and real-analytic in h around zero, since the vanishing factors of numerator and denominator cancel.

Use the elementary expansions
\[
\log\left(\sqrt{1-x^2}\,\frac{\operatorname{atanh}x}{x}\right)
=-x^2/6-19x^4/180+O(x^6),
\]
\[
\operatorname{atanh}x=x+x^3/3+x^5/5+O(x^7).
\]
Since \(d/u=2h\) and \(d/v=2sh/(2-s)\), the optimizer has
\[
\delta_*(s,h)=a(s)h+b(s)h^3+O_s(h^5),\quad
a=\frac{2(1-s)}{3(2-s)},\quad
b=\frac{16(1-s)(2s^2-4s+9)}{45(2-s)^3}.
\]
To collect the exact coefficient, for a branch \(q=u\) or \(v\), sign \(\sigma=+1\) or \(-1\), let \(r=s/q\) and write
\[
\sqrt{q^2-s^2h^2}\exp(\sigma\delta_*\operatorname{atanh}(sh/q))
=q[1+L_2h^2+L_4h^4+L_6h^6+O(h^8)].
\]
Setting \(e_2=\sigma ar\), \(e_4=\sigma(br+ar^3/3)\), \(e_6=\sigma(br^3/3+ar^5/5)\), multiplication of the square-root and exponential series gives
\[
L_2=e_2-r^2/2,\qquad
L_4=e_4+e_2^2/2-r^2e_2/2-r^4/8,
\]
\[
L_6=e_6+e_2e_4+e_2^3/6
-r^2(e_4+e_2^2/2)/2-r^4e_2/8-r^6/16.
\]
Sum \(q=u,\sigma=+1\) and \(q=v,\sigma=-1\). This yields \(Z_B=1+z_2h^2+z_4h^4+z_6h^6+O(h^8)\), where
\[
z_2=-\frac{2s}{2-s},\quad
z_4=-\frac{2s(31s^2-62s+40)}{9(2-s)^3},
\]
\[
z_6=-\frac{4s(2557s^4-10228s^3+20124s^2-19792s+7744)}{405(2-s)^5}.
\]
The unknown coefficient of \(h^5\) in \(\delta_*\) cancels from the sixth-order sum because the two branches have \(ur_u=vr_v=s\) with opposite signs. Thus the displayed coefficients are complete even without finding that optimizer coefficient. Their analytic remainders are even in h and begin at order eight.

Applying \(-\log(1+x)=-x+x^2/2-x^3/3+\cdots\) gives
\[
C_B=\frac{2s}{2-s}h^2+
\frac{4s(11s^2-22s+20)}{9(2-s)^3}h^4
+\frac{32s(179s^4-716s^3+1728s^2-2024s+968)}{405(2-s)^5}h^6
+O_s(h^8).
\]
By symmetry, T has exactly the Chernoff optimizer \(t=1/2\); therefore
\[
C_T=-\log(1-s+s\sqrt{1-4h^2})
=2sh^2+(2s+2s^2)h^4+
(4s+4s^2+\tfrac83 s^3)h^6+O_s(h^8).
\]
Subtracting \(C_B\) from \(C_T/(2-s)\) cancels the quadratic term, reproduces \(A(s)\) from the predecessor, and yields the new rational \(B_6(s)\). The remainders are real-analytic in \(h^2\) uniformly for s on compact neighborhoods inside \((0,1)\).

The algebraic identity \(9s_*^2-40s_*+4=0\) reduces \(B_6(s_*)\) to the displayed radical. This number is strictly negative by exact integer inequalities \(953^2<91\cdot100^2\) and \(2413784\cdot953>22963736\cdot100\), since \(\sqrt{91}>953/100\). The derivative is
\[
A'(s_*)=\frac{127\sqrt{91}-1183}{250}>0
\]
by \(127\cdot953>1183\cdot100\).

For \(h\ne0\), set \(G(s,h)=F(s,h)/h^4\), and extend analytically by \(G(s,0)=A(s)\). Since \(A(s_*)=0\) and \(A'(s_*)>0\), the real-analytic implicit-function theorem supplies exactly one local root curve \(s_c(h)\). The equation is even in h, so the curve is even. Comparing order \(h^2\) in \(G(s_c(h),h)=0\) gives
\[
\kappa=-\frac{B_6(s_*)}{A'(s_*)}
=\frac{1946672-162368\sqrt{91}}{2764125}.
\]
It is positive because \(\sqrt{91}<10\) and \(1946672>162368\cdot10\). Continuity of the positive s-derivative establishes the local orientation of the sign change. QED.

## Exact computation and source/observer scope

The accompanying VERIFY.py uses exact SymPy rational-function algebra and a quadratic algebraic number to recompute the optimizer and coefficient identities through degree six. Its four integer sign checks certify the strict comparisons without floating-point approximations. The actual run and version are in RUN_EVIDENCE.txt; the script is an arithmetic cross-check of the analytic proof, not an independent formal or mathematical review.

The map \(T\to B\) retains only one typed event label in the paired-state test and discards other source/erasure information. The result is scoped to these hypotheses, costs and future testing operations; it provides no claim of lossless global observer compression, no change in the nine-parameter recovery theorem, and no independent native X6 dynamics. The frozen science pin and P000/Heartbeat World constraints are preserved.

**Next:** investigate global-in-s existence and uniqueness (or a multiple-root counterexample) for fixed lawful positive h, and pursue certified finite-\(h=1/42\) root intervals. The mother ten-label decoder minimax still has the reported bounds \([1/2,2/3]\). Native Owner/CLAIM, independent review and mathematical admission remain outstanding.
