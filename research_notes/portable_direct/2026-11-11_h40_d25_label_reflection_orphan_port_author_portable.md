# D25/LIFT — Second-label involution and exact orphaned weighted residual

Date: 2026-11-11. Status: AUTHOR-PROVED / EXACT-FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_SOURCE_CHECKPOINT.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Theorem 1: exact label reflection and exceptional boundary

For every prime p>5 let D=F_p minus {0,-1,-2}, T(t)=-2(t+1)/(t+2), lambda(t)=t+T(t)=(t²-2)/(t+2). A label lambda is represented by an orbit in D exactly if lambda != -1 and Delta(lambda)=(lambda+4)²-8 is a square in F_p (including zero); represented orbit is unique and has size 1 or 2. Indeed the inverse polynomial is

    t²-lambda*t-2(lambda+1)=0,

with discriminant Delta; t=-2 is never a root since substitution is 2, while t=0 or -1 appears only when lambda=-1. The involution S(lambda)=-8-lambda preserves Delta exactly. Within the set of represented labels it pairs every lambda except the **unique orphan lambda=-7** (which S sends to prohibited -1), and the possible self-reflected label lambda=-4, which exists exactly if (-2/p)=+1. The orphan is the legal moving T-orbit t=-3,-4.

The self-reflected *label* lambda=-4 must not be confused with a T-fixed point: Delta(-4)=-8 nonzero for p>5, so when present it labels a moving two-element orbit. T-fixed points instead occur at Delta=0.

## Theorem 2: exact weighted orphan contribution

Write p=6m+1+4epsilon with epsilon in {0,1}, N=-2^{-(2m+epsilon)} mod p, V_epsilon(t)=U(t)^m(t+2)^epsilon, U=(t+1)(t+2)^2/t, and w_epsilon(t)=(2-12epsilon-(3+10epsilon)t)/(t+2). For the orphan label -7 define A_{-7}=N sum_{t=-3,-4} V_epsilon(t), B_{-7}=N sum V_epsilon(t)w_epsilon(t).

Put q=(2/3)^m, s=3^m in F_p. Then for **all p>5**,

    A_{-7}=N*((-1)^epsilon*q + (-2)^epsilon*s),
    B_{-7}=-N*((11+18epsilon)*(-1)^epsilon*q+(7+14epsilon)*(-2)^epsilon*s).

Proof: U(-3)=2/3, U(-4)=3, w_epsilon(-3)=-(11+18epsilon), w_epsilon(-4)=-(7+14epsilon), (t+2)^epsilon=(-1)^epsilon or (-2)^epsilon respectively. Substitution proves both formulas.

Consequently any pairing of all legal quotient labels via S must retain the orphan correction:

    Sum_{legal lambda} (A_lambda,B_lambda)
       = (A_{-7},B_{-7})
         + Sum_{lambda < S(lambda), both legal} [(A_lambda,B_lambda)+(A_{S(lambda)},B_{S(lambda)})]
         + optional (A_{-4},B_{-4}).

Here '<' is any arbitrary total ordering of representatives used once; it has no algebraic meaning. Fixed-label contribution is present only if (-2/p)=+1. The theorem is a precise BRC source/observer preservation boundary for these two ports, not a proof that regular paired contributions cancel.

## Exact independently executed finite verification

A verifier reconstructs all actual T-orbits and raw A/B values; checks label discriminant, S pairing, singleton label, two-symbol boundary formula, full source-preserving A/B decomposition, and fixed-label count for every p with 7<=p<=2500. Results: 364 primes; 210031 original T-orbit labels; 104745 two-label S pairs; 177 self-reflected labels; 364 orphaned labels; **PASS**. In particular at p=7 the orphan weighted B=3 while total B=0, so cancellation must retain other label contributions.

Science continuation: study whether the S-paired weighted terms have a character-dependent cancellation identity once label/orientation H and fixed-versus-moving information are retained; compare actual signed LIFT second-digit observer before native interpretation. True native H0/B0, semilinear Frobenius and kappa/Delta-R are still NOT_RUN in author-side work. UR V2 four-file original remains unverified at 94687 bytes/SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; preserve completed UR math. Formal Source claim and independent review remain unavailable.