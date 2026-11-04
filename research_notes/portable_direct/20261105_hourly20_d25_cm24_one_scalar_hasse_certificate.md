# D25 CM(-24): one-scalar Hasse first-jet and square-norm certificate

Date: 2026-11-05. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Status: AUTHOR-DERIVED / EXACT ALGEBRAIC PROOF / 168-PRIME FINITE CHECK / UNREVIEWED / NOT_ADMITTED. Legendre/CM auxiliary, NOT the original native H0/B0 experiment.

## Theorem
For every prime p>=5, p=5 mod 8, let m=(p-1)/2, r=(p-1)/4, n=r+1. Work in A=F_p[t]/(Q), Q=t^4-140t^3+294t^2-140t+1. Set
H=sum_{j=0}^m binom(m,j)^2 t^j,
C=16t(1-t^2)H'(t)+(1+2t-7t^2)H(t),
y=t+t^(-1), u=(y+2)/24=(1+t)^2/(24t), D=t^(-n)C, a_p=u^r D.

Then y^2-140y+292=0, y^p=140-y, K=F_p[y]=F_{p^2} is the inversion-fixed subfield of A, D lies in K, and
    D^p = u^(2r) D,      u^(p+1)=1.
Consequently **a_p belongs to F_p** and reconstructs the entire quartic first-jet:
    C = a_p t^n u^(-r) in A.
This is ONE ground-field scalar for the full inversion-covariant four-coordinate Hasse jet, rather than a separate scalar in each of two quadratic factors.

If D=d0+d1*y, then
    d0^2+140*d0*d1+292*d1^2 = a_p^2 (mod p).
Thus the previously defined two-coordinate norm is always a square or zero. Vanishing of Q|C is equivalent to a_p=0. Earlier author-side inert-class theorem gives a_p != 0 for p=13 mod 24. The split-class statement a_p=0 for all p=5 mod 24 remains the exact open claim.

## Proof
Q is reciprocal and has constant term 1, so t is a unit and y=t+t^(-1) satisfies y^2-140y+292=0. This quadratic has discriminant 18432=2^11*3^2; (2/p)=-1 for p=5 mod8, hence its two roots are Frobenius-conjugate: y^p=140-y. The fixed subalgebra under t -> t^(-1) is exactly K=F_p[y] (basis 1,y).

The Hasse polynomial is reciprocal: H(t^(-1))=t^(-m)H(t). Differentiating and using 16m=-8 mod p yields C(t^(-1))=t^(-m-2)C(t)=t^(-2n)C(t). Thus D=t^(-n)C is inversion-fixed, D in K.

Consume the preceding exact CM first-jet equation C^p=Gamma*C, Gamma=-4s^(m+2), with f=t^p and s=-(1+f)/(2(1+t)), s^2(1-t)^2=f. As m+2=2n:
    D^p=t^(-n(p-1))*Gamma*D
       =-4*(s^2*t/f)^n*D
       =-4*(t/(1-t)^2)^n*D
       =-4*(y-2)^(-n)*D.
In K, (y-2)=4u^2. Euler's criterion gives 4^n=-4, so D^p=u^(-2n)D. Also (y+2)(142-y)=24^2, hence u^p=u^(-1), u^(p+1)=1. As -2n is congruent to 2r modulo p+1, D^p=u^(2r)D. Therefore (u^r D)^p=u^(-r)u^(2r)D=u^rD, proving a_p in F_p. Conversely every a in F_p gives the first-jet eigenline D=a u^(-r), C=a t^n u^(-r); no exceptional normalization case occurs. The quadratic norm is D*D^p=a_p^2. Conjugating y->140-y gives the displayed quadratic form. QED.

## Finite exact verification and BRC observer
Attached stdlib Python checker computes all 168 primes 5<=p<=5000 with p=5 mod8 (85 split, 83 inert). It checks t inverse, K polynomial/Frobenius, norm(u), earlier C^p=Gamma*C, new D^p=u^(2r)D, D=d0+d1*y, a_p in F_p, reconstruction, square norm. ALL 168 PASS.
p=13: a=8, (d0,d1)=(1,10), norm=12;
p=29: a=0, (d0,d1)=(0,0), norm=0;
p=37: a=20, (d0,d1)=(19,21), norm=30;
p=53: a=0, (d0,d1)=(0,0), norm=0;
p=373: a=125, (d0,d1)=(239,40), norm=332.

For p=373, both 125 and -125=248 square to 332 mod373: the norm-only observer preserves zero detection but loses the sign. The a_p scalar preserves this distinction and reconstructs the full constrained jet. BRC resolution: COMPOSE_APPLIED to previous first-jet Frobenius, reciprocal branch provenance and norm observer; the signed finite-field scalar is not positive-weight branch mass. This is a classical auxiliary representation; no native P000 six-axis transfer is asserted.

## Continuation
Do not reprove the prior two-isogeny, Hasse scaling, or Frobenius first-jet. Seek an independent finite CM / 3-isogeny / character sum formula for the single a_p and prove a_p=0 for all p=5 mod24, then connect to the Jacobi-Green-Wronskian p^2 correction. The frozen D24 second-digit Delta_p-R_p mod p and native original-class p373 divided-power, eta, kappa, Frobenius orientation remain separate. Native Source durable checkpoint is unchanged; this report is author-side portable evidence only. Dependency: research_notes/portable_direct/20261105_hourly20_d25_cm24_hasse_firstjet_eigenline.md.
