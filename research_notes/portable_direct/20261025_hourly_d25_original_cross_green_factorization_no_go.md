# D25/LIFT — original-vs-terminating Jacobi cross-Green pairing: a scoped first-lift no-go

Date: 2026-10-25; second research unit after third-jet terminal forcing in this TASK_RESEARCH lane. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; stable logical conversation chatgpt-research-hourly-enterprise-math-20260923. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Status AUTHOR-DERIVED / AUTHOR-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No new native CLAIM, OPEN, or checkpoint.

## Exact question and scope

An earlier *self*-Green pairing U with the second terminating Jacobi jet F2 added no independent source information. Does pairing the **original nonterminating-source cutoff polynomial** with the terminating Jacobi U produce a genuinely new source port for the signed Clausen reflected corner? **At the first two normalized p-adic digits, no: the full cross Wronskian is forced by the existing parameter jets.** This is a precise scoped negative result; it does not rule out cross-source pairings that explicitly retain the *ordered cutoff/reflected-tail projection*, which has not entered this pairing.

Let p=6m+1>=7 be prime, N=p-1, h=p/6, theta=z d/dz,

\[
b_n(x)=\frac{(-x)_n(-2x)_n}{(n!)^2},\quad
\Phi(x,z)=\sum_{n=0}^N b_n(x)z^n,\quad
U=\Phi(m,z),\quad V=\partial_x\Phi(m,z),\quad Y=\partial_x^2\Phi(m,z).
\]

The actual original source is S=Phi(-1/6,z)=Phi(m-h,z); at z0=1/2 it evaluates to the original g. Define the signed antisymmetric bilinear W=US'-SU' and the cutoff scalar

\[
C_p=(p-\tfrac56)(p-\tfrac23)b_N(-1/6),\qquad v_p(C_p)=2.
\]

**Theorem A (exact rational cross-source Green identity):**
Over Q[z],

\[
\boxed{z(1-z)W'+[1+(3m-1)z]W=
U\{h(3\theta-4m+2h)S-C_p z^{p-1}\}.}
\]

**Theorem B (first two normalized digits, all p in this class):**
Coefficientwise in the p-local polynomial ring,

\[
\boxed{\frac{W}{p}\equiv-\frac16(UV'-VU')
+\frac{p}{72}(UY'-YU')\pmod{p^2}.}
\]

Thus this cross-Green pairing, at this precision and without an additional independent cutoff source, is a deterministic observer of (U,V,Y). In particular, it supplies no independent value of the separate ordered reflected Clausen tail T_jet,p.

**Inert-point corollary (conditional on the previously accepted first-digit p|g for p=13,19 mod24).** Put z0=1/2. The source translation gives p|U(z0) and p|S(z0). Hence the exact Green right-hand side is divisible by p², and

\[
\boxed{\frac{W(z_0)}p\equiv\frac{V(z_0)U'(z_0)}6\pmod p},\qquad
\boxed{\frac{W'(z_0)+W(z_0)}p\equiv0\pmod p.}
\]

The second identity is a consequence of U(z0)=0 mod p and the homogeneous terminating Jacobi ODE, not an independent relation to T_jet. It does not state that the Wronskian vanishes after normalization.

## Proof

The exact truncated recurrence (n+1)² b_(n+1)(x)=(n-x)(n-2x)b_n(x) implies

\[
\mathcal L_x\Phi(x,z)=-(N-x)(N-2x)b_N(x)z^p,\quad
\mathcal L_x=\theta^2-z(\theta-x)(\theta-2x).
\]

Since S=Phi(m-h,z), the exact operator difference is

\[
\mathcal L_m-\mathcal L_{m-h}=h z(3\theta-4m+2h).
\]

Also L_m U=0 because U is a degree-m terminating hypergeometric polynomial. After division by z, L_m becomes D_m=z(1-z)d²/dz²+[1+(3m-1)z]d/dz-2m². The antisymmetric identity U D_m S-S D_m U equals z(1-z)W'+[1+(3m-1)z]W. Substitute the two source equations to obtain A.

Every b_n(x) for n<p has coefficients in Z_(p), so the source translation has a coefficientwise Taylor expansion

\[
S=U-\frac p6 V+\frac{p^2}{72}Y\pmod{p^3}.
\]

Substitute in W=US'-SU', cancel the U U' terms, and divide by p. This gives B without discarding any source branch. Since n=p-1 has two independent numerator factors divisible by p at x=-1/6, C_p has exact p-valuation 2.

For the inert corollary the earlier independently accepted source input is p|S(z0)=g. The Taylor relation gives p|U(z0). Both W and W' are coefficientwise divisible by p; B at z0 gives W/p=VU'/6 (mod p). In A, the hU term is divisible by p² and the C_p U term by p³. The Green left side at z0 is [W'+(p+1)W]/4, so (W'+W)/p=0 (mod p). Equivalently B gives W'/p=VU''/6; the homogeneous D_m U(z0)=0 with U(z0)=0 and 3m+1=(p+1)/2 forces U''+U'=0 mod p. This proves the claimed redundancy. QED.

## Exact evidence and BRC boundary

The companion check generates the original source S from its own Pochhammer recurrence, and (U,V,Y) from the terminating polynomial's independent parameter-jet recurrence, modulo p³. It verifies coefficientwise source translation, exact pointwise Green identity modulo p³, W/p through its second normalized digit, and the inert specialization on all 35 primes p=1 (mod6), 7<=p<=373 (19 in the target residue classes). All PASS. Example target (p, W(1/2)/p mod p): (13,9), (19,15), (37,15), (43,38), (373,54); Green left-hand side is 0 mod p² in all such cases. These are author checks, not independent math review or native CM experimentation.

BRC resolution COMPOSE_APPLIED: populations are (i) original rank n<p at parameter -1/6 and (ii) terminating Jacobi rank n<=m at parameter m; signs, jet order, parameter translation and p-valuation are preserved. The Wronskian is a legitimate signed bilinear, but its observed information factors through already known jets. The separate rank-threshold/clipped high-rank reflection is not included; **a source-preserving projection is required to add that missing information**, rather than relabeling the pairing as independent Clausen evidence. No original CM H0/B0, [X]U mod p², Frobenius/kappa mapping or all-target supercongruence follows.

## Next discriminating unit

Try a **rank-cutoff-aware**, rather than total-source, cross bilinear: let U_low(z)=sum_(j=0)^m b_j(m)z^j and V_high(z)=sum_(n=2m+1)^(p-1) (b_n''(m)/2)z^n. Keep the exact degree projection P_>=p of U_low*V_high before applying (1+6theta) and evaluating z=1/2. Verify whether a finite recurrence/Gosper or differential creative-telescoping certificate expresses that *signed projected* port in terms of the first-Jacobi derivative observers and universal endpoint forcing. No accidental substitution z^p=z before theta. Failed rational telescopers should be recorded as scoped obstructions, not as proof of mathematical impossibility.

Mother D25/LIFT/JT2 OPEN; frozen pin and Source contributor history unchanged. Current exact native continuation read was blocked by CONTROL_QUOTA; Issue #1558 is the responsible path. Neither this Git artifact nor earlier portable notes are Source predecessor completed units.
