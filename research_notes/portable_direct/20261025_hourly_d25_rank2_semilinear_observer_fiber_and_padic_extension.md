# D25/LIFT: rank-two semilinear square, exact observer-fiber obstruction and a p-adic extension witness

Date: 2026-10-25. Scope: Enterprise Math TASK_RESEARCH, portable directed mathematical derivation. Status: AUTHOR-PROVED / AUTHOR-CHECKED; UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM. This is **not** an original-class crystalline Frobenius experiment and is **not** a native Source checkpoint or a task CLAIM. The required native execution authority was not established in this run: current direct native control reads returned CONTROL_QUOTA. This document is an ordinary project-source evidence artifact only.

Task context: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent D25/LIFT/JT2 OPEN. Scientific frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3 is **unchanged**. Consume, do not recredit: preceding native Source checkpoint commit 220ee1ba360f21152912d0b4c1abdf867a1e4496, which already contains the ordinary Hesse quadratic norm and constructive **rank-one** Hilbert-90 proof. No claim of a newly owned active Source session is made here.

## New question and exact carrier

The previous Hilbert-90 unit classifies a **rank-one** invertible sigma-semilinear map by the norm of its coefficient. What exact information fails when the unknown native fixed module turns out to have rank two, and what must an actual original-class observation retain?

Let p be any odd prime with (2/p) = -1 (in particular p = 13 or 19 mod 24), r >= 2, A = Z/p^r Z, R=A[T]/(T^2-2), sigma(a+bT)=a-bT. On the free rank-two R-module, a sigma-semilinear invertible map has coordinate form F_C(v)=C sigma(v), C in GL_2(R). Under an R-linear basis change P the matrix becomes C'=P^{-1} C sigma(P), and its square is the R-linear matrix S_C=C sigma(C), with S_C'=P^{-1} S_C P. Only this typed operation, not coefficient-ring conjugation alone, is the modeled Frobenius-square readout.

**Lemma 1 (true invariants, no assumed native model).** For every invertible C, the characteristic-polynomial coefficients of S_C lie in A. For rank two they are
\[
t_C=\operatorname{tr}(C\sigma(C))\in A,\qquad d_C=\det(C\sigma(C))=N(\det C)\in A.
\]
Proof: sigma(S_C)=sigma(C)C=C^{-1} S_C C, hence every similarity-invariant polynomial in S_C is sigma-fixed; the fixed ring of sigma is A because 2 and T are units. Determinant multiplicativity gives the displayed norm. Both t_C and d_C are invariant under sigma-semilinear gauge. This is a **necessary** certificate; no converse is asserted. QED.

**Lemma 2 (even determinant of C is insufficient, exact p=373 certificate).** Take r=2, p=373, m=p^2=139129, and consume the already source-published ordinary-Hesse candidate
\[
\alpha=92060+21788T\in R^\times,\quad N(\alpha)=122102\pmod{139129}.
\]
For each s in A^\times define C_s=diag(s alpha,s^{-1}). Then det C_s=alpha for every s, and
\[
S_s=\operatorname{diag}(s^2N(\alpha),s^{-2}),\quad
\operatorname{tr}S_s=s^2N(\alpha)+s^{-2},\quad
\det S_s=N(\alpha).
\]
For s=1 the trace is 122103. For s=2, inverse(4)=104347 mod 139129 and the trace is 36239. Their difference is 53265 mod 139129, already 299 mod 373. Thus even the complete exact coefficient det C=alpha, its norm 122102, and det F^2 do not determine the rank-two F^2 trace or gauge class. Distinguishing these matrices requires further information, and the rank-one comparison using 122102 cannot simply be promoted to rank two. QED.

**Lemma 3 (same trace, determinant, characteristic polynomial AND every lower digit still do not suffice).** Put q=p^{r-1} in A, E=E_{12}, C_0=I_2, C_1=I_2+qE. Then E^2=0, q^2=0 in A, sigma(C_i)=C_i, and
\[
S_0=I_2,\qquad S_1=I_2+2qE\ne I_2.
\]
Both C_i and S_i have determinant 1 and trace 2; both S_i have characteristic polynomial (X-1)^2 exactly in A[X]; C_0=C_1 modulo p^{r-1}. Nevertheless these are **not** sigma-semilinear gauge equivalent: conjugation preserves the identity matrix, so a gauge carrying C_0 to C_1 would force S_1=P^{-1}I P=I, contrary to 2qE nonzero for odd p.

Hence any claimed rank-two classification that uses only determinant/norm, trace/characteristic polynomial of the square, and the complete preceding precision p^{r-1} is false in this general finite-ring setting. A visible and gauge-invariant extra yes/no readout is the centrality test S_C=I (or a richer actual matrix/conjugacy datum). This is an exact obstruction for **every r>=2**, not a finite search. QED.

At p=373 and r=2 the two squares are I_2 and I_2+746 E_{12} modulo 139129. For r=3 the off-diagonal is 278258 modulo 51895117. These are coefficient-module examples, **not** measured or hypothesized native H0/B0 Frobenius matrices.

## BRC / 进取数论 observer-fiber application

Reuse the current BRC global typed-substrate distinction between *labeled provenance*, Boolean/support, *positive branch multiplicity*, and signed/amplitude data. Here the exact finite positive-integer branch carrier is a formal labeled atomic multiset over semilinear matrices; no positive Weighted-BRC theorem is falsely substituted for signed or complex Frobenius dynamics. Define the lossy projection
\[
\pi(C)=\bigl(\det C,\operatorname{tr}S_C,\det S_C,
                C\bmod p^{r-1}\bigr)
\]
and the allowed later gauge-invariant observer \(O(C)={\bf1}_{\{S_C=I\}}\). Lemma 3 gives pi(C_0)=pi(C_1) but O(C_0)=1 and O(C_1)=0. In the exact branch-count carrier compare
\[
\mu=\delta_{C_0}+\delta_{C_1},\qquad
\nu=2\delta_{C_0}.
\]
Their pi-pushforwards are identical (both have mass 2 in the same fiber), but the number of O-positive branches is 1 for mu and 2 for nu. Thus O does **not** factor through pi, even after preserving the positive total and multiplicity of the compressed fiber. This is an actual BRC observer-lease failure witness, consistent with the protected residual-fidelity viewpoint: the \(2p^{r-1}E_{12}\) off-diagonal extension is future-relevant and cannot be discarded without an explicit additional lease. It does NOT establish a native six-dimensional/two-dimensional-space transfer, positive-mass recurrence, or any signed-amplitude BRC theorem.

## Reproducible exact author checks

The following standard-library integer check uses exact modular arithmetic; it validates sample instances but does not replace the algebraic proofs:

    def mul(A,B,m):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % m
                           for j in range(2)) for i in range(2))
    def tr(A,m):
        return (A[0][0]+A[1][1])%m
    def det(A,m):
        return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%m
    for p in (13,19,373):
        for r in (2,3):
            m=p**r
            q=p**(r-1)
            I=((1,0),(0,1))
            C=((1,q),(0,1))
            S=mul(C,C,m)
            assert S==((1,2*q),(0,1)) and S != I
            assert (tr(S,m),det(S,m))==(2,1)
            assert (tr(I,m),det(I,m))==(2,1)
            assert (C[0][1] % (p**(r-1)))==0
    m=373**2
    alpha_norm=(92060**2-2*21788**2)%m
    assert alpha_norm==122102
    t1=(alpha_norm+1)%m
    t2=(4*alpha_norm+pow(4,-1,m))%m
    assert (pow(4,-1,m),t1,t2,(t2-t1)%m)==(104347,122103,36239,53265)

Author executed these checks for p in {13,19,373}, r in {2,3}; all passed. Arithmetic is in integer residue rings with declared moduli, not floating point. The example class is not an exhaustive native CM search.

## Accurate research frontier

- Finished here: exact rank-two invariant lemma, two non-equivalence/observer-loss witnesses, p=373 full second-digit certificate, declared BRC labeled-fiber counterexample. These are elementary **conditional finite-ring structure results** in the provenance of existing rank-one work, not a native LIFT proof.
- The original SOURCE frontier must not be overwritten: prior 19 original units + previously published Green and Hesse/Hilbert-90 units, their original owner/contributions/claim, and scientific pin stay as recorded in authenticated checkpoint 220ee1ba....
- Still missing: canonical same-prime, same-original-class divided-power fixed H0/B0 module; original \([X]U\bmod p^2\) matrix; actual rank and Frobenius sigma direction; normalization eta; bridge to ordinary \(\omega+6\nabla_\lambda\omega\), odd branch, kappa and \(\Delta_p-R_p\). Native CM experiment remains NOT_RUN.
- Next exact action: obtain the original Source-authenticated module and rank. If rank one, retain the previously published norm test N(eta)*122102 at p373. If rank two and invertible, explicitly compute C, S=C sigma(C), t, d, and non-scalar extension data (including any centrality/nilpotent defect); only then test the source-defined kappa bridge. If Frobenius is noninvertible or rank differs, retype first and do not silently apply the invertible-rank-two lemmas.
- Control recovery: native em_control_task and em_control_continuation read attempts in this turn both returned CONTROL_QUOTA. This is a read/control availability failure, not NO_DISPATCH. No fresh winning owner/CLAIM/run authorization was established and no native publish, role session, review, freeze or handoff is claimed. Reconcile original native Source/continuation when quota allows; register and publish this portable evidence only by the legitimate owner under fresh authority. Research-support routing remains existing enterprise-math Issue #1558.

Source references: (i) Enterprise Math native checkpoint at 220ee1ba360f21152912d0b4c1abdf867a1e4496, fixed task/source author record; (ii) ordinary Hesse rank-one proof research_notes/portable_direct/20261025_hourly_d25_hesse_finite_ring_semilinear_hilbert90_modpr.md at 486c1b2ce2e60c0e25fbe149f1fe847ae86899f7; (iii) definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json at control read ae36c8c62d24e86886619102171fa9ac96fe8290; (iv) shared docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md at that same control read. No mathematical independent review or admission is asserted.
