# D25: complementary finite Gauss kernel for signed Clausen overflow

2026-11-06 | TASK_RESEARCH author proof | FINITE_VERIFIED 80 primes | UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0_B0.
Existing task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance). Mother goal remains Delta_p-R_p=0 mod p for p=13,19 mod24. Native p373 H0/B0 divided-power/Frobenius under Issue #1559 remains NOT_EXECUTED/PENDING_OWNER.

## Starting exact boundary, already established (not newly credited)

For p=6m+1>3 prime, define in F_p

d_i=(1/6)_i(1/3)_i / [2^i(i!)^2], 0<=i<=m;
e_r=36^(r-1)((r-1)!)^2 / product_(s=1)^r[(1-6s)(1-3s)], 1<=r<=m;

J_p=sum_(1<=r<=i<=m) (1+6(i-r)) d_i e_r mod p.

The already-proved signed Clausen identity is W_p = S_p(S_p+12T_p)-2p^2 J_p mod p^3, with R_p=2J_p mod p. The actual still-open equivalent two-moment condition is 24(S_p/p)M2_p - (p/3)(S_p/p)^2 = 1+2pJ_p mod p^2.

## A. New finite reciprocal binomial kernel (PROVED, all p=6m+1>3)

For every 1<=r<=m,

e_r = 2^r / [36 r^2 C(m+r,r) C(2m+r,r)] (mod p).            (A1)

And d_i = 2^(-i) C(m,i)C(2m,i) mod p, 0<=i<=m. Therefore

J_p = (1/36) sum_(1<=r<=i<=m) (1+6(i-r)) 2^(r-i)
      C(m,i)C(2m,i)/[r^2 C(m+r,r)C(2m+r,r)] (mod p).          (A2)

Proof: 6m=p-1, hence (6s-1)=6(m+s) mod p and (3s-1)=3(2m+s) mod p. The product of the two negative factors is positive, giving product_(s=1)^r (1-6s)(1-3s)=18^r(m+1)_r(2m+1)_r mod p. Since (m+1)_r=r!C(m+r,r) and (2m+1)_r=r!C(2m+r,r), (A1) follows. All denominators are nonzero since 2m+r<=3m<p and r<p. Since (1/6)=-m and (1/3)=-2m in F_p, the d_i identity follows. Substitution yields (A2). Index order, signed weight and branch multiplicity are retained.

## B. New complementary nonhomogeneous finite Picard-Fuchs identity

Let theta=z d/dz, D_m(z)=sum_(i=0)^m d_i z^i and E_m(z)=sum_(r=1)^m e_r z^r over F_p[z]. Then exactly

[36 theta^2-z(6theta+1)(3theta+1)] D_m(z) = 0,             (B1)
[(6theta-1)(3theta-1)-36 z theta^2] E_m(z)
    = z - 36m^2 e_m z^(m+1).                               (B2)

The operator z multiplies after the theta-polynomial acts.

Proof: 36 i^2 d_i=(6i-5)(3i-2)d_(i-1); all interior coefficients vanish in (B1), and the terminal degree m+1 is -(6m+1)(3m+1)d_m=0 mod p. For E, e_1=1/10 and e_(r+1)/e_r=36r^2/[(6r+5)(3r+2)] in F_p. Thus degree 1 of (B2) is 5*2*e_1=1, interior degrees 2..m vanish and degree m+1 is -36m^2e_m. This terminal is nonzero because each factor e_m and m is a unit modulo p, likewise the degree-1 source 1 is nonzero. In particular E_m is not a homogeneous companion: removing either nonzero source changes the finite problem.

The recurrence of E has complementary hypergeometric parameters 5/6 and 2/3, compared with original Gauss 1/6 and 1/3. This is an algebraic companion, NOT an authenticated crystalline adjoint/Frobenius.

## C. Exact ordered-pair coefficient readout

Let Erev_m(z)=sum_(r=1)^m e_r z^(m-r), and c_k=[z^k]D_m(z)Erev_m(z). Then

J_p=sum_(n=0)^(m-1)(1+6n)c_(m+n)
   =[z^(2m-1)]D_m(z)Erev_m(z)
      *sum_(n=0)^(m-1)(1+6n)z^(m-1-n) (mod p).              (C1)

Proof: c_(m+n) sums precisely i-r=n>=0 with i<=m, r>=1. This exact signed triangle is the low/high BRC joint-port readout; it does not turn the triangle into a full square. This expression supplies a finite Green-like coefficient interface but makes no complexity-improvement claim over the existing O(m) signed-prefix recurrence.

## Executed exact check

A newly authored Python standard-library checker d25_reciprocal_gauss_kernel_check_20261106.py independently checks (A1)-(A2), every coefficient of (B1)-(B2) through degree m+1, and three exact algorithms for J (joint-pair direct, signed-prefix and independent convolution), for ALL 80 primes p=6m+1, 7<=p<=997. Zero failed assertions. Representative (p, D_m(1), theta D_m(1), E_m(1), e_m, -36m^2e_m, J_p) in F_p:

(13,0,7,0,9,4,0)
(19,0,1,5,1,18,6)
(67,0,40,9,36,31,44)
(373,0,294,45,37,336,98).

The nonzero J at p19 and p373 is retained even when D_m(1)=0. Finite check is not an all-prime proof of D25 LIFT. Statements A-C have direct algebraic proofs independent of this finite check.

BRC: COMPOSE_APPLIED using original signed ordered low/high joint population and valuation-sensitive cutoff, no positive-mass quotient, no native X6 ontology change. Auxiliary variable z is external number-theoretic notation.

## Smallest remaining scientific action

Use both actual inhomogeneous finite operators (B1)-(B2) and coefficient observer (C1) to search a joint Green/Lagrange concomitant whose boundary is exactly 2J_p and whose bulk couples to the already proved two-moment target 24GM2-pG^2/3 mod p^2. It must pass adversarial nonzero J examples at p19 and p373; any residual bulk terms need explicit p-adic valuation/provenance. Uniform LIFT remains OPEN. Original p373 fixed native H0/B0 [X]U mod139129, rank, eta, semilinear direction, kappa and independent replication remain NOT_EXECUTED / PENDING_OWNER (#1559). No session/claim/run/Result or independent Driver acceptance is asserted by this note.

Evidence: author exact code, previous signed Clausen note at ca7b5ce2b8044eb3b12e0ca69226e396fef3bfa9, previous Picard moment note at 91498715d1a95cc4773a711b8e9386ba3760ccb2; original scientific pin above.