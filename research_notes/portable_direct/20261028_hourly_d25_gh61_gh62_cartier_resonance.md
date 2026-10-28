# D25/LIFT GH-61–GH-62: rational Cartier residue and corrected two-gate Frobenius selection

2026-10-28 Asia/Hong_Kong. TASK_RESEARCH author proof; exact finite-field checks; UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research logical conversation chatgpt-research-hourly-enterprise-math-20260923, not maintenance chatgpt-hourly-enterprise-math-20260921. These are portable author results, NOT a native CLAIM/run/checkpoint/Result or independent acceptance.

Predecessor inputs: the same directory's 20261028_hourly_d25_gh55_gh57_uniform_legendre_port_jets.md and 20261028_hourly_d25_gh58_gh59_frobenius_boundary.md. Distinct later signed CM-isogeny GH-58/59 and torsion GH-60 are not the results below.

## GH-61: global Hermite residue and nonzero Cartier obstruction

Let p=8m+3>=11 be prime, k=F_p,
F(z)=sum_{r=0}^m ((-m)_r)^2 z^r/((2m+2)_r r!),
G(z)=(16z d/dz+5)F(z), D=binom(3m+1,m) in k^*.
F satisfies
L Y=z(1-z)Y''+(5/4-7z/4)Y'-9Y/64=0.  (61.0)
The leading coefficient of F is D^(-1), F(0)=1, F(1) is a unit, and F has only simple roots away from 0,1. For the last claim, at any multiple root r with r(1-r)!=0 the unique formal ODE recursion forces all derivatives of F to vanish through deg(F)<p, contradicting nonzero F.

Set q(z)=z^(-2m-2)(1-z)^(4m+1), and omega=q dz/F^2. Then q'/q=-B/A for A=z(1-z), B=5/4-7z/4. If W=F Y'-F'Y, the exact reduction formulas are
(W/q)'=F L(Y)/(A q),   (Y/F)'=(W/q)(q/F^2). (61.1)

THEOREM 61.1: There is R(z) in k(z) with
q/F^2 = R'(z) - D^2/z.  (61.2)
Proof: At a simple root r of F, the double-pole omega has zero simple-pole residue since F''(r)/F'(r)=-B(r)/A(r)=q'(r)/q(r). The only remaining finite pole is at zero, order at most 2m+2<p. At infinity, q/F^2~-D^2/z; the residue of omega there is +D^2. Hence the residue at zero is -D^2. After removing -D^2 dz/z all residues vanish; every finite pole order is <p and infinity is O(z^-2)dz. Partial fractions integrate term by term with invertible denominators 1,...,p-1. The resulting rational primitive lies in k(z) by Galois descent. No new axiom is introduced.

THEOREM 61.2: For every chart a in F_p\{0,1}, expanding at w=z-a, even if F(a)=0 and the expansion is Laurent,
[w^(p-1)](q(a+w)/F(a+w)^2)=-D^2/a !=0.  (61.3)
A derivative of a Laurent series has zero w^(p-1) coefficient in characteristic p; the 1/(a+w) coefficient there is a^(-p)=a^(-1), so (61.2) proves the formula.

THEOREM 61.3: The complete space of full formal power series Y in k[[w]] satisfying L Y=0 is
{F(a+w)h(w^p):h in k[[w^p]]}. (61.4)
Proof: for a solution S=W/q has derivative zero, so S in k[[w^p]]. Also (Y/F)'=S omega. If S is nonzero choose smallest j with s_j w^(jp) nonzero. At any F root omega has a double pole with zero w^(-1) residue; at a nonroot it is regular. The coefficient of w^((j+1)p-1) in S omega is s_j(-D^2/a); subsequent s_(j+1) can only multiply the vanished w^(-1) residue. This contradicts the vanishing of every Laurent-derivative coefficient of exponent kp-1. Thus W=0, Y/F is a Laurent series of p-th-power exponents, and because F is either a unit or a simple root, no negative p-power exponent can occur for Y regular. The converse follows since d(h(w^p))/dw=0. QED.

## GH-62: correct two-resonance criterion, with exact counterexample

For chart a in k\{0,1}, given (u,v)=(Y(a),Y'(a)), form only the uniquely determined degree-(p-1) jet Y_<p=sum_{n=0}^{p-1} b_n w^n using L coefficient equations n=0,...,p-3. All leading factors a(1-a)(n+1)(n+2) are units. Define the two actual resonant residuals
C_a=-[w^(p-2)] L(Y_<p) = ((9a-3)/4)b_(p-1)+(169/64)b_(p-2);
D_a=-[w^(p-1)] L(Y_<p) = (25/64)b_(p-1). (62.1)
Let W_a=F(a)v-F'(a)u and q_a=q(a). Then
C_a=(1-a)D^2 F(a)W_a/q_a. (62.2)
If F(a)=0,
C_a=0,   D_a=(1-a)D^2 F'(a)^2 u/q_a. (62.3)

Proof of (62.2) if F(a)!=0: since L Y_<p starts at w^(p-2), (61.1) implies S=W/q=c+delta w^(p-1)+O(w^p), c=W_a/q_a and delta=C_a F(a)/(a(1-a)q_a). Now (Y_<p/F)' has no w^(p-1) term; compare (S omega)_(p-1) using omega_(p-1)=-D²/a, omega_0=q_a/F(a)^2. This gives (62.2). By the same computation in the universal rational chart variable a (where a^(-p) replaces a^(-1)), the equality extends to roots of F; no pole appears in the equality itself.

Proof of (62.3): at a root let f1=F'(a)!=0. The Laurent differential omega has leading coefficient (q_a/f1²)w^(-2), zero w^(-1) residue, and Cartier coefficient -D²/a. Since C_a=0, (61.1) implies
S=W/q=c+sigma w^p-D_a f1 w^(p+1)/(a(1-a)q_a)+O(w^(p+2)),
with c=-f1 u/q_a and sigma unrestricted. Coefficient w^(p-1) in the derivative (Y_<p/F)' is zero, hence
0=-c D²/a -D_a/(a(1-a)f1).
Solving gives D_a=(1-a)D² f1² u/q_a, as required.

Consequently
ker_{k²}(C_a,D_a)=k*(F(a),F'(a)) (62.4)
for EVERY ordinary chart a. At a nonroot C is a nonzero scalar of W_a; at a simple root C is identically zero while D is a nonzero scalar of u. In terms of the original labeled G port at a, use v=(g-5u)/(16a). These two actual compatibility equations preserve the F/G observer and do not turn finite data into a full formal solution without this test.

COUNTEREXAMPLE TO A GENERIC SINGLE-TERMINAL SELECTOR: p=43, m=5, a=6, (F(a),F'(a),D,q_a)=(20,37,25,1). The two independent initial pairs (u,v)=(1,0) and (0,1) give
(b_(p-2),b_(p-1),C,D_a)=(22,0,3,0) and (16,0,10,0).
Thus the terminal b_(p-1) vanishes for *every* pair yet earlier C is nonzero. This refutes inferring the first resonance from terminal vanishing at an arbitrary ordinary chart. It does NOT refute the unproved all-prime G_m(9)=0 conjecture or even a special single-terminal statement at a=9. The previous GH-59 sufficiency argument used the n=p-2 equation after imposing b_(p-1)=0 without establishing it; (62.4) replaces that potential gap with a correct unconditional pair criterion.

## Exact executable evidence and source types

Companion standard-library program 20261028_hourly_d25_gh61_gh62_cartier_resonance_check.py uses integer modular arithmetic and true Laurent inversion. Re-executed author checker PASS: all 76 primes 11<=p<2000, p=3 mod8; centers a=2,9,-1, two basis initial pairs each (456 tests of (62.2), 37 F-root charts verifying (62.3)), 14 independent direct Laurent expansions incl roots, and the exact p43 center-6 counterexample. Finite checks supplement the symbolic argument, not independent mathematical review.

BRC COMPOSE_APPLIED: retain original rank, F/G labels, chart a, p-dependent coefficient order, separate first/terminal residuals, full formal vs finite-jet observation and distinct arithmetic/source provenance. This finite-field ordinary-point chart is NOT native X6, W/S, six Hasse, Green R23/R36, physical observer or time coordinate. P000 ACTIVE remains unchanged.

Next scientific obligation: independent CM/Katz/finite-character proof or counterexample of G_m(9)=0 for ALL primes p=11 mod24, not another sum rearrangement. Separately assess the special a=9 terminal-only criterion with exact first-gate dependence; preserve original GH-3 truncated sum, GH-20/21 higher precision, signed square-fiber G, W/S, six Hasse, eta/kappa, p=373 native experiment, and independent Driver review.

Native control: observed backend 0.6.11, research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED, native active jobs 5/5. The current connector has no callable historical lane recovery_status. No new native session, CLAIM, OPEN, checkpoint, Result, review, or changes to historical service sessions, requests, uploads, staging or contributions. Control support awdawmip/enterprise-math#1558 remains. GitHub author evidence is NOT a canonical native Source checkpoint/admission. No scheduler, frequency, phase, enabled-status, notification setting or frozen science pin was changed.
