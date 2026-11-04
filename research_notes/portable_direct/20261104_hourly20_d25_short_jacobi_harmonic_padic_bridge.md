# D25 — Short Jacobi–harmonic kernel and a one-boundary inhomogeneous Picard–Fuchs certificate

Date: 2026-11-04. Classification: AUTHOR-DERIVED / EXACT SCOPED ALGEBRAIC PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific input pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
Research lane is distinct from the control-maintenance lane. This portable work does not impersonate a native service session, claim or result.

## Theorem 1: exact short-kernel Jacobi–harmonic lift

For every prime p=8q+5 >=5, all rational coefficients below lie in Z_(p). Put
\[
c_j=\frac{(5/8)_j(7/8)_j}{(j!)^2 9^j},\qquad C(z)=\sum_{j=0}^{q}c_jz^j,\qquad
J_j=\binom qj\binom{3q+1}j9^{-j},\quad J(z)=\sum_{j=0}^q J_jz^j.
\]
Define the finite harmonic corrections (empty sums are zero)
\[
h_j=\frac18\sum_{r=q-j+1}^{q}\frac1r+
\frac38\sum_{r=3q+2-j}^{3q+1}\frac1r,\qquad
K(z)=\sum_{j=0}^{q}J_j h_j z^j.
\]
Then **coefficientwise in Z_(p)[z] modulo p^2**,
\[
\boxed{C(z)\equiv J(z)-pK(z)\pmod{p^2}.}\tag{1}
\]
In addition, for the classical Jacobi polynomial \(P_q^{(0,2q+1)}\), an exact rational polynomial identity is
\[
\boxed{J(z)=(1-z/9)^q P_q^{(0,2q+1)}
\left(\frac{1+z/9}{1-z/9}\right).}\tag{2}
\]
The right side has the removable denominator canceled as a polynomial. Thus with \(U=(8/9)^q\) and \(P=P_q^{(0,2q+1)}\),
\[
\boxed{J(1)=U P(5/4),\qquad J'(1)=U\left(\frac9{32}P'(5/4)-\frac q8P(5/4)\right).}\tag{3}
\]
The first-digit class-selection question is thereby expressed as the finite Jacobi congruences \(P(5/4)=0\) for p mod24=13 and \(9P'(5/4)-4qP(5/4)=0\) for p mod24=5, each modulo p. Those class-selected congruences remain unproved in general; the earlier exclusive-zero lemma is retained at its actual scope.

**Proof.** Since p=8q+5,
\(5/8=-q+p/8\) and \(7/8=-(3q+1)+3p/8\).
For j<=q, expand each Pochhammer product around its negative integer parameter. Its baseline is \((-q)_j(-(3q+1))_j/(j!)^2=\binom qj\binom{3q+1}j\). The linear correction is precisely \(-p h_j\). All factors \(1,\dots,3q+1\) are p-units, proving (1). Identity (2) is the terminating Pfaff transformation followed by the defining Jacobi polynomial sum: on the right, the j-th term reduces to \(\binom qj\binom{3q+1}j(z/9)^j\). Differentiate at z=1 to obtain (3).

## Theorem 2: exact endpoint source and a shorter harmonic differential equation

Write \(\theta=z\,d/dz\), and let
\[
L_0=\theta^2-\frac z9(\theta-q)(\theta-3q-1),\quad
L_C=\theta^2-\frac z9(\theta+5/8)(\theta+7/8).
\]
Then \(L_0J=0\) identically over Q and the shortened original series has **exact** terminal forcing
\[
\boxed{L_C C=-\frac{p(p+2)c_q}{576}z^{q+1}.}\tag{4}
\]
Combining (1) and (4) yields a new first-order deformation equation in F_p[z]:
\[
\boxed{
L_0 K+\frac z{72}(4\theta-6q-1)J
=\frac{c_q}{288}\,z^{q+1}\pmod p.
}\tag{5}
\]
Its right side is a single, nonzero terminal coefficient \(c_q/288\) modulo p; the left side separates the harmonic correction from the deformation of the differential operator. This is an operator identity across **all coefficients**, rather than only the final scalar observation.

At z=1 the following jet identities are exact rational equalities:
\[
\boxed{8J''(1)+(9+4q)J'(1)-q(3q+1)J(1)=0,}\tag{6}
\]
\[
\boxed{8C''(1)+\frac{13}{2}C'(1)-\frac{35}{64}C(1)
=-\frac{p(p+2)c_q}{64}.}\tag{7}
\]

**Proof.** The terminating hypergeometric polynomial \(J={}_2F_1(-q,-3q-1;1;z/9)\) solves \(L_0J=0\). The recurrence for \(c_j\) cancels every interior coefficient of \(L_CC\), leaving exactly the coefficient at \(z^{q+1}\) in (4), where \(q+5/8=p/8\) and \(q+7/8=(p+2)/8\). The exact operator difference is
\[
L_C-L_0=-\frac{pz}{72}(4\theta-6q-1)-\frac{p^2z}{192}.
\]
Substitute \(C=J-pK\) modulo \(p^2\) and divide the resulting divisible polynomial coefficientwise by p; (4) becomes (5). Divide (4) and \(L_0J=0\) by the common factor z and set z=1 to obtain (6) and (7). All divisions are legitimate in the stated localized ring.

## Application to the still-open selected second digit

Let \(F_p=\sum_{k=0}^{p-1}(1/8)_k(3/8)_k z^k/[(k!)^2 9^k]\), \(N=(p+1)/2\), \(u=(8/9)^N\), and \(E_p=(F_p-(1-z/9)^N C)/p\bmod p\), whose complete polynomial construction is in the earlier verified author-side Euler-defect note. Set \(e_0=E_p(1)\), \(e_1=(\theta E_p)(1)\).

On p mod24=13, **assuming the first-digit selector** \(J(1)=0\bmod p\), the selected second-digit cancellation is equivalent to
\[
\boxed{u\,[J(1)/p-K(1)]+e_0=0\pmod p.}\tag{8}
\]
On p mod24=5, **assuming** \(J'(1)=0\bmod p\), the selected weighted cancellation is equivalent to
\[
\boxed{u\,[16J'(1)/p-J(1)-16K'(1)]+e_0+16e_1=0\pmod p.}\tag{9}
\]
These are source-resolved, checkable reductions; their vanishing is not proved here. They separate a short integer Jacobi observable, a short harmonic perturbation and the earlier Euler middle-carry/log correction.

For p mod24=13 the zero of J at z=1 is simple whenever the known exclusive-zero statement applies. For p mod24=5 and q>0, if J'(1)=0 modulo p and J(1) is a unit, (6) gives \(J''(1)=q(3q+1)J(1)/8\neq0\bmod p\), yielding a simple critical-point lift. At p=5, q=0 and J is constant; this is an explicit exceptional case for that critical-point route.

BRC typed carriers: retain each j-indexed original c_j and finite J_j, the two separate reciprocal-harmonic sources in h_j, the operator-deformation forcing, source-exact q and p, and signed value/derivative ports. Projecting to a scalar before applying (5) would erase the distinction between the harmonic and Euler-carry sources.

## Executed finite-exact checks and provenance

Actual Python standard-library run: **PASS 168 primes p<=5000, p mod8=5; 47,813 short unit coefficients**, with coefficientwise comparison of (1), every coefficient of (5), independent binomial/Jacobi evaluation (2)-(3), both exact jets (6)-(7), and the observed class selectors. The class selectors are finite checked, not universally proved. Representative p=373 (q=46): \((J(1),J'(1),K(1),K'(1))=(0,41,332,372)\bmod373\). At p=13, \((0,12,1,1)\); at p=29, \((7,0,22,12)\). The executable checker is d25_short_jacobi_harmonic_port_20261104.py. Local git-blob hash of the executed checker: efd2a44c2965bbef577adf37bc7b318ca358b1fb.

Author-side input: the existing 20261104_hourly20_d25_euler_second_digit_defect.md at immutable Enterprise Math commit 7dc28e2d153f275f71ae027e1e48d9fb8cb23d23. Classical Pfaff/Jacobi identities are inputs, not newly claimed discoveries. The present two short-kernel identities and exact operator forcing are the new scoped deductions.

Native control Source continuation request rhourly20-20261104-2019-cont-read completed SUCCEEDED at source commit 7ae3f50cd0d5b44efb3503ca56789da2d755eb42 as observed 2026-11-04 12:22:50 UTC. It continues to show SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED, route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION and execution_authorized=false. Native original-class H0/B0 divided-power module, [X]U mod p^2, semilinear normalization eta, p373 experiment, and D24 Delta_p-R_p remain distinct pending work; no current service session, claim/open, Source checkpoint, mathematical review or admission is asserted by this author-side note.

Next precise research action: derive a Jacobi or finite-field symmetry proving one of the two first-digit conditions in (3) on each residue class, then prove the appropriate source-resolved second-digit cancellation (8) or (9) via the inhomogeneous equation (5). Preserve frozen p373 native experiment as a separate task-dependent evidence requirement.
