# D25: second-order Teichmüller four-jet and signed 216↔2304 repair

Date: 2026-11-02, Asia/Hong_Kong. **AUTHOR-DERIVED / EXACT ALGEBRA / FINITE EXACT CHECKS (45 target primes) / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Not the original-class H0/B0 native experiment or a canonical Source checkpoint.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Preserve immutable scientific source c47e13e4aba0e006366f989d6334d443f6333ae3, P000 and ACTIVE worldview. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. Prior author proof: research_notes/portable_direct/20261102_hourly_d25_frobenius_teichmueller_cm_jet_cocycle.md, which established only the first gauge digit modulo p.

## A. Exact second-order Teichmüller transport

For any prime p>=5, P(z) in Z_(p)[z], p-unit z, theta=z*d/dz, f_j=(theta^j P)(z), q=(z^(p-1)-1)/p and omega=z^(p²) modulo p³:

~~~text
(theta^j P)(omega) =
  f_j + p*q*f_(j+1)
      + p²*[q*f_(j+1)+(q²/2)*(f_(j+2)-f_(j+1))]
  (mod p³), for every j>=0.                            (A1)
~~~

Proof: omega/z=(z^(p-1))^(p+1)=(1+pq)^(p+1)
=1+pq+p²q (mod p³). For any Q in Z_(p)[z],
Q(z(1+t))=Q(z)+t theta Q(z)
+t²(theta²-theta)Q(z)/2 (mod t³).
Substitute t=pq+p²q and Q=theta^j P. Moreover omega^(p-1)=
(1+pq)^(p²)=1 (mod p³). For any z'=z (mod p),
z'=z(1+pu) implies z'^(p²)=omega (mod p³). Thus the lift
depends only on the reduced nonzero residue, not the rational representative.

## B. Corrected four-port observer

Assume f0=f1=0 (mod p). The following are genuine p-local quotients:

~~~text
V0 = f0/p+p*[q*(f1/p)+(q²/2)*f2]                (mod p²)
V1 = f1/p+q*f2+p*[q*f2+(q²/2)*(f3-f2)]       (mod p²)
V2 = f2+p*q*f3                                   (mod p²)
V3 = f3                                           (mod p)
~~~

By (A1), these equal respectively
P(omega)/p, theta P(omega)/p, theta²P(omega), theta³P(omega),
at the indicated precisions. All four are invariant under z'=z mod p
for the same polynomial. For weighted Y=(1+c theta)P one has the
**two-digit compensation formula**

~~~text
[Y(omega)-Y(z)]/p =
  c*q*f2 + p*[q*(f1/p)+c*q*f2
              +(q²/2)*(f2+c*(f3-f2))] (mod p²). (B2)
~~~

This is obtained by combining (A1) at j=0,1 and f1=0 mod p.
The first digit c*q*f2 recovers the previous result; the bracket
gives the next digit. This is a scoped observer statement at p³ precision,
not a claim of a universal minimal jet dimension.

## C. Exact signed D25 source application

Retain the ORIGINAL finite sums, indexed k=0,...,p-1:
F_A(x)=sum (1/2)_k(1/3)_k(2/3)_k x^k/(k!)³,
F_B(x)=sum (1/4)_k(1/2)_k(3/4)_k x^k/(k!)³.
At z_A=1/2,z_B=1/9, put Y_A=(1+6theta)F_A,
Y_B=(1+8theta)F_B, and
delta_A=[Y_A(z_A^(p²))-Y_A(z_A)]/p,
delta_B=[Y_B(z_B^(p²))-Y_B(z_B)]/p (both mod p²).
The original signed weighted bridge transforms by p*G_p (mod p³),
where G_p=delta_A-2delta_B (mod p²).

For p=373, p²=139129:
q_A=123259 and q_B=15437 (mod p²);
(V0,V1,V2,V3)_A=(138383,104894,97899,73);
(V0,V1,V2,V3)_B=(18277,52254,123426,63);
delta_A=72101, delta_B=18921; hence

~~~text
G_373=34259=316+373*91 (mod 139129).
~~~

The first digit 316 independently matches the prior p² study;
**91 is a new second-digit signed-source discriminator**.
Uncompensated transfer of a signed weighted bridge across the two
independent Teichmüller substitutions fails at this fixed observer.
It does not refute or prove the original unshifted frozen mother goal.

| p | q_A | q_B | delta_A | delta_B | G_p | digits |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 140 | 166 | 56 | 109 | 7 | 7,0 |
| 19 | 92 | 40 | 306 | 276 | 115 | 1,6 |
| 37 | 850 | 1111 | 636 | 405 | 1195 | 11,32 |
| 61 | 25 | 2658 | 637 | 2467 | 3145 | 34,51 |
| 373 | 123259 | 15437 | 72101 | 18921 | 34259 | 316,91 |

Validation: standard-library exact original-hypergeometric recurrence
produced all 45 primes p<=1000 with p mod24 in {13,19}. For both
polynomials it separately evaluated at z and z^(p²), verified (A1)
and all four ports, (B2), weighted residual, and two alternative
same-residue representatives per prime. 45/45 passed in the actually
executed author-side checker. No native H0/B0 computation or Lean
verification was performed. Portable complete proof and runnable
checker also retained as a conversation artifact.

BRC: COMPOSE_APPLIED using original indexed signed/weighted streams,
rational point and Fermat quotient mod p², p-local valuations and
four Euler jets. Future observer operations are rational representative
change, weighted Euler readout and the signed bridge mod p³. (A1)-(B2)
certify observer-safe reduction at that scope; first-digit-only ports
cannot determine the p373 second gauge digit 91. This is classical
finite-ring algebra, not a native six-axis/X6 equivalence assertion.

Next science: construct and test a sourced non-scalar triangular
correspondence between the two original repaired four-port tuples
that preserves the signed bridge at unshifted points for both p=13,19
mod24. Discriminate at p373 against separately typed fourth-digit
ratio 228:114, raw derivative mismatch 138, projective first-lift
defect 365, first Teich shift 316 and second digit 91. Retain the
Clausen signed cutoff, and then return to Delta_p-R_p=0 mod p.

Control read: Gateway 0.6.11 2026-11-02 CODE_REVIEW_REQUIRED
(UPSTREAM_CODE_REVIEW_REQUIRED), research_authority_granted=false,
executor_binding_configured=false, new-job quota 5/5. Original
same-lane recovery #6637 SUCCEEDED read-only; continuation #6638
definitively FAILED. #1558 owns the repair and #1559 the native
H0/B0 benchmark. This neutral author artifact is neither source CLAIM,
OPEN, checkpoint, Result, Review, registered Research-Activity nor
mathematical admission. No scheduler or notification change.
