# D25 — finite Gauss deformation, original-source Wronskian and second-carry transport

2026-11-02 (+08:00). AUTHOR-DERIVED / HAND-PROVED ALGEBRA / EXACT FINITE CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; unchanged frozen scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane chatgpt-research-hourly-enterprise-math-20260923; maintenance chatgpt-hourly-enterprise-math-20260921 is separate. Parent goal Delta_p-R_p=0 mod p for p=13,19 mod24. External original 216 arithmetic; not a P000 native transfer.

## Inherited sources and open question

For prime p=6r+1>=7, in Z_(p) with theta=z*d/dz, define

  ell(z) = sum_(k=0)^r binom(r,k)binom(2r,k) z^k,
  h_k = (1/6)_k(1/3)_k/(k!)^2,
  a_k = (1/2)_k(1/3)_k(2/3)_k/(k!)^3,
  G(z) = sum_(k=0)^(p-1) h_k z^k,
  F(z) = sum_(k=0)^(p-1) a_k z^k.

The earlier finite Clausen theorem gives G^2=F mod p^2 coefficientwise and G=ell mod p. Existing accepted target CM0 establishes ell(1/2)=0 mod p for p=13,19 mod24. Existing earlier bridge defined R_A=(F-ell^2)/p mod p, g=ell(1/2)/p mod p, j=(theta ell)(1/2) mod p, and identified the still-open universal second carry

  12*g*j + [(1+6*theta)R_A](1/2) ?= 1 mod p.

Those earlier statements are not new mathematical credit. Parallel 2026-11-02 research also used a cited external CM Theorem 2 on an unweighted scalar; it remains a distinct contribution.

## Unit U1 — forced finite Gauss equation

Set Q=(G-ell)/p mod p coefficientwise; Q is a polynomial of degree <=2r over F_p. Define L_r=theta^2-z*(theta-r)*(theta-2r). Then, coefficientwise over F_p[z],

  [U1] L_r Q = z*(theta/2-2*r/3)*ell.

Proof: ell satisfies L_r ell=0 exactly. The truncated G satisfies theta^2 G-z*(theta+1/6)*(theta+1/3)G=0 mod p^2 as a polynomial, including the degree-p terminal term, since h_(p-1) has exact p-adic valuation 2. The exact parameter product is

  (theta+1/6)*(theta+1/3)
    = (theta-r)*(theta-2r)+p*(theta/2-2r/3)+p^2/18.

Insert G=ell+pQ mod p^2, subtract the ell equation and divide by p. QED.

Q_0=0 and the original coefficient source yields the explicit triangular recurrence, for 1<=k<=2r,

  [U1-rec] Q_k = { (k-1-r)*(k-1-2r)*Q_(k-1)
                    + [(k-1)/2-2r/3]*ell_(k-1) } / k^2 mod p,

where ell_j=0 for j>r. All divisors are units. Original parameter perturbation gives, for k<=r,

  Q_k = binom(r,k)binom(2r,k) *
        [ (1/6)*sum_(j=0)^(k-1) 1/(j-r)
          +(1/3)*sum_(j=0)^(k-1) 1/(j-2r) ] mod p;

for 1<=s<=r the middle-band reflected certificate is

  Q_(r+s) = (-1)^s*r!*(2r)!*(s-1)!/
            [6*(r-s)!*((r+s)!)^2] mod p.

Q_k=0 for k>2r. These denominators remain prime-to-p.

## Unit U2 — first-order Wronskian forcing by original 216 coefficients

Define Omega(z)=ell(z)*theta Q(z)-Q(z)*theta ell(z), degree <=3r. Then

  [U2] (1-z)*Omega'(z)+3*r*Omega(z)
        = (theta/4-2*r/3)*ell(z)^2 mod p.

Proof: convert the homogeneous Gauss equation for ell and the forced equation for Q to their ordinary second-order forms. Subtract Q times the first from ell times the second and use Omega=z*(ell Q'-Q ell'). The resulting derivative identity is exactly U2. QED.

By the earlier *coefficientwise* finite Clausen relation ell^2=F mod p and 6r=p-1,

  [U2-source] (1-z)*Omega'+3*r*Omega
              = (1/36)*sum_(n=0)^(2r) (9*n+4)*a_n*z^n mod p.

Let s_n=(9n+4)*a_n/36 for 0<=n<=2r and s_n=0 thereafter. Omega(0)=0 and its coefficients omega_n obey

  [U2-rec] omega_0=0;
           omega_(n+1)=[s_n-(3r-n)*omega_n]/(n+1) mod p, 0<=n<3r.

All n+1<p, so this is a unique polynomial solution in degree <=3r. It computes the complete Wronskian from *original a_n*, using O(p) modular operations and memory and no full R_A reconstruction for the declared (1+6theta) future observation. This is a provenance-preserving arithmetic BRC interface, not a native X6 or physical theorem.

## Unit U3 — explicit finite Green kernel

Unrolling U2-rec gives, for 1<=n<=3r,

  [U3] omega_n = sum_(k=0)^min(n-1,2r)
         (-1)^(n-k-1) * k!*(3r-k-1)!/(n!*(3r-n)!)
         * (9k+4)*a_k/36 mod p.

The proof is direct induction on n; all factorial arguments are below p. Consequently Omega(1/2)=sum_(n=1)^(3r) omega_n*2^(-n) mod p is a fully original-source finite Green-kernel expression.

## CM special-point reduction and remaining target

From G^2=F mod p^2, the correction R_A=2*ell*Q mod p coefficientwise. Thus

  [(1+6theta)R_A](1/2)
    = 2*ell*Q+12*((theta ell)*Q+ell*(theta Q)) at z=1/2.

At inherited CM0, ell(1/2)=0 mod p and hence

  [Bridge] [(1+6theta)R_A](1/2)
         = 12*j*Q(1/2) = -12*Omega(1/2) mod p.

Therefore the previous all-target second-carry open problem is exactly

  [OPEN] 12*g*j - 12*Omega(1/2) ?= 1 mod p
         for all p=13,19 mod24.

OPEN remains a conjecture in this note. The older equivalent Clausen scalar route 12*j*(G(1/2)/p) was already known, so it is not claimed as new; U1/U2/U3 provide a new operator/source interface and explicitly checkable Green kernel.

## Actually executed tests and finite certificates

A Python standard-library checker computes Q in two independent ways (original hypergeometric coefficients modulo p^2 and U1-rec), Omega in two ways (ell*theta Q-Q*theta ell and U2-rec from original a_n), and checks the finite Clausen weighted original F observer and R_A coefficient division. All 611 primes p<=10000 with p=1 mod6 passed. All 312 target primes p=13,19 mod24 in this finite range satisfied inherited CM0, Bridge and finite second carry=1. An independently evaluated finite Green-kernel double sum verified U3 at p=7,13,19,31,37,43,373,1171. The all-prime OPEN remains unproved.

For p=373: g=340, j=294, Q(1/2)=57, Omega(1/2)=27, [(1+6theta)R_A](1/2)=49, and G(1/2)/p=24 mod373. The source split is 12*g*j=325 and -12*Omega=49, hence 325+49=374=1 mod373. Non-CM p=31 also passes the general identity (ell(1/2)=21, Omega=23).

## Next exact unit and source/control status

Seek a genuine all-target terminating/WZ/CM-transform certificate for OPEN, using U3's finite source kernel and a verified lift for g; then reuse the previously verified three-band p^3 source tower for the next carry. Native original same-class p373 H0/B0 benchmark remains separately pending at enterprise-math Issue #1559. Existing control support Issue #1558 owns the upstream authorization/deployment defect.

At 2026-11-02 status read, live Gateway 0.6.11 reported CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and active quota 5/5. The same logical Research lane's earlier #6637 was read-only recovery; #6638 a terminal FAILED continuation, not replayed. Old actual service session, contribution IDs and neutral preserved staging are untouched. These author-side proof/program/log bytes do not establish a new native CLAIM/OPEN/Source checkpoint/Result/review. Native activity registration remains REGISTER_PENDING.
