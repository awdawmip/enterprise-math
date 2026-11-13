# A3: sharp five-site binary witness for every scale and depth

**Date:** 2026-11-13. **Status:** additional exact Driver mathematical proof, restricted A3 signed-\(S_4\) model; original frozen Result and authors unchanged.

**Source/provenance:** Original task RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION; publication TP2-D2D715EB36415B0CA0C5; researcher EM-A3SCR-7A41D2; frozen Result RR-9FF7F84F01C577774649. This improves the same-Driver-context [one-universal-input all-scale theorem](2026-11-13_a3_universal_one_binary_input_orbit_naturality.md), which marked two roots on *every* positive shell. The present theorem only needs **at most five marked lattice sites** for arbitrary scales. It is not an independent second review.

## Theorem and probe construction

Keep the original A3 carrier
\[
B_n=\{x\in\mathbb Z^4:\sum_i x_i=0,\ \|x\|_\infty\le n\},
\qquad S_r=B_r\setminus B_{r-1},
\qquad \rho_g=\operatorname{sgn}(g)P_g,\quad g\in S_4.
\]
Let \(h=(12)\), \(H=\{e,h\}\), and use a binary-capable full-label state space \(X_n=A^{B_n}\), \(|A|\ge2\). The global \(H\)-action is \(\rho_h\) on **every** shell. Write
\[
E_r=\{r(e_1-e_2),\ r(e_1-e_3)\},\qquad b=e_3-e_4,\qquad q=n-d+1.
\]
The following subsets \(M_{n,d}\subseteq B_{n+1}\) define an explicit **single input state** \(F_{n+1}^{n,d}\), equal to a second label exactly on \(M_{n,d}\) and a first label elsewhere:
\[
M_{n,d}=
\begin{cases}
\{b\}\cup E_q\cup E_{q+1},&q\ge2,\ d\ge2,\\
\{b\}\cup E_q,&q\ge2,\ d=1,\\
E_1\cup E_2,&q=1,\ n\ge2,\\
E_1,&n=d=1.
\end{cases}
\tag{1}
\]
The number of marked positions is respectively \(5,3,4,2\), **independent of \(n\)**. Note \(q+1\le n\) in the first line, so none of the required marks lies on the discarded top shell \(S_{n+1}\).

**Constant-size single-input criterion.** For all \(n\ge d\ge1\) and all \(g_-,g_+\in S_4\), the output-orbit naturality equation
\[
\pi_n(J_nD_{n+1,d}(g_+)_*f)
=\pi_n(D_{n,d}(g_-)_*J_nf)
\quad\text{for every }f\in X_{n+1}
\tag{2}
\]
holds if and only if (2) holds for the **one predetermined input** \(f=F_{n+1}^{n,d}\) of (1).

Its exact four-regime classification is unchanged:
\[
\begin{array}{c|l}
q\ge2,\ d=1&g_-=e,\ g_+\text{ arbitrary}\\
q\ge2,\ d\ge2&g_-=g_+=e\\
q=1,\ n\ge2&g_-\in H,\ g_+=e\\
n=d=1&g_-\in H,\ g_+\text{ arbitrary.}
\end{array}
\tag{3}
\]

**Sharpness within root-supported sparse binary probes.** When \(q\ge2\) and \(d\ge2\), any binary probe that uses a constant background label and marks only oriented root sites \(\pm r(e_i-e_j)\) requires **at least five marked positions** to distinguish (2) for every pair of aligners. Hence the five-site construction attains the minimum in that declared probe class. No assertion of minimality among arbitrary full-carrier binary colorings is made.

## Proof of sufficiency

**Rigid shell pair.** For every \(r\ge1\), the setwise stabilizer of \(E_r\) in the signed \(S_4\) action is trivial. For even permutations, preserving the two positive-headed roots requires fixing index 1, permuting indices 2 and 3, and fixing 4; only identity is even. For odd permutations, the signed action flips both roots, producing two distinct positive heads and a common negative tail; it cannot preserve \(E_r\), which has one common positive head and two distinct tails.

**Global \(H\)-choice.** The two output supports for any fixed probe must be identical or related by the *same* global \(\rho_h\), not separate \(H\)-choices on different shells. The single inner marker \(b=e_3-e_4\) satisfies \(\rho_hb=-b\ne b\). On the inner shell \(S_1\), both paths act as identity when \(q\ge2\); hence the presence of \(b\) forces the global \(H\)-choice to be identity, \(\epsilon=0\).

For \(q\ge2\), at the transition shell \(S_q\) the upper path acts as identity and the lower path by \(\rho_{g_-}\). Because the marked pair \(E_q\) is rigid and \(\epsilon=0\), output equality forces \(g_-=e\). If \(d\ge2\), then on the overlap shell \(S_{q+1}\) the upper path acts by \(g_+\) and the lower path by \(g_-\). The marked rigid pair \(E_{q+1}\) forces \(g_+=g_-=e\). If \(d=1\), no overlap shell survives, and \(g_+\) has no effect on the output.

For \(q=1\), there is no inner shell. At \(S_1\), the upper path is identity and the lower path is \(g_-\). The rigidity of \(E_1\) forces \(g_-=h^\epsilon\) for the one global choice \(\epsilon\in\{0,1\}\). If \(n\ge2\), the overlap shell \(S_2\) has upper action \(g_+\), lower action \(g_-\), and rigid pair \(E_2\); therefore \(g_-=h^\epsilon g_+\), which forces \(g_+=e\). For \(n=d=1\), the upper action affects only the discarded shell, so \(g_+\) is arbitrary. This proves that the single probe implies exactly (3). Conversely (3) makes the two **carrier** output maps equal up to one global \(\rho_h\), which proves (2) for every labeling. QED.

## Proof of sharpness in the declared rooted probe class

Assume \(q\ge2,d\ge2\), and let \(M\) be the set of minority-labeled oriented root sites. The three disjoint shell regions impose independent information requirements:

1. **Inactive inner shells \(r<q\): at least one mark.** If their support is globally \(h\)-invariant (in particular, empty), take \(g_-=h,g_+=e\). The output defect equals \(\rho_h\) on every active shell and identity on the inner shells. Because the inner labeling is \(h\)-invariant, the two outputs are equal in the global \(H\)-orbit even though (3) is false. Thus some inner marking that breaks \(h\) is necessary.

2. **Transition shell \(S_q\): at least two root marks.** If \(M\cap S_q\) is empty or one oriented root, choose nonidentity \(g\in S_4\) stabilizing every mark there (any single oriented root has a nontrivial order-two stabilizer). Set \(g_-=g_+=g\). On all overlap shells the two path actions agree exactly; on \(S_q\) the lone marked root is fixed; on inactive shells both actions are identity. The outputs coincide exactly, contradicting (3).

3. **Overlap shells \(q<r\le n\): at least two root marks in total.** If there are zero or one such marks, take \(g_-=e\) and a nonidentity \(g_+\) stabilizing the lone root, if any. The two outputs coincide exactly on every marked site, again contradicting (3).

The regions are disjoint, so \(|M|\ge1+2+2=5\). The first line of (1) realizes equality. This minimum is **only** for fixed-minority-label, oriented-root-support binary probes, not general A3 labelings or arbitrary multi-label experiments. QED.

## Exact finite regression and consequences

The [pure-Python exact checker](../../research_checks/A3_CONSTANT_SIZE_ORBIT_PROBE_20261113.py) tests the single marked subset in each \((n,d)\) regime against the full exact table for every \(g_-,g_+\in S_4\), over **all 15 regimes \(1\le d\le n\le5\)**. This is \(15\cdot24^2=8,640\) comparisons. Local execution returned PASS with **zero mismatches** and largest support size five; syntax/byte verification was performed separately. The all-\(n,d\) strength comes from the proof above, not from finite cases.

This compression is substantive: a test state with \(2n\) marked roots in the earlier theorem is replaced by **at most five** precisely located marked roots, with sharp root-supported support bound in the \(q\ge2,d\ge2\) regime. It concerns the *output-orbit* square only. Intrinsic quotient-state operators still require the independent centralizer condition \(g_\pm\in C_{S_4}(h)\). The reduced carrier is the restricted A3 model; native HEARTBEAT_WORLD X6 transfer needs a separate P000-respecting map and readout certificate.

The original researcher's frozen Result, contribution provenance, immutable task publications, current CLAIM scope and formal review state remain intact. This is a same-context mathematical Driver supplement, not a Native Result acceptance, Task completion or mother-objective closure.
