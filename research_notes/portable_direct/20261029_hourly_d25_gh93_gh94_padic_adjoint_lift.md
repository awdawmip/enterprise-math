# D25/LIFT GH-93–GH-94 — exact p-local adjoint lift and sharp signed-observer defect

2026-10-29 · author Research lane: chatgpt-research-hourly-enterprise-math-20260923.
**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.** This is not a Source CLAIM, authorized OPEN, native checkpoint, Result or independent review. Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (not the mutable control-head). Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION / D25/LIFT/JT2 remains OPEN; the exact historical task/publication is RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / TP2-B6F4FC938FF94941C1B7.

## Original sources and type constraints

Let p=4d+3>=7 be prime, R=Z_(p), theta=z d/dz. Keep the original finite source S(z)=sum_{i=0}^d c_i z^i and distinct reflected source U(z)=sum_{j=0}^d h_j z^j. Both begin at c_0=h_0=1, with exact rational recurrences

c_(i+1)/c_i=(4i+1)^3/((4i+2)(4i+3)(4i+4)),
h_(j+1)/h_j=(4j+3)^3/((4j+4)(4j+5)(4j+6)).

All factors in their numerators and denominators for index <d are p-units. Hence c_i,h_j, and c_d,h_d lie in R^×. All integrations below divide only by integers 1,...,2d+1=(p-1)/2, also p-units. Define

L_- = theta(theta-1/2)(theta-1/4)-z(theta+1/4)^3,
L_+ = theta(theta+1/4)(theta+1/2)-z(theta+3/4)^3.

Let B(X,Y) be the *ordered*, source-faithful GH-84 concomitant

B(X,Y)=(1-z)[Y theta²X-(theta Y)(theta X)+(theta²Y)X]
 +(z-3)Y theta X/4+(3-5z)(theta Y)X/4+(2-7z)YX/16.

Write B=B(S,U), V=B(S,theta U), W=64V+40B, H=(8theta+5)U, J=theta H and T=(8theta+1)S. H here denotes the reflected Laurent double-pole observer, NOT an elliptic Hasse invariant.

## GH-93: exact rational/p-local terminal defects and finite-source reconstruction

**Theorem 93.1 (exact for all stated p, not merely mod p).** With
alpha=-(p-2)^3 c_d/64 and beta=-p^3 h_d/64,

L_- S = alpha z^(d+1),       L_+ U = beta z^(d+1).            (93.1)

Proof: the interior coefficients vanish over Q by the exact source recurrences. The terminal coefficients are -(d+1/4)^3 c_d and -(d+3/4)^3 h_d, respectively; since d=(p-3)/4 they equal alpha and beta. Note v_p(alpha)=0 and v_p(beta)=3, the latter sharply because h_d is a unit.

The exact logarithmic adjunction L_-^dagger=-L_+ and GH-84's algebraic Lagrange identity give theta B=U L_-S+S L_+U. Because B(0)=1/8 and the degree is at most 2d+1<p, coefficientwise integration is valid in R[z] and uniquely yields

B(z)=1/8 + alpha sum_j h_j z^(d+1+j)/(d+1+j)
           + beta sum_i c_i z^(d+1+i)/(d+1+i).               (93.2)

Set Q(theta)=(theta+3/4)^3. The exact commutator [L_+,theta]=zQ(theta) implies
theta V=alpha z^(d+1)theta U + beta(d+1)z^(d+1)S + z S Q(theta)U.
Since V(0)=0, direct finite integration proves

W(z)=5
 +64 sum_{i,j=0}^d c_i h_j (j+3/4)^3 z^(i+j+1)/(i+j+1)
 +8alpha sum_{j=0}^d (8j+5)h_j z^(d+1+j)/(d+1+j)
 +beta[64(d+1)+40] sum_{i=0}^d c_i z^(d+1+i)/(d+1+i).       (93.3)

This is an *exact* p-local lift of GH-91 (91.6), preserving original/reflected branch labels and the two terminal defects.

Let R_p(z)=sum_j(8j+5)h_j z^(d+1+j)/(d+1+j) and M_p(z)=sum_i c_i z^(d+1+i)/(d+1+i). If W_naive is the mod-p GH-91 finite-source formula evaluated unchanged on the rational coefficients at higher precision, then the exact difference is

W-W_naive = c_d(-3p/2+3p²/4-p³/8)R_p - p³h_d(2p+7)M_p/8.  (93.4)

In particular W-W_naive = -3p c_d R_p/2 (mod p²). The omitted first correction is **not** generally zero: at target z=9, p=7 gives W(9)=26 and W_naive(9)=5 modulo 49 (difference 21=3p), and p=11 gives 20 and 108 modulo 121 (difference 33=3p). This is a counterexample to a *naive p² lift of the source formula*, not to GH-3's mod-p conjecture.

## GH-94: universal identity and exact p³ obstruction

Define the GH-91 full signed expression

R91(S,U)=(z-1)JT+[2(z+3)J+(z+15)U/8]S
       +H[8(1-z)theta²S+2(z-3)theta S+(15z+5)S/8].

**Theorem 94.1 (universal differential identity).** For *arbitrary* S,U polynomials over any commutative ring with 2 invertible,

64 B(S,theta U)+40 B(S,U)-R91(S,U) = 64 S L_+U.           (94.1)

Proof: substitute the ordered B formula into the left; its coefficient of theta²S is 8(1-z)(8theta U+5U)=8(1-z)H. Collect the coefficients of theta S and S and replace J by (8theta²+5theta)U. The uncancelled expression is exactly 64S[(1-z)theta³U+(3-9z)theta²U/4+(2-27z)theta U/16-27zU/64] = 64 S L_+U. This is a polynomial identity without using recurrences or the desired special-value vanishing. A separate SymPy calculation checked (94.1) with arbitrary free jets.

Specializing to the original S,U gives

W-R91(S,U) = -p³ h_d z^(d+1) S.                          (94.2)

Therefore GH-91's homogeneous signed syzygy is valid **modulo p³**, but not modulo p⁴: the coefficient of z^(d+1) in its defect equals -p³ h_d (since S(0)=1), and h_d is a p-unit. The global p-adic valuation of that coefficient is **exactly 3 for every p**. This is a sharp theorem, not an inference from finite sample verification.

**Theorem 94.2 (signed derivative repair).** From the exact two Lagrange identities and [L_+,theta]=zQ(theta),

theta W = 8H(L_-S) + S(64theta+40)(L_+U) + 64zS Q(theta)U. (94.3)

The differential operator (64theta+40) acts on (L_+U) *before* multiplication by S. Substituting (93.1) yields

theta W = c_d(1-3p/2+3p²/4-p³/8)z^(d+1)H
        -p³ h_d(2p+7)z^(d+1)S/8
        +64zS(theta+3/4)^3 U.                               (94.4)

Modulo p this recovers GH-92 (92.1). Beyond p it retains the necessary original/reflective source corrections. **Neither H(9)=0 modulo p² nor T(9)=0 modulo p² follows from these identities alone.** GH-3 remains OPEN; no native p=373 experiment is claimed.

## Independent verification and observer classification

An actually executed Python standard-library exact residue-ring program constructed full polynomials S,U,B,V,W,L_-,L_+, the source sums and derivative terms in Z/(p^4)Z for **86 primes 7<=p<1000, p≡3 mod4**. Equations (93.1)–(93.5) and (94.2),(94.4) passed complete coefficient comparisons; the second-digit source correction at z=9 was nonzero in all 86 samples. A separate exact SymPy free-jet computation passed (94.1) over Q[z]. These are author checks of the algebra and finite-precision implementation, not independent mathematics review or all-prime GH-3 arithmetic proof.

BRC: COMPOSE_APPLIED to the existing signed-jet, two-source family. Population (p,z,original i,reflected j), carrier p-local coefficient/valuation vectors, observer reductions mod p^k and theta-jets; preserve nonzero p and p³ residual channels, phase/sign, index provenance and permissible future specialization. Mod-p compression discards these higher-digit defects. This is an external arithmetic chart, NOT a replacement for P000 native 6D Cell semantics; six native spatial axes, 120-degree native orthogonality and one time dimension remain assumed.

**Next action:** independently evaluate source-labelled R_p(9), M_p(9) and the signed GH-92 eigenport via genuine p-adic CM/Jacobi/WZ arithmetic, keeping the new p² correction in the U(9)≠0 and U(9)=0 fibers. Preserve GH-83 Laurent B_0L, GH-20/GH-21 second-digit moments, W/S, Hasse ports, R23/R36 and native p=373 as separate obligations. The old session/request/staging and current Source ownership must be reconciled through existing support #1558, not re-created from this portable proof; status remains UNREVIEWED / NOT_ADMITTED.