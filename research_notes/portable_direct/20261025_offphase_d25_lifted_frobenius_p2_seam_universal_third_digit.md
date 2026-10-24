# D25/LIFT: lifted Frobenius seam and universal third-digit correction

2026-10-25 | TASK_RESEARCH | PORTABLE AUTHOR PROOF / AUTHOR EXACT CHECK / UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent D25/LIFT/JT2 OPEN. Frozen scientific source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3. This is an author-side refinement of the published original-factor WZ five-port observer, not an original-class CM/DP comparison or an independent review.

## Inherited definitions, exact port identities

Let p=6m+1>=13 be prime, n=2m, and work over Z_(p)[[z]]. The preexisting exact series Q_p(z) from 20261025_offphase_d25_source_factor_jet_all_precision.md satisfies
\[
Q_p(z)=2mC(z)F_U(z)+\frac{3z}{220}B(z)F_\sigma(z),\qquad Q_p(p)=\frac{S_{m+1}-S_m}{p}.
\]
From 20261025_offphase_d25_frobenius_sparse_fiveport_seam_modp.md, let
\[
A_p(z)=2mC(z)K_U(z),\quad L_p(z)=\frac{3z}{220}B(z)P_{\rm base}(z),\quad H_p(z)=A_p(z)+L_p(z).
\]
Here K_U is exactly F_U with its full j=1,...,p-2 squared factor removed and (1-z)^(-2) inserted; P_base is exactly F_sigma with its j=1,...,p-1 squared factor removed. Original C,B, and the five distinct factorial port origins are unchanged. In particular C(0)=-2, A_p(0)=-4m and L_p(0)=0.

Set
\[
T_p(z)=\prod_{j=1}^{p-1}(1+z/j),\quad E_p(z)=1-z^{p-1},\quad
R_p(z)=\frac{1-z}{1+z/(p-1)}.
\]

## Theorem

**Exact integral lift.** For every such p,
\[
\boxed{Q_p(z)=T_p(z)^2\{R_p(z)^2A_p(z)+L_p(z)\}.}\tag{1}
\]
The polynomial
\[
D_p(z)=(T_p(z)-E_p(z))/p\in\mathbb Z_{(p)}[z]
\]
is well defined and integral. Coefficientwise over F_p[[z]], **to every degree**, the first lifted seam is
\[
\boxed{
\frac{Q_p-E_p^2H_p}{p}
\equiv
2E_p\left(D_pH_p-E_p\,\frac{zA_p}{(p-1)(1+z/(p-1))}\right)\pmod p.
}\tag{2}
\]
This has no forbidden division by coefficient index d, even for d=p or p^2.

**Sharp low-coefficient defect.** Write H_{p-1}^{(1)}=\sum_{j=1}^{p-1}1/j. There is the exact rational identity
\[
\boxed{[z](Q_p-E_p^2H_p)=4p/3-8mH_{p-1}^{(1)}.}\tag{3}
\]
Since H_{p-1}^{(1)}=0 mod p^2 in Z_(p), it follows that
\[
\boxed{[z](Q_p-E_p^2H_p)/p=4/3\pmod p\ne0.}\tag{4}
\]
The mod-p seam in the previous note first changes the degree-(p-1) coefficient by -4/3. The *new* mod-p^2 seam differs already at degree one by p*(4/3) modulo p^2. These are distinct coefficient-modulus statements.

**Universal compressed third digit.** Evaluating the original source jet at its actual argument z=p gives
\[
\boxed{\frac{S_{m+1}-S_m}{p}\equiv H_p(p)+\frac43p^2\pmod{p^3}.}\tag{5}
\]
The constant is universal for this particular compressed WZ source representation, not a native CM/DP matching scalar.

## Proof

The original old-edge full product is \(\prod_{j=1}^{p-2}(1+z/j)^2\). The compressed old edge has (1-z)^(-2). Multiplication by T_p(z)^2 R_p(z)^2 cancels exactly the extra j=p-1 factor and the compressed (1-z)^(-2). The full first tail equals T_p(z)^2 P_base(z). This proves (1) *as an exact identity*, retaining the old-edge versus four-tail provenance.

Over F_p the reciprocals of j permute the nonzero field, so T_p(z)=E_p(z) mod p in F_p[z]; denominators are p-units. Thus D_p is integral. The following rational identity is exact:
\[
R_p(z)=1-\frac{pz}{(p-1)(1+z/(p-1))}.
\]
Substitute T_p=E_p+pD_p and this R_p into (1), expand modulo p^2, subtract E_p^2H_p and divide coefficientwise by p. This proves (2).

Differentiate (1) at z=0, using T_p(0)=R_p(0)=E_p(0)=1, T'_p(0)=H_{p-1}^{(1)}, R'_p(0)=-p/(p-1), E'_p(0)=0, A_p(0)=-4m, L_p(0)=0. The derivatives of A_p+L_p cancel against that of E_p^2H_p, and
\[
[z](Q_p-E_p^2H_p)
=2(-4m)H_{p-1}^{(1)}+2(-4m)(-p/(p-1))
=-8mH_{p-1}^{(1)}+4p/3.
\]
This is (3).

For clarity, the harmonic congruence needed here has a short proof for p>3. Pair j and p-j to get
\[
H_{p-1}^{(1)}
=p\sum_{j=1}^{(p-1)/2}\frac{1}{j(p-j)}
\equiv-p\sum_{j=1}^{(p-1)/2}j^{-2}\pmod{p^2}.
\]
The half-sum equals half the full sum modulo p; the full inverse-square sum over F_p^* is zero because p-1 does not divide p-3. Therefore H_{p-1}^{(1)} is divisible by p^2 and (4) holds.

Every coefficient of Q_p-E_p^2H_p is divisible by p, and its constant coefficient vanishes. Evaluated at z=p, degrees >=2 are divisible by p^3. The linear term (3) times p is 4p^2/3 modulo p^3, while E_p(p)^2=(1-p^{p-1})^2=1 mod p^3. Combine with inherited exact Q_p(p)=(S_{m+1}-S_m)/p to obtain (5). QED.

## Executed finite regression and limits

A local author-side standard-library Python calculation separately built the original complete-factor old edge and first tail, the compressed factors, and exact rational C(p),B(p). All arithmetic used integers, fractions and modular inverses only of known p-units modulo p^3. The checked normalized residues (Q_p(p)-E_p(p)^2 H_p(p))/p^2 modulo p were:

| p | 13 | 19 | 31 | 37 | 43 | 61 | 67 | 73 | 79 | 97 | 103 | 109 | 127 | 139 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| residue | 10 | 14 | 22 | 26 | 30 | 42 | 46 | 50 | 54 | 66 | 70 | 74 | 86 | 94 |

14/14 agree with 4*inverse(3) modulo p. This is a focused **author source-factor check**, not a separate original-factorial reconstruction, formal proof checker, independent Driver pass, or native CM experiment. The universal assertion rests on the exact algebra above.

BRC/Enterprise-coordinate interface: the carrier explicitly preserves the original five-source labels and p-valuation before scalar H_p readout. This representation map is an external p-adic arithmetic observer, not a P000 native-X6 plane, positive-mass BRC dynamics or no-loss CM correspondence.

## Current recovery state and next precise action

Original genuine WZ identity, all-precision source-factor construction and earlier mod-p Frobenius seam are inherited and not recredited. New author-side unit: exact lift (1)-(2), coefficient identity (3)-(4), and third-digit correction (5).

Latest available GitHub native checkpoint pointer identifies another Researcher session, not ours; no takeover. The attempted current exact canonical continuation returned CONTROL_QUOTA. Hence this file is portable evidence only: no own registered service identity, CLAIM, OPEN, native Source checkpoint, Result, audit, review or admission. Current-input seeds, if encountered later, require completed_units=[] and full readback of initial inputs before typed preparation. Do not repeat unknown mutations.

The source-required native hard input remains the actual same-prime same-class normalized H0/B0 divided-power/Frobenius representative, [X]U mod p^2, semilinearity direction, leading factor and the c_p/kappa_p bridge to Delta_p-R_p. The separate UR V2 four-file original remains UNVERIFIED: historical length 94687 and SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76, not replaced by the WZ note. Next legitimate owner/Driver action: reconcile original receipts/staging; obtain source continuation and winning claim if permitted; attach this already-proved portable unit with correct contributor/provenance (no re-proof), and seek genuinely source-selected native CM data.