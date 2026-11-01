# D25 / SECOND-DIGIT-LIFT — Fixed-CM Hasse–Gegenbauer first-order bridge

2026-10-29. AUTHOR-SIDE / PROVED FINITE ALGEBRAIC THEOREM / EXECUTED 194-PRIME MODULAR CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_EXECUTED.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Research conversation chatgpt-research-onhour-enterprise-math-20260923; not the maintenance lane. Prior fixed-argument Legendre parameter jet: 8e61fa5c5a03e8826147089ea4ffde7624534c77. Prior Legendre Frobenius carry: c423e6b9802ca23a453b85c3018ea0b818aa5332.

## Theorem (every odd prime p>3; exact unchanged CM argument)

Put e=floor((p-1)/4), k=(p-1)/2 and use the quadratic coefficient ring R=(Z/p²Z)[x]/(x²-8/9). Define t=(1-x)/2, so 36t²-36t+1=0 and z=4t(1-t)=1/9 exactly. Let

A(T)=1-2xT+T²,  B_e(x)=[T^e]A(T)^k,

H_p(t)=sum_{j=0}^{e} binom(k,2j) binom(2j,j) ((1-t)/4)^j,

h_e=sum_{i=1}^e 1/i, and

J_e(x)=sum_{j=1}^e [(-e)_j(e+1)_j/(j!)²] (sum_{i=0}^{j-1}1/(e+1+i)) ((1-x)/2)^j.

All denominators are p-units because 2e<p. Then there is a whole-polynomial congruence evaluated in R:

**B_e(x) - (-1)^e H_p(t) = -(p/2)[h_e P_e(x)+J_e(x)] (mod p²).** (1)

This explicitly bridges the previous finite Frobenius binomial B_e to the *actual external* CM/Hasse/Jacobi polynomial H_p, with the first-order mismatch retained. It neither identifies B_e and H_p as equal modulo p² nor shifts the original observation.

## Proof

Use the classical finite Gegenbauer generating identity C_e^lambda(x)=[T^e](1-2xT+T²)^(-lambda). Exactly B_e=C_e^{(1-p)/2}. Taylor expansion in lambda about lambda=1/2 is p-integral (e<p) and yields B_e=P_e-(p/2)(partial_lambda C_e^lambda)|_{1/2} modulo p².

The exact classical Gegenbauer-to-Jacobi identity is
C_e^lambda(x)=((2lambda)_e/(lambda+1/2)_e) P_e^(lambda-1/2,lambda-1/2)(x).
Its derivative at 1/2 is h_e P_e+partial_alpha P_e^(alpha,0)|0+partial_beta P_e^(0,beta)|0.

For the identical finite external Hasse polynomial the terminating Jacobi identity gives
H_p(t)=P_e^(0,-p/2)(2t-1)=P_e^(0,-p/2)(-x)=(-1)^e P_e^(-p/2,0)(x).
First-order expansion in alpha gives (-1)^e H_p=P_e-(p/2)partial_alpha P_e^(alpha,0)|0. Subtract: the alpha port cancels *exactly*. The beta derivative is J_e by the terminating hypergeometric expansion
P_e^(0,beta)(x)=sum_{j=0}^e (-e)_j(e+1+beta)_j/(j!)² ((1-x)/2)^j.
This proves (1) without analytic or p-adic convergence assumptions. The identity is algebraic in x prior to using x²=8/9.

## New direct original-K transport (p=5,7 mod 8)

For these branches e is odd. Write S_e=h_eP_e+J_e. The previously PROVED fixed-argument Legendre and Frobenius results combine with (1) to give the FOUR-PORT formula

K_b(1/9) =
   -x^p H_p(t)
   -(p/2)x^p S_e(x)
   -(p/2)(C_{p+e}+3x^p C_e)
   +(5p/8)G_{r,b}(1/9)    (mod p²). (2)

Q_p,C_j and G_{r,b} have exactly their source definitions in the prior cited notes. The first two terms may separately have x-components. Only their properly composed value equals the scalar x^p B_e. This is a matched finite CM/Hasse source transport, *not* an all-prime Root2 proof.

## Executed exact residues

Companion checker independently evaluates finite binomial Hasse, the A^k coefficient by a polynomial recurrence, ordinary Legendre by another recurrence, and the beta-Jacobi parameter derivative by a terminating rising-factorial sum in the full 2-component ring. PASS for all 194 primes 5<=p<1200.

p | -x^p H (scalar,x) | -(p/2)x^p S (scalar,x) | composed x^p B | H_const+2H_x (mod p²)
13 | (52,52) | (13,117) | (65,0) | 0
23 | (92,207) | (46,322) | (138,0) | 115
37 | (1332,1110) | (259,259) | (222,0) | 0
373 | (10817,10444) | (114511,128685) | (125328,0) | 0

At 373 the nonzero x ports sum to 139129=p², while scalar ports sum to 125328=336p. Together with the independently computed earlier carry 105932=284p and original parameter jet 46998=126p this reproduces K_b(1/9)=0 (mod 373²) by 336+284+126=746=2p. This is ONE exact prime certificate, not an infinite-prime theorem.

For odd e, writing B_e=x*b_e, formula (1) makes the earlier Hasse line H_const+2H_x=0 equivalent, whenever p|b_e and H is p-divisible, to
2(b_e/p)+(S_const+2S_x)/2=0 (mod p). (3)
The 13-mod-24 rank-line remains a **finite observed conjecture**, not a proven all-prime consequence. The 23-mod-24 branch is an explicit contrast: at p=23 its line residue is 115, despite original K_b=0 modulo 23² in the finite observed data.

## Source, BRC, and actual next work

BRC COMPOSE_APPLIED: carrier includes branch x, fixed z, Hasse, B_e, P_e, Jacobi beta jet, Gegenbauer jet, Frobenius Q/C signed carry, original G, integer valuations and observer order. Reduction to a scalar is safe only after the entire ring identity, not term-by-term; the p=373 nonzero cancelling x ports are a concrete witness. External x is not a new P000 spatial axis; ACTIVE six-axis/one-time worldview and frozen Source pin unchanged.

Result is AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED. All-prime Root2 and 216/2304 mod p³ bridge remain open. Native #1559 remains OPEN/UNASSIGNED as read 2026-10-29, requiring actual original-class p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius, signed Green/Hesse, kappa and Delta_p-R_p. Scalar CM/Gegenbauer work is NOT that native experiment.

NEXT SCIENTIFIC ACTION: Prove or falsify 13-class scalar four-port cancellation in (2) by actual CM/finite character-sum or matched WZ evaluation, with independent rank-line obligation (3) and 23-class counter-control; do not repeat already completed finite transforms. Native #1559 executor/acceptance remains parallel top operational obligation.

CONTROL CONTINUATION: Research conversation above, no verified own session/claim/run/target_request_id; Site tool exposed no callable recovery_status and reports static read-only/research_authority_granted=false. No presumed empty queue or Source CLAIM/checkpoint/Result/review. This artifact and checker are author-side durable evidence only; formal Source admission still requires authenticated source continuity, true owner and independent review.