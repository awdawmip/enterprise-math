# D25/LIFT — Exact two-port differential closure and linear-time prime-field recurrence

Date: 2026-11-11. Status: AUTHOR_PROVED / EXACT_SYMBOLIC_RATIONAL_VERIFIED / FINITE_5130_PRIMES / UNREVIEWED / NOT_ADMITTED. Parent objective ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION remains OPEN; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Author-side portable evidence, not a native CLAIM/checkpoint/Result/review. Existing H40 cubic-carrier and fixed-orbit contributions are antecedents, not new credit.

## Theorem (all m>=0, both epsilon branches, over Q[[z]])

Let K_m^(e)(X)=sum_{k=0}^m binom(m,k)binom(2m+e,k)X^k, A_m^e=K_m^e(1/2), B_m^e=(1-6e)A_m^e+6(K_m^e)'(1/2), and F_e(z)=sum_m A_m^e z^m, G_e(z)=sum_m B_m^e z^m.

Exact differential identities:

(D0) (5-z)G_0=(5+11z)F_0+12(3z+2)zF_0'.

(D1) (8-5z)G_1=(169z-40)F_1+204z²F_1'.

Write D(z)=2z²-71z+16. Then:

(ODE0) z(z-5)D(z)F_0''+(5z³-106z²+702z-40)F_0'+(z²-4z+80)F_0=0.

(ODE1) z(5z-8)D(z)F_1''+(35z³-782z²+1744z-192)F_1'+15(z²-8z+32)F_1=0.

F_0(0)=F_1(0)=1. With A_n=B_n=0 for negative n, the coefficient recurrences are:

(R0) 40(n+1)(2n+1)A_(n+1)^0 = (371n²+331n+80)A_n^0+(-81n²+137n-60)A_(n-1)^0+(2n²-5n+3)A_(n-2)^0.

(R1) 64(n+1)(2n+3)A_(n+1)^1 = (648n²+1096n+480)A_n^1+(-371n²+331n-80)A_(n-1)^1+(10n²-15n+5)A_(n-2)^1.

(P0) 5B_n^0=(24n+5)A_n^0+(36n-25)A_(n-1)^0+B_(n-1)^0.

(P1) 8B_n^1=-40A_n^1+(204n-35)A_(n-1)^1+5B_(n-1)^1.

B_0^0=1, B_0^1=-5. The equations for n=0 hold.

## Derivation

The original binomial polynomial is [u^m]((1+u)(1+xu)²)^m(1+xu)^e. For P(u,x)=(1+u)(1+xu)² and the formal root u=zP(u,x), Lagrange inversion gives

sum_m K_m^e(x) z^m = (1+xu)^e/(1-z∂_uP(u,x)).

At x=1/2 put u=2s, d=1-s-4s²; then 2s=z(1+2s)(1+s)² and F_e=(1+2s)(1+s)^(e+1)/d. Moreover z(d/dz)=s(1+2s)(1+s)/d * (d/ds). Differentiate the kernel at fixed z with respect to x and use G_e=(1-6e)F_e+6∂_x F_e. This gives

G_0=(1+s)(1+2s)(1+22s+89s²+56s³+16s⁴)/d³;

G_1=(1+s)²(1+2s)(-5+46s+119s²-40s³-80s⁴)/d³.

Substitution and polynomial denominator clearing prove (D0),(D1). Twice applying the displayed z-derivative and clearing denominators prove (ODE0),(ODE1). Coefficient extraction gives (R0),(R1),(P0),(P1). All identities are over Q, not finite-prime guesses.

## Finite-field corollary and validation

For every prime p>5 uniquely p=6m+1+4e, all denominators in (R0)/(R1) up to index n=m-1 are nonzero modulo p: n+1<p and 2n+3<p. Also 5 and 8 are invertible. Thus (A_m^e,B_m^e) mod p is computable in O(m) finite-field arithmetic using an O(m) inverse table and a constant-size live recurrence frontier, without factorial or binomial reconstruction. This is an operation-count statement, not a sublinear bit-complexity claim.

Independent original-binomial exact rational checks covered all 0<=m<=80 in each branch (162 port identities, 160 ODE recurrence identities). Exact symbolic simplification established two differential identities and two ODE identities. A new recurrence-based exact modular sweep covered all 5130 primes 7<=p<=50000: 2583 had A_m=0; 2547 had B_m=0; no two-zero/nonzero-nonzero case; the previously observed quadratic selector chi_{-6}(p) had no exceptions in this *finite* range. The universal chi-selector proof remains open. Examples: p=7:(A,B)=(2,0), p=13:(0,6), p=19:(0,12), p=157:(0,80), p=373:(0,171).

BRC observer lease: the complete epsilon-labelled coefficient prefix A_0..A_m plus the explicit differential transfer reconstructs B_0..B_m under finite-prefix/port-reading operations. The single endpoint A_m is not assumed sufficient. Existing cubic algebraic carrier is COMPOSE_APPLIED, not replaced by a new top-level BRC mechanism.

Next science: derive or refute an exact residue-class identity using (R0)/(R1),(P0)/(P1) at the special m to force the chi_{-6} port selector; preserve the original D25 second-digit H0/B0 and Frobenius obligations.

UR V2 original bundle: original 94687-byte artifact with SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76 remains unrecovered after local, GitHub and targeted Drive checks. Prior UR mathematics is not recomputed. The current gateway returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false for recovery, prior receipt and status; no Source write or identity/CLAIM is asserted.

Antecedent (author-side) research_notes/portable_direct/2026-11-11_h40_d25_two_port_cubic_algebraic_carrier_author_portable.md and research_notes/portable_direct/2026-11-11_h40_d25_mobius_fixed_orbit_exact_ports_author_portable.md. Full local three-file exact packet is available with this run.