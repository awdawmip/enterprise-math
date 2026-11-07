# D25: exact finite-field Frobenius factorization of the 2304 Gauss-square carry

2026-11-07, TASK_RESEARCH author-side PROVED finite-field algebra / exact finite checks, UNREVIEWED / NOT_ADMITTED. Completes the next distinct unit after the aggregate-carry precision ladder. Research logical lane chatgpt-research-hourly-enterprise-math-20260923 only. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## New general theorem (all p ≡ 5 mod 8, p prime)
Set r=(5p−1)/8, s=(7p−3)/8, n=(p−1)/4, t=(p+1)/2, k=(p−5)/8, and in F_p[z] define
G(z)=sum_{i=0}^r binom(r,i)binom(s,i) z^i.
These are exactly the p-unit coefficient reductions of the truncated Gauss polynomial with hypergeometric parameters (1/8,3/8;1). Let H(z) be the quotient of G(z) by (1−z)^t, and Q(z) the degree-<p part of G(z)^2.

Then H exists in F_p[z] and has degree k; moreover

G(z) = (1−z)^t H(z),
Q(z) = (1−z)H(z)^2,
G(z)^2 = (1−z^p)Q(z).

Thus the entire high-degree Cauchy carry has an EXACT polynomial identity

C_G(z)=Pi_{degree≥p}(G(z)^2)=−z^p Q(z) (mod p).

In particular, the *discarded aggregate carry is not zero*: its coefficient range is p through p+n, and its maximal coefficient is the negative of the top coefficient of Q. It is a Frobenius-shifted, signed copy of the whole projected low-degree polynomial; coefficient-wise source information is lost if one simply evaluates G(z)^2 instead of first projecting.

### Proof using Vandermonde and exact root multiplicity
For every 0≤d≤r, the d-th divided derivative at z=1 is
G^(d)(1)/d! = sum_{i=d}^r binom(r,i)binom(s,i)binom(i,d)
            = binom(r,d)binom(r+s−d,r).
Here r+s=(3p−1)/2. If 0≤d≤(p−1)/2, then p≤r+s−d<2p, and the upper index modulo p is <r. Lucas's theorem makes the second binomial 0 mod p. At d=t=(p+1)/2, r+s−t=p−1, and binom(r,t)binom(p−1,r) is nonzero mod p. Hence z=1 is a root of G of EXACT multiplicity t. Since deg G=r, there is a polynomial H of degree r−t=k with G=(1−z)^t H. In characteristic p, (1−z)^p=1−z^p; therefore G^2=(1−z)^(p+1)H²=(1−z^p)(1−z)H². The latter factor Q=(1−z)H² has degree 2k+1=n<p. Its high-degree part is exactly −z^p Q; its low-degree part is Q. QED.

This is also a direct *finite Clausen factorization*: because the classical formal Clausen identity relates G² to the 2304 3F2 coefficient series, Q is exactly the mod-p truncation of the 2304 unweighted series through degree n. The new result does not require assuming a target weighted congruence.

## Exact projection at the true argument and testable extra question
Set z0=1/9 in F_p. The theorem gives C_G(z0)=−z0 Q(z0) and C_G'(z0)=−z0 Q'(z0), because the derivative of z^p is zero in characteristic p. The 24 primes p<500 with p≡5 mod8 were checked using exact binomials, full polynomial multiplication, repeated-root verification, and direct F_p evaluations.

In the 12 checked primes p≡13 mod24, H(z0)=0, so Q(z0)=Q'(z0)=C_G(z0)=C_G'(z0)=0.
In the 12 checked primes p≡5 mod24, H(z0)≠0 and Q(z0)≠0; p=5 yields Q(z0)=2, while p=29 yields Q(z0)=21.
These statements at z0=1/9 are FINITE EVIDENCE only; the universal character/residue-class splitting is a separate OPEN lemma, not proved here. The general polynomial factorization above IS proved.

The previously proved p-adic digit U1=5 at high degree r+s applies at precision p² and does not follow from an equality mod p; this Frobenius factorization is a complementary first-digit observer, not a replacement for the three-digit source ladder.

## Scope, evidence and continuation
Companion script d25_gauss_clausen_frobenius_factor_20261107.py executed locally with EXACT 24/24 PASS for all p≡5 mod8 below 500. This is author-side work, not a native experiment or mathematical admission. It consumes 20261107_hourly20_d25_aggregate_carry_precision_ladder.md without repeating its proof.

Mother target remains OPEN: Delta_p=R_p (modp) for p≡13,19 mod24, via the frozen W_p=p (mod p³) bridge. NEXT: establish or refute the class-specific exact H_p(1/9)=0 statement for all p≡13 mod24 (e.g. via CM finite-field hypergeometric polynomial), while constructing a two-leg Heun/Frobenius finite transformation that preserves both the new signed Frobenius carry −z^p Q and the separate p² normalized digit 5. Test p=13,19,37,43,109,373; retain frozen native p373 experiment as unperformed.

Current native backend admission remains BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false), Site CONFIGURED_NOT_LIVE_VERIFIED (research_authority_granted=false). Original Research lane requests and protected session/claim/run/staging UNKNOWN_PRESERVE; no native session/claim/open/checkpoint, Result, review or independent admission asserted. Controller support: awdawmip/enterprise-math#1558.