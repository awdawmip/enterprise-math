# Independent bounded paper review of the three-integral CM observer

Verdict: PASS for the conditional finite constructor, fixed CM observer, OLD-R boundary reduction, and the two precisely stated rational-antidifference no-go arguments. No mathematical correction was found. Equations (19) and (21) remain unproved; LIFT remains OPEN in both required classes p=13,19 mod24.

This is informal Root-authorized local paper preparation, not formal Researcher/Driver acceptance. Native Researcher ID: UNKNOWN. Native Driver ID: UNKNOWN. The session label `cm24_forcing_peer_review` is only a local agent label; no native identity is created and no EM-ENTERPRISE-3F2857 identity is used. There was no native Task, Claim, identity, Source, host, accepted Result, remote operation, provider request, numerical prime test or prime campaign. The author's .py checker was hashed as opaque bytes, never semantically read or executed. Its saved JSON and the helper's saved text report were read only as provenance; no mathematical conclusion below is inferred from their PASS entries.

P000, Heartbeat native X6/time, joint-observer preservation and residual-fidelity contracts were already completely read in the immediately preceding review and remain the controlling scope. The variable z, Frobenius field, CM extension and finite integrals are external finite classical arithmetic readouts. Native X6 and separately typed time are unchanged. Both marked CM branches and the full independently specified OLD-R/tau observers are retained. No scalar formula is promoted to full native X6 propagation or complete-state reduction.

## Frozen objects, inputs and contribution disclosure

The complete main paper (12,897 bytes) and complete OLD-R helper (7,056 bytes) were read. All seven formal inputs and five formal outputs in FINAL_UNIT_PINS.json have matching byte lengths, SHA256 values and Git blob SHA1 values. The pin file is 4,497 bytes, SHA256 `23153c5de26970a6022f449b77ad7b76c5c17fb375a7fca37d2fa276e285e1e6`. Main-paper SHA256 is `7657c63dcdf2255dc5ec581e24ec525854b6c63cd5dc39248af0477d6b204cdb`; helper SHA256 is `4b7e025753eca30878cf77fc53ba2edf17ead191885fdd873bcc4cf8b265e7fa`.

The three independent scalar/Green/adjoint papers and both complete forcing papers were completely read in this session's preceding forcing review; those reads were reused after verifying unchanged hashes. Both exact old Source returns were now completely read to check the original OLD-R and JT2 definitions. The preceding forcing review is an explicit premise, with REVIEW.md SHA256 `f46c7dc3909be1395afd239a706c52da6585a3169dfb1a184504afde51e80795`; the present review does not infer or enlarge its scope. The already frozen finite transport, reflection descent and CM0 remain stated prerequisites.

The root reviewer recomputed the forcing basis, degree/unit-integral arguments, pole repairs, interpolation and CM coefficients independently on paper. The local helper `kernel_spotcheck` independently checked OLD-R (20), the triangular remainder and both no-go proofs, without scripts, files, prime calculations or additional children. Its native ID is also UNKNOWN. This review is independent of the proof authors' calculations, but is not called blind because their full arguments and recorded checks were available.

## 1. Polynomial W, divided companion T and forcing basis: PASS

For n<=2m, each term in (z+1)^(p-1)H(B) has nonnegative denominator-clearing exponent p-1-3n. Its polynomial degree is p-1-n, so only n=0 contributes the top term, with coefficient one. Thus W is monic of degree p-1. At z=1/3, B=0 and W=(4/3)^(p-1)=1; p>=7 makes all these constants units. Consequently T=(W-1)/(3z-1) is an exact polynomial of degree p-2, with no hidden rational pole.

Let a,b,d denote precisely the main paper's (7). The original forcing bracket is az+b. Replacing H(B)/(z+1) by W/(X+1), with X=z^p, gives denominator 3d(X)(3z-1), so (8) has the correct factors.

The elementary division

    (az+b)/(3z-1)=a/3+(a/3+b)/(3z-1)

and W/(3z-1)=T+1/(3z-1) yield exactly alpha W+beta T+chi(3z-1)^(p-1). Here 1/(3z-1)=(3z-1)^(p-1)/(3X-1) follows in characteristic p. Direct expansion gives

    a=-3X^3+11X^2+3X+5,
    b=9X^3-21X^2+15X-3,
    Xa+b=-3X^4+20X^3-18X^2+20X-3=J'(X)d(X).

Thus alpha+chi=-(Xa+b)/(3d)=-J'(X)/3. This verifies the top-basis cancellation, including its sign. Since 3^(p-1)=1, each of W-z^(p-1), T and (3z-1)^(p-1)-z^(p-1) has degree at most p-2. Equation (9) is therefore an exact identity in F_p(z), rather than an integration that divides by p.

## 2. Three integrals and their normalization: PASS

A polynomial of degree <=p-2 has a unique primitive with zero constant and degree <=p-1. Coefficient integration divides by j+1 in 1,...,p-1, all units. There is no degree-p derivative-zero mode in this normalized degree range. This proves that all three definitions (10) are independent, legal finite constructors.

The binomial coefficient identity binom(p-1,j)=(-1)^j gives (3z-1)^(p-1)=sum_(j=0)^(p-1)3^jz^j. Removing its top coefficient, which is one, gives (11). Hence I_E(1/3)=H_(p-1)/3=0, by the ordinary nonzero-residue harmonic sum. No analytic logarithm, period or target boundary is chosen in this computation.

Every rational coefficient alpha(X), beta(X), chi(X) has derivative zero because X=z^p. Differentiating (12) therefore recovers (9) exactly. The three-integral P_hat is a legal primitive of Q. Its uncorrected pole bound 3p is real and is correctly left for the explicit repair.

## 3. The two 3p pole repairs and infinity condition: PASS

All terms of P_hat have denominator d(X)=(X^2-1)^3 and polynomial numerators after X=z^p. At X=1, a=16,b=0,3X-1=2; at X=-1, a=16,b=-48,3X-1=-4. Substituting these values in N gives precisely the two r_+,r_- expressions in (13), with the displayed signs.

The linear polynomial n in (14) has n(1)=-r_+ and n(-1)=-r_-. Thus N(z,z^p)+n(z^p) vanishes at z=1 and z=-1. Since X^2-1=(z^2-1)^p, the denominator has order 3p at each endpoint; one exact numerator zero lowers each pole to at most 3p-1. No evaluation divides by an endpoint pole. The repair is derivative zero and uses only the three independently normalized integrals, not CM, OLD-R or q_3.

At infinity, alpha and beta have order X^-2, chi has order X^-3, and all I polynomials have degree <=p-1. Hence P_hat=O(z^(-p-1)). The correction n(X)/d(X) is O(z^-5p), so P has the same decay and [z^-p]P=0. This independently fixes the infinity coefficient needed for the next reconstruction. It does not identify P with the earlier partial-fraction primitive G, and the paper correctly distinguishes them.

## 4. Complete boundary reconstruction: PASS

The reviewed preceding forcing theorem fixes Xi, its endpoint data and its z^-p coefficient. Xi-P is proper, derivative zero, and has only the two endpoint poles, each of order at most 3p-1. Thus it has the form h(z^p) with h=N_0(X)/(X^2-1)^2, deg N_0<=3. This is the same four-dimensional kernel, with no polynomial or free constant.

The three regular, distinct nodes 0,3,1/3 determine a degree-at-most-two numerator eta. The displayed Lagrange formula has values eta(0)=v0, eta(3)=64v3 and eta(1/3)=64va/81, exactly matching the squared denominator factors at those nodes. The remaining numerator freedom is a multiple of N(X). Since [z^-p]P=0, eta/(X^2-1)^2 has no z^-p coefficient, and J has coefficient 3, the coefficient of J must be q_3/3. Formula (16) follows uniquely from the actual finite and infinity boundaries; it is not fitted to an expected CM value.

## 5. CM observer Lambda and both q_3 contributions: PASS

At the marked CM pair X=zeta^-1=3+2delta, X^2=6X-1 implies

    a=-12(3X-1), a+3b=96X^2,
    (3X-1)^2=8X^2, X^2-1=2(3X-1).

These relations give alpha=1/[6(3X-1)]=-1/6+delta/8, beta=-1/6 and chi=-alpha. Therefore 12P_hat has exactly the coefficient (1-3zeta)/4 on I_W-I_E and coefficient -2 on I_T, as in (17). This verifies the primitive's small CM expression independently of the recorded symbolic output.

Using the same quadratic relation, the three interpolation coefficients reduce respectively to zeta, 3-zeta and zeta-1/3. Substitution into (16) therefore produces

    12Xi(zeta)=12P(zeta)-zeta P(0)
       -(3-zeta)P(3)-(zeta-1/3)P(1/3)+2q_3.

The finite endpoints contribute

    (3q_3/8)[(3-zeta)+(zeta-1/3)]=q_3;

the infinity term contributes 12(q_3/3)J(X)=q_3 because J(X)=1/4. This proves (18) and its factor two without setting q_3 from a target discrepancy. Evaluation denominators are units at both marked CM branches for the specified prime classes. The complete observer lies in F_p through the reviewed Xi/U relation; that fact does not authorize replacing individual extension-field summands by base-field values or dropping the conjugate branch.

## 6. OLD-R boundary, triangular term and missing identity: PASS AS EQUIVALENCES

The exact two old Source returns retain the same B_i=v_i2^-i, D_r, and weight 1+6(i-r). The constant-term formula uses the expansion at v=0. Its coefficients are 1+6j, so the main paper's (19) has exactly OLD-R+6tau, with 6tau=-(2/3) times the finite integral. Integral denominators in this correction lie in 1,...,4m<p.

For a direct independent OLD-R boundary check, put F=A_m D_m. The weight in F(1)-6F'(1) on a pair (i,r) is 1+6(i-r). Splitting pairs into i>=r and r>i gives

    F(1)-6F'(1)=OLD-R/2-T_old.

The second set has weight -(6(r-i)-1), and includes i=0, exactly as in the fixed triangular T_old. Under CM0, A_m(1)=V(1/2)=0 and A_m'(1)=-V'(1/2)/2. Hence OLD-R=6V'(1/2)D_m(1)+2T_old. This proves (20); it does not evaluate either endpoint D_m(1) or T_old.

The helper's operator endpoints also pass: L D_m=z/18-2m^2D_m z^(m+1), while L A_m=(m+1/6)(m+1/3)B_m z^-m. Both exact endpoint terms are retained; only the second vanishes after reduction modulo p because m+1/6=0. The residue calculation has the same signs as the direct pair split.

Combining (20) with C_rev(1/2)V'(1/2)=-4tau gives 6tau=-(3/2)C_rev(1/2)V'(1/2), and thus (21) is exactly (19). The new T(z) from polynomial division and the old T_old triangular sum are distinct and are not equated.

Neither (19) nor (21) is evaluated by any of the constructor, endpoint or CM calculations. The equality to zero remains the substantive proof obligation.

## 7. Two rational-antidifference no-go proofs and precise scope: PASS

For the B ansatz, multiplication by its ratio denominator gives

    (i+1/6)(i+1/3)Q(i+1)-2(i+1)^2Q(i)
      =2(i+1)^2[1+6(i-r)].

A first pole in an integer-shift orbit must be 5/6 or 2/3, while a last pole must be -1. These cannot be in one integer-shift orbit, so a rational Q over Q(r)(i) has no finite poles and is polynomial. Coprimality of the first quadratic with (i+1)^2 then forces i^2 to divide Q(i). The leading coefficients 1 and -2 make the left-hand degree deg Q+2; the affine right side has degree 3. The required degree one contradicts the forced degree at least two.

For the D ansatz, the corresponding first and last poles must be 1 and one of -5/6,-2/3. Their shift orbits are incompatible, so Q over Q(i)(r) is polynomial. Substitution at the two last-coefficient roots forces Q(1/6)=Q(1/3)=0, hence degree at least two. The leading coefficients 2 and -1 again force degree one for the stated nonzero-slope affine weight, giving a contradiction. A nonzero constant weight would instead force degree zero, also contradictory. Thus the helper's stated extension to nonzero affine weights is justified.

These statements exclude precisely universal characteristic-zero one-variable rational first antidifferences of Q(i)B_i or Q(r)D_r with the specified affine weights. They do not exclude growing-degree finite-field certificates, double-sum certificates, higher-order telescopers, other function classes, or an independent evaluation of the fixed remainder. They do not imply LIFT is false or impossible. The helper's final list of next approaches is read as possible alternatives, not an exhaustive impossibility theorem for all other methods.

## Final scope

The three-integral forcing constructor, independent pole repair, four-boundary reconstruction, Lambda+2q_3 formula and fixed OLD-R boundary reduction pass. The two no-go proofs pass only at their expressly stated ansatz scope. No mathematical edits to author files are required or made.

The last identity Lambda_p+2q_3+OLD-R_p+6tau_p=0, equivalently (19)/(21), remains OPEN. LIFT, the weighted p^3 supercongruence, raw period normalization and native full-X6 propagation remain unproved by this unit. A future proof must compare the fully fixed independent constituents; uniqueness of Xi or existence of a primitive is not such a comparison.
