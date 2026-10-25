# D25/LIFT — oriented diagonal rank-moment transfer and unique low-channel diagonal source

Date: 2026-10-26. TASK_RESEARCH portable contribution, task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

**Status: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** No original-class native CM experiment, Source run/checkpoint authorization, Result or admission is inferred from this note.

## Inputs and exact sources

Consume (without re-crediting) the corrected Clausen rank/Hasse recurrence in research_notes/portable_direct/20261025_hourly_d25_clausen_operator_rank_boundary.md, and dual-strip flux in research_notes/portable_direct/20261026_hourly_d25_dual_strip_flux_r11.md. Aim: pass the corrected operator through the *oriented lower reflection triangle* with the quadratic labelled rank observable still present.

Let p=6m+1>=7 be prime, J=2m, and let
\[
u_{a,r}=[t^a]\frac{(-m-t)_r(-2m-2t)_r}{(1-p/2-3t)_r r!}.
\]
Indices a<0 vanish and u_{a,0}=1_{a=0}. All displayed equalities are over the p-local coefficient ring, and therefore descend to Z/p^2.

For all integers n and s=0,1,2 define (including zero outside the displayed domain)
\[
X_s^{a,b}(n)=\sum_{\substack{1\le j,\ell\le J\\\ell-j=n}} j^s u_{a,j}u_{b,p-\ell}.
\]
When a<0 or b<0 the moment vanishes. Set \(C_b(e)=u_{b,p-e}\) for \(1\le e\le J\) and zero elsewhere.

## Theorem A — exact oriented diagonal transfer with disjoint source ports

Define
\[
\begin{aligned}
D_{a,b}(n)={}&X_2^{a,b}(n)-\frac p2X_1^{a,b}(n)-3X_1^{a-1,b}(n)\\
&-X_2^{a,b}(n+1)+3mX_1^{a,b}(n+1)-2m^2X_0^{a,b}(n+1)\\
&+3X_1^{a-1,b}(n+1)-4mX_0^{a-1,b}(n+1)-2X_0^{a-2,b}(n+1).
\end{aligned}
\]
For every a,b>=0 and every integer n,
\[
\boxed{D_{a,b}(n)=S_a C_b(n+1)+T_a C_b(J+n+1),}\tag{A1}
\]
where
\[
S_a=2m^2 1_{a=0}+4m1_{a=1}+2 1_{a=2},\quad
T_a=2m u_{a-1,J}-2u_{a-2,J}.
\]
The S port has support 0<=n<=J-1, whereas the T port has support -J<=n<=-1, so the two sources have **disjoint signed orientations**.

Proof: Multiply the exact corrected rank/Hasse recurrence at rank j by u_{b,p-ell} and sum over 1<=j,ell<=J at fixed ell-j=n. Unshifted terms give \(X_2(n)-(p/2)X_1(n)-3X_1^{a-1,b}(n)\). Shift the terms originally at j-1 by j'=j-1, so ell-j'=n+1. Extend the sum j'=0,...,J-1 to 1,...,J. The polynomial (j'-m)(j'-2m) creates \(X_2-3mX_1+2m^2X_0\), while the linear Hasse term \(3j'-4m\) and quadratic Hasse term 2 create the remaining moments, all at index n+1. The omitted j'=0 endpoint gives \(S_a C_b(n+1)\) because u_{a,0}=1_{a=0}; the artificially included j'=J endpoint is corrected by \(T_a C_b(J+n+1)\), using (J-m)(J-2m)=0. Every inner rank cancels identically. Supports are the two direct inequalities on ell. QED.

## Corollary B — three active p^4 channels are homogeneous on the strict lower triangle

Since J=2m>m, u_{0,J}=0. Consequently \(T_0=T_1=0\). For any b>=0 and a=0,1:
\[
\boxed{D_{a,b}(n)=S_a u_{b,p-1}\,1_{n=0}\quad(n\le0),\qquad
D_{a,b}(n)=0\quad(n<0).}\tag{B1}
\]
Exactly the three actual corrected p^4 reflection channels (a,b)=(0,2),(1,2),(0,3) have a=0 or 1. Their quadratic-rank operator flux has no interior forcing at negative orientations; a single diagonal ell=j injection survives. This is *not* a global WZ cancellation: the mirrored high-rank operators contribute K and p boundary ports, the signed 2^n weighting remains, and the diagonal cannot be dropped.

At p=13, m=2, u_{2,p-1}=1 (mod13), hence D_{0,2}(0)=D_{1,2}(0)=8 (mod13). Both are zero for all n<0.

## Author exact check and next unit

The companion standard-library Python checker reuses the adjacent exact jet generator, directly sums every labelled diagonal for a=0..4,b in {2,3}, s=0,1,2 over all n. PASS for all 22 target primes p<=211 (p≡1 mod6). This checks, but does not prove, the all-prime claim. Proof is the exact coefficientwise argument above. Independent review and native CM test are NOT_RUN.

**BRC COMPOSE_APPLIED:** carrier retains labelled (j,ell), oriented n=ell-j, Hasse source (a,b), valuations, finite rank cutoffs and signed channels. The mass-only observer X_0 is not future-operator sufficient for the quadratic rank action; X_0,X_1,X_2 and both boundary ports are. This is an external algebraic model; no invented P000 X6 native projection.

**Next smallest unfinished unit:** derive the mirrored high-strip diagonal moment transfer, then combine with (A1) on n<=0, keeping p/K high-strip boundary terms and ell=j diagonal source, to find a true coupled WZ/adjoint identity or a certified signed defect. Parent D25/LIFT/JT2 remains OPEN: actual same-class native H0/B0, [X]U mod p^2, semilinear Frobenius, eta, kappa and independent review still missing.
