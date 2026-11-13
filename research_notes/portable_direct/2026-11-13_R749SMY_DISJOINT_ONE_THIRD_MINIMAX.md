# R749SMY — Exact interior disjoint-complement Walsh minimax point with calibration penalty

Date: 2026-11-13 (Asia/Shanghai). Research lineage: R749SMQ–R749SMX, especially R749SMW and R749SMX. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged). This is an auxiliary finite signed-source observer calculation, not a native X6 Cell/Link/Port event. Author-side proof/evidence; independent mathematical review pending.

## Mathematical question and theorem

Write \(G=\mathbb F_2^4\), \(\chi_k(x)=(-1)^{k\cdot x}\), \(C=\{1,2,4,8,15\}\), and \(B=\{3,5,6,7,9,10,11,12,13,14\}\). Fix the ten retained B moments as \(m_3=m_{12}=1/3\), with all other \(m_b=0\). Let \(F\subseteq\Delta(G)\) be the compatible source fiber and let \(\operatorname{TV}(p,q)=\frac12\sum_x|p_x-q_x|\).

Define the unrestricted full-source Chebyshev risk
\[
 \rho(F)=\min_{q\in\Delta(G)}\max_{\mu\in F}\operatorname{TV}(q,\mu)
\]
and the calibrated risk
\[
 \rho_{\mathrm{cal}}(F)=\min_{q\in F}\max_{\mu\in F}\operatorname{TV}(q,\mu).
\]

**Theorem (sharp interior point).** On this exact rational fiber,
\[
\boxed{\rho(F)=\frac{92}{225},\qquad
       \rho_{\mathrm{cal}}(F)=\frac49,\qquad
       \rho_{\mathrm{cal}}(F)-\rho(F)=\frac8{225}.}
\]
It is an interior point \((t,s)=(1/3,1/3)\), different from R749SMW's interior point \((1/2,1/2)\) whose unrestricted radius is \(2/5\). The extrema are taken over all probability decoders, without restricting their dependence on the input moments to be linear or affine.

## Symmetry reduces the decoder

Let \(A=\chi_3\), \(D=\chi_{12}\), \(P=\chi_1\), \(Q=\chi_4\), four independent binary signs. The remaining omitted C characters become \(AP,DQ,AD\). The full fiber, by R749SMX, has probabilities
\[
 \mu(A,D,P,Q)=\frac{1+(A+D)/3+hAD+uP+vAP+wQ+zDQ}{16},
\]
with exact positivity conditions \(1+(A+D)/3+hAD\ge|u+vA|+|w+zD|\) for each \(A,D=\pm1\).

The source-translation subgroup that fixes \(A,D\) has four elements and preserves the fiber, because all other retained B moments are zero. The invertible sign-coordinate interchange \((A,D,P,Q)\mapsto(D,A,Q,P)\) permutes C and B internally and preserves the equal values \(m_3=m_{12}\). Total variation loss is convex in the decoder; averaging any decoder over these symmetries cannot increase its maximum loss. Therefore an optimal decoder exists that is uniform within each four-state sign class \((A,D)\), with total class masses
\[
(q_{++},q_{+-},q_{-+},q_{--})=(a,b,b,c),\quad
 c=1-a-2b,\quad a,b,c\ge0.
\]
For a calibrated decoder, the ten B moment equations additionally give \(a-c=1/3\), equivalently \(a+b=2/3\). Symmetrization preserves calibration.

## Three explicit lower-bound witnesses

The following three probability measures are listed by their nonzero masses at the integer source labels \(x=0,\dots,15\); all unlisted masses vanish.

- \(\mu_A\): labels \(4,7,8,11\) each carry \(1/12\); labels \(12,13,14,15\) each carry \(1/6\).
- \(\mu_B\): labels \(3,7,11,12,13,14\) each carry \(1/9\); labels \(5,6,9,10\) each carry \(1/36\); label \(15\) carries \(2/9\).
- \(\mu_C\): labels \(0,3,12,15\) each carry \(1/6\); labels \(5,6,9,10\) each carry \(1/12\).

Exact signed Walsh summation verifies that each of the three belongs to F. Take the events
\[
\begin{aligned}
S_A&=\{4,7,8,11,12,13,14,15\},\\
S_B&=\{5,6,7,9,10,11,13,14,15\},\\
S_C&=\{0,3,5,6,9,10,12,15\}.
\end{aligned}
\]
The respective witness masses are \(\mu_A(S_A)=1\), \(\mu_B(S_B)=7/9\), \(\mu_C(S_C)=1\).

For any symmetrized decoder with sign-class masses \((a,b,b,c)\), the inequality \(\operatorname{TV}(q,\mu)\ge\mu(S)-q(S)\) yields three necessary bounds for the worst-case radius r:
\[
 r\ge L_A=1-\frac a2-\frac{3b}{2},\qquad
 r\ge L_B=-\frac29+\frac{3a}{4}+b,\qquad
 r\ge L_C=2b.
\]
Taking the convex combination
\[
\frac{12}{25}L_A+\frac8{25}L_B+\frac5{25}L_C
=\frac{92}{225}
\]
eliminates both free decoder masses exactly. Thus \(\rho(F)\ge92/225\) for *all* decoders.

For calibrated q, the additional relation \(a+b=2/3\) turns the first and third bounds into \(r\ge2/3-b\) and \(r\ge2b\). Their smallest possible maximum is \(4/9\), attained at \(b=2/9\). Hence \(\rho_{\rm cal}(F)\ge4/9\). These are exact analytic dual certificates.

## Explicit decoders and exhaustive upper certificate

For unrestricted prediction, choose
\[
(a,b,b,c)=\left(\frac{128}{225},\frac{46}{225},
\frac{46}{225},\frac1{45}\right).
\]
For calibrated prediction, choose
\[
(a,b,b,c)=\left(\frac49,\frac29,\frac29,\frac19\right).
\]
Assign each class mass equally to its four source states. Both are valid probability laws and the second reproduces every one of the ten B moments. The unrestricted decoder instead has \(m_3=m_{12}=41/75\), so it is genuinely uncalibrated.

The five-dimensional positivity polytope in \((h,u,v,w,z)\) is full dimensional at this moment vector: \(h=ts=1/9\), \(u=v=w=z=0\) gives a strictly positive point. Its sixteen nonnegativity inequalities describe a bounded polytope. Every vertex therefore has five independent active inequalities. Exhaustively enumerate all \(\binom{16}{5}=4368\) subsets, solve their equalities with exact rational Gaussian elimination, then enforce all sixteen inequalities.

The companion exact checker obtains 3,008 nonsingular active matrices, 312 feasible active systems (with repetitions), and exactly 37 distinct probability vertices. For every feasible vertex it verifies the source simplex and all retained B moments independently. For the two explicit decoders the precise total variation distance histograms are:

| Distance | Unrestricted vertex count | Calibrated vertex count |
|---|---:|---:|
| \(92/225\) | 9 | 0 |
| \(353/900\) | 16 | 0 |
| \(1/3\) | 8 | 12 |
| \(67/300\) | 4 | 0 |
| \(4/9\) | 0 | 5 |
| \(3/8\) | 0 | 16 |
| \(1/4\) | 0 | 4 |

The maximum distances are exactly \(92/225\) and \(4/9\). Since total variation distance from a fixed decoder is convex in the source law, its maximum over the full continuous probability fiber is attained at an extreme point. Thus the exhaustive rational checks certify the upper bounds everywhere in the stated fiber. Together with the three explicit lower witnesses, they prove the theorem.

Reproduction: R749SMY_DISJOINT_ONE_THIRD_EXACT_CHECK.py uses only Python standard-library fractions.Fraction and deterministic integer combinatorics; it prints the output corresponding to R749SMY_DISJOINT_ONE_THIRD_RESULTS.json. No floating-point computations, random search, external optimization solver or sampled-continuum inference enters the proof.

## Consequence, status and further research

At this particular interior moment vector, forcing a predictor to reproduce the retained Walsh moments increases worst-case full-source prediction error by exactly \(8/225\). The unrestricted optimal center has predicted \(A,D\) means \(41/75\) rather than the constrained source means \(1/3\); this is a rigorously quantified geometric consequence of minimizing worst-case total variation over a fiber.

Next objective: derive the phase decomposition of the complete disjoint-edge two-moment function \(\rho_B(t,s)\), with exact breakpoints and parametric dual certificates. Keep this B disjoint-edge orbit separate from the complementary adjacent-edge and five-circuit orbits. Transferring the abstract observer result into Heartbeat World requires an actual licensed native V29/V39 Cell/Link/Port correspondence preserving the intended future operations. Independent scientific review and any formal project admission remain open.
