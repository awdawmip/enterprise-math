# D25/LIFT — exact symmetric-half-rank Hesse Green descent, observer-faithful reduction, and p373 next digit

2026-10-25. TASK_RESEARCH, author algebraic proof + exact integer check, UNREVIEWED / NOT_ADMITTED. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Distinct from Source-native CM/divided-power experiments, original LIFT observer, independent review, and Result acceptance.

## Inherited, not recredited
For every prime p=6m+1 >=13, n=2m=(p-1)/3, define in Z_(p):
c_k=(3k)!/[27^k(k!)^3], A(X)=sum_(k=0)^n c_k X^k, B(X)=A(1-X), Y=X(1-X), t=1-2X, C=(p+1)c_n/9.
Prior coefficientwise reflection proved D=(A-B)/p=t Phi_p(Y) with deg Phi<=m-1. Previous ordered Green pairing W=Y(AB'-A'B) satisfies
d_X(W/p)=C[X^n B-(1-X)^n A].
Earlier source equations LA=-pCX^n and LB=-pC(1-X)^n, L=d_X(Yd_X)-2/9, are used as exact input.

## NEW theorem (exact in Q[Y], p-integral)
There is unique G_p in Z_(p)[Y] of degree <=m such that (A+B)/2=G_p(Y). Labeled reconstruction is
 A=G_p(Y)+(p/2)t Phi_p(Y), B=G_p(Y)-(p/2)t Phi_p(Y).   (1)
Define F_0=F_1=1, F_r=F_(r-1)-YF_(r-2); S_0=2, S_1=1, S_r=S_(r-1)-YS_(r-2).
Then (1-X)^n-X^n=tF_(n-1)(Y), (1-X)^n+X^n=S_n(Y).
For N=Y(1-4Y)d_Y^2+(1-6Y)d_Y-2/9,
 N G_p=-(pC/2)S_n(Y).                                        (2)
The exact ordered normalized pairing K_p(Y)=W(X)/p has two identical expressions:
 K_p=Y[2G_p Phi_p+(1-4Y)(G_p'Phi_p-G_p Phi_p')],             (3)
 K_p=-C Integral_0^Y [F_(n-1)(s)G_p(s)+(p/2)S_n(s)Phi_p(s)] ds. (4)
The finite polynomial integral has zero constant and denominators j+1<=2m<p, hence is p-integral. Mod p this yields
 K_p(Y)=-C sum_(j=0)^(2m-1) ([s^j](F_(n-1)(s)G_p(s))/(j+1)) Y^(j+1) mod p.  (5)
Since A=B mod p, G_p mod p is already determined by ordinary A mod p. Thus the first digit of this PARTICULAR normalized W-pairing does not require the p-level reflection defect Phi, despite W/p's original definition. The next digit does require Phi and higher G. Evaluation at T^2=2, u=(2-T)/4, Y(u)=1/8 gives extension-free scalar via Y=1/8 in (5); no CM kappa identification.

Proof: reflection X->1-X fixes Y and changes sign of t; invariant polynomial ring (2 invertible) gives G and inherited odd D=tPhi gives (1). Compute d_XY=t, d_X^2G=-2G'_Y+t^2G''_Y; consequently L G=NG. Average LA,LB to prove (2). Direct substitution A=G+(p/2)D and B=G-(p/2)D into W/p cancels quadratic terms, leaving Y(G'_X D-GD'_X). Since G'_X=tG'_Y and D'_X=-2Phi+t^2Phi', obtain (3). Independently X^n B-(1-X)^n A=-t[F_(n-1)G+(p/2)S_nPhi]. The inherited d_X(W/p) identity yields tK'_Y=-Ct[...]. Cancel nonzero POLYNOMIAL t over Q[X], not evaluation at any point. W(0)=0 fixes the integration constant and gives (4). Degree of the integrand <=2m-1 and 2m<p ensure all denominators invertible modulo p. Reduction yields (5), proving theorem for all stated primes, not by finite extrapolation.

## Independent source-arithmetic author certificate, fixed scope
Original factorial c_k reconstructed mod p^3; expand A((1-t)/2) into even/odd coefficients to independently recover G and Phi; evaluate (4) mod p^2. Independently evaluate original A(u),A'(u) in (Z/p^3Z)[T]/(T^2-2), and W/p directly, and also independently compute (5) mod p.
All three routes passed:
p | W(u)/p mod p | W(u)/p mod p^2
13 | 6 | 6
19 | 3 | 98
37 | 26 | 655
43 | 6 | 1210
61 | 21 | 753
67 | 63 | 666
211 | 43 | 26418
373 | 286 | 99504

NEW p=373 next-digit result: W(u)/373 = 99504 = 286+373*266 mod 373^2, so W(u)=37114992 mod 373^3. The prior source note had only W(u)/373=286 mod 373. The integer regression is author-run, not peer review, proof-kernel certification, or native CM experiment.

BRC COMPOSE_APPLIED: typed carrier (p,X,Y,t,sigma;A,B;G,Phi;F,S;W/p). (1) retains exact provenance and branch; (5) is observer-faithful only for the first digit of the signed W-pairing. No quotient to native divided-power H0/B0 or original LIFT is established; P000 remains fixed. Task parent remains OPEN: obtain the actual same-prime same-original-class H0/B0 DP representative, semilinear Frobenius direction, normalized [X]U mod p^2 and source-based kappa bridge to Delta_p-R_p. Do not repeat prior Hesse reflection, Green inverse, WZ/Cauchy scans, 19 native completed units. Status remains UNREVIEWED / NOT_ADMITTED until genuine Source checkpoint/readback and independent review.