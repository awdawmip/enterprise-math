# A3: sharp three-site binary probe using free signed-\(S_4\) carrier points

**Date:** 2026-11-13. **Scope:** exact A3 shell model, same Driver mathematical context as the five-site rooted-probe audit. **Attribution:** original frozen Result `RR-9FF7F84F01C577774649`, task `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`, researcher `EM-A3SCR-7A41D2`; this is a Driver supplement, not an independent review or Native Result disposition.

## Theorem

For the original carrier \(B_n=\{x\in\mathbb Z^4:\sum_i x_i=0,\ \|x\|_\infty\le n\}\), signed action \(\rho_g=\operatorname{sgn}(g)P_g\) of \(S_4\), global \(H=\{e,h\}\) with \(h=(12)\), and full label space \(A^{B_n}\) where \(|A|\ge2\), fix any \(n\ge d\ge1\) and \(q=n-d+1\).

Let \(a=e_1-e_2,\ b=e_3-e_4,\ E_1=\{e_1-e_2,e_1-e_3\}\) and
\[
v_r=(r,r-1,1-r,-r)\in S_r\qquad(r\ge2).
\]
Use one binary labeling of \(B_{n+1}\), marking exactly the set
\[
M_{n,d}=
\begin{cases}
\{b,v_q,v_{q+1}\},&q\ge2,\ d\ge2;\\
\{b,v_q\},&q\ge2,\ d=1;\\
E_1\cup\{v_2\},&q=1,\ n\ge2;\\
\{a\},&n=d=1.
\end{cases}
\tag{1}
\]
Every other site carries the background label. The output-orbit equation
\[
\pi_n(J_nD_{n+1,d}(g_+)_*f)=
\pi_n(D_{n,d}(g_-)_*J_nf)
\tag{2}
\]
holds for **every** \(f\in A^{B_{n+1}}\) if and only if it holds on this **single** binary input. The exact classifications are, respectively,
\[
(g_-,g_+)=(e,e),\qquad
g_-=e\ (g_+\text{ arbitrary}),\qquad
g_-\in H,\ g_+=e,\qquad
g_-\in H\ (g_+\text{ arbitrary}).
\tag{3}
\]

Furthermore, among **single-input binary labelings with a constant background and finitely many differently labeled sites**, the minimum numbers of marked sites required for this universal equivalence test in these four regimes are **3, 2, 3, 1**, respectively. This removes the oriented-root-only restriction of the preceding five-site sharpness statement.

## Proof

**Free point lemma.** Every \(v_r\), \(r\ge2\), has four pairwise distinct coordinates. An even permutation fixing it must be the identity. For an odd \(g\), the equation \(\rho_gv_r=v_r\) requires \(P_gv_r=-v_r\). Because the entries are precisely \(\{r,r-1,1-r,-r\}\), the unique permutation taking \(v_r\) to \(-v_r\) is the product of two disjoint transpositions, which is even. Thus \(\operatorname{Stab}_{\rho}(v_r)=\{e\}\). Also \(\operatorname{Stab}_{\rho}(a)=H\), \(\rho_h b=-b\ne b\), and the pair \(E_1\) has trivial setwise signed stabilizer (the two common-headed roots distinguish the orientation and parity).

The \(H\)-orbit comparison in (2) uses **one global** \(h^\epsilon\) for all surviving shells. If \(q\ge2\), both paths fix \(S_1\). The mark \(b\) forces \(\epsilon=0\); the unique free mark \(v_q\) on the transition shell (upper path identity, lower path \(g_-\)) then forces \(g_-=e\). When \(d\ge2\), the free mark \(v_{q+1}\) on an overlap shell (upper path \(g_+\), lower path \(g_-\)) forces \(g_+=e\). At \(d=1\), no overlap shell survives and \(g_+\) is unrestricted.

If \(q=1,\ n\ge2\), the \(E_1\) support on the first shell and its trivial setwise stabilizer force \(g_-=h^\epsilon\). The unique free \(v_2\) on the overlap shell forces \(g_+=e\). Finally \(n=d=1\) has only the first shell, and the single mark \(a\) has stabilizer exactly \(H\), so \(g_-\in H\). Conversely, each case of (3) makes the two entire carrier outputs agree up to one global \(H\)-action for every labeling. This proves the criterion for all scales and depths, not merely the tested finite range.

**Sharpness in the stated binary-background class.** For \(q\ge2,d\ge2\), marks are indispensable in each of three *disjoint* surviving regions: an inactive inner shell, the transition shell \(S_q\), and an overlap shell \(S_{q+1},\dots,S_n\). If no inner site is marked, \(g_-=h,g_+=e\) is a false positive by global \(H\)-equivalence. If no transition site is marked, \(g_-=g_+\ne e\) is an exact false positive. If no overlap site is marked, \(g_-=e,g_+\ne e\) is an exact false positive. Hence at least three marks are necessary. The same first two arguments prove the lower bound two when \(q\ge2,d=1\).

For \(q=1,n\ge2\), there must be a mark both on \(S_1\) and on an overlap shell: without an \(S_1\) mark, \(g_-=h,g_+=e\) gives an \(H\)-orbit false positive; without an overlap mark, \(g_-=e,g_+\ne e\) gives an exact false positive. Suppose exactly one mark \(x\in S_1\) and one overlap mark. Every \(x\in S_1\) has nontrivial stabilizer under signed \(S_4\): its entries belong to \(\{-1,0,1\}\), sum to zero, and are a root or a permutation of \((1,1,-1,-1)\). If some stabilizer element \(k\notin H\) exists, choose \(g_-=g_+=k\); both paths agree exactly on both marked sites, falsely satisfying (2). Otherwise its nontrivial stabilizer is exactly \(H\), so \(x\) is \(h\)-fixed: choosing \(g_-=e,g_+=h\) makes the two outputs globally \(H\)-equivalent, another false positive. Two marks cannot suffice; the three-site construction attains the bound.

When \(n=d=1\), zero marks cannot distinguish \(g_-\notin H\); the single mark \(a\) attains the bound one. This proves all sharp counts. \(\square\)

## Verification and status

The exact checker `research_checks/A3_SHARP_THREE_SITE_ORBIT_PROBE_20261113.py` exhaustively tested every \(g_-,g_+\in S_4\) and all \(1\le d\le n\le8\): **20,736 exact alignment cases, zero disagreements**, maximum three marked sites. It also tests the stabilizers for the specific points. The all-scale theorem rests on the argument above; finite checks are regression evidence.

This strengthens [the previous rooted five-site theorem](2026-11-13_a3_sharp_five_site_orbit_probe.md) without invalidating its explicitly restricted optimality claim. The result concerns the output-orbit equation; intrinsic quotient operators have the separate centralizer prerequisite. It does not promote the original frozen Result to Native `ACCEPTED`, take the original researcher's CLAIM, or close the mother objective.
