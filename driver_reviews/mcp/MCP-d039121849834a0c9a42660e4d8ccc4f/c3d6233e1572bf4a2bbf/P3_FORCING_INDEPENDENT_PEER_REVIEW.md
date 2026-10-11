# Independent local paper review of the frozen p^3 forcing unit

Verdict: PASS for the finite formulas and equivalence (1)--(17), on the explicitly frozen first-digit, finite-transport, reflection and CM0 premises. No mathematical correction or missing second-function boundary was found. The remaining assertion Delta_p=0 is NOT proved by this unit; LIFT remains OPEN in both prime classes p=13,19 mod24.

This review is Root-authorized, informal, local paper preparation, not native Researcher/Driver acceptance. Reviewer native Researcher ID: UNKNOWN; native Driver ID: UNKNOWN. The local session label is `cm24_forcing_peer_review`, not a registered native identity, and it does not reuse EM-ENTERPRISE-3F2857 or any other identity. No Task, Claim, identity, Source, host, immutable RR or activity was created or changed. The proof authors' scripts and check JSONs were hashed as opaque bytes, never semantically read or executed. No symbolic arithmetic script, numerical prime test, prime campaign, provider query or remote write was used in the mathematical review.

The mandatory P000, Heartbeat X6/time and joint-observer preservation contracts were read before mathematical reasoning; the residual-fidelity companion was also read. Every polynomial, rational function, finite-field calculation and CM algebraic extension below is an explicitly external finite classical arithmetic readout. Native X6/time remains unchanged. No finite readout result is promoted to native full-X6 propagation, native spatial identity, raw period normalization or the mother goal.

## Reviewed bytes and independence

The complete 13,938-byte main paper and 9,596-byte algebra audit were read. FINAL_LIFT_UNIT_PINS.json is 5,025 bytes with SHA256 `a378d1f166681db9454d63f338d0c35d9b2ce76c9511854ad045013a9b17e94e`. All six outputs and all six listed inputs match its lengths, SHA256 values and Git blob SHA1 values. In particular the main paper has SHA256 `94eeceb098514b235888e78528585406487e61651d820ce8e512a130934cfda2`, and the algebra audit has SHA256 `efdd6682b36a481c14b4d6abff58aa62b4c028dae0367fd33808103c75db93f3`.

The complete first-digit complement and shared parent audit were read. The complete independent scalar/reverse-Gauss, global reflection, adjoint concomitant and shared Green-kernel papers were read to check definitions and prerequisites. This review accepts the already frozen primary finite transport and CM0 as premises; it does not reopen or amend their immutable Result. The first-digit pole/shape certificate was inspected directly rather than inferred from a check report.

The reviewer independently recomputed the residual recurrence, factorial next digit, pullback/Wronskian signs, divided reference, pole and kernel bounds, CM product, critical reference precision and final target equivalence on paper. A short local helper `kernel_spotcheck` independently checked pole/integrability/kernel/interpolation arguments; its `boundary_formula_check` helper checked endpoint and infinity arithmetic. Both helpers also have UNKNOWN native IDs, made no files or numerical tests, and were not proof authors. These contributions are disclosed; the review is independent of the authors' derivations, but is not called a blind review because their full papers and shared audit were available.

## 1. Full cutoff and the next coefficient of kappa: PASS

The factorial form b_n=(3n)!/[27^n(n!)^3] gives valuations exactly 0,1,2 in the three stated index blocks because n<p and floor(3n/p) is respectively 0,1,2. Thus discarding the last block is valid through p^2 and is invalid through p^3.

The x^n coefficient of D_HF below the last degree is

    (n+1)^2 b_(n+1) - (n+1/3)(n+2/3)b_n=0.

The remaining coefficient is exactly -kappa at x^(p-1), with kappa=(p-2/3)(p-1/3)b_(p-1). The sign and full degree in (1) are correct.

For an independent next-digit check, write Q=(p-1)!, remove p,2p from (3p-3)!, and retain all three unit blocks. Modulo p^2 this gives

    (3p-3)!/p^2
      =2 Q^2 (p-3)![1+pH_(p-1)+2pH_(p-3)].

Here H_(p-1)=0 and H_(p-3)=3/2 modulo p. After division by Q^3 the rational factor 2/[(p-1)(p-2)] is 1+3p/2, while the last-block correction is 1+3p. With 27^(p-1)=1+3p q_3 this proves

    b_(p-1)/p^2=1+p(9/2-3q_3) mod p^2,
    kappa/p^2=(2/9)(1-3p q_3) mod p^2.

The multiplier p^2-p+2/9 cancels the 9p/2 term. In particular the leading forcing kappa/p^2=2/9 mod p and the stronger infinity calculation both pass without a Wilson-quotient normalization.

## 2. Pullback sign and legal division: PASS

K B'=B(1-B) immediately gives O(F(B))=B'(D_HF)(B). The identity A(1-A)=2L^2KA' supplies the F'' and F' coefficients of the second pullback. Its constant coefficient is checked by KL'=-J(z)/3 and

    J'(z)=(2/3)[A'/(2L)-LB'].

Consequently O(LF(A))=A'/(2L)(D_HF)(A) exactly. Product differentiation then gives R'=fO(g)-gO(f), so the minus sign and the order of both terms in main-paper (3) are correct.

The complete earlier certificate supplies R=-(p/3)J(z^p) mod p^2. Passing from its 4m truncation to the present full truncation changes R only by p^2, so the same first-digit premise applies. This establishes coefficientwise divisibility before Xi is used, in the p-integral rational-function localization at p-primitive denominators. It does not authorize evaluating at an endpoint pole or choosing another lift of J.

Differentiating the exact displayed lift produces p^2 z^(p-1)J'(z^p)/3. Dividing after this differentiation yields precisely Phi in (5). The reference contribution is therefore retained at the needed order. The unforced derivative-zero argument from precision p^2 cannot be used for R/p at precision p^3.

## 3. Cyclotomic poles, integrability and four-dimensional kernel: PASS

For the full F, the direct endpoint estimates give order at most 3p-1 for R at each of 1,-1. The characteristic-zero reference J(z^p) has additional cyclotomic poles, so its modulo-p^2 expansion is necessary. With D=z^2-1,

    E_p=(z^(2p)-1-D^p)/p

is integral by binomial divisibility and has D as a factor by its two exact zeros. Expanding (D^p+pE_p)^(-2) gives precisely (6). The first bracket R+pN(z^p)/(3D^(2p)) is p^2-divisible by the frozen first digit and has only the two endpoint denominators; its quotient has pole order at most 3p-1. The correction N(z^p)E_p/D^(3p) has the same bound because D divides E_p. Thus (7), including the absence of additional reduced poles, is justified.

At infinity the exact derivative starts at z^(-p-1); the exact R has limit zero, so integrating over characteristic zero gives R=O(z^-p). The fixed reference also has this decay. Coefficientwise division with proper monic denominators preserves it. Phi consequently has no polynomial part.

Because Xi is already a rational primitive, the local Phi coefficients at k=1,p+1,2p+1 must vanish. These are exactly the forbidden noninvertible integration exponents in the given range. Formula (12) therefore defines a fixed proper primitive G with unit denominators and no local kernel modes at orders p,2p.

The proper remainder Xi-G is in F_p(z^p). Its two pole orders are multiples of p and at most 3p-1, hence only p,2p are possible. Its numerator over (t^2-1)^2 has degree at most 3. This establishes exactly four kernel dimensions, rather than merely an upper estimate or a hidden arbitrary constant.

## 4. Three finite endpoints and infinity: PASS

R vanishes exactly at 0,3,1/3. Taylor expansion of the literal reference uses increments 3pq_3 and -pq_3/3 at 3 and 1/3. Together with J'(3)=3/8 and J'(1/3)=-27/8, it gives Xi(0)=0 and Xi(3)=Xi(1/3)=3q_3/8. These corrected values cannot be replaced by zero through a modulo-p Frobenius substitution.

The leading term of the exact forcing bracket is -9^p z^(-p-1)/2; therefore [z^-p]R=-kappa 9^p/(2p). Since [z^-p]J(z^p)=3, the numerator of (10) is divisible by p. The next-digit kappa calculation above gives 9^p kappa/(2p^2)=1-pq_3 mod p^2, hence [z^-p]Xi=q_3.

The three distinct nodes are regular units for p>=7. Their values determine a unique degree-at-most-two interpolant eta with eta(a)=(Xi(a)-G(a))(a^2-1)^2. A degree-at-most-three numerator vanishing at all three nodes is a multiple of N(t). Since eta/(t^2-1)^2 begins at t^-2 and J begins with 3t^-1, the infinity coefficient determines this remaining multiple as c=(q_3-[z^-p]G)/3. Formula (13) is consequently the entire uniquely fixed second function, not a fitted normalization.

## 5. CM reflection product and precision: PASS

The retained full reflection identity is F(x)=M(q)-p^2 tC(q)/2, where q=4x(1-x), t=1-2x. Its derivative is

    F'(x)=4tM'(q)+p^2C(q)-2p^2t^2C'(q).

At alpha,beta this gives exactly the four displayed CM value/derivative congruences. Multiplication cancels the full reflection corrections in F(beta)F'(alpha)-F(alpha)F'(beta), leaving -4delta M_0M_1 modulo p^3; the value product is M_0^2 modulo p^3.

At zeta, (zeta-1)^2=4zeta and (zeta+1)^2=8zeta yield A'=B'=-3/(8zeta), Kr=1/8 and KL'=-1/12. Thus

    R(zeta)=-M_0^2/12-M_0M_1/2=-pU_p/12 mod p^3.

The M_0^2 term must survive at this order. CM0 establishes p|M_0; M_0 modulo p^3 and M_1 modulo p^2 suffice for the final U modulo p^2 and R modulo p^3. The paper's use of exact M values also makes its displayed derivative congruences unambiguous.

The exact identity 1/4-J(t)=(t^2-6t+1)^2/[4(t^2-1)^2] is correct. For the two inert classes zeta^p-zeta^-1 is divisible by p, and the denominator is a unit. Its squared numerator therefore gives J(zeta^p)=1/4 modulo p^2. This is precisely the precision needed after multiplication by p and division by p^2 in Xi. No assertion that literal zeta^p equals zeta^-1 modulo p^2 is used. Substituting proves (16), including its sign.

## 6. Original target and explicit residual: PASS AS EQUIVALENCE; VANISHING OPEN

The source-pinned OLD-R uses r<=i<=m with its original D_r and weights 1+6(i-r). The series (1+5v)/(1-v)^2 has coefficients 1+6j, so the constant-term reformulation preserves the exact original observer. The adjoint paper's tau integral also matches its original Wronskian scalar: the integrand has degree at most 4m-1, hence every integral denominator 1,...,4m is a unit. Neither observer is assigned from Xi or U.

The frozen transport G_ph=U_p-6p tau_p makes the old second-digit target equivalent to (U_p-1)/p=OLD-R_p+6tau_p. Formula (16) turns this into 12Xi_p(zeta)+OLD-R_p+6tau_p=0. In (13), zeta^p=zeta^-1 only modulo p and J(zeta^-1)=1/4. Therefore 12cJ=q_3-[z^-p]G and the displayed Delta (17) is exactly this residual. The complete residual is a base-field scalar by the independently derived U identity; individual branch terms need not be base-field scalars.

The paper correctly stops at this equivalence. Endpoint uniqueness of Xi, integrability of Phi, the four fixed kernel constants and double-critical reference cancellation do not evaluate Delta. In particular no separate claim that Delta vanishes, LIFT is proved, the second weighted supercongruence is proved, or native propagation is proved is accepted here. A successor proof still has to compare the fixed constructor with the independent OLD-R and tau observers without fitting a boundary.

Review completed within the bounded local unit. No author bytes were edited. File evidence and scope flags are recorded in REVIEW_PINS.json.
