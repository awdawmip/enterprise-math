# PREFIX-770 / R6 — Strict transverse stability of the diagonal Gamma phase ratio

Date: 2026-11-14. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_EXACT_INTEGER_DERIVATIVE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.
Scope: the external 189-layer killed-Pascal BRC stopping and independent Gamma-clock maximum model. This is a direct continuation of PREFIX-769, without upgrading the conclusion to native X6 dynamics.

## Theorem 770.1 — exact transverse second-order coefficient

For the two-clock maximum Y(p,z) let
\[
\mu=E[Y],\quad W=\operatorname{Var}Y,\quad
A(p,z)=-\partial_p\partial_z\mu(p,z),\quad
D(p,z)=-\partial_p\partial_z W(p,z),\quad
Q(p,z)=A(p,z)/D(p,z)
\]
where D>0. Both A and D are symmetric under p,z exchange because the independent clocks have the same frozen family.

Fix u=5029714/10^8. Take the transverse path p=u+t,z=u-t and let s=s(u), d=s'(u), e=s''(u), f=s'''(u). Denote the exact PREFIX-760 Erlang kernels by K and L. Set
\[
m=2{\bf1}^Ts-s^TKs,\quad v={\bf1}^Td-d^TKs,\quad
A_0=d^TKd,\quad B_0=d^TLd,\quad D_0=B_0+2v^2-2mA_0.
\]
The t² coefficients of the relevant symmetric expansions are:
\[
A_2=f^TKd-e^TKe,\qquad B_2=f^TLd-e^TLe,
\]
\[
m_2={\bf1}^Te-e^TKs+A_0,\quad
2v_{p,2}={\bf1}^Tf-f^TKs+e^TKd,
\]
\[
D_2=B_2+2v(2v_{p,2})-2m_2^2-2m_2A_0-2mA_2.
\]
Here \(\mu(u+t,u-t)=m+m_2t^2+O(t^4)\), and \(v_p(u+t,u-t)=v+v_{p,1}t+v_{p,2}t^2+O(t^3)\) with \(v_{p,1}=m_2\), while \(v_z(t)=v_p(-t)\).
Exchange symmetry forces all odd transverse Taylor coefficients of Q to vanish. Therefore
\[
Q(u+t,u-t)=Q(u,u)+Q_2t^2+O(t^4),\quad
Q_2=\frac{A_2D_0-A_0D_2}{D_0^2}.
\]

**Proof.** Differentiate each rational survivor polynomial term by term to third order, expand s(u+t),d(u+t) and their u-t partners, and multiply the symmetric bilinear forms K,L. The expression for m_2 follows from the t² coefficient of s_+^T K s_-; the mixed derivative D=B+2v_pv_z-2mu A then gives D_2. Divide the even Taylor series A(t)/D(t), using D_0>0. All series are finite-polynomial identities near u, hence the remainder statements follow from analyticity. QED.

## Theorem 770.2 — certified strict transverse minimum at a rational point

The standalone exact-integer program reconstructs all 189 frozen survivor rows, confirms 9,529 nonzero survivor positions and the empty terminal row, forms their first, second and third derivatives at u=5029714/10^8, and computes the integer-scaled A_0,D_0,A_2,D_2.

Writing H=(10^8)^188, T=2^377, E=H²T, the program works with scaled A_0^*=EA_0, D_0^*=E²D_0, A_2^*=EA_2 and D_2^*=E²D_2. It strictly confirms:
\[
D_0^*>0,\quad A_0^*>0,\quad
21(D_0^*)^2<
E(A_2^*D_0^*-A_0^*D_2^*)<
22(D_0^*)^2.
\]
Thus
\[
\boxed{21<Q_2<22},\qquad Q_2\approx21.345867162752126839763676735068.
\]
In particular, at this rational u, \(Q(u+t,u-t)>Q(u,u)\) for all sufficiently small nonzero real t. The transverse direction has positive second derivative \(2Q_2>42\), giving a strict local minimum along the fixed-midpoint anti-diagonal path.

This settles a local off-diagonal instability question left open in PREFIX-769: infinitesimal symmetric separation of the two Gamma parameters does not improve the pointwise upper witness at this particular u.

## Provenance and verification

Scientific input pin remains f42f2906d77f24085c123f3ccfe9667d41caa96d. Reused numerical identities and source code: PREFIX-768/769 exact 189-layer width predicate, Pascal survivor recursion, and K,L kernels. New exact computation: third survivor derivatives and integer sign certificate for the transverse quadratic coefficient. The author-local execution printed ALL_CHECKS_PASS PREFIX770 TRANSVERSE and established the strict integer double inequality above; displayed decimals are not used in proof comparisons.

Reproduce with Python 3 standard library: research_notes/portable_direct/PREFIX770_R6_TRANSVERSE_PHASE_CHECK.py. Output summary: PREFIX770_R6_TRANSVERSE_PHASE_RESULTS.json. This is an author-level exact finite certificate pending independent review.

The result concerns one rational diagonal parameter and one transverse direction. The minimum of Q over the full two-parameter square, uniqueness of the diagonal stationary root, and genuine 1/768 cell exclusion remain separate research questions.

Next: certify a positive transverse coefficient uniformly over the PREFIX-769 stationary bracket by rational interval arithmetic, and independently test whether another off-diagonal region or boundary yields Q lower than the current diagonal candidate.
