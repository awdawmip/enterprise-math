# D25 / SECOND-DIGIT-LIFT — second-parameter-jet CM Hasse–Gegenbauer p³ bridge

2026-10-29. AUTHOR-SIDE / PROVED ALL-PRIME FINITE POLYNOMIAL CONGRUENCE / 60+1 EXECUTED EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.

Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Earlier in this actual research run, first-order CM finite bridge was persisted at Enterprise Math main commit 9bbc4807c9e54b36093efbacd7da04f61366d57e.

## Theorem: one more exact p-adic digit, preserving the fixed original argument

For any odd prime p>3 let e=floor((p-1)/4), k=(p-1)/2. Work in R3=(Z/p³Z)[x]/(x²-8/9), put t=(1-x)/2, so 4t(1-t)=1/9 exactly, and define

B_e(x)=[T^e](1-2xT+T²)^k;

H_p(t)=sum_{j=0}^{e} binom(k,2j) binom(2j,j) ((1-t)/4)^j;

P=P_e(x) (ordinary Legendre polynomial); h_e=sum_{i=1}^e 1/i; h2_e=sum_{i=1}^e 1/i².

For finite Jacobi P_e^(alpha,beta)(x), write J_a, J_b, J_ab and J_bb for the respective first and mixed/second derivatives at alpha=beta=0. Define

D1=h_e P + J_b,

D2=(h_e²-3h2_e)P+2h_e(J_a+J_b)+2J_ab+J_bb.

Then coefficientwise as polynomials in x (before the quadratic specialization):

**B_e(x)-(-1)^e H_p((1-x)/2) = -(p/2) D1(x)+(p²/8)D2(x) (mod p³).** (1)

All denominators are p-units: 2e<p. The new second-order port D2 includes the mixed and beta-beta Jacobi parameter derivatives; the first-order formula alone is insufficient at p³.

## Algebraic proof

Let C_e^lambda(x)=[T^e](1-2xT+T²)^(-lambda) denote Gegenbauer. Exactly B_e=C_e^(1/2-p/2), while the exact finite Jacobi identity for Hasse is (-1)^e H_p=P_e^(-p/2,0)(x). Put delta=-p/2 and Taylor-expand finite coefficient polynomials through order delta². Both parameter expansions are p-integral because e<p:

B_e = P + delta*C'_e + (delta²/2) C''_e (mod p³),
(-1)^e H_p = P + delta*J_a + (delta²/2)*J_aa (mod p³).

The identity C_e^lambda=(2lambda)_e/(lambda+1/2)_e * P_e^(lambda-1/2,lambda-1/2) gives prefactor f with f(1/2)=1, f'(1/2)=h_e, f''(1/2)=h_e²-3h2_e. Hence C'_e-J_a=D1 and C''_e-J_aa=D2. Subtract and replace delta=-p/2 to obtain (1), including the factor p²/8.

Every derivative is a finite rational polynomial and may be computed independently from the exact binomial Jacobi sum

P_e^(alpha,beta)(x)=sum_{j=0}^e binom(e+alpha,e-j)*binom(e+beta,j)*((x-1)/2)^j*((x+1)/2)^(e-j).

If c_j=binom(e,j)²((x-1)/2)^j((x+1)/2)^(e-j), a_j=h_e-h_j, b_j=h_e-h_{e-j}, d_j=h2_e-h2_{e-j}, then
P=sum c_j, J_a=sum c_j*a_j, J_b=sum c_j*b_j, J_ab=sum c_j*a_j*b_j, J_bb=sum c_j*(b_j²-d_j).
This supplies a fully explicit exact modular checker independent of differentiation software.

## Executed integer certificate

Actual Python standard-library calculations in (Z/p³Z)[x]/(x²-8/9) passed for all 60 primes 5<=p<300 and p=373, with B_e obtained by coefficient recurrence for (1-2xT+T²)^k, Hasse by integer binomial sum and all jets from the independent Jacobi binomial representation.

p | -(p/2)D1 (constant,x) | (p²/8)D2 | B_e-(-1)^eH_p
13 | (2080,429) | (1183,1521) | (1066,1950) mod 2197
23 | (11431,11293) | (11109,1587) | (10373,713) mod 12167
373 | (13645086,35470808) | (24764962,50086440) | (38410048,33662131) mod 51895117

For p=373 the second-jet residue D2 mod p is (305,269), and its p² contribution has both nonzero components. Dropping this term spoils the third-digit Hasse connection. It is NOT yet a p³ formula for the original K_b: the previous original K_b parameter transfer and finite Frobenius carry are at p² precision. The theorem is all-prime, the finite checks are regression evidence, and no unproved CM supersingular-to-Root2 implication is asserted.

## BRC/Source and next exact work

BRC COMPOSE_APPLIED: preserve original B_e, Hasse, x-branch, P, first/mixed/second Jacobi jets, original observation z=1/9, signed p-adic valuation and future scalar readout; do not quotient away x before composing all ports. This is external CM polynomial algebra, not a new P000 spatial plane. ACTIVE worldview, P000 and frozen scientific pin unchanged.

NEXT: (i) derive the missing p³ version of the ORIGINAL K_b finite parameter jet, retaining the quadratic Taylor correction and exact cutoff; (ii) derive the Frobenius third-digit carry before any scalar observer; (iii) compose these with (1) and seek an actual arithmetic CM/WZ proof of the full p≡13 (mod24) Root2 and 216/2304 bridge. These remain separate proof obligations, not achievements of (1).

Native Issue #1559 remains the non-substitutable original-class p373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius, signed Green/Hesse, kappa and Delta-R, with real native executor and independent acceptance required. No native run or formal Source checkpoint/CLAIM/Result/review was performed by this Site: static read-only Site status reports no Researcher write authority, and no own session/claim/run/target_request_id is verified. Research conversation chatgpt-research-onhour-enterprise-math-20260923 remains logically separate from maintenance. AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED.