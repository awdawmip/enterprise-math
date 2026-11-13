# A3: one universal binary input certifies the all-scale orbit naturality equation

**2026-11-13 · Driver mathematical audit · scope: restricted A3 signed-\(S_4\) carrier.**

**Provenance.** Original task `RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION`, publication `TP2-D2D715EB36415B0CA0C5`, original researcher `EM-A3SCR-7A41D2`, frozen Result `RR-9FF7F84F01C577774649`. This is a new criterion derived in the existing Driver context from the [all-radius orbit theorem](2026-11-13_a3_all_scale_orbit_naturality_and_intrinsic_quotient_square.md) and [single descent probe](2026-11-13_a3_single_binary_probe_centralizer_theorem.md); it is not a second independent review, a change to the frozen Result, or Native Review admission.

## Theorem: a fixed, aligner-independent binary input suffices

Let
\[
B_n=\{x\in\mathbb Z^4:\sum_i x_i=0,\ \|x\|_\infty\le n\},\quad
S_r=B_r\setminus B_{r-1},
\quad\rho_g=\operatorname{sgn}(g)P_g\quad(g\in S_4).
\]
Let \(h=(12)\), \(H=\{e,h\}\), and \(X_n=A^{B_n}\) with **at least two distinct labels**. Write \(D_{n,d}(g)\) for the carrier permutation that acts by \(\rho_g\) on shells \(r\ge n-d+1\), and by identity on lower shells. Let \(J_n:X_{n+1}\to X_n\) restrict labels and let \(\pi_n:X_n\to X_n/H\) be the *global*, rather than shellwise, orbit projection.

For each \(m\ge1\), define the **same explicit binary input**, independent of the depth and of both aligners:
\[
F_m(x)=
\begin{cases}
1,&x=r(e_1-e_2)\text{ or }r(e_1-e_3)\text{ for some }1\le r\le m,\\
0,&\text{otherwise.}
\end{cases}
\]
Here \(0,1\) denote any two different elements of \(A\).

**Uniform one-input theorem.** For every \(n\ge d\ge1\) and every \(g_-,g_+\in S_4\), the following are equivalent:

**(i)** The complete output-orbit equality holds for **every** input \(f\in X_{n+1}\):
\[
\pi_n\big(J_nD_{n+1,d}(g_+)_*f\big)
=\pi_n\big(D_{n,d}(g_-)_*J_nf\big).
\]

**(ii)** The very same equality holds for the **single predetermined** input \(f=F_{n+1}\).

**(iii)** With \(q=n-d+1\), the aligners satisfy the exact all-scale classification:

| Regime | Necessary and sufficient condition |
|---|---|
| \(q\ge2,\ d=1\) | \(g_-=e\), \(g_+\) arbitrary |
| \(q\ge2,\ d\ge2\) | \(g_-=g_+=e\) |
| \(q=1,\ n\ge2\) | \(g_-\in H,\ g_+=e\) |
| \(n=d=1\) | \(g_-\in H\), \(g_+\) arbitrary |

Thus one binary labeling containing **two marked roots per positive shell**, chosen before the aligners and depth are known, is a universal separating experiment for this entire family of *output-orbit* naturality equations.

## Proof

**1. A two-root shell signature has trivial set stabilizer.** Define
\[
E_r=\{r(e_1-e_2),\,r(e_1-e_3)\}\subseteq S_r.
\]
Under an even \(g\), its image is the two-root set with common positive coordinate \(g(1)\) and negative coordinates \(g(2),g(3)\). If \(\rho_gE_r=E_r\), then \(g(1)=1\), \(\{g(2),g(3)\}=\{2,3\}\), and \(g(4)=4\). The only candidates are \(e\) and \((23)\); the latter is odd, so the only even solution is \(e\). Under an odd \(g\), the signed action reverses both roots, yielding two distinct positive coordinates and one common negative coordinate; such a set cannot equal \(E_r\), which has one common positive coordinate and distinct negatives. Consequently
\[
\operatorname{Stab}_{S_4}(E_r)=\{e\}\qquad\text{for every }r\ge1.
\tag{1}
\]
In particular, for \(\alpha,\beta\in S_4\), \(\rho_\alpha E_r=\rho_\beta E_r\) implies \(\alpha=\beta\).

**2. The two output supports are shellwise translates of the same rigid signatures.** Let \(q=n-d+1\). On shells \(1\le r\le n\), the upper-then-restrict path acts on \(E_r\) by
\[
u_r=\begin{cases}e,&r\le q,\\g_+,&r\ge q+1,\end{cases}
\]
and the restrict-then-lower path by
\[
\ell_r=\begin{cases}e,&r<q,\\g_-,&r\ge q.\end{cases}
\]
The upper shell \(S_{n+1}\) is discarded by restriction; its input labels do not affect either output. Therefore the two binary output supports for \(F_{n+1}\) are exactly the disjoint shell unions \(\bigcup_{r=1}^n\rho_{u_r}E_r\) and \(\bigcup_{r=1}^n\rho_{\ell_r}E_r\).

**3. One global \(H\)-choice forces the whole defect.** Equality of these two binary outputs modulo the global \(H\)-action means that a **single** \(\epsilon\in\{0,1\}\) satisfies
\[
\rho_{\ell_r}E_r=\rho_{h^\epsilon u_r}E_r
\quad\text{for all }1\le r\le n.
\]
By (1), this holds exactly when
\[
\ell_r=h^\epsilon u_r\quad\text{for every }r,
\quad\text{equivalently}\quad
\ell_r u_r^{-1}=h^\epsilon
\text{ globally across all shells.}
\tag{2}
\]
Condition (2) is precisely the statement that the two carrier output permutations differ by one global \(H\)-element; hence they give equal output orbits for *every* coloring \(f\). This proves (ii)\(\Rightarrow\)(i); the reverse implication is immediate.

**4. Extract the table.** If \(q\ge2\), the inactive shell \(S_1\) forces \(\epsilon=0\); the transition shell \(S_q\) gives \(g_-=e\), and a further overlap shell exists iff \(d\ge2\), in which case \(g_+=e\). If \(q=1\), the first shell gives \(g_-=h^\epsilon\), and when \(n\ge2\), an overlap shell gives \(g_+=e\). When \(n=d=1\), the upper aligner acts only on a shell removed by restriction. This yields (iii), completing the proof.

## Minimal shell signature and precise scope

A **single oriented root** in \(S_r\) has a two-element stabilizer under this signed \(S_4\) action (\(|S_4|=24\), and the oriented-root orbit has 12 points); therefore a one-root shell signature is not a free \(S_4\)-signature. The above two-root set is minimal **among root-subset signatures with trivial signed-\(S_4\) stabilizer on one shell**. The theorem does not assert optimality among all possible binary colorings of an entire carrier.

This is a statement about **output orbits** \(\pi_n J_nD_{n+1,d}(g_+)_*\) and \(\pi_nD_{n,d}(g_-)_*J_n\). It does not by itself guarantee that either partial move induces an intrinsic quotient-state operator; for that stronger square the separate centralizer criterion \(g_\pm\in C_{S_4}(h)\) remains necessary.

The carrier is the declared restricted A3 auxiliary model, not a native six-axis space. Any transfer to HEARTBEAT_WORLD X6 requires its own source/observer/operation-preserving interpretation under P000.

## Executable finite regression

The corresponding [pure-Python checker](../../research_checks/A3_UNIVERSAL_BINARY_NATURALITY_WITNESS_20261113.py) tests the **single input \(F_{n+1}\)** against the exact table for every \((g_-,g_+)\in S_4^2\) and all \(1\le d\le n\le4\), using integer root pairs and exact permutations. Its local execution passed all **5,760** comparisons, with positive counts by \((n,d)\) equal to:
\[
48,24,2,24,1,2,24,1,1,2
\]
in lexicographic \((n,d)\) order. The script also checks that the two-root signature has trivial stabilizer while a single oriented root has a stabilizer of order two. The universal quantifiers in the theorem are discharged by the proof above; the finite test is a regression.

**Admission/continuation.** This is an additional same-context Driver mathematical contribution linked to the existing A3 return. Original author and frozen Result bytes remain intact. Native review requires lawful current-Source Result admission, the original role/DA gates and independence disclosure; no Task or mother-objective closure is inferred.
