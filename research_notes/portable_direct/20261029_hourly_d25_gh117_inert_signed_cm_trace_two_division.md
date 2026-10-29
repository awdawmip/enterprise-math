# D25/LIFT portable GH-117 — inert CM Frobenius sign via rational 2-torsion and a halving obstruction

Date: 2026-10-29 Asia/Hong_Kong. AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. The scientific frozen Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Research logical lane chatgpt-research-hourly-enterprise-math-20260923 only; no native CLAIM/OPEN/checkpoint.

## Theorem (complements GH-116)

For every prime p >= 19 with p == 19 (mod 24), let q=p^2, choose r in F_q with r^2=2, set T=2r/3, B=(1+T)/8, and consider the GH-100 actual reflected-Hasse CM curve

    C_T: v^2=u^3+u^2+B*u = u*(u-rho_plus)*(u-rho_minus).

Then its signed Frobenius trace and exact finite-field point count satisfy

    a_q(C_T)=+2p,
    #C_T(F_q)=(p-1)^2.

The result is valid for the **entire inert p==19 mod24 branch**, not merely for tested primes. Together with GH-116 (p==11 mod24), it supplies the full p==3 mod8 signed trace classification, but it does not evaluate the separate reflected tail R_p(9).

## Proof with explicit algebraic 2-division obstruction

1. Since p==19 mod24, (2/p)=(3/p)=-1 and (6/p)=+1. Thus r^p=-r and we may choose eta in F_p with eta^2=6. The curve is nonsingular because T^2=8/9 !=1. GH-113's imported classical CM/Deuring classification gives Hasse coefficient E_p(8/9)=0 (the prime is inert in Q(sqrt(-6))). The standard Hasse/Frobenius congruence then gives p | a_q, while the Hasse bound gives |a_q|<=2p.

2. The quadratic factor x^2+x+B has discriminant

    delta=1-4B=(1-T)/2=((r-1)/eta)^2.

   Thus both rho_plus=(-1+(r-1)/eta)/2 and rho_minus=(-1-(r-1)/eta)/2 lie in F_q. Hence all four 2-torsion points are rational and 4 divides #C_T(F_q)=p^2+1-a_q. Because p==3 mod4, reduction modulo 4 gives a_q==2 (mod4). Combined with p|a_q and |a_q|<=2p, the only two possible values are

    a_q=+2p  OR  a_q=-2p.

3. Show that P=(0,0) is **not** twice an F_q-point. For s=(r-1)/eta, s^p=(-r-1)/eta and s*s^p=-1/6, s+s^p=-2/eta. A direct norm computation yields

    N_(q/p)(rho_plus)=(5+2*eta)/24,
    N_(q/p)(rho_minus)=(5-2*eta)/24.

   Let w_plus=r+eta/r and w_minus=r-eta/r. They satisfy w_plus^p=-w_plus and w_minus^p=-w_minus and

    w_plus^2=5+2*eta,  w_minus^2=5-2*eta.

   Therefore chi_p(5±2eta)=w_±^(p-1)=-1. Since chi_p(24)=chi_p(6)=+1, we obtain

    chi_q(rho_plus)=chi_p(N(rho_plus))=-1,
    chi_q(rho_minus)=chi_p(N(rho_minus))=-1.

   As -1 is a square in F_q, neither -rho_plus nor -rho_minus is a square. The standard 2-descent halving criterion for y^2=(x-e1)(x-e2)(x-e3) says (e1,0) is twice a rational point only if e1-e2 and e1-e3 are rational squares. Taking e1=0 proves P is not divisible by 2 in C_T(F_q).

4. If the remaining possibility a_q=-2p held, the Frobenius polynomial would be (X+p)^2. The endomorphism algebra of an elliptic curve over a finite field has no nonzero nilpotents, so q-Frobenius would equal multiplication by -p. Since p==3 mod4, -p==1 mod4, every geometric 4-torsion point would then be fixed by Frobenius and rational over F_q. In particular the nonzero 2-torsion P would have a rational half, contradicting step 3. Hence a_q=+2p and the point-count formula follows. QED.

## Exact executable checks

The independent companion C++17 program enumerates all p<800 with p==19 mod24 (19 primes). For each it constructs eta, the actual F_(p^2) roots rho±, verifies the discriminant and both non-square norm characters, then exhaustively evaluates the q-element quadratic-character sum of the original cubic. All 19 return a_q=2p. Examples: p=19 -> a_q=38, #=324; p=43 -> 86, #=1764; p=67 -> 134, #=4356; p=787 -> 1574, #=617796. This is an exact finite check of the proof and its implementation, not the basis for the infinite-prime theorem.

## Cross-branch result, BRC and next obligation

GH-116 split branch: if p==11 mod24 and p=2x²+3y², then a_(p²)=6y²-4x². GH-117 inert branch: if p==19 mod24, then a_(p²)=2p. These are two distinct arithmetic carriers and source branches even though both use the same reflected elliptic curve C_T. BRC resolution COMPOSE_APPLIED: preserve p class, field extension, actual 2-torsion roots, norm characters, rational-halving obstruction, exact signed trace and the point-count readout; do not collapse supersingularity to the bare observation a_q==0 (mod p), which loses the sign and rational torsion.

The derivation imports GH-113's unreviewed author-side CM/Hasse-source bridge and standard elliptic-curve theorems (Hasse bound, 2-descent and Frobenius endomorphism). It is not a proof of GH-83 stationarity, of R_3347(9)=0, nor of GH-3 T_(p,9)=0 mod p. The next distinct scientific task remains a genuinely independent CM/Jacobi/WZ evaluation that predicts the reflected-tail special value from more than the already classified signed elliptic trace; trace-only classification does not supply the missing additive period.
