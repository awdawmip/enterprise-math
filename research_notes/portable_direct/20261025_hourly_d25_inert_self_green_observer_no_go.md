# D25/LIFT — exact Jacobi self-Green identity and inert-point information-loss certificate

2026-10-25; TASK_RESEARCH portable author result; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CHECKPOINT. D25/LIFT/JT2 still OPEN.

## Question / scoped negative outcome

Does the standard self-adjoint Green/Wronskian pairing of the original terminating Jacobi polynomial and its second parameter jet provide a **new independent signed identity** capable of canceling the nonzero terminal forcing at the inert D25 observer z=1/2? Answer: **No, not by self-pairing alone.** Below is an exact polynomial certificate showing that the entire pairing reduces to the original second-jet differential equation; on the inert mod-p fiber the forcing information vanishes under multiplication by the terminating source, while its first normalized lift has a precise residual port. This rules out a scoped shortcut; it does not rule out a genuinely cross-source Jacobi/Clausen telescoper.

Set p=6m+1>=7 prime, b_n(x)=(-x)_n(-2x)_n/(n!)^2 and
\[
U=F_0(z)=\sum_{n=0}^{p-1}b_n(m)z^n,\quad
V=F_1(z)=\left.\partial_x\sum_{n<p}b_n(x)z^n\right|_{m},\quad
Y=F_2(z)=\left.\partial_x^2\sum_{n<p}b_n(x)z^n\right|_{m}.
\]
All are rational polynomials p-integral coefficientwise. Define
\[
D_my=z(1-z)y''+[1+(3m-1)z]y'-2m^2y,\quad
\theta=z\frac{d}{dz},\quad K_p=-40m^2\,b_{p-1}''(m)/2.
\]
The exact previous source relations are \(D_mU=0\) and
\[
D_mY=-2(3\theta-4m)V+4U+K_pz^{p-1}.
\]

## Result I: exact signed Green identity (all primes, rational polynomials)

Define the antisymmetric provenance-preserving bilinear \(\mathcal W=UY'-YU'\). Then
\[
\boxed{\quad
z(1-z)\mathcal W'+[1+(3m-1)z]\mathcal W
=U\bigl[-2(3\theta-4m)V+4U+K_pz^{p-1}\bigr].\quad}
\tag{1}
\]
This is an exact polynomial identity, not just a mod-p observation. It follows by expanding \(U D_mY-Y D_mU\); the second derivative terms combine as \(z(1-z)\mathcal W'\) and the zeroth-order terms cancel. Equivalently, with \(\mu=(1-z)^{-3m-1}\), the exact rational Lagrange identity is
\[
\frac{d}{dz}\left[z(1-z)^{-3m}\mathcal W\right]
=(1-z)^{-3m-1}U[-2(3\theta-4m)V+4U+K_pz^{p-1}].
\]
The latter introduces an auxiliary rational-function port; the polynomial form (1) is the primary p-local certificate and requires no evaluation at a pole.

At z=1/2, direct algebra yields
\[
[z(1-z)\mathcal W'+(1+(3m-1)z)\mathcal W]_{z=1/2}
=
U_0[(\theta^2+3m\theta)Y]_0-Y_0[(\theta^2+3m\theta)U]_0,
\]
where subscript 0 denotes evaluation at 1/2. Because \(D_mU=0\) gives \([(\theta^2+3m\theta)U]_0=2m^2U_0\), the left side equals
\[
U_0[(\theta^2+3m\theta-2m^2)Y]_0.
\]
Thus (1) at the point is *exactly the original second-jet ODE multiplied by U_0*. It adds **no independent constraint** on the unpaired Clausen reflected tail and is not a proof of LIFT.

## Result II: inert-point loss and minimal retained first lift

For the target classes p=13,19 (mod24), consume (do not re-prove) the separate accepted first-digit D25 input \(p\mid g\), with the source translation \(g=U_0-(p/6)V_0\pmod{p^2}\). It follows \(p\mid U_0\) in the p-local ring. Let \(u_p=U_0/p\in\mathbb Z_{(p)}\) and let \(G_p\) be the left side of (1) evaluated at 1/2. Then:
\[
\boxed{\quad G_p\equiv0\pmod p;\qquad
\frac{G_p}{p}\equiv
u_p\bigl[-2(3\theta-4m)V_0-4\bigr]\pmod p.\quad}
\tag{2}
\]
Indeed \(G_p=U_0[-2(3\theta-4m)V_0+4U_0+K_p2^{1-p}]\), while the previously established source endpoint \(K_p\equiv-4\bmod p\) and Fermat's theorem yield \(K_p2^{1-p}\equiv-4\bmod p\). The \(4U_0\) term is divisible by p.

Consequently **a mod-p self-Green pairing erases the nonzero endpoint port**, even though the original second-jet ODE retains it. The minimal first-lift repair for this *particular observed product* is the residue \(u_p\) together with the existing V/derivative port. This is a sufficient representation of the normalized product, not a claim of unique or globally minimal state, and \(u_p\) is not asserted nonzero for all target primes. The normalized pairing is still the original ODE times \(u_p\); it does not create a new Clausen relation.

## Explicit evidence and kill criterion

The adjacent checker uses p-local Taylor jets of the original Pochhammer recurrence, retains the signed parameter derivatives, and independently compares the whole p^2 source identity with the normalized inert observer. It passed all 35 primes p=1 (mod6), 7<=p<=373; 19 target-class primes additionally satisfied (2) with exact residues. Examples (p, u_p mod p, G_p/p mod p): (13,7,5), (19,6,7), (37,21,36), (43,4,9), (373,340,140). A distinct rational-polynomial check of the complete Green identity passed p=7,13,19,31,37,43. Finite checks are author corroboration, not universal proof or independent review. Result I has algebraic proof; Result II is **conditional on the named first-digit certificate**, rather than being a new all-prime inertness theorem.

BRC: COMPOSE_APPLIED with actual signed bilinear source ports and explicit observer/allowed-operation horizon. Erasure is demonstrated on the inert quotient U_0 mod p, and the repair preserves p-adic valuation and source rank. Green self-pairing is a valid identity but **not an independent direction**; counting it as an additional proof would double-count the same ODE. Its scalar z-variable belongs to an auxiliary formal hypergeometric model; no native X6 geometry, time dynamics or CM Frobenius is inferred.

## Next exact action

KILL as an independent proof route: any future attempt to close \(\Delta_p-R_{\mathrm{ref},p}\) with only the terminating U/Y self-Green identity (without an additional source observer) is redundant and inert at the declared mod-p point. CONTINUE with a *cross-source* signed bilinear/telescoping certificate directly coupling the Clausen reflected tail \(T_{\rm jet,p}\) to the original Jacobi source while preserving \(K_p z^p\) and, when needed, the higher precision formula from 20261025_hourly_d25_terminal_jet_p3_harmonic_fermat.md. Still missing: native original-class CM H_0/B_0, [X]U mod p^2, semilinear normalization/direction, kappa map, independent review and fresh native Source authority. No new claim/run/checkpoint is represented by this portable artifact.
